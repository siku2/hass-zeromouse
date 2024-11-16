import base64
import dataclasses
import json
import logging
import uuid
from types import TracebackType
from typing import Any, Self

import websockets.asyncio.client as ws_client
import websockets.exceptions
from pycognito import Cognito, UserObj
from websockets.typing import Subprotocol

_LOGGER = logging.getLogger(__name__)

_APPSYNC_HOST = "f36gc6o7jnewxe37dhn3fochza.appsync-api.eu-central-1.amazonaws.com"
_GRAPHQL_BASE_URL = f"https://{_APPSYNC_HOST}/graphql"
_APPSYNC_REALTIME_HOST = _APPSYNC_HOST.replace("appsync-api", "appsync-realtime-api")

_USER_POOL_ID = "eu-central-1_LS6CKN0t1"
_CLIENT_ID = "7pdec0rbivg5hg8u3pke4veg0f"
_API_KEY = "da2-r5hq3osgpbdmtd6nx67tvlyxum"

_USER_ATTR_CAT_ENTERED = "custom:ntf_CAT_ENTERED"
_USER_ATTR_CAT_ENTRY_DENIED = "custom:ntf_CAT_ENTRY_DENIED"


@dataclasses.dataclass(kw_only=True, frozen=True)
class NotificationSettings:
    cat_entered: bool
    cat_entry_denied: bool

    @classmethod
    def from_user_obj(cls, user: UserObj) -> Self:
        return cls(
            cat_entered=getattr(user, _USER_ATTR_CAT_ENTERED) == "1",
            cat_entry_denied=getattr(user, _USER_ATTR_CAT_ENTRY_DENIED) == "1",
        )


class _Api:
    def __init__(self, cognito: Cognito) -> None:
        self._loop = asyncio.get_event_loop()
        self._cognito = cognito

    @classmethod
    async def login(cls, username: str, password: str) -> Self:
        loop = asyncio.get_event_loop()
        cognito = Cognito(
            _USER_POOL_ID,
            _CLIENT_ID,
            username=username,
        )
        await loop.run_in_executor(
            None,
            cognito.authenticate,  # type: ignore
            password,
        )
        return cls(cognito)

    def store_credentials(self) -> dict[str, str]:
        assert isinstance(self._cognito.id_token, str)  # type: ignore
        assert isinstance(self._cognito.refresh_token, str)  # type: ignore
        assert isinstance(self._cognito.access_token, str)  # type: ignore
        return {
            "id_token": self._cognito.id_token,
            "refresh_token": self._cognito.refresh_token,
            "access_token": self._cognito.access_token,
        }

    @classmethod
    async def from_stored_credentials(cls, credentials: dict[str, str]) -> Self:
        cognito = Cognito(
            _USER_POOL_ID,
            _CLIENT_ID,
            **credentials,
        )
        this = cls(cognito)
        await this._update_access_token()
        return this

    async def _update_access_token(self) -> None:
        await self._loop.run_in_executor(None, self._cognito.check_token)

    async def _get_user(self) -> UserObj:
        await self._update_access_token()
        return await self._loop.run_in_executor(
            None,
            self._cognito.get_user,  # type: ignore
        )

    async def get_notification_settings(self) -> NotificationSettings:
        user = await self._get_user()
        return NotificationSettings.from_user_obj(user)


class _Subscription:
    """Subscriptions don't do anything yet."""

    def __init__(self) -> None:
        url = _build_appsync_realtime_url(
            _APPSYNC_REALTIME_HOST,
            {
                "host": _APPSYNC_HOST,
                "x-api-key": _API_KEY,
            },
            {},
        )
        self._connect = ws_client.connect(url, subprotocols=[Subprotocol("graphql-ws")])
        self._reconnect = True
        self._ws: ws_client.ClientConnection | None = None
        self._task: asyncio.Task[None] | None = None
        self._timeout_interval_ms: int | None = None

    async def __aenter__(self) -> Self:
        assert self._task is None
        self._reconnect = True
        self._task = asyncio.create_task(self.__run())
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        self._reconnect = False
        if ws := self._ws:
            await ws.close()
        if task := self._task:
            self._task = None
            await task

    async def _send(self, type: str, **kwargs: Any) -> None:
        assert self._ws is not None
        await self._ws.send(json.dumps({**kwargs, "type": type}))

    async def _send_start_subscription(self, id: uuid.UUID, query: str) -> None:
        await self._send(
            "start",
            id=str(id),
            payload={
                "data": query,
                "extensions": {
                    "authorization": {"host": _APPSYNC_HOST, "x-api-key": _API_KEY}
                },
            },
        )

    async def _on_connection_ack(self) -> None:
        await self._send_start_subscription(
            uuid.uuid4(),
            '{"query":"subscription OnCreateMbrPtfEventData($filter: ModelSubscriptionMbrPtfEventDataFilterInput) {\\n  onCreateMbrPtfEventData(filter: $filter) {\\n    eventID\\n    eventTime\\n    type\\n    Images {\\n      nextToken\\n      __typename\\n    }\\n    deviceID\\n    classification_byNet\\n    ownerID\\n    sensor_ref_brightness\\n    sensor_ref_exposureCtrl\\n    sensor_ref_gainCtrl\\n    pir_time_to_time0\\n    air {\\n      time\\n      value\\n      __typename\\n    }\\n    isSeen\\n    isFlagged\\n    isHidden\\n    isDeleted\\n    createdAt\\n    updatedAt\\n    __typename\\n  }\\n}\\n","variables":{}}',
        )

    async def _on_data(self, data: Any) -> None:
        pass

    async def __run_reader(self, ws: ws_client.ClientConnection) -> None:
        self._timeout_interval_ms = None
        await self._send("connection_init")
        async for msg in ws:
            obj = json.loads(msg)
            ty = obj["type"]
            _LOGGER.debug("new message from appsync: %s", obj)
            match ty:
                case "ka":
                    # TODO: reset keepalive timer
                    pass
                case "connection_ack":
                    self._timeout_interval_ms = obj["payload"]["connectionTimeoutMs"]
                    await self._on_connection_ack()
                case "data":
                    await self._on_data(obj["payload"]["data"])
                case "error":
                    _LOGGER.error("error from appsync: %s", obj.get("payload"))
                case _:
                    _LOGGER.warning(
                        "received unknown message type from appsync: %s", obj
                    )

    async def __run(self) -> None:
        _LOGGER.debug("starting subscription worker")
        async for ws in self._connect:
            self._ws = ws
            try:
                await self.__run_reader(ws)
            except websockets.exceptions.ConnectionClosed:
                pass
            finally:
                self._ws = None
            if not self._reconnect:
                break
        _LOGGER.debug("stopping subscription worker")


def _build_appsync_realtime_url(
    host: str, header: dict[str, Any], payload: dict[str, Any]
) -> str:
    def _encode(obj: dict[str, Any]) -> str:
        return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode()

    return f"wss://{host}/graphql?header={_encode(header)}&payload={_encode(payload)}"


