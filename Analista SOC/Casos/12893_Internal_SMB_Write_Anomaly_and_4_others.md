=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "f414cda3-19b9-49a0-b65c-eaaa6d971a711785574803328-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14667,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1.5,
                    "aella_tuples": "192.168.169.179.10.11.1.1.53.32",
                    "anomaly_id": "hBSEvJ8BI3UnQyDOsNtX",
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
                        "INFO RustDesk Relay Domain in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "rs-ny.rustdesk.com"
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
                    "duration": 34,
                    "end_bucket_time": 1785574500000,
                    "end_reason": 1,
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
                                "id": 2044076,
                                "ids_severity": "low",
                                "name": "INFO RustDesk Relay Domain in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 63.51,
                    "file_extract_timestamp": 1785574230137,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2023-02-02T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2023_02_02"
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
                                "2023_02_02"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 32114,
                                        "opcode": 0,
                                        "rrname": "rs-ny.rustdesk.com",
                                        "rrtype": "AAAA",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 93,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.179",
                                "src_port": 45601,
                                "start": "2026-08-01T08:50:30.137349+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2023_02_02",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO RustDesk Relay Domain in DNS Lookup\\\"; dns.query; content:\\\"rs-\\\"; startswith; fast_pattern; pcre:\\\"/[a-z]{2}/Ri\\\"; dotprefix; content:\\\".rustdesk.com\\\"; nocase; endswith; reference:url,rustdesk.com; classtype:misc-activity; sid:2044076; rev:1; metadata:attack_target Client_Endpoint, created_at 2023_02_02, deployment Perimeter, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2023_02_02;)\\n\"",
                            "updated": "2023_02_02"
                        },
                        "severity": "low",
                        "signature": "INFO RustDesk Relay Domain in DNS Lookup",
                        "signature_id": 2044076
                    },
                    "inbytes_delta": 150,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 9,
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "section_type": "Additional Answer",
                            "transaction_id": 32114
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "sierra.ns.cloudflare.com",
                                    "host_type": "SOA",
                                    "name": "rustdesk.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 104
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 34,
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 34,
                            "transaction_id": 32114
                        },
                        "transaction_id": 32114
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
                    "orig_id": "hBSEvJ8BI3UnQyDOsNtX",
                    "orig_index": "aella-maltrace-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 89,
                    "outbytes_total": 93,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 34,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1785574230753,
                    "response_time": 34,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.179",
                    "srcip": "192.168.169.179",
                    "srcip_assetid": "886043da-7b30-11f1-bb76-be2f2074df47",
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
                    "srcip_host": "192.168.169.179",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.179.2044076.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 45601,
                    "start_bucket_time": 1785574200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785574803267,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 562992,
                        "status": "New"
                    },
                    "stellar_da_input": 1460,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f414cda3-19b9-49a0-b65c-eaaa6d971a711785574803328-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785574230532,
                    "timestamp_utc": "2026-08-01T08:50:30.000Z",
                    "tos": 0,
                    "totalbytes": 239,
                    "totalpackets": 2,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785574803327,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 3.0) of exploit attempts with the IDS signature \"INFO RustDesk Relay Domain in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 1.5) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "760e01e5-6ce0-45ce-84a7-81ecf4bc8bc81785576603424-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14688,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 2,
                    "aella_tuples": "192.168.169.151.10.11.1.1.53.32",
                    "anomaly_id": "8hWivJ8BI3UnQyDOI8U7",
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
                        "INFO RustDesk Relay Domain in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "rs-ny.rustdesk.com"
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
                    "duration": 28,
                    "end_bucket_time": 1785576300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 38,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2044076,
                                "ids_severity": "low",
                                "name": "INFO RustDesk Relay Domain in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 90.51,
                    "file_extract_timestamp": 1785576162902,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2023-02-02T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2023_02_02"
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
                                "2023_02_02"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 43658,
                                        "opcode": 0,
                                        "rrname": "rs-ny.rustdesk.com",
                                        "rrtype": "AAAA",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 93,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.151",
                                "src_port": 35271,
                                "start": "2026-08-01T09:22:42.902238+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2023_02_02",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO RustDesk Relay Domain in DNS Lookup\\\"; dns.query; content:\\\"rs-\\\"; startswith; fast_pattern; pcre:\\\"/[a-z]{2}/Ri\\\"; dotprefix; content:\\\".rustdesk.com\\\"; nocase; endswith; reference:url,rustdesk.com; classtype:misc-activity; sid:2044076; rev:1; metadata:attack_target Client_Endpoint, created_at 2023_02_02, deployment Perimeter, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2023_02_02;)\\n\"",
                            "updated": "2023_02_02"
                        },
                        "severity": "low",
                        "signature": "INFO RustDesk Relay Domain in DNS Lookup",
                        "signature_id": 2044076
                    },
                    "inbytes_delta": 150,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 9,
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "section_type": "Additional Answer",
                            "transaction_id": 43658
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "sierra.ns.cloudflare.com",
                                    "host_type": "SOA",
                                    "name": "rustdesk.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 900
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 28,
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 28,
                            "transaction_id": 43658
                        },
                        "transaction_id": 43658
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
                    "orig_id": "8hWivJ8BI3UnQyDOI8U7",
                    "orig_index": "aella-maltrace-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 89,
                    "outbytes_total": 93,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 28,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1785576163422,
                    "response_time": 28,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.151",
                    "srcip": "192.168.169.151",
                    "srcip_assetid": "cdb3768c-cf78-11f0-bc8a-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.151",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.151.2044076.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 35271,
                    "start_bucket_time": 1785576000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785576603404,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 433123,
                        "status": "New"
                    },
                    "stellar_da_input": 1460,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "760e01e5-6ce0-45ce-84a7-81ecf4bc8bc81785576603424-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785576163126,
                    "timestamp_utc": "2026-08-01T09:22:43.000Z",
                    "tos": 0,
                    "totalbytes": 239,
                    "totalpackets": 2,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785576603424,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 4.0) of exploit attempts with the IDS signature \"INFO RustDesk Relay Domain in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 2.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "86b8981e-9881-4385-a0e1-3803926d763c1785577202781-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14692,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 2.5,
                    "aella_tuples": "192.168.169.151.10.11.1.1.53.32",
                    "anomaly_id": "qhaqvJ8BI3UnQyDO_AiY",
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
                        "INFO RustDesk Relay Domain in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "rs-ny.rustdesk.com"
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
                    "duration": 0,
                    "end_bucket_time": 1785576900000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 39,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2044076,
                                "ids_severity": "low",
                                "name": "INFO RustDesk Relay Domain in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 97.8,
                    "file_extract_timestamp": 1785576739892,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2023-02-02T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2023_02_02"
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
                                "2023_02_02"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 16210,
                                        "opcode": 0,
                                        "rrname": "rs-ny.rustdesk.com",
                                        "rrtype": "AAAA",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 93,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.151",
                                "src_port": 51834,
                                "start": "2026-08-01T09:32:19.892221+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2023_02_02",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO RustDesk Relay Domain in DNS Lookup\\\"; dns.query; content:\\\"rs-\\\"; startswith; fast_pattern; pcre:\\\"/[a-z]{2}/Ri\\\"; dotprefix; content:\\\".rustdesk.com\\\"; nocase; endswith; reference:url,rustdesk.com; classtype:misc-activity; sid:2044076; rev:1; metadata:attack_target Client_Endpoint, created_at 2023_02_02, deployment Perimeter, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2023_02_02;)\\n\"",
                            "updated": "2023_02_02"
                        },
                        "severity": "low",
                        "signature": "INFO RustDesk Relay Domain in DNS Lookup",
                        "signature_id": 2044076
                    },
                    "inbytes_delta": 150,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 9,
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "section_type": "Additional Answer",
                            "transaction_id": 16210
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "sierra.ns.cloudflare.com",
                                    "host_type": "SOA",
                                    "name": "rustdesk.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 323
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2020-07-01T14:00:21Z",
                            "effective_tld": "rustdesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "rs-ny.rustdesk.com",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 0,
                            "transaction_id": 16210
                        },
                        "transaction_id": 16210
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
                    "orig_id": "qhaqvJ8BI3UnQyDO_AiY",
                    "orig_index": "aella-maltrace-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 89,
                    "outbytes_total": 93,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1785576740144,
                    "response_time": 0,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.151",
                    "srcip": "192.168.169.151",
                    "srcip_assetid": "cdb3768c-cf78-11f0-bc8a-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.151",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.151.2044076.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51834,
                    "start_bucket_time": 1785576600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785577202770,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 452587,
                        "status": "New"
                    },
                    "stellar_da_input": 1460,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "86b8981e-9881-4385-a0e1-3803926d763c1785577202781-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785576739943,
                    "timestamp_utc": "2026-08-01T09:32:19.000Z",
                    "tos": 0,
                    "totalbytes": 239,
                    "totalpackets": 2,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785577202780,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 5.0) of exploit attempts with the IDS signature \"INFO RustDesk Relay Domain in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 2.5) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "a00222a5-f123-44f2-ab08-b14ef33ebe7e1785579902558-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14695,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 14,
                    "aella_tuples": "192.168.169.48.10.11.1.1.445.185",
                    "anomaly_id": "FxfWvJ8BI3UnQyDOLUx4",
                    "app_path": "smb.dcerpc",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.48"
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
                    "duration": 42469,
                    "end_bucket_time": 1785579600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 38,
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
                    "fidelity": 34.06,
                    "flow_score": 100,
                    "inbytes_delta": 2182,
                    "inbytes_total": 777245,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
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
                    "orig_id": "FxfWvJ8BI3UnQyDOLUx4",
                    "orig_index": "aella-adr-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2002,
                    "outbytes_total": 155247,
                    "outpkts_delta": 10,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785579578112,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.48",
                    "srcip": "192.168.169.48",
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
                    "srcip_host": "nb-mjcasanas.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 58774,
                    "start_bucket_time": 1785579300000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1785579902536,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 322191,
                        "status": "New"
                    },
                    "stellar_da_input": 1970,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a00222a5-f123-44f2-ab08-b14ef33ebe7e1785579902558-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785579576999,
                    "timestamp_utc": "2026-08-01T10:19:36.000Z",
                    "tos": 0,
                    "totalbytes": 932492,
                    "totalpackets": 19,
                    "typical": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785579902557,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.48, name: nb-mjcasanas.technoma.local\" private) has sent an anomalously large number (#: 14) of SMB write requests, compared to its typical number (#: 2), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ec3b6adc-9edd-4eca-844d-c712810e0d441785580202977-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14696,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 23,
                    "aella_tuples": "192.168.169.2.10.11.1.1.445.185",
                    "anomaly_id": "RhfYvJ8BI3UnQyDO7GVr",
                    "app_path": "smb.dcerpc",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.2"
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
                    "duration": 100486,
                    "end_bucket_time": 1785579900000,
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
                    "fidelity": 92.98,
                    "flow_score": 100,
                    "inbytes_delta": 1609,
                    "inbytes_total": 794467,
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
                                "processing_time": 2,
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
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "samr",
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
                    "orig_id": "RhfYvJ8BI3UnQyDO7GVr",
                    "orig_index": "aella-adr-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 5628,
                    "outbytes_total": 183362,
                    "outpkts_delta": 11,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785579752316,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.2",
                    "srcip": "192.168.169.2",
                    "srcip_assetid": "a0db7a80-df6b-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "NB-FCANDIA",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 55865,
                    "start_bucket_time": 1785579600000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1785580202955,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 442760,
                        "status": "New"
                    },
                    "stellar_da_input": 1966,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ec3b6adc-9edd-4eca-844d-c712810e0d441785580202977-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785579751558,
                    "timestamp_utc": "2026-08-01T10:22:31.000Z",
                    "tos": 0,
                    "totalbytes": 977829,
                    "totalpackets": 20,
                    "typical": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785580202977,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.2, name: NB-FCANDIA\" private) has sent an anomalously large number (#: 23) of SMB write requests, compared to its typical number (#: 2), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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