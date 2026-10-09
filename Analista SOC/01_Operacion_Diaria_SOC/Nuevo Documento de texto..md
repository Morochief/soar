=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.06.19-000027",
                "_type": "_doc",
                "_id": "23480192-a5de-4d7d-b899-9c7621970b1a1782551401882-YWVsbGEtc2VyLTIwMjYuMDYuMjctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 2,
                "_seq_no": 11417,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "info",
                    "actual": 14,
                    "aella_tuples": "147.182.241.81.10.11.3.196.443.4",
                    "anomaly_id": "_StTCJ8Bp04rSdVkizfN",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "SSL",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "147.182.241.81"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1782551084192,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.3.196",
                    "dstip": "10.11.3.196",
                    "dstip_assetid": "3317f000-d78c-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.11.3.196",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "end_bucket_time": 1782551100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1782551084192,
                        "utm": {
                            "feature": "ssl"
                        }
                    },
                    "event_category": "killchain",
                    "event_name": "scanner_rep",
                    "event_score": 33,
                    "event_source": "new_ml",
                    "event_status": "Closed",
                    "event_type": "reconn",
                    "fidelity": 81.73,
                    "fortinet": {
                        "date": "2026-06-27",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "DMZ Servers",
                        "dstintfrole": "lan",
                        "dstuuid": "336467fc-e4cd-51f0-0609-65d15b34d938",
                        "event_time": "2026-06-27 06:04:44",
                        "eventsubtype": "certificate-anomaly",
                        "eventtime": "1782551084191874269",
                        "eventtype": "ssl-anomaly",
                        "hostname": "190.104.178.146",
                        "level": "information",
                        "logid": "1700062307",
                        "msg": "Server certificate and SNI mismatched",
                        "policytype": "policy",
                        "poluuid": "c98b32b0-e4cd-51f0-f9ca-f18e6561c980",
                        "profile": "certificate-inspection",
                        "rule_id": 219,
                        "service": "SSL",
                        "sessionid": "1971331828",
                        "sni": "190.104.178.146",
                        "srccountry": "United States",
                        "srcintf": "port2",
                        "srcintfrole": "wan",
                        "srcuuid": "5979d106-ca16-51f0-0dc9-c378a1008977",
                        "subtype": "ssl",
                        "time": "06:04:44",
                        "tlsver": "tls1.2",
                        "type": "utm",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_219",
                    "lateral": false,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 190
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
                    "orig_id": "_StTCJ8Bp04rSdVkizfN",
                    "orig_index": "aella-adr-2026.06.27-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parser_raw_msg": "<190>date=2026-06-27 time=06:04:44 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1782551084191874269 tz=\"-0300\" logid=\"1700062307\" type=\"utm\" subtype=\"ssl\" eventtype=\"ssl-anomaly\" level=\"information\" vd=\"root\" action=\"info\" policyid=219 poluuid=\"c98b32b0-e4cd-51f0-f9ca-f18e6561c980\" policytype=\"policy\" sessionid=1971331828 service=\"SSL\" profile=\"certificate-inspection\" srcip=147.182.241.81 srcport=60696 srccountry=\"United States\" dstip=10.11.3.196 dstport=443 dstcountry=\"Reserved\" srcintf=\"port2\" srcintfrole=\"wan\" dstintf=\"DMZ Servers\" dstintfrole=\"lan\" srcuuid=\"5979d106-ca16-51f0-0dc9-c378a1008977\" dstuuid=\"336467fc-e4cd-51f0-0609-65d15b34d938\" proto=6 tlsver=\"tls1.2\" sni=\"190.104.178.146\" eventsubtype=\"certificate-anomaly\" msg=\"Server certificate and SNI mismatched\" hostname=\"190.104.178.146\"",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1782551112740,
                    "run_every": 5,
                    "severity": 20,
                    "srcip": "147.182.241.81",
                    "srcip_asn": 14061,
                    "srcip_asn_org": "DigitalOcean, LLC",
                    "srcip_geo": {
                        "city": "Santa Clara",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.3931,
                        "longitude": -121.962,
                        "region": "California"
                    },
                    "srcip_geo_point": "37.3931,-121.962",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "147.182.241.81",
                    "srcip_reputation": "Scanner",
                    "srcip_reputation_source": "ETPro",
                    "srcip_type": "public",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 60696,
                    "start_bucket_time": 1782550800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1782551401866,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 281236,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2615,
                    "stellar_index_id": "aella-ser-2026.06.27-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "23480192-a5de-4d7d-b899-9c7621970b1a1782551401882-YWVsbGEtc2VyLTIwMjYuMDYuMjctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 64,
                    "timestamp": 1782551084192,
                    "timestamp_utc": "2026-06-27T09:04:44.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 2,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1782551401882,
                    "xdr_event": {
                        "description": "An anomalously large number (#: 14) of connections has been observed from a host (\"IP/name: 147.182.241.81\") with a reputation category of Scanner. The typical number of connections is 2, measured in a 5.0-minute interval.",
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
                    },
                    "user_action": {
                        "last_user": "kevinmoraes@technoma.com.py",
                        "history": [
                            {
                                "action_user": "kevinmoraes@technoma.com.py",
                                "action_time": 1782557993868,
                                "action": "Status changed to Closed"
                            }
                        ],
                        "last_action": "Status changed to Closed",
                        "last_modified": 1782557993868
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.06.19-000027",
                "_type": "_doc",
                "_id": "d5ae641e-b34c-4e5d-8c76-e23feee13c7d1782555304616-YWVsbGEtc2VyLTIwMjYuMDYuMjctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 2,
                "_seq_no": 11418,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "dropped",
                    "actual": 1,
                    "aella_tuples": "138.197.87.21.10.11.3.196.80.4",
                    "anomaly_id": "pC2MCJ8Bp04rSdVkdSw7",
                    "anomaly_tag": "rare",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "days_silent": 23,
                    "detected_fields": [
                        "ips.signature"
                    ],
                    "detected_values": [
                        "Multiple.Routers.GPON.formLogin.Remote.Command.Injection"
                    ],
                    "dev_class": "ips",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "direction": "outgoing",
                    "domain_creation": 1782554743979,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.3.196",
                    "dstip": "10.11.3.196",
                    "dstip_assetid": "3317f000-d78c-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.11.3.196",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "end_bucket_time": 1782555000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1782554743979,
                        "utm": {
                            "feature": "ips"
                        }
                    },
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_pub_priv",
                    "event_score": 51,
                    "event_source": "new_ml",
                    "event_status": "Closed",
                    "event_summary": {
                        "dominant_severity": "high",
                        "ips": {
                            "action_count": {
                                "dropped": 1
                            },
                            "severity_count": {
                                "high": 1
                            }
                        },
                        "ips_signatures_summarize": [
                            {
                                "action": "dropped",
                                "id": "52588",
                                "ips_severity": "high",
                                "name": "Multiple.Routers.GPON.formLogin.Remote.Command.Injection"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 36.24,
                    "fortinet": {
                        "agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
                        "attackid": "52588",
                        "craction": "8192",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-06-27",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "DMZ Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-06-27 07:05:43",
                        "eventtime": "1782554743978702300",
                        "eventtype": "signature",
                        "hostname": "190.104.178.146",
                        "httpmethod": "POST",
                        "incidentserialno": "298081217",
                        "level": "alert",
                        "logid": "0419016384",
                        "msg": "applications3: Multiple.Routers.GPON.formLogin.Remote.Command.Injection",
                        "policytype": "policy",
                        "poluuid": "c98b32b0-e4cd-51f0-f9ca-f18e6561c980",
                        "profile": "IPS_Servidores",
                        "referralurl": "http://190.104.178.146:80/admin/login.asp",
                        "rule_id": 219,
                        "service": "HTTP",
                        "sessionid": "1975276193",
                        "severity": "high",
                        "srccountry": "United States",
                        "srcintf": "port2",
                        "srcintfrole": "wan",
                        "subtype": "ips",
                        "time": "07:05:43",
                        "type": "utm",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_219",
                    "ips": {
                        "action": "dropped",
                        "severity": "high",
                        "signature": "Multiple.Routers.GPON.formLogin.Remote.Command.Injection",
                        "signature_id": "52588"
                    },
                    "lateral": false,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 185
                        }
                    },
                    "msg_class": "ips",
                    "msg_data": [
                        {
                            "name": "ref",
                            "strvalue": "http://www.fortinet.com/ids/VID52588"
                        }
                    ],
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
                    "orig_id": "pC2MCJ8Bp04rSdVkdSw7",
                    "orig_index": "aella-maltrace-2026.06.27-e511c3fc54cd4d668bb67612c2ef4b04",
                    "parser_raw_msg": "<185>date=2026-06-27 time=07:05:43 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1782554743978702300 tz=\"-0300\" logid=\"0419016384\" type=\"utm\" subtype=\"ips\" eventtype=\"signature\" level=\"alert\" vd=\"root\" severity=\"high\" srcip=138.197.87.21 srccountry=\"United States\" dstip=10.11.3.196 dstcountry=\"Reserved\" srcintf=\"port2\" srcintfrole=\"wan\" dstintf=\"DMZ Servers\" dstintfrole=\"lan\" sessionid=1975276193 action=\"dropped\" proto=6 service=\"HTTP\" policyid=219 poluuid=\"c98b32b0-e4cd-51f0-f9ca-f18e6561c980\" policytype=\"policy\" attack=\"Multiple.Routers.GPON.formLogin.Remote.Command.Injection\" srcport=33942 dstport=80 hostname=\"190.104.178.146\" url=\"/boaform/admin/formLogin\" agent=\"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0\" httpmethod=\"POST\" referralurl=\"http://190.104.178.146:80/admin/login.asp\" direction=\"outgoing\" attackid=52588 profile=\"IPS_Servidores\" ref=\"http://www.fortinet.com/ids/VID52588\" incidentserialno=298081217 msg=\"applications3: Multiple.Routers.GPON.formLogin.Remote.Command.Injection\" crscore=30 craction=8192 crlevel=\"high\"",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1782554848445,
                    "severity": 60,
                    "srcip": "138.197.87.21",
                    "srcip_asn": 14061,
                    "srcip_asn_org": "DigitalOcean, LLC",
                    "srcip_geo": {
                        "city": "Clifton",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 40.8364,
                        "longitude": -74.1403,
                        "region": "New Jersey"
                    },
                    "srcip_geo_point": "40.8364,-74.1403",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "138.197.87.21",
                    "srcip_reputation": "Good",
                    "srcip_sig_id": "138.197.87.21.null",
                    "srcip_type": "public",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 33942,
                    "start_bucket_time": 1782554700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1782555304571,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "rare",
                        "detection_time": 453960,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3352,
                    "stellar_index_id": "aella-ser-2026.06.27-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "d5ae641e-b34c-4e5d-8c76-e23feee13c7d1782555304616-YWVsbGEtc2VyLTIwMjYuMDYuMjctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat": "Multiple.Routers.GPON.formLogin.Remote.Command.Injection",
                    "threat_score": 0,
                    "timestamp": 1782554743979,
                    "timestamp_utc": "2026-06-27T10:05:43.000Z",
                    "typical": 0,
                    "url": "/boaform/admin/formLogin",
                    "url_list": [
                        "/boaform/admin/formLogin"
                    ],
                    "url_reputation": "Good",
                    "url_reputation_source": "",
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1782555304616,
                    "xdr_event": {
                        "description": "In external traffic, a rarely seen exploit attempt with the IPS signature \"Multiple.Routers.GPON.formLogin.Remote.Command.Injection\" has been observed after 23 days of silence.",
                        "display_name": "Public to Private Exploit Anomaly",
                        "framework_version": "v8",
                        "name": "exploit_attempt_pub_priv",
                        "scope": "External",
                        "subtype": {
                            "display_name": "IPS Traffic Anomaly",
                            "name": "ips_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis",
                            "IPS Detection"
                        ],
                        "technique": {
                            "id": "T1190",
                            "name": "Exploit Public-Facing Application"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    },
                    "user_action": {
                        "last_user": "kevinmoraes@technoma.com.py",
                        "history": [
                            {
                                "action_user": "kevinmoraes@technoma.com.py",
                                "action_time": 1782557993868,
                                "action": "Status changed to Closed"
                            }
                        ],
                        "last_action": "Status changed to Closed",
                        "last_modified": 1782557993868
                    }
                }
            }
        ]
    }
}