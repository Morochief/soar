=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "bc306719-632d-4433-8074-c1699433c3051783519742305-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4940,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.45.10.11.1.1.53.32",
                    "alert_time": 1783519742265,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-08 14:06:14 UTC",
                        "first_timestamp": 1783519574776,
                        "last_time_utc": "2026-07-08 14:06:14 UTC",
                        "last_timestamp": 1783519574776,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-08T14:07:00.000Z",
                        "scheduled_timestamp": 1783519620000
                    },
                    "detected_fields": [
                        "metadata.request.effective_tld",
                        "metadata.response.domain_creation"
                    ],
                    "detected_values": [
                        "quantarelay.net",
                        "2026-06-29T21:53:58Z"
                    ],
                    "domain_list": [
                        "b.quantarelay.net"
                    ],
                    "domain_reputation": "Good",
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:50:56:af:ff:5a.1101.10.11.1.1",
                    "dstip": "10.11.1.1",
                    "dstip_assetid": "31ce6d84-caab-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
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
                    "duration": 27447,
                    "end_bucket_time": 1783519620000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "network",
                    "event_name": "new_registered_domain",
                    "event_score": 62,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "conn",
                    "fidelity": 100,
                    "flow_score": 98,
                    "inbytes_delta": 336,
                    "inbytes_total": 336,
                    "inpkts_delta": 2,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": -1,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 1,
                            "domain_creation": "2026-06-29T21:53:58Z",
                            "effective_tld": "quantarelay.net",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "b.quantarelay.net",
                            "query_type": "AAAA",
                            "transaction_id": 21085
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns-cloud-a1.googledomains.com",
                                    "host_type": "SOA",
                                    "name": "quantarelay.net",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 300
                                }
                            ],
                            "domain_creation": "2026-06-29T21:53:58Z",
                            "effective_tld": "quantarelay.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 85,
                            "query": "b.quantarelay.net",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 85,
                            "transaction_id": 21085
                        },
                        "transaction_id": 21085
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
                    "orig_id": "QL8NQp8BBi0xHyA-jA95",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1783519574776,
                    "orig_timestamp_utc": "2026-07-08T14:06:14.000Z",
                    "orig_write_time": 1783519610939,
                    "outbytes_delta": 149,
                    "outbytes_total": 149,
                    "outpkts_delta": 2,
                    "port_name": "ethernet1",
                    "processing_time": 54,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1783519606749,
                    "response_time": 54,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.45",
                    "srcip": "192.168.169.45",
                    "srcip_assetid": "29a0d6dc-cac5-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-fcaceres.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 60437,
                    "start_bucket_time": 1783519320000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1783519742265,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 131326,
                        "status": "New"
                    },
                    "stellar_da_input": 2091,
                    "stellar_index": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bc306719-632d-4433-8074-c1699433c3051783519742305-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1783519620000,
                    "summary_start": 1783519320000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783519574776,
                    "timestamp_utc": "2026-07-08T14:06:14.000Z",
                    "tos": 0,
                    "totalbytes": 485,
                    "totalpackets": 4,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783519742305,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.45, name: nb-fcaceres.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain quantarelay.net,  which was registered on 2026-06-29T21:53:58Z  (less than 90 days ago).",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "4354d668-90cd-4c37-8f53-bd308cceb9691783520043621-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4943,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "encrypted_phishing_site",
                    "action": "passthrough",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.45.35.241.1.16.443.4",
                    "alert_time": 1783520043583,
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTPS",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-08 14:04:30 UTC",
                        "first_timestamp": 1783519470127,
                        "last_time_utc": "2026-07-08 14:04:30 UTC",
                        "last_timestamp": 1783519470127,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "dynamic_phishing_encrypted",
                        "scheduled_time_utc": "2026-07-08T14:12:00.000Z",
                        "scheduled_timestamp": 1783519920000
                    },
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "direction": "outgoing",
                    "domain_creation": 1783519470127,
                    "dscp_name": "Best Effort",
                    "dstip": "35.241.1.16",
                    "dstip_asn": 396982,
                    "dstip_asn_org": "Google LLC",
                    "dstip_domain_creation": "2026-06-29T21:53:58Z",
                    "dstip_geo": {
                        "city": "Kansas City",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 39.1027,
                        "longitude": -94.5778,
                        "region": "Missouri"
                    },
                    "dstip_geo_point": "39.1027,-94.5778",
                    "dstip_host": "b.quantarelay.net",
                    "dstip_reputation": "Good",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 443,
                    "end_bucket_time": 1783519920000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783519470127,
                        "utm": {
                            "feature": "Web Filtering"
                        }
                    },
                    "event_category": "killchain",
                    "event_name": "encrypted_phishing_site",
                    "event_score": 26,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 20,
                    "fortinet": {
                        "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/201001",
                        "authserver": "AD1",
                        "cat": "55",
                        "catdesc": "Meaningless Content",
                        "date": "2026-07-08",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "United States",
                        "dstintf": "port1",
                        "dstintfrole": "wan",
                        "dstuuid": "5979d106-ca16-51f0-0dc9-c378a1008977",
                        "event_time": "2026-07-08 11:04:31",
                        "eventtime": "1783519470127056802",
                        "eventtype": "ftgd_allow",
                        "group": "TECHNOMA/USUARIOS",
                        "hostname": "b.quantarelay.net",
                        "httpmethod": "POST",
                        "level": "notice",
                        "logid": "0317013312",
                        "msg": "URL belongs to an allowed category in policy",
                        "policytype": "policy",
                        "poluuid": "460219e8-ca3f-51f0-e8ee-8c9a765155ab",
                        "profile": "WF-Technoma",
                        "ratemethod": "domain",
                        "referralurl": "https://www.anker.com/",
                        "reqtype": "referral",
                        "rule_id": 91,
                        "service": "HTTPS",
                        "sessionid": "1074493057",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcuuid": "5979d106-ca16-51f0-0dc9-c378a1008977",
                        "subtype": "webfilter",
                        "time": "11:04:31",
                        "type": "utm",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_91",
                    "inbytes_total": 5152,
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
                    "orig_id": "JL8OQp8BBi0xHyA-xjFW",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1783519470127,
                    "orig_timestamp_utc": "2026-07-08T14:04:30.000Z",
                    "orig_write_time": 1783519690895,
                    "outbytes_total": 6065,
                    "parser_raw_msg": "<189>date=2026-07-08 time=11:04:31 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783519470127056802 tz=\"-0300\" logid=\"0317013312\" type=\"utm\" subtype=\"webfilter\" eventtype=\"ftgd_allow\" level=\"notice\" vd=\"root\" policyid=91 poluuid=\"460219e8-ca3f-51f0-e8ee-8c9a765155ab\" policytype=\"policy\" sessionid=1074493057 user=\"FCACERES\" group=\"TECHNOMA/USUARIOS\" authserver=\"AD1\" srcip=192.168.169.45 srcport=56990 srccountry=\"Reserved\" srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" srcuuid=\"5979d106-ca16-51f0-0dc9-c378a1008977\" dstip=35.241.1.16 dstport=443 dstcountry=\"United States\" dstintf=\"port1\" dstintfrole=\"wan\" dstuuid=\"5979d106-ca16-51f0-0dc9-c378a1008977\" proto=6 httpmethod=\"POST\" service=\"HTTPS\" hostname=\"b.quantarelay.net\" agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/201001\" profile=\"WF-Technoma\" action=\"passthrough\" reqtype=\"referral\" url=\"https://b.quantarelay.net/v1/pixel\" referralurl=\"https://www.anker.com/\" sentbyte=6065 rcvdbyte=5152 direction=\"outgoing\" msg=\"URL belongs to an allowed category in policy\" ratemethod=\"domain\" cat=55 catdesc=\"Meaningless Content\"",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783519683685,
                    "severity": 30,
                    "src_tuples": "00:00:00:00:00:00.0.192.168.169.45",
                    "srcip": "192.168.169.45",
                    "srcip_assetid": "750f611c-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-fcaceres.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "FCACERES",
                    "srcip_usersid": "FCACERES",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 56990,
                    "start_bucket_time": 1783519620000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783520043583,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 352688,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3313,
                    "stellar_index": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "4354d668-90cd-4c37-8f53-bd308cceb9691783520043621-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1783519920000,
                    "summary_start": 1783519620000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783519470127,
                    "timestamp_utc": "2026-07-08T14:04:30.000Z",
                    "totalbytes": 11217,
                    "totalpackets": 0,
                    "url": "https://b.quantarelay.net/v1/pixel",
                    "url_list": [
                        "https://b.quantarelay.net/v1/pixel"
                    ],
                    "url_reputation": "Good",
                    "url_reputation_source": "",
                    "user": {
                        "name": "FCACERES"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783520043621,
                    "xdr_event": {
                        "description": "A suspicious visit was observed in encrypted traffic  from \"IP: 192.168.169.45, name: nb-fcaceres.technoma.local\" to \"IP: 35.241.1.16, name: b.quantarelay.net\"  which has a recently registered domain (b.quantarelay.net).  This indicates a possible phishing site.",
                        "display_name": "Possible Encrypted Phishing Site Visit",
                        "framework_version": "v8",
                        "name": "encrypted_phishing_site",
                        "scope": "",
                        "tactic": {
                            "id": "TA0001",
                            "name": "Initial Access"
                        },
                        "tags": [
                            "Network Traffic Analysis",
                            "Phishing"
                        ],
                        "technique": {
                            "id": "T1566",
                            "name": "Phishing"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}