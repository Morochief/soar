# Alerta Original - Raw JSON Interflow (Lote de 2 Eventos)
**ID de Secuencia Principal:** `19395` (Rango: `19395` - `19571`)  
**Fecha de Ingesta:** 2026-09-24  
**Tenant:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "4ee142bd-7ef8-4954-99d9-ac4bf80a1a8a1790261103513-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19395,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 227,
                    "aella_tuples": "192.168.15.16.192.168.169.157.7680.4",
                    "anomaly_id": "z_jZ06ABI3UnQyDOEtEq",
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
                    "domain_creation": 1790260509842,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.157",
                    "dstip": "192.168.169.157",
                    "dstip_assetid": "63864caa-1189-11f1-b2c6-62a12c107cbc",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "192.168.169.157",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1790260800000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790260509842
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
                    "fidelity": 98.88,
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
                        "event_time": "2026-09-24 11:35:10",
                        "eventtime": "1790260509842133226",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:6b:8d:ec:30:fa",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "7340220",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN-15",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "11:35:10",
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
                    "orig_id": "z_jZ06ABI3UnQyDOEtEq",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=11:35:10 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790260509842133226 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.15.16 srcport=51602 srcintf=\"VLAN-15\" srcintfrole=\"lan\" dstip=192.168.169.157 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=7340220 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" mastersrcmac=\"50:6b:8d:ec:30:fa\" srcmac=\"50:6b:8d:ec:30:fa\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790260609938,
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
                    "srcport": 51602,
                    "start_bucket_time": 1790260500000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790261102529,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 490881,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2300,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "4ee142bd-7ef8-4954-99d9-ac4bf80a1a8a1790261103513-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790260509842,
                    "timestamp_utc": "2026-09-24T14:35:09.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790261103513,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.15.16 private) has had actions blocked by a firewall too many times (#: 227), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_id": "45da8062-29ad-4a06-be24-1e3d3b1913621790263207869-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19571,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 242,
                    "aella_tuples": "192.168.15.16.192.168.169.157.7680.4",
                    "anomaly_id": "Rv3506ABI3UnQyDOGNmf",
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
                    "domain_creation": 1790262600072,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.157",
                    "dstip": "192.168.169.157",
                    "dstip_assetid": "63864caa-1189-11f1-b2c6-62a12c107cbc",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "192.168.169.157",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1790262900000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790262600072
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
                    "fidelity": 95.78,
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
                        "event_time": "2026-09-24 12:10:00",
                        "eventtime": "1790262600072071631",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:6b:8d:ec:30:fa",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "9720443",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN-15",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "12:10:00",
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
                    "orig_id": "Rv3506ABI3UnQyDOGNmf",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-09-24 time=12:10:00 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790262600072071631 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.15.16 srcport=52132 srcintf=\"VLAN-15\" srcintfrole=\"lan\" dstip=192.168.169.157 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=9720443 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"50:6b:8d:ec:30:fa\" srcmac=\"50:6b:8d:ec:30:fa\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790262705341,
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
                    "srcport": 52132,
                    "start_bucket_time": 1790262600000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790263207501,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 496617,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2384,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "45da8062-29ad-4a06-be24-1e3d3b1913621790263207869-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790262600072,
                    "timestamp_utc": "2026-09-24T15:10:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 28,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790263207869,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.15.16 private) has had actions blocked by a firewall too many times (#: 242), compared to the typical number of blocks (#: 28), measured in a 5.0-minute interval.",
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
