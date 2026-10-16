#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — MÓDULO DE REPORTES DE ABUSO & ESCANEO (OPENXDR COCKPIT)
=============================================================================
Analizador y formateador automático de notificaciones de abuso para IPs atacantes
y de escaneo perimetral detectadas en Stellar Cyber OpenXDR / FortiGate.
- Parsea volcados JSON nativos de Interflow / Athena / Elasticsearch o syslogs.
- Mapea ASN / Proveedor con buzón oficial de abuso (abuse@...).
- Genera asunto y cuerpo en inglés con log limpio y botones de copia de 1-clic.
=============================================================================
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QLineEdit,
    QPushButton, QFileDialog, QMessageBox, QFrame, QSplitter,
    QComboBox, QApplication, QWidget, QStatusBar, QSizePolicy
)
from PySide6.QtGui import QFont, QColor, QPalette

# Directorio base
BASE_DIR = Path(__file__).resolve().parent

# =============================================================================
# CATÁLOGO OFICIAL DE BUZONES DE ABUSO POR PROVEEDOR / ASN
# =============================================================================
ABUSE_CONTACTS_MAP = {
    "cloudflare": "abuse@cloudflare.com",
    "datacamp": "abuse@datacamp.co.uk",
    "cdn77": "abuse@datacamp.co.uk",
    "digitalocean": "abuse@digitalocean.com",
    "amazon": "abuse@amazonaws.com",
    "aws": "abuse@amazonaws.com",
    "google": "network-abuse@google.com",
    "microsoft": "abuse@microsoft.com",
    "azure": "abuse@microsoft.com",
    "hetzner": "abuse@hetzner.com",
    "ovh": "abuse@ovh.net",
    "linode": "abuse@linode.com",
    "akamai": "abuse@akamai.com",
    "hostinger": "abuse@hostinger.com",
    "vultr": "abuse@vultr.com",
    "choopa": "abuse@constant.com",
    "the constant company": "abuse@constant.com",
    "leaseweb": "abuse@leaseweb.com",
    "tencent": "abuse@tencent.com",
    "alibaba": "abuse@alibaba-inc.com",
    "volcano": "security@bytedance.com",
    "bytedance": "security@bytedance.com",
    "oracle": "abuse@oracle.com",
    "fastly": "abuse@fastly.com",
    "contabo": "abuse@contabo.com",
    "braveway": "abuse@braveway.com",
    "wifiber": "abuse@braveway.com"
}


_RDAP_CACHE: Dict[str, Dict[str, Optional[str]]] = {}


def consultar_asn_abuse_info(asn: Any) -> Optional[Dict[str, str]]:
    """Consulta el buzón de abuso del Sistema Autónomo BGP vía RDAP aut-num y socket Whois port 43."""
    if not asn:
        return None
    asn_clean = str(asn).upper().replace("AS", "").strip()
    if not asn_clean.isdigit():
        return None

    import urllib.request
    import socket

    endpoints = [
        f"https://rdap.db.ripe.net/aut-num/AS{asn_clean}",
        f"https://rdap.org/aut-num/{asn_clean}",
        f"https://rdap.arin.net/registry/aut-num/{asn_clean}",
        f"https://rdap.apnic.net/aut-num/{asn_clean}",
        f"https://rdap.afrinic.net/rdap/aut-num/{asn_clean}"
    ]
    for url in endpoints:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TechnomaSOC/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=2.5) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                    # Remarks
                    for rem in data.get("remarks", []):
                        for d in rem.get("description", []):
                            m = re.search(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', d)
                            if m and "abuse" in d.lower():
                                return {"email": m.group(1).strip(), "asn": f"AS{asn_clean}", "holder": data.get("name", "")}

                    # Entities
                    def _find_abuse(entities):
                        for ent in entities:
                            roles = ent.get("roles", [])
                            vcards = (ent.get("vcardArray") or [[], []])[1]
                            for card in vcards:
                                if isinstance(card, list) and len(card) > 3 and card[0] == "email":
                                    em = str(card[3]).strip()
                                    if "abuse" in roles or "abuse" in em.lower():
                                        return em
                            sub = _find_abuse(ent.get("entities", []))
                            if sub:
                                return sub
                        return None

                    em = _find_abuse(data.get("entities", []))
                    if em:
                        return {"email": em, "asn": f"AS{asn_clean}", "holder": data.get("name", "")}
        except Exception:
            continue

    # Fallback Socket Port 43
    for srv in ["whois.ripe.net", "whois.radb.net", "whois.arin.net", "whois.apnic.net"]:
        try:
            s = socket.create_connection((srv, 43), timeout=2.5)
            s.sendall(f"AS{asn_clean}\r\n".encode())
            raw = b""
            while True:
                d = s.recv(4096)
                if not d:
                    break
                raw += d
            s.close()
            text = raw.decode("utf-8", errors="ignore")
            m = re.search(r'abuse-mailbox:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+)', text, re.I)
            if m:
                return {"email": m.group(1).strip(), "asn": f"AS{asn_clean}", "holder": ""}
            m2 = re.search(r'Abuse contact.*?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+)', text, re.I)
            if m2:
                return {"email": m2.group(1).strip(), "asn": f"AS{asn_clean}", "holder": ""}
        except Exception:
            pass

    return None


def consultar_rdap_abuse_info(ip: str, asn_num: Any = None) -> Dict[str, Optional[str]]:
    """Consulta la API de RDAP y Whois para extraer el correo de abuso validado (IP o ASN BGP) y titular del bloque."""
    if not ip:
        return {"email": None, "org": None, "netname": None, "tech_email": None, "asn_abuse": None}
    cache_key = f"{ip}_{asn_num or ''}"
    if cache_key in _RDAP_CACHE:
        return _RDAP_CACHE[cache_key]

    result: Dict[str, Optional[str]] = {
        "email": None,
        "org": None,
        "netname": None,
        "tech_email": None,
        "asn_abuse": None
    }
    try:
        import urllib.request
        endpoints = [
            f"https://rdap.org/ip/{ip}",
            f"https://rdap.db.ripe.net/ip/{ip}",
            f"https://rdap.arin.net/registry/ip/{ip}",
            f"https://rdap.afrinic.net/rdap/ip/{ip}",
            f"https://rdap.apnic.net/ip/{ip}",
            f"https://rdap.lacnic.net/rdap/ip/{ip}"
        ]
        for url in endpoints:
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "TechnomaSOC/1.0", "Accept": "application/rdap+json"}
                )
                with urllib.request.urlopen(req, timeout=3.0) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                        result["netname"] = data.get("name")

                        def _search_rdap(obj):
                            if isinstance(obj, dict):
                                roles = obj.get("roles", [])
                                vcards = obj.get("vcardArray", [])
                                cards = vcards[1] if isinstance(vcards, list) and len(vcards) > 1 else []

                                for c in cards:
                                    if isinstance(c, list) and len(c) > 3:
                                        prop_type = c[0]
                                        prop_val = str(c[3]).strip()
                                        if prop_type == "email":
                                            if ("abuse" in roles or "abuse" in prop_val.lower()) and not result["email"]:
                                                result["email"] = prop_val
                                            elif any(r in roles for r in ["technical", "administrative", "tech", "admin"]) and not result["tech_email"]:
                                                result["tech_email"] = prop_val
                                        elif prop_type in ["org", "fn"] and not result["org"]:
                                            if prop_val and not prop_val.endswith("-MNT") and "role object" not in prop_val.lower():
                                                if any(r in roles for r in ["registrant", "administrative", "owner"]):
                                                    result["org"] = prop_val

                                for v in obj.values():
                                    _search_rdap(v)
                            elif isinstance(obj, list):
                                for item in obj:
                                    _search_rdap(item)

                        _search_rdap(data)

                        if not result["org"] and result["netname"]:
                            clean_nn = result["netname"].replace("_", " ").strip()
                            if clean_nn:
                                result["org"] = clean_nn

                        if result["email"] and result["org"]:
                            break
            except Exception:
                continue
    except Exception:
        pass

    # 2. Si no se encontró buzón directo de abuso en el objeto IP, consultar el ASN BGP
    effective_asn = asn_num
    if not effective_asn:
        try:
            req_bgp = urllib.request.Request(
                f"https://stat.ripe.net/data/network-info/data.json?resource={ip}",
                headers={"User-Agent": "TechnomaSOC/1.0", "Accept": "application/json"}
            )
            with urllib.request.urlopen(req_bgp, timeout=2.5) as resp_bgp:
                if resp_bgp.status == 200:
                    d_bgp = json.loads(resp_bgp.read().decode("utf-8", errors="ignore"))
                    asns_list = d_bgp.get("data", {}).get("asns", [])
                    if asns_list:
                        effective_asn = asns_list[0]
        except Exception:
            pass

    if effective_asn:
        asn_contact = consultar_asn_abuse_info(effective_asn)
        if asn_contact and asn_contact.get("email"):
            result["asn_abuse"] = asn_contact["email"]
            if not result["email"]:
                result["email"] = asn_contact["email"]

    # 3. Fallback a contacto técnico si aún no hay email de abuso
    if not result["email"] and result["tech_email"]:
        result["email"] = result["tech_email"]

    _RDAP_CACHE[cache_key] = result
    _RDAP_CACHE[ip] = result
    return result


