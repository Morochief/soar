=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "8cdd5e6a-5584-4969-855d-29ff3e51c3da1784728562196-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2372,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "CsYaip8BI3UnQyDO9A70",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25007",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "ae4c07a3-70fd-43e3-a206-b619b5c6197c"
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
                        "ip": "172.16.202.7"
                    },
                    "hostip": "172.16.202.7",
                    "hostip_assetid": "b9bca4ec-7edb-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.7",
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
                    "orig_id": "CsYaip8BI3UnQyDO9A70",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-22T13:49:10.907Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "ad40b9fb-c835-4206-9f58-b53861452b6c",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "ae4c07a3-70fd-43e3-a206-b619b5c6197c",
                        "location": "NBCJPPA25007",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ASU6209",
                        "source_info": {
                            "ip": "172.16.202.7"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "693bfe1072291113e7f8cea6",
                        "when": "2026-07-22T13:48:37.000Z"
                    },
                    "stellar": {
                        "detection_time": 112021,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "8cdd5e6a-5584-4969-855d-29ff3e51c3da1784728562196-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784728150907,
                    "timestamp_utc": "2026-07-22T13:49:10.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ASU6209"
                    },
                    "username": "CAJAANDE\\ASU6209",
                    "write_by": "sef",
                    "write_time": 1784728562196,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.7\", User Name of \"CAJAANDE\\ASU6209\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "7bf2d533-b529-4590-86e9-df13e3464ce51784728919908-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2375,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YMYfip8BI3UnQyDOiGqy",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25007",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "ae4c07a3-70fd-43e3-a206-b619b5c6197c"
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
                        "ip": "172.16.202.7"
                    },
                    "hostip": "172.16.202.7",
                    "hostip_assetid": "b9bca4ec-7edb-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.7",
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
                    "orig_id": "YMYfip8BI3UnQyDOiGqy",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-22T13:49:10.907Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "ad40b9fb-c835-4206-9f58-b53861452b6c",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "ae4c07a3-70fd-43e3-a206-b619b5c6197c",
                        "location": "NBCJPPA25007",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\ASU6209",
                        "source_info": {
                            "ip": "172.16.202.7"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "693bfe1072291113e7f8cea6",
                        "when": "2026-07-22T13:48:37.000Z"
                    },
                    "stellar": {
                        "detection_time": 169753,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "7bf2d533-b529-4590-86e9-df13e3464ce51784728919908-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784728150907,
                    "timestamp_utc": "2026-07-22T13:49:10.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\ASU6209"
                    },
                    "username": "CAJAANDE\\ASU6209",
                    "write_by": "sef",
                    "write_time": 1784728919908,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.7\", User Name of \"CAJAANDE\\ASU6209\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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