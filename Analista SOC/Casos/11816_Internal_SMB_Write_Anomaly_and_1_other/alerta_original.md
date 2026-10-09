=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "c6cb0d9d-d55c-43d0-984e-6a9f80aafc561783518902685-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4929,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 62,
                    "aella_tuples": "192.168.169.105.10.11.1.5.445.185",
                    "anomaly_id": "Arz6QZ8BBi0xHyA-ePIa",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.105"
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
                    "duration": 40671,
                    "end_bucket_time": 1783518600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [],
                        "smb_path_summary": []
                    },
                    "event_type": "conn",
                    "fidelity": 98.16,
                    "flow_score": 100,
                    "inbytes_delta": 38622,
                    "inbytes_total": 525188,
                    "inpkts_delta": 612,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 16,
                                "processing_time": 4,
                                "response_time": 10
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 17,
                                "version": 2
                            },
                            "response": {
                                "command": 17,
                                "nt_status": 0,
                                "processing_time": 3,
                                "response_time": 9,
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
                                "processing_time": 379,
                                "response_time": 385,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 17,
                                "version": 2
                            },
                            "response": {
                                "command": 17,
                                "nt_status": 0,
                                "processing_time": 1,
                                "response_time": 7,
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
                                "processing_time": 24,
                                "response_time": 30,
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
                                "processing_time": 142,
                                "response_time": 148,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 175,
                                "response_time": 181
                            }
                        },
                        {
                            "request": {
                                "command": 16,
                                "filename": "TESORERIA\\PRESTAMOS\\PMOS ITTI THN 27-03 V4.xlsx",
                                "version": 2
                            },
                            "response": {
                                "command": 16,
                                "nt_status": 0,
                                "processing_time": 5,
                                "response_time": 11,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 17,
                                "version": 2
                            },
                            "response": {
                                "command": 17,
                                "nt_status": 0,
                                "processing_time": 6,
                                "response_time": 12,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 17,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 9,
                                "version": 2
                            },
                            "response": {
                                "processing_time": 86,
                                "response_time": 92,
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
                    "orig_id": "Arz6QZ8BBi0xHyA-ePIa",
                    "orig_index": "aella-adr-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 4898707,
                    "outbytes_total": 43166520,
                    "outpkts_delta": 3765,
                    "port_name": "ethernet1",
                    "processing_time": 82,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783518350245,
                    "response_time": 88,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username": "hectorbazan",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.105",
                    "srcip": "192.168.169.105",
                    "srcip_assetid": "58eae3e4-fe12-11f0-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-hbazan.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 60589,
                    "start_bucket_time": 1783518300000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783518902667,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 542029,
                        "status": "New"
                    },
                    "stellar_da_input": 2088,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c6cb0d9d-d55c-43d0-984e-6a9f80aafc561783518902685-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 6,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783518349430,
                    "timestamp_utc": "2026-07-08T13:45:49.000Z",
                    "tos": 0,
                    "totalbytes": 43691708,
                    "totalpackets": 4377,
                    "typical": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783518902685,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.105, name: nb-hbazan.technoma.local\" private) has sent an anomalously large number (#: 62) of SMB write requests, compared to its typical number (#: 4), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "f60d0a6b-f04a-415f-845a-116de86dbbe01783519502653-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4938,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 36,
                    "aella_tuples": "192.168.169.114.10.11.1.5.445.185",
                    "anomaly_id": "cr4EQp8BBi0xHyA-_xsX",
                    "app_path": "smb",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.114"
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
                    "duration": 1311738,
                    "end_bucket_time": 1783519200000,
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
                            "\\\\10.11.1.5\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\10.11.1.5\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 92.31,
                    "flow_score": 100,
                    "inbytes_delta": 1456,
                    "inbytes_total": 347335,
                    "inpkts_delta": 8,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "request": {
                                "command": 5,
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 5,
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
                                "response_time": 5,
                                "version": 2
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
                                "processing_time": 0,
                                "response_time": 5,
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
                                "processing_time": 0,
                                "response_time": 5,
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
                                "response_time": 5,
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
                                "response_time": 5,
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
                                "response_time": 5,
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
                                "response_time": 5,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 8,
                                "version": 2
                            },
                            "response": {
                                "processing_time": 0,
                                "response_time": 5,
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
                    "orig_id": "cr4EQp8BBi0xHyA-_xsX",
                    "orig_index": "aella-adr-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1860,
                    "outbytes_total": 823265,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783519041420,
                    "response_time": 5,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username": "jorgevaliente",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.114",
                    "srcip": "192.168.169.114",
                    "srcip_assetid": "daf84290-cbaf-11f0-b1b7-828ad4fe26cd",
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
                    "srcport": 52800,
                    "start_bucket_time": 1783518900000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1783519502631,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 451951,
                        "status": "New"
                    },
                    "stellar_da_input": 2000,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f60d0a6b-f04a-415f-845a-116de86dbbe01783519502653-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 5,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783519041049,
                    "timestamp_utc": "2026-07-08T13:57:21.000Z",
                    "tos": 0,
                    "totalbytes": 1170600,
                    "totalpackets": 17,
                    "typical": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783519502652,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.114, name: nb-jvaliente.technoma.local\" private) has sent an anomalously large number (#: 36) of SMB write requests, compared to its typical number (#: 4), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\10.11.1.5\\IPC$ very frequently.",
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