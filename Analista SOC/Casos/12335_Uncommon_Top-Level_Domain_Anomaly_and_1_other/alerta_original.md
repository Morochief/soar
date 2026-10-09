=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "283cf307-6083-4cf6-9ea7-a06a4c5902171784297702803-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14463,
                "_primary_term": 3,
                "_ignored": [
                    "metadata.request.domain_creation"
                ],
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.49.10.11.1.1.53.32",
                    "anomaly_id": "XbFncJ8BI3UnQyDO_DPk",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 23,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "www.farmatodo.com.ve",
                        "farmatodo.com.ve"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "www.farmatodo.com.ve"
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
                    "duration": 57,
                    "end_bucket_time": 1784297400000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 25,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 37.62,
                    "flow_score": 100,
                    "inbytes_delta": 246,
                    "inbytes_total": 246,
                    "inpkts_delta": 4,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "",
                            "effective_tld": "farmatodo.com.ve",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "www.farmatodo.com.ve",
                            "query_type": "HTTPS",
                            "transaction_id": 5620
                        },
                        "transaction_id": 5620
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
                    "orig_id": "XbFncJ8BI3UnQyDO_DPk",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 398,
                    "outbytes_total": 398,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784297288311,
                    "response_time": 0,
                    "severity": 20,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.49",
                    "srcip": "192.168.169.49",
                    "srcip_assetid": "03575614-cc86-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-daquino.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 62742,
                    "start_bucket_time": 1784297100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784297702744,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 412251,
                        "status": "New"
                    },
                    "stellar_da_input": 911,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "283cf307-6083-4cf6-9ea7-a06a4c5902171784297702803-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784297287473,
                    "timestamp_utc": "2026-07-17T14:08:07.000Z",
                    "tos": 0,
                    "totalbytes": 644,
                    "totalpackets": 10,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784297702803,
                    "xdr_event": {
                        "description": "The host nb-daquino.technoma.local has sent a DNS query with a new top-level domain farmatodo.com.ve, that has never been seen before in the past 23 days. Investigate whether the host should be blocked.",
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
                "_id": "60ecb1eb-77b1-40f8-a9e9-93d645a579e61784304302497-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14606,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.49.10.11.1.1.53.32",
                    "anomaly_id": "97rNcJ8BI3UnQyDOJ5pG",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 22,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "i.clean.gg",
                        "clean.gg"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "i.clean.gg"
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
                    "end_bucket_time": 1784304000000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 24,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 36.2,
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
                            "effective_tld": "clean.gg",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "i.clean.gg",
                            "query_type": "HTTPS",
                            "transaction_id": 23129
                        },
                        "transaction_id": 23129
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
                    "orig_id": "97rNcJ8BI3UnQyDOJ5pG",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 388,
                    "outbytes_total": 388,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784303912476,
                    "response_time": 0,
                    "severity": 20,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.49",
                    "srcip": "192.168.169.49",
                    "srcip_assetid": "fda7a6c2-cb0b-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-daquino.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51059,
                    "start_bucket_time": 1784303700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784304302482,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 382277,
                        "status": "New"
                    },
                    "stellar_da_input": 902,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "60ecb1eb-77b1-40f8-a9e9-93d645a579e61784304302497-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784303911906,
                    "timestamp_utc": "2026-07-17T15:58:31.000Z",
                    "tos": 0,
                    "totalbytes": 634,
                    "totalpackets": 10,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784304302497,
                    "xdr_event": {
                        "description": "The host nb-daquino.technoma.local has sent a DNS query with a new top-level domain clean.gg, that has never been seen before in the past 22 days. Investigate whether the host should be blocked.",
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