def detectar_buzones_abuso(org_name: str, asn_num: Any = None, ip: Optional[str] = None) -> tuple[str, str]:
    """
    Identifica TODOS los correos de abuso aplicables (BGP/Hosting + Dueño del bloque en RDAP/Whois + ASN aut-num).
    Si existen dos entidades distintas (ej. Datacamp y BraveWay, o Cloud Innovation y VPSVAULT.HOST),
    combina ambos correos y ambas entidades para máxima precisión en el asunto y cuerpo del reporte.
    Retorna (correos_combinados, org_label_completa).
    """
    emails: List[str] = []
    org_clean = (org_name or "").strip()
    org_lower = org_clean.lower()

    # 1. Buzón del proveedor según catálogo local
    for kw, email in ABUSE_CONTACTS_MAP.items():
        if kw in org_lower:
            if email not in emails:
                emails.append(email)
            break

    # 2. Consultar en vivo a RDAP / WHOIS para IP y ASN BGP
    rdap_org = None
    if ip:
        rdap_info = consultar_rdap_abuse_info(ip, asn_num=asn_num)
        rdap_email = rdap_info.get("email")
        asn_abuse = rdap_info.get("asn_abuse")
        tech_email = rdap_info.get("tech_email")
        rdap_org = rdap_info.get("org")

        for em in [asn_abuse, rdap_email, tech_email]:
            if em and em.lower() not in [e.lower() for e in emails] and "@" in em:
                emails.append(em)

    # 3. Construir etiqueta de organización conjunta si hay dos entidades distintas
    org_label = org_clean if org_clean and org_clean != "Desconocido" else ""
    if rdap_org:
        clean_curr = re.sub(r'[^a-zA-Z0-9]', '', org_label).lower()
        clean_rdap = re.sub(r'[^a-zA-Z0-9]', '', rdap_org).lower()
        if not org_label:
            org_label = rdap_org
        elif clean_curr and clean_rdap and clean_curr not in clean_rdap and clean_rdap not in clean_curr:
            org_label = f"{rdap_org} / {org_label}"

    if not org_label:
        org_label = "Desconocido"

    if not emails:
        emails = ["Verificar Whois / RDAP (ej. abuse@...)"]

    return ", ".join(emails), org_label


def extraer_log_limpio(raw_msg: str) -> str:
    """Extrae desde 'srcip=' en adelante del syslog crudo del FortiGate para máxima claridad."""
    if not raw_msg:
        return ""
    match = re.search(r'(srcip=.*)$', raw_msg)
    if match:
        return match.group(1).strip()
    return raw_msg.strip()


# =============================================================================
# PERSISTENCIA Y CONSULTA DE IPS YA REPORTADAS (HISTÓRICO SOC)
# =============================================================================
def obtener_ips_reportadas_historico() -> Dict[str, Dict[str, Any]]:
    """Carga el diccionario de IPs previamente reportadas desde registro_ips_reportadas.json."""
    ruta = BASE_DIR / "Analista SOC" / "registro_ips_reportadas.json"
    if not ruta.exists():
        return {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {item["ip"]: item for item in data.get("reported_ips", []) if "ip" in item}
    except Exception:
        return {}


def registrar_ip_como_reportada(ip_data: Dict[str, Any]) -> bool:
    """Registra una IP en el histórico JSON y Markdown para evitar duplicados."""
    ruta_json = BASE_DIR / "Analista SOC" / "registro_ips_reportadas.json"
    ruta_md = BASE_DIR / "Analista SOC" / "Registro_IPs_Reportadas_Abuso.md"
    ip = ip_data.get("ip")
    if not ip:
        return False

    # 1. Actualizar JSON
    datos_json = {"updated_at": "2026-10-09T13:50:00-03:00", "analyst": "Kevin Moraes", "reported_ips": []}
    if ruta_json.exists():
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                datos_json = json.load(f)
        except Exception:
            pass

    lista = datos_json.setdefault("reported_ips", [])
    encontrado = False
    for item in lista:
        if item.get("ip") == ip:
            item.update(ip_data)
            encontrado = True
            break
    if not encontrado:
        lista.append(ip_data)

    from datetime import datetime
    datos_json["updated_at"] = datetime.now().isoformat()
    try:
        ruta_json.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos_json, f, indent=2, ensure_ascii=False)
    except Exception:
        return False

    # 2. Actualizar Markdown si no figura la IP
    if ruta_md.exists():
        try:
            with open(ruta_md, "r", encoding="utf-8") as f:
                md_content = f.read()
            if f"`{ip}`" not in md_content:
                num = len(lista)
                num_str = f"{num:02d}"
                pais = ip_data.get("country", "Desconocido")
                org = ip_data.get("org", "Desconocido")
                serv = f"{ip_data.get('service', 'HTTPS')} ({ip_data.get('port', 443)})"
                inc = "Fuerza Bruta" if ip_data.get("incident_type") == "fuerza_bruta" else "Escaneo"
                recip = ip_data.get("recipient", "abuse@cloudflare.com")
                bcc = ip_data.get("bcc", "Ivan")
                subj = ip_data.get("subject", f"Scan - {ip}")
                nueva_fila = f"| **{num_str}** | `{ip}` | 09/10/2026 | {org} | {pais} | {serv} | {inc} | `{recip}` | `{bcc}` | `{subj}` | 🟢 Notificado |\n"

                if "\n---\n\n## 🔍 Detalle Técnico" in md_content:
                    md_content = md_content.replace("\n---\n\n## 🔍 Detalle Técnico", f"{nueva_fila}\n---\n\n## 🔍 Detalle Técnico")
                else:
                    md_content += f"\n{nueva_fila}"

                with open(ruta_md, "w", encoding="utf-8") as f:
                    f.write(md_content)
        except Exception:
            pass

    return True


# =============================================================================

