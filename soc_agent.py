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

import re
import ipaddress
from functools import lru_cache

from openai import OpenAI
from soc_prompts import SYSTEM_PROMPT_TRIAGE

BASE_DIR = Path(__file__).resolve().parent
AD_INVENTORY_PATH = BASE_DIR / "Analista SOC" / "02_Base_de_Conocimiento" / "ad_users_inventory.md"

# Subredes conocidas (antes se comparaba con `"192.168.15." in texto`, que también
# coincidía con 192.168.150-159.x y etiquetaba mal esas IPs).
SUBREDES_CONOCIDAS = [
    (ipaddress.ip_network("192.168.169.0/24"), "192.168.169.0/24 (WiFi_Corp / Usuarios Technoma)"),
    (ipaddress.ip_network("192.168.15.0/24"), "192.168.15.0/24 (VLAN-15 Servidores y Sensores Technoma)"),
    (ipaddress.ip_network("172.16.0.0/16"), "172.16.0.0/16 (Red Corporativa Caja Ande)"),
]


def _mtime(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0.0


@lru_cache(maxsize=4)
def _usuarios_ad_cache(path_str: str, mtime: float) -> frozenset:
    path = Path(path_str)
    if not path.exists():
        return frozenset()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return frozenset(
            line.strip().lstrip("- ").strip().lower()
            for line in f
            if line.strip() and not line.startswith("#") and not line.startswith("*")
        )


def cargar_usuarios_ad() -> frozenset:
    """Set de cuentas del inventario de AD (una por línea '- usuario'), cacheado por fecha de modificación."""
    return _usuarios_ad_cache(str(AD_INVENTORY_PATH), _mtime(AD_INVENTORY_PATH))


def _normalizar_usuario(username: str) -> str:
    u = (username or "").strip().lower()
    if "\\" in u:
        u = u.split("\\")[-1]
    if "@" in u:
        u = u.split("@")[0]
    return u.strip()


def _contiene_token(texto_lower: str, token: str) -> bool:
    """Coincidencia por token completo (no substring): 'admin' no coincide dentro de 'administrador'."""
    return re.search(rf"(?<![\w.\-$]){re.escape(token)}(?![\w\-$]|\.\w)", texto_lower) is not None


def _etiqueta_subred(valor: str) -> str:
    try:
        ip = ipaddress.ip_address(valor.strip())
    except ValueError:
        return ""
    for net, etiqueta in SUBREDES_CONOCIDAS:
        if ip in net:
            return f"[Subred] {etiqueta}"
    return ""

NVIDIA_BASE_URL = os.environ.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
NVIDIA_MODEL_FAST = os.environ.get("NVIDIA_MODEL_FAST", "meta/llama-3.2-11b-vision-instruct")
NVIDIA_MODEL_DEEP = os.environ.get("NVIDIA_MODEL_DEEP", "meta/llama-3.2-90b-vision-instruct")
NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", NVIDIA_MODEL_FAST)


def ejecutar_herramienta_local(nombre: str, args: dict) -> str:
    if nombre == "buscar_usuario_active_directory":
        username = args.get("username", "")
        print(f"  ⚡ [Tool] Consultando Directorio Activo para usuario: '{username}'...", flush=True)
        if not AD_INVENTORY_PATH.exists():
            return f"Inventario no encontrado en {AD_INVENTORY_PATH}"
        clean_user = _normalizar_usuario(username)
        if len(clean_user) < 3:
            return f"Usuario '{username}' no válido para buscar en Active Directory (vacío o demasiado corto)."
        # Coincidencia EXACTA de la cuenta (antes: substring, y un usuario vacío "encontraba" todo el archivo)
        if clean_user in cargar_usuarios_ad():
            return (f"Usuario '{username}' FIGURA en el inventario de Active Directory como cuenta '{clean_user}'. "
                    "Esto solo confirma que la cuenta existe; no prueba que la actividad sea legítima.")
        return f"Usuario '{username}' NO encontrado en el inventario de Active Directory."

    elif nombre == "buscar_activo_o_ip":
        ip_o_host = args.get("ip_o_host", "")
        print(f"  ⚡ [Tool] Consultando inventario de infraestructura para: '{ip_o_host}'...", flush=True)
        query = ip_o_host.lower().strip()
        if len(query) < 3:
            return f"No se encontró registro para '{ip_o_host}' (valor vacío o demasiado corto)."
        resultados = []
        fuentes = [
            (BASE_DIR / "Analista SOC" / "computers_and_servers.md", "[Caja Ande]"),
            (BASE_DIR / "Analista SOC" / "Reportes" / "Reporte_Consolidado_Cortex_XDR_Technoma.md", "[Cortex Technoma]"),
            (BASE_DIR / "deep_dive_soc_gateway.md", "[Red/Gateway]"),
        ]
        for ruta, etiqueta in fuentes:
            if not ruta.exists():
                continue
            with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    # Token completo: '10.0.0.1' ya no coincide con '10.0.0.15'
                    if _contiene_token(line.lower(), query):
                        resultados.append(f"{etiqueta} {line.strip()[:110]}")
        subred = _etiqueta_subred(query)
        if subred:
            resultados.append(subred)

        if resultados:
            return "Activo encontrado:\n" + "\n".join(resultados[:8])
        return f"No se encontró registro para '{ip_o_host}' en los inventarios conocidos."

    elif nombre == "consultar_heuristica_falso_positivo":
        termino = args.get("termino", "")
        print(f"  ⚡ [Tool] Buscando precedentes de falsos positivos para: '{termino}'...", flush=True)
        query = termino.lower().strip()
        if len(query) < 3:
            return f"Sin precedentes específicos para '{termino}'."
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

    def _es_privada(x: str) -> bool:
        try:
            return ipaddress.ip_address(x).is_private
        except ValueError:
            return False

    for ip in sorted(ips, key=lambda x: (not _es_privada(x), x))[:6]:
        info = ejecutar_herramienta_local("buscar_activo_o_ip", {"ip_o_host": ip})
        if "No se encontró" not in info:
            hallazgos.append(f"• **IP {ip}:** {info.strip()}")
            
    # 2. Hostnames
    hosts = set(re.findall(r"\b(?:NB-[A-Za-z0-9_-]+|[a-zA-Z0-9_-]+\.technoma\.local|[a-zA-Z0-9_-]+\.teamviewer\.com|router\d+\.teamviewer\.com)\b", texto, re.I))
    for h in list(hosts)[:6]:
        info = ejecutar_herramienta_local("buscar_activo_o_ip", {"ip_o_host": h})
        hallazgos.append(f"• **Host {h}:** {info.strip()}")
        
    # 3. Usuarios en Active Directory (coincidencia por token completo, no substring)
    ad_users = cargar_usuarios_ad()
    if ad_users:
        texto_lower = texto.lower()
        usuarios_encontrados = set()
        for u in ad_users:
            if len(u) >= 4 and _contiene_token(texto_lower, u):
                usuarios_encontrados.add(u)

        m_users = re.findall(r'(?:username|usuario|user)\s*[:=]?\s*["\']?([a-zA-Z0-9_.\\@-]+)', texto, re.I)
        for mu in m_users:
            mu_clean = _normalizar_usuario(mu)
            if mu_clean in ad_users:
                usuarios_encontrados.add(mu_clean)

        for u in sorted(usuarios_encontrados)[:4]:
            hallazgos.append(
                f"• **Cuenta presente en Active Directory:** `{u}` (existe en technoma.local; "
                "esto NO prueba que la actividad sea legítima — una cuenta válida puede estar comprometida)"
            )

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


def ejecutar_consulta(prompt_usuario: str, modelo: str = None, contexto_memoria: str = ""):
    """
    Ejecuta el triaje forense. `contexto_memoria` (opcional) es el paquete de casos históricos
    del RAG que arma soar_web.py; antes se calculaba pero nunca llegaba a la IA.
    Lanza RuntimeError si no hay credenciales (antes hacía sys.exit dentro del servidor web).
    """
    target_model = modelo or NVIDIA_MODEL
    client = OpenAI(
        base_url=NVIDIA_BASE_URL,
        api_key=NVIDIA_API_KEY
    )

    system_instruction = SYSTEM_PROMPT_TRIAGE

    from soar_ai_client import is_antigravity_available, SoarUnifiedOpenAIClient

    antigravity_ok = is_antigravity_available()
    if not antigravity_ok and not NVIDIA_API_KEY:
        raise RuntimeError("Ni Google Antigravity OAuth ni NVIDIA_API_KEY están disponibles (defínela en el archivo .env).")

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

    if contexto_memoria:
        prompt_enriquecido += (
            "\n\n---\n### MEMORIA DEL SOC (casos históricos, plantillas y playbooks relacionados):\n"
            f"{contexto_memoria}\n---\n"
            "Usa esta memoria como referencia; verifica que realmente aplique a este caso antes de reutilizar un veredicto."
        )

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

    try:
        _main_consulta(args, parser)
    except RuntimeError as e:
        print(f"❌ {e}")
        sys.exit(1)


def _main_consulta(args, parser):
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
