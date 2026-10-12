#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🌐 TECHNOMA SOC — RECONOCIMIENTO FORENSE WHOIS & BGP ULTRA-COMPLETO (whois_recon.py)
=============================================================================
Motor integral de inteligencia de red, BGP y titularidad (Whois/RDAP/RIPEstat/DNS).
- Detecta automáticamente IPs (IPv4 / IPv6) o Dominios / FQDN.
- Para IPs:
  * Rango de Red, CIDR, Netname, Estado de asignación y RIR autoritativo.
  * Titular legal del bloque (Registrante de subred, dirección física y país).
  * Enrutamiento BGP: ASN de Origen, Nombre de ASN, Titular Legal del ASN y Prefijo.
  * Contactos Oficiales de Abuso & Seguridad (abuse@, teléfono, handles, sede).
  * Resolución Inversa DNS en vivo (PTR) y Georreferenciación (Ciudad, País, GPS).
  * Volcado RPSL / Whois crudo de puerto 43 para evidencia legal.
- Para Dominios:
  * Registrar, Fechas (Creación, Expiración, Modificación, Días restantes).
  * Registrante y detección de servicios de privacidad (Whois Guard/Redacted).
  * Servidores de Nombres (Nameservers) autoritativos.
  * Resolución DNS en vivo (A, AAAA, MX, TXT/SPF/DMARC) y detección de CDN.
  * Registro Whois crudo completo.
