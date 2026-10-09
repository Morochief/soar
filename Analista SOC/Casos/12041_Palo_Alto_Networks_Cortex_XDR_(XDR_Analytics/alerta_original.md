=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "b95a51f2-db2a-4dcd-8cb8-ad3db9386e2a1783824916355-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9699,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Ljs-VJ8BI3UnQyDO2HRH",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128827"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "An unsigned process performed an uncommon service deactivation"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.27",
                        "name": "NB-ABOGADO"
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
                    "orig_id": "Ljs-VJ8BI3UnQyDO2HRH",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a407:836d:d6d:5a3c:56d6:affd",
                            "2803:7d80:a407:836d:9f8d:92b7:3f21:e5b0"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128827",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Impact",
                        "deduplicate_tokens": null,
                        "description": "A service was disabled on the host NB-ABOGADO. The process instsrv.exe disabled the service Nginx1",
                        "detection_timestamp": 1783824336511,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "db65ee7516a94bb6ab821136ab2ed385",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "action_registry_data": "4",
                                "action_registry_key_name": "HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Services\\Nginx1",
                                "action_registry_value_name": "Start",
                                "actor_causality_id": "Ad0RfsYSkHEAAIQ8AAAAAA==",
                                "actor_process_causality_id": "Ad0RfsYSkHEAAIQ8AAAAAA==",
                                "actor_process_command_line": "instsrv  Nginx1 remove",
                                "actor_process_image_md5": "9f7acaad365af0d1a3cd9261e3208b9b",
                                "actor_process_image_name": "instsrv.exe",
                                "actor_process_image_path": "C:\\Program Files (x86)\\HikCentral\\VSM Servers\\Web Service\\Nginx1\\instsrv.exe",
                                "actor_process_image_sha256": "f7b0a444b590eb8a6b46cedf544bcb3117c85cab02b599b45d61b8a590095c9c",
                                "actor_process_instance_id": "Ad0RqJ6bP7cAAHEQAAAAAA==",
                                "actor_process_os_pid": 28944,
                                "actor_process_signature_status": "Unsigned",
                                "actor_thread_thread_id": 28948,
                                "agent_host_boot_time": 1782501466212,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0RfsYSkHEAAIQ8AAAAAA==",
                                "causality_actor_process_command_line": "sihost.exe",
                                "causality_actor_process_execution_time": 1783806408002,
                                "causality_actor_process_image_md5": "af9ba4aa79ba3cdd28236a06d05b70d4",
                                "causality_actor_process_image_name": "sihost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\sihost.exe",
                                "causality_actor_process_image_sha256": "6e271366388fbc5a1e2e5204e7cf98557b44db2e9e34e1b6a7c8e7b80e14caab",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1Q38jrFT1x9ABnCYQ==",
                                "event_sub_type": 4,
                                "event_timestamp": 1783824336511,
                                "event_type": "Registry Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0FoHvTrcMAAARYAAAAAA==",
                                "os_actor_process_command_line": "C:\\Windows\\system32\\services.exe",
                                "os_actor_process_image_name": "services.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\services.exe",
                                "os_actor_process_image_sha256": "3a2f7f00b24ae7291e2a9557e9b16be4c6846b725a26acad5ed65db951d64508",
                                "os_actor_process_instance_id": "Ad0FoHvTrcMAAARYAAAAAA==",
                                "os_actor_process_os_pid": 1112,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 6620,
                                "user_name": "NT AUTHORITY\\SYSTEM"
                            }
                        ],
                        "external_id": "56f75047-70aa-4f4c-8e6c-d1b43590084c",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.27"
                        ],
                        "host_name": "NB-ABOGADO",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783824359157,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "9d96de8e-036e-414d-baac-064aef4271bc",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0040 - Impact"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1489 - Service Stop"
                        ],
                        "name": "An unsigned process performed an uncommon service deactivation",
                        "original_tags": [
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
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
                        "variation_rule_id": "d18b1420-e339-4a01-b15c-4b48f7adbe48"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "instsrv  Nginx1 remove",
                                "executable": "C:\\Program Files (x86)\\HikCentral\\VSM Servers\\Web Service\\Nginx1\\instsrv.exe",
                                "hash": {
                                    "md5": "9f7acaad365af0d1a3cd9261e3208b9b",
                                    "sha256": "f7b0a444b590eb8a6b46cedf544bcb3117c85cab02b599b45d61b8a590095c9c"
                                },
                                "name": "instsrv.exe",
                                "pid": 28944
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 84660,
                        "status": "New"
                    },
                    "stellar_da_input": 5513,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b95a51f2-db2a-4dcd-8cb8-ad3db9386e2a1783824916355-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783824336511,
                    "timestamp_utc": "2026-07-12T02:45:36.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\SYSTEM"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783824916355,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"an unsigned process performed an uncommon service deactivation\" on host \"NB-ABOGADO\" (\"192.168.100.27\"). The behavioral analytics system identified this \"impact\" threat through rule \"9d96de8e-036e-414d-baac-064aef4271bc\" with status \"matched\".. Analytics details: \"A service was disabled on the host NB-ABOGADO. The process instsrv.exe disabled the service Nginx1\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): An unsigned process performed an uncommon service deactivation",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-an_unsigned_process_performed_an_uncommon_service_deactivation",
                        "scope": "",
                        "tactic": {
                            "id": "TA0040",
                            "name": "Impact"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1489",
                            "name": "Service Stop"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0040",
                                    "name": "Impact"
                                },
                                "technique": {
                                    "id": "T1489",
                                    "name": "Service Stop"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "67856015-a639-4c2b-89d5-42db357df16c1783824916347-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9698,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "LTs-VJ8BI3UnQyDO2HRH",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128830"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.27",
                        "name": "NB-ABOGADO"
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
                    "orig_id": "LTs-VJ8BI3UnQyDO2HRH",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a407:836d:9f8d:92b7:3f21:e5b0",
                            "2803:7d80:a407:836d:807a:8890:33f4:b65b"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128830",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "The process Launcher.exe was executed within 34 seconds from boot by the Causality Group Owner (CGO):EpicGamesLauncher.exe. The execution chain may indicate on a possible persistence mechanism on boot. This behavior was seen on 0 hosts and 0 unique days in the last 30 days",
                        "detection_timestamp": 1783824515820,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "db65ee7516a94bb6ab821136ab2ed385",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "action_process_image_command_line": "\"C:/Users/axelbogado/Desktop/HITMAN3/Launcher.exe\"  -AUTH_LOGIN=unused -AUTH_PASSWORD=45aa2630287243ffb703d1aa0af87151 -AUTH_TYPE=exchangecode -epicapp=Eider -epicenv=Prod -EpicPortal -epicusername=\"RonaldoAguero\" -epicuserid=5b7883e7d72446ba845a4f518a5e0018 -epiclocale=es-ES -epicsandboxid=ed55aa5edc5941de92fd7f64de415793",
                                "action_process_image_name": "Launcher.exe",
                                "action_process_image_sha256": "c5ddcc0d4c8573dba283e53bac86a7a2b11c49be44587fda1932ce2bd67f6712",
                                "action_process_instance_id": "Ad0RqQkTMc4AAD6gAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "IO INTERACTIVE A/S",
                                "actor_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "actor_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "actor_process_command_line": "\"C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe\" \"C:/HITM/Launcher/Portal/Binaries/Win64/EpicGamesLauncher.exe\"  -forwarduri -silent -AllowSoftwareRendering -SaveToUserDir -Messaging -enablehighdpi -EOSBootstrappedFlag -ForcedRestart",
                                "actor_process_image_md5": "738a2024fb578c0b1d8a4fab71ce69c6",
                                "actor_process_image_name": "EpicGamesLauncher.exe",
                                "actor_process_image_path": "C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe",
                                "actor_process_image_sha256": "066a2bdd57d6165a5d6510627fc0b589cb5d117a716b508e1ebd7fc0e57c65f3",
                                "actor_process_instance_id": "Ad0RqP7sGxYAAC9QAAAAAA==",
                                "actor_process_os_pid": 12112,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Epic Games Inc.",
                                "actor_thread_thread_id": 12060,
                                "agent_host_boot_time": 1783824481772,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe\" com.epicgames.launcher://apps/ed55aa5edc5941de92fd7f64de415793%3A7d9ce7dd6f2e4ee98a55bd50a9bb78e0%3AEider?action=launch&silent=true",
                                "causality_actor_process_execution_time": 1783824537897,
                                "causality_actor_process_image_md5": "738a2024fb578c0b1d8a4fab71ce69c6",
                                "causality_actor_process_image_name": "EpicGamesLauncher.exe",
                                "causality_actor_process_image_path": "C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe",
                                "causality_actor_process_image_sha256": "066a2bdd57d6165a5d6510627fc0b589cb5d117a716b508e1ebd7fc0e57c65f3",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Epic Games Inc.",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1Q6rD3FT1x9AABWKA==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783824515820,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "os_actor_process_command_line": "\"C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe\" \"C:/HITM/Launcher/Portal/Binaries/Win64/EpicGamesLauncher.exe\"  -forwarduri -silent -AllowSoftwareRendering -SaveToUserDir -Messaging -enablehighdpi -EOSBootstrappedFlag -ForcedRestart",
                                "os_actor_process_image_name": "EpicGamesLauncher.exe",
                                "os_actor_process_image_path": "C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe",
                                "os_actor_process_image_sha256": "066a2bdd57d6165a5d6510627fc0b589cb5d117a716b508e1ebd7fc0e57c65f3",
                                "os_actor_process_instance_id": "Ad0RqP7sGxYAAC9QAAAAAA==",
                                "os_actor_process_os_pid": 12112,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Epic Games Inc.",
                                "os_actor_thread_thread_id": 12060,
                                "user_name": "TECHNOMA\\axelbogado"
                            }
                        ],
                        "external_id": "76f77ec4-a4f2-4667-9bb4-28c3baa1db5a",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.27"
                        ],
                        "host_name": "NB-ABOGADO",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783824730804,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "d5ccf589-5f6c-4f8d-bfcd-47cd23bb8152",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0004 - Privilege Escalation",
                            "TA0003 - Persistence"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1547 - Boot or Logon Autostart Execution"
                        ],
                        "name": "Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics",
                        "original_tags": [
                            "DT:Generic Persistence Analytics",
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:Generic Persistence Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "2c8f318d-e570-4d2a-94bf-2bd75f0e5fb4"
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "c5ddcc0d4c8573dba283e53bac86a7a2b11c49be44587fda1932ce2bd67f6712"
                            },
                            "name": "Launcher.exe",
                            "parent": {
                                "command_line": "\"C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe\" \"C:/HITM/Launcher/Portal/Binaries/Win64/EpicGamesLauncher.exe\"  -forwarduri -silent -AllowSoftwareRendering -SaveToUserDir -Messaging -enablehighdpi -EOSBootstrappedFlag -ForcedRestart",
                                "executable": "C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe",
                                "hash": {
                                    "md5": "738a2024fb578c0b1d8a4fab71ce69c6",
                                    "sha256": "066a2bdd57d6165a5d6510627fc0b589cb5d117a716b508e1ebd7fc0e57c65f3"
                                },
                                "name": "EpicGamesLauncher.exe",
                                "pid": 12112
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 84652,
                        "status": "New"
                    },
                    "stellar_da_input": 7578,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "67856015-a639-4c2b-89d5-42db357df16c1783824916347-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783824515820,
                    "timestamp_utc": "2026-07-12T02:48:35.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\axelbogado"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783824916347,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"execution of an uncommon process with a local/domain user sid at an early startup stage with uncommon characteristics\" on host \"NB-ABOGADO\" (\"192.168.100.27\"). The behavioral analytics system identified this \"persistence\" threat through rule \"d5ccf589-5f6c-4f8d-bfcd-47cd23bb8152\" with status \"matched\". The suspicious behavior involved \"Launcher.exe\" executed by user \"TECHNOMA\\axelbogado\". Analytics details: \"The process Launcher.exe was executed within 34 seconds from boot by the Causality Group Owner (CGO):EpicGamesLauncher.exe. The execution chain may indicate on a possible persistence mechanism on boot. This behavior was seen on 0 hosts and 0 unique days in the last 30 days\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-execution_of_an_uncommon_process_with_a_local_domain_user_sid_at_an_early_startup_stage_with_uncommon_characteristics",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "8b2f3e0d-1e47-4650-8d3f-8c09e1cf0a311783825273717-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9700,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "NztDVJ8BI3UnQyDOY5JA",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128829"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.27",
                        "name": "NB-ABOGADO"
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
                    "orig_id": "NztDVJ8BI3UnQyDOY5JA",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a407:836d:9f8d:92b7:3f21:e5b0",
                            "2803:7d80:a407:836d:807a:8890:33f4:b65b"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128829",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "The process HITMAN3.exe was executed within 43 seconds from boot by the Causality Group Owner (CGO):EpicGamesLauncher.exe. The execution chain may indicate on a possible persistence mechanism on boot. This behavior was seen on 0 hosts and 0 unique days in the last 30 days",
                        "detection_timestamp": 1783824524890,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "db65ee7516a94bb6ab821136ab2ed385",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "action_process_image_command_line": "\"retail\\hitman3.exe\" -AUTH_LOGIN=unused -AUTH_PASSWORD=45aa2630287243ffb703d1aa0af87151 -AUTH_TYPE=exchangecode -epicapp=Eider -epicenv=Prod -EpicPortal -epicusername=\"RonaldoAguero\" -epicuserid=5b7883e7d72446ba845a4f518a5e0018 -epiclocale=es-ES -epicsandboxid=ed55aa5edc5941de92fd7f64de415793",
                                "action_process_image_name": "HITMAN3.exe",
                                "action_process_image_sha256": "189a289d8093abea7cb378d04eccd72518918105f00866777cd3144e8e1292fd",
                                "action_process_instance_id": "Ad0RqQ6hWVYAAB3UAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "IO INTERACTIVE A/S",
                                "actor_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "actor_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "actor_process_command_line": "\"C:/Users/axelbogado/Desktop/HITMAN3/Launcher.exe\"  -AUTH_LOGIN=unused -AUTH_PASSWORD=45aa2630287243ffb703d1aa0af87151 -AUTH_TYPE=exchangecode -epicapp=Eider -epicenv=Prod -EpicPortal -epicusername=\"RonaldoAguero\" -epicuserid=5b7883e7d72446ba845a4f518a5e0018 -epiclocale=es-ES -epicsandboxid=ed55aa5edc5941de92fd7f64de415793",
                                "actor_process_image_md5": "a083c667887733886856ddd3b892f5c7",
                                "actor_process_image_name": "Launcher.exe",
                                "actor_process_image_path": "C:\\Users\\axelbogado\\Desktop\\HITMAN3\\Launcher.exe",
                                "actor_process_image_sha256": "c5ddcc0d4c8573dba283e53bac86a7a2b11c49be44587fda1932ce2bd67f6712",
                                "actor_process_instance_id": "Ad0RqQkTMc4AAD6gAAAAAA==",
                                "actor_process_os_pid": 16032,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "IO INTERACTIVE A/S",
                                "actor_thread_thread_id": 16040,
                                "agent_host_boot_time": 1783824481772,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe\" com.epicgames.launcher://apps/ed55aa5edc5941de92fd7f64de415793%3A7d9ce7dd6f2e4ee98a55bd50a9bb78e0%3AEider?action=launch&silent=true",
                                "causality_actor_process_execution_time": 1783824537897,
                                "causality_actor_process_image_md5": "738a2024fb578c0b1d8a4fab71ce69c6",
                                "causality_actor_process_image_name": "EpicGamesLauncher.exe",
                                "causality_actor_process_image_path": "C:\\HITM\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe",
                                "causality_actor_process_image_sha256": "066a2bdd57d6165a5d6510627fc0b589cb5d117a716b508e1ebd7fc0e57c65f3",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Epic Games Inc.",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1Q60C3FT1x9AABicw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783824524890,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0RqPx4j2YAADF4AAAAAA==",
                                "os_actor_process_command_line": "\"C:/Users/axelbogado/Desktop/HITMAN3/Launcher.exe\"  -AUTH_LOGIN=unused -AUTH_PASSWORD=45aa2630287243ffb703d1aa0af87151 -AUTH_TYPE=exchangecode -epicapp=Eider -epicenv=Prod -EpicPortal -epicusername=\"RonaldoAguero\" -epicuserid=5b7883e7d72446ba845a4f518a5e0018 -epiclocale=es-ES -epicsandboxid=ed55aa5edc5941de92fd7f64de415793",
                                "os_actor_process_image_name": "Launcher.exe",
                                "os_actor_process_image_path": "C:\\Users\\axelbogado\\Desktop\\HITMAN3\\Launcher.exe",
                                "os_actor_process_image_sha256": "c5ddcc0d4c8573dba283e53bac86a7a2b11c49be44587fda1932ce2bd67f6712",
                                "os_actor_process_instance_id": "Ad0RqQkTMc4AAD6gAAAAAA==",
                                "os_actor_process_os_pid": 16032,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "IO INTERACTIVE A/S",
                                "os_actor_thread_thread_id": 16040,
                                "user_name": "TECHNOMA\\axelbogado"
                            }
                        ],
                        "external_id": "97f8f94a-5af4-41bd-bda7-5e59397703fb",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.27"
                        ],
                        "host_name": "NB-ABOGADO",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783824730438,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "d5ccf589-5f6c-4f8d-bfcd-47cd23bb8152",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0004 - Privilege Escalation",
                            "TA0003 - Persistence"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1547 - Boot or Logon Autostart Execution"
                        ],
                        "name": "Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics",
                        "original_tags": [
                            "DOM:Security",
                            "DS:PANW/XDR Agent",
                            "DT:Generic Persistence Analytics"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:Generic Persistence Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "2c8f318d-e570-4d2a-94bf-2bd75f0e5fb4"
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "189a289d8093abea7cb378d04eccd72518918105f00866777cd3144e8e1292fd"
                            },
                            "name": "HITMAN3.exe",
                            "parent": {
                                "command_line": "\"C:/Users/axelbogado/Desktop/HITMAN3/Launcher.exe\"  -AUTH_LOGIN=unused -AUTH_PASSWORD=45aa2630287243ffb703d1aa0af87151 -AUTH_TYPE=exchangecode -epicapp=Eider -epicenv=Prod -EpicPortal -epicusername=\"RonaldoAguero\" -epicuserid=5b7883e7d72446ba845a4f518a5e0018 -epiclocale=es-ES -epicsandboxid=ed55aa5edc5941de92fd7f64de415793",
                                "executable": "C:\\Users\\axelbogado\\Desktop\\HITMAN3\\Launcher.exe",
                                "hash": {
                                    "md5": "a083c667887733886856ddd3b892f5c7",
                                    "sha256": "c5ddcc0d4c8573dba283e53bac86a7a2b11c49be44587fda1932ce2bd67f6712"
                                },
                                "name": "Launcher.exe",
                                "pid": 16032
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 143540,
                        "status": "New"
                    },
                    "stellar_da_input": 7698,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8b2f3e0d-1e47-4650-8d3f-8c09e1cf0a311783825273717-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783824524890,
                    "timestamp_utc": "2026-07-12T02:48:44.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\axelbogado"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783825273716,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"execution of an uncommon process with a local/domain user sid at an early startup stage with uncommon characteristics\" on host \"NB-ABOGADO\" (\"192.168.100.27\"). The behavioral analytics system identified this \"persistence\" threat through rule \"d5ccf589-5f6c-4f8d-bfcd-47cd23bb8152\" with status \"matched\". The suspicious behavior involved \"HITMAN3.exe\" executed by user \"TECHNOMA\\axelbogado\". Analytics details: \"The process HITMAN3.exe was executed within 43 seconds from boot by the Causality Group Owner (CGO):EpicGamesLauncher.exe. The execution chain may indicate on a possible persistence mechanism on boot. This behavior was seen on 0 hosts and 0 unique days in the last 30 days\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Execution of an uncommon process with a local/domain user SID at an early startup stage with uncommon characteristics",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-execution_of_an_uncommon_process_with_a_local_domain_user_sid_at_an_early_startup_stage_with_uncommon_characteristics",
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
            }
        ]
    }
}