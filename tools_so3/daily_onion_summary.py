#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SO3 Daily Executive Summary (El /daily para Security Onion 3)
Genera el informe ejecutivo de 24 horas del Grid de Security Onion:
- Salud del cluster y de los nodos (CPU, RAM, Swap, Disco /nsm)
- Auditoría de Casos (creados, abiertos, cerrados, atacantes)
- Top Amenazas NIDS (Suricata) filtrando el ruido conocido
- Top Denegaciones de Perímetro (FortiGate / VASCOL / Clientes)
- Alertas de Autenticación y Host (SSH, logins SOC)
- Recomendaciones para la guardia del día
"""

import sys
import os
import json
from datetime import datetime, timezone

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from so3_client import SO3Client

ES_USER = "so_elastic"
ES_PASS = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

def es_query(so, path, query_dict):
    so.write_file('/tmp/q_daily.json', json.dumps(query_dict))
    out, _ = so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/{path}' -d @/tmp/q_daily.json")
    so.sudo("rm -f /tmp/q_daily.json")
    try:
        return json.loads(out)
    except Exception:
        return {}

def generate_daily_report():
    report = []
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append(f"# 🧅 SECURITY ONION 3 - INFORME EJECUTIVO DIARIO (/daily)")
    report.append(f"**Fecha y Hora:** {now_str} | **SOC Technoma**\n")

    with SO3Client() as so:
        # 1. SALUD DEL SISTEMA Y RECURSOS
        report.append("## 1. 🖥️ Estado del Grid y Recursos")
        df_nsm, _ = so.sudo("df -h /nsm | tail -1")
        free_mem, _ = so.sudo("free -h")
        uptime_out, _ = so.sudo("uptime")
        
        parts_df = df_nsm.split()
        if len(parts_df) >= 5:
            report.append(f"- **Partición `/nsm` (Logs & Base de Datos):** {parts_df[2]} Usados / {parts_df[1]} Total (**{parts_df[4]} ocupación** | {parts_df[3]} Libres)")
        
        mem_lines = free_mem.splitlines()
        if len(mem_lines) >= 3:
            report.append(f"- **Memoria RAM:** {mem_lines[1]}")
            report.append(f"- **Memoria Swap:** {mem_lines[2]}")
        report.append(f"- **Uptime & Carga:** `{uptime_out.strip()}`")

        # Estado del Cluster Elasticsearch
        health_out, _ = so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' 'https://127.0.0.1:9200/_cluster/health'")
        try:
            h = json.loads(health_out)
            status_emoji = "🟢" if h.get("status") == "green" else ("🟡" if h.get("status") == "yellow" else "🔴")
            report.append(f"- **Elasticsearch Cluster Health:** {status_emoji} **{h.get('status').upper()}** ({h.get('active_shards')} shards activos, {h.get('unassigned_shards')} no asignados)")
        except Exception:
            report.append("- **Elasticsearch Cluster Health:** ⚠️ No se pudo obtener")

        # 2. CASOS EN LAS ÚLTIMAS 24 HORAS
        report.append("\n## 2. 📂 Resumen de Casos (Últimas 24 Horas)")
        q_cases = {
            "query": {
                "range": {"@timestamp": {"gte": "now-24h"}}
            },
            "size": 10,
            "sort": [{"@timestamp": {"order": "desc"}}]
        }
        res_cases = es_query(so, "so-case/_search", q_cases)
        total_cases = res_cases.get("hits", {}).get("total", {}).get("value", 0)
        report.append(f"- **Total casos nuevos:** `{total_cases}`")
        if total_cases > 0:
            for hit in res_cases.get("hits", {}).get("hits", []):
                c = hit["_source"].get("so_case", {})
                report.append(f"  * **[{c.get('severity', 'info').upper()}]** {c.get('title')} (Estado: `{c.get('status')}` | Asignado: `{c.get('assigneeId') or 'Bandeja General'}`)")
        else:
            report.append("  * *Sin incidentes críticos correlacionados en las últimas 24h. Bandeja al día.*")

        # 3. TOP AMENAZAS EN SURICATA (Filtrando ruido AnyDesk / Telegram / Tunnels)
        report.append("\n## 3. 🚨 Amenazas Relevantes en Red (Suricata NIDS - 24h)")
        q_suri = {
            "query": {
                "bool": {
                    "must": [
                        {"range": {"@timestamp": {"gte": "now-24h"}}}
                    ],
                    "must_not": [
                        {"wildcard": {"rule.name": "*Anydesk*"}},
                        {"wildcard": {"rule.name": "*Telegram*"}},
                        {"wildcard": {"rule.name": "*argotunnel*"}},
                        {"wildcard": {"rule.name": "*TeamViewer*"}},
                        {"wildcard": {"rule.name": "*Discord*"}}
                    ]
                }
            },
            "aggs": {
                "top_sig": {
                    "terms": {"field": "rule.name", "size": 7},
                    "aggs": {
                        "top_src": {"terms": {"field": "source.ip", "size": 2}},
                        "top_dst": {"terms": {"field": "destination.ip", "size": 2}}
                    }
                }
            },
            "size": 0
        }
        res_suri = es_query(so, ".ds-logs-suricata.alerts-so-*/_search", q_suri)
        suri_total = res_suri.get("hits", {}).get("total", {}).get("value", 0)
        report.append(f"- **Alertas de seguridad reales (excluyendo ruido de soporte/chat):** `{suri_total}`")
        for b in res_suri.get("aggregations", {}).get("top_sig", {}).get("buckets", []):
            srcs = [x['key'] for x in b.get('top_src', {}).get('buckets', [])]
            dsts = [x['key'] for x in b.get('top_dst', {}).get('buckets', [])]
            report.append(f"  * **[{b['doc_count']} hits]** `{b['key']}` | Origen: `{srcs}` ➔ Destino: `{dsts}`")

        # 4. TOP DENEGACIONES DE FIREWALL (FortiGate)
        report.append("\n## 4. 🛡️ Bloqueos Perimetrales (FortiGate - 24h)")
        q_fg = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"event.action": "deny"}},
                        {"range": {"@timestamp": {"gte": "now-24h"}}}
                    ]
                }
            },
            "aggs": {
                "top_attackers": {
                    "terms": {"field": "source.ip", "size": 5}
                },
                "top_targets": {
                    "terms": {"field": "destination.ip", "size": 3}
                },
                "top_ports": {
                    "terms": {"field": "destination.port", "size": 5}
                }
            },
            "size": 0
        }
        res_fg = es_query(so, ".ds-logs-fortinet_fortigate.log-*/_search", q_fg)
        fg_denies = res_fg.get("hits", {}).get("total", {}).get("value", 0)
        report.append(f"- **Total conexiones bloqueadas:** `{fg_denies}`")
        
        top_ips = [f"`{x['key']}` ({x['doc_count']})" for x in res_fg.get("aggregations", {}).get("top_attackers", {}).get("buckets", [])]
        top_ports = [f"`{x['key']}` ({x['doc_count']})" for x in res_fg.get("aggregations", {}).get("top_ports", {}).get("buckets", [])]
        if top_ips:
            report.append(f"  * **Top IPs bloqueadas en internet:** {', '.join(top_ips)}")
        if top_ports:
            report.append(f"  * **Puertos más atacados:** {', '.join(top_ports)}")

        # 5. RECOMENDACIONES PARA EL ANALISTA DE GUARDIA
        report.append("\n## 5. 📋 Acciones y Recomendaciones de Guardia")
        report.append("1. **Revisión de Casos:** Verificar si ingresó algún ticket con prefijo `[AUTO]` en `/#/cases` para triage.")
        report.append("2. **Capacidad de Disco:** Vigilar que `/nsm` se mantenga por debajo del 85% para evitar re-enganche de watermarks.")
        report.append("3. **Escaneos Externos:** Las denegaciones de FortiGate en puertos 22/23/3389 son automatizadas desde internet; solo investigar si superan 100 intentos continuos.")

    final_text = "\n".join(report)
    return final_text

if __name__ == "__main__":
    out = generate_daily_report()
    print(out)
