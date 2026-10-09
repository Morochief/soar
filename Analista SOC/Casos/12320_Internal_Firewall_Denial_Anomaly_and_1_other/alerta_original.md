=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "0780b5be-d984-450b-bb12-7e47352125d31784289002952-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14184,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 434,
                    "aella_tuples": "192.168.169.30.10.0.200.51.5150.4",
                    "anomaly_id": "haPib58BI3UnQyDOKYHt",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/5150",
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
                    "domain_creation": 1784288400991,
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
                    "dstport": 5150,
                    "duration": 0,
                    "end_bucket_time": 1784288700000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784288400991
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
                    "fidelity": 99.12,
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
                        "event_time": "2026-07-17 08:40:01",
                        "eventtime": "1784288400990566293",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "e4:60:17:7f:85:e6",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/5150",
                        "sessionid": "1932889302",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-MAZCONA",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "08:40:01",
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
                    "orig_id": "haPib58BI3UnQyDOKYHt",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=08:40:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784288400990566293 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.30 srcname=\"NB-MAZCONA\" srcport=62547 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.200.51 dstport=5150 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1932889302 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" service=\"tcp/5150\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" unauthuser=\"manuelazcona\" unauthusersource=\"kerberos\" mastersrcmac=\"e4:60:17:7f:85:e6\" srcmac=\"e4:60:17:7f:85:e6\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784288516542,
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
                    "srcport": 62547,
                    "start_bucket_time": 1784288400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784289002881,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 482660,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2656,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "0780b5be-d984-450b-bb12-7e47352125d31784289002952-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784288400991,
                    "timestamp_utc": "2026-07-17T11:40:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 61,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784289002951,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.30, name: nb-mazcona.technoma.local private) has had actions blocked by a firewall too many times (#: 434), compared to the typical number of blocks (#: 61), measured in a 5.0-minute interval.",
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
                "_id": "7b8e0026-5f1d-4b3f-8132-f99ababc48c01784289302622-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14193,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 417,
                    "aella_tuples": "192.168.169.30.10.0.200.51.5150.4",
                    "anomaly_id": "MKPmb58BI3UnQyDO59S1",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/5150",
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
                    "domain_creation": 1784288701073,
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
                    "dstport": 5150,
                    "duration": 0,
                    "end_bucket_time": 1784289000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784288701073
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
                    "fidelity": 98.86,
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
                        "event_time": "2026-07-17 08:45:00",
                        "eventtime": "1784288701072627862",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "e4:60:17:7f:85:e6",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/5150",
                        "sessionid": "1933117051",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-MAZCONA",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "08:45:00",
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
                    "orig_id": "MKPmb58BI3UnQyDO59S1",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-17 time=08:45:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784288701072627862 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.30 srcname=\"NB-MAZCONA\" srcport=60141 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.0.200.51 dstport=5150 dstintf=\"AWS-TECHNOMA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1933117051 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" user=\"MANUELAZCONA\" authserver=\"AD1\" service=\"tcp/5150\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" unauthuser=\"manuelazcona\" unauthusersource=\"kerberos\" mastersrcmac=\"e4:60:17:7f:85:e6\" srcmac=\"e4:60:17:7f:85:e6\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784288827033,
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
                    "srcport": 60141,
                    "start_bucket_time": 1784288700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784289302586,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 471910,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2747,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "7b8e0026-5f1d-4b3f-8132-f99ababc48c01784289302622-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784288701073,
                    "timestamp_utc": "2026-07-17T11:45:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 61,
                    "user": {
                        "name": "MANUELAZCONA"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784289302622,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 192.168.169.30, name: nb-mazcona.technoma.local private) has had actions blocked by a firewall too many times (#: 417), compared to the typical number of blocks (#: 61), measured in a 5.0-minute interval.",
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