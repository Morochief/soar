{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "c6d38607-f753-4986-a4c5-005794f51a5b1788454175811-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 26853,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "iVYraKABI3UnQyDOO6N8",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA20120902",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e1157deb-d71e-49a6-a099-cdc0ef5ccb2e"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::WebControlViolation"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "WEB",
                    "host": {
                        "ip": "172.16.202.115"
                    },
                    "hostip": "172.16.202.115",
                    "hostip_host": "172.16.202.115",
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
                    "orig_id": "iVYraKABI3UnQyDOO6N8",
                    "orig_index": "aella-syslog-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-03T16:46:04.287Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "212cbf6d-aeaa-4ea8-815c-38047cdb69a5",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e1157deb-d71e-49a6-a099-cdc0ef5ccb2e",
                        "location": "CJPPA20120902",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\MP6236932",
                        "source_info": {
                            "ip": "172.16.202.115"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6a985a1e25f55650e21edf2d",
                        "when": "2026-09-03T16:45:48.000Z"
                    },
                    "stellar": {
                        "detection_time": 117302,
                        "status": "New"
                    },
                    "stellar_da_input": 1376,
                    "stellar_index_id": "aella-ser-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "c6d38607-f753-4986-a4c5-005794f51a5b1788454175811-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1788453964287,
                    "timestamp_utc": "2026-09-03T16:46:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\MP6236932"
                    },
                    "username": "CAJAANDE\\MP6236932",
                    "write_by": "sef",
                    "write_time": 1788454175811,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.115\", User Name of \"CAJAANDE\\MP6236932\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::WebControlViolation",
                            "name": "event_endpoint_webcontrolviolation"
                        },
                        "tactic": {
                            "id": "TA0002",
                            "name": "Execution"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "T1204",
                            "name": "User Execution"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0002",
                                    "name": "Execution"
                                },
                                "technique": {
                                    "id": "T1204",
                                    "name": "User Execution"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "ea1a0155-b123-4faf-b173-31239a6781721788454533129-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 26880,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "pVYvaKABI3UnQyDO9f5J",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA20120902",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e1157deb-d71e-49a6-a099-cdc0ef5ccb2e"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::WebControlViolation"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "WEB",
                    "host": {
                        "ip": "172.16.202.115"
                    },
                    "hostip": "172.16.202.115",
                    "hostip_host": "172.16.202.115",
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
                    "orig_id": "pVYvaKABI3UnQyDO9f5J",
                    "orig_index": "aella-syslog-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-03T16:46:04.287Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "212cbf6d-aeaa-4ea8-815c-38047cdb69a5",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e1157deb-d71e-49a6-a099-cdc0ef5ccb2e",
                        "location": "CJPPA20120902",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\MP6236932",
                        "source_info": {
                            "ip": "172.16.202.115"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6a985a1e25f55650e21edf2d",
                        "when": "2026-09-03T16:45:48.000Z"
                    },
                    "stellar": {
                        "detection_time": 164725,
                        "status": "New"
                    },
                    "stellar_da_input": 1376,
                    "stellar_index_id": "aella-ser-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "ea1a0155-b123-4faf-b173-31239a6781721788454533129-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1788453964287,
                    "timestamp_utc": "2026-09-03T16:46:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\MP6236932"
                    },
                    "username": "CAJAANDE\\MP6236932",
                    "write_by": "sef",
                    "write_time": 1788454533129,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.115\", User Name of \"CAJAANDE\\MP6236932\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::WebControlViolation",
                            "name": "event_endpoint_webcontrolviolation"
                        },
                        "tactic": {
                            "id": "TA0002",
                            "name": "Execution"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "T1204",
                            "name": "User Execution"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0002",
                                    "name": "Execution"
                                },
                                "technique": {
                                    "id": "T1204",
                                    "name": "User Execution"
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
