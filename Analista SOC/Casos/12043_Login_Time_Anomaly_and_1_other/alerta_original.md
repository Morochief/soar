=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6088e4f0-bc2a-4a11-8ccf-d1721fa6426d1783827902333-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9703,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "00:00-01:00 UTC-3:00",
                    "anomaly_id": "sjxoVJ8BI3UnQyDOBZAU",
                    "detected_fields": [
                        "srcip_usersid"
                    ],
                    "detected_values": [
                        "fabianrojas@technoma.com.py"
                    ],
                    "dscp_name": "Best Effort",
                    "end_bucket_time": 1783827600000,
                    "engid": "gsuite_Workspace-THN",
                    "engid_gateway": "",
                    "engid_name": "gsuite_Workspace-THN",
                    "event_category": "uba",
                    "event_detail": {
                        "is_suspicious": false,
                        "login_challenge_method": [
                            "none"
                        ],
                        "login_type": "reauth",
                        "name": "login_success",
                        "type": "login"
                    },
                    "event_name": "user_login_time",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 98.3,
                    "gsuite": {
                        "actor": {
                            "email": "fabianrojas@technoma.com.py",
                            "profileId": "110310147781444192197"
                        },
                        "etag": "\"e-6P-1PgHg-a_APD3OoAD2ESC2P_5fMZbYztqEAlHhI/6h0umKK6oPu8UG3xlTgQUdvLmwI\"",
                        "events": [
                            {
                                "name": "login_success",
                                "parameters": [
                                    {
                                        "name": "login_type",
                                        "value": "reauth"
                                    },
                                    {
                                        "multiValue": [
                                            "none"
                                        ],
                                        "name": "login_challenge_method"
                                    },
                                    {
                                        "boolValue": false,
                                        "name": "is_suspicious"
                                    }
                                ],
                                "resourceIds": [
                                    "30j0zll174w6qi"
                                ],
                                "type": "login"
                            }
                        ],
                        "id": {
                            "applicationName": "login",
                            "customerId": "C02am33mw",
                            "time": "2026-07-12T03:26:49.088Z",
                            "uniqueQualifier": "-8341104688959755566"
                        },
                        "ipAddress": "181.121.212.232",
                        "kind": "admin#reports#activity",
                        "networkInfo": {
                            "ipAsn": [
                                23201
                            ],
                            "regionCode": "PY",
                            "subdivisionCode": "PY-11"
                        },
                        "resourceDetails": [
                            {
                                "id": "30j0zll174w6qi",
                                "ownerDetails": {
                                    "ownerIdentity": [
                                        {
                                            "customerIdentity": {
                                                "id": "02am33mw"
                                            }
                                        }
                                    ],
                                    "ownerType": "CUSTOMER"
                                },
                                "title": "fabianrojas@technoma.com.py",
                                "type": "USER"
                            }
                        ]
                    },
                    "lateral": false,
                    "locid": "unassigned location",
                    "login_result": "success",
                    "login_type": "gsuite",
                    "msg_class": "gsuite",
                    "msg_origin": {
                        "source": "gsuite"
                    },
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "sjxoVJ8BI3UnQyDOBZAU",
                    "orig_index": "aella-audit-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "severity": 40,
                    "srcip": "181.121.212.232",
                    "srcip_asn": 23201,
                    "srcip_asn_org": "Telecel S.A.",
                    "srcip_geo": {
                        "city": "Luque",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2682,
                        "longitude": -57.4863,
                        "region": "Central Department"
                    },
                    "srcip_geo_point": "-25.2682,-57.4863",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "181.121.212.232",
                    "srcip_reputation": "Good",
                    "srcip_type": "public",
                    "srcip_username": "fabianrojas@technoma.com.py",
                    "srcip_usersid": "fabianrojas@technoma.com.py",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1783827300000,
                    "stellar": {
                        "alert_time": 1783827902316,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 371296,
                        "status": "New"
                    },
                    "stellar_da_input": 1548,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6088e4f0-bc2a-4a11-8ccf-d1721fa6426d1783827902333-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783826809088,
                    "timestamp_utc": "2026-07-12T03:26:49.000Z",
                    "typical": 0.42,
                    "typical_range": "09:00-12:00 UTC-3:00",
                    "username": "fabianrojas@technoma.com.py",
                    "write_by": "sef",
                    "write_time": 1783827902333,
                    "xdr_event": {
                        "description": "The account with ID \"fabianrojas@technoma.com.py\", username \"fabianrojas@technoma.com.py\" has logged in at an abnormal time range 00:00-01:00 UTC-3:00, compared to the typical login time range: 09:00-12:00 UTC-3:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "aa921e2c-e9cc-4c30-bbd4-241c0875dd131783827903559-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 9704,
                "_primary_term": 3,
                "found": true,
                "_source": {
                    "actual": 0,
                    "actual_range": "00:00-01:00 UTC-3:00",
                    "anomaly_id": "sjxoVJ8BI3UnQyDOBZAU",
                    "detected_fields": [
                        "srcip_usersid"
                    ],
                    "detected_values": [
                        "fabianrojas@technoma.com.py"
                    ],
                    "dscp_name": "Best Effort",
                    "end_bucket_time": 1783827600000,
                    "engid": "gsuite_Workspace-THN",
                    "engid_gateway": "",
                    "engid_name": "gsuite_Workspace-THN",
                    "event_category": "uba",
                    "event_detail": {
                        "is_suspicious": false,
                        "login_challenge_method": [
                            "none"
                        ],
                        "login_type": "reauth",
                        "name": "login_success",
                        "type": "login"
                    },
                    "event_name": "user_login_time",
                    "event_score": 54,
                    "event_source": "new_ml",
                    "event_status": "New",
                    "event_type": "uba",
                    "fidelity": 98.3,
                    "gsuite": {
                        "actor": {
                            "email": "fabianrojas@technoma.com.py",
                            "profileId": "110310147781444192197"
                        },
                        "etag": "\"e-6P-1PgHg-a_APD3OoAD2ESC2P_5fMZbYztqEAlHhI/6h0umKK6oPu8UG3xlTgQUdvLmwI\"",
                        "events": [
                            {
                                "name": "login_success",
                                "parameters": [
                                    {
                                        "name": "login_type",
                                        "value": "reauth"
                                    },
                                    {
                                        "multiValue": [
                                            "none"
                                        ],
                                        "name": "login_challenge_method"
                                    },
                                    {
                                        "boolValue": false,
                                        "name": "is_suspicious"
                                    }
                                ],
                                "resourceIds": [
                                    "30j0zll174w6qi"
                                ],
                                "type": "login"
                            }
                        ],
                        "id": {
                            "applicationName": "login",
                            "customerId": "C02am33mw",
                            "time": "2026-07-12T03:26:49.088Z",
                            "uniqueQualifier": "-8341104688959755566"
                        },
                        "ipAddress": "181.121.212.232",
                        "kind": "admin#reports#activity",
                        "networkInfo": {
                            "ipAsn": [
                                23201
                            ],
                            "regionCode": "PY",
                            "subdivisionCode": "PY-11"
                        },
                        "resourceDetails": [
                            {
                                "id": "30j0zll174w6qi",
                                "ownerDetails": {
                                    "ownerIdentity": [
                                        {
                                            "customerIdentity": {
                                                "id": "02am33mw"
                                            }
                                        }
                                    ],
                                    "ownerType": "CUSTOMER"
                                },
                                "title": "fabianrojas@technoma.com.py",
                                "type": "USER"
                            }
                        ]
                    },
                    "lateral": false,
                    "locid": "unassigned location",
                    "login_result": "success",
                    "login_type": "gsuite",
                    "msg_class": "gsuite",
                    "msg_origin": {
                        "source": "gsuite"
                    },
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "sjxoVJ8BI3UnQyDOBZAU",
                    "orig_index": "aella-audit-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "severity": 40,
                    "srcip": "181.121.212.232",
                    "srcip_asn": 23201,
                    "srcip_asn_org": "Telecel S.A.",
                    "srcip_geo": {
                        "city": "Luque",
                        "countryCode": "PY",
                        "countryName": "Paraguay",
                        "latitude": -25.2682,
                        "longitude": -57.4863,
                        "region": "Central Department"
                    },
                    "srcip_geo_point": "-25.2682,-57.4863",
                    "srcip_geo_source": "maxmind",
                    "srcip_host": "181.121.212.232",
                    "srcip_reputation": "Good",
                    "srcip_type": "public",
                    "srcip_username": "fabianrojas@technoma.com.py",
                    "srcip_usersid": "fabianrojas@technoma.com.py",
                    "srcip_version": "ipv4",
                    "start_bucket_time": 1783827300000,
                    "stellar": {
                        "alert_time": 1783827902328,
                        "alert_timestamp_field": "write_time",
                        "detection_time": 371308,
                        "status": "New"
                    },
                    "stellar_da_input": 1548,
                    "stellar_index_id": "aella-ser-2026.07.12-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "aa921e2c-e9cc-4c30-bbd4-241c0875dd131783827903559-YWVsbGEtc2VyLTIwMjYuMDcuMTItZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783826809088,
                    "timestamp_utc": "2026-07-12T03:26:49.000Z",
                    "typical": 0.42,
                    "typical_range": "09:00-12:00 UTC-3:00",
                    "username": "fabianrojas@technoma.com.py",
                    "write_by": "sef",
                    "write_time": 1783827903559,
                    "xdr_event": {
                        "description": "The account with ID \"fabianrojas@technoma.com.py\", username \"fabianrojas@technoma.com.py\" has logged in at an abnormal time range 00:00-01:00 UTC-3:00, compared to the typical login time range: 09:00-12:00 UTC-3:00 observed for this account.",
                        "display_name": "Login Time Anomaly",
                        "framework_version": "v8",
                        "name": "user_login_time",
                        "scope": "External",
                        "tactic": {
                            "id": "XTA0004",
                            "name": "XDR UBA"
                        },
                        "tags": [
                            "External",
                            "User Behavior Analytics",
                            "Identity Detection"
                        ],
                        "technique": {
                            "id": "XT4005",
                            "name": "XDR Time Anomaly"
                        },
                        "xdr_killchain_stage": "Initial Attempts",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}