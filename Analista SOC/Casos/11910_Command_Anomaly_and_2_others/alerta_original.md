=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ace642fd-b624-48df-8712-cc1d3a1500211783610701361-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6969,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 137,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "b39c420c-4f3c-4148-a8ed-67186a5142aa",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "LRtyR58BBi0xHyA-gClv",
                    "anomaly_tag": "spike",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783610400000,
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
                    "event_score": 21,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 42,
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
                    "orig_id": "LRtyR58BBi0xHyA-gClv",
                    "orig_index": "aella-audit-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "sshd--sshd",
                    "parent_proc_name": "sshd",
                    "path": "/usr/sbin/sshd",
                    "primary": "unset",
                    "process_name": "sshd",
                    "process_user": "0",
                    "program_name": "/usr/sbin/sshd",
                    "receive_time": 1783610109050,
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
                    "start_bucket_time": 1783610100000,
                    "stellar": {
                        "alert_time": 1783610701306,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 587156,
                        "status": "New"
                    },
                    "stellar_da_input": 1240,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ace642fd-b624-48df-8712-cc1d3a1500211783610701361-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783610108193,
                    "timestamp_utc": "2026-07-09T15:15:08.000Z",
                    "tty": "(none)",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783610701361,
                    "xdr_event": {
                        "description": "The command \"/usr/sbin/sshd -D -o Auth...r ec2-instance-connect -R\" has been executed an anomalously large number (#: 137) of times compared to the typical number of executions (#: 1.0) in a 5.0-minute interval.",
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
                "_id": "8dafcd41-9629-449e-854a-04d9a40b92711783611001859-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6972,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 129,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "b39c420c-4f3c-4148-a8ed-67186a5142aa",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "8ht3R58BBi0xHyA--a9K",
                    "anomaly_tag": "spike",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783610700000,
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
                    "event_score": 21,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 38.91,
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
                    "orig_id": "8ht3R58BBi0xHyA--a9K",
                    "orig_index": "aella-audit-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "sshd--sshd",
                    "parent_proc_name": "sshd",
                    "path": "/usr/sbin/sshd",
                    "primary": "unset",
                    "process_name": "sshd",
                    "process_user": "0",
                    "program_name": "/usr/sbin/sshd",
                    "receive_time": 1783610464000,
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
                    "start_bucket_time": 1783610400000,
                    "stellar": {
                        "alert_time": 1783611001848,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 529075,
                        "status": "New"
                    },
                    "stellar_da_input": 1240,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "8dafcd41-9629-449e-854a-04d9a40b92711783611001859-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783610462918,
                    "timestamp_utc": "2026-07-09T15:21:02.000Z",
                    "tty": "(none)",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783611001859,
                    "xdr_event": {
                        "description": "The command \"/usr/sbin/sshd -D -o Auth...r ec2-instance-connect -R\" has been executed an anomalously large number (#: 129) of times compared to the typical number of executions (#: 1.0) in a 5.0-minute interval.",
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
                "_id": "c18bfd0d-5aa4-4dca-9235-07a242babbda1783611301627-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6975,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "executed",
                    "actual": 133,
                    "agent": {
                        "computer_name": "ip-10-40-2-152",
                        "ephemeral_id": "b39c420c-4f3c-4148-a8ed-67186a5142aa",
                        "id": "41cf8cbc-75ea-43d2-b183-05b6de957433",
                        "name": "ee2aa8bfa67440a499e20245b2b268c6",
                        "type": "auditbeat",
                        "version": "8.5.3"
                    },
                    "anomaly_id": "dBx8R58BBi0xHyA-jhiQ",
                    "anomaly_tag": "spike",
                    "audit_status": "success",
                    "category": "audit-rule",
                    "command": "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R",
                    "computer_name": "ip-10-40-2-152",
                    "cwd": "/",
                    "detected_fields": [
                        "command"
                    ],
                    "detected_values": [
                        "/usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect -R"
                    ],
                    "dscp_name": "Best Effort",
                    "ecs": {
                        "version": "8.0.0"
                    },
                    "end_bucket_time": 1783611000000,
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
                    "event_score": 21,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "cnc",
                    "fidelity": 40.47,
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
                    "orig_id": "dBx8R58BBi0xHyA-jhiQ",
                    "orig_index": "aella-audit-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parent_child": "sshd--sshd",
                    "parent_proc_name": "sshd",
                    "path": "/usr/sbin/sshd",
                    "primary": "unset",
                    "process_name": "sshd",
                    "process_user": "0",
                    "program_name": "/usr/sbin/sshd",
                    "receive_time": 1783610764101,
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
                    "start_bucket_time": 1783610700000,
                    "stellar": {
                        "alert_time": 1783611301594,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 528465,
                        "status": "New"
                    },
                    "stellar_da_input": 1240,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c18bfd0d-5aa4-4dca-9235-07a242babbda1783611301627-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tags": "exec",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783610763432,
                    "timestamp_utc": "2026-07-09T15:26:03.000Z",
                    "tty": "(none)",
                    "typical": 1,
                    "username": "root",
                    "write_by": "sef",
                    "write_time": 1783611301627,
                    "xdr_event": {
                        "description": "The command \"/usr/sbin/sshd -D -o Auth...r ec2-instance-connect -R\" has been executed an anomalously large number (#: 133) of times compared to the typical number of executions (#: 1.0) in a 5.0-minute interval.",
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
            }
        ]
    }
}