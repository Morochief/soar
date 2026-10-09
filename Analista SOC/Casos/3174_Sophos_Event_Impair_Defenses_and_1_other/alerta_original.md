=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "1ad4be1b-72f5-428a-99a9-7de71b1ee1891784201937017-YWVsbGEtc2VyLTIwMjYuMDcuMTYtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11820,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "_1K2ap8BI3UnQyDOTl0y",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA026",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "40a5ab0f-340d-4136-ad78-f62c3c156418"
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
                        "ip": "172.16.202.46"
                    },
                    "hostip": "172.16.202.46",
                    "hostip_host": "172.16.202.46",
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
                    "orig_id": "_1K2ap8BI3UnQyDOTl0y",
                    "orig_index": "aella-syslog-2026.07.16-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-16T11:32:44.781Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4c2634be-46d9-4e16-837f-2c7baa78221c",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "40a5ab0f-340d-4136-ad78-f62c3c156418",
                        "location": "CJPPA026",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\Ktroche",
                        "source_info": {
                            "ip": "172.16.202.46"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "6932c09258fc555f47174077",
                        "when": "2026-07-16T11:32:44.759Z"
                    },
                    "stellar": {
                        "detection_time": 176848,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.07.16-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "1ad4be1b-72f5-428a-99a9-7de71b1ee1891784201937017-YWVsbGEtc2VyLTIwMjYuMDcuMTYtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784201564781,
                    "timestamp_utc": "2026-07-16T11:32:44.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Ktroche"
                    },
                    "username": "CAJAANDE\\Ktroche",
                    "write_by": "sef",
                    "write_time": 1784201937017,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.46\", User Name of \"CAJAANDE\\Ktroche\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "875bf088-79f4-4420-b0fe-801428d0f4fe1784202175249-YWVsbGEtc2VyLTIwMjYuMDcuMTYtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11827,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "W1K6ap8BI3UnQyDO4Zvp",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA026",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "40a5ab0f-340d-4136-ad78-f62c3c156418"
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
                        "ip": "172.16.202.46"
                    },
                    "hostip": "172.16.202.46",
                    "hostip_host": "172.16.202.46",
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
                    "orig_id": "W1K6ap8BI3UnQyDO4Zvp",
                    "orig_index": "aella-syslog-2026.07.16-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-16T11:32:44.781Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4c2634be-46d9-4e16-837f-2c7baa78221c",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "40a5ab0f-340d-4136-ad78-f62c3c156418",
                        "location": "CJPPA026",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\Ktroche",
                        "source_info": {
                            "ip": "172.16.202.46"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "6932c09258fc555f47174077",
                        "when": "2026-07-16T11:32:44.759Z"
                    },
                    "stellar": {
                        "detection_time": 115060,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.07.16-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "875bf088-79f4-4420-b0fe-801428d0f4fe1784202175249-YWVsbGEtc2VyLTIwMjYuMDcuMTYtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784201564781,
                    "timestamp_utc": "2026-07-16T11:32:44.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Ktroche"
                    },
                    "username": "CAJAANDE\\Ktroche",
                    "write_by": "sef",
                    "write_time": 1784202175249,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.46\", User Name of \"CAJAANDE\\Ktroche\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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