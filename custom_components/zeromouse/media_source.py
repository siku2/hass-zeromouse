import dataclasses
from typing import Literal, NewType, Self

from homeassistant.components.media_source import (
    BrowseMediaSource,
    MediaSource,
    MediaSourceItem,
    PlayMedia,
)


class ZeroMouseMediaSource(MediaSource):
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia:
        raise NotImplementedError

    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource:
        """

        - Top level ZeroMouse entry.
            - All devices
                - All Events
        """
        if not item.identifier:
            pass
        raise NotImplementedError
