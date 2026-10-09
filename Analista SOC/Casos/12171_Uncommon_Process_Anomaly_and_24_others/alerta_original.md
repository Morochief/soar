=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "a9c65824-6d1b-47f2-a3d0-c8cce08d5b0d1784096101757-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10885,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "unmounted",
                    "actual": 89,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "c5ffa91c-3b61-4b51-a4ad-eff93305a602",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "OPxkZJ8BI3UnQyDOINKi",
                    "anomaly_tag": "spike",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/lib/systemd/systemd-executor --deserialize 71 --log-level info --log-target journal-or-kmsg",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/lib/systemd/systemd-executor --deserialize 71 --log-level info --log-target journal-or-kmsg"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784095800000,
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
                    "event_score": 14,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 13.32,
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
                    "orig_id": "OPxkZJ8BI3UnQyDOINKi",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "systemd--(mandb)",
                    "parent_proc_name": "systemd",
                    "path": "/run/systemd/mount-rootfs/dev/pts",
                    "primary": "unset",
                    "process_name": "(mandb)",
                    "process_user": "0",
                    "program_name": "/usr/lib/systemd/systemd-executor",
                    "receive_time": 1784095703393,
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
                    "start_bucket_time": 1784095500000,
                    "stellar": {
                        "alert_time": 1784096101740,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 390357,
                        "status": "New"
                    },
                    "stellar_da_input": 1231,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a9c65824-6d1b-47f2-a3d0-c8cce08d5b0d1784096101757-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "mount_audit",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784095700959,
                    "timestamp_utc": "2026-07-15T06:08:20.000Z",
                    "tty": "(none)",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784096101757,
                    "xdr_event": {
                        "description": "The command \"/usr/lib/systemd/systemd-...og-target journal-or-kmsg\" has been executed an anomalously large number (#: 89) of times compared to the typical number of executions (#: 1.0) in a 5.0-minute interval.",
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
                "_id": "f66c7455-6030-4de1-b847-49e59f8395ed1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10894,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "PP2DZJ8BI3UnQyDOjtuh",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /usr/bin/dpkg-maintscript-helper rm_conffile /etc/network/if-up.d/openssh-server 1:7.9p1-1~ -- upgrade 1:9.6p1-3ubuntu13.16 1:9.6p1-3ubuntu13.18",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 18,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "dpkg-maintscrip"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 26.44,
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
                    "orig_id": "PP2DZJ8BI3UnQyDOjtuh",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/dpkg-maintscript-helper",
                    "primary": "unset",
                    "process_name": "dpkg-maintscrip",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1784097761475,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201916,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430761,
                        "status": "New"
                    },
                    "stellar_da_input": 1235,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f66c7455-6030-4de1-b847-49e59f8395ed1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097758747,
                    "timestamp_utc": "2026-07-15T06:42:38.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process dpkg-maintscrip, that has never been observed by Stellar Cyber before (or been seen very rarely) after 18 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "e5bac532-631e-4fcb-86fc-f0e794eb33641784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10893,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "Wf2DZJ8BI3UnQyDOjtuh",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/bin/perl /usr/bin/deb-systemd-invoke stop rescue-ssh.target",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 35,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "deb-systemd-inv"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 53.61,
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
                    "orig_id": "Wf2DZJ8BI3UnQyDOjtuh",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/deb-systemd-invoke",
                    "primary": "unset",
                    "process_name": "deb-systemd-inv",
                    "process_user": "0",
                    "program_name": "deb-systemd-inv",
                    "receive_time": 1784097762489,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201907,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430749,
                        "status": "New"
                    },
                    "stellar_da_input": 1144,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e5bac532-631e-4fcb-86fc-f0e794eb33641784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097758854,
                    "timestamp_utc": "2026-07-15T06:42:38.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process deb-systemd-inv, that has never been observed by Stellar Cyber before (or been seen very rarely) after 35 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "ff737d97-58a0-44f0-b13d-6929b93614b21784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10900,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "sv2DZJ8BI3UnQyDOjtui",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/openssh-client.prerm upgrade 1:9.6p1-3ubuntu13.18",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "openssh-client."
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "sv2DZJ8BI3UnQyDOjtui",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/openssh-client.prerm",
                    "primary": "unset",
                    "process_name": "openssh-client.",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1784097764580,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201977,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430820,
                        "status": "New"
                    },
                    "stellar_da_input": 1166,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ff737d97-58a0-44f0-b13d-6929b93614b21784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759069,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process openssh-client., that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "ac234fda-ed38-4286-bac7-f38d0e17187c1784098201909-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10890,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deleted",
                    "actual": 89,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "uv2DZJ8BI3UnQyDOjtui",
                    "anomaly_tag": "spike",
                    "audit_status": "fail",
                    "category": "audit-rule",
                    "command": "/usr/bin/dpkg --status-fd 11 --no-triggers --unpack --auto-deconfigure /var/cache/apt/archives/openssh-sftp-server_1%3a9.6p1-3ub",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/bin/dpkg --status-fd 11 --no-triggers --unpack --auto-deconfigure /var/cache/apt/archives/openssh-sftp-server_1%3a9.6p1-3ub"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "event_score": 7,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 1.72,
                    "fim_action": "deleted",
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
                    "orig_id": "uv2DZJ8BI3UnQyDOjtui",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "unattended-upgr--dpkg",
                    "parent_proc_name": "unattended-upgr",
                    "path": "/usr/bin/ssh-keygen.dpkg-tmp",
                    "primary": "unset",
                    "process_name": "dpkg",
                    "process_user": "0",
                    "program_name": "/usr/bin/dpkg",
                    "receive_time": 1784097767880,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201901,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "population_spike",
                        "detection_time": 430743,
                        "status": "New"
                    },
                    "stellar_da_input": 1393,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ac234fda-ed38-4286-bac7-f38d0e17187c1784098201909-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "software_change",
                    "targetfile_delete": {
                        "action": "DELETE",
                        "group": "",
                        "inode": "24572",
                        "mode": "0755",
                        "name": "/usr/bin/ssh-keygen.dpkg-tmp",
                        "owner": ""
                    },
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759205,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098201909,
                    "xdr_event": {
                        "description": "The command \"/usr/bin/dpkg --status-fd...sftp-server_1%3a9.6p1-3ub\" has been executed an anomalously large number (#: 89) of times compared to the typical number of executions of other commands, which diverges from its recent low volume. The typical number of executions of other commands is 1.0 in a 5.0-minute interval.",
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
                "_id": "73ef2790-af74-48ba-a3ce-571dfb96b9841784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10896,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "1v2DZJ8BI3UnQyDOjtuk",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "getent group _ssh",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "getent"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "1v2DZJ8BI3UnQyDOjtuk",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/getent",
                    "primary": "unset",
                    "process_name": "getent",
                    "process_user": "0",
                    "program_name": "/usr/bin/getent",
                    "receive_time": 1784097768782,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201933,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430776,
                        "status": "New"
                    },
                    "stellar_da_input": 1076,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "73ef2790-af74-48ba-a3ce-571dfb96b9841784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759288,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process getent, that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "daef8c85-3c5c-48c8-89d2-7eab0ac80e0a1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10895,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "Z_2DZJ8BI3UnQyDOjtuh",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "dpkg-statoverride --list /usr/bin/ssh-agent",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 26,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "dpkg-statoverri"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "event_score": 34,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 42.95,
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
                    "orig_id": "Z_2DZJ8BI3UnQyDOjtuh",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/dpkg-statoverride",
                    "primary": "unset",
                    "process_name": "dpkg-statoverri",
                    "process_user": "0",
                    "program_name": "/usr/bin/dpkg-statoverride",
                    "receive_time": 1784097768782,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201923,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430763,
                        "status": "New"
                    },
                    "stellar_da_input": 1133,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "daef8c85-3c5c-48c8-89d2-7eab0ac80e0a1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759294,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process dpkg-statoverri, that has never been observed by Stellar Cyber before (or been seen very rarely) after 26 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "b12dad9b-f00f-4fd4-8c67-78fedbd383ab1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10891,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "changed-file-ownership-of",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "hf2DZJ8BI3UnQyDOjtuh",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "chgrp _ssh /usr/bin/ssh-agent",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "chgrp"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
                    "fim_action": "attributes_modified",
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
                    "orig_id": "hf2DZJ8BI3UnQyDOjtuh",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/ssh-agent",
                    "primary": "unset",
                    "process_name": "chgrp",
                    "process_user": "0",
                    "program_name": "/usr/bin/chgrp",
                    "receive_time": 1784097768782,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201859,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430702,
                        "status": "New"
                    },
                    "stellar_da_input": 1152,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b12dad9b-f00f-4fd4-8c67-78fedbd383ab1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "software_change",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759301,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process chgrp, that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "9057c27f-1f31-46da-ab32-fe4e57a420d91784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10901,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "9v2DZJ8BI3UnQyDOjtul",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /var/lib/dpkg/info/openssh-server.postinst configure 1:9.6p1-3ubuntu13.16",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "openssh-server."
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "9v2DZJ8BI3UnQyDOjtul",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/var/lib/dpkg/info/openssh-server.postinst",
                    "primary": "unset",
                    "process_name": "openssh-server.",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1784097769877,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201986,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430829,
                        "status": "New"
                    },
                    "stellar_da_input": 1174,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "9057c27f-1f31-46da-ab32-fe4e57a420d91784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759571,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process openssh-server., that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "3ee915b7-c417-410d-96d2-26d446e67ab11784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10908,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "v_2DZJ8BI3UnQyDOjtui",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /usr/bin/ucf --three-way --debconf-ok --sum-file /usr/share/openssh/sshd_config.md5sum /tmp/tmp.Y0GpV93qDU /etc/ssh/sshd_config",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "ucf"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "v_2DZJ8BI3UnQyDOjtui",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/ucf",
                    "primary": "unset",
                    "process_name": "ucf",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1784097769877,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098202066,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 430908,
                        "status": "New"
                    },
                    "stellar_da_input": 1186,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3ee915b7-c417-410d-96d2-26d446e67ab11784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759593,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process ucf, that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "d86fa0b5-a5d5-4be2-acb4-3fb81f41a6371784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10902,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "s_2DZJ8BI3UnQyDOtd1J",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "perl -nle print \"\\Q$_\\E\\n\"",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "perl"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "s_2DZJ8BI3UnQyDOtd1J",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/perl",
                    "primary": "unset",
                    "process_name": "perl",
                    "process_user": "0",
                    "program_name": "perl",
                    "receive_time": 1784097770878,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201995,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 420948,
                        "status": "New"
                    },
                    "stellar_da_input": 1075,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d86fa0b5-a5d5-4be2-acb4-3fb81f41a6371784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759635,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process perl, that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "6b954d8c-9d58-4244-a164-52bb2503b2ea1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10906,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "6f2DZJ8BI3UnQyDOtd1M",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "readlink -e /usr/bin/pager",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 18,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "readlink"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "event_score": 29,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "exploit",
                    "fidelity": 26.44,
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
                    "orig_id": "6f2DZJ8BI3UnQyDOtd1M",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/readlink",
                    "primary": "unset",
                    "process_name": "readlink",
                    "process_user": "0",
                    "program_name": "/usr/bin/readlink",
                    "receive_time": 1784097770878,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098202043,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 420996,
                        "status": "New"
                    },
                    "stellar_da_input": 1091,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6b954d8c-9d58-4244-a164-52bb2503b2ea1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759643,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process readlink, that has never been observed by Stellar Cyber before (or been seen very rarely) after 18 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "70bc3b3b-a7ab-40a6-b369-10dddf7b5fc01784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10899,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "ff2DZJ8BI3UnQyDOtd1I",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "md5sum /etc/ssh/sshd_config",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 74,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "md5sum"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.27,
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
                    "orig_id": "ff2DZJ8BI3UnQyDOtd1I",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/md5sum",
                    "primary": "unset",
                    "process_name": "md5sum",
                    "process_user": "0",
                    "program_name": "/usr/bin/md5sum",
                    "receive_time": 1784097770878,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098201965,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 420920,
                        "status": "New"
                    },
                    "stellar_da_input": 1086,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "70bc3b3b-a7ab-40a6-b369-10dddf7b5fc01784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759685,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process md5sum, that has never been observed by Stellar Cyber before (or been seen very rarely) after 74 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "af3c190e-61dc-4544-af2b-dbf673da1b4d1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10909,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "B_2DZJ8BI3UnQyDOtd5N",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/bin/sh /usr/bin/ucfr openssh-server /etc/ssh/sshd_config",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 76,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "ucfr"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 77.87,
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
                    "orig_id": "B_2DZJ8BI3UnQyDOtd5N",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/bin/ucfr",
                    "primary": "unset",
                    "process_name": "ucfr",
                    "process_user": "0",
                    "program_name": "/usr/bin/dash",
                    "receive_time": 1784097770878,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098202075,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421028,
                        "status": "New"
                    },
                    "stellar_da_input": 1110,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "af3c190e-61dc-4544-af2b-dbf673da1b4d1784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759691,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process ucfr, that has never been observed by Stellar Cyber before (or been seen very rarely) after 76 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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
                "_id": "3efaa183-34e8-42a2-a2a2-45f4ed3274461784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 10912,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 1,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "983abefc-561b-4dc5-9913-a57e4c0c84de",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "uP2DZJ8BI3UnQyDOtd1J",
                    "audit_status": "fail",
                    "category": "audit-rule",
                    "command": "/usr/bin/perl /usr/sbin/update-rc.d ssh defaults",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "days_silent": 35,
                    "detected_fields": [
                        "process_name"
                    ],
                    "detected_values": [
                        "update-rc.d"
                    ],
                    "detector_index": 0,
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1784097900000,
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
                    "fidelity": 53.61,
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
                    "orig_id": "uP2DZJ8BI3UnQyDOtd1J",
                    "orig_index": "aella-audit-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "path": "/usr/sbin/systemctl",
                    "primary": "unset",
                    "process_name": "update-rc.d",
                    "process_user": "0",
                    "program_name": "update-rc.d",
                    "receive_time": 1784097771921,
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
                    "start_bucket_time": 1784097600000,
                    "stellar": {
                        "alert_time": 1784098202105,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421055,
                        "status": "New"
                    },
                    "stellar_da_input": 1109,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "3efaa183-34e8-42a2-a2a2-45f4ed3274461784098202915-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784097759773,
                    "timestamp_utc": "2026-07-15T06:42:39.000Z",
                    "tty": "pts0",
                    "typical": 0,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1784098202915,
                    "xdr_event": {
                        "description": "A process update-rc.d, that has never been observed by Stellar Cyber before (or been seen very rarely) after 35 days of silence, has been launched on \"IP: 10.40.2.152, name: ip-10-40-2-152\".",
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