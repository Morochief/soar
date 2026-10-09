<USER_REQUEST>
=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "d7d585c3-bee2-4ed1-92a5-5794632a7e4b1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18938,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "01:00-02:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 49,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 72.32,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403342,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411252,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d7d585c3-bee2-4ed1-92a5-5794632a7e4b1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "600af0a7-bae4-4b42-b793-ee143e6cb0c41790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18942,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "01:00-02:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 49,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 72.32,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403370,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411280,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "600af0a7-bae4-4b42-b793-ee143e6cb0c41790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "4ad37acd-e182-4c14-b1e3-bcdbc9a47cfa1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18945,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "01:00-02:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 49,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 72.32,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403390,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411300,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4ad37acd-e182-4c14-b1e3-bcdbc9a47cfa1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "fc700075-dbcd-4fc0-9fe9-a741e387ab121790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18946,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "02:00-03:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 15.58,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403397,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411307,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fc700075-dbcd-4fc0-9fe9-a741e387ab121790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 02:00-03:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "c2c2632f-25d5-4805-b568-88aa5ee9393d1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18947,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "02:00-03:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 15.58,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403409,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411319,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c2c2632f-25d5-4805-b568-88aa5ee9393d1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 02:00-03:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "e357e22c-d08b-4faf-b563-ca823148cb081790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18948,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "02:00-03:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 15.58,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403418,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411328,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e357e22c-d08b-4faf-b563-ca823148cb081790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 02:00-03:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "63e9f138-a283-45e6-b4fa-1fdfa4f047621790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18949,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "02:00-03:00 UTC-4:00",
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "653903a7-dc86-4e8a-9242-93397ddad03d",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8tj50qABI3UnQyDO-p8Q",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "bdominguez"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1790246100000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "success"
                    },
                    "event_category": "uba",
                    "event_data": {
                        "PackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                        "Status": "0x0",
                        "TargetUserName": "bdominguez",
                        "Workstation": "CJPPA056"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 15.58,
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
                    "lateral": false,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "success",
                    "login_type": "windows_login",
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
                    "orig_id": "8tj50qABI3UnQyDO-p8Q",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245961684,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980117,
                    "record_number": "230895873",
                    "service_id": "CJPPA056",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "bdominguez",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403429,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411339,
                        "status": "New"
                    },
                    "stellar_da_input": 1400,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "63e9f138-a283-45e6-b4fa-1fdfa4f047621790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242709555,
                    "timestamp_utc": "2026-09-24T09:38:29.000Z",
                    "type": "wineventlog",
                    "typical": 0.92,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "bdominguez",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account bdominguez has logged in at an abnormal time range 02:00-03:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-09-24T07:50:43-03:00.

The user's current state is as follows:
Active Document: c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Cloud_Drive_Data_Exfiltration_Anomaly_josemarin\analisis_soc.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Cloud_Drive_Data_Exfiltration_Anomaly_josemarin\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\02_Base_de_Conocimiento\plantillas_cierre_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\145120_Palo_Alto_Networks_Cortex_XDR_route_exe_NB-RBARRETO\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\command_center.py (LANGUAGE_PYTHON)
</ADDITIONAL_METADATA>