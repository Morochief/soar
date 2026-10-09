=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "e5abc7e1-2b5e-4a0f-9b7f-90e6344f9c521784964002714-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5962,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 11,
                    "aella_tuples": "192.168.169.127.10.11.1.1.445.185",
                    "anomaly_id": "1XocmJ8BI3UnQyDO7vb7",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.127"
                    ],
                    "detector_index": 0,
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
                    "dstport": 445,
                    "duration": 7923,
                    "end_bucket_time": 1784963700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [],
                        "smb_path_summary": []
                    },
                    "event_type": "conn",
                    "fidelity": 43.25,
                    "flow_score": 100,
                    "inbytes_delta": 1538,
                    "inbytes_total": 11346,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
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
                    "orig_id": "1XocmJ8BI3UnQyDO7vb7",
                    "orig_index": "aella-adr-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1946,
                    "outbytes_total": 18665,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784963455543,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.127",
                    "srcip": "192.168.169.127",
                    "srcip_assetid": "905efa22-cb18-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.127",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 59678,
                    "start_bucket_time": 1784963400000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784964002652,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 542368,
                        "status": "New"
                    },
                    "stellar_da_input": 1912,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e5abc7e1-2b5e-4a0f-9b7f-90e6344f9c521784964002714-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 3,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784963455065,
                    "timestamp_utc": "2026-07-25T07:10:55.000Z",
                    "tos": 0,
                    "totalbytes": 30011,
                    "totalpackets": 18,
                    "typical": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784964002714,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.127\" private) has sent an anomalously large number (#: 11) of SMB write requests, compared to its typical number (#: 2), measured in a 5.0-minute interval.",
                        "display_name": "Internal SMB Write Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_anomaly",
                        "scope": "Internal",
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Internal",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "29945497-8fc1-4172-8aa1-4c0cc2632f511784974501841-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5970,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 103,
                    "aella_tuples": "10.11.1.1.45.161.239.50.80.562",
                    "anomaly_id": "kH_AmJ8BI3UnQyDO93JS",
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
                    "dstip": "45.161.239.50",
                    "dstip_asn": 61512,
                    "dstip_asn_org": "GIG@NET SOCIEDAD ANONIMA",
                    "dstip_geo": {
                        "city": "Ciudad del Este",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.5036,
                        "longitude": -54.6507,
                        "region": "Alto Paraná Department"
                    },
                    "dstip_geo_point": "-25.5036,-54.6507",
                    "dstip_host": "45.161.239.50",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 80,
                    "duration": 96934,
                    "end_bucket_time": 1784974200000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 23,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 56.94,
                    "flow_score": 98,
                    "inbytes_delta": 5440263,
                    "inbytes_total": 275275829,
                    "inpkts_delta": 3600,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "mime_type": "application/octet-stream",
                                "processing_time": 8,
                                "response_time": 8
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 264,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 265,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 251,
                                "mime_type": "application/octet-stream",
                                "processing_time": 678,
                                "response_time": 678
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 266,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 252,
                                "mime_type": "application/octet-stream",
                                "processing_time": 8,
                                "response_time": 8
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 267,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 253,
                                "mime_type": "application/octet-stream",
                                "processing_time": 7,
                                "response_time": 7
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 268,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 254,
                                "mime_type": "application/octet-stream",
                                "processing_time": 7,
                                "response_time": 7
                            }
                        },
                        {
                            "request": {
                                "index": 269,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
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
                    "orig_id": "kH_AmJ8BI3UnQyDO93JS",
                    "orig_index": "aella-adr-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 11871,
                    "outbytes_total": 1399065,
                    "outpkts_delta": 162,
                    "port_name": "ethernet1",
                    "processing_time": 141,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784974200092,
                    "response_time": 141,
                    "severity": 15,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 60537,
                    "start_bucket_time": 1784973900000,
                    "state": "Created",
                    "stellar": {
                        "alert_time": 1784974501825,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 291680,
                        "status": "New",
                        "threshold": 31
                    },
                    "stellar_da_input": 3707,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "29945497-8fc1-4172-8aa1-4c0cc2632f511784974501841-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784974199226,
                    "timestamp_utc": "2026-07-25T10:09:59.000Z",
                    "tos": 2,
                    "totalbytes": 276674894,
                    "totalpackets": 3762,
                    "url": "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                    "url_list": [
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D"
                    ],
                    "url_reputation": "Good",
                    "url_reputation_source": "",
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784974501841,
                    "xdr_event": {
                        "description": "The internal application windows_update has an anomalously large number (#: 103) of connections from one or more source hosts to one or more external hosts (such as from \"IP: 10.11.1.1, name: technoma.local\" to \"IP/name: 45.161.239.50\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 31) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "fea20bb6-e0ae-4947-8f1a-1e99183254b71784974801766-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5971,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 70,
                    "aella_tuples": "10.11.1.1.45.161.239.50.80.562",
                    "anomaly_id": "hH_AmJ8BI3UnQyDO93JI",
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
                    "dstip": "45.161.239.50",
                    "dstip_asn": 61512,
                    "dstip_asn_org": "GIG@NET SOCIEDAD ANONIMA",
                    "dstip_geo": {
                        "city": "Ciudad del Este",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.5036,
                        "longitude": -54.6507,
                        "region": "Alto Paraná Department"
                    },
                    "dstip_geo_point": "-25.5036,-54.6507",
                    "dstip_host": "45.161.239.50",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 80,
                    "duration": 101437,
                    "end_bucket_time": 1784974500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "pripub_appid",
                    "event_score": 23,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 51.38,
                    "flow_score": 98,
                    "inbytes_delta": 5440401,
                    "inbytes_total": 254605257,
                    "inpkts_delta": 3600,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 251,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 230,
                                "mime_type": "application/octet-stream",
                                "processing_time": 997,
                                "response_time": 997
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 252,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 231,
                                "mime_type": "application/octet-stream",
                                "processing_time": 289,
                                "response_time": 289
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 253,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 232,
                                "mime_type": "application/octet-stream",
                                "processing_time": 281,
                                "response_time": 281
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 254,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 233,
                                "mime_type": "application/octet-stream",
                                "processing_time": 8,
                                "response_time": 8
                            }
                        },
                        {
                            "request": {
                                "host": "3.tlu.dl.delivery.mp.microsoft.com",
                                "index": 255,
                                "method": "GET",
                                "server": "3.tlu.dl.delivery.mp.microsoft.com",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
                            },
                            "response": {
                                "code": 206,
                                "file_type": "data",
                                "index": 234,
                                "mime_type": "application/octet-stream",
                                "processing_time": 565,
                                "response_time": 565
                            }
                        },
                        {
                            "request": {
                                "index": 256,
                                "method": "GET",
                                "uri": "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                                "user_agent": "Microsoft-Delivery-Optimization/10.0"
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
                    "orig_id": "hH_AmJ8BI3UnQyDO93JI",
                    "orig_index": "aella-adr-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 18726,
                    "outbytes_total": 1369031,
                    "outpkts_delta": 269,
                    "port_name": "ethernet1",
                    "processing_time": 428,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784974204087,
                    "response_time": 428,
                    "severity": 15,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 60539,
                    "start_bucket_time": 1784974200000,
                    "state": "Created",
                    "stellar": {
                        "alert_time": 1784974801748,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 591502,
                        "status": "New",
                        "threshold": 31
                    },
                    "stellar_da_input": 3684,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fea20bb6-e0ae-4947-8f1a-1e99183254b71784974801766-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784974203797,
                    "timestamp_utc": "2026-07-25T10:10:03.000Z",
                    "tos": 2,
                    "totalbytes": 255974288,
                    "totalpackets": 3869,
                    "url": "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D,/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                    "url_list": [
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D",
                        "/filestreamingservice/files/ee36ea64-efe5-4b97-92f3-fc35979cea50?P1=1784990671&P2=404&P3=2&P4=cMB3HY6Wa9xgD8bPFXlMzsbfI7UlUx314rizaDR5KwwhEz4P%2BuZkUU4l4xTSoNMdp5y8iDiy0%2BEoUM4vgcOMaw%3D%3D"
                    ],
                    "url_reputation": "Good",
                    "url_reputation_source": "",
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784974801766,
                    "xdr_event": {
                        "description": "The internal application windows_update has an anomalously large number (#: 70) of connections from one or more source hosts to one or more external hosts (such as from \"IP: 10.11.1.1, name: technoma.local\" to \"IP/name: 45.161.239.50\") in a 5.0-minute interval. This number of connections exceeds the threshold value of (#: 31) connections per interval, while 99.99% of all other 5.0-minute intervals, corresponding to different applications in the past two weeks, fall below this threshold.",
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