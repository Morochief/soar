=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "48028417-be0e-4604-8da6-1c9de216381c1783701001754-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 8783,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 11,
                    "aella_tuples": "36.104.147.6.10.40.2.152.22.198",
                    "anomaly_id": "Q_PWTJ8BI3UnQyDO6ell",
                    "appid": 198,
                    "appid_family": "Encrypted",
                    "appid_name": "ssh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "36.104.147.6"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "12:b7:9e:19:51:47.0.10.40.2.152",
                    "dstip": "10.40.2.152",
                    "dstip_aella_flag": 1,
                    "dstip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "dstip_geo_point": "39.0469,-77.4903",
                    "dstip_host": "ip-10-40-2-152",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "12:b7:9e:19:51:47",
                    "dstport": 22,
                    "duration": 10240,
                    "end_bucket_time": 1783700700000,
                    "end_reason": 1,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event_category": "killchain",
                    "event_name": "scanner_rep",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 90.16,
                    "flow_score": 100,
                    "host": {
                        "ip": "10.40.2.152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "inbytes_delta": 1727,
                    "inbytes_total": 1727,
                    "inpkts_delta": 8,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "response": {
                            "processing_time": 12,
                            "response_time": 1303,
                            "version": "2.0"
                        }
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "linux_agent"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 0,
                    "netid_name": "vlan0",
                    "obsid": 170394264,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "Q_PWTJ8BI3UnQyDO6ell",
                    "orig_index": "aella-adr-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2582,
                    "outbytes_total": 2582,
                    "outpkts_delta": 10,
                    "port_name": "ethernet0",
                    "process_name": "systemd",
                    "process_user": "root",
                    "processing_time": 12,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783700577938,
                    "response_time": 1303,
                    "run_every": 5,
                    "severity": 20,
                    "srcip": "36.104.147.6",
                    "srcip_asn": 4134,
                    "srcip_asn_org": "Chinanet",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "CN",
                        "countryName": "China",
                        "latitude": 34.7732,
                        "longitude": 113.722,
                        "region": "Unknown"
                    },
                    "srcip_geo_point": "34.7732,113.722",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "36.104.147.6",
                    "srcip_reputation": "Scanner",
                    "srcip_reputation_source": "ETPro",
                    "srcip_type": "public",
                    "srcip_version": "ipv4",
                    "srcmac": "12:c2:40:1e:d2:1f",
                    "srcport": 52462,
                    "start_bucket_time": 1783700400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783701001743,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421330,
                        "status": "New"
                    },
                    "stellar_da_input": 890,
                    "stellar_index_id": "aella-ser-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "48028417-be0e-4604-8da6-1c9de216381c1783701001754-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 1291,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 57,
                    "timestamp": 1783700566651,
                    "timestamp_utc": "2026-07-10T16:22:46.000Z",
                    "tos": 0,
                    "totalbytes": 4309,
                    "totalpackets": 18,
                    "typical": 1,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783701001754,
                    "xdr_event": {
                        "description": "An anomalously large number (#: 11) of connections has been observed from a host (\"IP/name: 36.104.147.6\") with a reputation category of Scanner. The typical number of connections is 1, measured in a 5.0-minute interval.",
                        "display_name": "Scanner Reputation Anomaly",
                        "framework_version": "v8",
                        "name": "scanner_rep",
                        "scope": "",
                        "tactic": {
                            "id": "TA0043",
                            "name": "Reconnaissance"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1595",
                            "name": "Active Scanning"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "43ee6fcc-5e71-4d93-9eb5-b577cc11bca31783701601877-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 8790,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 8,
                    "aella_tuples": "36.104.147.6.10.40.2.152.22.198",
                    "anomaly_id": "J_TfTJ8BI3UnQyDOKF2V",
                    "appid": 198,
                    "appid_family": "Encrypted",
                    "appid_name": "ssh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "36.104.147.6"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "12:b7:9e:19:51:47.0.10.40.2.152",
                    "dstip": "10.40.2.152",
                    "dstip_aella_flag": 1,
                    "dstip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "dstip_geo_point": "39.0469,-77.4903",
                    "dstip_host": "ip-10-40-2-152",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "12:b7:9e:19:51:47",
                    "dstport": 22,
                    "duration": 7339,
                    "end_bucket_time": 1783701300000,
                    "end_reason": 4,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event_category": "killchain",
                    "event_name": "scanner_rep",
                    "event_score": 32,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 71.58,
                    "flow_score": 100,
                    "host": {
                        "ip": "10.40.2.152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "inbytes_delta": 3301,
                    "inbytes_total": 3301,
                    "inpkts_delta": 15,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "response": {
                            "processing_time": 13,
                            "response_time": 230,
                            "version": "2.0"
                        }
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "linux_agent"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 0,
                    "netid_name": "vlan0",
                    "obsid": 170394264,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "J_TfTJ8BI3UnQyDOKF2V",
                    "orig_index": "aella-adr-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 3358,
                    "outbytes_total": 3358,
                    "outpkts_delta": 16,
                    "port_name": "ethernet0",
                    "process_name": "systemd",
                    "process_user": "root",
                    "processing_time": 13,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783701114001,
                    "response_time": 230,
                    "run_every": 5,
                    "severity": 20,
                    "srcip": "36.104.147.6",
                    "srcip_asn": 4134,
                    "srcip_asn_org": "Chinanet",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "CN",
                        "countryName": "China",
                        "latitude": 34.7732,
                        "longitude": 113.722,
                        "region": "Unknown"
                    },
                    "srcip_geo_point": "34.7732,113.722",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "36.104.147.6",
                    "srcip_reputation": "Scanner",
                    "srcip_reputation_source": "ETPro",
                    "srcip_type": "public",
                    "srcip_version": "ipv4",
                    "srcmac": "12:c2:40:1e:d2:1f",
                    "srcport": 36368,
                    "start_bucket_time": 1783701000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783701601846,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 481258,
                        "status": "New"
                    },
                    "stellar_da_input": 887,
                    "stellar_index_id": "aella-ser-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "43ee6fcc-5e71-4d93-9eb5-b577cc11bca31783701601877-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 217,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 57,
                    "timestamp": 1783701106573,
                    "timestamp_utc": "2026-07-10T16:31:46.000Z",
                    "tos": 0,
                    "totalbytes": 6659,
                    "totalpackets": 31,
                    "typical": 2,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783701601877,
                    "xdr_event": {
                        "description": "An anomalously large number (#: 8) of connections has been observed from a host (\"IP/name: 36.104.147.6\") with a reputation category of Scanner. The typical number of connections is 2, measured in a 5.0-minute interval.",
                        "display_name": "Scanner Reputation Anomaly",
                        "framework_version": "v8",
                        "name": "scanner_rep",
                        "scope": "",
                        "tactic": {
                            "id": "TA0043",
                            "name": "Reconnaissance"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1595",
                            "name": "Active Scanning"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}