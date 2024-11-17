import logging
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.helpers import httpx_client
from .api import Api
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ZeroMouseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            username = user_input[CONF_USERNAME]
            await self.async_set_unique_id(username)
            try:
                api = await Api.login(
                    username,
                    user_input[CONF_PASSWORD],
                    httpx_client=httpx_client.get_async_client(self.hass),
                )
                data = api.store_credentials()
            except Exception:
                _LOGGER.warning("failed to log in", exc_info=True)
                errors["base"] = "invalid_credentials"
            else:
                self._abort_if_unique_id_configured(data)
                return self.async_create_entry(
                    title=username,
                    data=data,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_USERNAME,
                        default=user_input.get(CONF_USERNAME) if user_input else None,
                    ): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )
