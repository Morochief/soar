=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "2fd5d2f4-f104-4596-9821-9ce5a2d9674c1784216704093-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12148,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.null",
                    "anomaly_id": "mWWRa58BI3UnQyDO4j1J",
                    "anomaly_tag": "spike",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.8.8",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstport": 53,
                    "end_bucket_time": 1784216400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 16,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2060507,
                                "ids_severity": "low",
                                "name": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 10.67,
                    "file_extract_timestamp": 1784216143551,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-03T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_03_03"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0011"
                            ],
                            "mitre_tactic_name": [
                                "Command_And_Control"
                            ],
                            "mitre_technique_id": [
                                "T1219"
                            ],
                            "mitre_technique_name": [
                                "Remote_Access_Software"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "AnyDesk"
                            ],
                            "updated_at": [
                                "2025_03_03"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 14775,
                                        "opcode": 0,
                                        "rrname": "relay-2bab18c5.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 168,
                                "bytes_toserver": 225,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 62397,
                                "start": "2026-07-16T15:34:23.541755+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_03",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\\\"; dns.query; dotprefix; content:\\\".net.anydesk.com\\\"; nocase; endswith; reference:url,support.anydesk.com/knowledge/firewall; classtype:misc-activity; sid:2060507; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_03"
                        },
                        "severity": "low",
                        "signature": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "signature_id": 2060507
                    },
                    "inbytes_total": 168,
                    "inpkts_total": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "mWWRa58BI3UnQyDO4j1J",
                    "orig_index": "aella-maltrace-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 225,
                    "outpkts_total": 2,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784216143952,
                    "score": 30,
                    "severity": 20,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ad.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "10.11.1.1.2060507.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 62397,
                    "start_bucket_time": 1784216100000,
                    "stellar": {
                        "alert_time": 1784216704079,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 553492,
                        "status": "New"
                    },
                    "stellar_da_input": 1656,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2fd5d2f4-f104-4596-9821-9ce5a2d9674c1784216704093-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784216143762,
                    "timestamp_utc": "2026-07-16T15:35:43.000Z",
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784216704093,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 10.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 5.0) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_pub",
                        "scope": "External",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1190",
                            "name": "Exploit Public-Facing Application"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "4e53c19c-61f1-4f7c-bce8-cbb348e8401f1784217002479-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12153,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "10.11.1.1.192.168.169.135.389.4",
                    "alert_time": 1784217002404,
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp389",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-16 15:34:02 UTC",
                        "first_timestamp": 1784216042302,
                        "last_time_utc": "2026-07-16 15:34:02 UTC",
                        "last_timestamp": 1784216042302,
                        "repeat_count": 1,
                        "time_window_ms": 86400000
                    },
                    "ath_info": {
                        "rule_name": "exploit_attempt",
                        "scheduled_time_utc": "2026-07-16T15:48:00.000Z",
                        "scheduled_timestamp": 1784216880000
                    },
                    "correlation_info": [
                        {
                            "_id": "f70f7fe5-a20e-492f-9e36-298d1c3e41ea1784134803446-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                            "dstip": "10.11.1.1",
                            "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                            "ids": {
                                "signature": "INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup"
                            },
                            "index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                            "original_event": {
                                "actual": 3,
                                "aella_tuples": "192.168.169.135.10.11.1.1.53.32",
                                "anomaly_id": "BB-vZp8BI3UnQyDO4kn0",
                                "anomaly_tag": "spike",
                                "appid": 32,
                                "appid_family": "Network",
                                "appid_name": "dns",
                                "appid_stdport": "yes",
                                "cust_file": 0,
                                "detected_fields": [
                                    "ids.signature",
                                    "ids.severity"
                                ],
                                "detected_values": [
                                    "INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup",
                                    "low"
                                ],
                                "direction": "EveTxRx",
                                "domain_list": [
                                    "relay-930279ff.net.anydesk.com"
                                ],
                                "domain_reputation": "Good",
                                "dscp_name": "Best Effort",
                                "dst_tuples": "null.1101.10.11.1.1",
                                "dstip": "10.11.1.1",
                                "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                                "dstip_geo": {
                                    "city": "Asunción",
                                    "countryCode": "PY",
                                    "countryName": "Paraguay",
                                    "latitude": -25.2869,
                                    "longitude": -57.6511,
                                    "region": "Asuncion"
                                },
                                "dstip_geo_point": "-25.2869,-57.6511",
                                "dstip_host": "ad.technoma.local",
                                "dstip_reputation": "Good",
                                "dstip_type": "private",
                                "dstip_version": "ipv4",
                                "dstmac": "00:50:56:af:ff:5a",
                                "dstport": 53,
                                "end_bucket_time": 1784134500000,
                                "engid": "4e3eab0649114a80a089a5d5a078994d",
                                "engid_gateway": "190.104.178.146",
                                "engid_name": "technoma-sensor",
                                "event_category": "killchain",
                                "event_name": "exploit_attempt_priv_priv",
                                "event_score": 23,
                                "event_source": "new_ml",
                                "event_status": "Closed",
                                "event_summary": {
                                    "dominant_severity": "low",
                                    "ids_signatures_summarize": [
                                        {
                                            "id": 2060512,
                                            "ids_severity": "low",
                                            "name": "INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup"
                                        }
                                    ],
                                    "total_signatures": 1
                                },
                                "event_type": "exploit",
                                "fidelity": 18.53,
                                "file_extract_timestamp": 1784134227250,
                                "file_name": "",
                                "file_path": "",
                                "fileid": "",
                                "flow_score": 98,
                                "handler": "ids-event",
                                "ids": {
                                    "action": "allowed",
                                    "category": "Misc activity",
                                    "created_ts": "2025-03-03T00:00:00Z",
                                    "gid": 1,
                                    "metadata": {
                                        "affected_product": [
                                            "Any"
                                        ],
                                        "attack_target": [
                                            "Client_and_Server"
                                        ],
                                        "confidence": [
                                            "High"
                                        ],
                                        "created_at": [
                                            "2025_03_03"
                                        ],
                                        "deployment": [
                                            "Perimeter"
                                        ],
                                        "mitre_tactic_id": [
                                            "TA0011"
                                        ],
                                        "mitre_tactic_name": [
                                            "Command_And_Control"
                                        ],
                                        "mitre_technique_id": [
                                            "T1219"
                                        ],
                                        "mitre_technique_name": [
                                            "Remote_Access_Software"
                                        ],
                                        "performance_impact": [
                                            "Low"
                                        ],
                                        "signature_severity": [
                                            "Informational"
                                        ],
                                        "tag": [
                                            "AnyDesk"
                                        ],
                                        "updated_at": [
                                            "2025_03_03"
                                        ]
                                    },
                                    "payload_details": {
                                        "app_proto": "dns",
                                        "dns": {
                                            "query": [
                                                {
                                                    "id": 52895,
                                                    "opcode": 0,
                                                    "rrname": "boot.net.anydesk.com",
                                                    "rrtype": "A",
                                                    "tx_id": 0,
                                                    "type": "query"
                                                }
                                            ],
                                            "version": 2
                                        },
                                        "flow": {
                                            "bytes_toclient": 0,
                                            "bytes_toserver": 84,
                                            "dest_ip": "10.11.1.1",
                                            "dest_port": 53,
                                            "pkts_toclient": 0,
                                            "pkts_toserver": 1,
                                            "src_ip": "192.168.169.135",
                                            "src_port": 50778,
                                            "start": "2026-07-15T16:50:27.250787+0000"
                                        }
                                    },
                                    "rev": 1,
                                    "rule": {
                                        "created": "2025_03_03",
                                        "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup\\\"; dns.query; bsize:20; content:\\\"boot.net.anydesk.com\\\"; nocase; classtype:misc-activity; sid:2060512; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                                        "updated": "2025_03_03"
                                    },
                                    "severity": "low",
                                    "signature": "INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup",
                                    "signature_id": 2060512
                                },
                                "inbytes_delta": 266,
                                "inbytes_total": 0,
                                "inpkts_delta": 1,
                                "inpkts_total": 0,
                                "is_dga": "no",
                                "lateral": true,
                                "locid": "unassigned location",
                                "md5": "",
                                "metadata": {
                                    "_whitelist": -1,
                                    "is_tunneling": 0,
                                    "request": {
                                        "dga_score": 0,
                                        "domain_creation": "2004-02-07T15:49:37Z",
                                        "effective_tld": "anydesk.com",
                                        "flags": 256,
                                        "message_type": "QUERY",
                                        "query": "relay-930279ff.net.anydesk.com",
                                        "query_type": "A",
                                        "transaction_id": 39133
                                    },
                                    "transaction_id": 39133
                                },
                                "msg_class": "ids_event",
                                "msg_origin": {
                                    "processor": {
                                        "type": "maltrace"
                                    },
                                    "source": "modular_sensor"
                                },
                                "msgtype": 1,
                                "msgtype_name": "start",
                                "netid": 1101,
                                "netid_name": "vlan1101",
                                "new_file": 0,
                                "obsid": 3232239430,
                                "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                                "org_name": "Technoma",
                                "orig_id": "BB-vZp8BI3UnQyDO4kn0",
                                "orig_index": "aella-maltrace-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                                "outbytes_delta": 170,
                                "outbytes_total": 84,
                                "outpkts_delta": 2,
                                "outpkts_total": 1,
                                "port_name": "ethernet1",
                                "processing_time": 13,
                                "proto": 17,
                                "proto_name": "udp",
                                "receive_time": 1784134227699,
                                "response_time": 13,
                                "score": 30,
                                "severity": 25,
                                "sha256": "",
                                "src_tuples": "null.1101.192.168.169.135",
                                "srcip": "192.168.169.135",
                                "srcip_assetid": "f0eae3ca-f2d6-11f0-a51f-3a0341ec6ca6",
                                "srcip_geo": {
                                    "city": "Asunción",
                                    "countryCode": "PY",
                                    "countryName": "Paraguay",
                                    "latitude": -25.2869,
                                    "longitude": -57.6511,
                                    "region": "Asuncion"
                                },
                                "srcip_geo_point": "-25.2869,-57.6511",
                                "srcip_geo_source": "maxmind",
                                "srcip_host": "nb-fcandia.technoma.local",
                                "srcip_reputation": "Good",
                                "srcip_sig_id": "192.168.169.135.2060512.0",
                                "srcip_type": "private",
                                "srcip_version": "ipv4",
                                "srcmac": "00:09:0f:09:0a:04",
                                "srcport": 50778,
                                "start_bucket_time": 1784134200000,
                                "state": "Established",
                                "stellar": {
                                    "alert_time": 1784134803409,
                                    "alert_timestamp_field": "timestamp",
                                    "anomaly_tag_subtype": "individual_spike",
                                    "detection_time": 572645,
                                    "status": "New"
                                },
                                "stellar_da_input": 1656,
                                "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                                "stellar_uuid": "f70f7fe5-a20e-492f-9e36-298d1c3e41ea1784134803446-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                                "tenant_name": "technoma",
                                "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                                "threat_score": 0,
                                "timestamp": 1784134227514,
                                "timestamp_utc": "2026-07-15T16:50:27.000Z",
                                "tos": 0,
                                "totalbytes": 436,
                                "totalpackets": 3,
                                "typical": 0.5,
                                "user_action": {
                                    "alert_to_last": 1267918,
                                    "history": [
                                        {
                                            "action": "Status changed to Closed",
                                            "action_time": 1784136071363,
                                            "action_user": "ilsongonzalez@technoma.com.py"
                                        }
                                    ],
                                    "last_action": "Status changed to Closed",
                                    "last_modified": 1784136071363,
                                    "last_timestamp": 1784136071363,
                                    "last_user": "ilsongonzalez@technoma.com.py"
                                },
                                "vlan": 1101,
                                "write_by": "sef",
                                "write_time": 1784134803445,
                                "xdr_event": {
                                    "description": "In internal traffic, an anomalously high number (#: 6.0) of exploit attempts with the IDS signature \"INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 3.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                                    "display_name": "Exploit Attempt (Low Severity)",
                                    "framework_version": "v8",
                                    "name": "exploit_attempt_priv_priv",
                                    "scope": "Internal",
                                    "subtype": {
                                        "display_name": "IDS Traffic Anomaly",
                                        "name": "ids_traffic_anomaly"
                                    },
                                    "tactic": {
                                        "id": "TA0008",
                                        "name": "Lateral Movement"
                                    },
                                    "tags": [
                                        "Internal",
                                        "Network Traffic Analysis"
                                    ],
                                    "technique": {
                                        "id": "T1210",
                                        "name": "Exploitation of Remote Services"
                                    },
                                    "xdr_killchain_stage": "Propagation",
                                    "xdr_killchain_version": "v1"
                                }
                            },
                            "query_name": "exploit",
                            "readable_name": "exploit",
                            "srcip": "192.168.169.135",
                            "srcip_assetid": "f0eae3ca-f2d6-11f0-a51f-3a0341ec6ca6",
                            "timestamp": 1784134227514,
                            "timestamp_utc": "2026-07-15T16:50:27.000Z",
                            "write_time": 1784134803445,
                            "write_time_utc": "2026-07-15T17:00:03.000Z"
                        },
                        {
                            "_id": "gmWQa58BI3UnQyDO0iiD",
                            "appid_name": "tcp389",
                            "dstip": "192.168.169.135",
                            "dstip_assetid": "f0eae3ca-f2d6-11f0-a51f-3a0341ec6ca6",
                            "index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                            "original_event": {
                                "aella_tuples": "10.11.1.1.192.168.169.135.389.4",
                                "appid": 4,
                                "appid_family": "Standard",
                                "appid_name": "tcp389",
                                "appid_stdport": "yes",
                                "dscp_name": "Best Effort",
                                "dst_tuples": "00:09:0f:09:0a:04.1101.192.168.169.135",
                                "dstip": "192.168.169.135",
                                "dstip_assetid": "f0eae3ca-f2d6-11f0-a51f-3a0341ec6ca6",
                                "dstip_geo": {
                                    "city": "Asunción",
                                    "countryCode": "PY",
                                    "countryName": "Paraguay",
                                    "latitude": -25.2869,
                                    "longitude": -57.6511,
                                    "region": "Asuncion"
                                },
                                "dstip_geo_point": "-25.2869,-57.6511",
                                "dstip_host": "nb-fcandia.technoma.local",
                                "dstip_reputation": "Good",
                                "dstip_type": "private",
                                "dstip_version": "ipv4",
                                "dstmac": "00:09:0f:09:0a:04",
                                "dstport": 389,
                                "duration": 0,
                                "end_reason": 1,
                                "engid": "4e3eab0649114a80a089a5d5a078994d",
                                "engid_gateway": "190.104.178.146",
                                "engid_name": "technoma-sensor",
                                "flow_score": 96,
                                "inbytes_delta": 0,
                                "inbytes_total": 0,
                                "inpkts_delta": 0,
                                "locid": "unassigned location",
                                "msg_class": "interflow_traffic",
                                "msg_origin": {
                                    "category": "traffic",
                                    "processor": {
                                        "type": "aella_flow"
                                    },
                                    "source": "modular_sensor"
                                },
                                "msgtype": 4,
                                "msgtype_name": "startend",
                                "netid": 1101,
                                "netid_name": "vlan1101",
                                "obsid": 3232239430,
                                "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                                "org_name": "Technoma",
                                "outbytes_delta": 66,
                                "outbytes_total": 66,
                                "outpkts_delta": 1,
                                "port_name": "ethernet1",
                                "processing_time": 0,
                                "proto": 6,
                                "proto_name": "tcp",
                                "receive_time": 1784216073926,
                                "response_time": 0,
                                "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                                "srcip": "10.11.1.1",
                                "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                                "srcip_geo": {
                                    "city": "Asunción",
                                    "countryCode": "PY",
                                    "countryName": "Paraguay",
                                    "latitude": -25.2869,
                                    "longitude": -57.6511,
                                    "region": "Asuncion"
                                },
                                "srcip_geo_point": "-25.2869,-57.6511",
                                "srcip_geo_source": "maxmind",
                                "srcip_host": "ad.technoma.local",
                                "srcip_reputation": "Good",
                                "srcip_type": "private",
                                "srcip_version": "ipv4",
                                "srcmac": "00:50:56:af:ff:5a",
                                "srcport": 64894,
                                "state": "HalfOpened",
                                "stellar_da_input": 748,
                                "stellar_index_id": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                                "stellar_uuid": "e9b544fa-582b-4d2f-ad67-aeb6eb62d62a1784216073926",
                                "tcp_rtt": 0,
                                "tenant_name": "technoma",
                                "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                                "threat_score": 0,
                                "timestamp": 1784216042302,
                                "timestamp_utc": "2026-07-16T15:34:02.000Z",
                                "tos": 2,
                                "totalbytes": 66,
                                "totalpackets": 1,
                                "vlan": 1101,
                                "write_time": 1784216080280
                            },
                            "query_name": "seen_traffic",
                            "readable_name": "seen_traffic",
                            "srcip": "10.11.1.1",
                            "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                            "timestamp": 1784216042302,
                            "timestamp_utc": "2026-07-16T15:34:02.000Z",
                            "write_time": 1784216080280,
                            "write_time_utc": "2026-07-16T15:34:40.000Z"
                        }
                    ],
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:09:0f:09:0a:04.1101.192.168.169.135",
                    "dstip": "192.168.169.135",
                    "dstip_assetid": "f0eae3ca-f2d6-11f0-a51f-3a0341ec6ca6",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "nb-fcandia.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 389,
                    "duration": 0,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 47,
                    "event_status": "New",
                    "exploit_id": "f70f7fe5-a20e-492f-9e36-298d1c3e41ea1784134803446-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "exploit_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                    "fidelity": 18.53,
                    "flow_score": 96,
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-03T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_03_03"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0011"
                            ],
                            "mitre_tactic_name": [
                                "Command_And_Control"
                            ],
                            "mitre_technique_id": [
                                "T1219"
                            ],
                            "mitre_technique_name": [
                                "Remote_Access_Software"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "AnyDesk"
                            ],
                            "updated_at": [
                                "2025_03_03"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 52895,
                                        "opcode": 0,
                                        "rrname": "boot.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 84,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.135",
                                "src_port": 50778,
                                "start": "2026-07-15T16:50:27.250787+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_03",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup\\\"; dns.query; bsize:20; content:\\\"boot.net.anydesk.com\\\"; nocase; classtype:misc-activity; sid:2060512; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_03"
                        },
                        "severity": "low",
                        "signature": "INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup",
                        "signature_id": 2060512
                    },
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "indices": {
                        "exploit": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                        "seen_traffic": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050"
                    },
                    "inpkts_delta": 0,
                    "locid": "unassigned location",
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "f70f7fe5-a20e-492f-9e36-298d1c3e41ea1784134803446-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "orig_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                    "orig_timestamp": 1784216042302,
                    "orig_timestamp_utc": "2026-07-16T15:34:02.000Z",
                    "orig_write_time": 1784217002390,
                    "outbytes_delta": 66,
                    "outbytes_total": 66,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784216073926,
                    "response_time": 0,
                    "seen_traffic_id": "gmWQa58BI3UnQyDO0iiD",
                    "seen_traffic_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "severity": 75,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ad.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 64894,
                    "state": "HalfOpened",
                    "stellar": {
                        "alert_time": 1784217002404,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 922124,
                        "status": "New"
                    },
                    "stellar_da_input": 748,
                    "stellar_index": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4e53c19c-61f1-4f7c-bce8-cbb348e8401f1784217002479-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_info": {
                        "tenant_name": "technoma",
                        "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04"
                    },
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784216042302,
                    "timestamp_utc": "2026-07-16T15:34:02.000Z",
                    "tos": 2,
                    "totalbytes": 66,
                    "totalpackets": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784217002479,
                    "write_time_utc": "2026-07-16T15:50:02.404Z",
                    "xdr_event": {
                        "description": "An exploited host with vulnerabilities initiated a connection to the exploit attacker, which could indicate the host being compromised and performing C&C activities. See if the exploit was successful. Check the source host, and consider blocking.",
                        "display_name": "Exploited C&C Connection",
                        "event_source": "built-in-playbook",
                        "framework_version": "v8",
                        "name": "exploit_attempt_correlation",
                        "scope": "Internal",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2014",
                            "name": "XDR Command and Control Connection Exploitation"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ec66e0b0-7efb-4669-be84-53c7634cbc951784217003450-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12158,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 10.5,
                    "aella_tuples": "192.168.169.82.10.11.1.1.53.32",
                    "anomaly_id": "WmWVa58BI3UnQyDO2JTC",
                    "anomaly_tag": "spike",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "relay-33421df1.net.anydesk.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 53,
                    "duration": 29,
                    "end_bucket_time": 1784216700000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 24,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2060507,
                                "ids_severity": "low",
                                "name": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 21.11,
                    "file_extract_timestamp": 1784216404472,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-03T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_03_03"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0011"
                            ],
                            "mitre_tactic_name": [
                                "Command_And_Control"
                            ],
                            "mitre_technique_id": [
                                "T1219"
                            ],
                            "mitre_technique_name": [
                                "Remote_Access_Software"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "AnyDesk"
                            ],
                            "updated_at": [
                                "2025_03_03"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 33436,
                                        "opcode": 0,
                                        "rrname": "relay-33421df1.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 94,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.82",
                                "src_port": 62190,
                                "start": "2026-07-16T15:40:04.472888+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_03",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\\\"; dns.query; dotprefix; content:\\\".net.anydesk.com\\\"; nocase; endswith; reference:url,support.anydesk.com/knowledge/firewall; classtype:misc-activity; sid:2060507; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_03"
                        },
                        "severity": "low",
                        "signature": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "signature_id": 2060507
                    },
                    "inbytes_delta": 106,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2004-02-07T15:49:37Z",
                            "effective_tld": "anydesk.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "relay-33421df1.net.anydesk.com",
                            "query_type": "A",
                            "transaction_id": 33436
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "103.88.232.147",
                                    "host_type": "A",
                                    "name": "relay-33421df1.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                }
                            ],
                            "domain_creation": "2004-02-07T15:49:37Z",
                            "effective_tld": "anydesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 29,
                            "query": "relay-33421df1.net.anydesk.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "103.88.232.147"
                            ],
                            "response_time": 29,
                            "transaction_id": 33436
                        },
                        "transaction_id": 33436
                    },
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "WmWVa58BI3UnQyDO2JTC",
                    "orig_index": "aella-maltrace-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 90,
                    "outbytes_total": 94,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 29,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784216405102,
                    "response_time": 29,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.82",
                    "srcip": "192.168.169.82",
                    "srcip_assetid": "3250ceaa-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "nb-rduarte.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.82.2060507.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 62190,
                    "start_bucket_time": 1784216400000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784217003434,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 593155,
                        "status": "New"
                    },
                    "stellar_da_input": 1664,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ec66e0b0-7efb-4669-be84-53c7634cbc951784217003450-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784216404916,
                    "timestamp_utc": "2026-07-16T15:40:04.000Z",
                    "tos": 0,
                    "totalbytes": 196,
                    "totalpackets": 2,
                    "typical": 1.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784217003450,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 21.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 10.5) from the typical value of (#: 1.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_priv",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Internal",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1210",
                            "name": "Exploitation of Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ecba7102-d6f4-45e7-a190-bae7603fd8da1784217004456-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12159,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5.5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.null",
                    "anomaly_id": "RWWVa58BI3UnQyDO2JRP",
                    "anomaly_tag": "spike",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.8.8",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstport": 53,
                    "end_bucket_time": 1784216700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 20,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2060507,
                                "ids_severity": "low",
                                "name": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 21.11,
                    "file_extract_timestamp": 1784216404473,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-03T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_03_03"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0011"
                            ],
                            "mitre_tactic_name": [
                                "Command_And_Control"
                            ],
                            "mitre_technique_id": [
                                "T1219"
                            ],
                            "mitre_technique_name": [
                                "Remote_Access_Software"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "AnyDesk"
                            ],
                            "updated_at": [
                                "2025_03_03"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 2245,
                                        "opcode": 0,
                                        "rrname": "relay-33421df1.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 298,
                                "bytes_toserver": 202,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 62072,
                                "start": "2026-07-16T15:37:33.678848+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_03",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\\\"; dns.query; dotprefix; content:\\\".net.anydesk.com\\\"; nocase; endswith; reference:url,support.anydesk.com/knowledge/firewall; classtype:misc-activity; sid:2060507; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_03"
                        },
                        "severity": "low",
                        "signature": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "signature_id": 2060507
                    },
                    "inbytes_total": 298,
                    "inpkts_total": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "RWWVa58BI3UnQyDO2JRP",
                    "orig_index": "aella-maltrace-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 202,
                    "outpkts_total": 2,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784216405102,
                    "score": 30,
                    "severity": 20,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ad.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "10.11.1.1.2060507.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 62072,
                    "start_bucket_time": 1784216400000,
                    "stellar": {
                        "alert_time": 1784217004366,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 594190,
                        "status": "New"
                    },
                    "stellar_da_input": 1655,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ecba7102-d6f4-45e7-a190-bae7603fd8da1784217004456-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784216404916,
                    "timestamp_utc": "2026-07-16T15:40:04.000Z",
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784217004456,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 11.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 5.5) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_pub",
                        "scope": "External",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1190",
                            "name": "Exploit Public-Facing Application"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}

