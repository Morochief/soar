=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "513a343b-e8c7-4cde-b322-7f1a7782520e1783679974991-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 8144,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "JNqZS58BI3UnQyDO-_qI",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA011",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e30e2c78-76db-4812-98e4-99ccd1fa3748"
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
                        "ip": "172.16.202.31"
                    },
                    "hostip": "172.16.202.31",
                    "hostip_assetid": "579e2420-73a5-11f1-b2b7-5ae6db116d2f",
                    "hostip_host": "172.16.202.31",
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
                    "orig_id": "JNqZS58BI3UnQyDO-_qI",
                    "orig_index": "aella-syslog-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-10T10:32:54.891Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "5be63215-b68a-46ec-b8b1-c14bdb638eb3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e30e2c78-76db-4812-98e4-99ccd1fa3748",
                        "location": "CJPPA011",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\demiguel",
                        "source_info": {
                            "ip": "172.16.202.31"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fed561055368e6696c5e",
                        "when": "2026-07-10T10:32:29.000Z"
                    },
                    "stellar": {
                        "detection_time": 164732,
                        "status": "New"
                    },
                    "stellar_da_input": 1360,
                    "stellar_index_id": "aella-ser-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "513a343b-e8c7-4cde-b322-7f1a7782520e1783679974991-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783679574891,
                    "timestamp_utc": "2026-07-10T10:32:54.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\demiguel"
                    },
                    "username": "CAJAANDE\\demiguel",
                    "write_by": "sef",
                    "write_time": 1783679974991,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.31\", User Name of \"CAJAANDE\\demiguel\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "fc9c196e-63b8-476d-bd3a-7640eded8f681783680213202-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 8146,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "NdueS58BI3UnQyDOjhyI",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA011",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "e30e2c78-76db-4812-98e4-99ccd1fa3748"
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
                        "ip": "172.16.202.31"
                    },
                    "hostip": "172.16.202.31",
                    "hostip_assetid": "579e2420-73a5-11f1-b2b7-5ae6db116d2f",
                    "hostip_host": "172.16.202.31",
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
                    "orig_id": "NdueS58BI3UnQyDOjhyI",
                    "orig_index": "aella-syslog-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-10T10:32:54.891Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "5be63215-b68a-46ec-b8b1-c14bdb638eb3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "e30e2c78-76db-4812-98e4-99ccd1fa3748",
                        "location": "CJPPA011",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\demiguel",
                        "source_info": {
                            "ip": "172.16.202.31"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fed561055368e6696c5e",
                        "when": "2026-07-10T10:32:29.000Z"
                    },
                    "stellar": {
                        "detection_time": 103037,
                        "status": "New"
                    },
                    "stellar_da_input": 1360,
                    "stellar_index_id": "aella-ser-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "fc9c196e-63b8-476d-bd3a-7640eded8f681783680213202-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783679574891,
                    "timestamp_utc": "2026-07-10T10:32:54.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\demiguel"
                    },
                    "username": "CAJAANDE\\demiguel",
                    "write_by": "sef",
                    "write_time": 1783680213202,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.31\", User Name of \"CAJAANDE\\demiguel\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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