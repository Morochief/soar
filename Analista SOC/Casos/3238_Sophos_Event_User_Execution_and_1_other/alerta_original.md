=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "28358a13-e129-419d-8531-1e9b14f5ec851784803011031-YWVsbGEtc2VyLTIwMjYuMDcuMjMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 3490,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "q_-Kjp8BI3UnQyDOq0wN",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA037",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e28d4600-bff6-4751-83fc-21420f3cbc2a"
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
                        "ip": "172.16.202.57"
                    },
                    "hostip": "172.16.202.57",
                    "hostip_assetid": "9395d82a-6eea-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.57",
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
                    "orig_id": "q_-Kjp8BI3UnQyDOq0wN",
                    "orig_index": "aella-syslog-2026.07.23-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-23T10:33:38.175Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2ad159c5-1269-45d4-a7b9-3e7c28a728b1",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e28d4600-bff6-4751-83fc-21420f3cbc2a",
                        "location": "CJPPA037",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\CJPPA_3509448",
                        "source_info": {
                            "ip": "172.16.202.57"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926feabd6996931ea6fb560",
                        "when": "2026-07-23T10:33:03.000Z"
                    },
                    "stellar": {
                        "detection_time": 130877,
                        "status": "New"
                    },
                    "stellar_da_input": 1375,
                    "stellar_index_id": "aella-ser-2026.07.23-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "28358a13-e129-419d-8531-1e9b14f5ec851784803011031-YWVsbGEtc2VyLTIwMjYuMDcuMjMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784802818175,
                    "timestamp_utc": "2026-07-23T10:33:38.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\CJPPA_3509448"
                    },
                    "username": "CAJAANDE\\CJPPA_3509448",
                    "write_by": "sef",
                    "write_time": 1784803011031,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.57\", User Name of \"CAJAANDE\\CJPPA_3509448\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "3558b7f0-b0f9-48aa-9913-d6c61e959b431784803249289-YWVsbGEtc2VyLTIwMjYuMDcuMjMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 3493,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "R_-Pjp8BI3UnQyDOPm_S",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA037",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e28d4600-bff6-4751-83fc-21420f3cbc2a"
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
                        "ip": "172.16.202.57"
                    },
                    "hostip": "172.16.202.57",
                    "hostip_assetid": "9395d82a-6eea-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.57",
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
                    "orig_id": "R_-Pjp8BI3UnQyDOPm_S",
                    "orig_index": "aella-syslog-2026.07.23-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-23T10:33:38.175Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2ad159c5-1269-45d4-a7b9-3e7c28a728b1",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e28d4600-bff6-4751-83fc-21420f3cbc2a",
                        "location": "CJPPA037",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\CJPPA_3509448",
                        "source_info": {
                            "ip": "172.16.202.57"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926feabd6996931ea6fb560",
                        "when": "2026-07-23T10:33:03.000Z"
                    },
                    "stellar": {
                        "detection_time": 69144,
                        "status": "New"
                    },
                    "stellar_da_input": 1375,
                    "stellar_index_id": "aella-ser-2026.07.23-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "3558b7f0-b0f9-48aa-9913-d6c61e959b431784803249289-YWVsbGEtc2VyLTIwMjYuMDcuMjMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784802818175,
                    "timestamp_utc": "2026-07-23T10:33:38.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\CJPPA_3509448"
                    },
                    "username": "CAJAANDE\\CJPPA_3509448",
                    "write_by": "sef",
                    "write_time": 1784803249289,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.57\", User Name of \"CAJAANDE\\CJPPA_3509448\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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