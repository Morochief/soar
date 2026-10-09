=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "d4f3c4fd-fc2c-425e-ba57-203500ccf94c1783522142629-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4979,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.73.10.11.1.1.53.32",
                    "alert_time": 1783522142542,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-08 14:41:55 UTC",
                        "first_timestamp": 1783521715039,
                        "last_time_utc": "2026-07-08 14:41:55 UTC",
                        "last_timestamp": 1783521715039,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-08T14:47:00.000Z",
                        "scheduled_timestamp": 1783522020000
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
                        "quantarelay.net"
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
                    "duration": 327,
                    "end_bucket_time": 1783522020000,
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
                    "inbytes_delta": 168,
                    "inbytes_total": 168,
                    "inpkts_delta": 1,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 1,
                            "domain_creation": "2026-06-29T21:53:58Z",
                            "effective_tld": "quantarelay.net",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "quantarelay.net",
                            "query_type": "AAAA",
                            "transaction_id": 11604
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
                            "processing_time": 327,
                            "query": "quantarelay.net",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 327,
                            "transaction_id": 11604
                        },
                        "transaction_id": 11604
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
                    "orig_id": "4cIwQp8BBi0xHyA-gfhn",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1783521715039,
                    "orig_timestamp_utc": "2026-07-08T14:41:55.000Z",
                    "orig_write_time": 1783521901845,
                    "outbytes_delta": 75,
                    "outbytes_total": 75,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 327,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1783521896086,
                    "response_time": 327,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.73",
                    "srcip": "192.168.169.73",
                    "srcip_assetid": "0d406c98-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ilgonzalez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 50083,
                    "start_bucket_time": 1783521720000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1783522142542,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 240697,
                        "status": "New"
                    },
                    "stellar_da_input": 1247,
                    "stellar_index": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d4f3c4fd-fc2c-425e-ba57-203500ccf94c1783522142629-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1783522020000,
                    "summary_start": 1783521720000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783521715039,
                    "timestamp_utc": "2026-07-08T14:41:55.000Z",
                    "tos": 0,
                    "totalbytes": 243,
                    "totalpackets": 2,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783522142629,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.73, name: nb-ilgonzalez.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain quantarelay.net,  which was registered on 2026-06-29T21:53:58Z  (less than 90 days ago).",
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
                "_id": "d1e146e3-4280-4d1b-812a-6bfaac3a87771783522442537-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4987,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.73.10.11.1.1.53.32",
                    "alert_time": 1783522442455,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-08 14:47:34 UTC",
                        "first_timestamp": 1783522054640,
                        "last_time_utc": "2026-07-08 14:47:34 UTC",
                        "last_timestamp": 1783522054640,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-07-08T14:52:00.000Z",
                        "scheduled_timestamp": 1783522320000
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
                    "duration": 93992,
                    "end_bucket_time": 1783522320000,
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
                    "inbytes_delta": 0,
                    "inbytes_total": 0,
                    "inpkts_delta": 0,
                    "is_dga": "no",
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 0,
                        "request": {
                            "dga_score": 1,
                            "domain_creation": "2026-06-29T21:53:58Z",
                            "effective_tld": "quantarelay.net",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "b.quantarelay.net",
                            "query_type": "AAAA",
                            "transaction_id": 42630
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ns-cloud-a1.googledomains.com",
                                    "host_type": "SOA",
                                    "name": "quantarelay.net",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 229
                                }
                            ],
                            "domain_creation": "2026-06-29T21:53:58Z",
                            "effective_tld": "quantarelay.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 22,
                            "query": "b.quantarelay.net",
                            "query_type": "AAAA",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 22,
                            "transaction_id": 42630
                        },
                        "transaction_id": 42630
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
                    "msgtype_name": "replica",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "b8M0Qp8BBi0xHyA-cmf1",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1783522054640,
                    "orig_timestamp_utc": "2026-07-08T14:47:34.000Z",
                    "orig_write_time": 1783522160752,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 11,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1783522152296,
                    "response_time": 11,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.73",
                    "srcip": "192.168.169.73",
                    "srcip_assetid": "0d406c98-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ilgonzalez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 60232,
                    "start_bucket_time": 1783522020000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1783522442455,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 281703,
                        "status": "New"
                    },
                    "stellar_da_input": 1815,
                    "stellar_index": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "d1e146e3-4280-4d1b-812a-6bfaac3a87771783522442537-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1783522320000,
                    "summary_start": 1783522020000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783522054640,
                    "timestamp_utc": "2026-07-08T14:47:34.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1783522442536,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.73, name: nb-ilgonzalez.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain quantarelay.net,  which was registered on 2026-06-29T21:53:58Z  (less than 90 days ago).",
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
                "_id": "02add51f-2f10-4205-ab70-cb49c83388191783522442878-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4988,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "unencrypted_phishing_site",
                    "action": "passthrough",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.73.35.241.1.16.80.4",
                    "alert_time": 1783522442833,
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-08 14:47:34 UTC",
                        "first_timestamp": 1783522054751,
                        "last_time_utc": "2026-07-08 14:47:34 UTC",
                        "last_timestamp": 1783522054751,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "dynamic_phishing_unencrypted",
                        "scheduled_time_utc": "2026-07-08T14:52:00.000Z",
                        "scheduled_timestamp": 1783522320000
                    },
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "direction": "outgoing",
                    "domain_creation": 1783522054751,
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
                    "dstport": 80,
                    "end_bucket_time": 1783522320000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1783522054751,
                        "utm": {
                            "feature": "Web Filtering"
                        }
                    },
                    "event_category": "killchain",
                    "event_name": "unencrypted_phishing_site",
                    "event_score": 35,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_type": "reconn",
                    "fidelity": 50,
                    "fortinet": {
                        "agent": "curl/8.5.0",
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
                        "event_time": "2026-07-08 11:47:35",
                        "eventtime": "1783522054751040506",
                        "eventtype": "ftgd_allow",
                        "group": "FSSO-TECNOLOGIA",
                        "hostname": "b.quantarelay.net",
                        "httpmethod": "GET",
                        "level": "notice",
                        "logid": "0317013312",
                        "msg": "URL belongs to an allowed category in policy",
                        "policytype": "policy",
                        "poluuid": "460219e8-ca3f-51f0-e8ee-8c9a765155ab",
                        "profile": "WF-Technoma",
                        "ratemethod": "domain",
                        "reqtype": "direct",
                        "rule_id": 91,
                        "service": "HTTP",
                        "sessionid": "1078181127",
                        "srccountry": "Reserved",
                        "srcintf": "WiFi_Corp",
                        "srcintfrole": "lan",
                        "srcuuid": "5979d106-ca16-51f0-0dc9-c378a1008977",
                        "subtype": "webfilter",
                        "time": "11:47:35",
                        "type": "utm",
                        "tz": "-0300",
                        "vd": "root"
                    },
                    "fw_policy_id": "FG-Technoma_91",
                    "inbytes_total": 0,
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
                    "orig_id": "rcM1Qp8BBi0xHyA-rYvJ",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.07-000050",
                    "orig_timestamp": 1783522054751,
                    "orig_timestamp_utc": "2026-07-08T14:47:34.000Z",
                    "orig_write_time": 1783522241115,
                    "outbytes_total": 80,
                    "parser_raw_msg": "<189>date=2026-07-08 time=11:47:35 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1783522054751040506 tz=\"-0300\" logid=\"0317013312\" type=\"utm\" subtype=\"webfilter\" eventtype=\"ftgd_allow\" level=\"notice\" vd=\"root\" policyid=91 poluuid=\"460219e8-ca3f-51f0-e8ee-8c9a765155ab\" policytype=\"policy\" sessionid=1078181127 user=\"ILSONGONZALEZ\" group=\"FSSO-TECNOLOGIA\" authserver=\"AD1\" srcip=192.168.169.73 srcport=58056 srccountry=\"Reserved\" srcintf=\"WiFi_Corp\" srcintfrole=\"lan\" srcuuid=\"5979d106-ca16-51f0-0dc9-c378a1008977\" dstip=35.241.1.16 dstport=80 dstcountry=\"United States\" dstintf=\"port1\" dstintfrole=\"wan\" dstuuid=\"5979d106-ca16-51f0-0dc9-c378a1008977\" proto=6 httpmethod=\"GET\" service=\"HTTP\" hostname=\"b.quantarelay.net\" agent=\"curl/8.5.0\" profile=\"WF-Technoma\" action=\"passthrough\" reqtype=\"direct\" url=\"http://b.quantarelay.net/\" sentbyte=80 rcvdbyte=0 direction=\"outgoing\" msg=\"URL belongs to an allowed category in policy\" ratemethod=\"domain\" cat=55 catdesc=\"Meaningless Content\"",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1783522237989,
                    "severity": 30,
                    "src_tuples": "00:00:00:00:00:00.0.192.168.169.73",
                    "srcip": "192.168.169.73",
                    "srcip_assetid": "0d406c98-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-ilgonzalez.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_username": "ILSONGONZALEZ",
                    "srcip_usersid": "ILSONGONZALEZ",
                    "srcip_version": "ipv4",
                    "srcmac": "00:00:00:00:00:00",
                    "srcport": 58056,
                    "start_bucket_time": 1783522020000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1783522442833,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 201718,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 3104,
                    "stellar_index": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "02add51f-2f10-4205-ab70-cb49c83388191783522442878-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1783522320000,
                    "summary_start": 1783522020000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783522054751,
                    "timestamp_utc": "2026-07-08T14:47:34.000Z",
                    "totalbytes": 80,
                    "totalpackets": 0,
                    "url": "http://b.quantarelay.net/",
                    "url_list": [
                        "http://b.quantarelay.net/"
                    ],
                    "url_reputation": "Good",
                    "url_reputation_source": "",
                    "user": {
                        "name": "ILSONGONZALEZ"
                    },
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1783522442878,
                    "xdr_event": {
                        "description": "A suspicious visit was observed in unencrypted traffic  from \"IP: 192.168.169.73, name: nb-ilgonzalez.technoma.local\" to \"IP: 35.241.1.16, name: b.quantarelay.net\"  which has a recently registered domain (b.quantarelay.net).  This indicates a possible phishing site.",
                        "display_name": "Possible Unencrypted Phishing Site Visit",
                        "framework_version": "v8",
                        "name": "unencrypted_phishing_site",
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