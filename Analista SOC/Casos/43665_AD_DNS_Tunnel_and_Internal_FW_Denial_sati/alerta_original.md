# Evidencia Cruda - Lote de Alertas de Interflow (Secuencia 43665)

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "76d5e699-b1a7-475b-bad2-eb4910068fb01790864402619-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43666,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 187,
                    "aella_tuples": "10.212.134.209.10.11.1.1.53.4",
                    "anomaly_id": "3s_P96ABI3UnQyDOJ_pY",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "10.212.134.209"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790863825994,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "ad.technoma.local",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_username": "FLAVIOBENEGAS",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 53,
                    "duration": 0,
                    "end_bucket_time": 1790864100000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790863825994
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
                    "fidelity": 95.99,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "sati",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-10-01",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-10-01 11:10:26",
                        "eventtime": "1790863825993874415",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "699710625",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "11:10:26",
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
                    "orig_id": "3s_P96ABI3UnQyDOJ_pY",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-10-01 time=11:10:26 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790863825993874415 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.209 srcport=53514 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=699710625 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"FLAVIOBENEGAS\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790863934879,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.209",
                    "srcip": "10.212.134.209",
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
                    "srcip_host": "10.212.134.209",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "sati",
                    "srcip_usersid": "sati",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 53514,
                    "start_bucket_time": 1790863800000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790864402608,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 461445,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "76d5e699-b1a7-475b-bad2-eb4910068fb01790864402619-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790863825994,
                    "timestamp_utc": "2026-10-01T14:10:25.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 22,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790864402619,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.209 private) has had actions blocked by a firewall too many times (#: 187), compared to the typical number of blocks (#: 22), measured in a 5.0-minute interval.",
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
                "_id": "38b58f4e-257f-4955-a6db-67007b6e8cff1790864402006-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43665,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 570,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "e8_N96ABI3UnQyDOpMCx",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "10.11.1.1",
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RZABALA.technoma.local"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
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
                    "dstmac": "00:50:56:af:55:19",
                    "dstport": 53,
                    "duration": 44,
                    "end_bucket_time": 1790864100000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 52,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 14.44,
                    "flow_score": 98,
                    "inbytes_delta": 201,
                    "inbytes_total": 606,
                    "inpkts_delta": 2,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 24835
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.24",
                                    "host_type": "A",
                                    "name": "NB-RZABALA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RZABALA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RZABALA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.24"
                            ],
                            "response_time": 0,
                            "transaction_id": 24835,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 24835
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 2,
                    "msgtype_name": "end",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "e8_N96ABI3UnQyDOpMCx",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 510,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 54,
                    "receive_time": 1790863839510,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "srcip": "10.11.1.1",
                    "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "ad.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 64780,
                    "start_bucket_time": 1790863800000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790864401978,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 560025,
                        "status": "New"
                    },
                    "stellar_da_input": 1228,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "38b58f4e-257f-4955-a6db-67007b6e8cff1790864402006-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790863839115,
                    "timestamp_utc": "2026-10-01T14:10:39.000Z",
                    "tos": 0,
                    "total_entropy": 163,
                    "totalbytes": 1116,
                    "totalpackets": 3,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ACHAMORRO",
                        "NB-APAREDES",
                        "NB-ARESQUIN",
                        "NB-ASAUCEDO",
                        "NB-AZORRILLA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 27.88,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790864402006,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 570 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RZABALA.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ACHAMORRO.\" The typical volume of traffic transmitted through this tunnel is 27 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
                        "display_name": "DNS Tunneling Anomaly",
                        "framework_version": "v8",
                        "name": "dns_tunnel",
                        "scope": "",
                        "tactic": {
                            "id": "TA0010",
                            "name": "Exfiltration"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1048",
                            "name": "Exfiltration Over Alternative Protocol"
                        },
                        "xdr_killchain_stage": "Exfiltration & Impact",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
```
