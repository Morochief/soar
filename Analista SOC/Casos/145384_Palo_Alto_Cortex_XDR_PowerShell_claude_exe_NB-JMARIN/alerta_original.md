# Lote Completo de Alertas Nativas de Interflow - Stellar Cyber / Cortex XDR

```json
{
    "data": {
        "docs": [
            {
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "a13f04e1-6bf2-49ef-bfd8-74eee141fb3a1790261061888-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19386,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "7fne06ABI3UnQyDOFoSh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "145384"
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
                        "ip": "192.168.169.69",
                        "name": "NB-JMARIN"
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
                    "orig_id": "7fne06ABI3UnQyDOFoSh",
                    "orig_index": "aella-syslog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "145384",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 1 different endpoints and on 2 unique days in the last 30 days",
                        "detection_timestamp": 1790260448112,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "aa013ed0b63c45a285db5878c8020507",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBSADIAVgAwAEwAVQBOAHYAYgBXADEAaABiAG0AUQBnAFkAWABkAHoASQBDADEARgBjAG4ASgB2AGMAawBGAGoAZABHAGwAdgBiAGkAQgBUAGEAVwB4AGwAYgBuAFIAcwBlAFUATgB2AGIAbgBSAHAAYgBuAFYAbABJAEgAdwBnAFUAMgBWAHMAWgBXAE4AMABMAFUAOQBpAGEAbQBWAGoAZABDAEIAVABiADMAVgB5AFkAMgBVADcASQBGAFIAbABjADMAUQB0AFUARwBGADAAYQBDAEEAaQBRAHoAcABjAFUASABKAHYAWgAzAEoAaABiAFMAQgBHAGEAVwB4AGwAYcAxAHgAQgBiAFcARgA2AGIAMgA1AGMAUQBWAGQAVABRADAAeABKAFYAagBKAGMAWQBYAGQAegBMAG0AVgA0AFoAUwBJADcASQBGAFIAbABjADMAUQB0AFUARwBGADAAYQBDAEEAaQBKAEcAVgB1AGQAagBwAFYAVQAwAFYAUwBVAEYASgBQAFIAawBsAE0AUgBWAHcAdQBZAFgAZAB6AEkAagBzAGcAWgAyAGwAMABJAEMAMQBEAEkAQwA0AGcAYgBHADkAbgBJAEMAMAB0AGIAMgA1AGwAYgBHAGwAdQBaAFMAQQB0AE0AeQBBAHQATABTAEIAegBaAFgASgAyAGEAVwBOAGwAYwB5ADkAcABiAG4AWgB2AGEAVwBOAGwAYwB5ADkAcwBhAFgATgAwAEwAVwBwAHYAWQBuAE0APQAnAAoACgBpAGYAIAAoAC0AbgBvAHQAIAAkAEUAbgBjAG8AZABkAGUAZABDAG8AbQBtAGQAYQBuAGQAKQAgAHsACgAgACAAIAAgAFcAcgBpAHQAZQAtAE8AdQB0AHAAdQB0ACAAJwB7ACIAdgBhAGwAaQBkACIAOgBmAGEAbABzAGUALAAiAGUAcgByAG8AcgBzACIAOgBbAHsAIgBtAGUAcwBzAGEAZwBlACIAOgAiAE4AbwAgAGMAbwBtAG0AYQBuAGQAIABwAHIAbwB2AGkAZABlAGQAIgAsACIAZQByAHIAbwByAEkAZAAiADoAIgBOAG8ASQBuAHAAdQB0ACIAfQBdACwAIgBzAHQAYQB0AGUAbQBlAG4AdABzACIAOgBbAF0ALAAiAHYAYQByAGkAYQBiAGwAZQBzACIAOgBbAF0ALAAiAGgAYQBzAFMAdABvAHAAUABhAHIAcwBpAG4AZwAiADoAZgBhAGwAcwBlACwAIgBvAHIAaQBnAGkAbgBhAGwAQwBvAG0AbQBhAG4AZAAiADoAIgAiAH0AJwAKACAAIAAgACAAZQB4AGkAdAAgADAACgB9AAoACgAkAEMAbwBtAG0AYQBuAGQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACQARQBuAGMAbwBkAGUAZABDAG8AbQBtAGEAbgBkACkAKQAKAAoAJAB0AG8AawBlAG4AcwAgAD0AIAAkAG4AdQBsAGwACgAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAgAD0AIAAkAG4AdQBsAGwACgAkAGEAcwB0ACAAPQAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAHMAZQByAF0AOgA6AFAAYQByAHMAZQBJAG4AcAB1AHQAKAAKACAAIAAgACAAJABDAG8AbQBtAGEAbgBkACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHQAbwBrAGUAbgBzACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAKACkACgAKACQAYQBsAGwAVgBhAHIAaQBhAGIAbABlAHMAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBSAGEAdwBDAG8AbQBtAGEAbgBkAEUAbABlAG0AZQBuAHQAcwAgAHsACgAgACAAIAAgAHAAYQByAGEAbQAoAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQAQQBzAHQAXQAkAEMAbQBkAEEAcwB0ACkACgAgACAAIAAgACQAZQBsAGUAbQBzACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAYwBlACAAaQBuACAAJABDAG0AZABBAHMAdAAuAEMAbwBtAG0AYQBuAGQARQBsAGUAbQBlAG4AdABzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7ACAAdABlAHgAdAAgAD0AIAAkAGMAZQAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGMAZQAuAFAAUwBPAGIAagBlAGMAdAAuAFAAcgBvAHAAZQByAHQAaQBlAHMAWwAnAFYAYQBsAHUAZQAnAF0AIAAtAGEAbgBkACAAJABuAHUAbABsACAALQBuAGUAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AYQBuAGQAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AaQBzACAAWwBzAHQAcgBpAG4AZwBdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAHYAYQBsAHUAZQAgAD0AIAAkAGMAZQAuAFYAYQBsAHUAZQAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAGUAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAGUAeABwAHIAZQBzAHMAaQBvAG4AVAB5AHAAZQAgAD0AIAAkAGMAZQAuAEUAeABwAHIAZQBzAHMAaQBvAG4ALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAkAGEAPQAkAGMAZQAuAEEAcgBnAHUAbQBlAG4AdAA7AGkAZgAoACQAYQApAHsAJABjAGUARABhAHQAYQAuAGMAaABpAGwAZAByAGUAbgA9AEAAKABAAHsAdAB5AHAAZQA9ACQAYQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7AHQAZQB4AHQAPQAkAGEALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQAfQApAH0ACgAgACAAIAAgACAAIAAgACAAWwB2AG8AaQBkAF0AJABlAGwAZQBtAHMALgBBAGQAZAAoACQAYwBlAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAGUAbABlAG0AcwAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUgBhAHcAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AKAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkACgAgACAAIAAgACQAcgBlAHMAdQBsAHQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJAByAGUAZABpAHIAIABpAG4AIAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAHIAZQBkAGkAcgAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARgBpAGwAZQBSAGUAZABpAHIAZQBjAHQAaQBvAG4AQQBzAHQAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBhAHAAcABlAG4AZAAgAD0AIABbAGIAbwBvAGwAXQAkAHIAZQBkAGkAcgAuAEEAcABwAGUAbgBkAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGYAcgBvAG0AUwB0AHIAZQBhAG0AIAA9ACAAJAByAGUAZABpAHIALgBGAHIAbwBtAFMAdAByAGUAYQBtAC4AVABvAFMAdAByAGkAbgBnACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBsAG8AYwBhAHQAaQBvAG4AVABlAHgAdAAgAD0AIAAkAHIAZQBkAGkAcgAuAEwAbwBjAGEAdABpAG8AbgAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAFsAdgBvAGkAZABdACQAcgBlAHMAdQBsAHQALgBBAGQAZAAoACQAcgBlAGQAaQByAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAHIAZQBzAHUAbAB0AAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBTAGUAYwB1AHIAaQB0AHkAUABhAHQAdABlAHIAbgBzACgAJABBACkAIAB7AAoAIAAgACAAIAAkAHAAIAA9ACAAQAB7AH0ACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAbgAgAGkAbgAgACQAQQAuAEYAaQBuAGQAQQBsAGwAKAB7ACAAcABhAHIAYQBtACgAJAB4ACkACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQQByAHIAYQB5AEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARQB4AHAAYQBuAGQAYQBiAGwAZQBTAHQAcgBpAG4AZwBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAYwByAGkAcAB0AEIAbABvAGMAawBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAGUAbgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0ACgAgACAAIAAgAH0ALAAgACQAdAByAHUAZQApACkAIAB7ACAAcwB3AGkAdABjAGgAIAAoACQAbgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQApACAAewAKACAAIAAgACAAIAAgACAAIAAnAEkAbgB2AG8AawBlAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAEEAcgByAGEAeQBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBQAGEAcgBlAG4ARQB4AHAA",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e",
                                "action_process_instance_id": "Ad1MMcQuJ4MAAD58AAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "actor_process_image_md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "actor_process_os_pid": 20712,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 22820,
                                "agent_host_boot_time": 1789448823249,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe\" --startup",
                                "causality_actor_process_execution_time": 1789474985757,
                                "causality_actor_process_image_md5": "aa4170dc30a78889600814f0f0cd10e2",
                                "causality_actor_process_image_name": "claude.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe",
                                "causality_actor_process_image_sha256": "c04ae4e15258d73c3dfe268ca5e0e7a90650073fc6ce11dd75fecb5f16aa9214",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Anthropic, PBC",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABoNPWmolk570oAHwgcg==",
                                "event_sub_type": 1,
                                "event_timestamp": 1790260448112,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "os_actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "os_actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "os_actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "os_actor_process_os_pid": 20712,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 22820,
                                "user_name": "TECHNOMA\\josemarin"
                            }
                        ],
                        "external_id": "8518f008-f435-4f7c-aa23-6c4fd6e1dd12",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.69"
                        ],
                        "host_name": "NB-JMARIN",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1790260585809,
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
                            "DOM:Security"
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
                                "sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "executable": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "hash": {
                                    "md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                    "sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50"
                                },
                                "name": "claude.exe",
                                "pid": 20712
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 120671,
                        "status": "New"
                    },
                    "stellar_da_input": 25227,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "a13f04e1-6bf2-49ef-bfd8-74eee141fb3a1790261061888-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790260448112,
                    "timestamp_utc": "2026-09-24T14:34:08.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josemarin"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1790261061888,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JMARIN\" (\"192.168.169.69\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josemarin\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 1 different endpoints and on 2 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "61ae8e5a-aa4e-4d1d-a565-284d62795cbd1790261061879-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19385,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "7Pne06ABI3UnQyDOFoSh",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "145386"
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
                        "ip": "192.168.169.69",
                        "name": "NB-JMARIN"
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
                    "orig_id": "7Pne06ABI3UnQyDOFoSh",
                    "orig_index": "aella-syslog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "145386",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 2 different endpoints and on 3 unique days in the last 30 days",
                        "detection_timestamp": 1790260606374,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "aa013ed0b63c45a285db5878c8020507",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBkADIAbAB1AFoAMgBWADAASQBDADAAdABkAG0AVgB5AGMAMgBsAHYAYgBqAHMAZwBkADIAbAB1AFoAMgBWADAASQBHAGwAdQBjADMAUgBoAGIARwB3AGcATABTADEAcABaAEMAQgBCAGIAVwBGADYAYgAyADQAdQBRAFYAZABUAFEAMAB4AEoASQBDADEAbABJAEMAMAB0AFYAVwBOAGoAWgBYAEIAMABMAFgAQgBoAFkAMgB0AGgAWgAyAFUAdABZAFcAZAB5AFoAVwBWAHQAWgBXADUAMABjAHkAQQB0AEwAVwBGAGoAWQAyAFYAdwBkAEMAMQB6AGIAMwBWAHkAWQAyAFUAdABZAFcAZAB5AFoAVwBWAHQAWgBXADUAMABjAHkAQQB5AFAAaQBZAHgASQBIAHcAZwBVADIAVgBzAFoAVwBOADAATABVADkAaQBhAG0AVgBqAGQAQwBBAHQAVABHAEYAegBkAEMAQQB4AE4AUQA9AD0AJwAKAAoAaQBmACAAKAAtAG4AbwB0ACAAJABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAKQAgAHsACgAgACAAIAAgAFcAcgBpAHQAZQAtAE8AdQB0AHAAdQB0ACAAJwB7ACIAdgBhAGwAaQBkACIAOgBmAGEAbABzAGUALAAiAGUAcgByAG8AcgBzACIAOgBbAHsAIgBtAGUAcwBzAGEAZwBlACIAOgAiAE4AbwAgAGMAbwBtAG0AYQBuAGQAIABwAHIAbwB2AGkAZABlAGQAIgAsACIAZQByAHIAbwByAEkAZAAiADoAIgBOAG8ASQBuAHAAdQB0ACIAfQBdACwAIgBzAHQAYQB0AGUAbQBlAG4AdABzACIAOgBbAF0ALAAiAHYAYQByAGkAYQBiAGwAZQBzACIAOgBbAF0ALAAiAGgAYQBzAFMAdABvAHAAUABhAHIAcwBpAG4AZwAiADoAZgBhAGwAcwBlACwAIgBvAHIAaQBnAGkAbgBhAGwAQwBvAG0AbQBhAG4AZAAiADoAIgAiAH0AJwAKACAAIAAgACAAZQB4AGkAdAAgADAACgB9AAoACgAkAEMAbwBtAG0AYQBuAGQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACQARQBuAGMAbwBkAGUAZABDAG8AbQBtAGEAbgBkACkAKQAKAAoAJAB0AG8AawBlAG4AcwAgAD0AIAAkAG4AdQBsAGwACgAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAgAD0AIAAkAG4AdQBsAGwACgAkAGEAcwB0ACAAPQAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAHMAZQByAF0AOgA6AFAAYQByAHMAZQBJAG4AcAB1AHQAKAAKACAAIAAgACAAJABDAG8AbQBtAGEAbgBkACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHQAbwBrAGUAbgBzACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAKACkACgAKACQAYQBsAGwAVgBhAHIAaQBhAGIAbABlAHMAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBSAGEAdwBDAG8AbQBtAGEAbgBkAEUAbABlAG0AZQBuAHQAcwAgAHsACgAgACAAIAAgAHAAYQByAGEAbQAoAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQAQQBzAHQAXQAkAEMAbQBkAEEAcwB0ACkACgAgACAAIAAgACQAZQBsAGUAbQBzACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAYwBlACAAaQBuACAAJABDAG0AZABBAHMAdAAuAEMAbwBtAG0AYQBuAGQARQBsAGUAbQBlAG4AdABzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7ACAAdABlAHgAdAAgAD0AIAAkAGMAZQAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGMAZQAuAFAAUwBPAGIAagBlAGMAdAAuAFAAcgBvAHAAZQByAHQAaQBlAHMAWwAnAFYAYQBsAHUAZQAnAF0AIAAtAGEAbgBkACAAJABuAHUAbABsACAALQBuAGUAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AYQBuAGQAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AaQBzACAAWwBzAHQAcgBpAG4AZwBdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAHYAYQBsAHUAZQAgAD0AIAAkAGMAZQAuAFYAYQBsAHUAZQAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAGUAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAGUAeABwAHIAZQBzAHMAaQBvAG4AVAB5AHAAZQAgAD0AIAAkAGMAZQAuAEUAeABwAHIAZQBzAHMAaQBvAG4ALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAkAGEAPQAkAGMAZQAuAEEAcgBnAHUAbQBlAG4AdAA7AGkAZgAoACQAYQApAHsAJABjAGUARABhAHQAYQAuAGMAaABpAGwAZAByAGUAbgA9AEAAKABAAHsAdAB5AHAAZQA9ACQAYQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7AHQAZQB4AHQAPQAkAGEALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQAfQApAH0ACgAgACAAIAAgACAAIAAgACAAWwB2AG8AaQBkAF0AJABlAGwAZQBtAHMALgBBAGQAZAAoACQAYwBlAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAGUAbABlAG0AcwAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUgBhAHcAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AKAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkACgAgACAAIAAgACQAcgBlAHMAdQBsAHQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJAByAGUAZABpAHIAIABpAG4AIAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAHIAZQBkAGkAcgAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARgBpAGwAZQBSAGUAZABpAHIAZQBjAHQAaQBvAG4AQQBzAHQAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBhAHAAcABlAG4AZAAgAD0AIABbAGIAbwBvAGwAXQAkAHIAZQBkAGkAcgAuAEEAcABwAGUAbgBkAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGYAcgBvAG0AUwB0AHIAZQBhAG0AIAA9ACAAJAByAGUAZABpAHIALgBGAHIAbwBtAFMAdAByAGUAYQBtAC4AVABvAFMAdAByAGkAbgBnACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBsAG8AYwBhAHQAaQBvAG4AVABlAHgAdAAgAD0AIAAkAHIAZQBkAGkAcgAuAEwAbwBjAGEAdABpAG8AbgAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAFsAdgBvAGkAZABdACQAcgBlAHMAdQBsAHQALgBBAGQAZAAoACQAcgBlAGQAaQByAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAHIAZQBzAHUAbAB0AAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBTAGUAYwB1AHIAaQB0AHkAUABhAHQAdABlAHIAbgBzACgAJABBACkAIAB7AAoAIAAgACAAIAAkAHAAIAA9ACAAQAB7AH0ACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAbgAgAGkAbgAgACQAQQAuAEYAaQBuAGQAQQBsAGwAKAB7ACAAcABhAHIAYQBtACgAJAB4ACkACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQQByAHIAYQB5AEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARQB4AHAAYQBuAGQAYQBiAGwAZQBTAHQAcgBpAG4AZwBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAYwByAGkAcAB0AEIAbABvAGMAawBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAGUAbgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0ACgAgACAAIAAgAH0ALAAgACQAdAByAHUAZQApACkAIAB7ACAAcwB3AGkAdABjAGgAIAAoACQAbgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQApACAAewAKACAAIAAgACAAIAAgACAAIAAnAEkAbgB2AG8AawBlAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAEEAcgByAGEAeQBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBQAGEAcgBlAG4ARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdAAnACAAewAgACQAcAAuAGgAYQBzAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AcwAgAD0AIAAkAHQAcgB1AGUAIAB9AAoAIAAgACAAIAAgACAAIAAgACcARQB4AHAAYQBuAGQAYQBiAGwAZQBTAHQAcgBpAG4AZwBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMARQB4AHAAYQBuAGQAYQB",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e",
                                "action_process_instance_id": "Ad1MMiKGOPoAAF7sAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "actor_process_image_md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "actor_process_os_pid": 20712,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 22820,
                                "agent_host_boot_time": 1789448823249,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe\" --startup",
                                "causality_actor_process_execution_time": 1789474985757,
                                "causality_actor_process_image_md5": "aa4170dc30a78889600814f0f0cd10e2",
                                "causality_actor_process_image_name": "claude.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe",
                                "causality_actor_process_image_sha256": "c04ae4e15258d73c3dfe268ca5e0e7a90650073fc6ce11dd75fecb5f16aa9214",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Anthropic, PBC",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABoNPZBLhk570oAHw/Bg==",
                                "event_sub_type": 1,
                                "event_timestamp": 1790260606374,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "os_actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "os_actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "os_actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "os_actor_process_os_pid": 20712,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 22820,
                                "user_name": "TECHNOMA\\josemarin"
                            }
                        ],
                        "external_id": "aaa166c4-69cf-418a-aa68-1101510dbfeb",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.69"
                        ],
                        "host_name": "NB-JMARIN",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1790260882600,
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
                            "DOM:Security"
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
                                "sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "executable": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "hash": {
                                    "md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                    "sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50"
                                },
                                "name": "claude.exe",
                                "pid": 20712
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 178412,
                        "status": "New"
                    },
                    "stellar_da_input": 25227,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "bc4000b8-0d9b-40a7-b608-fc130e7c7f111790261419239-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790260777279,
                    "timestamp_utc": "2026-09-24T14:39:37.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josemarin"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1790261419239,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JMARIN\" (\"192.168.169.69\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josemarin\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 0 different endpoints and on 0 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
                "_index": "stellar-index-v1-ser-cf73a415c8794884a0c35b458b7c73ae-68e4cbd80c1098a3aec33727-2026.09.17-000033",
                "_type": "_doc",
                "_id": "64e50263-4a35-4d53-88cf-8312c4f889871790266183430-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                "_version": 1,
                "_seq_no": 19796,
                "_primary_term": 1,
                "found": true,
                "_source": {
                    "aella_tuples": "null.null.null.null",
                    "anomaly_id": "-QQr1KABI3UnQyDO5nxz",
                    "appid_stdport": "yes",
                    "detected_fields": [
                        "tenantid",
                        "palo_alto_networks.alert_id"
                    ],
                    "detected_values": [
                        "e511c3fc54cd4d668bb67612c2ef4b04",
                        "145404"
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
                        "ip": "192.168.169.69",
                        "name": "NB-JMARIN"
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
                    "orig_id": "-QQr1KABI3UnQyDO5nxz",
                    "orig_index": "aella-syslog-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
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
                        "alert_id": "145404",
                        "alert_type": "Unclassified",
                        "attempt_counter": 0,
                        "bioc_category_enum_key": null,
                        "bioc_indicator": null,
                        "case_id": null,
                        "category": "Execution",
                        "deduplicate_tokens": null,
                        "description": "The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 2 different endpoints and on 3 unique days in the last 30 days",
                        "detection_timestamp": 1790265623248,
                        "device_product_id": null,
                        "device_serial_number": null,
                        "device_type": null,
                        "device_vendor_id": null,
                        "device_vendor_name": null,
                        "dynamic_fields": null,
                        "end_match_attempt_ts": null,
                        "endpoint_id": "aa013ed0b63c45a285db5878c8020507",
                        "events": [
                            {
                                "action_country": "UNKNOWN",
                                "action_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "action_process_image_command_line": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -NonInteractive -NoLogo -EncodedCommand JABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAIAA9ACAAJwBVADIAVgAwAEwAVQB4AHYAWQAyAEYAMABhAFcAOQB1AEkARQBNADYAWABGAFYAegBaAFgASgB6AFgARwBwAHYAYwAyAFYAdABZAFgASgBwAGIAbAB4AEUAWgBYAE4AcgBkAEcAOQB3AFgARgBSAEkAVABsAHgARwBZAFcATgAwAGQAWABKAGgAYwAxAHgAaABhAFMAMQBqAGIARwA5ADEAWgBDADEAdwBiADMASgAwAFkAVwB3AEsASgBHAFYAdQBkAGoAcABRAFcAVAAwAGkASgBHAFYAdQBkAGoAcABNAFQAMABOAEIAVABFAEYAUQBVAEUAUgBCAFYARQBGAGMAVQBIAEoAdgBaADMASgBoAGIAWABOAGMAVQBIAGwAMABhAEcAOQB1AFgARgBCADUAZABHAGgAdgBiAGoATQB4AE0AbAB4AHcAZQBYAFIAbwBiADIANAB1AFoAWABoAGwASQBnAG8AawBiAFQAMQBUAGQARwBGAHkAZABDADEAUQBjAG0AOQBqAFoAWABOAHoASQBHADUAdgBaAEcAVQBnAEwAVQBGAHkAWgAzAFYAdABaAFcANQAwAFQARwBsAHoAZABDAEEAaQBjADIATgB5AGEAWABCADAAYwB5ADkAcwBiADIATgBoAGIAQwAxADAAWgBYAE4AMABMADIAMQB2AFkAMgBzAHQAYwAyAFYAeQBkAG0AVgB5AEwAbQBOAHEAYwB5AEkAZwBMAFYAQgBoAGMAMwBOAFUAYQBIAEoAMQBJAEMAMQBYAGEAVwA1AGsAYgAzAGQAVABkAEgAbABzAFoAUwBCAEkAYQBXAFIAawBaAFcANABLAEoASABZADkAVQAzAFIAaABjAG4AUQB0AFUASABKAHYAWQAyAFYAegBjAHkAQQBpAGIAbgBCADQATABtAE4AdABaAEMASQBnAEwAVQBGAHkAWgAzAFYAdABaAFcANQAwAFQARwBsAHoAZABDAEEAaQBkAG0AbAAwAFoAUwBBAHQATABXAE4AdgBiAG0AWgBwAFoAeQBCAHoAWQAzAEoAcABjAEgAUgB6AEwAMgB4AHYAWQAyAEYAcwBMAFgAUgBsAGMAMwBRAHYAZABtAGwAMABaAFMANQBzAGIAMgBOAGgAYgBDADEAdABiADIATgByAEwAbQBOAHYAYgBtAFoAcABaAHkANQBxAGMAeQBJAGcATABWAEIAaABjADMATgBVAGEASABKADEASQBDADEAWABhAFcANQBrAGIAMwBkAFQAZABIAGwAcwBaAFMAQgBJAGEAVwBSAGsAWgBXADQASwBVADMAUgBoAGMAbgBRAHQAVQAyAHgAbABaAFgAQQBnAE4AZwBvAG8AUwBXADUAMgBiADIAdABsAEwAVgBKAGwAYwAzAFIATgBaAFgAUgBvAGIAMgBRAGcASQBtAGgAMABkAEgAQQA2AEwAeQA5AHMAYgAyAE4AaABiAEcAaAB2AGMAMwBRADYATgBUAEUAMwBNAHkAOQBwAGIAbgBaAHYAYQBXAE4AbABjAHoAOQBoAGQAWABSAG8AYgAzAEoAegBYADIAOQB1AGIASABrADkATQBTAEkAcABMAG0ARgAxAGQARwBoAHYAYwBuAE0AZwBmAEMAQgBEAGIAMgA1ADIAWgBYAEoAMABWAEcAOAB0AFMAbgBOAHYAYgBpAEEAdABRADIAOQB0AGMASABKAGwAYwAzAE0ASwBJAGkAUQBvAEoARwAwAHUAUwBXAFEAcABJAEMAUQBvAEoASABZAHUAUwBXAFEAcABJAGkAQgA4AEkARQA5ADEAZABDADEARwBhAFcAeABsAEkAQwBJAGsAWgBXADUAMgBPAGwAUgBGAFQAVgBCAGMAYwBHAGwAawBjAHkANQAwAGUASABRAGkAJwAKAAoAaQBmACAAKAAtAG4AbwB0ACAAJABFAG4AYwBvAGQAZQBkAEMAbwBtAG0AYQBuAGQAKQAgAHsACgAgACAAIAAgAFcAcgBpAHQAZQAtAE8AdQB0AHAAdQB0ACAAJwB7ACIAdgBhAGwAaQBkACIAOgBmAGEAbABzAGUALAAiAGUAcgByAG8AcgBzACIAOgBbAHsAIgBtAGUAcwBzAGEAZwBlACIAOgAiAE4AbwAgAGMAbwBtAG0AYQBuAGQAIABwAHIAbwB2AGkAZABlAGQAIgAsACIAZQByAHIAbwByAEkAZAAiADoAIgBOAG8ASQBuAHAAdQB0ACIAfQBdACwAIgBzAHQAYQB0AGUAbQBlAG4AdABzACIAOgBbAF0ALAAiAHYAYQByAGkAYQBiAGwAZQBzACIAOgBbAF0ALAAiAGgAYQBzAFMAdABvAHAAUABhAHIAcwBpAG4AZwAiADoAZgBhAGwAcwBlACwAIgBvAHIAaQBnAGkAbgBhAGwAQwBvAG0AbQBhAG4AZAAiADoAIgAiAH0AJwAKACAAIAAgACAAZQB4AGkAdAAgADAACgB9AAoACgAkAEMAbwBtAG0AYQBuAGQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACQARQBuAGMAbwBkAGUAZABDAG8AbQBtAGEAbgBkACkAKQAKAAoAJAB0AG8AawBlAG4AcwAgAD0AIAAkAG4AdQBsAGwACgAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAgAD0AIAAkAG4AdQBsAGwACgAkAGEAcwB0ACAAPQAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAHMAZQByAF0AOgA6AFAAYQByAHMAZQBJAG4AcAB1AHQAKAAKACAAIAAgACAAJABDAG8AbQBtAGEAbgBkACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHQAbwBrAGUAbgBzACwACgAgACAAIAAgAFsAcgBlAGYAXQAkAHAAYQByAHMAZQBFAHIAcgBvAHIAcwAKACkACgAKACQAYQBsAGwAVgBhAHIAaQBhAGIAbABlAHMAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBSAGEAdwBDAG8AbQBtAGEAbgBkAEUAbABlAG0AZQBuAHQAcwAgAHsACgAgACAAIAAgAHAAYQByAGEAbQAoAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQAQQBzAHQAXQAkAEMAbQBkAEEAcwB0ACkACgAgACAAIAAgACQAZQBsAGUAbQBzACAAPQAgAFsAUwB5AHMAdABlAG0ALgBDAG8AbABsAGUAYwB0AGkAbwBuAHMALgBBAHIAcgBhAHkATABpAHMAdABdADoAOgBuAGUAdwAoACkACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAYwBlACAAaQBuACAAJABDAG0AZABBAHMAdAAuAEMAbwBtAG0AYQBuAGQARQBsAGUAbQBlAG4AdABzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAYwBlAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7ACAAdABlAHgAdAAgAD0AIAAkAGMAZQAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGMAZQAuAFAAUwBPAGIAagBlAGMAdAAuAFAAcgBvAHAAZQByAHQAaQBlAHMAWwAnAFYAYQBsAHUAZQAnAF0AIAAtAGEAbgBkACAAJABuAHUAbABsACAALQBuAGUAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AYQBuAGQAIAAkAGMAZQAuAFYAYQBsAHUAZQAgAC0AaQBzACAAWwBzAHQAcgBpAG4AZwBdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAHYAYQBsAHUAZQAgAD0AIAAkAGMAZQAuAFYAYQBsAHUAZQAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAGUAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAEMAbwBtAG0AYQBuAGQARQB4AHAAcgBlAHMAcwBpAG8AbgBBAHMAdABdACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGUARABhAHQAYQAuAGUAeABwAHIAZQBzAHMAaQBvAG4AVAB5AHAAZQAgAD0AIAAkAGMAZQAuAEUAeABwAHIAZQBzAHMAaQBvAG4ALgBHAGUAdABUAHkAcABlACgAKQAuAE4AYQBtAGUACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAkAGEAPQAkAGMAZQAuAEEAcgBnAHUAbQBlAG4AdAA7AGkAZgAoACQAYQApAHsAJABjAGUARABhAHQAYQAuAGMAaABpAGwAZAByAGUAbgA9AEAAKABAAHsAdAB5AHAAZQA9ACQAYQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQA7AHQAZQB4AHQAPQAkAGEALgBFAHgAdABlAG4AdAAuAFQAZQB4AHQAfQApAH0ACgAgACAAIAAgACAAIAAgACAAWwB2AG8AaQBkAF0AJABlAGwAZQBtAHMALgBBAGQAZAAoACQAYwBlAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAGUAbABlAG0AcwAKAH0ACgAKAGYAdQBuAGMAdABpAG8AbgAgAEcAZQB0AC0AUgBhAHcAUgBlAGQAaQByAGUAYwB0AGkAbwBuAHMAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AKAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkACgAgACAAIAAgACQAcgBlAHMAdQBsAHQAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAEMAbwBsAGwAZQBjAHQAaQBvAG4AcwAuAEEAcgByAGEAeQBMAGkAcwB0AF0AOgA6AG4AZQB3ACgAKQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAJAByAGUAZABpAHIAIABpAG4AIAAkAFIAZQBkAGkAcgBlAGMAdABpAG8AbgBzACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEAIAA9ACAAQAB7ACAAdAB5AHAAZQAgAD0AIAAkAGMAZQAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQAgAH0ACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAHIAZQBkAGkAcgAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARgBpAGwAZQBSAGUAZABpAHIAZQBjAHQAaQBvAG4AQQBzAHQAXQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBhAHAAcABlAG4AZAAgAD0AIABbAGIAbwBvAGwAXQAkAHIAZQBkAGkAcgAuAEEAcABwAGUAbgBkAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAByAGUAZABpAHIARABhAHQAYQAuAGYAcgBvAG0AUwB0AHIAZQBhAG0AIAA9ACAAJAByAGUAZABpAHIALgBGAHIAbwBtAFMAdAByAGUAYQBtAC4AVABvAFMAdAByAGkAbgBnACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcgBlAGQAaQByAEQAYQB0AGEALgBsAG8AYwBhAHQAaQBvAG4AVABlAHgAdAAgAD0AIAAkAHIAZQBkAGkAcgAuAEwAbwBjAGEAdABpAG8AbgAuAEUAeAB0AGUAbgB0AC4AVABlAHgAdAAKACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgAFsAdgBvAGkAZABdACQAcgBlAHMAdQBsAHQALgBBAGQAZAAoACQAcgBlAGQAaQByAEQAYQB0AGEAKQAKACAAIAAgACAAfQAKACAAIAAgACAAcgBlAHQAdQByAG4AIAAkAHIAZQBzAHUAbAB0AAoAfQAKAAoAZgB1AG4AYwB0AGkAbwBuACAARwBlAHQALQBTAGUAYwB1AHIAaQB0AHkAUABhAHQAdABlAHIAbgBzACgAJABBACkAIAB7AAoAIAAgACAAIAAkAHAAIAA9ACAAQAB7AH0ACgAgACAAIAAgAGYAbwByAGUAYQBjAGgAIAAoACQAbgAgAGkAbgAgACQAQQAuAEYAaQBuAGQAQQBsAGwAKAB7ACAAcABhAHIAYQBtACgAJAB4ACkACgAgACAAIAAgACAAIAAgACAAJAB4ACAALQBpAHMAIABbAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBMAGEAbgBnAHUAYQBnAGUALgBNAGUAbQBiAGUAcgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4AQQByAHIAYQB5AEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAXQAgAC0AbwByAAoAIAAgACAAIAAgACAAIAAgACQAeAAgAC0AaQBzACAAWwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4ATABhAG4AZwB1AGEAZwBlAC4ARQB4AHAAYQBuAGQAYQBiAGwAZQBTAHQAcgBpAG4AZwBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFMAYwByAGkAcAB0AEIAbABvAGMAawBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0AIAAtAG8AcgAKACAAIAAgACAAIAAgACAAIAAkAHgAIAAtAGkAcwAgAFsAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEwAYQBuAGcAdQBhAGcAZQAuAFAAYQByAGUAbgBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0AF0ACgAgACAAIAAgAH0ALAAgACQAdAByAHUAZQApACkAIAB7ACAAcwB3AGkAdABjAGgAIAAoACQAbgAuAEcAZQB0AFQAeQBwAGUAKAApAC4ATgBhAG0AZQApACAAewAKACAAIAAgACAAIAAgACAAIAAnAEkAbgB2AG8AawBlAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAE0AZQBtAGIAZQByAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBNAGUAbQBiAGUAcgBJAG4AdgBvAGMAYQB0AGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAFMAdQBiAEUAeABwAHIAZQBzAHMAaQBvAG4AQQBzAHQAJwAgAHsAIAAkAHAALgBoAGEAcwBTAHUAYgBFAHgAcAByAGUAcwBzAGkAbwBuAHMAIAA9ACAAJAB0AHIAdQBlACAAfQAKACAAIAAgACAAIAAgACAAIAAnAEEAcgByAGEAeQBFAHgAcAByAGUAcwBzAGkAbwBuAEEAcwB0ACcAIAB7ACAAJABwAC4AaABhAHMAUwB1AGIARQB4AHAAcgBlAHMAcwBpAG8AbgBzACAAPQAgACQAdAByAHUAZQAgAH0ACgAgACAAIAAgACAAIAAgACAAJwBQAGEAcgBlAG4ARQB4AHAA",
                                "action_process_image_name": "powershell.exe",
                                "action_process_image_sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e",
                                "action_process_instance_id": "Ad1MPdDdHIkAABboAAAAAA==",
                                "action_process_signature_status": "Signed",
                                "action_process_signature_vendor": "Microsoft Corporation",
                                "actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "actor_process_image_md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                "actor_process_image_name": "claude.exe",
                                "actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "actor_process_os_pid": 20712,
                                "actor_process_signature_status": "Signed",
                                "actor_process_signature_vendor": "Anthropic, PBC",
                                "actor_thread_thread_id": 22820,
                                "agent_host_boot_time": 1789448823249,
                                "agent_install_type": "STANDARD",
                                "association_strength": 50,
                                "causality_actor_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "causality_actor_process_command_line": "\"C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe\" --startup",
                                "causality_actor_process_execution_time": 1789474985757,
                                "causality_actor_process_image_md5": "aa4170dc30a78889600814f0f0cd10e2",
                                "causality_actor_process_image_name": "claude.exe",
                                "causality_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Local\\AnthropicClaude\\claude.exe",
                                "causality_actor_process_image_sha256": "c04ae4e15258d73c3dfe268ca5e0e7a90650073fc6ce11dd75fecb5f16aa9214",
                                "causality_actor_process_signature_status": "Signed",
                                "causality_actor_process_signature_vendor": "Anthropic, PBC",
                                "contains_featured_host": "NO",
                                "contains_featured_ip": "NO",
                                "contains_featured_user": "NO",
                                "event_id": "AAABoNQlkj5k570oAIJ1xQ==",
                                "event_sub_type": 1,
                                "event_timestamp": 1790265623248,
                                "event_type": "Process Execution",
                                "fw_is_phishing": "N/A",
                                "os_actor_process_causality_id": "Ad1FDPW7mbcAADuYAAAAAA==",
                                "os_actor_process_command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "os_actor_process_image_name": "claude.exe",
                                "os_actor_process_image_path": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "os_actor_process_image_sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50",
                                "os_actor_process_instance_id": "Ad1MMNeAl1MAAFDoAAAAAA==",
                                "os_actor_process_os_pid": 20712,
                                "os_actor_process_signature_status": "Signed",
                                "os_actor_process_signature_vendor": "Anthropic, PBC",
                                "os_actor_thread_thread_id": 22820,
                                "user_name": "TECHNOMA\\josemarin"
                            }
                        ],
                        "external_id": "c46452a5-c95f-47be-aad5-d8b0db08fefa",
                        "filter_rule_id": null,
                        "host_ip": [
                            "192.168.169.69"
                        ],
                        "host_name": "NB-JMARIN",
                        "is_pcap": false,
                        "is_whitelisted": false,
                        "last_modified_ts": null,
                        "local_insert_ts": 1790265704209,
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
                            "DOM:Security"
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
                                "sha256": "8bb6fa8c283b4d92120b1ef249a9b311b0f804d4cabbe9981159976c8be76a5e"
                            },
                            "name": "powershell.exe",
                            "parent": {
                                "command_line": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe --output-format stream-json --verbose --input-format stream-json --effort medium --model claude-sonnet-5 --permission-prompt-tool stdio --allowedTools mcp__computer-use,mcp__ccd_session__spawn_task,mcp__ccd_session__dismiss_task,mcp__ccd_session__mark_chapter,mcp__ccd_session_mgmt__list_sessions,mcp__ccd_session_mgmt__get_session,mcp__ccd_session_mgmt__get_usage,mcp__ccd_session_mgmt__set_session_title,mcp__ccd_session_mgmt__send_message,mcp__ccd_session_mgmt__detach_session,mcp__ccd_sidebar__list_groups,mcp__ccd_sidebar__create_group,mcp__ccd_sidebar__set_view,mcp__ccd_session_mgmt__search_session_transcripts,mcp__ccd_session_mgmt__list_events,mcp__ccd_session_mgmt__export_transcript,mcp__scheduled-tasks__list_task_runs,mcp__ccd_session__read_widget_context,mcp__ccd_session__list_start_targets,mcp__ccd_view__show_pane,mcp__ccd_view__close_pane,mcp__ccd_view__get_layout,mcp__ccd_settings__get_settings,mcp__mcp-registry__search_mcp_registry,mcp__mcp-registry__suggest_connectors,mcp__mcp-registry__list_connectors,mcp__ccd_connectors__session_connectors_status,mcp__ccd_connectors__reconnect_session_connector,mcp__ccd_pr__get_status,mcp__ccd_window__open_session_in,mcp__ccd_window__close_split,mcp__ccd_window__set_sidebar_collapsed,mcp__ccd_window__get_window_layout --disallowedTools SubscribePR --setting-sources=user,project,local --permission-mode auto --include-partial-messages --await-initialize --thinking-display omitted --replay-user-messages --settings \"{\\\"deniedMcpServers\\\":[{\\\"serverName\\\":\\\"Claude Browser\\\"},{\\\"serverName\\\":\\\"Claude Code Android Emulator\\\"},{\\\"serverName\\\":\\\"Claude Code iOS Simulator\\\"},{\\\"serverName\\\":\\\"Claude Preview\\\"},{\\\"serverName\\\":\\\"Claude_Browser\\\"},{\\\"serverName\\\":\\\"Claude_Code_Android_Emulator\\\"},{\\\"serverName\\\":\\\"Claude_Code_iOS_Simulator\\\"},{\\\"serverName\\\":\\\"Claude_Preview\\\"},{\\\"serverName\\\":\\\"Claude_for_Chrome\\\"},{\\\"serverName\\\":\\\"Framebuffer\\\"},{\\\"serverName\\\":\\\"Window Halo\\\"},{\\\"serverName\\\":\\\"Window_Halo\\\"},{\\\"serverName\\\":\\\"ccd_connectors\\\"},{\\\"serverName\\\":\\\"ccd_directory\\\"},{\\\"serverName\\\":\\\"ccd_host\\\"},{\\\"serverName\\\":\\\"ccd_pr\\\"},{\\\"serverName\\\":\\\"ccd_session\\\"},{\\\"serverName\\\":\\\"ccd_session_mgmt\\\"},{\\\"serverName\\\":\\\"ccd_settings\\\"},{\\\"serverName\\\":\\\"ccd_sidebar\\\"},{\\\"serverName\\\":\\\"ccd_view\\\"},{\\\"serverName\\\":\\\"ccd_window\\\"},{\\\"serverName\\\":\\\"claude-in-chrome\\\"},{\\\"serverName\\\":\\\"claude_browser\\\"},{\\\"serverName\\\":\\\"claude_code_android_emulator\\\"},{\\\"serverName\\\":\\\"claude_code_ios_simulator\\\"},{\\\"serverName\\\":\\\"claude_for_chrome\\\"},{\\\"serverName\\\":\\\"claude_in_chrome\\\"},{\\\"serverName\\\":\\\"claude_preview\\\"},{\\\"serverName\\\":\\\"computer-use\\\"},{\\\"serverName\\\":\\\"computer_use\\\"},{\\\"serverName\\\":\\\"cowork\\\"},{\\\"serverName\\\":\\\"cowork-onboarding\\\"},{\\\"serverName\\\":\\\"cowork_onboarding\\\"},{\\\"serverName\\\":\\\"dev-debug\\\"},{\\\"serverName\\\":\\\"dev_debug\\\"},{\\\"serverName\\\":\\\"dispatch\\\"},{\\\"serverName\\\":\\\"framebuffer\\\"},{\\\"serverName\\\":\\\"mcp-registry\\\"},{\\\"serverName\\\":\\\"mcp_registry\\\"},{\\\"serverName\\\":\\\"plugins\\\"},{\\\"serverName\\\":\\\"remote-devices\\\"},{\\\"serverName\\\":\\\"remote_devices\\\"},{\\\"serverName\\\":\\\"scheduled-tasks\\\"},{\\\"serverName\\\":\\\"scheduled_tasks\\\"},{\\\"serverName\\\":\\\"session_info\\\"},{\\\"serverName\\\":\\\"skills\\\"},{\\\"serverName\\\":\\\"window_halo\\\"}]}\"",
                                "executable": "C:\\Users\\josemarin\\AppData\\Roaming\\Claude\\claude-code\\2.1.280\\claude.exe",
                                "hash": {
                                    "md5": "7b3ba02a4a896f3931d226585bb14f1a",
                                    "sha256": "6d3f8ff8abf9fd562263240da0222e0bf40e3f0370d6e51c0a6f938e2c7c3f50"
                                },
                                "name": "claude.exe",
                                "pid": 20712
                            }
                        }
                    ],
                    "severity": 35,
                    "stellar": {
                        "detection_time": 80872,
                        "status": "New"
                    },
                    "stellar_da_input": 25227,
                    "stellar_index_id": "aella-ser-2026.09.24-e511c3fc54cd4d668bb67612c2ef4b04",
                    "stellar_uuid": "02e3d1e5-b32b-46f5-b2fe-ba74c0d3889e1790266421703-YWVsbGEtc2VyLTIwMjYuMDkuMjQtZTUxMWMzZmM1NGNkNGQ2NjhiYjY3NjEyYzJlZjRiMDQ=",
                    "tenant_name": "technoma",
                    "tenantid": "e511c3fc54cd4d668bb67612c2ef4b04",
                    "threat_score": 0,
                    "timestamp": 1790265997328,
                    "timestamp_utc": "2026-09-24T16:06:37.000Z",
                    "totalbytes": 0,
                    "totalpackets": 0,
                    "user_list": [
                        {
                            "name": "TECHNOMA\\josemarin"
                        }
                    ],
                    "write_by": "sef",
                    "write_time": 1790266421703,
                    "xdr_event": {
                        "description": "Palo Alto Networks Cortex XDR Analytics BIOC detected \"powershell runs suspicious base64-encoded commands\" on host \"NB-JMARIN\" (\"192.168.169.69\"). The behavioral analytics system identified this \"execution\" threat through rule \"5daf5724-8e0a-4514-85d4-431bf4b193be\" with status \"matched\". The suspicious behavior involved \"powershell.exe\" executed by user \"TECHNOMA\\josemarin\". Analytics details: \"The process claude.exe execute the process powershell.exe with a long Base64-encoded command. This command line was seen on 2 different endpoints and on 3 unique days in the last 30 days\". Agent version \"8.5.0.624\" on \"Windows\" (\"Windows 11 [10.0 (Build 26200)]\") \"detected\" this analytics threat.",
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
```