# MAPEO DE SERVICIOS POR PUERTO DESTINO
# =============================================================================
PORT_SERVICE_MAP = {
    443: "HTTPS",
    80: "HTTP",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    22: "SSH",
    21: "FTP",
    23: "Telnet",
    3389: "RDP",
    25: "SMTP",
    587: "SMTP-Submission",
    465: "SMTPS",
    53: "DNS",
    3306: "MySQL",
    1433: "MSSQL",
    5432: "PostgreSQL",
    1521: "Oracle-DB",
    27017: "MongoDB",
    6379: "Redis",
    445: "SMB",
    139: "NetBIOS",
    161: "SNMP",
    389: "LDAP",
    636: "LDAPS"
}


def detectar_servicio_o_protocolo(source: Dict[str, Any]) -> str:
    """Extrae el protocolo o servicio afectado (HTTPS, SSH, RDP, etc.) del evento."""
    forti = source.get("fortinet", {}) if isinstance(source.get("fortinet"), dict) else {}
    service = (
        forti.get("service") or
        source.get("service") or
        source.get("appid_name")
    )
    if service and service.upper() not in ["UNSCANNED", "UNKNOWN", "NONE", ""]:
        return str(service).upper()

    dstport = source.get("dstport") or forti.get("dstport")
    if dstport:
        try:
            port_num = int(dstport)
            if port_num in PORT_SERVICE_MAP:
                return PORT_SERVICE_MAP[port_num]
            return f"Port {port_num}"
        except Exception:
            pass

    proto = source.get("proto_name") or source.get("proto") or "TCP"
    return str(proto).upper()


def detectar_tipo_incidente(source: Dict[str, Any]) -> tuple[str, str]:
    """
    Determina si el evento corresponde a 'fuerza_bruta' o 'escaneo'.
    Retorna (tipo_clave, etiqueta_humana):
      - ('fuerza_bruta', 'Ataque de Fuerza bruta')
      - ('escaneo', 'Escaneo')
    """
    reputation = (source.get("srcip_reputation") or "").lower()
    raw_msg = (source.get("parser_raw_msg") or source.get("msg") or "").lower()
    policyname = ""
    forti = source.get("fortinet", {}) if isinstance(source.get("fortinet"), dict) else {}
    if forti:
        policyname = str(forti.get("policyname") or "").lower()

    # Si Stellar/ETPro lo catalogó como Brute_Forcer o hay indicios explícitos
    if "brute_forcer" in reputation or "bruteforce" in reputation or "brute" in raw_msg:
        return "fuerza_bruta", "Ataque de Fuerza bruta"

    # Si el puerto es administrativo (SSH, RDP) y hubo denegaciones continuas
    dstport = str(source.get("dstport") or forti.get("dstport") or "")
    if dstport in ["22", "3389"] and "login" in raw_msg:
        return "fuerza_bruta", "Ataque de Fuerza bruta"

    return "escaneo", "Escaneo"


# =============================================================================
# GENERADOR DE PLANTILLAS FORMALES SEGÚN PLAYBOOK OFICIAL (01 a 04)
# =============================================================================
def construir_asunto_y_cuerpo(
    tipo_incidente: str,
    servicio: str,
    ip: str,
    org_label: str,
    dt_str: str,
    log_clean: str,
    plantilla_id: str = "04_eng",
    malware_name: str = "",
    malware_url: str = ""
) -> tuple[str, str, str]:
    """
    Construye el Asunto oficial, Asunto en inglés y el Cuerpo según el Playbook del SOC.
    Retorna (asunto_es, asunto_en, cuerpo).
    """
    es_brute = (tipo_incidente == "fuerza_bruta")

    # 1. Asuntos normalizados según Playbook:
    # Escaneo: "Escaneo - <IP> [<Organización>]"
    # Fuerza bruta: "Ataque de Fuerza bruta <Protocolo o servicio> - <IP> [<Organización>]"
    if es_brute:
        asunto_es = f"Ataque de Fuerza bruta {servicio} - {ip} [{org_label}]"
        asunto_en = f"Brute force attack {servicio} - {ip} [{org_label}]"
    else:
        asunto_es = f"Escaneo - {ip} [{org_label}]"
        asunto_en = f"Scan - {ip} [{org_label}]"

    # Textos de descripción de ataque
    desc_es = f"intentos de fuerza bruta contra nuestro servicio {servicio}" if es_brute else "escaneos de red no autorizados"
    desc_en = f"unauthorized brute force attempts against our {servicio} service" if es_brute else "unauthorized scanning / connection attempts"

    # 2. Cuerpos según plantilla seleccionada
    if plantilla_id == "04_eng":
        # Plantilla 04 (ENG) - Internacional para IPs extranjeras
        cuerpo = (
            f"Hello:\n"
            f"We have detected {desc_en} from an IP under your authority.\n"
            f"IP: {ip}\n"
            f"Date/Time: {dt_str}\n\n"
            f"It is attached the log for further investigation:\n"
            f"{log_clean}\n\n"
            f"We would appreciate your collaboration to address this issue or forward to someone who can.\n"
            f"Regards,\n"
            f"Technoma SOC"
        )
    elif plantilla_id == "04_esp":
        # Plantilla 04 (ESP) - Para destinatarios hispanohablantes extranjeros
        cuerpo = (
            f"Estimado/a:\n"
            f"Hemos detectado {desc_es} originados aparentemente desde una IP bajo su autoridad:\n"
            f"IP: {ip}\n"
            f"Fecha y Hora: {dt_str}\n\n"
            f"Adjuntamos un extracto de logs para que puedan investigarlo:\n"
            f"{log_clean}\n\n"
            f"Solicitamos su colaboración para tomar las acciones pertinentes o escalar a la persona apropiada.\n"
            f"Saludos,\n"
            f"Technoma SOC"
        )
    elif plantilla_id == "03_py":
        # Plantilla 03 (PY) - IP local paraguaya sin malware confirmado
        cuerpo = (
            f"Estimado/a:\n"
            f"Hemos detectado {desc_es} originados aparentemente desde una IP bajo su autoridad:\n"
            f"IP: {ip}\n\n"
            f"Adjuntamos un extracto de logs para que puedan investigarlo:\n"
            f"{log_clean}\n\n"
            f"Es posible que un equipo cuyo tráfico esté siendo redirigido a través de dicha IP esté infectado o comprometido. "
            f"Recomendamos realizar un análisis forense para determinar el origen de las conexiones. "
            f"En caso de que desee, el CERT-PY / Technoma SOC puede colaborar en el análisis forense.\n"
            f"En caso de que tenga alguna duda y/o quisiera más información, puede responder a este mismo correo, "
            f"o al final de éste encontrará nuestra información de contacto.\n\n"
            f"Saludos,\n"
            f"Technoma SOC"
        )
    elif plantilla_id == "02_py_malware":
        # Plantilla 02 (PY) - IP local paraguaya vinculada a Botnet / Malware
        m_name = malware_name or "Botnet / C2"
        m_url = malware_url or "https://cert.gov.py/"
        cuerpo = (
            f"Estimado/a:\n"
            f"Hemos detectado {desc_es} originados aparentemente desde una IP bajo su autoridad:\n"
            f"IP: {ip}\n\n"
            f"Adjuntamos un extracto de logs para que puedan investigarlo:\n"
            f"{log_clean}\n\n"
            f"Es posible que un equipo cuyo tráfico esté siendo redirigido a través de dicha IP esté infectado o comprometido. "
            f"Hemos identificado que dicha IP está vinculada a una botnet, denominada {m_name}. Puede encontrar más información aquí: {m_url}\n"
            f"Recomendamos realizar un análisis forense para determinar el equipo infectado y tomar las acciones correctivas necesarias.\n"
            f"En caso de que desee, el CERT-PY / Technoma SOC puede colaborar en el análisis forense.\n"
            f"En caso de que tenga alguna duda y/o quisiera más información, puede responder a este mismo correo, "
            f"o al final de éste encontrará nuestra información de contacto.\n\n"
            f"Saludos,\n"
            f"Technoma SOC"
        )
    elif plantilla_id == "01_solicitar_info":
        # Plantilla 01 - Solicitud de información al reportante
        cuerpo = (
            f"Estimado/a:\n\n"
            f"Muchas gracias por su reporte! Para poder investigar el incidente necesitamos que nos proporcione "
            f"algún registro o log en el que se visualicen los escaneos y/o intentos de fuerza bruta. "
            f"El log debe incluir como mínimo, la siguiente información:\n"
            f"- Fecha y hora de las conexiones\n"
            f"- IP de origen de las conexiones\n"
            f"- IP de destino de las conexiones\n"
            f"- Protocolo o servicio afectado (SSH, FTP, RDP, HTTP, HTTPS, MySQL, etc.)\n\n"
            f"Saludos,\n"
            f"Technoma SOC"
        )
    elif plantilla_id == "05_seguimiento":
        # Plantilla 05 - Seguimiento de caso previo sin respuesta
        cuerpo = (
            f"Estimado/a:\n\n"
            f"Días atrás hemos remitido una notificación indicando un incidente sobre posibles actividades no autorizadas "
            f"({desc_es}) originadas aparentemente desde una IP bajo su autoridad ({ip}).\n\n"
            f"Agradeceremos informarnos si han podido tomar conocimiento e iniciar las acciones de remediación pertinentes.\n\n"
            f"Saludos,\n"
            f"Technoma SOC"
        )
    else:
        cuerpo = f"IP: {ip}\nLog:\n{log_clean}"

    return asunto_es, asunto_en, cuerpo


