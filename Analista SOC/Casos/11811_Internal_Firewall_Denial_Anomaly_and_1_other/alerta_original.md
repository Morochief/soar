=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "e36521ba-784f-4c1d-90d6-8d4bbbfe1b391783518303762-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4879,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 152,
                    "aella_tuples": "192.168.169.58.10.0.14.200.1900.4",
                    "anomaly_id": "tbzzQZ8BBi0xHyA-JBP4",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "MMS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "nb-ncristaldo.technoma.local"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1783517731643,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.0.14.200",
                    "dstip": "10.0.14.200",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.0.14.200",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 1900,
                    "duration": 0,
                    "end_bucket_time": 1783518000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783517731643
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 68,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 87.03,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "AD1",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-08",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "AWS-TECHNOMA-2",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-08 10:35:32",
                        "eventtime": "1783517731642916284",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "70:d8:23:5b:67:3d",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "MMS",
                        "sessionid": "1071601069",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-NCRISTALDO",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:35:32",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "unauthuser": "nestorcristaldo",
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
                    "orig_id": "tbzzQZ8BBi0xHyA-JBP4",
                    "orig_index": "aella-adr-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-08 time=10:35:32 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783517731642916284 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.58 srcname=\"NB-NCRISTALDO   \" srcport=54741 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.14.200 dstport=1900 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1071601069 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"NESTORCRISTALDO\" authserver=\"AD1\" service=\"MMS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" unauthuser=\"nestorcristaldo\" unauthusersource=\"kerberos\" mastersrcmac=\"70:d8:23:5b:67:3d\" srcmac=\"70:d8:23:5b:67:3d\" srcserver=0",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1783517872903,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "70:d8:23:5b:67:3d.0.192.168.169.58",
                    "srcip": "192.168.169.58",
                    "srcip_assetid": "32cd0f10-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ncristaldo.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "70:d8:23:5b:67:3d",
                    "srcport": 54741,
                    "start_bucket_time": 1783517700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783518302823,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421993,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2709,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "e36521ba-784f-4c1d-90d6-8d4bbbfe1b391783518303762-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783517731643,
                    "timestamp_utc": "2026-07-08T13:35:31.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 21,
                    "user": {
                        "name": "NESTORCRISTALDO"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783518303762,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.58, name: nb-ncristaldo.technoma.local private) has had actions blocked by a firewall too many times (#: 152), compared to the typical number of blocks (#: 21), measured in a 5.0-minute interval.",
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
                "_id": "24d64ccf-621c-4df8-8ee2-736892b9d0f61783518604576-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4911,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 148,
                    "aella_tuples": "192.168.169.58.10.0.14.200.80.4",
                    "anomaly_id": "A7z3QZ8BBi0xHyA-bJYb",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "nb-ncristaldo.technoma.local"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1783518011761,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.0.14.200",
                    "dstip": "10.0.14.200",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.0.14.200",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "duration": 0,
                    "end_bucket_time": 1783518300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783518011761
                    },
                    "event_category": "network",
                    "event_name": "fw_action",
                    "event_score": 50,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_action": []
                    },
                    "event_type": "conn",
                    "fidelity": 35.13,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "AD1",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-08",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "AWS-TECHNOMA-2",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-08 10:40:12",
                        "eventtime": "1783518011760676471",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "70:d8:23:5b:67:3d",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "HTTP",
                        "sessionid": "1071992541",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-NCRISTALDO",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "10:40:12",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "unauthuser": "nestorcristaldo",
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
                    "orig_id": "A7z3QZ8BBi0xHyA-bJYb",
                    "orig_index": "aella-adr-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-08 time=10:40:12 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783518011760676471 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.58 srcname=\"NB-NCRISTALDO   \" srcport=51969 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.14.200 dstport=80 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1071992541 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" user=\"NESTORCRISTALDO\" authserver=\"AD1\" service=\"HTTP\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" unauthuser=\"nestorcristaldo\" unauthusersource=\"kerberos\" mastersrcmac=\"70:d8:23:5b:67:3d\" srcmac=\"70:d8:23:5b:67:3d\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783518158505,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "70:d8:23:5b:67:3d.0.192.168.169.58",
                    "srcip": "192.168.169.58",
                    "srcip_assetid": "32cd0f10-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ncristaldo.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "70:d8:23:5b:67:3d",
                    "srcport": 51969,
                    "start_bucket_time": 1783518000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783518603825,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 442678,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2706,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "24d64ccf-621c-4df8-8ee2-736892b9d0f61783518604576-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783518011761,
                    "timestamp_utc": "2026-07-08T13:40:11.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 21,
                    "user": {
                        "name": "NESTORCRISTALDO"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783518604576,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.58, name: nb-ncristaldo.technoma.local private) has had actions blocked by a firewall too many times (#: 148), compared to the typical number of blocks (#: 21), measured in a 5.0-minute interval.",
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