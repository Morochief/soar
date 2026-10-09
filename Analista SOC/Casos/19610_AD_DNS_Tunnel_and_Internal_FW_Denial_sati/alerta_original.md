# Lote de Alertas Originales - Stellar Cyber Interflow

- **Caso:** 19610_AD_DNS_Tunnel_and_Internal_FW_Denial_sati
- **Cantidad de Eventos:** 15
- **Reglas Involucradas:** `dns_tunnel` (13 eventos), `new_registered_domain` (1 evento), `internal_fw_action` (1 evento)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Actores Principales:** `ad.technoma.local` (`10.11.1.1`), `ad2.technoma.local` (`10.11.1.2`), `10.212.134.200` (`sati`, SSL-VPN)

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "d03c87ee-be4c-4822-9357-f9bcb63e22e31790263686578-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19610,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "alert_time": 1790263686447,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 15:17:55 UTC",
                        "first_timestamp": 1790263075210,
                        "last_time_utc": "2026-09-24 15:17:55 UTC",
                        "last_timestamp": 1790263075210,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T15:26:00.000Z",
                        "scheduled_timestamp": 1790263560000
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
                    "duration": 35,
                    "end_bucket_time": 1790263560000,
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
                    "is_dga": "no",
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
                            "transaction_id": 14891
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
                                    "host_addr": "151.101.1.91",
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
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 35,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.129.91",
                                "151.101.65.91",
                                "151.101.1.91",
                                "151.101.193.91"
                            ],
                            "response_time": 35,
                            "transaction_id": 14891
                        },
                        "transaction_id": 14891
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
                    "orig_id": "lf8B1KABI3UnQyDOgi7m",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790263075210,
                    "orig_timestamp_utc": "2026-09-24T15:17:55.000Z",
                    "orig_write_time": 1790263261445,
                    "outbytes_delta": 99,
                    "outbytes_total": 99,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 35,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790263256769,
                    "response_time": 35,
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
                    "srcport": 58807,
                    "start_bucket_time": 1790263260000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263686447,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 425002,
                        "status": "New"
                    },
                    "stellar_da_input": 1723,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d03c87ee-be4c-4822-9357-f9bcb63e22e31790263686578-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790263560000,
                    "summary_start": 1790263260000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263075210,
                    "timestamp_utc": "2026-09-24T15:17:55.000Z",
                    "tos": 0,
                    "totalbytes": 262,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263686578,
                    "xdr_event": {
                        "description": "A host \"IP: 10.11.1.1, name: ad.technoma.local\" queried \"IP: 10.11.1.2, name: ad2.technoma.local\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
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
                "_id": "2a8f477f-f03f-4979-ad50-dd66e8222cdf1790263801942-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19615,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 533,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "_f8D1KABI3UnQyDO8orz",
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
                        "NB-RFGONZALEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RFGONZALEZ.technoma.local"
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
                    "end_bucket_time": 1790263500000,
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
                    "inbytes_delta": 104,
                    "inbytes_total": 104,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RFGONZALEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RFGONZALEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 41886
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.34",
                                    "host_type": "A",
                                    "name": "NB-RFGONZALEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RFGONZALEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RFGONZALEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.34"
                            ],
                            "response_time": 0,
                            "transaction_id": 41886,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 41886
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
                    "orig_id": "_f8D1KABI3UnQyDO8orz",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 88,
                    "outbytes_total": 88,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790263418758,
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
                    "srcport": 55329,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263801916,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 380542,
                        "status": "New"
                    },
                    "stellar_da_input": 1235,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2a8f477f-f03f-4979-ad50-dd66e8222cdf1790263801942-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263236559,
                    "timestamp_utc": "2026-09-24T15:20:36.000Z",
                    "tos": 0,
                    "total_entropy": 156,
                    "totalbytes": 192,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-JLOPEZ",
                        "NB-DRODAS",
                        "NB-CFLORENCIANO",
                        "NB-FKOCHMANN",
                        "NB-FOLAZAR"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 23.62,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263801941,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 533 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RFGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-CFLORENCIANO.\" The typical volume of traffic transmitted through this tunnel is 23 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "ca5dc490-d518-4380-a814-f3f033125aa31790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19616,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 620,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "5P8E1KABI3UnQyDOjqdd",
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
                        "NB-ZGONZALEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-ZGONZALEZ.technoma.local"
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
                    "end_bucket_time": 1790263500000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 59,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 21.32,
                    "flow_score": 98,
                    "inbytes_delta": 103,
                    "inbytes_total": 103,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-ZGONZALEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-ZGONZALEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 62516
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.115",
                                    "host_type": "A",
                                    "name": "NB-ZGONZALEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-ZGONZALEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-ZGONZALEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.115"
                            ],
                            "response_time": 0,
                            "transaction_id": 62516,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 62516
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
                    "orig_id": "5P8E1KABI3UnQyDOjqdd",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 87,
                    "outbytes_total": 87,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 59,
                    "receive_time": 1790263458376,
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
                    "srcip_host": "technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 53074,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263801922,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 340637,
                        "status": "New"
                    },
                    "stellar_da_input": 1233,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ca5dc490-d518-4380-a814-f3f033125aa31790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263277195,
                    "timestamp_utc": "2026-09-24T15:21:17.000Z",
                    "tos": 0,
                    "total_entropy": 176,
                    "totalbytes": 190,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "AD2",
                        "NB-ACHAMORRO",
                        "NB-ADIARTE",
                        "NB-AZORRILLA",
                        "NB-CARANDA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 13.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 620 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-ZGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ACHAMORRO.\" The typical volume of traffic transmitted through this tunnel is 13 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "67e982de-249d-40f4-9ada-a5d381e55ee71790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19617,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 645,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "lf8F1KABI3UnQyDOTsAJ",
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
                        "NB-WGONZALEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-WGONZALEZ.technoma.local"
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
                    "end_bucket_time": 1790263500000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 62,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 24.23,
                    "flow_score": 98,
                    "inbytes_delta": 103,
                    "inbytes_total": 103,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-WGONZALEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-WGONZALEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 9190
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.32",
                                    "host_type": "A",
                                    "name": "NB-WGONZALEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-WGONZALEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-WGONZALEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.32"
                            ],
                            "response_time": 0,
                            "transaction_id": 9190,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 9190
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
                    "orig_id": "lf8F1KABI3UnQyDOTsAJ",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 87,
                    "outbytes_total": 87,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 61,
                    "receive_time": 1790263500303,
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
                    "srcport": 49547,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263801926,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 291349,
                        "status": "New"
                    },
                    "stellar_da_input": 1230,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "67e982de-249d-40f4-9ada-a5d381e55ee71790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263317866,
                    "timestamp_utc": "2026-09-24T15:21:57.000Z",
                    "tos": 0,
                    "total_entropy": 184,
                    "totalbytes": 190,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "ADM-FS",
                        "NB-AGARCIA",
                        "NB-AMARTINEZ",
                        "NB-APAREDES",
                        "NB-CGALLARDO"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 17.25,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 645 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-WGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AMARTINEZ.\" The typical volume of traffic transmitted through this tunnel is 17 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "5fb42afa-21d8-41cc-80d0-ff7b2d93e6981790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19618,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 486,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "af8D1KABI3UnQyDOLGu2",
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
                    "duration": 37,
                    "end_bucket_time": 1790263500000,
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
                    "inbytes_delta": 205,
                    "inbytes_total": 1121,
                    "inpkts_delta": 2,
                    "is_dga": "no",
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
                            "transaction_id": 52001
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
                            "transaction_id": 52001,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 52001
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 2,
                    "msgtype_name": "end",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "af8D1KABI3UnQyDOLGu2",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 945,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 47,
                    "receive_time": 1790263362389,
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
                    "srcport": 64780,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263801929,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 431168,
                        "status": "New"
                    },
                    "stellar_da_input": 1229,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "5fb42afa-21d8-41cc-80d0-ff7b2d93e6981790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263361290,
                    "timestamp_utc": "2026-09-24T15:22:41.000Z",
                    "tos": 0,
                    "total_entropy": 143,
                    "totalbytes": 2066,
                    "totalpackets": 3,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ASAUCEDO",
                        "NB-DRODAS",
                        "NB-DSAAVERA",
                        "NB-FOLAZAR",
                        "NB-HBAZAN"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 28.22,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 486 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ASAUCEDO.\" The typical volume of traffic transmitted through this tunnel is 28 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "791a10a3-ab4d-4b0e-b568-700fa1e8c96a1790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19619,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 542,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "CP8D1KABI3UnQyDO8IkR",
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
                        "NB-ZGONZALEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-ZGONZALEZ.technoma.local"
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
                    "duration": 10108,
                    "end_bucket_time": 1790263500000,
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
                    "inbytes_delta": 202,
                    "inbytes_total": 202,
                    "inpkts_delta": 2,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-ZGONZALEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-ZGONZALEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 35111
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.115",
                                    "host_type": "A",
                                    "name": "NB-ZGONZALEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-ZGONZALEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-ZGONZALEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.115"
                            ],
                            "response_time": 0,
                            "transaction_id": 35111,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 35111
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
                    "orig_id": "CP8D1KABI3UnQyDO8IkR",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 170,
                    "outbytes_total": 170,
                    "outpkts_delta": 2,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790263413742,
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
                    "srcport": 59838,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263802448,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 381494,
                        "status": "New"
                    },
                    "stellar_da_input": 1718,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "791a10a3-ab4d-4b0e-b568-700fa1e8c96a1790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263399099,
                    "timestamp_utc": "2026-09-24T15:23:19.000Z",
                    "tos": 0,
                    "total_entropy": 155,
                    "totalbytes": 372,
                    "totalpackets": 4,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AZORRILLA",
                        "NB-ACHAMORRO",
                        "NB-ADIARTE",
                        "NB-CARANDA",
                        "NB-CVELAZQUEZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 20.43,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 542 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-ZGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-CVELAZQUEZ.\" The typical volume of traffic transmitted through this tunnel is 20 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "dda009be-4b0d-400d-8526-457ee114a5d91790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19620,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 435,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "2f8G1KABI3UnQyDO-f06",
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
                        "NB-ROSAV.technoma.local"
                    ],
                    "domain_list": [
                        "NB-ROSAV.technoma.local"
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
                    "end_bucket_time": 1790263500000,
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
                    "inbytes_delta": 99,
                    "inbytes_total": 99,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-ROSAV.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-ROSAV.technoma.local",
                            "query_type": "A",
                            "transaction_id": 52220
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.54",
                                    "host_type": "A",
                                    "name": "NB-ROSAV.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-ROSAV.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-ROSAV.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.54"
                            ],
                            "response_time": 0,
                            "transaction_id": 52220,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 52220
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
                    "orig_id": "2f8G1KABI3UnQyDO-f06",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 83,
                    "outbytes_total": 83,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 41,
                    "receive_time": 1790263611331,
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
                    "srcport": 56533,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263802451,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 181883,
                        "status": "New"
                    },
                    "stellar_da_input": 1218,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "dda009be-4b0d-400d-8526-457ee114a5d91790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263429540,
                    "timestamp_utc": "2026-09-24T15:23:49.000Z",
                    "tos": 0,
                    "total_entropy": 123,
                    "totalbytes": 182,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AGARCIA",
                        "NB-AMARTINEZ",
                        "NB-APAREDES",
                        "NB-CGALLARDO",
                        "NB-CYUDIZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 18.04,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 435 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-ROSAV.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AMARTINEZ.\" The typical volume of traffic transmitted through this tunnel is 18 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "3ebb8928-9c71-4c51-aa8d-f86c1e1aa8c21790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19621,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 785,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "owAH1KABI3UnQyDOvx8O",
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
                    "duration": 75,
                    "end_bucket_time": 1790263500000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 70,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 36.26,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "no",
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
                            "transaction_id": 24372
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
                            "processing_time": 75,
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.82"
                            ],
                            "response_time": 75,
                            "transaction_id": 24372,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 24372
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
                    "orig_id": "owAH1KABI3UnQyDOvx8O",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 75,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 74,
                    "receive_time": 1790263663085,
                    "response_time": 75,
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
                    "srcport": 56481,
                    "start_bucket_time": 1790263200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263802453,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 131704,
                        "status": "New"
                    },
                    "stellar_da_input": 1231,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3ebb8928-9c71-4c51-aa8d-f86c1e1aa8c21790263802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263480442,
                    "timestamp_utc": "2026-09-24T15:24:40.000Z",
                    "tos": 0,
                    "total_entropy": 227,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-CFLORENCIANO",
                        "NB-AGILL",
                        "NB-AINSAURRALDE",
                        "NB-CGOMEZ",
                        "NB-CLSALCEDO"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 24.67,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263802950,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 785 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-CFLORENCIANO.\" The typical volume of traffic transmitted through this tunnel is 24 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "f76210e0-4602-470d-b81e-da474774ac201790264102551-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19639,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 474,
                    "aella_tuples": "10.212.134.200.10.11.1.1.53.4",
                    "anomaly_id": "Hf8G1KABI3UnQyDO0_kG",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790263503481,
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
                    "dstip_username": "JOSEPAREDES",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790263800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790263503481
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
                    "fidelity": 99.7,
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
                        "event_time": "2026-09-24 12:25:03",
                        "eventtime": "1790263503481294110",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "10830119",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "12:25:03",
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
                    "orig_id": "Hf8G1KABI3UnQyDO0_kG",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=12:25:03 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790263503481294110 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=54766 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=10830119 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JOSEPAREDES\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790263602319,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 54766,
                    "start_bucket_time": 1790263500000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790264102538,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 491820,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2351,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "f76210e0-4602-470d-b81e-da474774ac201790264102551-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263503481,
                    "timestamp_utc": "2026-09-24T15:25:03.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 29,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790264102551,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 474), compared to the typical number of blocks (#: 29), measured in a 5.0-minute interval.",
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
                "_id": "f63f4c9b-b745-449b-9ca4-94a01a9b58f31790264101912-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19638,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 698,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "6AAI1KABI3UnQyDOq0Ot",
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
                    "end_bucket_time": 1790263800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 66,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 29.67,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "no",
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
                            "transaction_id": 55386
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
                            "transaction_id": 55386,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 55386
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
                    "orig_id": "6AAI1KABI3UnQyDOq0Ot",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 67,
                    "receive_time": 1790263724267,
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
                    "srcport": 54428,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264101894,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 371046,
                        "status": "New"
                    },
                    "stellar_da_input": 1226,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f63f4c9b-b745-449b-9ca4-94a01a9b58f31790264101912-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263541325,
                    "timestamp_utc": "2026-09-24T15:25:41.000Z",
                    "tos": 0,
                    "total_entropy": 203,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AARAUJO",
                        "NB-AGILL",
                        "NB-CALVAREZ",
                        "NB-CFLORENCIANO",
                        "NB-CGOMEZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 28.33,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264101912,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 698 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-CFLORENCIANO.\" The typical volume of traffic transmitted through this tunnel is 28 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "a704cd70-11bc-46fd-8338-af4b189301651790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19640,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 533,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "FgAJ1KABI3UnQyDOR1ca",
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
                        "SRV-AZADCONNECT.technoma.local"
                    ],
                    "domain_list": [
                        "SRV-AZADCONNECT.technoma.local"
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
                    "end_bucket_time": 1790263800000,
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
                    "inbytes_delta": 106,
                    "inbytes_total": 106,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "transaction_id": 41341
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "10.11.1.3",
                                    "host_type": "A",
                                    "name": "SRV-AZADCONNECT.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "10.11.1.3"
                            ],
                            "response_time": 0,
                            "transaction_id": 41341,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 41341
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
                    "orig_id": "FgAJ1KABI3UnQyDOR1ca",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 90,
                    "outbytes_total": 90,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 49,
                    "receive_time": 1790263761014,
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
                    "srcport": 50734,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264101898,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 330132,
                        "status": "New"
                    },
                    "stellar_da_input": 1236,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a704cd70-11bc-46fd-8338-af4b189301651790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263578535,
                    "timestamp_utc": "2026-09-24T15:26:18.000Z",
                    "tos": 0,
                    "total_entropy": 150,
                    "totalbytes": 196,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-GGIMENEZ",
                        "NB-ADIARTE",
                        "NB-ACHAMORRO",
                        "NB-AZORRILLA",
                        "NB-CARANDA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 25.67,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264102920,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 533 Bytes) of tunneled, high-entropy traffic through DNS (domain: SRV-AZADCONNECT.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ACHAMORRO.\" The typical volume of traffic transmitted through this tunnel is 25 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "fe4825d9-a1cf-44ea-86b5-0c295e0df1f21790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19641,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 562,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "GwAH1KABI3UnQyDOJgxa",
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
                        "NB-JCRISTALDO.technoma.local"
                    ],
                    "domain_list": [
                        "NB-JCRISTALDO.technoma.local"
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
                    "duration": 10129,
                    "end_bucket_time": 1790263800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 51,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 13.73,
                    "flow_score": 98,
                    "inbytes_delta": 311,
                    "inbytes_total": 311,
                    "inpkts_delta": 3,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-JCRISTALDO.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-JCRISTALDO.technoma.local",
                            "query_type": "A",
                            "transaction_id": 58900
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.85",
                                    "host_type": "A",
                                    "name": "NB-JCRISTALDO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-JCRISTALDO.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-JCRISTALDO.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.85"
                            ],
                            "response_time": 0,
                            "transaction_id": 58900,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 58900
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
                    "orig_id": "GwAH1KABI3UnQyDOJgxa",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 263,
                    "outbytes_total": 263,
                    "outpkts_delta": 3,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 55,
                    "receive_time": 1790263626259,
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
                    "srcport": 59838,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264102169,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 470910,
                        "status": "New"
                    },
                    "stellar_da_input": 2225,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fe4825d9-a1cf-44ea-86b5-0c295e0df1f21790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263612361,
                    "timestamp_utc": "2026-09-24T15:26:52.000Z",
                    "tos": 0,
                    "total_entropy": 166,
                    "totalbytes": 574,
                    "totalpackets": 6,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ABARRETO",
                        "NB-DRAMIREZ",
                        "NB-FARIAS",
                        "NB-MJCASANAS",
                        "NB-FROJAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 31.62,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264102920,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 562 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-JCRISTALDO.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-MJCASANAS.\" The typical volume of traffic transmitted through this tunnel is 31 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "f590b84c-89d1-485d-af40-fbc059a57bd71790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19642,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 547,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "xQAH1KABI3UnQyDOmRtE",
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
                        "NB-OALVARENGA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-OALVARENGA.technoma.local"
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
                    "duration": 56,
                    "end_bucket_time": 1790263800000,
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
                    "inbytes_delta": 406,
                    "inbytes_total": 808,
                    "inpkts_delta": 4,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-OALVARENGA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-OALVARENGA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 30452
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.67",
                                    "host_type": "A",
                                    "name": "NB-OALVARENGA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-OALVARENGA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-OALVARENGA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.67"
                            ],
                            "response_time": 0,
                            "transaction_id": 30452,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 30452
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 2,
                    "msgtype_name": "end",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "xQAH1KABI3UnQyDOmRtE",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 257,
                    "outbytes_total": 680,
                    "outpkts_delta": 3,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790263656063,
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
                    "srcport": 64780,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264102214,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 441303,
                        "status": "New"
                    },
                    "stellar_da_input": 2202,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f590b84c-89d1-485d-af40-fbc059a57bd71790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263655129,
                    "timestamp_utc": "2026-09-24T15:27:35.000Z",
                    "tos": 0,
                    "total_entropy": 155,
                    "totalbytes": 1488,
                    "totalpackets": 7,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AARAUJO",
                        "NB-FBENEGAS",
                        "NB-AINSAURRALDE",
                        "NB-CALVAREZ",
                        "NB-CFLORENCIANO"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 18.2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264102920,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 547 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-OALVARENGA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AINSAURRALDE.\" The typical volume of traffic transmitted through this tunnel is 18 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "1383cdd7-0b1b-4447-a210-34cabd3c7be31790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19643,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 630,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "ggAK1KABI3UnQyDO85_K",
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
                        "NB-SFERNANDEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-SFERNANDEZ.technoma.local"
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
                    "end_bucket_time": 1790263800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 60,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 22.55,
                    "flow_score": 98,
                    "inbytes_delta": 104,
                    "inbytes_total": 104,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 23866
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.120",
                                    "host_type": "A",
                                    "name": "NB-SFERNANDEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.120"
                            ],
                            "response_time": 0,
                            "transaction_id": 23866,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 23866
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
                    "orig_id": "ggAK1KABI3UnQyDO85_K",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 88,
                    "outbytes_total": 88,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 59,
                    "receive_time": 1790263874664,
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
                    "srcport": 50396,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264102216,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 221407,
                        "status": "New"
                    },
                    "stellar_da_input": 1236,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "1383cdd7-0b1b-4447-a210-34cabd3c7be31790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263693562,
                    "timestamp_utc": "2026-09-24T15:28:13.000Z",
                    "tos": 0,
                    "total_entropy": 180,
                    "totalbytes": 192,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-APRETTE",
                        "NB-ARESQUIN",
                        "NB-BBENITEZ",
                        "NB-CAQUINO",
                        "NB-DRODAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 15.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264102920,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 630 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-SFERNANDEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ARESQUIN.\" The typical volume of traffic transmitted through this tunnel is 15 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "63f5ca55-444a-4d51-b94c-1c6bc1572cef1790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19644,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 581,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "vAAL1KABI3UnQyDOkbON",
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
                        "NB-RMARTINEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RMARTINEZ.technoma.local"
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
                    "end_bucket_time": 1790263800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 16.37,
                    "flow_score": 98,
                    "inbytes_delta": 103,
                    "inbytes_total": 103,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RMARTINEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RMARTINEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 55364
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.76",
                                    "host_type": "A",
                                    "name": "NB-RMARTINEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RMARTINEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RMARTINEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.76"
                            ],
                            "response_time": 0,
                            "transaction_id": 55364,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 55364
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
                    "orig_id": "vAAL1KABI3UnQyDOkbON",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 87,
                    "outbytes_total": 87,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 56,
                    "receive_time": 1790263916519,
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
                    "srcport": 56981,
                    "start_bucket_time": 1790263500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790264102219,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 181266,
                        "status": "New"
                    },
                    "stellar_da_input": 1232,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "63f5ca55-444a-4d51-b94c-1c6bc1572cef1790264102920-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263734281,
                    "timestamp_utc": "2026-09-24T15:28:54.000Z",
                    "tos": 0,
                    "total_entropy": 168,
                    "totalbytes": 190,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ABARRETO",
                        "NB-DRAMIREZ",
                        "NB-FARIAS",
                        "NB-FMORA",
                        "NB-XLEGUIZAMON"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 31.21,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790264102920,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 581 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RMARTINEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-XLEGUIZAMON.\" The typical volume of traffic transmitted through this tunnel is 31 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