# =============================================================================
# MOTOR DE PROCESAMIENTO FORENSE DE ABUSO (Interflow / Stellar Cyber)
# =============================================================================
class AbuseReportEngine:
    @staticmethod
    def parse_payload(raw_text: str) -> List[Dict[str, Any]]:
        """
        Parsea texto que contenga uno o más objetos JSON de Stellar Cyber / Interflow.
        Soporta diccionarios directos, arrays, hits de Elasticsearch o Athena.
        """
        if not raw_text or not raw_text.strip():
            return []

        clean_text = raw_text.strip()
        data = None

        # 1. Intentar carga JSON directa
        try:
            data = json.loads(clean_text)
        except Exception:
            # 2. Intentar extraer bloque JSON con regex si hay texto antes o después
            match = re.search(r'(\{.*\}|\[.*\])', clean_text, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1))
                except Exception:
                    pass

        if not data:
            # 3. Intentar procesar como log crudo de FortiGate si tiene formato key=value
            if "srcip=" in clean_text:
                return AbuseReportEngine._parse_raw_syslog_fallback(clean_text)
            return []

        # Normalizar items
        if isinstance(data, dict):
            if "ctx" in data and "payload" in data["ctx"]:
                items = data["ctx"]["payload"].get("filtered", [])
            elif "hits" in data and isinstance(data["hits"], dict):
                items = data["hits"].get("hits", [])
            elif "data" in data and "docs" in data["data"]:
                items = data["data"].get("docs", [])
            elif "docs" in data:
                items = data.get("docs", [])
            else:
                items = [data]
        elif isinstance(data, list):
            items = data
        else:
            items = []

        ips_procesadas: Dict[str, Dict[str, Any]] = {}

        for item in items:
            source = item.get("_source", item) if isinstance(item, dict) else {}
            if not isinstance(source, dict):
                continue

            ip = source.get("srcip")
            if not ip:
                continue

            if ip not in ips_procesadas:
                asn_org = source.get("srcip_asn_org") or "Desconocido"
                asn_num = source.get("srcip_asn") or ""

                # Normalizar etiqueta amigable
                if "Cloudflare" in asn_org:
                    org_label = "Cloudflare Inc."
                elif "Volcano" in asn_org:
                    org_label = "Beijing Volcano Engine Technology Co., Ltd."
                elif "Datacamp" in asn_org:
                    org_label = "Datacamp Limited"
                elif "DigitalOcean" in asn_org:
                    org_label = "DigitalOcean, LLC"
                elif "Google" in asn_org:
                    org_label = "Google LLC"
                elif "Microsoft" in asn_org:
                    org_label = "Microsoft Corporation"
                else:
                    org_label = asn_org

                # Buzón de abuso oficial y etiqueta combinada (BGP + RDAP titular)
                buzon_abuso, org_label_completa = detectar_buzones_abuso(org_label, asn_num, ip=ip)

                # Fecha y Hora local (preferencia GMT-3 de FortiGate)
                forti = source.get("fortinet", {}) if isinstance(source.get("fortinet"), dict) else {}
                fecha = forti.get("date") or "2026-10-09"
                hora = forti.get("time") or "08:00:00"
                tz = forti.get("tz") or "-0300"
                tz_label = "GMT-3" if "-0300" in tz else tz
                dt_str = f"{fecha} {hora} {tz_label}"

                # Servicio o protocolo afectado
                servicio = detectar_servicio_o_protocolo(source)

                # Clasificación de incidente (Fuerza Bruta vs Escaneo)
                tipo_incidente, tipo_label = detectar_tipo_incidente(source)

                # Log crudo limpio
                raw_msg = source.get("parser_raw_msg") or source.get("msg") or ""
                log_clean = extraer_log_limpio(raw_msg)
                if not log_clean:
                    # Construir un log sintético mínimo si no vino parser_raw_msg
                    dstip = source.get("dstip", "")
                    dstport = source.get("dstport", "")
                    proto = source.get("proto_name", "tcp")
                    log_clean = f"srcip={ip} dstip={dstip} dstport={dstport} proto={proto} service={servicio}"

                # País y reputación
                country = (
                    source.get("srccountry") or
                    source.get("srcip_geo", {}).get("countryName") or
                    "Desconocido"
                )
                country_code = (
                    source.get("srcip_geo", {}).get("countryCode") or
                    ("PY" if "paraguay" in country.lower() else "")
                )
                reputation = source.get("srcip_reputation") or "Threat Score " + str(source.get("threat_score", "N/A"))

                # Plantilla sugerida por defecto: Si es PY -> 03_py; si es extranjera -> 04_eng
                sugerencia_plantilla = "03_py" if country_code == "PY" else "04_eng"

                asunto_es, asunto_en, cuerpo_defecto = construir_asunto_y_cuerpo(
                    tipo_incidente=tipo_incidente,
                    servicio=servicio,
                    ip=ip,
                    org_label=org_label_completa,
                    dt_str=dt_str,
                    log_clean=log_clean,
                    plantilla_id=sugerencia_plantilla
                )

                # El asunto por defecto se rige por el idioma de la plantilla
                asunto_defecto = asunto_en if sugerencia_plantilla == "04_eng" else asunto_es

                correo_completo = (
                    f"To: {buzon_abuso}\n"
                    f"Subject: {asunto_defecto}\n\n"
                    f"{cuerpo_defecto}"
                )

                ips_procesadas[ip] = {
                    "ip": ip,
                    "org": org_label_completa,
                    "org_label": org_label_completa,
                    "asn": asn_num,
                    "country": country,
                    "country_code": country_code,
                    "reputation": reputation,
                    "servicio": servicio,
                    "tipo_incidente": tipo_incidente,
                    "tipo_label": tipo_label,
                    "datetime": dt_str,
                    "log": log_clean,
                    "abuse_email": buzon_abuso,
                    "plantilla_id": sugerencia_plantilla,
                    "asunto_es": asunto_es,
                    "asunto_en": asunto_en,
                    "asunto": asunto_defecto,
                    "cuerpo": cuerpo_defecto,
                    "correo_completo": correo_completo,
                    "hits": 1
                }
            else:
                ips_procesadas[ip]["hits"] += 1

        return list(ips_procesadas.values())

    @staticmethod
    def _parse_raw_syslog_fallback(text: str) -> List[Dict[str, Any]]:
        """Fallback para cuando se pega un syslog sin formato JSON."""
        srcip_m = re.search(r'srcip=([0-9\.]+)', text)
        if not srcip_m:
            return []
        ip = srcip_m.group(1)
        country_m = re.search(r'srccountry="?([^"\s]+)"?', text)
        country = country_m.group(1) if country_m else "Desconocido"
        date_m = re.search(r'date=([0-9\-]+)', text)
        time_m = re.search(r'time=([0-9\:]+)', text)
        dt_str = f"{date_m.group(1) if date_m else '2026-10-09'} {time_m.group(1) if time_m else '08:00:00'} GMT-3"

        log_clean = extraer_log_limpio(text)
        asunto = f"Scan - {ip}"
        cuerpo = (
            f"Hello:\n"
            f"We have detected unauthorized scanning / connection attempts from an IP under your authority:\n"
            f"IP: {ip}\n"
            f"Date/Time: {dt_str}\n\n"
            f"Attached log for further investigation:\n"
            f"{log_clean}\n\n"
            f"We would appreciate your collaboration to address this issue or forward to someone who can.\n"
            f"Regards,\n"
            f"Technoma SOC"
        )
        buzon, org_res = detectar_buzones_abuso("", ip=ip)
        asunto = f"Scan - {ip} [{org_res}]"
        correo_completo = (
            f"To: {buzon}\n"
            f"Subject: {asunto}\n\n"
            f"{cuerpo}"
        )
        return [{
            "ip": ip,
            "org": org_res,
            "asn": "",
            "country": country,
            "reputation": "N/A",
            "datetime": dt_str,
            "hits": 1,
            "abuse_email": buzon,
            "asunto": asunto,
            "cuerpo": cuerpo,
            "log": log_clean,
            "correo_completo": correo_completo
        }]


