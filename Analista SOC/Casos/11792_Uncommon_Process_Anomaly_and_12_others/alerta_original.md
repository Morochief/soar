=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "48011b40-0318-44c3-89ab-f76964783e9e1783491902644-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4261,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 68,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "w6ZiQJ8BBi0xHyA-JTvO",
                    "anomaly_tag": "spike",
                    "audit_status": "fail",
                    "category": "audit-rule",
                    "command": "/usr/bin/dpkg --status-fd 11 --no-triggers --unpack --auto-deconfigure /var/cache/apt/archives/gzip_1.12-1ubuntu3.2_amd64.deb",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/bin/dpkg --status-fd 11 --no-triggers --unpack --auto-deconfigure /var/cache/apt/archives/gzip_1.12-1ubuntu3.2_amd64.deb"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
                    "engid": "ee2aa8bfa67440a499e20245b2b268c6",
                    "engid_device_class": "Linux",
                    "engid_device_desc": "ubuntu-24.04",
                    "engid_gateway": "54.91.215.126",
                    "engid_name": "ip-10-40-2-152",
                    "event": {
                        "module": "auditd"
                    },
                    "event_category": "killchain",
                    "event_name": "command_anomaly",
                    "event_score": 6,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 1.2,
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
                    "orig_id": "w6ZiQJ8BBi0xHyA-JTvO",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/sbin/sh",
                    "primary": "unset",
                    "process_name": "dpkg",
                    "process_user": "0",
                    "program_name": "/usr/bin/dpkg",
                    "receive_time": 1783491592580,
                    "record_type": "syscall",
                    "secondary": "root",
                    "service": {
                        "type": "auditd"
                    },
                    "severity": 15,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901624,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "population_spike",
                        "detection_time": 299775,
                        "status": "New"
                    },
                    "stellar_da_input": 1174,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "48011b40-0318-44c3-89ab-f76964783e9e1783491902644-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491590585,
                    "timestamp_utc": "2026-07-08T06:19:50.000Z",
                    "tty": "pts0",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902644,
                    "xdr_event": {
                        "description": "The command \"/usr/bin/dpkg --status-fd...1.12-1ubuntu3.2_amd64.deb\" has been executed an anomalously large number (#: 68) of times compared to the typical number of executions of other commands, which diverges from its recent low volume. The typical number of executions of other commands is 1.0 in a 5.0-minute interval.",
                        "display_name": "Command Anomaly",
                        "framework_version": "v8",
                        "name": "command_anomaly",
                        "scope": "",
                        "tactic": {
                            "id": "TA0002",
                            "name": "Execution"
                        },
                        "tags": [
                            "Internal"
                        ],
                        "technique": {
                            "id": "T1059",
                            "name": "Command and Scripting Interpreter"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "497e1a09-c999-4730-8b32-6fec68ea0d931783491901381-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4254,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "x6ZiQJ8BBi0xHyA-JTvO",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "dpkg-divert --truename /bin/zfgrep",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 68,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "dpkg-divert"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 75.59,
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
                    "orig_id": "x6ZiQJ8BBi0xHyA-JTvO",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/dpkg-divert",
                    "primary": "unset",
                    "process_name": "dpkg-divert",
                    "process_user": "0",
                    "program_name": "/usr/bin/dpkg-divert",
                    "receive_time": 1783491593651,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901371,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 299518,
                        "status": "New"
                    },
                    "stellar_da_input": 1108,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "497e1a09-c999-4730-8b32-6fec68ea0d931783491901381-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491591287,
                    "timestamp_utc": "2026-07-08T06:19:51.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491901381,
                    "xdr_event": {
                        "description": "A process dpkg-divert, that has never been observed by Stellar Cyber before (or been seen very rarely) after 68 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "15af71a9-0400-4256-9212-c07d196f450f1783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4256,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "0aZiQJ8BBi0xHyA-JTvO",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/gzip.postinst configure 1.12-1ubuntu3.1",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 237,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "gzip.postinst"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 44,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 93.13,
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
                    "orig_id": "0aZiQJ8BBi0xHyA-JTvO",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/gzip.postinst",
                    "primary": "unset",
                    "process_name": "gzip.postinst",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491597752,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901379,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 299524,
                        "status": "New"
                    },
                    "stellar_da_input": 1147,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "15af71a9-0400-4256-9212-c07d196f450f1783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491591418,
                    "timestamp_utc": "2026-07-08T06:19:51.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902443,
                    "xdr_event": {
                        "description": "A process gzip.postinst, that has never been observed by Stellar Cyber before (or been seen very rarely) after 237 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "8f453417-a8c5-45fc-8e73-84532e647e081783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4258,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "a6ZiQJ8BBi0xHyA-JTzg",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/install-info.postinst triggered /usr/share/info",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 32,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "install-info.po"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 36,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 50.01,
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
                    "orig_id": "a6ZiQJ8BBi0xHyA-JTzg",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/install-info.postinst",
                    "primary": "unset",
                    "process_name": "install-info.po",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491598755,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901394,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 299526,
                        "status": "New"
                    },
                    "stellar_da_input": 1165,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8f453417-a8c5-45fc-8e73-84532e647e081783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491591523,
                    "timestamp_utc": "2026-07-08T06:19:51.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902443,
                    "xdr_event": {
                        "description": "A process install-info.po, that has never been observed by Stellar Cyber before (or been seen very rarely) after 32 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "e4a11bf3-bf8a-4a7d-b6d8-9aa5099834be1783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4260,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "BaZiQJ8BBi0xHyA-JTzV",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /usr/sbin/update-info-dir",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 32,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "update-info-dir"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 36,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 50.01,
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
                    "orig_id": "BaZiQJ8BBi0xHyA-JTzV",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/sbin/update-info-dir",
                    "primary": "unset",
                    "process_name": "update-info-dir",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491598755,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901410,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 299549,
                        "status": "New"
                    },
                    "stellar_da_input": 1109,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e4a11bf3-bf8a-4a7d-b6d8-9aa5099834be1783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491591525,
                    "timestamp_utc": "2026-07-08T06:19:51.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902443,
                    "xdr_event": {
                        "description": "A process update-info-dir, that has never been observed by Stellar Cyber before (or been seen very rarely) after 32 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "4d55e2dd-05ad-4a75-ae5f-be9527f407e11783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4257,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "1aZiQJ8BBi0xHyA-JTvO",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "install-info /usr/share/info/gnupg.info.gz /usr/share/info/dir",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 32,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "install-info"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 36,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 50.01,
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
                    "orig_id": "1aZiQJ8BBi0xHyA-JTvO",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/install-info",
                    "primary": "unset",
                    "process_name": "install-info",
                    "process_user": "0",
                    "program_name": "/usr/bin/install-info",
                    "receive_time": 1783491598755,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901386,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 299531,
                        "status": "New"
                    },
                    "stellar_da_input": 1139,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "4d55e2dd-05ad-4a75-ae5f-be9527f407e11783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491591559,
                    "timestamp_utc": "2026-07-08T06:19:51.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902443,
                    "xdr_event": {
                        "description": "A process install-info, that has never been observed by Stellar Cyber before (or been seen very rarely) after 32 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "89eeb5af-8c77-45f4-a810-e0f2151edf891783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4259,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "yqZiQJ8BBi0xHyA-c0CM",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/python3.12.prerm upgrade 3.12.3-1ubuntu0.15",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "python3.12.prer"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491600000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "yqZiQJ8BBi0xHyA-c0CM",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/python3.12.prerm",
                    "primary": "unset",
                    "process_name": "python3.12.prer",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491611642,
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
                    "start_bucket_time": 1783491300000,
                    "stellar": {
                        "alert_time": 1783491901403,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 279657,
                        "status": "New"
                    },
                    "stellar_da_input": 1156,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "89eeb5af-8c77-45f4-a810-e0f2151edf891783491902443-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491599985,
                    "timestamp_utc": "2026-07-08T06:19:59.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783491902443,
                    "xdr_event": {
                        "description": "A process python3.12.prer, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "069fdd1c-b515-43d6-bd8a-2382707800e81783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4266,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "DKZiQJ8BBi0xHyA-c0GV",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/libpython3.12-stdlib:amd64.prerm upgrade 3.12.3-1ubuntu0.15",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "libpython3.12-s"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "DKZiQJ8BBi0xHyA-c0GV",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/libpython3.12-stdlib:amd64.prerm",
                    "primary": "unset",
                    "process_name": "libpython3.12-s",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491613651,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201904,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580141,
                        "status": "New"
                    },
                    "stellar_da_input": 1188,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "069fdd1c-b515-43d6-bd8a-2382707800e81783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491600401,
                    "timestamp_utc": "2026-07-08T06:20:00.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492202908,
                    "xdr_event": {
                        "description": "A process libpython3.12-s, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "fcf3a379-bbfc-4d98-974e-519d25d7a7c11783492201901-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4264,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "vKZiQJ8BBi0xHyA-c0CH",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/libpython3.12-minimal:amd64.prerm upgrade 3.12.3-1ubuntu0.15",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "libpython3.12-m"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "vKZiQJ8BBi0xHyA-c0CH",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/libpython3.12-minimal:amd64.prerm",
                    "primary": "unset",
                    "process_name": "libpython3.12-m",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491616843,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201890,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580138,
                        "status": "New"
                    },
                    "stellar_da_input": 1190,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fcf3a379-bbfc-4d98-974e-519d25d7a7c11783492201901-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491600909,
                    "timestamp_utc": "2026-07-08T06:20:00.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492201901,
                    "xdr_event": {
                        "description": "A process libpython3.12-m, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "2f7dbe77-3427-47fe-8aa3-a58a4585ce631783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4267,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "3KZiQJ8BBi0xHyA-c0CM",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/python3.12-minimal.postinst configure 3.12.3-1ubuntu0.13",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "python3.12-mini"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "3KZiQJ8BBi0xHyA-c0CM",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/python3.12-minimal.postinst",
                    "primary": "unset",
                    "process_name": "python3.12-mini",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491617854,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201914,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580164,
                        "status": "New"
                    },
                    "stellar_da_input": 1180,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2f7dbe77-3427-47fe-8aa3-a58a4585ce631783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491601632,
                    "timestamp_utc": "2026-07-08T06:20:01.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492202908,
                    "xdr_event": {
                        "description": "A process python3.12-mini, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "83b31915-446a-46db-b282-6eb6d38654cb1783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4268,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "_KZiQJ8BBi0xHyA-c0CM",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/python3.12.postinst configure 3.12.3-1ubuntu0.13",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "python3.12.post"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "_KZiQJ8BBi0xHyA-c0CM",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/python3.12.postinst",
                    "primary": "unset",
                    "process_name": "python3.12.post",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491617854,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201921,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580170,
                        "status": "New"
                    },
                    "stellar_da_input": 1164,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "83b31915-446a-46db-b282-6eb6d38654cb1783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491604075,
                    "timestamp_utc": "2026-07-08T06:20:04.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492202908,
                    "xdr_event": {
                        "description": "A process python3.12.post, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "2256ada5-4690-4ed0-8d77-c78c60178f531783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4270,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "_aZiQJ8BBi0xHyA-c0CM",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/systemd.postinst triggered /usr/lib/binfmt.d",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "systemd.postins"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "_aZiQJ8BBi0xHyA-c0CM",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/systemd.postinst",
                    "primary": "unset",
                    "process_name": "systemd.postins",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1783491618849,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201939,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580188,
                        "status": "New"
                    },
                    "stellar_da_input": 1157,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2256ada5-4690-4ed0-8d77-c78c60178f531783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491605823,
                    "timestamp_utc": "2026-07-08T06:20:05.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492202908,
                    "xdr_event": {
                        "description": "A process systemd.postins, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "abfb8a4b-24c4-4682-8e66-01cad452871d1783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4269,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "564757fe-f772-4329-b2fe-916d895eb9d1",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "36ZiQJ8BBi0xHyA-c0CM",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/lib/systemd/systemd-binfmt",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 75,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "systemd-binfmt"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783491900000,
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
                    "event_score": 41,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 77.86,
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
                    "orig_id": "36ZiQJ8BBi0xHyA-c0CM",
                    "orig_index": "aella-audit-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "systemd--systemd-binfmt",
                    "parent_proc_name": "systemd",
                    "path": "/usr/lib/systemd/systemd-binfmt",
                    "primary": "unset",
                    "process_name": "systemd-binfmt",
                    "process_user": "0",
                    "program_name": "/usr/lib/systemd/systemd-binfmt",
                    "receive_time": 1783491618849,
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
                    "start_bucket_time": 1783491600000,
                    "stellar": {
                        "alert_time": 1783492201928,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 580178,
                        "status": "New"
                    },
                    "stellar_da_input": 1161,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "abfb8a4b-24c4-4682-8e66-01cad452871d1783492202908-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783491605902,
                    "timestamp_utc": "2026-07-08T06:20:05.000Z",
                    "tty": "(none)",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783492202908,
                    "xdr_event": {
                        "description": "A process systemd-binfmt, that has never been observed by Stellar Cyber before (or been seen very rarely) after 75 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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