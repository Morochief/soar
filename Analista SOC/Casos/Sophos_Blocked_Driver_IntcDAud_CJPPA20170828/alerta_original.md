{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.02-000032",
                "_type": "_doc",
                "_id": "217d26e7-990b-49b5-ae7a-a7cd5cf12de91788518736704-YWVsbGEtc2VyLTIwMjYuMDkuMDQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 368,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "GYYDbKABI3UnQyDO4Ry8",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA20170828",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "fa059987-9724-4b32-99fb-c9e6b727cf33"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CoreBlockedDriverDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb"
                        }
                    },
                    "group": "RUNTIME_DETECTIONS",
                    "host": {
                        "ip": "172.16.202.86"
                    },
                    "hostip": "172.16.202.86",
                    "hostip_assetid": "b36e5324-a163-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.86",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "locid": "unassigned location",
                    "msg_class": "sophos_events",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "id": "69402f1ea496888ec6063954",
                            "name": "sophos_events",
                            "type": "log_collector"
                        },
                        "source": "sophos_events",
                        "vendor": "sophos"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "GYYDbKABI3UnQyDO4Ry8",
                    "orig_index": "aella-syslog-2026.09.04-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb",
                    "sophos": {
                        "appSha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb",
                        "created_at": "2026-09-04T10:42:29.165Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "886ac728-64ac-4133-84dd-e57b68c11257",
                        "endpoint_type": "computer",
                        "group": "RUNTIME_DETECTIONS",
                        "id": "fa059987-9724-4b32-99fb-c9e6b727cf33",
                        "location": "CJPPA20170828",
                        "name": "Driver detected: 'C:\\Windows\\System32\\drivers\\IntcDAud.sys'",
                        "origin": "DRIVER_BLOCKLIST",
                        "severity": "medium",
                        "source": "CAJAANDE\\MP5681371",
                        "source_info": {
                            "ip": "172.16.202.86"
                        },
                        "threat": "UnauthorizedDriver",
                        "type": "Event::Endpoint::CoreBlockedDriverDetection",
                        "user_id": "6a980a057b58ddc084517daf",
                        "when": "2026-09-04T10:42:10.049Z"
                    },
                    "stellar": {
                        "detection_time": 148302,
                        "status": "New"
                    },
                    "stellar_da_input": 1759,
                    "stellar_index_id": "aella-ser-2026.09.04-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "217d26e7-990b-49b5-ae7a-a7cd5cf12de91788518736704-YWVsbGEtc2VyLTIwMjYuMDkuMDQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "UnauthorizedDriver",
                    "threat_score": 0,
                    "timestamp": 1788518549165,
                    "timestamp_utc": "2026-09-04T10:42:29.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\MP5681371"
                    },
                    "username": "CAJAANDE\\MP5681371",
                    "write_by": "sef",
                    "write_time": 1788518736704,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CoreBlockedDriverDetection\", Host IP of \"172.16.202.86\", User Name of \"CAJAANDE\\MP5681371\".\nThe description of the event states that \"Driver detected: 'C:\\Windows\\System32\\drivers\\IntcDAud.sys'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CoreBlockedDriverDetection",
                            "name": "event_endpoint_coreblockeddriverdetection"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.02-000032",
                "_type": "_doc",
                "_id": "3be61316-10a9-49e5-ab26-1af6c2f583741788518974961-YWVsbGEtc2VyLTIwMjYuMDkuMDQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 370,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "loYIbKABI3UnQyDOdErD",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA20170828",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "fa059987-9724-4b32-99fb-c9e6b727cf33"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CoreBlockedDriverDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb"
                        }
                    },
                    "group": "RUNTIME_DETECTIONS",
                    "host": {
                        "ip": "172.16.202.86"
                    },
                    "hostip": "172.16.202.86",
                    "hostip_assetid": "b36e5324-a163-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.86",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "locid": "unassigned location",
                    "msg_class": "sophos_events",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "id": "69402f1ea496888ec6063954",
                            "name": "sophos_events",
                            "type": "log_collector"
                        },
                        "source": "sophos_events",
                        "vendor": "sophos"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "loYIbKABI3UnQyDOdErD",
                    "orig_index": "aella-syslog-2026.09.04-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb",
                    "sophos": {
                        "appSha256": "5c1135081e29d7f4a97d5caa2c8fbe1dd04ec7a3d8e648e69f2aa9ebdd88ebbb",
                        "created_at": "2026-09-04T10:42:29.165Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "886ac728-64ac-4133-84dd-e57b68c11257",
                        "endpoint_type": "computer",
                        "group": "RUNTIME_DETECTIONS",
                        "id": "fa059987-9724-4b32-99fb-c9e6b727cf33",
                        "location": "CJPPA20170828",
                        "name": "Driver detected: 'C:\\Windows\\System32\\drivers\\IntcDAud.sys'",
                        "origin": "DRIVER_BLOCKLIST",
                        "severity": "medium",
                        "source": "CAJAANDE\\MP5681371",
                        "source_info": {
                            "ip": "172.16.202.86"
                        },
                        "threat": "UnauthorizedDriver",
                        "type": "Event::Endpoint::CoreBlockedDriverDetection",
                        "user_id": "6a980a057b58ddc084517daf",
                        "when": "2026-09-04T10:42:10.049Z"
                    },
                    "stellar": {
                        "detection_time": 86561,
                        "status": "New"
                    },
                    "stellar_da_input": 1759,
                    "stellar_index_id": "aella-ser-2026.09.04-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "3be61316-10a9-49e5-ab26-1af6c2f583741788518974961-YWVsbGEtc2VyLTIwMjYuMDkuMDQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "UnauthorizedDriver",
                    "threat_score": 0,
                    "timestamp": 1788518549165,
                    "timestamp_utc": "2026-09-04T10:42:29.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\MP5681371"
                    },
                    "username": "CAJAANDE\\MP5681371",
                    "write_by": "sef",
                    "write_time": 1788518974961,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CoreBlockedDriverDetection\", Host IP of \"172.16.202.86\", User Name of \"CAJAANDE\\MP5681371\".\nThe description of the event states that \"Driver detected: 'C:\\Windows\\System32\\drivers\\IntcDAud.sys'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CoreBlockedDriverDetection",
                            "name": "event_endpoint_coreblockeddriverdetection"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
