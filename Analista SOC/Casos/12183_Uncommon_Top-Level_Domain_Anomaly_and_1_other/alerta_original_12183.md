=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "5cd6fe70-1580-4f59-b0ad-b72de8d0344b1784125203073-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11091,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 30.5,
                    "aella_tuples": "192.168.169.108.10.11.1.1.53.32",
                    "anomaly_id": "8xIeZp8BI3UnQyDOAttT",
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
                        "INFO Clearbit Logo Query in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "logo.clearbit.com"
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
                    "duration": 7,
                    "end_bucket_time": 1784124900000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 26,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2044300,
                                "ids_severity": "low",
                                "name": "INFO Clearbit Logo Query in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 26.95,
                    "file_extract_timestamp": 1784124660844,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 100,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2023-02-22T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2023_02_22"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "updated_at": [
                                "2023_02_22"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "query": [
                                    {
                                        "id": 2009,
                                        "opcode": 0,
                                        "rrname": "logo.clearbit.com",
                                        "rrtype": "A",
                                        "tx_id": 0,
                                        "type": "query"
                                    }
                                ],
                                "version": 2
                            },
                            "flow": {
                                "bytes_toclient": 311,
                                "bytes_toserver": 355,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 3,
                                "pkts_toserver": 5,
                                "src_ip": "192.168.169.108",
                                "src_port": 62504,
                                "start": "2026-07-15T14:11:00.839777+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2023_02_22",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Clearbit Logo Query in DNS Lookup\\\"; dns.query; content:\\\"logo.clearbit.com\\\"; nocase; bsize:17; classtype:misc-activity; sid:2044300; rev:1; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, created_at 2023_02_22, deployment Perimeter, confidence High, signature_severity Informational, updated_at 2023_02_22;)\\n\"",
                            "updated": "2023_02_22"
                        },
                        "severity": "low",
                        "signature": "INFO Clearbit Logo Query in DNS Lookup",
                        "signature_id": 2044300
                    },
                    "inbytes_delta": 419,
                    "inbytes_total": 311,
                    "inpkts_delta": 5,
                    "inpkts_total": 3,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2003-07-04T18:10:12Z",
                            "effective_tld": "clearbit.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "logo.clearbit.com",
                            "query_type": "A",
                            "transaction_id": 2009
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns-1077.awsdns-06.org",
                                    "host_type": "SOA",
                                    "name": "clearbit.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 733
                                }
                            ],
                            "domain_creation": "2003-07-04T18:10:12Z",
                            "effective_tld": "clearbit.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "logo.clearbit.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 2,
                            "transaction_id": 2009
                        },
                        "transaction_id": 2009
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
                    "orig_id": "8xIeZp8BI3UnQyDOAttT",
                    "orig_index": "aella-maltrace-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 395,
                    "outbytes_total": 355,
                    "outpkts_delta": 6,
                    "outpkts_total": 5,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784124661186,
                    "response_time": 2,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.108",
                    "srcip": "192.168.169.108",
                    "srcip_assetid": "daf84290-cbaf-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-aortellado.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.108.2044300.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 62504,
                    "start_bucket_time": 1784124600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784125203062,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 532532,
                        "status": "New"
                    },
                    "stellar_da_input": 1470,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "5cd6fe70-1580-4f59-b0ad-b72de8d0344b1784125203073-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784124660940,
                    "timestamp_utc": "2026-07-15T14:11:00.000Z",
                    "tos": 0,
                    "totalbytes": 814,
                    "totalpackets": 11,
                    "typical": 4.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784125203073,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 61.0) of exploit attempts with the IDS signature \"INFO Clearbit Logo Query in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 30.5) from the typical value of (#: 4.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "5610b37a-fe2d-45c7-ae09-3f9ad1d8d7011784126102578-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11094,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "ZBQxZp8BI3UnQyDOs6g_",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 49,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "hb-production-ingressnginx-lb.verta.host",
                        "verta.host"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "hb-production-ingressnginx-lb.verta.host"
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
                    "duration": 180797,
                    "end_bucket_time": 1784125800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 30,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 65.84,
                    "flow_score": 98,
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2016-09-14T08:51:44.000Z",
                            "effective_tld": "verta.host",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "hb-production-ingressnginx-lb.verta.host",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 53756
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns-1044.awsdns-02.org",
                                    "host_type": "SOA",
                                    "name": "verta.host",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 650
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2016-09-14T08:51:44.000Z",
                            "effective_tld": "verta.host",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 30,
                            "query": "hb-production-ingressnginx-lb.verta.host",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 30,
                            "transaction_id": 53756
                        },
                        "transaction_id": 53756
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
                    "msgtype_name": "replica",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "ZBQxZp8BI3UnQyDOs6g_",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 31,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784125954647,
                    "response_time": 31,
                    "severity": 20,
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
                    "srcport": 63016,
                    "start_bucket_time": 1784125500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784126102516,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 142129,
                        "status": "New"
                    },
                    "stellar_da_input": 2321,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "5610b37a-fe2d-45c7-ae09-3f9ad1d8d7011784126102578-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784125771223,
                    "timestamp_utc": "2026-07-15T14:29:31.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784126102578,
                    "xdr_event": {
                        "description": "The host ad.technoma.local has sent a DNS query with a new top-level domain verta.host, that has never been seen before in the past 49 days. Investigate whether the host should be blocked.",
                        "display_name": "Uncommon Top-Level Domain Anomaly",
                        "framework_version": "v13",
                        "name": "dns_new_tld",
                        "scope": "",
                        "subtype": {
                            "display_name": "Sensor DNS Data Source",
                            "name": "dns_new_tld_sensor"
                        },
                        "tactic": {
                            "id": "TA0011",
                            "name": "Command and Control"
                        },
                        "tags": [
                            "DNS Anomaly",
                            "Top-Level Domain"
                        ],
                        "technique": {
                            "id": "T1071",
                            "name": "Application Layer Protocol",
                            "subtechnique": {
                                "id": "T1071.001",
                                "name": "DNS"
                            }
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}