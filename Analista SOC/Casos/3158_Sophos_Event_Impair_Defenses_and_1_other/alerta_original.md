=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "2f1d6147-0a98-421a-bf70-2b468cc1e4d11784113071342-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 10984,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "sQRqZZ8BI3UnQyDOts6Q",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA006",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "a899b289-8686-4679-9bde-ccf4fd6a9ed9"
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
                        "ip": "172.16.202.26"
                    },
                    "hostip": "172.16.202.26",
                    "hostip_assetid": "abf4e6a2-6eec-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.26",
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
                    "orig_id": "sQRqZZ8BI3UnQyDOts6Q",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T10:52:53.899Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "e3b3beb9-9582-4556-b6fe-77a574af9dba",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "a899b289-8686-4679-9bde-ccf4fd6a9ed9",
                        "location": "CJPPA006",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\4806661",
                        "source_info": {
                            "ip": "172.16.202.26"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69935bcd1299ac27e9062fb5",
                        "when": "2026-07-15T10:52:53.877Z"
                    },
                    "stellar": {
                        "detection_time": 151179,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "2f1d6147-0a98-421a-bf70-2b468cc1e4d11784113071342-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784112773899,
                    "timestamp_utc": "2026-07-15T10:52:53.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\4806661"
                    },
                    "username": "CAJAANDE\\4806661",
                    "write_by": "sef",
                    "write_time": 1784113071342,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.26\", User Name of \"CAJAANDE\\4806661\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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
                "_id": "acd76181-b450-4582-8ad5-0d31ac7f7a251784113309615-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 10987,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "pgRvZZ8BI3UnQyDOcfy5",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA006",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "a899b289-8686-4679-9bde-ccf4fd6a9ed9"
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
                        "ip": "172.16.202.26"
                    },
                    "hostip": "172.16.202.26",
                    "hostip_assetid": "abf4e6a2-6eec-11f1-923e-5ae6db116d2f",
                    "hostip_host": "172.16.202.26",
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
                    "orig_id": "pgRvZZ8BI3UnQyDOcfy5",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T10:52:53.899Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "e3b3beb9-9582-4556-b6fe-77a574af9dba",
                        "endpoint_type": "computer",
                        "group": "UPDATING",
                        "id": "a899b289-8686-4679-9bde-ccf4fd6a9ed9",
                        "location": "CJPPA006",
                        "name": "Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.",
                        "severity": "low",
                        "source": "CAJAANDE\\4806661",
                        "source_info": {
                            "ip": "172.16.202.26"
                        },
                        "type": "Event::Endpoint::UpdateFailure",
                        "user_id": "69935bcd1299ac27e9062fb5",
                        "when": "2026-07-15T10:52:53.877Z"
                    },
                    "stellar": {
                        "detection_time": 79444,
                        "status": "New"
                    },
                    "stellar_da_input": 1571,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "acd76181-b450-4582-8ad5-0d31ac7f7a251784113309615-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784112773899,
                    "timestamp_utc": "2026-07-15T10:52:53.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\4806661"
                    },
                    "username": "CAJAANDE\\4806661",
                    "write_by": "sef",
                    "write_time": 1784113309615,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::UpdateFailure\", Host IP of \"172.16.202.26\", User Name of \"CAJAANDE\\4806661\".\nThe description of the event states that \"Failed to install UNINSTALLER64,SED64,MCS,SSE64,SFS64,SHS,UI64,AMSI64,SME64,ESH64,LIVETERMINAL64,EFW64,LiveQuery64,NTP64,SDU64,HMPA64,SAUXG: 80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00,80041f00.\"",
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