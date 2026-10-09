# Alertas Originales Interflow / Stellar Cyber - Lote de 10 Eventos

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "f495884e-9f00-432f-9f47-aa9b3dc3d8581790253188306-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19072,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "alert_time": 1790253188137,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 12:25:03 UTC",
                        "first_timestamp": 1790252703572,
                        "last_time_utc": "2026-09-24 12:25:03 UTC",
                        "last_timestamp": 1790252703572,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T12:31:00.000Z",
                        "scheduled_timestamp": 1790253060000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "firefox-portal-detection.com",
                        "2026-07-01T15:40:13Z"
                    ],
                    "domain_list": [
                        "firefox-portal-detection.com"
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
                    "duration": 27,
                    "end_bucket_time": 1790253060000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 163,
                    "inbytes_total": 163,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 16805
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.129.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.193.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.1.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 27,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.129.91",
                                "151.101.65.91",
                                "151.101.193.91",
                                "151.101.1.91"
                            ],
                            "response_time": 27,
                            "transaction_id": 16805
                        },
                        "transaction_id": 16805
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
                    "orig_id": "kuZj06ABI3UnQyDOR-sz",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790252703572,
                    "orig_timestamp_utc": "2026-09-24T12:25:03.000Z",
                    "orig_write_time": 1790252891786,
                    "outbytes_delta": 99,
                    "outbytes_total": 99,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 27,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790252886315,
                    "response_time": 27,
                    "severity": 50,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 59429,
                    "start_bucket_time": 1790252760000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253188137,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 296351,
                        "status": "New"
                    },
                    "stellar_da_input": 1721,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f495884e-9f00-432f-9f47-aa9b3dc3d8581790253188306-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790253060000,
                    "summary_start": 1790252760000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790252703572,
                    "timestamp_utc": "2026-09-24T12:25:03.000Z",
                    "tos": 0,
                    "totalbytes": 262,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253188306,
                    "xdr_event": {
                        "description": "A host \"IP: 10.11.1.1, name: ad.technoma.local\" queried \"IP: 8.8.8.8, name: dns.google\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "bc448a75-fbf8-43d9-a035-eef6e67e3c4d1790253302075-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19073,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 409,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Pedl06ABI3UnQyDOPTEf",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253000000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 3163
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.10",
                                    "host_type": "A",
                                    "name": "NB-RZABALA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.10"
                            ],
                            "response_time": 0,
                            "transaction_id": 3163,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 3163
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
                    "orig_id": "Pedl06ABI3UnQyDOPTEf",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 39,
                    "receive_time": 1790253014453,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 49584,
                    "start_bucket_time": 1790252700000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253302043,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 281262,
                        "status": "New"
                    },
                    "stellar_da_input": 1224,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bc448a75-fbf8-43d9-a035-eef6e67e3c4d1790253302075-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790252832670,
                    "timestamp_utc": "2026-09-24T12:27:12.000Z",
                    "tos": 0,
                    "total_entropy": 118,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ALOVERA",
                        "NB-CYUDIZ",
                        "NB-FCANDIA",
                        "NB-FSERVIN",
                        "NB-GCABANAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 36.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253302075,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 409 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RZABALA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-GCABANAS.\" The typical volume of traffic transmitted through this tunnel is 36 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "56295893-6632-4a6e-bf31-002a5e7453621790253303088-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19074,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 431,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "AOdm06ABI3UnQyDOK08F",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253000000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 10184
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.10",
                                    "host_type": "A",
                                    "name": "NB-RZABALA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.10"
                            ],
                            "response_time": 0,
                            "transaction_id": 10184,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 10184
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
                    "orig_id": "AOdm06ABI3UnQyDOK08F",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 40,
                    "receive_time": 1790253074606,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 52536,
                    "start_bucket_time": 1790252700000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253302048,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 221253,
                        "status": "New"
                    },
                    "stellar_da_input": 1226,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "56295893-6632-4a6e-bf31-002a5e7453621790253303088-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790252893662,
                    "timestamp_utc": "2026-09-24T12:28:13.000Z",
                    "tos": 0,
                    "total_entropy": 123,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-CFARINA",
                        "NB-CGALLARDO",
                        "NB-JMARIN",
                        "NB-RFGONZALEZ",
                        "NB-ALOVERA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 22.65,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253303088,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 431 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RZABALA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-RFGONZALEZ.\" The typical volume of traffic transmitted through this tunnel is 22 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "172cc929-f91d-4f13-977e-bda4b2be16f41790253603644-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19085,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 6,
                    "aella_tuples": "192.168.169.36.10.11.1.1.53.32",
                    "anomaly_id": "Cedl06ABI3UnQyDOqj_x",
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
                        "DNS Query for .cc TLD",
                        "high"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "gtracenep.admaster.cc"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
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
                    "duration": 33,
                    "end_bucket_time": 1790253300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 71,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "high",
                        "ids_signatures_summarize": [
                            {
                                "id": 2027758,
                                "ids_severity": "high",
                                "name": "DNS Query for .cc TLD"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 63.51,
                    "file_extract_timestamp": 1790253041872,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Potentially Bad Traffic",
                        "created_ts": "2019-07-26T00:00:00Z",
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
                                "2019_07_26"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "updated_at": [
                                "2020_09_17"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 57082,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "gtracenep.admaster.cc",
                                        "rrtype": "HTTPS"
                                    }
                                ],
                                "rcode": "NOERROR",
                                "rd": true,
                                "tx_id": 0,
                                "type": "request",
                                "version": 3
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 85,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.36",
                                "src_port": 53042,
                                "start": "2026-09-24T12:30:41.872155+0000"
                            }
                        },
                        "rev": 5,
                        "rule": {
                            "created": "2019_07_26",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET DNS Query for .cc TLD\\\"; dns.query; content:\\\".cc\\\"; endswith; fast_pattern; classtype:bad-unknown; sid:2027758; rev:5; metadata:affected_product Any, attack_target Client_Endpoint, created_at 2019_07_26, deployment Perimeter, confidence High, signature_severity Informational, updated_at 2020_09_17;)\\n\"",
                            "updated": "2020_09_17"
                        },
                        "severity": "high",
                        "signature": "DNS Query for .cc TLD",
                        "signature_id": 2027758
                    },
                    "inbytes_delta": 146,
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
                            "dga_score": 0,
                            "domain_creation": "2024-07-12T03:58:33Z",
                            "effective_tld": "admaster.cc",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "gtracenep.admaster.cc",
                            "query_type": "HTTPS",
                            "transaction_id": 57082
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns6.wixdns.net",
                                    "host_type": "SOA",
                                    "name": "admaster.cc",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 850
                                }
                            ],
                            "domain_creation": "2024-07-12T03:58:33Z",
                            "effective_tld": "admaster.cc",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 33,
                            "query": "gtracenep.admaster.cc",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 33,
                            "transaction_id": 57082
                        },
                        "transaction_id": 57082
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
                    "orig_id": "Cedl06ABI3UnQyDOqj_x",
                    "orig_index": "aella-maltrace-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 81,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 33,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790253042388,
                    "response_time": 33,
                    "score": 60,
                    "severity": 75,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.36",
                    "srcip": "192.168.169.36",
                    "srcip_assetid": "a3458c88-ceaf-11f0-bc8a-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "nb-daquino.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.36.2027758",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 53042,
                    "start_bucket_time": 1790253000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253603629,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 553059,
                        "status": "New"
                    },
                    "stellar_da_input": 1475,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "172cc929-f91d-4f13-977e-bda4b2be16f41790253603644-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253042198,
                    "timestamp_utc": "2026-09-24T12:30:42.000Z",
                    "tos": 0,
                    "totalbytes": 227,
                    "totalpackets": 2,
                    "typical": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253603644,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 6.0) of exploit attempts with the IDS signature \"DNS Query for .cc TLD\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 6.0) from the typical value of (#: 2.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "df2fe4f7-a7a0-441f-baf0-4c558919811e1790253601895-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19082,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 433,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "mudn06ABI3UnQyDO1ITC",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-AZORRILLA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-AZORRILLA.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 50795,
                    "end_bucket_time": 1790253300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 204,
                    "inbytes_total": 204,
                    "inpkts_delta": 2,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-AZORRILLA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-AZORRILLA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 62485
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.65",
                                    "host_type": "A",
                                    "name": "NB-AZORRILLA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-AZORRILLA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-AZORRILLA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.65"
                            ],
                            "response_time": 0,
                            "transaction_id": 62485,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 62485
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
                    "orig_id": "mudn06ABI3UnQyDO1ITC",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 172,
                    "outbytes_total": 172,
                    "outpkts_delta": 2,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 41,
                    "receive_time": 1790253181051,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 57709,
                    "start_bucket_time": 1790253000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253601875,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 410680,
                        "status": "New"
                    },
                    "stellar_da_input": 1723,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "df2fe4f7-a7a0-441f-baf0-4c558919811e1790253601895-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253127564,
                    "timestamp_utc": "2026-09-24T12:32:07.000Z",
                    "tos": 0,
                    "total_entropy": 126,
                    "totalbytes": 376,
                    "totalpackets": 4,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-CLEIVA",
                        "NB-CYUDIZ",
                        "NB-FCANDIA",
                        "NB-FSERVIN",
                        "NB-GCABANAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253601894,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 433 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-AZORRILLA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-GCABANAS.\" The typical volume of traffic transmitted through this tunnel is 3 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "51a2b8a7-e46c-4928-b70d-7a40a44440611790253602898-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19083,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 526,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "rOdr06ABI3UnQyDOgf9H",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-ODACOSTA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-ODACOSTA.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 102,
                    "inbytes_total": 102,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-ODACOSTA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-ODACOSTA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 22571
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.71",
                                    "host_type": "A",
                                    "name": "NB-ODACOSTA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-ODACOSTA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-ODACOSTA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.71"
                            ],
                            "response_time": 0,
                            "transaction_id": 22571,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 22571
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
                    "orig_id": "rOdr06ABI3UnQyDOgf9H",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 86,
                    "outbytes_total": 86,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790253421891,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 57239,
                    "start_bucket_time": 1790253000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253601880,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 171294,
                        "status": "New"
                    },
                    "stellar_da_input": 1229,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "51a2b8a7-e46c-4928-b70d-7a40a44440611790253602898-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253239552,
                    "timestamp_utc": "2026-09-24T12:33:59.000Z",
                    "tos": 0,
                    "total_entropy": 153,
                    "totalbytes": 188,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-JOSEB",
                        "NB-JPALACIOS",
                        "NB-JRIVAROLA",
                        "wpad",
                        "ad2"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253602898,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 526 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-ODACOSTA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-JPALACIOS.\" The typical volume of traffic transmitted through this tunnel is 1 Byte, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "68fb7d76-e7ec-42d2-9036-63d067b619731790253902354-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19090,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 373,
                    "aella_tuples": "10.212.134.203.10.11.1.1.53.4",
                    "anomaly_id": "sudr06ABI3UnQyDOLvba",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.203"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790253301880,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
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
                    "dstip_username": "JUNIORAGUERO",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790253301880
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 71,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 99.52,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 09:35:02",
                        "eventtime": "1790253301880416289",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "4293900263",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "09:35:02",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_origin": {
                        "category": "firewall",
                        "processor": {
                            "name": "in_udp,parser-stellar,filter_stellar_parser-forti_fortigate",
                            "type": "log_forwarder"
                        },
                        "source": "fw_fortigate"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 0,
                    "netid_name": "vlan0",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "sudr06ABI3UnQyDOLvba",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=09:35:02 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790253301880416289 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.203 srcport=55155 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=4293900263 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JUNIORAGUERO\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790253401952,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.203",
                    "srcip": "10.212.134.203",
                    "srcip_assetid": "19c1aeca-8a1f-11f1-9610-8e57707220c4",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "10.212.134.203",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 55155,
                    "start_bucket_time": 1790253300000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790253902344,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 491598,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "68fb7d76-e7ec-42d2-9036-63d067b619731790253902354-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253301880,
                    "timestamp_utc": "2026-09-24T12:35:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 28,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790253902354,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.203 private) has had actions blocked by a firewall too many times (#: 373), compared to the typical number of blocks (#: 28), measured in a 5.0-minute interval.",
                        "display_name": "Internal Firewall Denial Anomaly",
                        "framework_version": "v8",
                        "name": "internal_fw_action",
                        "scope": "Internal",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "Internal",
                            "Network Traffic Analysis",
                            "Firewall Anomalies"
                        ],
                        "technique": {
                            "id": "XT2002",
                            "name": "XDR Firewall Anomaly"
                        },
                        "xdr_killchain_stage": "Exploration",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "45515496-9d4f-41b8-8b16-3a448b252a2b1790253901897-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19089,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 418,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Ouht06ABI3UnQyDOBjVe",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-JRAGUERO.technoma.local"
                    ],
                    "domain_list": [
                        "NB-JRAGUERO.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 150,
                    "inbytes_total": 150,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-JRAGUERO.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-JRAGUERO.technoma.local",
                            "query_type": "A",
                            "transaction_id": 13269
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.100.31",
                                    "host_type": "A",
                                    "name": "NB-JRAGUERO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                },
                                {
                                    "host_addr": "192.168.199.1",
                                    "host_type": "A",
                                    "name": "NB-JRAGUERO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                },
                                {
                                    "host_addr": "10.212.134.205",
                                    "host_type": "A",
                                    "name": "NB-JRAGUERO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                },
                                {
                                    "host_addr": "192.168.234.1",
                                    "host_type": "A",
                                    "name": "NB-JRAGUERO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-JRAGUERO.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-JRAGUERO.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.100.31",
                                "192.168.199.1",
                                "10.212.134.205",
                                "192.168.234.1"
                            ],
                            "response_time": 0,
                            "transaction_id": 13269,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 13269
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
                    "orig_id": "Ouht06ABI3UnQyDOBjVe",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 86,
                    "outbytes_total": 86,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 40,
                    "receive_time": 1790253523519,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 60487,
                    "start_bucket_time": 1790253300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253901883,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 371092,
                        "status": "New"
                    },
                    "stellar_da_input": 1605,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "45515496-9d4f-41b8-8b16-3a448b252a2b1790253901897-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253341214,
                    "timestamp_utc": "2026-09-24T12:35:41.000Z",
                    "tos": 0,
                    "total_entropy": 121,
                    "totalbytes": 236,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AINSAURRALDE",
                        "NB-AZORRILLA",
                        "NB-BBENITEZ",
                        "NB-DAQUINO",
                        "NB-ECANETE"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253901897,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 418 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-JRAGUERO.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AINSAURRALDE.\" The typical volume of traffic transmitted through this tunnel is 1 Byte, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "b157b43e-259f-4244-b539-2a5af7578c951790253902905-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19091,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 520,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Luhv06ABI3UnQyDOVYR1",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-TIBANEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-TIBANEZ.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 260
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.82",
                                    "host_type": "A",
                                    "name": "NB-TIBANEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.82"
                            ],
                            "response_time": 0,
                            "transaction_id": 260,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 260
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
                    "orig_id": "Luhv06ABI3UnQyDOVYR1",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 49,
                    "receive_time": 1790253676841,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 53265,
                    "start_bucket_time": 1790253300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253901923,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 220777,
                        "status": "New"
                    },
                    "stellar_da_input": 1222,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b157b43e-259f-4244-b539-2a5af7578c951790253902905-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253493797,
                    "timestamp_utc": "2026-09-24T12:38:13.000Z",
                    "tos": 0,
                    "total_entropy": 150,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ARUIZ",
                        "NB-ASAUCEDO",
                        "NB-DSAAVERA",
                        "NB-FARIAS",
                        "NB-LARCE"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 20,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253902905,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 520 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ASAUCEDO.\" The typical volume of traffic transmitted through this tunnel is 20 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "1f853c01-fbdd-4999-9c26-01d5e23a85931790253902905-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19092,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 479,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Y-hw06ABI3UnQyDOPqEI",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-TIBANEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-TIBANEZ.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790253600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 21204
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.82",
                                    "host_type": "A",
                                    "name": "NB-TIBANEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.82"
                            ],
                            "response_time": 0,
                            "transaction_id": 21204,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 21204
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
                    "orig_id": "Y-hw06ABI3UnQyDOPqEI",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 46,
                    "receive_time": 1790253737716,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
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
                    "srcport": 50607,
                    "start_bucket_time": 1790253300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790253902089,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 160632,
                        "status": "New"
                    },
                    "stellar_da_input": 1226,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "1f853c01-fbdd-4999-9c26-01d5e23a85931790253902905-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790253554838,
                    "timestamp_utc": "2026-09-24T12:39:14.000Z",
                    "tos": 0,
                    "total_entropy": 139,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ARUIZ",
                        "NB-FARIAS",
                        "NB-MSOSA",
                        "NB-RZABALA",
                        "NB-LARCE"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 36.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790253902905,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 479 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-RZABALA.\" The typical volume of traffic transmitted through this tunnel is 36 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
```
