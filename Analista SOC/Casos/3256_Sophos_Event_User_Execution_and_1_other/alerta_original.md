=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "6c248713-79e7-492a-9e8d-188c3e6b1c001784898304989-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4900,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "i0k4lJ8BI3UnQyDOi_ap",
                    "appid_stdport": "yes",
                    "computer_name": "VMCTIC-01",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "b3747739-37f3-4e0d-95fc-a150f2ba79a1"
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
                        "ip": "172.16.202.211"
                    },
                    "hostip": "172.16.202.211",
                    "hostip_assetid": "7454b676-da6a-11f0-bee4-aa0456b9a54a",
                    "hostip_host": "172.16.202.211",
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
                    "orig_id": "i0k4lJ8BI3UnQyDOi_ap",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T13:00:37.081Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2939ebda-ae4f-4efe-a802-9fb76bb708f6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "b3747739-37f3-4e0d-95fc-a150f2ba79a1",
                        "location": "VMCTIC-01",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\CAJA53021",
                        "source_info": {
                            "ip": "172.16.202.211"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692725d8629ec142cd9dbf5a",
                        "when": "2026-07-24T13:00:01.000Z"
                    },
                    "stellar": {
                        "detection_time": 144403,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "6c248713-79e7-492a-9e8d-188c3e6b1c001784898304989-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784898037081,
                    "timestamp_utc": "2026-07-24T13:00:37.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\CAJA53021"
                    },
                    "username": "CAJAANDE\\CAJA53021",
                    "write_by": "sef",
                    "write_time": 1784898304989,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.211\", User Name of \"CAJAANDE\\CAJA53021\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "4f7290f3-debc-4342-80ef-5dc6cb4d1aab1784898543267-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4903,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "t0o9lJ8BI3UnQyDOHVEn",
                    "appid_stdport": "yes",
                    "computer_name": "VMCTIC-01",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "b3747739-37f3-4e0d-95fc-a150f2ba79a1"
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
                        "ip": "172.16.202.211"
                    },
                    "hostip": "172.16.202.211",
                    "hostip_assetid": "7454b676-da6a-11f0-bee4-aa0456b9a54a",
                    "hostip_host": "172.16.202.211",
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
                    "orig_id": "t0o9lJ8BI3UnQyDOHVEn",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T13:00:37.081Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2939ebda-ae4f-4efe-a802-9fb76bb708f6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "b3747739-37f3-4e0d-95fc-a150f2ba79a1",
                        "location": "VMCTIC-01",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\CAJA53021",
                        "source_info": {
                            "ip": "172.16.202.211"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "692725d8629ec142cd9dbf5a",
                        "when": "2026-07-24T13:00:01.000Z"
                    },
                    "stellar": {
                        "detection_time": 82838,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "4f7290f3-debc-4342-80ef-5dc6cb4d1aab1784898543267-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784898037081,
                    "timestamp_utc": "2026-07-24T13:00:37.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\CAJA53021"
                    },
                    "username": "CAJAANDE\\CAJA53021",
                    "write_by": "sef",
                    "write_time": 1784898543266,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.211\", User Name of \"CAJAANDE\\CAJA53021\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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