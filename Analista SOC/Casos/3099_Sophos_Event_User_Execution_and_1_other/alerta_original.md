=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "bcd5a8e4-b6c8-433a-8924-9e7b7511885e1783681761688-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 8153,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YNy1S58BI3UnQyDOdAzh",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25210",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "5efbe08c-90e7-41b9-a350-1a34943cc161"
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
                        "ip": "172.16.202.105"
                    },
                    "hostip": "172.16.202.105",
                    "hostip_assetid": "f575ad9c-6ef2-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.105",
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
                    "orig_id": "YNy1S58BI3UnQyDOdAzh",
                    "orig_index": "aella-syslog-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-10T11:02:26.275Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "27f533be-19ab-4c41-b5aa-5ebd546ccfd7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "5efbe08c-90e7-41b9-a350-1a34943cc161",
                        "location": "NBCJPPA25210",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\Mbrizuela",
                        "source_info": {
                            "ip": "172.16.202.105"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fa18e598016d827c8abf",
                        "when": "2026-07-10T11:02:00.000Z"
                    },
                    "stellar": {
                        "detection_time": 151153,
                        "status": "New"
                    },
                    "stellar_da_input": 1374,
                    "stellar_index_id": "aella-ser-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "bcd5a8e4-b6c8-433a-8924-9e7b7511885e1783681761688-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783681346275,
                    "timestamp_utc": "2026-07-10T11:02:26.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Mbrizuela"
                    },
                    "username": "CAJAANDE\\Mbrizuela",
                    "write_by": "sef",
                    "write_time": 1783681761687,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.105\", User Name of \"CAJAANDE\\Mbrizuela\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "c689ec46-679a-4c7e-a888-3b6bc03f6aba1783681999943-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 8155,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Pty6S58BI3UnQyDOCDry",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25210",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "5efbe08c-90e7-41b9-a350-1a34943cc161"
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
                        "ip": "172.16.202.105"
                    },
                    "hostip": "172.16.202.105",
                    "hostip_assetid": "f575ad9c-6ef2-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.105",
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
                    "orig_id": "Pty6S58BI3UnQyDOCDry",
                    "orig_index": "aella-syslog-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-10T11:02:26.275Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "27f533be-19ab-4c41-b5aa-5ebd546ccfd7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "5efbe08c-90e7-41b9-a350-1a34943cc161",
                        "location": "NBCJPPA25210",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\Mbrizuela",
                        "source_info": {
                            "ip": "172.16.202.105"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fa18e598016d827c8abf",
                        "when": "2026-07-10T11:02:00.000Z"
                    },
                    "stellar": {
                        "detection_time": 89369,
                        "status": "New"
                    },
                    "stellar_da_input": 1374,
                    "stellar_index_id": "aella-ser-2026.07.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "c689ec46-679a-4c7e-a888-3b6bc03f6aba1783681999943-YWVsbGEtc2VyLTIwMjYuMDcuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783681346275,
                    "timestamp_utc": "2026-07-10T11:02:26.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Mbrizuela"
                    },
                    "username": "CAJAANDE\\Mbrizuela",
                    "write_by": "sef",
                    "write_time": 1783681999942,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.105\", User Name of \"CAJAANDE\\Mbrizuela\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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