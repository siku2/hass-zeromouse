# Websocket

## Request

```http
GET /graphql?header={jwt}&payload={something} HTTP/1.1
origin: https://f36gc6o7jnewxe37dhn3fochza.appsync-realtime-api.eu-central-1.amazonaws.com
Sec-WebSocket-Protocol: graphql-ws
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: {key}
Sec-WebSocket-Version: 13
Sec-WebSocket-Extensions: permessage-deflate
Host: {hexid}.appsync-realtime-api.eu-central-1.amazonaws.com
Accept-Encoding: gzip
User-Agent: okhttp/4.9.2
content-length: 0
```

## Response

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: {key}
Sec-WebSocket-Protocol: graphql-ws
content-length: 0
```

`[OUTGOING] {"type":"connection_init"}`

`[INCOMING] {"type":"connection_ack","payload":{"connectionTimeoutMs":300000}}`

`[INCOMING] {"type":"ka"}`

`[OUTGOING]`

```json
{
    "id": "{uuid}",
    "payload": {
        "data": "{\"query\":\"subscription OnCreateMbrPtfEventData($filter: ModelSubscriptionMbrPtfEventDataFilterInput) {\\n  onCreateMbrPtfEventData(filter: $filter) {\\n    eventID\\n    eventTime\\n    type\\n    Images {\\n      nextToken\\n      __typename\\n    }\\n    deviceID\\n    classification_byNet\\n    ownerID\\n    sensor_ref_brightness\\n    sensor_ref_exposureCtrl\\n    sensor_ref_gainCtrl\\n    pir_time_to_time0\\n    air {\\n      time\\n      value\\n      __typename\\n    }\\n    isSeen\\n    isFlagged\\n    isHidden\\n    isDeleted\\n    createdAt\\n    updatedAt\\n    __typename\\n  }\\n}\\n\",\"variables\":{}}",
        "extensions": {
            "authorization": {
                "host": "{hex id}.appsync-api.eu-central-1.amazonaws.com",
                "x-amz-date": "{rfc3339}",
                "x-api-key": "{key}",
                "x-amz-user-agent": "aws-amplify/5.2.5 react-native"
            }
        }
    },
    "type": "start"
}
```

`[INCOMING] {"id":"{uuid}","type":"start_ack"}`

`[INCOMING] {"type":"ka"}`

`[INCOMING] {"type":"ka"}`

`[INCOMING] {"type":"ka"}`
