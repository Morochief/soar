=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "8721d4b8-1270-4b27-a2ea-37970ad5de2b1784894469132-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4831,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "alert_time": 1784894469093,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-24 11:51:32 UTC",
                        "first_timestamp": 1784893892194,
                        "last_time_utc": "2026-07-24 11:51:32 UTC",
                        "last_timestamp": 1784893892194,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-24T11:59:00.000Z",
                        "scheduled_timestamp": 1784894340000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "theagenticx.ai",
                        "2026-05-04T19:37:09Z"
                    ],
                    "domain_list": [
                        "sync.theagenticx.ai"
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
                    "duration": 28,
                    "end_bucket_time": 1784894340000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 154,
                    "inbytes_total": 154,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2026-05-04T19:37:09Z",
                            "effective_tld": "theagenticx.ai",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "sync.theagenticx.ai",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 62531
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "kareem.ns.cloudflare.com",
                                    "host_type": "SOA",
                                    "name": "theagenticx.ai",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 1086
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2026-05-04T19:37:09Z",
                            "effective_tld": "theagenticx.ai",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 28,
                            "query": "sync.theagenticx.ai",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 28,
                            "transaction_id": 62531
                        },
                        "transaction_id": 62531
                    },
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
                    "orig_id": "-kX6k58BI3UnQyDOSZ04",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.16-000051",
                    "orig_timestamp": 1784893892194,
                    "orig_timestamp_utc": "2026-07-24T11:51:32.000Z",
                    "orig_write_time": 1784894080285,
                    "outbytes_delta": 90,
                    "outbytes_total": 90,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 28,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784894073648,
                    "response_time": 28,
                    "severity": 50,
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
                    "srcport": 62926,
                    "start_bucket_time": 1784894040000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784894469093,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 388808,
                        "status": "New"
                    },
                    "stellar_da_input": 1354,
                    "stellar_index": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8721d4b8-1270-4b27-a2ea-37970ad5de2b1784894469132-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1784894340000,
                    "summary_start": 1784894040000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784893892194,
                    "timestamp_utc": "2026-07-24T11:51:32.000Z",
                    "tos": 0,
                    "totalbytes": 244,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784894469132,
                    "xdr_event": {
                        "description": "A host \"IP: 10.11.1.1, name: ad.technoma.local\" queried \"IP: 8.8.8.8, name: dns.google\"  for the domain theagenticx.ai,  which was registered on 2026-05-04T19:37:09Z  (less than 90 days ago).",
                        "display_name": "Recently Registered Domains",
                        "framework_version": "v8",
                        "name": "new_registered_domain",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2008",
                            "name": "XDR New Domain"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ec0dd6ba-d8bb-4cdf-9ef5-8257c5bde0201784895304290-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4844,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 6,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "anomaly_id": "8EYElJ8BI3UnQyDOCCrw",
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
                        "relay-174f8762.net.anydesk.com"
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
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 101,
                    "end_bucket_time": 1784895000000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 23,
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
                    "fidelity": 31.08,
                    "file_extract_timestamp": 1784894714666,
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
                                        "id": 59153,
                                        "opcode": 0,
                                        "rrname": "relay-174f8762.net.anydesk.com",
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
                                "dest_ip": "8.8.4.4",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 54014,
                                "start": "2026-07-24T12:05:14.666703+0000"
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
                    "inbytes_delta": 117,
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
                            "domain_creation": "2004-02-07T15:49:37Z",
                            "effective_tld": "anydesk.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "relay-174f8762.net.anydesk.com",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 59153
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "177.54.150.120",
                                    "host_type": "A",
                                    "name": "relay-174f8762.net.anydesk.com",
                                    "section_type": "Answer",
                                    "ttl": 300
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2004-02-07T15:49:37Z",
                            "effective_tld": "anydesk.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 101,
                            "query": "relay-174f8762.net.anydesk.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "177.54.150.120"
                            ],
                            "response_time": 101,
                            "transaction_id": 59153
                        },
                        "transaction_id": 59153
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
                    "orig_id": "8EYElJ8BI3UnQyDOCCrw",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 101,
                    "outbytes_total": 105,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 101,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784894715203,
                    "response_time": 101,
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
                    "srcport": 54014,
                    "start_bucket_time": 1784894700000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784895304253,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 584076,
                        "status": "New"
                    },
                    "stellar_da_input": 1652,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ec0dd6ba-d8bb-4cdf-9ef5-8257c5bde0201784895304290-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784894715007,
                    "timestamp_utc": "2026-07-24T12:05:15.000Z",
                    "tos": 0,
                    "totalbytes": 218,
                    "totalpackets": 2,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784895304290,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 12.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 6.0) from the typical value of (#: 1.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "4df902d6-bf99-4715-a614-438d4b4561db1784895603520-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4847,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 9.5,
                    "aella_tuples": "192.168.169.50.10.11.1.1.53.32",
                    "anomaly_id": "W0YIlJ8BI3UnQyDOnX-N",
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
                        "mobile.events.data.microsoft.com"
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
                    "dstip_host": "technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 53,
                    "duration": 29216,
                    "end_bucket_time": 1784895300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 15,
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
                    "fidelity": 5,
                    "file_extract_timestamp": 1784895013570,
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
                                        "id": 2704,
                                        "opcode": 0,
                                        "rrname": "relay-acc712f4.net.anydesk.com",
                                        "rrtype": "A",
                                        "tx_id": 46,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 4740,
                                "bytes_toserver": 2133,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 23,
                                "pkts_toserver": 24,
                                "src_ip": "192.168.169.50",
                                "src_port": 58655,
                                "start": "2026-07-24T12:04:23.824729+0000"
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
                    "inbytes_delta": 0,
                    "inbytes_total": 4740,
                    "inpkts_delta": 0,
                    "inpkts_total": 23,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "1991-05-02T04:00:00Z",
                            "effective_tld": "microsoft.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "mobile.events.data.microsoft.com",
                            "query_type": "A",
                            "transaction_id": 63087
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "mobile.events.data.trafficmanager.net",
                                    "host_type": "CNAME",
                                    "name": "mobile.events.data.microsoft.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host": "onedscolprdwus66.westus.cloudapp.azure.com",
                                    "host_type": "CNAME",
                                    "name": "mobile.events.data.trafficmanager.net",
                                    "section_type": "Answer",
                                    "ttl": 21
                                },
                                {
                                    "host_addr": "20.184.175.3",
                                    "host_type": "A",
                                    "name": "onedscolprdwus66.westus.cloudapp.azure.com",
                                    "section_type": "Answer",
                                    "ttl": 5
                                }
                            ],
                            "domain_creation": "1991-05-02T04:00:00Z",
                            "effective_tld": "microsoft.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "mobile.events.data.microsoft.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "20.184.175.3"
                            ],
                            "response_time": 0,
                            "transaction_id": 63087
                        },
                        "transaction_id": 63087
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
                    "orig_id": "W0YIlJ8BI3UnQyDOnX-N",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 0,
                    "outbytes_total": 2133,
                    "outpkts_delta": 0,
                    "outpkts_total": 24,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784895013958,
                    "response_time": 0,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.50",
                    "srcip": "192.168.169.50",
                    "srcip_assetid": "d724b8c8-4cb6-11f1-ab17-da767f579487",
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
                    "srcip_host": "192.168.169.50",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.50.2060507.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 58655,
                    "start_bucket_time": 1784895000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784895603477,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 583093,
                        "status": "New"
                    },
                    "stellar_da_input": 1678,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4df902d6-bf99-4715-a614-438d4b4561db1784895603520-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784895013773,
                    "timestamp_utc": "2026-07-24T12:10:13.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 1.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784895603520,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 19.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 9.5) from the typical value of (#: 1.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "77aab9d0-ca7d-4bf5-8a09-cd67dbe8ecd51784895604532-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4848,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "XkYIlJ8BI3UnQyDOnX__",
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
                        "play.google.com"
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
                    "duration": 26,
                    "end_bucket_time": 1784895300000,
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
                    "file_extract_timestamp": 1784895014258,
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
                                        "id": 32873,
                                        "opcode": 0,
                                        "rrname": "relay-8a3338e6.net.anydesk.com",
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
                                "src_port": 62781,
                                "start": "2026-07-24T12:10:14.258072+0000"
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
                    "inbytes_delta": 136,
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
                            "query": "play.google.com",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 21342
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns1.google.com",
                                    "host_type": "SOA",
                                    "name": "google.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 1
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
                            "processing_time": 26,
                            "query": "play.google.com",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 26,
                            "transaction_id": 21342
                        },
                        "transaction_id": 21342
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
                    "orig_id": "XkYIlJ8BI3UnQyDOnX__",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 86,
                    "outbytes_total": 105,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 26,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784895014477,
                    "response_time": 26,
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
                    "srcport": 62781,
                    "start_bucket_time": 1784895000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784895604427,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 583956,
                        "status": "New"
                    },
                    "stellar_da_input": 1652,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "77aab9d0-ca7d-4bf5-8a09-cd67dbe8ecd51784895604532-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784895014274,
                    "timestamp_utc": "2026-07-24T12:10:14.000Z",
                    "tos": 0,
                    "totalbytes": 222,
                    "totalpackets": 2,
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784895604532,
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "e94a0d22-7ccb-43f8-bda2-16e8c9ad05891784897103807-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4871,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 75,
                    "aella_tuples": "192.168.169.87.10.11.1.1.445.185",
                    "anomaly_id": "XkgflJ8BI3UnQyDOYRnP",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.87"
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
                    "duration": 2064,
                    "end_bucket_time": 1784896800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 31,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$",
                            "\\\\ad.technoma.local\\sysvol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\sysvol",
                                "value": 1
                            },
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 2
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 74.07,
                    "flow_score": 100,
                    "inbytes_delta": 1832,
                    "inbytes_total": 6748,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "metadata": [
                        {
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
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{BEEBC998-BD1B-455A-A795-FCB34CBFB139}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 1,
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
                                "path": "\\\\ad.technoma.local\\sysvol",
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
                                "filename": "technoma.local\\Policies\\{31B2F340-016D-11D2-945F-00C04FB984F9}\\User",
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
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "XkgflJ8BI3UnQyDOYRnP",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 5584,
                    "outbytes_total": 16928,
                    "outpkts_delta": 10,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784896506038,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.87",
                    "srcip": "192.168.169.87",
                    "srcip_assetid": "e0717cd8-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.87",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 59664,
                    "start_bucket_time": 1784896500000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784897102784,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 592253,
                        "status": "New"
                    },
                    "stellar_da_input": 2062,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e94a0d22-7ccb-43f8-bda2-16e8c9ad05891784897103807-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784896505569,
                    "timestamp_utc": "2026-07-24T12:35:05.000Z",
                    "tos": 0,
                    "totalbytes": 23676,
                    "totalpackets": 19,
                    "typical": 16,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784897103807,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.87\" private) has sent an anomalously large number (#: 75) of SMB read requests, compared to its typical number (#: 16), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$, \\\\ad.technoma.local\\sysvol very frequently.",
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