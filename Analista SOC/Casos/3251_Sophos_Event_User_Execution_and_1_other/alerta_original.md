=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "49b54fe6-5c88-4958-ad4e-a4347badbaf61784890204574-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4711,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "NkO8k58BI3UnQyDO72AL",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA081",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "9258b1be-5ec3-4617-aa15-d3a02b8c4256"
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
                        "ip": "172.16.202.111"
                    },
                    "hostip": "172.16.202.111",
                    "hostip_assetid": "0434f4ac-7928-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.111",
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
                    "orig_id": "NkO8k58BI3UnQyDO72AL",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T10:44:15.896Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bbec545c-b266-4e5c-8f98-c884fdd92da6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "9258b1be-5ec3-4617-aa15-d3a02b8c4256",
                        "location": "CJPPA081",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\c3412949",
                        "source_info": {
                            "ip": "172.16.202.111"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6931c69758fc555f47173d20",
                        "when": "2026-07-24T10:43:41.000Z"
                    },
                    "stellar": {
                        "detection_time": 144291,
                        "status": "New"
                    },
                    "stellar_da_input": 1363,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "49b54fe6-5c88-4958-ad4e-a4347badbaf61784890204574-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784889855896,
                    "timestamp_utc": "2026-07-24T10:44:15.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\c3412949"
                    },
                    "username": "CAJAANDE\\c3412949",
                    "write_by": "sef",
                    "write_time": 1784890204574,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.111\", User Name of \"CAJAANDE\\c3412949\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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
                "_id": "891d8269-520f-49d3-8b94-4cad4f66ceec1784890442808-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                "_version": 1,
                "_seq_no": 4719,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "bUPBk58BI3UnQyDOg4Vm",
                    "appid_stdport": "yes",
                    "computer_name": "CJPPA081",
                    "detected_fields": [
                        "tenantid",
                        "sophos.id"
                    ],
                    "detected_values": [
                        "392cf7319d694d53889280340fff51e9",
                        "9258b1be-5ec3-4617-aa15-d3a02b8c4256"
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
                        "ip": "172.16.202.111"
                    },
                    "hostip": "172.16.202.111",
                    "hostip_assetid": "0434f4ac-7928-11f1-bdbf-be2f2074df47",
                    "hostip_host": "172.16.202.111",
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
                    "orig_id": "bUPBk58BI3UnQyDOg4Vm",
                    "orig_index": "aella-syslog-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "severity": 15,
                    "sophos": {
                        "created_at": "2026-07-24T10:44:15.896Z",
                        "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                        "endpoint_id": "bbec545c-b266-4e5c-8f98-c884fdd92da6",
                        "endpoint_type": "computer",
                        "group": "WEB",
                        "id": "9258b1be-5ec3-4617-aa15-d3a02b8c4256",
                        "location": "CJPPA081",
                        "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
                        "severity": "low",
                        "source": "CAJAANDE\\c3412949",
                        "source_info": {
                            "ip": "172.16.202.111"
                        },
                        "type": "Event::Endpoint::WebControlViolation",
                        "user_id": "6931c69758fc555f47173d20",
                        "when": "2026-07-24T10:43:41.000Z"
                    },
                    "stellar": {
                        "detection_time": 82367,
                        "status": "New"
                    },
                    "stellar_da_input": 1363,
                    "stellar_index_id": "aella-ser-2026.07.24-392cf7319d694d53889280340fff51e9",
                    "stellar_uuid": "891d8269-520f-49d3-8b94-4cad4f66ceec1784890442808-YWVsbGEtc2VyLTIwMjYuMDcuMjQtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
                    "tenant_name": "CAJAANDE",
                    "tenantid": "392cf7319d694d53889280340fff51e9",
                    "threat_score": 0,
                    "timestamp": 1784889855896,
                    "timestamp_utc": "2026-07-24T10:44:15.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user": {
                        "name": "CAJAANDE\\c3412949"
                    },
                    "username": "CAJAANDE\\c3412949",
                    "write_by": "sef",
                    "write_time": 1784890442808,
                    "xdr_event": {
                        "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.111\", User Name of \"CAJAANDE\\c3412949\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
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