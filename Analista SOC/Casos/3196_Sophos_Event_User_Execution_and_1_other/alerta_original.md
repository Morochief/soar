=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "1e83772a-3aa2-414a-bf48-b5ec2cf91a5f1784306051527-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 14668,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "lrzrcJ8BI3UnQyDOM_3M",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA068",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "6f46a4ee-6583-4bf8-9303-c5a72a3e77e3"
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
                    "orig_id": "lrzrcJ8BI3UnQyDOM_3M",
                    "orig_index": "aella-syslog-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-17T16:28:33.713Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "431247e4-cc5f-4eb6-a3ee-719aec6bc3fc",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "6f46a4ee-6583-4bf8-9303-c5a72a3e77e3",
                        "location": "CJPPA068",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ypalma",
                        "source_info": {
                            "ip": "172.16.202.88"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6928885528a45437badcd858",
                        "when": "2026-07-17T16:28:02.000Z"
                    },
                    "stellar": {
                        "detection_time": 161381,
                        "status": "New"
                    },
                    "stellar_da_input": 1354,
                    "stellar_index_id": "aella-ser-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "1e83772a-3aa2-414a-bf48-b5ec2cf91a5f1784306051527-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784305713713,
                    "timestamp_utc": "2026-07-17T16:28:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ypalma"
                    },
                    "username": "CAJAANDE\\ypalma",
                    "write_by": "sef",
                    "write_time": 1784306051527,
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
                "_id": "f522c9e7-ab63-48ce-b11e-6a0dc989a4c81784306289773-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 14672,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "ir3vcJ8BI3UnQyDOylj_",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA068",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "6f46a4ee-6583-4bf8-9303-c5a72a3e77e3"
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
                    "orig_id": "ir3vcJ8BI3UnQyDOylj_",
                    "orig_index": "aella-syslog-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-17T16:28:33.713Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "431247e4-cc5f-4eb6-a3ee-719aec6bc3fc",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "6f46a4ee-6583-4bf8-9303-c5a72a3e77e3",
                        "location": "CJPPA068",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ypalma",
                        "source_info": {
                            "ip": "172.16.202.88"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6928885528a45437badcd858",
                        "when": "2026-07-17T16:28:02.000Z"
                    },
                    "stellar": {
                        "detection_time": 99170,
                        "status": "New"
                    },
                    "stellar_da_input": 1354,
                    "stellar_index_id": "aella-ser-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "f522c9e7-ab63-48ce-b11e-6a0dc989a4c81784306289773-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784305713713,
                    "timestamp_utc": "2026-07-17T16:28:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ypalma"
                    },
                    "username": "CAJAANDE\\ypalma",
                    "write_by": "sef",
                    "write_time": 1784306289773,
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