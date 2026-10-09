# Lote de Alertas Originales - Stellar Cyber Interflow

- **Caso:** 19306_DNS_Tunnel_Webex_and_Firefox_Portal_nb-jdurand
- **Cantidad de Eventos:** 2
- **Reglas Involucradas:** `dns_tunnel` (1 evento), `new_registered_domain` (1 evento)
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Host Afectado:** `nb-jdurand.technoma.local` (`192.168.169.144`)

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "ad548a21-9a10-4509-9295-5b7ed91f9d0a1790259002963-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19306,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 415,
                    "aella_tuples": "192.168.169.144.10.11.1.1.53.32",
                    "anomaly_id": "ofO606ABI3UnQyDOFrKO",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.144",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "client-logs-a.wbx2.com"
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
                    "duration": 56,
                    "end_bucket_time": 1790258700000,
                    "end_reason": 4,
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
                    "flow_score": 100,
                    "inbytes_delta": 246,
                    "inbytes_total": 246,
                    "inpkts_delta": 4,
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
                            "query": "client-logs-a.wbx2.com",
                            "query_type": "HTTPS",
                            "transaction_id": 32745
                        },
                        "transaction_id": 32745
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
                    "orig_id": "ofO606ABI3UnQyDOFrKO",
                    "orig_index": "aella-adr-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 400,
                    "outbytes_total": 400,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 0,
                    "proto": 6,
                    "proto_name": "tcp",
                    "query_count": 29,
                    "receive_time": 1790258574459,
                    "response_time": 0,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.144",
                    "srcip": "192.168.169.144",
                    "srcip_assetid": "b0fe715a-2224-11f1-818c-26eb39a0cd74",
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
                    "srcip_host": "nb-jdurand.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 49670,
                    "start_bucket_time": 1790258400000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1790259002437,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 421430,
                        "status": "New"
                    },
                    "stellar_da_input": 915,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "ad548a21-9a10-4509-9295-5b7ed91f9d0a1790259002963-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 5,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790258573601,
                    "timestamp_utc": "2026-09-24T14:02:53.000Z",
                    "tos": 0,
                    "total_entropy": 84,
                    "totalbytes": 646,
                    "totalpackets": 10,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "prod-achm-registration2.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-achm-registration2.d71.prod.infra.webex.com.ns-1371.awsdns-43.org",
                        "mercury-connection-partition0-a",
                        "locus-a",
                        "meeting-container-a",
                        "directory-search-a"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 27.43,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790259002963,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 415 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.144, name: nb-jdurand.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-achm-registration2.wbx2.com.wxt-registration-...on2.d71.prod.infra.webex.com.ns-1371.awsdns-43.org.\" The typical volume of traffic transmitted through this tunnel is 27 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "59342690-15fa-476f-9aa3-c17f37d15b0d1790263987728-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19631,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "new_registered_domain",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "192.168.169.144.10.11.1.1.53.32",
                    "alert_time": 1790263987185,
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-09-24 15:27:57 UTC",
                        "first_timestamp": 1790263677499,
                        "last_time_utc": "2026-09-24 15:27:57 UTC",
                        "last_timestamp": 1790263677499,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "new_registered_domain",
                        "scheduled_time_utc": "2026-09-24T15:31:00.000Z",
                        "scheduled_timestamp": 1790263860000
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
                    "end_bucket_time": 1790263860000,
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
                            "transaction_id": 19887
                        },
                        "response": {
                            "answers": [
                                {
                                    "host_addr": "151.101.129.91",
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
                                    "host_addr": "151.101.193.91",
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
                                }
                            ],
                            "domain_creation": "2026-07-01T15:40:13Z",
                            "effective_tld": "firefox-portal-detection.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 3,
                            "query": "firefox-portal-detection.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "151.101.129.91",
                                "151.101.65.91",
                                "151.101.193.91",
                                "151.101.1.91"
                            ],
                            "response_time": 3,
                            "transaction_id": 19887
                        },
                        "transaction_id": 19887
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
                    "msgtype_name": "replica",
                    "netid": 1101,
                    "netid_name": "vlan1101",
                    "obsid": 3232239430,
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "org_name": "Technoma",
                    "orig_id": "ZwAH1KABI3UnQyDO6ynC",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.18-000057",
                    "orig_timestamp": 1790263677499,
                    "orig_timestamp_utc": "2026-09-24T15:27:57.000Z",
                    "orig_write_time": 1790263681485,
                    "outbytes_delta": 0,
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "port_name": "ethernet1",
                    "processing_time": 9,
                    "proto": 17,
                    "proto_name": "udp",
                    "receive_time": 1790263678510,
                    "response_time": 9,
                    "severity": 50,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.144",
                    "srcip": "192.168.169.144",
                    "srcip_assetid": "b0fe715a-2224-11f1-818c-26eb39a0cd74",
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
                    "srcip_host": "nb-jdurand.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 65403,
                    "start_bucket_time": 1790263560000,
                    "state": "Established",
                    "stellar": {
                        "alert_time": 1790263987185,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 305700,
                        "status": "New"
                    },
                    "stellar_da_input": 2823,
                    "stellar_index": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "59342690-15fa-476f-9aa3-c17f37d15b0d1790263987728-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1790263860000,
                    "summary_start": 1790263560000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790263677499,
                    "timestamp_utc": "2026-09-24T15:27:57.000Z",
                    "tos": 0,
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1790263987727,
                    "xdr_event": {
                        "description": "A host \"IP: 192.168.169.144, name: nb-jdurand.technoma.local\" queried \"IP: 10.11.1.1, name: ad.technoma.local\"  for the domain firefox-portal-detection.com,  which was registered on 2026-07-01T15:40:13Z  (less than 90 days ago).",
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
