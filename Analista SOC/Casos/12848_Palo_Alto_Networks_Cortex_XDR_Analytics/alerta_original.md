=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "f64ee672-f8d7-42eb-8acc-2428db668b2b1785496744449-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13393,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "M9Xjt58BI3UnQyDO2aJf",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "133192"
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
                        "ip": "10.218.107.102",
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
                    "orig_id": "M9Xjt58BI3UnQyDO2aJf",
                    "orig_index": "aella-syslog-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "133192",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Defense Evasion",
                        "deduplicate_tokens": null,
                        "description": "The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPOJ7740_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is de81d7c4e9bf664ca1112cc7b3f456ea91c72868afd1d0f97b44c67529f1aa6e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 1 hosts and 2 unique days in the last 30 days",
                        "detection_timestamp": 1785496261457,
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
                                "actor_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "actor_process_image_md5": "07fe1be55d1049c7b48e270c466502d4",
                                "actor_process_image_name": "svchost.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "actor_process_image_sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2",
                                "actor_process_instance_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_os_pid": 4604,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 12580,
                                "agent_host_boot_time": 1785157455994,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "causality_actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "causality_actor_process_execution_time": 1785157467409,
                                "causality_actor_process_image_md5": "07fe1be55d1049c7b48e270c466502d4",
                                "causality_actor_process_image_name": "svchost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "causality_actor_process_image_sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn7fffQ/183DHABBvmw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1785496261457,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0dyHTLjfkAABjsAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\wbem\\wmiprvse.exe\u0000-secured\u0000-Embedding",
                                "os_actor_process_image_name": "WmiPrvSE.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                                "os_actor_process_image_sha256": "db815f552d1b935a203a347b3220e3804818d1128ef1d8dd2e5cf0b3918fa990",
                                "os_actor_process_instance_id": "Ad0dyHTLjfkAABjsAAAAAA==",
                                "os_actor_process_os_pid": 6380,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 10816,
                                "user_name": "NT AUTHORITY\\SYSTEM"
                            }
                        ],
                        "external_id": "51b721e2-e9a0-4239-9e0e-a3f857dab483",
                        "filter_rule_id": null,
                        "host_ip": [
                            "10.218.107.102"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1785496560584,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "f50c7054-8530-4f07-afe1-fe9de6a2045a",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0005 - Stealth",
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
                            "DT:Malicious Service Analytics",
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
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
                                    "md5": "07fe1be55d1049c7b48e270c466502d4",
                                    "sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2"
                                },
                                "name": "svchost.exe",
                                "pid": 4604
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 154055,
                        "status": "New"
                    },
                    "stellar_da_input": 6073,
                    "stellar_index_id": "aella-ser-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f64ee672-f8d7-42eb-8acc-2428db668b2b1785496744449-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785496261457,
                    "timestamp_utc": "2026-07-31T11:11:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\SYSTEM"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1785496744449,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"svchost.exe loads a rare unsigned module\" on host \"NB-EFRETES\" (\"10.218.107.102\"). The behavioral analytics system identified this \"defense evasion\" threat through rule \"f50c7054-8530-4f07-afe1-fe9de6a2045a\" with status \"matched\".. Analytics details: \"The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPOJ7740_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is de81d7c4e9bf664ca1112cc7b3f456ea91c72868afd1d0f97b44c67529f1aa6e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 1 hosts and 2 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
                            },
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
                "_id": "9856a353-68eb-4a65-89d6-3baf9a0128091785496744439-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13392,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "MtXjt58BI3UnQyDO2aJf",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "133191"
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
                        "ip": "10.218.107.102",
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
                    "orig_id": "MtXjt58BI3UnQyDO2aJf",
                    "orig_index": "aella-syslog-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "133191",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Defense Evasion",
                        "deduplicate_tokens": null,
                        "description": "The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPLJM227_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is a83edad207b9779665dbe9597e2501eb9e5fc5da875974ab8231bceab411df8e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 1 hosts and 2 unique days in the last 30 days",
                        "detection_timestamp": 1785496261547,
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
                                "actor_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "actor_process_image_md5": "07fe1be55d1049c7b48e270c466502d4",
                                "actor_process_image_name": "svchost.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "actor_process_image_sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2",
                                "actor_process_instance_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "actor_process_os_pid": 4604,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 12580,
                                "agent_host_boot_time": 1785157455994,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0dyHRf4tsAABH8AAAAAA==",
                                "causality_actor_process_command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt",
                                "causality_actor_process_execution_time": 1785157467409,
                                "causality_actor_process_image_md5": "07fe1be55d1049c7b48e270c466502d4",
                                "causality_actor_process_image_name": "svchost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\svchost.exe",
                                "causality_actor_process_image_sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn7fffWn183DHABBvrw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1785496261547,
                                "event_type": "Load Image Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0dyHTLjfkAABjsAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\wbem\\wmiprvse.exe\u0000-secured\u0000-Embedding",
                                "os_actor_process_image_name": "WmiPrvSE.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                                "os_actor_process_image_sha256": "db815f552d1b935a203a347b3220e3804818d1128ef1d8dd2e5cf0b3918fa990",
                                "os_actor_process_instance_id": "Ad0dyHTLjfkAABjsAAAAAA==",
                                "os_actor_process_os_pid": 6380,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 10816,
                                "user_name": "NT AUTHORITY\\SYSTEM"
                            }
                        ],
                        "external_id": "d78b0fd5-2a15-4305-b5eb-c0345ed3fb14",
                        "filter_rule_id": null,
                        "host_ip": [
                            "10.218.107.102"
                        ],
                        "host_name": "NB-EFRETES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1785496557011,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "f50c7054-8530-4f07-afe1-fe9de6a2045a",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0005 - Stealth",
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
                            "DT:Malicious Service Analytics",
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
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
                                    "md5": "07fe1be55d1049c7b48e270c466502d4",
                                    "sha256": "1222a44a5fdb4efde4dfcb41093648627950e7ec02d8667f1c26ccae31d922e2"
                                },
                                "name": "svchost.exe",
                                "pid": 4604
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 154040,
                        "status": "New"
                    },
                    "stellar_da_input": 6073,
                    "stellar_index_id": "aella-ser-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "9856a353-68eb-4a65-89d6-3baf9a0128091785496744439-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785496261547,
                    "timestamp_utc": "2026-07-31T11:11:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "NT AUTHORITY\\SYSTEM"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1785496744439,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"svchost.exe loads a rare unsigned module\" on host \"NB-EFRETES\" (\"10.218.107.102\"). The behavioral analytics system identified this \"defense evasion\" threat through rule \"f50c7054-8530-4f07-afe1-fe9de6a2045a\" with status \"matched\".. Analytics details: \"The unsigned module C:\\Windows\\System32\\spool\\drivers\\x64\\3\\HPLJM227_FaxPCSendRenderPlugin.dll was executed using svchost.exe on NB-EFRETES. The hash of the module is a83edad207b9779665dbe9597e2501eb9e5fc5da875974ab8231bceab411df8e. Svchost.exe is a Windows signed executable that loads and executes services. Attackers can use svchost.exe to load their malicious DLL into memory and execute it covertly. The command line of the running svchost is C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Winmgmt. This module hash was seen on 1 hosts and 2 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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