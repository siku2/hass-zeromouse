# Patch device config

## Request

```http
PATCH https://kus3g3tct7.execute-api.eu-central-1.amazonaws.com/DEV/?deviceID={id} HTTP/2.0
accept: application/json, text/plain, */*
auth-token: {jwt}
content-type: application/json
content-length: 33
accept-encoding: gzip
user-agent: okhttp/4.9.2
```

```json
{"rfid":{"blockEnabled":1}}
```

## Response

```http
HTTP/2.0 200 
date: {date header}
content-type: application/json
content-length: 33
x-amzn-requestid: {uuid}
x-amz-apigw-id: {id}
x-amzn-trace-id: {stuff}
```

```json
{"message":"Shadow updated successfully."}
```
