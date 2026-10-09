=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "4c127f6b-6442-43b9-afa1-07802fbb6e281786103776245-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4605,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "WYQT3J8BI3UnQyDOJrkJ",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25008",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "0bbffcdd-79ef-4ddf-84d3-f89093860ae1"
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
                        "ip": "172.16.202.66"
                    },
                    "hostip": "172.16.202.66",
                    "hostip_assetid": "60640008-8420-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.66",
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
                    "orig_id": "WYQT3J8BI3UnQyDOJrkJ",
                    "orig_index": "aella-syslog-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-07T11:52:30.713Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "180014ff-238d-4cba-956d-dcaa9e12a2ee",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "0bbffcdd-79ef-4ddf-84d3-f89093860ae1",
                        "location": "NBCJPPA25008",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\caja53024",
                        "source_info": {
                            "ip": "172.16.202.66"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fdaa53107e08b0f2fa5d",
                        "when": "2026-08-07T11:51:46.000Z"
                    },
                    "stellar": {
                        "detection_time": 106087,
                        "status": "New"
                    },
                    "stellar_da_input": 1371,
                    "stellar_index_id": "aella-ser-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "4c127f6b-6442-43b9-afa1-07802fbb6e281786103776245-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1786103550713,
                    "timestamp_utc": "2026-08-07T11:52:30.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\caja53024"
                    },
                    "username": "CAJAANDE\\caja53024",
                    "write_by": "sef",
                    "write_time": 1786103776245,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.66\", User Name of \"CAJAANDE\\caja53024\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "ae5f0e65-94dd-4f1d-b18e-175eaead8d8c1786103776245-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4606,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "W4QT3J8BI3UnQyDOJrkJ",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25008",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "1ef637dd-c637-4acb-8606-f85ecd9790a3"
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
                        "ip": "172.16.202.66"
                    },
                    "hostip": "172.16.202.66",
                    "hostip_assetid": "60640008-8420-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.66",
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
                    "orig_id": "W4QT3J8BI3UnQyDOJrkJ",
                    "orig_index": "aella-syslog-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-07T11:53:19.723Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "180014ff-238d-4cba-956d-dcaa9e12a2ee",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "1ef637dd-c637-4acb-8606-f85ecd9790a3",
                        "location": "NBCJPPA25008",
                        "name": "'https://www-reddit-com.translate.goog' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\caja53024",
                        "source_info": {
                            "ip": "172.16.202.66"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fdaa53107e08b0f2fa5d",
                        "when": "2026-08-07T11:52:36.000Z"
                    },
                    "stellar": {
                        "detection_time": 106093,
                        "status": "New"
                    },
                    "stellar_da_input": 1380,
                    "stellar_index_id": "aella-ser-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "ae5f0e65-94dd-4f1d-b18e-175eaead8d8c1786103776245-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1786103599723,
                    "timestamp_utc": "2026-08-07T11:53:19.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\caja53024"
                    },
                    "username": "CAJAANDE\\caja53024",
                    "write_by": "sef",
                    "write_time": 1786103776245,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.66\", User Name of \"CAJAANDE\\caja53024\".\nThe description of the event states that \"'https://www-reddit-com.translate.goog' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "3158943a-1f95-4912-bd60-58736cb08ba71786104133597-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4611,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "gYQX3J8BI3UnQyDOufVF",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25008",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "0bbffcdd-79ef-4ddf-84d3-f89093860ae1"
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
                        "ip": "172.16.202.66"
                    },
                    "hostip": "172.16.202.66",
                    "hostip_assetid": "60640008-8420-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.66",
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
                    "orig_id": "gYQX3J8BI3UnQyDOufVF",
                    "orig_index": "aella-syslog-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-07T11:52:30.713Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "180014ff-238d-4cba-956d-dcaa9e12a2ee",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "0bbffcdd-79ef-4ddf-84d3-f89093860ae1",
                        "location": "NBCJPPA25008",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\caja53024",
                        "source_info": {
                            "ip": "172.16.202.66"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fdaa53107e08b0f2fa5d",
                        "when": "2026-08-07T11:51:46.000Z"
                    },
                    "stellar": {
                        "detection_time": 163511,
                        "status": "New"
                    },
                    "stellar_da_input": 1371,
                    "stellar_index_id": "aella-ser-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "3158943a-1f95-4912-bd60-58736cb08ba71786104133597-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1786103550713,
                    "timestamp_utc": "2026-08-07T11:52:30.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\caja53024"
                    },
                    "username": "CAJAANDE\\caja53024",
                    "write_by": "sef",
                    "write_time": 1786104133597,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.66\", User Name of \"CAJAANDE\\caja53024\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "b448841e-ad82-477a-97aa-6f507bb53ca11786104133597-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4612,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "g4QX3J8BI3UnQyDOufVF",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25008",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "1ef637dd-c637-4acb-8606-f85ecd9790a3"
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
                        "ip": "172.16.202.66"
                    },
                    "hostip": "172.16.202.66",
                    "hostip_assetid": "60640008-8420-11f1-8b6c-36d860317dc9",
                    "hostip_host": "172.16.202.66",
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
                    "orig_id": "g4QX3J8BI3UnQyDOufVF",
                    "orig_index": "aella-syslog-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-08-07T11:53:19.723Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "180014ff-238d-4cba-956d-dcaa9e12a2ee",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "1ef637dd-c637-4acb-8606-f85ecd9790a3",
                        "location": "NBCJPPA25008",
                        "name": "'https://www-reddit-com.translate.goog' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\caja53024",
                        "source_info": {
                            "ip": "172.16.202.66"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926fdaa53107e08b0f2fa5d",
                        "when": "2026-08-07T11:52:36.000Z"
                    },
                    "stellar": {
                        "detection_time": 163517,
                        "status": "New"
                    },
                    "stellar_da_input": 1380,
                    "stellar_index_id": "aella-ser-2026.08.07-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "b448841e-ad82-477a-97aa-6f507bb53ca11786104133597-YWVsbGEtc2VyLTIwMjYuMDguMDctMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1786103599723,
                    "timestamp_utc": "2026-08-07T11:53:19.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\caja53024"
                    },
                    "username": "CAJAANDE\\caja53024",
                    "write_by": "sef",
                    "write_time": 1786104133597,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.66\", User Name of \"CAJAANDE\\caja53024\".\nThe description of the event states that \"'https://www-reddit-com.translate.goog' blocked due to category 'Proxies & Translators'\"",
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