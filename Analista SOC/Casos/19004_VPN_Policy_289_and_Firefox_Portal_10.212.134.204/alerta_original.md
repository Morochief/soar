# Alertas Originales Interflow / Stellar Cyber - Lote de 4 Eventos

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "e45b9f8d-867a-4b49-9bd3-0d25c5e22f5d1790250302924-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19004,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "close",
                    "actual": 1,
                    "aella_tuples": "10.212.134.204.10.186.73.251.8089.4",
                    "anomaly_id": "0-E006ABI3UnQyDOs8u0",
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "tcp/8089",
                    "appid_stdport": "yes",
                    "days_silent": 37,
                    "detected_fields": [
                        "fw_policy_id"
                    ],
                    "detected_values": [
                        "FG-Technoma_289"
                    ],
                    "detector_index": 0,
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1790249827808,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.10.186.73.251",
                    "dstip": "10.186.73.251",
                    "dstip_assetid": "ed1e1b66-b20e-11f1-bdc7-32ca1fa0b082",
                    "dstip_geo": {
                        "city": "Unknown",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "10.186.73.251",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 8089,
                    "duration": 1,
                    "end_bucket_time": 1790250000000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1790249827808
                    },
                    "event_category": "network",
                    "event_name": "fw_policy_id",
                    "event_score": 45,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_summary": {
                        "fw_utm_policy": []
                    },
                    "event_type": "conn",
                    "fidelity": 56.66,
                    "fortinet": {
                        "appcat": "unscanned",
                        "authserver": "LDAP_Tech",
                        "date": "2026-09-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "VMEDIA-2",
                        "dstintfrole": "undefined",
                        "event_time": "2026-09-24 08:37:08",
                        "eventtime": "1790249827807881227",
                        "group": "VPN_POSVENTA",
                        "level": "notice",
                        "logid": "0000000013",
                        "policyname": "SSLVPN_TO_ITTI_VOIP",
                        "policytype": "policy",
                        "poluuid": "559febf6-23a3-51f1-86f1-91c963e9e2da",
                        "rule_id": 289,
                        "service": "tcp/8089",
                        "sessionid": "4289969079",
                        "srccountry": "Reserved",
                        "srcintf": "ssl.root",
                        "srcintfrole": "undefined",
                        "subtype": "forward",
                        "time": "08:37:08",
                        "trandisp": "snat",
                        "transip": "172.22.22.246",
                        "transport": "65345",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vpntype": "ipsecvpn"
                    },
                    "fw_policy_id": "FG-Technoma_289",
                    "inbytes_total": 2651,
                    "inpkts_delta": 6,
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
                    "orig_id": "0-E006ABI3UnQyDOs8u0",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 2238,
                    "outpkts_delta": 8,
                    "parser_raw_msg": "<189>date=2026-09-24 time=08:37:08 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1790249827807881227 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=10.212.134.204 srcport=65345 srcintf=\"ssl.root\" srcintfrole=\"undefined\" dstip=10.186.73.251 dstport=8089 dstintf=\"VMEDIA-2\" dstintfrole=\"undefined\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=4289969079 proto=6 action=\"close\" policyid=289 policytype=\"policy\" poluuid=\"559febf6-23a3-51f1-86f1-91c963e9e2da\" policyname=\"SSLVPN_TO_ITTI_VOIP\" user=\"federicoobregon\" group=\"VPN_POSVENTA\" authserver=\"LDAP_Tech\" service=\"tcp/8089\" trandisp=\"snat\" transip=172.22.22.246 transport=65345 appcat=\"unscanned\" duration=1 sentbyte=2238 rcvdbyte=2651 sentpkt=8 rcvdpkt=6 vpntype=\"ipsecvpn\"",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1790249831482,
                    "severity": 40,
                    "src_tuples": "00:00:00:00:00:00.0.10.212.134.204",
                    "srcip": "10.212.134.204",
                    "srcip_assetid": "496177b0-cad9-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "10.212.134.204",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 65345,
                    "start_bucket_time": 1790249700000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790250302889,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 462340,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2575,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "e45b9f8d-867a-4b49-9bd3-0d25c5e22f5d1790250302924-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790249827808,
                    "timestamp_utc": "2026-09-24T11:37:07.000Z",
                    "totalbytes": 4889,
                    "totalpackets": 14,
                    "typical": 0,
                    "user": {
                        "name": "federicoobregon"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1790250302923,
                    "xdr_event": {
                        "description": "In internal traffic, the connection from IP/name: 10.212.134.204 (private) to IP/name: 10.186.73.251 (private) has triggered a policy (ID: \"FG-Technoma_289\") that has never been observed by Stellar Cyber before (or been seen very rarely) on the firewall (type: \"fw_fortigate\") after 37 days of silence.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "e353fe55-5a85-4a40-8398-e1b246a339961790254988779-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19125,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.212.134.204.10.11.1.1.53.32",
                    "alert_time": 1790254988661,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 13:00:10 UTC",
                        "first_timestamp": 1790254810315,
                        "last_time_utc": "2026-09-24 13:00:10 UTC",
                        "last_timestamp": 1790254810315,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T13:01:00.000Z",
                        "scheduled_timestamp": 1790254860000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "firefox-portal-detection.com",
                        "2026-07-01T15:40:13Z"
                    ],
                    "domain_list": [
                        "firefox-portal-detection.com"
                    ],
                    "domain_reputation": "Good",
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
                    "dstport": 53,
                    "duration": 1534,
                    "end_bucket_time": 1790254860000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "transaction_id": 18930
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "section_type": "Answer"
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 27,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.65.91"
                            ],
                            "response_time": 27,
                            "transaction_id": 18930
                        },
                        "transaction_id": 18930
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 3,
                    "msgtype_name": "replica",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "k-uA06ABI3UnQyDOtAL5",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790254810315,
                    "orig_timestamp_utc": "2026-09-24T13:00:10.000Z",
                    "orig_write_time": 1790254820587,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 13,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790254811078,
                    "response_time": 13,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.10.212.134.204",
                    "srcip": "10.212.134.204",
                    "srcip_assetid": "496177b0-cad9-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-jraguero.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 59119,
                    "start_bucket_time": 1790254560000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1790254988661,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 168074,
                        "status": "New"
                    },
                    "stellar_da_input": 3348,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e353fe55-5a85-4a40-8398-e1b246a339961790254988779-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790254860000,
                    "summary_start": 1790254560000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790254810315,
                    "timestamp_utc": "2026-09-24T13:00:10.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790254988779,
                    "xdr_event": {
                        "description": "A host \"IP: 10.212.134.204, name: nb-jraguero.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
                        "display_name": "Recently Registered Domains",
                        "framework_version": "v8",
                        "name": "new_registered_domain",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2008",
                            "name": "XDR New Domain"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "89ed052e-cd8c-4767-b0cb-ef27c4ec0b3f1790255886017-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19190,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.212.134.204.10.11.1.1.53.32",
                    "alert_time": 1790255885893,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 13:14:11 UTC",
                        "first_timestamp": 1790255651722,
                        "last_time_utc": "2026-09-24 13:14:11 UTC",
                        "last_timestamp": 1790255651722,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T13:16:00.000Z",
                        "scheduled_timestamp": 1790255760000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "firefox-portal-detection.com",
                        "2026-07-01T15:40:13Z"
                    ],
                    "domain_list": [
                        "firefox-portal-detection.com"
                    ],
                    "domain_reputation": "Good",
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
                    "dstport": 53,
                    "end_bucket_time": 1790255760000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 382,
                    "inbytes_total": 382,
                    "inpkts_delta": 3,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "transaction_id": 34825
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.1.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.193.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.129.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 27,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.65.91",
                                "151.101.1.91",
                                "151.101.193.91",
                                "151.101.129.91"
                            ],
                            "response_time": 27,
                            "transaction_id": 34825
                        },
                        "transaction_id": 34825
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "V-yN06ABI3UnQyDOh-Ac",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790255651722,
                    "orig_timestamp_utc": "2026-09-24T13:14:11.000Z",
                    "orig_write_time": 1790255660803,
                    "outbytes_delta": 337,
                    "outbytes_total": 337,
                    "outpkts_delta": 4,
                    "port_name": "ethernet1",
                    "processing_time": 14,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790255653903,
                    "response_time": 14,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.10.212.134.204",
                    "srcip": "10.212.134.204",
                    "srcip_assetid": "496177b0-cad9-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-jraguero.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 61112,
                    "start_bucket_time": 1790255460000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1790255885893,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 225090,
                        "status": "New"
                    },
                    "stellar_da_input": 2938,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "89ed052e-cd8c-4767-b0cb-ef27c4ec0b3f1790255886017-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790255760000,
                    "summary_start": 1790255460000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790255651722,
                    "timestamp_utc": "2026-09-24T13:14:11.000Z",
                    "tos": 0,
                    "totalbytes": 719,
                    "totalpackets": 7,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790255886017,
                    "xdr_event": {
                        "description": "A host \"IP: 10.212.134.204, name: nb-jraguero.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
                        "display_name": "Recently Registered Domains",
                        "framework_version": "v8",
                        "name": "new_registered_domain",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2008",
                            "name": "XDR New Domain"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "e9bba582-c0ef-4db9-8a61-4531d838bb241790257386328-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19242,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "10.212.134.204.10.11.1.1.53.32",
                    "alert_time": 1790257386190,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 13:36:44 UTC",
                        "first_timestamp": 1790257004080,
                        "last_time_utc": "2026-09-24 13:36:44 UTC",
                        "last_timestamp": 1790257004080,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T13:41:00.000Z",
                        "scheduled_timestamp": 1790257260000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "firefox-portal-detection.com",
                        "2026-07-01T15:40:13Z"
                    ],
                    "domain_list": [
                        "firefox-portal-detection.com"
                    ],
                    "domain_reputation": "Good",
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
                    "dstport": 53,
                    "end_bucket_time": 1790257260000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "181.103.4.178",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "transaction_id": 30217
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.1.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.193.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.65.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "151.101.129.91",
                                    "host_type": "A",
                                    "name": "firefox-portal-detection.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 26,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.1.91",
                                "151.101.193.91",
                                "151.101.65.91",
                                "151.101.129.91"
                            ],
                            "response_time": 26,
                            "transaction_id": 30217
                        },
                        "transaction_id": 30217
                    },
                    "msg_class": "interflow_traffic",
                    "msg_origin": {
                        "category": "traffic",
                        "processor": {
                            "type": "aella_flow"
                        },
                        "source": "modular_sensor"
                    },
                    "msgtype": 1,
                    "msgtype_name": "start",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "rvCi06ABI3UnQyDOIxG7",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790257004080,
                    "orig_timestamp_utc": "2026-09-24T13:36:44.000Z",
                    "orig_write_time": 1790257011001,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 8,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790257005899,
                    "response_time": 8,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.10.212.134.204",
                    "srcip": "10.212.134.204",
                    "srcip_assetid": "496177b0-cad9-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-jraguero.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 53031,
                    "start_bucket_time": 1790256960000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1790257386190,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 375189,
                        "status": "New"
                    },
                    "stellar_da_input": 2978,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e9bba582-c0ef-4db9-8a61-4531d838bb241790257386328-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790257260000,
                    "summary_start": 1790256960000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790257004080,
                    "timestamp_utc": "2026-09-24T13:36:44.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790257386328,
                    "xdr_event": {
                        "description": "A host \"IP: 10.212.134.204, name: nb-jraguero.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
                        "display_name": "Recently Registered Domains",
                        "framework_version": "v8",
                        "name": "new_registered_domain",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0002",
                            "name": "XDR NBA"
                        },
                        "tags": [
                            "External",
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT2008",
                            "name": "XDR New Domain"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}
```
