=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "1cc7a1bb-4e3d-4a5e-905a-5df9a36179801784789703686-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3475,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1.5,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "anomaly_id": "HPm5jZ8BI3UnQyDOeAMM",
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
                        "INFO DNS Query to Cloudflare Tunneling Domain (argotunnel .com)",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "cfd-features.argotunnel.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.4.4",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_geo": {
                        "city": "Westfield",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 42.1293,
                        "longitude": -72.7522,
                        "region": "Massachusetts"
                    },
                    "dstip_geo_point": "42.1293,-72.7522",
                    "dstip_host": "8.8.4.4",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1784789400000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2047122,
                                "ids_severity": "low",
                                "name": "INFO DNS Query to Cloudflare Tunneling Domain (argotunnel .com)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 63.51,
                    "file_extract_timestamp": 1784789162150,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2023-08-09T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2023_08_09"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Description_Generated_By_Proofpoint_Nexus"
                            ],
                            "updated_at": [
                                "2023_08_09"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 55924,
                                        "opcode": 0,
                                        "rrname": "cfd-features.argotunnel.com",
                                        "rrtype": "TXT",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 102,
                                "dest_ip": "8.8.4.4",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 53935,
                                "start": "2026-07-23T06:46:02.150758+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2023_08_09",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO DNS Query to Cloudflare Tunneling Domain (argotunnel .com)\\\"; dns.query; dotprefix; content:\\\".argotunnel.com\\\"; nocase; endswith; reference:url,www.guidepointsecurity.com/blog/tunnel-vision-cloudflared-abused-in-the-wild/; classtype:misc-activity; sid:2047122; rev:1; metadata:attack_target Client_Endpoint, created_at 2023_08_09, deployment Perimeter, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2023_08_09;)\\n\"",
                            "updated": "2023_08_09"
                        },
                        "severity": "low",
                        "signature": "INFO DNS Query to Cloudflare Tunneling Domain (argotunnel .com)",
                        "signature_id": 2047122
                    },
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_shouldDup": "true",
                        "_whitelist": 0,
                        "is_tunneling": 12,
                        "request": {
                            "dga_score": 1,
                            "domain_creation": "2018-01-18T22:33:16Z",
                            "effective_tld": "argotunnel.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "cfd-features.argotunnel.com",
                            "query_type": "TXT",
                            "section_type": "Additional Answer",
                            "transaction_id": 55924
                        },
                        "transaction_id": 55924
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
                    "orig_id": "HPm5jZ8BI3UnQyDOeAMM",
                    "orig_index": "aella-maltrace-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 98,
                    "outbytes_total": 102,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784789162497,
                    "response_time": 0,
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
                    "srcip_host": "technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "10.11.1.1.2047122.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 53935,
                    "start_bucket_time": 1784789100000,
                    "state": "HalfOpened",
                    "stellar": {
                        "alert_time": 1784789703631,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 533459,
                        "status": "New"
                    },
                    "stellar_da_input": 1477,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "1cc7a1bb-4e3d-4a5e-905a-5df9a36179801784789703686-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784789162293,
                    "timestamp_utc": "2026-07-23T06:46:02.000Z",
                    "tos": 0,
                    "totalbytes": 98,
                    "totalpackets": 1,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784789703685,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 3.0) of exploit attempts with the IDS signature \"INFO DNS Query to Cloudflare Tunneling Domain (argotunnel .com)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 1.5) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "7e0b34b8-0332-403a-a530-41d34192f4511784798403163-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3484,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 78,
                    "aella_tuples": "192.168.169.119.10.11.1.1.445.185",
                    "anomaly_id": "w_1Ajp8BI3UnQyDOhBbh",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.119"
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
                    "end_bucket_time": 1784798100000,
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
                            "\\\\ad.technoma.local\\IPC$",
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 1
                            },
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 3
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 97.34,
                    "flow_score": 100,
                    "inbytes_delta": 2593,
                    "inbytes_total": 2593,
                    "inpkts_delta": 11,
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
                                "processing_time": 1,
                                "response_time": 3,
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
                                "processing_time": 1,
                                "response_time": 3,
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
                            }
                        },
                        {
                            "request": {
                                "command": 11,
                                "filename": "technoma.local\\Policies\\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\\gpt.ini",
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
                            "response": {
                                "command": 5,
                                "processing_time": 1,
                                "response_time": 3
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
                            },
                            "response": {
                                "processing_time": 1,
                                "response_time": 3,
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
                    "orig_id": "w_1Ajp8BI3UnQyDOhBbh",
                    "orig_index": "aella-adr-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 6063,
                    "outbytes_total": 6063,
                    "outpkts_delta": 14,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784798016145,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.119",
                    "srcip": "192.168.169.119",
                    "srcip_assetid": "20292710-fd3f-11f0-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.119",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49731,
                    "start_bucket_time": 1784797800000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784798403151,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 382874,
                        "status": "New"
                    },
                    "stellar_da_input": 2075,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7e0b34b8-0332-403a-a530-41d34192f4511784798403163-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784798015846,
                    "timestamp_utc": "2026-07-23T09:13:35.000Z",
                    "tos": 0,
                    "totalbytes": 8656,
                    "totalpackets": 25,
                    "typical": 10,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784798403163,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.119\" private) has sent an anomalously large number (#: 78) of SMB read requests, compared to its typical number (#: 10), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$, \\\\ad.technoma.local\\SysVol very frequently.",
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
            }
        ]
    }
}