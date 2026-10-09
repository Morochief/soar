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
                "_id": "8a54ea3f-20f3-4a26-b853-d635df8c91a71790246403303-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18929,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403283,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411184,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8a54ea3f-20f3-4a26-b853-d635df8c91a71790246403303-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246403303,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "7e16bd1f-3572-487d-951d-9f666a0533701790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18930,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403289,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411190,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7e16bd1f-3572-487d-951d-9f666a0533701790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "142de74f-9495-4122-988b-d183aef514351790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18931,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403297,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411198,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "142de74f-9495-4122-988b-d183aef514351790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "0999d771-db0e-4bff-a32b-f83e63d157fe1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18932,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403303,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411204,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "0999d771-db0e-4bff-a32b-f83e63d157fe1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "91a9e292-f55c-4580-b8e8-931f757cc1e21790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18933,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403310,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411211,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "91a9e292-f55c-4580-b8e8-931f757cc1e21790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "f91b10b4-1d88-41f3-bf21-3c6ef0c9229c1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18934,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403316,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411217,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f91b10b4-1d88-41f3-bf21-3c6ef0c9229c1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "aa1f643a-bb8a-4a89-acd0-78a3110012291790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18935,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403322,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411223,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "aa1f643a-bb8a-4a89-acd0-78a3110012291790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "c5271041-c242-40ff-9cda-61604fff13aa1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18936,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403329,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411230,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c5271041-c242-40ff-9cda-61604fff13aa1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "f46c9b5a-0bef-4acb-8b41-61d70364b0471790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18937,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403335,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411236,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f46c9b5a-0bef-4acb-8b41-61d70364b0471790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "b6bed196-71c2-4960-aa9f-d42d6f4d42211790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18939,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403348,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411249,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b6bed196-71c2-4960-aa9f-d42d6f4d42211790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "6ec0c119-832e-48e5-afda-0a2ef6e87cd21790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18940,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403357,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411258,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6ec0c119-832e-48e5-afda-0a2ef6e87cd21790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "e5cb3af3-847c-445c-86aa-885bfff697061790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18941,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403364,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411265,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e5cb3af3-847c-445c-86aa-885bfff697061790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "b66183f5-0fa6-4a05-951c-f189e22955df1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18943,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403377,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411278,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b66183f5-0fa6-4a05-951c-f189e22955df1790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
                "_id": "96638b5f-2ff3-4d35-97a5-232146ca1e291790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 18944,
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
                    "anomaly_id": "Etj50qABI3UnQyDO-qAQ",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "event_data.TargetUserName"
                    ],
                    "detected_values": [
                        "2296189"
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
                        "TargetUserName": "2296189",
                        "Workstation": "CJPPA20150819"
                    },
                    "event_id": 4776,
                    "event_name": "user_login_time",
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 14.56,
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
                    "orig_id": "Etj50qABI3UnQyDO-qAQ",
                    "orig_index": "aella-wineventlog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "process_id": 692,
                    "process_time": 1790245962544,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1790245980495,
                    "record_number": "230896252",
                    "service_id": "CJPPA20150819",
                    "severity": 40,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "srcip_username": "2296189",
                    "start_bucket_time": 1790245800000,
                    "stellar": {
                        "alert_time": 1790246403384,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 411285,
                        "status": "New"
                    },
                    "stellar_da_input": 1404,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "96638b5f-2ff3-4d35-97a5-232146ca1e291790246404315-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Credential Validation",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9700,
                    "threat_score": 0,
                    "timestamp": 1790242994972,
                    "timestamp_utc": "2026-09-24T09:43:14.000Z",
                    "type": "wineventlog",
                    "typical": 0.91,
                    "typical_range": "06:00-16:00 UTC-4:00",
                    "username": "2296189",
                    "write_by": "sef",
                    "write_time": 1790246404315,
                    "xdr_event": {
                        "description": "The account 2296189 has logged in at an abnormal time range 01:00-02:00 UTC-4:00, compared to the typical login time range: 06:00-16:00 UTC-4:00 observed for this account.",
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
The current local time is: 2026-09-24T09:07:39-03:00.

The user's current state is as follows:
Active Document: c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Cloud_Drive_Data_Exfiltration_Anomaly_josemarin\analisis_soc.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\145120_Palo_Alto_Networks_Cortex_XDR_route_exe_NB-RBARRETO\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\command_center.py (LANGUAGE_PYTHON)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Cloud_Drive_Data_Exfiltration_Anomaly_josemarin\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\02_Base_de_Conocimiento\plantillas_cierre_soc.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>