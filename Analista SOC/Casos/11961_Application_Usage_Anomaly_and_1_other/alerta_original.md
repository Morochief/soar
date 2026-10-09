=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "e8954a67-7231-43a2-99bd-87738ffc65f91783670101956-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 8122,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5,
                    "aella_tuples": "192.168.15.75.162.159.61.3.443.5283",
                    "anomaly_id": "TtUAS58BI3UnQyDOBfSa",
                    "app_path": "ssl.https",
                    "appid": 5283,
                    "appid_family": "Network",
                    "appid_name": "doh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "appid"
                    ],
                    "detected_values": [
                        "5283"
                    ],
                    "dscp_name": "Best Effort",
                    "dstip": "162.159.61.3",
                    "dstip_asn": 13335,
                    "dstip_asn_org": "Cloudflare, Inc.",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "UN",
                        "countryName": "Unknown",
                        "latitude": null,
                        "longitude": null
                    },
                    "dstip_geo_point": "0.0,0.0",
                    "dstip_host": "162.159.61.3",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 443,
                    "duration": 6,
                    "end_bucket_time": 1783669800000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 23,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 56.79,
                    "flow_score": 98,
                    "inbytes_delta": 66,
                    "inbytes_total": 66,
                    "inpkts_delta": 1,
                    "lateral": false,
                    "locid": "unassigned location",
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
                    "orig_id": "TtUAS58BI3UnQyDOBfSa",
                    "orig_index": "aella-adr-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 60,
                    "outbytes_total": 60,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783669710164,
                    "response_time": 0,
                    "severity": 15,
                    "src_tuples": "00:50:56:96:49:9e.15.192.168.15.75",
                    "srcip": "192.168.15.75",
                    "srcip_assetid": "077d9fa6-70bd-11f1-801d-5ae6db116d2f",
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
                    "srcport": 57059,
                    "start_bucket_time": 1783669500000,
                    "state": "NoSYN",
                    "stellar": {
                        "alert_time": 1783670101945,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 381786,
                        "status": "New",
                        "threshold": 4
                    },
                    "stellar_da_input": 770,
                    "stellar_index_id": "aella-ser-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e8954a67-7231-43a2-99bd-87738ffc65f91783670101956-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783669678599,
                    "timestamp_utc": "2026-07-10T07:47:58.000Z",
                    "tos": 0,
                    "totalbytes": 126,
                    "totalpackets": 2,
                    "vlan": 15,
                    "write_by": "sef",
                    "write_time": 1783670101955,
                    "xdr_event": {
                        "description": "The internal application doh has an anomalously large number (#: 5) of connections from one or more source hosts to one or more external hosts (such as from \"IP/name: 192.168.15.75\" to \"IP/name: 162.159.61.3\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 4) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
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
                "_id": "31853c68-dc15-4662-bf32-e50ab23c4d3c1783670402214-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 8123,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 5,
                    "aella_tuples": "192.168.15.75.162.159.61.3.443.5283",
                    "anomaly_id": "pdYES58BI3UnQyDOJRcp",
                    "app_path": "ssl.https",
                    "appid": 5283,
                    "appid_family": "Network",
                    "appid_name": "doh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "appid"
                    ],
                    "detected_values": [
                        "5283"
                    ],
                    "dscp_name": "Best Effort",
                    "dstip": "162.159.61.3",
                    "dstip_asn": 13335,
                    "dstip_asn_org": "Cloudflare, Inc.",
                    "dstip_domain_creation": "2018-03-27T22:15:59Z",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "UN",
                        "countryName": "Unknown",
                        "latitude": null,
                        "longitude": null
                    },
                    "dstip_geo_point": "0.0,0.0",
                    "dstip_host": "chrome.cloudflare-dns.com",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 443,
                    "duration": 6,
                    "end_bucket_time": 1783670100000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 23,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 56.79,
                    "flow_score": 98,
                    "inbytes_delta": 66,
                    "inbytes_total": 66,
                    "inpkts_delta": 1,
                    "lateral": false,
                    "locid": "unassigned location",
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
                    "orig_id": "pdYES58BI3UnQyDOJRcp",
                    "orig_index": "aella-adr-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 60,
                    "outbytes_total": 60,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783669981134,
                    "response_time": 0,
                    "severity": 15,
                    "src_tuples": "00:50:56:96:49:9e.15.192.168.15.75",
                    "srcip": "192.168.15.75",
                    "srcip_assetid": "077d9fa6-70bd-11f1-801d-5ae6db116d2f",
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
                    "srcport": 57059,
                    "start_bucket_time": 1783669800000,
                    "state": "NoSYN",
                    "stellar": {
                        "alert_time": 1783670402169,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 411965,
                        "status": "New",
                        "threshold": 4
                    },
                    "stellar_da_input": 770,
                    "stellar_index_id": "aella-ser-2026.07.10-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "31853c68-dc15-4662-bf32-e50ab23c4d3c1783670402214-YWVsbGEtc2VyLTIwMjYuMDcuMTAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783669948636,
                    "timestamp_utc": "2026-07-10T07:52:28.000Z",
                    "tos": 0,
                    "totalbytes": 126,
                    "totalpackets": 2,
                    "vlan": 15,
                    "write_by": "sef",
                    "write_time": 1783670402214,
                    "xdr_event": {
                        "description": "The internal application doh has an anomalously large number (#: 5) of connections from one or more source hosts to one or more external hosts (such as from \"IP/name: 192.168.15.75\" to \"IP: 162.159.61.3, name: chrome.cloudflare-dns.com\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 4) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
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