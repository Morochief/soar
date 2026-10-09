=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "0832ae01-cdd9-4d93-bd27-ed0b9ef0c3871784295001873-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14390,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 580,
                    "aella_tuples": "192.168.169.142.10.11.1.1.53.32",
                    "anomaly_id": "zKw-cJ8BI3UnQyDOo6MW",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.142",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "proximity-a.wbx2.com"
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
                    "duration": 23578,
                    "end_bucket_time": 1784294700000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 56,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 17.96,
                    "flow_score": 98,
                    "inbytes_delta": 605,
                    "inbytes_total": 748,
                    "inpkts_delta": 2,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "proximity-a.wbx2.com",
                            "query_type": "A",
                            "transaction_id": 42402
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-achm-general2.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "proximity-a.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 52
                                },
                                {
                                    "host": "wxt-general-ingressgateway-ds.wxtgen-prod-achm-general2.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-achm-general2.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 0
                                },
                                {
                                    "host_addr": "170.72.245.148",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway-ds.wxtgen-prod-achm-general2.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 1
                                },
                                {
                                    "host_addr": "170.72.245.78",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway-ds.wxtgen-prod-achm-general2.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 1
                                },
                                {
                                    "host_addr": "170.72.245.164",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway-ds.wxtgen-prod-achm-general2.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 1
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 4107,
                            "query": "proximity-a.wbx2.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "170.72.245.148",
                                "170.72.245.78",
                                "170.72.245.164"
                            ],
                            "response_time": 4107,
                            "transaction_id": 42402
                        },
                        "transaction_id": 42402
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
                    "orig_id": "zKw-cJ8BI3UnQyDOo6MW",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 240,
                    "outbytes_total": 405,
                    "outpkts_delta": 3,
                    "port_name": "ethernet1",
                    "processing_time": 4107,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 40,
                    "receive_time": 1784294575487,
                    "response_time": 4107,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "710eb350-073c-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-grodas.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 63760,
                    "start_bucket_time": 1784294400000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784295001865,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421492,
                        "status": "New"
                    },
                    "stellar_da_input": 2212,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "0832ae01-cdd9-4d93-bd27-ed0b9ef0c3871784295001873-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784294574372,
                    "timestamp_utc": "2026-07-17T13:22:54.000Z",
                    "tos": 0,
                    "total_entropy": 116,
                    "totalbytes": 1153,
                    "totalpackets": 5,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "prod-achm-registration2.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration2.prod.infra.webex.com.ns-888.awsdns-47.net",
                        "u2c",
                        "u2c-a.wbx2.com.prod-achm-registration2.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration2.prod.infra.webex.com",
                        "web-authentication-a",
                        "prod-achm-general2.wbx2.com.wxt-general-ingressgateway-ds.wxtgen-prod-achm-general2.prod.infra.webex.com"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 30.8,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784295001873,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 580 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.142, name: nb-grodas.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-achm-registration2.wbx2.com.wxt-registration-...tration2.prod.infra.webex.com.ns-888.awsdns-47.net.\" The typical volume of traffic transmitted through this tunnel is 30 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "08d50116-ea74-4535-aa7b-1f875116dca51784296801793-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 14428,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 393,
                    "aella_tuples": "192.168.169.142.10.11.1.1.53.32",
                    "anomaly_id": "JK9bcJ8BI3UnQyDOBNuY",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.142",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "calendar-a.wbx2.com"
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
                    "duration": 3754,
                    "end_bucket_time": 1784296500000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 46,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 10,
                    "flow_score": 98,
                    "inbytes_delta": 469,
                    "inbytes_total": 708,
                    "inpkts_delta": 2,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "calendar-a.wbx2.com",
                            "query_type": "A",
                            "transaction_id": 8197
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-achm-general1.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "calendar-a.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 49
                                },
                                {
                                    "host": "wxt-general-ingressgateway.wxtgen-prod-achm-general1.d70.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-achm-general1.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "170.72.245.187",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway.wxtgen-prod-achm-general1.d70.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "170.72.245.245",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway.wxtgen-prod-achm-general1.d70.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "170.72.245.31",
                                    "host_type": "A",
                                    "name": "wxt-general-ingressgateway.wxtgen-prod-achm-general1.d70.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 29,
                            "query": "calendar-a.wbx2.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "170.72.245.187",
                                "170.72.245.245",
                                "170.72.245.31"
                            ],
                            "response_time": 29,
                            "transaction_id": 8197
                        },
                        "transaction_id": 8197
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
                    "orig_id": "JK9bcJ8BI3UnQyDOBNuY",
                    "orig_index": "aella-adr-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 79,
                    "outbytes_total": 272,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 29,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 30,
                    "receive_time": 1784296434741,
                    "response_time": 29,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.142",
                    "srcip": "192.168.169.142",
                    "srcip_assetid": "710eb350-073c-11f1-b2c6-62a12c107cbc",
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
                    "srcip_host": "nb-aholmer.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 53890,
                    "start_bucket_time": 1784296200000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1784296801784,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 361457,
                        "status": "New"
                    },
                    "stellar_da_input": 1941,
                    "stellar_index_id": "aella-ser-2026.07.17-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "08d50116-ea74-4535-aa7b-1f875116dca51784296801793-YWVsbGEtc2VyLTIwMjYuMDcuMTctZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784296433621,
                    "timestamp_utc": "2026-07-17T13:53:53.000Z",
                    "tos": 0,
                    "total_entropy": 86,
                    "totalbytes": 980,
                    "totalpackets": 3,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "prod-achm-mercury1.wbx2.com.wxt-mercury-ingressgateway.acmhwxt-prd-2.prod.infra.webex.com.ns-1633.awsdns-12.co.uk",
                        "llm1-connection-a",
                        "prod-achm-mercury1.wbx2.com.wxt-mercury-ingressgateway.acmhwxt-prd-2.prod.infra.webex.com",
                        "mercury-connection-partition2-a",
                        "conv-a"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 25.91,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784296801793,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 393 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.142, name: nb-aholmer.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-achm-mercury1.wbx2.com.wxt-mercury-ingressgat...prd-2.prod.infra.webex.com.ns-1633.awsdns-12.co.uk.\" The typical volume of traffic transmitted through this tunnel is 25 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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