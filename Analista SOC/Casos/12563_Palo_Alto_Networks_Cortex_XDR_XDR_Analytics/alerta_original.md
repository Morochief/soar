=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "3a090ad6-65b0-4563-add0-c06eb13b43fe1784823137656-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3621,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "gRW-j58BI3UnQyDOTfdK",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "131708"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "An uncommon LOLBIN added to startup-related Registry keys"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.50",
                        "name": "NB-ALPIZZUTI"
                    },
                    "locid": "unassigned location",
                    "msg_class": "palo_alto_networks_cortex_xdr_alerts",
                    "msg_origin": {
                        "category": "threat_intel",
                        "processor": {
                            "id": "6939ef90a77d64c0b0abb567",
                            "name": "palo_alto_networks_cortex_xdr",
                            "type": "log_collector"
                        },
                        "source": "palo_alto_networks_cortex_xdr",
                        "vendor": "palo_alto_networks"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "gRW-j58BI3UnQyDOTfdK",
                    "orig_index": "aella-syslog-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "9.0.0.16757",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "131708",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "windowsdesktop-runtime-6.0.11-win-x64.exe registered a LOLBIN to be run on the next login or boot, the activity initiated by nci_x64_26.0_7476.4950.305.exe. In the past 30 days, the LOLBIN has been seen registered to the registry on 0 different days and on 0 additional endpoints. The LOLBIN was registered at HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce, in the {c4846f79-a633-4ae4-92a3-92fdbeb33da2} registry value. The registered LOLBIN is \"C:\\ProgramData\\Package Cache\\{c4846f79-a633-4ae4-92a3-92fdbeb33da2}\\windowsdesktop-runtime-6.0.11-win-x64.exe\" /burn.runonce",
                        "detection_timestamp": 1784822727468,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "d5075c351c694d029cbc99ffe8492beb",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "action_registry_data": "\"C:\\ProgramData\\Package Cache\\{c4846f79-a633-4ae4-92a3-92fdbeb33da2}\\windowsdesktop-runtime-6.0.11-win-x64.exe\" /burn.runonce",
                                "action_registry_key_name": "HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                                "action_registry_value_name": "{c4846f79-a633-4ae4-92a3-92fdbeb33da2}",
                                "actor_causality_id": "Ad0avG5JBJcAAIEgAAAAAA==",
                                "actor_process_causality_id": "Ad0avG5JBJcAAIEgAAAAAA==",
                                "actor_process_command_line": "\"C:\\WINDOWS\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe\" -q -burn.elevated BurnPipe.{16DB66BF-522A-46B0-86BE-192FBA915320} {982C30A2-C083-4980-9F25-9991C47C0EDE} 12604",
                                "actor_process_image_md5": "182aa2cc4f6911fcfaa64612d77b69b4",
                                "actor_process_image_name": "windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "actor_process_image_path": "C:\\Windows\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "actor_process_image_sha256": "c966caa94f8abdccf5bff16cbbe6fc0ff4cba6f25a54dbd61427b9bdc3362b0c",
                                "actor_process_instance_id": "Ad0avSlEAvAAAGfAAAAAAA==",
                                "actor_process_os_pid": 26560,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 28896,
                                "agent_host_boot_time": 1784579655433,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0avG5JBJcAAIEgAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\alfredopizzuti\\Downloads\\nci_x64_26.0_7476.4950.305.exe\" ",
                                "causality_actor_process_execution_time": 1784822449788,
                                "causality_actor_process_image_md5": "ff205f3e06a4d2015c00560e4a0cd5e8",
                                "causality_actor_process_image_name": "nci_x64_26.0_7476.4950.305.exe",
                                "causality_actor_process_image_path": "C:\\Users\\alfredopizzuti\\Downloads\\nci_x64_26.0_7476.4950.305.exe",
                                "causality_actor_process_image_sha256": "a0f10df1bfcc081050af17014a1c9285baee51bfe7866aa49f680e96f9b37130",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Nanosoft AS",
                                "cloud_provider": "others",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn4+6FC1WDZziACUZjQ==",
                                "event_sub_type": 4,
                                "event_timestamp": 1784822727468,
                                "event_type": "Registry Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0avG5JBJcAAIEgAAAAAA==",
                                "os_actor_process_command_line": "\"C:\\WINDOWS\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe\" -q -burn.elevated BurnPipe.{16DB66BF-522A-46B0-86BE-192FBA915320} {982C30A2-C083-4980-9F25-9991C47C0EDE} 12604",
                                "os_actor_process_image_name": "windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "os_actor_process_image_path": "C:\\Windows\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "os_actor_process_image_sha256": "c966caa94f8abdccf5bff16cbbe6fc0ff4cba6f25a54dbd61427b9bdc3362b0c",
                                "os_actor_process_instance_id": "Ad0avSlEAvAAAGfAAAAAAA==",
                                "os_actor_process_os_pid": 26560,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 28896,
                                "user_name": "TECHNOMA\\alfredopizzuti"
                            }
                        ],
                        "external_id": "85da5104-e2af-4b93-90b0-5a515cd1f5f0",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.50"
                        ],
                        "host_name": "NB-ALPIZZUTI",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1784822940911,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "cfb4e6ce-8f82-4d76-b5ed-79ab8e68c571",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0004 - Privilege Escalation",
                            "TA0003 - Persistence"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1547 - Boot or Logon Autostart Execution"
                        ],
                        "name": "An uncommon LOLBIN added to startup-related Registry keys",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "0f8549d8-3217-4900-a9e1-d2ae3be2042e"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "\"C:\\WINDOWS\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe\" -q -burn.elevated BurnPipe.{16DB66BF-522A-46B0-86BE-192FBA915320} {982C30A2-C083-4980-9F25-9991C47C0EDE} 12604",
                                "executable": "C:\\Windows\\Temp\\{331C1E0F-7FC7-4021-AA9A-ED27E136D335}\\.be\\windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "hash": {
                                    "md5": "182aa2cc4f6911fcfaa64612d77b69b4",
                                    "sha256": "c966caa94f8abdccf5bff16cbbe6fc0ff4cba6f25a54dbd61427b9bdc3362b0c"
                                },
                                "name": "windowsdesktop-runtime-6.0.11-win-x64.exe",
                                "pid": 26560
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 97158,
                        "status": "New"
                    },
                    "stellar_da_input": 7187,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3a090ad6-65b0-4563-add0-c06eb13b43fe1784823137656-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784822727468,
                    "timestamp_utc": "2026-07-23T16:05:27.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\alfredopizzuti"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1784823137656,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"an uncommon lolbin added to startup-related registry keys\" on host \"NB-ALPIZZUTI\" (\"192.168.169.50\"). The behavioral analytics system identified this \"persistence\" threat through rule \"cfb4e6ce-8f82-4d76-b5ed-79ab8e68c571\" with status \"matched\".. Analytics details: \"windowsdesktop-runtime-6.0.11-win-x64.exe registered a LOLBIN to be run on the next login or boot, the activity initiated by nci_x64_26.0_7476.4950.305.exe. In the past 30 days, the LOLBIN has been seen registered to the registry on 0 different days and on 0 additional endpoints. The LOLBIN was registered at HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce, in the {c4846f79-a633-4ae4-92a3-92fdbeb33da2} registry value. The registered LOLBIN is \"C:\\ProgramData\\Package Cache\\{c4846f79-a633-4ae4-92a3-92fdbeb33da2}\\windowsdesktop-runtime-6.0.11-win-x64.exe\" /burn.runonce\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): An uncommon LOLBIN added to startup-related Registry keys",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-an_uncommon_lolbin_added_to_startup_related_registry_keys",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1547",
                            "name": "Boot or Logon Autostart Execution"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1547",
                                    "name": "Boot or Logon Autostart Execution"
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0003",
                                    "name": "Persistence"
                                },
                                "technique": {
                                    "id": "T1547",
                                    "name": "Boot or Logon Autostart Execution"
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
                "_id": "e37f38b6-672d-4a3b-a393-44a307f192201784823733248-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3624,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "0RbHj58BI3UnQyDOdIXz",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "131714"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.50",
                        "name": "NB-ALPIZZUTI"
                    },
                    "locid": "unassigned location",
                    "msg_class": "palo_alto_networks_cortex_xdr_alerts",
                    "msg_origin": {
                        "category": "threat_intel",
                        "processor": {
                            "id": "6939ef90a77d64c0b0abb567",
                            "name": "palo_alto_networks_cortex_xdr",
                            "type": "log_collector"
                        },
                        "source": "palo_alto_networks_cortex_xdr",
                        "vendor": "palo_alto_networks"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "0RbHj58BI3UnQyDOdIXz",
                    "orig_index": "aella-syslog-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "9.0.0.16757",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "131714",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "The process msiexec.exe loaded the DLL \"MSI3A1E.tmp\" on host NB-ALPIZZUTI. This DLL name is signed by CSOFT AS, which was seen on 1 other hosts in the last 30 days. In the last 30 days, the DLL's hash e872b68519de4d7e2bd816fe008adf64500fc763506acd413241fb861c811b42 was seen on 0 other hosts. Both DLL hash and signature vendor are rare, which might indicate an attacker performing DLL Hijacking. The DLL signature vendor was rarely seen globally",
                        "detection_timestamp": 1784823099453,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "d5075c351c694d029cbc99ffe8492beb",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "actor_causality_id": "Ad0avgch94QAAGisAAAAAA==",
                                "actor_process_causality_id": "Ad0avgch94QAAGisAAAAAA==",
                                "actor_process_command_line": "C:\\Windows\\System32\\MsiExec.exe -Embedding 319172CC81C39B322FF4416109F766AC E Global\\MSI0000",
                                "actor_process_image_md5": "183491a5b8cc2ab1b0b8da63423f3486",
                                "actor_process_image_name": "msiexec.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\msiexec.exe",
                                "actor_process_image_sha256": "954d7d13a11827116cc88a12b1e12ce34604264948cc32e4a3ef6d6d6afa2913",
                                "actor_process_instance_id": "Ad0avgch94QAAGisAAAAAA==",
                                "actor_process_os_pid": 26796,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 9912,
                                "agent_host_boot_time": 1784579655433,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0avgch94QAAGisAAAAAA==",
                                "causality_actor_process_command_line": "C:\\Windows\\System32\\MsiExec.exe -Embedding 319172CC81C39B322FF4416109F766AC E Global\\MSI0000",
                                "causality_actor_process_execution_time": 1784823135706,
                                "causality_actor_process_image_md5": "183491a5b8cc2ab1b0b8da63423f3486",
                                "causality_actor_process_image_name": "msiexec.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\msiexec.exe",
                                "causality_actor_process_image_sha256": "954d7d13a11827116cc88a12b1e12ce34604264948cc32e4a3ef6d6d6afa2913",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "cloud_provider": "others",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn4+/wUZWDZziACXclg==",
                                "event_sub_type": 1,
                                "event_timestamp": 1784823099453,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0avgch94QAAGisAAAAAA==",
                                "os_actor_process_command_line": "C:\\Windows\\System32\\MsiExec.exe -Embedding 319172CC81C39B322FF4416109F766AC E Global\\MSI0000",
                                "os_actor_process_image_name": "msiexec.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\msiexec.exe",
                                "os_actor_process_image_sha256": "954d7d13a11827116cc88a12b1e12ce34604264948cc32e4a3ef6d6d6afa2913",
                                "os_actor_process_instance_id": "Ad0avgch94QAAGisAAAAAA==",
                                "os_actor_process_os_pid": 26796,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 9912,
                                "user_name": "NT AUTHORITY\\SYSTEM"
                            }
                        ],
                        "external_id": "c5b14e89-3c3d-44ad-b987-362e2abb344f",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.50"
                        ],
                        "host_name": "NB-ALPIZZUTI",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1784823251871,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "3c2645a1-40cd-4c93-8cfe-ae37551b3036",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0002 - Execution",
                            "TA0003 - Persistence",
                            "TA0005 - Defense Evasion",
                            "TA0004 - Privilege Escalation",
                            "TA0005 - Stealth"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1574.001 - Hijack Execution Flow: DLL"
                        ],
                        "name": "A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "DT:DLL Hijacking Analytics"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:DLL Hijacking Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "024921da-7958-459c-a123-ec4efb33fb06"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "C:\\Windows\\System32\\MsiExec.exe -Embedding 319172CC81C39B322FF4416109F766AC E Global\\MSI0000",
                                "executable": "C:\\Windows\\System32\\msiexec.exe",
                                "hash": {
                                    "md5": "183491a5b8cc2ab1b0b8da63423f3486",
                                    "sha256": "954d7d13a11827116cc88a12b1e12ce34604264948cc32e4a3ef6d6d6afa2913"
                                },
                                "name": "msiexec.exe",
                                "pid": 26796
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 92741,
                        "status": "New"
                    },
                    "stellar_da_input": 6142,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e37f38b6-672d-4a3b-a393-44a307f192201784823733248-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784823099453,
                    "timestamp_utc": "2026-07-23T16:11:39.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\SYSTEM"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1784823733248,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"a rare dll, signed by a rarely seen vendor, was hijacked into a microsoft process\" on host \"NB-ALPIZZUTI\" (\"192.168.169.50\"). The behavioral analytics system identified this \"persistence\" threat through rule \"3c2645a1-40cd-4c93-8cfe-ae37551b3036\" with status \"matched\".. Analytics details: \"The process msiexec.exe loaded the DLL \"MSI3A1E.tmp\" on host NB-ALPIZZUTI. This DLL name is signed by CSOFT AS, which was seen on 1 other hosts in the last 30 days. In the last 30 days, the DLL's hash e872b68519de4d7e2bd816fe008adf64500fc763506acd413241fb861c811b42 was seen on 0 other hosts. Both DLL hash and signature vendor are rare, which might indicate an attacker performing DLL Hijacking. The DLL signature vendor was rarely seen globally\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-a_rare_dll_signed_by_a_rarely_seen_vendor_was_hijacked_into_a_microsoft_process",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1574",
                            "name": "Hijack Execution Flow",
                            "subtechnique": {
                                "id": "T1574.001",
                                "name": "DLL Search Order Hijacking"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0003",
                                    "name": "Persistence"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
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
                "_id": "454e30d5-3bd9-4040-bdfc-d8ab9401e0dd1784823733226-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 3623,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "0BbHj58BI3UnQyDOdIXz",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "131713"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.50",
                        "name": "NB-ALPIZZUTI"
                    },
                    "locid": "unassigned location",
                    "msg_class": "palo_alto_networks_cortex_xdr_alerts",
                    "msg_origin": {
                        "category": "threat_intel",
                        "processor": {
                            "id": "6939ef90a77d64c0b0abb567",
                            "name": "palo_alto_networks_cortex_xdr",
                            "type": "log_collector"
                        },
                        "source": "palo_alto_networks_cortex_xdr",
                        "vendor": "palo_alto_networks"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "0BbHj58BI3UnQyDOdIXz",
                    "orig_index": "aella-syslog-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "9.0.0.16757",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "131713",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "The process msiexec.exe loaded the DLL \"MSI6D3B.tmp\" on host NB-ALPIZZUTI. This DLL name is signed by OOO Nanosoft Razrabotka, which was seen on 1 other hosts in the last 30 days. In the last 30 days, the DLL's hash 2ae299f5681310b5b75f5f2b59130328382398333ff54ded4ee949f08150988c was seen on 0 other hosts. Both DLL hash and signature vendor are rare, which might indicate an attacker performing DLL Hijacking. The DLL signature vendor was rarely seen globally",
                        "detection_timestamp": 1784823177808,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "d5075c351c694d029cbc99ffe8492beb",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "actor_causality_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "actor_process_causality_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "actor_process_command_line": "C:\\Windows\\syswow64\\MsiExec.exe -Embedding 6B25AC670036AD6BD881241283C9C29A",
                                "actor_process_image_md5": "71d92e7cbed867effa8029a9997de31f",
                                "actor_process_image_name": "msiexec.exe",
                                "actor_process_image_path": "C:\\Windows\\SysWOW64\\msiexec.exe",
                                "actor_process_image_sha256": "9ad651a90a9e14e33f55df39971ddd8553ed87603548b1821bcaec081eb770ea",
                                "actor_process_instance_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "actor_process_os_pid": 22336,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 13780,
                                "agent_host_boot_time": 1784579655433,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "causality_actor_process_command_line": "C:\\Windows\\syswow64\\MsiExec.exe -Embedding 6B25AC670036AD6BD881241283C9C29A",
                                "causality_actor_process_execution_time": 1784822929507,
                                "causality_actor_process_image_md5": "71d92e7cbed867effa8029a9997de31f",
                                "causality_actor_process_image_name": "msiexec.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\SysWOW64\\msiexec.exe",
                                "causality_actor_process_image_sha256": "9ad651a90a9e14e33f55df39971ddd8553ed87603548b1821bcaec081eb770ea",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "cloud_provider": "others",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn4/A81lWDZziACYMig==",
                                "event_sub_type": 1,
                                "event_timestamp": 1784823177808,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "os_actor_process_command_line": "C:\\Windows\\syswow64\\MsiExec.exe -Embedding 6B25AC670036AD6BD881241283C9C29A",
                                "os_actor_process_image_name": "msiexec.exe",
                                "os_actor_process_image_path": "C:\\Windows\\SysWOW64\\msiexec.exe",
                                "os_actor_process_image_sha256": "9ad651a90a9e14e33f55df39971ddd8553ed87603548b1821bcaec081eb770ea",
                                "os_actor_process_instance_id": "Ad0avYw6P0IAAFdAAAAAAA==",
                                "os_actor_process_os_pid": 22336,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 13780,
                                "user_name": "TECHNOMA\\alfredopizzuti"
                            }
                        ],
                        "external_id": "2267ea9f-d67b-4c15-b40a-4b6f72338b98",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.50"
                        ],
                        "host_name": "NB-ALPIZZUTI",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1784823250994,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "3c2645a1-40cd-4c93-8cfe-ae37551b3036",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0002 - Execution",
                            "TA0003 - Persistence",
                            "TA0005 - Defense Evasion",
                            "TA0004 - Privilege Escalation",
                            "TA0005 - Stealth"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1574.001 - Hijack Execution Flow: DLL"
                        ],
                        "name": "A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "DT:DLL Hijacking Analytics"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:DLL Hijacking Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "024921da-7958-459c-a123-ec4efb33fb06"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "C:\\Windows\\syswow64\\MsiExec.exe -Embedding 6B25AC670036AD6BD881241283C9C29A",
                                "executable": "C:\\Windows\\SysWOW64\\msiexec.exe",
                                "hash": {
                                    "md5": "71d92e7cbed867effa8029a9997de31f",
                                    "sha256": "9ad651a90a9e14e33f55df39971ddd8553ed87603548b1821bcaec081eb770ea"
                                },
                                "name": "msiexec.exe",
                                "pid": 22336
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 92722,
                        "status": "New"
                    },
                    "stellar_da_input": 6095,
                    "stellar_index_id": "aella-ser-2026.07.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "454e30d5-3bd9-4040-bdfc-d8ab9401e0dd1784823733226-YWVsbGEtc2VyLTIwMjYuMDcuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784823177808,
                    "timestamp_utc": "2026-07-23T16:12:57.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\alfredopizzuti"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1784823733226,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"a rare dll, signed by a rarely seen vendor, was hijacked into a microsoft process\" on host \"NB-ALPIZZUTI\" (\"192.168.169.50\"). The behavioral analytics system identified this \"persistence\" threat through rule \"3c2645a1-40cd-4c93-8cfe-ae37551b3036\" with status \"matched\".. Analytics details: \"The process msiexec.exe loaded the DLL \"MSI6D3B.tmp\" on host NB-ALPIZZUTI. This DLL name is signed by OOO Nanosoft Razrabotka, which was seen on 1 other hosts in the last 30 days. In the last 30 days, the DLL's hash 2ae299f5681310b5b75f5f2b59130328382398333ff54ded4ee949f08150988c was seen on 0 other hosts. Both DLL hash and signature vendor are rare, which might indicate an attacker performing DLL Hijacking. The DLL signature vendor was rarely seen globally\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-a_rare_dll_signed_by_a_rarely_seen_vendor_was_hijacked_into_a_microsoft_process",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1574",
                            "name": "Hijack Execution Flow",
                            "subtechnique": {
                                "id": "T1574.001",
                                "name": "DLL Search Order Hijacking"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0003",
                                    "name": "Persistence"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1574",
                                    "name": "Hijack Execution Flow",
                                    "subtechnique": {
                                        "id": "T1574.001",
                                        "name": "DLL Search Order Hijacking"
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