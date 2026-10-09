=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6341472c-9e51-41b0-819d-689654b1b4491784473802344-YWVsbGEtc2VyLTIwMjYuMDcuMTktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 16665,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "client-rst",
                    "actual": 1,
                    "aella_tuples": "192.168.15.50.10.180.74.6.50577.4",
                    "anomaly_id": "VhTqep8BI3UnQyDOuTXK",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/50577",
                    "appid_stdport": "yes",
                    "days_silent": 235,
                    "detected_fields": [
                        "fw_policy_id"
                    ],
                    "detected_values": [
                        "FG-Technoma_318"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784473496788,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.180.74.6",
                    "dstip": "10.180.74.6",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.180.74.6",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 50577,
                    "duration": 6,
                    "end_bucket_time": 1784473500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784473496788
                    },
                    "event_category": "network",
                    "event_name": "fw_policy_id",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_policy": []
                    },
                    "event_type": "conn",
                    "fidelity": 93.06,
                    "fortinet": {
                        "appcat": "unscanned",
                        "date": "2026-07-19",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "WEPA-HUB-TIGO",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-19 12:04:56",
                        "eventtime": "1784473496787880255",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "00:50:56:96:bd:13",
                        "osname": "Windows",
                        "policyname": "MagicInfo a CCEE",
                        "policytype": "policy",
                        "poluuid": "9b2290bc-82bb-51f1-9738-4a61e1d22762",
                        "rule_id": 318,
                        "service": "tcp/50577",
                        "sessionid": "2147249095",
                        "srccountry": "Reserved",
                        "srchwvendor": "VMware",
                        "srcintf": "VLAN-15",
                        "srcintfrole": "lan",
                        "srcname": "P-ITTI-MCINFO-1",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "12:04:56",
                        "trandisp": "snat",
                        "transip": "172.26.22.3",
                        "transport": "53071",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vpntype": "ipsecvpn",
                        "vwlid": "0"
                    },
                    "fw_policy_id": "FG-Technoma_318",
                    "inbytes_total": 1404,
                    "inpkts_delta": 12,
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
                    "orig_id": "VhTqep8BI3UnQyDOuTXK",
                    "orig_index": "aella-adr-2026.07.19-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 3588,
                    "outpkts_delta": 12,
                    "parser_raw_msg": "<189>date=2026-07-19 time=12:04:56 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784473496787880255 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.15.50 srcname=\"P-ITTI-MCINFO-1\" srcport=53071 srcintf=\"VLAN-15\" srcintfrole=\"lan\" dstip=10.180.74.6 dstport=50577 dstintf=\"WEPA-HUB-TIGO\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=2147249095 proto=6 action=\"client-rst\" policyid=318 policytype=\"policy\" poluuid=\"9b2290bc-82bb-51f1-9738-4a61e1d22762\" policyname=\"MagicInfo a CCEE\" service=\"tcp/50577\" trandisp=\"snat\" transip=172.26.22.3 transport=53071 appcat=\"unscanned\" duration=6 sentbyte=3588 rcvdbyte=1404 sentpkt=12 rcvdpkt=12 vpntype=\"ipsecvpn\" vwlid=0 srchwvendor=\"VMware\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"00:50:56:96:bd:13\" srcmac=\"00:50:56:96:bd:13\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784473625985,
                    "severity": 40,
                    "src_tuples": "00:50:56:96:bd:13.0.192.168.15.50",
                    "srcip": "192.168.15.50",
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
                    "srcip_host": "192.168.15.50",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:96:bd:13",
                    "srcport": 53071,
                    "start_bucket_time": 1784473200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784473802333,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 171867,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2794,
                    "stellar_index_id": "aella-ser-2026.07.19-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "6341472c-9e51-41b0-819d-689654b1b4491784473802344-YWVsbGEtc2VyLTIwMjYuMDcuMTktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784473496788,
                    "timestamp_utc": "2026-07-19T15:04:56.000Z",
                    "totalbytes": 4992,
                    "totalpackets": 24,
                    "typical": 0,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784473802344,
                    "xdr_event": {
                        "description": "In internal traffic, the connection from IP/name: 192.168.15.50 (private) to IP/name: 10.180.74.6 (private) has triggered a policy (ID: \"FG-Technoma_318\") that has never been observed by Stellar Cyber before (or been seen very rarely) on the firewall (type: \"fw_fortigate\") after 235 days of silence.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6fc3b16a-79c3-4430-a404-0171eb3ab52a1784473803356-YWVsbGEtc2VyLTIwMjYuMDcuMTktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 16666,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "action": "server-rst",
                    "actual": 1,
                    "aella_tuples": "10.180.74.6.192.168.15.50.990.4",
                    "anomaly_id": "DBTqep8BI3UnQyDOuDX_",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/990",
                    "appid_stdport": "yes",
                    "days_silent": 235,
                    "detected_fields": [
                        "fw_policy_id"
                    ],
                    "detected_values": [
                        "FG-Technoma_320"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784473497776,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:96:bd:13.0.192.168.15.50",
                    "dstip": "192.168.15.50",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "192.168.15.50",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:96:bd:13",
                    "dstport": 990,
                    "duration": 8,
                    "end_bucket_time": 1784473500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784473497776
                    },
                    "event_category": "network",
                    "event_name": "fw_policy_id",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_policy": []
                    },
                    "event_type": "conn",
                    "fidelity": 93.06,
                    "fortinet": {
                        "appcat": "unscanned",
                        "date": "2026-07-19",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "VLAN-15",
                        "dstintfrole": "lan",
                        "event_time": "2026-07-19 12:04:57",
                        "eventtime": "1784473497775887152",
                        "level": "notice",
                        "logid": "0000000013",
                        "policyname": "CCEE a MagicInfo",
                        "policytype": "policy",
                        "poluuid": "f0a48c38-82bc-51f1-65b1-9697e76801d4",
                        "rule_id": 320,
                        "service": "tcp/990",
                        "sessionid": "2147248310",
                        "srccountry": "Reserved",
                        "srcintf": "WEPA-HUB-TIGO",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "12:04:57",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vpntype": "ipsecvpn"
                    },
                    "fw_policy_id": "FG-Technoma_320",
                    "inbytes_total": 5104,
                    "inpkts_delta": 31,
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
                            "name": "dsthwvendor",
                            "strvalue": "VMware"
                        },
                        {
                            "name": "masterdstmac",
                            "strvalue": "00:50:56:96:bd:13"
                        },
                        {
                            "name": "dstserver",
                            "strvalue": "0"
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
                    "orig_id": "DBTqep8BI3UnQyDOuDX_",
                    "orig_index": "aella-adr-2026.07.19-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 3612,
                    "outpkts_delta": 33,
                    "parser_raw_msg": "<189>date=2026-07-19 time=12:04:57 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784473497775887152 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.180.74.6 srcport=60800 srcintf=\"WEPA-HUB-TIGO\" srcintfrole=\"undefined\" dstip=192.168.15.50 dstport=990 dstintf=\"VLAN-15\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=2147248310 proto=6 action=\"server-rst\" policyid=320 policytype=\"policy\" poluuid=\"f0a48c38-82bc-51f1-65b1-9697e76801d4\" policyname=\"CCEE a MagicInfo\" service=\"tcp/990\" trandisp=\"noop\" appcat=\"unscanned\" duration=8 sentbyte=3612 rcvdbyte=5104 sentpkt=33 rcvdpkt=31 vpntype=\"ipsecvpn\" dsthwvendor=\"VMware\" masterdstmac=\"00:50:56:96:bd:13\" dstmac=\"00:50:56:96:bd:13\" dstserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784473625985,
                    "severity": 40,
                    "src_tuples": "00:00:00:00:00:00.0.10.180.74.6",
                    "srcip": "10.180.74.6",
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
                    "srcip_host": "10.180.74.6",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 60800,
                    "start_bucket_time": 1784473200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784473802431,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 172035,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2617,
                    "stellar_index_id": "aella-ser-2026.07.19-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "6fc3b16a-79c3-4430-a404-0171eb3ab52a1784473803356-YWVsbGEtc2VyLTIwMjYuMDcuMTktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784473497776,
                    "timestamp_utc": "2026-07-19T15:04:57.000Z",
                    "totalbytes": 8716,
                    "totalpackets": 64,
                    "typical": 0,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784473803356,
                    "xdr_event": {
                        "description": "In internal traffic, the connection from IP/name: 10.180.74.6 (private) to IP/name: 192.168.15.50 (private) has triggered a policy (ID: \"FG-Technoma_320\") that has never been observed by Stellar Cyber before (or been seen very rarely) on the firewall (type: \"fw_fortigate\") after 235 days of silence.",
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