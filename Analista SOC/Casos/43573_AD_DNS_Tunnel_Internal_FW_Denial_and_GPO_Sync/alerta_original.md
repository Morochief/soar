<USER_REQUEST>
=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "5de682cc-0b5d-4546-a6db-413c99a8db4b1790862604404-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43581,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 987,
                    "aella_tuples": "192.168.171.142.10.11.1.1.53.4",
                    "anomaly_id": "Fsuz96ABI3UnQyDOr5EA",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "192.168.171.142"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790862014668,
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
                    "end_bucket_time": 1790862300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790862014668
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
                    "fidelity": 99.92,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-10-01",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-10-01 10:40:15",
                        "eventtime": "1790862014667907535",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "de:7d:93:bf:80:cd",
                        "osname": "Android",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "697356977",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN304",
                        "srcintfrole": "lan",
                        "srcname": "Android_00HEJTOT",
                        "srcserver": "0",
                        "srcswversion": "10",
                        "subtype": "forward",
                        "time": "10:40:15",
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
                    "orig_id": "Fsuz96ABI3UnQyDOr5EA",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-10-01 time=10:40:15 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790862014667907535 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.171.142 srcname=\"Android_00HEJTOT\" srcport=37552 srcintf=\"VLAN304\" srcintfrole=\"lan\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=697356977 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" dstuser=\"FLAVIOBENEGAS\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Android\" srcswversion=\"10\" mastersrcmac=\"de:7d:93:bf:80:cd\" srcmac=\"de:7d:93:bf:80:cd\" srcserver=0",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790862132029,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "de:7d:93:bf:80:cd.0.192.168.171.142",
                    "srcip": "192.168.171.142",
                    "srcip_assetid": "60d1971a-b1db-11f1-8965-32ca1fa0b082",
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
                    "srcip_host": "192.168.171.142",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "de:7d:93:bf:80:cd",
                    "srcport": 37552,
                    "start_bucket_time": 1790862000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790862603482,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462607,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2484,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "5de682cc-0b5d-4546-a6db-413c99a8db4b1790862604404-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862014668,
                    "timestamp_utc": "2026-10-01T13:40:14.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 23,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790862604404,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.171.142 private) has had actions blocked by a firewall too many times (#: 987), compared to the typical number of blocks (#: 23), measured in a 5.0-minute interval.",
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
                "_id": "f00a7767-7c67-4bc2-b20e-2cbb0522065e1790862604404-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43582,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 258,
                    "aella_tuples": "10.212.134.208.10.11.1.1.53.4",
                    "anomaly_id": "csuz96ABI3UnQyDO15VZ",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "DNS",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip_host"
                    ],
                    "detected_values": [
                        "nb-fabianacuna.technoma.local"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790862020359,
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
                    "end_bucket_time": 1790862300000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790862020359
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
                    "fidelity": 98.94,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "AD1",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-10-01",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "Citrix Servers",
                        "dstintfrole": "lan",
                        "event_time": "2026-10-01 10:40:20",
                        "eventtime": "1790862020359185988",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "697364349",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "10:40:20",
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
                    "orig_id": "csuz96ABI3UnQyDO15VZ",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-10-01 time=10:40:20 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790862020359185988 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.208 srcport=33005 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=697364349 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"FABIANACUñA\" authserver=\"AD1\" dstuser=\"FLAVIOBENEGAS\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790862140239,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.208",
                    "srcip": "10.212.134.208",
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
                    "srcip_host": "nb-fabianacuna.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "FABIANACUñA",
                    "srcip_usersid": "FABIANACUñA",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 33005,
                    "start_bucket_time": 1790862000000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790862603614,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 452982,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2387,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "f00a7767-7c67-4bc2-b20e-2cbb0522065e1790862604404-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862020359,
                    "timestamp_utc": "2026-10-01T13:40:20.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 23,
                    "user": {
                        "name": "FABIANACUñA"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790862604404,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP: 10.212.134.208, name: nb-fabianacuna.technoma.local private) has had actions blocked by a firewall too many times (#: 258), compared to the typical number of blocks (#: 23), measured in a 5.0-minute interval.",
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
                "_id": "a72a6b23-6e20-4564-b309-477c8ca08ca41790862601669-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43573,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 578,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "gsu096ABI3UnQyDO6cZg",
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
                        "NB-SFERNANDEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-SFERNANDEZ.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 55,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 17.24,
                    "flow_score": 98,
                    "inbytes_delta": 104,
                    "inbytes_total": 104,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 1296
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.120",
                                    "host_type": "A",
                                    "name": "NB-SFERNANDEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.120"
                            ],
                            "response_time": 0,
                            "transaction_id": 1296,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 1296
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "gsu096ABI3UnQyDO6cZg",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 88,
                    "outbytes_total": 88,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 57,
                    "receive_time": 1790862217476,
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
                    "srcport": 57090,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601628,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 380256,
                        "status": "New"
                    },
                    "stellar_da_input": 1234,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a72a6b23-6e20-4564-b309-477c8ca08ca41790862601669-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862036011,
                    "timestamp_utc": "2026-10-01T13:40:36.000Z",
                    "tos": 0,
                    "total_entropy": 169,
                    "totalbytes": 192,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "ad2",
                        "NB-ADIARTE",
                        "NB-AORTELLADO",
                        "NB-CARANDA",
                        "NB-CFARINA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 28.62,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862601669,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 578 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-SFERNANDEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AORTELLADO.\" The typical volume of traffic transmitted through this tunnel is 28 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "f68e5061-767c-4f01-a00e-d9b57a44c5ad1790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43574,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 586,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "G8u196ABI3UnQyDOhtsv",
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
                        "NB-TMARIN.technoma.local"
                    ],
                    "domain_list": [
                        "NB-TMARIN.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 56,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 18.26,
                    "flow_score": 98,
                    "inbytes_delta": 100,
                    "inbytes_total": 100,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-TMARIN.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-TMARIN.technoma.local",
                            "query_type": "A",
                            "transaction_id": 19672
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.126",
                                    "host_type": "A",
                                    "name": "NB-TMARIN.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-TMARIN.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-TMARIN.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.126"
                            ],
                            "response_time": 0,
                            "transaction_id": 19672,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 19672
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "G8u196ABI3UnQyDOhtsv",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 84,
                    "outbytes_total": 84,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 58,
                    "receive_time": 1790862259078,
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
                    "srcport": 55258,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601656,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 339956,
                        "status": "New"
                    },
                    "stellar_da_input": 1224,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "f68e5061-767c-4f01-a00e-d9b57a44c5ad1790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862076683,
                    "timestamp_utc": "2026-10-01T13:41:16.000Z",
                    "tos": 0,
                    "total_entropy": 170,
                    "totalbytes": 184,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "ad2",
                        "NB-AMARTINEZ",
                        "NB-ANGELRA2",
                        "NB-AZORRILLA",
                        "NB-DRODAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 19.33,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 586 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TMARIN.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AMARTINEZ.\" The typical volume of traffic transmitted through this tunnel is 19 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "167d3c66-3917-4dd7-ba10-9c3e463158461790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43575,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 675,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Xcu296ABI3UnQyDORPM9",
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
                        "SRV-AZADCONNECT.technoma.local"
                    ],
                    "domain_list": [
                        "SRV-AZADCONNECT.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 64,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 27.31,
                    "flow_score": 98,
                    "inbytes_delta": 106,
                    "inbytes_total": 106,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "transaction_id": 47426
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "10.11.1.3",
                                    "host_type": "A",
                                    "name": "SRV-AZADCONNECT.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "10.11.1.3"
                            ],
                            "response_time": 0,
                            "transaction_id": 47426,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 47426
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "Xcu296ABI3UnQyDORPM9",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 90,
                    "outbytes_total": 90,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 63,
                    "receive_time": 1790862300075,
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
                    "srcport": 65516,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601705,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 290979,
                        "status": "New"
                    },
                    "stellar_da_input": 1236,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "167d3c66-3917-4dd7-ba10-9c3e463158461790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862117389,
                    "timestamp_utc": "2026-10-01T13:41:57.000Z",
                    "tos": 0,
                    "total_entropy": 193,
                    "totalbytes": 196,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-CLEIVA",
                        "NB-JENCISO",
                        "NB-ECANETE",
                        "NB-FBENEGAS",
                        "NB-HVERA"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 23.77,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 675 Bytes) of tunneled, high-entropy traffic through DNS (domain: SRV-AZADCONNECT.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-FBENEGAS.\" The typical volume of traffic transmitted through this tunnel is 23 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "c621d77c-119a-4ad6-afc7-e193167b3a701790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43576,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 563,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Ucu096ABI3UnQyDOH576",
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
                        "NB-RLLEDO.technoma.local"
                    ],
                    "domain_list": [
                        "NB-RLLEDO.technoma.local"
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
                    "duration": 63,
                    "end_bucket_time": 1790862300000,
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
                    "fidelity": 14.56,
                    "flow_score": 98,
                    "inbytes_delta": 200,
                    "inbytes_total": 622,
                    "inpkts_delta": 2,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-RLLEDO.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-RLLEDO.technoma.local",
                            "query_type": "A",
                            "transaction_id": 17288
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.79",
                                    "host_type": "A",
                                    "name": "NB-RLLEDO.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-RLLEDO.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-RLLEDO.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.79"
                            ],
                            "response_time": 0,
                            "transaction_id": 17288,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 17288
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
                    "orig_id": "Ucu096ABI3UnQyDOH576",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 84,
                    "outbytes_total": 510,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 54,
                    "receive_time": 1790862162023,
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
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601760,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 431080,
                        "status": "New"
                    },
                    "stellar_da_input": 1225,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "c621d77c-119a-4ad6-afc7-e193167b3a701790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862161674,
                    "timestamp_utc": "2026-10-01T13:42:41.000Z",
                    "tos": 0,
                    "total_entropy": 160,
                    "totalbytes": 1132,
                    "totalpackets": 3,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ADIARTE",
                        "NB-ODACOSTA",
                        "NB-AORTELLADO",
                        "NB-CARANDA",
                        "NB-NSANCHEZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 27.67,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 563 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-RLLEDO.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AORTELLADO.\" The typical volume of traffic transmitted through this tunnel is 27 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "2303944a-e86c-4048-aa7d-6aaa6a412d091790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43577,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 534,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "kMy396ABI3UnQyDOWyEM",
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
                        "NB-TMARIN.technoma.local"
                    ],
                    "domain_list": [
                        "NB-TMARIN.technoma.local"
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
                    "duration": 1,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 100,
                    "inbytes_total": 100,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-TMARIN.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-TMARIN.technoma.local",
                            "query_type": "A",
                            "transaction_id": 54409
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.126",
                                    "host_type": "A",
                                    "name": "NB-TMARIN.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-TMARIN.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 1,
                            "query": "NB-TMARIN.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.126"
                            ],
                            "response_time": 1,
                            "transaction_id": 54409,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 54409
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "kMy396ABI3UnQyDOWyEM",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 84,
                    "outbytes_total": 84,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 1,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 51,
                    "receive_time": 1790862379413,
                    "response_time": 1,
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
                    "srcport": 55974,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601776,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 220269,
                        "status": "New"
                    },
                    "stellar_da_input": 1224,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "2303944a-e86c-4048-aa7d-6aaa6a412d091790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862198712,
                    "timestamp_utc": "2026-10-01T13:43:18.000Z",
                    "tos": 0,
                    "total_entropy": 154,
                    "totalbytes": 184,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-AMARTINEZ",
                        "NB-AZORRILLA",
                        "NB-FCANDIA",
                        "NB-GCABANAS",
                        "NB-HCOLMAN"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 19.36,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 534 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TMARIN.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AMARTINEZ.\" The typical volume of traffic transmitted through this tunnel is 19 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "14c4f60a-29a9-4073-a943-13d4d0b85d031790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43578,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 655,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "w8y496ABI3UnQyDOHTnl",
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
                        "NB-WGONZALEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-WGONZALEZ.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 63,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 25.43,
                    "flow_score": 98,
                    "inbytes_delta": 103,
                    "inbytes_total": 103,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-WGONZALEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-WGONZALEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 31725
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.46",
                                    "host_type": "A",
                                    "name": "NB-WGONZALEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-WGONZALEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-WGONZALEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.46"
                            ],
                            "response_time": 0,
                            "transaction_id": 31725,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 31725
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "w8y496ABI3UnQyDOHTnl",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 87,
                    "outbytes_total": 87,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 62,
                    "receive_time": 1790862421475,
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
                    "srcport": 60634,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601817,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 171033,
                        "status": "New"
                    },
                    "stellar_da_input": 1232,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "14c4f60a-29a9-4073-a943-13d4d0b85d031790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862239364,
                    "timestamp_utc": "2026-10-01T13:43:59.000Z",
                    "tos": 0,
                    "total_entropy": 190,
                    "totalbytes": 190,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ARUIZ",
                        "NB-RDESCALZO",
                        "NB-DFERNANDEZ",
                        "NB-JAQUINO",
                        "NB-ECANETE"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 18.8,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 655 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-WGONZALEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-DFERNANDEZ.\" The typical volume of traffic transmitted through this tunnel is 18 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "02db6c6e-6783-4ca4-a58c-f1409d9bd28d1790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43579,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 609,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "bcy496ABI3UnQyDOtVAm",
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
                        "NB-SFERNANDEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-SFERNANDEZ.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862300000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 58,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 19.97,
                    "flow_score": 98,
                    "inbytes_delta": 104,
                    "inbytes_total": 104,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 46365
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.120",
                                    "host_type": "A",
                                    "name": "NB-SFERNANDEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-SFERNANDEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-SFERNANDEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.120"
                            ],
                            "response_time": 0,
                            "transaction_id": 46365,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 46365
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "bcy496ABI3UnQyDOtVAm",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 88,
                    "outbytes_total": 88,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 57,
                    "receive_time": 1790862461578,
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
                    "srcport": 57644,
                    "start_bucket_time": 1790862000000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862601842,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 131053,
                        "status": "New"
                    },
                    "stellar_da_input": 1236,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "02db6c6e-6783-4ca4-a58c-f1409d9bd28d1790862602678-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862281049,
                    "timestamp_utc": "2026-10-01T13:44:41.000Z",
                    "tos": 0,
                    "total_entropy": 175,
                    "totalbytes": 192,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ADIARTE",
                        "NB-ALPIZZUTI",
                        "NB-AORTELLADO",
                        "NB-GVERA",
                        "NB-JMARIN"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 18.33,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862602678,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 609 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-SFERNANDEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AORTELLADO.\" The typical volume of traffic transmitted through this tunnel is 18 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "b375dbc2-10ba-4cba-a8fb-39aa8d38b0821790862841821-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43593,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 1,
                    "aella_tuples": "10.11.1.2.10.11.1.1.49672.4346",
                    "alert_time": 1790862841737,
                    "app_path": "dcerpc.msrpc",
                    "appid": 4346,
                    "appid_family": "Application",
                    "appid_name": "ms_ad",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-10-01 13:51:30 UTC",
                        "first_timestamp": 1790862690226,
                        "last_time_utc": "2026-10-01 13:51:30 UTC",
                        "last_timestamp": 1790862690226,
                        "repeat_count": 1,
                        "time_window_ms": 86400000
                    },
                    "ath_info": {
                        "rule_name": "exploit_attempt",
                        "scheduled_time_utc": "2026-10-01T13:52:00.000Z",
                        "scheduled_timestamp": 1790862720000
                    },
                    "correlation_info": [
                        {
                            "_id": "39954806-e5b9-4d00-949d-13e8040fce8e1790808003465-YWVsbGEtc2VyLTIwMjYuMDkuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                            "dstip": "10.11.1.2",
                            "dstip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                            "ids": {
                                "signature": "HUNTING Possible Powershell .ps1 Script Use Over SMB"
                            },
                            "index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                            "original_event": {
                                "actual": 7,
                                "aella_tuples": "10.11.1.1.10.11.1.2.445.4346",
                                "anomaly_id": "xot09KABI3UnQyDOf9CH",
                                "anomaly_tag": "rare",
                                "app_path": "smb.dcerpc",
                                "appid": 4346,
                                "appid_family": "Application",
                                "appid_name": "smb",
                                "appid_stdport": "yes",
                                "cust_file": 0,
                                "days_silent": 128,
                                "detected_fields": [
                                    "ids.signature",
                                    "ids.severity"
                                ],
                                "detected_values": [
                                    "HUNTING Possible Powershell .ps1 Script Use Over SMB",
                                    "high"
                                ],
                                "direction": "EveTxRx",
                                "dscp_name": "Best Effort",
                                "dst_tuples": "null.1101.10.11.1.2",
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
                                "dstport": 445,
                                "duration": 12162,
                                "end_bucket_time": 1790807700000,
                                "engid": "4e3eab0649114a80a089a5d5a078994d",
                                "engid_gateway": "181.103.4.178",
                                "engid_name": "technoma-sensor",
                                "event_category": "killchain",
                                "event_name": "exploit_attempt_priv_priv",
                                "event_score": 79,
                                "event_source": "new_ml",
                                "event_status": "New",
                                "event_summary": {
                                    "dominant_severity": "high",
                                    "ids_signatures_summarize": [
                                        {
                                            "id": 2027204,
                                            "ids_severity": "high",
                                            "name": "HUNTING Possible Powershell .ps1 Script Use Over SMB"
                                        }
                                    ],
                                    "total_signatures": 1
                                },
                                "event_type": "exploit",
                                "fidelity": 87.03,
                                "file_extract_timestamp": 1790807665211,
                                "file_name": "",
                                "file_path": "",
                                "fileid": "",
                                "flow_score": 98,
                                "handler": "ids-event",
                                "ids": {
                                    "action": "allowed",
                                    "category": "Potentially Bad Traffic",
                                    "created_ts": "2019-04-16T00:00:00Z",
                                    "gid": 1,
                                    "metadata": {
                                        "affected_product": [
                                            "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                                        ],
                                        "attack_target": [
                                            "Client_Endpoint"
                                        ],
                                        "confidence": [
                                            "Medium"
                                        ],
                                        "created_at": [
                                            "2019_04_16"
                                        ],
                                        "deployment": [
                                            "Internal"
                                        ],
                                        "signature_severity": [
                                            "Informational"
                                        ],
                                        "tag": [
                                            "Description_Generated_By_Proofpoint_Nexus"
                                        ],
                                        "updated_at": [
                                            "2019_07_26"
                                        ]
                                    },
                                    "payload_details": {
                                        "app_proto": "smb",
                                        "flow": {
                                            "bytes_toclient": 246748,
                                            "bytes_toserver": 244841,
                                            "dest_ip": "10.11.1.2",
                                            "dest_port": 445,
                                            "pkts_toclient": 813,
                                            "pkts_toserver": 840,
                                            "src_ip": "10.11.1.1",
                                            "src_port": 50459,
                                            "start": "2026-09-30T22:34:09.284028+0000"
                                        }
                                    },
                                    "rev": 2,
                                    "rule": {
                                        "created": "2019_04_16",
                                        "rule": "\"alert smb any any -> $HOME_NET 445 (msg:\\\"ET HUNTING Possible Powershell .ps1 Script Use Over SMB\\\"; flow:established,to_server; content:\\\"SMB\\\"; depth:8; content:\\\"|00|.|00|p|00|s|00|1|00|\\\"; nocase; distance:0; classtype:bad-unknown; sid:2027204; rev:2; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, created_at 2019_04_16, deployment Internal, confidence Medium, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2019_07_26;)\\n\"",
                                        "updated": "2019_07_26"
                                    },
                                    "severity": "high",
                                    "signature": "HUNTING Possible Powershell .ps1 Script Use Over SMB",
                                    "signature_id": 2027204
                                },
                                "inbytes_delta": 2238,
                                "inbytes_total": 246748,
                                "inpkts_delta": 9,
                                "inpkts_total": 813,
                                "lateral": true,
                                "locid": "unassigned location",
                                "md5": "",
                                "metadata": [
                                    {
                                        "response": {
                                            "command": 11,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 5,
                                            "filename": "lsarpc",
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 5,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 11,
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 11,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 6,
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 6,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 10,
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 10,
                                            "nt_status": 259,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "response": {
                                            "command": 10,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 5,
                                            "filename": "technoma.local\\policies\\{21D4988D-E575-4017-8FFB-70C6D8D618F9}",
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 5,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 16,
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 16,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 5,
                                            "filename": "technoma.local\\policies\\{21D4988D-E575-4017-8FFB-70C6D8D618F9}\\gpt.ini",
                                            "version": 2
                                        },
                                        "response": {
                                            "command": 5,
                                            "nt_status": 0,
                                            "processing_time": 0,
                                            "response_time": 0,
                                            "version": 2
                                        }
                                    },
                                    {
                                        "request": {
                                            "command": 16,
                                            "version": 2
                                        }
                                    }
                                ],
                                "msg_class": "ids_event",
                                "msg_origin": {
                                    "processor": {
                                        "type": "maltrace"
                                    },
                                    "source": "modular_sensor"
                                },
                                "msgtype": 3,
                                "msgtype_name": "start",
                                "netid": 1101,
                                "netid_name": "vlan1101",
                                "new_file": 0,
                                "obsid": 3232239430,
                                "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                                "org_name": "Technoma",
                                "orig_id": "xot09KABI3UnQyDOf9CH",
                                "orig_index": "aella-maltrace-2026.09.30-e511c3fc54cd4d668bb67612c2ef4b04",
                                "outbytes_delta": 2280,
                                "outbytes_total": 244841,
                                "outpkts_delta": 10,
                                "outpkts_total": 840,
                                "port_name": "ethernet1",
                                "processing_time": 0,
                                "proto": 6,
                                "proto_name": "tcp",
                                "receive_time": 1790807665718,
                                "response_time": 0,
                                "score": 60,
                                "severity": 75,
                                "sha256": "",
                                "src_tuples": "null.1101.10.11.1.1",
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
                                "srcip_sig_id": "10.11.1.1.2027204",
                                "srcip_type": "private",
                                "srcip_version": "ipv4",
                                "srcmac": "00:50:56:af:ff:5a",
                                "srcport": 50459,
                                "start_bucket_time": 1790807400000,
                                "state": "Created",
                                "stellar": {
                                    "alert_time": 1790808003441,
                                    "alert_timestamp_field": "timestamp",
                                    "anomaly_tag_subtype": "rare",
                                    "detection_time": 332787,
                                    "status": "New"
                                },
                                "stellar_da_input": 1438,
                                "stellar_index_id": "aella-ser-2026.09.30-e511c3fc54cd4d668bb67612c2ef4b04",
                                "stellar_uuid": "39954806-e5b9-4d00-949d-13e8040fce8e1790808003465-YWVsbGEtc2VyLTIwMjYuMDkuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                                "tcp_rtt": 0,
                                "tenant_name": "technoma",
                                "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                                "threat_score": 0,
                                "timestamp": 1790807665527,
                                "timestamp_utc": "2026-09-30T22:34:25.000Z",
                                "tos": 2,
                                "totalbytes": 48457,
                                "totalpackets": 19,
                                "typical": 0,
                                "vlan": 1101,
                                "write_by": "sef",
                                "write_time": 1790808003465,
                                "xdr_event": {
                                    "description": "In internal traffic, a rarely seen exploit attempt with the IDS signature \"HUNTING Possible Powershell .ps1 Script Use Over SMB\" has been observed after 128 days of silence.",
                                    "display_name": "Private to Private Exploit Anomaly",
                                    "framework_version": "v8",
                                    "name": "exploit_attempt_priv_priv",
                                    "scope": "Internal",
                                    "subtype": {
                                        "display_name": "IDS Traffic Anomaly",
                                        "name": "ids_traffic_anomaly"
                                    },
                                    "tactic": {
                                        "id": "TA0008",
                                        "name": "Lateral Movement"
                                    },
                                    "tags": [
                                        "Internal",
                                        "Network Traffic Analysis"
                                    ],
                                    "technique": {
                                        "id": "T1210",
                                        "name": "Exploitation of Remote Services"
                                    },
                                    "xdr_killchain_stage": "Propagation",
                                    "xdr_killchain_version": "v1"
                                }
                            },
                            "query_name": "exploit",
                            "readable_name": "exploit",
                            "srcip": "10.11.1.1",
                            "srcip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                            "timestamp": 1790807665527,
                            "timestamp_utc": "2026-09-30T22:34:25.000Z",
                            "write_time": 1790808003465,
                            "write_time_utc": "2026-09-30T22:40:03.000Z"
                        },
                        {
                            "_id": "a8y896ABI3UnQyDOZObr",
                            "appid_name": "ms_ad",
                            "dstip": "10.11.1.1",
                            "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                            "index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.24-000058",
                            "original_event": {
                                "aella_tuples": "10.11.1.2.10.11.1.1.49672.4346",
                                "app_path": "dcerpc.msrpc",
                                "appid": 4346,
                                "appid_family": "Application",
                                "appid_name": "ms_ad",
                                "appid_stdport": "yes",
                                "dscp_name": "Best Effort",
                                "dst_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
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
                                "dstip_version": "ipv4",
                                "dstmac": "00:50:56:af:ff:5a",
                                "dstport": 49672,
                                "duration": 14364,
                                "end_reason": 5,
                                "engid": "4e3eab0649114a80a089a5d5a078994d",
                                "engid_gateway": "181.103.4.178",
                                "engid_name": "technoma-sensor",
                                "flow_score": 98,
                                "inbytes_delta": 2359,
                                "inbytes_total": 2359,
                                "inpkts_delta": 7,
                                "locid": "unassigned location",
                                "metadata": [
                                    {
                                        "request": {
                                            "message_type": "AP_REQ"
                                        },
                                        "response": {
                                            "message_type": "AP_REP",
                                            "processing_time": 0,
                                            "response_time": 0
                                        }
                                    },
                                    {
                                        "request": {
                                            "message_type": "AP_REP"
                                        }
                                    }
                                ],
                                "msg_class": "interflow_traffic",
                                "msg_origin": {
                                    "category": "traffic",
                                    "processor": {
                                        "type": "aella_flow"
                                    },
                                    "source": "modular_sensor"
                                },
                                "msgtype": 4,
                                "msgtype_name": "startend",
                                "netid": 1101,
                                "netid_name": "vlan1101",
                                "obsid": 3232239430,
                                "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                                "org_name": "Technoma",
                                "outbytes_delta": 3434,
                                "outbytes_total": 3434,
                                "outpkts_delta": 9,
                                "port_name": "ethernet1",
                                "processing_time": 0,
                                "proto": 6,
                                "proto_name": "tcp",
                                "receive_time": 1790862707352,
                                "response_time": 0,
                                "src_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                                "srcip": "10.11.1.2",
                                "srcip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
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
                                "srcip_host": "ad2.technoma.local",
                                "srcip_reputation": "Good",
                                "srcip_type": "private",
                                "srcip_version": "ipv4",
                                "srcmac": "00:50:56:af:55:19",
                                "srcport": 64957,
                                "state": "Aborted",
                                "stellar_da_input": 948,
                                "stellar_index_id": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                                "stellar_uuid": "45371b60-548a-4779-838e-ce364ebe674b1790862707352",
                                "tcp_rtt": 0,
                                "tenant_name": "technoma",
                                "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                                "threat_score": 0,
                                "timestamp": 1790862690226,
                                "timestamp_utc": "2026-10-01T13:51:30.000Z",
                                "tos": 2,
                                "totalbytes": 5793,
                                "totalpackets": 16,
                                "vlan": 1101,
                                "write_time": 1790862711962
                            },
                            "query_name": "seen_traffic",
                            "readable_name": "seen_traffic",
                            "srcip": "10.11.1.2",
                            "srcip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
                            "timestamp": 1790862690226,
                            "timestamp_utc": "2026-10-01T13:51:30.000Z",
                            "write_time": 1790862711962,
                            "write_time_utc": "2026-10-01T13:51:51.000Z"
                        }
                    ],
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
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
                    "dstip_version": "ipv4",
                    "dstmac": "00:50:56:af:ff:5a",
                    "dstport": 49672,
                    "duration": 14364,
                    "end_reason": 5,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_score": 78,
                    "event_status": "New",
                    "exploit_id": "39954806-e5b9-4d00-949d-13e8040fce8e1790808003465-YWVsbGEtc2VyLTIwMjYuMDkuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "exploit_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                    "fidelity": 87.03,
                    "flow_score": 98,
                    "ids": {
                        "action": "allowed",
                        "category": "Potentially Bad Traffic",
                        "created_ts": "2019-04-16T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Windows_XP_Vista_7_8_10_Server_32_64_Bit"
                            ],
                            "attack_target": [
                                "Client_Endpoint"
                            ],
                            "confidence": [
                                "Medium"
                            ],
                            "created_at": [
                                "2019_04_16"
                            ],
                            "deployment": [
                                "Internal"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "Description_Generated_By_Proofpoint_Nexus"
                            ],
                            "updated_at": [
                                "2019_07_26"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "smb",
                            "flow": {
                                "bytes_toclient": 246748,
                                "bytes_toserver": 244841,
                                "dest_ip": "10.11.1.2",
                                "dest_port": 445,
                                "pkts_toclient": 813,
                                "pkts_toserver": 840,
                                "src_ip": "10.11.1.1",
                                "src_port": 50459,
                                "start": "2026-09-30T22:34:09.284028+0000"
                            }
                        },
                        "rev": 2,
                        "rule": {
                            "created": "2019_04_16",
                            "rule": "\"alert smb any any -> $HOME_NET 445 (msg:\\\"ET HUNTING Possible Powershell .ps1 Script Use Over SMB\\\"; flow:established,to_server; content:\\\"SMB\\\"; depth:8; content:\\\"|00|.|00|p|00|s|00|1|00|\\\"; nocase; distance:0; classtype:bad-unknown; sid:2027204; rev:2; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, created_at 2019_04_16, deployment Internal, confidence Medium, signature_severity Informational, tag Description_Generated_By_Proofpoint_Nexus, updated_at 2019_07_26;)\\n\"",
                            "updated": "2019_07_26"
                        },
                        "severity": "high",
                        "signature": "HUNTING Possible Powershell .ps1 Script Use Over SMB",
                        "signature_id": 2027204
                    },
                    "inbytes_delta": 2359,
                    "inbytes_total": 2359,
                    "indices": {
                        "exploit": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                        "seen_traffic": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.24-000058"
                    },
                    "inpkts_delta": 7,
                    "locid": "unassigned location",
                    "metadata": [
                        {
                            "request": {
                                "message_type": "AP_REQ"
                            },
                            "response": {
                                "message_type": "AP_REP",
                                "processing_time": 0,
                                "response_time": 0
                            }
                        },
                        {
                            "request": {
                                "message_type": "AP_REP"
                            }
                        }
                    ],
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "39954806-e5b9-4d00-949d-13e8040fce8e1790808003465-YWVsbGEtc2VyLTIwMjYuMDkuMzAtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "orig_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                    "orig_timestamp": 1790862690226,
                    "orig_timestamp_utc": "2026-10-01T13:51:30.000Z",
                    "orig_write_time": 1790862841401,
                    "outbytes_delta": 3434,
                    "outbytes_total": 3434,
                    "outpkts_delta": 9,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790862707352,
                    "response_time": 0,
                    "seen_traffic_id": "a8y896ABI3UnQyDOZObr",
                    "seen_traffic_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.24-000058",
                    "severity": 75,
                    "src_tuples": "00:50:56:af:55:19.1101.10.11.1.2",
                    "srcip": "10.11.1.2",
                    "srcip_assetid": "3173e6f2-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "ad2.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:55:19",
                    "srcport": 64957,
                    "state": "Aborted",
                    "stellar": {
                        "alert_time": 1790862841737,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 129775,
                        "status": "New"
                    },
                    "stellar_da_input": 948,
                    "stellar_index": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "b375dbc2-10ba-4cba-a8fb-39aa8d38b0821790862841821-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 0,
                    "tenant_info": {
                        "tenant_name": "technoma",
                        "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04"
                    },
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862690226,
                    "timestamp_utc": "2026-10-01T13:51:30.000Z",
                    "tos": 2,
                    "totalbytes": 5793,
                    "totalpackets": 16,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862841821,
                    "write_time_utc": "2026-10-01T13:54:01.736Z",
                    "xdr_event": {
                        "description": "An exploited host with vulnerabilities initiated a connection to the exploit attacker, which could indicate the host being compromised and performing C&C activities. See if the exploit was successful. Check the source host, and consider blocking.",
                        "display_name": "Exploited C&C Connection",
                        "event_source": "built-in-playbook",
                        "framework_version": "v8",
                        "name": "exploit_attempt_correlation",
                        "scope": "Internal",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2014",
                            "name": "XDR Command and Control Connection Exploitation"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "6752de49-f318-47b3-83b8-41be055e68581790862902032-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43594,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 573,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Tcy596ABI3UnQyDOeW-E",
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
                        "NB-TIBANEZ.technoma.local"
                    ],
                    "domain_list": [
                        "NB-TIBANEZ.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 53,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 15.26,
                    "flow_score": 98,
                    "inbytes_delta": 101,
                    "inbytes_total": 101,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "transaction_id": 2677
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.81",
                                    "host_type": "A",
                                    "name": "NB-TIBANEZ.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-TIBANEZ.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-TIBANEZ.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.81"
                            ],
                            "response_time": 0,
                            "transaction_id": 2677,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 2677
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "Tcy596ABI3UnQyDOeW-E",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 85,
                    "outbytes_total": 85,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 55,
                    "receive_time": 1790862513876,
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
                    "srcport": 57071,
                    "start_bucket_time": 1790862300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862901970,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 381018,
                        "status": "New"
                    },
                    "stellar_da_input": 1224,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6752de49-f318-47b3-83b8-41be055e68581790862902032-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862331759,
                    "timestamp_utc": "2026-10-01T13:45:31.000Z",
                    "tos": 0,
                    "total_entropy": 168,
                    "totalbytes": 186,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ACHAMORRO",
                        "NB-AGILL",
                        "NB-DLOVERA",
                        "NB-FKOCHMANN",
                        "NB-FROJAS"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 30.8,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862902032,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 573 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-TIBANEZ.technoma.local) has been observed between \"IP: 10.11.1.1, name: ad.technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-ACHAMORRO.\" The typical volume of traffic transmitted through this tunnel is 30 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "2e741f61-4ffe-4218-bb48-7de6df7d9d441790862902742-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43595,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 204,
                    "aella_tuples": "10.212.134.209.10.11.1.1.53.4",
                    "anomaly_id": "38y496ABI3UnQyDOlEwF",
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
                    "domain_creation": 1790862343484,
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
                    "end_bucket_time": 1790862600000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790862343484
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
                    "fidelity": 89.21,
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
                        "event_time": "2026-10-01 10:45:43",
                        "eventtime": "1790862343483505487",
                        "level": "notice",
                        "logid": "0000000013",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "DNS",
                        "sessionid": "697773193",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "10:45:43",
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
                    "orig_id": "38y496ABI3UnQyDOlEwF",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-10-01 time=10:45:43 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790862343483505487 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.209 srcport=42545 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.11.1.1 dstport=53 dstintf=\"Citrix Servers\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=697773193 proto=17 action=\"deny\" policyid=0 policytype=\"policy\" user=\"sati\" authserver=\"sati\" dstuser=\"FLAVIOBENEGAS\" service=\"DNS\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\"",
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790862456480,
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
                    "srcport": 42545,
                    "start_bucket_time": 1790862300000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790862902721,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 440866,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2357,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "2e741f61-4ffe-4218-bb48-7de6df7d9d441790862902742-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862343484,
                    "timestamp_utc": "2026-10-01T13:45:43.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 23,
                    "user": {
                        "name": "sati"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790862902742,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 10.212.134.209 private) has had actions blocked by a firewall too many times (#: 204), compared to the typical number of blocks (#: 23), measured in a 5.0-minute interval.",
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
                "_id": "cb9207e1-8bb4-4169-a71c-ba1e90c2703f1790862903919-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43605,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 8.5,
                    "aella_tuples": "10.11.1.1.8.8.8.8.53.32",
                    "anomaly_id": "gsy396ABI3UnQyDOAQ7g",
                    "anomaly_tag": "spike",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "cust_file": 0,
                    "detected_fields": [
                        "ids.signature",
                        "ids.severity"
                    ],
                    "detected_values": [
                        "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "low"
                    ],
                    "direction": "EveTxRx",
                    "domain_list": [
                        "trouter-atm-pub-ent.trafficmanager.NET"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dstip": "8.8.8.8",
                    "dstip_asn": 15169,
                    "dstip_asn_org": "Google LLC",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.751,
                        "longitude": -97.822,
                        "region": "Unknown"
                    },
                    "dstip_geo_point": "37.751,-97.822",
                    "dstip_host": "dns.google",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:09:0f:09:0a:04",
                    "dstport": 53,
                    "duration": 58182,
                    "end_bucket_time": 1790862600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "exploit_attempt_priv_pub",
                    "event_score": 27,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "dominant_severity": "low",
                        "ids_signatures_summarize": [
                            {
                                "id": 2060507,
                                "ids_severity": "low",
                                "name": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup"
                            }
                        ],
                        "total_signatures": 1
                    },
                    "event_type": "exploit",
                    "fidelity": 50.98,
                    "file_extract_timestamp": 1790862351517,
                    "file_name": "",
                    "file_path": "",
                    "fileid": "",
                    "flow_score": 98,
                    "handler": "ids-event",
                    "ids": {
                        "action": "allowed",
                        "category": "Misc activity",
                        "created_ts": "2025-03-03T00:00:00Z",
                        "gid": 1,
                        "metadata": {
                            "affected_product": [
                                "Any"
                            ],
                            "attack_target": [
                                "Client_and_Server"
                            ],
                            "confidence": [
                                "High"
                            ],
                            "created_at": [
                                "2025_03_03"
                            ],
                            "deployment": [
                                "Perimeter"
                            ],
                            "mitre_tactic_id": [
                                "TA0011"
                            ],
                            "mitre_tactic_name": [
                                "Command_And_Control"
                            ],
                            "mitre_technique_id": [
                                "T1219"
                            ],
                            "mitre_technique_name": [
                                "Remote_Access_Software"
                            ],
                            "performance_impact": [
                                "Low"
                            ],
                            "signature_severity": [
                                "Informational"
                            ],
                            "tag": [
                                "AnyDesk"
                            ],
                            "updated_at": [
                                "2025_03_03"
                            ]
                        },
                        "payload_details": {
                            "app_proto": "dns",
                            "dns": {
                                "flags": "100",
                                "id": 23602,
                                "opcode": 0,
                                "queries": [
                                    {
                                        "rrname": "relay-8a3338e6.net.anydesk.com",
                                        "rrtype": "A"
                                    }
                                ],
                                "rcode": "NOERROR",
                                "rd": true,
                                "tx_id": 0,
                                "type": "request",
                                "version": 3
                            },
                            "flow": {
                                "bytes_toclient": 0,
                                "bytes_toserver": 105,
                                "dest_ip": "8.8.8.8",
                                "dest_port": 53,
                                "pkts_toclient": 0,
                                "pkts_toserver": 1,
                                "src_ip": "10.11.1.1",
                                "src_port": 61918,
                                "start": "2026-10-01T13:45:51.517755+0000"
                            }
                        },
                        "rev": 1,
                        "rule": {
                            "created": "2025_03_03",
                            "rule": "\"alert dns $HOME_NET any -> any any (msg:\\\"ET INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\\\"; dns.query; dotprefix; content:\\\".net.anydesk.com\\\"; nocase; endswith; reference:url,support.anydesk.com/knowledge/firewall; classtype:misc-activity; sid:2060507; rev:1; metadata:affected_product Any, attack_target Client_and_Server, created_at 2025_03_03, deployment Perimeter, performance_impact Low, confidence High, signature_severity Informational, tag AnyDesk, updated_at 2025_03_03, mitre_tactic_id TA0011, mitre_tactic_name Command_And_Control, mitre_technique_id T1219, mitre_technique_name Remote_Access_Software;)\\n\"",
                            "updated": "2025_03_03"
                        },
                        "severity": "low",
                        "signature": "INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup",
                        "signature_id": 2060507
                    },
                    "inbytes_delta": 634,
                    "inbytes_total": 0,
                    "inpkts_delta": 2,
                    "inpkts_total": 0,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "md5": "",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2005-11-25T00:16:41Z",
                            "effective_tld": "trafficmanager.net",
                            "flags": 256,
                            "host_type": "OPT",
                            "message_type": "QUERY",
                            "query": "trouter-atm-pub-ent.trafficmanager.NET",
                            "query_type": "HTTPS",
                            "section_type": "Additional Answer",
                            "transaction_id": 15984
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "pub-ent-uswe-10-t.trouter.teams.microsoft.com",
                                    "host_type": "CNAME",
                                    "name": "trouter-atm-pub-ent.trafficmanager.NET",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host": "partition-cname-trouter.pub-ent-uswe-10.ic3-edf-trouter.westus-prod.cosmic.office.NET",
                                    "host_type": "CNAME",
                                    "name": "pub-ent-uswe-10-t.trouter.teams.microsoft.com",
                                    "section_type": "Answer",
                                    "ttl": 1724
                                },
                                {
                                    "host": "cosmic-westus-ns-7af9208f098f.trafficmanager.NET",
                                    "host_type": "CNAME",
                                    "name": "partition-cname-trouter.pub-ent-uswe-10.ic3-edf-trouter.westus-prod.cosmic.office.NET",
                                    "section_type": "Answer",
                                    "ttl": 15
                                },
                                {
                                    "host": "partition-cname-trouter-ic3-edf-trouter-service-trouter-2.d02-651.ic3-edf-trouter.01-westus-prod.cosmic.office.NET",
                                    "host_type": "CNAME",
                                    "name": "cosmic-westus-ns-7af9208f098f.trafficmanager.NET",
                                    "section_type": "Answer",
                                    "ttl": 15
                                },
                                {
                                    "host": "ns1-33.azure-dns.com",
                                    "host_type": "SOA",
                                    "name": "01-westus-prod.cosmic.office.NET",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 300
                                },
                                {
                                    "host_type": "OPT",
                                    "section_type": "Additional Answer"
                                }
                            ],
                            "domain_creation": "2005-11-25T00:16:41Z",
                            "effective_tld": "trafficmanager.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 40,
                            "query": "trouter-atm-pub-ent.trafficmanager.NET",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 40,
                            "transaction_id": 15984
                        },
                        "transaction_id": 15984
                    },
                    "msg_class": "ids_event",
                    "msg_origin": {
                        "processor": {
                            "type": "maltrace"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "new_file": 0,
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "gsy396ABI3UnQyDOAQ7g",
                    "orig_index": "aella-maltrace-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 191,
                    "outbytes_total": 105,
                    "outpkts_delta": 2,
                    "outpkts_total": 1,
                    "port_name": "ethernet1",
                    "processing_time": 33,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790862352154,
                    "response_time": 33,
                    "score": 30,
                    "severity": 20,
                    "sha256": "",
                    "src_tuples": "null.1101.10.11.1.1",
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
                    "srcip_sig_id": "10.11.1.1.2060507",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 61918,
                    "start_bucket_time": 1790862300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862903913,
                        "alert_timestamp_field": "timestamp",
                        "anomaly_tag_subtype": "individual_spike",
                        "detection_time": 542870,
                        "status": "New"
                    },
                    "stellar_da_input": 1698,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "cb9207e1-8bb4-4169-a71c-ba1e90c2703f1790862903919-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862351962,
                    "timestamp_utc": "2026-10-01T13:45:51.000Z",
                    "tos": 0,
                    "totalbytes": 825,
                    "totalpackets": 4,
                    "typical": 1.5,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862903919,
                    "xdr_event": {
                        "description": "In traffic from internal to external hosts, an anomalously high number (#: 17.0) of exploit attempts with the IDS signature \"INFO Anydesk Relay Domain (net .anydesk .com) in DNS Lookup\" were observed in a 5.0-minute interval. The accumulated ids.severity of these exploit attempts spiked to (#: 8.5) from the typical value of (#: 1.5), with \"critical\" IDS signatures counted as 2, \"high\" counted as 1, \"low\" counted as 0.5, and others counted as 1.",
                        "display_name": "Private to Public Exploit Anomaly",
                        "framework_version": "v8",
                        "name": "exploit_attempt_priv_pub",
                        "scope": "External",
                        "subtype": {
                            "display_name": "IDS Traffic Anomaly",
                            "name": "ids_traffic_anomaly"
                        },
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "T1190",
                            "name": "Exploit Public-Facing Application"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "fd9bc799-3c99-4c70-b4cd-92eb641708c91790862903049-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43596,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 602,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "Tsy696ABI3UnQyDOFo2w",
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
                        "NB-ODACOSTA.technoma.local"
                    ],
                    "domain_list": [
                        "NB-ODACOSTA.technoma.local"
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
                    "duration": 0,
                    "end_bucket_time": 1790862600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 57,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 18.93,
                    "flow_score": 98,
                    "inbytes_delta": 102,
                    "inbytes_total": 102,
                    "inpkts_delta": 1,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "NB-ODACOSTA.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "NB-ODACOSTA.technoma.local",
                            "query_type": "A",
                            "transaction_id": 55033
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "192.168.169.76",
                                    "host_type": "A",
                                    "name": "NB-ODACOSTA.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "NB-ODACOSTA.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "NB-ODACOSTA.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "192.168.169.76"
                            ],
                            "response_time": 0,
                            "transaction_id": 55033,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 55033
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 4,
                    "msgtype_name": "startend",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "Tsy696ABI3UnQyDOFo2w",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 86,
                    "outbytes_total": 86,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 56,
                    "receive_time": 1790862553500,
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
                    "srcip_host": "technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:50:56:af:ff:5a",
                    "srcport": 52983,
                    "start_bucket_time": 1790862300000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1790862902003,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 341038,
                        "status": "New"
                    },
                    "stellar_da_input": 1229,
                    "stellar_index_id": "aella-ser-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "fd9bc799-3c99-4c70-b4cd-92eb641708c91790862903049-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790862372310,
                    "timestamp_utc": "2026-10-01T13:46:12.000Z",
                    "tos": 0,
                    "total_entropy": 171,
                    "totalbytes": 188,
                    "totalpackets": 2,
                    "tunnel_domain": "technoma.local",
                    "tunnel_payloads": [
                        "NB-ANGELRA2",
                        "NB-AORTELLADO",
                        "NB-ARESQUIN",
                        "NB-ASAUCEDO",
                        "NB-CALVAREZ"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 22.8,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790862903049,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 602 Bytes) of tunneled, high-entropy traffic through DNS (domain: NB-ODACOSTA.technoma.local) has been observed between \"IP: 10.11.1.1, name: technoma.local\" and \"IP: 10.11.1.2, name: ad2.technoma.local\". One of the tunnel payloads is \"NB-AORTELLADO.\" The typical volume of traffic transmitted through this tunnel is 22 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "3cede955-25e1-44a4-8225-9b742069fa351790862903049-YWVsbGEtc2VyLTIwMjYuMTAuMDEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 43597,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 566,
                    "aella_tuples": "10.11.1.1.10.11.1.2.53.32",
                    "anomaly_id": "BMy396ABI3UnQyDO9zjx",
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
                        "SRV-AZADCONNECT.technoma.local"
                    ],
                    "domain_list": [
                        "SRV-AZADCONNECT.technoma.local"
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
                    "duration": 43,
                    "end_bucket_time": 1790862600000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 51,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 13.73,
                    "flow_score": 98,
                    "inbytes_delta": 207,
                    "inbytes_total": 613,
                    "inpkts_delta": 2,
                    "is_dga": "pending",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "transaction_id": 1360
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "10.11.1.3",
                                    "host_type": "A",
                                    "name": "SRV-AZADCONNECT.technoma.local",
                                    "section_type": "Answer",
                                    "ttl": 1200
                                }
                            ],
                            "effective_tld": "SRV-AZADCONNECT.technoma.local",
                            "flags": 34176,
                            "message_type": "RESPONSE",
                            "processing_time": 0,
                            "query": "SRV-AZADCONNECT.technoma.local",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "10.11.1.3"
                            ],
                            "response_time": 0,
                            "transaction_id": 1360,
                            "whois_query_attempt": 1,
                            "whois_query_flag": 1
                        },
                        "transaction_id": 1360
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
                    "orig_id": "BMy396ABI3UnQyDO9zjx",
                    "orig_index": "aella-adr-2026.10.01-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 90,
                    "outbytes_total": 517,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 53,
                    "receive_time": 1790862417523,
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
                    "srcma
<truncated 3798 bytes>

NOTE: The output was truncated because it was too long. Use a more targeted query or a smaller range to get the information you need.