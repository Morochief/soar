=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "dc7edd9b-86ce-4ff2-9db1-fefbc53c3b9b1784898302456-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4894,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 101,
                    "aella_tuples": "192.168.169.96.10.11.1.1.445.185",
                    "anomaly_id": "-kkzlJ8BI3UnQyDONInO",
                    "app_path": "smb.dcerpc",
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
                    "duration": 114777,
                    "end_bucket_time": 1784898000000,
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
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 97.75,
                    "flow_score": 100,
                    "inbytes_delta": 1372,
                    "inbytes_total": 209321,
                    "inpkts_delta": 8,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
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
                                "response_time": 4,
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
                                "processing_time": 1,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                    "orig_id": "-kkzlJ8BI3UnQyDONInO",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1933,
                    "outbytes_total": 221261,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784897806362,
                    "response_time": 4,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.96",
                    "srcip": "192.168.169.96",
                    "srcip_assetid": "32d584c4-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-caranda.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 55234,
                    "start_bucket_time": 1784897700000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784898302433,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 491945,
                        "status": "New"
                    },
                    "stellar_da_input": 1968,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "dc7edd9b-86ce-4ff2-9db1-fefbc53c3b9b1784898302456-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784897805175,
                    "timestamp_utc": "2026-07-24T12:56:45.000Z",
                    "tos": 0,
                    "totalbytes": 430582,
                    "totalpackets": 17,
                    "typical": 16,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784898302456,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.96, name: nb-caranda.technoma.local\" private) has sent an anomalously large number (#: 101) of SMB read requests, compared to its typical number (#: 16), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_id": "6542f3d0-cdf1-4592-b549-f5fc8b0616ae1784898302784-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4895,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 100,
                    "aella_tuples": "192.168.169.96.10.11.1.1.445.185",
                    "anomaly_id": "-kkzlJ8BI3UnQyDONInO",
                    "app_path": "smb.dcerpc",
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
                    "duration": 114777,
                    "end_bucket_time": 1784898000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_anomaly",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [
                            "\\\\ad.technoma.local\\IPC$"
                        ],
                        "smb_path_summary": [
                            {
                                "key": "\\\\ad.technoma.local\\IPC$",
                                "value": 1
                            }
                        ]
                    },
                    "event_type": "conn",
                    "fidelity": 98.94,
                    "flow_score": 100,
                    "inbytes_delta": 1372,
                    "inbytes_total": 209321,
                    "inpkts_delta": 8,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
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
                                "response_time": 4,
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
                                "processing_time": 1,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                                "response_time": 4,
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
                    "orig_id": "-kkzlJ8BI3UnQyDONInO",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1933,
                    "outbytes_total": 221261,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784897806362,
                    "response_time": 4,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.96",
                    "srcip": "192.168.169.96",
                    "srcip_assetid": "32d584c4-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-caranda.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 55234,
                    "start_bucket_time": 1784897700000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784898302772,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 492284,
                        "status": "New"
                    },
                    "stellar_da_input": 1968,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6542f3d0-cdf1-4592-b549-f5fc8b0616ae1784898302784-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 4,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784897805175,
                    "timestamp_utc": "2026-07-24T12:56:45.000Z",
                    "tos": 0,
                    "totalbytes": 430582,
                    "totalpackets": 17,
                    "typical": 5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784898302784,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.96, name: nb-caranda.technoma.local\" private) has sent an anomalously large number (#: 100) of SMB write requests, compared to its typical number (#: 5), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\ad.technoma.local\\IPC$ very frequently.",
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
                "_id": "fa64cfbf-d219-4dfa-8cc1-d36217e2711a1784899202866-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4913,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 54,
                    "aella_tuples": "192.168.169.144.10.11.1.1.445.185",
                    "anomaly_id": "sEpBlJ8BI3UnQyDOi682",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.144"
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
                    "duration": 32388,
                    "end_bucket_time": 1784898900000,
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
                    "fidelity": 98.09,
                    "flow_score": 100,
                    "inbytes_delta": 1562,
                    "inbytes_total": 89000,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 1,
                                "response_time": 3,
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
                    "orig_id": "sEpBlJ8BI3UnQyDOi682",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1946,
                    "outbytes_total": 106325,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784898742042,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 40,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.144",
                    "srcip": "192.168.169.144",
                    "srcip_assetid": "b7f65a54-0104-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.144",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54406,
                    "start_bucket_time": 1784898600000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784899202837,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 452601,
                        "status": "New"
                    },
                    "stellar_da_input": 1914,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fa64cfbf-d219-4dfa-8cc1-d36217e2711a1784899202866-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784898741316,
                    "timestamp_utc": "2026-07-24T13:12:21.000Z",
                    "tos": 0,
                    "totalbytes": 195325,
                    "totalpackets": 18,
                    "typical": 3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784899202866,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.144\" private) has sent an anomalously large number (#: 54) of SMB write requests, compared to its typical number (#: 3), measured in a 5.0-minute interval.",
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
                "_id": "69d0a891-a0ca-46d8-9967-e569548a37d41784899202917-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4914,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 54,
                    "aella_tuples": "192.168.169.144.10.11.1.1.445.185",
                    "anomaly_id": "sEpBlJ8BI3UnQyDOi682",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.144"
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
                    "duration": 32388,
                    "end_bucket_time": 1784898900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "smb_read_anomaly",
                    "event_score": 30,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "smb_path_list": [],
                        "smb_path_summary": []
                    },
                    "event_type": "conn",
                    "fidelity": 66.96,
                    "flow_score": 100,
                    "inbytes_delta": 1562,
                    "inbytes_total": 89000,
                    "inpkts_delta": 9,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "response": {
                                "command": 5,
                                "nt_status": 0,
                                "processing_time": 1,
                                "response_time": 3,
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
                    "orig_id": "sEpBlJ8BI3UnQyDOi682",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1946,
                    "outbytes_total": 106325,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784898742042,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.144",
                    "srcip": "192.168.169.144",
                    "srcip_assetid": "b7f65a54-0104-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.144",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54406,
                    "start_bucket_time": 1784898600000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784899202898,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 452662,
                        "status": "New"
                    },
                    "stellar_da_input": 1914,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "69d0a891-a0ca-46d8-9967-e569548a37d41784899202917-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784898741316,
                    "timestamp_utc": "2026-07-24T13:12:21.000Z",
                    "tos": 0,
                    "totalbytes": 195325,
                    "totalpackets": 18,
                    "typical": 12,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784899202917,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP/name: 192.168.169.144\" private) has sent an anomalously large number (#: 54) of SMB read requests, compared to its typical number (#: 12), measured in a 5.0-minute interval.",
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