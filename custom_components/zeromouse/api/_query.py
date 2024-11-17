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
    sort_direction: Literal["ASC", "DESC"],
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


@dataclasses.dataclass(frozen=True)
class MbrPtfFlap:
    device_id: str
    name: str
    model: str
    network_name: str
    owner_id: str
    ver_hardware: str | None
    ver_major: str
    ver_minor: str
    ver_revision: str
    boot_count: int
    event_count: int
    created_at: str
    updated_at: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            device_id=data["deviceID"],
            name=data["name"],
            model=data["model"],
            network_name=data["networkName"],
            owner_id=data["ownerID"],
            ver_hardware=data.get("verHardware"),
            ver_major=data["verMajor"],
            ver_minor=data["verMinor"],
            ver_revision=data["verRevision"],
            boot_count=data["bootCount"],
            event_count=data["eventCount"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
        )


_LIST_MBR_PTF_FLAP_DATA = """
query ListMbrPtfFlapData($deviceID: ID, $filter: ModelMbrPtfFlapDataFilterInput, $limit: Int, $nextToken: String, $sortDirection: ModelSortDirection) {
  listMbrPtfFlapData(
    deviceID: $deviceID
    filter: $filter
    limit: $limit
    nextToken: $nextToken
    sortDirection: $sortDirection
  ) {
    items {
      deviceID
      name
      model
      networkName
      ownerID
      verHardware
      verMajor
      verMinor
      verRevision
      bootCount
      eventCount
      createdAt
      updatedAt
    }
    nextToken
  }
}
"""


def list_mbr_ptf_flap_data(
    *,
    device_id: str | None,
    limit: int,
    next_token: str | None,
    sort_direction: Literal["ASC", "DESC"],
) -> dict[str, Any]:
    return {
        "query": _LIST_MBR_PTF_FLAP_DATA,
        "variables": {
            "deviceID": device_id,
            "limit": limit,
            "nextToken": next_token,
            "sortDirection": sort_direction,
        },
    }
