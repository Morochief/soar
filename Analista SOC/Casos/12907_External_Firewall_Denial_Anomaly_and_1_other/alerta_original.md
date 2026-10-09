=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "82b6426e-d961-4198-b6c9-0e9749194bb51785672936007-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14805,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 214,
                    "aella_tuples": "192.168.169.131.173.243.143.6.443.4",
                    "anomaly_id": "gD5fwp8BI3UnQyDOG1Sw",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-FortiGuard",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.131"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785672308134,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.143.6",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_domain_creation": "2001-07-27T19:09:38Z",
                    "dstip_geo": {
                        "city": "Nepean",
                        "countryCode": "CA",
                        "countryName": "Canada",
                        "latitude": 45.2722,
                        "longitude": -75.7522,
                        "region": "Ontario"
                    },
                    "dstip_geo_point": "45.2722,-75.7522",
                    "dstip_host": "fctupdate.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785672600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785672308134
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 94.73,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-02",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcity": "Undefined",
                        "dstcountry": "United States",
                        "dstinetsvc": "Fortinet-FortiGuard",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-08-02 09:05:07",
                        "eventtime": "1785672308134125850",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "3468836696",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "09:05:07",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "1"
                    },
                    "fw_policy_id": "FG-Technoma_214",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "lateral": false,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_data": [
                        {
                            "name": "vwlquality",
                            "strvalue": "Seq_num(1 port2 Internet), alive, selected"
                        },
                        {
                            "name": "vwlname",
                            "strvalue": "Internet_Usuarios"
                        },
                        {
                            "name": "srcfamily",
                            "strvalue": "FortiGate"
                        },
                        {
                            "name": "srchwversion",
                            "strvalue": "40F"
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
                    "orig_id": "gD5fwp8BI3UnQyDOG1Sw",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=09:05:07 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785672308134125850 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=4621 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.143.6 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3468836696 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785672433306,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:d4:6c:51.0.192.168.169.131",
                    "srcip": "192.168.169.131",
                    "srcip_assetid": "7fee923e-852a-11f1-8b6c-36d860317dc9",
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
                    "srcip_host": "192.168.169.131",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:d4:6c:51",
                    "srcport": 4621,
                    "start_bucket_time": 1785672300000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785672935094,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 494835,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3252,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "82b6426e-d961-4198-b6c9-0e9749194bb51785672936007-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785672308134,
                    "timestamp_utc": "2026-08-02T12:05:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 10,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785672936007,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 214), compared to the typical number of blocks (#: 10), measured in a 5.0-minute interval.",
                        "display_name": "External Firewall Denial Anomaly",
                        "framework_version": "v8",
                        "name": "external_fw_action",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis",
                            "Firewall Anomalies"
                        ],
                        "technique": {
                            "id": "XT2002",
                            "name": "XDR Firewall Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "0365b92d-9eed-47cc-8789-45cbdf46e73e1785676203497-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14806,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 197,
                    "aella_tuples": "192.168.169.131.96.45.46.46.853.4",
                    "anomaly_id": "gj-Rwp8BI3UnQyDOdrFy",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-FortiGuard",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.131"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785675600825,
                    "dscp_name": "Best Effort",
                    "dstip": "96.45.46.46",
                    "dstip_asn": 16509,
                    "dstip_asn_org": "Amazon.com, Inc.",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "96.45.46.46",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 853,
                    "duration": 0,
                    "end_bucket_time": 1785675900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785675600825
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 98.88,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-02",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcity": "Undefined",
                        "dstcountry": "Canada",
                        "dstinetsvc": "Fortinet-FortiGuard",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-08-02 10:00:01",
                        "eventtime": "1785675600824783314",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "3472271661",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:00:01",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "1"
                    },
                    "fw_policy_id": "FG-Technoma_214",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "lateral": false,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_data": [
                        {
                            "name": "vwlquality",
                            "strvalue": "Seq_num(1 port2 Internet), alive, selected"
                        },
                        {
                            "name": "vwlname",
                            "strvalue": "Internet_Usuarios"
                        },
                        {
                            "name": "srcfamily",
                            "strvalue": "FortiGate"
                        },
                        {
                            "name": "srchwversion",
                            "strvalue": "40F"
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
                    "orig_id": "gj-Rwp8BI3UnQyDOdrFy",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=10:00:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785675600824783314 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=2980 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=96.45.46.46 dstport=853 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3472271661 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785675732744,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:d4:6c:51.0.192.168.169.131",
                    "srcip": "192.168.169.131",
                    "srcip_assetid": "7fee923e-852a-11f1-8b6c-36d860317dc9",
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
                    "srcip_host": "192.168.169.131",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:d4:6c:51",
                    "srcport": 2980,
                    "start_bucket_time": 1785675600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785676203464,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 463169,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3234,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "0365b92d-9eed-47cc-8789-45cbdf46e73e1785676203497-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785675600825,
                    "timestamp_utc": "2026-08-02T13:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 9,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785676203497,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 197), compared to the typical number of blocks (#: 9), measured in a 5.0-minute interval.",
                        "display_name": "External Firewall Denial Anomaly",
                        "framework_version": "v8",
                        "name": "external_fw_action",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis",
                            "Firewall Anomalies"
                        ],
                        "technique": {
                            "id": "XT2002",
                            "name": "XDR Firewall Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "1912a28f-527c-444d-8149-e3458414f2911785676502346-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14808,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 192,
                    "aella_tuples": "192.168.169.131.96.45.45.45.853.4",
                    "anomaly_id": "Gj-Wwp8BI3UnQyDOC9RK",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-FortiGuard",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.131"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785675904037,
                    "dscp_name": "Best Effort",
                    "dstip": "96.45.45.45",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "96.45.45.45",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 853,
                    "duration": 0,
                    "end_bucket_time": 1785676200000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785675904037
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 98.77,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-02",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcity": "Undefined",
                        "dstcountry": "United States",
                        "dstinetsvc": "Fortinet-FortiGuard",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-08-02 10:05:04",
                        "eventtime": "1785675904036970295",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "3472625211",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:05:04",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "1"
                    },
                    "fw_policy_id": "FG-Technoma_214",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "lateral": false,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_data": [
                        {
                            "name": "vwlquality",
                            "strvalue": "Seq_num(1 port2 Internet), alive, selected"
                        },
                        {
                            "name": "vwlname",
                            "strvalue": "Internet_Usuarios"
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
                    "orig_id": "Gj-Wwp8BI3UnQyDOC9RK",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=10:05:04 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785675904036970295 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=15169 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=96.45.45.45 dstport=853 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3472625211 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785676038172,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:d4:6c:51.0.192.168.169.131",
                    "srcip": "192.168.169.131",
                    "srcip_assetid": "7fee923e-852a-11f1-8b6c-36d860317dc9",
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
                    "srcip_host": "192.168.169.131",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:d4:6c:51",
                    "srcport": 15169,
                    "start_bucket_time": 1785675900000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785676502298,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 461935,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3044,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "1912a28f-527c-444d-8149-e3458414f2911785676502346-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785675904037,
                    "timestamp_utc": "2026-08-02T13:05:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 9,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785676502345,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 192), compared to the typical number of blocks (#: 9), measured in a 5.0-minute interval.",
                        "display_name": "External Firewall Denial Anomaly",
                        "framework_version": "v8",
                        "name": "external_fw_action",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis",
                            "Firewall Anomalies"
                        ],
                        "technique": {
                            "id": "XT2002",
                            "name": "XDR Firewall Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}

---------------------------------------------------------------------------
[+] MEMORIA SOAR: Logs de Interflow recuperados desde el caché RAM.