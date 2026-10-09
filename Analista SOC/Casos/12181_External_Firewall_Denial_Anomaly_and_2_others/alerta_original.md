=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "9b1cb78f-f166-4288-915a-5b7c6f657cf51784123403457-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11060,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 623,
                    "aella_tuples": "192.168.169.19.186.16.19.19.443.4",
                    "anomaly_id": "JhAEZp8BI3UnQyDOOkgR",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Akamai-CDN",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.19"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784122833581,
                    "dscp_name": "Best Effort",
                    "dstip": "186.16.19.19",
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
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1784123100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784122833581
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
                    "fidelity": 99.83,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcity": "Undefined",
                        "dstcountry": "Paraguay",
                        "dstinetsvc": "Akamai-CDN",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "4",
                        "event_time": "2026-07-15 10:40:34",
                        "eventtime": "1784122833581183299",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "fe:a6:14:7a:32:28",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Akamai-CDN",
                        "sessionid": "1743038571",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:40:34",
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
                    "orig_id": "JhAEZp8BI3UnQyDOOkgR",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=10:40:34 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784122833581183299 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.19 srcport=57696 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=186.16.19.19 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Akamai-CDN\" dstcountry=\"Paraguay\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=4 sessionid=1743038571 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Akamai-CDN\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"fe:a6:14:7a:32:28\" srcmac=\"fe:a6:14:7a:32:28\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784122973662,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "fe:a6:14:7a:32:28.0.192.168.169.19",
                    "srcip": "192.168.169.19",
                    "srcip_assetid": "3356040a-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.19",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "fe:a6:14:7a:32:28",
                    "srcport": 57696,
                    "start_bucket_time": 1784122800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784123403418,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 423190,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3007,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "9b1cb78f-f166-4288-915a-5b7c6f657cf51784123403457-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784122833581,
                    "timestamp_utc": "2026-07-15T13:40:33.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 18,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784123403457,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.19 private) has actions blocked by a firewall too many times (#: 623), compared to the typical number of blocks (#: 18), measured in a 5.0-minute interval.",
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
                "_id": "c6cbea34-a9a0-46d2-b57f-24e087c485d41784124305627-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11072,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 769,
                    "aella_tuples": "192.168.169.19.151.101.3.6.443.4",
                    "anomaly_id": "MxERZp8BI3UnQyDOz6I9",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Apple-App.Store",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.19"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784123702191,
                    "dscp_name": "Best Effort",
                    "dstip": "151.101.3.6",
                    "dstip_asn": 54113,
                    "dstip_asn_org": "Fastly, Inc.",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "151.101.3.6",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1784124000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784123702191
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
                    "fidelity": 99.88,
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
                        "dstcountry": "United States",
                        "dstinetsvc": "Apple-App.Store",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-07-15 10:55:02",
                        "eventtime": "1784123702191377789",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "fe:a6:14:7a:32:28",
                        "osname": "iOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Apple-App.Store",
                        "sessionid": "1744094603",
                        "srccountry": "Reserved",
                        "srchwvendor": "Apple",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "iPhone",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:55:02",
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
                    "orig_id": "MxERZp8BI3UnQyDOz6I9",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=10:55:02 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784123702191377789 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.19 srcname=\"iPhone\" srcport=60539 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=151.101.3.6 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Apple-App.Store\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1744094603 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Apple-App.Store\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Apple\" devtype=\"Phone\" srcfamily=\"iPhone\" osname=\"iOS\" mastersrcmac=\"fe:a6:14:7a:32:28\" srcmac=\"fe:a6:14:7a:32:28\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784123860048,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "fe:a6:14:7a:32:28.0.192.168.169.19",
                    "srcip": "192.168.169.19",
                    "srcip_assetid": "3356040a-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.19",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "fe:a6:14:7a:32:28",
                    "srcport": 60539,
                    "start_bucket_time": 1784123700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784124305476,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 435275,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3250,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "c6cbea34-a9a0-46d2-b57f-24e087c485d41784124305627-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784123702191,
                    "timestamp_utc": "2026-07-15T13:55:02.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 18,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784124305627,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.19 private) has actions blocked by a firewall too many times (#: 769), compared to the typical number of blocks (#: 18), measured in a 5.0-minute interval.",
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
                "_id": "95a0f879-829e-4f52-a186-36e7955b35511784124302773-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 11071,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 1,
                    "aella_tuples": "192.168.169.19.192.168.40.133.7000.4",
                    "anomaly_id": "RxIVZp8BI3UnQyDOyQ4j",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "VDOLIVE",
                    "appid_stdport": "yes",
                    "days_silent": 20,
                    "detected_fields": [
                        "fw_policy_id"
                    ],
                    "detected_values": [
                        "FG-Technoma_214"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784123978988,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.40.133",
                    "dstip": "192.168.40.133",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "192.168.40.133",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7000,
                    "duration": 0,
                    "end_bucket_time": 1784124000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784123978988
                    },
                    "event_category": "network",
                    "event_name": "fw_policy_id",
                    "event_score": 37,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_policy": []
                    },
                    "event_type": "conn",
                    "fidelity": 31.95,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-15",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "event_time": "2026-07-15 10:59:39",
                        "eventtime": "1784123978988325247",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "fe:a6:14:7a:32:28",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "VDOLIVE",
                        "sessionid": "1744433473",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:59:39",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "1"
                    },
                    "fw_policy_id": "FG-Technoma_214",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "lateral": true,
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
                    "orig_id": "RxIVZp8BI3UnQyDOyQ4j",
                    "orig_index": "aella-adr-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-15 time=10:59:39 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784123978988325247 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.19 srcport=57084 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=192.168.40.133 dstport=7000 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1744433473 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"VDOLIVE\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"fe:a6:14:7a:32:28\" srcmac=\"fe:a6:14:7a:32:28\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784124129862,
                    "severity": 40,
                    "src_tuples": "fe:a6:14:7a:32:28.0.192.168.169.19",
                    "srcip": "192.168.169.19",
                    "srcip_assetid": "3356040a-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.19",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "fe:a6:14:7a:32:28",
                    "srcport": 57084,
                    "start_bucket_time": 1784123700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784124302731,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 172053,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2824,
                    "stellar_index_id": "aella-ser-2026.07.15-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "95a0f879-829e-4f52-a186-36e7955b35511784124302773-YWVsbGEtc2VyLTIwMjYuMDcuMTUtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784123978988,
                    "timestamp_utc": "2026-07-15T13:59:38.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 0,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784124302773,
                    "xdr_event": {
                        "description": "In internal traffic, the connection from IP/name: 192.168.169.19 (private) to IP/name: 192.168.40.133 (private) has triggered a policy (ID: \"FG-Technoma_214\") that has never been observed by Stellar Cyber before (or been seen very rarely) on the firewall (type: \"fw_fortigate\") after 20 days of silence.",
                        "display_name": "Internal Firewall Policy Anomaly",
                        "framework_version": "v8",
                        "name": "internal_fw_policy_id",
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
            }
        ]
    }
}