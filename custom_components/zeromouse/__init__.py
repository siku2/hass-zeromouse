import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers import httpx_client

from .api import Api, AuthError

_LOGGER = logging.getLogger(__name__)

_PLATFORMS: list[Platform] = []


type ZeroMouseConfigEntry = ConfigEntry[Api]


async def async_setup_entry(hass: HomeAssistant, entry: ZeroMouseConfigEntry) -> bool:
    try:
        api = await Api.from_stored_credentials(
            entry.data,
            httpx_client=httpx_client.get_async_client(hass),
        )
    except AuthError as err:
        raise ConfigEntryAuthFailed(err) from err
    entry.runtime_data = api
    _LOGGER.debug("successfully logged in with stored credentials")
    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ZeroMouseConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
