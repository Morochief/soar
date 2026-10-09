=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "f0754e3b-ea00-433c-bd52-83743ea4d1f11784112118358-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 10949,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "zQRdZZ8BI3UnQyDOIk4D",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA014",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "7ec832ac-f45b-4878-830e-ab0869b1d842"
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
                        "ip": "172.16.202.34"
                    },
                    "hostip": "172.16.202.34",
                    "hostip_assetid": "9bc29af0-696e-11f1-ba15-5ae6db116d2f",
                    "hostip_host": "172.16.202.34",
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
                    "orig_id": "zQRdZZ8BI3UnQyDOIk4D",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T10:36:07.986Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "e66ea0b2-f54e-4266-a4f9-027fb0a7402f",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "7ec832ac-f45b-4878-830e-ab0869b1d842",
                        "location": "CJPPA014",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\dlopez",
                        "source_info": {
                            "ip": "172.16.202.34"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69394908a86a82641d1dade4",
                        "when": "2026-07-15T10:36:07.961Z"
                    },
                    "stellar": {
                        "detection_time": 88176,
                        "status": "New"
                    },
                    "stellar_da_input": 1568,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "f0754e3b-ea00-433c-bd52-83743ea4d1f11784112118358-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784111767986,
                    "timestamp_utc": "2026-07-15T10:36:07.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\dlopez"
                    },
                    "username": "CAJAANDE\\dlopez",
                    "write_by": "sef",
                    "write_time": 1784112118358,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.34\", User Name of \"CAJAANDE\\dlopez\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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
                "_id": "0add6e83-8a1b-42f2-8534-e6d13af3e29e1784112475741-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 10979,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YQRhZZ8BI3UnQyDOj3co",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA014",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "7ec832ac-f45b-4878-830e-ab0869b1d842"
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
                        "ip": "172.16.202.34"
                    },
                    "hostip": "172.16.202.34",
                    "hostip_assetid": "9bc29af0-696e-11f1-ba15-5ae6db116d2f",
                    "hostip_host": "172.16.202.34",
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
                    "orig_id": "YQRhZZ8BI3UnQyDOj3co",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T10:36:07.986Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "e66ea0b2-f54e-4266-a4f9-027fb0a7402f",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "7ec832ac-f45b-4878-830e-ab0869b1d842",
                        "location": "CJPPA014",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\dlopez",
                        "source_info": {
                            "ip": "172.16.202.34"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69394908a86a82641d1dade4",
                        "when": "2026-07-15T10:36:07.961Z"
                    },
                    "stellar": {
                        "detection_time": 155530,
                        "status": "New"
                    },
                    "stellar_da_input": 1568,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "0add6e83-8a1b-42f2-8534-e6d13af3e29e1784112475741-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784111767986,
                    "timestamp_utc": "2026-07-15T10:36:07.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\dlopez"
                    },
                    "username": "CAJAANDE\\dlopez",
                    "write_by": "sef",
                    "write_time": 1784112475741,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.34\", User Name of \"CAJAANDE\\dlopez\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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