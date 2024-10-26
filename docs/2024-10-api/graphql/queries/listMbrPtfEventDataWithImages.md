# listMbrPtfEventDataWithImages

## Request

```http
POST https://f36gc6o7jnewxe37dhn3fochza.appsync-api.eu-central-1.amazonaws.com/graphql HTTP/2.0
accept: application/json, text/plain, */*
user-agent: aws-amplify/5.2.5 react-native
authorization: {jwt}
x-amz-user-agent: aws-amplify/5.2.5 react-native
content-type: application/json; charset=UTF-8
content-length: 333
accept-encoding: gzip
```

```json
{
    "query": "query listMbrPtfEventDataWithImages($ownerID: String!, $sortDirection: ModelSortDirection, $filter: ModelMbrPtfEventDataFilterInput, $limit: Int, $nextToken: String) {\n  listEventByOwner(\n    ownerID: $ownerID\n    sortDirection: $sortDirection\n    filter: $filter\n    limit: $limit\n    nextToken: $nextToken\n  ) {\n    items {\n      eventID\n      eventTime\n      type\n      deviceID\n      ownerID\n      isSeen\n      isFlagged\n      isHidden\n      classification_byNet\n      createdAt\n      updatedAt\n      __typename\n      Images {\n        items {\n          id\n          filePath\n          deviceID\n        }\n      }\n    }\n    nextToken\n    __typename\n  }\n}\n",
    "variables": {
        "limit": 20,
        "nextToken": null,
        "ownerID": "{uuid}",
        "sortDirection": "DESC",
        "filter": {
            "isDeleted": {
                "eq": 0
            },
            "isHidden": {
                "eq": 0
            }
        }
    }
}
```

## Response

```http
HTTP/2.0 200 
content-type: application/json;charset=UTF-8
date: {date header}
x-amzn-requestid: {uuid}
x-amzn-appsync-tokensconsumed: 2
vary: accept-encoding
x-cache: Miss from cloudfront
via: 1.1 {hex id}.cloudfront.net (CloudFront)
x-amz-cf-pop: {short id}
x-amz-cf-id: {b64 id}
content-length: 3333
```

```json
{
    "data": {
        "listEventByOwner": {
            "items": [
                {
                    "eventID": "{event uuid}",
                    "eventTime": 1729973143,
                    "type": "CAT_ENTERED",
                    "deviceID": "{weird id}",
                    "ownerID": "{uuid}",
                    "isSeen": null,
                    "isFlagged": null,
                    "isHidden": 0,
                    "classification_byNet": "clean",
                    "createdAt": "{rfc3339}",
                    "updatedAt": "{rfc3339}",
                    "__typename": "MbrPtfEventData",
                    "Images": {
                        "items": [
                            {
                                "id": "{uuid}",
                                "filePath": "devices/{weird id}/events/{event uuid}/images/1.jpg",
                                "deviceID": "{weird id}"
                            },
                            {
                                "id": "{uuid}",
                                "filePath": "devices/{weird id}/events/{event uuid}/images/7.jpg",
                                "deviceID": "{weird id}"
                            }
                        ]
                    }
                },
                {
                    "eventID": "{event uuid}",
                    "eventTime": 1729973143,
                    "type": "ENTRY_DENIED",
                    "deviceID": "{weird id}",
                    "ownerID": "{uuid}",
                    "isSeen": null,
                    "isFlagged": null,
                    "isHidden": 0,
                    "classification_byNet": "prey",
                    "createdAt": "{rfc3339}",
                    "updatedAt": "{rfc3339}",
                    "__typename": "MbrPtfEventData",
                    "Images": {
                        "items": [
                            {
                                "id": "{uuid}",
                                "filePath": "devices/{weird id}/events/{event uuid}/images/0.jpg",
                                "deviceID": "{weird id}"
                            },
                            {
                                "id": "{uuid}",
                                "filePath": "devices/{weird id}/events/{event uuid}/images/7.jpg",
                                "deviceID": "{weird id}"
                            }
                        ]
                    }
                },
            ],
            "nextToken": "{jwt}",
            "__typename": "ModelMbrPtfEventDataConnection"
        }
    }
}
```
