# Alertas Originales Interflow / Stellar Cyber - Lote de 2 Eventos

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "49a8d5a6-8225-4f3f-a023-2bf0ad64df2a1790259903645-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19343,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 217,
                    "aella_tuples": "192.168.15.16.192.168.169.102.7680.4",
                    "anomaly_id": "5vXG06ABI3UnQyDO5tCr",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/7680",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.15.16"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790259308565,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.102",
                    "dstip": "192.168.169.102",
                    "dstip_assetid": "fe9206f2-cf7c-11f0-bc8a-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "nb-evera.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "ENRIQUEVERA",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1790259600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790259308565
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
                    "fidelity": 98.66,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "WiFi_Corp",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 11:15:08",
                        "eventtime": "1790259308565366951",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:6b:8d:ec:30:fa",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "5953925",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN-15",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "11:15:08",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
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
                    "orig_id": "5vXG06ABI3UnQyDO5tCr",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:15:08 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790259308565366951 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.15.16 srcport=65013 srcintf=\"VLAN-15\" srcintfrole=\"lan\" dstip=192.168.169.102 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=5953925 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" dstuser=\"ENRIQUEVERA\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"50:6b:8d:ec:30:fa\" srcmac=\"50:6b:8d:ec:30:fa\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790259414218,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "50:6b:8d:ec:30:fa.0.192.168.15.16",
                    "srcip": "192.168.15.16",
                    "srcip_assetid": "42e742ac-e26c-11f0-bee4-aa0456b9a54a",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "192.168.15.16",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "50:6b:8d:ec:30:fa",
                    "srcport": 65013,
                    "start_bucket_time": 1790259300000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790259902716,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 481813,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2439,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "49a8d5a6-8225-4f3f-a023-2bf0ad64df2a1790259903645-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790259308565,
                    "timestamp_utc": "2026-09-24T14:15:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790259903645,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.15.16 private) has had actions blocked by a firewall too many times (#: 217), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "166b29a7-862c-4593-8309-09bf3cdcdcfc1790261702677-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19424,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "timeout",
                    "actual": 1,
                    "aella_tuples": "192.168.169.102.10.179.105.31.7680.4",
                    "anomaly_id": "D_rm06ABI3UnQyDOzOWz",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/7680",
                    "appid_stdport": "yes",
                    "days_silent": 23,
                    "detected_fields": [
                        "fw_policy_id"
                    ],
                    "detected_values": [
                        "FG-Technoma_190"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790261385768,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.179.105.31",
                    "dstip": "10.179.105.31",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.179.105.31",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 12,
                    "end_bucket_time": 1790261400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790261385768
                    },
                    "event_category": "network",
                    "event_name": "fw_policy_id",
                    "event_score": 39,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_policy": []
                    },
                    "event_type": "conn",
                    "fidelity": 37.63,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "AD1",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "UPAY-P5-PRI",
                        "dstintfrole": "undefined",
                        "event_time": "2026-09-24 11:49:46",
                        "eventtime": "1790261385767891008",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "70:d8:23:82:03:52",
                        "osname": "Windows",
                        "policyname": "THN A UPAY P5",
                        "policytype": "policy",
                        "poluuid": "46a48c78-ca3f-51f0-f325-000011dbfb2b",
                        "rule_id": 190,
                        "service": "tcp/7680",
                        "sessionid": "8325822",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcname": "NB-EVERA",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "11:49:46",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "unauthuser": "enriquevera",
                        "unauthusersource": "kerberos",
                        "vd": "root",
                        "vpntype": "ipsecvpn"
                    },
                    "fw_policy_id": "FG-Technoma_190",
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
                    "orig_id": "D_rm06ABI3UnQyDOzOWz",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 104,
                    "outpkts_delta": 2,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:49:46 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790261385767891008 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.102 srcname=\"NB-EVERA        \" srcport=49677 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.179.105.31 dstport=7680 dstintf=\"UPAY-P5-PRI\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=8325822 proto=6 action=\"timeout\" policyid=190 policytype=\"policy\" poluuid=\"46a48c78-ca3f-51f0-f325-000011dbfb2b\" policyname=\"THN A UPAY P5\" user=\"ENRIQUEVERA\" authserver=\"AD1\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=12 sentbyte=104 rcvdbyte=0 sentpkt=2 rcvdpkt=0 vpntype=\"ipsecvpn\" osname=\"Windows\" srcswversion=\"10/11\" unauthuser=\"enriquevera\" unauthusersource=\"kerberos\" mastersrcmac=\"70:d8:23:82:03:52\" srcmac=\"70:d8:23:82:03:52\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790261501916,
                    "severity": 40,
                    "src_tuples": "70:d8:23:82:03:52.0.192.168.169.102",
                    "srcip": "192.168.169.102",
                    "srcip_assetid": "fe9206f2-cf7c-11f0-bc8a-828ad4fe26cd",
                    "srcip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "srcip_geo_point": "-25.2869,-57.6511",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "nb-evera.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "70:d8:23:82:03:52",
                    "srcport": 49677,
                    "start_bucket_time": 1790261100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790261702649,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 191894,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2777,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "166b29a7-862c-4593-8309-09bf3cdcdcfc1790261702677-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790261385768,
                    "timestamp_utc": "2026-09-24T14:49:45.000Z",
                    "totalbytes": 104,
                    "totalpackets": 2,
                    "typical": 0,
                    "user": {
                        "name": "ENRIQUEVERA"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790261702677,
                    "xdr_event": {
                        "description": "In internal traffic, the connection from IP: 192.168.169.102, name: nb-evera.technoma.local (private) to IP/name: 10.179.105.31 (private) has triggered a policy (ID: \"FG-Technoma_190\") that has never been observed by Stellar Cyber before (or been seen very rarely) on the firewall (type: \"fw_fortigate\") after 23 days of silence.",
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
```
