=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "fc5739db-b518-4167-9c4b-49d9a83d90641784896803034-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4863,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 2,
                    "aella_tuples": "192.168.169.82.10.11.1.5.445.185",
                    "anomaly_id": "e0cblJ8BI3UnQyDOE81Y",
                    "anomaly_tag": "spike",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO NTLM Session Setup Request - Auth",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.5",
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
                    "end_bucket_time": 1784896500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 28,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2067087,
                                "ids_severity": "low",
                                "name": "INFO NTLM Session Setup Request - Auth"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 35.84,
                    "file_extract_timestamp": 1784896229411,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 100,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2026-01-26T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "Medium"
                            ],
                            "created_at": [
                                "2026_01_26"
                            ],
                            "deployment": [
                                "Internal",
                                "Perimeter"
                            ],
                            "performance_impact": [
                                "Significant"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tls_state": [
                                "plaintext"
                            ],
                            "updated_at": [
                                "2026_01_26"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "smb",
                            "flow": {
                                "bytes_toclient": 841,
                                "bytes_toserver": 1431,
                                "dest_ip": "10.11.1.5",
                                "dest_port": 445,
                                "pkts_toclient": 3,
                                "pkts_toserver": 5,
                                "src_ip": "192.168.169.82",
                                "src_port": 51722,
                                "start": "2026-07-24T12:30:29.000390+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2026_01_26",
                            "rule": "\"alert tcp-pkt $HOME_NET any -> any 445 (msg:\\\"ET INFO NTLM Session Setup Request - Auth\\\"; flow:established,to_server; content:\\\"NTLMSSP|00 03 00 00 00|\\\"; fast_pattern; threshold:type limit,count 1,seconds 300,track by_src; classtype:misc-activity; sid:2067087; rev:1; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, tls_state plaintext, created_at 2026_01_26, deployment Perimeter, deployment Internal, performance_impact Significant, confidence Medium, signature_severity Informational, updated_at 2026_01_26; target:src_ip;)\\n\"",
                            "updated": "2026_01_26"
                        },
                        "severity": "low",
                        "signature": "INFO NTLM Session Setup Request - Auth",
                        "signature_id": 2067087,
                        "source": {
                            "ip": "10.11.1.5",
                            "port": 445
                        },
                        "target": {
                            "ip": "192.168.169.82",
                            "port": 51722
                        }
                    },
                    "inbytes_delta": 2414,
                    "inbytes_total": 841,
                    "inpkts_delta": 10,
                    "inpkts_total": 3,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "md5": "",
                    "metadata": [
                        {
                            "request": {
                                "command": 0,
                                "nt_status": 0,
                                "version": 2
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 31,
                                "response_time": 126,
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
                                "nt_status": -1073741802,
                                "processing_time": 3,
                                "response_time": 98,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 1,
                                "username": "melissasosa",
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 15,
                                "response_time": 110,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\10.11.1.5\\DocsAdministracion",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
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
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 0,
                                "response_time": 95
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        }
                    ],
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "e0cblJ8BI3UnQyDOE81Y",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2747,
                    "outbytes_total": 1431,
                    "outpkts_delta": 11,
                    "outpkts_total": 5,
                    "port_name": "ethernet1",
                    "processing_time": 5,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784896229771,
                    "response_time": 100,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "smb_username": "melissasosa",
                    "smb_username_count": 1,
                    "smb_username_set": [
                        "melissasosa"
                    ],
                    "src_tuples": "null.1101.192.168.169.82",
                    "srcip": "192.168.169.82",
                    "srcip_assetid": "3250ceaa-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.82",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.82.2067087.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51722,
                    "start_bucket_time": 1784896200000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784896803024,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 572839,
                        "status": "New"
                    },
                    "stellar_da_input": 1513,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fc5739db-b518-4167-9c4b-49d9a83d90641784896803034-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 95,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784896229580,
                    "timestamp_utc": "2026-07-24T12:30:29.000Z",
                    "tos": 0,
                    "totalbytes": 5161,
                    "totalpackets": 21,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784896803034,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 4.0) of exploit attempts with the IDS signature \"INFO NTLM Session Setup Request - Auth\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 2.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_priv",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
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
                "_id": "37b5f865-729d-4974-bada-2fdf2c1250a31784896804047-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4864,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 2,
                    "aella_tuples": "192.168.169.82.10.11.1.5.445.185",
                    "anomaly_id": "gUcblJ8BI3UnQyDOE81_",
                    "anomaly_tag": "spike",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO NTLM Session Setup Request - Negotiate",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.5",
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
                    "end_bucket_time": 1784896500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 28,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2067085,
                                "ids_severity": "low",
                                "name": "INFO NTLM Session Setup Request - Negotiate"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 35.84,
                    "file_extract_timestamp": 1784896229306,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 100,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2026-01-26T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "Medium"
                            ],
                            "created_at": [
                                "2026_01_26"
                            ],
                            "deployment": [
                                "Internal",
                                "Perimeter"
                            ],
                            "performance_impact": [
                                "Significant"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tls_state": [
                                "plaintext"
                            ],
                            "updated_at": [
                                "2026_01_26"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "smb",
                            "flow": {
                                "bytes_toclient": 440,
                                "bytes_toserver": 704,
                                "dest_ip": "10.11.1.5",
                                "dest_port": 445,
                                "pkts_toclient": 2,
                                "pkts_toserver": 4,
                                "src_ip": "192.168.169.82",
                                "src_port": 51722,
                                "start": "2026-07-24T12:30:29.000390+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2026_01_26",
                            "rule": "\"alert tcp-pkt $HOME_NET any -> any 445 (msg:\\\"ET INFO NTLM Session Setup Request - Negotiate\\\"; flow:established,to_server; content:\\\"NTLMSSP|00 01 00 00 00|\\\"; fast_pattern; threshold:type limit,count 1,seconds 300,track by_src; classtype:misc-activity; sid:2067085; rev:1; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, tls_state plaintext, created_at 2026_01_26, deployment Perimeter, deployment Internal, performance_impact Significant, confidence Medium, signature_severity Informational, updated_at 2026_01_26; target:src_ip;)\\n\"",
                            "updated": "2026_01_26"
                        },
                        "severity": "low",
                        "signature": "INFO NTLM Session Setup Request - Negotiate",
                        "signature_id": 2067085,
                        "source": {
                            "ip": "10.11.1.5",
                            "port": 445
                        },
                        "target": {
                            "ip": "192.168.169.82",
                            "port": 51722
                        }
                    },
                    "inbytes_delta": 2414,
                    "inbytes_total": 440,
                    "inpkts_delta": 10,
                    "inpkts_total": 2,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "md5": "",
                    "metadata": [
                        {
                            "request": {
                                "command": 0,
                                "nt_status": 0,
                                "version": 2
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 31,
                                "response_time": 126,
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
                                "nt_status": -1073741802,
                                "processing_time": 3,
                                "response_time": 98,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 1,
                                "username": "melissasosa",
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 15,
                                "response_time": 110,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\10.11.1.5\\DocsAdministracion",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
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
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 0,
                                "response_time": 95
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        }
                    ],
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "gUcblJ8BI3UnQyDOE81_",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2747,
                    "outbytes_total": 704,
                    "outpkts_delta": 11,
                    "outpkts_total": 4,
                    "port_name": "ethernet1",
                    "processing_time": 5,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784896229771,
                    "response_time": 100,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "smb_username": "melissasosa",
                    "smb_username_count": 1,
                    "smb_username_set": [
                        "melissasosa"
                    ],
                    "src_tuples": "null.1101.192.168.169.82",
                    "srcip": "192.168.169.82",
                    "srcip_assetid": "3250ceaa-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.82",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.82.2067085.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51722,
                    "start_bucket_time": 1784896200000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784896803168,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 572914,
                        "status": "New"
                    },
                    "stellar_da_input": 1516,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "37b5f865-729d-4974-bada-2fdf2c1250a31784896804047-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 95,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784896229580,
                    "timestamp_utc": "2026-07-24T12:30:29.000Z",
                    "tos": 0,
                    "totalbytes": 5161,
                    "totalpackets": 21,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784896804047,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 4.0) of exploit attempts with the IDS signature \"INFO NTLM Session Setup Request - Negotiate\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 2.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_priv",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
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
                "_id": "696e0beb-e7d8-41f2-923b-a1db96ada55d1784896804047-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4865,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 2,
                    "aella_tuples": "192.168.169.82.10.11.1.5.445.185",
                    "anomaly_id": "gEcblJ8BI3UnQyDOE81-",
                    "anomaly_tag": "spike",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO NTLMv1 Session Setup Response - Challenge",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.192.168.169.82",
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
                    "end_bucket_time": 1784896500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 28,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2067086,
                                "ids_severity": "low",
                                "name": "INFO NTLMv1 Session Setup Response - Challenge"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 35.84,
                    "file_extract_timestamp": 1784896229310,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 100,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2026-01-26T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "Medium"
                            ],
                            "created_at": [
                                "2026_01_26"
                            ],
                            "deployment": [
                                "Internal",
                                "Perimeter"
                            ],
                            "performance_impact": [
                                "Significant"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tls_state": [
                                "plaintext"
                            ],
                            "updated_at": [
                                "2026_01_26"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "smb",
                            "flow": {
                                "bytes_toclient": 841,
                                "bytes_toserver": 704,
                                "dest_ip": "10.11.1.5",
                                "dest_port": 445,
                                "pkts_toclient": 3,
                                "pkts_toserver": 4,
                                "src_ip": "192.168.169.82",
                                "src_port": 51722,
                                "start": "2026-07-24T12:30:29.000390+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2026_01_26",
                            "rule": "\"alert tcp-pkt any 445 -> $HOME_NET any (msg:\\\"ET INFO NTLMv1 Session Setup Response - Challenge\\\"; flow:established,to_client; content:\\\"|2b 06 01 04 01 82 37 02 02 0a|\\\"; content:\\\"NTLMSSP|00 02 00 00 00|\\\"; fast_pattern; threshold:type limit,count 1,seconds 300,track by_dst; classtype:misc-activity; sid:2067086; rev:1; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, tls_state plaintext, created_at 2026_01_26, deployment Perimeter, deployment Internal, performance_impact Significant, confidence Medium, signature_severity Informational, updated_at 2026_01_26; target:dest_ip;)\\n\"",
                            "updated": "2026_01_26"
                        },
                        "severity": "low",
                        "signature": "INFO NTLMv1 Session Setup Response - Challenge",
                        "signature_id": 2067086,
                        "source": {
                            "ip": "10.11.1.5",
                            "port": 445
                        },
                        "target": {
                            "ip": "192.168.169.82",
                            "port": 51722
                        }
                    },
                    "inbytes_delta": 2414,
                    "inbytes_total": 841,
                    "inpkts_delta": 10,
                    "inpkts_total": 3,
                    "lateral": true,
                    "locid": "unassigned location",
                    "login_type": "smb_traffic",
                    "md5": "",
                    "metadata": [
                        {
                            "request": {
                                "command": 0,
                                "nt_status": 0,
                                "version": 2
                            },
                            "response": {
                                "command": 0,
                                "nt_status": 0,
                                "processing_time": 31,
                                "response_time": 126,
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
                                "nt_status": -1073741802,
                                "processing_time": 3,
                                "response_time": 98,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 1,
                                "username": "melissasosa",
                                "version": 2
                            },
                            "response": {
                                "command": 1,
                                "nt_status": 0,
                                "processing_time": 15,
                                "response_time": 110,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 3,
                                "path": "\\\\10.11.1.5\\DocsAdministracion",
                                "version": 2
                            },
                            "response": {
                                "command": 3,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
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
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "command": 11,
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "response": {
                                "command": 5,
                                "processing_time": 0,
                                "response_time": 95
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
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
                                "response_time": 95,
                                "version": 2
                            }
                        },
                        {
                            "request": {
                                "command": 5,
                                "filename": "",
                                "version": 2
                            },
                            "response": {
                                "processing_time": 0,
                                "response_time": 95,
                                "version": 2
                            }
                        }
                    ],
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "gEcblJ8BI3UnQyDOE81-",
                    "orig_index": "aella-maltrace-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2747,
                    "outbytes_total": 704,
                    "outpkts_delta": 11,
                    "outpkts_total": 4,
                    "port_name": "ethernet1",
                    "processing_time": 5,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784896229771,
                    "response_time": 100,
                    "score": 30,
                    "severity": 25,
                    "sha256": "",
                    "smb_username": "melissasosa",
                    "smb_username_count": 1,
                    "smb_username_set": [
                        "melissasosa"
                    ],
                    "src_tuples": "null.1101.10.11.1.5",
                    "srcip": "192.168.169.82",
                    "srcip_assetid": "3250ceaa-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.82",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "10.11.1.5.2067086.0",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51722,
                    "start_bucket_time": 1784896200000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784896803294,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 573048,
                        "status": "New"
                    },
                    "stellar_da_input": 1519,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "696e0beb-e7d8-41f2-923b-a1db96ada55d1784896804047-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 95,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784896229580,
                    "timestamp_utc": "2026-07-24T12:30:29.000Z",
                    "tos": 0,
                    "totalbytes": 5161,
                    "totalpackets": 21,
                    "typical": 0.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784896804047,
                    "xdr_event": {
                        "description": "In internal traffic, an anomalously high number (#: 4.0) of exploit attempts with the IDS signature \"INFO NTLMv1 Session Setup Response - Challenge\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 2.0) from the typical value of (#: 0.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Exploit Attempt (Low Severity)",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_priv",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
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
                "_id": "e3b5c845-708b-4042-b1ca-9faaeacc83421784897102791-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4870,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 103,
                    "aella_tuples": "192.168.169.28.10.11.1.5.445.185",
                    "anomaly_id": "8EgjlJ8BI3UnQyDOBlv2",
                    "appid": 185,
                    "appid_family": "File",
                    "appid_name": "smb",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "192.168.169.28"
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
                    "duration": 15913,
                    "end_bucket_time": 1784896800000,
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
                    "fidelity": 97.91,
                    "flow_score": 100,
                    "inbytes_delta": 20752,
                    "inbytes_total": 221886,
                    "inpkts_delta": 22,
                    "lateral": true,
                    "locid": "unassigned location",
                    "metadata": [
                        {
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
                                "filename": "CONCILIACIÓN BANCARIA",
                                "version": 2
                            },
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
                                "command": 14,
                                "version": 2
                            },
                            "response": {
                                "command": 14,
                                "filename": "",
                                "nt_status": 0,
                                "processing_time": 0,
                                "response_time": 2,
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
                                "response_time": 2,
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
                                "processing_time": 0,
                                "response_time": 2,
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
                    "orig_id": "8EgjlJ8BI3UnQyDOBlv2",
                    "orig_index": "aella-adr-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 2183,
                    "outbytes_total": 22751,
                    "outpkts_delta": 12,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784896744922,
                    "response_time": 2,
                    "run_every": 5,
                    "severity": 20,
                    "smb_username": "jorgevaliente",
                    "smb_username_count": 0,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.28",
                    "srcip": "192.168.169.28",
                    "srcip_assetid": "660c1fe8-cab4-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-rlledo.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 55391,
                    "start_bucket_time": 1784896500000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1784897102749,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 352420,
                        "status": "New"
                    },
                    "stellar_da_input": 1984,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e3b5c845-708b-4042-b1ca-9faaeacc83421784897102791-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 2,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784896744505,
                    "timestamp_utc": "2026-07-24T12:39:04.000Z",
                    "tos": 0,
                    "totalbytes": 244637,
                    "totalpackets": 34,
                    "typical": 16,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784897102790,
                    "xdr_event": {
                        "description": "In internal traffic, a host (\"IP: 192.168.169.28, name: nb-rlledo.technoma.local\" private) has sent an anomalously large number (#: 103) of SMB read requests, compared to its typical number (#: 16), measured in a 5.0-minute interval. In this time interval, the source host accesses \\\\10.11.1.5\\IPC$ very frequently.",
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