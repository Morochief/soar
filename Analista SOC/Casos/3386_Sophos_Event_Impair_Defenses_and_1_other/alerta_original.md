=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "2d1857ce-8f0f-4660-91b8-7fdb777413f61785927959937-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 668,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "AfCX0Z8BI3UnQyDOvDLX",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA005",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "ab779d50-6287-4aed-aa08-d86d6c79e400"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::UpdateFailure"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "UPDATING",
                    "host": {
                        "ip": "172.16.202.25"
                    },
                    "hostip": "172.16.202.25",
                    "hostip_assetid": "17c2d542-6eed-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.25",
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
                    "orig_id": "AfCX0Z8BI3UnQyDOvDLX",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T10:59:11.891Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bf905f57-844b-4bdd-b654-0dc957c6dc23",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "ab779d50-6287-4aed-aa08-d86d6c79e400",
                        "location": "CJPPA005",
                        "name": "Failed to install CRTSETUP: general error.",
                        "severity": "low",
                        "source": "CAJAANDE\\4806661",
                        "source_info": {
                            "ip": "172.16.202.25"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69935bcd1299ac27e9062fb5",
                        "when": "2026-08-05T10:59:11.885Z"
                    },
                    "stellar": {
                        "detection_time": 149763,
                        "status": "New"
                    },
                    "stellar_da_input": 1319,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "2d1857ce-8f0f-4660-91b8-7fdb777413f61785927959937-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785927551891,
                    "timestamp_utc": "2026-08-05T10:59:11.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\4806661"
                    },
                    "username": "CAJAANDE\\4806661",
                    "write_by": "sef",
                    "write_time": 1785927959937,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.25\", User Name of \"CAJAANDE\\4806661\".\nThe description of the event states that \"Failed to install CRTSETUP: general error.\"",
                        "display_name": "Sophos Event: Impair Defenses",
                        "framework_version": "v13",
                        "name": "sophos_event-defense_evasion-impair_defenses",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::UpdateFailure",
                            "name": "event_endpoint_updatefailure"
                        },
                        "tactic": {
                            "id": "TA0005",
                            "name": "Defense Evasion"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "T1562",
                            "name": "Impair Defenses"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1562",
                                    "name": "Impair Defenses"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "2fed60de-c8cb-4fc3-ba73-4f6d8ba9cd991785928198182-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 669,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "NPCc0Z8BI3UnQyDOUFfa",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA005",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "ab779d50-6287-4aed-aa08-d86d6c79e400"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::UpdateFailure"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "UPDATING",
                    "host": {
                        "ip": "172.16.202.25"
                    },
                    "hostip": "172.16.202.25",
                    "hostip_assetid": "17c2d542-6eed-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.25",
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
                    "orig_id": "NPCc0Z8BI3UnQyDOUFfa",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T10:59:11.891Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bf905f57-844b-4bdd-b654-0dc957c6dc23",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "ab779d50-6287-4aed-aa08-d86d6c79e400",
                        "location": "CJPPA005",
                        "name": "Failed to install CRTSETUP: general error.",
                        "severity": "low",
                        "source": "CAJAANDE\\4806661",
                        "source_info": {
                            "ip": "172.16.202.25"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69935bcd1299ac27e9062fb5",
                        "when": "2026-08-05T10:59:11.885Z"
                    },
                    "stellar": {
                        "detection_time": 87962,
                        "status": "New"
                    },
                    "stellar_da_input": 1319,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "2fed60de-c8cb-4fc3-ba73-4f6d8ba9cd991785928198182-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785927551891,
                    "timestamp_utc": "2026-08-05T10:59:11.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\4806661"
                    },
                    "username": "CAJAANDE\\4806661",
                    "write_by": "sef",
                    "write_time": 1785928198182,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.25\", User Name of \"CAJAANDE\\4806661\".\nThe description of the event states that \"Failed to install CRTSETUP: general error.\"",
                        "display_name": "Sophos Event: Impair Defenses",
                        "framework_version": "v13",
                        "name": "sophos_event-defense_evasion-impair_defenses",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::UpdateFailure",
                            "name": "event_endpoint_updatefailure"
                        },
                        "tactic": {
                            "id": "TA0005",
                            "name": "Defense Evasion"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "T1562",
                            "name": "Impair Defenses"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1562",
                                    "name": "Impair Defenses"
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