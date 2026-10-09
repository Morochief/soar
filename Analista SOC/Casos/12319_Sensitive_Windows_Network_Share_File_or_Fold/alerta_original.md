=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "e60bc513-64a8-4431-9d86-7f624f5978a11784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14179,
                "_primary_term": 3,
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
                    "anomaly_id": "QKPkb58BI3UnQyDOAaCB",
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
                    "end_bucket_time": 1784288760000,
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
                        "IpAddress": "172.16.202.54",
                        "IpPort": "56936",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x39bebb8ebc",
                        "SubjectUserName": "jdiaz",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1723"
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
                    "orig_id": "QKPkb58BI3UnQyDOAaCB",
                    "orig_index": "aella-wineventlog-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784288603813,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784288634822,
                    "record_number": "219316359",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.54",
                    "srcip": "172.16.202.54",
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
                    "srcip_host": "172.16.202.54",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "jdiaz",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1723",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784288640000,
                    "stellar": {
                        "alert_time": 1784288880492,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 239611,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2551,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e60bc513-64a8-4431-9d86-7f624f5978a11784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 3076,
                    "threat_score": 0,
                    "timestamp": 1784288602276,
                    "timestamp_utc": "2026-07-17T11:43:22.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784288881552,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: jdiaz, sid: S-1-5-21-4088095093-1662279969-3535480394-1723) from IP 172.16.202.54. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "c0661917-ef59-4089-9a97-377406f0b4cb1784288880535-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14178,
                "_primary_term": 3,
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
                    "anomaly_id": "Q6Pkb58BI3UnQyDOAaCL",
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
                    "end_bucket_time": 1784288760000,
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
                        "IpAddress": "172.16.202.54",
                        "IpPort": "56936",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x39bebb8ebc",
                        "SubjectUserName": "jdiaz",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1723"
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
                    "orig_id": "Q6Pkb58BI3UnQyDOAaCL",
                    "orig_index": "aella-wineventlog-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784288603814,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784288634822,
                    "record_number": "219316363",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.54",
                    "srcip": "172.16.202.54",
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
                    "srcip_host": "172.16.202.54",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "jdiaz",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1723",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784288640000,
                    "stellar": {
                        "alert_time": 1784288880489,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 239617,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2551,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c0661917-ef59-4089-9a97-377406f0b4cb1784288880535-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1764,
                    "threat_score": 0,
                    "timestamp": 1784288602948,
                    "timestamp_utc": "2026-07-17T11:43:22.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784288880535,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: jdiaz, sid: S-1-5-21-4088095093-1662279969-3535480394-1723) from IP 172.16.202.54. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "2c14aae3-7b26-4b62-a26b-dee3bf139d401784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14181,
                "_primary_term": 3,
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
                    "anomaly_id": "PKPkb58BI3UnQyDOAaBw",
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
                    "end_bucket_time": 1784288760000,
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
                        "IpAddress": "172.16.202.54",
                        "IpPort": "56936",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x39bebb8ebc",
                        "SubjectUserName": "jdiaz",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1723"
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
                    "orig_id": "PKPkb58BI3UnQyDOAaBw",
                    "orig_index": "aella-wineventlog-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784288603814,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784288634822,
                    "record_number": "219316367",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.54",
                    "srcip": "172.16.202.54",
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
                    "srcip_host": "172.16.202.54",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "jdiaz",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1723",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784288640000,
                    "stellar": {
                        "alert_time": 1784288880497,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 239612,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2551,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2c14aae3-7b26-4b62-a26b-dee3bf139d401784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1764,
                    "threat_score": 0,
                    "timestamp": 1784288603068,
                    "timestamp_utc": "2026-07-17T11:43:23.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784288881552,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: jdiaz, sid: S-1-5-21-4088095093-1662279969-3535480394-1723) from IP 172.16.202.54. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ec4cc680-ed6d-4482-8d53-5685b9d4d19c1784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14180,
                "_primary_term": 3,
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
                    "anomaly_id": "RqPkb58BI3UnQyDOAaCR",
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
                    "end_bucket_time": 1784288760000,
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
                        "IpAddress": "172.16.202.54",
                        "IpPort": "56936",
                        "ObjectType": "File",
                        "RelativeTargetName": "protected_storage",
                        "ShareName": "\\\\*\\IPC$",
                        "SubjectDomainName": "CAJAANDE",
                        "SubjectLogonId": "0x39bebb8ebc",
                        "SubjectUserName": "jdiaz",
                        "SubjectUserSid": "S-1-5-21-4088095093-1662279969-3535480394-1723"
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
                    "orig_id": "RqPkb58BI3UnQyDOAaCR",
                    "orig_index": "aella-wineventlog-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 4,
                    "process_time": 1784288603814,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784288634822,
                    "record_number": "219316371",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.202.54",
                    "srcip": "172.16.202.54",
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
                    "srcip_host": "172.16.202.54",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "jdiaz",
                    "srcip_usersid": "S-1-5-21-4088095093-1662279969-3535480394-1723",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1784288640000,
                    "stellar": {
                        "alert_time": 1784288880495,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 239613,
                        "rule_id": "windows_security_152",
                        "rule_revision": 2,
                        "status": "New",
                        "task": "windows_security_5145"
                    },
                    "stellar_da_input": 2550,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ec4cc680-ed6d-4482-8d53-5685b9d4d19c1784288881552-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Detailed File Share",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1764,
                    "threat_score": 0,
                    "timestamp": 1784288603240,
                    "timestamp_utc": "2026-07-17T11:43:23.000Z",
                    "type": "wineventlog",
                    "write_by": "sef",
                    "write_time": 1784288881552,
                    "xdr_event": {
                        "description": "A potentially sensitive network share object (\\\\*\\IPC$\\\\protected_storage) was accessed on the host (IP: 172.16.201.8, name: VMBASE8) by the user (name: jdiaz, sid: S-1-5-21-4088095093-1662279969-3535480394-1723) from IP 172.16.202.54. This detection was triggered by a rule with the following description: \"Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers.\"",
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