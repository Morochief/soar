=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "7c67bd9f-9747-4db7-ad7b-3dbc4f50d0911784125332093-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11092,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "tBMmZp8BI3UnQyDO2q6w",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "129461"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "An uncommon file added to startup-related Registry keys by a commonly known and signed application"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.131",
                        "name": "NB-JRIVAROLA"
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
                    "orig_id": "tBMmZp8BI3UnQyDO2q6w",
                    "orig_index": "aella-syslog-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "129461",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Persistence",
                        "deduplicate_tokens": null,
                        "description": "python-3.14.2-amd64.exe registered a file to be run on the next login or boot, the activity initiated by sihost.exe. In the past 30 days, the file has been seen registered to the registry on 0 different days and on 0 additional endpoints. The file was registered at HKEY_USERS\\S-1-5-21-2518681205-442819635-436077046-3245\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce, in the {0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff} registry value. The registered file is \"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" /burn.runonce",
                        "detection_timestamp": 1784124649723,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "9dc83ca3d52343f286b1a250ee90059e",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_signature_status": "N/A",
                                "action_registry_data": "\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" /burn.runonce",
                                "action_registry_key_name": "HKEY_USERS\\S-1-5-21-2518681205-442819635-436077046-3245\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                                "action_registry_value_name": "{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}",
                                "actor_causality_id": "Ad0UYXWTwBkAACOUAAAAAA==",
                                "actor_process_causality_id": "Ad0UYXWTwBkAACOUAAAAAA==",
                                "actor_process_command_line": "\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.clean.room=\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.filehandle.attached=652 -burn.filehandle.self=668 /uninstall",
                                "actor_process_image_md5": "29cdcc0085365e52075e963ca233106b",
                                "actor_process_image_name": "python-3.14.2-amd64.exe",
                                "actor_process_image_path": "C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe",
                                "actor_process_image_sha256": "293fee043651e2db80b6e98db6574c0f54d62eaa2718ecfbc0493b551ad0897a",
                                "actor_process_instance_id": "Ad0UY8vBQkIAAEroAAAAAA==",
                                "actor_process_os_pid": 19176,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Python Software Foundation",
                                "actor_thread_thread_id": 19140,
                                "agent_host_boot_time": 1784123594137,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0UYXWTwBkAACOUAAAAAA==",
                                "causality_actor_process_command_line": "sihost.exe",
                                "causality_actor_process_execution_time": 1784123670822,
                                "causality_actor_process_image_md5": "af9ba4aa79ba3cdd28236a06d05b70d4",
                                "causality_actor_process_image_name": "sihost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\sihost.exe",
                                "causality_actor_process_image_sha256": "6e271366388fbc5a1e2e5204e7cf98557b44db2e9e34e1b6a7c8e7b80e14caab",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "cloud_provider": "others",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn2YeH7DrHKgGAALToA==",
                                "event_sub_type": 4,
                                "event_timestamp": 1784124649723,
                                "event_type": "Registry Event",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0UYXWTwBkAACOUAAAAAA==",
                                "os_actor_process_command_line": "\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.clean.room=\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.filehandle.attached=652 -burn.filehandle.self=668 /uninstall",
                                "os_actor_process_image_name": "python-3.14.2-amd64.exe",
                                "os_actor_process_image_path": "C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe",
                                "os_actor_process_image_sha256": "293fee043651e2db80b6e98db6574c0f54d62eaa2718ecfbc0493b551ad0897a",
                                "os_actor_process_instance_id": "Ad0UY8vBQkIAAEroAAAAAA==",
                                "os_actor_process_os_pid": 19176,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Python Software Foundation",
                                "os_actor_thread_thread_id": 19140,
                                "user_name": "TECHNOMA\\jorgerivarola"
                            }
                        ],
                        "external_id": "15c4ea25-bd60-4cbc-9ab4-6a8b62e17950",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.131"
                        ],
                        "host_name": "NB-JRIVAROLA",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1784124813040,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "cfb4e6ce-8f82-4d76-b5ed-79ab8e68c571",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0003 - Persistence",
                            "TA0004 - Privilege Escalation"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1547 - Boot or Logon Autostart Execution"
                        ],
                        "name": "An uncommon file added to startup-related Registry keys by a commonly known and signed application",
                        "original_tags": [
                            "EG:Technoma",
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
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "variation_rule_id": "c1e8f346-7fb1-4899-bb4f-849104b3c5de"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.clean.room=\"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" -burn.filehandle.attached=652 -burn.filehandle.self=668 /uninstall",
                                "executable": "C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe",
                                "hash": {
                                    "md5": "29cdcc0085365e52075e963ca233106b",
                                    "sha256": "293fee043651e2db80b6e98db6574c0f54d62eaa2718ecfbc0493b551ad0897a"
                                },
                                "name": "python-3.14.2-amd64.exe",
                                "pid": 19176
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 81895,
                        "status": "New"
                    },
                    "stellar_da_input": 7549,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7c67bd9f-9747-4db7-ad7b-3dbc4f50d0911784125332093-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784124649723,
                    "timestamp_utc": "2026-07-15T14:10:49.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\jorgerivarola"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1784125332092,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"an uncommon file added to startup-related registry keys by a commonly known and signed application\" on host \"NB-JRIVAROLA\" (\"192.168.169.131\"). The behavioral analytics system identified this \"persistence\" threat through rule \"cfb4e6ce-8f82-4d76-b5ed-79ab8e68c571\" with status \"matched\".. Analytics details: \"python-3.14.2-amd64.exe registered a file to be run on the next login or boot, the activity initiated by sihost.exe. In the past 30 days, the file has been seen registered to the registry on 0 different days and on 0 additional endpoints. The file was registered at HKEY_USERS\\S-1-5-21-2518681205-442819635-436077046-3245\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce, in the {0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff} registry value. The registered file is \"C:\\Users\\jorgerivarola\\AppData\\Local\\Package Cache\\{0ef3959c-4dd0-4cd2-9d49-307eaf0a2bff}\\python-3.14.2-amd64.exe\" /burn.runonce\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): An uncommon file added to startup-related Registry keys by a commonly known and signed application",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-an_uncommon_file_added_to_startup_related_registry_keys_by_a_commonly_known_and_signed_application",
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
                "_id": "d82349b2-34dc-43e5-957b-07571d00acf21784131205399-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11209,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 521,
                    "aella_tuples": "192.168.171.115.192.168.169.131.7680.4",
                    "anomaly_id": "aBt6Zp8BI3UnQyDO8jti",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/7680",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "NTB-ITTI0800"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784130600325,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.131",
                    "dstip": "192.168.169.131",
                    "dstip_assetid": "beabf79e-cac4-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "nb-jrivarola.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JORGERIVAROLA",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1784130900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784130600325
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 71,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 99.81,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "WiFi_Corp",
                        "dstintfrole": "lan",
                        "event_time": "2026-07-15 12:50:01",
                        "eventtime": "1784130600325419245",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "a8:59:5f:6d:8a:8a",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "1752284840",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN304",
                        "srcintfrole": "lan",
                        "srcname": "NB-SFERNANDEZ",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "12:50:01",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "lateral": true,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_origin": {
                        "category": "firewall",
                        "processor": {
                            "name": "in_udp,parser-stellar,filter_stellar_parser-forti_fortigate",
                            "type": "log_forwarder"
                        },
                        "source": "fw_fortigate"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 0,
                    "netid_name": "vlan0",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "aBt6Zp8BI3UnQyDO8jti",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=12:50:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784130600325419245 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.171.115 srcname=\"NB-SFERNANDEZ\" srcport=59532 srcintf=\"VLAN304\" srcintfrole=\"lan\" dstip=192.168.169.131 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1752284840 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" dstuser=\"JORGERIVAROLA\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"a8:59:5f:6d:8a:8a\" srcmac=\"a8:59:5f:6d:8a:8a\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784130750439,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "a8:59:5f:6d:8a:8a.0.192.168.171.115",
                    "srcip": "192.168.171.115",
                    "srcip_assetid": "8bb9b7e0-d6fe-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "NTB-ITTI0800",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "a8:59:5f:6d:8a:8a",
                    "srcport": 59532,
                    "start_bucket_time": 1784130600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784131204693,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 444149,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2547,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "d82349b2-34dc-43e5-957b-07571d00acf21784131205399-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784130600325,
                    "timestamp_utc": "2026-07-15T15:50:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 27,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784131205399,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.171.115, name: NTB-ITTI0800 private) has had actions blocked by a firewall too many times (#: 521), compared to the typical number of blocks (#: 27), measured in a 5.0-minute interval.",
                        "display_name": "Internal Firewall Denial Anomaly",
                        "framework_version": "v8",
                        "name": "internal_fw_action",
                        "scope": "Internal",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "Internal",
                            "Network Traffic Analysis",
                            "Firewall Anomalies"
                        ],
                        "technique": {
                            "id": "XT2002",
                            "name": "XDR Firewall Anomaly"
                        },
                        "xdr_killchain_stage": "Exploration",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}