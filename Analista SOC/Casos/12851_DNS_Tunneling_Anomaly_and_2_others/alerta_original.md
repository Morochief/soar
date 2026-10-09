=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "697969f5-1aa0-4c6f-8f97-90b39d2ec75e1785500101696-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13425,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 472,
                    "aella_tuples": "192.168.169.40.10.11.1.1.53.32",
                    "anomaly_id": "rNcUuJ8BI3UnQyDOOfZe",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.40",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "locus-r.wbx2.com"
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
                    "duration": 26,
                    "end_bucket_time": 1785499800000,
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
                    "inbytes_delta": 237,
                    "inbytes_total": 237,
                    "inpkts_delta": 1,
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
                            "query": "locus-r.wbx2.com",
                            "query_type": "A",
                            "transaction_id": 51632
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-aore-meet2.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "locus-r.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 33
                                },
                                {
                                    "host": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet2.b81.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-aore-meet2.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 33
                                },
                                {
                                    "host_addr": "170.72.250.188",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet2.b81.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 33
                                },
                                {
                                    "host_addr": "170.72.250.223",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet2.b81.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 33
                                },
                                {
                                    "host_addr": "170.72.250.82",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet2.b81.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 33
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 26,
                            "query": "locus-r.wbx2.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "170.72.250.188",
                                "170.72.250.223",
                                "170.72.250.82"
                            ],
                            "response_time": 26,
                            "transaction_id": 51632
                        },
                        "transaction_id": 51632
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
                    "orig_id": "rNcUuJ8BI3UnQyDOOfZe",
                    "orig_index": "aella-adr-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 76,
                    "outbytes_total": 76,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 26,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 32,
                    "receive_time": 1785499753286,
                    "response_time": 26,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.40",
                    "srcip": "192.168.169.40",
                    "srcip_assetid": "a2ae5c3a-caf6-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-fmora.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 59708,
                    "start_bucket_time": 1785499500000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785500101612,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 341324,
                        "status": "New"
                    },
                    "stellar_da_input": 1904,
                    "stellar_index_id": "aella-ser-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "697969f5-1aa0-4c6f-8f97-90b39d2ec75e1785500101696-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785499571649,
                    "timestamp_utc": "2026-07-31T12:06:11.000Z",
                    "tos": 0,
                    "total_entropy": 90,
                    "totalbytes": 313,
                    "totalpackets": 2,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "u2c",
                        "u2c-a.wbx2.com.prod-achm-registration1.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration1.d70.prod.infra.webex.com",
                        "u2c-a",
                        "prod-achm-registration1.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration1.d70.prod.infra.webex.com.ns-1155.awsdns-16.org",
                        "wdm-r"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 30.14,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785500101696,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 472 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.40, name: nb-fmora.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-achm-registration1.wbx2.com.wxt-registration-...on1.d70.prod.infra.webex.com.ns-1155.awsdns-16.org.\" The typical volume of traffic transmitted through this tunnel is 30 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "49495fc9-82f1-4690-9ebe-c236ce57bf211785500701659-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13436,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 606,
                    "aella_tuples": "192.168.169.40.10.11.1.1.53.32",
                    "anomaly_id": "0NgfuJ8BI3UnQyDO19ov",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.40",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "locus-r.wbx2.com"
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
                    "duration": 64,
                    "end_bucket_time": 1785500400000,
                    "end_reason": 1,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event_category": "killchain",
                    "event_name": "dns_tunnel",
                    "event_score": 59,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "action",
                    "fidelity": 21.52,
                    "flow_score": 98,
                    "inbytes_delta": 237,
                    "inbytes_total": 237,
                    "inpkts_delta": 1,
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
                            "query": "locus-r.wbx2.com",
                            "query_type": "A",
                            "transaction_id": 11585
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-aore-meet1.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "locus-r.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 36
                                },
                                {
                                    "host": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet1.b80.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-aore-meet1.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 36
                                },
                                {
                                    "host_addr": "170.72.250.201",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet1.b80.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "170.72.250.15",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet1.b80.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                },
                                {
                                    "host_addr": "170.72.250.231",
                                    "host_type": "A",
                                    "name": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet1.b80.prod.infra.webex.com",
                                    "section_type": "Answer",
                                    "ttl": 60
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 64,
                            "query": "locus-r.wbx2.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "170.72.250.201",
                                "170.72.250.15",
                                "170.72.250.231"
                            ],
                            "response_time": 64,
                            "transaction_id": 11585
                        },
                        "transaction_id": 11585
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
                    "orig_id": "0NgfuJ8BI3UnQyDO19ov",
                    "orig_index": "aella-adr-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 76,
                    "outbytes_total": 76,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 64,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 41,
                    "receive_time": 1785500517640,
                    "response_time": 64,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.40",
                    "srcip": "192.168.169.40",
                    "srcip_assetid": "a2ae5c3a-caf6-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-fmora.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 60729,
                    "start_bucket_time": 1785500100000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785500701614,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 180635,
                        "status": "New"
                    },
                    "stellar_da_input": 1904,
                    "stellar_index_id": "aella-ser-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "49495fc9-82f1-4690-9ebe-c236ce57bf211785500701659-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785500336063,
                    "timestamp_utc": "2026-07-31T12:18:56.000Z",
                    "tos": 0,
                    "total_entropy": 117,
                    "totalbytes": 313,
                    "totalpackets": 2,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "u2c",
                        "u2c-a.wbx2.com.prod-achm-registration1.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration1.d70.prod.infra.webex.com.ns-1155.awsdns-16.org",
                        "u2c-a",
                        "prod-achm-registration1.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration1.d70.prod.infra.webex.com.ns-1155.awsdns-16.org",
                        "u2c-r"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 33.99,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785500701659,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 606 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.40, name: nb-fmora.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"u2c-a.wbx2.com.prod-achm-registration1.wbx2.com.wx...on1.d70.prod.infra.webex.com.ns-1155.awsdns-16.org.\" The typical volume of traffic transmitted through this tunnel is 33 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "cb68bfe8-51fb-49eb-b9ca-dcbd2ce6be3e1785501001614-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 13438,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 484,
                    "aella_tuples": "192.168.169.40.10.11.1.1.53.32",
                    "anomaly_id": "N9gguJ8BI3UnQyDO5vCp",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.40",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "locus-r.wbx2.com"
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
                    "duration": 56,
                    "end_bucket_time": 1785500700000,
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
                    "inbytes_delta": 189,
                    "inbytes_total": 189,
                    "inpkts_delta": 1,
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
                            "query": "locus-r.wbx2.com",
                            "query_type": "HTTPS",
                            "transaction_id": 10690
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-aore-meet2.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "locus-r.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 17
                                },
                                {
                                    "host": "wxt-meet-ingressgateway-ds.wxtm-prod-aore-meet2.b81.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-aore-meet2.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 37
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 56,
                            "query": "locus-r.wbx2.com",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 56,
                            "transaction_id": 10690
                        },
                        "transaction_id": 10690
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
                    "orig_id": "N9gguJ8BI3UnQyDO5vCp",
                    "orig_index": "aella-adr-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 76,
                    "outbytes_total": 76,
                    "outpkts_delta": 1,
                    "port_name": "ethernet1",
                    "processing_time": 56,
                    "proto": 17,
                    "proto_name": "udp",
                    "query_count": 33,
                    "receive_time": 1785500586417,
                    "response_time": 56,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.40",
                    "srcip": "192.168.169.40",
                    "srcip_assetid": "a2ae5c3a-caf6-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-fmora.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 51864,
                    "start_bucket_time": 1785500400000,
                    "state": "Expired",
                    "stellar": {
                        "alert_time": 1785501001594,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 411017,
                        "status": "New"
                    },
                    "stellar_da_input": 1403,
                    "stellar_index_id": "aella-ser-2026.07.31-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "cb68bfe8-51fb-49eb-b9ca-dcbd2ce6be3e1785501001614-YWVsbGEtc2VyLTIwMjYuMDcuMzEtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1785500405063,
                    "timestamp_utc": "2026-07-31T12:20:05.000Z",
                    "tos": 0,
                    "total_entropy": 94,
                    "totalbytes": 265,
                    "totalpackets": 2,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "wdm-r",
                        "prod-aore-registration2.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-aore-registration2.b81.prod.infra.webex.com.ns-1068.awsdns-05.org",
                        "mercury-connection-partition1-r",
                        "prod-aore-mercury1.wbx2.com.wxt-mercury-ingressgateway.wxtmer-prod-aore-mercury1.b80.prod.infra.webex.com.ns-738.awsdns-28.net",
                        "conv-r"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 32.83,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1785501001614,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 484 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.40, name: nb-fmora.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-aore-registration2.wbx2.com.wxt-registration-...on2.b81.prod.infra.webex.com.ns-1068.awsdns-05.org.\" The typical volume of traffic transmitted through this tunnel is 32 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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