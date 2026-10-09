=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.02-000032",
                "_type": "_doc",
                "_id": "48d05ae1-42a4-4f5a-8374-bca82217bf681789056786207-YWVsbGEtc2VyLTIwMjYuMDkuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 12649,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "vQUWjKABI3UnQyDOU-LY",
                    "appid_stdport": "yes",
                    "computer_name": "cjppa_hp_26001",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "454aad1b-5d7e-41b6-b261-272efd36ded1"
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
                        "ip": "172.16.202.16"
                    },
                    "hostip": "172.16.202.16",
                    "hostip_assetid": "11acffa8-9fac-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.16",
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
                    "orig_id": "vQUWjKABI3UnQyDOU-LY",
                    "orig_index": "aella-syslog-2026.09.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-10T16:07:50.931Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bce5bd50-ce1c-4317-af79-fadf6346fbe6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "454aad1b-5d7e-41b6-b261-272efd36ded1",
                        "location": "cjppa_hp_26001",
                        "name": "'https://s328.erome.com' blocked due to category 'Adult/Sexually Explicit'",
                        "severity": "low",
                        "source": "CAJAANDE\\agaray",
                        "source_info": {
                            "ip": "172.16.202.16"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "69272bb00ccaad6f2468c7a3",
                        "when": "2026-09-10T16:07:30.000Z"
                    },
                    "stellar": {
                        "detection_time": 117864,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.09.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "48d05ae1-42a4-4f5a-8374-bca82217bf681789056786207-YWVsbGEtc2VyLTIwMjYuMDkuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1789056470931,
                    "timestamp_utc": "2026-09-10T16:07:50.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\agaray"
                    },
                    "username": "CAJAANDE\\agaray",
                    "write_by": "sef",
                    "write_time": 1789056786207,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.16\", User Name of \"CAJAANDE\\agaray\".\nThe description of the event states that \"'https://s328.erome.com' blocked due to category 'Adult/Sexually Explicit'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.02-000032",
                "_type": "_doc",
                "_id": "786ba681-646e-46f9-90ce-a5febf3f412d1789057143548-YWVsbGEtc2VyLTIwMjYuMDkuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 12655,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "yAYajKABI3UnQyDO7CnU",
                    "appid_stdport": "yes",
                    "computer_name": "cjppa_hp_26001",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "454aad1b-5d7e-41b6-b261-272efd36ded1"
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
                        "ip": "172.16.202.16"
                    },
                    "hostip": "172.16.202.16",
                    "hostip_assetid": "11acffa8-9fac-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.16",
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
                    "orig_id": "yAYajKABI3UnQyDO7CnU",
                    "orig_index": "aella-syslog-2026.09.10-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-10T16:07:50.931Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bce5bd50-ce1c-4317-af79-fadf6346fbe6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "454aad1b-5d7e-41b6-b261-272efd36ded1",
                        "location": "cjppa_hp_26001",
                        "name": "'https://s328.erome.com' blocked due to category 'Adult/Sexually Explicit'",
                        "severity": "low",
                        "source": "CAJAANDE\\agaray",
                        "source_info": {
                            "ip": "172.16.202.16"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "69272bb00ccaad6f2468c7a3",
                        "when": "2026-09-10T16:07:30.000Z"
                    },
                    "stellar": {
                        "detection_time": 174601,
                        "status": "New"
                    },
                    "stellar_da_input": 1362,
                    "stellar_index_id": "aella-ser-2026.09.10-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "786ba681-646e-46f9-90ce-a5febf3f412d1789057143548-YWVsbGEtc2VyLTIwMjYuMDkuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1789056470931,
                    "timestamp_utc": "2026-09-10T16:07:50.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\agaray"
                    },
                    "username": "CAJAANDE\\agaray",
                    "write_by": "sef",
                    "write_time": 1789057143547,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.16\", User Name of \"CAJAANDE\\agaray\".\nThe description of the event states that \"'https://s328.erome.com' blocked due to category 'Adult/Sexually Explicit'\"",
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