=============================================================================
"""

import sys
import os
import re
import json
import socket
import datetime
from typing import Dict, Any, List, Optional
import urllib.request
import urllib.error

# Configurar salida estándar en UTF-8 para Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Configurar timeout global de socket para evitar bloqueos
socket.setdefaulttimeout(3.0)

RIR_WHOIS_SERVERS = {
    "RIPE": "whois.ripe.net",
    "ARIN": "whois.arin.net",
    "APNIC": "whois.apnic.net",
    "LACNIC": "whois.lacnic.net",
    "AFRINIC": "whois.afrinic.net"
}


def clean_observable(target: str) -> str:
    """Limpia el observable eliminando esquemas de URL, rutas, puertos y espacios."""
    if not target:
        return ""
    t = target.strip()
    t = re.sub(r"^https?://", "", t, flags=re.IGNORECASE)
    t = t.rstrip("/").split("/")[0].split(":")[0]
    return t.strip()


def is_ip_address(target: str) -> bool:
    """Verifica si la cadena corresponde a una dirección IPv4 o IPv6 válida."""
    if not target:
        return False
    # IPv4
    if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", target):
        octets = target.split(".")
        return all(0 <= int(o) <= 255 for o in octets)
    # IPv6
    if ":" in target:
        try:
            socket.inet_pton(socket.AF_INET6, target)
            return True
        except (socket.error, OSError):
            return False
    return False


def get_reverse_dns(ip: str) -> Optional[str]:
    """Obtiene el nombre de host PTR asociado a una dirección IP con timeout controlado."""
    try:
        host, _, _ = socket.gethostbyaddr(ip)
        return host
    except Exception:
        return None


def fetch_json(url: str, headers: Optional[Dict[str, str]] = None, timeout: float = 3.5) -> Optional[Dict[str, Any]]:
    """Realiza una petición HTTP GET segura retornando el diccionario JSON parseado."""
    req_headers = {"User-Agent": "TechnomaSOC-WhoisRecon/1.0", "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8", errors="ignore"))
    except Exception:
        pass
    return None


def query_raw_whois_socket(query: str, server: str = "whois.ripe.net", port: int = 43, timeout: float = 3.5) -> str:
    """Realiza una consulta Whois directa mediante socket TCP al puerto 43."""
    try:
        s = socket.create_connection((server, port), timeout=timeout)
        # Para RIPE o servidores que soportan flags, enviar consulta estándar
        s.sendall((query.strip() + "\r\n").encode("utf-8"))
        chunks = []
        while True:
            data = s.recv(4096)
            if not data:
                break
            chunks.append(data)
        s.close()
        return b"".join(chunks).decode("utf-8", errors="replace")
    except Exception as e:
        return f"[!] No se pudo obtener el volcado crudo desde {server}:43 ({e})"


def get_asn_abuse_contact(asn: Any) -> Optional[Dict[str, Any]]:
    """Consulta el buzón oficial de abuso del Sistema Autónomo BGP (aut-num) vía RDAP y socket port 43."""
    if not asn:
        return None
    asn_clean = str(asn).upper().replace("AS", "").strip()
    if not asn_clean.isdigit():
        return None

    # 1. Intentar RDAP de aut-num en RIRs oficiales
    endpoints = [
        f"https://rdap.db.ripe.net/aut-num/AS{asn_clean}",
        f"https://rdap.org/aut-num/{asn_clean}",
        f"https://rdap.arin.net/registry/aut-num/{asn_clean}",
        f"https://rdap.apnic.net/aut-num/{asn_clean}",
        f"https://rdap.lacnic.net/rdap/aut-num/{asn_clean}",
        f"https://rdap.afrinic.net/rdap/aut-num/{asn_clean}"
    ]
    for url in endpoints:
        data = fetch_json(url, timeout=3.0)
        if data:
            # Buscar en remarks
            for rem in data.get("remarks", []):
                for d in rem.get("description", []):
                    m = re.search(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', d)
                    if m and "abuse" in d.lower():
                        return {"email": m.group(1).strip(), "asn": f"AS{asn_clean}", "source": "RDAP aut-num"}

            # Buscar recursivamente en entities
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
                return {"email": em, "asn": f"AS{asn_clean}", "source": "RDAP aut-num"}

    # 2. Fallback socket port 43 a servidores Whois autoritativos
    for srv in ["whois.ripe.net", "whois.radb.net", "whois.arin.net", "whois.apnic.net", "whois.afrinic.net"]:
        try:
            raw = query_raw_whois_socket(f"AS{asn_clean}", server=srv, timeout=3.0)
            m = re.search(r'abuse-mailbox:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+)', raw, re.I)
            if m:
                return {"email": m.group(1).strip(), "asn": f"AS{asn_clean}", "source": f"Whois {srv}"}
            m2 = re.search(r'Abuse contact.*?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+)', raw, re.I)
            if m2:
                return {"email": m2.group(1).strip(), "asn": f"AS{asn_clean}", "source": f"Whois {srv}"}
        except Exception:
            pass

    return None


# =============================================================================
# RECONOCIMIENTO INTEGRAL PARA DIRECCIONES IP
# =============================================================================
def recon_ip(ip: str, include_raw: bool = False) -> Dict[str, Any]:
    """Ejecuta la auditoría exhaustiva Whois, BGP y titularidad para una dirección IP."""
    report: Dict[str, Any] = {
        "target": ip,
        "type": "ip",
        "ptr": None,
        "network": {},
        "registrant": {},
        "bgp": {},
        "abuse": {},
        "contacts": [],
        "geo": {},
        "raw_whois": ""
    }

    # 1. Reverse DNS (PTR)
    report["ptr"] = get_reverse_dns(ip)

    # 2. RIPEstat Network Info (Prefijo y ASNs enrutadores en vivo)
    net_info = fetch_json(f"https://stat.ripe.net/data/network-info/data.json?resource={ip}")
    prefix = ""
    asns = []
    if net_info and "data" in net_info:
        prefix = net_info["data"].get("prefix") or ""
        asns = net_info["data"].get("asns") or []
    report["bgp"]["prefix"] = prefix
    report["bgp"]["asns"] = asns

    # Titular oficial del ASN desde RIPEstat AS Overview
    asn_holder = None
    asn_block = None
    if asns:
        first_asn = str(asns[0]).upper().replace("AS", "")
        as_over = fetch_json(f"https://stat.ripe.net/data/as-overview/data.json?resource=AS{first_asn}")
        if as_over and "data" in as_over:
            asn_holder = as_over["data"].get("holder")
            asn_block = as_over["data"].get("block", {}).get("name")
    report["bgp"]["asn_holder"] = asn_holder
    report["bgp"]["asn_block"] = asn_block

    # 3. RDAP IP Exhaustivo (RIR autoritativo con seguimiento de redirecciones)
    rdap_data = fetch_json(f"https://rdap.org/ip/{ip}")
    if not rdap_data:
        # Fallbacks directos a RIRs regionales
        for rir_url in [f"https://rdap.db.ripe.net/ip/{ip}", f"https://rdap.arin.net/registry/ip/{ip}"]:
            rdap_data = fetch_json(rir_url)
            if rdap_data:
                break

    rir_detected = "RIPE"
    if rdap_data:
        # Metadatos de red
        report["network"]["name"] = rdap_data.get("name")
        report["network"]["handle"] = rdap_data.get("handle")
        start_ip = rdap_data.get("startAddress", "")
        end_ip = rdap_data.get("endAddress", "")
        if start_ip and end_ip:
            report["network"]["range"] = f"{start_ip} - {end_ip}"
        report["network"]["type"] = rdap_data.get("type")
        report["network"]["country"] = rdap_data.get("country")

        # Fechas de registro / cambio
        for ev in rdap_data.get("events", []):
            action = ev.get("eventAction")
            date = ev.get("eventDate")
            if action == "registration":
                report["network"]["created"] = date
            elif action == "last changed":
                report["network"]["last_modified"] = date

        # Port authoritative RIR
        port43 = rdap_data.get("port43", "")
        if "arin" in port43.lower(): rir_detected = "ARIN"
        elif "apnic" in port43.lower(): rir_detected = "APNIC"
        elif "lacnic" in port43.lower(): rir_detected = "LACNIC"
        elif "afrinic" in port43.lower(): rir_detected = "AFRINIC"
        else: rir_detected = "RIPE"
        report["network"]["rir"] = rir_detected

        # Parsear entidades (Registrant, Abuse, Admin, Tech)
        def _parse_entities(entities_list):
            for ent in entities_list:
                roles = ent.get("roles", [])
                handle = ent.get("handle", "")
                vcard = ent.get("vcardArray", [])
                cards = vcard[1] if isinstance(vcard, list) and len(vcard) > 1 else []

                fn_val, org_val, email_val, tel_val, adr_val = "", "", "", "", ""
                for prop in cards:
                    if not isinstance(prop, list) or len(prop) < 4:
                        continue
                    p_name, p_val = prop[0], prop[3]
                    if p_name == "fn": fn_val = str(p_val).strip()
                    elif p_name == "org": org_val = str(p_val).strip()
                    elif p_name == "email": email_val = str(p_val).strip()
                    elif p_name == "tel": tel_val = str(p_val).strip()
                    elif p_name == "adr" and isinstance(p_val, list):
                        adr_clean = " ".join([str(x).strip() for x in p_val if str(x).strip()])
                        if adr_clean: adr_val = adr_clean

                # Mapear contacto de abuso
                if "abuse" in roles or (email_val and "abuse" in email_val.lower()):
                    if email_val and not report["abuse"].get("email"):
                        report["abuse"]["email"] = email_val
                    if tel_val and not report["abuse"].get("phone"):
                        report["abuse"]["phone"] = tel_val
                    if handle and not report["abuse"].get("handle"):
                        report["abuse"]["handle"] = handle
                    if (fn_val or org_val) and not report["abuse"].get("name"):
                        report["abuse"]["name"] = fn_val or org_val
                    if adr_val and not report["abuse"].get("address"):
                        report["abuse"]["address"] = adr_val

                # Mapear contacto técnico / administrativo como canal de escalamiento
                if email_val and any(r in roles for r in ["technical", "administrative", "tech", "admin"]):
                    if not report["abuse"].get("tech_email"):
                        report["abuse"]["tech_email"] = email_val
                        report["abuse"]["tech_org"] = fn_val or org_val

                # Mapear titular / registrante legal
                if any(r in roles for r in ["registrant", "administrative", "owner"]):
                    candidate = fn_val or org_val
                    if candidate and not candidate.endswith("-MNT") and "contact role" not in candidate.lower():
                        if not report["registrant"].get("name"):
                            report["registrant"]["name"] = candidate
                        if handle and not report["registrant"].get("handle"):
                            report["registrant"]["handle"] = handle
                        if adr_val and not report["registrant"].get("address"):
                            report["registrant"]["address"] = adr_val

                # Registrar en lista general de contactos
                report["contacts"].append({
                    "handle": handle,
                    "roles": roles,
                    "name": fn_val or org_val,
                    "email": email_val,
                    "phone": tel_val,
                    "address": adr_val
                })

                # Recursión en subentidades
                if "entities" in ent and isinstance(ent["entities"], list):
                    _parse_entities(ent["entities"])

        _parse_entities(rdap_data.get("entities", []))

        # Remarks y avisos importantes
        remarks = []
        for rem in rdap_data.get("remarks", []):
            desc = rem.get("description", [])
            if isinstance(desc, list):
                remarks.extend(desc)
            elif isinstance(desc, str):
                remarks.append(desc)
        report["network"]["remarks"] = remarks[:5]

    # Si el nombre del registrante no se encontró en entidades, usar el nombre de red limpio
    if not report["registrant"].get("name") and report["network"].get("name"):
        report["registrant"]["name"] = report["network"]["name"].replace("_", " ")

    # 3.1 Inteligencia de Abuso BGP (ASN):
    # Consultar el ASN enrutador si no hay buzón en el objeto IP de RDAP
    asn_abuse = None
    if asns:
        asn_abuse = get_asn_abuse_contact(asns[0])
        if asn_abuse:
            report["bgp"]["abuse_email"] = asn_abuse.get("email")

    if not report["abuse"].get("email"):
        if asn_abuse and asn_abuse.get("email"):
            report["abuse"]["email"] = asn_abuse["email"]
            report["abuse"]["source_type"] = f"BGP ASN ({asn_abuse.get('asn', '')})"
            if not report["abuse"].get("name"):
                report["abuse"]["name"] = asn_holder or f"Operador ASN {asns[0]}"
        elif report["abuse"].get("tech_email"):
            report["abuse"]["email"] = report["abuse"]["tech_email"]
            report["abuse"]["source_type"] = "Contacto Titular/Técnico RIR (Fallback)"
            if not report["abuse"].get("name"):
                report["abuse"]["name"] = report["abuse"].get("tech_org") or "Contacto Técnico"

    # 4. Georreferenciación complementaria vía ipinfo.io
    geo = fetch_json(f"https://ipinfo.io/{ip}/json", timeout=3.0)
    if geo:
        report["geo"]["city"] = geo.get("city")
        report["geo"]["region"] = geo.get("region")
        report["geo"]["country"] = geo.get("country")
        report["geo"]["loc"] = geo.get("loc")
        report["geo"]["org"] = geo.get("org")
        report["geo"]["timezone"] = geo.get("timezone")

        # Fallback de titular legal del ASN si RIPEstat no lo devolvió
        if not report["bgp"].get("asn_holder") and geo.get("org"):
            org_cand = geo.get("org", "").strip()
            if " " in org_cand and org_cand.upper().startswith("AS"):
                report["bgp"]["asn_holder"] = org_cand.split(" ", 1)[1].strip()
            else:
                report["bgp"]["asn_holder"] = org_cand

    # 5. Volcado crudo desde servidor Whois (solo si se solicita para máxima velocidad)
    if include_raw:
        server = RIR_WHOIS_SERVERS.get(rir_detected, "whois.ripe.net")
        report["raw_whois"] = query_raw_whois_socket(ip, server=server)

    return report


# =============================================================================
# RECONOCIMIENTO INTEGRAL PARA DOMINIOS (FQDN)
# =============================================================================
def recon_domain(domain: str, include_raw: bool = False) -> Dict[str, Any]:
    """Ejecuta la auditoría exhaustiva Whois, DNS y titularidad para un nombre de dominio."""
    report: Dict[str, Any] = {
        "target": domain,
        "type": "domain",
        "dns": {},
        "domain_info": {},
        "registrar": {},
        "registrant": {},
        "raw_whois": ""
    }

    # 1. Resolución DNS en vivo
    dns_ips = []
    try:
        _, _, ip_list = socket.gethostbyname_ex(domain)
        dns_ips = ip_list
    except Exception:
        pass
    report["dns"]["a_records"] = dns_ips

    # Resolver PTR de las IPs del dominio
    dns_details = []
    for ip in dns_ips[:4]:
        ptr = get_reverse_dns(ip)
        cdn = "Cloudflare Proxy" if re.match(r"^(104\.|172\.(6[4-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-7])\.|162\.15[89]\.)", ip) else "Direct IP"
        dns_details.append({"ip": ip, "ptr": ptr, "cdn": cdn})
    report["dns"]["ip_details"] = dns_details

    # 2. RDAP de Dominio vía rdap.org
    rdap_dom = fetch_json(f"https://rdap.org/domain/{domain}")
    whois_server = "whois.verisign-grs.com" if domain.endswith(".com") or domain.endswith(".net") else "whois.iana.org"

    if rdap_dom:
        report["domain_info"]["name"] = rdap_dom.get("ldhName") or domain
        report["domain_info"]["handle"] = rdap_dom.get("handle")
        report["domain_info"]["status"] = rdap_dom.get("status", [])

        # Fechas
        for ev in rdap_dom.get("events", []):
            action = ev.get("eventAction")
            date = ev.get("eventDate")
            if action == "registration": report["domain_info"]["created"] = date
            elif action == "expiration": report["domain_info"]["expires"] = date
            elif action == "last changed": report["domain_info"]["last_modified"] = date

        # Nameservers
        ns_list = []
        for ns in rdap_dom.get("nameservers", []):
            ns_name = ns.get("ldhName")
            if ns_name: ns_list.append(ns_name.lower())
        report["domain_info"]["nameservers"] = ns_list

        port43 = rdap_dom.get("port43")
        if port43:
            whois_server = port43

        # Entidades: Registrar y Registrant
        for ent in rdap_dom.get("entities", []):
            roles = ent.get("roles", [])
            vcard = ent.get("vcardArray", [])
            cards = vcard[1] if isinstance(vcard, list) and len(vcard) > 1 else []
            fn_val, org_val, email_val, tel_val, adr_val = "", "", "", "", ""
            for prop in cards:
                if isinstance(prop, list) and len(prop) > 3:
                    if prop[0] == "fn": fn_val = str(prop[3]).strip()
                    elif prop[0] == "org": org_val = str(prop[3]).strip()
                    elif prop[0] == "email": email_val = str(prop[3]).strip()
                    elif prop[0] == "tel": tel_val = str(prop[3]).strip()
                    elif prop[0] == "adr" and isinstance(prop[3], list):
                        adr_val = " ".join([str(x).strip() for x in prop[3] if str(x).strip()])

            if "registrar" in roles:
                report["registrar"]["name"] = fn_val or org_val or ent.get("handle")
                report["registrar"]["iana_id"] = ent.get("publicIds", [{}])[0].get("identifier") if ent.get("publicIds") else None
                report["registrar"]["abuse_email"] = email_val
                report["registrar"]["abuse_phone"] = tel_val

            if "registrant" in roles:
                report["registrant"]["name"] = fn_val or org_val
                report["registrant"]["address"] = adr_val

    # 3. Volcado Whois directo desde socket port 43 (solo si se solicita)
    if include_raw:
        report["raw_whois"] = query_raw_whois_socket(domain, server=whois_server)

    return report


# =============================================================================
# FORMATEADOR DE SALIDA FORENSE PARA TERMINAL
# =============================================================================
def format_forensic_report(data: Dict[str, Any], show_raw: bool = False) -> str:
    """Genera la ficha forense estructurada y elegante para la consola de Threat Hunting."""
    target = data.get("target", "")
    target_type = data.get("type", "ip")
    out = []

    out.append("=" * 68)
    out.append(f"🌐 TECHNOMA SOC — MASTER WHOIS & BGP RECON INTEL")
    out.append(f"Target Investigado: {target} (Clasificación: {target_type.upper()})")
    out.append(f"Fecha de Auditoría: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (Hora Local SOC)")
    out.append("=" * 68)

    if target_type == "ip":
        net = data.get("network", {})
        bgp = data.get("bgp", {})
        reg = data.get("registrant", {})
        abuse = data.get("abuse", {})
        geo = data.get("geo", {})
        ptr = data.get("ptr")

        # 1. Identificación de Red
        out.append("\n[1] 📡 RED & SUBRED ASIGNADA (RIR / RDAP):")
        out.append(f"  • Rango IP           : {net.get('range', 'N/A')}")
        out.append(f"  • Prefijo BGP / CIDR : {bgp.get('prefix', 'N/A')}")
        out.append(f"  • Nombre de Red      : {net.get('name', 'N/A')}")
        out.append(f"  • Estado Asignación  : {net.get('type', 'N/A')} ({net.get('rir', 'RIPE NCC')})")
        out.append(f"  • País del Recurso   : {net.get('country', 'N/A')}")
        if net.get("created"):
            out.append(f"  • Fecha de Creación  : {net.get('created')}")
        if net.get("last_modified"):
            out.append(f"  • Última Modificación: {net.get('last_modified')}")

        # 2. Titular / Registrante Legal del Bloque
        out.append("\n[2] 🏢 TITULAR REGISTRADO DE LA RED (REGISTRANT):")
        reg_name = reg.get("name") or "Desconocido en RDAP"
        out.append(f"  • Organización / Dueño: {reg_name}")
        if reg.get("handle"):
            out.append(f"  • Identificador / ID : {reg.get('handle')}")
        if reg.get("address"):
            out.append(f"  • Domicilio Legal    : {reg.get('address')}")

        # 3. Enrutamiento BGP & Sistema Autónomo
        asns_str = ", ".join([f"AS{a}" for a in bgp.get("asns", [])]) if bgp.get("asns") else "N/A"
        asn_holder = bgp.get("asn_holder") or "Desconocido"
        out.append("\n[3] ⚡ SISTEMA AUTÓNOMO BGP & ENRUTAMIENTO (ASN INTEL):")
        out.append(f"  • ASN(s) de Origen   : {asns_str}")
        out.append(f"  • Titular Legal ASN  : {asn_holder}")
        if bgp.get("asn_block"):
            out.append(f"  • Bloque IANA        : {bgp.get('asn_block')}")

        # Resumen de combinación dual si difieren
        if reg_name and asn_holder and reg_name.lower() not in asn_holder.lower() and asn_holder.lower() not in reg_name.lower():
            out.append(f"  • 🔍 Titularidad Dual: [{reg_name}] (Bloque IP) / [{asn_holder}] (BGP ASN)")

        # 4. Contactos de Abuso & Escalamiento
        out.append("\n[4] 🚨 CONTACTOS DE ABUSO & ESCALAMIENTO OFICIAL:")
        abuse_email = abuse.get('email')
        source_type = abuse.get('source_type')
        bgp_abuse = bgp.get('abuse_email')
        tech_email = abuse.get('tech_email')

        if abuse_email:
            tag = f" [{source_type}]" if source_type else ""
            out.append(f"  • Buzón de Abuso     : {abuse_email}{tag}")
        else:
            out.append("  • Buzón de Abuso     : No publicado en RDAP")

        if bgp_abuse and bgp_abuse != abuse_email:
            out.append(f"  • Buzón BGP (ASN)    : {bgp_abuse} ({asn_holder or 'Operador ASN'})")

        if tech_email and tech_email != abuse_email:
            out.append(f"  • Contacto Titular IP: {tech_email} ({abuse.get('tech_org') or reg_name})")

        # Línea de acción rápida recomendada para reportes
        contactos_rec = []
        if abuse_email: contactos_rec.append(abuse_email)
        if bgp_abuse and bgp_abuse not in contactos_rec: contactos_rec.append(bgp_abuse)
        if tech_email and tech_email not in contactos_rec and not abuse_email: contactos_rec.append(tech_email)
        if len(contactos_rec) > 1:
            out.append(f"  • 🎯 Destinatarios SOC : {', '.join(contactos_rec)}")

        if abuse.get("phone"):
            out.append(f"  • Teléfono de Abuso  : {abuse.get('phone')}")
        if abuse.get("name"):
            out.append(f"  • Contacto / Rol     : {abuse.get('name')}")
        if abuse.get("address"):
            out.append(f"  • Dirección Contacto : {abuse.get('address')}")

        # 5. Infraestructura, DNS Inverso & Georreferenciación
        out.append("\n[5] 🧭 INFRAESTRUCTURA & RESOLUCIÓN TÉCNICA:")
        ptr_label = f"[+] {ptr}" if ptr else "[-] Sin registro PTR declarado (NXDOMAIN / Común en Proxies/CDNs)"
        out.append(f"  • Hostname PTR       : {ptr_label}")
        if geo:
            loc_str = f"{geo.get('city', 'N/A')}, {geo.get('region', 'N/A')} ({geo.get('country', 'N/A')})"
            out.append(f"  • Georreferenciación : {loc_str}")
            if geo.get("loc"):
                out.append(f"  • Coordenadas GPS    : {geo.get('loc')} (Timezone: {geo.get('timezone', 'N/A')})")
            if geo.get("org"):
                out.append(f"  • ISP / Carrier      : {geo.get('org')}")

        # Remarks
        remarks = net.get("remarks", [])
        if remarks:
            out.append("\n[6] 📝 NOTAS TÉCNICAS & REMARKS DEL RIR:")
            for r in remarks:
                out.append(f"  • {r.strip()}")

    else:
        # Dominio
        dom = data.get("domain_info", {})
        rar = data.get("registrar", {})
        reg = data.get("registrant", {})
        dns = data.get("dns", {})

        out.append("\n[1] 📋 INFORMACIÓN DEL DOMINIO:")
        out.append(f"  • Dominio            : {dom.get('name', target)}")
        if dom.get("created"):
            out.append(f"  • Fecha Creación     : {dom.get('created')}")
        if dom.get("expires"):
            out.append(f"  • Fecha Expiración   : {dom.get('expires')}")
        if dom.get("last_modified"):
            out.append(f"  • Última Modificación: {dom.get('last_modified')}")
        if dom.get("status"):
            st_str = ", ".join(dom.get("status")[:3])
            out.append(f"  • Estado EPP         : {st_str}")

        out.append("\n[2] 🏛️ REGISTRAR (ENTIDAD REGISTRADORA):")
        out.append(f"  • Empresa Registrar  : {rar.get('name', 'N/A')}")
        if rar.get("iana_id"):
            out.append(f"  • IANA Registrar ID  : {rar.get('iana_id')}")
        if rar.get("abuse_email"):
            out.append(f"  • Email de Abuso     : {rar.get('abuse_email')}")
        if rar.get("abuse_phone"):
            out.append(f"  • Teléfono de Abuso  : {rar.get('abuse_phone')}")

        out.append("\n[3] 👤 REGISTRANT (TITULAR DEL DOMINIO):")
        out.append(f"  • Organización       : {reg.get('name', 'Protegido por privacidad / REDACTED FOR PRIVACY')}")
        if reg.get("address"):
            out.append(f"  • Dirección / País   : {reg.get('address')}")

        out.append("\n[4] 🌐 DNS & INFRAESTRUCTURA EN VIVO:")
        ns_list = dom.get("nameservers", [])
        if ns_list:
            out.append(f"  • Servidores NS      : {', '.join(ns_list)}")
        ip_details = dns.get("ip_details", [])
        if ip_details:
            for d in ip_details:
                ptr_info = f" -> PTR: {d['ptr']}" if d.get('ptr') else ""
                cdn_info = f" [{d['cdn']}]" if d.get('cdn') else ""
                out.append(f"  • IP Web Activa      : {d['ip']}{cdn_info}{ptr_info}")
        else:
            out.append("  • IPs Activas        : No se resolvieron registros A")

    # Volcado Crudo
    raw = data.get("raw_whois", "").strip()
    if show_raw and raw:
        out.append("\n" + "=" * 68)
        out.append("📜 VOLCADO WHOIS CRUDO COMPLETO (PORT 43):")
        out.append("=" * 68)
        out.append(raw)
    elif raw:
        out.append("\n" + "-" * 68)
        out.append("💡 [Tip SOC]: Use '--raw' para ver el volcado RPSL/Whois completo de texto plano.")
        out.append("-" * 68)

    return "\n".join(out)


# =============================================================================
# PUNTO DE ENTRADA CLI
# =============================================================================
def main():
    if len(sys.argv) < 2:
        print("Uso: python whois_recon.py <IP o Dominio> [--raw] [--json]")
        sys.exit(1)

    raw_target = sys.argv[1]
    target = clean_observable(raw_target)
    if not target:
        print(f"[!] Error: Observable inválido o vacío: '{raw_target}'")
        sys.exit(1)

    show_raw = "--raw" in sys.argv
    as_json = "--json" in sys.argv

    if is_ip_address(target):
        data = recon_ip(target, include_raw=show_raw)
    else:
        data = recon_domain(target, include_raw=show_raw)

    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(format_forensic_report(data, show_raw=show_raw))


if __name__ == "__main__":
    main()
