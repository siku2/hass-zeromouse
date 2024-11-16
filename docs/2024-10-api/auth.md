# Authentication

Uses AWS Cognito.

## Start

```http
POST https://cognito-idp.eu-central-1.amazonaws.com/ HTTP/2.0
x-amz-target: AWSCognitoIdentityProviderService.InitiateAuth
x-amz-user-agent: aws-amplify/5.0.4 react-native
cache-control: no-store
content-type: application/x-amz-json-1.1
content-length: 333
accept-encoding: gzip
user-agent: okhttp/4.9.2
```

```json
{"AuthFlow":"USER_SRP_AUTH","ClientId":"7pdec0rbivg5hg8u3pke4veg0f","AuthParameters":{"USERNAME":"{email}","SRP_A":"{hex something}"},"ClientMetadata":{}}
```

## Relevant values

```yaml
identity_pool_id: "eu-central-1:2b2f7d40-d6f9-474e-a06b-6441c4059601"
user_pool_id: eu-central-1_LS6CKN0t1
client_id: 7pdec0rbivg5hg8u3pke4veg0f
aws_appsync_api_key: da2-r5hq3osgpbdmtd6nx67tvlyxum
```
