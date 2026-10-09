=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "137488f7-7733-4e17-9194-81057dce05181783596902900-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6720,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 920,
                    "aella_tuples": "192.168.169.44.10.49.70.100.0.4",
                    "anomaly_id": "cQahRp8BBi0xHyA-kP8D",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "PING",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.44"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1783596300245,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.49.70.100",
                    "dstip": "10.49.70.100",
                    "dstip_assetid": "37532aa4-efb5-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.49.70.100",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 0,
                    "duration": 0,
                    "end_bucket_time": 1783596600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783596300245
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
                    "fidelity": 99.87,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-09",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcountry": "Reserved",
                        "dstintf": "DCTigo-TEDs-PRI",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-09 08:25:00",
                        "eventtime": "1783596300245493133",
                        "identifier": "41815",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "bc:6e:e2:ae:99:d0",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "PING",
                        "sessionid": "1163313092",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "08:25:00",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
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
                    "orig_id": "cQahRp8BBi0xHyA-kP8D",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-09 time=08:25:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783596300245493133 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.44 identifier=41815 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.49.70.100 dstintf=\"DCTigo-TEDs-PRI\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1163313092 proto=1 action=\"deny\" policyid=0 policytype=\"policy\" service=\"PING\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" devtype=\"Router\" mastersrcmac=\"bc:6e:e2:ae:99:d0\" srcmac=\"bc:6e:e2:ae:99:d0\" srcserver=0",
                    "proto": 1,
                    "proto_name": "icmp",
                    "receive_time": 1783596414604,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "bc:6e:e2:ae:99:d0.0.192.168.169.44",
                    "srcip": "192.168.169.44",
                    "srcip_assetid": "b18c05ca-caad-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.44",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "bc:6e:e2:ae:99:d0",
                    "srcport": 0,
                    "start_bucket_time": 1783596300000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783596902878,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 482202,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2444,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "137488f7-7733-4e17-9194-81057dce05181783596902900-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783596300245,
                    "timestamp_utc": "2026-07-09T11:25:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 62,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783596902899,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.169.44 private) has had actions blocked by a firewall too many times (#: 920), compared to the typical number of blocks (#: 62), measured in a 5.0-minute interval.",
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
                "_id": "dbc6c8bf-1405-4554-80a2-330fe6b7212f1783597203507-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6726,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 854,
                    "aella_tuples": "192.168.169.44.10.49.70.100.0.4",
                    "anomaly_id": "hQemRp8BBi0xHyA-I0jF",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "PING",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.44"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1783596600285,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.49.70.100",
                    "dstip": "10.49.70.100",
                    "dstip_assetid": "37532aa4-efb5-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.49.70.100",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 0,
                    "duration": 0,
                    "end_bucket_time": 1783596900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783596600285
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
                    "fidelity": 99.85,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-09",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcountry": "Reserved",
                        "dstintf": "DCTigo-TEDs-PRI",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-09 08:30:01",
                        "eventtime": "1783596600285034637",
                        "identifier": "41875",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "bc:6e:e2:ae:99:d0",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "PING",
                        "sessionid": "1163650600",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "08:30:01",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
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
                    "orig_id": "hQemRp8BBi0xHyA-I0jF",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-09 time=08:30:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783596600285034637 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.44 identifier=41875 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.49.70.100 dstintf=\"DCTigo-TEDs-PRI\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1163650600 proto=1 action=\"deny\" policyid=0 policytype=\"policy\" service=\"PING\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" devtype=\"Router\" mastersrcmac=\"bc:6e:e2:ae:99:d0\" srcmac=\"bc:6e:e2:ae:99:d0\" srcserver=0",
                    "proto": 1,
                    "proto_name": "icmp",
                    "receive_time": 1783596719448,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "bc:6e:e2:ae:99:d0.0.192.168.169.44",
                    "srcip": "192.168.169.44",
                    "srcip_assetid": "b18c05ca-caad-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.44",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "bc:6e:e2:ae:99:d0",
                    "srcport": 0,
                    "start_bucket_time": 1783596600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783597203493,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 482656,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2444,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "dbc6c8bf-1405-4554-80a2-330fe6b7212f1783597203507-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783596600285,
                    "timestamp_utc": "2026-07-09T11:30:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 62,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783597203507,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.169.44 private) has had actions blocked by a firewall too many times (#: 854), compared to the typical number of blocks (#: 62), measured in a 5.0-minute interval.",
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
                "_id": "00dcf9bb-3f32-4c75-a76d-a843fa3a3a151783597502408-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6730,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 770,
                    "aella_tuples": "192.168.169.44.10.49.70.100.0.4",
                    "anomaly_id": "DAerRp8BBi0xHyA-BaWt",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "PING",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.169.44"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1783596900237,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.49.70.100",
                    "dstip": "10.49.70.100",
                    "dstip_assetid": "37532aa4-efb5-11f0-bee4-aa0456b9a54a",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.49.70.100",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 0,
                    "duration": 0,
                    "end_bucket_time": 1783597200000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783596900237
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
                    "fidelity": 99.81,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-09",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "DCTigo-TEDs-PRI",
                        "dstintfrole": "undefined",
                        "event_time": "2026-07-09 08:35:00",
                        "eventtime": "1783596900237175103",
                        "identifier": "41935",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "bc:6e:e2:ae:99:d0",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "PING",
                        "sessionid": "1164028641",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "08:35:00",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
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
                    "orig_id": "DAerRp8BBi0xHyA-BaWt",
                    "orig_index": "aella-adr-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-09 time=08:35:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783596900237175103 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.169.44 identifier=41935 srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" dstip=10.49.70.100 dstintf=\"DCTigo-TEDs-PRI\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=1164028641 proto=1 action=\"deny\" policyid=0 policytype=\"policy\" service=\"PING\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 vpntype=\"ipsecvpn\" crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"bc:6e:e2:ae:99:d0\" srcmac=\"bc:6e:e2:ae:99:d0\" srcserver=0",
                    "proto": 1,
                    "proto_name": "icmp",
                    "receive_time": 1783597036106,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "bc:6e:e2:ae:99:d0.0.192.168.169.44",
                    "srcip": "192.168.169.44",
                    "srcip_assetid": "b18c05ca-caad-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "192.168.169.44",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "bc:6e:e2:ae:99:d0",
                    "srcport": 0,
                    "start_bucket_time": 1783596900000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783597502380,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 461662,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2406,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "00dcf9bb-3f32-4c75-a76d-a843fa3a3a151783597502408-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783596900237,
                    "timestamp_utc": "2026-07-09T11:35:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 62,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783597502408,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.169.44 private) has had actions blocked by a firewall too many times (#: 770), compared to the typical number of blocks (#: 62), measured in a 5.0-minute interval.",
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