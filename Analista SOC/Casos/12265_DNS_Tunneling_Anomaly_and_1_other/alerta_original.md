=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "325f6ebf-e4ef-40d5-98b6-403f9ec40bb11784213701869-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12072,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 366,
                    "aella_tuples": "192.168.169.99.10.11.1.1.53.32",
                    "anomaly_id": "TGFna58BI3UnQyDOLYEL",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.99",
                        "powerplatform.com"
                    ],
                    "domain_list": [
                        "5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com"
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
                    "duration": 80,
                    "end_bucket_time": 1784213400000,
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
                    "inbytes_delta": 639,
                    "inbytes_total": 639,
                    "inpkts_delta": 5,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 1,
                            "domain_creation": "2002-09-30T20:21:54Z",
                            "effective_tld": "powerplatform.com",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com",
                            "query_type": "A",
                            "transaction_id": 33329
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "ppapigw.br-cm001.gateway.prod.cm.powerapps.com",
                                    "host_type": "CNAME",
                                    "name": "5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com",
                                    "section_type": "Answer",
                                    "ttl": 233
                                },
                                {
                                    "host": "apigw-prdcm001-br.trafficmanager.net",
                                    "host_type": "CNAME",
                                    "name": "ppapigw.br-cm001.gateway.prod.cm.powerapps.com",
                                    "section_type": "Answer",
                                    "ttl": 2267
                                },
                                {
                                    "host": "ppapigw.sbr-cm001.gateway.prod.cm.powerapps.com",
                                    "host_type": "CNAME",
                                    "name": "apigw-prdcm001-br.trafficmanager.net",
                                    "section_type": "Answer",
                                    "ttl": 97
                                },
                                {
                                    "host": "igw.sbr-cm001.gateway.prod.cm.powerapps.com.privatelink.powerplatform.com",
                                    "host_type": "CNAME",
                                    "name": "ppapigw.sbr-cm001.gateway.prod.cm.powerapps.com",
                                    "section_type": "Answer",
                                    "ttl": 2379
                                },
                                {
                                    "host": "prdcm001sbrigw-tm.trafficmanager.net",
                                    "host_type": "CNAME",
                                    "name": "igw.sbr-cm001.gateway.prod.cm.powerapps.com.privatelink.powerplatform.com",
                                    "section_type": "Answer",
                                    "ttl": 728
                                },
                                {
                                    "host_addr": "4.203.146.0",
                                    "host_type": "A",
                                    "name": "prdcm001sbrigw-tm.trafficmanager.net",
                                    "section_type": "Answer",
                                    "ttl": 60
                                }
                            ],
                            "domain_creation": "2002-09-30T20:21:54Z",
                            "effective_tld": "powerplatform.com",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 41,
                            "query": "5bbcc1a171964832b76a345a31a53a.eb.tenant.api.powerplatform.com",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "4.203.146.0"
                            ],
                            "response_time": 55,
                            "transaction_id": 33329
                        },
                        "transaction_id": 33329
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
                    "orig_id": "TGFna58BI3UnQyDOLYEL",
                    "orig_index": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 440,
                    "outbytes_total": 440,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 41,
                    "proto": 6,
                    "proto_name": "tcp",
                    "query_count": 33,
                    "receive_time": 1784213348636,
                    "response_time": 55,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.99",
                    "srcip": "192.168.169.99",
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
                    "srcip_host": "nb-agsilvero.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 53959,
                    "start_bucket_time": 1784213100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784213701850,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 351166,
                        "status": "New"
                    },
                    "stellar_da_input": 2253,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "325f6ebf-e4ef-40d5-98b6-403f9ec40bb11784213701869-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 14,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784213348442,
                    "timestamp_utc": "2026-07-16T14:49:08.000Z",
                    "tos": 0,
                    "total_entropy": 89,
                    "totalbytes": 1079,
                    "totalpackets": 11,
                    "tunnel_domain": "powerplatform.com",
                    "tunnel_payloads": [
                        "ppapigw.us-il103.gateway.prod.island.powerapps.com.apigw-prdil103-us.trafficmanager.net.ppapigw.eus-il103.gateway.prod.island.powerapps.com.igw.eus-il103.gateway.prod.island.powerapps.com.privatelink.powerplatform.com.prdil103eusigw-tm.trafficmanager.net",
                        "5bbcc1a171964832b76a345a31a53a.eb.tenant.api",
                        "ppapigw.br-cm001.gateway.prod.cm.powerapps.com.apigw-prdcm001-br.trafficmanager.net.ppapigw.sbr-cm001.gateway.prod.cm.powerapps.com.igw.sbr-cm001.gateway.prod.cm.powerapps.com.privatelink.powerplatform.com.prdcm001sbrigw-tm.trafficmanager.net.tm1.dns-tm.com",
                        "default5bbcc1a171964832b76a345a31a53a.eb.environment.api",
                        "il-5bbcc1a171964832b76a345a31a53a.eb.tenant.api"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 29.3,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784213701869,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 366 Bytes) of tunneled, high-entropy traffic through DNS (domain: powerplatform.com) has been observed between \"IP: 192.168.169.99, name: nb-agsilvero.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"ppapigw.br-cm001.gateway.prod.cm.powerapps.com.api...rdcm001sbrigw-tm.trafficmanager.net.tm1.dns-tm.com.\" The typical volume of traffic transmitted through this tunnel is 29 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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
                "_id": "e0dd9e0f-edcc-441a-b47d-664d3aad85561784213702891-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 12074,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 470,
                    "aella_tuples": "192.168.169.99.10.11.1.1.53.32",
                    "anomaly_id": "d2Fna58BI3UnQyDO7pSe",
                    "appid": 32,
                    "appid_family": "Network",
                    "appid_name": "dns",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "srcip",
                        "metadata.request.effective_tld"
                    ],
                    "detected_values": [
                        "192.168.169.99",
                        "azure-apim.net"
                    ],
                    "domain_list": [
                        "global.consent.azure-apim.net"
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
                    "duration": 67,
                    "end_bucket_time": 1784213400000,
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
                    "inbytes_delta": 642,
                    "inbytes_total": 642,
                    "inpkts_delta": 5,
                    "is_dga": "no",
                    "lateral": false,
                    "locid": "unassigned location",
                    "metadata": {
                        "_whitelist": 0,
                        "is_tunneling": 8,
                        "request": {
                            "dga_score": 0,
                            "domain_creation": "2015-09-21T22:25:49Z",
                            "effective_tld": "azure-apim.net",
                            "flags": 256,
                            "message_type": "QUERY",
                            "query": "global.consent.azure-apim.net",
                            "query_type": "A",
                            "transaction_id": 4660
                        },
                        "response": {
                            "answers": [
                                {
                                    "host": "global-consent.trafficmanager.net",
                                    "host_type": "CNAME",
                                    "name": "global.consent.azure-apim.net",
                                    "section_type": "Answer",
                                    "ttl": 257
                                },
                                {
                                    "host": "brazil-001.consent.azure-apim.net",
                                    "host_type": "CNAME",
                                    "name": "global-consent.trafficmanager.net",
                                    "section_type": "Answer",
                                    "ttl": 236
                                },
                                {
                                    "host": "brazil-001-consent.trafficmanager.net",
                                    "host_type": "CNAME",
                                    "name": "brazil-001.consent.azure-apim.net",
                                    "section_type": "Answer",
                                    "ttl": 1572
                                },
                                {
                                    "host": "power-consent-brazilsouth.azurewebsites.net",
                                    "host_type": "CNAME",
                                    "name": "brazil-001-consent.trafficmanager.net",
                                    "section_type": "Answer",
                                    "ttl": 26
                                },
                                {
                                    "host": "waws-prod-cq1-001a.sip.azurewebsites.windows.net",
                                    "host_type": "CNAME",
                                    "name": "power-consent-brazilsouth.azurewebsites.net",
                                    "section_type": "Answer",
                                    "ttl": 957
                                },
                                {
                                    "host": "waws-prod-cq1-001.brazilsouth.cloudapp.azure.com",
                                    "host_type": "CNAME",
                                    "name": "waws-prod-cq1-001a.sip.azurewebsites.windows.net",
                                    "section_type": "Answer",
                                    "ttl": 3110
                                },
                                {
                                    "host_addr": "23.97.96.32",
                                    "host_type": "A",
                                    "name": "waws-prod-cq1-001.brazilsouth.cloudapp.azure.com",
                                    "section_type": "Answer",
                                    "ttl": 10
                                }
                            ],
                            "domain_creation": "2015-09-21T22:25:49Z",
                            "effective_tld": "azure-apim.net",
                            "flags": 33152,
                            "message_type": "RESPONSE",
                            "processing_time": 50,
                            "query": "global.consent.azure-apim.net",
                            "query_type": "A",
                            "reply_code": "No Error",
                            "resolved_ips": [
                                "23.97.96.32"
                            ],
                            "response_time": 55,
                            "transaction_id": 4660
                        },
                        "transaction_id": 4660
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
                    "orig_id": "d2Fna58BI3UnQyDO7pSe",
                    "orig_index": "aella-adr-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "outbytes_delta": 407,
                    "outbytes_total": 407,
                    "outpkts_delta": 6,
                    "port_name": "ethernet1",
                    "processing_time": 50,
                    "proto": 6,
                    "proto_name": "tcp",
                    "query_count": 31,
                    "receive_time": 1784213399155,
                    "response_time": 55,
                    "severity": 98,
                    "src_tuples": "00:09:0f:09:0a:04.1101.192.168.169.99",
                    "srcip": "192.168.169.99",
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
                    "srcip_host": "nb-agsilvero.technoma.local",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "00:09:0f:09:0a:04",
                    "srcport": 54328,
                    "start_bucket_time": 1784213100000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784213702002,
                        "alert_timestamp_field": "timestamp",
                        "detection_time": 301478,
                        "status": "New"
                    },
                    "stellar_da_input": 2243,
                    "stellar_index_id": "aella-ser-2026.07.16-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "e0dd9e0f-edcc-441a-b47d-664d3aad85561784213702891-YWVsbGEtc2VyLTIwMjYuMDcuMTYtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tcp_rtt": 5,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1784213398124,
                    "timestamp_utc": "2026-07-16T14:49:58.000Z",
                    "tos": 0,
                    "total_entropy": 94,
                    "totalbytes": 1049,
                    "totalpackets": 11,
                    "tunnel_domain": "azure-apim.net",
                    "tunnel_payloads": [
                        "msmanaged-na",
                        "power-apim-msmanaged-na.azure-api.net.apimgmttmipzxrbrcjfvkgqeqvgvifxmhdwm7ixglx2e6pvdap.trafficmanager.net.power-apim-msmanaged-na-eastus-01.regional.azure-api.net.api792f053babc7405a8b145e005294c309ayglieg0npbzykbgbk6fv.eastus.cloudapp.azure.com",
                        "msmanaged-na.consent",
                        "global.consent",
                        "msmanaged-na-consent.trafficmanager.net.power-consent-westus.azurewebsites.net.waws-prod-bay-053a.sip.azurewebsites.windows.net.waws-prod-bay-053.westus.cloudapp.azure.com"
                    ],
                    "tunnel_type": "point_to_point",
                    "typical": 29.15,
                    "vlan": 1101,
                    "write_by": "sef",
                    "write_time": 1784213702891,
                    "xdr_event": {
                        "description": "An anomalously large amount (#: 470 Bytes) of tunneled, high-entropy traffic through DNS (domain: azure-apim.net) has been observed between \"IP: 192.168.169.99, name: nb-agsilvero.technoma.local\" and \"IP: 10.11.1.1, name: ad.technoma.local\". One of the tunnel payloads is \"power-apim-msmanaged-na.azure-api.net.apimgmttmipz...309ayglieg0npbzykbgbk6fv.eastus.cloudapp.azure.com.\" The typical volume of traffic transmitted through this tunnel is 29 Bytes, measured in a 5.0-minute interval. This indicates potential DNS tunnelling.",
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

[*] Solicitando comando PUT de asignacion para Ticket 12265...

[+] REPORTE: Caso e historial de notas impactados con exito en el backend.