=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "b031fe1d-5e22-4acb-ae9e-caf7ef46e4a11784195709825-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11757,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1111,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "gU5Sap8BI3UnQyDO1ccF",
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
                    "end_bucket_time": 1784195400000,
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
                        "IpPort": "30246",
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
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            168
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 168,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 26.41,
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
                    "num_failed": 146,
                    "num_successful": 0,
                    "opcode": "Información",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "gU5Sap8BI3UnQyDO1ccF",
                    "orig_index": "aella-wineventlog-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784195203637,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784195233986,
                    "record_number": "219096817",
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
                    "start_bucket_time": 1784195100000,
                    "stellar": {
                        "alert_time": 1784195708773,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 468362,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b031fe1d-5e22-4acb-ae9e-caf7ef46e4a11784195709825-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4624,
                    "threat_score": 0,
                    "timestamp": 1784195201795,
                    "timestamp_utc": "2026-07-16T09:46:41.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1111,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784195709824,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 168 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 1111.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "04dd2069-ad60-4f13-ae6e-0c103538cc1d1784196009024-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11758,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "accumulated_anomalous_failures": 1133,
                    "agent": {
                        "computer_name": "VMBASE8",
                        "ephemeral_id": "9e134770-74c3-404d-b06f-41b4f5e667d8",
                        "id": "d274804f-525e-4b1b-9256-941c5dc3d060",
                        "name": "4c735067a7f5483ca72265eb5324214c",
                        "type": "winlogbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "gU5Sap8BI3UnQyDO1ccF",
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
                    "end_bucket_time": 1784195400000,
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
                        "IpPort": "30246",
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
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "failed_details": [
                            168
                        ],
                        "successful_details": [
                            0
                        ],
                        "time_bucket": 5,
                        "total_fail_ratio": 1,
                        "total_failed": 168,
                        "total_successful": 0
                    },
                    "event_type": "reconn",
                    "fidelity": 27.09,
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
                    "orig_id": "gU5Sap8BI3UnQyDO1ccF",
                    "orig_index": "aella-wineventlog-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "percent_failed": 1,
                    "process_id": 692,
                    "process_time": 1784195203637,
                    "provider_guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
                    "receive_time": 1784195233986,
                    "record_number": "219096817",
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
                    "start_bucket_time": 1784195100000,
                    "stellar": {
                        "alert_time": 1784196009012,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 768601,
                        "status": "New"
                    },
                    "stellar_da_input": 3173,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "04dd2069-ad60-4f13-ae6e-0c103538cc1d1784196009024-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "task": "Kerberos Authentication Service",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "thread_id": 4624,
                    "threat_score": 0,
                    "timestamp": 1784195201795,
                    "timestamp_utc": "2026-07-16T09:46:41.000Z",
                    "type": "wineventlog",
                    "username": "HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py",
                    "weighted_anomaly_score": 1133,
                    "wineventlog_version": 2,
                    "write_by": "sef",
                    "write_time": 1784196009024,
                    "xdr_event": {
                        "description": "In internal traffic, IP/name: 172.16.201.4 (private) has 168 outgoing login failures related to windows_login in the last 5.0 minutes. The failure percentage rate was 100.00%. This host has had a weighted anomaly score of 1133.",
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
            }
        ]
    }
}