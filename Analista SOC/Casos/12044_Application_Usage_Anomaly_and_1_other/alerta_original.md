=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "c31649e5-8870-4479-9aa2-65789910f8861783828501938-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9705,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 9,
                    "aella_tuples": "192.168.15.75.172.217.115.4.443.51",
                    "anomaly_id": "_TxuVJ8BI3UnQyDO4r5w",
                    "app_path": "ssl.https",
                    "appid": 51,
                    "appid_family": "Webmail",
                    "appid_name": "gmail",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "appid"
                    ],
                    "detected_values": [
                        "51"
                    ],
                    "dscp_name": "Best Effort",
                    "dstip": "172.217.115.4",
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
                    "dstip_host": "play.googleapis.com",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 443,
                    "duration": 1222,
                    "end_bucket_time": 1783828200000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 18,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 23.92,
                    "flow_score": 98,
                    "inbytes_delta": 232150,
                    "inbytes_total": 232150,
                    "inpkts_delta": 171,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "request": {
                            "fingerprint_ja4": "t13d221100_231e334592e8_533b6d20482b"
                        },
                        "response": {
                            "mitm_score": 50,
                            "processing_time": 104,
                            "response_time": 104
                        }
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
                    "netid": 15,
                    "netid_name": "vlan15",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "_TxuVJ8BI3UnQyDO4r5w",
                    "orig_index": "aella-adr-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 15369,
                    "outbytes_total": 15369,
                    "outpkts_delta": 91,
                    "port_name": "ethernet1",
                    "processing_time": 104,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783827974302,
                    "response_time": 104,
                    "severity": 15,
                    "src_tuples": "00:50:56:96:49:9e.15.192.168.15.75",
                    "srcip": "192.168.15.75",
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
                    "srcip_host": "192.168.15.75",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:96:49:9e",
                    "srcport": 53556,
                    "start_bucket_time": 1783827900000,
                    "state": "NoSYN",
                    "stellar": {
                        "alert_time": 1783828501890,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 521598,
                        "status": "New",
                        "threshold": 6
                    },
                    "stellar_da_input": 946,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c31649e5-8870-4479-9aa2-65789910f8861783828501938-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783827940308,
                    "timestamp_utc": "2026-07-12T03:45:40.000Z",
                    "tos": 2,
                    "totalbytes": 247519,
                    "totalpackets": 262,
                    "vlan": 15,
                    "write_by": "sef",
                    "write_time": 1783828501938,
                    "xdr_event": {
                        "description": "The internal application gmail has an anomalously large number (#: 9) of connections from one or more source hosts to one or more external hosts (such as from \"IP/name: 192.168.15.75\" to \"IP: 172.217.115.4, name: play.googleapis.com\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 6) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
                        "display_name": "Application Usage Anomaly",
                        "framework_version": "v8",
                        "name": "pripub_appid",
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
                            "id": "XT2003",
                            "name": "XDR App Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "c876141e-0469-48cc-91e3-2d0eb4f7cf981783828502952-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9706,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 9,
                    "aella_tuples": "192.168.15.75.142.251.0.95.443.3618",
                    "anomaly_id": "VDxuVJ8BI3UnQyDO4b7p",
                    "app_path": "ssl.https",
                    "appid": 3618,
                    "appid_family": "Web",
                    "appid_name": "google_api",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "appid"
                    ],
                    "detected_values": [
                        "3618"
                    ],
                    "dscp_name": "Best Effort",
                    "dstip": "142.251.0.95",
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
                    "dstip_host": "142.251.0.95",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 443,
                    "duration": 793,
                    "end_bucket_time": 1783828200000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 18,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 23.92,
                    "flow_score": 98,
                    "inbytes_delta": 2284,
                    "inbytes_total": 2284,
                    "inpkts_delta": 9,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "request": {
                            "fingerprint_ja4": "t13d221100_231e334592e8_533b6d20482b"
                        },
                        "response": {
                            "mitm_score": 50,
                            "processing_time": 47,
                            "response_time": 47
                        }
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
                    "netid": 15,
                    "netid_name": "vlan15",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "VDxuVJ8BI3UnQyDO4b7p",
                    "orig_index": "aella-adr-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1517,
                    "outbytes_total": 1517,
                    "outpkts_delta": 8,
                    "port_name": "ethernet1",
                    "processing_time": 47,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783827973347,
                    "response_time": 47,
                    "severity": 15,
                    "src_tuples": "00:50:56:96:49:9e.15.192.168.15.75",
                    "srcip": "192.168.15.75",
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
                    "srcip_host": "192.168.15.75",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:96:49:9e",
                    "srcport": 53557,
                    "start_bucket_time": 1783827900000,
                    "state": "NoSYN",
                    "stellar": {
                        "alert_time": 1783828501922,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 521699,
                        "status": "New",
                        "threshold": 6
                    },
                    "stellar_da_input": 933,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c876141e-0469-48cc-91e3-2d0eb4f7cf981783828502952-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783827940759,
                    "timestamp_utc": "2026-07-12T03:45:40.000Z",
                    "tos": 2,
                    "totalbytes": 3801,
                    "totalpackets": 17,
                    "vlan": 15,
                    "write_by": "sef",
                    "write_time": 1783828502952,
                    "xdr_event": {
                        "description": "The internal application google_api has an anomalously large number (#: 9) of connections from one or more source hosts to one or more external hosts (such as from \"IP/name: 192.168.15.75\" to \"IP/name: 142.251.0.95\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 6) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
                        "display_name": "Application Usage Anomaly",
                        "framework_version": "v8",
                        "name": "pripub_appid",
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
                            "id": "XT2003",
                            "name": "XDR App Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}