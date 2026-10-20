#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🤖 SOC AGENT - Asistente Autónomo de Triaje y Correlación Forense
Technoma Security Operations Center (SOC)
Motor: NVIDIA NIM (Llama 3.2 11B / 90B) / OpenAI Client
=============================================================================
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Asegurar codificación UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Cargar variables de entorno
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent

NVIDIA_BASE_URL = os.environ.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
NVIDIA_MODEL_FAST = os.environ.get("NVIDIA_MODEL_FAST", "meta/llama-3.2-11b-vision-instruct")
NVIDIA_MODEL_DEEP = os.environ.get("NVIDIA_MODEL_DEEP", "meta/llama-3.2-90b-vision-instruct")
NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", NVIDIA_MODEL_FAST)


def ejecutar_herramienta_local(nombre: str, args: dict) -> str:
    if nombre == "buscar_usuario_active_directory":
        username = args.get("username", "")
        print(f"  ⚡ [Tool] Consultando Directorio Activo para usuario: '{username}'...", flush=True)
        path = BASE_DIR / "Analista SOC" / "02_Base_de_Conocimiento" / "ad_users_inventory.md"
        if not path.exists():
            return f"Inventario no encontrado en {path}"
        clean_user = username.lower().strip().replace("technoma\\", "").replace("cajaande\\", "")
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
        lines = [line.strip().lower() for line in contenido.splitlines() if line.strip()]
        coincidencias = [l for l in lines if clean_user in l]
        if coincidencias:
            return f"Usuario '{username}' ENCONTRADO en Active Directory: {', '.join(coincidencias)} (Usuario Corporativo Válido)."
        return f"Usuario '{username}' NO encontrado en el inventario de Active Directory."

    elif nombre == "buscar_activo_o_ip":
        ip_o_host = args.get("ip_o_host", "")
        print(f"  ⚡ [Tool] Consultando inventario de infraestructura para: '{ip_o_host}'...", flush=True)
        query = ip_o_host.lower().strip()
        resultados = []
        p1 = BASE_DIR / "Analista SOC" / "computers_and_servers.md"
        if p1.exists():
            with open(p1, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if query in line.lower():
                        resultados.append(f"[Caja Ande] {line.strip()[:110]}")
        p2 = BASE_DIR / "Analista SOC" / "Reportes" / "Reporte_Consolidado_Cortex_XDR_Technoma.md"
        if p2.exists():
            with open(p2, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if query in line.lower():
                        resultados.append(f"[Cortex Technoma] {line.strip()[:110]}")
        p3 = BASE_DIR / "deep_dive_soc_gateway.md"
        if p3.exists():
            with open(p3, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if query in line.lower():
                        resultados.append(f"[Red/Gateway] {line.strip()[:110]}")
        if "192.168.169." in query:
            resultados.append("[Subred] 192.168.169.0/24 (WiFi_Corp / Usuarios Technoma)")
        if "192.168.15." in query:
            resultados.append("[Subred] 192.168.15.0/24 (VLAN-15 Servidores y Sensores Technoma)")
        if "172.16." in query:
            resultados.append("[Subred] 172.16.0.0/16 (Red Corporativa Caja Ande)")

        if resultados:
            return "Activo encontrado:\n" + "\n".join(resultados[:8])
        return f"No se encontró registro para '{ip_o_host}' en los inventarios conocidos."

    elif nombre == "consultar_heuristica_falso_positivo":
        termino = args.get("termino", "")
        print(f"  ⚡ [Tool] Buscando precedentes de falsos positivos para: '{termino}'...", flush=True)
        query = termino.lower().strip()
        hallazgos = []
        p1 = BASE_DIR / "prompt_stellar_python.md"
        if p1.exists():
            with open(p1, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if query in line.lower() and len(line.strip()) > 10:
                        hallazgos.append(f"[Heurística] {line.strip()[:120]}")
        p2 = BASE_DIR / "Analista SOC" / "Bitacora_Personal_Casos_SOC.md"
        if p2.exists():
            with open(p2, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if query in line.lower() and len(line.strip()) > 15:
                        hallazgos.append(f"[Bitácora Previa] {line.strip()[:120]}")
        if hallazgos:
            return "Precedentes encontrados:\n" + "\n".join(hallazgos[:6])
        return f"Sin precedentes específicos para '{termino}'."

    elif nombre == "consultar_playbook_soc":
        tipo_incidente = args.get("tipo_incidente", "")
        print(f"  ⚡ [Tool] Consultando catálogo de playbooks para: '{tipo_incidente}'...", flush=True)
        path = BASE_DIR / "00_Playbooks" / "SOC_Incident_Response_Playbooks_Master.md"
        if not path.exists():
            return "Playbooks no encontrados."
        query = tipo_incidente.lower()
        coincidencias = []
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if any(k in line.lower() for k in [query, "playbook", "pb-"]):
                    if len(coincidencias) < 4:
                        coincidencias.append(line.strip())
        if coincidencias:
            return "Playbook relacionado:\n" + "\n".join(coincidencias)
        return "Aplicar PB-2.2 (Monitoreo Operativo y Triaje)."

    return f"Herramienta '{nombre}' no reconocida."


OPENAI_TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "buscar_usuario_active_directory",
            "description": "Busca un usuario en el inventario oficial de Active Directory (ad_users_inventory.md) para verificar si es un colaborador legítimo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Nombre de usuario o cuenta detectada"}
                },
                "required": ["username"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_activo_o_ip",
            "description": "Consulta el inventario de servidores, hosts y topología de red para identificar qué es un hostname o IP.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ip_o_host": {"type": "string", "description": "Dirección IP o nombre de host"}
                },
                "required": ["ip_o_host"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultar_heuristica_falso_positivo",
            "description": "Consulta los precedentes de falsos positivos y comportamientos conocidos en la bitácora del SOC.",
            "parameters": {
                "type": "object",
                "properties": {
                    "termino": {"type": "string", "description": "Término de búsqueda o tipo de alerta"}
                },
                "required": ["termino"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultar_playbook_soc",
            "description": "Consulta el catálogo de playbooks del SOC para obtener guías de resolución.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tipo_incidente": {"type": "string", "description": "Tipo de alerta o naturaleza del incidente"}
                },
                "required": ["tipo_incidente"]
            }
        }
    }
]


import re


# =============================================================================
# COMPACTACIÓN DE INTERFLOW (sin perder eventos ni precisión)
#   1. Extrae TODOS los JSON pegados (uno o varios) y deduplica por _id.
#   2. Desenvuelve _source y quita solo ruido de infraestructura (ids, geo, tuplas...).
#   3. Los campos idénticos en todos los eventos se escriben UNA vez ("comunes").
#   4. Por evento solo van los campos que varían.
#   5. Totales, ventana horaria, sumas y rangos se calculan en Python (exactos).
# =============================================================================
MAX_CHARS_PROMPT = int(os.environ.get("SOC_MAX_CHARS", "60000"))

_RUIDO = {
    "_index", "_type", "_id", "_version", "_seq_no", "_primary_term", "found",
    "aella_tuples", "src_tuples", "dst_tuples", "anomaly_id", "orig_id", "orig_index",
    "stellar_uuid", "stellar_index_id", "stellar_da_input", "stellar.alert_time",
    "stellar.alert_timestamp_field", "stellar.detection_time", "write_by", "write_time",
    "receive_time", "start_bucket_time", "end_bucket_time", "engid", "obsid", "org_id",
    "tenantid", "locid", "dscp_name", "tos", "msgtype", "msgtype_name", "netid", "end_reason",
    "detected_fields", "detected_values", "domain_list", "timestamp", "processing_time",
    "srcip_assetid", "dstip_assetid", "srcip_version", "dstip_version", "msg_class",
    "xdr_event.framework_version", "xdr_event.xdr_killchain_version", "xdr_event.scope",
    "metadata.response.query", "metadata.response.query_type", "metadata.response.transaction_id",
    "metadata.response.domain_creation", "metadata.response.effective_tld",
    "metadata.response.flags", "metadata.request.flags", "metadata.transaction_id",
    "metadata.response.processing_time", "metadata.response.response_time",
}
_RUIDO_SUFIJO = ("_geo", "_geo_point", "_geo_source")
_RUIDO_PREFIJO = ("msg_origin.",)
_NUM_RANGO = ["event_score", "severity", "flow_score", "threat_score", "actual", "typical",
              "total_entropy", "totalbytes", "totalpackets", "query_count", "fidelity"]
_NUM_SUMA = ["totalbytes", "inbytes_total", "outbytes_total", "totalpackets"]
_UNICOS = ["srcip", "srcip_host", "dstip", "dstip_host", "dstport", "proto_name", "appid_name",
           "event_name", "event_category", "tunnel_domain", "domain_reputation", "tenant_name",
           "engid_name"]


def _aplanar(d, pref=""):
    out = {}
    for k, v in d.items():
        kk = f"{pref}{k}"
        if isinstance(v, dict):
            out.update(_aplanar(v, kk + "."))
        else:
            out[kk] = v
    return out


def _es_ruido(k):
    return (k in _RUIDO or k.split(".")[0].endswith(_RUIDO_SUFIJO) or k.startswith(_RUIDO_PREFIJO))


def _valor_compacto(k, v):
    if isinstance(v, list):
        if v and all(isinstance(x, dict) for x in v):
            partes = []
            for x in v:
                destino = x.get("host") or x.get("host_addr") or ""
                partes.append(f"{x.get('name', '')}>{destino}({x.get('host_type', '')})")
            return partes
        return v
    return v


def _recolectar_docs(o, prof=0):
    if prof > 6:
        return []
    if isinstance(o, dict):
        if isinstance(o.get("docs"), list):
            return [d for d in o["docs"] if isinstance(d, dict)]
        if "_source" in o or ("srcip" in o and "event_name" in o):
            return [o]
        r = []
        for v in o.values():
            r += _recolectar_docs(v, prof + 1)
        return r
    if isinstance(o, list):
        r = []
        for x in o:
            r += _recolectar_docs(x, prof + 1)
        return r
    return []


def _extraer_jsons(texto):
    dec = json.JSONDecoder()
    i, docs, resto, ult = 0, [], [], 0
    while True:
        m = re.search(r"[\{\[]", texto[i:])
        if not m:
            break
        ini = i + m.start()
        try:
            obj, fin = dec.raw_decode(texto, ini)
        except ValueError:
            i = ini + 1
            continue
        encontrados = _recolectar_docs(obj)
        if encontrados:
            docs += encontrados
            resto.append(texto[ult:ini])
            ult = fin
        i = fin
    resto.append(texto[ult:])
    return docs, "".join(resto).strip()


def _resumen_exacto(fuentes, total_bruto):
    res = {"eventos_recibidos": total_bruto, "eventos_unicos": len(fuentes)}
    ts = sorted(s.get("timestamp_utc") for s in fuentes if s.get("timestamp_utc"))
    if ts:
        res["ventana_utc"] = {"primero": ts[0], "ultimo": ts[-1]}
    from collections import Counter
    for k in _UNICOS:
        c = Counter(str(s[k]) for s in fuentes if k in s)
        if c:
            res[k] = dict(c.most_common(10)) if len(c) > 1 else f"{next(iter(c))} (x{sum(c.values())})"
    rangos = {}
    for k in _NUM_RANGO:
        vals = [s[k] for s in fuentes if isinstance(s.get(k), (int, float))]
        if vals:
            rangos[k] = {"min": round(min(vals), 4), "max": round(max(vals), 4)}
    if rangos:
        res["rangos"] = rangos
    sumas = {}
    for k in _NUM_SUMA:
        vals = [s[k] for s in fuentes if isinstance(s.get(k), (int, float))]
        if vals:
            sumas[k] = round(sum(vals), 4)
    if sumas:
        res["sumas"] = sumas
    pay = []
    for s in fuentes:
        for p in s.get("tunnel_payloads", []) or []:
            if p not in pay:
                pay.append(p)
    if pay:
        res["tunnel_payloads_unicos"] = pay[:40]
    return res


def _dumps(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))


