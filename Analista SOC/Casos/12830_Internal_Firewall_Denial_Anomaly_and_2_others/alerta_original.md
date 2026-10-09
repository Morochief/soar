=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "7e1b3fba-7594-4aba-acb8-c1d4033a796f1785442803240-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12740,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 226,
                    "aella_tuples": "192.168.171.115.192.168.169.76.7680.4",
                    "anomaly_id": "uLaotJ8BI3UnQyDOQBem",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/7680",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "NB-SFERNANDEZ"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785442204913,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.76",
                    "dstip": "192.168.169.76",
                    "dstip_assetid": "d6d43ac8-cac6-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "nb-amunoz.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "ALBERTMUNOZ",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1785442500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785442204913
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 70,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 97.33,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-30",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "WiFi_Corp",
                        "dstintfrole": "lan",
                        "event_time": "2026-07-30 17:10:05",
                        "eventtime": "1785442204912604985",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "a8:59:5f:6d:8a:8a",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "3223659666",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN304",
                        "srcintfrole": "lan",
                        "srcname": "NB-SFERNANDEZ",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "17:10:05",
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
                    "orig_id": "uLaotJ8BI3UnQyDOQBem",
                    "orig_index": "aella-adr-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-30 time=17:10:05 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785442204912604985 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.171.115 srcname=\"NB-SFERNANDEZ\" srcport=57797 srcintf=\"VLAN304\" srcintfrole=\"lan\" dstip=192.168.169.76 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=3223659666 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" dstuser=\"ALBERTMUNOZ\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"a8:59:5f:6d:8a:8a\" srcmac=\"a8:59:5f:6d:8a:8a\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785442345946,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "a8:59:5f:6d:8a:8a.0.192.168.171.115",
                    "srcip": "192.168.171.115",
                    "srcip_assetid": "10ab3040-dd13-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "NB-SFERNANDEZ",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "a8:59:5f:6d:8a:8a",
                    "srcport": 57797,
                    "start_bucket_time": 1785442200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785442803222,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 452393,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2541,
                    "stellar_index_id": "aella-ser-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "7e1b3fba-7594-4aba-acb8-c1d4033a796f1785442803240-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785442204913,
                    "timestamp_utc": "2026-07-30T20:10:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 26,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785442803240,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.171.115, name: NB-SFERNANDEZ private) has had actions blocked by a firewall too many times (#: 226), compared to the typical number of blocks (#: 26), measured in a 5.0-minute interval.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "71e1a80e-146e-4922-8cd6-8a6da74a2f2b1785444452445-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12772,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "192.168.169.76.94.242.58.56.443.null",
                    "anomaly_id": "b7jHtJ8BI3UnQyDOB9Q-",
                    "appid_name": "https",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "133150"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "dstip": "94.242.58.56",
                    "dstip_asn": 42532,
                    "dstip_asn_org": "SIA VEESP",
                    "dstip_geo": {
                        "city": "Stockholm",
                        "countryCode": "SE",
                        "countryName": "Sweden",
                        "latitude": 59.3779,
                        "longitude": 17.9155,
                        "region": "Stockholm County"
                    },
                    "dstip_geo_point": "59.3779,17.9155",
                    "dstip_host": "teknogods.com",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstport": 443,
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Rare unsigned binary connected to a globally rare external host"
                        }
                    },
                    "event_score": 55,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 55,
                    "host": {
                        "ip": "192.168.169.76",
                        "name": "NB-AMUNOZ"
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
                    "orig_id": "b7jHtJ8BI3UnQyDOB9Q-",
                    "orig_index": "aella-syslog-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "133150",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": 529,
                        "category": "Command and Control",
                        "deduplicate_tokens": null,
                        "description": "The rare binary TeknoMW3_Client_Launcher.exe connected to a rare external host. The address it tried to contact was teknogods.com. This unsigned process was seen on 0 hosts and across 0 unique days in the last 30 days. The actor sent 0.0002498626708984375MB and recved 0.0033969879150390625MB during the network session. The address teknogods.com was connected by 0 different endpoints across 0 unique days in the last 30 days. This is an uncommon communication pattern",
                        "detection_timestamp": 1785443793326,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "740a4ccb4057481fae581a1d991eaad2",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_external_hostname": "teknogods.com",
                                "action_local_ip": "192.168.169.76",
                                "action_local_port": 8450,
                                "action_process_signature_status": "N/A",
                                "action_remote_ip": "94.242.58.56",
                                "action_remote_port": 443,
                                "actor_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "actor_process_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "actor_process_command_line": "\"C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe\" ",
                                "actor_process_image_md5": "059060791187766dfed2a08eeb089e45",
                                "actor_process_image_name": "TeknoMW3_Client_Launcher.exe",
                                "actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe",
                                "actor_process_image_sha256": "8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b",
                                "actor_process_instance_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "actor_process_os_pid": 32760,
                                "actor_process_signature_status": "Unsigned",
                                "actor_thread_thread_id": 17700,
                                "agent_host_boot_time": 1785398225678,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe\" ",
                                "causality_actor_process_execution_time": 1785443785561,
                                "causality_actor_process_image_md5": "059060791187766dfed2a08eeb089e45",
                                "causality_actor_process_image_name": "TeknoMW3_Client_Launcher.exe",
                                "causality_actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe",
                                "causality_actor_process_image_sha256": "8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b",
                                "causality_actor_process_signature_status": "Unsigned",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "dst_action_country": "SE",
                                "dst_action_external_hostname": "teknogods.com",
                                "dst_agent_id": "94.242.58.56",
                                "dst_association_strength": 10,
                                "event_id": "ODY4NTkwMzA5MjI1NDA5ODEzMg==",
                                "event_sub_type": 5,
                                "event_timestamp": 1785443793326,
                                "event_type": "Network Connections",
                                "fw_app_id": "ip,tcp,ssl",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "os_actor_process_command_line": "\"C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe\" ",
                                "os_actor_process_image_name": "TeknoMW3_Client_Launcher.exe",
                                "os_actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe",
                                "os_actor_process_image_sha256": "8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b",
                                "os_actor_process_instance_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "os_actor_process_os_pid": 32760,
                                "os_actor_process_signature_status": "Unsigned",
                                "os_actor_thread_thread_id": 17700,
                                "story_id": "ODY4NTkwMzA5MjI1NDA5ODEzMg==",
                                "user_name": "TECHNOMA\\albertmunoz"
                            }
                        ],
                        "external_id": "68ae13f4-e43c-460d-a5bc-9c259de7e0e9",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.76"
                        ],
                        "host_name": "NB-AMUNOZ",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1785444035837,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "91a94867-03ff-4361-a592-47bc82fc3418",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0011 - Command and Control"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1071.001 - Application Layer Protocol: Web Protocols"
                        ],
                        "name": "Rare unsigned binary connected to a globally rare external host",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DT:EDR Windows C2 Analytics",
                            "DOM:Security"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "medium",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:EDR Windows C2 Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "891e3a6b-5b19-4033-8d20-c2e2377ccdc1"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "\"C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe\" ",
                                "executable": "C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe",
                                "hash": {
                                    "md5": "059060791187766dfed2a08eeb089e45",
                                    "sha256": "8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b"
                                },
                                "name": "TeknoMW3_Client_Launcher.exe",
                                "pid": 32760
                            }
                        }
                    ],
                    "severity": 55,
                    "src_tuples": "null.0.192.168.169.76",
                    "srcip": "192.168.169.76",
                    "srcip_assetid": "d6d43ac8-cac6-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "nb-amunoz.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 8450,
                    "stellar": {
                        "detection_time": 82291,
                        "status": "New"
                    },
                    "stellar_da_input": 6396,
                    "stellar_index_id": "aella-ser-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "71e1a80e-146e-4922-8cd6-8a6da74a2f2b1785444452445-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785443793326,
                    "timestamp_utc": "2026-07-30T20:36:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\albertmunoz"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1785444452445,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"rare unsigned binary connected to a globally rare external host\" on host \"NB-AMUNOZ\" (\"192.168.169.76\"). The behavioral analytics system identified this \"command and control\" threat through rule \"91a94867-03ff-4361-a592-47bc82fc3418\" with status \"matched\".. Analytics details: \"The rare binary TeknoMW3_Client_Launcher.exe connected to a rare external host. The address it tried to contact was teknogods.com. This unsigned process was seen on 0 hosts and across 0 unique days in the last 30 days. The actor sent 0.0002498626708984375MB and recved 0.0033969879150390625MB during the network session. The address teknogods.com was connected by 0 different endpoints across 0 unique days in the last 30 days. This is an uncommon communication pattern\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Rare unsigned binary connected to a globally rare external host",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-rare_unsigned_binary_connected_to_a_globally_rare_external_host",
                        "scope": "",
                        "tactic": {
                            "id": "TA0011",
                            "name": "Command and Control"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1071",
                            "name": "Application Layer Protocol",
                            "subtechnique": {
                                "id": "T1071.001",
                                "name": "Web Protocols"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0011",
                                    "name": "Command and Control"
                                },
                                "technique": {
                                    "id": "T1071",
                                    "name": "Application Layer Protocol",
                                    "subtechnique": {
                                        "id": "T1071.001",
                                        "name": "Web Protocols"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "440c77e6-09bd-4926-9925-b6b996a51c991785444452445-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12771,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "192.168.169.76.94.242.58.56.443.null",
                    "anomaly_id": "brjHtJ8BI3UnQyDOB9Q-",
                    "appid_name": "https",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "133151"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "dstip": "94.242.58.56",
                    "dstip_asn": 42532,
                    "dstip_asn_org": "SIA VEESP",
                    "dstip_geo": {
                        "city": "Stockholm",
                        "countryCode": "SE",
                        "countryName": "Sweden",
                        "latitude": 59.3779,
                        "longitude": 17.9155,
                        "region": "Stockholm County"
                    },
                    "dstip_geo_point": "59.3779,17.9155",
                    "dstip_host": "teknogods.com",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstport": 443,
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "medium",
                        "threat": {
                            "name": "Rare unsigned binary connected to a globally rare external host"
                        }
                    },
                    "event_score": 55,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 55,
                    "host": {
                        "ip": "192.168.169.76",
                        "name": "NB-AMUNOZ"
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
                    "orig_id": "brjHtJ8BI3UnQyDOB9Q-",
                    "orig_index": "aella-syslog-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "133151",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": 529,
                        "category": "Command and Control",
                        "deduplicate_tokens": null,
                        "description": "The rare binary iw5mp.exe connected to a rare external host. The address it tried to contact was teknogods.com. This unsigned process was seen on 0 hosts and across 0 unique days in the last 30 days. The actor sent 0.00042438507080078125MB and recved 0.003726959228515625MB during the network session. The address teknogods.com was connected by 0 different endpoints across 0 unique days in the last 30 days. This is an uncommon communication pattern",
                        "detection_timestamp": 1785443871721,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "740a4ccb4057481fae581a1d991eaad2",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_external_hostname": "teknogods.com",
                                "action_local_ip": "192.168.169.76",
                                "action_local_port": 54608,
                                "action_process_signature_status": "N/A",
                                "action_remote_ip": "94.242.58.56",
                                "action_remote_port": 443,
                                "actor_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "actor_process_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "actor_process_command_line": "+server 127.0.0.1:27016",
                                "actor_process_image_md5": "2616ecd588b610f4324ac4887f31e82c",
                                "actor_process_image_name": "iw5mp.exe",
                                "actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\iw5mp.exe",
                                "actor_process_image_sha256": "c2cb2335f1e2dd9f714fc90db429bafd41bdf47b59a27c509fbc27509c8587cd",
                                "actor_process_instance_id": "Ad0gY0CP0k4AAGfoAAAAAA==",
                                "actor_process_os_pid": 26600,
                                "actor_process_signature_status": "Invalid Signature",
                                "actor_process_signature_vendor": "Valve Corporation",
                                "actor_thread_thread_id": 19164,
                                "agent_host_boot_time": 1785398225678,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe\" ",
                                "causality_actor_process_execution_time": 1785443785561,
                                "causality_actor_process_image_md5": "059060791187766dfed2a08eeb089e45",
                                "causality_actor_process_image_name": "TeknoMW3_Client_Launcher.exe",
                                "causality_actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\TeknoMW3_Client_Launcher.exe",
                                "causality_actor_process_image_sha256": "8ddf64f5e0831de63794a6474b73636ce52768b491fcff658a3304b9679f229b",
                                "causality_actor_process_signature_status": "Unsigned",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "dst_action_country": "SE",
                                "dst_action_external_hostname": "teknogods.com",
                                "dst_agent_id": "94.242.58.56",
                                "dst_association_strength": 10,
                                "event_id": "NDA2OTQ5MzMxODE1NjkwMjkyMA==",
                                "event_sub_type": 5,
                                "event_timestamp": 1785443871721,
                                "event_type": "Network Connections",
                                "fw_app_id": "ip,tcp,ssl,ssl",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0gYxbip8MAAH/4AAAAAA==",
                                "os_actor_process_command_line": "+server 127.0.0.1:27016",
                                "os_actor_process_image_name": "iw5mp.exe",
                                "os_actor_process_image_path": "C:\\Call of Duty Modern Warfare 3\\iw5mp.exe",
                                "os_actor_process_image_sha256": "c2cb2335f1e2dd9f714fc90db429bafd41bdf47b59a27c509fbc27509c8587cd",
                                "os_actor_process_instance_id": "Ad0gY0CP0k4AAGfoAAAAAA==",
                                "os_actor_process_os_pid": 26600,
                                "os_actor_process_signature_status": "Invalid Signature",
                                "os_actor_process_signature_vendor": "Valve Corporation",
                                "os_actor_thread_thread_id": 19164,
                                "story_id": "NDA2OTQ5MzMxODE1NjkwMjkyMA==",
                                "user_name": "TECHNOMA\\albertmunoz"
                            }
                        ],
                        "external_id": "88c8aaf1-44ec-427c-ad2a-6e13c5cc5ab9",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.76"
                        ],
                        "host_name": "NB-AMUNOZ",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1785444037559,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "91a94867-03ff-4361-a592-47bc82fc3418",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0011 - Command and Control"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1071.001 - Application Layer Protocol: Web Protocols"
                        ],
                        "name": "Rare unsigned binary connected to a globally rare external host",
                        "original_tags": [
                            "DS:PANW/XDR Agent",
                            "DT:EDR Windows C2 Analytics",
                            "DOM:Security"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "medium",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DT:EDR Windows C2 Analytics",
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": "891e3a6b-5b19-4033-8d20-c2e2377ccdc1"
                    },
                    "process_list": [
                        {
                            "parent": {
                                "command_line": "+server 127.0.0.1:27016",
                                "executable": "C:\\Call of Duty Modern Warfare 3\\iw5mp.exe",
                                "hash": {
                                    "md5": "2616ecd588b610f4324ac4887f31e82c",
                                    "sha256": "c2cb2335f1e2dd9f714fc90db429bafd41bdf47b59a27c509fbc27509c8587cd"
                                },
                                "name": "iw5mp.exe",
                                "pid": 26600
                            }
                        }
                    ],
                    "severity": 55,
                    "src_tuples": "null.0.192.168.169.76",
                    "srcip": "192.168.169.76",
                    "srcip_assetid": "d6d43ac8-cac6-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "nb-amunoz.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcport": 54608,
                    "stellar": {
                        "detection_time": 82279,
                        "status": "New"
                    },
                    "stellar_da_input": 6265,
                    "stellar_index_id": "aella-ser-2026.07.30-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "440c77e6-09bd-4926-9925-b6b996a51c991785444452445-YWVsbGEtc2VyLTIwMjYuMDcuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785443871721,
                    "timestamp_utc": "2026-07-30T20:37:51.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\albertmunoz"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1785444452445,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"rare unsigned binary connected to a globally rare external host\" on host \"NB-AMUNOZ\" (\"192.168.169.76\"). The behavioral analytics system identified this \"command and control\" threat through rule \"91a94867-03ff-4361-a592-47bc82fc3418\" with status \"matched\".. Analytics details: \"The rare binary iw5mp.exe connected to a rare external host. The address it tried to contact was teknogods.com. This unsigned process was seen on 0 hosts and across 0 unique days in the last 30 days. The actor sent 0.00042438507080078125MB and recved 0.003726959228515625MB during the network session. The address teknogods.com was connected by 0 different endpoints across 0 unique days in the last 30 days. This is an uncommon communication pattern\". Agent version \"9.0.0.16757\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): Rare unsigned binary connected to a globally rare external host",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-rare_unsigned_binary_connected_to_a_globally_rare_external_host",
                        "scope": "",
                        "tactic": {
                            "id": "TA0011",
                            "name": "Command and Control"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1071",
                            "name": "Application Layer Protocol",
                            "subtechnique": {
                                "id": "T1071.001",
                                "name": "Web Protocols"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0011",
                                    "name": "Command and Control"
                                },
                                "technique": {
                                    "id": "T1071",
                                    "name": "Application Layer Protocol",
                                    "subtechnique": {
                                        "id": "T1071.001",
                                        "name": "Web Protocols"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}