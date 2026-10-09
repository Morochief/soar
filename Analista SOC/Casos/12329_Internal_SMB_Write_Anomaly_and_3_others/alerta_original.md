=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "747ee1df-e877-4d9c-a1cf-b27998bcbca81784294702530-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14386,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 3.5,
                    "aella_tuples": "192.168.169.144.10.11.1.1.53.32",
                    "anomaly_id": "uaw6cJ8BI3UnQyDO9jVs",
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
                        "INFO Observed Discord Domain in DNS Lookup (discord .com)",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "status.discord.com"
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
                    "end_bucket_time": 1784294400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 25,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2035465,
                                "ids_severity": "low",
                                "name": "INFO Observed Discord Domain in DNS Lookup (discord .com)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 24.49,
                    "file_extract_timestamp": 1784294339270,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2022-03-15T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2022_03_15"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Description_Generated_By_Proofpoint_Nexus"
                            ],
                            "updated_at": [
                                "2022_11_30"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 49174,
                                        "opcode": 0,
                                        "rrname": "status.discord.com",
                                        "rrtype": "A",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 82,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.144",
                                "src_port": 64515,
                                "start": "2026-07-17T13:18:59.270150+0000"
                            }
                        },
                        "rev": 4,
                        "rule": {
                            "created": "2022_03_15",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Observed Discord Domain in DNS Lookup (discord .com)\\\"; dns.query; dotprefix; content:\\\".discord.com\\\"; endswith; reference:md5,03f93498e1006ffa3a1f9fcb6170525a; classtype:misc-activity; sid:2035465; rev:4; metadata:created_at 2022_03_15, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2022_11_30;)\\n\"",
                            "updated": "2022_11_30"
                        },
                        "severity": "low",
                        "signature": "INFO Observed Discord Domain in DNS Lookup (discord .com)",
                        "signature_id": 2035465
                    },
                    "inbytes_delta": 391,
                    "inbytes_total": 0,
                    "inpkts_delta": 2,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_shouldDup": "true",
                        "_whitelist": 0,
                        "is_tunneling": 2,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2000-11-06T11:45:38Z",
                            "effective_tld": "discord.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "status.discord.com",
                            "query_type": "A",
                            "transaction_id": 49174
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "162.159.135.232",
                                    "host_type": "A",
                                    "name": "status.discord.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                },
                                {
                                    "host_addr": "162.159.138.232",
                                    "host_type": "A",
                                    "name": "status.discord.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                },
                                {
                                    "host_addr": "162.159.128.233",
                                    "host_type": "A",
                                    "name": "status.discord.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                },
                                {
                                    "host_addr": "162.159.136.232",
                                    "host_type": "A",
                                    "name": "status.discord.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                },
                                {
                                    "host_addr": "162.159.137.232",
                                    "host_type": "A",
                                    "name": "status.discord.com",
                                    "section_type": "Answer",
                                    "ttl": 299
                                }
                            ],
                            "domain_creation": "2000-11-06T11:45:38Z",
                            "effective_tld": "discord.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 30,
                            "query": "status.discord.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "162.159.135.232",
                                "162.159.138.232",
                                "162.159.128.233",
                                "162.159.136.232",
                                "162.159.137.232"
                            ],
                            "response_time": 30,
                            "transaction_id": 49174
                        },
                        "transaction_id": 49174
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
                    "orig_id": "uaw6cJ8BI3UnQyDO9jVs",
                    "orig_index": "aella-maltrace-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 282,
                    "outbytes_total": 82,
                    "outpkts_delta": 3,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 10,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784294339994,
                    "response_time": 10,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.144",
                    "srcip": "192.168.169.144",
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
                    "srcip_host": "192.168.169.144",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.144.2035465.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 64515,
                    "start_bucket_time": 1784294100000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784294702511,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 362317,
                        "status": "New"
                    },
                    "stellar_da_input": 1411,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "747ee1df-e877-4d9c-a1cf-b27998bcbca81784294702530-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784294339729,
                    "timestamp_utc": "2026-07-17T13:18:59.000Z",
                    "tos": 0,
                    "totalbytes": 673,
                    "totalpackets": 5,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784294702530,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 7.0) of exploit attempts with the IDS signature \"INFO Observed Discord Domain in DNS Lookup (discord .com)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 3.5) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "48bcc38a-6172-4c1f-abe6-d7e0e7b9a4ff1784295002889-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14391,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 12.5,
                    "aella_tuples": "192.168.169.124.10.11.1.1.53.null",
                    "anomaly_id": "D6w8cJ8BI3UnQyDOCVTl",
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
                    "dstport": 53,
                    "end_bucket_time": 1784294700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 28,
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
                    "fidelity": 33.64,
                    "file_extract_timestamp": 1784294405964,
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
                                        "id": 44345,
                                        "opcode": 0,
                                        "rrname": "relay-94cb70f6.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 6,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 538,
                                "bytes_toserver": 353,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 3,
                                "pkts_toserver": 4,
                                "src_ip": "192.168.169.124",
                                "src_port": 49789,
                                "start": "2026-07-17T13:20:04.356535+0000"
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
                    "inbytes_total": 538,
                    "inpkts_total": 3,
                    "is_dga": "no",
                    "lateral": true,
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
                    "orig_id": "D6w8cJ8BI3UnQyDOCVTl",
                    "orig_index": "aella-maltrace-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 353,
                    "outpkts_total": 4,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784294406456,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.124",
                    "srcip": "192.168.169.124",
                    "srcip_assetid": "5865af62-eaf8-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "192.168.169.124",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.124.2060507.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 49789,
                    "start_bucket_time": 1784294400000,
                    "stellar": {
                        "alert_time": 1784295002868,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 592163,
                        "status": "New"
                    },
                    "stellar_da_input": 1672,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "48bcc38a-6172-4c1f-abe6-d7e0e7b9a4ff1784295002889-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784294406277,
                    "timestamp_utc": "2026-07-17T13:20:06.000Z",
                    "typical": 1.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784295002889,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 25.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 12.5) from the typical value of (#: 1.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "aab61bf8-9da0-4713-9f00-efb5ce5f7d241784295003923-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14394,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 1.5,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "anomaly_id": "46w_cJ8BI3UnQyDOscS0",
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
                        "INFO Discord Chat Service Domain in DNS Lookup (discord .com)",
                        "low"
                    ],
                    "direction": "EveTxRx",
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
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 3631,
                    "end_bucket_time": 1784294700000,
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
                                "id": 2060503,
                                "ids_severity": "low",
                                "name": "INFO Discord Chat Service Domain in DNS Lookup (discord .com)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 63.51,
                    "file_extract_timestamp": 1784294645707,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-02-28T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_02_28"
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
                                "T1573"
                            ],
                            "mitre_technique_name": [
                                "Encrypted_Channel"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Chat_Service",
                                "Discord"
                            ],
                            "updated_at": [
                                "2025_02_28"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 23917,
                                        "opcode": 0,
                                        "rrname": "discord.com",
                                        "rrtype": "HTTPS",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 259,
                                "bytes_toserver": 201,
                                "dest_ip": "8.8.4.4",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 63042,
                                "start": "2026-07-17T13:21:04.000576+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_02_28",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Discord Chat Service Domain in DNS Lookup (discord .com)\\\"; dns.query; bsize:11; content:\\\"discord.com\\\"; nocase; reference:url,discord.com/developers/docs/events/gateway; classtype:misc-activity; sid:2060503; rev:1; metadata:affected_product Any, attack_target Client_Endpoint, created_at 2025_02_28, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag Discord, tag Chat_Service, updated_at 2025_02_28, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1573, mitre_technique_name Encrypted_Channel;)\\n\"",
                            "updated": "2025_02_28"
                        },
                        "severity": "low",
                        "signature": "INFO Discord Chat Service Domain in DNS Lookup (discord .com)",
                        "signature_id": 2060503
                    },
                    "inbytes_delta": 449,
                    "inbytes_total": 259,
                    "inpkts_delta": 1,
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
                    "msgtype": 2,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "46w_cJ8BI3UnQyDOscS0",
                    "orig_index": "aella-maltrace-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 0,
                    "outbytes_total": 201,
                    "outpkts_delta": 0,
                    "outpkts_total": 2,
                    "port_name": "ethernet1",
                    "processing_time": 24,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784294646149,
                    "response_time": 24,
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
                    "srcip_sig_id": "10.11.1.1.2060503.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 63042,
                    "start_bucket_time": 1784294400000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784295003853,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 353582,
                        "status": "New"
                    },
                    "stellar_da_input": 1651,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "aab61bf8-9da0-4713-9f00-efb5ce5f7d241784295003923-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784294645950,
                    "timestamp_utc": "2026-07-17T13:24:05.000Z",
                    "tos": 0,
                    "totalbytes": 834,
                    "totalpackets": 1,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784295003923,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 3.0) of exploit attempts with the IDS signature \"INFO Discord Chat Service Domain in DNS Lookup (discord .com)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 1.5) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "bbeea7be-5bb1-4652-9cd6-c812834bdc061784295003619-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14393,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 24,
                    "aella_tuples": "192.168.169.85.10.11.1.1.445.185",
                    "anomaly_id": "vaxAcJ8BI3UnQyDOKdK8",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.85"
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
                    "duration": 1314,
                    "end_bucket_time": 1784294700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 51,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [],
                        "smb_path_summary": []
                    },
                    "event_type": "conn",
                    "fidelity": 81.05,
                    "flow_score": 100,
                    "inbytes_delta": 1570,
                    "inbytes_total": 14413,
                    "inpkts_delta": 9,
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
                                "command": 6,
                                "version": 2
                            },
                            "response": {
                                "command": 6,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 4,
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
                                "processing_time": 2,
                                "response_time": 6,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
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
                    "orig_id": "vaxAcJ8BI3UnQyDOKdK8",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1993,
                    "outbytes_total": 17463,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784294671550,
                    "response_time": 4,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.85",
                    "srcip": "192.168.169.85",
                    "srcip_assetid": "5689b254-d6af-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "nb-oscandia.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 41369,
                    "start_bucket_time": 1784294400000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784295003594,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 323375,
                        "status": "New"
                    },
                    "stellar_da_input": 1932,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bbeea7be-5bb1-4652-9cd6-c812834bdc061784295003619-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784294671179,
                    "timestamp_utc": "2026-07-17T13:24:31.000Z",
                    "tos": 0,
                    "totalbytes": 31876,
                    "totalpackets": 18,
                    "typical": 3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784295003619,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.85, name: nb-oscandia.technoma.local\" private) has sent an anomalously large number (#: 24) of SMB write requests, compared to its typical number (#: 3), measured in a 5.0-minute interval.",
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