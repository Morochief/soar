=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "5f5ebb00-8e48-4238-a79b-90277508a5c51784711702631-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2072,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 94,
                    "aella_tuples": "192.168.169.119.10.11.1.1.445.185",
                    "anomaly_id": "W7cViZ8BI3UnQyDORuHS",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.119"
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
                    "end_bucket_time": 1784711400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 34,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$",
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 2
                            },
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 4
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 98.59,
                    "flow_score": 100,
                    "inbytes_delta": 2593,
                    "inbytes_total": 2593,
                    "inpkts_delta": 11,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "metadata": [
                        {
                            "request": {
                                "command": 114,
                                "nt_status": 0,
                                "user_id": 0,
                                "version": 1
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 2,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 0,
                                "version": 2
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 1,
                                "response_time": 3,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 1,
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 2,
                                "response_time": 4,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\SysVol",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 11,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 11,
                                "filename": "technoma.local\\Policies\\{3F7D6B5B-761B-4B7D-9C9D-9D3E8E200B52}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 1,
                                "response_time": 3
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
                                "command": 5,
                                "filename": "technoma.local\\Policies\\{8172E035-096F-4520-9BFF-42E70678B00F}\\gpt.ini",
                                "version": 2
                            },
                            "response": {
                                "processing_time": 1,
                                "response_time": 3,
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
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "W7cViZ8BI3UnQyDORuHS",
                    "orig_index": "aella-adr-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 6063,
                    "outbytes_total": 6063,
                    "outpkts_delta": 14,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784711293161,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.119",
                    "srcip": "192.168.169.119",
                    "srcip_assetid": "20292710-fd3f-11f0-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-noc2.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49732,
                    "start_bucket_time": 1784711100000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784711702613,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 402413,
                        "status": "New"
                    },
                    "stellar_da_input": 2075,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "5f5ebb00-8e48-4238-a79b-90277508a5c51784711702631-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784711292025,
                    "timestamp_utc": "2026-07-22T09:08:12.000Z",
                    "tos": 0,
                    "totalbytes": 8656,
                    "totalpackets": 25,
                    "typical": 10,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784711702631,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.119, name: nb-noc2.technoma.local\" private) has sent an anomalously large number (#: 94) of SMB read requests, compared to its typical number (#: 10), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$, \\\\ad.technoma.local\\SysVol very frequently.",
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
                "_id": "68fdb041-dee0-4a2a-bc0d-a7eacdb3cfbb1784711702429-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2071,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 28,
                    "aella_tuples": "192.168.169.119.10.11.1.1.445.185",
                    "anomaly_id": "urcWiZ8BI3UnQyDOCueB",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.119"
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
                    "duration": 50103,
                    "end_bucket_time": 1784711400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$",
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 3
                            },
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 90.45,
                    "flow_score": 100,
                    "inbytes_delta": 1780,
                    "inbytes_total": 1450200,
                    "inpkts_delta": 10,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 6,
                                "processing_time": 0,
                                "response_time": 2
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
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\ad.technoma.local\\IPC$",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "lsarpc",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
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
                                "processing_time": 0,
                                "response_time": 2,
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
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "command": 9,
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
                                "command": 9,
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
                    "orig_id": "urcWiZ8BI3UnQyDOCueB",
                    "orig_index": "aella-adr-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1970,
                    "outbytes_total": 187758,
                    "outpkts_delta": 10,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784711342536,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.119",
                    "srcip": "192.168.169.119",
                    "srcip_assetid": "20292710-fd3f-11f0-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-noc2.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49732,
                    "start_bucket_time": 1784711100000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784711702410,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 352201,
                        "status": "New"
                    },
                    "stellar_da_input": 1949,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "68fdb041-dee0-4a2a-bc0d-a7eacdb3cfbb1784711702429-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784711342129,
                    "timestamp_utc": "2026-07-22T09:09:02.000Z",
                    "tos": 0,
                    "totalbytes": 1637958,
                    "totalpackets": 20,
                    "typical": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784711702429,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.119, name: nb-noc2.technoma.local\" private) has sent an anomalously large number (#: 28) of SMB write requests, compared to its typical number (#: 4), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$, \\\\ad.technoma.local\\SysVol very frequently.",
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
            }
        ]
    }
}