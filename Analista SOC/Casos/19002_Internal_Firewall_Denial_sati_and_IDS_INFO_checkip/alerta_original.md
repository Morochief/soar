<USER_REQUEST>
=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "5af9a241-0a8c-4c22-8e33-571f2ca6b5431790250003001-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19002,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 436,
                    "aella_tuples": "10.212.134.203.10.11.1.1.53.4",
                    "anomaly_id": "HeEu06ABI3UnQyDOS0XS",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.203"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790249407196,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JUNIORAGUERO",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790249700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790249407196
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
                    "fidelity": 98.18,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 08:30:07",
                        "eventtime": "1790249407196308956",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "4289504744",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "08:30:07",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "HeEu06ABI3UnQyDOS0XS",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=08:30:07 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790249407196308956 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.203 srcport=44591 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=4289504744 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JUNIORAGUERO\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790249411581,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.203",
                    "srcip": "10.212.134.203",
                    "srcip_assetid": "19c1aeca-8a1f-11f1-9610-8e57707220c4",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "10.212.134.203",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 44591,
                    "start_bucket_time": 1790249400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790250002966,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 582404,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "5af9a241-0a8c-4c22-8e33-571f2ca6b5431790250003001-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790249407196,
                    "timestamp_utc": "2026-09-24T11:30:07.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 57,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790250003001,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.203 private) has had actions blocked by a firewall too many times (#: 436), compared to the typical number of blocks (#: 57), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "6508ee6b-2421-4604-92aa-2f2a4bbf4c691790251202727-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19015,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 789,
                    "aella_tuples": "10.212.134.203.10.11.1.1.53.4",
                    "anomaly_id": "YOJA06ABI3UnQyDOw-RH",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.203"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790250614609,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JUNIORAGUERO",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790250900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790250614609
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
                    "fidelity": 99.84,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 08:50:14",
                        "eventtime": "1790250614609290211",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "4290818372",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "08:50:14",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "YOJA06ABI3UnQyDOw-RH",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=08:50:14 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790250614609290211 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.203 srcport=39989 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=4290818372 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JUNIORAGUERO\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790250624103,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.203",
                    "srcip": "10.212.134.203",
                    "srcip_assetid": "19c1aeca-8a1f-11f1-9610-8e57707220c4",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "10.212.134.203",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 39989,
                    "start_bucket_time": 1790250600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790251202707,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 572043,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "6508ee6b-2421-4604-92aa-2f2a4bbf4c691790251202727-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790250614609,
                    "timestamp_utc": "2026-09-24T11:50:14.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 57,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790251202727,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.203 private) has had actions blocked by a firewall too many times (#: 789), compared to the typical number of blocks (#: 57), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "527f9712-ed5e-414f-b73c-7c234e1e781c1790251502626-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19018,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 549,
                    "aella_tuples": "10.212.134.203.10.11.1.1.53.4",
                    "anomaly_id": "NuNF06ABI3UnQyDOW2jg",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.203"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790250902853,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JUNIORAGUERO",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790251200000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790250902853
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
                    "fidelity": 99.57,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 08:55:03",
                        "eventtime": "1790250902853457772",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "4291140914",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "08:55:03",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "NuNF06ABI3UnQyDOW2jg",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=08:55:03 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790250902853457772 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.203 srcport=46210 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=4291140914 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JUNIORAGUERO\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790250929347,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.203",
                    "srcip": "10.212.134.203",
                    "srcip_assetid": "19c1aeca-8a1f-11f1-9610-8e57707220c4",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "10.212.134.203",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 46210,
                    "start_bucket_time": 1790250900000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790251502606,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 571128,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "527f9712-ed5e-414f-b73c-7c234e1e781c1790251502626-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790250902853,
                    "timestamp_utc": "2026-09-24T11:55:02.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 57,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790251502626,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.203 private) has had actions blocked by a firewall too many times (#: 549), compared to the typical number of blocks (#: 57), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "97b5cfe4-09de-4cfa-a447-23b0578157f21790251502928-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19019,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "192.168.169.37.10.11.1.1.53.32",
                    "anomaly_id": "XeNH06ABI3UnQyDOm6ad",
                    "anomaly_tag": "rare",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "days_silent": 16,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)",
                        "high"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "checkip.amazonaws.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "null.1101.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 53,
                    "duration": 32,
                    "end_bucket_time": 1790251200000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_priv",
                    "event_score": 50,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "high",
                        "ids_signatures_summarize": [
                            {
                                "id": 2054140,
                                "ids_severity": "high",
                                "name": "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 22,
                    "file_extract_timestamp": 1790251073907,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Device Retrieving External IP Address Detected",
                        "created_ts": "2024-06-28T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2024_06_28"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0007"
                            ],
                            "mitre_tactic_name": [
                                "Discovery"
                            ],
                            "mitre_technique_id": [
                                "T1614"
                            ],
                            "mitre_technique_name": [
                                "System_Location_Discovery"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "reviewed_at": [
                                "2024_10_04"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "External_IP_Lookup"
                            ],
                            "updated_at": [
                                "2024_06_28"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 28050,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "checkip.amazonaws.com",
                                        "rrtype": "A"
                                    }
                                ],
                                "rcode": "NOERROR",
                                "rd": true,
                                "tx_id": 0,
                                "type": "request",
                                "version": 3
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 85,
                                "dest_ip": "10.11.1.1",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "192.168.169.37",
                                "src_port": 58536,
                                "start": "2026-09-24T11:57:53.907777+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2024_06_28",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)\\\"; dns.query; bsize:21; content:\\\"checkip.amazonaws.com\\\"; nocase; reference:url,github.com/chubin/awesome-console-services; classtype:external-ip-check; sid:2054140; rev:1; metadata:affected_product Any, attack_target Client_Endpoint, created_at 2024_06_28, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag External_IP_Lookup, updated_at 2024_06_28, reviewed_at 2024_10_04, mitre_tactic_id TA0007, mitre_tactic_name Discovery, mitre_technique_id T1614, mitre_technique_name System_Location_Discovery;)\\n\"",
                            "updated": "2024_06_28"
                        },
                        "severity": "high",
                        "signature": "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)",
                        "signature_id": 2054140
                    },
                    "inbytes_delta": 248,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": true,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2005-08-18T02:10:45Z",
                            "effective_tld": "amazonaws.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "checkip.amazonaws.com",
                            "query_type": "A",
                            "transaction_id": 28050
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "checkip.check-ip.aws.a2z.com",
                                    "host_type": "CNAME",
                                    "name": "checkip.amazonaws.com",
                                    "section_type": "Answer",
                                    "ttl": 327
                                },
                                {
                                    "host_addr": "52.4.57.244",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.63.192.44",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "54.145.222.151",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "23.23.243.85",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.60.146.222",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "3.229.251.178",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.59.168.164",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "3.226.168.191",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                }
                            ],
                            "domain_creation": "2005-08-18T02:10:45Z",
                            "effective_tld": "amazonaws.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 32,
                            "query": "checkip.amazonaws.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "52.4.57.244",
                                "100.63.192.44",
                                "54.145.222.151",
                                "23.23.243.85",
                                "100.60.146.222",
                                "3.229.251.178",
                                "100.59.168.164",
                                "3.226.168.191"
                            ],
                            "response_time": 32,
                            "transaction_id": 28050
                        },
                        "transaction_id": 28050
                    },
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "XeNH06ABI3UnQyDOm6ad",
                    "orig_index": "aella-maltrace-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 81,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 32,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790251074231,
                    "response_time": 32,
                    "score": 60,
                    "severity": 75,
                    "sha256": "",
                    "src_tuples": "null.1101.192.168.169.37",
                    "srcip": "192.168.169.37",
                    "srcip_assetid": "5af20bc0-fe05-11f0-b2c6-62a12c107cbc",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "192.168.169.37",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "192.168.169.37.2054140",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 58536,
                    "start_bucket_time": 1790250900000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790251502911,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "rare",
                        "detection_time": 422321,
                        "status": "New"
                    },
                    "stellar_da_input": 1777,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "97b5cfe4-09de-4cfa-a447-23b0578157f21790251502928-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790251074031,
                    "timestamp_utc": "2026-09-24T11:57:54.000Z",
                    "tos": 0,
                    "totalbytes": 329,
                    "totalpackets": 2,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790251502928,
                    "xdr_event": {
                        "description": "In internal traffic, a rarely seen exploit attempt with the IDS signature \"INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)\" has been observed after 16 days of silence.",
                        "display_name": "Private to Private Exploit Anomaly",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_priv",
                        "scope": "Internal",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0008",
                            "name": "Lateral Movement"
                        },
                        "tags": [
                            "Internal",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1210",
                            "name": "Exploitation of Remote Services"
                        },
                        "xdr_killchain_stage": "Propagation",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "7da45111-169d-4765-8ad2-05e8a985016c1790251503930-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19020,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "XuNH06ABI3UnQyDOnKY2",
                    "anomaly_tag": "rare",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "days_silent": 16,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)",
                        "high"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "checkip.amazonaws.com"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.8.8",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 31,
                    "end_bucket_time": 1790251200000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 43,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "high",
                        "ids_signatures_summarize": [
                            {
                                "id": 2054140,
                                "ids_severity": "high",
                                "name": "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 22,
                    "file_extract_timestamp": 1790251073908,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Device Retrieving External IP Address Detected",
                        "created_ts": "2024-06-28T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2024_06_28"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0007"
                            ],
                            "mitre_tactic_name": [
                                "Discovery"
                            ],
                            "mitre_technique_id": [
                                "T1614"
                            ],
                            "mitre_technique_name": [
                                "System_Location_Discovery"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "reviewed_at": [
                                "2024_10_04"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "External_IP_Lookup"
                            ],
                            "updated_at": [
                                "2024_06_28"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 62609,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "checkip.amazonaws.com",
                                        "rrtype": "A"
                                    }
                                ],
                                "rcode": "NOERROR",
                                "rd": true,
                                "tx_id": 0,
                                "type": "request",
                                "version": 3
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 96,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 61123,
                                "start": "2026-09-24T11:57:53.908605+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2024_06_28",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)\\\"; dns.query; bsize:21; content:\\\"checkip.amazonaws.com\\\"; nocase; reference:url,github.com/chubin/awesome-console-services; classtype:external-ip-check; sid:2054140; rev:1; metadata:affected_product Any, attack_target Client_Endpoint, created_at 2024_06_28, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag External_IP_Lookup, updated_at 2024_06_28, reviewed_at 2024_10_04, mitre_tactic_id TA0007, mitre_tactic_name Discovery, mitre_technique_id T1614, mitre_technique_name System_Location_Discovery;)\\n\"",
                            "updated": "2024_06_28"
                        },
                        "severity": "high",
                        "signature": "INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)",
                        "signature_id": 2054140
                    },
                    "inbytes_delta": 259,
                    "inbytes_total": 0,
                    "inpkts_delta": 1,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2005-08-18T02:10:45Z",
                            "effective_tld": "amazonaws.com",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "checkip.amazonaws.com",
                            "query_type": "A",
                            "section_type": "Additional Answer",
                            "transaction_id": 62609
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "checkip.check-ip.aws.a2z.com",
                                    "host_type": "CNAME",
                                    "name": "checkip.amazonaws.com",
                                    "section_type": "Answer",
                                    "ttl": 327
                                },
                                {
                                    "host_addr": "52.4.57.244",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.63.192.44",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "54.145.222.151",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "23.23.243.85",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.60.146.222",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "3.229.251.178",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "100.59.168.164",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "3.226.168.191",
                                    "host_type": "A",
                                    "name": "checkip.check-ip.aws.a2z.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2005-08-18T02:10:45Z",
                            "effective_tld": "amazonaws.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 31,
                            "query": "checkip.amazonaws.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "52.4.57.244",
                                "100.63.192.44",
                                "54.145.222.151",
                                "23.23.243.85",
                                "100.60.146.222",
                                "3.229.251.178",
                                "100.59.168.164",
                                "3.226.168.191"
                            ],
                            "response_time": 31,
                            "transaction_id": 62609
                        },
                        "transaction_id": 62609
                    },
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "XuNH06ABI3UnQyDOnKY2",
                    "orig_index": "aella-maltrace-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 92,
                    "outbytes_total": 96,
                    "outpkts_delta": 1,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 31,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790251074231,
                    "response_time": 31,
                    "score": 60,
                    "severity": 60,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "ad.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "10.11.1.1.2054140",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 61123,
                    "start_bucket_time": 1790250900000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790251503868,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "rare",
                        "detection_time": 423160,
                        "status": "New"
                    },
                    "stellar_da_input": 1763,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "7da45111-169d-4765-8ad2-05e8a985016c1790251503930-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790251074031,
                    "timestamp_utc": "2026-09-24T11:57:54.000Z",
                    "tos": 0,
                    "totalbytes": 351,
                    "totalpackets": 2,
                    "typical": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790251503930,
                    "xdr_event": {
                        "description": "In external traffic, a rarely seen exploit attempt with the IDS signature \"INFO External IP Lookup Domain in DNS Lookup (checkip .amazonaws .com)\" has been observed after 16 days of silence.",
                        "display_name": "Private to Public Exploit Anomaly",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_pub",
                        "scope": "External",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1190",
                            "name": "Exploit Public-Facing Application"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-09-24T09:12:37-03:00.

The user's current state is as follows:
Active Document: c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Login_Time_Anomaly_2296189_CJPPA20150819\analisis_soc.md (LANGUAGE_MARKDOWN)
Cursor is on line: 228
Other open documents:
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Login_Time_Anomaly_2296189_CJPPA20150819\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\Cloud_Drive_Data_Exfiltration_Anomaly_josemarin\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\02_Base_de_Conocimiento\plantillas_cierre_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Casos\145120_Palo_Alto_Networks_Cortex_XDR_route_exe_NB-RBARRETO\analisis_soc.md (LANGUAGE_MARKDOWN)
- c:\Users\kevinmoraes\Documents\soc-env\command_center.py (LANGUAGE_PYTHON)
</ADDITIONAL_METADATA>