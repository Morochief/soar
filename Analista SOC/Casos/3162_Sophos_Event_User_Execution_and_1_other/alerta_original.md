=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "bcbb93dc-eac0-4cda-b716-70d32d65f5e91784116645117-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11006,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "mAehZZ8BI3UnQyDOzDQ4",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA040",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "bfa03087-676e-4e05-ae88-d648d4ad8136"
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
                        "ip": "172.16.202.60"
                    },
                    "hostip": "172.16.202.60",
                    "hostip_assetid": "2986129a-7941-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.60",
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
                    "orig_id": "mAehZZ8BI3UnQyDOzDQ4",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T11:53:07.971Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2d3ab4fe-1e57-4f38-801d-54ba45018aa7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "bfa03087-676e-4e05-ae88-d648d4ad8136",
                        "location": "CJPPA040",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\benitez.sege",
                        "source_info": {
                            "ip": "172.16.202.60"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6932d09772291113e7f8ccfc",
                        "when": "2026-07-15T11:52:37.000Z"
                    },
                    "stellar": {
                        "detection_time": 114952,
                        "status": "New"
                    },
                    "stellar_da_input": 1372,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "bcbb93dc-eac0-4cda-b716-70d32d65f5e91784116645117-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784116387971,
                    "timestamp_utc": "2026-07-15T11:53:07.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\benitez.sege"
                    },
                    "username": "CAJAANDE\\benitez.sege",
                    "write_by": "sef",
                    "write_time": 1784116645117,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.60\", User Name of \"CAJAANDE\\benitez.sege\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "08b3e8cc-4089-4e38-ad01-151b9ca4b9c31784117002487-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11007,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YQemZZ8BI3UnQyDOYHQQ",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA040",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "bfa03087-676e-4e05-ae88-d648d4ad8136"
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
                        "ip": "172.16.202.60"
                    },
                    "hostip": "172.16.202.60",
                    "hostip_assetid": "2986129a-7941-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.60",
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
                    "orig_id": "YQemZZ8BI3UnQyDOYHQQ",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T11:53:07.971Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2d3ab4fe-1e57-4f38-801d-54ba45018aa7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "bfa03087-676e-4e05-ae88-d648d4ad8136",
                        "location": "CJPPA040",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\benitez.sege",
                        "source_info": {
                            "ip": "172.16.202.60"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6932d09772291113e7f8ccfc",
                        "when": "2026-07-15T11:52:37.000Z"
                    },
                    "stellar": {
                        "detection_time": 172334,
                        "status": "New"
                    },
                    "stellar_da_input": 1372,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "08b3e8cc-4089-4e38-ad01-151b9ca4b9c31784117002487-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784116387971,
                    "timestamp_utc": "2026-07-15T11:53:07.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\benitez.sege"
                    },
                    "username": "CAJAANDE\\benitez.sege",
                    "write_by": "sef",
                    "write_time": 1784117002487,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.60\", User Name of \"CAJAANDE\\benitez.sege\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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