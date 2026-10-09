=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "cb7be255-f78a-45b2-b37b-13ce05bce0b81785071402975-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6592,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 207,
                    "aella_tuples": "192.168.169.131.141.109.161.95.443.4",
                    "anomaly_id": "cKeEnp8BI3UnQyDOz_Es",
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
                    "domain_creation": 1785070804640,
                    "dscp_name": "Best Effort",
                    "dstip": "141.109.161.95",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_domain_creation": "2001-07-27T19:09:38Z",
                    "dstip_geo": {
                        "city": "Calgary",
                        "countryCode": "CA",
                        "countryName": "Canada",
                        "latitude": 51.0455,
                        "longitude": -114.1988,
                        "region": "Alberta"
                    },
                    "dstip_geo_point": "51.0455,-114.1988",
                    "dstip_host": "globalproductapi.fortinet.net.geo.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785071100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785070804640
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
                    "fidelity": 99.08,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-26",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcity": "Undefined",
                        "dstcountry": "Canada",
                        "dstinetsvc": "Fortinet-FortiGuard",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-07-26 10:00:05",
                        "eventtime": "1785070804639526919",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "2816972419",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:00:05",
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
                    "orig_id": "cKeEnp8BI3UnQyDOz_Es",
                    "orig_index": "aella-adr-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-26 time=10:00:05 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785070804639526919 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=21490 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=141.109.161.95 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=2816972419 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785070925648,
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
                    "srcport": 21490,
                    "start_bucket_time": 1785070800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785071402958,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 472409,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3101,
                    "stellar_index_id": "aella-ser-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "cb7be255-f78a-45b2-b37b-13ce05bce0b81785071402975-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785070804640,
                    "timestamp_utc": "2026-07-26T13:00:04.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785071402975,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 207), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "0a905a74-3693-4f27-90c5-7d029fdf126e1785071702353-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6597,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 171,
                    "aella_tuples": "192.168.169.131.173.243.132.25.443.4",
                    "anomaly_id": "z6iJnp8BI3UnQyDOhxCH",
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
                    "domain_creation": 1785071101260,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.132.25",
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
                    "dstip_host": "globallogctrl.fortinet.net.geo.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785071400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785071101260
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
                    "fidelity": 98.04,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-26",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcity": "Undefined",
                        "dstcountry": "Canada",
                        "dstinetsvc": "Fortinet-FortiGuard",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-07-26 10:05:01",
                        "eventtime": "1785071101259604450",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "2817333295",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:05:01",
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
                    "orig_id": "z6iJnp8BI3UnQyDOhxCH",
                    "orig_index": "aella-adr-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-26 time=10:05:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785071101259604450 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=20942 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.132.25 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=2817333295 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785071236523,
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
                    "srcport": 20942,
                    "start_bucket_time": 1785071100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785071702300,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 461931,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3101,
                    "stellar_index_id": "aella-ser-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "0a905a74-3693-4f27-90c5-7d029fdf126e1785071702353-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785071101260,
                    "timestamp_utc": "2026-07-26T13:05:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785071702353,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 171), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "2f4d5509-0f77-4fdb-94dc-5102050dc9541785075002842-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6635,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 172,
                    "aella_tuples": "192.168.169.131.173.243.143.6.443.4",
                    "anomaly_id": "-qm7np8BI3UnQyDOuX57",
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
                    "domain_creation": 1785074400418,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.143.6",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_geo": {
                        "city": "Nepean",
                        "countryCode": "CA",
                        "countryName": "Canada",
                        "latitude": 45.2722,
                        "longitude": -75.7522,
                        "region": "Ontario"
                    },
                    "dstip_geo_point": "45.2722,-75.7522",
                    "dstip_host": "173.243.143.6",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785074700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785074400418
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
                    "fidelity": 98.32,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-26",
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
                        "event_time": "2026-07-26 11:00:01",
                        "eventtime": "1785074400418433383",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "2820970601",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:00:01",
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
                    "orig_id": "-qm7np8BI3UnQyDOuX57",
                    "orig_index": "aella-adr-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-26 time=11:00:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785074400418433383 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=18227 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.143.6 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=2820970601 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785074528768,
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
                    "srcport": 18227,
                    "start_bucket_time": 1785074400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785075002780,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 472506,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3322,
                    "stellar_index_id": "aella-ser-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "2f4d5509-0f77-4fdb-94dc-5102050dc9541785075002842-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785074400418,
                    "timestamp_utc": "2026-07-26T14:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785075002842,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 172), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "188749bd-5b87-4691-918e-6937147cea8d1785075302329-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6640,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 197,
                    "aella_tuples": "192.168.169.131.173.243.132.25.443.4",
                    "anomaly_id": "DanAnp8BI3UnQyDOdKGf",
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
                    "domain_creation": 1785074702016,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.132.25",
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
                    "dstip_host": "globallogctrl.fortinet.net.geo.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785075000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785074702016
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
                    "fidelity": 98.98,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-26",
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
                        "event_time": "2026-07-26 11:05:02",
                        "eventtime": "1785074702015599372",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "2821291441",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:05:02",
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
                    "orig_id": "DanAnp8BI3UnQyDOdKGf",
                    "orig_index": "aella-adr-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-26 time=11:05:02 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785074702015599372 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=21433 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.132.25 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=2821291441 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785074835785,
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
                    "srcport": 21433,
                    "start_bucket_time": 1785074700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785075302308,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462013,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3310,
                    "stellar_index_id": "aella-ser-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "188749bd-5b87-4691-918e-6937147cea8d1785075302329-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785074702016,
                    "timestamp_utc": "2026-07-26T14:05:02.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785075302329,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 197), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "bf6a0465-9284-485c-a801-7c75ef1044851785078603361-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6676,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 172,
                    "aella_tuples": "192.168.169.131.173.243.132.25.443.4",
                    "anomaly_id": "lqrynp8BI3UnQyDOqf8W",
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
                    "domain_creation": 1785078000453,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.132.25",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_geo": {
                        "city": "Nepean",
                        "countryCode": "CA",
                        "countryName": "Canada",
                        "latitude": 45.2722,
                        "longitude": -75.7522,
                        "region": "Ontario"
                    },
                    "dstip_geo_point": "45.2722,-75.7522",
                    "dstip_host": "173.243.132.25",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1785078300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785078000453
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
                    "fidelity": 95.89,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-26",
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
                        "event_time": "2026-07-26 12:00:01",
                        "eventtime": "1785078000452874911",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:d4:6c:51",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "2824804208",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "12:00:01",
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
                    "orig_id": "lqrynp8BI3UnQyDOqf8W",
                    "orig_index": "aella-adr-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-26 time=12:00:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785078000452874911 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.131 srcport=21832 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.132.25 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=2824804208 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:d4:6c:51\" srcmac=\"94:ff:3c:d4:6c:51\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785078124080,
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
                    "srcport": 21832,
                    "start_bucket_time": 1785078000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785078603306,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 473032,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3310,
                    "stellar_index_id": "aella-ser-2026.07.26-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "bf6a0465-9284-485c-a801-7c75ef1044851785078603361-YWVsbGEtc2VyLTIwMjYuMDcuMjYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785078000453,
                    "timestamp_utc": "2026-07-26T15:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 9,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785078603361,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.131 private) has actions blocked by a firewall too many times (#: 172), compared to the typical number of blocks (#: 9), measured in a 5.0-minute interval.",
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