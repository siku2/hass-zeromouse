import asyncio
import base64
import json
import logging
import uuid
from types import TracebackType
from typing import Any, Self

import websockets.asyncio.client as ws_client
import websockets.exceptions
from websockets.typing import Subprotocol

from ._consts import APPSYNC_API_KEY, APPSYNC_HOST, APPSYNC_REALTIME_HOST

_LOGGER = logging.getLogger(__name__)


class Subscription:
    """Subscriptions don't do anything yet."""

    def __init__(self) -> None:
        url = _build_appsync_realtime_url(
            APPSYNC_REALTIME_HOST,
            {
                "host": APPSYNC_HOST,
                "x-api-key": APPSYNC_API_KEY,
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
                    "authorization": {
                        "host": APPSYNC_HOST,
                        "x-api-key": APPSYNC_API_KEY,
                    }
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
