=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "37adb1dc-4db8-4b41-aff5-f19a6575e53e1784127004689-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11110,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5.5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "QhU4Zp8BI3UnQyDO3lY8",
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
                        "6-prod-dynamite-prod-09-us-signaler-pa.clients6.google.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.8.8",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_domain_creation": "1997-09-15T04:00:00Z",
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
                    "duration": 89,
                    "end_bucket_time": 1784126700000,
                    "end_reason": 1,
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
                    "file_extract_timestamp": 1784126429026,
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
                                        "id": 27246,
                                        "opcode": 0,
                                        "rrname": "relay-94cb70f6.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 105,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 61754,
                                "start": "2026-07-15T14:40:29.026729+0000"
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
                    "inbytes_delta": 179,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "1997-09-15T04:00:00Z",
                            "effective_tld": "google.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "6-prod-dynamite-prod-09-us-signaler-pa.clients6.google.com",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 22090
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns1.google.com",
                                    "host_type": "SOA",
                                    "name": "google.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 60
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "1997-09-15T04:00:00Z",
                            "effective_tld": "google.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 89,
                            "query": "6-prod-dynamite-prod-09-us-signaler-pa.clients6.google.com",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 89,
                            "transaction_id": 22090
                        },
                        "transaction_id": 22090
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
                    "orig_id": "QhU4Zp8BI3UnQyDO3lY8",
                    "orig_index": "aella-maltrace-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 129,
                    "outbytes_total": 105,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 89,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784126429418,
                    "response_time": 89,
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
                    "srcport": 61754,
                    "start_bucket_time": 1784126400000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784127004651,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 573879,
                        "status": "New"
                    },
                    "stellar_da_input": 1652,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "37adb1dc-4db8-4b41-aff5-f19a6575e53e1784127004689-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784126429232,
                    "timestamp_utc": "2026-07-15T14:40:29.000Z",
                    "tos": 0,
                    "totalbytes": 308,
                    "totalpackets": 2,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127004688,
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "58cbdf3f-5abe-41e0-8b5b-43e98857d82b1784127604120-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11123,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5.5,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.null",
                    "anomaly_id": "3RZCZp8BI3UnQyDOUlF7",
                    "anomaly_tag": "spike",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO Abused Hosting Domain in DNS Lookup (azurewebsites .net)",
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
                    "dstport": 53,
                    "end_bucket_time": 1784127300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 24,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2063117,
                                "ids_severity": "low",
                                "name": "INFO Abused Hosting Domain in DNS Lookup (azurewebsites .net)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 35.84,
                    "file_extract_timestamp": 1784127045303,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-06-20T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "Medium"
                            ],
                            "created_at": [
                                "2025_06_20"
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
                                "T1102"
                            ],
                            "mitre_technique_name": [
                                "Web_Service"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "updated_at": [
                                "2025_06_20"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 60572,
                                        "opcode": 0,
                                        "rrname": "app-pbi-wfe-brazil-south-v3.pbi-wfe-brazil-south-v3-ase.p.azurewebsites.NET",
                                        "rrtype": "A",
                                        "tx_id": 2,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 133,
                                "bytes_toserver": 267,
                                "dest_ip": "8.8.4.4",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 62566,
                                "start": "2026-07-15T14:47:05.499693+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_06_20",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Abused Hosting Domain in DNS Lookup (azurewebsites .net)\\\"; dns.query; dotprefix; content:\\\".azurewebsites.net\\\"; nocase; endswith; reference:url,azure.microsoft.com/en-us/products/app-service/web; classtype:misc-activity; sid:2063117; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_06_20, deployment Perimeter, performance_impact Low, confidence Medium, signature_severity Informational, updated_at 2025_06_20, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1102, mitre_technique_name Web_Service;)\\n\"",
                            "updated": "2025_06_20"
                        },
                        "severity": "low",
                        "signature": "INFO Abused Hosting Domain in DNS Lookup (azurewebsites .net)",
                        "signature_id": 2063117
                    },
                    "inbytes_total": 133,
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
                    "orig_id": "3RZCZp8BI3UnQyDOUlF7",
                    "orig_index": "aella-maltrace-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 267,
                    "outpkts_total": 2,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784127045773,
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
                    "srcip_sig_id": "10.11.1.1.2063117.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 62566,
                    "start_bucket_time": 1784127000000,
                    "stellar": {
                        "alert_time": 1784127604113,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 553811,
                        "status": "New"
                    },
                    "stellar_da_input": 1676,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "58cbdf3f-5abe-41e0-8b5b-43e98857d82b1784127604120-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784127045591,
                    "timestamp_utc": "2026-07-15T14:50:45.000Z",
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127604120,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 11.0) of exploit attempts with the IDS signature \"INFO Abused Hosting Domain in DNS Lookup (azurewebsites .net)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 5.5) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "327a7c3d-c79e-4677-807f-a99a26561b881784127602485-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11118,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 86,
                    "aella_tuples": "192.168.169.148.10.11.1.1.445.185",
                    "anomaly_id": "fBZDZp8BI3UnQyDOjnb7",
                    "app_path": "smb.dcerpc",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.148"
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
                    "duration": 113266,
                    "end_bucket_time": 1784127300000,
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
                    "fidelity": 98.12,
                    "flow_score": 100,
                    "inbytes_delta": 1372,
                    "inbytes_total": 224974,
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
                                "response_time": 3,
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
                                "response_time": 3,
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
                                "response_time": 3,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 2,
                                "response_time": 5,
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "fBZDZp8BI3UnQyDOjnb7",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1929,
                    "outbytes_total": 247459,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784127127104,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.148",
                    "srcip": "192.168.169.148",
                    "srcip_assetid": "ae01a7b0-cac7-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "NB-RVERON",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 64975,
                    "start_bucket_time": 1784127000000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784127602448,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 471934,
                        "status": "New"
                    },
                    "stellar_da_input": 1969,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "327a7c3d-c79e-4677-807f-a99a26561b881784127602485-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784127126904,
                    "timestamp_utc": "2026-07-15T14:52:06.000Z",
                    "tos": 0,
                    "totalbytes": 472433,
                    "totalpackets": 17,
                    "typical": 12,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127602485,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.148, name: NB-RVERON\" private) has sent an anomalously large number (#: 86) of SMB read requests, compared to its typical number (#: 12), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_id": "8028b51c-6507-4474-a88a-26941aa7f2c01784127602999-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11120,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 78,
                    "aella_tuples": "192.168.169.148.10.11.1.1.445.185",
                    "anomaly_id": "fBZDZp8BI3UnQyDOjnb7",
                    "app_path": "smb.dcerpc",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.148"
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
                    "duration": 113266,
                    "end_bucket_time": 1784127300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 54,
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
                    "fidelity": 98.84,
                    "flow_score": 100,
                    "inbytes_delta": 1372,
                    "inbytes_total": 224974,
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
                                "response_time": 3,
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
                                "response_time": 3,
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
                                "response_time": 3,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 2,
                                "response_time": 5,
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "fBZDZp8BI3UnQyDOjnb7",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1929,
                    "outbytes_total": 247459,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784127127104,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.148",
                    "srcip": "192.168.169.148",
                    "srcip_assetid": "ae01a7b0-cac7-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "NB-RVERON",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 64975,
                    "start_bucket_time": 1784127000000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784127602969,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 472455,
                        "status": "New"
                    },
                    "stellar_da_input": 1969,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8028b51c-6507-4474-a88a-26941aa7f2c01784127602999-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784127126904,
                    "timestamp_utc": "2026-07-15T14:52:06.000Z",
                    "tos": 0,
                    "totalbytes": 472433,
                    "totalpackets": 17,
                    "typical": 3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127602999,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.148, name: NB-RVERON\" private) has sent an anomalously large number (#: 78) of SMB write requests, compared to its typical number (#: 3), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_id": "e5bbc485-2d28-477e-8acb-3c03eba533351784127603502-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11122,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 58,
                    "aella_tuples": "192.168.169.160.10.11.1.1.445.185",
                    "anomaly_id": "FBZDZp8BI3UnQyDO2n3Q",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.160"
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
                    "end_bucket_time": 1784127300000,
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
                            "\\\\ad.technoma.local\\IPC$",
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 2
                            },
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 3
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 88.81,
                    "flow_score": 100,
                    "inbytes_delta": 2720,
                    "inbytes_total": 2720,
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
                                "processing_time": 0,
                                "response_time": 1,
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
                                "response_time": 1,
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
                                "response_time": 1,
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
                                "response_time": 1,
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
                    "orig_id": "FBZDZp8BI3UnQyDO2n3Q",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 6319,
                    "outbytes_total": 6319,
                    "outpkts_delta": 16,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784127141010,
                    "response_time": 1,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.160",
                    "srcip": "192.168.169.160",
                    "srcip_assetid": "0b223916-7624-11f1-bdbf-be2f2074df47",
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
                    "srcip_host": "NB-LCACERES",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 60193,
                    "start_bucket_time": 1784127000000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784127602484,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 452314,
                        "status": "New"
                    },
                    "stellar_da_input": 2048,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e5bbc485-2d28-477e-8acb-3c03eba533351784127603502-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 1,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784127140353,
                    "timestamp_utc": "2026-07-15T14:52:20.000Z",
                    "tos": 0,
                    "totalbytes": 9039,
                    "totalpackets": 27,
                    "typical": 12,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127603502,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.160, name: NB-LCACERES\" private) has sent an anomalously large number (#: 58) of SMB read requests, compared to its typical number (#: 12), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$, \\\\ad.technoma.local\\SysVol very frequently.",
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
                "_id": "22b4c9e4-62fa-4e98-aef0-bd27affd88c31784127602999-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11121,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 0.7867992836443896,
                    "aella_tuples": "192.168.169.160.10.11.1.1.445.26",
                    "anomaly_id": "pRZEZp8BI3UnQyDOxpfH",
                    "app_path": "smb",
                    "appid": 26,
                    "appid_family": "Middleware",
                    "appid_name": "dcerpc",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "dstip_type",
                        "appid_name"
                    ],
                    "detected_values": [
                        "192.168.169.160",
                        "private",
                        "dcerpc"
                    ],
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
                    "end_bucket_time": 1784127300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 26,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 78.68,
                    "flow_score": 100,
                    "inbytes_delta": 2287,
                    "inbytes_total": 2287,
                    "inpkts_delta": 11,
                    "locid": "unassigned location",
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
                                "path": "\\\\AD\\IPC$",
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
                                "command": 5,
                                "filename": "samr"
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
                                "processing_time": 0,
                                "response_time": 2
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
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "num_clust": 2,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "pRZEZp8BI3UnQyDOxpfH",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 5542,
                    "outbytes_total": 5542,
                    "outpkts_delta": 14,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784127202825,
                    "response_time": 2,
                    "severity": 15,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.160",
                    "srcip": "192.168.169.160",
                    "srcip_assetid": "0b223916-7624-11f1-bdbf-be2f2074df47",
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
                    "srcip_host": "NB-LCACERES",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 56259,
                    "start_bucket_time": 1784127000000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784127602987,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 392708,
                        "status": "New"
                    },
                    "stellar_da_input": 1918,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "22b4c9e4-62fa-4e98-aef0-bd27affd88c31784127602999-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "sum_clust_size": 151,
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784127201656,
                    "timestamp_utc": "2026-07-15T14:53:21.000Z",
                    "tos": 0,
                    "totalbytes": 7829,
                    "totalpackets": 25,
                    "training_days": 7,
                    "typical": 0.7,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784127602999,
                    "xdr_event": {
                        "description": "The usage pattern from 192.168.169.160 of private dcerpc is unusual compared to other 2 different types of usage patterns observed from 151 source IP addresses in the past 7 days.",
                        "display_name": "Internal Protocol Pattern Anomaly",
                        "framework_version": "v17",
                        "name": "internal_appflow_outlier",
                        "scope": "Internal",
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Network Traffic Analysis",
                            "Internal"
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