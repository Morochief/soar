{
  "aella_tuples": "null.null.null.null",
  "anomaly_id": "3DghkKABI3UnQyDOMS9T",
  "appid_stdport": "yes",
  "computer_name": "CJPPA048",
  "detected_fields": [
    "tenantid",
    "sophos.id"
  ],
  "detected_values": [
    "392cf7319d694d53889280340fff51e9",
    "f5dcdc98-94ae-431b-8932-1348d7ea487d"
  ],
  "dms_job_id": "sophos_events",
  "dscp_name": "Best Effort",
  "engid": "sophos_CAJA-ANDE-SOPHOS",
  "engid_gateway": "",
  "engid_name": "sophos_CAJA-ANDE-SOPHOS",
  "event": {
    "severity_str": "low",
    "threat": {
      "name": "Event::Endpoint::WebControlViolation"
    },
    "type": "Endpoint"
  },
  "event_score": 15,
  "event_source": "sophos_events",
  "event_status": "New",
  "fidelity": 15,
  "group": "WEB",
  "host": {
    "ip": "172.16.202.68"
  },
  "hostip": "172.16.202.68",
  "hostip_assetid": "77d1d1b4-9bba-11f1-b930-8e57707220c4",
  "hostip_host": "172.16.202.68",
  "hostip_reputation": "Good",
  "hostip_type": "private",
  "hostip_version": "ipv4",
  "locid": "unassigned location",
  "msg_class": "sophos_events",
  "msg_origin": {
    "category": "endpoint",
    "processor": {
      "id": "69402f1ea496888ec6063954",
      "name": "sophos_events",
      "type": "log_collector"
    },
    "source": "sophos_events",
    "vendor": "sophos"
  },
  "msgtype_name": "start",
  "netid": 0,
  "netid_name": "vlannull",
  "org_id": "cf73a415c8794884a0c35b458b7c73ae",
  "orig_id": "3DghkKABI3UnQyDOMS9T",
  "orig_index": "aella-syslog-2026.09.11-392cf7319d694d53889280340fff51e9",
  "severity": 15,
  "sophos": {
    "created_at": "2026-09-11T10:58:04.984Z",
    "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
    "endpoint_id": "47945a39-1879-4fec-a785-dd4de736d76c",
    "endpoint_type": "computer",
    "group": "WEB",
    "id": "f5dcdc98-94ae-431b-8932-1348d7ea487d",
    "location": "CJPPA048",
    "name": "'https://translate.google.com' blocked due to category 'Proxies & Translators'",
    "severity": "low",
    "source": "CAJAANDE\\rvalenzuela",
    "source_info": {
      "ip": "172.16.202.68"
    },
    "type": "Event::Endpoint::WebControlViolation",
    "user_id": "6939794361055368e669777f",
    "when": "2026-09-11T10:57:43.000Z"
  },
  "stellar": {
    "detection_time": 74463,
    "status": "New"
  },
  "stellar_da_input": 1369,
  "stellar_index_id": "aella-ser-2026.09.11-392cf7319d694d53889280340fff51e9",
  "stellar_uuid": "45dff196-0ae6-428b-bb55-44d1f58930d71789124563282-YWVsbGEtc2VyLTIwMjYuMDkuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
  "tenant_name": "CAJAANDE",
  "tenantid": "392cf7319d694d53889280340fff51e9",
  "threat_score": 0,
  "timestamp": 1789124284984,
  "timestamp_utc": "2026-09-11T10:58:04.000Z",
  "totalbytes": 0,
  "totalpackets": 0,
  "user": {
    "name": "CAJAANDE\\rvalenzuela"
  },
  "username": "CAJAANDE\\rvalenzuela",
  "write_by": "sef",
  "write_time": 1789124563282,
  "xdr_event": {
    "description": "Sophos reported a suspicious event with the following details - Threat Name of \"Event::Endpoint::WebControlViolation\", Host IP of \"172.16.202.68\", User Name of \"CAJAANDE\\rvalenzuela\".\nThe description of the event states that \"'https://translate.google.com' blocked due to category 'Proxies & Translators'\"",
    "display_name": "Sophos Event: User Execution",
    "framework_version": "v13",
    "name": "sophos_event-execution-user_execution",
    "scope": "",
    "subtype": {
      "display_name": "Event::Endpoint::WebControlViolation",
      "name": "event_endpoint_webcontrolviolation"
    },
    "tactic": {
      "id": "TA0002",
      "name": "Execution"
    },
    "tags": [
      "Sophos"
    ],
    "technique": {
      "id": "T1204",
      "name": "User Execution"
    },
    "ttps": [
      {
        "tactic": {
          "id": "TA0002",
          "name": "Execution"
        },
        "technique": {
          "id": "T1204",
          "name": "User Execution"
        }
      }
    ],
    "xdr_killchain_stage": "Persistent Foothold",
    "xdr_killchain_version": "v1"
  },
  "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.02-000032",
  "_id": "45dff196-0ae6-428b-bb55-44d1f58930d71789124563282-YWVsbGEtc2VyLTIwMjYuMDkuMTEtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=",
  "_type": "_doc"
}
