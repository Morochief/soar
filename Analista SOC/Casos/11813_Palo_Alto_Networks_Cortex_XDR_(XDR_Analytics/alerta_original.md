=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "aa6b7b39-eb0c-420b-a2fb-3e388e2c2d9d1783518431058-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4887,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "Yrz5QZ8BBi0xHyA-2tul",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128145"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "PowerShell runs suspicious base64-encoded commands"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.64",
                        "name": "NB-AMARTINEZ"
                    },
                    "locid": "unassigned location",
                    "msg_class": "palo_alto_networks_cortex_xdr_alerts",
                    "msg_origin": {
                        "category": "threat_intel",
                        "processor": {
                            "id": "6939ef90a77d64c0b0abb567",
                            "name": "palo_alto_networks_cortex_xdr",
                            "type": "log_collector"
                        },
                        "source": "palo_alto_networks_cortex_xdr",
                        "vendor": "palo_alto_networks"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "Yrz5QZ8BBi0xHyA-2tul",
                    "orig_index": "aella-syslog-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128145",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process Codex.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days",
                        "detection_timestamp": 1783517934875,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "8be0647c97e049e9968470c010f4d0ef",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "action_process_image_command_line": "powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand CgBmAHUAbgBjAHQAaQBvAG4AIABEAGUAYwBvAGQAZQAtAFIAbwB0ADEAMwAgAHsACgAgACAAcABhAHIAYQBtACgAWwBzAHQAcgBpAG4AZwBdACQAVABlAHgAdAApAAoACgAgACAALQBqAG8AaQBuACAAKAAkAFQAZQB4AHQALgBUAG8AQwBoAGEAcgBBAHIAcgBhAHkAKAApACAAfAAgAEYAbwByAEUAYQBjAGgALQBPAGIAagBlAGMAdAAgAHsACgAgACAAIAAgACQAYwAgAD0AIABbAGkAbgB0AF0AWwBjAGgAYQByAF0AJABfAAoAIAAgACAAIABpAGYAIAAoACQAYwAgAC0AZwBlACAAWwBpAG4AdABdAFsAYwBoAGEAcgBdACcAYQAnACAALQBhAG4AZAAgACQAYwAgAC0AbABlACAAWwBpAG4AdABdAFsAYwBoAGEAcgBdACcAegAnACkAIAB7AAoAIAAgACAAIAAgACAAWwBjAGgAYQByAF0AKAAoACgAJABjACAALQAgAFsAaQBuAHQAXQBbAGMAaABhAHIAXQAnAGEAJwAgACsAIAAxADMAKQAgACUAIAAyADYAKQAgACsAIABbAGkAbgB0AF0AWwBjAGgAYQByAF0AJwBhACcAKQAKACAAIAAgACAAfQAgAGUAbABzAGUAaQBmACAAKAAkAGMAIAAtAGcAZQAgAFsAaQBuAHQAXQBbAGMAaABhAHIAXQAnAEEAJwAgAC0AYQBuAGQAIAAkAGMAIAAtAGwAZQAgAFsAaQBuAHQAXQBbAGMAaABhAHIAXQAnAFoAJwApACAAewAKACAAIAAgACAAIAAgAFsAYwBoAGEAcgBdACgAKAAoACQAYwAgAC0AIABbAGkAbgB0AF0AWwBjAGgAYQByAF0AJwBBACcAIAArACAAMQAzACkAIAAlACAAMgA2ACkAIAArACAAWwBpAG4AdABdAFsAYwBoAGEAcgBdACcAQQAnACkACgAgACAAIAAgAH0AIABlAGwAcwBlACAAewAKACAAIAAgACAAIAAgACQAXwAKACAAIAAgACAAfQAKACAAIAB9ACkACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABDAG8AbgB2AGUAcgB0AC0ARgBpAGwAZQBUAGkAbQBlAEIAeQB0AGUAcwAgAHsACgAgACAAcABhAHIAYQBtACgACgAgACAAIAAgAFsAYgB5AHQAZQBbAF0AXQAkAEIAeQB0AGUAcwAsAAoAIAAgACAAIABbAGkAbgB0AF0AJABPAGYAZgBzAGUAdAAKACAAIAApAAoACgAgACAAaQBmACAAKAAkAEIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACAALQBsAHQAIAAoACQATwBmAGYAcwBlAHQAIAArACAAOAApACkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAbgB1AGwAbAAKACAAIAB9AAoACgAgACAAJABmAGkAbABlAFQAaQBtAGUAIAA9ACAAWwBCAGkAdABDAG8AbgB2AGUAcgB0AGUAcgBdADoAOgBUAG8ASQBuAHQANgA0ACgAJABCAHkAdABlAHMALAAgACQATwBmAGYAcwBlAHQAKQAKACAAIABpAGYAIAAoACQAZgBpAGwAZQBUAGkAbQBlACAALQBsAGUAIAAwACkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAbgB1AGwAbAAKACAAIAB9AAoACgAgACAAdAByAHkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgAFsARABhAHQAZQBUAGkAbQBlAF0AOgA6AEYAcgBvAG0ARgBpAGwAZQBUAGkAbQBlACgAJABmAGkAbABlAFQAaQBtAGUAKQAKACAAIAB9ACAAYwBhAHQAYwBoACAAewAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAG4AdQBsAGwACgAgACAAfQAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEMAbwBuAHYAZQByAHQALQBEAGEAdABlAFQAaQBtAGUAVABvAFUAbgBpAHgATQBpAGwAbABpAHMAZQBjAG8AbgBkAHMAIAB7AAoAIAAgAHAAYQByAGEAbQAoAFsATgB1AGwAbABhAGIAbABlAFsARABhAHQAZQBUAGkAbQBlAF0AXQAkAEQAYQB0AGUAVABpAG0AZQApAAoACgAgACAAaQBmACAAKAAkAG4AdQBsAGwAIAAtAGUAcQAgACQARABhAHQAZQBUAGkAbQBlACkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgADAACgAgACAAfQAKAAoAIAAgAHIAZQB0AHUAcgBuACAAWwBEAGEAdABlAFQAaQBtAGUATwBmAGYAcwBlAHQAXQAkAEQAYQB0AGUAVABpAG0AZQAuAFQAbwBVAG4AaQB2AGUAcgBzAGEAbABUAGkAbQBlACgAKQAgAHwAIABGAG8AcgBFAGEAYwBoAC0ATwBiAGoAZQBjAHQAIAB7ACAAJABfAC4AVABvAFUAbgBpAHgAVABpAG0AZQBNAGkAbABsAGkAcwBlAGMAbwBuAGQAcwAoACkAIAB9AAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAAUABhAHIAcwBlAC0AVQBzAGUAcgBBAHMAcwBpAHMAdABWAGEAbAB1AGUAIAB7AAoAIAAgAHAAYQByAGEAbQAoAAoAIAAgACAAIABbAHMAdAByAGkAbgBnAF0AJABFAG4AYwBvAGQAZQBkAE4AYQBtAGUALAAKACAAIAAgACAAWwBiAHkAdABlAFsAXQBdACQAQgB5AHQAZQBzAAoAIAAgACkACgAKACAAIAAkAGwAYQBzAHQAUgB1AG4AIAA9ACAAJABuAHUAbABsAAoAIAAgAGkAZgAgACgAJABCAHkAdABlAHMALgBMAGUAbgBnAHQAaAAgAC0AZwBlACAANgA4ACkAIAB7AAoAIAAgACAAIAAkAGwAYQBzAHQAUgB1AG4AIAA9ACAAQwBvAG4AdgBlAHIAdAAtAEYAaQBsAGUAVABpAG0AZQBCAHkAdABlAHMAIAAtAEIAeQB0AGUAcwAgACQAQgB5AHQAZQBzACAALQBPAGYAZgBzAGUAdAAgADYAMAAKACAAIAB9ACAAZQBsAHMAZQBpAGYAIAAoACQAQgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAIAAtAGcAZQAgADEANgApACAAewAKACAAIAAgACAAJABsAGEAcwB0AFIAdQBuACAAPQAgAEMAbwBuAHYAZQByAHQALQBGAGkAbABlAFQAaQBtAGUAQgB5AHQAZQBzACAALQBCAHkAdABlAHMAIAAkAEIAeQB0AGUAcwAgAC0ATwBmAGYAcwBlAHQAIAA4AAoAIAAgAH0ACgAKACAAIABbAHAAcwBjAHUAcwB0AG8AbQBvAGIAagBlAGMAdABdAEAAewAKACAAIAAgACAATgBhAG0AZQAgAD0AIABEAGUAYwBvAGQAZQAtAFIAbwB0ADEAMwAgACQARQBuAGMAbwBkAGUAZABOAGEAbQBlAAoAIAAgACAAIABSAHUAbgBDAG8AdQBuAHQAIAA9ACAAaQBmACAAKAAkAEIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACAALQBnAGUAIAA4ACkAIAB7ACAAWwBCAGkAdABDAG8AbgB2AGUAcgB0AGUAcgBdADoAOgBUAG8ASQBuAHQAMwAyACgAJABCAHkAdABlAHMALAAgADQAKQAgAH0AIABlAGwAcwBlACAAewAgADAAIAB9AAoAIAAgACAAIABMAGEAcwB0AFIAdQBuAE0AcwAgAD0AIABDAG8AbgB2AGUAcgB0AC0ARABhAHQAZQBUAGkAbQBlAFQAbwBVAG4AaQB4AE0AaQBsAGwAaQBzAGUAYwBvAG4AZABzACAAJABsAGEAcwB0AFIAdQBuAAoAIAAgAH0ACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABHAGUAdAAtAFUAcwBlAHIAQQBzAHMAaQBzAHQARQBuAHQAcgBpAGUAcwAgAHsACgAgACAAZgBvAHIAZQBhAGMAaAAgACgAJABjAG8AdQBuAHQASwBlAHkAIABpAG4AIABHAGUAdAAtAEMAaABpAGwAZABJAHQAZQBtACAAJwBIAEsAQwBVADoAXABTAG8AZgB0AHcAYQByAGUAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABDAHUAcgByAGUAbgB0AFYAZQByAHMAaQBvAG4AXABFAHgAcABsAG8AcgBlAHIAXABVAHMAZQByAEEAcwBzAGkAcwB0AFwAKgBcAEMAbwB1AG4AdAAnACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlACkAIAB7AAoAIAAgACAAIAAkAHAAcgBvAHAAcwAgAD0AIABHAGUAdAAtAEkAdABlAG0AUAByAG8AcABlAHIAdAB5ACAALQBQAGEAdABoACAAJABjAG8AdQBuAHQASwBlAHkALgBQAFMAUABhAHQAaAAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJABwAHIAbwBwACAAaQBuACAAJABwAHIAbwBwAHMALgBQAFMATwBiAGoAZQBjAHQALgBQAHIAbwBwAGUAcgB0AGkAZQBzACkAIAB7AAoAIAAgACAAIAAgACAAaQBmACAAKAAkAHAAcgBvAHAALgBOAGEAbQBlACAALQBpAG4AIAAnAFAAUwBQAGEAdABoACcALAAgACcAUABTAFAAYQByAGUAbgB0AFAAYQB0AGgAJwAsACAAJwBQAFMAQwBoAGkAbABkAE4AYQBtAGUAJwAsACAAJwBQAFMARAByAGkAdgBlACcALAAgACcAUABTAFAAcgBvAHYAaQBkAGUAcgAnACkAIAB7AAoAIAAgACAAIAAgACAAIAAgAGMAbwBuAHQAaQBuAHUAZQAKACAAIAAgACAAIAAgAH0ACgAKACAAIAAgACAAIAAgAGkAZgAgACgAJABwAHIAbwBwAC4AVgBhAGwAdQBlACAALQBpAHMAIABbAGIAeQB0AGUAWwBdAF0AKQAgAHsACgAgACAAIAAgACAAIAAgACAAUABhAHIAcwBlAC0AVQBzAGUAcgBBAHMAcwBpAHMAdABWAGEAbAB1AGUAIAAtAEUAbgBjAG8AZABlAGQATgBhAG0AZQAgACQAcAByAG8AcAAuAE4AYQBtAGUAIAAtAEIAeQB0AGUAcwAgACQAcAByAG8AcAAuAFYAYQBsAHUAZQAKACAAIAAgACAAIAAgAH0ACgAgACAAIAAgAH0ACgAgACAAfQAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AQQBwAHAARQB4AGUAYwB1AHQAYQBiAGwAZQBOAGEAbQBlAHMAIAB7AAoAIAAgAHAAYQByAGEAbQAoAFsAcwB0AHIAaQBuAGcAXQAkAEEAcABwAEkARAApAAoACgAgACAAJABtAGEAdABjAGgAZQBzACAAPQAgAFsAUgBlAGcAZQB4AF0AOgA6AE0AYQB0AGMAaABlAHMAKAAkAEEAcABwAEkARAAsACAAJwBbAF4AXABcAC8AIQAuAF0AKwBcAC4AZQB4AGUAJwAsACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBSAGUAZwB1AGwAYQByAEUAeABwAHIAZQBzAHMAaQBvAG4AcwAuAFIAZQBnAGUAeABPAHAAdABpAG8AbgBzAF0AOgA6AEkAZwBuAG8AcgBlAEMAYQBzAGUAKQAKACAAIABmAG8AcgBlAGEAYwBoACAAKAAkAG0AYQB0AGMAaAAgAGkAbgAgACQAbQBhAHQAYwBoAGUAcwApACAAewAKACAAIAAgACAAJABtAGEAdABjAGgALgBWAGEAbAB1AGUACgAgACAAfQAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUAByAG8AYwBlAHMAcwBLAGUAeQAgAHsACgAgACAAcABhAHIAYQBtACgAWwBzAHQAcgBpAG4AZwBdACQAVgBhAGwAdQBlACkACgAKACAAIAAkAHQAcgBpAG0AbQBlAGQAIAA9ACAAJABWAGEAbAB1AGUALgBUAHIAaQBtACgAKQAuAFQAcgBpAG0AKAAnACIAJwApAC4AVABvAEwAbwB3AGUAcgBJAG4AdgBhAHIAaQBhAG4AdAAoACkACgAgACAAaQBmACAAKAAkAHQAcgBpAG0AbQBlAGQALgBFAG4AZABzAFcAaQB0AGgAKAAnAC4AZQB4AGUAJwApACkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAdAByAGkAbQBtAGUAZAAuAFMAdQBiAHMAdAByAGkAbgBnACgAMAAsACAAJAB0AHIAaQBtAG0AZQBkAC4ATABlAG4AZwB0AGgAIAAtACAANAApAAoAIAAgAH0ACgAgACAAcgBlAHQAdQByAG4AIAAkAHQAcgBpAG0AbQBlAGQACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABHAGUAdAAtAFQAYQByAGcAZQB0AFAAcgBvAGMAZQBzAHMATgBhAG0AZQAgAHsACgAgACAAcABhAHIAYQBtACgAWwBzAHQAcgBpAG4AZwBdACQAQQBwAHAAKQAKAAoAIAAgACQAdAByAGkAbQBtAGUAZAAgAD0AIAAkAEEAcABwAC4AVAByAGkAbQAoACkALgBUAHIAaQBtACgAJwAiACcAKQAKACAAIABpAGYAIAAoACQAdAByAGkAbQBtAGUAZAAuAEwAZQBuAGcAdABoACAALQBlAHEAIAAwACkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAdAByAGkAbQBtAGUAZAAKACAAIAB9AAoACgAgACAAdAByAHkAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgAFsAUgBlAGcAZQB4AF0AOgA6AFIAZQBwAGwAYQBjAGUAKABbAEkATwAuAFAAYQB0AGgAXQA6ADoARwBlAHQARgBpAGwAZQBOAGEAbQBlACgAJAB0AHIAaQBtAG0AZQBkACkALAAgACcAXAAuAGUAeABlACQAJwAsACAAJwAnACwAIABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAFIAZQBnAHUAbABhAHIARQB4AHAAcgBlAHMAcwBpAG8AbgBzAC4AUgBlAGcAZQB4AE8AcAB0AGkAbwBuAHMAXQA6ADoASQBnAG4AbwByAGUAQwBhAHMAZQApAAoAIAAgAH0AIABjAGEAdABjAGgAIAB7AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgAFsAUgBlAGcAZQB4AF0AOgA6AFIAZQBwAGwAYQBjAGUAKAAkAHQAcgBpAG0AbQBlAGQALAAgACcAXAAuAGUAeABlACQAJwAsACAAJwAnACwAIABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAFIAZQBnAHUAbABhAHIARQB4AHAAcgBlAHMAcwBpAG8AbgBzAC4AUgBlAGcAZQB4AE8AcAB0AGkAbwBuAHMAXQA6ADoASQBnAG4AbwByAGUAQwBhAHMAZQApAAoAIAAgAH0ACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABOAGUAdwAtAFAAcgBvAGMAZQBzAHMAQQBwAHAASQBEACAAewAKACAAIABwAGEAcgBhAG0AKAAKACAAIAAgACAAWwBzAHQAcgBpAG4AZwBdACQAUAByAG8AYwBlAHMAcwBOAGEAbQBlACwACgAgACAAIAAgAFsAcwB0AHIAaQBuAGcAXQAkAFAAcgBvAGMAZQBzAHMAUABhAHQAaAAKACAAIAApAAoACgAgACAAaQBmACAAKAAkAFAAcgBvAGMAZQBzAHMAUABhAHQAaAAgAC0AYQBuAGQAIAAkAFAAcgBvAG",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "0ff6f2c94bc7e2833a5f7e16de1622e5dba70396f31c7d5f56381870317e8c46",
                                "action_process_instance_id": "Ad0O3ysthn8AAJOwAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "actor_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "actor_process_command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "actor_process_image_md5": "416d9334ffa3ba2c71c77e0f80a835d5",
                                "actor_process_image_name": "Codex.exe",
                                "actor_process_image_path": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "actor_process_image_sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c",
                                "actor_process_instance_id": "Ad0O156srsIAAEpEAAAAAA==",
                                "actor_process_os_pid": 19012,
                                "actor_process_signature_status": "Unsigned",
                                "actor_thread_thread_id": 27800,
                                "agent_host_boot_time": 1782367846903,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "causality_actor_process_command_line": "sihost.exe",
                                "causality_actor_process_execution_time": 1782389198003,
                                "causality_actor_process_image_md5": "af9ba4aa79ba3cdd28236a06d05b70d4",
                                "causality_actor_process_image_name": "sihost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\sihost.exe",
                                "causality_actor_process_image_sha256": "6e271366388fbc5a1e2e5204e7cf98557b44db2e9e34e1b6a7c8e7b80e14caab",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn0H0RhLsXu4wAHTN3Q==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783517934875,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "os_actor_process_command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "os_actor_process_image_name": "Codex.exe",
                                "os_actor_process_image_path": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "os_actor_process_image_sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c",
                                "os_actor_process_instance_id": "Ad0O156srsIAAEpEAAAAAA==",
                                "os_actor_process_os_pid": 19012,
                                "os_actor_process_signature_status": "Unsigned",
                                "os_actor_thread_thread_id": 27800,
                                "user_name": "TECHNOMA\\aracelymartinez"
                            }
                        ],
                        "external_id": "c8f8f7c0-61fe-47bd-9c74-3545beb473c5",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.64"
                        ],
                        "host_name": "NB-AMARTINEZ",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783518224461,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "5daf5724-8e0a-4514-85d4-431bf4b193be",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0002 - Execution"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1059.001 - Command and Scripting Interpreter: PowerShell"
                        ],
                        "name": "PowerShell runs suspicious base64-encoded commands",
                        "original_tags": [
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "0ff6f2c94bc7e2833a5f7e16de1622e5dba70396f31c7d5f56381870317e8c46"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "executable": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "hash": {
                                    "md5": "416d9334ffa3ba2c71c77e0f80a835d5",
                                    "sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c"
                                },
                                "name": "Codex.exe",
                                "pid": 19012
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 110189,
                        "status": "New"
                    },
                    "stellar_da_input": 14269,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "aa6b7b39-eb0c-420b-a2fb-3e388e2c2d9d1783518431058-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783517934875,
                    "timestamp_utc": "2026-07-08T13:38:54.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\aracelymartinez"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783518431058,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-AMARTINEZ\" (\"192.168.169.64\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\aracelymartinez\". Analytics details: \"The process Codex.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): PowerShell runs suspicious base64-encoded commands",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-powershell_runs_suspicious_base64_encoded_commands",
                        "scope": "",
                        "tactic": {
                            "id": "TA0002",
                            "name": "Execution"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1059",
                            "name": "Command and Scripting Interpreter",
                            "subtechnique": {
                                "id": "T1059.001",
                                "name": "PowerShell"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0002",
                                    "name": "Execution"
                                },
                                "technique": {
                                    "id": "T1059",
                                    "name": "Command and Scripting Interpreter",
                                    "subtechnique": {
                                        "id": "T1059.001",
                                        "name": "PowerShell"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            },
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "6c0fb2f5-e6de-44ac-a70f-40cc7ea2a3751783523195633-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 4994,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "XMVDQp8BBi0xHyA-PQnR",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128182"
                    ],
                    "dms_job_id": "palo_alto_cortex_xdr_analytics_bioc",
                    "dscp_name": "Best Effort",
                    "engid": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "engid_gateway": "",
                    "engid_name": "palo_alto_networks_cortex_CORTEX-XDR-V1",
                    "event": {
                        "severity_str": "low",
                        "threat": {
                            "name": "PowerShell runs suspicious base64-encoded commands"
                        }
                    },
                    "event_score": 35,
                    "event_source": "palo_alto_cortex_xdr",
                    "event_status": "New",
                    "fidelity": 35,
                    "host": {
                        "ip": "192.168.169.64",
                        "name": "NB-AMARTINEZ"
                    },
                    "locid": "unassigned location",
                    "msg_class": "palo_alto_networks_cortex_xdr_alerts",
                    "msg_origin": {
                        "category": "threat_intel",
                        "processor": {
                            "id": "6939ef90a77d64c0b0abb567",
                            "name": "palo_alto_networks_cortex_xdr",
                            "type": "log_collector"
                        },
                        "source": "palo_alto_networks_cortex_xdr",
                        "vendor": "palo_alto_networks"
                    },
                    "msgtype_name": "start",
                    "netid": 0,
                    "netid_name": "vlannull",
                    "org_id": "cf73a415c8794884a0c35b458b7c73ae",
                    "orig_id": "XMVDQp8BBi0xHyA-PQnR",
                    "orig_index": "aella-syslog-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.5.0.624",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128182",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process Codex.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days",
                        "detection_timestamp": 1783522789179,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "8be0647c97e049e9968470c010f4d0ef",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "action_process_image_command_line": "powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand CgAkAEUAcgByAG8AcgBBAGMAdABpAG8AbgBQAHIAZQBmAGUAcgBlAG4AYwBlACAAPQAgACIAUwB0AG8AcAAiAAoAJABQAHIAbwBnAHIAZQBzAHMAUAByAGUAZgBlAHIAZQBuAGMAZQAgAD0AIAAiAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUAIgAKAAoAJABjAG8AZABlACAAPQAgAEAAIgAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAFIAdQBuAHQAaQBtAGUALgBJAG4AdABlAHIAbwBwAFMAZQByAHYAaQBjAGUAcwA7AAoACgBbAFMAdAByAHUAYwB0AEwAYQB5AG8AdQB0ACgATABhAHkAbwB1AHQASwBpAG4AZAAuAFMAZQBxAHUAZQBuAHQAaQBhAGwAKQBdAAoAcAB1AGIAbABpAGMAIABzAHQAcgB1AGMAdAAgAFMASQBaAEUAIAB7AAoAIAAgAHAAdQBiAGwAaQBjACAAaQBuAHQAIABjAHgAOwAKACAAIABwAHUAYgBsAGkAYwAgAGkAbgB0ACAAYwB5ADsACgAgACAAcAB1AGIAbABpAGMAIABTAEkAWgBFACgAaQBuAHQAIAB4ACwAIABpAG4AdAAgAHkAKQAgAHsAIABjAHgAIAA9ACAAeAA7ACAAYwB5ACAAPQAgAHkAOwAgAH0ACgB9AAoACgBbAFMAdAByAHUAYwB0AEwAYQB5AG8AdQB0ACgATABhAHkAbwB1AHQASwBpAG4AZAAuAFMAZQBxAHUAZQBuAHQAaQBhAGwAKQBdAAoAcAB1AGIAbABpAGMAIABzAHQAcgB1AGMAdAAgAEIASQBUAE0AQQBQAEkATgBGAE8ASABFAEEARABFAFIAIAB7AAoAIAAgAHAAdQBiAGwAaQBjACAAdQBpAG4AdAAgAGIAaQBTAGkAegBlADsACgAgACAAcAB1AGIAbABpAGMAIABpAG4AdAAgAGIAaQBXAGkAZAB0AGgAOwAKACAAIABwAHUAYgBsAGkAYwAgAGkAbgB0ACAAYgBpAEgAZQBpAGcAaAB0ADsACgAgACAAcAB1AGIAbABpAGMAIAB1AHMAaABvAHIAdAAgAGIAaQBQAGwAYQBuAGUAcwA7AAoAIAAgAHAAdQBiAGwAaQBjACAAdQBzAGgAbwByAHQAIABiAGkAQgBpAHQAQwBvAHUAbgB0ADsACgAgACAAcAB1AGIAbABpAGMAIAB1AGkAbgB0ACAAYgBpAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgA7AAoAIAAgAHAAdQBiAGwAaQBjACAAdQBpAG4AdAAgAGIAaQBTAGkAegBlAEkAbQBhAGcAZQA7AAoAIAAgAHAAdQBiAGwAaQBjACAAaQBuAHQAIABiAGkAWABQAGUAbABzAFAAZQByAE0AZQB0AGUAcgA7AAoAIAAgAHAAdQBiAGwAaQBjACAAaQBuAHQAIABiAGkAWQBQAGUAbABzAFAAZQByAE0AZQB0AGUAcgA7AAoAIAAgAHAAdQBiAGwAaQBjACAAdQBpAG4AdAAgAGIAaQBDAGwAcgBVAHMAZQBkADsACgAgACAAcAB1AGIAbABpAGMAIAB1AGkAbgB0ACAAYgBpAEMAbAByAEkAbQBwAG8AcgB0AGEAbgB0ADsACgB9AAoACgBbAFMAdAByAHUAYwB0AEwAYQB5AG8AdQB0ACgATABhAHkAbwB1AHQASwBpAG4AZAAuAFMAZQBxAHUAZQBuAHQAaQBhAGwAKQBdAAoAcAB1AGIAbABpAGMAIABzAHQAcgB1AGMAdAAgAEIASQBUAE0AQQBQAEkATgBGAE8AIAB7AAoAIAAgAHAAdQBiAGwAaQBjACAAQgBJAFQATQBBAFAASQBOAEYATwBIAEUAQQBEAEUAUgAgAGIAbQBpAEgAZQBhAGQAZQByADsACgAgACAAcAB1AGIAbABpAGMAIAB1AGkAbgB0ACAAYgBtAGkAQwBvAGwAbwByAHMAOwAKAH0ACgAKAFsAQwBvAG0ASQBtAHAAbwByAHQAXQAKAFsASQBuAHQAZQByAGYAYQBjAGUAVAB5AHAAZQAoAEMAbwBtAEkAbgB0AGUAcgBmAGEAYwBlAFQAeQBwAGUALgBJAG4AdABlAHIAZgBhAGMAZQBJAHMASQBVAG4AawBuAG8AdwBuACkAXQAKAFsARwB1AGkAZAAoACIAYgBjAGMAMQA4AGIANwA5AC0AYgBhADEANgAtADQANAAyAGYALQA4ADAAYwA0AC0AOABhADUAOQBjADMAMABjADQANgAzAGIAIgApAF0ACgBwAHUAYgBsAGkAYwAgAGkAbgB0AGUAcgBmAGEAYwBlACAASQBTAGgAZQBsAGwASQB0AGUAbQBJAG0AYQBnAGUARgBhAGMAdABvAHIAeQAgAHsACgAgACAAdgBvAGkAZAAgAEcAZQB0AEkAbQBhAGcAZQAoAFMASQBaAEUAIABzAGkAegBlACwAIABpAG4AdAAgAGYAbABhAGcAcwAsACAAbwB1AHQAIABJAG4AdABQAHQAcgAgAHAAaABiAG0AKQA7AAoAfQAKAAoAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAGMAbABhAHMAcwAgAEMAbwBkAGUAeABTAGgAZQBsAGwASQBjAG8AbgBOAGEAdABpAHYAZQAgAHsACgAgACAAYwBvAG4AcwB0ACAAaQBuAHQAIABCAEkAXwBSAEcAQgAgAD0AIAAwADsACgAgACAAYwBvAG4AcwB0ACAAaQBuAHQAIABEAEkAQgBfAFIARwBCAF8AQwBPAEwATwBSAFMAIAA9ACAAMAA7AAoAIAAgAGMAbwBuAHMAdAAgAGkAbgB0ACAASQBDAE8ATgBfAE8ATgBMAFkAIAA9ACAANAA7AAoACgAgACAAWwBEAGwAbABJAG0AcABvAHIAdAAoACIAcwBoAGUAbABsADMAMgAuAGQAbABsACIALAAgAEMAaABhAHIAUwBlAHQAIAA9ACAAQwBoAGEAcgBTAGUAdAAuAFUAbgBpAGMAbwBkAGUALAAgAFAAcgBlAHMAZQByAHYAZQBTAGkAZwAgAD0AIABmAGEAbABzAGUAKQBdAAoAIAAgAHAAdQBiAGwAaQBjACAAcwB0AGEAdABpAGMAIABlAHgAdABlAHIAbgAgAHYAbwBpAGQAIABTAEgAQwByAGUAYQB0AGUASQB0AGUAbQBGAHIAbwBtAFAAYQByAHMAaQBuAGcATgBhAG0AZQAoAAoAIAAgACAAIABzAHQAcgBpAG4AZwAgAHAAcwB6AFAAYQB0AGgALAAKACAAIAAgACAASQBuAHQAUAB0AHIAIABwAGIAYwAsAAoAIAAgACAAIAByAGUAZgAgAEcAdQBpAGQAIAByAGkAaQBkACwACgAgACAAIAAgAFsATQBhAHIAcwBoAGEAbABBAHMAKABVAG4AbQBhAG4AYQBnAGUAZABUAHkAcABlAC4ASQBuAHQAZQByAGYAYQBjAGUAKQBdACAAbwB1AHQAIABJAFMAaABlAGwAbABJAHQAZQBtAEkAbQBhAGcAZQBGAGEAYwB0AG8AcgB5ACAAcABwAHYACgAgACAAKQA7AAoACgAgACAAWwBEAGwAbABJAG0AcABvAHIAdAAoACIAZwBkAGkAMwAyAC4AZABsAGwAIgApAF0ACgAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAGUAeAB0AGUAcgBuACAAYgBvAG8AbAAgAEQAZQBsAGUAdABlAE8AYgBqAGUAYwB0ACgASQBuAHQAUAB0AHIAIABoAE8AYgBqAGUAYwB0ACkAOwAKAAoAIAAgAFsARABsAGwASQBtAHAAbwByAHQAKAAiAGcAZABpADMAMgAuAGQAbABsACIAKQBdAAoAIAAgAHMAdABhAHQAaQBjACAAZQB4AHQAZQByAG4AIABpAG4AdAAgAEcAZQB0AEQASQBCAGkAdABzACgACgAgACAAIAAgAEkAbgB0AFAAdAByACAAaABkAGMALAAKACAAIAAgACAASQBuAHQAUAB0AHIAIABoAGIAbQBwACwACgAgACAAIAAgAHUAaQBuAHQAIAB1AFMAdABhAHIAdABTAGMAYQBuACwACgAgACAAIAAgAHUAaQBuAHQAIABjAFMAYwBhAG4ATABpAG4AZQBzACwACgAgACAAIAAgAGIAeQB0AGUAWwBdACAAbABwAHYAQgBpAHQAcwAsAAoAIAAgACAAIAByAGUAZgAgAEIASQBUAE0AQQBQAEkATgBGAE8AIABsAHAAYgBpACwACgAgACAAIAAgAHUAaQBuAHQAIAB1AFUAcwBhAGcAZQAKACAAIAApADsACgAKACAAIABbAEQAbABsAEkAbQBwAG8AcgB0ACgAIgB1AHMAZQByADMAMgAuAGQAbABsACIAKQBdAAoAIAAgAHMAdABhAHQAaQBjACAAZQB4AHQAZQByAG4AIABJAG4AdABQAHQAcgAgAEcAZQB0AEQAQwAoAEkAbgB0AFAAdAByACAAaABXAG4AZAApADsACgAKACAAIABbAEQAbABsAEkAbQBwAG8AcgB0ACgAIgB1AHMAZQByADMAMgAuAGQAbABsACIAKQBdAAoAIAAgAHMAdABhAHQAaQBjACAAZQB4AHQAZQByAG4AIABpAG4AdAAgAFIAZQBsAGUAYQBzAGUARABDACgASQBuAHQAUAB0AHIAIABoAFcAbgBkACwAIABJAG4AdABQAHQAcgAgAGgARABDACkAOwAKAAoAIAAgAHAAdQBiAGwAaQBjACAAcwB0AGEAdABpAGMAIABzAHQAcgBpAG4AZwAgAEcAZQB0AEEAcABwAHMARgBvAGwAZABlAHIASQBjAG8AbgBEAGEAdABhAFUAcgBsACgAcwB0AHIAaQBuAGcAIABhAHAAcABJAGQAKQAgAHsACgAgACAAIAAgAEcAdQBpAGQAIABpAGkAZAAgAD0AIABuAGUAdwAgAEcAdQBpAGQAKAAiAGIAYwBjADEAOABiADcAOQAtAGIAYQAxADYALQA0ADQAMgBmAC0AOAAwAGMANAAtADgAYQA1ADkAYwAzADAAYwA0ADYAMwBiACIAKQA7AAoAIAAgACAAIABJAFMAaABlAGwAbABJAHQAZQBtAEkAbQBhAGcAZQBGAGEAYwB0AG8AcgB5ACAAZgBhAGMAdABvAHIAeQA7AAoAIAAgACAAIABTAEgAQwByAGUAYQB0AGUASQB0AGUAbQBGAHIAbwBtAFAAYQByAHMAaQBuAGcATgBhAG0AZQAoACIAcwBoAGUAbABsADoAQQBwAHAAcwBGAG8AbABkAGUAcgBcAFwAIgAgACsAIABhAHAAcABJAGQALAAgAEkAbgB0AFAAdAByAC4AWgBlAHIAbwAsACAAcgBlAGYAIABpAGkAZAAsACAAbwB1AHQAIABmAGEAYwB0AG8AcgB5ACkAOwAKAAoAIAAgACAAIABJAG4AdABQAHQAcgAgAGgAYgBpAHQAbQBhAHAAOwAKACAAIAAgACAAZgBhAGMAdABvAHIAeQAuAEcAZQB0AEkAbQBhAGcAZQAoAG4AZQB3ACAAUwBJAFoARQAoADMAMgAsACAAMwAyACkALAAgAEkAQwBPAE4AXwBPAE4ATABZACwAIABvAHUAdAAgAGgAYgBpAHQAbQBhAHAAKQA7AAoAIAAgACAAIAB0AHIAeQAgAHsACgAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAHYAYQByACAAYgBpAHQAbQBhAHAAIAA9ACAAQgBpAHQAbQBhAHAARgByAG8AbQBIAEIAaQB0AG0AYQBwAFAAcgBlAHMAZQByAHYAZQBBAGwAcABoAGEAKABoAGIAaQB0AG0AYQBwACwAIAAzADIALAAgADMAMgApACkACgAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAHYAYQByACAAcwB0AHIAZQBhAG0AIAA9ACAAbgBlAHcAIABTAHkAcwB0AGUAbQAuAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACgAKQApACAAewAKACAAIAAgACAAIAAgACAAIABiAGkAdABtAGEAcAAuAFMAYQB2AGUAKABzAHQAcgBlAGEAbQAsACAAUwB5AHMAdABlAG0ALgBEAHIAYQB3AGkAbgBnAC4ASQBtAGEAZwBpAG4AZwAuAEkAbQBhAGcAZQBGAG8AcgBtAGEAdAAuAFAAbgBnACkAOwAKACAAIAAgACAAIAAgACAAIAByAGUAdAB1AHIAbgAgACIAZABhAHQAYQA6AGkAbQBhAGcAZQAvAHAAbgBnADsAYgBhAHMAZQA2ADQALAAiACAAKwAgAEMAbwBuAHYAZQByAHQALgBUAG8AQgBhAHMAZQA2ADQAUwB0AHIAaQBuAGcAKABzAHQAcgBlAGEAbQAuAFQAbwBBAHIAcgBhAHkAKAApACkAOwAKACAAIAAgACAAIAAgAH0ACgAgACAAIAAgAH0AIABmAGkAbgBhAGwAbAB5ACAAewAKACAAIAAgACAAIAAgAEQAZQBsAGUAdABlAE8AYgBqAGUAYwB0ACgAaABiAGkAdABtAGEAcAApADsACgAgACAAIAAgAH0ACgAgACAAfQAKAAoAIAAgAHMAdABhAHQAaQBjACAAUwB5AHMAdABlAG0ALgBEAHIAYQB3AGkAbgBnAC4AQgBpAHQAbQBhAHAAIABCAGkAdABtAGEAcABGAHIAbwBtAEgAQgBpAHQAbQBhAHAAUAByAGUAcwBlAHIAdgBlAEEAbABwAGgAYQAoAEkAbgB0AFAAdAByACAAaABiAGkAdABtAGEAcAAsACAAaQBuAHQAIAB3AGkAZAB0AGgALAAgAGkAbgB0ACAAaABlAGkAZwBoAHQAKQAgAHsACgAgACAAIAAgAHYAYQByACAAaQBuAGYAbwAgAD0AIABuAGUAdwAgAEIASQBUAE0AQQBQAEkATgBGAE8AKAApADsACgAgACAAIAAgAGkAbgBmAG8ALgBiAG0AaQBIAGUAYQBkAGUAcgAuAGIAaQBTAGkAegBlACAAPQAgACgAdQBpAG4AdAApAE0AYQByAHMAaABhAGwALgBTAGkAegBlAE8AZgAoAHQAeQBwAGUAbwBmACgAQgBJAFQATQBBAFAASQBOAEYATwBIAEUAQQBEAEUAUgApACkAOwAKACAAIAAgACAAaQBuAGYAbwAuAGIAbQBpAEgAZQBhAGQAZQByAC4AYgBpAFcAaQBkAHQAaAAgAD0AIAB3AGkAZAB0AGgAOwAKACAAIAAgACAAaQBuAGYAbwAuAGIAbQBpAEgAZQBhAGQAZQByAC4AYgBpAEgAZQBpAGcAaAB0ACAAPQAgAC0AaABlAGkAZwBoAHQAOwAKACAAIAAgACAAaQBuAGYAbwAuAGIAbQBpAEgAZQBhAGQAZQByAC4AYgBpAFAAbABhAG4AZQBzACAAPQAgADEAOwAKACAAIAAgACAAaQBuAGYAbwAuAGIAbQBpAEgAZQBhAGQAZQByAC4AYgBpAEIAaQB0AEMAbwB1AG4AdAAgAD0AIAAzADIAOwAKACAAIAAgACAAaQBuAGYAbwAuAGIAbQBpAEgAZQBhAGQAZQByAC4AYgBpAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAgAD0AIABCAEkAXwBSAEcAQgA7AAoAIAAgACAAIABpAG4AZgBvAC4AYgBtAGkASABlAGEAZABlAHIALgBiAGkAUwBpAHoAZQBJAG0AYQBnAGUAIAA9ACAAKAB1AGkAbgB0ACkAKAB3AGkAZAB0AGgAIAAqACAAaABlAGkAZwBoAHQAIAAqACAANAApADsACgAKACAAIAAgACAAYgB5AHQAZQBbAF0AIABwAGkAeABlAGwAcwAgAD0AIABuAGUAdwAgAGIAeQB0AGUAWwB3AGkAZAB0AGgAIAAqACAAaABlAGkAZwBoAH",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "0ff6f2c94bc7e2833a5f7e16de1622e5dba70396f31c7d5f56381870317e8c46",
                                "action_process_instance_id": "Ad0O6nidI0gAAHWwAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "actor_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "actor_process_command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "actor_process_image_md5": "416d9334ffa3ba2c71c77e0f80a835d5",
                                "actor_process_image_name": "Codex.exe",
                                "actor_process_image_path": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "actor_process_image_sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c",
                                "actor_process_instance_id": "Ad0O156srsIAAEpEAAAAAA==",
                                "actor_process_os_pid": 19012,
                                "actor_process_signature_status": "Unsigned",
                                "actor_thread_thread_id": 34064,
                                "agent_host_boot_time": 1782367846903,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "causality_actor_process_command_line": "sihost.exe",
                                "causality_actor_process_execution_time": 1782389198003,
                                "causality_actor_process_image_md5": "af9ba4aa79ba3cdd28236a06d05b70d4",
                                "causality_actor_process_image_name": "sihost.exe",
                                "causality_actor_process_image_path": "C:\\Windows\\System32\\sihost.exe",
                                "causality_actor_process_image_sha256": "6e271366388fbc5a1e2e5204e7cf98557b44db2e9e34e1b6a7c8e7b80e14caab",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn0I+WIPsXu4wAIF6hQ==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783522789179,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0EmxLX0hMAAAnwAAAAAA==",
                                "os_actor_process_command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "os_actor_process_image_name": "Codex.exe",
                                "os_actor_process_image_path": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "os_actor_process_image_sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c",
                                "os_actor_process_instance_id": "Ad0O156srsIAAEpEAAAAAA==",
                                "os_actor_process_os_pid": 19012,
                                "os_actor_process_signature_status": "Unsigned",
                                "os_actor_thread_thread_id": 34064,
                                "user_name": "TECHNOMA\\aracelymartinez"
                            }
                        ],
                        "external_id": "061406f4-290d-4043-806b-554525052fd4",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.64"
                        ],
                        "host_name": "NB-AMARTINEZ",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783522998681,
                        "mac": null,
                        "mac_addresses": null,
                        "malicious_urls": null,
                        "matching_service_rule_id": "5daf5724-8e0a-4514-85d4-431bf4b193be",
                        "matching_status": "MATCHED",
                        "mitre_tactic_id_and_name": [
                            "TA0002 - Execution"
                        ],
                        "mitre_technique_id_and_name": [
                            "T1059.001 - Command and Scripting Interpreter: PowerShell"
                        ],
                        "name": "PowerShell runs suspicious base64-encoded commands",
                        "original_tags": [
                            "DOM:Security",
                            "DS:PANW/XDR Agent"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "0ff6f2c94bc7e2833a5f7e16de1622e5dba70396f31c7d5f56381870317e8c46"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "\"C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe\" ",
                                "executable": "C:\\Program Files\\WindowsApps\\OpenAI.Codex_26.623.19656.0_x64__2p2nqsd0c76g0\\app\\Codex.exe",
                                "hash": {
                                    "md5": "416d9334ffa3ba2c71c77e0f80a835d5",
                                    "sha256": "86348eadb6e3a62383c13bec91d826d80d5dabc5147e17cf33f748d6c293aa0c"
                                },
                                "name": "Codex.exe",
                                "pid": 19012
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 64871,
                        "status": "New"
                    },
                    "stellar_da_input": 14269,
                    "stellar_index_id": "aella-ser-2026.07.08-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "6c0fb2f5-e6de-44ac-a70f-40cc7ea2a3751783523195633-YWVsbGEtc2VyLTIwMjYuMDcuMDgtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783522789179,
                    "timestamp_utc": "2026-07-08T14:59:49.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\aracelymartinez"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783523195632,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-AMARTINEZ\" (\"192.168.169.64\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\aracelymartinez\". Analytics details: \"The process Codex.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
                        "display_name": "Palo Alto Networks Cortex XDR (XDR Analytics BIOC): PowerShell runs suspicious base64-encoded commands",
                        "framework_version": "v13",
                        "name": "palo_alto_networks_cortex_xdr_xdr_analytics_bioc-powershell_runs_suspicious_base64_encoded_commands",
                        "scope": "",
                        "tactic": {
                            "id": "TA0002",
                            "name": "Execution"
                        },
                        "tags": [
                            "Palo Alto Networks"
                        ],
                        "technique": {
                            "id": "T1059",
                            "name": "Command and Scripting Interpreter",
                            "subtechnique": {
                                "id": "T1059.001",
                                "name": "PowerShell"
                            }
                        },
                        "ttps": [
                            {
                                "tactic": {
                                    "id": "TA0002",
                                    "name": "Execution"
                                },
                                "technique": {
                                    "id": "T1059",
                                    "name": "Command and Scripting Interpreter",
                                    "subtechnique": {
                                        "id": "T1059.001",
                                        "name": "PowerShell"
                                    }
                                }
                            }
                        ],
                        "xdr_killchain_stage": "Persistent Foothold",
                        "xdr_killchain_version": "v1"
                    }
                }
            }
        ]
    }
}