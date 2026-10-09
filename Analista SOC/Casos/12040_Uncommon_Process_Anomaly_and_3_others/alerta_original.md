=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "18e9ec58-cb01-47d2-89de-7ad0ef360cad1783811701549-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9690,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 7,
                    "aella_tuples": "188.32.210.218.10.40.2.152.22.198",
                    "anomaly_id": "vzVwU58BI3UnQyDO-NzE",
                    "appid": 198,
                    "appid_family": "Encrypted",
                    "appid_name": "ssh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "188.32.210.218"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "12:b7:9e:19:51:47.0.10.40.2.152",
                    "dstip": "10.40.2.152",
                    "dstip_aella_flag": 1,
                    "dstip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "dstip_geo_point": "39.0469,-77.4903",
                    "dstip_host": "ip-10-40-2-152",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "12:b7:9e:19:51:47",
                    "dstport": 22,
                    "duration": 804,
                    "end_bucket_time": 1783811400000,
                    "end_reason": 4,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event_category": "killchain",
                    "event_name": "scanner_rep",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 81.32,
                    "flow_score": 100,
                    "host": {
                        "ip": "10.40.2.152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "inbytes_delta": 2281,
                    "inbytes_total": 2281,
                    "inpkts_delta": 11,
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "request": {
                            "version": "2.0"
                        },
                        "response": {
                            "processing_time": 13,
                            "response_time": 125,
                            "version": "2.0"
                        }
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "linux_agent"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 0,
                    "netid_name": "vlan0",
                    "obsid": 170394264,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "vzVwU58BI3UnQyDO-NzE",
                    "orig_index": "aella-adr-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 1826,
                    "outbytes_total": 1826,
                    "outpkts_delta": 11,
                    "port_name": "ethernet0",
                    "process_name": "systemd",
                    "process_user": "root",
                    "processing_time": 13,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783811331381,
                    "response_time": 125,
                    "run_every": 5,
                    "severity": 20,
                    "srcip": "188.32.210.218",
                    "srcip_asn": 42610,
                    "srcip_asn_org": "Rostelecom",
                    "srcip_geo": {
                        "city": "Moscow",
                        "countryCode": "RU",
                        "countryName": "Russia",
                        "latitude": 55.7487,
                        "longitude": 37.6187,
                        "region": "Moscow"
                    },
                    "srcip_geo_point": "55.7487,37.6187",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "188.32.210.218",
                    "srcip_reputation": "Scanner",
                    "srcip_reputation_source": "ETPro",
                    "srcip_type": "public",
                    "srcip_version": "ipv4",
                    "srcmac": "12:c2:40:1e:d2:1f",
                    "srcport": 46220,
                    "start_bucket_time": 1783811100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783811701529,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 361359,
                        "status": "New"
                    },
                    "stellar_da_input": 916,
                    "stellar_index_id": "aella-ser-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "18e9ec58-cb01-47d2-89de-7ad0ef360cad1783811701549-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 112,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 97,
                    "timestamp": 1783811330180,
                    "timestamp_utc": "2026-07-11T23:08:50.000Z",
                    "tos": 0,
                    "totalbytes": 4107,
                    "totalpackets": 22,
                    "typical": 1,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783811701549,
                    "xdr_event": {
                        "description": "An anomalously large number (#: 7) of connections has been observed from a host (\"IP/name: 188.32.210.218\") with a reputation category of Scanner. The typical number of connections is 1, measured in a 5.0-minute interval.",
                        "display_name": "Scanner Reputation Anomaly",
                        "framework_version": "v8",
                        "name": "scanner_rep",
                        "scope": "",
                        "tactic": {
                            "id": "TA0043",
                            "name": "Reconnaissance"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1595",
                            "name": "Active Scanning"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "747a83e4-73c8-4af2-928e-27fcdd4b1ec01783813202344-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9694,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "17e1ae8b-d682-40d9-a8fe-b521743f8c55",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "WjaIU58BI3UnQyDOVXsA",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh -e /usr/lib/ubuntu-release-upgrader/release-upgrade-motd",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 24,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "release-upgrade"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783812900000,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event": {
                        "module": "auditd"
                    },
                    "event_category": "killchain",
                    "event_name": "network_uncommon_process",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 38.96,
                    "host": {
                        "ip": "10.40.2.152",
                        "name": "ip-10-40-2-152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "lateral": false,
                    "locid": "unassigned location",
                    "msg_class": "audit-rule",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "auditd"
                        },
                        "product": "auditbeat",
                        "source": "linux_agent",
                        "vendor": "elastic"
                    },
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "WjaIU58BI3UnQyDOVXsA",
                    "orig_index": "aella-audit-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "systemd--release-upgrade",
                    "parent_proc_name": "systemd",
                    "path": "/usr/lib/ubuntu-release-upgrader/release-upgrade-motd",
                    "primary": "unset",
                    "process_name": "release-upgrade",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783812862367,
                    "record_type": "syscall",
                    "secondary": "root",
                    "service": {
                        "type": "auditd"
                    },
                    "severity": 30,
                    "source_name": "auditd",
                    "src_tuples": "null.0.10.40.2.152",
                    "srcip": "10.40.2.152",
                    "srcip_aella_flag": 1,
                    "srcip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "srcip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "srcip_geo_point": "39.0469,-77.4903",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ip-10-40-2-152",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1783812600000,
                    "stellar": {
                        "alert_time": 1783813201338,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 329919,
                        "status": "New"
                    },
                    "stellar_da_input": 1199,
                    "stellar_index_id": "aella-ser-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "747a83e4-73c8-4af2-928e-27fcdd4b1ec01783813202344-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783812860910,
                    "timestamp_utc": "2026-07-11T23:34:20.000Z",
                    "tty": "(none)",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783813202344,
                    "xdr_event": {
                        "description": "A process release-upgrade, that has never been observed by Stellar Cyber before (or been seen very rarely) after 24 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
                        "display_name": "Uncommon Process Anomaly",
                        "framework_version": "v8",
                        "name": "network_uncommon_process",
                        "scope": "",
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Process Anomaly"
                        ],
                        "technique": {
                            "id": "XT1001",
                            "name": "XDR Process Anomaly"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "0a517cbe-2f9b-4672-a99d-452a464e91891783813202344-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9695,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "17e1ae8b-d682-40d9-a8fe-b521743f8c55",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "XTaIU58BI3UnQyDOVXsB",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "stat -c %Y /var/lib/ubuntu-release-upgrader/release-upgrade-available",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 14,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "stat"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783812900000,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event": {
                        "module": "auditd"
                    },
                    "event_category": "killchain",
                    "event_name": "network_uncommon_process",
                    "event_score": 26,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 19.08,
                    "host": {
                        "ip": "10.40.2.152",
                        "name": "ip-10-40-2-152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "lateral": false,
                    "locid": "unassigned location",
                    "msg_class": "audit-rule",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "auditd"
                        },
                        "product": "auditbeat",
                        "source": "linux_agent",
                        "vendor": "elastic"
                    },
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "XTaIU58BI3UnQyDOVXsB",
                    "orig_index": "aella-audit-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/stat",
                    "primary": "unset",
                    "process_name": "stat",
                    "process_user": "0",
                    "program_name": "/usr/bin/stat",
                    "receive_time": 1783812862367,
                    "record_type": "syscall",
                    "secondary": "root",
                    "service": {
                        "type": "auditd"
                    },
                    "severity": 30,
                    "source_name": "auditd",
                    "src_tuples": "null.0.10.40.2.152",
                    "srcip": "10.40.2.152",
                    "srcip_aella_flag": 1,
                    "srcip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "srcip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "srcip_geo_point": "39.0469,-77.4903",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ip-10-40-2-152",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1783812600000,
                    "stellar": {
                        "alert_time": 1783813201347,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 329926,
                        "status": "New"
                    },
                    "stellar_da_input": 1124,
                    "stellar_index_id": "aella-ser-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "0a517cbe-2f9b-4672-a99d-452a464e91891783813202344-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783812860926,
                    "timestamp_utc": "2026-07-11T23:34:20.000Z",
                    "tty": "(none)",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783813202344,
                    "xdr_event": {
                        "description": "A process stat, that has never been observed by Stellar Cyber before (or been seen very rarely) after 14 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
                        "display_name": "Uncommon Process Anomaly",
                        "framework_version": "v8",
                        "name": "network_uncommon_process",
                        "scope": "",
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Process Anomaly"
                        ],
                        "technique": {
                            "id": "XT1001",
                            "name": "XDR Process Anomaly"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "58a17d1c-4c5e-47c7-be49-4e41cc223deb1783813201334-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9693,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "17e1ae8b-d682-40d9-a8fe-b521743f8c55",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "YTaIU58BI3UnQyDOVXsG",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "expr 1783701977 + 86400",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 24,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "expr"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783812900000,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event": {
                        "module": "auditd"
                    },
                    "event_category": "killchain",
                    "event_name": "network_uncommon_process",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 38.96,
                    "host": {
                        "ip": "10.40.2.152",
                        "name": "ip-10-40-2-152"
                    },
                    "hostip": "10.40.2.152",
                    "hostip_aella_flag": 1,
                    "hostip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "hostip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "hostip_geo_point": "39.0469,-77.4903",
                    "hostip_host": "ip-10-40-2-152",
                    "hostip_reputation": "Good",
                    "hostip_type": "private",
                    "hostip_version": "ipv4",
                    "lateral": false,
                    "locid": "unassigned location",
                    "msg_class": "audit-rule",
                    "msg_origin": {
                        "category": "endpoint",
                        "processor": {
                            "type": "auditd"
                        },
                        "product": "auditbeat",
                        "source": "linux_agent",
                        "vendor": "elastic"
                    },
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "YTaIU58BI3UnQyDOVXsG",
                    "orig_index": "aella-audit-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/expr",
                    "primary": "unset",
                    "process_name": "expr",
                    "process_user": "0",
                    "program_name": "/usr/bin/expr",
                    "receive_time": 1783812862367,
                    "record_type": "syscall",
                    "secondary": "root",
                    "service": {
                        "type": "auditd"
                    },
                    "severity": 30,
                    "source_name": "auditd",
                    "src_tuples": "null.0.10.40.2.152",
                    "srcip": "10.40.2.152",
                    "srcip_aella_flag": 1,
                    "srcip_assetid": "45d85e56-f153-11f0-bee4-aa0456b9a54a",
                    "srcip_geo": {
                        "city": "Ashburn",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.0469,
                        "longitude": -77.4903,
                        "region": "Virginia"
                    },
                    "srcip_geo_point": "39.0469,-77.4903",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ip-10-40-2-152",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1783812600000,
                    "stellar": {
                        "alert_time": 1783813201320,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 329899,
                        "status": "New"
                    },
                    "stellar_da_input": 1078,
                    "stellar_index_id": "aella-ser-2026.07.11-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "58a17d1c-4c5e-47c7-be49-4e41cc223deb1783813201334-YWVsbGEtc2VyLTIwMjYuMDcuMTEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783812860931,
                    "timestamp_utc": "2026-07-11T23:34:20.000Z",
                    "tty": "(none)",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783813201334,
                    "xdr_event": {
                        "description": "A process expr, that has never been observed by Stellar Cyber before (or been seen very rarely) after 24 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
                        "display_name": "Uncommon Process Anomaly",
                        "framework_version": "v8",
                        "name": "network_uncommon_process",
                        "scope": "",
                        "tactic": {
                            "id": "XTA0001",
                            "name": "XDR EBA"
                        },
                        "tags": [
                            "Process Anomaly"
                        ],
                        "technique": {
                            "id": "XT1001",
                            "name": "XDR Process Anomaly"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}