# CreateFcmToken

## Request

```http
POST https://f36gc6o7jnewxe37dhn3fochza.appsync-api.eu-central-1.amazonaws.com/graphql HTTP/2.0
accept: application/json, text/plain, */*
user-agent: aws-amplify/5.2.5 react-native
authorization: {jwt}
x-amz-user-agent: aws-amplify/5.2.5 react-native
content-type: application/json; charset=UTF-8
content-length: 3333
accept-encoding: gzip
```

```json
{
    "query": "mutation CreateFcmToken($input: CreateFcmTokenInput!, $condition: ModelFcmTokenConditionInput) {\n  createFcmToken(input: $input, condition: $condition) {\n    id\n    owner\n    token\n    createdAt\n    updatedAt\n    __typename\n  }\n}\n",
    "variables": {
        "input": {
            "token": "{token}",
            "owner": "{uuid}"
        }
    }
}
```

## Response

```http
HTTP/2.0 200 
content-type: application/json;charset=UTF-8
content-length: 3333
date: {date header}
x-amzn-appsync-tokensconsumed: 1
x-amzn-requestid: {uuid}
x-cache: Miss from cloudfront
via: 1.1 {hex id}.cloudfront.net (CloudFront)
x-amz-cf-pop: ...
x-amz-cf-id: ...
```

```json
{
    "data": {
        "createFcmToken": {
            "id": "{uuid}",
            "owner": "{uuid}",
            "token": "{token}",
            "createdAt": "2024-10-26T19:32:54.624Z",
            "updatedAt": "2024-10-26T19:32:54.624Z",
            "__typename": "FcmToken"
        }
    }
}
```
