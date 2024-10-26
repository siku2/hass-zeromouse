# ListMbrPtfFlapData

## Request

```http
POST https://f36gc6o7jnewxe37dhn3fochza.appsync-api.eu-central-1.amazonaws.com/graphql HTTP/2.0
accept: application/json, text/plain, */*
user-agent: aws-amplify/5.2.5 react-native
authorization: ...
x-amz-user-agent: aws-amplify/5.2.5 react-native
content-type: application/json; charset=UTF-8
content-length: 3333
accept-encoding: gzip
```

```json
{
    "query": "query ListMbrPtfFlapData($deviceID: ID, $filter: ModelMbrPtfFlapDataFilterInput, $limit: Int, $nextToken: String, $sortDirection: ModelSortDirection) {\n  listMbrPtfFlapData(\n    deviceID: $deviceID\n    filter: $filter\n    limit: $limit\n    nextToken: $nextToken\n    sortDirection: $sortDirection\n  ) {\n    items {\n      deviceID\n      name\n      model\n      networkName\n      ownerID\n      verHardware\n      verMajor\n      verMinor\n      verRevision\n      bootCount\n      eventCount\n      createdAt\n      updatedAt\n      __typename\n    }\n    nextToken\n    __typename\n  }\n}\n",
    "variables": {
        "limit": 1000,
        "nextToken": null
    }
}
```

## Response

```http
HTTP/2.0 200 
content-type: application/json;charset=UTF-8
date: {date header}
x-amzn-requestid: {uuid}
x-amzn-appsync-tokensconsumed: 1
vary: accept-encoding
x-cache: Miss from cloudfront
via: 1.1 {hex id}.cloudfront.net (CloudFront)
x-amz-cf-pop: ...
x-amz-cf-id: ...
content-length: 3333
```

```json
{
    "data": {
        "listMbrPtfFlapData": {
            "items": [
                {
                    "deviceID": "{weird id}",
                    "name": "{human name}",
                    "model": "{weird id}",
                    "networkName": "{ssid}",
                    "ownerID": "{uuid}",
                    "verHardware": null,
                    "verMajor": "0",
                    "verMinor": "14",
                    "verRevision": "2",
                    "bootCount": 185,
                    "eventCount": 322,
                    "createdAt": "{rfc3339}",
                    "updatedAt": "{rfc3339}",
                    "__typename": "MbrPtfFlapData"
                }
            ],
            "nextToken": "{jwt}",
            "__typename": "ModelMbrPtfFlapDataConnection"
        }
    }
}
```
