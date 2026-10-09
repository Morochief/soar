=========================================================================
  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW
=========================================================================

{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.07.04-000028",
                "_type": "_doc",
                "_id": "132bc225-42fa-4b62-8a73-370622069f951783607289882-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6925,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "YBZFR58BBi0xHyA-cLTJ",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128396"
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
                        "ip": "192.168.169.89",
                        "name": "NB-JTORALES"
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
                    "orig_id": "YBZFR58BBi0xHyA-cLTJ",
                    "orig_index": "aella-syslog-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128396",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days",
                        "detection_timestamp": 1783606681475,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "ca9e9da710e240e89b3a64013cd02710",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBjAEcAOQAzAFoAWABKAHoAYQBHAFYAcwBiAEMAQQB0AFIAWABoAGwAWQAzAFYAMABhAFcAOQB1AFUARwA5AHMAYQBXAE4ANQBJAEUASgA1AGMARwBGAHoAYwB5AEEAdABSAG0AbABzAFoAUwBBAGkAUQB6AHAAYwBWAFgATgBsAGMAbgBOAGMAUwBrADkAVABSAFYAUgBQAGYAagBGAGMAUQBYAEIAdwBSAEcARgAwAFkAVgB4AE0AYgAyAE4AaABiAEYAeABVAFoAVwAxAHcAWABHAE4AcwBZAFgAVgBrAFoAVgB4AGoATABTADEAVgBjADIAVgB5AGMAeQAxAHEAYgAzAE4AbABkAEcAOQB5AFkAVwB4AGwAYwB5ADEARQBiADIATgAxAGIAVwBWAHUAZABIAE0AdABRADIAOQBrAFoAWABnAHQATQBqAEEAeQBOAGkAMAB3AE4AUwAwAHcATgBTADEAMABaAFMAMQB3AGQAVwBWAGsAWgBYAE0AdABZADIAOQB1AFoAVwBOADAAWQBYAEkAdABZAFcAdwB0AGMARwA5ADMAWgBYAEkAdABZAG0AbABjAE0ARABRADIATQAyAEkAeQBOAG0AVQB0AE4AagBkAGwATgBDADAAMABOAEcARgBrAEwAVwBFADAATQBXAFkAdABZAGoAbABrAFkAagBNAHkAWgBUAFIAawBNAFQAQQB5AFgASABOAGoAYwBtAEYAMABZADIAaAB3AFkAVwBSAGMAWQAyADkAdQBaAFcATgAwAFkAWABKAGYAYwBHADkAMwBaAFgASgBpAGEAUwA1AHcAYwB6AEUAaQAnAAoACgBpAGYAIAAoAC0AbgBvAHQAIAAkAEUAbgBjAG8AZABlAGQAQwBvAG0AbQBhAG4AZAApACAAewAKACAAIAAgACAAVwByAGkAdABlAC0ATwB1AHQAcAB1AHQAIAAnAHsAIgB2AGEAbABpAGQAIgA6AGYAYQBsAHMAZQAsACIAZQByAHIAbwByAHMAIgA6AFsAewAiAG0AZQBzAHMAYQBnAGUAIgA6ACIATgBvACAAYwBvAG0AbQBhAG4AZAAgAHAAcgBvAHYAaQBkAGUAZAAiACwAIgBlAHIAcgBvAHIASQBkACIAOgAiAE4AbwBJAG4AcAB1AHQAIgB9AF0ALAAiAHMAdABhAHQAZQBtAGUAbgB0AHMAIgA6AFsAXQAsACIAdgBhAHIAaQBhAGIAbABlAHMAIgA6AFsAXQAsACIAaABhAHMAUwB0AG8AcABQAGEAcgBzAGkAbgBnACIAOgBmAGEAbABzAGUALAAiAG8AcgBpAGcAaQBuAGEAbABDAG8AbQBtAGEAbgBkACIAOgAiACIAfQAnAAoAIAAgACAAIABlAHgAaQB0ACAAMAAKAH0ACgAKACQAQwBvAG0AbQBhAG4AZAAgAD0AIABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAUwB0AHIAaQBuAGcAKABbAFMAeQBzAHQAZQBtAC4AQwBvAG4AdgBlAHIAdABdADoAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgAJABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAKQApAAoACgAkAHQAbwBrAGUAbgBzACAAPQAgACQAbgB1AGwAbAAKACQAcABhAHIAcwBlAEUAcgByAG8AcgBzACAAPQAgACQAbgB1AGwAbAAKACQAYQBzAHQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AUABhAHIAcwBlAHIAXQA6ADoAUABhAHIAcwBlAEkAbgBwAHUAdAAoAAoAIAAgACAAIAAkAEMAbwBtAG0AYQBuAGQALAAKACAAIAAgACAAWwByAGUAZgBdACQAdABvAGsAZQBuAHMALAAKACAAIAAgACAAWwByAGUAZgBdACQAcABhAHIAcwBlAEUAcgByAG8AcgBzAAoAKQAKAAoAJABhAGwAbABWAGEAcgBpAGEAYgBsAGUAcwAgAD0AIABbAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4AQQByAHIAYQB5AEwAaQBzAHQAXQA6ADoAbgBlAHcAKAApAAoACgBmAHUAbgBjAHQAaQBvAG4AIABHAGUAdAAtAFIAYQB3AEMAbwBtAG0AYQBuAGQARQBsAGUAbQBlAG4AdABzACAAewAKACAAIAAgACAAcABhAHIAYQBtACgAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQwBvAG0AbQBhAG4AZABBAHMAdABdACQAQwBtAGQAQQBzAHQAKQAKACAAIAAgACAAJABlAGwAZQBtAHMAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJABjAGUAIABpAG4AIAAkAEMAbQBkAEEAcwB0AC4AQwBvAG0AbQBhAG4AZABFAGwAZQBtAGUAbgB0AHMAKQAgAHsACgAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAgAD0AIABAAHsAIAB0AHkAcABlACAAPQAgACQAYwBlAC4ARwBlAHQAVAB5AHAAZQAoACkALgBOAGEAbQBlADsAIAB0AGUAeAB0ACAAPQAgACQAYwBlAC4ARQB4AHQAZQBuAHQALgBUAGUAeAB0ACAAfQAKACAAIAAgACAAIAAgACAAIABpAGYAIAAoACQAYwBlAC4AUABTAE8AYgBqAGUAYwB0AC4AUAByAG8AcABlAHIAdABpAGUAcwBbACcAVgBhAGwAdQBlACcAXQAgAC0AYQBuAGQAIAAkAG4AdQBsAGwAIAAtAG4AZQAgACQAYwBlAC4AVgBhAGwAdQBlACAALQBhAG4AZAAgACQAYwBlAC4AVgBhAGwAdQBlACAALQBpAHMAIABbAHMAdAByAGkAbgBnAF0AKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGMAZQBEAGEAdABhAC4AdgBhAGwAdQBlACAAPQAgACQAYwBlAC4AVgBhAGwAdQBlAAoAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGMAZQAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQwBvAG0AbQBhAG4AZABFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGMAZQBEAGEAdABhAC4AZQB4AHAAcgBlAHMAcwBpAG8AbgBUAHkAcABlACAAPQAgACQAYwBlAC4ARQB4AHAAcgBlAHMAcwBpAG8AbgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgACQAYQA9ACQAYwBlAC4AQQByAGcAdQBtAGUAbgB0ADsAaQBmACgAJABhACkAewAkAGMAZQBEAGEAdABhAC4AYwBoAGkAbABkAHIAZQBuAD0AQAAoAEAAewB0AHkAcABlAD0AJABhAC4ARwBlAHQAVAB5AHAAZQAoACkALgBOAGEAbQBlADsAdABlAHgAdAA9ACQAYQAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAB9ACkAfQAKACAAIAAgACAAIAAgACAAIABbAHYAbwBpAGQAXQAkAGUAbABlAG0AcwAuAEEAZABkACgAJABjAGUARABhAHQAYQApAAoAIAAgACAAIAB9AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAZQBsAGUAbQBzAAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBSAGEAdwBSAGUAZABpAHIAZQBjAHQAaQBvAG4AcwAgAHsACgAgACAAIAAgAHAAYQByAGEAbQAoACQAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAKQAKACAAIAAgACAAJAByAGUAcwB1AGwAdAAgAD0AIABbAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4AQQByAHIAYQB5AEwAaQBzAHQAXQA6ADoAbgBlAHcAKAApAAoAIAAgACAAIABmAG8AcgBlAGEAYwBoACAAKAAkAHIAZQBkAGkAcgAgAGkAbgAgACQAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAKQAgAHsACgAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAgAD0AIABAAHsAIAB0AHkAcABlACAAPQAgACQAcgBlAGQAaQByAC4ARwBlAHQAVAB5AHAAZQAoACkALgBOAGEAbQBlACAAfQAKACAAIAAgACAAIAAgACAAIABpAGYAIAAoACQAcgBlAGQAaQByACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBGAGkAbABlAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBBAHMAdABdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGEAcABwAGUAbgBkACAAPQAgAFsAYgBvAG8AbABdACQAcgBlAGQAaQByAC4AQQBwAHAAZQBuAGQACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHIAZQBkAGkAcgBEAGEAdABhAC4AZgByAG8AbQBTAHQAcgBlAGEAbQAgAD0AIAAkAHIAZQBkAGkAcgAuAEYAcgBvAG0AUwB0AHIAZQBhAG0ALgBUAG8AUwB0AHIAaQBuAGcAKAApAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGwAbwBjAGEAdABpAG8AbgBUAGUAeAB0ACAAPQAgACQAcgBlAGQAaQByAC4ATABvAGMAYQB0AGkAbwBuAC4ARQB4AHQAZQBuAHQALgBUAGUAeAB0AAoAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAWwB2AG8AaQBkAF0AJAByAGUAcwB1AGwAdAAuAEEAZABkACgAJAByAGUAZABpAHIARABhAHQAYQApAAoAIAAgACAAIAB9AAoAIAAgACAAIAByAGUAdAB1AHIAbgAgACQAcgBlAHMAdQBsAHQACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABHAGUAdAAtAFMAZQBjAHUAcgBpAHQAeQBQAGEAdAB0AGUAcgBuAHMAKAAkAEEAKQAgAHsACgAgACAAIAAgACQAcAAgAD0AIABAAHsAfQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJABuACAAaQBuACAAJABBAC4ARgBpAG4AZABBAGwAbAAoAHsAIABwAGEAcgBhAG0AKAAkAHgAKQAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACAALQBvAHIACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBBAHIAcgBhAHkARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACAALQBvAHIACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBFAHgAcABhAG4AZABhAGIAbABlAFMAdAByAGkAbgBnAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AUABhAHIAZQBuAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAKACAAIAAgACAAfQAsACAAJAB0AHIAdQBlACkAKQAgAHsAIABzAHcAaQB0AGMAaAAgACgAJABuAC4ARwBlAHQAVAB5AHAAZQAoACkALgBOAGEAbQBlACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACcASQBuAHYAbwBrAGUATQBlAG0AYgBlAHIARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdAAnACAAewAgACQAcAAuAGgAYQBzAE0AZQBtAGIAZQByAEkAbgB2AG8AYwBhAHQAaQBvAG4AcwAgAD0AIAAkAHQAcgB1AGUAIAB9AAoAIAAgACAAIAAgACAAIAAgACcATQBlAG0AYgBlAHIARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdAAnACAAewAgACQAcAAuAGgAYQBzAE0AZQBtAGIAZQByAEkAbgB2AG8AYwBhAHQAaQBvAG4AcwAgAD0AIAAkAHQAcgB1AGUAIAB9AAoAIAAgACAAIAAgACAAIAAgACcAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdAAnACAAewAgACQAcAAuAGgAYQBzAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AcwAgAD0AIAAkAHQAcgB1AGUAIAB9AAoAIAAgACAAIAAgACAAIAAgACcAQQByAHIAYQB5AEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAHMAIAA9ACAAJAB",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e",
                                "action_process_instance_id": "Ad0Prcz4FrUAAAy4AAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "actor_process_image_md5": "289da3ebbffc187c60203c40cfcc49b5",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "actor_process_os_pid": 17652,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 28684,
                                "agent_host_boot_time": 1783560340747,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" ",
                                "causality_actor_process_execution_time": 1783561241864,
                                "causality_actor_process_image_md5": "5a9ac75012bcb1873ca24b906ce64e58",
                                "causality_actor_process_image_name": "Code.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                                "causality_actor_process_image_sha256": "88cd70cac1eee04385352785f942846980203ce049e30baf6c8f927005b645af",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn0c+dRYsZHbSAHkUbw==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783606681475,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "os_actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "os_actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "os_actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "os_actor_process_os_pid": 17652,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 28684,
                                "user_name": "TECHNOMA\\josetorales"
                            }
                        ],
                        "external_id": "37bca7d3-f483-493a-9a51-a39d0cd78829",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.89"
                        ],
                        "host_name": "NB-JTORALES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783606711341,
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
                            "DS:PANW/XDR Agent",
                            "EG:Technoma"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "executable": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "hash": {
                                    "md5": "289da3ebbffc187c60203c40cfcc49b5",
                                    "sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1"
                                },
                                "name": "claude.exe",
                                "pid": 17652
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 128871,
                        "status": "New"
                    },
                    "stellar_da_input": 15558,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "132bc225-42fa-4b62-8a73-370622069f951783607289882-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783606681475,
                    "timestamp_utc": "2026-07-09T14:18:01.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josetorales"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783607289881,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JTORALES\" (\"192.168.169.89\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josetorales\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
                "_id": "53ccb0d8-be75-4d70-95c5-cef103bf29031783608123686-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6936,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "SxhTR58BBi0xHyA-LQFI",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128404"
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
                        "ip": "192.168.169.89",
                        "name": "NB-JTORALES"
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
                    "orig_id": "SxhTR58BBi0xHyA-LQFI",
                    "orig_index": "aella-syslog-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128404",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days",
                        "detection_timestamp": 1783607750649,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "ca9e9da710e240e89b3a64013cd02710",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBjAEcAOQAzAFoAWABKAHoAYQBHAFYAcwBiAEMAQQB0AFIAWABoAGwAWQAzAFYAMABhAFcAOQB1AFUARwA5AHMAYQBXAE4ANQBJAEUASgA1AGMARwBGAHoAYwB5AEEAdABSAG0AbABzAFoAUwBBAGkAUQB6AHAAYwBWAFgATgBsAGMAbgBOAGMAUwBrADkAVABSAFYAUgBQAGYAagBGAGMAUQBYAEIAdwBSAEcARgAwAFkAVgB4AE0AYgAyAE4AaABiAEYAeABVAFoAVwAxAHcAWABHAE4AcwBZAFgAVgBrAFoAVgB4AGoATABTADEAVgBjADIAVgB5AGMAeQAxAHEAYgAzAE4AbABkAEcAOQB5AFkAVwB4AGwAYwB5ADEARQBiADIATgAxAGIAVwBWAHUAZABIAE0AdABRADIAOQBrAFoAWABnAHQATQBqAEEAeQBOAGkAMAB3AE4AUwAwAHcATgBTADEAMABaAFMAMQB3AGQAVwBWAGsAWgBYAE0AdABZADIAOQB1AFoAVwBOADAAWQBYAEkAdABZAFcAdwB0AGMARwA5ADMAWgBYAEkAdABZAG0AbABjAE0ARABRADIATQAyAEkAeQBOAG0AVQB0AE4AagBkAGwATgBDADAAMABOAEcARgBrAEwAVwBFADAATQBXAFkAdABZAGoAbABrAFkAagBNAHkAWgBUAFIAawBNAFQAQQB5AFgASABOAGoAYwBtAEYAMABZADIAaAB3AFkAVwBSAGMAZABtAFYAeQBYADIAMQBsAFoARwBsAGsAWQBYAE0AdQBjAEgATQB4AEkAZwA9AD0AJwAKAAoAaQBmACAAKAAtAG4AbwB0ACAAJABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAKQAgAHsACgAgACAAIAAgAFcAcgBpAHQAZQAtAE8AdQB0AHAAdQB0ACAAJwB7ACIAdgBhAGwAaQBkACIAOgBmAGEAbABzAGUALAAiAGUAcgByAG8AcgBzACIAOgBbAHsAIgBtAGUAcwBzAGEAZwBlACIAOgAiAE4AbwAgAGMAbwBtAG0AYQBuAGQAIABwAHIAbwB2AGkAZABlAGQAIgAsACIAZQByAHIAbwByAEkAZAAiADoAIgBOAG8ASQBuAHAAdQB0ACIAfQBdACwAIgBzAHQAYQB0AGUAbQBlAG4AdABzACIAOgBbAF0ALAAiAHYAYQByAGkAYQBiAGwAZQBzACIAOgBbAF0ALAAiAGgAYQBzAFMAdABvAHAAUABhAHIAcwBpAG4AZwAiADoAZgBhAGwAcwBlACwAIgBvAHIAaQBnAGkAbgBhAGwAQwBvAG0AbQBhAG4AZAAiADoAIgAiAH0AJwAKACAAIAAgACAAZQB4AGkAdAAgADAACgB9AAoACgAkAEMAbwBtAG0AYQBuAGQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACQARQBuAGMAbwBkAGUAZABDAG8AbQBtAGEAbgBkACkAKQAKAAoAJAB0AG8AawBlAG4AcwAgAD0AIAAkAG4AdQBsAGwACgAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAgAD0AIAAkAG4AdQBsAGwACgAkAGEAcwB0ACAAPQAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAHMAZQByAF0AOgA6AFAAYQByAHMAZQBJAG4AcAB1AHQAKAAKACAAIAAgACAAJABDAG8AbQBtAGEAbgBkACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHQAbwBrAGUAbgBzACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAKACkACgAKACQAYQBsAGwAVgBhAHIAaQBhAGIAbABlAHMAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBSAGEAdwBDAG8AbQBtAGEAbgBkAEUAbABlAG0AZQBuAHQAcwAgAHsACgAgACAAIAAgAHAAYQByAGEAbQAoAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQAQQBzAHQAXQAkAEMAbQBkAEEAcwB0ACkACgAgACAAIAAgACQAZQBsAGUAbQBzACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAYwBlACAAaQBuACAAJABDAG0AZABBAHMAdAAuAEMAbwBtAG0AYQBuAGQARQBsAGUAbQBlAG4AdABzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7ACAAdABlAHgAdAAgAD0AIAAkAGMAZQAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGMAZQAuAFAAUwBPAGIAagBlAGMAdAAuAFAAcgBvAHAAZQByAHQAaQBlAHMAWwAnAFYAYQBsAHUAZQAnAF0AIAAtAGEAbgBkACAAJABuAHUAbABsACAALQBuAGUAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AYQBuAGQAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AaQBzACAAWwBzAHQAcgBpAG4AZwBdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAHYAYQBsAHUAZQAgAD0AIAAkAGMAZQAuAFYAYQBsAHUAZQAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAGUAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAGUAeABwAHIAZQBzAHMAaQBvAG4AVAB5AHAAZQAgAD0AIAAkAGMAZQAuAEUAeABwAHIAZQBzAHMAaQBvAG4ALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAkAGEAPQAkAGMAZQAuAEEAcgBnAHUAbQBlAG4AdAA7AGkAZgAoACQAYQApAHsAJABjAGUARABhAHQAYQAuAGMAaABpAGwAZAByAGUAbgA9AEAAKABAAHsAdAB5AHAAZQA9ACQAYQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7AHQAZQB4AHQAPQAkAGEALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQAfQApAH0ACgAgACAAIAAgACAAIAAgACAAWwB2AG8AaQBkAF0AJABlAGwAZQBtAHMALgBBAGQAZAAoACQAYwBlAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAGUAbABlAG0AcwAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUgBhAHcAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AKAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkACgAgACAAIAAgACQAcgBlAHMAdQBsAHQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJAByAGUAZABpAHIAIABpAG4AIAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAHIAZQBkAGkAcgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAHIAZQBkAGkAcgAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARgBpAGwAZQBSAGUAZABpAHIAZQBjAHQAaQBvAG4AQQBzAHQAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBhAHAAcABlAG4AZAAgAD0AIABbAGIAbwBvAGwAXQAkAHIAZQBkAGkAcgAuAEEAcABwAGUAbgBkAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGYAcgBvAG0AUwB0AHIAZQBhAG0AIAA9ACAAJAByAGUAZABpAHIALgBGAHIAbwBtAFMAdAByAGUAYQBtAC4AVABvAFMAdAByAGkAbgBnACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBsAG8AYwBhAHQAaQBvAG4AVABlAHgAdAAgAD0AIAAkAHIAZQBkAGkAcgAuAEwAbwBjAGEAdABpAG8AbgAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAFsAdgBvAGkAZABdACQAcgBlAHMAdQBsAHQALgBBAGQAZAAoACQAcgBlAGQAaQByAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAHIAZQBzAHUAbAB0AAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBTAGUAYwB1AHIAaQB0AHkAUABhAHQAdABlAHIAbgBzACgAJABBACkAIAB7AAoAIAAgACAAIAAkAHAAIAA9ACAAQAB7AH0ACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAbgAgAGkAbgAgACQAQQAuAEYAaQBuAGQAQQBsAGwAKAB7ACAAcABhAHIAYQBtACgAJAB4ACkACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQQByAHIAYQB5AEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARQB4AHAAYQBuAGQAYQBiAGwAZQBTAHQAcgBpAG4AZwBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAYwByAGkAcAB0AEIAbABvAGMAawBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAGUAbgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0ACgAgACAAIAAgAH0ALAAgACQAdAByAHUAZQApACkAIAB7ACAAcwB3AGkAdABjAGgAIAAoACQAbgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQApACAAewAKACAAIAAgACAAIAAgACAAIAAnAEkAbgB2AG8AawBlAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAEEAcgByAGEAeQBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBzACAAPQAgACQAdAByAHUAZQA",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e",
                                "action_process_instance_id": "Ad0PsEpHjCYAAIWsAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "actor_process_image_md5": "289da3ebbffc187c60203c40cfcc49b5",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "actor_process_os_pid": 17652,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 28684,
                                "agent_host_boot_time": 1783560340747,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" ",
                                "causality_actor_process_execution_time": 1783561241864,
                                "causality_actor_process_image_md5": "5a9ac75012bcb1873ca24b906ce64e58",
                                "causality_actor_process_image_name": "Code.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                                "causality_actor_process_image_sha256": "88cd70cac1eee04385352785f942846980203ce049e30baf6c8f927005b645af",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn0dOxbosZHbSAH3R5w==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783607750649,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "os_actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "os_actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "os_actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "os_actor_process_os_pid": 17652,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 28684,
                                "user_name": "TECHNOMA\\josetorales"
                            }
                        ],
                        "external_id": "ea21661a-bd78-409f-a447-09cd6e554f0a",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.89"
                        ],
                        "host_name": "NB-JTORALES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783607920300,
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
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "executable": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "hash": {
                                    "md5": "289da3ebbffc187c60203c40cfcc49b5",
                                    "sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1"
                                },
                                "name": "claude.exe",
                                "pid": 17652
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 62540,
                        "status": "New"
                    },
                    "stellar_da_input": 15558,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "53ccb0d8-be75-4d70-95c5-cef103bf29031783608123686-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783607750649,
                    "timestamp_utc": "2026-07-09T14:35:50.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josetorales"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783608123686,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JTORALES\" (\"192.168.169.89\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josetorales\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
                "_id": "a876376d-bed8-4220-bbc9-4049cad51a6d1783608481012-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 6939,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "NRhXR58BBi0xHyA-v28l",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "128405"
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
                        "ip": "192.168.169.89",
                        "name": "NB-JTORALES"
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
                    "orig_id": "NRhXR58BBi0xHyA-v28l",
                    "orig_index": "aella-syslog-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "palo_alto_networks": {
                        "action": "DETECTED",
                        "action_pretty": "Detected",
                        "agent_data_collection_status": null,
                        "agent_device_domain": null,
                        "agent_fqdn": null,
                        "agent_ip_addresses_v6": null,
                        "agent_os_sub_type": "Windows 11 [10.0 (Build 26200)]",
                        "agent_os_type": "Windows",
                        "agent_version": "8.8.0.10622",
                        "alert_domain": "DOMAIN_SECURITY",
                        "alert_id": "128405",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days",
                        "detection_timestamp": 1783607837533,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "ca9e9da710e240e89b3a64013cd02710",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBjAEcAOQAzAFoAWABKAHoAYQBHAFYAcwBiAEMAQQB0AFIAWABoAGwAWQAzAFYAMABhAFcAOQB1AFUARwA5AHMAYQBXAE4ANQBJAEUASgA1AGMARwBGAHoAYwB5AEEAdABSAG0AbABzAFoAUwBBAGkAUQB6AHAAYwBWAFgATgBsAGMAbgBOAGMAUwBrADkAVABSAFYAUgBQAGYAagBGAGMAUQBYAEIAdwBSAEcARgAwAFkAVgB4AE0AYgAyAE4AaABiAEYAeABVAFoAVwAxAHcAWABHAE4AcwBZAFgAVgBrAFoAVgB4AGoATABTADEAVgBjADIAVgB5AGMAeQAxAHEAYgAzAE4AbABkAEcAOQB5AFkAVwB4AGwAYwB5ADEARQBiADIATgAxAGIAVwBWAHUAZABIAE0AdABRADIAOQBrAFoAWABnAHQATQBqAEEAeQBOAGkAMAB3AE4AUwAwAHcATgBTADEAMABaAFMAMQB3AGQAVwBWAGsAWgBYAE0AdABZADIAOQB1AFoAVwBOADAAWQBYAEkAdABZAFcAdwB0AGMARwA5ADMAWgBYAEkAdABZAG0AbABjAE0ARABRADIATQAyAEkAeQBOAG0AVQB0AE4AagBkAGwATgBDADAAMABOAEcARgBrAEwAVwBFADAATQBXAFkAdABZAGoAbABrAFkAagBNAHkAWgBUAFIAawBNAFQAQQB5AFgASABOAGoAYwBtAEYAMABZADIAaAB3AFkAVwBSAGMAYgBHAGwAegBkAEcARgB5AFgAMgAxAGwAWgBHAGwAawBZAFgATgBmAGIAVwBWADAAWQBTADUAdwBjAHoARQBpACcACgAKAGkAZgAgACgALQBuAG8AdAAgACQARQBuAGMAbwBkAGUAZABDAG8AbQBtAGEAbgBkACkAIAB7AAoAIAAgACAAIABXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACcAewAiAHYAYQBsAGkAZAAiADoAZgBhAGwAcwBlACwAIgBlAHIAcgBvAHIAcwAiADoAWwB7ACIAbQBlAHMAcwBhAGcAZQAiADoAIgBOAG8AIABjAG8AbQBtAGEAbgBkACAAcAByAG8AdgBpAGQAZQBkACIALAAiAGUAcgByAG8AcgBJAGQAIgA6ACIATgBvAEkAbgBwAHUAdAAiAH0AXQAsACIAcwB0AGEAdABlAG0AZQBuAHQAcwAiADoAWwBdACwAIgB2AGEAcgBpAGEAYgBsAGUAcwAiADoAWwBdACwAIgBoAGEAcwBTAHQAbwBwAFAAYQByAHMAaQBuAGcAIgA6AGYAYQBsAHMAZQAsACIAbwByAGkAZwBpAG4AYQBsAEMAbwBtAG0AYQBuAGQAIgA6ACIAIgB9ACcACgAgACAAIAAgAGUAeABpAHQAIAAwAAoAfQAKAAoAJABDAG8AbQBtAGEAbgBkACAAPQAgAFsAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAVABGADgALgBHAGUAdABTAHQAcgBpAG4AZwAoAFsAUwB5AHMAdABlAG0ALgBDAG8AbgB2AGUAcgB0AF0AOgA6AEYAcgBvAG0AQgBhAHMAZQA2ADQAUwB0AHIAaQBuAGcAKAAkAEUAbgBjAG8AZABlAGQAQwBvAG0AbQBhAG4AZAApACkACgAKACQAdABvAGsAZQBuAHMAIAA9ACAAJABuAHUAbABsAAoAJABwAGEAcgBzAGUARQByAHIAbwByAHMAIAA9ACAAJABuAHUAbABsAAoAJABhAHMAdAAgAD0AIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBQAGEAcgBzAGUAcgBdADoAOgBQAGEAcgBzAGUASQBuAHAAdQB0ACgACgAgACAAIAAgACQAQwBvAG0AbQBhAG4AZAAsAAoAIAAgACAAIABbAHIAZQBmAF0AJAB0AG8AawBlAG4AcwAsAAoAIAAgACAAIABbAHIAZQBmAF0AJABwAGEAcgBzAGUARQByAHIAbwByAHMACgApAAoACgAkAGEAbABsAFYAYQByAGkAYQBiAGwAZQBzACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUgBhAHcAQwBvAG0AbQBhAG4AZABFAGwAZQBtAGUAbgB0AHMAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AKABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBDAG8AbQBtAGEAbgBkAEEAcwB0AF0AJABDAG0AZABBAHMAdAApAAoAIAAgACAAIAAkAGUAbABlAG0AcwAgAD0AIABbAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4AQQByAHIAYQB5AEwAaQBzAHQAXQA6ADoAbgBlAHcAKAApAAoAIAAgACAAIABmAG8AcgBlAGEAYwBoACAAKAAkAGMAZQAgAGkAbgAgACQAQwBtAGQAQQBzAHQALgBDAG8AbQBtAGEAbgBkAEUAbABlAG0AZQBuAHQAcwApACAAewAKACAAIAAgACAAIAAgACAAIAAkAGMAZQBEAGEAdABhACAAPQAgAEAAewAgAHQAeQBwAGUAIAA9ACAAJABjAGUALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUAOwAgAHQAZQB4AHQAIAA9ACAAJABjAGUALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAGUALgBQAFMATwBiAGoAZQBjAHQALgBQAHIAbwBwAGUAcgB0AGkAZQBzAFsAJwBWAGEAbAB1AGUAJwBdACAALQBhAG4AZAAgACQAbgB1AGwAbAAgAC0AbgBlACAAJABjAGUALgBWAGEAbAB1AGUAIAAtAGEAbgBkACAAJABjAGUALgBWAGEAbAB1AGUAIAAtAGkAcwAgAFsAcwB0AHIAaQBuAGcAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEALgB2AGEAbAB1AGUAIAA9ACAAJABjAGUALgBWAGEAbAB1AGUACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIABpAGYAIAAoACQAYwBlACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBDAG8AbQBtAGEAbgBkAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEALgBlAHgAcAByAGUAcwBzAGkAbwBuAFQAeQBwAGUAIAA9ACAAJABjAGUALgBFAHgAcAByAGUAcwBzAGkAbwBuAC4ARwBlAHQAVAB5AHAAZQAoACkALgBOAGEAbQBlAAoAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAJABhAD0AJABjAGUALgBBAHIAZwB1AG0AZQBuAHQAOwBpAGYAKAAkAGEAKQB7ACQAYwBlAEQAYQB0AGEALgBjAGgAaQBsAGQAcgBlAG4APQBAACgAQAB7AHQAeQBwAGUAPQAkAGEALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUAOwB0AGUAeAB0AD0AJABhAC4ARQB4AHQAZQBuAHQALgBUAGUAeAB0AH0AKQB9AAoAIAAgACAAIAAgACAAIAAgAFsAdgBvAGkAZABdACQAZQBsAGUAbQBzAC4AQQBkAGQAKAAkAGMAZQBEAGEAdABhACkACgAgACAAIAAgAH0ACgAgACAAIAAgAHIAZQB0AHUAcgBuACAAJABlAGwAZQBtAHMACgB9AAoACgBmAHUAbgBjAHQAaQBvAG4AIABHAGUAdAAtAFIAYQB3AFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACAAewAKACAAIAAgACAAcABhAHIAYQBtACgAJABSAGUAZABpAHIAZQBjAHQAaQBvAG4AcwApAAoAIAAgACAAIAAkAHIAZQBzAHUAbAB0ACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAcgBlAGQAaQByACAAaQBuACAAJABSAGUAZABpAHIAZQBjAHQAaQBvAG4AcwApACAAewAKACAAIAAgACAAIAAgACAAIAAkAHIAZQBkAGkAcgBEAGEAdABhACAAPQAgAEAAewAgAHQAeQBwAGUAIAA9ACAAJAByAGUAZABpAHIALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJAByAGUAZABpAHIAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEYAaQBsAGUAUgBlAGQAaQByAGUAYwB0AGkAbwBuAEEAcwB0AF0AKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHIAZQBkAGkAcgBEAGEAdABhAC4AYQBwAHAAZQBuAGQAIAA9ACAAWwBiAG8AbwBsAF0AJAByAGUAZABpAHIALgBBAHAAcABlAG4AZAAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBmAHIAbwBtAFMAdAByAGUAYQBtACAAPQAgACQAcgBlAGQAaQByAC4ARgByAG8AbQBTAHQAcgBlAGEAbQAuAFQAbwBTAHQAcgBpAG4AZwAoACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHIAZQBkAGkAcgBEAGEAdABhAC4AbABvAGMAYQB0AGkAbwBuAFQAZQB4AHQAIAA9ACAAJAByAGUAZABpAHIALgBMAG8AYwBhAHQAaQBvAG4ALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIABbAHYAbwBpAGQAXQAkAHIAZQBzAHUAbAB0AC4AQQBkAGQAKAAkAHIAZQBkAGkAcgBEAGEAdABhACkACgAgACAAIAAgAH0ACgAgACAAIAAgAHIAZQB0AHUAcgBuACAAJAByAGUAcwB1AGwAdAAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUwBlAGMAdQByAGkAdAB5AFAAYQB0AHQAZQByAG4AcwAoACQAQQApACAAewAKACAAIAAgACAAJABwACAAPQAgAEAAewB9AAoAIAAgACAAIABmAG8AcgBlAGEAYwBoACAAKAAkAG4AIABpAG4AIAAkAEEALgBGAGkAbgBkAEEAbABsACgAewAgAHAAYQByAGEAbQAoACQAeAApAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ATQBlAG0AYgBlAHIARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACAALQBvAHIACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEEAcgByAGEAeQBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEUAeABwAGEAbgBkAGEAYgBsAGUAUwB0AHIAaQBuAGcARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACAALQBvAHIACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBTAGMAcgBpAHAAdABCAGwAbwBjAGsARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACAALQBvAHIACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBQAGEAcgBlAG4ARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdAAoAIAAgACAAIAB9ACwAIAAkAHQAcgB1AGUAKQApACAAewAgAHMAdwBpAHQAYwBoACAAKAAkAG4ALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUAKQAgAHsACgAgACAAIAAgACAAIAAgACAAJwBJAG4AdgBvAGsAZQBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMATQBlAG0AYgBlAHIASQBuAHYAbwBjAGEAdABpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMATQBlAG0AYgBlAHIASQBuAHYAbwBjAGEAdABpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBBAHIAcgBhAHkARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdAAnACAAewAgACQAcAAuAGgAYQBzAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AcwA",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e",
                                "action_process_instance_id": "Ad0PsH4RsaoAABWgAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "actor_process_image_md5": "289da3ebbffc187c60203c40cfcc49b5",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "actor_process_os_pid": 17652,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 28684,
                                "agent_host_boot_time": 1783560340747,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" ",
                                "causality_actor_process_execution_time": 1783561241864,
                                "causality_actor_process_image_md5": "5a9ac75012bcb1873ca24b906ce64e58",
                                "causality_actor_process_image_name": "Code.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josetorales\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                                "causality_actor_process_image_sha256": "88cd70cac1eee04385352785f942846980203ce049e30baf6c8f927005b645af",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Microsoft Corporation",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABn0dQGR4sZHbSAH5D2A==",
                                "event_sub_type": 1,
                                "event_timestamp": 1783607837533,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad0PQ/PPNtYAACrUAAAAAA==",
                                "os_actor_process_command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "os_actor_process_image_sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1",
                                "os_actor_process_instance_id": "Ad0PrQSVGK0AAET0AAAAAA==",
                                "os_actor_process_os_pid": 17652,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 28684,
                                "user_name": "TECHNOMA\\josetorales"
                            }
                        ],
                        "external_id": "c7cd1c10-66e8-474e-9f39-2e1b4ff8818a",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.89"
                        ],
                        "host_name": "NB-JTORALES",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1783607927961,
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
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "resolution_comment": null,
                        "resolution_status": "STATUS_010_NEW",
                        "severity": "low",
                        "source": "XDR Analytics BIOC",
                        "starred": false,
                        "tags": [
                            "DS:PANW/XDR Agent",
                            "DOM:Security",
                            "EG:Technoma"
                        ],
                        "variation_rule_id": null
                    },
                    "process_list": [
                        {
                            "hash": {
                                "sha256": "c6e6838840944783f05a942973a8f194288279cf7ccccb6b38979857006a2f8e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "c:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe --output-format stream-json --verbose --input-format stream-json --max-thinking-tokens 31999 --permission-prompt-tool stdio --setting-sources=user,project,local --permission-mode default --include-partial-messages --debug --debug-to-stderr --enable-auth-status --no-chrome --replay-user-messages",
                                "executable": "C:\\Users\\josetorales\\.vscode\\extensions\\anthropic.claude-code-2.1.204-win32-x64\\resources\\native-binary\\claude.exe",
                                "hash": {
                                    "md5": "289da3ebbffc187c60203c40cfcc49b5",
                                    "sha256": "e1d82bf346d99db3e611b75a4afc5fdf1530d8d8c546389cf45ac8250bce4af1"
                                },
                                "name": "claude.exe",
                                "pid": 17652
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 120355,
                        "status": "New"
                    },
                    "stellar_da_input": 15558,
                    "stellar_index_id": "aella-ser-2026.07.09-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a876376d-bed8-4220-bbc9-4049cad51a6d1783608481012-YWVsbGEtc2VyLTIwMjYuMDcuMDktZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1783607837533,
                    "timestamp_utc": "2026-07-09T14:37:17.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josetorales"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1783608481012,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JTORALES\" (\"192.168.169.89\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josetorales\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.8.0.10622\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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