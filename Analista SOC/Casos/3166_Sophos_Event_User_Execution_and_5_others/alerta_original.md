=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "421fc56a-821e-4a59-9794-326b1d45dc281784129272846-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11146,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "ehliZp8BI3UnQyDOGDU_",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "3a04c8f8-1f80-45a5-b48f-7f24e8d21989"
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
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "ehliZp8BI3UnQyDOGDU_",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:24:52.309Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "3a04c8f8-1f80-45a5-b48f-7f24e8d21989",
                        "location": "CJPPA036",
                        "name": "'https://llvpn.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:24:23.000Z"
                    },
                    "stellar": {
                        "detection_time": 141438,
                        "status": "New"
                    },
                    "stellar_da_input": 1352,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "421fc56a-821e-4a59-9794-326b1d45dc281784129272846-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129092309,
                    "timestamp_utc": "2026-07-15T15:24:52.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129272846,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"'https://llvpn.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6d503ab5-2559-4246-b5e4-b3060b0578101784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11152,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "cxlmZp8BI3UnQyDOqZ_E",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "3a04c8f8-1f80-45a5-b48f-7f24e8d21989"
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
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "cxlmZp8BI3UnQyDOqZ_E",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:24:52.309Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "3a04c8f8-1f80-45a5-b48f-7f24e8d21989",
                        "location": "CJPPA036",
                        "name": "'https://llvpn.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:24:23.000Z"
                    },
                    "stellar": {
                        "detection_time": 80180,
                        "status": "New"
                    },
                    "stellar_da_input": 1352,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "6d503ab5-2559-4246-b5e4-b3060b0578101784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129092309,
                    "timestamp_utc": "2026-07-15T15:24:52.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129511134,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"'https://llvpn.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "65472eda-9d2f-4ba0-a170-1785c2eda7f21784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11153,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "dBlmZp8BI3UnQyDOqZ_E",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "0f1ff151-5688-4ec0-9335-c96af4c768fa"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::WebFilteringBlocked"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "WEB",
                    "host": {
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "dBlmZp8BI3UnQyDOqZ_E",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:25:26.264Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "0f1ff151-5688-4ec0-9335-c96af4c768fa",
                        "location": "CJPPA036",
                        "name": "Access was blocked to \"tiktokshopping.xyz\" because of \"Mal/HTMLGen-A\".",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebFilteringBlocked",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:24:57.000Z"
                    },
                    "stellar": {
                        "detection_time": 80186,
                        "status": "New"
                    },
                    "stellar_da_input": 1359,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "65472eda-9d2f-4ba0-a170-1785c2eda7f21784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129126264,
                    "timestamp_utc": "2026-07-15T15:25:26.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129511134,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebFilteringBlocked\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"Access was blocked to \"tiktokshopping.xyz\" because of \"Mal/HTMLGen-A\".\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::WebFilteringBlocked",
                            "name": "event_endpoint_webfilteringblocked"
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "9b8e13fb-cfbe-4bcf-a429-02ef618b76411784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11155,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "dxlmZp8BI3UnQyDOqZ_E",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "0894bb2a-e4ea-4d9b-8109-d15d0d86ba25"
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
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "dxlmZp8BI3UnQyDOqZ_E",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:26:13.291Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "0894bb2a-e4ea-4d9b-8109-d15d0d86ba25",
                        "location": "CJPPA036",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:25:44.000Z"
                    },
                    "stellar": {
                        "detection_time": 80194,
                        "status": "New"
                    },
                    "stellar_da_input": 1363,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "9b8e13fb-cfbe-4bcf-a429-02ef618b76411784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129173291,
                    "timestamp_utc": "2026-07-15T15:26:13.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129511134,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "84f47863-d346-492c-8bda-3f6cf17b3c541784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11156,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "eRlmZp8BI3UnQyDOqZ_E",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "557988ee-b911-4553-958e-23fcd64a59d0"
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
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "eRlmZp8BI3UnQyDOqZ_E",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:27:02.252Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "557988ee-b911-4553-958e-23fcd64a59d0",
                        "location": "CJPPA036",
                        "name": "'https://addressimpertinenceclockwise.com' blocked due to category 'Spam URLs'",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:26:32.000Z"
                    },
                    "stellar": {
                        "detection_time": 80200,
                        "status": "New"
                    },
                    "stellar_da_input": 1363,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "84f47863-d346-492c-8bda-3f6cf17b3c541784129511134-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129222252,
                    "timestamp_utc": "2026-07-15T15:27:02.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129511134,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"'https://addressimpertinenceclockwise.com' blocked due to category 'Spam URLs'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "f9a5c4ab-09e6-4447-876c-19533bf0b0491784129511136-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 11154,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "exlmZp8BI3UnQyDOqZ_E",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA036",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "4be0e097-4a3e-4645-8faa-106ef7b00afe"
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
                        "ip": "172.16.202.56"
                    },
                    "hostip": "172.16.202.56",
                    "hostip_assetid": "8b4cfe64-7949-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.56",
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
                    "orig_id": "exlmZp8BI3UnQyDOqZ_E",
                    "orig_index": "aella-syslog-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-15T15:28:15.266Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "4a2a8252-f179-4cdb-8847-1a53875959b3",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "4be0e097-4a3e-4645-8faa-106ef7b00afe",
                        "location": "CJPPA036",
                        "name": "'https://corsproxy.io' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\egonzalez",
                        "source_info": {
                            "ip": "172.16.202.56"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692706d953107e08b0f2fa6b",
                        "when": "2026-07-15T15:27:46.000Z"
                    },
                    "stellar": {
                        "detection_time": 80215,
                        "status": "New"
                    },
                    "stellar_da_input": 1355,
                    "stellar_index_id": "aella-ser-2026.07.15-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "f9a5c4ab-09e6-4447-876c-19533bf0b0491784129511136-YWVsbGEtc2VyLTIwMjYuMDcuMTUtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784129295266,
                    "timestamp_utc": "2026-07-15T15:28:15.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\egonzalez"
                    },
                    "username": "CAJAANDE\\egonzalez",
                    "write_by": "sef",
                    "write_time": 1784129511136,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.56\", User Name of \"CAJAANDE\\egonzalez\".\nThe description of the event states that \"'https://corsproxy.io' blocked due to category 'Proxies & Translators'\"",
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