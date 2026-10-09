=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "cad996ea-83f5-445c-aacd-d5687ecd93511784722801522-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2245,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "actual": 484,
                    "aella_tuples": "192.168.169.18.10.11.1.1.53.32",
                    "anomaly_id": "276_iZ8BI3UnQyDOuABa",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.18",
                        "wbx2.com"
                    ],
                    "domain_list": [
                        "wdm-r.wbx2.com"
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
                    "end_bucket_time": 1784722500000,
                    "end_reason": 4,
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
                    "flow_score": 100,
                    "inbytes_delta": 554,
                    "inbytes_total": 554,
                    "inpkts_delta": 5,
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
                            "query": "wdm-r.wbx2.com",
                            "query_type": "HTTPS",
                            "transaction_id": 33321
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "prod-aore-registration1.wbx2.com",
                                    "host_type": "CNAME",
                                    "name": "wdm-r.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 22
                                },
                                {
                                    "host": "wxt-registration-ingressgateway-ds.wxtreg-prod-aore-registration1.b80.prod.infra.webex.com",
                                    "host_type": "CNAME",
                                    "name": "prod-aore-registration1.wbx2.com",
                                    "section_type": "Answer",
                                    "ttl": 22
                                },
                                {
                                    "host": "ns-738.awsdns-28.net",
                                    "host_type": "SOA",
                                    "name": "b80.prod.infra.webex.com",
                                    "section_type": "Authoritative Name Server",
                                    "ttl": 703
                                }
                            ],
                            "domain_creation": "2013-04-01T23:34:52Z",
                            "effective_tld": "wbx2.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 43,
                            "query": "wdm-r.wbx2.com",
                            "query_type": "HTTPS",
                            "reply_code": "No Error",
                            "resolved_ips": [],
                            "response_time": 51,
                            "transaction_id": 33321
                        },
                        "transaction_id": 33321
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
                    "orig_id": "276_iZ8BI3UnQyDOuABa",
                    "orig_index": "aella-adr-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 392,
                    "outbytes_total": 392,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 43,
                    "proto": 6,
                    "proto_name": "tcp",
                    "query_count": 32,
                    "receive_time": 1784722462380,
                    "response_time": 51,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.18",
                    "srcip": "192.168.169.18",
                    "srcip_assetid": "7514ba2c-cabe-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "nb-joseb.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 62177,
                    "start_bucket_time": 1784722200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784722801471,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 331156,
                        "status": "New"
                    },
                    "stellar_da_input": 1589,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "cad996ea-83f5-445c-aacd-d5687ecd93511784722801522-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 8,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784722461799,
                    "timestamp_utc": "2026-07-22T12:14:21.000Z",
                    "tos": 0,
                    "total_entropy": 92,
                    "totalbytes": 946,
                    "totalpackets": 11,
                    "tunnel_domain": "wbx2.com",
                    "tunnel_payloads": [
                        "mercury-connection-partition1-r",
                        "locus-r",
                        "wdm-r",
                        "prod-aore-registration1.wbx2.com.wxt-registration-ingressgateway-ds.wxtreg-prod-aore-registration1.b80.prod.infra.webex.com",
                        "prod-aore-mercury2.wbx2.com.wxt-mercury-ingressgateway-ds.wxtmer-prod-aore-mercury2.b81.prod.infra.webex.com.ns-1068.awsdns-05.org"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 29.91,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784722801522,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 484 Bytes) of tunneled, high-entropy traffic through DNS (domain: wbx2.com) has been observed between \"IP: 192.168.169.18, name: nb-joseb.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"prod-aore-mercury2.wbx2.com.wxt-mercury-ingressgat...ry2.b81.prod.infra.webex.com.ns-1068.awsdns-05.org.\" The typical volume of traffic transmitted through this tunnel is 29 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "e0922988-83dd-4918-9e95-311d7f357bde1784725803945-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 2293,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "action": "deny",
                    "actual": 164,
                    "aella_tuples": "192.168.15.16.192.168.169.18.7680.4",
                    "anomaly_id": "KcHriZ8BI3UnQyDO1cNP",
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
                    "domain_creation": 1784725200912,
                    "dscp_name": "Best Effort",
                    "dst_tuples": "00:00:00:00:00:00.0.192.168.169.18",
                    "dstip": "192.168.169.18",
                    "dstip_assetid": "7514ba2c-cabe-11f0-b1b7-828ad4fe26cd",
                    "dstip_geo": {
                        "city": "Asunción",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2869,
                        "longitude": -57.6511,
                        "region": "Asuncion"
                    },
                    "dstip_geo_point": "-25.2869,-57.6511",
                    "dstip_host": "192.168.169.18",
                    "dstip_reputation": "Good",
                    "dstip_type": "private",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 7680,
                    "duration": 0,
                    "end_bucket_time": 1784725500000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784725200912
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
                    "fidelity": 96.62,
                    "fortinet": {
                        "appcat": "unscanned",
                        "craction": "131072",
                        "crlevel": "high",
                        "crscore": "30",
                        "date": "2026-07-22",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "dstcountry": "Reserved",
                        "dstintf": "WiFi_Corp",
                        "dstintfrole": "lan",
                        "event_time": "2026-07-22 10:00:01",
                        "eventtime": "1784725200911836150",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:6b:8d:ec:30:fa",
                        "osname": "Windows",
                        "policytype": "policy",
                        "rule_id": 0,
                        "service": "tcp/7680",
                        "sessionid": "2427754933",
                        "srccountry": "Reserved",
                        "srcintf": "VLAN-15",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "srcswversion": "10/11",
                        "subtype": "forward",
                        "time": "10:00:01",
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
                    "orig_id": "KcHriZ8BI3UnQyDO1cNP",
                    "orig_index": "aella-adr-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_total": 0,
                    "outpkts_delta": 0,
                    "parser_raw_msg": "<189>date=2026-07-22 time=10:00:01 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784725200911836150 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=192.168.15.16 srcport=59063 srcintf=\"VLAN-15\" srcintfrole=\"lan\" dstip=192.168.169.18 dstport=7680 dstintf=\"WiFi_Corp\" dstintfrole=\"lan\" srccountry=\"Reserved\" dstcountry=\"Reserved\" sessionid=2427754933 proto=6 action=\"deny\" policyid=0 policytype=\"policy\" service=\"tcp/7680\" trandisp=\"noop\" appcat=\"unscanned\" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 crscore=30 craction=131072 crlevel=\"high\" osname=\"Windows\" srcswversion=\"10/11\" mastersrcmac=\"50:6b:8d:ec:30:fa\" srcmac=\"50:6b:8d:ec:30:fa\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784725354026,
                    "run_every": 5,
                    "severity": 60,
                    "src_tuples": "50:6b:8d:ec:30:fa.0.192.168.15.16",
                    "srcip": "192.168.15.16",
                    "srcip_assetid": "42e742ac-e26c-11f0-bee4-aa0456b9a54a",
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
                    "srcip_host": "192.168.15.16",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "50:6b:8d:ec:30:fa",
                    "srcport": 59063,
                    "start_bucket_time": 1784725200000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784725803392,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 442951,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2430,
                    "stellar_index_id": "aella-ser-2026.07.22-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "e0922988-83dd-4918-9e95-311d7f357bde1784725803945-YWVsbGEtc2VyLTIwMjYuMDcuMjItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784725200912,
                    "timestamp_utc": "2026-07-22T13:00:00.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "typical": 21,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784725803945,
                    "xdr_event": {
                        "description": "In internal traffic, a source host (IP/name: 192.168.15.16 private) has had actions blocked by a firewall too many times (#: 164), compared to the typical number of blocks (#: 21), measured in a 5.0-minute interval.",
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