def preparar_entrada(texto: str) -> str:
    """Convierte uno o varios JSON de Interflow en un bloque compacto y exacto."""
    t = texto.strip()
    docs, prosa = _extraer_jsons(t)
    if not docs:
        return t[:MAX_CHARS_PROMPT] + ("\n...[entrada truncada]" if len(t) > MAX_CHARS_PROMPT else "")

    vistos, fuentes = set(), []
    for d in docs:
        src = d.get("_source", d)
        clave = d.get("_id") or src.get("stellar_uuid") or _dumps(src)
        if clave in vistos:
            continue
        vistos.add(clave)
        fuentes.append(src)
    fuentes.sort(key=lambda s: s.get("timestamp_utc", ""))

    desc = next((s.get("xdr_event", {}).get("description") for s in fuentes
                 if isinstance(s.get("xdr_event"), dict) and s["xdr_event"].get("description")), None)

    planos = []
    for s in fuentes:
        p = {}
        for k, v in _aplanar(s).items():
            if _es_ruido(k) or k == "xdr_event.description":
                continue
            if v is None or v == "" or v == [] or v == {}:
                continue
            p[k] = _valor_compacto(k, v)
        planos.append(p)

    comunes = {}
    if len(planos) > 1:
        for k in planos[0]:
            ref = _dumps(planos[0][k])
            if all(k in p and _dumps(p[k]) == ref for p in planos[1:]):
                comunes[k] = planos[0][k]
    eventos = [{"i": n + 1, **{k: v for k, v in p.items() if k not in comunes}}
               for n, p in enumerate(planos)]

    def armar(evs, nota=""):
        partes = []
        if prosa:
            partes.append(prosa)
        partes.append("[RESUMEN CALCULADO POR EL SISTEMA SOBRE TODOS LOS EVENTOS (valores exactos; no recalcular)]")
        partes.append(_dumps(_resumen_exacto(fuentes, len(docs))))
        if desc:
            partes.append("[DESCRIPCIÓN NATIVA STELLAR (del primer evento; los números cambian por evento)]")
            partes.append(desc)
        if comunes:
            partes.append(f"[CAMPOS IDÉNTICOS EN LOS {len(planos)} EVENTOS]")
            partes.append(_dumps(comunes))
        partes.append("[EVENTOS: solo campos que varían]" + nota)
        partes += [_dumps(e) for e in evs]
        return "\n".join(partes)

    salida = armar(eventos)
    # Si aún es enorme: quitar primero lo más voluminoso por evento (los totales ya están en el resumen)
    for pesado in ("metadata.response.answers", "tunnel_payloads"):
        if len(salida) <= MAX_CHARS_PROMPT:
            break
        eventos = [{k: v for k, v in e.items() if k != pesado} for e in eventos]
        salida = armar(eventos, f" (se omitió '{pesado}' por tamaño)")
    while len(salida) > MAX_CHARS_PROMPT and len(eventos) > 5:
        eventos = eventos[: max(5, int(len(eventos) * 0.7))]
        salida = armar(eventos, f" (solo los primeros {len(eventos)} de {len(planos)}; el resumen cubre todos)")
    return salida


