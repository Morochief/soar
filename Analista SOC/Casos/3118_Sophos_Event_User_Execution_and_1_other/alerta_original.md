=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ae386ff5-36f9-4522-a899-406078b94f7b1783790138414-YWVsbGEtc2VyLTIwMjYuMDcuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 9660,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YywrUp8BI3UnQyDOh70s",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA068",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "56b4180f-15b2-4d9e-90ae-80d44283c5d7"
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
                        "ip": "172.16.202.88"
                    },
                    "hostip": "172.16.202.88",
                    "hostip_assetid": "9033cff2-73ae-11f1-b2b7-5ae6db116d2f",
                    "hostip_host": "172.16.202.88",
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
                    "orig_id": "YywrUp8BI3UnQyDOh70s",
                    "orig_index": "aella-syslog-2026.07.11-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-11T17:12:34.927Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "431247e4-cc5f-4eb6-a3ee-719aec6bc3fc",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "56b4180f-15b2-4d9e-90ae-80d44283c5d7",
                        "location": "CJPPA068",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ypalma",
                        "source_info": {
                            "ip": "172.16.202.88"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6928885528a45437badcd858",
                        "when": "2026-07-11T17:12:07.000Z"
                    },
                    "stellar": {
                        "detection_time": 127465,
                        "status": "New"
                    },
                    "stellar_da_input": 1354,
                    "stellar_index_id": "aella-ser-2026.07.11-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "ae386ff5-36f9-4522-a899-406078b94f7b1783790138414-YWVsbGEtc2VyLTIwMjYuMDcuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783789954927,
                    "timestamp_utc": "2026-07-11T17:12:34.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ypalma"
                    },
                    "username": "CAJAANDE\\ypalma",
                    "write_by": "sef",
                    "write_time": 1783790138414,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.88\", User Name of \"CAJAANDE\\ypalma\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "f37c29d5-7b75-43d5-abdc-8276db49436c1783790376707-YWVsbGEtc2VyLTIwMjYuMDcuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 9661,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "zywwUp8BI3UnQyDOGt7B",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA068",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "56b4180f-15b2-4d9e-90ae-80d44283c5d7"
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
                        "ip": "172.16.202.88"
                    },
                    "hostip": "172.16.202.88",
                    "hostip_assetid": "9033cff2-73ae-11f1-b2b7-5ae6db116d2f",
                    "hostip_host": "172.16.202.88",
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
                    "orig_id": "zywwUp8BI3UnQyDOGt7B",
                    "orig_index": "aella-syslog-2026.07.11-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-11T17:12:34.927Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "431247e4-cc5f-4eb6-a3ee-719aec6bc3fc",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "56b4180f-15b2-4d9e-90ae-80d44283c5d7",
                        "location": "CJPPA068",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ypalma",
                        "source_info": {
                            "ip": "172.16.202.88"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6928885528a45437badcd858",
                        "when": "2026-07-11T17:12:07.000Z"
                    },
                    "stellar": {
                        "detection_time": 65745,
                        "status": "New"
                    },
                    "stellar_da_input": 1354,
                    "stellar_index_id": "aella-ser-2026.07.11-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "f37c29d5-7b75-43d5-abdc-8276db49436c1783790376707-YWVsbGEtc2VyLTIwMjYuMDcuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1783789954927,
                    "timestamp_utc": "2026-07-11T17:12:34.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ypalma"
                    },
                    "username": "CAJAANDE\\ypalma",
                    "write_by": "sef",
                    "write_time": 1783790376707,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.88\", User Name of \"CAJAANDE\\ypalma\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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