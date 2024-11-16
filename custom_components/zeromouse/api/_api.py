import asyncio
import dataclasses
import logging
from typing import Self

from pycognito import Cognito, UserObj

from ._consts import (
    CLIENT_ID,
    USER_ATTR_CAT_ENTERED,
    USER_ATTR_CAT_ENTRY_DENIED,
    USER_POOL_ID,
)

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


class Api:
    def __init__(self, cognito: Cognito) -> None:
        self._loop = asyncio.get_event_loop()
        self._cognito = cognito

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