---------------------------------------------------------------------------
[+] NOTA: Reporte guardado exitosamente en:
C:/Users/kevinmoraes/Downloads/Analista SOC/Casos/12267_Exploited_C&C_Connection_and_1_other.md

[*] Enviando orden de cierre definitivo para Ticket 12267 con veredicto: False Positive...

[+] REPORTE: Caso e historial de notas impactados con exito en el backend.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11004] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11004] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
HTTPSConnectionPool(host='technoma.stellarcyber.cloud', port=443): Max retries exceeded with url: /connect/api/v1/access_token (Caused by NameResolutionError("HTTPSConnection(host='technoma.stellarcyber.cloud', port=443): Failed to resolve 'technoma.stellarcyber.cloud' ([Errno 11001] getaddrinfo failed)"))
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/cases?limit=100
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/data_sensors
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

---------------------------------------------------------------------------
[!] ERROR DE CONEXIÓN CON API (SOAR):
401 Client Error: Unauthorized for url: https://technoma.stellarcyber.cloud/connect/api/v1/tenants
[!] Sugerencia: Verifique su conexión de red, VPN o si 'technoma.stellarcyber.cloud' responde a ping.

[*] Solicitando comando PUT de asignacion para Ticket 3186...

[+] REPORTE: Caso e historial de notas impactados con exito en el backend.