=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "f4b5bafe-bb8e-45e5-9b38-251922152c6b1785498182683-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 13405,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "n9b6t58BI3UnQyDORpFQ",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA0041",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "8655b7f5-f15b-484d-b341-5fc6edfe7818"
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
                        "ip": "172.16.202.61"
                    },
                    "hostip": "172.16.202.61",
                    "hostip_assetid": "04644626-84f4-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.61",
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
                    "orig_id": "n9b6t58BI3UnQyDORpFQ",
                    "orig_index": "aella-syslog-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-31T11:40:33.816Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "d5c1ea9f-d242-4033-966a-44eb333dba1c",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "8655b7f5-f15b-484d-b341-5fc6edfe7818",
                        "location": "CJPPA0041",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\mcalcena",
                        "source_info": {
                            "ip": "172.16.202.61"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fb80d6996931ea6fb55c",
                        "when": "2026-07-31T11:39:55.000Z"
                    },
                    "stellar": {
                        "detection_time": 122440,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "f4b5bafe-bb8e-45e5-9b38-251922152c6b1785498182683-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785498033816,
                    "timestamp_utc": "2026-07-31T11:40:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\mcalcena"
                    },
                    "username": "CAJAANDE\\mcalcena",
                    "write_by": "sef",
                    "write_time": 1785498182683,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.61\", User Name of \"CAJAANDE\\mcalcena\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "e9ea2d7a-e343-4ced-b374-4572f08adb491785498420901-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 13409,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "-9b-t58BI3UnQyDO2sRa",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA0041",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "8655b7f5-f15b-484d-b341-5fc6edfe7818"
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
                        "ip": "172.16.202.61"
                    },
                    "hostip": "172.16.202.61",
                    "hostip_assetid": "04644626-84f4-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.61",
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
                    "orig_id": "-9b-t58BI3UnQyDO2sRa",
                    "orig_index": "aella-syslog-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-31T11:40:33.816Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "d5c1ea9f-d242-4033-966a-44eb333dba1c",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "8655b7f5-f15b-484d-b341-5fc6edfe7818",
                        "location": "CJPPA0041",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\mcalcena",
                        "source_info": {
                            "ip": "172.16.202.61"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fb80d6996931ea6fb55c",
                        "when": "2026-07-31T11:39:55.000Z"
                    },
                    "stellar": {
                        "detection_time": 60637,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e9ea2d7a-e343-4ced-b374-4572f08adb491785498420901-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785498033816,
                    "timestamp_utc": "2026-07-31T11:40:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\mcalcena"
                    },
                    "username": "CAJAANDE\\mcalcena",
                    "write_by": "sef",
                    "write_time": 1785498420901,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.61\", User Name of \"CAJAANDE\\mcalcena\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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

---------------------------------------------------------------------------
[+] MEMORIA SOAR: Logs de Interflow recuperados desde el caché RAM.