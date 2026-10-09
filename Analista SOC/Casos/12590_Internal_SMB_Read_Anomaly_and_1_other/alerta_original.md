=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "696f6bfd-7eff-4675-a9d9-f3bc1d27d01e1784882404796-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4618,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 8.5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "7D9Ak58BI3UnQyDO4Kcj",
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
                        "www-www.bing.com.trafficmanager.NET"
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
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 30,
                    "end_bucket_time": 1784882100000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 30,
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
                    "fidelity": 69.48,
                    "file_extract_timestamp": 1784881925945,
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
                                        "id": 6475,
                                        "opcode": 0,
                                        "rrname": "relay-f348b09a.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 188,
                                "bytes_toserver": 209,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 63144,
                                "start": "2026-07-24T08:30:27.460563+0000"
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
                    "inbytes_delta": 210,
                    "inbytes_total": 188,
                    "inpkts_delta": 1,
                    "inpkts_total": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2005-11-25T00:16:41Z",
                            "effective_tld": "trafficmanager.net",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "www-www.bing.com.trafficmanager.NET",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 1748
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "www.bing.com.edgekey.NET",
                                    "host_type": "CNAME",
                                    "name": "www-www.bing.com.trafficmanager.NET",
                                    "section_type": "Answer",
                                    "ttl": 51
                                },
                                {
                                    "host": "e86303.dscx.akamaiedge.NET",
                                    "host_type": "CNAME",
                                    "name": "www.bing.com.edgekey.NET",
                                    "section_type": "Answer",
                                    "ttl": 20517
                                },
                                {
                                    "host_addr": "2.18.127.247",
                                    "host_type": "A",
                                    "name": "e86303.dscx.akamaiedge.NET",
                                    "section_type": "Answer",
                                    "ttl": 20
                                },
                                {
                                    "host_addr": "2.18.127.234",
                                    "host_type": "A",
                                    "name": "e86303.dscx.akamaiedge.NET",
                                    "section_type": "Answer",
                                    "ttl": 20
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2005-11-25T00:16:41Z",
                            "effective_tld": "trafficmanager.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 30,
                            "query": "www-www.bing.com.trafficmanager.NET",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "2.18.127.247",
                                "2.18.127.234"
                            ],
                            "response_time": 30,
                            "transaction_id": 1748
                        },
                        "transaction_id": 1748
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
                    "orig_id": "7D9Ak58BI3UnQyDO4Kcj",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 106,
                    "outbytes_total": 209,
                    "outpkts_delta": 1,
                    "outpkts_total": 2,
                    "port_name": "ethernet1",
                    "processing_time": 30,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784881926459,
                    "response_time": 30,
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
                    "srcport": 63144,
                    "start_bucket_time": 1784881800000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784882404741,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 474483,
                        "status": "New"
                    },
                    "stellar_da_input": 1655,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "696f6bfd-7eff-4675-a9d9-f3bc1d27d01e1784882404796-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784881926266,
                    "timestamp_utc": "2026-07-24T08:32:06.000Z",
                    "tos": 0,
                    "totalbytes": 316,
                    "totalpackets": 2,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784882404796,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 17.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 8.5) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "b6f2fac6-d9d2-4df3-9151-2602b6f6d9e91784885403067-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4651,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 66,
                    "aella_tuples": "192.168.169.119.10.11.1.1.445.185",
                    "anomaly_id": "DkBsk58BI3UnQyDO1eci",
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
                    "end_bucket_time": 1784885100000,
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
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 3
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 96.9,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "processing_time": 3,
                                "response_time": 6,
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
                                "response_time": 3,
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
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 1,
                                "response_time": 4
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
                                "processing_time": 1,
                                "response_time": 4,
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
                                "response_time": 3,
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
                                "response_time": 4,
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
                    "orig_id": "DkBsk58BI3UnQyDO1eci",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 6063,
                    "outbytes_total": 6063,
                    "outpkts_delta": 14,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784884807750,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.119",
                    "srcip": "192.168.169.119",
                    "srcip_assetid": "4ee27dbc-3cf6-11f1-94e3-72abedb727d0",
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
                    "srcip_host": "nb-noc2.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49738,
                    "start_bucket_time": 1784884800000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784885403051,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 592676,
                        "status": "New"
                    },
                    "stellar_da_input": 2075,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b6f2fac6-d9d2-4df3-9151-2602b6f6d9e91784885403067-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784884806501,
                    "timestamp_utc": "2026-07-24T09:20:06.000Z",
                    "tos": 0,
                    "totalbytes": 8656,
                    "totalpackets": 25,
                    "typical": 10,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784885403067,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.119, name: nb-noc2.technoma.local\" private) has sent an anomalously large number (#: 66) of SMB read requests, compared to its typical number (#: 10), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\SysVol very frequently.",
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