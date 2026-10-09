=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "801290ec-b47b-41b6-9969-975f8c3c60441784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4734,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "sEPNk58BI3UnQyDOkuDk",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "sEPNk58BI3UnQyDOkuDk",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438972",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280322,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129947,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2556,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "801290ec-b47b-41b6-9969-975f8c3c60441784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4376,
                    "threat_score": 0,
                    "timestamp": 1784891104740,
                    "timestamp_utc": "2026-07-24T11:05:04.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "a1602387-01e0-4298-94df-cfa566f70c961784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4737,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "bEPNk58BI3UnQyDOkuDB",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "bEPNk58BI3UnQyDOkuDB",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438977",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280329,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129951,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2558,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a1602387-01e0-4298-94df-cfa566f70c961784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10316,
                    "threat_score": 0,
                    "timestamp": 1784891104864,
                    "timestamp_utc": "2026-07-24T11:05:04.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "8943b415-754b-40ac-8167-f6fa9d5ddb841784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4745,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "uEPNk58BI3UnQyDOkuDm",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "uEPNk58BI3UnQyDOkuDm",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438981",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280355,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129960,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2557,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8943b415-754b-40ac-8167-f6fa9d5ddb841784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4376,
                    "threat_score": 0,
                    "timestamp": 1784891105008,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "52eee57a-74c4-4408-af97-84cfd16694071784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4739,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "mEPNk58BI3UnQyDOkuDj",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "mEPNk58BI3UnQyDOkuDj",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105900,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438985",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280335,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129955,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2554,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "52eee57a-74c4-4408-af97-84cfd16694071784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891105147,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "5eb6afe6-eb40-4863-a259-38ff2957827a1784891280328-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4733,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "y0PNk58BI3UnQyDOk-As",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "y0PNk58BI3UnQyDOk-As",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105900,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438989",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280316,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129942,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2554,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "5eb6afe6-eb40-4863-a259-38ff2957827a1784891280328-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891105266,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891280327,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "d25acf0d-c2c7-4e5a-b0d8-6c7a735e0c9d1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4738,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "bUPNk58BI3UnQyDOkuDB",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "bUPNk58BI3UnQyDOkuDB",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105900,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438993",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280332,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129954,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2553,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d25acf0d-c2c7-4e5a-b0d8-6c7a735e0c9d1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891105390,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "a6c6e20b-6297-40d6-a470-d59bef55f5071784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4746,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "uUPNk58BI3UnQyDOkuDm",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "uUPNk58BI3UnQyDOkuDm",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891105900,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891141218,
                    "record_number": "220438997",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280359,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129964,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2554,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a6c6e20b-6297-40d6-a470-d59bef55f5071784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891105463,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "3157e925-3e50-4d47-885d-f1403df45b9b1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4735,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "d0PNk58BI3UnQyDOkuDK",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "d0PNk58BI3UnQyDOkuDK",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142279,
                    "record_number": "220439001",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280324,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129948,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2555,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3157e925-3e50-4d47-885d-f1403df45b9b1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891105610,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "1a9103c7-9c4b-41d4-b943-0fedcafac54e1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4740,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "kUPNk58BI3UnQyDOkuDd",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "kUPNk58BI3UnQyDOkuDd",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142279,
                    "record_number": "220439005",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280339,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129956,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2558,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "1a9103c7-9c4b-41d4-b943-0fedcafac54e1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10316,
                    "threat_score": 0,
                    "timestamp": 1784891105792,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "bcbfb19d-6bf6-4739-98dc-47bc3c582f9e1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4742,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "skPNk58BI3UnQyDOkuDk",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "skPNk58BI3UnQyDOkuDk",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142279,
                    "record_number": "220439009",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280346,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129961,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2557,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bcbfb19d-6bf6-4739-98dc-47bc3c582f9e1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4376,
                    "threat_score": 0,
                    "timestamp": 1784891105913,
                    "timestamp_utc": "2026-07-24T11:05:05.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "d342d569-0e3a-4c5a-8bb9-30b1ad04bb901784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4751,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "xEPNk58BI3UnQyDOk-Ag",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "xEPNk58BI3UnQyDOk-Ag",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142279,
                    "record_number": "220439013",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280371,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129920,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2557,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d342d569-0e3a-4c5a-8bb9-30b1ad04bb901784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4376,
                    "threat_score": 0,
                    "timestamp": 1784891106033,
                    "timestamp_utc": "2026-07-24T11:05:06.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ebc94a7c-983f-4a50-95fd-67f73a1a5a271784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4736,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "eEPNk58BI3UnQyDOkuDK",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "eEPNk58BI3UnQyDOkuDK",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142279,
                    "record_number": "220439017",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280327,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129951,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2556,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ebc94a7c-983f-4a50-95fd-67f73a1a5a271784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891106248,
                    "timestamp_utc": "2026-07-24T11:05:06.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ca5a7a05-c3cd-4ea2-bc6d-3c31854a251a1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4741,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "kkPNk58BI3UnQyDOkuDd",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "kkPNk58BI3UnQyDOkuDd",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891106952,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891142280,
                    "record_number": "220439021",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280343,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129960,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2557,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ca5a7a05-c3cd-4ea2-bc6d-3c31854a251a1784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4376,
                    "threat_score": 0,
                    "timestamp": 1784891106446,
                    "timestamp_utc": "2026-07-24T11:05:06.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "bb969339-1273-4d49-af7f-f3e5ed8cfb611784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4749,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "k0PNk58BI3UnQyDOkuDd",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "k0PNk58BI3UnQyDOkuDd",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891108043,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891143371,
                    "record_number": "220439025",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280366,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129936,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2557,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bb969339-1273-4d49-af7f-f3e5ed8cfb611784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 6560,
                    "threat_score": 0,
                    "timestamp": 1784891106521,
                    "timestamp_utc": "2026-07-24T11:05:06.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ede027be-692e-4416-b9f8-dd275af876791784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4747,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "s0PNk58BI3UnQyDOkuDk",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_id",
                        "computer_name"
                    ],
                    "detected_values": [
                        "5145",
                        "VMBASE8"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784891160000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_data": {
                        "AccessList": "%%1538\n\t\t\t\t%%1541\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t",
                        "AccessMask": "0x12019f",
                        "AccessReason": "-",
                        "IpAddress": "172.16.202.41",
                        "IpPort": "49753",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x4135d8a5b8",
                        "SubjectUserName": "gocampos",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1719"
                    },
                    "event_id": 5145,
                    "event_score": 75,
                    "event_source": "rule_detection",
                    "event_status": "New",
                    "fidelity": 75,
                    "host": {
                        "ip": "172.16.201.8",
                        "name": "VMBASE8"
                    },
                    "hostip": "172.16.201.8",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "e964a518-d13a-11f0-a1a2-828ad4fe26cd",
                    "hostip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "hostip_geo_point": "-25.2869,-57.6511",
                    "hostip_host": "VMBASE8",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "keywords": [
                        "Auditoría correcta"
                    ],
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "msg_class": "Microsoft-Windows-Security-Auditing",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "winlogbeat"
                        },
                        "product": "auditbeat",
                        "source": "windows_agent",
                        "vendor": "elastic"
                    },
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "s0PNk58BI3UnQyDOkuDk",
                    "orig_index": "aella-wineventlog-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784891108043,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784891143371,
                    "record_number": "220439029",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.41",
                    "srcip": "172.16.202.41",
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
                    "srcip_host": "172.16.202.41",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "gocampos",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1719",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784891040000,
                    "stellar": {
                        "alert_time": 1784891280361,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129965,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2556,
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ede027be-692e-4416-b9f8-dd275af876791784891281337-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 272,
                    "threat_score": 0,
                    "timestamp": 1784891106717,
                    "timestamp_utc": "2026-07-24T11:05:06.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784891281337,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: gocampos, sid: S-1-5-21-4088095093-1662279969-3535480394-1719) from IP 172.16.202.41. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
                        "display_name": "Sensitive Windows Network Share File or Folder Accessed",
                        "framework_version": "v8",
                        "name": "windows_security_sensitive_networkshare",
                        "references": [
                            "https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html"
                        ],
                        "scope": "",
                        "subtype": {
                            "display_name": "Protected Storage Service Access",
                            "name": "security_win_security_protected_storage_service_access"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1021",
                            "name": "Remote Services",
                            "subtechnique": {
                                "id": "T1021.002",
                                "name": "SMB/Windows Admin Shares"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0008",
                                    "name": "Lateral Movement"
                                },
                                "technique": {
                                    "id": "T1021",
                                    "name": "Remote Services",
                                    "subtechnique": {
                                        "id": "T1021.002",
                                        "name": "SMB/Windows Admin Shares"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}