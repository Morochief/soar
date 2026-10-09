=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "a43ca90b-5010-4f2d-8bcc-8edbe9a080c91784707505875-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 1831,
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
                    "anomaly_id": "tLXPiJ8BI3UnQyDOjMUa",
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
                    "end_bucket_time": 1784706900000,
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
                        "IpPort": "59297",
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
                    "num_failed": 6,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "tLXPiJ8BI3UnQyDOjMUa",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784706690915,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784706724913,
                    "record_number": "220086845",
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
                    "start_bucket_time": 1784705400000,
                    "stellar": {
                        "alert_time": 1784707505861,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 775437,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a43ca90b-5010-4f2d-8bcc-8edbe9a080c91784707505875-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 264,
                    "threat_score": 0,
                    "timestamp": 1784706689458,
                    "timestamp_utc": "2026-07-22T07:51:29.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1369,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784707505875,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1369.",
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
                "_id": "60ebda97-9429-4204-bf2e-5b2b9e6b645d1784707504810-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 1830,
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
                    "anomaly_id": "jLXSiJ8BI3UnQyDOJdfy",
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
                    "end_bucket_time": 1784707200000,
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
                        "IpPort": "59498",
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
                    "fidelity": 94.51,
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
                    "login_failure_rate": "32.98",
                    "login_failure_rate_raw": 32.978730805891644,
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
                    "orig_id": "jLXSiJ8BI3UnQyDOJdfy",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1784706859615,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784706893615,
                    "record_number": "220087033",
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
                    "start_bucket_time": 1784706900000,
                    "stellar": {
                        "alert_time": 1784707504772,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 603805,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "60ebda97-9429-4204-bf2e-5b2b9e6b645d1784707504810-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9900,
                    "threat_score": 0,
                    "timestamp": 1784706857750,
                    "timestamp_utc": "2026-07-22T07:54:17.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "32.14",
                    "unknown_users_rate_raw": 32.143826228527296,
                    "unknown_users_to_login_failures": "0.97",
                    "unknown_users_to_login_failures_raw": 0.9746835443037974,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784707504810,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 32.98 and of usernames not recognized by the system is 32.14.",
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
                "_id": "bb3a6301-b1e9-45cb-9a51-1c67ef8b354c1784707506886-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 1832,
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
                    "anomaly_id": "gbXUiJ8BI3UnQyDOIOQi",
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
                    "end_bucket_time": 1784707200000,
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
                        "IpPort": "59706",
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
                            28,
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
                        "total_failed": 144,
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
                    "orig_id": "gbXUiJ8BI3UnQyDOIOQi",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784706990940,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707024944,
                    "record_number": "220087294",
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
                    "start_bucket_time": 1784705700000,
                    "stellar": {
                        "alert_time": 1784707506004,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 475497,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bb3a6301-b1e9-45cb-9a51-1c67ef8b354c1784707506886-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 264,
                    "threat_score": 0,
                    "timestamp": 1784706990511,
                    "timestamp_utc": "2026-07-22T07:56:30.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1364,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784707506886,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1364.",
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
                "_id": "faab03c3-d110-4141-87f3-eecb6699f41e1784707806170-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2037,
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
                    "anomaly_id": "gbXUiJ8BI3UnQyDOIOQi",
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
                    "end_bucket_time": 1784707200000,
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
                        "IpPort": "59706",
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
                            28,
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
                        "total_failed": 144,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 20.12,
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
                    "orig_id": "gbXUiJ8BI3UnQyDOIOQi",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784706990940,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707024944,
                    "record_number": "220087294",
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
                    "start_bucket_time": 1784705700000,
                    "stellar": {
                        "alert_time": 1784707806142,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 775635,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "faab03c3-d110-4141-87f3-eecb6699f41e1784707806170-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 264,
                    "threat_score": 0,
                    "timestamp": 1784706990511,
                    "timestamp_utc": "2026-07-22T07:56:30.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1368,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784707806170,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1368.",
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
                "_id": "8ab507e7-4c36-44f5-a446-4d08247caf561784707807192-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2038,
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
                    "anomaly_id": "O7bXiJ8BI3UnQyDOowB1",
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
                    "end_bucket_time": 1784707500000,
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
                        "IpPort": "59988",
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
                            28,
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
                        "total_failed": 144,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 20.05,
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
                    "orig_id": "O7bXiJ8BI3UnQyDOowB1",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707219397,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707253404,
                    "record_number": "220087632",
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
                    "start_bucket_time": 1784706000000,
                    "stellar": {
                        "alert_time": 1784707806289,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 545774,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8ab507e7-4c36-44f5-a446-4d08247caf561784707807192-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9900,
                    "threat_score": 0,
                    "timestamp": 1784707217981,
                    "timestamp_utc": "2026-07-22T08:00:17.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1364,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784707807191,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1364.",
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
                "_id": "7e05d158-4ef7-4e1e-a1ca-ef75d1a638211784708106049-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2039,
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
                    "anomaly_id": "O7bXiJ8BI3UnQyDOowB1",
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
                    "end_bucket_time": 1784707500000,
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
                        "IpPort": "59988",
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
                            28,
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
                        "total_failed": 144,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 20.14,
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
                    "orig_id": "O7bXiJ8BI3UnQyDOowB1",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707219397,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707253404,
                    "record_number": "220087632",
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
                    "start_bucket_time": 1784706000000,
                    "stellar": {
                        "alert_time": 1784708106036,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 845521,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7e05d158-4ef7-4e1e-a1ca-ef75d1a638211784708106049-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 9900,
                    "threat_score": 0,
                    "timestamp": 1784707217981,
                    "timestamp_utc": "2026-07-22T08:00:17.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1368,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708106048,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1368.",
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
                "_id": "3a8eaf79-48f4-47a7-b11a-ce6097ac98aa1784708107067-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2040,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1363,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "qrbdiJ8BI3UnQyDOSS4W",
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
                    "end_bucket_time": 1784707800000,
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
                        "IpPort": "60550",
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
                    "fidelity": 20.03,
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
                    "orig_id": "qrbdiJ8BI3UnQyDOSS4W",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707594249,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707628248,
                    "record_number": "220088379",
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
                    "start_bucket_time": 1784706300000,
                    "stellar": {
                        "alert_time": 1784708106167,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 475497,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3a8eaf79-48f4-47a7-b11a-ce6097ac98aa1784708107067-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 264,
                    "threat_score": 0,
                    "timestamp": 1784707592479,
                    "timestamp_utc": "2026-07-22T08:06:32.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1363,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708107067,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1363.",
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
                "_id": "d9665f66-8dd8-4f23-af62-001f13e55e291784708406153-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2042,
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
                    "anomaly_id": "qrbdiJ8BI3UnQyDOSS4W",
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
                    "end_bucket_time": 1784707800000,
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
                        "IpPort": "60550",
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
                    "fidelity": 20.16,
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
                    "orig_id": "qrbdiJ8BI3UnQyDOSS4W",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707594249,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707628248,
                    "record_number": "220088379",
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
                    "start_bucket_time": 1784706300000,
                    "stellar": {
                        "alert_time": 1784708406138,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 775468,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d9665f66-8dd8-4f23-af62-001f13e55e291784708406153-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 264,
                    "threat_score": 0,
                    "timestamp": 1784707592479,
                    "timestamp_utc": "2026-07-22T08:06:32.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1369,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708406153,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1369.",
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
                "_id": "cdee311a-0141-476e-b9b2-a22cdc528a011784708404885-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2041,
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
                    "anomaly_id": "5LbfiJ8BI3UnQyDO4UK7",
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
                    "end_bucket_time": 1784708100000,
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
                        "IpPort": "60750",
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
                    "login_failure_rate": "32.47",
                    "login_failure_rate_raw": 32.47147471145139,
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
                    "orig_id": "5LbfiJ8BI3UnQyDO4UK7",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1784707760002,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707794003,
                    "record_number": "220088729",
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
                    "start_bucket_time": 1784707800000,
                    "stellar": {
                        "alert_time": 1784708404866,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 603937,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "cdee311a-0141-476e-b9b2-a22cdc528a011784708404885-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784707758256,
                    "timestamp_utc": "2026-07-22T08:09:18.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "31.64",
                    "unknown_users_rate_raw": 31.638872795773157,
                    "unknown_users_to_login_failures": "0.97",
                    "unknown_users_to_login_failures_raw": 0.9743589743589743,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708404885,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 32.47 and of usernames not recognized by the system is 31.64.",
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
                "_id": "07d38542-d4e5-4891-9ade-0fdffeda9e961784708407165-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2043,
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
                    "anomaly_id": "rbbhiJ8BI3UnQyDOGUsI",
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
                    "end_bucket_time": 1784708100000,
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
                        "IpPort": "60877",
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
                        "total_failed": 144,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 20.05,
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
                    "orig_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707845899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707879914,
                    "record_number": "220088822",
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
                    "start_bucket_time": 1784706600000,
                    "stellar": {
                        "alert_time": 1784708406256,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 525586,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "07d38542-d4e5-4891-9ade-0fdffeda9e961784708407165-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784707845453,
                    "timestamp_utc": "2026-07-22T08:10:45.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1364,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708407165,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1364.",
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
                "_id": "ce78cd8b-3191-4762-89d6-e6a447c5308e1784708409733-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2044,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7685,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "172.16.201.4"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784708100000,
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
                        "IpPort": "60877",
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
                    "event_name": "user_login_fail",
                    "event_score": 71,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            166
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 166,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.56,
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
                    "num_failed": 144,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707845899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707879914,
                    "record_number": "220088822",
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
                    "start_bucket_time": 1784707800000,
                    "stellar": {
                        "alert_time": 1784708408730,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 528060,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ce78cd8b-3191-4762-89d6-e6a447c5308e1784708409733-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784707845453,
                    "timestamp_utc": "2026-07-22T08:10:45.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 7685,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708409733,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 166 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7685.",
                        "display_name": "Internal User Login Failure Anomaly",
                        "framework_version": "v8",
                        "name": "internal_user_login_fail",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "Kerberos Events",
                            "name": "internal_user_login_fail_kerberos"
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
                "_id": "945d7507-c46b-403b-8408-ab24f70e9d841784708705861-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2045,
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
                    "anomaly_id": "rbbhiJ8BI3UnQyDOGUsI",
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
                    "end_bucket_time": 1784708100000,
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
                        "IpPort": "60877",
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
                        "total_failed": 144,
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
                    "orig_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707845899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707879914,
                    "record_number": "220088822",
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
                    "start_bucket_time": 1784706600000,
                    "stellar": {
                        "alert_time": 1784708705790,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 825120,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "945d7507-c46b-403b-8408-ab24f70e9d841784708705861-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784707845453,
                    "timestamp_utc": "2026-07-22T08:10:45.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1368,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708705861,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 144) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1368.",
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
                "_id": "0f22b982-eae4-4694-b913-21b963722ed31784708708789-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2047,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7707,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "computer_name": "VMBASE8",
                    "detected_fields": [
                        "srcip"
                    ],
                    "detected_values": [
                        "172.16.201.4"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784708100000,
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
                        "IpPort": "60877",
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
                    "event_name": "user_login_fail",
                    "event_score": 71,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            166
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 166,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.58,
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
                    "num_failed": 22,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "rbbhiJ8BI3UnQyDOGUsI",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784707845899,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784707879914,
                    "record_number": "220088822",
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
                    "start_bucket_time": 1784707800000,
                    "stellar": {
                        "alert_time": 1784708708720,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 828050,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "0f22b982-eae4-4694-b913-21b963722ed31784708708789-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784707845453,
                    "timestamp_utc": "2026-07-22T08:10:45.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 7707,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708708789,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 166 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7707.",
                        "display_name": "Internal User Login Failure Anomaly",
                        "framework_version": "v8",
                        "name": "internal_user_login_fail",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "Kerberos Events",
                            "name": "internal_user_login_fail_kerberos"
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
                "_id": "08ad2114-873e-4426-b888-10e8c87eef191784708706869-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2046,
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
                    "anomaly_id": "cbbliJ8BI3UnQyDOEGsf",
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
                    "end_bucket_time": 1784708400000,
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
                        "IpPort": "61244",
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
                    "fidelity": 20.06,
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
                    "orig_id": "cbbliJ8BI3UnQyDOEGsf",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784708105656,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784708139660,
                    "record_number": "220089322",
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
                    "start_bucket_time": 1784706900000,
                    "stellar": {
                        "alert_time": 1784708705904,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 565313,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "08ad2114-873e-4426-b888-10e8c87eef191784708706869-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784708104293,
                    "timestamp_utc": "2026-07-22T08:15:04.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1365,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784708706869,
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "209cfc5f-4fb5-463c-8ab0-7a4b7097866a1784709006191-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2048,
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
                    "anomaly_id": "cbbliJ8BI3UnQyDOEGsf",
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
                    "end_bucket_time": 1784708400000,
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
                        "IpPort": "61244",
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
                    "orig_id": "cbbliJ8BI3UnQyDOEGsf",
                    "orig_index": "aella-wineventlog-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784708105656,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784708139660,
                    "record_number": "220089322",
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
                    "start_bucket_time": 1784706900000,
                    "stellar": {
                        "alert_time": 1784709006184,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 865593,
                        "status": "New"
                    },
                    "stellar_da_input": 3174,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "209cfc5f-4fb5-463c-8ab0-7a4b7097866a1784709006191-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1784708104293,
                    "timestamp_utc": "2026-07-22T08:15:04.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1369,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784709006191,
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
            }
        ]
    }
}