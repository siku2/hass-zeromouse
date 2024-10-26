# Get config

## Request

```http
GET https://kus3g3tct7.execute-api.eu-central-1.amazonaws.com/DEV/?deviceID={id} HTTP/2.0
accept: application/json, text/plain, */*
auth-token: {jwt}
accept-encoding: gzip
user-agent: okhttp/4.9.2
content-length: 0
```

## Response

```http
HTTP/2.0 200 
date: {date header}
content-type: application/json
content-length: 3333
x-amzn-requestid: {uuid}
x-amz-apigw-id: {id}
x-amzn-trace-id: {blob}
```

```json
{
    "state": {
        "desired": {
            "rfid": {
                "blockState": 512,
                "blockEnabled": 1
            }
        },
        "reported": {
            "system": {
                "bootCount": 186,
                "wifiRestrtCount": 0,
                "pirTriggerCount": 303,
                "airThrsholdCount": 0,
                "eventCount": 327,
                "ownerID": "{uuid}",
                "identityID": "{aws arn}",
                "finaleIntervalMaxCount": 12,
                "finaleIntervalDelta": 5,
                "metricLastResetReason": "SW",
                "metricWifiConnectCount": 1,
                "metricMQTTErrorCount": 0,
                "metricWifiRSSI": -88,
                "finaleMeanDelta": 20,
                "finaleFreePercent": 15,
                "verMajor": 0,
                "verMinor": 14,
                "verRevision": 2
            },
            "camera": {
                "brightness": -2,
                "exposureCtrl": 0,
                "gainCtrl": 0,
                "gainCtrlMax": 20,
                "whiteBalance": 0,
                "hMirror": 0,
                "vFlip": 0,
                "autoExpLevel": 64,
                "autoExpMax": 250,
                "autoGainCtrl": 128,
                "autoGainCtrlMin": 112,
                "autoGainCtrlMax": 144,
                "autoGainStbl": 128,
                "autoGainStblMin": 120,
                "autoGainStblMax": 136,
                "gainCeiling": 3,
                "dcBrightDetLvl1": 0,
                "dcBrightDetLvl2": 50,
                "dcBrightDetLvl3": 100,
                "dcBrightDetLvl4": 150,
                "dcBrightDetLvl5": 200,
                "dcBrightDetLvl6": 250
            },
            "iot": {
                "respDelayCSecs": 200,
                "pubImageTopic": ""
            },
            "proximity": {
                "irDelayT0ValueMs": 0,
                "irFreeValue": 550,
                "irFreeValueRaw": 550,
                "irRangeIgnoreEvent": 100,
                "irThreshValueOut": 2000,
                "irSlopeThreshValue": 20
            },
            "rfid": {
                "blockEnabled": 0,
                "blockState": 512,
                "blockFeedback": 0,
                "blockCount": 52,
                "unblockCount": 270,
                "unblockRstCount": 0,
                "responseTimeout": 25000,
                "lastRefEventMaxCount": 10,
                "lastRefEventMaxTimeSec": 1800
            }
        },
        "delta": {
            "rfid": {
                "blockEnabled": 1
            }
        }
    },
    "metadata": {
        "desired": {
            "rfid": {
                "blockState": {
                    "timestamp": 1729974640
                },
                "blockEnabled": {
                    "timestamp": 1729974835
                }
            }
        },
        "reported": {
            "system": {
                "bootCount": {
                    "timestamp": 1729973259
                },
                "wifiRestrtCount": {
                    "timestamp": 1729973259
                },
                "pirTriggerCount": {
                    "timestamp": 1729973259
                },
                "airThrsholdCount": {
                    "timestamp": 1729973259
                },
                "eventCount": {
                    "timestamp": 1729974644
                },
                "ownerID": {
                    "timestamp": 1729973259
                },
                "identityID": {
                    "timestamp": 1729973259
                },
                "finaleIntervalMaxCount": {
                    "timestamp": 1729973259
                },
                "finaleIntervalDelta": {
                    "timestamp": 1729973259
                },
                "metricLastResetReason": {
                    "timestamp": 1729973259
                },
                "metricWifiConnectCount": {
                    "timestamp": 1729974644
                },
                "metricMQTTErrorCount": {
                    "timestamp": 1729974644
                },
                "metricWifiRSSI": {
                    "timestamp": 1729974644
                },
                "finaleMeanDelta": {
                    "timestamp": 1729973259
                },
                "finaleFreePercent": {
                    "timestamp": 1729973259
                },
                "verMajor": {
                    "timestamp": 1729973259
                },
                "verMinor": {
                    "timestamp": 1729973259
                },
                "verRevision": {
                    "timestamp": 1729973259
                }
            },
            "camera": {
                "brightness": {
                    "timestamp": 1729973259
                },
                "exposureCtrl": {
                    "timestamp": 1729973259
                },
                "gainCtrl": {
                    "timestamp": 1729973259
                },
                "gainCtrlMax": {
                    "timestamp": 1729973259
                },
                "whiteBalance": {
                    "timestamp": 1729973259
                },
                "hMirror": {
                    "timestamp": 1729973259
                },
                "vFlip": {
                    "timestamp": 1729973259
                },
                "autoExpLevel": {
                    "timestamp": 1729973259
                },
                "autoExpMax": {
                    "timestamp": 1729973259
                },
                "autoGainCtrl": {
                    "timestamp": 1729973259
                },
                "autoGainCtrlMin": {
                    "timestamp": 1729973259
                },
                "autoGainCtrlMax": {
                    "timestamp": 1729973259
                },
                "autoGainStbl": {
                    "timestamp": 1729973259
                },
                "autoGainStblMin": {
                    "timestamp": 1729973259
                },
                "autoGainStblMax": {
                    "timestamp": 1729973259
                },
                "gainCeiling": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl1": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl2": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl3": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl4": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl5": {
                    "timestamp": 1729973259
                },
                "dcBrightDetLvl6": {
                    "timestamp": 1729973259
                }
            },
            "iot": {
                "respDelayCSecs": {
                    "timestamp": 1729973259
                },
                "pubImageTopic": {
                    "timestamp": 1729973259
                }
            },
            "proximity": {
                "irDelayT0ValueMs": {
                    "timestamp": 1729973259
                },
                "irFreeValue": {
                    "timestamp": 1729973259
                },
                "irFreeValueRaw": {
                    "timestamp": 1729973259
                },
                "irRangeIgnoreEvent": {
                    "timestamp": 1729973259
                },
                "irThreshValueOut": {
                    "timestamp": 1729973259
                },
                "irSlopeThreshValue": {
                    "timestamp": 1729973259
                }
            },
            "rfid": {
                "blockEnabled": {
                    "timestamp": 1729974747
                },
                "blockState": {
                    "timestamp": 1729974644
                },
                "blockFeedback": {
                    "timestamp": 1729974747
                },
                "blockCount": {
                    "timestamp": 1729973259
                },
                "unblockCount": {
                    "timestamp": 1729974644
                },
                "unblockRstCount": {
                    "timestamp": 1729973259
                },
                "responseTimeout": {
                    "timestamp": 1729973259
                },
                "lastRefEventMaxCount": {
                    "timestamp": 1729973259
                },
                "lastRefEventMaxTimeSec": {
                    "timestamp": 1729973259
                }
            }
        }
    },
    "version": 1056,
    "timestamp": 1729974836
}
```
