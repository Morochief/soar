=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6e802b32-91ae-486f-95bf-08d4605cdddd1783613403411-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 7030,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 3,
                    "aella_tuples": "192.168.169.12.10.11.1.1.53.32",
                    "anomaly_id": "dB6cR58BBi0xHyA-kKW3",
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
                        "boot.net.anydesk.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "25b83024-f2ed-11f0-8ce2-3a0341ec6ca6",
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
                    "duration": 32,
                    "end_bucket_time": 1783613100000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 47,
                    "event_source": "new_ml",
                    "event_status": "New",
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
                    "file_extract_timestamp": 1783612867021,
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
                                        "id": 34069,
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
                                "src_ip": "192.168.169.12",
                                "src_port": 53416,
                                "start": "2026-07-09T16:01:07.021163+0000"
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
                    "inbytes_delta": 234,
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
                            "query": "boot.net.anydesk.com",
                            "query_type": "A",
                            "transaction_id": 34069
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "boot-relays.net.anydesk.com",
                                    "host_type": "CNAME",
                                    "name": "boot.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "141.95.145.210",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "57.128.101.74",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "195.181.174.173",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "57.128.101.77",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "195.181.174.174",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "57.128.101.78",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "57.128.101.75",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_addr": "37.59.29.33",
                                    "host_type": "A",
                                    "name": "boot-relays.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                }
                            ],
                            "domain_creation": "2004-02-07T15:49:37Z",
                            "effective_tld": "anydesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 32,
                            "query": "boot.net.anydesk.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "141.95.145.210",
                                "57.128.101.74",
                                "195.181.174.173",
                                "57.128.101.77",
                                "195.181.174.174",
                                "57.128.101.78",
                                "57.128.101.75",
                                "37.59.29.33"
                            ],
                            "response_time": 32,
                            "transaction_id": 34069
                        },
                        "transaction_id": 34069
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
                    "orig_id": "dB6cR58BBi0xHyA-kKW3",
                    "orig_index": "aella-maltrace-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 80,
                    "outbytes_total": 84,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 32,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1783612867433,
                    "response_time": 32,
                    "score": 30,
                    "severity": 75,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.12",
                    "srcip": "192.168.169.12",
                    "srcip_assetid": "6c60bfa2-cb90-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-kmoraez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.12.2060512.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 53416,
                    "start_bucket_time": 1783612800000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1783613403403,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 532595,
                        "status": "New"
                    },
                    "stellar_da_input": 1654,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6e802b32-91ae-486f-95bf-08d4605cdddd1783613403411-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783612867238,
                    "timestamp_utc": "2026-07-09T16:01:07.000Z",
                    "tos": 0,
                    "totalbytes": 314,
                    "totalpackets": 2,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783613403411,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 6.0) of exploit attempts with the IDS signature \"INFO Anydesk Domain (boot .net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 3.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Private to Private Exploit Anomaly",
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
                "_id": "a4b73368-7055-4e80-a5e6-79bc8106471d1783613702351-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 7034,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 83,
                    "aella_tuples": "192.168.169.99.10.11.1.1.445.185",
                    "anomaly_id": "_R-hR58BBi0xHyA-6Q-9",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.99"
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
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 445,
                    "duration": 235985,
                    "end_bucket_time": 1783613400000,
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
                            "\\\\ad.technoma.local\\sysvol",
                            "\\\\10.11.1.5\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\sysvol",
                                "value": 2
                            },
                            {
                                "key": "\\\\10.11.1.5\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 97.64,
                    "flow_score": 100,
                    "inbytes_delta": 2056,
                    "inbytes_total": 725984,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "metadata": [
                        {
                            "request": {
                                "command": 1,
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 3,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\sysvol",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 1,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{31B2F340-016D-11D2-945F-00C04FB984F9}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 1,
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
                                "response_time": 1,
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
                                "response_time": 1,
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
                                "response_time": 1,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{87B52B57-07B6-4758-9B97-96AA41B2A7B6}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 1,
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
                                "response_time": 1,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            },
                            "response": {
                                "processing_time": 0,
                                "response_time": 1,
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "_R-hR58BBi0xHyA-6Q-9",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 5987,
                    "outbytes_total": 113677,
                    "outpkts_delta": 12,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783613214082,
                    "response_time": 1,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.99",
                    "srcip": "192.168.169.99",
                    "srcip_assetid": "a3278434-5f48-11f1-ba15-5ae6db116d2f",
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
                    "srcip_host": "nb-aruiz.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 64531,
                    "start_bucket_time": 1783613100000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783613702320,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 481604,
                        "status": "New"
                    },
                    "stellar_da_input": 2106,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a4b73368-7055-4e80-a5e6-79bc8106471d1783613702351-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 1,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783613213664,
                    "timestamp_utc": "2026-07-09T16:06:53.000Z",
                    "tos": 0,
                    "totalbytes": 839661,
                    "totalpackets": 21,
                    "typical": 14,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783613702351,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.99, name: nb-aruiz.technoma.local\" private) has sent an anomalously large number (#: 83) of SMB read requests, compared to its typical number (#: 14), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\sysvol, \\\\10.11.1.5\\IPC$ very frequently.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "f225d6c4-25b9-4d89-9bd4-abad3a5309fd1783614902536-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 7088,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 63,
                    "aella_tuples": "192.168.169.84.10.11.1.1.445.185",
                    "anomaly_id": "eyC2R58BBi0xHyA-NpzT",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.84"
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
                    "duration": 2170,
                    "end_bucket_time": 1783614600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 3
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 90.78,
                    "flow_score": 100,
                    "inbytes_delta": 2264,
                    "inbytes_total": 102407,
                    "inpkts_delta": 17,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\IPC$",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "filename": "lsarpc",
                                "version": 2
                            },
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 0,
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
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 9,
                                "processing_time": 1,
                                "response_time": 5
                            }
                        },
                        {
                            "request": {
                                "command": 16,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 8,
                                "processing_time": 0,
                                "response_time": 4
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
                                "command": 8
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "eyC2R58BBi0xHyA-NpzT",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2546,
                    "outbytes_total": 93114,
                    "outpkts_delta": 15,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783614546220,
                    "response_time": 4,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.84",
                    "srcip": "192.168.169.84",
                    "srcip_assetid": "fe9206f2-cf7c-11f0-bc8a-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.84",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54652,
                    "start_bucket_time": 1783614300000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783614902528,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 351619,
                        "status": "New"
                    },
                    "stellar_da_input": 2026,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f225d6c4-25b9-4d89-9bd4-abad3a5309fd1783614902536-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783614545569,
                    "timestamp_utc": "2026-07-09T16:29:05.000Z",
                    "tos": 0,
                    "totalbytes": 195521,
                    "totalpackets": 32,
                    "typical": 14,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783614902536,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.84\" private) has sent an anomalously large number (#: 63) of SMB read requests, compared to its typical number (#: 14), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "45e63d5d-4623-47fc-ad1f-f5c436f06b871783614902536-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 7089,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 30,
                    "aella_tuples": "192.168.169.84.10.11.1.1.445.185",
                    "anomaly_id": "eyC2R58BBi0xHyA-NpzT",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.84"
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
                    "duration": 2170,
                    "end_bucket_time": 1783614600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 51,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 2
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 81.02,
                    "flow_score": 100,
                    "inbytes_delta": 2264,
                    "inbytes_total": 102407,
                    "inpkts_delta": 17,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\IPC$",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "filename": "lsarpc",
                                "version": 2
                            },
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 0,
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
                                "processing_time": 0,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 9,
                                "processing_time": 1,
                                "response_time": 5
                            }
                        },
                        {
                            "request": {
                                "command": 16,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 8,
                                "processing_time": 0,
                                "response_time": 4
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
                                "command": 8
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "eyC2R58BBi0xHyA-NpzT",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2546,
                    "outbytes_total": 93114,
                    "outpkts_delta": 15,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783614546220,
                    "response_time": 4,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.84",
                    "srcip": "192.168.169.84",
                    "srcip_assetid": "fe9206f2-cf7c-11f0-bc8a-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.84",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54652,
                    "start_bucket_time": 1783614300000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783614902528,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 351619,
                        "status": "New"
                    },
                    "stellar_da_input": 2026,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "45e63d5d-4623-47fc-ad1f-f5c436f06b871783614902536-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783614545569,
                    "timestamp_utc": "2026-07-09T16:29:05.000Z",
                    "tos": 0,
                    "totalbytes": 195521,
                    "totalpackets": 32,
                    "typical": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783614902536,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.84\" private) has sent an anomalously large number (#: 30) of SMB write requests, compared to its typical number (#: 4), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
                        "display_name": "Internal SMB Write Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_anomaly",
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
                            "id": "T1021",
                            "name": "Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "53be126e-2b7d-4e09-8baf-03f075d8c6df1783614903557-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 7090,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 34,
                    "aella_tuples": "192.168.169.113.10.11.1.1.445.185",
                    "anomaly_id": "YCC2R58BBi0xHyA-XqAw",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.113"
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
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 445,
                    "duration": 83081,
                    "end_bucket_time": 1783614600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 91.12,
                    "flow_score": 100,
                    "inbytes_delta": 1372,
                    "inbytes_total": 754850,
                    "inpkts_delta": 8,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\IPC$",
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
                                "command": 5,
                                "filename": "lsarpc",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 1,
                                "response_time": 3,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
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
                                "processing_time": 0,
                                "response_time": 2,
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "YCC2R58BBi0xHyA-XqAw",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1929,
                    "outbytes_total": 130487,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783614556567,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.113",
                    "srcip": "192.168.169.113",
                    "srcip_assetid": "52fba076-f7b5-11f0-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-jdurand.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 50191,
                    "start_bucket_time": 1783614300000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783614902691,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 341735,
                        "status": "New"
                    },
                    "stellar_da_input": 1944,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "53be126e-2b7d-4e09-8baf-03f075d8c6df1783614903557-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783614555797,
                    "timestamp_utc": "2026-07-09T16:29:15.000Z",
                    "tos": 0,
                    "totalbytes": 885337,
                    "totalpackets": 17,
                    "typical": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783614903557,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.113, name: nb-jdurand.technoma.local\" private) has sent an anomalously large number (#: 34) of SMB write requests, compared to its typical number (#: 4), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
                        "display_name": "Internal SMB Write Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_anomaly",
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
                            "id": "T1021",
                            "name": "Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}