=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "89e00d79-c0f1-42bf-8b00-c906aa333cd91784213702485-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12073,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 135,
                    "aella_tuples": "192.168.169.96.10.11.1.5.445.185",
                    "anomaly_id": "p2Fja58BI3UnQyDOzywA",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.96"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:0c:29:82:49:5f.1101.10.11.1.5",
                    "dstip": "10.11.1.5",
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
                    "duration": 7751210,
                    "end_bucket_time": 1784213400000,
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
                    "fidelity": 99.09,
                    "flow_score": 100,
                    "inbytes_delta": 40928,
                    "inbytes_total": 26595294,
                    "inpkts_delta": 38,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 92,
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
                                "response_time": 92,
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
                                "processing_time": 1,
                                "response_time": 93,
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
                                "response_time": 92,
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
                                "response_time": 92,
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
                                "response_time": 92,
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
                                "response_time": 92,
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
                                "response_time": 92,
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
                                "response_time": 92,
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
                    "orig_id": "p2Fja58BI3UnQyDOzywA",
                    "orig_index": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2685,
                    "outbytes_total": 2804143,
                    "outpkts_delta": 28,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784213125555,
                    "response_time": 92,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username": "angelicalovera",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.96",
                    "srcip": "192.168.169.96",
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
                    "srcip_host": "nb-alovera.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 50501,
                    "start_bucket_time": 1784213100000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784213702472,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 572151,
                        "status": "New"
                    },
                    "stellar_da_input": 1963,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "89e00d79-c0f1-42bf-8b00-c906aa333cd91784213702485-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 92,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784213124501,
                    "timestamp_utc": "2026-07-16T14:45:24.000Z",
                    "tos": 0,
                    "totalbytes": 29399437,
                    "totalpackets": 66,
                    "typical": 13,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784213702485,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.96, name: nb-alovera.technoma.local\" private) has sent an anomalously large number (#: 135) of SMB read requests, compared to its typical number (#: 13), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "c86a71a9-056a-4b9e-a32a-bb555e6f90661784214302601-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12090,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 178,
                    "aella_tuples": "192.168.169.96.10.11.1.5.445.185",
                    "anomaly_id": "SGJua58BI3UnQyDOByKq",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.96"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:0c:29:82:49:5f.1101.10.11.1.5",
                    "dstip": "10.11.1.5",
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
                    "duration": 8421100,
                    "end_bucket_time": 1784214000000,
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
                            "\\\\10.11.1.5\\IPC$",
                            "\\\\ad.technoma.local\\SysVol"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\10.11.1.5\\IPC$",
                                "value": 1
                            },
                            {
                                "key": "\\\\ad.technoma.local\\SysVol",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 99.44,
                    "flow_score": 100,
                    "inbytes_delta": 2539,
                    "inbytes_total": 36410949,
                    "inpkts_delta": 13,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 92,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "path": "\\\\10.11.1.5\\IPC$",
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 92,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 3,
                                "processing_time": 0,
                                "response_time": 92
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
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": -1073741412,
                                "processing_time": 0,
                                "response_time": 92,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 92
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "command": 8,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 92,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 1,
                                "response_time": 93
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
                                "response_time": 92,
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
                                "processing_time": 0,
                                "response_time": 92,
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
                                "response_time": 92,
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
                    "orig_id": "SGJua58BI3UnQyDOByKq",
                    "orig_index": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2024,
                    "outbytes_total": 3486437,
                    "outpkts_delta": 14,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784213795482,
                    "response_time": 92,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username": "angelicalovera",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.96",
                    "srcip": "192.168.169.96",
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
                    "srcip_host": "nb-alovera.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 50501,
                    "start_bucket_time": 1784213700000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784214302584,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 502256,
                        "status": "New"
                    },
                    "stellar_da_input": 2051,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c86a71a9-056a-4b9e-a32a-bb555e6f90661784214302601-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 92,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784213794391,
                    "timestamp_utc": "2026-07-16T14:56:34.000Z",
                    "tos": 0,
                    "totalbytes": 39897386,
                    "totalpackets": 27,
                    "typical": 13,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784214302600,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.96, name: nb-alovera.technoma.local\" private) has sent an anomalously large number (#: 178) of SMB read requests, compared to its typical number (#: 13), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\10.11.1.5\\IPC$, \\\\ad.technoma.local\\SysVol very frequently.",
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