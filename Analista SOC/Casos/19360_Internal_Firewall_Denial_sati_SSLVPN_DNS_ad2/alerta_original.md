# Alerta Original - Raw JSON Interflow (Lote de 5 Eventos)
**ID de Secuencia Principal:** `19360` (Rango: `19360` - `19622`)  
**Fecha de Ingesta:** 2026-09-24  
**Tenant:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "d03e5ff8-50b8-40df-a4a6-f22dd606d4f21790260502393-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19360,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 549,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "fvfQ06ABI3UnQyDOhYL5",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790259958789,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JOSEPAREDES",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790260200000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790259958789
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
                    "fidelity": 99.83,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 11:25:58",
                        "eventtime": "1790259958789138699",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "6714460",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "11:25:58",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "fvfQ06ABI3UnQyDOhYL5",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:25:58 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790259958789138699 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=56046 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=6714460 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JOSEPAREDES\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790260048571,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 56046,
                    "start_bucket_time": 1790259900000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790260502374,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 451109,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2349,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "d03e5ff8-50b8-40df-a4a6-f22dd606d4f21790260502393-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790259958789,
                    "timestamp_utc": "2026-09-24T14:25:58.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790260502393,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 549), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_id": "acc9621b-ecdf-44a0-be1d-b2235e8bd3921790260802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19373,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 204,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "d_jU06ABI3UnQyDO7yg1",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790260231542,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "JOSEPAREDES",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790260500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790260231542
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
                    "fidelity": 98.11,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 11:30:31",
                        "eventtime": "1790260231542001688",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "7023107",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "11:30:31",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "d_jU06ABI3UnQyDO7yg1",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:30:31 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790260231542001688 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=45743 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=7023107 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"JOSEPAREDES\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790260333749,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 45743,
                    "start_bucket_time": 1790260200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790260802916,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462145,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2349,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "acc9621b-ecdf-44a0-be1d-b2235e8bd3921790260802950-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790260231542,
                    "timestamp_utc": "2026-09-24T14:30:31.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790260802950,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 204), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_id": "27faa4b0-63ca-46dc-8ce4-3fc84295d2a61790261706501-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19430,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 368,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "4Pri06ABI3UnQyDOOSTZ",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790261102067,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790261400000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790261102067
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
                    "fidelity": 99.68,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 11:45:02",
                        "eventtime": "1790261102067282702",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "8016065",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "11:45:02",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "4Pri06ABI3UnQyDOOSTZ",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:45:02 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790261102067282702 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=55666 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=8016065 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790261204308,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 55666,
                    "start_bucket_time": 1790261100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790261705597,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 494808,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2294,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "27faa4b0-63ca-46dc-8ce4-3fc84295d2a61790261706501-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790261102067,
                    "timestamp_utc": "2026-09-24T14:45:02.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790261706501,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 368), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_id": "b486cc18-0bdf-4efc-a65f-17d090c38af61790262606598-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19476,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 212,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "F_zv06ABI3UnQyDOyW2v",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790262000125,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790262300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790262000125
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
                    "fidelity": 87.35,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 11:59:59",
                        "eventtime": "1790262000125100974",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "9037803",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "11:59:59",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "F_zv06ABI3UnQyDOyW2v",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:59:59 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790262000125100974 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=50622 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=9037803 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262092893,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 50622,
                    "start_bucket_time": 1790262000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790262606091,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 505412,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2294,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "b486cc18-0bdf-4efc-a65f-17d090c38af61790262606598-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262000125,
                    "timestamp_utc": "2026-09-24T15:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 28,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790262606598,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 212), compared to the typical number of blocks (#: 28), measured in a 5.0-minute interval.",
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
                "_id": "f2ace2fa-d7f0-48dc-b60d-dfc473c22f0a1790263207869-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19570,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 366,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "2P3506ABI3UnQyDOP-Ni",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790262606772,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790262900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790262606772
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
                    "fidelity": 99.54,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 12:10:07",
                        "eventtime": "1790262606772426915",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "9728205",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "12:10:07",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "2P3506ABI3UnQyDOP-Ni",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=12:10:07 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790262606772426915 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=49149 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=9728205 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790262713943,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 49149,
                    "start_bucket_time": 1790262600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790263207331,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 486550,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2294,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "f2ace2fa-d7f0-48dc-b60d-dfc473c22f0a1790263207869-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262606772,
                    "timestamp_utc": "2026-09-24T15:10:06.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 28,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790263207869,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 366), compared to the typical number of blocks (#: 28), measured in a 5.0-minute interval.",
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
                "_id": "394addef-3a87-4530-86c6-a726852fcf211790263806374-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19622,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 520,
                    "aella_tuples": "10.212.134.200.10.11.1.2.53.4",
                    "anomaly_id": "1v8C1KABI3UnQyDOGkU4",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.200"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790263209738,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.2",
                    "dstip": "10.11.1.2",
                    "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad2.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790263500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790263209738
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
                    "fidelity": 99.76,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-09-24 12:20:09",
                        "eventtime": "1790263209738028747",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "10486555",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "12:20:09",
                        "trandisp": "noop",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_0",
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
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
                    "orig_id": "1v8C1KABI3UnQyDOGkU4",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=12:20:09 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790263209738028747 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.200 srcport=44831 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.2 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=10486555 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790263294410,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.200",
                    "srcip": "10.212.134.200",
                    "srcip_assetid": "fed3cf7e-db48-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "10.212.134.200",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 44831,
                    "start_bucket_time": 1790263200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790263805404,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 504550,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2296,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "394addef-3a87-4530-86c6-a726852fcf211790263806374-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263209738,
                    "timestamp_utc": "2026-09-24T15:20:09.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 29,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790263806374,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.200 private) has had actions blocked by a firewall too many times (#: 520), compared to the typical number of blocks (#: 29), measured in a 5.0-minute interval.",
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
```
