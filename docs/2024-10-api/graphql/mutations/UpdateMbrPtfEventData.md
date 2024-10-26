# UpdateMbrPtfEventData

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
    "query": "mutation UpdateMbrPtfEventData($input: UpdateMbrPtfEventDataInput!, $condition: ModelMbrPtfEventDataConditionInput) {\n  updateMbrPtfEventData(input: $input, condition: $condition) {\n    eventID\n    eventTime\n    type\n    Images {\n      nextToken\n      __typename\n    }\n    deviceID\n    classification_byNet\n    ownerID\n    sensor_ref_brightness\n    sensor_ref_exposureCtrl\n    sensor_ref_gainCtrl\n    pir_time_to_time0\n    air {\n      time\n      value\n      __typename\n    }\n    isSeen\n    isFlagged\n    isHidden\n    isDeleted\n    createdAt\n    updatedAt\n    __typename\n  }\n}\n",
    "variables": {
        "input": {
            "deviceID": "{device id}",
            "eventID": "{event uuid}",
            "isDeleted": 1
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
x-amzn-appsync-tokensconsumed: 1
vary: accept-encoding
x-cache: Miss from cloudfront
via: 1.1 {hex id}.cloudfront.net (CloudFront)
x-amz-cf-pop: {short id}
x-amz-cf-id: {id}
content-length: 3333
```

```json
{
    "data": {
        "updateMbrPtfEventData": {
            "eventID": "{event uuid}",
            "eventTime": 1729974000,
            "type": "CAT_ENTERED",
            "Images": {
                "nextToken": null,
                "__typename": "ModelMbrPtfImageDataConnection"
            },
            "deviceID": "{device id}",
            "classification_byNet": "clean",
            "ownerID": "{uuid}",
            "sensor_ref_brightness": -2,
            "sensor_ref_exposureCtrl": 0,
            "sensor_ref_gainCtrl": 0,
            "pir_time_to_time0": -2344,
            "air": [
                {
                    "time": -500,
                    "value": 500,
                    "__typename": "AIRMeasurement"
                },
                {
                    "time": 300,
                    "value": 1770,
                    "__typename": "AIRMeasurement"
                }
            ],
            "isSeen": null,
            "isFlagged": null,
            "isHidden": 0,
            "isDeleted": 1,
            "createdAt": "{rfc3339}",
            "updatedAt": "{rfc3339}",
            "__typename": "MbrPtfEventData"
        }
    }
}
```
