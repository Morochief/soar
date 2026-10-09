=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "dc1378cc-d673-4079-914d-b2cecf5fbc591790173390860-YWVsbGEtc2VyLTIwMjYuMDkuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13313,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "iGykzqABI3UnQyDOzoga",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "145120"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Uncommon routing table listing via route.exe"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.50",
                        "name": "NB-RBARRETO"
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
                    "orig_id": "iGykzqABI3UnQyDOzoga",
                    "orig_index": "aella-syslog-2026.09.23-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "145120",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Discovery",
                        "deduplicate_tokens": null,
                        "description": "The 'route' command was executed on NB-RBARRETO to list the routing table. Child process command line: route  print . The command line was seen on 3 hosts in the last 30 days",
                        "detection_timestamp": 1790172724372,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "92c062d66f2c4443a2f73e771513e375",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "action_process_image_command_line": "route  print ",
                                "action_process_image_name": "ROUTE.EXE",
                                "action_process_image_sha256": "79a71edb01e35dcac272bffc400383286c14b8090c61687603fc51ad7999e5c9",
                                "action_process_instance_id": "Ad1LZYPzv4YAAAkEAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "actor_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "actor_process_image_md5": "ce396564392fafaad5c07a5e2dade4e6",
                                "actor_process_image_name": "cmd.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\cmd.exe",
                                "actor_process_image_sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb",
                                "actor_process_instance_id": "Ad1LZYPjKkQAAFGsAAAAAA==",
                                "actor_process_os_pid": 20908,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 20412,
                                "agent_host_boot_time": 1790083466773,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Program Files\\OpenConnect-GUI\\openconnect-gui.exe\" ",
                                "causality_actor_process_execution_time": 1790084279083,
                                "causality_actor_process_image_md5": "57853802f19ee50f6433eb0752b89a55",
                                "causality_actor_process_image_name": "openconnect-gui.exe",
                                "causality_actor_process_image_path": "C:\\Program Files\\OpenConnect-GUI\\openconnect-gui.exe",
                                "causality_actor_process_image_sha256": "b7c15d26ab765d5086081fd3d47211071c781edaf73f2f9a7b1d824fbad8eae9",
                                "causality_actor_process_signature_status": "Invalid Signature",
                                "causality_actor_process_signature_vendor": "Open Source Developer",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABoM6cBlefU15SABCRMg==",
                                "event_sub_type": 1,
                                "event_timestamp": 1790172724372,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "os_actor_process_image_name": "cmd.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\cmd.exe",
                                "os_actor_process_image_sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb",
                                "os_actor_process_instance_id": "Ad1LZYPjKkQAAFGsAAAAAA==",
                                "os_actor_process_os_pid": 20908,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 20412,
                                "user_name": "TECHNOMA\\rubenbarreto"
                            }
                        ],
                        "external_id": "cae38d5e-2ac3-4c86-bde2-bd21e8b3a497",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.50",
                            "192.168.254.11"
                        ],
                        "host_name": "NB-RBARRETO",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1790172811283,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "758e8ed7-e953-11e9-b4ee-8c8590c9ccd1",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0007 - Discovery"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1016 - System Network Configuration Discovery"
                        ],
                        "name": "Uncommon routing table listing via route.exe",
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
                                "sha256": "79a71edb01e35dcac272bffc400383286c14b8090c61687603fc51ad7999e5c9"
                            },
                            "name": "ROUTE.EXE",
                            "parent": {
                                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "executable": "C:\\Windows\\System32\\cmd.exe",
                                "hash": {
                                    "md5": "ce396564392fafaad5c07a5e2dade4e6",
                                    "sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb"
                                },
                                "name": "cmd.exe",
                                "pid": 20908
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 89858,
                        "status": "New"
                    },
                    "stellar_da_input": 5932,
                    "stellar_index_id": "aella-ser-2026.09.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "dc1378cc-d673-4079-914d-b2cecf5fbc591790173390860-YWVsbGEtc2VyLTIwMjYuMDkuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790172724372,
                    "timestamp_utc": "2026-09-23T14:12:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\rubenbarreto"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1790173390860,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"uncommon routing table listing via route.exe\" on host \"NB-RBARRETO\" (\"192.168.169.50\"). The behavioral analytics system identified this \"discovery\" threat through rule \"758e8ed7-e953-11e9-b4ee-8c8590c9ccd1\" with status \"matched\". The suspicious behavior involved \"ROUTE.EXE\" executed by user \"TECHNOMA\\rubenbarreto\". Analytics details: \"The 'route' command was executed on NB-RBARRETO to list the routing table. Child process command line: route  print . The command line was seen on 3 hosts in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Uncommon routing table listing via route.exe",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-uncommon_routing_table_listing_via_route_exe",
                        "scope": "",
                        "tactic": {
                            "id": "TA0007",
                            "name": "Discovery"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1016",
                            "name": "System Network Configuration Discovery"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0007",
                                    "name": "Discovery"
                                },
                                "technique": {
                                    "id": "T1016",
                                    "name": "System Network Configuration Discovery"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Exploration",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "0a16dec2-1008-4872-a18a-cae2a9dfb30b1790181491010-YWVsbGEtc2VyLTIwMjYuMDkuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13665,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "j30gz6ABI3UnQyDOhVvt",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "145167"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "Uncommon routing table listing via route.exe"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.50",
                        "name": "NB-RBARRETO"
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
                    "orig_id": "j30gz6ABI3UnQyDOhVvt",
                    "orig_index": "aella-syslog-2026.09.23-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "145167",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Discovery",
                        "deduplicate_tokens": null,
                        "description": "The 'route' command was executed on NB-RBARRETO to list the routing table. Child process command line: route  print . The command line was seen on 3 hosts in the last 30 days",
                        "detection_timestamp": 1790180825967,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "92c062d66f2c4443a2f73e771513e375",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "action_process_image_command_line": "route  print ",
                                "action_process_image_name": "ROUTE.EXE",
                                "action_process_image_sha256": "79a71edb01e35dcac272bffc400383286c14b8090c61687603fc51ad7999e5c9",
                                "action_process_instance_id": "Ad1LeGBvSuAAAAuoAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "actor_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "actor_process_command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "actor_process_image_md5": "ce396564392fafaad5c07a5e2dade4e6",
                                "actor_process_image_name": "cmd.exe",
                                "actor_process_image_path": "C:\\Windows\\System32\\cmd.exe",
                                "actor_process_image_sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb",
                                "actor_process_instance_id": "Ad1LeGBfvq0AACyYAAAAAA==",
                                "actor_process_os_pid": 11416,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Microsoft Corporation",
                                "actor_thread_thread_id": 24840,
                                "agent_host_boot_time": 1790083466773,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Program Files\\OpenConnect-GUI\\openconnect-gui.exe\" ",
                                "causality_actor_process_execution_time": 1790084279083,
                                "causality_actor_process_image_md5": "57853802f19ee50f6433eb0752b89a55",
                                "causality_actor_process_image_name": "openconnect-gui.exe",
                                "causality_actor_process_image_path": "C:\\Program Files\\OpenConnect-GUI\\openconnect-gui.exe",
                                "causality_actor_process_image_sha256": "b7c15d26ab765d5086081fd3d47211071c781edaf73f2f9a7b1d824fbad8eae9",
                                "causality_actor_process_signature_status": "Invalid Signature",
                                "causality_actor_process_signature_vendor": "Open Source Developer",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABoM8XokefU15SABLkVw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1790180825967,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad1Kl5T3qtwAAE5IAAAAAA==",
                                "os_actor_process_command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "os_actor_process_image_name": "cmd.exe",
                                "os_actor_process_image_path": "C:\\Windows\\System32\\cmd.exe",
                                "os_actor_process_image_sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb",
                                "os_actor_process_instance_id": "Ad1LeGBfvq0AACyYAAAAAA==",
                                "os_actor_process_os_pid": 11416,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Microsoft Corporation",
                                "os_actor_thread_thread_id": 24840,
                                "user_name": "TECHNOMA\\rubenbarreto"
                            }
                        ],
                        "external_id": "55a6f0b3-b46a-416e-9cf5-47d13495ae86",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.50",
                            "192.168.254.11"
                        ],
                        "host_name": "NB-RBARRETO",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1790180928755,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "758e8ed7-e953-11e9-b4ee-8c8590c9ccd1",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0007 - Discovery"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1016 - System Network Configuration Discovery"
                        ],
                        "name": "Uncommon routing table listing via route.exe",
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
                                "sha256": "79a71edb01e35dcac272bffc400383286c14b8090c61687603fc51ad7999e5c9"
                            },
                            "name": "ROUTE.EXE",
                            "parent": {
                                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /C \"route print\" 2>&1",
                                "executable": "C:\\Windows\\System32\\cmd.exe",
                                "hash": {
                                    "md5": "ce396564392fafaad5c07a5e2dade4e6",
                                    "sha256": "97ac98b1a92c286054cce55239cfccdfc23a5517bd07fe693072c9ca96c7dabb"
                                },
                                "name": "cmd.exe",
                                "pid": 11416
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 80887,
                        "status": "New"
                    },
                    "stellar_da_input": 5932,
                    "stellar_index_id": "aella-ser-2026.09.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "0a16dec2-1008-4872-a18a-cae2a9dfb30b1790181491010-YWVsbGEtc2VyLTIwMjYuMDkuMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790180825967,
                    "timestamp_utc": "2026-09-23T16:27:05.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\rubenbarreto"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1790181491009,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"uncommon routing table listing via route.exe\" on host \"NB-RBARRETO\" (\"192.168.169.50\"). The behavioral analytics system identified this \"discovery\" threat through rule \"758e8ed7-e953-11e9-b4ee-8c8590c9ccd1\" with status \"matched\". The suspicious behavior involved \"ROUTE.EXE\" executed by user \"TECHNOMA\\rubenbarreto\". Analytics details: \"The 'route' command was executed on NB-RBARRETO to list the routing table. Child process command line: route  print . The command line was seen on 3 hosts in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Uncommon routing table listing via route.exe",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-uncommon_routing_table_listing_via_route_exe",
                        "scope": "",
                        "tactic": {
                            "id": "TA0007",
                            "name": "Discovery"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1016",
                            "name": "System Network Configuration Discovery"
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0007",
                                    "name": "Discovery"
                                },
                                "technique": {
                                    "id": "T1016",
                                    "name": "System Network Configuration Discovery"
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Exploration",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
