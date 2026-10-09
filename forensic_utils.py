"""
Utilidades compartidas para la higienización forense y manipulación de datos JSON.
Implementa el patrón DRY y mejora la complejidad algorítmica de listas a frozensets (O(N) -> O(1)).
"""

from typing import Union, Dict, List, Any

# Frozenset de campos permitidos - O(1) lookup, construido UNA vez a nivel de módulo.
CORE_FIELDS = frozenset([
    "srcip", "dstip", "action", "policyname", "appid_name", "event_description", "parser_raw_msg",
    "process_name", "command", "process_path", "process_cmdline", "parent_process_name", "parent_process_cmdline",
    "dst_host", "dns_query", "dns_name", "domain", "dstport", "srcport", "username", "user_name", "user", "hostname", "host_name",
    "reputation", "process_reputation", "file_reputation", "ip_reputation", "severity", "fidelity",
    "filename", "file_name", "file_path", "md5", "sha256", "event_name", "event_type", "event_category",
    "metadata", "request", "response", "query", "query_type", "answers", "host", "host_addr", "host_type", "reply_code",
    "tunnel_domain", "tunnel_payloads", "tunnel_type", "total_entropy", "xdr_event", "description", "display_name", "name",
    "detected_fields", "detected_values", "domain_list", "domain_reputation", "srcip_host", "dstip_host",
    "actual", "typical", "dev_class", "dev_type", "device", "fortinet", "dstinetsvc", "dstintf", "dstintfrole",
    "srcintf", "srcintfrole", "srcname", "devid", "sessionid", "msg_data", "strvalue",
    "anomaly_tag", "audit_status", "cwd", "parent_proc_name", "parent_child", "process_user", "secondary",
    "program_name", "path", "engid_gateway", "engid_device_class", "engid_device_desc", "agent", "ephemeral_id", "tty",
    "accumulated_anomalous_failures", "event_id", "log_name", "login_result", "login_type", "task", "service_id",
    "event_data", "Status", "ServiceName", "TargetUserName", "TargetDomainName", "IpAddress", "IpPort",
    "TicketEncryptionType", "PreAuthEncryptionType", "wineventlog_version", "weighted_anomaly_score", "keywords", "opcode",
    "inbytes_delta", "inbytes_total", "outbytes_delta", "outbytes_total", "inpkts_delta", "inpkts_total", "outpkts_delta", "outpkts_total",
    "totalbytes", "totalpackets", "resolved_ips", "domain_creation", "effective_tld", "dga_score", "ttl", "transaction_id",
    "anomaly_id", "lateral", "_detection_id", "ath_info", "ath_deduplication", "group", "authserver", "vpntype", "srcmac", "dstmac",
    "sophos", "computer_name", "dms_job_id", "endpoint_id", "endpoint_type", "customer_id", "user_id", "source_info", "user_action", "location",
    "last_modified_ts", "starred", "filter_rule_id", "org_id", "event_source", "data", "is_whitelisted", "_index",
    "actor_process_signature_vendor", "device_product_id", "local_insert_ts", "timestamp_utc", "technique", "threat", "processor",
    "alert_id", "device_vendor_name", "actor_process_causality_id", "_version", "orig_id", "os_actor_process_os_pid",
    "action_process_signature_vendor", "hash", "association_strength", "actor_process_image_name", "os_actor_process_instance_id",
    "contains_featured_host", "bioc_indicator", "process_list", "causality_actor_process_signature_status", "orig_index",
    "action_process_image_sha256", "tags", "agent_version", "type", "id", "_primary_term", "source", "vendor", "deduplicate_tokens",
    "causality_actor_process_image_name", "variation_rule_id", "agent_fqdn", "event_sub_type", "fw_is_phishing", "agent_device_domain",
    "framework_version", "agent_os_type", "parent", "stellar", "mitre_technique_id_and_name", "ip", "device_type", "external_id",
    "tenantid", "_source", "events", "case_id", "write_time", "category", "_type", "command_line", "alert_domain",
    "action_process_image_command_line", "agent_data_collection_status", "causality_actor_process_image_path",
    "os_actor_process_signature_status", "action_process_causality_id", "actor_process_instance_id", "os_actor_thread_thread_id",
    "causality_actor_process_command_line", "msg_class", "engid_name", "xdr_killchain_stage", "locid", "found", "attempt_counter",
    "mac_addresses", "original_tags", "stellar_uuid", "event_status", "agent_host_boot_time", "cloud_provider", "actor_process_image_sha256",
    "contains_featured_user", "msg_origin", "action_pretty", "device_vendor_id", "causality_actor_process_signature_vendor",
    "alert_type", "ttps", "contains_featured_ip", "actor_process_signature_status", "end_match_attempt_ts", "agent_ip_addresses_v6",
    "event", "actor_causality_id", "timestamp", "dynamic_fields", "resolution_status", "severity_str", "device_serial_number",
    "action_process_image_name", "malicious_urls", "scope", "write_by", "engid", "os_actor_process_causality_id",
    "detection_timestamp", "event_score", "dscp_name", "_id", "stellar_index_id", "tactic", "causality_actor_process_image_sha256",
    "os_actor_process_command_line", "executable", "palo_alto_networks", "os_actor_process_image_path", "resolution_comment",
    "action_country", "matching_status", "os_actor_process_image_sha256", "pid", "docs", "aella_tuples", "action_process_signature_status",
    "msgtype_name", "agent_install_type", "matching_service_rule_id", "causality_actor_process_execution_time",
    "os_actor_process_image_name", "actor_process_os_pid", "detection_time", "actor_process_image_path", "causality_actor_causality_id",
    "os_actor_process_signature_vendor", "status", "actor_thread_thread_id", "threat_score", "bioc_category_enum_key",
    "event_timestamp", "mitre_tactic_id_and_name", "xdr_killchain_version", "is_pcap", "tenant_name", "actor_process_command_line",
    "user_list", "_seq_no", "appid_stdport", "agent_os_sub_type", "netid_name", "stellar_da_input", "netid",
    "causality_actor_process_image_md5", "actor_process_image_md5", "action_process_instance_id", "mac", "host_ip",
    "duration", "time_window_ms", "last_user", "fw_policy_id", "eventtype", "last_time_utc", "appid_family", "policytype", "port_name", "is_tunneling",
    "srcip_reputation", "orig_write_time", "srccountry", "message_type", "_whitelist", "alert_timestamp_field", "orig_timestamp_utc", "srcip_assetid",
    "latitude", "feature", "action_time", "history", "src_tuples", "dstcountry", "cat", "date", "city", "subtype", "longitude", "log", "appid",
    "countryName", "srcuuid", "eventtime", "last_timestamp", "msgtype", "catdesc", "advanced", "rule_name", "repeat_count", "direction",
    "region", "processing_time", "httpmethod", "syslog", "logid", "start_bucket_time", "srcip_geo_point", "url_reputation_source", "last_action",
    "last_modified", "rule_id", "dstip_reputation_source", "srcip_geo", "stellar_index", "tz", "scheduled_time_utc", "proto_name", "utm",
    "event_time", "action_user", "first_timestamp", "receive_time", "is_dga", "dstip_reputation", "poluuid", "countryCode", "srcip_geo_source",
    "flags", "dstip_asn_org", "alert_time", "stellar_client_addr", "msg", "time", "dstip_geo", "url", "end_bucket_time", "dstip_asn",
    "dstip_geo_point", "state", "profile", "proto", "dstuuid", "vd", "reqtype", "first_time_utc", "summary_start", "srcip_type", "dev_name",
    "service", "section_type", "dstip_version", "stellar_ingestion_port", "level", "req_domain_name", "url_list", "end_reason", "flow_score",
    "anomaly_tag_subtype", "url_reputation", "tos", "obsid", "dstip_type", "srcip_version", "response_time", "vlan", "summary_end", "org_name",
    "ratemethod", "priority", "scheduled_timestamp", "orig_timestamp",
    "pkts_toclient", "handler", "detector_index", "signature", "start", "write_time_utc", "src_ip", "created_ts", "smb_path_list", "seen_traffic_id",
    "original_event", "seen_traffic_index", "rrname", "days_silent", "dst_tuples", "indices", "performance_impact", "tenant_info", "flow", "exploit",
    "cust_file", "attack_target", "dns", "exploit_id", "smb_username_count", "bytes_toclient", "fileid", "payload_details", "file_extract_timestamp",
    "created_at", "gid", "confidence", "dstip_assetid", "tcp_rtt", "readable_name", "rrtype", "smb_path_summary", "src_port", "srcip_sig_id", "score",
    "correlation_info", "app_proto", "key", "dest_port", "signature_id", "seen_traffic", "dest_ip", "exploit_index", "pkts_toserver", "index",
    "nt_status", "updated", "query_name", "new_file", "tx_id", "ids", "rule", "bytes_toserver", "value", "reviewed_at", "event_summary", "alert_to_last",
    "updated_at", "affected_product", "signature_severity", "version", "run_every", "deployment", "rev", "created"
])

def clean_forensic_data(data: Union[Dict[str, Any], List[Any], Any], depth: int = 0, max_depth: int = 10) -> Union[Dict[str, Any], List[Any], None]:
    if not isinstance(data, (dict, list)):
        return data
    if depth > max_depth:
        return None
        
    if isinstance(data, list):
        result = []
        for item in data:
            cleaned = clean_forensic_data(item, depth + 1, max_depth)
            if cleaned is not None:
                result.append(cleaned)
        return result
        
    elif isinstance(data, dict):
        cleaned = {}
        # Filtrado optimizado: O(1) usando frozenset global en lugar de recrear lista local
        # Filtrado optimizado: O(K) iterando directamente sobre data
        for k, v in data.items():
            if k in CORE_FIELDS:
                cleaned[k] = v
            elif isinstance(v, (dict, list)):
                res = clean_forensic_data(v, depth + 1, max_depth)
                if res is not None and res != {} and res != []:
                    cleaned[k] = res
                    
        return cleaned if cleaned else None
        
    return None
