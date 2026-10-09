# Alertas Originales Interflow / Stellar Cyber - Lote de 4 Eventos

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "bcc79162-d256-4abc-80e6-4ec9f7cef8121790262001880-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19437,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 224,
                    "aella_tuples": "10.11.1.5.199.232.214.172.80.562",
                    "anomaly_id": "__rl06ABI3UnQyDOu7mA",
                    "app_path": "http.microsoft",
                    "appid": 562,
                    "appid_family": "Web",
                    "appid_name": "windows_update",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "appid"
                    ],
                    "detected_values": [
                        "562"
                    ],
                    "dscp_name": "Best Effort",
                    "dstip": "199.232.214.172",
                    "dstip_asn": 54113,
                    "dstip_asn_org": "Fastly, Inc.",
                    "dstip_domain_creation": "2011-04-18T21:25:29Z",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "bg.microsoft.map.fastly.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 80,
                    "duration": 91979,
                    "end_bucket_time": 1790261700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 23,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 55.4,
                    "flow_score": 98,
                    "inbytes_delta": 683767,
                    "inbytes_total": 18900368,
                    "inpkts_delta": 464,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "mime_type": "application/octet-stream",
                                "processing_time": 1,
                                "response_time": 1
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 168,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/47e375ad-a10c-4c90-a161-555d91c9a5ad?P1=1790277960&P2=404&P3=2&P4=gNhzSK2wl%2FIGtTs2v96SvEMI6SiwFM2VENf5BeOV0muTjC1yrFdFQnkAO%2B2EOHaTYscNQoeFDLemofp6u%2F7TTw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 167,
                                "mime_type": "application/octet-stream",
                                "processing_time": 25,
                                "response_time": 25
                            }
                        }
                    ],
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 3,
                    "msgtype_name": "update",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "__rl06ABI3UnQyDOu7mA",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 18209,
                    "outbytes_total": 508806,
                    "outpkts_delta": 247,
                    "port_name": "ethernet1",
                    "processing_time": 20,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790261439887,
                    "response_time": 20,
                    "severity": 15,
                    "src_tuples": "00:0c:29:82:49:5f.1101.10.11.1.5",
                    "srcip": "10.11.1.5",
                    "srcip_assetid": "336850d8-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "adm-fs.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:0c:29:82:49:5f",
                    "srcport": 53458,
                    "start_bucket_time": 1790261400000,
                    "state": "Created",
                    "stellar": {
                        "alert_time": 1790262001874,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 560298,
                        "status": "New",
                        "threshold": 76
                    },
                    "stellar_da_input": 3444,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bcc79162-d256-4abc-80e6-4ec9f7cef8121790262001880-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790261438839,
                    "timestamp_utc": "2026-09-24T14:50:38.000Z",
                    "tos": 2,
                    "totalbytes": 19409174,
                    "totalpackets": 711,
                    "url": "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/47e375ad-a10c-4c90-a161-555d91c9a5ad?P1=1790277960&P2=404&P3=2&P4=gNhzSK2wl%2FIGtTs2v96SvEMI6SiwFM2VENf5BeOV0muTjC1yrFdFQnkAO%2B2EOHaTYscNQoeFDLemofp6u%2F7TTw%3D%3D",
                    "url_reputation": "Good",
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790262001880,
                    "xdr_event": {
                        "description": "The internal application windows_update has an anomalously large number (#: 224) of connections from one or more source hosts to one or more external hosts in a 5.0-minute interval.",
                        "display_name": "Application Usage Anomaly",
                        "framework_version": "v8",
                        "name": "pripub_appid",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "technique": {
                            "id": "XT2003",
                            "name": "XDR App Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "0891ddc8-7461-467e-8a02-6defc4dc35f41790262301647-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19449,
                "_source": {
                    "actual": 160,
                    "anomaly_id": "7fvp06ABI3UnQyDO_GdK",
                    "appid_name": "windows_update",
                    "dstip": "199.232.210.172",
                    "dstip_host": "office.microsoft.map.fastly.net",
                    "event_name": "pripub_appid",
                    "srcip": "10.11.1.5",
                    "srcip_host": "adm-fs.technoma.local",
                    "timestamp_utc": "2026-09-24T14:55:09.000Z"
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "b4d3a86e-aa6d-47bd-9d70-9d526d115e0b1790262602156-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19465,
                "_source": {
                    "actual": 217,
                    "anomaly_id": "Lvzx06ABI3UnQyDO7cHd",
                    "appid_name": "windows_update",
                    "dstip": "199.232.214.172",
                    "dstip_host": "fg.microsoft.map.fastly.net",
                    "event_name": "pripub_appid",
                    "srcip": "10.11.1.5",
                    "srcip_host": "adm-fs.technoma.local",
                    "timestamp_utc": "2026-09-24T15:03:51.000Z"
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "6663655d-5263-4be6-aade-093954856d091790263202027-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19561,
                "_source": {
                    "actual": 196,
                    "anomaly_id": "Nv3306ABI3UnQyDO4KwJ",
                    "appid_name": "windows_update",
                    "dstip": "199.232.214.172",
                    "dstip_host": "bg.microsoft.map.fastly.net",
                    "event_name": "pripub_appid",
                    "srcip": "10.11.1.5",
                    "srcip_host": "adm-fs.technoma.local",
                    "timestamp_utc": "2026-09-24T15:10:21.000Z"
                }
            }
        ]
    }
}
```
