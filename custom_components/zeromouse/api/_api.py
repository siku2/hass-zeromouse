import asyncio
import dataclasses
import logging
from typing import Any, Self

import httpx
from pycognito import Cognito, UserObj

from ._consts import (
    CLIENT_ID,
    GRAPHQL_BASE_URL,
    USER_ATTR_CAT_ENTERED,
    USER_ATTR_CAT_ENTRY_DENIED,
    USER_POOL_ID,
)
from ._query import MbrPtfEvent, list_mbr_ptf_event_data_with_images

_LOGGER = logging.getLogger(__name__)


@dataclasses.dataclass(kw_only=True, frozen=True)
class NotificationSettings:
    cat_entered: bool
    cat_entry_denied: bool

    @classmethod
    def from_user_obj(cls, user: UserObj) -> Self:
        return cls(
            cat_entered=getattr(user, USER_ATTR_CAT_ENTERED) == "1",
            cat_entry_denied=getattr(user, USER_ATTR_CAT_ENTRY_DENIED) == "1",
        )


class GraphqlRequestError(Exception): ...


class Api:
    def __init__(self, cognito: Cognito) -> None:
        self._loop = asyncio.get_event_loop()
        self._cognito = cognito
        self._client = httpx.AsyncClient()

    @classmethod
    async def login(cls, username: str, password: str) -> Self:
        loop = asyncio.get_event_loop()
        cognito = Cognito(
            USER_POOL_ID,
            CLIENT_ID,
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
            USER_POOL_ID,
            CLIENT_ID,
            **credentials,
        )
        this = cls(cognito)
        await this._update_access_token()
        return this

    async def _update_access_token(self) -> str:
        await self._loop.run_in_executor(None, self._cognito.check_token)
        return self._cognito.access_token  # type: ignore

    async def _get_user(self) -> UserObj:
        await self._update_access_token()
        return await self._loop.run_in_executor(
            None,
            self._cognito.get_user,  # type: ignore
        )

    async def get_user_id(self) -> str:
        user = await self._get_user()
        return user.sub  # type: ignore

    async def get_notification_settings(self) -> NotificationSettings:
        user = await self._get_user()
        return NotificationSettings.from_user_obj(user)

    async def _graphql_request(self, data: dict[str, Any]) -> Any:
        access_token = await self._update_access_token()
        resp = await self._client.post(
            GRAPHQL_BASE_URL,
            json=data,
            headers={"Authorization": access_token},
        )
        resp.raise_for_status()
        body = resp.json()
        if "errors" in body:
            raise GraphqlRequestError(body["errors"])
        return body["data"]

    async def list_mbr_ptf_events(self, owner_id: str) -> list[MbrPtfEvent]:
        query = list_mbr_ptf_event_data_with_images(
            limit=20,
            next_token=None,
            owner_id=owner_id,
            sort_direction="DESC",
        )
        data = await self._graphql_request(query)
        try:
            return [
                MbrPtfEvent.from_dict(item)
                for item in data["listEventByOwner"]["items"]
            ]
        except Exception:
            _LOGGER.error("failed to parse response: %s", data)
            raise
