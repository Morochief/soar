=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "8518863b-4ccb-450a-ae05-c22732a2bd3d1784299976264-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 14507,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "G7WPcJ8BI3UnQyDOpyC7",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA010",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "1113dd99-b388-42a1-84b6-a9f52a5c62a7"
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
                        "ip": "172.16.202.30"
                    },
                    "hostip": "172.16.202.30",
                    "hostip_host": "172.16.202.30",
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
                    "orig_id": "G7WPcJ8BI3UnQyDOpyC7",
                    "orig_index": "aella-syslog-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-17T14:47:28.748Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "c25f4eb2-a3d2-4702-b8d0-6cd437cd6489",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "1113dd99-b388-42a1-84b6-a9f52a5c62a7",
                        "location": "CJPPA010",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\gsosa",
                        "source_info": {
                            "ip": "172.16.202.30"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6927044db73d1e40ff07a7e6",
                        "when": "2026-07-17T14:46:58.000Z"
                    },
                    "stellar": {
                        "detection_time": 85898,
                        "status": "New"
                    },
                    "stellar_da_input": 1351,
                    "stellar_index_id": "aella-ser-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "8518863b-4ccb-450a-ae05-c22732a2bd3d1784299976264-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784299648748,
                    "timestamp_utc": "2026-07-17T14:47:28.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\gsosa"
                    },
                    "username": "CAJAANDE\\gsosa",
                    "write_by": "sef",
                    "write_time": 1784299976264,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.30\", User Name of \"CAJAANDE\\gsosa\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "6803dd50-3c4d-489b-8652-724e848d62fd1784300333601-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 14513,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "5rWUcJ8BI3UnQyDOPZi7",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA010",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "1113dd99-b388-42a1-84b6-a9f52a5c62a7"
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
                        "ip": "172.16.202.30"
                    },
                    "hostip": "172.16.202.30",
                    "hostip_host": "172.16.202.30",
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
                    "orig_id": "5rWUcJ8BI3UnQyDOPZi7",
                    "orig_index": "aella-syslog-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-17T14:47:28.748Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "c25f4eb2-a3d2-4702-b8d0-6cd437cd6489",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "1113dd99-b388-42a1-84b6-a9f52a5c62a7",
                        "location": "CJPPA010",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\gsosa",
                        "source_info": {
                            "ip": "172.16.202.30"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6927044db73d1e40ff07a7e6",
                        "when": "2026-07-17T14:46:58.000Z"
                    },
                    "stellar": {
                        "detection_time": 142993,
                        "status": "New"
                    },
                    "stellar_da_input": 1351,
                    "stellar_index_id": "aella-ser-2026.07.17-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "6803dd50-3c4d-489b-8652-724e848d62fd1784300333601-YWVsbGEtc2VyLTIwMjYuMDcuMTctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784299648748,
                    "timestamp_utc": "2026-07-17T14:47:28.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\gsosa"
                    },
                    "username": "CAJAANDE\\gsosa",
                    "write_by": "sef",
                    "write_time": 1784300333600,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.30\", User Name of \"CAJAANDE\\gsosa\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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