# =============================================================================
# WIDGET REUTILIZABLE DE GENERACIÓN DE REPORTES DE ABUSO
# =============================================================================
class AbuseReportWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reportes_actuales: List[Dict[str, Any]] = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        # 1. Cabecera Informativa
        header_card = QFrame()
        header_card.setStyleSheet("background-color: #121721; border: 1px solid #232c3d; border-radius: 6px; padding: 6px;")
        h_layout = QHBoxLayout(header_card)
        h_layout.setContentsMargins(8, 6, 8, 6)

        lbl_title = QLabel("📧 Formateador Automático de Notificaciones de Abuso")
        lbl_title.setStyleSheet("font-weight: 700; color: #58a6ff; font-size: 13px;")
        h_layout.addWidget(lbl_title)

        h_layout.addStretch()

        self.lbl_stats = QLabel("Total IPs: 0 | Intentos: 0")
        self.lbl_stats.setStyleSheet("color: #8b949e; font-size: 11px; font-weight: 600;")
        h_layout.addWidget(self.lbl_stats)

        layout.addWidget(header_card)

        # 2. Selector de IP si hay múltiples
        sel_row = QHBoxLayout()
        lbl_sel = QLabel("Seleccionar IP Atacante:")
        lbl_sel.setStyleSheet("color: #e6edf3; font-weight: 600; font-size: 12px;")
        sel_row.addWidget(lbl_sel)

        self.combo_ips = QComboBox()
        self.combo_ips.setStyleSheet("""
            QComboBox {
                background-color: #1c2333;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 4px 8px;
                font-weight: 500;
            }
            QComboBox:hover { border-color: #58a6ff; }
        """)
        self.combo_ips.currentIndexChanged.connect(self._on_ip_selected)
        sel_row.addWidget(self.combo_ips, 1)

        layout.addLayout(sel_row)

        # Banner de Advertencia si la IP ya fue reportada
        self.banner_ya_reportada = QFrame()
        self.banner_ya_reportada.setStyleSheet("""
            QFrame {
                background-color: #2b1d07;
                border: 1px solid #d29922;
                border-radius: 4px;
                padding: 4px 8px;
            }
        """)
        b_layout = QHBoxLayout(self.banner_ya_reportada)
        b_layout.setContentsMargins(6, 4, 6, 4)
        self.lbl_alerta_reportada = QLabel("⚠️ ATENCIÓN: Esta IP ya fue reportada anteriormente.")
        self.lbl_alerta_reportada.setStyleSheet("color: #f0883e; font-weight: 700; font-size: 11px;")
        b_layout.addWidget(self.lbl_alerta_reportada)
        self.banner_ya_reportada.setVisible(False)
        layout.addWidget(self.banner_ya_reportada)

        # 3. Selectores del Playbook Oficial: Tipo de Incidente y Plantilla
        playbook_row = QHBoxLayout()

        lbl_tipo = QLabel("Incidente:")
        lbl_tipo.setFixedWidth(65)
        lbl_tipo.setStyleSheet("color: #8b949e; font-weight: 600;")
        playbook_row.addWidget(lbl_tipo)

        self.combo_tipo = QComboBox()
        self.combo_tipo.setStyleSheet("background-color: #1c2333; color: #e6edf3; border: 1px solid #30363d; border-radius: 4px; padding: 4px 6px;")
        self.combo_tipo.addItem("💥 Ataque de Fuerza bruta", "fuerza_bruta")
        self.combo_tipo.addItem("🔍 Escaneo de Puertos/Servicios", "escaneo")
        self.combo_tipo.currentIndexChanged.connect(self._on_playbook_config_changed)
        playbook_row.addWidget(self.combo_tipo, 1)

        lbl_plantilla = QLabel("Plantilla:")
        lbl_plantilla.setFixedWidth(60)
        lbl_plantilla.setStyleSheet("color: #8b949e; font-weight: 600;")
        playbook_row.addWidget(lbl_plantilla)

        self.combo_plantilla = QComboBox()
        self.combo_plantilla.setStyleSheet("background-color: #1c2333; color: #e6edf3; border: 1px solid #30363d; border-radius: 4px; padding: 4px 6px;")
        self.combo_plantilla.addItem("🌐 Plantilla 04 (ENG - Internacional)", "04_eng")
        self.combo_plantilla.addItem("🌐 Plantilla 04 (ESP - Extranjero)", "04_esp")
        self.combo_plantilla.addItem("🇵🇾 Plantilla 03 (PY - Local sin Malware)", "03_py")
        self.combo_plantilla.addItem("🦠 Plantilla 02 (PY - Con Malware/Botnet)", "02_py_malware")
        self.combo_plantilla.addItem("❓ Plantilla 01 (Solicitar Logs)", "01_solicitar_info")
        self.combo_plantilla.addItem("⏰ Plantilla 05 (Seguimiento / Reaviso)", "05_seguimiento")
        self.combo_plantilla.currentIndexChanged.connect(self._on_playbook_config_changed)
        playbook_row.addWidget(self.combo_plantilla, 1)

        layout.addLayout(playbook_row)

        # 4. Destinatario Sugerido (To)
        to_row = QHBoxLayout()
        lbl_to = QLabel("Destinatario (To):")
        lbl_to.setFixedWidth(110)
        lbl_to.setStyleSheet("color: #8b949e; font-weight: 600;")
        to_row.addWidget(lbl_to)

        self.txt_to = QLineEdit()
        self.txt_to.setReadOnly(True)
        self.txt_to.setStyleSheet("background-color: #0d1117; color: #3fb950; border: 1px solid #232c3d; border-radius: 4px; padding: 5px; font-weight: 600;")
        to_row.addWidget(self.txt_to, 1)

        self.btn_copy_to = QPushButton("📋 Copiar To")
        self.btn_copy_to.setStyleSheet("background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; padding: 5px 10px; border-radius: 4px;")
        self.btn_copy_to.clicked.connect(lambda: self.copy_to_clipboard(self.txt_to.text(), "Destinatario copiado"))
        to_row.addWidget(self.btn_copy_to)
        layout.addLayout(to_row)

        # 5. Asunto (Subject) con selector de idioma
        subj_row = QHBoxLayout()
        lbl_subj = QLabel("Asunto (Subject):")
        lbl_subj.setFixedWidth(110)
        lbl_subj.setStyleSheet("color: #8b949e; font-weight: 600;")
        subj_row.addWidget(lbl_subj)

        self.txt_subj = QLineEdit()
        self.txt_subj.setReadOnly(False)
        self.txt_subj.setStyleSheet("background-color: #0d1117; color: #58a6ff; border: 1px solid #232c3d; border-radius: 4px; padding: 5px; font-weight: 600;")
        subj_row.addWidget(self.txt_subj, 1)

        self.combo_asunto_lang = QComboBox()
        self.combo_asunto_lang.setStyleSheet("background-color: #1c2333; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 4px 6px;")
        self.combo_asunto_lang.addItem("Español", "es")
        self.combo_asunto_lang.addItem("Inglés", "en")
        self.combo_asunto_lang.currentIndexChanged.connect(self._on_playbook_config_changed)
        subj_row.addWidget(self.combo_asunto_lang)

        self.btn_copy_subj = QPushButton("📋 Copiar Asunto")
        self.btn_copy_subj.setStyleSheet("background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; padding: 5px 10px; border-radius: 4px;")
        self.btn_copy_subj.clicked.connect(lambda: self.copy_to_clipboard(self.txt_subj.text(), "Asunto copiado"))
        subj_row.addWidget(self.btn_copy_subj)
        layout.addLayout(subj_row)

        # 6. Cuerpo del Correo (Body)
        lbl_body = QLabel("Cuerpo del Correo Oficial (Playbook SOC):")
        lbl_body.setStyleSheet("color: #8b949e; font-weight: 600; font-size: 11px;")
        layout.addWidget(lbl_body)

        self.txt_body = QTextEdit()
        self.txt_body.setReadOnly(False)
        self.txt_body.setStyleSheet("""
            QTextEdit {
                background-color: #0d1117;
                color: #e6edf3;
                border: 1px solid #232c3d;
                border-radius: 6px;
                font-family: 'Consolas', monospace;
                font-size: 12px;
                padding: 8px;
            }
        """)
        self.txt_body.setMinimumHeight(130)
        layout.addWidget(self.txt_body, 1)

        # 7. Filas de Botones de Acción (Distribución responsiva en 2 niveles)
        actions_container = QVBoxLayout()
        actions_container.setSpacing(6)

        row_tools = QHBoxLayout()
        row_tools.setSpacing(8)

        self.btn_copy_body = QPushButton("📋 Copiar Cuerpo")
        self.btn_copy_body.setStyleSheet("background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; padding: 6px 12px; border-radius: 5px; font-weight: 500;")
        self.btn_copy_body.clicked.connect(lambda: self.copy_to_clipboard(self.txt_body.toPlainText(), "Cuerpo del correo copiado"))
        row_tools.addWidget(self.btn_copy_body)

        self.btn_copy_log = QPushButton("📋 Copiar Log Crudo")
        self.btn_copy_log.setStyleSheet("background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; padding: 6px 12px; border-radius: 5px; font-weight: 500;")
        self.btn_copy_log.clicked.connect(self._copy_current_log)
        row_tools.addWidget(self.btn_copy_log)

        self.btn_guardar_reporte = QPushButton("💾 Marcar como Reportada")
        self.btn_guardar_reporte.setStyleSheet("background-color: #1f6feb; color: #ffffff; border: 1px solid #388bfd; padding: 6px 14px; border-radius: 5px; font-weight: 600;")
        self.btn_guardar_reporte.clicked.connect(self._marcar_actual_como_reportada)
        row_tools.addWidget(self.btn_guardar_reporte)

        actions_container.addLayout(row_tools)

        row_cf = QHBoxLayout()
        row_cf.setSpacing(8)
        self.btn_cf_api = QPushButton("☁️ Reportar a Cloudflare API (1-Clic)")
        self.btn_cf_api.setStyleSheet("background-color: #d97706; color: #ffffff; border: 1px solid #f59e0b; padding: 7px 14px; border-radius: 5px; font-weight: 700;")
        self.btn_cf_api.clicked.connect(self._enviar_cloudflare_api)
        row_cf.addWidget(self.btn_cf_api)
        actions_container.addLayout(row_cf)

        self.btn_copy_all = QPushButton("🚀 Copiar Correo Completo (To + Subject + Body)")
        self.btn_copy_all.setStyleSheet("background-color: #238636; color: #ffffff; border: 1px solid #2ea043; padding: 8px 16px; border-radius: 5px; font-weight: 700; font-size: 13px;")
        self.btn_copy_all.clicked.connect(self._copy_full_email)
        actions_container.addWidget(self.btn_copy_all)

        layout.addLayout(actions_container)

    def cargar_datos_desde_texto(self, raw_text: str) -> int:
        """Parsea el texto y carga los reportes en el widget. Retorna cantidad de IPs."""
        reportes = AbuseReportEngine.parse_payload(raw_text)
        self.reportes_actuales = reportes
        self.combo_ips.blockSignals(True)
        self.combo_ips.clear()

        if not reportes:
            self.lbl_stats.setText("Total IPs: 0")
            self.txt_to.clear()
            self.txt_subj.clear()
            self.txt_body.setPlainText("No se encontraron registros de escaneo o IPs públicas en la entrada analizada.\nPega un JSON de Stellar Cyber / Interflow.")
            self.combo_ips.addItem("Ninguna IP detectada")
            self.combo_ips.blockSignals(False)
            self.banner_ya_reportada.setVisible(False)
            return 0

        total_hits = sum(r["hits"] for r in reportes)
        self.lbl_stats.setText(f"Total IPs: {len(reportes)} | Eventos Totales: {total_hits}")

        historico_ips = obtener_ips_reportadas_historico()
        for r in reportes:
            ip = r["ip"]
            tag_reportada = ""
            if ip in historico_ips:
                f_rep = historico_ips[ip].get("date", "Anteriormente")
                tag_reportada = f" ⚠️ [YA REPORTADA: {f_rep}]"
            icon = "💥" if r["tipo_incidente"] == "fuerza_bruta" else "🔍"
            label = f"{icon} {ip} · {r['org']} ({r['country']}) — {r['tipo_label']} {r['servicio']} ({r['hits']} ev.){tag_reportada}"
            self.combo_ips.addItem(label)

        self.combo_ips.blockSignals(False)
        self._mostrar_reporte(0)
        return len(reportes)

    def _on_ip_selected(self, index: int):
        if 0 <= index < len(self.reportes_actuales):
            self._mostrar_reporte(index)

    def _mostrar_reporte(self, index: int):
        if not (0 <= index < len(self.reportes_actuales)):
            return
        rep = self.reportes_actuales[index]
        self.txt_to.setText(rep["abuse_email"])

        # Verificar si la IP ya fue reportada históricamente
        historico_ips = obtener_ips_reportadas_historico()
        ip = rep["ip"]
        if ip in historico_ips:
            h = historico_ips[ip]
            f_rep = h.get("date", "09/10/2026")
            recip = h.get("recipient", rep["abuse_email"])
            subj = h.get("subject", "N/A")
            self.lbl_alerta_reportada.setText(
                f"⚠️ ATENCIÓN: La IP {ip} ya figura como NOTIFICADA el {f_rep} (Destinatario: {recip} | Asunto: '{subj}'). Evitar envío duplicado."
            )
            self.banner_ya_reportada.setVisible(True)
        else:
            self.banner_ya_reportada.setVisible(False)

        # Sincronizar selectores sin disparar eventos en bucle
        self.combo_tipo.blockSignals(True)
        self.combo_plantilla.blockSignals(True)
        self.combo_asunto_lang.blockSignals(True)

        idx_tipo = self.combo_tipo.findData(rep["tipo_incidente"])
        if idx_tipo >= 0:
            self.combo_tipo.setCurrentIndex(idx_tipo)

        idx_plantilla = self.combo_plantilla.findData(rep["plantilla_id"])
        if idx_plantilla >= 0:
            self.combo_plantilla.setCurrentIndex(idx_plantilla)

        # Idioma del asunto sugerido
        idx_lang = self.combo_asunto_lang.findData("en" if rep["plantilla_id"] == "04_eng" else "es")
        if idx_lang >= 0:
            self.combo_asunto_lang.setCurrentIndex(idx_lang)

        self.combo_tipo.blockSignals(False)
        self.combo_plantilla.blockSignals(False)
        self.combo_asunto_lang.blockSignals(False)

        self._regenerar_contenido_actual()

    def _marcar_actual_como_reportada(self):
        idx = self.combo_ips.currentIndex()
        if not (0 <= idx < len(self.reportes_actuales)):
            return
        rep = self.reportes_actuales[idx]
        ip = rep["ip"]

        from datetime import datetime
        hoy = datetime.now().strftime("%Y-%m-%d")
        datos = {
            "ip": ip,
            "date": hoy,
            "org": rep.get("org", "Desconocido"),
            "country": rep.get("country", "Desconocido"),
            "service": rep.get("servicio", "HTTPS"),
            "port": 443,
            "incident_type": self.combo_tipo.currentData() or rep.get("tipo_incidente", "escaneo"),
            "recipient": self.txt_to.text().strip(),
            "bcc": "Ivan",
            "subject": self.txt_subj.text().strip(),
            "status": "notificado"
        }
        ok = registrar_ip_como_reportada(datos)
        if ok:
            QMessageBox.information(
                self,
                "Registro Guardado",
                f"✓ La IP {ip} ha quedado guardada en el historial JSON y en Registro_IPs_Reportadas_Abuso.md."
            )
            # Actualizar texto del combobox
            texto_actual = self.combo_ips.itemText(idx)
            if "YA REPORTADA" not in texto_actual:
                self.combo_ips.setItemText(idx, f"{texto_actual} ⚠️ [YA REPORTADA: {hoy}]")
            self._mostrar_reporte(idx)
        else:
            QMessageBox.warning(self, "Error", f"No se pudo guardar el registro para {ip}.")

    def _enviar_cloudflare_api(self):
        """Envía el reporte de abuso directamente a la API de Cloudflare Trust & Safety."""
        idx = self.combo_ips.currentIndex()
        if not (0 <= idx < len(self.reportes_actuales)):
            QMessageBox.warning(self, "Aviso", "No hay ningún reporte o IP seleccionada.")
            return
        rep = self.reportes_actuales[idx]
        ip = rep.get("ip")
        log_clean = rep.get("log", "")

        token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
        account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")

        import urllib.request
        import urllib.error
        import urllib.parse

        url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/abuse-reports/abuse_network"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "TechnomaSOC-AbuseReporter/1.0"
        }
        data = {
            "act": "abuse_network",
            "source_ips": ip,
            "destination_ips": "10.11.3.196",
            "ports_protocols": f"{rep.get('port', 443)}/TCP",
            "justification": f"SOC Technoma Security Report - Raw Log:\n{log_clean}",
            "name": "Kevin Moraes",
            "email": "kevinmoraes@technoma.com.py",
            "company": "Technoma SOC"
        }

        try:
            encoded_data = urllib.parse.urlencode(data).encode("utf-8")
            req = urllib.request.Request(url, data=encoded_data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=10) as resp:
                res_json = json.loads(resp.read().decode("utf-8", errors="ignore"))
                report_id = res_json.get("result", {}).get("id", "OK")
                QMessageBox.information(
                    self,
                    "Reporte Cloudflare Enviado",
                    f"✓ Reporte enviado con éxito a Cloudflare Trust & Safety API.\nID de Reporte: {report_id}\nIP: {ip}"
                )
                self._marcar_actual_como_reportada()
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            if "Not entitled to use feature" in err_body:
                msg = (
                    "⚠️ Cloudflare respondió: 'Not entitled to use feature: Abuse Report API'\n\n"
                    "Motivo: El endpoint de envío directo por API (POST) requiere que la cuenta esté enrolada "
                    "en el Cloudflare Trusted Reporter Program (Enterprise / Whitelist de confianza).\n\n"
                    "Tu token es 100% válido y tiene permisos de Trust & Safety activos.\n"
                    "Para enviar esta denuncia de inmediato, puedes usar el botón 'Copiar Correo Completo' "
                    "hacia abuse@cloudflare.com o el formulario web oficial."
                )
                QMessageBox.warning(self, "Entitlement de Cloudflare", msg)
            else:
                QMessageBox.critical(self, "Error Cloudflare API", f"Error {e.code}: {err_body}")
        except Exception as ex:
            QMessageBox.critical(self, "Error de Conexión", f"Fallo al conectar con Cloudflare API:\n{str(ex)}")

    def _on_playbook_config_changed(self):
        """Regenera asunto y cuerpo cuando el usuario cambia el tipo, plantilla o idioma."""
        self._regenerar_contenido_actual()

    def _regenerar_contenido_actual(self):
        idx = self.combo_ips.currentIndex()
        if not (0 <= idx < len(self.reportes_actuales)):
            return
        rep = self.reportes_actuales[idx]

        tipo_sel = self.combo_tipo.currentData() or rep["tipo_incidente"]
        plantilla_sel = self.combo_plantilla.currentData() or rep["plantilla_id"]
        lang_sel = self.combo_asunto_lang.currentData() or "es"

        asunto_es, asunto_en, cuerpo = construir_asunto_y_cuerpo(
            tipo_incidente=tipo_sel,
            servicio=rep["servicio"],
            ip=rep["ip"],
            org_label=rep["org_label"],
            dt_str=rep["datetime"],
            log_clean=rep["log"],
            plantilla_id=plantilla_sel
        )

        asunto_elegido = asunto_en if lang_sel == "en" else asunto_es
        self.txt_subj.setText(asunto_elegido)
        self.txt_body.setPlainText(cuerpo)

    def _copy_current_log(self):
        idx = self.combo_ips.currentIndex()
        if 0 <= idx < len(self.reportes_actuales):
            self.copy_to_clipboard(self.reportes_actuales[idx]["log"], "Log crudo copiado")

    def _copy_full_email(self):
        to_val = self.txt_to.text()
        subj_val = self.txt_subj.text()
        body_val = self.txt_body.toPlainText()
        if to_val or subj_val or body_val:
            full_mail = f"To: {to_val}\nSubject: {subj_val}\n\n{body_val}"
            self.copy_to_clipboard(full_mail, "Correo completo copiado al portapapeles")

    def copy_to_clipboard(self, text: str, msg: str):
        if not text:
            return
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        # Mostrar notificación flotante o en ventana principal
        window = self.window()
        if hasattr(window, "statusBar") and callable(window.statusBar):
            window.statusBar().showMessage(f"✓ {msg}", 4000)
        else:
            QMessageBox.information(self, "Portapapeles", f"{msg} correctamente.")


