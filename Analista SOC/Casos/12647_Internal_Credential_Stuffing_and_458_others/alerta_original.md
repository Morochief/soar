=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "85518d67-e1e0-4150-9878-27ba49441d421785021606385-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6086,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 520,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8JOHm58BI3UnQyDOalh0",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "srcip_username"
                    ],
                    "detected_values": [
                        "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1785021000000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "failure"
                    },
                    "event_category": "killchain",
                    "event_data": {
                        "AccountAvailableKeys": "-",
                        "AccountSupportedEncryptionTypes": "-",
                        "ClientAdvertizedEncryptionTypes": "-",
                        "DCAvailableKeys": "-",
                        "DCSupportedEncryptionTypes": "-",
                        "IpAddress": "::ffff:172.16.201.4",
                        "IpPort": "37309",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x6",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                        "TicketEncryptionType": "0xffffffff",
                        "TicketOptions": "0x40810010"
                    },
                    "event_id": 4768,
                    "event_name": "cloud_account_login_failure",
                    "event_score": 18,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            30,
                            28,
                            30,
                            30,
                            28
                        ],
                        "successful_details": [
                            0,
                            0,
                            0,
                            0,
                            0
                        ],
                        "time_bucket": 25,
                        "total_fail_ratio": 1,
                        "total_failed": 146,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 1.56,
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
                        "Error de auditoría"
                    ],
                    "lateral": true,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "fail",
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
                    "num_failed": 4,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "8JOHm58BI3UnQyDOalh0",
                    "orig_index": "aella-wineventlog-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785020727012,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785020763267,
                    "record_number": "220657102",
                    "service_id": "CAJAANDE.LOCAL",
                    "severity": 60,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.201.4",
                    "srcip": "172.16.201.4",
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
                    "srcip_host": "172.16.201.4",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785019500000,
                    "stellar": {
                        "alert_time": 1785021606366,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 836005,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "85518d67-e1e0-4150-9878-27ba49441d421785021606385-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1785020725076,
                    "timestamp_utc": "2026-07-25T23:05:25.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 520,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785021606385,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 520.",
                        "display_name": "Internal Account Login Failure Anomaly",
                        "framework_version": "v8",
                        "name": "internal_cloud_account_login_failure",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "Kerberos Events",
                            "name": "internal_cloud_account_login_failure_kerberos"
                        },
                        "tactic": {
                            "id": "TA0006",
                            "name": "Credential Access"
                        },
                        "tags": [
                            "Internal",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1110",
                            "name": "Brute Force"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "abcb69ba-cda9-4f8f-919e-1838f32b4c3f1785021605174-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6085,
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
                    "anomaly_id": "VpOLm58BI3UnQyDOFXNM",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "msg_class",
                        "service_id"
                    ],
                    "detected_values": [
                        "Microsoft-Windows-Security-Auditing",
                        "CAJAANDE.LOCAL"
                    ],
                    "detector_index": 2,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1785021300000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "failure"
                    },
                    "event_category": "killchain",
                    "event_data": {
                        "AccountAvailableKeys": "-",
                        "AccountSupportedEncryptionTypes": "-",
                        "ClientAdvertizedEncryptionTypes": "-",
                        "DCAvailableKeys": "-",
                        "DCSupportedEncryptionTypes": "-",
                        "IpAddress": "::ffff:172.16.201.4",
                        "IpPort": "37646",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x6",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                        "TicketEncryptionType": "0xffffffff",
                        "TicketOptions": "0x40810010"
                    },
                    "event_id": 4768,
                    "event_name": "credential_stuffing",
                    "event_score": 81,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 95.66,
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
                        "Error de auditoría"
                    ],
                    "lateral": true,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_failure_rate": "32.81",
                    "login_failure_rate_raw": 32.80516537472348,
                    "login_result": "fail",
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
                    "orig_id": "VpOLm58BI3UnQyDOFXNM",
                    "orig_index": "aella-wineventlog-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1785020966843,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785021003092,
                    "record_number": "220657509",
                    "service_id": "CAJAANDE.LOCAL",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.201.4",
                    "srcip": "172.16.201.4",
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
                    "srcip_host": "172.16.201.4",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785021000000,
                    "stellar": {
                        "alert_time": 1785021605082,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 594628,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "abcb69ba-cda9-4f8f-919e-1838f32b4c3f1785021605174-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9536,
                    "threat_score": 0,
                    "timestamp": 1785020966010,
                    "timestamp_utc": "2026-07-25T23:09:26.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "31.94",
                    "unknown_users_rate_raw": 31.94187154907286,
                    "unknown_users_to_login_failures": "0.97",
                    "unknown_users_to_login_failures_raw": 0.9736842105263158,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785021605174,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 32.81 and of usernames not recognized by the system is 31.94.",
                        "display_name": "Internal Credential Stuffing",
                        "framework_version": "v8",
                        "name": "internal_credential_stuffing",
                        "scope": "Internal",
                        "tactic": {
                            "id": "TA0006",
                            "name": "Credential Access"
                        },
                        "tags": [
                            "Internal",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1110",
                            "name": "Brute Force"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "999bb471-9f77-47dd-a166-fcb7558680351785021607395-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6087,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 533,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "ZpOMm58BI3UnQyDO6YCm",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "srcip_username"
                    ],
                    "detected_values": [
                        "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1785021300000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "failure"
                    },
                    "event_category": "killchain",
                    "event_data": {
                        "AccountAvailableKeys": "-",
                        "AccountSupportedEncryptionTypes": "-",
                        "ClientAdvertizedEncryptionTypes": "-",
                        "DCAvailableKeys": "-",
                        "DCSupportedEncryptionTypes": "-",
                        "IpAddress": "::ffff:172.16.201.4",
                        "IpPort": "37804",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x6",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                        "TicketEncryptionType": "0xffffffff",
                        "TicketOptions": "0x40810010"
                    },
                    "event_id": 4768,
                    "event_name": "cloud_account_login_failure",
                    "event_score": 19,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            30,
                            30,
                            28,
                            30,
                            30
                        ],
                        "successful_details": [
                            0,
                            0,
                            0,
                            0,
                            0
                        ],
                        "time_bucket": 25,
                        "total_fail_ratio": 1,
                        "total_failed": 148,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 1.85,
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
                        "Error de auditoría"
                    ],
                    "lateral": true,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "fail",
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
                    "num_failed": 24,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "ZpOMm58BI3UnQyDO6YCm",
                    "orig_index": "aella-wineventlog-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785021084200,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785021120450,
                    "record_number": "220657668",
                    "service_id": "CAJAANDE.LOCAL",
                    "severity": 60,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.201.4",
                    "srcip": "172.16.201.4",
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
                    "srcip_host": "172.16.201.4",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785019800000,
                    "stellar": {
                        "alert_time": 1785021606514,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 476240,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "999bb471-9f77-47dd-a166-fcb7558680351785021607395-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 3512,
                    "threat_score": 0,
                    "timestamp": 1785021082684,
                    "timestamp_utc": "2026-07-25T23:11:22.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 533,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785021607395,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 533.",
                        "display_name": "Internal Account Login Failure Anomaly",
                        "framework_version": "v8",
                        "name": "internal_cloud_account_login_failure",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "Kerberos Events",
                            "name": "internal_cloud_account_login_failure_kerberos"
                        },
                        "tactic": {
                            "id": "TA0006",
                            "name": "Credential Access"
                        },
                        "tags": [
                            "Internal",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1110",
                            "name": "Brute Force"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "173dd737-9560-47e4-87e8-53abf8d290641785021905788-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6089,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 539,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "ZpOMm58BI3UnQyDO6YCm",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "srcip_username"
                    ],
                    "detected_values": [
                        "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1785021300000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "failure"
                    },
                    "event_category": "killchain",
                    "event_data": {
                        "AccountAvailableKeys": "-",
                        "AccountSupportedEncryptionTypes": "-",
                        "ClientAdvertizedEncryptionTypes": "-",
                        "DCAvailableKeys": "-",
                        "DCSupportedEncryptionTypes": "-",
                        "IpAddress": "::ffff:172.16.201.4",
                        "IpPort": "37804",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x6",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                        "TicketEncryptionType": "0xffffffff",
                        "TicketOptions": "0x40810010"
                    },
                    "event_id": 4768,
                    "event_name": "cloud_account_login_failure",
                    "event_score": 19,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            30,
                            30,
                            28,
                            30,
                            30
                        ],
                        "successful_details": [
                            0,
                            0,
                            0,
                            0,
                            0
                        ],
                        "time_bucket": 25,
                        "total_fail_ratio": 1,
                        "total_failed": 148,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 1.98,
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
                        "Error de auditoría"
                    ],
                    "lateral": true,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_result": "fail",
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
                    "num_failed": 6,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "ZpOMm58BI3UnQyDO6YCm",
                    "orig_index": "aella-wineventlog-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785021084200,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785021120450,
                    "record_number": "220657668",
                    "service_id": "CAJAANDE.LOCAL",
                    "severity": 60,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.201.4",
                    "srcip": "172.16.201.4",
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
                    "srcip_host": "172.16.201.4",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785019800000,
                    "stellar": {
                        "alert_time": 1785021905755,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 775481,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "173dd737-9560-47e4-87e8-53abf8d290641785021905788-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 3512,
                    "threat_score": 0,
                    "timestamp": 1785021082684,
                    "timestamp_utc": "2026-07-25T23:11:22.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 539,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785021905788,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 539.",
                        "display_name": "Internal Account Login Failure Anomaly",
                        "framework_version": "v8",
                        "name": "internal_cloud_account_login_failure",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "Kerberos Events",
                            "name": "internal_cloud_account_login_failure_kerberos"
                        },
                        "tactic": {
                            "id": "TA0006",
                            "name": "Credential Access"
                        },
                        "tags": [
                            "Internal",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1110",
                            "name": "Brute Force"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "850a0a63-29f9-4f27-9b6e-c05b72218c651785021904941-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6088,
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
                    "anomaly_id": "d5OPm58BI3UnQyDOqJJH",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "msg_class",
                        "service_id"
                    ],
                    "detected_values": [
                        "Microsoft-Windows-Security-Auditing",
                        "CAJAANDE.LOCAL"
                    ],
                    "detector_index": 2,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1785021600000,
                    "engid": "4c735067a7f5483ca72265eb5324214c",
                    "engid_device_class": "Windows",
                    "engid_device_desc": "windows-x64(Windows Server 2019 Standard-10.0.17763)",
                    "engid_gateway": "190.52.189.87",
                    "engid_name": "VMBASE8",
                    "event": {
                        "outcome": "failure"
                    },
                    "event_category": "killchain",
                    "event_data": {
                        "AccountAvailableKeys": "-",
                        "AccountSupportedEncryptionTypes": "-",
                        "ClientAdvertizedEncryptionTypes": "-",
                        "DCAvailableKeys": "-",
                        "DCSupportedEncryptionTypes": "-",
                        "IpAddress": "::ffff:172.16.201.4",
                        "IpPort": "38064",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x6",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                        "TicketEncryptionType": "0xffffffff",
                        "TicketOptions": "0x40810010"
                    },
                    "event_id": 4768,
                    "event_name": "credential_stuffing",
                    "event_score": 81,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 95.1,
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
                        "Error de auditoría"
                    ],
                    "lateral": true,
                    "level": "Información",
                    "locid": "unassigned location",
                    "log_name": "Security",
                    "login_failure_rate": "33.71",
                    "login_failure_rate_raw": 33.712600084281505,
                    "login_result": "fail",
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
                    "orig_id": "d5OPm58BI3UnQyDOqJJH",
                    "orig_index": "aella-wineventlog-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1785021268539,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785021304795,
                    "record_number": "220658024",
                    "service_id": "CAJAANDE.LOCAL",
                    "severity": 75,
                    "source_name": "Microsoft-Windows-Security-Auditing",
                    "src_tuples": "null.0.172.16.201.4",
                    "srcip": "172.16.201.4",
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
                    "srcip_host": "172.16.201.4",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785021300000,
                    "stellar": {
                        "alert_time": 1785021904932,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 594498,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.25-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "850a0a63-29f9-4f27-9b6e-c05b72218c651785021904941-YWVsbGEtc2VyLTIwMjYuMDcuMjUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1785021266743,
                    "timestamp_utc": "2026-07-25T23:14:26.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "33.28",
                    "unknown_users_rate_raw": 33.28038726268815,
                    "unknown_users_to_login_failures": "0.99",
                    "unknown_users_to_login_failures_raw": 0.9871794871794872,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785021904941,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 33.71 and of usernames not recognized by the system is 33.28.",
                        "display_name": "Internal Credential Stuffing",
                        "framework_version": "v8",
                        "name": "internal_credential_stuffing",
                        "scope": "Internal",
                        "tactic": {
                            "id": "TA0006",
                            "name": "Credential Access"
                        },
                        "tags": [
                            "Internal",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "T1110",
                            "name": "Brute Force"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}