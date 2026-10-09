=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "d6091a61-22da-47e1-91ed-28cf916404171784206203427-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11905,
                "_primary_term": 3,
                "_ignored": [
                    "metadata.request.domain_creation"
                ],
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.43.10.11.1.1.53.32",
                    "anomaly_id": "w1byap8BI3UnQyDOb0rx",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 36,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "en.meming.world",
                        "meming.world"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "en.meming.world"
                    ],
                    "domain_reputation": "Good",
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
                    "dstport": 53,
                    "duration": 63,
                    "end_bucket_time": 1784205900000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 28,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 55.51,
                    "flow_score": 100,
                    "inbytes_delta": 246,
                    "inbytes_total": 246,
                    "inpkts_delta": 4,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "",
                            "effective_tld": "meming.world",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "en.meming.world",
                            "query_type": "HTTPS",
                            "transaction_id": 4668
                        },
                        "transaction_id": 4668
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
                    "orig_id": "w1byap8BI3UnQyDOb0rx",
                    "orig_index": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 393,
                    "outbytes_total": 393,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784205699181,
                    "response_time": 0,
                    "severity": 20,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.43",
                    "srcip": "192.168.169.43",
                    "srcip_assetid": "29a0d6dc-cac5-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-larce.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 20336,
                    "start_bucket_time": 1784205600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784206203412,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 502929,
                        "status": "New"
                    },
                    "stellar_da_input": 906,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d6091a61-22da-47e1-91ed-28cf916404171784206203427-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784205698553,
                    "timestamp_utc": "2026-07-16T12:41:38.000Z",
                    "tos": 0,
                    "totalbytes": 639,
                    "totalpackets": 10,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784206203427,
                    "xdr_event": {
                        "description": "The host nb-larce.technoma.local has sent a DNS query with a new top-level domain meming.world, that has never been seen before in the past 36 days. Investigate whether the host should be blocked.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "3c1c18ba-4625-415b-a04d-4f080a4e00451784209144865-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11956,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.43.10.11.1.1.53.32",
                    "alert_time": 1784209144793,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-16 13:36:02 UTC",
                        "first_timestamp": 1784208962029,
                        "last_time_utc": "2026-07-16 13:36:02 UTC",
                        "last_timestamp": 1784208962029,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-16T13:37:00.000Z",
                        "scheduled_timestamp": 1784209020000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "None",
                        "2026-05-04T19:37:09Z"
                    ],
                    "domain_list": [
                        "sync.theagenticx.ai"
                    ],
                    "domain_reputation": "Good",
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
                    "dstport": 53,
                    "duration": 105,
                    "end_bucket_time": 1784209020000,
                    "end_reason": 4,
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
                    "flow_score": 100,
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 0,
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "172.240.45.49",
                                    "host_type": "A",
                                    "name": "sync.theagenticx.ai",
                                    "section_type": "Answer",
                                    "ttl": 300
                                }
                            ],
                            "domain_creation": "2026-05-04T19:37:09Z",
                            "effective_tld": "theagenticx.ai",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "query": "sync.theagenticx.ai",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "172.240.45.49"
                            ],
                            "transaction_id": 39605
                        },
                        "transaction_id": 39605
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
                    "orig_id": "vFska58BI3UnQyDOVCY0",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1784208962029,
                    "orig_timestamp_utc": "2026-07-16T13:36:02.000Z",
                    "orig_write_time": 1784208970222,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 29,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784208962457,
                    "response_time": 32,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.43",
                    "srcip": "192.168.169.43",
                    "srcip_assetid": "29a0d6dc-cac5-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-larce.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 1078,
                    "start_bucket_time": 1784208720000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784209144793,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 174571,
                        "status": "New"
                    },
                    "stellar_da_input": 1492,
                    "stellar_index": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3c1c18ba-4625-415b-a04d-4f080a4e00451784209144865-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1784209020000,
                    "summary_start": 1784208720000,
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784208962029,
                    "timestamp_utc": "2026-07-16T13:36:02.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784209144864,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.43, name: nb-larce.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain theagenticx.ai,  which was registered on 2026-05-04T19:37:09Z  (less than 90 days ago).",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "dbab1d48-d77c-4862-9a08-57bca6a9e02d1784209144865-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11957,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.43.10.11.1.1.53.32",
                    "alert_time": 1784209144796,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-16 13:36:02 UTC",
                        "first_timestamp": 1784208962029,
                        "last_time_utc": "2026-07-16 13:36:02 UTC",
                        "last_timestamp": 1784208962029,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-16T13:37:00.000Z",
                        "scheduled_timestamp": 1784209020000
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
                    "dstport": 53,
                    "duration": 105,
                    "end_bucket_time": 1784209020000,
                    "end_reason": 4,
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
                    "flow_score": 100,
                    "inbytes_delta": 464,
                    "inbytes_total": 464,
                    "inpkts_delta": 6,
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
                            "message_type": "QUERY",
                            "query": "sync.theagenticx.ai",
                            "query_type": "A",
                            "transaction_id": 39605
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "172.240.45.49",
                                    "host_type": "A",
                                    "name": "sync.theagenticx.ai",
                                    "section_type": "Answer",
                                    "ttl": 300
                                }
                            ],
                            "domain_creation": "2026-05-04T19:37:09Z",
                            "effective_tld": "theagenticx.ai",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 29,
                            "query": "sync.theagenticx.ai",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "172.240.45.49"
                            ],
                            "response_time": 32,
                            "transaction_id": 39605
                        },
                        "transaction_id": 39605
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
                    "orig_id": "u1ska58BI3UnQyDOVCY0",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1784208962029,
                    "orig_timestamp_utc": "2026-07-16T13:36:02.000Z",
                    "orig_write_time": 1784208970222,
                    "outbytes_delta": 463,
                    "outbytes_total": 463,
                    "outpkts_delta": 7,
                    "port_name": "ethernet1",
                    "processing_time": 29,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784208962457,
                    "response_time": 32,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.43",
                    "srcip": "192.168.169.43",
                    "srcip_assetid": "29a0d6dc-cac5-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-larce.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 1078,
                    "start_bucket_time": 1784208720000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784209144796,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 174574,
                        "status": "New"
                    },
                    "stellar_da_input": 1492,
                    "stellar_index": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "dbab1d48-d77c-4862-9a08-57bca6a9e02d1784209144865-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1784209020000,
                    "summary_start": 1784208720000,
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784208962029,
                    "timestamp_utc": "2026-07-16T13:36:02.000Z",
                    "tos": 0,
                    "totalbytes": 927,
                    "totalpackets": 13,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784209144864,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.43, name: nb-larce.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain theagenticx.ai,  which was registered on 2026-05-04T19:37:09Z  (less than 90 days ago).",
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