=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "792d7c27-f297-4cca-9580-247bd645a34b1784804102542-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3495,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 127,
                    "aella_tuples": "192.168.169.15.10.11.1.5.445.185",
                    "anomaly_id": "j_-Vjp8BI3UnQyDO96ay",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.15"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:0c:29:82:49:5f.1101.10.11.1.5",
                    "dstip": "10.11.1.5",
                    "dstip_assetid": "336850d8-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "adm-fs.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:0c:29:82:49:5f",
                    "dstport": 445,
                    "duration": 45607,
                    "end_bucket_time": 1784803800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 34,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [],
                        "smb_path_summary": []
                    },
                    "event_type": "conn",
                    "fidelity": 99.12,
                    "flow_score": 100,
                    "inbytes_delta": 49102,
                    "inbytes_total": 10903219,
                    "inpkts_delta": 50,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2
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
                                "response_time": 2,
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
                                "response_time": 2,
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
                                "processing_time": 9,
                                "response_time": 11,
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
                                "response_time": 2,
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
                                "response_time": 2,
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
                                "response_time": 2,
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
                                "response_time": 2,
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
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
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
                    "orig_id": "j_-Vjp8BI3UnQyDO96ay",
                    "orig_index": "aella-adr-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2925,
                    "outbytes_total": 147777,
                    "outpkts_delta": 21,
                    "port_name": "ethernet1",
                    "processing_time": 1,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784803613948,
                    "response_time": 3,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username": "danielsaavedra",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.15",
                    "srcip": "192.168.169.15",
                    "srcip_assetid": "bea4d810-cac4-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ainsaurralde.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 63421,
                    "start_bucket_time": 1784803500000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784804102519,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 482268,
                        "status": "New"
                    },
                    "stellar_da_input": 1938,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "792d7c27-f297-4cca-9580-247bd645a34b1784804102542-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784803613617,
                    "timestamp_utc": "2026-07-23T10:46:53.000Z",
                    "tos": 0,
                    "totalbytes": 11050996,
                    "totalpackets": 71,
                    "typical": 12,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784804102542,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.15, name: nb-ainsaurralde.technoma.local\" private) has sent an anomalously large number (#: 127) of SMB read requests, compared to its typical number (#: 12), measured in a 5.0-minute interval.",
                        "display_name": "Internal SMB Read Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_read_anomaly",
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
                            "id": "T1210",
                            "name": "Exploitation of Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "590a6ebb-2d10-496f-ad61-0e8edb0bef691784810402987-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3530,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 69,
                    "aella_tuples": "192.168.169.64.10.11.1.5.445.185",
                    "anomaly_id": "owT1jp8BI3UnQyDOpPZ1",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.64"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:0c:29:82:49:5f.1101.10.11.1.5",
                    "dstip": "10.11.1.5",
                    "dstip_assetid": "336850d8-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "adm-fs.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:0c:29:82:49:5f",
                    "dstport": 445,
                    "duration": 297495,
                    "end_bucket_time": 1784810100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 32,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\10.11.1.5\\IPC$",
                            "\\\\ad.technoma.local\\sysvol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\10.11.1.5\\IPC$",
                                "value": 1
                            },
                            {
                                "key": "\\\\ad.technoma.local\\sysvol",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 85.16,
                    "flow_score": 100,
                    "inbytes_delta": 2174,
                    "inbytes_total": 432726,
                    "inpkts_delta": 17,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 6,
                                "nt_status": 0,
                                "processing_time": 16,
                                "response_time": 18
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\10.11.1.5\\IPC$",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 415,
                                "response_time": 417,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "srvsvc",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 223,
                                "response_time": 225,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            },
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 219,
                                "response_time": 221,
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
                                "processing_time": 211,
                                "response_time": 213,
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
                                "processing_time": 237,
                                "response_time": 239,
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
                                "processing_time": 214,
                                "response_time": 216,
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
                                "processing_time": 204,
                                "response_time": 206,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 6,
                                "version": 2
                            },
                            "response": {
                                "command": 6,
                                "nt_status": 0,
                                "processing_time": 211,
                                "response_time": 213,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
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
                    "orig_id": "owT1jp8BI3UnQyDOpPZ1",
                    "orig_index": "aella-adr-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1650,
                    "outbytes_total": 67709,
                    "outpkts_delta": 8,
                    "port_name": "ethernet1",
                    "processing_time": 216,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784809881563,
                    "response_time": 218,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username": "jorgevaliente",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.64",
                    "srcip": "192.168.169.64",
                    "srcip_assetid": "9bb67eee-7cc1-11f1-8b6c-36d860317dc9",
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
                    "srcip_host": "nb-jvaliente.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 64985,
                    "start_bucket_time": 1784809800000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784810402975,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 512774,
                        "status": "New"
                    },
                    "stellar_da_input": 2021,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "590a6ebb-2d10-496f-ad61-0e8edb0bef691784810402987-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784809879954,
                    "timestamp_utc": "2026-07-23T12:31:19.000Z",
                    "tos": 0,
                    "totalbytes": 500435,
                    "totalpackets": 25,
                    "typical": 16,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784810402987,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.64, name: nb-jvaliente.technoma.local\" private) has sent an anomalously large number (#: 69) of SMB read requests, compared to its typical number (#: 16), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\10.11.1.5\\IPC$, \\\\ad.technoma.local\\sysvol very frequently.",
                        "display_name": "Internal SMB Read Anomaly",
                        "framework_version": "v8",
                        "name": "internal_smb_read_anomaly",
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
                            "id": "T1210",
                            "name": "Exploitation of Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}