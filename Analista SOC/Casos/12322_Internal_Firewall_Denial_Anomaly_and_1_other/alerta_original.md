=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "31b77f34-62b2-45a2-ba2b-cebefc87f48b1784290202874-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14219,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 265,
                    "aella_tuples": "192.168.169.30.10.0.200.51.137.4",
                    "anomaly_id": "4KT1b58BI3UnQyDOPf56",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "udp/137",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "nb-mazcona.technoma.local"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784289620077,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.0.200.51",
                    "dstip": "10.0.200.51",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.0.200.51",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 137,
                    "duration": 0,
                    "end_bucket_time": 1784289900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784289620077
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 70,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 97.28,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "AD1",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-17",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "AWS-TECHNOMA-2",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-17 09:00:20",
                        "eventtime": "1784289620077241449",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "e4:60:17:7f:85:e6",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "udp/137",
                        "sessionid": "1933972161",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-MAZCONA",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "09:00:20",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "unauthuser": "manuelazcona",
                        "unauthusersource": "kerberos",
                        "vd": "root",
                        "vpntype": "ipsecvpn"
                    },
                    "fw_policy_id": "FG-Technoma_0",
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
                    "orig_id": "4KT1b58BI3UnQyDOPf56",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=09:00:20 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784289620077241449 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.30 srcname=\"NB-MAZCONA\" srcport=137 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.200.51 dstport=137 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1933972161 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"MANUELAZCONA\" authserver=\"AD1\" service=\"udp/137\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" unauthuser=\"manuelazcona\" unauthusersource=\"kerberos\" mastersrcmac=\"e4:60:17:7f:85:e6\" srcmac=\"e4:60:17:7f:85:e6\" srcserver=0",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784289766508,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "e4:60:17:7f:85:e6.0.192.168.169.30",
                    "srcip": "192.168.169.30",
                    "srcip_assetid": "73099234-da77-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "nb-mazcona.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "e4:60:17:7f:85:e6",
                    "srcport": 137,
                    "start_bucket_time": 1784289600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784290202858,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 432533,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2740,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "31b77f34-62b2-45a2-ba2b-cebefc87f48b1784290202874-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784289620077,
                    "timestamp_utc": "2026-07-17T12:00:20.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 33,
                    "user": {
                        "name": "MANUELAZCONA"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784290202874,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.30, name: nb-mazcona.technoma.local private) has had actions blocked by a firewall too many times (#: 265), compared to the typical number of blocks (#: 33), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "84a63fa5-90c5-48a4-9f04-27d9bec4f2671784290803242-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14238,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 276,
                    "aella_tuples": "192.168.169.30.10.0.200.51.137.4",
                    "anomaly_id": "lKX9b58BI3UnQyDO8cxc",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "udp/137",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "nb-rzabala.technoma.local"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784290200972,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.0.200.51",
                    "dstip": "10.0.200.51",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.0.200.51",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 137,
                    "duration": 0,
                    "end_bucket_time": 1784290500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784290200972
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
                    "fidelity": 98.17,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-17",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "AWS-TECHNOMA-2",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-17 09:10:00",
                        "eventtime": "1784290200971804398",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "e4:60:17:7f:85:e6",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "udp/137",
                        "sessionid": "1934672307",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-MAZCONA",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "09:10:00",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "unauthuser": "manuelazcona",
                        "unauthusersource": "kerberos",
                        "vd": "root",
                        "vpntype": "ipsecvpn"
                    },
                    "fw_policy_id": "FG-Technoma_0",
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
                    "orig_id": "lKX9b58BI3UnQyDO8cxc",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=09:10:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784290200971804398 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.30 srcname=\"NB-MAZCONA\" srcport=137 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.200.51 dstport=137 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1934672307 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" service=\"udp/137\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" unauthuser=\"manuelazcona\" unauthusersource=\"kerberos\" mastersrcmac=\"e4:60:17:7f:85:e6\" srcmac=\"e4:60:17:7f:85:e6\" srcserver=0",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1784290336796,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "e4:60:17:7f:85:e6.0.192.168.169.30",
                    "srcip": "192.168.169.30",
                    "srcip_assetid": "73099234-da77-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "nb-rzabala.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "e4:60:17:7f:85:e6",
                    "srcport": 137,
                    "start_bucket_time": 1784290200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784290803218,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462829,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2649,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "84a63fa5-90c5-48a4-9f04-27d9bec4f2671784290803242-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784290200972,
                    "timestamp_utc": "2026-07-17T12:10:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 33,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784290803242,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.30, name: nb-rzabala.technoma.local private) has had actions blocked by a firewall too many times (#: 276), compared to the typical number of blocks (#: 33), measured in a 5.0-minute interval.",
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
            }
        ]
    }
}