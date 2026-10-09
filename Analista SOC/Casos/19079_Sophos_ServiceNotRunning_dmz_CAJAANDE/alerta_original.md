# Alertas Originales Interflow / Stellar Cyber

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "b628c30b-ae6d-4732-b5a0-6a7fe16d94a21790253327185-YWVsbGEtc2VyLTIwMjYuMDkuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 19079,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Kedo06ABI3UnQyDOHoz4",
                    "appid_stdport": "yes",
                    "computer_name": "dmz",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "31ced54d-949b-4e6c-af50-2a0c0dc5be66"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "high",
                        "threat": {
                            "name": "Event::Endpoint::ServiceNotRunning"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 65,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 65,
                    "group": "PROTECTION",
                    "host": {
                        "ip": "192.168.30.5"
                    },
                    "hostip": "192.168.30.5",
                    "hostip_assetid": "e7cf1ae0-d9d1-11f0-bee4-aa0456b9a54a",
                    "hostip_host": "192.168.30.5",
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
                    "orig_id": "Kedo06ABI3UnQyDOHoz4",
                    "orig_index": "aella-syslog-2026.09.24-392cf7319d694d53889280340fff51e9",
                    "severity": 65,
                    "sophos": {
                        "created_at": "2026-09-24T12:30:05.884Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "cd39704e-447e-4167-8980-2c8a8e6e4cfb",
                        "endpoint_type": "server",
                        "group": "PROTECTION",
                        "id": "31ced54d-949b-4e6c-af50-2a0c0dc5be66",
                        "location": "dmz",
                        "name": "One or more Sophos services are missing or not running",
                        "severity": "high",
                        "source_info": {
                            "ip": "192.168.30.5"
                        },
                        "type": "Event::Endpoint::ServiceNotRunning",
                        "when": "2026-09-24T12:30:05.872Z"
                    },
                    "stellar": {
                        "detection_time": 116523,
                        "status": "New"
                    },
                    "stellar_da_input": 1188,
                    "stellar_index_id": "aella-ser-2026.09.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "b628c30b-ae6d-4732-b5a0-6a7fe16d94a21790253327185-YWVsbGEtc2VyLTIwMjYuMDkuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1790253005884,
                    "timestamp_utc": "2026-09-24T12:30:05.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "write_by": "sef",
                    "write_time": 1790253327185,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::ServiceNotRunning\", Host IP of \"192.168.30.5\".\nThe description of the event states that \"One or more Sophos services are missing or not running\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::ServiceNotRunning",
                            "name": "event_endpoint_servicenotrunning"
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "15ecac21-8633-4468-82e9-a5190fc7ef641790253684586-YWVsbGEtc2VyLTIwMjYuMDkuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 19088,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "9uhs06ABI3UnQyDOrygn",
                    "appid_stdport": "yes",
                    "computer_name": "dmz",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "31ced54d-949b-4e6c-af50-2a0c0dc5be66"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "high",
                        "threat": {
                            "name": "Event::Endpoint::ServiceNotRunning"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 65,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 65,
                    "group": "PROTECTION",
                    "host": {
                        "ip": "192.168.30.5"
                    },
                    "hostip": "192.168.30.5",
                    "hostip_assetid": "e7cf1ae0-d9d1-11f0-bee4-aa0456b9a54a",
                    "hostip_host": "192.168.30.5",
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
                    "orig_id": "9uhs06ABI3UnQyDOrygn",
                    "orig_index": "aella-syslog-2026.09.24-392cf7319d694d53889280340fff51e9",
                    "severity": 65,
                    "sophos": {
                        "created_at": "2026-09-24T12:30:05.884Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "cd39704e-447e-4167-8980-2c8a8e6e4cfb",
                        "endpoint_type": "server",
                        "group": "PROTECTION",
                        "id": "31ced54d-949b-4e6c-af50-2a0c0dc5be66",
                        "location": "dmz",
                        "name": "One or more Sophos services are missing or not running",
                        "severity": "high",
                        "source_info": {
                            "ip": "192.168.30.5"
                        },
                        "type": "Event::Endpoint::ServiceNotRunning",
                        "when": "2026-09-24T12:30:05.872Z"
                    },
                    "stellar": {
                        "detection_time": 174391,
                        "status": "New"
                    },
                    "stellar_da_input": 1188,
                    "stellar_index_id": "aella-ser-2026.09.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "15ecac21-8633-4468-82e9-a5190fc7ef641790253684586-YWVsbGEtc2VyLTIwMjYuMDkuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1790253005884,
                    "timestamp_utc": "2026-09-24T12:30:05.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "write_by": "sef",
                    "write_time": 1790253684586,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::ServiceNotRunning\", Host IP of \"192.168.30.5\".\nThe description of the event states that \"One or more Sophos services are missing or not running\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::ServiceNotRunning",
                            "name": "event_endpoint_servicenotrunning"
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
```