# =============================================================================
# DIÁLOGO INDEPENDIENTE (STANDALONE & OPENXDR INTEGRATION)
# =============================================================================
class AbuseReportDialog(QDialog):
    def __init__(self, parent=None, initial_text: str = ""):
        super().__init__(parent)
        self.setWindowTitle("Technoma SOC — Generador de Reportes de Abuso & Escaneo")
        
        # 1. Habilitar Maximizar, Minimizar y Cerrar nativos de Windows
        self.setWindowFlags(
            Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint
        )
        
        # 2. Adaptar dinámicamente según la resolución y escala de la pantalla activa
        self.adaptar_tamano_pantalla()
        self.apply_theme()
        self.init_ui(initial_text)

    def adaptar_tamano_pantalla(self):
        """Calcula las dimensiones ideales según la pantalla activa para ser 100% responsivo."""
        screen = QApplication.primaryScreen()
        if screen:
            avail = screen.availableGeometry()
            # 88% del ancho y 86% del alto disponible para que no desborde en notebooks ni monitores grandes
            target_w = min(1360, max(820, int(avail.width() * 0.88)))
            target_h = min(880, max(520, int(avail.height() * 0.86)))
            self.resize(target_w, target_h)
            self.setMinimumSize(780, 480)
            # Centrar en pantalla disponible
            self.move(
                avail.x() + (avail.width() - target_w) // 2,
                avail.y() + (avail.height() - target_h) // 2
            )
        else:
            self.resize(1120, 700)
            self.setMinimumSize(780, 480)

    def apply_theme(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #0b0e14;
                color: #e6edf3;
            }
            QWidget {
                background-color: #0b0e14;
                color: #e6edf3;
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
                font-size: 13px;
            }
            QFrame.card {
                background-color: #121721;
                border: 1px solid #232c3d;
                border-radius: 8px;
            }
            QLabel.cardTitle {
                font-size: 14px;
                font-weight: 600;
                color: #58a6ff;
            }
            QTextEdit {
                background-color: #0d1117;
                border: 1px solid #232c3d;
                border-radius: 6px;
                color: #e6edf3;
                font-family: 'Consolas', monospace;
                font-size: 12px;
                padding: 8px;
            }
            QTextEdit:focus { border: 1px solid #58a6ff; }
            QPushButton {
                background-color: #21262d;
                color: #c9d1d9;
                border: 1px solid #30363d;
                padding: 7px 14px;
                border-radius: 6px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #30363d;
                color: #f0f6fc;
            }
            QPushButton.primary {
                background-color: #1f6feb;
                color: #ffffff;
                border: 1px solid #388bfd;
                font-weight: 600;
            }
            QPushButton.primary:hover { background-color: #388bfd; }
            QStatusBar {
                background-color: #161b22;
                border-top: 1px solid #232c3d;
                color: #8b949e;
                font-size: 11px;
            }
            QSplitter::handle {
                background-color: #1c2333;
                border: 1px solid #30363d;
                border-radius: 4px;
                margin: 4px 1px;
            }
            QSplitter::handle:hover {
                background-color: #58a6ff;
            }
        """)

    def init_ui(self, initial_text: str):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(14, 14, 14, 10)
        main_layout.setSpacing(10)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(8)

        # Panel Izquierdo: Entrada de JSON
        left_card = QFrame()
        left_card.setProperty("class", "card")
        left_card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        left_layout = QVBoxLayout(left_card)
        left_layout.setContentsMargins(12, 12, 12, 12)
        left_layout.setSpacing(8)

        lbl_in = QLabel("📥 Pegar JSON de Stellar Cyber / Interflow")
        lbl_in.setProperty("class", "cardTitle")
        left_layout.addWidget(lbl_in)

        lbl_hint = QLabel("Pega el volcado JSON nativo o log de firewall para formatear el correo:")
        lbl_hint.setStyleSheet("color: #8b949e; font-size: 11px;")
        left_layout.addWidget(lbl_hint)

        self.input_text = QTextEdit()
        self.input_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.input_text.setPlaceholderText("Pega aquí el JSON completo con { \"srcip\": \"...\", ... }")
        if initial_text:
            self.input_text.setPlainText(initial_text)
        left_layout.addWidget(self.input_text, 1)

        btn_row = QHBoxLayout()
        self.btn_load = QPushButton("📂 Cargar Archivo")
        self.btn_load.clicked.connect(self._load_file)
        btn_row.addWidget(self.btn_load)

        self.btn_clear = QPushButton("🗑️ Limpiar")
        self.btn_clear.clicked.connect(self._clear_all)
        btn_row.addWidget(self.btn_clear)
        left_layout.addLayout(btn_row)

        self.btn_process = QPushButton("⚡ Formatear Correo de Abuso")
        self.btn_process.setProperty("class", "primary")
        self.btn_process.setFixedHeight(38)
        self.btn_process.clicked.connect(self._process_input)
        left_layout.addWidget(self.btn_process)

        self.splitter.addWidget(left_card)

        # Panel Derecho: Widget de Visualización y Copia
        right_card = QFrame()
        right_card.setProperty("class", "card")
        right_card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_card)
        right_layout.setContentsMargins(10, 10, 10, 10)

        self.widget_reporte = AbuseReportWidget(self)
        right_layout.addWidget(self.widget_reporte)
        self.splitter.addWidget(right_card)

        # Configuración de proporciones responsivas (38% entrada, 62% reporte)
        self.splitter.setStretchFactor(0, 4)
        self.splitter.setStretchFactor(1, 6)
        w_actual = self.width() if self.width() > 0 else 1100
        self.splitter.setSizes([int(w_actual * 0.38), int(w_actual * 0.62)])

        main_layout.addWidget(self.splitter, 1)

        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Listo para procesar logs de abuso.")
        main_layout.addWidget(self.status_bar)

        if initial_text:
            self._process_input()

    def _process_input(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Entrada Vacía", "Por favor pega un volcado JSON en el cuadro de texto.")
            return
        cant = self.widget_reporte.cargar_datos_desde_texto(text)
        if cant > 0:
            self.status_bar.showMessage(f"✓ Se procesaron {cant} IP(s) únicas correctamente.", 4000)
        else:
            self.status_bar.showMessage("⚠️ No se pudieron extraer IPs válidas del texto ingresado.", 4000)

    def _load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo JSON de Interflow", str(BASE_DIR), "Archivos JSON (*.json);;Todos los archivos (*.*)")
        if path:
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                self.input_text.setPlainText(content)
                self._process_input()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo leer el archivo: {e}")

    def _clear_all(self):
        self.input_text.clear()
        self.widget_reporte.cargar_datos_desde_texto("")
        self.status_bar.showMessage("Cuadro limpiado.", 3000)


# =============================================================================
# EJECUCIÓN DIRECTA
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Soporte para abrir con archivo pasado por argumento
    texto_inicial = ""
    if len(sys.argv) > 1:
        ruta = Path(sys.argv[1])
        if ruta.exists():
            with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                texto_inicial = f.read()

    dialog = AbuseReportDialog(initial_text=texto_inicial)
    dialog.show()
    sys.exit(app.exec())
