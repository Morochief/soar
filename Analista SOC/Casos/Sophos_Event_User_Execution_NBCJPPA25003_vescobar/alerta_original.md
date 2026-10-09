{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "6869922e-49e3-4309-9689-282610e8c6391788445122843-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 26515,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "9kyhZ6ABI3UnQyDO5QOo",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25003",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "14521ad6-c2e1-4319-bc95-183515510065"
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
                        "ip": "172.16.202.21"
                    },
                    "hostip": "172.16.202.21",
                    "hostip_assetid": "c2af3dc2-a031-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.21",
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
                    "orig_id": "9kyhZ6ABI3UnQyDO5QOo",
                    "orig_index": "aella-syslog-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-03T14:17:11.424Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "96ca5a99-a370-4426-80df-4be7391472c4",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "14521ad6-c2e1-4319-bc95-183515510065",
                        "location": "NBCJPPA25003",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\vescobar",
                        "source_info": {
                            "ip": "172.16.202.21"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926ff53e598016d827c8ad4",
                        "when": "2026-09-03T14:16:55.000Z"
                    },
                    "stellar": {
                        "detection_time": 64466,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "6869922e-49e3-4309-9689-282610e8c6391788445122843-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1788445031424,
                    "timestamp_utc": "2026-09-03T14:17:11.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\vescobar"
                    },
                    "username": "CAJAANDE\\vescobar",
                    "write_by": "sef",
                    "write_time": 1788445122843,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.21\", User Name of \"CAJAANDE\\vescobar\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "c342cf40-3902-4ffa-8cf3-9b1d5c48fb331788445480148-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 26518,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "gkymZ6ABI3UnQyDOeXQx",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25003",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "14521ad6-c2e1-4319-bc95-183515510065"
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
                        "ip": "172.16.202.21"
                    },
                    "hostip": "172.16.202.21",
                    "hostip_assetid": "c2af3dc2-a031-11f1-9514-8e57707220c4",
                    "hostip_host": "172.16.202.21",
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
                    "orig_id": "gkymZ6ABI3UnQyDOeXQx",
                    "orig_index": "aella-syslog-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-09-03T14:17:11.424Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "96ca5a99-a370-4426-80df-4be7391472c4",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "14521ad6-c2e1-4319-bc95-183515510065",
                        "location": "NBCJPPA25003",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\vescobar",
                        "source_info": {
                            "ip": "172.16.202.21"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6926ff53e598016d827c8ad4",
                        "when": "2026-09-03T14:16:55.000Z"
                    },
                    "stellar": {
                        "detection_time": 121825,
                        "status": "New"
                    },
                    "stellar_da_input": 1368,
                    "stellar_index_id": "aella-ser-2026.09.03-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "c342cf40-3902-4ffa-8cf3-9b1d5c48fb331788445480148-YWVsbGEtc2VyLTIwMjYuMDkuMDMtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1788445031424,
                    "timestamp_utc": "2026-09-03T14:17:11.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\vescobar"
                    },
                    "username": "CAJAANDE\\vescobar",
                    "write_by": "sef",
                    "write_time": 1788445480148,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.21\", User Name of \"CAJAANDE\\vescobar\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
