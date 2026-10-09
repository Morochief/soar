=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "de1a4003-aa78-4003-896e-7770895d7ffa1785925577429-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 655,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "O-9z0Z8BI3UnQyDOHRXd",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA026",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "b525daa4-5f45-435d-bf9e-0b52e659ce51"
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
                    "hostip_assetid": "c42c9296-68a3-11f1-ba15-5ae6db116d2f",
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
                    "orig_id": "O-9z0Z8BI3UnQyDOHRXd",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T10:22:17.534Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4c2634be-46d9-4e16-837f-2c7baa78221c",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "b525daa4-5f45-435d-bf9e-0b52e659ce51",
                        "location": "CJPPA026",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\Ktroche",
                        "source_info": {
                            "ip": "172.16.202.46"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "6932c09258fc555f47174077",
                        "when": "2026-08-05T10:22:17.510Z"
                    },
                    "stellar": {
                        "detection_time": 167257,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "de1a4003-aa78-4003-896e-7770895d7ffa1785925577429-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785925337534,
                    "timestamp_utc": "2026-08-05T10:22:17.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Ktroche"
                    },
                    "username": "CAJAANDE\\Ktroche",
                    "write_by": "sef",
                    "write_time": 1785925577429,
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "e360a3bd-78f1-4fd1-afcb-3b91b1ba99d31785925815675-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 656,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "mu930Z8BI3UnQyDOsTbK",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA026",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "b525daa4-5f45-435d-bf9e-0b52e659ce51"
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
                    "hostip_assetid": "c42c9296-68a3-11f1-ba15-5ae6db116d2f",
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
                    "orig_id": "mu930Z8BI3UnQyDOsTbK",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T10:22:17.534Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4c2634be-46d9-4e16-837f-2c7baa78221c",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "b525daa4-5f45-435d-bf9e-0b52e659ce51",
                        "location": "CJPPA026",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\Ktroche",
                        "source_info": {
                            "ip": "172.16.202.46"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "6932c09258fc555f47174077",
                        "when": "2026-08-05T10:22:17.510Z"
                    },
                    "stellar": {
                        "detection_time": 105499,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e360a3bd-78f1-4fd1-afcb-3b91b1ba99d31785925815675-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785925337534,
                    "timestamp_utc": "2026-08-05T10:22:17.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\Ktroche"
                    },
                    "username": "CAJAANDE\\Ktroche",
                    "write_by": "sef",
                    "write_time": 1785925815675,
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