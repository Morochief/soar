=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "767897c5-9dde-4011-b858-3d587e664d261784126402507-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11097,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 1105,
                    "aella_tuples": "192.168.169.25.186.16.19.203.80.4",
                    "anomaly_id": "NBQyZp8BI3UnQyDOn75t",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.25"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784125839518,
                    "dscp_name": "Best Effort",
                    "dstip": "186.16.19.203",
                    "dstip_asn": 23201,
                    "dstip_asn_org": "Telecel S.A.",
                    "dstip_domain_creation": "1999-03-03T05:00:00Z",
                    "dstip_geo": {
                        "city": "Lambaré",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.3438,
                        "longitude": -57.6079,
                        "region": "Central Department"
                    },
                    "dstip_geo_point": "-25.3438,-57.6079",
                    "dstip_host": "a2047.dscapi9.akamai.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "duration": 0,
                    "end_bucket_time": 1784126100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784125839518
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
                    "fidelity": 99.92,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Paraguay",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "event_time": "2026-07-15 11:30:40",
                        "eventtime": "1784125839518253916",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "52:05:57:35:e7:20",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "HTTP",
                        "sessionid": "1746728478",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:30:40",
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
                            "strvalue": "Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected"
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
                    "orig_id": "NBQyZp8BI3UnQyDOn75t",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=11:30:40 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784125839518253916 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.25 srcport=55702 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=186.16.19.203 dstport=80 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstcountry=\"Paraguay\" sessionid=1746728478 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"HTTP\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"52:05:57:35:e7:20\" srcmac=\"52:05:57:35:e7:20\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784126015667,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "52:05:57:35:e7:20.0.192.168.169.25",
                    "srcip": "192.168.169.25",
                    "srcip_assetid": "23ccd16e-05af-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.25",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "52:05:57:35:e7:20",
                    "srcport": 55702,
                    "start_bucket_time": 1784125800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784126402487,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 382111,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2809,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "767897c5-9dde-4011-b858-3d587e664d261784126402507-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784125839518,
                    "timestamp_utc": "2026-07-15T14:30:39.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 17,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784126402507,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.25 private) has actions blocked by a firewall too many times (#: 1105), compared to the typical number of blocks (#: 17), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "ce8ed782-ee01-4bd5-9b0f-c5545547fdf41784126702717-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11101,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 314,
                    "aella_tuples": "192.168.169.25.186.16.19.50.443.4",
                    "anomaly_id": "FRU2Zp8BI3UnQyDOlB9c",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Akamai-CDN",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.25"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784126100193,
                    "dscp_name": "Best Effort",
                    "dstip": "186.16.19.50",
                    "dstip_asn": 23201,
                    "dstip_asn_org": "Telecel S.A.",
                    "dstip_domain_creation": "1999-03-03T05:00:00Z",
                    "dstip_geo": {
                        "city": "Lambaré",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.3438,
                        "longitude": -57.6079,
                        "region": "Central Department"
                    },
                    "dstip_geo_point": "-25.3438,-57.6079",
                    "dstip_host": "a434.dscr.akamai.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1784126400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784126100193
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
                    "fidelity": 92.23,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Phone",
                        "dstcity": "Undefined",
                        "dstcountry": "Paraguay",
                        "dstinetsvc": "Akamai-CDN",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "4",
                        "event_time": "2026-07-15 11:35:01",
                        "eventtime": "1784126100193291109",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "52:05:57:35:e7:20",
                        "osname": "iOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Akamai-CDN",
                        "sessionid": "1747045359",
                        "srccountry": "Reserved",
                        "srchwvendor": "Apple",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "iPhone-SPS",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:35:01",
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
                            "strvalue": "Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected"
                        },
                        {
                            "name": "vwlname",
                            "strvalue": "Internet_Usuarios"
                        },
                        {
                            "name": "srcfamily",
                            "strvalue": "iPhone"
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
                    "orig_id": "FRU2Zp8BI3UnQyDOlB9c",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=11:35:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784126100193291109 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.25 srcname=\"iPhone-SPS\" srcport=56098 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=186.16.19.50 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Akamai-CDN\" dstcountry=\"Paraguay\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=4 sessionid=1747045359 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Akamai-CDN\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Apple\" devtype=\"Phone\" srcfamily=\"iPhone\" osname=\"iOS\" mastersrcmac=\"52:05:57:35:e7:20\" srcmac=\"52:05:57:35:e7:20\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784126272693,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "52:05:57:35:e7:20.0.192.168.169.25",
                    "srcip": "192.168.169.25",
                    "srcip_assetid": "23ccd16e-05af-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.25",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "52:05:57:35:e7:20",
                    "srcport": 56098,
                    "start_bucket_time": 1784126100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784126702703,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 422507,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3225,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "ce8ed782-ee01-4bd5-9b0f-c5545547fdf41784126702717-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784126100193,
                    "timestamp_utc": "2026-07-15T14:35:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 17,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784126702717,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.25 private) has actions blocked by a firewall too many times (#: 314), compared to the typical number of blocks (#: 17), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "78cd5443-9500-4ea0-9c68-94861b9ce7f71784127003337-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11109,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 1093,
                    "aella_tuples": "192.168.169.25.186.16.19.203.80.4",
                    "anomaly_id": "ohU7Zp8BI3UnQyDOUJIm",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.25"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784126434826,
                    "dscp_name": "Best Effort",
                    "dstip": "186.16.19.203",
                    "dstip_asn": 23201,
                    "dstip_asn_org": "Telecel S.A.",
                    "dstip_domain_creation": "1999-03-03T05:00:00Z",
                    "dstip_geo": {
                        "city": "Lambaré",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.3438,
                        "longitude": -57.6079,
                        "region": "Central Department"
                    },
                    "dstip_geo_point": "-25.3438,-57.6079",
                    "dstip_host": "a1520.dscc.akamai.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "duration": 0,
                    "end_bucket_time": 1784126700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784126434826
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
                    "fidelity": 99.92,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Phone",
                        "dstcountry": "Paraguay",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "event_time": "2026-07-15 11:40:35",
                        "eventtime": "1784126434826308566",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "52:05:57:35:e7:20",
                        "osname": "iOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "HTTP",
                        "sessionid": "1747447998",
                        "srccountry": "Reserved",
                        "srchwvendor": "Apple",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "iPhone-SPS",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:40:35",
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
                            "strvalue": "Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected"
                        },
                        {
                            "name": "vwlname",
                            "strvalue": "Internet_Usuarios"
                        },
                        {
                            "name": "srcfamily",
                            "strvalue": "iPhone"
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
                    "orig_id": "ohU7Zp8BI3UnQyDOUJIm",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=11:40:35 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784126434826308566 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.25 srcname=\"iPhone-SPS\" srcport=59347 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=186.16.19.203 dstport=80 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstcountry=\"Paraguay\" sessionid=1747447998 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"HTTP\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Apple\" devtype=\"Phone\" srcfamily=\"iPhone\" osname=\"iOS\" mastersrcmac=\"52:05:57:35:e7:20\" srcmac=\"52:05:57:35:e7:20\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784126580935,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "52:05:57:35:e7:20.0.192.168.169.25",
                    "srcip": "192.168.169.25",
                    "srcip_assetid": "23ccd16e-05af-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "192.168.169.25",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "52:05:57:35:e7:20",
                    "srcport": 59347,
                    "start_bucket_time": 1784126400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784127003328,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 413154,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3027,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "78cd5443-9500-4ea0-9c68-94861b9ce7f71784127003337-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784126434826,
                    "timestamp_utc": "2026-07-15T14:40:34.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 17,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784127003337,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.25 private) has actions blocked by a firewall too many times (#: 1093), compared to the typical number of blocks (#: 17), measured in a 5.0-minute interval.",
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