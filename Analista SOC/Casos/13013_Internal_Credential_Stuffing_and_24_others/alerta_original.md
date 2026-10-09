=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "018c9590-6041-4528-a18a-9294409f642b1785919806006-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 627,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1368,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "mOsQ0Z8BI3UnQyDOtfCm",
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
                    "end_bucket_time": 1785919200000,
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
                        "IpPort": "9521",
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
                    "event_score": 42,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            28,
                            30,
                            30,
                            28,
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
                        "total_failed": 146,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 20.13,
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
                    "orig_id": "mOsQ0Z8BI3UnQyDOtfCm",
                    "orig_index": "aella-wineventlog-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785918910689,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785918953411,
                    "record_number": "222309092",
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
                    "start_bucket_time": 1785917700000,
                    "stellar": {
                        "alert_time": 1785919805992,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 845551,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "018c9590-6041-4528-a18a-9294409f642b1785919806006-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 11036,
                    "threat_score": 0,
                    "timestamp": 1785918909281,
                    "timestamp_utc": "2026-08-05T08:35:09.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1368,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785919806006,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1368.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "4c075ab3-3376-4d55-93b8-91e0045358261785919807014-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 628,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1365,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "4-wX0Z8BI3UnQyDOHiGw",
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
                    "end_bucket_time": 1785919500000,
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
                        "IpPort": "10155",
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
                    "event_score": 42,
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
                    "fidelity": 20.07,
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
                    "num_failed": 26,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "4-wX0Z8BI3UnQyDOHiGw",
                    "orig_index": "aella-wineventlog-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785919331856,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785919374591,
                    "record_number": "222310162",
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
                    "start_bucket_time": 1785918000000,
                    "stellar": {
                        "alert_time": 1785919806091,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 425249,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4c075ab3-3376-4d55-93b8-91e0045358261785919807014-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785919330672,
                    "timestamp_utc": "2026-08-05T08:42:10.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1365,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785919807014,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1365.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "13b119a1-61c1-484a-a064-576a0312ea8b1785920105930-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 629,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1369,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "4-wX0Z8BI3UnQyDOHiGw",
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
                    "end_bucket_time": 1785919500000,
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
                        "IpPort": "10155",
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
                    "event_score": 42,
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
                    "fidelity": 20.15,
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
                    "orig_id": "4-wX0Z8BI3UnQyDOHiGw",
                    "orig_index": "aella-wineventlog-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785919331856,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785919374591,
                    "record_number": "222310162",
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
                    "start_bucket_time": 1785918000000,
                    "stellar": {
                        "alert_time": 1785920105904,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 725062,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "13b119a1-61c1-484a-a064-576a0312ea8b1785920105930-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785919330672,
                    "timestamp_utc": "2026-08-05T08:42:10.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1369,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785920105929,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1369.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "ce2ce7db-fd99-4516-b95e-5a129119b3101785920106938-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 630,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1364,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "0uwa0Z8BI3UnQyDOx0iS",
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
                    "end_bucket_time": 1785919800000,
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
                        "IpPort": "10490",
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
                    "event_score": 42,
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
                    "fidelity": 20.04,
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
                    "orig_id": "0uwa0Z8BI3UnQyDOx0iS",
                    "orig_index": "aella-wineventlog-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785919573353,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785919616096,
                    "record_number": "222310611",
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
                    "start_bucket_time": 1785918300000,
                    "stellar": {
                        "alert_time": 1785920106032,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 485364,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ce2ce7db-fd99-4516-b95e-5a129119b3101785920106938-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785919571504,
                    "timestamp_utc": "2026-08-05T08:46:11.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1364,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785920106938,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1364.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.03-000030",
                "_type": "_doc",
                "_id": "56e96cc5-aeea-4f98-9264-68e08459b67e1785920406075-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 634,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1370,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "0uwa0Z8BI3UnQyDOx0iS",
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
                    "end_bucket_time": 1785919800000,
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
                        "IpPort": "10490",
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
                    "event_score": 42,
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
                    "fidelity": 20.17,
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
                    "orig_id": "0uwa0Z8BI3UnQyDOx0iS",
                    "orig_index": "aella-wineventlog-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785919573353,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785919616096,
                    "record_number": "222310611",
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
                    "start_bucket_time": 1785918300000,
                    "stellar": {
                        "alert_time": 1785920406060,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 785392,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.05-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "56e96cc5-aeea-4f98-9264-68e08459b67e1785920406075-YWVsbGEtc2VyLTIwMjYuMDguMDUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785919571504,
                    "timestamp_utc": "2026-08-05T08:46:11.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1370,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785920406075,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1370.",
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
            }
        ]
    }
}