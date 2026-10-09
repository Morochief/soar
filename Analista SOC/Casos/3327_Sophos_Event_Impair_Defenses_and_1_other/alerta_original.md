=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "c21bd528-0da2-44fa-a2ca-ff1944f91a331785500326866-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 13430,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "k9gauJ8BI3UnQyDOUGu6",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA034",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "6acabb71-b9ed-4ddc-a667-1f5124aac1bd"
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
                        "ip": "172.16.202.54"
                    },
                    "hostip": "172.16.202.54",
                    "hostip_assetid": "c4717e46-6eee-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.54",
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
                    "orig_id": "k9gauJ8BI3UnQyDOUGu6",
                    "orig_index": "aella-syslog-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-31T12:12:08.663Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "41723887-6d20-4ea3-bead-8d8d14c3e8cb",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "6acabb71-b9ed-4ddc-a667-1f5124aac1bd",
                        "location": "CJPPA034",
                        "name": "Failed to install CRTSETUP: general error.",
                        "severity": "low",
                        "source": "CAJAANDE\\jdiaz",
                        "source_info": {
                            "ip": "172.16.202.54"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69397a8ae598016d827c95d6",
                        "when": "2026-07-31T12:12:08.645Z"
                    },
                    "stellar": {
                        "detection_time": 166751,
                        "status": "New"
                    },
                    "stellar_da_input": 1313,
                    "stellar_index_id": "aella-ser-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "c21bd528-0da2-44fa-a2ca-ff1944f91a331785500326866-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785499928663,
                    "timestamp_utc": "2026-07-31T12:12:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jdiaz"
                    },
                    "username": "CAJAANDE\\jdiaz",
                    "write_by": "sef",
                    "write_time": 1785500326866,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.54\", User Name of \"CAJAANDE\\jdiaz\".\nThe description of the event states that \"Failed to install CRTSETUP: general error.\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "5a47c712-c632-4b70-b3d1-96e1c2d60bc61785500565127-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 13435,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "0NgeuJ8BI3UnQyDO5cdR",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA034",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "6acabb71-b9ed-4ddc-a667-1f5124aac1bd"
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
                        "ip": "172.16.202.54"
                    },
                    "hostip": "172.16.202.54",
                    "hostip_assetid": "c4717e46-6eee-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.54",
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
                    "orig_id": "0NgeuJ8BI3UnQyDO5cdR",
                    "orig_index": "aella-syslog-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-31T12:12:08.663Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "41723887-6d20-4ea3-bead-8d8d14c3e8cb",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "6acabb71-b9ed-4ddc-a667-1f5124aac1bd",
                        "location": "CJPPA034",
                        "name": "Failed to install CRTSETUP: general error.",
                        "severity": "low",
                        "source": "CAJAANDE\\jdiaz",
                        "source_info": {
                            "ip": "172.16.202.54"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69397a8ae598016d827c95d6",
                        "when": "2026-07-31T12:12:08.645Z"
                    },
                    "stellar": {
                        "detection_time": 104922,
                        "status": "New"
                    },
                    "stellar_da_input": 1313,
                    "stellar_index_id": "aella-ser-2026.07.31-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "5a47c712-c632-4b70-b3d1-96e1c2d60bc61785500565127-YWVsbGEtc2VyLTIwMjYuMDcuMzEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785499928663,
                    "timestamp_utc": "2026-07-31T12:12:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jdiaz"
                    },
                    "username": "CAJAANDE\\jdiaz",
                    "write_by": "sef",
                    "write_time": 1785500565127,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.54\", User Name of \"CAJAANDE\\jdiaz\".\nThe description of the event states that \"Failed to install CRTSETUP: general error.\"",
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