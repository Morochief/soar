=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "6e73ea0f-a789-4962-8b83-8ffbe64028a11784720116877-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2192,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "MbyaiZ8BI3UnQyDOoRnP",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA040",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "3b56ad71-0692-452d-bad9-a3f7064e1b00"
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
                        "ip": "172.16.202.60"
                    },
                    "hostip": "172.16.202.60",
                    "hostip_assetid": "2986129a-7941-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.60",
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
                    "orig_id": "MbyaiZ8BI3UnQyDOoRnP",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-22T11:30:31.724Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2d3ab4fe-1e57-4f38-801d-54ba45018aa7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "3b56ad71-0692-452d-bad9-a3f7064e1b00",
                        "location": "CJPPA040",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\benitez.sege",
                        "source_info": {
                            "ip": "172.16.202.60"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6932d09772291113e7f8ccfc",
                        "when": "2026-07-22T11:29:58.000Z"
                    },
                    "stellar": {
                        "detection_time": 76638,
                        "status": "New"
                    },
                    "stellar_da_input": 1372,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "6e73ea0f-a789-4962-8b83-8ffbe64028a11784720116877-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784719831724,
                    "timestamp_utc": "2026-07-22T11:30:31.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\benitez.sege"
                    },
                    "username": "CAJAANDE\\benitez.sege",
                    "write_by": "sef",
                    "write_time": 1784720116877,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.60\", User Name of \"CAJAANDE\\benitez.sege\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "e3b7aefe-94c5-485d-9ca1-c24682e7e1121784720474206-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2196,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "FryfiZ8BI3UnQyDOW1Cs",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA040",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "3b56ad71-0692-452d-bad9-a3f7064e1b00"
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
                        "ip": "172.16.202.60"
                    },
                    "hostip": "172.16.202.60",
                    "hostip_assetid": "2986129a-7941-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.60",
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
                    "orig_id": "FryfiZ8BI3UnQyDOW1Cs",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-22T11:30:31.724Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2d3ab4fe-1e57-4f38-801d-54ba45018aa7",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "3b56ad71-0692-452d-bad9-a3f7064e1b00",
                        "location": "CJPPA040",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\benitez.sege",
                        "source_info": {
                            "ip": "172.16.202.60"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6932d09772291113e7f8ccfc",
                        "when": "2026-07-22T11:29:58.000Z"
                    },
                    "stellar": {
                        "detection_time": 124115,
                        "status": "New"
                    },
                    "stellar_da_input": 1372,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e3b7aefe-94c5-485d-9ca1-c24682e7e1121784720474206-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784719831724,
                    "timestamp_utc": "2026-07-22T11:30:31.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\benitez.sege"
                    },
                    "username": "CAJAANDE\\benitez.sege",
                    "write_by": "sef",
                    "write_time": 1784720474206,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.60\", User Name of \"CAJAANDE\\benitez.sege\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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