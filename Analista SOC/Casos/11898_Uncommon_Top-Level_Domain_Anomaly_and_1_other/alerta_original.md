=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "7fb137c5-f047-4729-ac1e-1d7b01d448dd1783600502607-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6780,
                "_primary_term": 1,
                "_ignored": [
                    "metadata.request.domain_creation"
                ],
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.16.10.11.1.1.53.32",
                    "anomaly_id": "TwvaRp8BBi0xHyA-BWql",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 35,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "www.magistvlatino.lat",
                        "magistvlatino.lat"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "www.magistvlatino.lat"
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
                    "duration": 139,
                    "end_bucket_time": 1783600200000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 28,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 54.37,
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
                            "effective_tld": "magistvlatino.lat",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "www.magistvlatino.lat",
                            "query_type": "HTTPS",
                            "transaction_id": 37995
                        },
                        "transaction_id": 37995
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
                    "orig_id": "TwvaRp8BBi0xHyA-BWql",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 399,
                    "outbytes_total": 399,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783600118730,
                    "response_time": 0,
                    "severity": 20,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.16",
                    "srcip": "192.168.169.16",
                    "srcip_assetid": "342045f8-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-rmartinez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 58962,
                    "start_bucket_time": 1783599900000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783600502566,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 381751,
                        "status": "New"
                    },
                    "stellar_da_input": 914,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7fb137c5-f047-4729-ac1e-1d7b01d448dd1783600502607-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783600117934,
                    "timestamp_utc": "2026-07-09T12:28:37.000Z",
                    "tos": 0,
                    "totalbytes": 645,
                    "totalpackets": 10,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783600502607,
                    "xdr_event": {
                        "description": "The host nb-rmartinez.technoma.local has sent a DNS query with a new top-level domain magistvlatino.lat, that has never been seen before in the past 35 days. Investigate whether the host should be blocked.",
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
                "_id": "d1e01f7b-9a6a-45a3-80ea-c2e054c2df141783604102611-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6870,
                "_primary_term": 1,
                "_ignored": [
                    "metadata.request.domain_creation"
                ],
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.16.10.11.1.1.53.32",
                    "anomaly_id": "ZhAOR58BBi0xHyA--bIC",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "days_silent": 202,
                    "detected_fields": [
                        "metadata.request.query",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "www.pinta.art",
                        "www.pinta.art"
                    ],
                    "detector_index": 0,
                    "domain_list": [
                        "www.pinta.art"
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
                    "duration": 47,
                    "end_bucket_time": 1783603800000,
                    "end_reason": 4,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "fidelity": 91.92,
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
                            "effective_tld": "www.pinta.art",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "www.pinta.art",
                            "query_type": "HTTPS",
                            "transaction_id": 49305
                        },
                        "transaction_id": 49305
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
                    "orig_id": "ZhAOR58BBi0xHyA--bIC",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 391,
                    "outbytes_total": 391,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783603587115,
                    "response_time": 0,
                    "severity": 20,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.16",
                    "srcip": "192.168.169.16",
                    "srcip_assetid": "342045f8-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-rmartinez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54364,
                    "start_bucket_time": 1783603500000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783604102596,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 511663,
                        "status": "New"
                    },
                    "stellar_da_input": 905,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d1e01f7b-9a6a-45a3-80ea-c2e054c2df141783604102611-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783603586064,
                    "timestamp_utc": "2026-07-09T13:26:26.000Z",
                    "tos": 0,
                    "totalbytes": 637,
                    "totalpackets": 10,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783604102611,
                    "xdr_event": {
                        "description": "The host nb-rmartinez.technoma.local has sent a DNS query with a new top-level domain www.pinta.art, that has never been seen before in the past 202 days. Investigate whether the host should be blocked.",
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