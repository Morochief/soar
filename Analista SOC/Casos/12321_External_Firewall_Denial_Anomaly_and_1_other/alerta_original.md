=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "5b2c5bbf-e418-4d71-9dc4-cb744fc7c6c51784289003970-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14189,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 324,
                    "aella_tuples": "192.168.169.31.17.167.200.74.443.4",
                    "anomaly_id": "uaPjb58BI3UnQyDOYpbO",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Apple-Web",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.31"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784288482526,
                    "dscp_name": "Best Effort",
                    "dstip": "17.167.200.74",
                    "dstip_asn": 714,
                    "dstip_asn_org": "Apple Inc.",
                    "dstip_domain_creation": "1999-05-12T21:15:16Z",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "gsp85-ssl.ls2-apple.com.akadns.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1784288700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784288482526
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
                    "fidelity": 98.25,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-17",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcity": "Undefined",
                        "dstcountry": "United States",
                        "dstinetsvc": "Apple-Web",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-07-17 08:41:22",
                        "eventtime": "1784288482525967305",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "42:f2:0a:8a:1c:a1",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Apple-Web",
                        "sessionid": "1932950333",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "08:41:22",
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
                    "orig_id": "uaPjb58BI3UnQyDOYpbO",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=08:41:22 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784288482525967305 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.31 srcport=50164 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=17.167.200.74 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Apple-Web\" dstcountry=\"United States\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1932950333 proto=6 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Apple-Web\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"42:f2:0a:8a:1c:a1\" srcmac=\"42:f2:0a:8a:1c:a1\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784288598190,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "42:f2:0a:8a:1c:a1.0.192.168.169.31",
                    "srcip": "192.168.169.31",
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
                    "srcip_host": "192.168.169.31",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "42:f2:0a:8a:1c:a1",
                    "srcport": 50164,
                    "start_bucket_time": 1784288400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784289003178,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 402865,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3014,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "5b2c5bbf-e418-4d71-9dc4-cb744fc7c6c51784289003970-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784288482526,
                    "timestamp_utc": "2026-07-17T11:41:22.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 11,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784289003970,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.31 private) has actions blocked by a firewall too many times (#: 324), compared to the typical number of blocks (#: 11), measured in a 5.0-minute interval.",
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
                "_id": "9114bd3a-86f5-4b85-880f-ac05094c1c111784289303634-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14195,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 420,
                    "aella_tuples": "192.168.169.31.186.16.30.97.443.4",
                    "anomaly_id": "wKPnb58BI3UnQyDOqORY",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "Meta-Whatsapp",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.31"
                    ],
                    "detector_index": 1,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784288751885,
                    "dscp_name": "Best Effort",
                    "dstip": "186.16.30.97",
                    "dstip_asn": 23201,
                    "dstip_asn_org": "Telecel S.A.",
                    "dstip_domain_creation": "2009-02-20T00:48:09Z",
                    "dstip_geo": {
                        "city": "Lambaré",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.3438,
                        "longitude": -57.6079,
                        "region": "Central Department"
                    },
                    "dstip_geo_point": "-25.3438,-57.6079",
                    "dstip_host": "media.fasu6-2.fna.whatsapp.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "duration": 0,
                    "end_bucket_time": 1784289000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784288751885
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
                    "fidelity": 99.52,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-17",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Phone",
                        "dstcity": "Undefined",
                        "dstcountry": "Paraguay",
                        "dstinetsvc": "Meta-Whatsapp",
                        "dstintf": "port2",
                        "dstintfrole": "wan",
                        "dstregion": "Undefined",
                        "dstreputation": "5",
                        "event_time": "2026-07-17 08:45:51",
                        "eventtime": "1784288751885143800",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "42:f2:0a:8a:1c:a1",
                        "osname": "iOS",
                        "policyname": "Block_WIFI-Corp",
                        "policytype": "policy",
                        "poluuid": "0b94f7f4-d060-51f0-635b-34e653224fc4",
                        "rule_id": 214,
                        "service": "Meta-Whatsapp",
                        "sessionid": "1933164116",
                        "srccountry": "Reserved",
                        "srchwvendor": "Apple",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "srcswversion": "26.5.2",
                        "subtype": "forward",
                        "time": "08:45:51",
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
                    "orig_id": "wKPnb58BI3UnQyDOqORY",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=08:45:51 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784288751885143800 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.31 srcport=51603 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=186.16.30.97 dstport=443 dstintf=\"port2\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstinetsvc=\"Meta-Whatsapp\" dstcountry=\"Paraguay\" dstregion=\"Undefined\" dstcity=\"Undefined\" dstreputation=5 sessionid=1933164116 proto=17 action=\"deny\" policyid=214 policytype=\"policy\" poluuid=\"0b94f7f4-d060-51f0-635b-34e653224fc4\" policyname=\"Block_WIFI-Corp\" service=\"Meta-Whatsapp\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vwlid=1 vwlquality=\"Seq_num(1 port2 Internet), alive, sla(0x1), gid(2), num of pass(1), selected\" vwlname=\"Internet_Usuarios\" crscore=30 craction=131072 crlevel=\"high\" srchwvendor=\"Apple\" devtype=\"Phone\" srcfamily=\"iPhone\" osname=\"iOS\" srcswversion=\"26.5.2\" mastersrcmac=\"42:f2:0a:8a:1c:a1\" srcmac=\"42:f2:0a:8a:1c:a1\" srcserver=0",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784288876295,
                    "run_every": 5,
                    "severity": 40,
                    "src_tuples": "42:f2:0a:8a:1c:a1.0.192.168.169.31",
                    "srcip": "192.168.169.31",
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
                    "srcip_host": "192.168.169.31",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "42:f2:0a:8a:1c:a1",
                    "srcport": 51603,
                    "start_bucket_time": 1784288700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784289302714,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 422440,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3244,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "9114bd3a-86f5-4b85-880f-ac05094c1c111784289303634-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784288751885,
                    "timestamp_utc": "2026-07-17T11:45:51.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 11,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784289303634,
                    "xdr_event": {
                        "description": "In external traffic, a source host (IP/name: 192.168.169.31 private) has actions blocked by a firewall too many times (#: 420), compared to the typical number of blocks (#: 11), measured in a 5.0-minute interval.",
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