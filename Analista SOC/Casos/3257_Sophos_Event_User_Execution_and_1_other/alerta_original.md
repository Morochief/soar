=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "aa15612b-8429-4da3-beeb-232825556fe31784899138799-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4912,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "U0tGlJ8BI3UnQyDOQgkA",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25009",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "330f8670-ef59-4e52-9719-ca0dc929ccca"
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
                        "ip": "172.16.202.39"
                    },
                    "hostip": "172.16.202.39",
                    "hostip_assetid": "93ce7734-7ab6-11f1-8d8d-be2f2074df47",
                    "hostip_host": "172.16.202.39",
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
                    "orig_id": "U0tGlJ8BI3UnQyDOQgkA",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T13:12:52.076Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "cd59cf96-32c9-47ef-ad76-efbc8d724101",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "330f8670-ef59-4e52-9719-ca0dc929ccca",
                        "location": "NBCJPPA25009",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\chidalgo",
                        "source_info": {
                            "ip": "172.16.202.39"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "69285a2772291113e7f8cae2",
                        "when": "2026-07-24T13:12:17.000Z"
                    },
                    "stellar": {
                        "detection_time": 78703,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "aa15612b-8429-4da3-beeb-232825556fe31784899138799-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784898772076,
                    "timestamp_utc": "2026-07-24T13:12:52.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\chidalgo"
                    },
                    "username": "CAJAANDE\\chidalgo",
                    "write_by": "sef",
                    "write_time": 1784899138799,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.39\", User Name of \"CAJAANDE\\chidalgo\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "36033458-f055-4bd4-a5ea-8055ad8ac8cd1784899496159-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4919,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "sUtKlJ8BI3UnQyDO2V7X",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25009",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "330f8670-ef59-4e52-9719-ca0dc929ccca"
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
                        "ip": "172.16.202.39"
                    },
                    "hostip": "172.16.202.39",
                    "hostip_assetid": "93ce7734-7ab6-11f1-8d8d-be2f2074df47",
                    "hostip_host": "172.16.202.39",
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
                    "orig_id": "sUtKlJ8BI3UnQyDO2V7X",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T13:12:52.076Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "cd59cf96-32c9-47ef-ad76-efbc8d724101",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "330f8670-ef59-4e52-9719-ca0dc929ccca",
                        "location": "NBCJPPA25009",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\chidalgo",
                        "source_info": {
                            "ip": "172.16.202.39"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "69285a2772291113e7f8cae2",
                        "when": "2026-07-24T13:12:17.000Z"
                    },
                    "stellar": {
                        "detection_time": 135681,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "36033458-f055-4bd4-a5ea-8055ad8ac8cd1784899496159-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784898772076,
                    "timestamp_utc": "2026-07-24T13:12:52.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\chidalgo"
                    },
                    "username": "CAJAANDE\\chidalgo",
                    "write_by": "sef",
                    "write_time": 1784899496158,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.39\", User Name of \"CAJAANDE\\chidalgo\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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