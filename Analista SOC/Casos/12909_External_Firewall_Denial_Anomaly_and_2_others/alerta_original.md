=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "ed1e2eff-ef06-431e-840a-2cc8d0f6bbd21785679803928-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14816,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 178,
                    "aella_tuples": "192.168.169.142.96.45.45.45.853.4",
                    "anomaly_id": "KkHIwp8BI3UnQyDOGCqQ",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-FortiGuard",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.142"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785679203577,
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
                    "end_bucket_time": 1785679500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785679203577
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
                    "fidelity": 98.49,
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
                        "event_time": "2026-08-02 11:00:03",
                        "eventtime": "1785679203577071794",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "3476033725",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:00:03",
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
                    "orig_id": "KkHIwp8BI3UnQyDOGCqQ",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=11:00:03 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785679203577071794 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=17367 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=96.45.45.45 dstport=853 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3476033725 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785679316985,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "7e15352a-cac3-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.142",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:f5:49:a5",
                    "srcport": 17367,
                    "start_bucket_time": 1785679200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785679802960,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 482580,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3250,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "ed1e2eff-ef06-431e-840a-2cc8d0f6bbd21785679803928-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785679203577,
                    "timestamp_utc": "2026-08-02T14:00:03.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785679803928,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 178), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "ba5db0ad-4d43-4bad-823c-592d9918667e1785680103272-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14818,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 141,
                    "aella_tuples": "192.168.169.142.141.109.161.95.443.4",
                    "anomaly_id": "x0HMwp8BI3UnQyDO-Ut7",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-Web",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.142"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785679500958,
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
                    "end_bucket_time": 1785679800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785679500958
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 52,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 86.65,
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
                        "dstinetsvc": "Fortinet-Web",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-08-02 11:05:00",
                        "eventtime": "1785679500958485505",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-Web",
                        "sessionid": "3476339657",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:05:00",
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
                    "orig_id": "x0HMwp8BI3UnQyDO-Ut7",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=11:05:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785679500958485505 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=4691 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=141.109.161.95 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-Web\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3476339657 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-Web\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785679637871,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "7e15352a-cac3-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.142",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:f5:49:a5",
                    "srcport": 4691,
                    "start_bucket_time": 1785679500000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785680102281,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 461915,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3205,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "ba5db0ad-4d43-4bad-823c-592d9918667e1785680103272-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785679500958,
                    "timestamp_utc": "2026-08-02T14:05:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 8,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785680103272,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 141), compared to the typical number of blocks (#: 8), measured in a 5.0-minute interval.",
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
                "_id": "e8250d48-1da4-422c-99b0-f10bc35f9b9b1785683703597-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14825,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 187,
                    "aella_tuples": "192.168.169.142.96.45.46.46.853.4",
                    "anomaly_id": "JUIDw58BI3UnQyDO5sfN",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Fortinet-FortiGuard",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.142"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1785683110316,
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
                    "end_bucket_time": 1785683400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1785683110316
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
                    "fidelity": 97.76,
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
                        "event_time": "2026-08-02 12:05:10",
                        "eventtime": "1785683110315649003",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "3480018928",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "12:05:10",
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
                    "orig_id": "JUIDw58BI3UnQyDO5sfN",
                    "orig_index": "aella-adr-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-02 time=12:05:10 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1785683110315649003 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=24826 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=96.45.46.46 dstport=853 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=3480018928 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1785683235545,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "7e15352a-cac3-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.142",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "94:ff:3c:f5:49:a5",
                    "srcport": 24826,
                    "start_bucket_time": 1785683100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1785683702717,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462465,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3236,
                    "stellar_index_id": "aella-ser-2026.08.02-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "e8250d48-1da4-422c-99b0-f10bc35f9b9b1785683703597-YWVsbGEtc2VyLTIwMjYuMDguMDItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785683110316,
                    "timestamp_utc": "2026-08-02T15:05:10.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 10,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1785683703597,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 187), compared to the typical number of blocks (#: 10), measured in a 5.0-minute interval.",
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