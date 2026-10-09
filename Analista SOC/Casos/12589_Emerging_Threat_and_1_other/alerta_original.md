=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "0190dcd0-0b0c-4188-bd01-8be0cd1d90821784879465195-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4581,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "emerging_threat_dstip",
                    "action": "close",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "172.17.10.124.146.112.61.104.80.4",
                    "alert_time": 1784879465142,
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-24 07:44:26 UTC",
                        "first_timestamp": 1784879066192,
                        "last_time_utc": "2026-07-24 07:44:26 UTC",
                        "last_timestamp": 1784879066192,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "emerging_threat_dstip",
                        "scheduled_time_utc": "2026-07-24T07:49:00.000Z",
                        "scheduled_timestamp": 1784879340000
                    },
                    "detected_fields": [
                        "dstip",
                        "srcip"
                    ],
                    "detected_values": [
                        "146.112.61.104",
                        "172.17.10.124"
                    ],
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784879066192,
                    "dscp_name": "Best Effort",
                    "dstip": "146.112.61.104",
                    "dstip_asn": 36692,
                    "dstip_asn_org": "Cisco OpenDNS, LLC",
                    "dstip_domain_creation": "2025-10-10T08:01:56Z",
                    "dstip_geo": {
                        "city": "San Jose",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.4073,
                        "longitude": -121.939,
                        "region": "California"
                    },
                    "dstip_geo_point": "37.4073,-121.939",
                    "dstip_host": "blacksaltys.com",
                    "dstip_host_reputation": "emerging_threat",
                    "dstip_host_reputation_source": "SocGholish_Malware_2025_03",
                    "dstip_reputation": "emerging_threat",
                    "dstip_reputation_source": "SocGholish_Malware_2025_03",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "duration": 1,
                    "end_bucket_time": 1784879340000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784879066192
                    },
                    "event_category": "killchain",
                    "event_name": "emerging_threat",
                    "event_score": 84,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_summary": {
                        "ioc_source_repu_summary": {
                            "dstip_reputation": [
                                "emerging_threat"
                            ],
                            "dstip_reputation_source": [
                                "SocGholish_Malware_2025_03"
                            ]
                        }
                    },
                    "event_type": "delivery",
                    "fidelity": 90,
                    "fortinet": {
                        "appcat": "unscanned",
                        "date": "2026-07-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcountry": "United States",
                        "dstintf": "port1",
                        "dstintfrole": "wan",
                        "event_time": "2026-07-24 04:44:26",
                        "eventtime": "1784879066191879890",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:03:00:02:00:00",
                        "policyname": "Serv-a-Internet",
                        "policytype": "policy",
                        "poluuid": "4607889c-ca3f-51f0-882a-9813e2bd364a",
                        "rule_id": 136,
                        "service": "HTTP",
                        "sessionid": "2605092843",
                        "srccountry": "Reserved",
                        "srcintf": "LAB-SERVER",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "04:44:26",
                        "trandisp": "snat",
                        "transip": "190.128.219.210",
                        "transport": "5176",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "0"
                    },
                    "fw_policy_id": "FG-Technoma_136",
                    "inbytes_total": 862,
                    "inpkts_delta": 4,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_data": [
                        {
                            "name": "shapingpolicyid",
                            "strvalue": "3"
                        },
                        {
                            "name": "shapingpolicyname",
                            "strvalue": "TS_Servidores"
                        },
                        {
                            "name": "shapersentname",
                            "strvalue": "FULL"
                        },
                        {
                            "name": "shaperdropsentbyte",
                            "strvalue": "0"
                        },
                        {
                            "name": "shaperrcvdname",
                            "strvalue": "FULL"
                        },
                        {
                            "name": "shaperdroprcvdbyte",
                            "strvalue": "0"
                        }
                    ],
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
                    "orig_id": "Vz4Xk58BI3UnQyDOsZAq",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.16-000051",
                    "orig_timestamp": 1784879066192,
                    "orig_timestamp_utc": "2026-07-24T07:44:26.000Z",
                    "orig_write_time": 1784879230489,
                    "outbytes_total": 408,
                    "outpkts_delta": 5,
                    "parser_raw_msg": "<189>date=2026-07-24 time=04:44:26 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784879066191879890 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=172.17.10.124 srcport=5176 srcintf=\"LAB-SERVER\" srcintfrole=\"lan\" dstip=146.112.61.104 dstport=80 dstintf=\"port1\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstcountry=\"United States\" sessionid=2605092843 proto=6 action=\"close\" policyid=136 policytype=\"policy\" poluuid=\"4607889c-ca3f-51f0-882a-9813e2bd364a\" policyname=\"Serv-a-Internet\" service=\"HTTP\" trandisp=\"snat\" transip=190.128.219.210 transport=5176 appcat=\"unscanned\" duration=1 sentbyte=408 rcvdbyte=862 sentpkt=5 rcvdpkt=4 shapingpolicyid=3 shapingpolicyname=\"TS_Servidores\" shapersentname=\"FULL\" shaperdropsentbyte=0 shaperrcvdname=\"FULL\" shaperdroprcvdbyte=0 vwlid=0 devtype=\"Router\" mastersrcmac=\"50:03:00:02:00:00\" srcmac=\"50:03:00:02:00:00\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784879229522,
                    "severity": 80,
                    "src_tuples": "50:03:00:02:00:00.0.172.17.10.124",
                    "srcip": "172.17.10.124",
                    "srcip_assetid": "30c11fe0-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "172.17.10.124",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "50:03:00:02:00:00",
                    "srcport": 5176,
                    "start_bucket_time": 1784879040000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784879465142,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 234653,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2993,
                    "stellar_index": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "0190dcd0-0b0c-4188-bd01-8be0cd1d90821784879465195-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1784879340000,
                    "summary_start": 1784879040000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 75,
                    "timestamp": 1784879066192,
                    "timestamp_utc": "2026-07-24T07:44:26.000Z",
                    "totalbytes": 1270,
                    "totalpackets": 9,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784879465195,
                    "xdr_event": {
                        "description": "The traffic from \"IP/name: 172.17.10.124\" to \"IP: 146.112.61.104, name: blacksaltys.com\" has one or more emerging threats (SocGholish_Malware_2025_03) on the destination IP 146.112.61.104.",
                        "display_name": "Emerging Threat",
                        "framework_version": "v8",
                        "name": "emerging_threat",
                        "scope": "",
                        "tactic": {
                            "id": "XTA0005",
                            "name": "XDR Intel"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT5003",
                            "name": "XDR Emerging Threat"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.19-000029",
                "_type": "_doc",
                "_id": "72887481-e2b0-4c62-b6fc-b428fd7983801784889676408-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4704,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "_detection_id": "emerging_threat_dstip",
                    "action": "close",
                    "actual": 1,
                    "advanced": 2,
                    "aella_tuples": "172.17.10.124.146.112.61.104.80.4",
                    "alert_time": 1784889676366,
                    "appid": 4,
                    "appid_family": "Standard",
                    "appid_name": "HTTP",
                    "appid_stdport": "yes",
                    "ath_deduplication": {
                        "first_time_utc": "2026-07-24 10:33:10 UTC",
                        "first_timestamp": 1784889190852,
                        "last_time_utc": "2026-07-24 10:33:10 UTC",
                        "last_timestamp": 1784889190852,
                        "repeat_count": 1,
                        "time_window_ms": null
                    },
                    "ath_info": {
                        "rule_name": "emerging_threat_dstip",
                        "scheduled_time_utc": "2026-07-24T10:39:00.000Z",
                        "scheduled_timestamp": 1784889540000
                    },
                    "detected_fields": [
                        "dstip",
                        "srcip"
                    ],
                    "detected_values": [
                        "146.112.61.104",
                        "172.17.10.124"
                    ],
                    "dev_class": "firewall",
                    "dev_type": "fw_fortigate",
                    "device": {
                        "name": "FG-Technoma"
                    },
                    "domain_creation": 1784889190852,
                    "dscp_name": "Best Effort",
                    "dstip": "146.112.61.104",
                    "dstip_asn": 36692,
                    "dstip_asn_org": "Cisco OpenDNS, LLC",
                    "dstip_domain_creation": "2025-10-10T08:01:56Z",
                    "dstip_geo": {
                        "city": "San Jose",
                        "countryCode": "US",
                        "countryName": "United States",
                        "latitude": 37.4073,
                        "longitude": -121.939,
                        "region": "California"
                    },
                    "dstip_geo_point": "37.4073,-121.939",
                    "dstip_host": "blacksaltys.com",
                    "dstip_host_reputation": "emerging_threat",
                    "dstip_host_reputation_source": "SocGholish_Malware_2025_03",
                    "dstip_reputation": "emerging_threat",
                    "dstip_reputation_source": "SocGholish_Malware_2025_03",
                    "dstip_type": "public",
                    "dstip_version": "ipv4",
                    "dstmac": "00:00:00:00:00:00",
                    "dstport": 80,
                    "duration": 1,
                    "end_bucket_time": 1784889540000,
                    "engid": "4e3eab0649114a80a089a5d5a078994d",
                    "engid_gateway": "190.104.178.146",
                    "engid_name": "technoma-sensor",
                    "event": {
                        "timestamp": 1784889190852
                    },
                    "event_category": "killchain",
                    "event_name": "emerging_threat",
                    "event_score": 84,
                    "event_source": "sa",
                    "event_status": "New",
                    "event_summary": {
                        "ioc_source_repu_summary": {
                            "dstip_reputation": [
                                "emerging_threat"
                            ],
                            "dstip_reputation_source": [
                                "SocGholish_Malware_2025_03"
                            ]
                        }
                    },
                    "event_type": "delivery",
                    "fidelity": 90,
                    "fortinet": {
                        "appcat": "unscanned",
                        "date": "2026-07-24",
                        "dev_name": "FG-Technoma",
                        "devid": "FG120GTK24022543",
                        "devtype": "Router",
                        "dstcountry": "United States",
                        "dstintf": "port1",
                        "dstintfrole": "wan",
                        "event_time": "2026-07-24 07:33:11",
                        "eventtime": "1784889190851885493",
                        "level": "notice",
                        "logid": "0000000013",
                        "mastersrcmac": "50:03:00:02:00:00",
                        "policyname": "Serv-a-Internet",
                        "policytype": "policy",
                        "poluuid": "4607889c-ca3f-51f0-882a-9813e2bd364a",
                        "rule_id": 136,
                        "service": "HTTP",
                        "sessionid": "2615890658",
                        "srccountry": "Reserved",
                        "srcintf": "LAB-SERVER",
                        "srcintfrole": "lan",
                        "srcserver": "0",
                        "subtype": "forward",
                        "time": "07:33:11",
                        "trandisp": "snat",
                        "transip": "190.128.219.210",
                        "transport": "5159",
                        "type": "traffic",
                        "tz": "-0300",
                        "vd": "root",
                        "vwlid": "0"
                    },
                    "fw_policy_id": "FG-Technoma_136",
                    "inbytes_total": 862,
                    "inpkts_delta": 4,
                    "locid": "unassigned location",
                    "log": {
                        "syslog": {
                            "priority": 189
                        }
                    },
                    "msg_class": "firewall",
                    "msg_data": [
                        {
                            "name": "shapingpolicyid",
                            "strvalue": "3"
                        },
                        {
                            "name": "shapingpolicyname",
                            "strvalue": "TS_Servidores"
                        },
                        {
                            "name": "shapersentname",
                            "strvalue": "FULL"
                        },
                        {
                            "name": "shaperdropsentbyte",
                            "strvalue": "0"
                        },
                        {
                            "name": "shaperrcvdname",
                            "strvalue": "FULL"
                        },
                        {
                            "name": "shaperdroprcvdbyte",
                            "strvalue": "0"
                        }
                    ],
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
                    "orig_id": "FUOyk58BI3UnQyDOQgub",
                    "orig_index": "stellar-index-v1-adr-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.16-000051",
                    "orig_timestamp": 1784889190852,
                    "orig_timestamp_utc": "2026-07-24T10:33:10.000Z",
                    "orig_write_time": 1784889360565,
                    "outbytes_total": 408,
                    "outpkts_delta": 5,
                    "parser_raw_msg": "<189>date=2026-07-24 time=07:33:11 devname=\"FG-Technoma\" devid=\"FG120GTK24022543\" eventtime=1784889190851885493 tz=\"-0300\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" srcip=172.17.10.124 srcport=5159 srcintf=\"LAB-SERVER\" srcintfrole=\"lan\" dstip=146.112.61.104 dstport=80 dstintf=\"port1\" dstintfrole=\"wan\" srccountry=\"Reserved\" dstcountry=\"United States\" sessionid=2615890658 proto=6 action=\"close\" policyid=136 policytype=\"policy\" poluuid=\"4607889c-ca3f-51f0-882a-9813e2bd364a\" policyname=\"Serv-a-Internet\" service=\"HTTP\" trandisp=\"snat\" transip=190.128.219.210 transport=5159 appcat=\"unscanned\" duration=1 sentbyte=408 rcvdbyte=862 sentpkt=5 rcvdpkt=4 shapingpolicyid=3 shapingpolicyname=\"TS_Servidores\" shapersentname=\"FULL\" shaperdropsentbyte=0 shaperrcvdname=\"FULL\" shaperdroprcvdbyte=0 vwlid=0 devtype=\"Router\" mastersrcmac=\"50:03:00:02:00:00\" srcmac=\"50:03:00:02:00:00\" srcserver=0",
                    "proto": 6,
                    "proto_name": "tcp",
                    "receive_time": 1784889359859,
                    "severity": 80,
                    "src_tuples": "50:03:00:02:00:00.0.172.17.10.124",
                    "srcip": "172.17.10.124",
                    "srcip_assetid": "30c11fe0-caab-11f0-b1b7-828ad4fe26cd",
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
                    "srcip_host": "172.17.10.124",
                    "srcip_reputation": "Good",
                    "srcip_type": "private",
                    "srcip_version": "ipv4",
                    "srcmac": "50:03:00:02:00:00",
                    "srcport": 5159,
                    "start_bucket_time": 1784889240000,
                    "state": "Closed",
                    "stellar": {
                        "alert_time": 1784889676366,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 315801,
                        "status": "New"
                    },
                    "stellar_client_addr": "127.0.0.1",
                    "stellar_da_input": 2993,
                    "stellar_index": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_index_id": "aella-ser-2026.07.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_ingestion_port": 5149,
                    "stellar_uuid": "72887481-e2b0-4c62-b6fc-b428fd7983801784889676408-YWVsbGEtc2VyLTIwMjYuMDcuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "summary_end": 1784889540000,
                    "summary_start": 1784889240000,
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 75,
                    "timestamp": 1784889190852,
                    "timestamp_utc": "2026-07-24T10:33:10.000Z",
                    "totalbytes": 1270,
                    "totalpackets": 9,
                    "vlan": 0,
                    "write_by": "sef",
                    "write_time": 1784889676408,
                    "xdr_event": {
                        "description": "The traffic from \"IP/name: 172.17.10.124\" to \"IP: 146.112.61.104, name: blacksaltys.com\" has one or more emerging threats (SocGholish_Malware_2025_03) on the destination IP 146.112.61.104.",
                        "display_name": "Emerging Threat",
                        "framework_version": "v8",
                        "name": "emerging_threat",
                        "scope": "",
                        "tactic": {
                            "id": "XTA0005",
                            "name": "XDR Intel"
                        },
                        "tags": [
                            "Network Traffic Analysis"
                        ],
                        "technique": {
                            "id": "XT5003",
                            "name": "XDR Emerging Threat"
                        },
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}