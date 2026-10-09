=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "b98e4894-844d-48f7-91db-f2c25f1492651787497804404-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5144,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 190,
                    "aella_tuples": "192.168.169.142.173.243.132.25.443.4",
                    "anomaly_id": "-H4jL6ABI3UnQyDOeelE",
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
                    "domain_creation": 1787497200901,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.132.25",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_domain_creation": "2001-07-27T19:09:38Z",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "globallogctrl.fortinet.net.geo.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1787497500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1787497200901
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
                    "fidelity": 97.75,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-23",
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
                        "event_time": "2026-08-23 12:00:00",
                        "eventtime": "1787497200901041581",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "1169971584",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "12:00:00",
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
                    "orig_id": "-H4jL6ABI3UnQyDOeelE",
                    "orig_index": "aella-adr-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-23 time=12:00:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1787497200901041581 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=18856 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.132.25 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"Canada\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1169971584 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1787497241840,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "2cd21d4e-852c-11f1-8b6c-36d860317dc9",
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
                    "srcport": 18856,
                    "start_bucket_time": 1787497200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1787497803749,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 555214,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3242,
                    "stellar_index_id": "aella-ser-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "b98e4894-844d-48f7-91db-f2c25f1492651787497804404-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1787497200901,
                    "timestamp_utc": "2026-08-23T15:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 11,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1787497804404,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 190), compared to the typical number of blocks (#: 11), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "e59c2f2e-71e4-4c02-9055-b0dd214e529e1787498103633-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5146,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 232,
                    "aella_tuples": "192.168.169.142.173.243.143.6.443.4",
                    "anomaly_id": "dX8oL6ABI3UnQyDONA1h",
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
                    "domain_creation": 1787497500578,
                    "dscp_name": "Best Effort",
                    "dstip": "173.243.143.6",
                    "dstip_asn": 40934,
                    "dstip_asn_org": "Fortinet Inc.",
                    "dstip_domain_creation": "2001-07-27T19:09:38Z",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "globalfctupdate.fortinet.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1787497800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1787497500578
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
                    "fidelity": 99.09,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-23",
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
                        "event_time": "2026-08-23 12:05:00",
                        "eventtime": "1787497500578168554",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "1170258212",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "12:05:00",
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
                    "orig_id": "dX8oL6ABI3UnQyDONA1h",
                    "orig_index": "aella-adr-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-23 time=12:05:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1787497500578168554 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=18321 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=173.243.143.6 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1170258212 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1787497550544,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "2cd21d4e-852c-11f1-8b6c-36d860317dc9",
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
                    "srcport": 18321,
                    "start_bucket_time": 1787497500000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1787498103140,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 544651,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3254,
                    "stellar_index_id": "aella-ser-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "e59c2f2e-71e4-4c02-9055-b0dd214e529e1787498103633-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1787497500578,
                    "timestamp_utc": "2026-08-23T15:05:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 11,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1787498103633,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 232), compared to the typical number of blocks (#: 11), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.08.18-000031",
                "_type": "_doc",
                "_id": "22865306-494c-4a29-a024-89bd18dde1c61787498402543-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 5147,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 174,
                    "aella_tuples": "192.168.169.142.96.45.45.45.853.4",
                    "anomaly_id": "_H8tL6ABI3UnQyDOFjF5",
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
                    "domain_creation": 1787497800748,
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
                    "end_bucket_time": 1787498100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1787497800748
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
                    "fidelity": 94.43,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-08-23",
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
                        "event_time": "2026-08-23 12:10:00",
                        "eventtime": "1787497800748200225",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "94:ff:3c:f5:49:a5",
                        "osname": "FortiOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Fortinet-FortiGuard",
                        "sessionid": "1170545383",
                        "srccountry": "Reserved",
                        "srchwvendor": "Fortinet",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "12:10:00",
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
                    "orig_id": "_H8tL6ABI3UnQyDOFjF5",
                    "orig_index": "aella-adr-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-08-23 time=12:10:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1787497800748200225 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.142 srcport=7105 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=96.45.45.45 dstport=853 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Fortinet-FortiGuard\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1170545383 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Fortinet-FortiGuard\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Fortinet\" devtype=\"Router\" srcfamily=\"FortiGate\" osname=\"FortiOS\" srchwversion=\"40F\" mastersrcmac=\"94:ff:3c:f5:49:a5\" srcmac=\"94:ff:3c:f5:49:a5\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1787497865719,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "94:ff:3c:f5:49:a5.0.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "2cd21d4e-852c-11f1-8b6c-36d860317dc9",
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
                    "srcport": 7105,
                    "start_bucket_time": 1787497800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1787498402506,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 523945,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3248,
                    "stellar_index_id": "aella-ser-2026.08.23-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "22865306-494c-4a29-a024-89bd18dde1c61787498402543-YWVsbGEtc2VyLTIwMjYuMDguMjMtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1787497800748,
                    "timestamp_utc": "2026-08-23T15:10:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 11,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1787498402543,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.142 private) has actions blocked by a firewall too many times (#: 174), compared to the typical number of blocks (#: 11), measured in a 5.0-minute interval.",
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