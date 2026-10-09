=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "3dc8696b-54e5-4063-be6c-7fe895db16a91785574505787-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14486,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1301,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "dxR9vJ8BI3UnQyDOE6Qe",
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
                    "end_bucket_time": 1785573900000,
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
                        "IpPort": "8831",
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
                    "event_score": 41,
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
                    "fidelity": 18.7,
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
                    "num_failed": 8,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "dxR9vJ8BI3UnQyDOE6Qe",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785573699476,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573739700,
                    "record_number": "221736923",
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
                    "start_bucket_time": 1785572400000,
                    "stellar": {
                        "alert_time": 1785574505777,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 765028,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3dc8696b-54e5-4063-be6c-7fe895db16a91785574505787-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785573697827,
                    "timestamp_utc": "2026-08-01T08:41:37.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1301,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574505787,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1301.",
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
                "_id": "185402d9-517a-4c97-9bd3-fd19499aa68b1785574504760-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14485,
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
                    "anomaly_id": "9RR_vJ8BI3UnQyDOgral",
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
                    "end_bucket_time": 1785574200000,
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
                        "IpPort": "9064",
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
                    "login_failure_rate": "31.54",
                    "login_failure_rate_raw": 31.54080841620559,
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
                    "orig_id": "9RR_vJ8BI3UnQyDOgral",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1785573850200,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573890441,
                    "record_number": "221737216",
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
                    "start_bucket_time": 1785573900000,
                    "stellar": {
                        "alert_time": 1785574504735,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 604394,
                        "status": "New"
                    },
                    "stellar_da_input": 3169,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "185402d9-517a-4c97-9bd3-fd19499aa68b1785574504760-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 6492,
                    "threat_score": 0,
                    "timestamp": 1785573848319,
                    "timestamp_utc": "2026-08-01T08:44:08.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "30.74",
                    "unknown_users_rate_raw": 30.742306937314307,
                    "unknown_users_to_login_failures": "0.97",
                    "unknown_users_to_login_failures_raw": 0.9746835443037974,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574504760,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 31.54 and of usernames not recognized by the system is 30.74.",
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
                "_id": "29518ed5-4a2c-4299-9ac2-f1dd336b0cad1785574506797-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14487,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1296,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "7BSAvJ8BI3UnQyDObbwb",
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
                    "end_bucket_time": 1785574200000,
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
                        "IpPort": "9142",
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
                    "event_score": 41,
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
                    "fidelity": 18.58,
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
                    "orig_id": "7BSAvJ8BI3UnQyDObbwb",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785573909787,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573950021,
                    "record_number": "221737293",
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
                    "start_bucket_time": 1785572700000,
                    "stellar": {
                        "alert_time": 1785574505920,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 545571,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "29518ed5-4a2c-4299-9ac2-f1dd336b0cad1785574506797-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785573908542,
                    "timestamp_utc": "2026-08-01T08:45:08.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1296,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574506797,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1296.",
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
                "_id": "312d3762-7394-49cc-b4ac-9fa86b1d67071785574509637-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14488,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7307,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "7BSAvJ8BI3UnQyDObbwb",
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
                    "end_bucket_time": 1785574200000,
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
                        "IpPort": "9142",
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
                            164
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 164,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.15,
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
                    "num_failed": 142,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "7BSAvJ8BI3UnQyDObbwb",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785573909787,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573950021,
                    "record_number": "221737293",
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
                    "start_bucket_time": 1785573900000,
                    "stellar": {
                        "alert_time": 1785574508650,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 548301,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "312d3762-7394-49cc-b4ac-9fa86b1d67071785574509637-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785573908542,
                    "timestamp_utc": "2026-08-01T08:45:08.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 7307,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574509637,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 164 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7307.",
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
                "_id": "fe81a41d-9e37-4bed-aa81-2e3173b974861785574806160-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14669,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1304,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "7BSAvJ8BI3UnQyDObbwb",
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
                    "end_bucket_time": 1785574200000,
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
                        "IpPort": "9142",
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
                    "event_score": 41,
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
                    "fidelity": 18.75,
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
                    "num_failed": 8,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "7BSAvJ8BI3UnQyDObbwb",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785573909787,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573950021,
                    "record_number": "221737293",
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
                    "start_bucket_time": 1785572700000,
                    "stellar": {
                        "alert_time": 1785574806109,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 845760,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fe81a41d-9e37-4bed-aa81-2e3173b974861785574806160-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785573908542,
                    "timestamp_utc": "2026-08-01T08:45:08.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1304,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574806160,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1304.",
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
                "_id": "c7cdcbb3-b85a-4f30-acd1-8470c7aa0e421785574810596-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14671,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7329,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "7BSAvJ8BI3UnQyDObbwb",
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
                    "end_bucket_time": 1785574200000,
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
                        "IpPort": "9142",
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
                            164
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 164,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.17,
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
                    "orig_id": "7BSAvJ8BI3UnQyDObbwb",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785573909787,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785573950021,
                    "record_number": "221737293",
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
                    "start_bucket_time": 1785573900000,
                    "stellar": {
                        "alert_time": 1785574810520,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 850171,
                        "status": "New"
                    },
                    "stellar_da_input": 3171,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c7cdcbb3-b85a-4f30-acd1-8470c7aa0e421785574810596-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785573908542,
                    "timestamp_utc": "2026-08-01T08:45:08.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 7329,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574810596,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 164 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7329.",
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
                "_id": "55580b37-c4fb-4c75-9852-bc0255fa303b1785574805551-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14668,
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
                    "anomaly_id": "CxSEvJ8BI3UnQyDOF9dh",
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
                    "end_bucket_time": 1785574500000,
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
                        "IpPort": "9470",
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
                    "fidelity": 94.44,
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
                    "login_failure_rate": "30.23",
                    "login_failure_rate_raw": 30.230761479291925,
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
                    "orig_id": "CxSEvJ8BI3UnQyDOF9dh",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1785574150563,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574190790,
                    "record_number": "221737693",
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
                    "start_bucket_time": 1785574200000,
                    "stellar": {
                        "alert_time": 1785574805540,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 604941,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "55580b37-c4fb-4c75-9852-bc0255fa303b1785574805551-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 10752,
                    "threat_score": 0,
                    "timestamp": 1785574149361,
                    "timestamp_utc": "2026-08-01T08:49:09.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "29.83",
                    "unknown_users_rate_raw": 29.827684659568032,
                    "unknown_users_to_login_failures": "0.99",
                    "unknown_users_to_login_failures_raw": 0.9866666666666667,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574805551,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 30.23 and of usernames not recognized by the system is 29.83.",
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
                "_id": "a51b3b76-a9a1-4843-9438-37506ce7537a1785574807168-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14670,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1296,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "HxSFvJ8BI3UnQyDOAODk",
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
                    "end_bucket_time": 1785574500000,
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
                        "IpPort": "9573",
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
                    "event_score": 41,
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
                    "fidelity": 18.59,
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
                    "num_failed": 20,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "HxSFvJ8BI3UnQyDOAODk",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574211331,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574251566,
                    "record_number": "221737773",
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
                    "start_bucket_time": 1785573000000,
                    "stellar": {
                        "alert_time": 1785574806284,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 545919,
                        "status": "New"
                    },
                    "stellar_da_input": 3170,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a51b3b76-a9a1-4843-9438-37506ce7537a1785574807168-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785574209630,
                    "timestamp_utc": "2026-08-01T08:50:09.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1296,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785574807168,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1296.",
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
                "_id": "8dbf47fd-317b-455d-8806-a1c04b2074111785575106327-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14672,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1304,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "HxSFvJ8BI3UnQyDOAODk",
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
                    "end_bucket_time": 1785574500000,
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
                        "IpPort": "9573",
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
                    "event_score": 41,
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
                    "fidelity": 18.76,
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
                    "num_failed": 8,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "HxSFvJ8BI3UnQyDOAODk",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574211331,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574251566,
                    "record_number": "221737773",
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
                    "start_bucket_time": 1785573000000,
                    "stellar": {
                        "alert_time": 1785575106286,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 845921,
                        "status": "New"
                    },
                    "stellar_da_input": 3170,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8dbf47fd-317b-455d-8806-a1c04b2074111785575106327-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785574209630,
                    "timestamp_utc": "2026-08-01T08:50:09.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1304,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575106326,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 28 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 28 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1304.",
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
                "_id": "4be44638-791e-44e7-8c40-35d5edc693d01785575110358-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14674,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7325,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "MhWLvJ8BI3UnQyDOaQ6k",
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
                    "end_bucket_time": 1785574800000,
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
                        "IpPort": "10184",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x12",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
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
                            164
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 164,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.17,
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
                    "num_failed": 142,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "MhWLvJ8BI3UnQyDOaQ6k",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574636068,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574676314,
                    "record_number": "221738492",
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
                    "srcip_username": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785574500000,
                    "stellar": {
                        "alert_time": 1785575109310,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 428722,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4be44638-791e-44e7-8c40-35d5edc693d01785575110358-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 6492,
                    "threat_score": 0,
                    "timestamp": 1785574634702,
                    "timestamp_utc": "2026-08-01T08:57:14.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
                    "weighted_anomaly_score": 7325,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575110358,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 164 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7325.",
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
                "_id": "13ef4ba2-5e47-4c00-aae3-43522b057ce91785575107336-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14673,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1298,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "kRWLvJ8BI3UnQyDO3hHL",
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
                    "end_bucket_time": 1785574800000,
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
                        "IpPort": "10222",
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
                    "event_score": 41,
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
                    "fidelity": 18.64,
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
                    "orig_id": "kRWLvJ8BI3UnQyDO3hHL",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574662381,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574702624,
                    "record_number": "221738550",
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
                    "start_bucket_time": 1785573300000,
                    "stellar": {
                        "alert_time": 1785575106426,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 396044,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "13ef4ba2-5e47-4c00-aae3-43522b057ce91785575107336-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785574661173,
                    "timestamp_utc": "2026-08-01T08:57:41.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1298,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575107335,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1298.",
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
                "_id": "c1cd202c-3894-4f8c-9443-70cd03db13f81785575409012-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14678,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 7347,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "MhWLvJ8BI3UnQyDOaQ6k",
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
                    "end_bucket_time": 1785574800000,
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
                        "IpPort": "10184",
                        "PreAuthEncryptionType": "0x2d",
                        "PreAuthType": "-",
                        "ResponseTicket": "-",
                        "ServiceAvailableKeys": "-",
                        "ServiceName": "krbtgt/CAJAANDE.LOCAL",
                        "ServiceSid": "S-1-0-0",
                        "ServiceSupportedEncryptionTypes": "-",
                        "SessionKeyEncryptionType": "0x2d",
                        "Status": "0x12",
                        "TargetDomainName": "CAJAANDE.LOCAL",
                        "TargetSid": "S-1-0-0",
                        "TargetUserName": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
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
                            164
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 164,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 98.19,
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
                    "orig_id": "MhWLvJ8BI3UnQyDOaQ6k",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574636068,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574676314,
                    "record_number": "221738492",
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
                    "srcip_username": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
                    "srcip_usersid": "S-1-0-0",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1785574500000,
                    "stellar": {
                        "alert_time": 1785575409005,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 728417,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c1cd202c-3894-4f8c-9443-70cd03db13f81785575409012-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 6492,
                    "threat_score": 0,
                    "timestamp": 1785574634702,
                    "timestamp_utc": "2026-08-01T08:57:14.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
                    "weighted_anomaly_score": 7347,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575409012,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 164 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 7347.",
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
                "_id": "7c4eb3fc-f8c5-4ebf-a0db-7691ea92aef01785575406180-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14676,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1306,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "kRWLvJ8BI3UnQyDO3hHL",
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
                    "end_bucket_time": 1785574800000,
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
                        "IpPort": "10222",
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
                    "event_score": 41,
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
                    "fidelity": 18.81,
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
                    "num_failed": 8,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "kRWLvJ8BI3UnQyDO3hHL",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574662381,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574702624,
                    "record_number": "221738550",
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
                    "start_bucket_time": 1785573300000,
                    "stellar": {
                        "alert_time": 1785575406144,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 695762,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7c4eb3fc-f8c5-4ebf-a0db-7691ea92aef01785575406180-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785574661173,
                    "timestamp_utc": "2026-08-01T08:57:41.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1306,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575406180,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 146) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 28 failures, 0 successes\nLast 15.0-10.0 minutes: 30 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 28 failures, 0 successes.\n This account has a weighted anomaly score of 1306.",
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
                "_id": "6a27b41d-a8be-4156-a3bd-59d2d245d31d1785575405296-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14675,
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
                    "anomaly_id": "bBWNvJ8BI3UnQyDOPhxh",
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
                    "end_bucket_time": 1785575100000,
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
                        "IpPort": "10346",
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
                    "fidelity": 94.1,
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
                    "login_failure_rate": "30.24",
                    "login_failure_rate_raw": 30.238379222873654,
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
                    "orig_id": "bBWNvJ8BI3UnQyDOPhxh",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "possible_breached_ips": [],
                    "process_id": 692,
                    "process_time": 1785574750480,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574790721,
                    "record_number": "221738715",
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
                    "start_bucket_time": 1785574800000,
                    "stellar": {
                        "alert_time": 1785575405283,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 604988,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6a27b41d-a8be-4156-a3bd-59d2d245d31d1785575405296-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "suspicious_ips": [
                        "172.16.201.4"
                    ],
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 6492,
                    "threat_score": 0,
                    "timestamp": 1785574749066,
                    "timestamp_utc": "2026-08-01T08:59:09.000Z",
                    "type": "wineventlog",
                    "unknown_users_rate": "29.43",
                    "unknown_users_rate_raw": 29.432022443597024,
                    "unknown_users_to_login_failures": "0.97",
                    "unknown_users_to_login_failures_raw": 0.9733333333333334,
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575405296,
                    "xdr_event": {
                        "description": "In internal traffic of type Microsoft-Windows-Security-Auditing, the target domain \"CAJAANDE.LOCAL\" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures per minute is 30.24 and of usernames not recognized by the system is 29.43.",
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
                "_id": "e87d9d55-ad8c-473a-bf63-484349ad6ced1785575407192-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14677,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1298,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "4RWPvJ8BI3UnQyDOiSwV",
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
                    "end_bucket_time": 1785575100000,
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
                        "IpPort": "10574",
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
                    "event_score": 41,
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
                    "fidelity": 18.64,
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
                    "num_failed": 20,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "4RWPvJ8BI3UnQyDOiSwV",
                    "orig_index": "aella-wineventlog-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1785574903073,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1785574943314,
                    "record_number": "221738972",
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
                    "start_bucket_time": 1785573600000,
                    "stellar": {
                        "alert_time": 1785575406309,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 455702,
                        "status": "New"
                    },
                    "stellar_da_input": 3172,
                    "stellar_index_id": "aella-ser-2026.08.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e87d9d55-ad8c-473a-bf63-484349ad6ced1785575407192-YWVsbGEtc2VyLTIwMjYuMDguMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 1832,
                    "threat_score": 0,
                    "timestamp": 1785574901920,
                    "timestamp_utc": "2026-08-01T09:01:41.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1298,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1785575407192,
                    "xdr_event": {
                        "description": "In internal traffic, the account with ID \"S-1-0-0\", username \"HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py\" showed an anomalously high number (#: 148) of account login failures in the last 25.0 minutes. The failure percentage rate was 100.00%, and logins for the account were distributed across the 25.0 minutes as follows:\nLast 5.0 minutes: 30 failures, 0 successes\nLast 10.0-5.0 minutes: 30 failures, 0 successes\nLast 15.0-10.0 minutes: 28 failures, 0 successes\nLast 20.0-15.0 minutes: 30 failures, 0 successes\nLast 25.0-20.0 minutes: 30 failures, 0 successes.\n This account has a weighted anomaly score of 1298.",
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