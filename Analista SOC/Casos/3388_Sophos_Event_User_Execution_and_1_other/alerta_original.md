=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "50b403e9-9de8-4804-869c-5552c850d08e1785928793795-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 673,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "TPCl0Z8BI3UnQyDOeK-M",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA011",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "da4ee3de-f234-453b-a9a3-6f5a3f1a614d"
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
                        "ip": "172.16.202.31"
                    },
                    "hostip": "172.16.202.31",
                    "hostip_assetid": "9125e798-8424-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.31",
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
                    "orig_id": "TPCl0Z8BI3UnQyDOeK-M",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T11:17:22.130Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "5be63215-b68a-46ec-b8b1-c14bdb638eb3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "da4ee3de-f234-453b-a9a3-6f5a3f1a614d",
                        "location": "CJPPA011",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\demiguel",
                        "source_info": {
                            "ip": "172.16.202.31"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fed561055368e6696c5e",
                        "when": "2026-08-05T11:16:40.000Z"
                    },
                    "stellar": {
                        "detection_time": 83631,
                        "status": "New"
                    },
                    "stellar_da_input": 1360,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "50b403e9-9de8-4804-869c-5552c850d08e1785928793795-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785928642130,
                    "timestamp_utc": "2026-08-05T11:17:22.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\demiguel"
                    },
                    "username": "CAJAANDE\\demiguel",
                    "write_by": "sef",
                    "write_time": 1785928793795,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.31\", User Name of \"CAJAANDE\\demiguel\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "cb46b427-4b08-4589-9d77-22ab7864675e1785929151130-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 682,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "TvCq0Z8BI3UnQyDODNd_",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA011",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "da4ee3de-f234-453b-a9a3-6f5a3f1a614d"
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
                        "ip": "172.16.202.31"
                    },
                    "hostip": "172.16.202.31",
                    "hostip_assetid": "9125e798-8424-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.31",
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
                    "orig_id": "TvCq0Z8BI3UnQyDODNd_",
                    "orig_index": "aella-syslog-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-05T11:17:22.130Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "5be63215-b68a-46ec-b8b1-c14bdb638eb3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "da4ee3de-f234-453b-a9a3-6f5a3f1a614d",
                        "location": "CJPPA011",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\demiguel",
                        "source_info": {
                            "ip": "172.16.202.31"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fed561055368e6696c5e",
                        "when": "2026-08-05T11:16:40.000Z"
                    },
                    "stellar": {
                        "detection_time": 140949,
                        "status": "New"
                    },
                    "stellar_da_input": 1360,
                    "stellar_index_id": "aella-ser-2026.08.05-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "cb46b427-4b08-4589-9d77-22ab7864675e1785929151130-YWVsbGEtc2VyLTIwMjYuMDguMDUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1785928642130,
                    "timestamp_utc": "2026-08-05T11:17:22.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\demiguel"
                    },
                    "username": "CAJAANDE\\demiguel",
                    "write_by": "sef",
                    "write_time": 1785929151129,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.31\", User Name of \"CAJAANDE\\demiguel\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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