import dataclasses
from typing import Any, Literal, Self


@dataclasses.dataclass(frozen=True)
class Image:
    id: str
    file_path: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id=data["id"],
            file_path=data["filePath"],
        )


@dataclasses.dataclass(frozen=True)
class MbrPtfEvent:
    event_id: str
    event_time: int
    type: Literal["CAT_ENTERED", "CAT_ENTRY_DENIED"]
    device_id: str
    owner_id: str
    is_seen: bool | None
    is_flagged: bool | None
    is_hidden: int | None
    classification_by_net: Literal["clean", "prey"]
    created_at: str
    updated_at: str
    images: list[Image]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            event_id=data["eventID"],
            event_time=data["eventTime"],
            type=data["type"],
            device_id=data["deviceID"],
            owner_id=data["ownerID"],
            is_seen=data["isSeen"],
            is_flagged=data["isFlagged"],
            is_hidden=data["isHidden"],
            classification_by_net=data["classification_byNet"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            images=[Image.from_dict(image) for image in data["Images"]["items"]],
        )


_LIST_MBR_PTF_EVENT_DATA_WITH_IMAGES = """
query listMbrPtfEventDataWithImages($ownerID: String!, $sortDirection: ModelSortDirection, $filter: ModelMbrPtfEventDataFilterInput, $limit: Int, $nextToken: String) {
  listEventByOwner(
    ownerID: $ownerID
    sortDirection: $sortDirection
    filter: $filter
    limit: $limit
    nextToken: $nextToken
  ) {
    items {
      eventID
      eventTime
      type
      deviceID
      ownerID
      isSeen
      isFlagged
      isHidden
      classification_byNet
      createdAt
      updatedAt
      Images {
        items {
          id
          filePath
        }
      }
    }
    nextToken
  }
}
"""


def list_mbr_ptf_event_data_with_images(
    *,
    limit: int,
    next_token: str | None,
    owner_id: str,
    sort_direction: Literal["DESC"],
    show_deleted: bool = False,
    show_hidden: bool = False,
) -> dict[str, Any]:
    return {
        "query": _LIST_MBR_PTF_EVENT_DATA_WITH_IMAGES,
        "variables": {
            "limit": limit,
            "nextToken": next_token,
            "ownerID": owner_id,
            "sortDirection": sort_direction,
            "filter": {
                "isDeleted": {"eq": int(show_deleted)},
                "isHidden": {"eq": int(show_hidden)},
            },
        },
    }
