=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "b94f5454-7bb7-4c49-b586-939561be0c001784717496076-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2135,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "1rpxiZ8BI3UnQyDOba3V",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "90e85ff2-ef4c-4aa7-a523-a2c8d8bd0686"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "1rpxiZ8BI3UnQyDOba3V",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:48:41.862Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "90e85ff2-ef4c-4aa7-a523-a2c8d8bd0686",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:08.388Z"
                    },
                    "stellar": {
                        "detection_time": 155973,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "b94f5454-7bb7-4c49-b586-939561be0c001784717496076-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717321862,
                    "timestamp_utc": "2026-07-22T10:48:41.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717496076,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "e57601f7-ee48-4f39-88e9-049881516c5b1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2139,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "PLp2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "90e85ff2-ef4c-4aa7-a523-a2c8d8bd0686"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "PLp2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:48:41.862Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "90e85ff2-ef4c-4aa7-a523-a2c8d8bd0686",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:08.388Z"
                    },
                    "stellar": {
                        "detection_time": 94227,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e57601f7-ee48-4f39-88e9-049881516c5b1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717321862,
                    "timestamp_utc": "2026-07-22T10:48:41.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "ac08ad6c-cfc4-40dd-87b0-c3ce2b13a96b1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2140,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Pbp2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "25c0236c-04de-47e0-a61c-efe4a9de8e0d"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "Pbp2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:49:08.203Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "25c0236c-04de-47e0-a61c-efe4a9de8e0d",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:33.597Z"
                    },
                    "stellar": {
                        "detection_time": 94233,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "ac08ad6c-cfc4-40dd-87b0-c3ce2b13a96b1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717348203,
                    "timestamp_utc": "2026-07-22T10:49:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "e73e02fe-f1d2-421c-a64d-03f2d02f7e961784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2141,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Prp2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "efeb0b3b-fc1a-4b80-b84b-f400bbe5209d"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "Prp2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:13.438Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "efeb0b3b-fc1a-4b80-b84b-f400bbe5209d",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:35.159Z"
                    },
                    "stellar": {
                        "detection_time": 94235,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e73e02fe-f1d2-421c-a64d-03f2d02f7e961784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717353438,
                    "timestamp_utc": "2026-07-22T10:49:13.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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
                "_id": "83005707-8d6e-4146-b504-43cd755b11431784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2142,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "P7p2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "93038666-8417-44f2-a4a0-0ebc2255ce1a"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "P7p2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:21.860Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "93038666-8417-44f2-a4a0-0ebc2255ce1a",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:48.301Z"
                    },
                    "stellar": {
                        "detection_time": 94239,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "83005707-8d6e-4146-b504-43cd755b11431784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717361860,
                    "timestamp_utc": "2026-07-22T10:49:21.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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
                "_id": "9bb32605-77aa-4ff3-98e3-e75b3288b1b41784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2143,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "QLp2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "34d10c3b-d962-49da-ba99-b60e41f8c5e4"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "QLp2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:49:32.870Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "34d10c3b-d962-49da-ba99-b60e41f8c5e4",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:59.956Z"
                    },
                    "stellar": {
                        "detection_time": 94245,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "9bb32605-77aa-4ff3-98e3-e75b3288b1b41784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717372870,
                    "timestamp_utc": "2026-07-22T10:49:32.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "e386b427-3d42-4b7f-9379-a10e7c7df61d1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2144,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Qbp2iZ8BI3UnQyDOAdK3",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "4c1f2aac-b55d-428c-ab58-f5e08694a50e"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "Qbp2iZ8BI3UnQyDOAdK3",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:45.868Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "4c1f2aac-b55d-428c-ab58-f5e08694a50e",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:49:12.609Z"
                    },
                    "stellar": {
                        "detection_time": 94248,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "e386b427-3d42-4b7f-9379-a10e7c7df61d1784717734356-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717385868,
                    "timestamp_utc": "2026-07-22T10:49:45.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784717734356,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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
                "_id": "bd3d928c-1688-4940-905f-3b46171e7a961784718091709-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2149,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "ebp6iZ8BI3UnQyDOlvQ1",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "25c0236c-04de-47e0-a61c-efe4a9de8e0d"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "ebp6iZ8BI3UnQyDOlvQ1",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:49:08.203Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "25c0236c-04de-47e0-a61c-efe4a9de8e0d",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:33.597Z"
                    },
                    "stellar": {
                        "detection_time": 151527,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "bd3d928c-1688-4940-905f-3b46171e7a961784718091709-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717348203,
                    "timestamp_utc": "2026-07-22T10:49:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784718091709,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "65d245d8-4bb8-4eef-a958-4714b544e3601784718091719-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2150,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "erp6iZ8BI3UnQyDOlvQ1",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "efeb0b3b-fc1a-4b80-b84b-f400bbe5209d"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "erp6iZ8BI3UnQyDOlvQ1",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:13.438Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "efeb0b3b-fc1a-4b80-b84b-f400bbe5209d",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:35.159Z"
                    },
                    "stellar": {
                        "detection_time": 151532,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "65d245d8-4bb8-4eef-a958-4714b544e3601784718091719-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717353438,
                    "timestamp_utc": "2026-07-22T10:49:13.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784718091719,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nse64DC.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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
                "_id": "a84a9d9a-076f-42fb-9487-9f13ca1968411784718091719-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2151,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "e7p6iZ8BI3UnQyDOlvQ1",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "93038666-8417-44f2-a4a0-0ebc2255ce1a"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "e7p6iZ8BI3UnQyDOlvQ1",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:21.860Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "93038666-8417-44f2-a4a0-0ebc2255ce1a",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:48.301Z"
                    },
                    "stellar": {
                        "detection_time": 151536,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "a84a9d9a-076f-42fb-9487-9f13ca1968411784718091719-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717361860,
                    "timestamp_utc": "2026-07-22T10:49:21.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784718091719,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsnC74F.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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
                "_id": "1decf2fa-2827-4a5a-a962-ba4e65a212751784718091722-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2152,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "fLp6iZ8BI3UnQyDOlvQ1",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "34d10c3b-d962-49da-ba99-b60e41f8c5e4"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaDetection"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 45,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 45,
                    "file": {
                        "hash": {
                            "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d"
                        }
                    },
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "fLp6iZ8BI3UnQyDOlvQ1",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 45,
                    "sha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                    "sophos": {
                        "appSha256": "ddccebbf499672af3a74be6fb838b804a66679f7689dde137c39f4e0df1be11d",
                        "created_at": "2026-07-22T10:49:32.870Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "34d10c3b-d962-49da-ba99-b60e41f8c5e4",
                        "location": "NBCJPPA25002",
                        "name": "PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'",
                        "origin": "ML",
                        "severity": "medium",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaDetection",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:48:59.956Z"
                    },
                    "stellar": {
                        "detection_time": 151546,
                        "status": "New"
                    },
                    "stellar_da_input": 1713,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "1decf2fa-2827-4a5a-a962-ba4e65a212751784718091722-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717372870,
                    "timestamp_utc": "2026-07-22T10:49:32.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784718091722,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaDetection\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA detected: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: User Execution",
                        "framework_version": "v13",
                        "name": "sophos_event-execution-user_execution",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaDetection",
                            "name": "event_endpoint_corepuadetection"
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
                "_id": "b2caaebe-4bf3-45a2-badd-dcb1597d5aa91784718091745-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 2153,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "fbp6iZ8BI3UnQyDOlvQ1",
                    "appid_stdport": "yes",
                    "computer_name": "NBCJPPA25002",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "4c1f2aac-b55d-428c-ab58-f5e08694a50e"
                    ],
                    "dms_job_id": "sophos_events",
                    "dscp_name": "Best Effort",
                    "engid": "sophos_CAJA-ANDE-SOPHOS",
                    "engid_gateway": "",
                    "engid_name": "sophos_CAJA-ANDE-SOPHOS",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Event::Endpoint::CorePuaClean"
                        },
                        "type": "Endpoint"
                    },
                    "event_score": 15,
                    "event_source": "sophos_events",
                    "event_status": "New",
                    "fidelity": 15,
                    "group": "PUA",
                    "host": {
                        "ip": "172.16.202.10"
                    },
                    "hostip": "172.16.202.10",
                    "hostip_assetid": "83528688-76d9-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.10",
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
                    "orig_id": "fbp6iZ8BI3UnQyDOlvQ1",
                    "orig_index": "aella-syslog-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "core_remedy_items": {
                            "items": [
                                {
                                    "descriptor": "C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll",
                                    "processPath": "",
                                    "result": "NOT_FOUND",
                                    "sophosPid": "",
                                    "suspendResult": "NOT_APPLICABLE",
                                    "type": "file"
                                }
                            ],
                            "totalItems": 1
                        },
                        "created_at": "2026-07-22T10:49:45.868Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "2b2357b1-672b-486b-b240-d82bd4070138",
                        "endpoint_type": "computer",
                        "group": "PUA",
                        "id": "4c1f2aac-b55d-428c-ab58-f5e08694a50e",
                        "location": "NBCJPPA25002",
                        "name": "PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'",
                        "severity": "low",
                        "source": "CAJAANDE\\jatc59",
                        "source_info": {
                            "ip": "172.16.202.10"
                        },
                        "threat": "Generic ML PUA",
                        "type": "Event::Endpoint::CorePuaClean",
                        "user_id": "6926f9f972291113e7f8ca80",
                        "when": "2026-07-22T10:49:12.609Z"
                    },
                    "stellar": {
                        "detection_time": 151551,
                        "status": "New"
                    },
                    "stellar_da_input": 1673,
                    "stellar_index_id": "aella-ser-2026.07.22-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "b2caaebe-4bf3-45a2-badd-dcb1597d5aa91784718091745-YWVsbGEtc2VyLTIwMjYuMDcuMjItMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat": "Generic ML PUA",
                    "threat_score": 0,
                    "timestamp": 1784717385868,
                    "timestamp_utc": "2026-07-22T10:49:45.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\jatc59"
                    },
                    "username": "CAJAANDE\\jatc59",
                    "write_by": "sef",
                    "write_time": 1784718091745,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::CorePuaClean\", Host IP of \"172.16.202.10\", User Name of \"CAJAANDE\\jatc59\".\nThe description of the event states that \"PUA cleaned up: 'Generic ML PUA' at 'C:\\Users\\jatc59\\AppData\\Local\\Temp\\nsj2E47.tmp\\System.dll'\"",
                        "display_name": "Sophos Event: XDR Endpoint Indicator of Threat",
                        "framework_version": "v13",
                        "name": "sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat",
                        "scope": "",
                        "subtype": {
                            "display_name": "Event::Endpoint::CorePuaClean",
                            "name": "event_endpoint_corepuaclean"
                        },
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Sophos"
                        ],
                        "technique": {
                            "id": "XT1004",
                            "name": "XDR Endpoint Indicator of Threat"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "XTA0001",
                                    "name": "XDR EBA"
                                },
                                "technique": {
                                    "id": "XT1004",
                                    "name": "XDR Endpoint Indicator of Threat"
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