def auto_enriquecer_contexto(texto: str) -> str:
    """Extrae automáticamente IPs, hostnames y usuarios para consultarlos en local en <10ms."""
    texto = texto[:200_000]
    hallazgos = []
    
    # 1. IPs (prioriza privadas internas de la organización)
    ips = set(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", texto))
    for ip in sorted(ips, key=lambda x: (not x.startswith(("192.168.", "10.", "172.")), x))[:6]:
        info = ejecutar_herramienta_local("buscar_activo_o_ip", {"ip_o_host": ip})
        if "No se encontró" not in info:
            hallazgos.append(f"• **IP {ip}:** {info.strip()}")
            
    # 2. Hostnames
    hosts = set(re.findall(r"\b(?:NB-[A-Za-z0-9_-]+|[a-zA-Z0-9_-]+\.technoma\.local|[a-zA-Z0-9_-]+\.teamviewer\.com|router\d+\.teamviewer\.com)\b", texto, re.I))
    for h in list(hosts)[:6]:
        info = ejecutar_herramienta_local("buscar_activo_o_ip", {"ip_o_host": h})
        hallazgos.append(f"• **Host {h}:** {info.strip()}")
        
    # 3. Usuarios en Active Directory
    path_ad = BASE_DIR / "Analista SOC" / "02_Base_de_Conocimiento" / "ad_users_inventory.md"
    if path_ad.exists():
        with open(path_ad, "r", encoding="utf-8", errors="ignore") as f:
            ad_users = {line.strip().lstrip("- ").strip().lower() for line in f if line.strip() and not line.startswith("#") and not line.startswith("*")}
        
        texto_lower = texto.lower()
        usuarios_encontrados = set()
        for u in ad_users:
            if len(u) >= 4 and u in texto_lower:
                usuarios_encontrados.add(u)
        
        m_users = re.findall(r'(?:username|usuario|user)\s*[:=]?\s*["\']?([a-zA-Z0-9_.-]+)', texto, re.I)
        for mu in m_users:
            mu_clean = mu.lower().strip()
            if mu_clean in ad_users:
                usuarios_encontrados.add(mu_clean)
                
        for u in list(usuarios_encontrados)[:4]:
            hallazgos.append(f"• **Usuario en Active Directory:** `{u}` (Colaborador corporativo legítimo en technoma.local)")

    # 4. Heurísticas y Precedentes en Base de Conocimiento
    texto_low = texto.lower()
    terminos_heuristica = []
    # Detección de dominios y herramientas SaaS conocidas
    for kw in ["wbx2", "webex", "teamviewer", "anydesk", "rustdesk", "dns_tunnel", "smb", "ntlm", "port 3000", "large upload", "exploit_attempt"]:
        if kw in texto_low:
            terminos_heuristica.append(kw)

    for th in terminos_heuristica[:4]:
        info = ejecutar_herramienta_local("consultar_heuristica_falso_positivo", {"termino": th})
        if "Sin precedentes" not in info:
            hallazgos.append(f"• **Precedente en Base de Conocimiento ({th}):** {info.strip()}")

    # 5. Cruce automático con el Cerebro Unificado de 7 Capas (Casos Históricos, SOC_GEM_v2 y Playbooks)
    try:
        from rag_engine import get_rag
        rag = get_rag()
        layers = rag.query_multi_layer(texto[:450])
        for cat_label, cat_key in [
            ("Memoria SOC (`SOC_GEM_v2` / Plantillas)", "MEMORIA_SOC"),
            ("Caso Histórico Resuelto (`Analista SOC/Casos/`)", "CASO_HISTORICO"),
            ("Playbook Oficial (`00_Playbooks/`)", "PLAYBOOK"),
        ]:
            hits = layers.get(cat_key, [])
            if hits:
                top_hit = hits[0]
                snippet = top_hit["content"][:400].replace("\n", " ").strip()
                hallazgos.append(
                    f"• **{cat_label} [{top_hit['rel_path']}] (Score {top_hit['score']}):** {snippet}..."
                )
    except Exception:
        pass

    if not hallazgos:
        return ""
    
    return "\n".join(hallazgos)


def ejecutar_consulta(prompt_usuario: str, modelo: str = None):
    target_model = modelo or NVIDIA_MODEL
    client = OpenAI(
        base_url=NVIDIA_BASE_URL,
        api_key=NVIDIA_API_KEY
    )

    system_instruction = (
        "Eres el Agente Autónomo de Ciberseguridad de Technoma SOC asistiendo al analista Kevin Moraes.\n"
        "Tu objetivo es el triaje forense y análisis integral de alertas de Stellar Cyber OpenXDR / Interflow, FortiGate y Cortex XDR.\n\n"
        "PRINCIPIOS FUNDAMENTALES DE ANÁLISIS FORENSE:\n"
        "1. CAUSALIDAD CONSOLIDADA (TERMINANTEMENTE PROHIBIDO EL DESORDEN):\n"
        "   - Está TERMINANTEMENTE PROHIBIDO fragmentar el dictamen en 'Alerta 1, Alerta 2, Alerta 3' o emitir análisis separados.\n"
        "   - Si recibes múltiples eventos, un lote o array 'docs' de Interflow, debes analizar la causalidad integral del incidente como UN ÚNICO CASO CONSOLIDADO, cruzando el tráfico, los activos y las firmas disparadas.\n"
        "2. USO DE EVIDENCIAS LOCALES Y PRECEDENTES DEL SOC:\n"
        "   - Considera prioritarias las evidencias técnicas locales ya verificadas en Active Directory e inventario que se adjuntan al caso.\n"
        "3. RIGOR FORENSE Y DESCARTE DE FALSOS POSITIVOS (PROHIBIDO SER UN 'LORO DE ALERTAS'):\n"
        "   - ESTÁ TERMINANTEMENTE PROHIBIDO repetir ciegamente la descripción genérica de la máquina (ej: si Stellar dice 'indicates potential DNS tunnelling').\n"
        "   - Tu rol como analista forense es verificar el DOMINIO REAL y los payloads. Los modelos de Machine Learning (new_ml) se confunden con frecuencia por alta entropía al procesar microservicios SaaS legítimos.\n"
        "   - Si el dominio involucrado (ej: wbx2.com / webex.com, teamviewer.com, google.com, microsoft.com) pertenece a una suite corporativa legítima y las IPs resueltas pertenecen a sus ASNs oficiales (ej: Cisco AS13445), DEBES clasificar el caso OBLIGATORIAMENTE como Benign True Positive / Falso Positivo Operativo, recomendando tuning/supresión en vez de declarar falsos incidentes de exfiltración.\n"
        "4. COMENTARIO DE CIERRE HUMANIZADO:\n"
        "   - El Comentario de Cierre Maestro debe ser redactado en un párrafo analítico continuo, fluido, profesional y elegante. Prohibidas listas numeradas mecánicas o introducciones de '1. El primer evento...'. Debe estar listo para copiar y pegar en auditorías o en el modal de cierre de Stellar Cyber.\n\n"
        "ESTRUCTURA OBLIGATORIA DEL DICTAMEN (LAS 4 FASES CLARAS):\n\n"
        "### Fase 1: Declaración de Ingesta y Resumen Ejecutivo Nativo Stellar Cyber\n"
        "- **Declaración de Ingesta:** Indica el total de eventos analizados en el lote, tenant y ventana horaria.\n"
        "- **Tabla Consolidada de Entidades Críticas:** Activo Origen (IP, Host, MAC), Activo Destino (IP, Host/Dominio, Puerto), Protocolo, Firmas IDS / Reglas disparadas, Severidad.\n"
        "- **Resumen Ejecutivo (Los 4 Puntos Oficiales de Stellar Cyber):**\n"
        "  * Resumen General: Breve síntesis del incidente y la anomalía detectada.\n"
        "  * Origen de la Amenaza: Host, IP y proceso o usuario causante.\n"
        "  * Impacto en el Destino: Qué activos recibieron el tráfico y si hubo compromiso.\n"
        "  * Mitigación y Estado: Estado del caso y acciones de respuesta.\n\n"
        "### Fase 2: Triaje y Correlación Forense Consolidada\n"
        "- **Disección Técnica y Causalidad Integral:** Explicación analítica clara de por qué el motor/IDS disparó la alerta y qué estaba ocurriendo en realidad (diferenciando ruido operativo de ataque real).\n"
        "- **IOCs y Firmas Relacionadas:** Tabla compacta con SID, nombre de firma, clasificación de severidad y payload/query.\n"
        "- **Matriz de Impacto CIA:** Evaluación breve (Confidencialidad: C0-C3, Integridad: I0-I3, Disponibilidad: A0-A3).\n"
        "- **Veredicto y Confianza:** Uno de los 4 cuadrantes (True Positive, False Positive, Benign True Positive / Falso Positivo Operativo, Unclear) con porcentaje de confianza analítica (0-100%).\n"
        "- **Mapeo MITRE ATT&CK y Playbook Technoma SOC:** Técnica MITRE y código de playbook (ej. PB-1.1, PB-6.1).\n\n"
        "### Fase 3: Instrucción de Cierre en Stellar Cyber (Cierre Humanizado)\n"
        "- **Estado:** Closed / Resolved.\n"
        "- **Resolution Tag:** False Positive / Benign / True Positive.\n"
        "- **Comentario de Cierre Maestro:** Un solo párrafo fluido, analítico y profesional (sin numeraciones ni viñetas mecánicas), redactado en un bloque de cita `> ...` listo para auditoría.\n"
        "- **Recomendación de Tuning / Regla de Supresión:** Parámetros exactos de filtro o whitelist en el sensor o firewall para mitigar falsos positivos.\n\n"
        "### Fase 4: Exportación de Bitácoras\n"
        "1. **Ficha para Bitácora Personal Markdown (`Bitacora_Personal_Casos_SOC.md`):** Ficha modular estructurada.\n"
        "2. **Bitácora Oficial de Turno (18 Columnas):** Tabla de apoyo visual de 18 columnas oficiales (A: Fecha/Hora, B: Analista [Kevin Moraes], C: Tenant, D: ID caso, E: Fuente, F: Nro Ticket, G: Prioridad, H: Tipo evento, I: Asunto, J: Activos, K: Descripción, L: Evidencia, M: Solicitud Acción, N: Estado, O: URL, P: Generación Ticket, Q: TICKET, R: Playbook) seguida obligatoriamente de un bloque ```tsv con 1 única línea con campos delimitados por tabuladores (\\t) y comillas dobles en campos largos para pegar en Excel con 1 clic."
    )

    from soar_ai_client import is_antigravity_available, SoarUnifiedOpenAIClient

    antigravity_ok = is_antigravity_available()
    if not antigravity_ok and not NVIDIA_API_KEY:
        print("❌ Ni Google Antigravity OAuth ni NVIDIA_API_KEY están disponibles (defínela en el archivo .env).")
        sys.exit(1)

    print("\n🔍 [SOC AGENT] Analizando caso localmente (Pre-extracción de evidencias)...", flush=True)
    evidencias_locales = auto_enriquecer_contexto(prompt_usuario)
    prompt_compacto = preparar_entrada(prompt_usuario)
    if len(prompt_usuario) > len(prompt_compacto):
        print(f"  ⚡ [Optimizer] Entrada compactada: {len(prompt_usuario):,} -> {len(prompt_compacto):,} caracteres.", flush=True)

    if evidencias_locales:
        prompt_enriquecido = (
            f"{prompt_compacto}\n\n"
            f"---\n"
            f"### EVIDENCIAS TÉCNICAS VERIFICADAS LOCALMENTE EN TECHNOMA (0-LATENCY):\n"
            f"{evidencias_locales}\n"
            f"---\n"
            f"Utiliza estas evidencias verificadas en tu dictamen consolidado."
        )
    else:
        prompt_enriquecido = prompt_compacto

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt_enriquecido}
    ]

    effective_model = os.environ.get("SOAR_AI_MODEL", "gemini-3.8-flash-high") if antigravity_ok else target_model
    provider_label = "Google Antigravity OAuth" if antigravity_ok else "NVIDIA NIM"
    client = SoarUnifiedOpenAIClient(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)

    print(f"🚀 Conectando con {provider_label} ({effective_model}) en modo streaming...", flush=True)
    print("\n" + "=" * 75)
    print(f"📋 DICTAMEN FORENSE DEL AGENTE SOC (Modelo: {effective_model})")
    print("=" * 75 + "\n", flush=True)

    stream = client.chat.completions.create(
        model=effective_model,
        messages=messages,
        temperature=0.3,
        max_tokens=8192,
        stream=True
    )

    full_response = []
    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
            full_response.append(delta.content)

    print("\n\n" + "=" * 75 + "\n", flush=True)
    return "".join(full_response)


def main():
    parser = argparse.ArgumentParser(description="SOC AGENT - Copiloto Autónomo de Triaje Forense")
    parser.add_argument("consulta", nargs="?", help="Texto o instrucción a analizar")
    parser.add_argument("-f", "--file", help="Ruta a un archivo JSON o de texto con la alerta cruda")
    args = parser.parse_args()

    if args.file:
        ruta = Path(args.file)
        if not ruta.exists():
            print(f"❌ Error: Archivo no encontrado: {ruta}")
            sys.exit(1)
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
        ejecutar_consulta(f"Analiza la siguiente alerta cruda:\n\n{contenido}")
    elif args.consulta:
        ejecutar_consulta(args.consulta)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
