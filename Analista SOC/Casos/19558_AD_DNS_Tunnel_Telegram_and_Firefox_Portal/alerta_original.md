# Alerta Original - Raw JSON Interflow (Lote de 11 Eventos)
**ID de Secuencia Principal:** `19558` (Rango: `19558` - `19576`)  
**Fecha de Ingesta:** 2026-09-24  
**Tenant:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "d418528f-f7b9-46b7-9a6f-c001641bb7b41790263087291-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19559,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "alert_time": 1790263087088,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 15:11:45 UTC",
                        "first_timestamp": 1790262705107,
                        "last_time_utc": "2026-09-24 15:11:45 UTC",
                        "last_timestamp": 1790262705107,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T15:16:00.000Z",
                        "scheduled_timestamp": 1790262960000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "None",
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
                    "duration": 0,
                    "end_bucket_time": 1790262960000,
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
                    "flow_score": 91,
                    "inbytes_delta": 163,
                    "inbytes_total": 163,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
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
                            "processing_time": 0,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.129.91",
                                "151.101.65.91",
                                "151.101.1.91",
                                "151.101.193.91"
                            ],
                            "response_time": 0,
                            "transaction_id": 34297
                        },
                        "transaction_id": 34297
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
                    "orig_id": "uv3506ABI3UnQyDOGtvZ",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790262705107,
                    "orig_timestamp_utc": "2026-09-24T15:11:45.000Z",
                    "orig_write_time": 1790262711376,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262707715,
                    "response_time": 0,
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
                    "srcport": 61696,
                    "start_bucket_time": 1790262660000,
                    "state": "HalfOpened",
                    "stellar": {
                        "alert_time": 1790263087088,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 375712,
                        "status": "New"
                    },
                    "stellar_da_input": 1510,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d418528f-f7b9-46b7-9a6f-c001641bb7b41790263087291-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790262960000,
                    "summary_start": 1790262660000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262705107,
                    "timestamp_utc": "2026-09-24T15:11:45.000Z",
                    "tos": 0,
                    "totalbytes": 163,
                    "totalpackets": 1,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263087291,
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
                "_id": "3be44c6c-0eff-45b5-8764-6dbd16c0092d1790263087291-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19558,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "alert_time": 1790263087088,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 15:11:49 UTC",
                        "first_timestamp": 1790262709082,
                        "last_time_utc": "2026-09-24 15:11:49 UTC",
                        "last_timestamp": 1790262709082,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T15:16:00.000Z",
                        "scheduled_timestamp": 1790262960000
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
                    "duration": 30,
                    "end_bucket_time": 1790262960000,
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
                            "transaction_id": 22705
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.129.91",
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
                            "processing_time": 30,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.65.91",
                                "151.101.129.91",
                                "151.101.193.91",
                                "151.101.1.91"
                            ],
                            "response_time": 30,
                            "transaction_id": 22705
                        },
                        "transaction_id": 22705
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
                    "orig_id": "cP7706ABI3UnQyDO_lAu",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790262709082,
                    "orig_timestamp_utc": "2026-09-24T15:11:49.000Z",
                    "orig_write_time": 1790262900785,
                    "outbytes_delta": 99,
                    "outbytes_total": 99,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 30,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262890759,
                    "response_time": 30,
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
                    "srcport": 58897,
                    "start_bucket_time": 1790262660000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263087088,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 186303,
                        "status": "New"
                    },
                    "stellar_da_input": 1721,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3be44c6c-0eff-45b5-8764-6dbd16c0092d1790263087291-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790262960000,
                    "summary_start": 1790262660000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262709082,
                    "timestamp_utc": "2026-09-24T15:11:49.000Z",
                    "tos": 0,
                    "totalbytes": 262,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263087291,
                    "xdr_event": {
                        "description": "A host \"IP: 10.11.1.1, name: ad.technoma.local\" queried \"IP: 8.8.4.4, name: dns.google\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
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
                "_id": "37058927-772b-42dd-9082-de03bd77f1031790263203265-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19568,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 16.5,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Xv3306ABI3UnQyDOi6Ha",
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
                        "INFO Observed Telegram Domain in DNS Lookup (telegram .org)",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "firefox-portal-detection.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.2",
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
                    "end_bucket_time": 1790262900000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
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
                                "id": 2071627,
                                "ids_severity": "low",
                                "name": "INFO Observed Telegram Domain in DNS Lookup (telegram .org)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 89.06,
                    "file_extract_timestamp": 1790262601826,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2026-08-19T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2026_08_19"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Telegram",
                                "Description_Generated_By_Proofpoint_Nexus"
                            ],
                            "tls_state": [
                                "TLSDecrypt"
                            ],
                            "updated_at": [
                                "2026_08_19"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 58988,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "kws2-1.web.telegram.org",
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
                                "bytes_toserver": 98,
                                "dest_ip": "10.11.1.2",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 59407,
                                "start": "2026-09-24T15:10:01.826533+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2026_08_19",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Observed Telegram Domain in DNS Lookup (telegram .org)\\\"; dns.query; dotprefix; content:\\\".telegram.org\\\"; nocase; endswith; classtype:misc-activity; sid:2071627; rev:1; metadata:attack_target Client_Endpoint, tls_state TLSDecrypt, created_at 2026_08_19, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, tag Telegram, updated_at 2026_08_19;)\\n\"",
                            "updated": "2026_08_19"
                        },
                        "severity": "low",
                        "signature": "INFO Observed Telegram Domain in DNS Lookup (telegram .org)",
                        "signature_id": 2071627
                    },
                    "inbytes_delta": 163,
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
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 16485
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.1.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
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
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.1.91",
                                "151.101.129.91",
                                "151.101.65.91",
                                "151.101.193.91"
                            ],
                            "response_time": 0,
                            "transaction_id": 16485
                        },
                        "transaction_id": 16485
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
                    "orig_id": "Xv3306ABI3UnQyDOi6Ha",
                    "orig_index": "aella-maltrace-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 99,
                    "outbytes_total": 98,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262605121,
                    "response_time": 0,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
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
                    "srcip_sig_id": "10.11.1.1.2071627",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 59407,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263203257,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 592479,
                        "status": "New"
                    },
                    "stellar_da_input": 1586,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "37058927-772b-42dd-9082-de03bd77f1031790263203265-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262601843,
                    "timestamp_utc": "2026-09-24T15:10:01.000Z",
                    "tos": 0,
                    "totalbytes": 262,
                    "totalpackets": 2,
                    "typical": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263203265,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 33.0) of exploit attempts with the IDS signature \"INFO Observed Telegram Domain in DNS Lookup (telegram .org)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 16.5) from the typical value of (#: 2.0), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
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
                "_id": "fc6bd771-a1d9-4a90-bd0d-5d629fe1aff61790263204273-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19569,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 6,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "anomaly_id": "XP3306ABI3UnQyDOi6FM",
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
                        "INFO Observed Telegram Domain in DNS Lookup (telegram .org)",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "sb.l.google.com"
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
                    "duration": 16430,
                    "end_bucket_time": 1790262900000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
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
                                "id": 2071627,
                                "ids_severity": "low",
                                "name": "INFO Observed Telegram Domain in DNS Lookup (telegram .org)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 9.35,
                    "file_extract_timestamp": 1790262601826,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2026-08-19T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2026_08_19"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Telegram",
                                "Description_Generated_By_Proofpoint_Nexus"
                            ],
                            "tls_state": [
                                "TLSDecrypt"
                            ],
                            "updated_at": [
                                "2026_08_19"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 16112,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "kws2-1.web.telegram.org",
                                        "rrtype": "A"
                                    }
                                ],
                                "rcode": "NOERROR",
                                "rd": true,
                                "tx_id": 2,
                                "type": "request",
                                "version": 3
                            },
                            "flow": {
                                "bytes_toclient": 122,
                                "bytes_toserver": 188,
                                "dest_ip": "8.8.4.4",
                                "dest_port": 53,
                                "pkts_toclient": 1,
                                "pkts_toserver": 2,
                                "src_ip": "10.11.1.1",
                                "src_port": 61814,
                                "start": "2026-09-24T15:07:20.519578+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2026_08_19",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Observed Telegram Domain in DNS Lookup (telegram .org)\\\"; dns.query; dotprefix; content:\\\".telegram.org\\\"; nocase; endswith; classtype:misc-activity; sid:2071627; rev:1; metadata:attack_target Client_Endpoint, tls_state TLSDecrypt, created_at 2026_08_19, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, tag Telegram, updated_at 2026_08_19;)\\n\"",
                            "updated": "2026_08_19"
                        },
                        "severity": "low",
                        "signature": "INFO Observed Telegram Domain in DNS Lookup (telegram .org)",
                        "signature_id": 2071627
                    },
                    "inbytes_delta": 102,
                    "inbytes_total": 122,
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
                            "domain_creation": "1997-09-15T04:00:00Z",
                            "effective_tld": "google.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "sb.l.google.com",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 20154
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "142.251.129.174",
                                    "host_type": "A",
                                    "name": "sb.l.google.com",
                                    "section_type": "Answer",
                                    "ttl": 300
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
                            "processing_time": 91,
                            "query": "sb.l.google.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "142.251.129.174"
                            ],
                            "response_time": 91,
                            "transaction_id": 20154
                        },
                        "transaction_id": 20154
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
                    "orig_id": "XP3306ABI3UnQyDOi6FM",
                    "orig_index": "aella-maltrace-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 174,
                    "outbytes_total": 188,
                    "outpkts_delta": 2,
                    "outpkts_total": 2,
                    "port_name": "ethernet1",
                    "processing_time": 91,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262605121,
                    "response_time": 91,
                    "score": 30,
                    "severity": 20,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
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
                    "srcip_sig_id": "10.11.1.1.2071627",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 61814,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263204176,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 593430,
                        "status": "New"
                    },
                    "stellar_da_input": 1584,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fc6bd771-a1d9-4a90-bd0d-5d629fe1aff61790263204273-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262601843,
                    "timestamp_utc": "2026-09-24T15:10:01.000Z",
                    "tos": 0,
                    "totalbytes": 276,
                    "totalpackets": 3,
                    "typical": 1.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263204273,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 12.0) of exploit attempts with the IDS signature \"INFO Observed Telegram Domain in DNS Lookup (telegram .org)\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 6.0) from the typical value of (#: 1.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Private to Public Exploit Anomaly",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "1963dd0d-5923-4283-ba64-470db2c42a5e1790263201863-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19560,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 627,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Tf3406ABI3UnQyDOycxq",
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
                        "NB-RLLEDO.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RLLEDO.technoma.local"
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
                    "duration": 42,
                    "end_bucket_time": 1790262900000,
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
                    "fidelity": 22.47,
                    "flow_score": 98,
                    "inbytes_delta": 301,
                    "inbytes_total": 707,
                    "inpkts_delta": 3,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RLLEDO.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RLLEDO.technoma.local",
                            "query_type": "A",
                            "transaction_id": 36501
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.79",
                                    "host_type": "A",
                                    "name": "NB-RLLEDO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RLLEDO.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RLLEDO.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.79"
                            ],
                            "response_time": 0,
                            "transaction_id": 36501,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 36501
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
                    "orig_id": "Tf3406ABI3UnQyDOycxq",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 167,
                    "outbytes_total": 595,
                    "outpkts_delta": 2,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 61,
                    "receive_time": 1790262682682,
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
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263201844,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 511240,
                        "status": "New"
                    },
                    "stellar_da_input": 1705,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "1963dd0d-5923-4283-ba64-470db2c42a5e1790263201863-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262681772,
                    "timestamp_utc": "2026-09-24T15:11:21.000Z",
                    "tos": 0,
                    "total_entropy": 182,
                    "totalbytes": 1302,
                    "totalpackets": 5,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "AD2",
                        "NB-ACHAMORRO",
                        "NB-ADIARTE",
                        "NB-AZORRILLA",
                        "NB-CARANDA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 42.4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263201863,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 627 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RLLEDO.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ACHAMORRO.\" The typical volume of traffic transmitted through this tunnel is 42 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "b6808f79-6561-4cc9-bceb-f3f8f014fb321790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19562,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 576,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Of7806ABI3UnQyDOJVok",
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
                        "NB-LARCE.technoma.local"
                    ],
                    "domain_list": [
                        "NB-LARCE.technoma.local"
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
                    "end_bucket_time": 1790262900000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 15.36,
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
                            "effective_tld": "NB-LARCE.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-LARCE.technoma.local",
                            "query_type": "A",
                            "transaction_id": 53358
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.74",
                                    "host_type": "A",
                                    "name": "NB-LARCE.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-LARCE.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-LARCE.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.74"
                            ],
                            "response_time": 0,
                            "transaction_id": 53358,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 53358
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
                    "orig_id": "Of7806ABI3UnQyDOJVok",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 83,
                    "outbytes_total": 83,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 54,
                    "receive_time": 1790262900527,
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
                    "srcport": 51494,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263201888,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 291364,
                        "status": "New"
                    },
                    "stellar_da_input": 1218,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b6808f79-6561-4cc9-bceb-f3f8f014fb321790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262719061,
                    "timestamp_utc": "2026-09-24T15:11:59.000Z",
                    "tos": 0,
                    "total_entropy": 164,
                    "totalbytes": 182,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ARESQUIN",
                        "NB-CFARINA",
                        "NB-DAQUINO",
                        "NB-FSERVIN",
                        "NB-GGIMENEZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 19.11,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263202870,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 576 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-LARCE.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ARESQUIN.\" The typical volume of traffic transmitted through this tunnel is 19 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "b15eae42-7f78-4e85-bea6-638c7c9f45fc1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19563,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 448,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "EP7806ABI3UnQyDOmmvk",
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
                    "end_bucket_time": 1790262900000,
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
                            "transaction_id": 2038
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
                            "transaction_id": 2038,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 2038
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
                    "orig_id": "EP7806ABI3UnQyDOmmvk",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 43,
                    "receive_time": 1790262932358,
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
                    "srcport": 58059,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263201957,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 261296,
                        "status": "New"
                    },
                    "stellar_da_input": 1224,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b15eae42-7f78-4e85-bea6-638c7c9f45fc1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262749479,
                    "timestamp_utc": "2026-09-24T15:12:29.000Z",
                    "tos": 0,
                    "total_entropy": 130,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ABARRETO",
                        "NB-APAREDES",
                        "NB-TMARIN",
                        "NB-CLSALCEDO",
                        "NB-DRAMIREZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 26.3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263202870,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 448 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-CLSALCEDO.\" The typical volume of traffic transmitted through this tunnel is 26 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "7ec020c2-1903-492c-a757-4c4751ba67621790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19564,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 661,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "OP7906ABI3UnQyDOXofe",
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
                    "end_bucket_time": 1790262900000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 63,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 26.01,
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
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 61869
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
                            "transaction_id": 61869,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 61869
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
                    "orig_id": "OP7906ABI3UnQyDOXofe",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 63,
                    "receive_time": 1790262981591,
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
                    "srcport": 54852,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263202027,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 211354,
                        "status": "New"
                    },
                    "stellar_da_input": 1226,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7ec020c2-1903-492c-a757-4c4751ba67621790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262800198,
                    "timestamp_utc": "2026-09-24T15:13:20.000Z",
                    "tos": 0,
                    "total_entropy": 190,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "AD2",
                        "NB-AZORRILLA",
                        "NB-DFERNANDEZ",
                        "NB-DGODOY",
                        "NB-EORLANDINI"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 24.44,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263202870,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 661 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RZABALA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-DFERNANDEZ.\" The typical volume of traffic transmitted through this tunnel is 24 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "586c1bee-3f36-45f4-b1bd-d4b49036727f1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19565,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 546,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "yf7906ABI3UnQyDO0pkN",
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
                    "end_bucket_time": 1790262900000,
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
                            "transaction_id": 42787
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
                            "transaction_id": 42787,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 42787
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
                    "orig_id": "yf7906ABI3UnQyDO0pkN",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 87,
                    "outbytes_total": 87,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790263012394,
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
                    "srcport": 55850,
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263202061,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 181453,
                        "status": "New"
                    },
                    "stellar_da_input": 1232,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "586c1bee-3f36-45f4-b1bd-d4b49036727f1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262830748,
                    "timestamp_utc": "2026-09-24T15:13:50.000Z",
                    "tos": 0,
                    "total_entropy": 153,
                    "totalbytes": 190,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-APRETTE",
                        "NB-ARESQUIN",
                        "NB-BBENITEZ",
                        "NB-CAQUINO",
                        "NB-CFARINA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 31.56,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263202870,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 546 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-WGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ARESQUIN.\" The typical volume of traffic transmitted through this tunnel is 31 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "b8c8eb5e-b25c-4eb4-9221-81551be6d31f1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19566,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 499,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "l_7706ABI3UnQyDOtkYO",
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
                        "NB-MLOPEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-MLOPEZ.technoma.local"
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
                    "end_bucket_time": 1790262900000,
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
                    "inbytes_delta": 201,
                    "inbytes_total": 606,
                    "inpkts_delta": 2,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-MLOPEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-MLOPEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 16051
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.145",
                                    "host_type": "A",
                                    "name": "NB-MLOPEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-MLOPEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-MLOPEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.145"
                            ],
                            "response_time": 0,
                            "transaction_id": 16051,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 16051
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
                    "orig_id": "l_7706ABI3UnQyDOtkYO",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 84,
                    "outbytes_total": 510,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 47,
                    "receive_time": 1790262876258,
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
                    "start_bucket_time": 1790262600000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263202117,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 321174,
                        "status": "New"
                    },
                    "stellar_da_input": 1226,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b8c8eb5e-b25c-4eb4-9221-81551be6d31f1790263202870-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262874844,
                    "timestamp_utc": "2026-09-24T15:14:34.000Z",
                    "tos": 0,
                    "total_entropy": 143,
                    "totalbytes": 1116,
                    "totalpackets": 3,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ASAUCEDO",
                        "NB-DRODAS",
                        "NB-EVERA",
                        "NB-FOLAZAR",
                        "NB-HBAZAN"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 17.35,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263202870,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 499 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-MLOPEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ASAUCEDO.\" The typical volume of traffic transmitted through this tunnel is 17 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "00a1f478-27da-43c8-b965-956671ca98e21790263384093-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19576,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.11.1.1.8.8.4.4.53.32",
                    "alert_time": 1790263383945,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 15:13:27 UTC",
                        "first_timestamp": 1790262807535,
                        "last_time_utc": "2026-09-24 15:13:27 UTC",
                        "last_timestamp": 1790262807535,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T15:21:00.000Z",
                        "scheduled_timestamp": 1790263260000
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
                    "duration": 28,
                    "end_bucket_time": 1790263260000,
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
                            "transaction_id": 4257
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.129.91",
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
                                "151.101.65.91",
                                "151.101.129.91",
                                "151.101.193.91",
                                "151.101.1.91"
                            ],
                            "response_time": 27,
                            "transaction_id": 4257
                        },
                        "transaction_id": 4257
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
                    "orig_id": "QP7906ABI3UnQyDOhY0n",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790262807535,
                    "orig_timestamp_utc": "2026-09-24T15:13:27.000Z",
                    "orig_write_time": 1790263000591,
                    "outbytes_delta": 99,
                    "outbytes_total": 99,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 27,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262990595,
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
                    "srcport": 59551,
                    "start_bucket_time": 1790262960000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790263383945,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 383354,
                        "status": "New"
                    },
                    "stellar_da_input": 1719,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "00a1f478-27da-43c8-b965-956671ca98e21790263384093-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790263260000,
                    "summary_start": 1790262960000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262807535,
                    "timestamp_utc": "2026-09-24T15:13:27.000Z",
                    "tos": 0,
                    "totalbytes": 262,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263384093,
                    "xdr_event": {
                        "description": "A host \"IP: 10.11.1.1, name: ad.technoma.local\" queried \"IP: 8.8.4.4, name: dns.google\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
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
            }
        ]
    }
}
```
