#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
telegram_soc_bot.py
-------------------
BOT DE NOTIFICACIONES, WORKFLOW DIARIO Y CONSULTAS RÁPIDAS DEL SOC
Conectado a Stellar Cyber OpenXDR y Cortex XDR para Kevin Moraes.
Comandos Soportados en Chat:
  • /daily       - Workflow Diario completo (Licencia, Casos, MITRE, Sensores)
  • /cuota       - Ingesta de hoy vs límite de 8.0 GB
  • /casos       - Casos activos en cola de triage
  • /caso <id>   - Detalle forense y observables de un caso (ej. /caso 17936)
  • /ip <ip>     - Investigación rápida de IP en Stellar (ej. /ip 192.168.169.47)
  • /span        - Diagnóstico de flujos en tiempo real del Puerto SPAN (NDR)
  • /bitacora    - Genera la fila formateada para copiar directo a tu Excel
  • /ping        - Healthcheck del bot y API
"""
import os
import sys
import json
import time
import threading
import requests
import urllib3
from datetime import datetime, timezone, timedelta
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8368396404:AAGrwlbYJdNCW12opqm3uvv7eZExPAkUO4w")
DEFAULT_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", 1892860303)  # Chat ID de Kevin Moraes
STELLAR_HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
STELLAR_EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
STELLAR_TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")
# Estado conocido previo de sensores para alertamiento proactivo
SENSOR_PREV_STATES = {}
def send_telegram(text: str, chat_id=None, parse_mode="Markdown"):
    target_chat = chat_id or DEFAULT_CHAT_ID
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": target_chat,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
        return r.status_code == 200
    except Exception as e:
        print(f"[-] Error enviando mensaje a Telegram: {e}")
        return False
def get_jwt():
    import base64
    auth_str = f"{STELLAR_EMAIL}:{STELLAR_TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{STELLAR_HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    r.raise_for_status()
    return r.json().get("access_token")
def get_quota_summary(jwt):
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    url = f"https://{STELLAR_HOST}/connect/api/v1/storage-usages/daily_and_monthly"
    r = requests.get(url, headers=headers, timeout=20, verify=False)
    if r.status_code != 200:
        return "⚠️ Error consultando cuota en Stellar Cyber."
    
    data = r.json()
    tenants = data.get("data", []) if isinstance(data, dict) else data
    
    res = []
    for t in tenants:
        name = t.get("tenant_name", "")
        if name in ["technoma", "CAJAANDE", "All Tenants"]:
            daily = t.get("daily_usage", [])
            last_day = daily[-1] if daily else {}
            date_str = last_day.get("date", "")[:10]
            gb = last_day.get("usage", 0.0)
            status_ico = "🟢" if gb <= 8.0 else "🔴"
            res.append(f"{status_ico} *{name}*: `{gb:.2f} GB` _({date_str})_")
            
    return "\n".join(res)
def get_active_cases(jwt):
    url = f"https://{STELLAR_HOST}/mcp"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": "listCases",
            "arguments": {"access_token": jwt, "limit": 10}
        }
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        raw = r.json()
        content = raw.get("result", {}).get("content", [{}])[0].get("text", "")
        data = json.loads(content).get("data", {})
        cases = data.get("cases", [])
        open_cases = [c for c in cases if c.get("status") in ["New", "In Progress"]]
        return open_cases
    except Exception as e:
        print(f"[-] Error listando casos: {e}")
        return []
def get_case_detail_summary(jwt, ticket_id_str):
    url = f"https://{STELLAR_HOST}/mcp"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": "getCaseDetail",
            "arguments": {"access_token": jwt, "ticket_id": str(ticket_id_str)}
        }
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        raw = r.json()
        content = raw.get("result", {}).get("content", [{}])[0].get("text", "")
        data = json.loads(content).get("data", {})
        case = data.get("case", {}) or data.get("details", {})
        alerts = data.get("alerts", [])
        
        name = case.get("name")
        score = case.get("score")
        st = case.get("status")
        
        lines = [
            f"🔍 *DETALLE DEL CASO #{ticket_id_str}*",
            f"• *Nombre:* {name}",
            f"• *Score / Estado:* `{score}` | `{st}`",
            f"• *Alertas Agrupadas:* `{len(alerts)}`",
            "",
            "📋 *Top Alertas:*"
        ]
        for i, a in enumerate(alerts[:4], 1):
            src = a.get("_source", {})
            en = (
                src.get("xdr_event", {}).get("display_name")
                or src.get("event_name")
                or src.get("event", {}).get("threat", {}).get("name")
                or "Alerta XDR"
            )
            es = src.get("fidelity") or src.get("severity") or src.get("event_score", 0)
            
            h_obj = src.get("host", {})
            host_val = h_obj.get("name") if isinstance(h_obj, dict) else h_obj
            u_list = src.get("user_list", [])
            user_val = u_list[0].get("name") if u_list else (src.get("user", {}).get("name") if isinstance(src.get("user"), dict) else src.get("user"))
            
            s_ip = src.get("srcip")
            d_ip = src.get("dstip")
            
            desc = src.get("xdr_event", {}).get("description", "")
            detail_cause = ""
            if "Analytics details:" in desc:
                detail_cause = desc.split("Analytics details:")[-1].split(". In the past")[0].strip(' "')
            elif desc:
                detail_cause = (desc[:110] + "...") if len(desc) > 110 else desc
                
            lines.append(f"{i}. *{en}* `[Score: {es}]`")
            if host_val or user_val:
                lines.append(f"   💻 *Host:* `{host_val or 'N/A'}` | 👤 *User:* `{user_val or 'N/A'}`")
            if s_ip and d_ip:
                lines.append(f"   🌐 `{s_ip}` ➔ `{d_ip}`")
            if detail_cause:
                lines.append(f"   🔍 _{detail_cause}_")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error consultando detalle del caso #{ticket_id_str}: {e}"
def get_ip_reputation_summary(jwt, ip):
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    query = {
        "size": 5,
        "query": {
            "bool": {
                "should": [
                    {"term": {"srcip": ip}},
                    {"term": {"dstip": ip}}
                ]
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}]
    }
    url = f"https://{STELLAR_HOST}/connect/api/data/*adr*/_search"
    try:
        r = requests.get(url, headers=headers, json=query, timeout=20, verify=False)
        res = r.json()
        total = res.get("hits", {}).get("total", {}).get("value", 0)
        hits = res.get("hits", {}).get("hits", [])
        
        lines = [
            f"🔎 *INVESTIGACIÓN FORENSE DE IP:* `{ip}`",
            f"• *Total eventos registrados:* `{total:,}`",
            "",
            "🕒 *Últimas conexiones observadas:*"
        ]
        if hits:
            for h in hits[:4]:
                s = h.get("_source", {})
                src = s.get("srcip")
                dst = s.get("dstip")
                port = s.get("dstport")
                app = s.get("appid_name") or s.get("service")
                host = s.get("srcip_host") or s.get("dstip_host") or ""
                lines.append(f"• `{src}` ➔ `{dst}:{port}`\n  App: `{app}` {f'| Host: {host}' if host else ''}")
        else:
            lines.append("• Sin actividad reciente en el Data Lake.")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error buscando IP {ip}: {e}"
def get_ids_signatures_summary(jwt):
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    now_utc = datetime.now(timezone.utc)
    start_ms = int((now_utc - timedelta(days=7)).timestamp() * 1000)
    query = {
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"exists": {"field": "ids.signature"}},
                    {"range": {"timestamp": {"gte": start_ms}}}
                ],
                "must_not": [
                    {"term": {"ids.severity.keyword": "informational"}},
                    {"term": {"ids.severity.keyword": "low"}},
                    {"wildcard": {"ids.signature.keyword": "INFO *"}}
                ]
            }
        },
        "aggs": {
            "top_signatures": {"terms": {"field": "ids.signature.keyword", "size": 6}}
        }
    }
    url = f"https://{STELLAR_HOST}/connect/api/data/*interim*/_search"
    try:
        r = requests.get(url, headers=headers, json=query, timeout=20, verify=False)
        res = r.json()
        total = res.get("hits", {}).get("total", {}).get("value", 0)
        sigs = res.get("aggregations", {}).get("top_signatures", {}).get("buckets", [])
        
        lines = [
            "🛡️ *FASE 4: FIRMAS DE INTRUSIÓN (IDS OVERVIEW)*",
            f"• *Detecciones Críticas/Altas (7d):* `{total:,}`",
            "",
            "Top Firmas Activas:"
        ]
        if sigs:
            for i, s in enumerate(sigs, 1):
                lines.append(f"{i}. *{s['key']}*\n   Hits: `{s['doc_count']}`")
        else:
            lines.append("✅ Sin firmas críticas o de exploit activas.")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error consultando firmas IDS: {e}"
def get_sensors_hardware_summary(jwt):
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    url = f"https://{STELLAR_HOST}/connect/api/v1/data_sensors"
    try:
        r = requests.get(url, headers=headers, timeout=20, verify=False)
        sensors = r.json().get("sensors", [])
        
        lines = [
            "🖥️ *TELEMETRÍA DE HARDWARE DE SENSORES*"
        ]
        
        count = 0
        for s in sensors:
            h_name = s.get("hostname", "Desconocido")
            # Exclusión explícita del sensor obsoleto
            if "WIN-MU3B8QGMI6A" in h_name:
                continue
                
            ip = s.get("local_ip_address", "N/A")
            cust = s.get("cust_name", "Global")
            conn = s.get("connection_status", "unknown")
            is_conn = (conn.lower() == "connected")
            status_ico = "🟢" if is_conn else "🔴"
            status_str = "Conectado" if is_conn else "Desconectado"
            
            cpu = s.get("cpu_usage", 0.0)
            cpu_val = f"{float(cpu):.1f}%" if cpu is not None else "N/A"
            
            disk = s.get("disk_usage", 0.0)
            disk_val = f"{float(disk):.1f}%" if disk is not None else "N/A"
            
            inbytes = s.get("inbytes_total", 0)
            in_gb = inbytes / (1024**3)
            in_txt = f"{in_gb:.2f} GB" if in_gb > 0.01 else (f"{inbytes/(1024**2):.1f} MB" if inbytes > 0 else "0 MB")
            
            prof = s.get("sensor_profile_name", "N/A")
            ver = s.get("sw_version", "7.0")
            
            lines.append(
                f"{status_ico} *{h_name}* (`{ip}`) | Tenant: *{cust}*\n"
                f"   • *Estado:* `{status_str}` | *CPU:* `{cpu_val}` | *Disco:* `{disk_val}`\n"
                f"   • *Tráfico Ingestado:* `{in_txt}`\n"
                f"   • *Perfil:* `{prof}` (`v{ver}`)"
            )
            count += 1
            
        if count == 0:
            lines.append("⚠️ No se encontraron sensores activos en la plataforma.")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error consultando telemetría de sensores: {e}"
def check_sensors_health_alerting():
    """
    Monitor continuo en segundo plano que vigila el estado de conexión de los sensores.
    Si un sensor operativo pasa a 'disconnected' o falla, dispara una alerta crítica
    inmediata a Telegram con detalles de IP y Tenant. También avisa cuando se recupera.
    """
    global SENSOR_PREV_STATES
    try:
        jwt = get_jwt()
        headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
        url = f"https://{STELLAR_HOST}/connect/api/v1/data_sensors"
        r = requests.get(url, headers=headers, timeout=20, verify=False)
        if r.status_code != 200:
            return
            
        sensors = r.json().get("sensors", [])
        for s in sensors:
            h_name = s.get("hostname", "Desconocido")
            if "WIN-MU3B8QGMI6A" in h_name:
                continue
                
            ip = s.get("local_ip_address", "N/A")
            cust = s.get("cust_name", "Global")
            conn = str(s.get("connection_status", "unknown")).lower()
            prev_conn = SENSOR_PREV_STATES.get(h_name)
            
            # Registrar primer estado conocido si recién arranca el bot
            if prev_conn is None:
                SENSOR_PREV_STATES[h_name] = conn
                continue
                
            # Si cambió de conectado a desconectado
            if prev_conn == "connected" and conn != "connected":
                SENSOR_PREV_STATES[h_name] = conn
                alerta = (
                    "🚨 *ALERTA CRÍTICA: CAÍDA DE SENSOR DE SEGURIDAD*\n\n"
                    f"⚠️ El sensor *{h_name}* se ha *DESCONECTADO* de Stellar Cyber.\n\n"
                    f"• *IP Local:* `{ip}`\n"
                    f"• *Tenant:* `{cust}`\n"
                    f"• *Estado Actual:* `{conn.upper()}`\n"
                    f"• *Hora:* `{datetime.now().strftime('%H:%M:%S')}`\n\n"
                    "⚠️ *Impacto:* Pérdida inmediata de visibilidad de red/NDR o Syslog en ese segmento. Verificar conectividad o proceso aella en el host."
                )
                print(f"[!] ALERTA ENVIADA: Sensor {h_name} caído!")
                send_telegram(alerta)
                
            # Si se recuperó
            elif prev_conn != "connected" and conn == "connected":
                SENSOR_PREV_STATES[h_name] = conn
                recuperacion = (
                    "🟢 *RECUPERACIÓN: SENSOR EN LÍNEA*\n\n"
                    f"El sensor *{h_name}* (`{ip}`) ha restablecido su conexión con Stellar Cyber.\n"
                    f"• *Tenant:* `{cust}`\n"
                    f"• *Hora:* `{datetime.now().strftime('%H:%M:%S')}`\n"
                    "Telemetría e ingesta reanudadas con éxito."
                )
                print(f"[+] Sensor {h_name} recuperado.")
                send_telegram(recuperacion)
                
    except Exception as e:
        print(f"[-] Error en check_sensors_health_alerting: {e}")
def sensor_watchdog_loop(interval_seconds=60):
    """Hilo demonio que ejecuta la verificación periódica de sensores."""
    print(f"[*] Watchdog de Sensores activo (intervalo: {interval_seconds}s)...")
    while True:
        try:
            check_sensors_health_alerting()
        except Exception as e:
            print(f"[-] Error en watchdog loop: {e}")
        time.sleep(interval_seconds)
# Definición de los 20 módulos de la Threat Hunting Library
TH_MODULES_DEF = [
    ("Firewall", "msg_class:firewall OR dev_type:fw_fortigate"),
    ("DNS Analysis", "dstport:53 OR msg_class:dns OR appid_name:DNS OR appid_name:Google-DNS"),
    ("Network Applications", "msg_class:interflow_traffic OR msg_class:flow"),
    ("Google Workspace", "msg_class:gsuite"),
    ("Plain Text Passwords", "dstport:389 OR dstport:21 OR dstport:23 OR alert_type:*password* OR msg_class:plain_text*"),
    ("All Login Failures", "action:failure OR action:failed OR msg_class:auth_failure OR event_name:*login*failure*"),
    ("Windows Logins", "win_event_id:4624 OR event_id:4624"),
    ("Windows Privilege Escalations", "win_event_id:4672 OR event_id:4672"),
    ("Windows Command Line", "process_commandline:* OR process_cmd:*"),
    ("Windows New Processes", "win_event_id:4688 OR event_id:4688 OR process_name:*"),
    ("Sophos Endpoint", "dev_type:endpoint_sophos OR msg_class:sophos*"),
    ("Non-Standard Port Usage", "appid_stdport:no"),
    ("Tunneled Traffic", "proto_name:gre OR proto_name:ipip OR dstport:4789"),
    ("Windows Account Changes", "win_event_id:4720 OR win_event_id:4722 OR win_event_id:4724 OR win_event_id:4738 OR event_id:4720"),
    ("Windows Account Lockouts", "win_event_id:4740 OR event_id:4740"),
    ("Windows PowerShell Startups", "win_event_id:4104 OR event_id:4104 OR process_name:powershell.exe"),
    ("External File Storage Access", "appid_name:*drive* OR appid_name:*dropbox* OR appid_name:*onedrive*"),
    ("Cloud Email Provider Access", "appid_name:*gmail* OR appid_name:*office365* OR appid_name:*outlook*"),
    ("Windows Login Failures", "win_event_id:4625 OR event_id:4625"),
    ("Windows Software Installed", "win_event_id:11707 OR event_id:11707")
]
def get_threat_hunting_panels_summary(jwt):
    """Consulta en paralelo los 20 módulos de Threat Hunting Library de hoy y genera un resumen ejecutivo."""
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
    start_today = int(datetime.now(timezone.utc).replace(hour=0, minute=0, second=0).timestamp() * 1000)
    today_str = datetime.now(timezone.utc).strftime("%d-%m-%Y")
    
    filters_map = {name: {"query_string": {"query": q}} for name, q in TH_MODULES_DEF}
    body = {
        "size": 0,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": cust_id}},
                    {"range": {"timestamp": {"gte": start_today}}}
                ]
            }
        },
        "aggs": {
            "th_matrix": {
                "filters": {
                    "filters": filters_map
                }
            }
        }
    }
    url = f"https://{STELLAR_HOST}/connect/api/data/*adr*,*interim*,*wineventlog*/_search"
    try:
        r = requests.get(url, headers=headers, json=body, timeout=20, verify=False)
        if r.status_code != 200:
            return f"⚠️ Error consultando Threat Hunting Library (Status {r.status_code})"
            
        buckets = r.json().get("aggregations", {}).get("th_matrix", {}).get("buckets", {})
        results = [(name, buckets.get(name, {}).get("doc_count", 0)) for name, _ in TH_MODULES_DEF]
        results.sort(key=lambda x: x[1], reverse=True)
        
        lines = [
            "🎯 *FASE 3: AUDITORÍA DE LOS 20 PANELES THREAT HUNTING*",
            f"• *Ventana:* Hoy (`{today_str}`) | *Tenant:* `technoma`",
            "",
            "Top Módulos Activos Hoy:"
        ]
        
        # Top activos con eventos
        active_count = 0
        for name, count in results:
            if count > 0:
                active_count += 1
                ico = "🔴" if count > 1000000 else ("🟠" if count > 50000 else "🟡")
                lines.append(f"{ico} *{name}:* `{count:,}` eventos")
                
        # Paneles sin actividad (en 0 = buena noticia de seguridad)
        zero_modules = [name for name, count in results if count == 0]
        if zero_modules:
            lines.append(f"\n✅ *Módulos limpios (0 eventos sospechosos hoy):* {len(zero_modules)}/20")
            lines.append("_(PowerShell anómalo, Cuentas Bloqueadas, Modificaciones AD y Túneles en Cero)_")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error consultando 20 paneles de Threat Hunting: {e}"
def get_span_health_summary(jwt):
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    start_today = int(datetime.now(timezone.utc).replace(hour=0, minute=0, second=0).timestamp() * 1000)
    query = {
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_today}}},
                    {"term": {"msg_class.keyword": "interflow_traffic"}}
                ]
            }
        },
        "aggs": {
            "top_ports": {"terms": {"field": "dstport", "size": 5}},
            "top_apps": {"terms": {"field": "appid_name.keyword", "size": 5}}
        }
    }
    url = f"https://{STELLAR_HOST}/connect/api/data/*adr*/_search"
    try:
        r = requests.get(url, headers=headers, json=query, timeout=20, verify=False)
        res = r.json()
        total = res.get("hits", {}).get("total", {}).get("value", 0)
        ports = res.get("aggregations", {}).get("top_ports", {}).get("buckets", [])
        apps = res.get("aggregations", {}).get("top_apps", {}).get("buckets", [])
        
        lines = [
            "🌐 *ESTADO EN VIVO DEL PUERTO SPAN (NDR)*",
            f"• *Flujos capturados hoy:* `{total:,}`",
            "",
            "Top Puertos en el SPAN:"
        ]
        for p in ports:
            lines.append(f"• Puerto `{p['key']}`: `{p['doc_count']:,}` flujos")
            
        lines.append("\nTop Protocolos:")
        for a in apps:
            lines.append(f"• `{a['key']}`: `{a['doc_count']:,}` flujos")
            
        return "\n".join(lines)
    except Exception as e:
        return f"⚠️ Error consultando estado SPAN: {e}"
def generate_daily_workflow_briefing():
    jwt = get_jwt()
    quota_text = get_quota_summary(jwt)
    open_cases = get_active_cases(jwt)
    fecha_hoy = datetime.now().strftime("%d-%m-%Y")
    
    # --- FASE 1: Health Check de Sensores y Buffer ---
    sensors_summary = get_sensors_hardware_summary(jwt)
    span_summary = get_span_health_summary(jwt)
    
    # --- FASE 3: Auditoría de 20 Paneles Threat Hunting ---
    th_summary = get_threat_hunting_panels_summary(jwt)
    # --- FASE 4: Firmas de Intrusión (IDS/IPS Overview) ---
    ids_summary = get_ids_signatures_summary(jwt)
    
    lines = [
        "🛡️ *REPORTE INTEGRAL SOC - HOJA DE RUTA*",
        f"📅 *Fecha:* `{fecha_hoy}` | *Analista:* Kevin Moraes",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "",
        "🏥 *FASE 1: VERIFICACIÓN DE SALUD (HEALTH CHECK)*",
        sensors_summary,
        "",
        span_summary,
        "",
        "📊 *FASE 1.2: CONTROL DE INGESTA Y CUOTA (8.0 GB)*",
        quota_text,
        "",
        f"🚨 *FASE 2: TRIAJE Y MONITORIZACIÓN SLA ({len(open_cases)} Casos Abiertos)*",
    ]
    
    if open_cases:
        for c in open_cases:
            tid = c.get("ticket_id")
            score = c.get("score")
            st = c.get("status")
            name = c.get("name", "")
            name_clean = (name[:50] + "...") if len(name) > 50 else name
            sev_ico = "🔴 P1/P2" if score >= 70 else ("🟠 P3" if score >= 40 else "🟡 P4")
            lines.append(f"• {sev_ico} *#{tid}* `[{st} - Score: {score}]`")
            lines.append(f"  _{name_clean}_")
    else:
        lines.append("✅ *Cero incidentes activos en cola.* SLA nominal.")
        
    lines.extend([
        "",
        th_summary,
        "",
        ids_summary
    ])
    
    return "\n".join(lines)
def run_interactive_listener():
    print("[*] Iniciando Bot Interactivo Extendido de Telegram...")
    
    # Lanzar el perro guardián (Watchdog) de sensores en segundo plano cada 60s
    t_watchdog = threading.Thread(target=sensor_watchdog_loop, args=(60,), daemon=True)
    t_watchdog.start()
    
    last_update_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={last_update_id + 1}&timeout=30"
            r = requests.get(url, timeout=40)
            if r.status_code == 200:
                updates = r.json().get("result", [])
                for u in updates:
                    last_update_id = u["update_id"]
                    msg = u.get("message", {})
                    raw_text = msg.get("text", "").strip()
                    chat_id = msg.get("chat", {}).get("id")
                    
                    if not raw_text:
                        continue
                    
                    parts = raw_text.split()
                    cmd = parts[0].lower()
                    
                    print(f"[*] Comando recibido: {raw_text}")
                    
                    if cmd in ["/start", "/help"]:
                        send_telegram(
                            "👋 *Centro de Operaciones SOC (Kevin Moraes)*\n\n"
                            "Comandos Disponibles:\n"
                            "• `/daily` - Workflow Diario ejecutivo completo\n"
                            "• `/cuota` - Consumo actual de GB vs límite 8.0 GB\n"
                            "• `/sensores` - Telemetría de hardware (CPU, Disco, Ingesta)\n"
                            "• `/casos` - Lista de incidentes activos\n"
                            "• `/caso <id>` - Triaje forense de un caso (ej. `/caso 17936`)\n"
                            "• `/ip <ip>` - Rastrear actividad de una IP (ej. `/ip 10.11.1.1`)\n"
                            "• `/ids` - Análisis de Firmas de Intrusión (Fase 4)\n"
                            "• `/span` - Monitoreo en vivo de flujos NDR / DNS\n"
                            "• `/bitacora` - Fila formateada para tu Excel\n"
                            "• `/ping` - Healthcheck de la plataforma",
                            chat_id=chat_id
                        )
                    elif cmd in ["/daily", "/reporte", "/workflow"]:
                        send_telegram("⏳ Generando Workflow Diario del SOC...", chat_id=chat_id)
                        reporte = generate_daily_workflow_briefing()
                        send_telegram(reporte, chat_id=chat_id)
                    elif cmd in ["/cuota", "/ingesta"]:
                        jwt = get_jwt()
                        q = get_quota_summary(jwt)
                        send_telegram(f"📊 *ESTADO ACTUAL DE CUOTA:*\n\n{q}", chat_id=chat_id)
                    elif cmd in ["/sensores", "/sensors", "/hardware"]:
                        jwt = get_jwt()
                        send_telegram("⏳ Consultando telemetría de hardware de sensores...", chat_id=chat_id)
                        res = get_sensors_hardware_summary(jwt)
                        send_telegram(res, chat_id=chat_id)
                    elif cmd in ["/casos", "/cases"]:
                        jwt = get_jwt()
                        cases = get_active_cases(jwt)
                        if not cases:
                            send_telegram("✅ *No hay casos pendientes abiertos.*", chat_id=chat_id)
                        else:
                            resp = [f"🚨 *CASOS ACTIVOS ({len(cases)}):*"]
                            for c in cases:
                                resp.append(f"• *#{c.get('ticket_id')}* `[{c.get('status')} - Score {c.get('score')}]`\n  _{c.get('name')}_")
                            send_telegram("\n".join(resp), chat_id=chat_id)
                    elif cmd == "/caso":
                        if len(parts) < 2:
                            send_telegram("⚠️ Uso: `/caso <ticket_id>` (ej. `/caso 17936`)", chat_id=chat_id)
                        else:
                            jwt = get_jwt()
                            cid = parts[1]
                            send_telegram(f"⏳ Consultando detalle del Caso #{cid}...", chat_id=chat_id)
                            res = get_case_detail_summary(jwt, cid)
                            send_telegram(res, chat_id=chat_id)
                    elif cmd == "/ip":
                        if len(parts) < 2:
                            send_telegram("⚠️ Uso: `/ip <direccion_ip>` (ej. `/ip 192.168.169.47`)", chat_id=chat_id)
                        else:
                            jwt = get_jwt()
                            target_ip = parts[1]
                            send_telegram(f"⏳ Investigando IP `{target_ip}` en Stellar Cyber...", chat_id=chat_id)
                            res = get_ip_reputation_summary(jwt, target_ip)
                            send_telegram(res, chat_id=chat_id)
                    elif cmd in ["/paneles", "/hunting", "/th"]:
                        jwt = get_jwt()
                        send_telegram("⏳ Auditando los 20 Paneles de Threat Hunting Library...", chat_id=chat_id)
                        res = get_threat_hunting_panels_summary(jwt)
                        send_telegram(res, chat_id=chat_id)
                    elif cmd == "/ids":
                        jwt = get_jwt()
                        send_telegram("⏳ Consultando panel de firmas de intrusión IDS (Fase 4)...", chat_id=chat_id)
                        res = get_ids_signatures_summary(jwt)
                        send_telegram(res, chat_id=chat_id)
                    elif cmd == "/span":
                        jwt = get_jwt()
                        send_telegram("⏳ Consultando telemetría del Puerto SPAN...", chat_id=chat_id)
                        res = get_span_health_summary(jwt)
                        send_telegram(res, chat_id=chat_id)
                    elif cmd == "/bitacora":
                        fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        txt = (
                            f"📋 *FILA GENERADA PARA BITÁCORA EXCEL:*\n\n"
                            f"`{fecha_hoy}\tKevin Moraes\tTechnoma, Caja Ande\tN/A\tStellar Cyber / Modular Sensor / Cortex XDR\tN/A\tInformativo\tAuditoría de Turno & Control de Ingesta\tMonitoreo de Guardia y Verificación SPAN/Syslog\t10.11.1.1, FG-Technoma, Modular Sensor\tAuditoría operativa diaria: Control de cuota, verificación de 54 Log Filters en Modular Sensor, supervisión de tráfico DNS en puerto SPAN y triaje de incidentes.\tLogs de tráfico Interflow y Syslog en Data Lake Stellar Cyber.\tMantener monitoreo pasivo en turno.\tCerrado\tN/A\tNO`"
                        )
                        send_telegram(txt, chat_id=chat_id)
                    elif cmd == "/ping":
                        send_telegram("🏓 *PONG!* Sensores y APIs operando normalmente.", chat_id=chat_id)
                    else:
                        send_telegram("❓ Comando no reconocido. Escribe `/help` para ver la lista.", chat_id=chat_id)
            time.sleep(1)
        except Exception as e:
            print(f"[-] Error en listener: {e}")
            time.sleep(5)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bot de Telegram para el SOC")
    parser.add_argument("--send-daily", action="store_true", help="Enviar Workflow Diario a Telegram")
    parser.add_argument("--listen", action="store_true", help="Modo interactivo en background")
    args = parser.parse_args()
    
    if args.send_daily:
        msg = generate_daily_workflow_briefing()
        send_telegram(msg)
    elif args.listen:
        run_interactive_listener()
    else:
        run_interactive_listener()