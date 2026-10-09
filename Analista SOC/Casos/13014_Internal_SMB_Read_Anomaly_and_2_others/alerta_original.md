=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "8e0ccf33-0d6d-4589-8a27-814e51fc5a621785921302706-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 642,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 78,
                    "aella_tuples": "192.168.169.8.10.11.1.1.445.185",
                    "anomaly_id": "TOws0Z8BI3UnQyDOeeW8",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.8"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
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
                    "dstip_host": "technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 445,
                    "end_bucket_time": 1785921000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 34,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\SysVol",
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 2
                            },
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 97.8,
                    "flow_score": 100,
                    "inbytes_delta": 2533,
                    "inbytes_total": 2533,
                    "inpkts_delta": 10,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "metadata": [
                        {
                            "request": {
                                "command": 114,
                                "nt_status": 0,
                                "user_id": 0,
                                "version": 1
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 0,
                                "version": 2
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 1,
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 2,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\SysVol",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 11,
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            },
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{8172E035-096F-4520-9BFF-42E70678B00F}\\gpt.ini",
                                "version": 2
                            }
                        }
                    ],
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "TOws0Z8BI3UnQyDOeeW8",
                    "orig_index": "aella-adr-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 6123,
                    "outbytes_total": 6123,
                    "outpkts_delta": 15,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785920777214,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.8",
                    "srcip": "192.168.169.8",
                    "srcip_assetid": "dd5d85fc-40c3-11f1-96c3-72abedb727d0",
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
                    "srcip_host": "nb-chidalgo.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49717,
                    "start_bucket_time": 1785920700000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1785921302695,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 522345,
                        "status": "New"
                    },
                    "stellar_da_input": 2046,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8e0ccf33-0d6d-4589-8a27-814e51fc5a621785921302706-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785920776692,
                    "timestamp_utc": "2026-08-05T09:06:16.000Z",
                    "tos": 0,
                    "totalbytes": 8656,
                    "totalpackets": 25,
                    "typical": 10,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785921302706,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.8, name: nb-chidalgo.technoma.local\" private) has sent an anomalously large number (#: 78) of SMB read requests, compared to its typical number (#: 10), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\SysVol, \\\\ad.technoma.local\\IPC$ very frequently.",
                        "display_name": "Internal SMB Read Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_read_anomaly",
                        "scope": "Internal",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "09865a9b-7659-4968-b671-b8dcf288531a1785928202826-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 670,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1.5,
                    "aella_tuples": "192.168.169.31.10.11.1.1.53.32",
                    "anomaly_id": "ifCV0Z8BI3UnQyDOTB0h",
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
                        "INFO TeamViewer RMM Domain (teamviewer .com) in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "ssl.gstatic.com"
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
                    "end_bucket_time": 1785927900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 34,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2060630,
                                "ids_severity": "low",
                                "name": "INFO TeamViewer RMM Domain (teamviewer .com) in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 63.51,
                    "file_extract_timestamp": 1785927643334,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-05T00:00:00Z",
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
                                "2025_03_05"
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
                                "RMM",
                                "Teamviewer"
                            ],
                            "updated_at": [
                                "2025_03_05"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 4982,
                                        "opcode": 0,
                                        "rrname": "router8.teamviewer.com",
                                        "rrtype": "A",
                                        "tx_id": 8,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 790,
                                "bytes_toserver": 476,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 4,
                                "pkts_toserver": 5,
                                "src_ip": "192.168.169.31",
                                "src_port": 58266,
                                "start": "2026-08-05T10:59:56.158520+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_05",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO TeamViewer RMM Domain (teamviewer .com) in DNS Lookup\\\"; content:!\\\"|03|www\\\"; dns.query; dotprefix; content:\\\".teamviewer.com\\\"; fast_pattern; nocase; endswith; threshold:type limit, seconds 180, count 1, track by_src; reference:url,www.teamviewer.com; classtype:misc-activity; sid:2060630; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_05, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag Teamviewer, tag RMM, updated_at 2025_03_05, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_05"
                        },
                        "severity": "low",
                        "signature": "INFO TeamViewer RMM Domain (teamviewer .com) in DNS Lookup",
                        "signature_id": 2060630
                    },
                    "inbytes_delta": 0,
                    "inbytes_total": 790,
                    "inpkts_delta": 0,
                    "inpkts_total": 4,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2008-02-11T15:31:25Z",
                            "effective_tld": "gstatic.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "ssl.gstatic.com",
                            "query_type": "A",
                            "transaction_id": 35954
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "142.251.128.131",
                                    "host_type": "A",
                                    "name": "ssl.gstatic.com",
                                    "section_type": "Answer",
                                    "ttl": 41
                                }
                            ],
                            "domain_creation": "2008-02-11T15:31:25Z",
                            "effective_tld": "gstatic.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "ssl.gstatic.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "142.251.128.131"
                            ],
                            "response_time": 0,
                            "transaction_id": 35954
                        },
                        "transaction_id": 35954
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
                    "orig_id": "ifCV0Z8BI3UnQyDOTB0h",
                    "orig_index": "aella-maltrace-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 0,
                    "outbytes_total": 476,
                    "outpkts_delta": 0,
                    "outpkts_total": 5,
                    "port_name": "ethernet1",
                    "processing_time": 7,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1785927643703,
                    "response_time": 7,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.31",
                    "srcip": "192.168.169.31",
                    "srcip_assetid": "13a20368-df71-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "NB-ANGELRA2",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.31.2060630.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 58266,
                    "start_bucket_time": 1785927600000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1785928202804,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 552546,
                        "status": "New"
                    },
                    "stellar_da_input": 1669,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "09865a9b-7659-4968-b671-b8dcf288531a1785928202826-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785927643510,
                    "timestamp_utc": "2026-08-05T11:00:43.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785928202826,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 3.0) of exploit attempts with the IDS signature \"INFO TeamViewer RMM Domain (teamviewer .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 1.5) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "6b7aaaad-e25a-49a8-85fd-49d46e5444391785929403954-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 687,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "IfCn0Z8BI3UnQyDOTb5F",
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
                        "bx-0004.bx-msedge.NET"
                    ],
                    "domain_reputation": "Good",
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
                    "dstip_host": "8.8.8.8",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 32,
                    "end_bucket_time": 1785929100000,
                    "end_reason": 1,
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
                    "file_extract_timestamp": 1785928822927,
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
                                        "id": 62953,
                                        "opcode": 0,
                                        "rrname": "boot.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 156,
                                "bytes_toserver": 191,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 61859,
                                "start": "2026-08-05T11:16:23.422955+0000"
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
                    "inbytes_delta": 152,
                    "inbytes_total": 156,
                    "inpkts_delta": 1,
                    "inpkts_total": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2024-07-05T16:17:54Z",
                            "effective_tld": "bx-msedge.net",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "bx-0004.bx-msedge.NET",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 49153
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns1.bx-msedge.NET",
                                    "host_type": "SOA",
                                    "name": "bx-msedge.NET",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 25
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2024-07-05T16:17:54Z",
                            "effective_tld": "bx-msedge.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 32,
                            "query": "bx-0004.bx-msedge.NET",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 32,
                            "transaction_id": 49153
                        },
                        "transaction_id": 49153
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
                    "orig_id": "IfCn0Z8BI3UnQyDOTb5F",
                    "orig_index": "aella-maltrace-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 92,
                    "outbytes_total": 191,
                    "outpkts_delta": 1,
                    "outpkts_total": 2,
                    "port_name": "ethernet1",
                    "processing_time": 32,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1785928823412,
                    "response_time": 32,
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
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 61859,
                    "start_bucket_time": 1785928800000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785929403919,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 573647,
                        "status": "New"
                    },
                    "stellar_da_input": 1646,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6b7aaaad-e25a-49a8-85fd-49d46e5444391785929403954-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785928823196,
                    "timestamp_utc": "2026-08-05T11:20:23.000Z",
                    "tos": 0,
                    "totalbytes": 244,
                    "totalpackets": 2,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785929403954,
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
            }
        ]
    }
}