=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6733c8d4-5c70-4b5a-be84-bad755a8c4551783885309096-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9743,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "ulTXV58BI3UnQyDOOLJL",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128857"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "LOLBIN process executed with a high integrity level"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.70",
                        "name": "NB-EFRETES"
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
                    "orig_id": "ulTXV58BI3UnQyDOOLJL",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a40d:7030:b917:9a78:6822:bb95",
                            "2803:7d80:a40d:7030:98ca:9292:6ffa:3bc7"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128857",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Privilege Escalation",
                        "deduplicate_tokens": null,
                        "description": "The process rustdesk.exe executed a LOLBIN process cmd.exe with a higher integrity level. Process command line: \"C:\\Windows\\System32\\cmd.exe\"  /C C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\RustDesk_uninstall.bat. This behavior has not been observed in the last 30 days",
                        "detection_timestamp": 1783884708260,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "9a3386de89474922b290037b25009a7d",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0SM9VwFcIAADWEAAAAAA==",
                                "action_process_image_command_line": "\"C:\\Windows\\System32\\cmd.exe\"  /C C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\RustDesk_uninstall.bat",
                                "action_process_image_name": "cmd.exe",
                                "action_process_image_sha256": "75320a519959cc6d089ea3eba33c38caccb7f138a025ea439bc9686cdb79ded4",
                                "action_process_instance_id": "Ad0SNUMzTo4AADfoAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0SM9VwFcIAADWEAAAAAA==",
                                "actor_process_causality_id": "Ad0SM9VwFcIAADWEAAAAAA==",
                                "actor_process_command_line": "\"C:\\Program Files\\RustDesk\\rustdesk.exe\" --tray",
                                "actor_process_image_md5": "67c6517649180470bd162656542a7c9c",
                                "actor_process_image_name": "rustdesk.exe",
                                "actor_process_image_path": "C:\\Program Files\\RustDesk\\rustdesk.exe",
                                "actor_process_image_sha256": "3ccd9d5e1f14d1013d12e79c8426a07cc057510fe6d6676309771f03db2bfbdd",
                                "actor_process_instance_id": "Ad0SM9VwFcIAADWEAAAAAA==",
                                "actor_process_os_pid": 13700,
                                "actor_process_signature_status": "Invalid Signature",
                                "actor_process_signature_vendor": "PURSLANE",
                                "agent_host_boot_time": 1783877236746,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0SM9VwFcIAADWEAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Program Files\\RustDesk\\rustdesk.exe\" --tray",
                                "causality_actor_process_execution_time": 1783884172478,
                                "causality_actor_process_image_md5": "67c6517649180470bd162656542a7c9c",
                                "causality_actor_process_image_name": "rustdesk.exe",
                                "causality_actor_process_image_path": "C:\\Program Files\\RustDesk\\rustdesk.exe",
                                "causality_actor_process_image_sha256": "3ccd9d5e1f14d1013d12e79c8426a07cc057510fe6d6676309771f03db2bfbdd",
                                "causality_actor_process_signature_status": "Invalid Signature",
                                "causality_actor_process_signature_vendor": "PURSLANE",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1fRqhD183DHAATv9A==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783884708260,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0SI8BhRHMAACckAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Appinfo",
                                "os_actor_process_image_name": "svchost.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "os_actor_process_image_sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4",
                                "os_actor_process_instance_id": "Ad0SI8BhRHMAACckAAAAAA==",
                                "os_actor_process_os_pid": 10020,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 9792,
                                "user_name": "TECHNOMA\\elvisfretes"
                            }
                        ],
                        "external_id": "8e0f976c-194f-4e39-a960-eafa51eed4ea",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.70"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783884968696,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "365221fa-4c36-440f-824a-43885e9f3a6e",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0004 - Privilege Escalation",
                            "TA0005 - Defense Evasion"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1548 - Abuse Elevation Control Mechanism"
                        ],
                        "name": "LOLBIN process executed with a high integrity level",
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
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "75320a519959cc6d089ea3eba33c38caccb7f138a025ea439bc9686cdb79ded4"
                            },
                            "name": "cmd.exe",
                            "parent": {
                                "command_line": "\"C:\\Program Files\\RustDesk\\rustdesk.exe\" --tray",
                                "executable": "C:\\Program Files\\RustDesk\\rustdesk.exe",
                                "hash": {
                                    "md5": "67c6517649180470bd162656542a7c9c",
                                    "sha256": "3ccd9d5e1f14d1013d12e79c8426a07cc057510fe6d6676309771f03db2bfbdd"
                                },
                                "name": "rustdesk.exe",
                                "pid": 13700
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 158895,
                        "status": "New"
                    },
                    "stellar_da_input": 6200,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6733c8d4-5c70-4b5a-be84-bad755a8c4551783885309096-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783884708260,
                    "timestamp_utc": "2026-07-12T19:31:48.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\elvisfretes"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783885309096,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"lolbin process executed with a high integrity level\" on host \"NB-EFRETES\" (\"192.168.100.70\"). The behavioral analytics system identified this \"privilege escalation\" threat through rule \"365221fa-4c36-440f-824a-43885e9f3a6e\" with status \"matched\". The suspicious behavior involved \"cmd.exe\" executed by user \"TECHNOMA\\elvisfretes\". Analytics details: \"The process rustdesk.exe executed a LOLBIN process cmd.exe with a higher integrity level. Process command line: \"C:\\Windows\\System32\\cmd.exe\"  /C C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\RustDesk_uninstall.bat. This behavior has not been observed in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): LOLBIN process executed with a high integrity level",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-lolbin_process_executed_with_a_high_integrity_level",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1548",
                            "name": "Abuse Elevation Control Mechanism"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1548",
                                    "name": "Abuse Elevation Control Mechanism"
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1548",
                                    "name": "Abuse Elevation Control Mechanism"
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
                "_id": "61cead52-8d11-417b-97f9-db08303ba4331783885547353-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9744,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "192.168.100.70.54.64.167.132.80.null",
                    "anomaly_id": "LFTbV58BI3UnQyDOy9fB",
                    "appid_name": "http",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128860"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "dstip": "54.64.167.132",
                    "dstip_asn": 16509,
                    "dstip_asn_org": "Amazon.com, Inc.",
                    "dstip_geo": {
                        "city": "Tokyo",
                        "countryCode": "JP",
                        "countryName": "Japan",
                        "latitude": 35.6893,
                        "longitude": 139.6899,
                        "region": "Tokyo"
                    },
                    "dstip_geo_point": "35.6893,139.6899",
                    "dstip_host": "54.64.167.132",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstport": 80,
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Abnormal network communication with a rare combination of HTTP User Agent and HTTP Server where both the User Agent and the HTTP Server are rare"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.70",
                        "name": "NB-EFRETES"
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
                    "orig_id": "LFTbV58BI3UnQyDOy9fB",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a40d:7030:b917:9a78:6822:bb95",
                            "2803:7d80:a40d:7030:98ca:9292:6ffa:3bc7"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128860",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Command and Control",
                        "deduplicate_tokens": null,
                        "description": "An uncommon combination of HTTP User Agent and HTTP Server were detected during a session to go.epson.com. The uncommon User Agent header pattern: Install Navi. The rarity of both the User Agent and the HTTP Server elevates the suspicion level of the session",
                        "detection_timestamp": 1783885115697,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "9a3386de89474922b290037b25009a7d",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_external_hostname": "go.epson.com",
                                "action_local_ip": "192.168.100.70",
                                "action_local_port": 65054,
                                "action_process_signature_status": "N/A",
                                "action_remote_ip": "54.64.167.132",
                                "action_remote_port": 80,
                                "actor_causality_id": "Ad0SNhf8H2oAACacAAAAAA==",
                                "actor_process_causality_id": "Ad0SNhf8H2oAACacAAAAAA==",
                                "actor_process_command_line": "\"C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe\" ",
                                "actor_process_image_md5": "ff58c6b4d03dc49bde0692a6a2b05f1e",
                                "actor_process_image_name": "EpsonInstaller.exe",
                                "actor_process_image_path": "C:\\Users\\elvisfretes\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe",
                                "actor_process_image_sha256": "7ce732021021a450abc81cb60bcf0b1d0d3e1927f17bd591b5a89784eb52412b",
                                "actor_process_instance_id": "Ad0SNjG/ob4AACqAAAAAAA==",
                                "actor_process_os_pid": 10880,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "SEIKO EPSON CORPORATION",
                                "actor_thread_thread_id": 14812,
                                "agent_host_boot_time": 1783877236746,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0SNhf8H2oAACacAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\elvisfretes\\Downloads\\L3210_Lite_LA.exe\" ",
                                "causality_actor_process_execution_time": 1783885144030,
                                "causality_actor_process_image_md5": "380ccc7ce34739430cf851b360984f40",
                                "causality_actor_process_image_name": "L3210_Lite_LA.exe",
                                "causality_actor_process_image_path": "C:\\Users\\elvisfretes\\Downloads\\L3210_Lite_LA.exe",
                                "causality_actor_process_image_sha256": "20915060e0742a44d8fb89a4250a014c022b81bb30149c5f38fc140fab0a0a5d",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "SEIKO EPSON CORPORATION",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "dst_action_country": "JP",
                                "dst_action_external_hostname": "go.epson.com",
                                "dst_agent_id": "54.64.167.132",
                                "dst_association_strength": 10,
                                "event_id": "NTcyNjk0NDU1NTAwODEyNDQ3MA==",
                                "event_sub_type": 5,
                                "event_timestamp": 1783885115697,
                                "event_type": "Network Connections",
                                "fw_app_id": "ip,tcp,web-browsing",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0SNhf8H2oAACacAAAAAA==",
                                "os_actor_process_command_line": "\"C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe\" ",
                                "os_actor_process_image_name": "EpsonInstaller.exe",
                                "os_actor_process_image_path": "C:\\Users\\elvisfretes\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe",
                                "os_actor_process_image_sha256": "7ce732021021a450abc81cb60bcf0b1d0d3e1927f17bd591b5a89784eb52412b",
                                "os_actor_process_instance_id": "Ad0SNjG/ob4AACqAAAAAAA==",
                                "os_actor_process_os_pid": 10880,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "SEIKO EPSON CORPORATION",
                                "os_actor_thread_thread_id": 14812,
                                "story_id": "NTcyNjk0NDU1NTAwODEyNDQ3MA==",
                                "user_name": "TECHNOMA\\elvisfretes"
                            }
                        ],
                        "external_id": "b2212ea9-ec99-4b82-81f8-89b51bf48d2e",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.70"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783885414312,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "c13fd72e-8225-4e0c-a2fd-7ffefe159535",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0011 - Command and Control",
                            "TA0010 - Exfiltration"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1102 - Web Service",
                            "T1567 - Exfiltration Over Web Service"
                        ],
                        "name": "Abnormal network communication with a rare combination of HTTP User Agent and HTTP Server where both the User Agent and the HTTP Server are rare",
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
                        "variation_rule_id": "a8037308-5aad-404d-b428-39832fcfb4dd"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "\"C:\\Users\\ELVISF~1\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe\" ",
                                "executable": "C:\\Users\\elvisfretes\\AppData\\Local\\Temp\\L3210_Series_(LA)\\Installer\\EpsonInstaller.exe",
                                "hash": {
                                    "md5": "ff58c6b4d03dc49bde0692a6a2b05f1e",
                                    "sha256": "7ce732021021a450abc81cb60bcf0b1d0d3e1927f17bd591b5a89784eb52412b"
                                },
                                "name": "EpsonInstaller.exe",
                                "pid": 10880
                            }
                        }
                    ],
                    "severity": 35,
                    "src_tuples": "null.0.192.168.100.70",
                    "srcip": "192.168.100.70",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "192.168.100.70",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 65054,
                    "stellar": {
                        "detection_time": 97199,
                        "status": "New"
                    },
                    "stellar_da_input": 6708,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "61cead52-8d11-417b-97f9-db08303ba4331783885547353-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783885115697,
                    "timestamp_utc": "2026-07-12T19:38:35.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\elvisfretes"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783885547353,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"abnormal network communication with a rare combination of http user agent and http server where both the user agent and the http server are rare\" on host \"NB-EFRETES\" (\"192.168.100.70\"). The behavioral analytics system identified this \"command and control\" threat through rule \"c13fd72e-8225-4e0c-a2fd-7ffefe159535\" with status \"matched\".. Analytics details: \"An uncommon combination of HTTP User Agent and HTTP Server were detected during a session to go.epson.com. The uncommon User Agent header pattern: Install Navi. The rarity of both the User Agent and the HTTP Server elevates the suspicion level of the session\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Abnormal network communication with a rare combination of HTTP User Agent and HTTP Server where both the User Agent and the HTTP Server are rare",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-abnormal_network_communication_with_a_rare_combination_of_http_user_agent_and_http_server_where_both_the_user_agent_and_the_http_server_are_rare",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1567",
                            "name": "Exfiltration Over Web Service"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0010",
                                    "name": "Exfiltration"
                                },
                                "technique": {
                                    "id": "T1567",
                                    "name": "Exfiltration Over Web Service"
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0011",
                                    "name": "Command and Control"
                                },
                                "technique": {
                                    "id": "T1102",
                                    "name": "Web Service"
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
                "_id": "f98f75b4-11a9-44d5-adb8-83cc15c912831783886500347-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9746,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "lFXpV58BI3UnQyDOrj97",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128869"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Svchost.exe loads a rare unsigned module"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.70",
                        "name": "NB-EFRETES"
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
                    "orig_id": "lFXpV58BI3UnQyDOrj97",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a40d:7030:b917:9a78:6822:bb95",
                            "2803:7d80:a40d:7030:98ca:9292:6ffa:3bc7"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128869",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Defense Evasion",
                        "deduplicate_tokens": null,
                        "description": "The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPOJ7740_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is de81d7c4e9bf664ca1112cc7b3f456ea91c72868afd1d0f97b44c67529f1aa6e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 0 hosts and 0 unique days in the last 30 days",
                        "detection_timestamp": 1783885752031,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "9a3386de89474922b290037b25009a7d",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "actor_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "actor_process_image_md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                "actor_process_image_name": "svchost.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "actor_process_image_sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4",
                                "actor_process_instance_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_os_pid": 4464,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 8084,
                                "agent_host_boot_time": 1783877236746,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "causality_actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "causality_actor_process_execution_time": 1783877248252,
                                "causality_actor_process_image_md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                "causality_actor_process_image_name": "svchost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "causality_actor_process_image_sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1fhl0/183DHAAcTkw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783885752031,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0SN4hDVksAABYEAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
                                "os_actor_process_image_name": "WmiPrvSE.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                                "os_actor_process_image_sha256": "6a94d40bf022871c2c91ef67b60ccf42814447fc6090c96509a8ee94a11c5212",
                                "os_actor_process_instance_id": "Ad0SN4hDVksAABYEAAAAAA==",
                                "os_actor_process_os_pid": 5636,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 772,
                                "user_name": "NT AUTHORITY\\NETWORK SERVICE"
                            }
                        ],
                        "external_id": "914a6323-aaea-4cd8-af4c-c6fbcaf99a4d",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.70"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783885876730,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "f50c7054-8530-4f07-afe1-fe9de6a2045a",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0005 - Defense Evasion",
                            "TA0003 - Persistence",
                            "TA0004 - Privilege Escalation"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1036.004 - Masquerading: Masquerade Task or Service",
                            "T1543.003 - Create or Modify System Process: Windows Service"
                        ],
                        "name": "Svchost.exe loads a rare unsigned module",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "DT:Malicious Service Analytics"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:Malicious Service Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "executable": "C:\\Windows\\System32\\svchost.exe",
                                "hash": {
                                    "md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                    "sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4"
                                },
                                "name": "svchost.exe",
                                "pid": 4464
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 140191,
                        "status": "New"
                    },
                    "stellar_da_input": 6140,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f98f75b4-11a9-44d5-adb8-83cc15c912831783886500347-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783885752031,
                    "timestamp_utc": "2026-07-12T19:49:12.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\NETWORK SERVICE"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783886500347,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"svchost.exe loads a rare unsigned module\" on host \"NB-EFRETES\" (\"192.168.100.70\"). The behavioral analytics system identified this \"defense evasion\" threat through rule \"f50c7054-8530-4f07-afe1-fe9de6a2045a\" with status \"matched\".. Analytics details: \"The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPOJ7740_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is de81d7c4e9bf664ca1112cc7b3f456ea91c72868afd1d0f97b44c67529f1aa6e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 0 hosts and 0 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Svchost.exe loads a rare unsigned module",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-svchost_exe_loads_a_rare_unsigned_module",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1543",
                            "name": "Create or Modify System Process",
                            "subtechnique": {
                                "id": "T1543.003",
                                "name": "Windows Service"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1036",
                                    "name": "Masquerading",
                                    "subtechnique": {
                                        "id": "T1036.004",
                                        "name": "Masquerade Task or Service"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0003",
                                    "name": "Persistence"
                                },
                                "technique": {
                                    "id": "T1543",
                                    "name": "Create or Modify System Process",
                                    "subtechnique": {
                                        "id": "T1543.003",
                                        "name": "Windows Service"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1543",
                                    "name": "Create or Modify System Process",
                                    "subtechnique": {
                                        "id": "T1543.003",
                                        "name": "Windows Service"
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
                "_id": "22821074-2328-4e8e-9924-8e6c3fa9b6ee1783886500316-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9745,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "k1XpV58BI3UnQyDOrj97",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128871"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Svchost.exe loads a rare unsigned module"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.100.70",
                        "name": "NB-EFRETES"
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
                    "orig_id": "k1XpV58BI3UnQyDOrj97",
                    "orig_index": "aella-syslog-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": [
                            "2803:7d80:a40d:7030:b917:9a78:6822:bb95",
                            "2803:7d80:a40d:7030:98ca:9292:6ffa:3bc7"
                        ],
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128871",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Defense Evasion",
                        "deduplicate_tokens": null,
                        "description": "The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPLJM227_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is a83edad207b9779665dbe9597e2501eb9e5fc5da875974ab8231bceab411df8e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 0 hosts and 0 unique days in the last 30 days",
                        "detection_timestamp": 1783885752487,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "9a3386de89474922b290037b25009a7d",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "actor_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "actor_process_image_md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                "actor_process_image_name": "svchost.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "actor_process_image_sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4",
                                "actor_process_instance_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "actor_process_os_pid": 4464,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 8084,
                                "agent_host_boot_time": 1783877236746,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0SI7ZLMYcAABFwAAAAAA==",
                                "causality_actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "causality_actor_process_execution_time": 1783877248252,
                                "causality_actor_process_image_md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                "causality_actor_process_image_name": "svchost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "causality_actor_process_image_sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn1fhmRf183DHAAcTnw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783885752487,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0SN4hDVksAABYEAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
                                "os_actor_process_image_name": "WmiPrvSE.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                                "os_actor_process_image_sha256": "6a94d40bf022871c2c91ef67b60ccf42814447fc6090c96509a8ee94a11c5212",
                                "os_actor_process_instance_id": "Ad0SN4hDVksAABYEAAAAAA==",
                                "os_actor_process_os_pid": 5636,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 772,
                                "user_name": "NT AUTHORITY\\NETWORK SERVICE"
                            }
                        ],
                        "external_id": "0c69070a-ccba-42c8-81fa-3e78b74ff6ab",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.100.70"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783885878550,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "f50c7054-8530-4f07-afe1-fe9de6a2045a",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0005 - Defense Evasion",
                            "TA0003 - Persistence",
                            "TA0004 - Privilege Escalation"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1036.004 - Masquerading: Masquerade Task or Service",
                            "T1543.003 - Create or Modify System Process: Windows Service"
                        ],
                        "name": "Svchost.exe loads a rare unsigned module",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "DT:Malicious Service Analytics"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:Malicious Service Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "executable": "C:\\Windows\\System32\\svchost.exe",
                                "hash": {
                                    "md5": "b66e8cf8acf5a58e6bbb5f12fbc3e2ec",
                                    "sha256": "2178f1915f740cce64040107cd489e9e1ff828a7ea29cd706bc46ba0fbaa69c4"
                                },
                                "name": "svchost.exe",
                                "pid": 4464
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 140170,
                        "status": "New"
                    },
                    "stellar_da_input": 6140,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "22821074-2328-4e8e-9924-8e6c3fa9b6ee1783886500316-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783885752487,
                    "timestamp_utc": "2026-07-12T19:49:12.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\NETWORK SERVICE"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783886500316,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"svchost.exe loads a rare unsigned module\" on host \"NB-EFRETES\" (\"192.168.100.70\"). The behavioral analytics system identified this \"defense evasion\" threat through rule \"f50c7054-8530-4f07-afe1-fe9de6a2045a\" with status \"matched\".. Analytics details: \"The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPLJM227_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is a83edad207b9779665dbe9597e2501eb9e5fc5da875974ab8231bceab411df8e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 0 hosts and 0 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Svchost.exe loads a rare unsigned module",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-svchost_exe_loads_a_rare_unsigned_module",
                        "scope": "",
                        "tactic": {
                            "id": "TA0004",
                            "name": "Privilege Escalation"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1543",
                            "name": "Create or Modify System Process",
                            "subtechnique": {
                                "id": "T1543.003",
                                "name": "Windows Service"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0005",
                                    "name": "Defense Evasion"
                                },
                                "technique": {
                                    "id": "T1036",
                                    "name": "Masquerading",
                                    "subtechnique": {
                                        "id": "T1036.004",
                                        "name": "Masquerade Task or Service"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0003",
                                    "name": "Persistence"
                                },
                                "technique": {
                                    "id": "T1543",
                                    "name": "Create or Modify System Process",
                                    "subtechnique": {
                                        "id": "T1543.003",
                                        "name": "Windows Service"
                                    }
                                }
                            },
                            {
                                "tactic": {
                                    "id": "TA0004",
                                    "name": "Privilege Escalation"
                                },
                                "technique": {
                                    "id": "T1543",
                                    "name": "Create or Modify System Process",
                                    "subtechnique": {
                                        "id": "T1543.003",
                                        "name": "Windows Service"
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