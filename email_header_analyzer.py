"""
=============================================================================
  STELLAR CYBER OpenXDR - PHISHING & EMAIL HEADER ANALYZER (DFIR MODULE)
  Análisis Forense de Cabeceras RFC 822 / .EML / Anti-Spoofing & Hop-0
  Gobernanza: Technoma SOC L1/L2 - Formato DFIR de Alta Fidelidad
=============================================================================
"""

import re
import ipaddress
import urllib.parse
from email import message_from_string
from email.policy import default as default_policy
from typing import Dict, Any, List, Optional
from html import escape as he

from PySide6.QtCore import Qt, QUrl, QProcess
from PySide6.QtGui import QTextCursor, QColor, QDesktopServices, QCursor
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QTextBrowser,
    QPushButton, QFileDialog, QMessageBox, QFrame, QSplitter,
    QTableWidget, QTableWidgetItem, QHeaderView, QApplication,
    QScrollArea, QWidget, QCheckBox, QToolTip, QComboBox
)


def extract_domain_from_email(addr_str: str) -> str:
    """Extrae el dominio limpio de una dirección de correo (ej: 'Admin <ceo@empresa.com>' -> 'empresa.com')."""
    if not addr_str:
        return ""
    match = re.search(r'[\w\.-]+@([\w\.-]+\.[a-zA-Z]{2,})', addr_str)
    if match:
        return match.group(1).lower().strip()
    return ""


def defang_url(url: str) -> str:
    """Desofusca una URL para manipulación segura sin clics accidentales (hxxp://dominio[.]com)."""
    if not url:
        return ""
    clean = url.replace("http://", "hxxp://").replace("https://", "hxxps://")
    parts = clean.split("/", 3)
    if len(parts) >= 3:
        host = parts[2].replace(".", "[.]")
        parts[2] = host
        return "/".join(parts)
    return clean.replace(".", "[.]")


def parse_email_headers_forensic(raw_content: str) -> Dict[str, Any]:
    """
    Parsea cabeceras de correo RFC 822 / RFC 5322 y ejecuta heurísticas DFIR avanzadas:
    - X-Headers maliciosos y de antispam (X-PHP-Originating-Script, X-Mailer, SCL, compauth)
    - Matriz de Saltos RFC 5322 (Hop Table) con cálculo de retrasos temporales y fronteras de confianza
    - Matriz de Alineación DMARC RFC 7489 (SPF Alignment vs DKIM Alignment)
    - Detección de BEC / Account Takeover (cuando SPF/DKIM pasan pero hay fraude)
    - Desofuscación defensiva y extracción de URLs y IoCs
    Funciona 100% en memoria en Python.
    """
    import email.utils
    from datetime import datetime

    msg = message_from_string(raw_content, policy=default_policy)
    
    subject = str(msg.get("Subject", "")).strip() or "Sin Asunto"
    from_hdr = str(msg.get("From", "")).strip()
    return_path = str(msg.get("Return-Path", "")).strip()
    reply_to = str(msg.get("Reply-To", "")).strip()
    date_hdr = str(msg.get("Date", "")).strip()
    message_id = str(msg.get("Message-ID", "")).strip()
    auth_results = str(msg.get("Authentication-Results", "")).strip()
    received_spf = str(msg.get("Received-SPF", "")).strip()
    dkim_sig = str(msg.get("DKIM-Signature", "")).strip()

    # 0. Inspección Forense de X-Headers y Antispam Gateways
    x_php_script = str(msg.get("X-PHP-Originating-Script", "")).strip()
    x_mailer = str(msg.get("X-Mailer", "")).strip()
    x_originating_ip = str(msg.get("X-Originating-IP", "")).strip().strip("[]")
    x_forefront = str(msg.get("X-Forefront-Antispam-Report", "")).strip()
    x_proofpoint = str(msg.get("X-Proofpoint-Spam-Details", "")).strip()
    x_spam_status = str(msg.get("X-Spam-Status", "")).strip()

    # Recoger todas las cabeceras de Authentication-Results (puede haber más de una si pasó por varios gateways)
    all_auth_results = " ".join([str(h) for h in msg.get_all("Authentication-Results", [])])
    if not all_auth_results:
        all_auth_results = str(msg.get("Authentication-Results", "")).strip()

    # Extraer SCL (Spam Confidence Level de Microsoft 365: -1 a 9)
    scl_val = None
    if x_forefront:
        m_scl = re.search(r'\bSCL:(-?\d+)', x_forefront, re.IGNORECASE)
        if m_scl:
            scl_val = m_scl.group(1)
    
    # Extraer compauth (Composite Authentication verdict de M365)
    compauth_val = None
    if all_auth_results:
        m_comp = re.search(r'\bcompauth=(pass|fail)', all_auth_results, re.IGNORECASE)
        if m_comp:
            compauth_val = m_comp.group(1).upper()

    from_domain = extract_domain_from_email(from_hdr)
    return_domain = extract_domain_from_email(return_path)
    reply_domain = extract_domain_from_email(reply_to)

    # 1. Análisis de Autenticación Técnica (SPF / DKIM / DMARC)
    # Incluir también X-Spam-Status si contiene veredictos como dmarc_fail o spf_fail
    combined_auth = f"{all_auth_results} {received_spf} {x_spam_status}".lower()
    
    def _extract_auth_status(proto: str) -> str:
        # 1. Buscar patrón estándar proto=pass|fail
        pattern = rf"{proto}=(pass|fail|softfail|neutral|none|temperror|permerror)"
        m = re.search(pattern, combined_auth)
        if m:
            return m.group(1).upper()
        # 2. Buscar en SpamAssassin / X-Spam-Status (ej: DMARC_FAIL_QUAR, SPF_SOFTFAIL)
        if proto == "dmarc" and ("dmarc_fail" in combined_auth or "dmarc=fail" in combined_auth):
            return "FAIL"
        if proto == "spf" and "spf_softfail" in combined_auth:
            return "SOFTFAIL"
        if proto == "spf" and "spf_fail" in combined_auth:
            return "FAIL"
        if proto == "dkim" and dkim_sig:
            return "PRESENT (FIRMA EXISTE)"
        return "NO DECLARADO"

    spf_status = _extract_auth_status("spf")
    dkim_status = _extract_auth_status("dkim")
    dmarc_status = _extract_auth_status("dmarc")

    # Extraer dominio de firma DKIM (d=tag)
    dkim_domain = ""
    if dkim_sig:
        m_d = re.search(r'\bd=([a-zA-Z0-9\.\-_]+)', dkim_sig)
        if m_d:
            dkim_domain = m_d.group(1).lower().strip()
    elif "header.d=" in all_auth_results.lower():
        m_hd = re.search(r'header\.d=([a-zA-Z0-9\.\-_]+)', all_auth_results, re.IGNORECASE)
        if m_hd:
            dkim_domain = m_hd.group(1).lower().strip()

    # 2. Análisis de Saltos de Red (Hop Table RFC 5322) - Bottom-Up Cronológico
    received_headers = msg.get_all("Received", [])
    hops = []
    ipv4_regex = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    origin_ip = None

    # Si hay X-Originating-IP válida, tomarla en cuenta
    if x_originating_ip and re.match(r'^\d+\.\d+\.\d+\.\d+$', x_originating_ip):
        try:
            ip_o = ipaddress.ip_address(x_originating_ip)
            if not (ip_o.is_private or ip_o.is_loopback or ip_o.is_reserved or x_originating_ip.startswith("127.")):
                origin_ip = x_originating_ip
        except Exception:
            pass

    prev_dt = None
    hop_num = 1
    # Las cabeceras Received se añaden de abajo hacia arriba en orden cronológico
    for r_line in reversed(received_headers):
        r_str = str(r_line)
        ips_found = re.findall(ipv4_regex, r_str)
        valid_publics = []
        hop_ip = None
        for ip in ips_found:
            try:
                ip_obj = ipaddress.ip_address(ip)
                if not (ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_multicast or ip.startswith("127.") or ip.startswith("169.254.")):
                    valid_publics.append(ip)
                    if not hop_ip:
                        hop_ip = ip
                    if not origin_ip:
                        origin_ip = ip
            except Exception:
                pass
        
        # Extraer campos 'from' y 'by' del salto
        from_host = ""
        by_host = ""
        m_from = re.search(r'\bfrom\s+([^\s;]+)', r_str, re.IGNORECASE)
        if m_from:
            from_host = m_from.group(1).strip("()[]<>")
        m_by = re.search(r'\bby\s+([^\s;]+)', r_str, re.IGNORECASE)
        if m_by:
            by_host = m_by.group(1).strip("()[]<>")

        # Parsear fecha del salto si está presente al final después de ';'
        delay_sec = 0
        hop_dt = None
        if ";" in r_str:
            date_part = r_str.rsplit(";", 1)[-1].strip()
            try:
                tt = email.utils.parsedate_to_datetime(date_part)
                hop_dt = tt
                if prev_dt and hop_dt:
                    diff = (hop_dt - prev_dt).total_seconds()
                    delay_sec = max(0, int(diff))
                prev_dt = hop_dt
            except Exception:
                pass

        # Determinar límite de confianza (Trust Boundary)
        boundary = "Interno / Relay"
        r_lower = r_str.lower()
        if "outlook.com" in r_lower or "office365" in r_lower or "google.com" in r_lower or "pphosted.com" in r_lower:
            boundary = "Gateway Confiable"
        elif hop_num == 1:
            boundary = "🚨 Punto de Inyección / Hop 0"

        hops.append({
            "hop": hop_num,
            "from": from_host or "Desconocido",
            "by": by_host or "Desconocido",
            "ip": hop_ip or (valid_publics[0] if valid_publics else "Privada/Interna"),
            "delay": f"+{delay_sec}s" if hop_num > 1 else "0s",
            "delay_sec": delay_sec,
            "boundary": boundary,
            "raw": r_str[:160] + ("..." if len(r_str) > 160 else "")
        })
        hop_num += 1

    # 3. Alineación DMARC Formal (RFC 7489)
    def _extract_base_domain(dom):
        if not dom:
            return ""
        pts = dom.lower().strip().split(".")
        cc_tlds = {"com", "edu", "gov", "gob", "org", "net", "co", "mil", "nom"}
        if len(pts) >= 3 and pts[-2] in cc_tlds:
            return ".".join(pts[-3:])
        elif len(pts) >= 2:
            return ".".join(pts[-2:])
        return dom.lower().strip()

    base_from = _extract_base_domain(from_domain)
    base_return = _extract_base_domain(return_domain)
    base_reply = _extract_base_domain(reply_domain)
    base_dkim = _extract_base_domain(dkim_domain)

    # Alineación de Dominio:
    spf_aligned = bool(base_from and base_return and base_from == base_return)
    dkim_aligned = bool(base_from and base_dkim and base_from == base_dkim)

    spoofing_flags = []
    is_spoofed = False

    # A. Inyección de Scripts Maliciosos detectada (ej: PHP mail() spoofing)
    if x_php_script:
        is_spoofed = True
        spoofing_flags.append(
            f"🚨 INYECCIÓN POR SCRIPT WEB DETECTADA (X-PHP-Originating-Script): '{x_php_script}'. "
            f"El correo fue originado por un script PHP del servidor (típico de webs vulnerables o cPanel comprometidos)."
        )

    # B. Detección de Gateway Verdict (SCL y compauth)
    if scl_val is not None:
        try:
            scl_int = int(scl_val)
            if scl_int >= 5:
                spoofing_flags.append(
                    f"⚠️ GATEWAY ANTISPAM (SCL={scl_val}): Microsoft 365 marcó este correo como Spam / Phishing de alta confianza."
                )
        except Exception:
            pass

    if compauth_val == "FAIL":
        is_spoofed = True
        spoofing_flags.append("🚨 MICROSOFT COMPAUTH FAIL: Microsoft 365 invalidó la autenticidad combinada del remitente.")

    # C. Desalineación DMARC y Suplantación Directa
    if from_domain and return_domain and not spf_aligned:
        is_spoofed = True
        spoofing_flags.append(
            f"DESALINEACIÓN SPF (RFC 7489): El dominio remitente 'From' ({from_domain}) NO coincide con el 'Return-Path' ({return_domain}). Suplantación de identidad o envío no autorizado."
        )

    if from_domain and dkim_domain and not dkim_aligned:
        spoofing_flags.append(
            f"DESALINEACIÓN DKIM: La firma criptográfica DKIM pertenece a '{dkim_domain}', entidad diferente a '{from_domain}'."
        )

    if from_domain and reply_domain and base_from != base_reply:
        spoofing_flags.append(
            f"DESVÍO DE RESPUESTAS (Reply-To Mismatch): Las respuestas se redirigen a '{reply_domain}' fuera de la organización de '{from_domain}'. Indicador clave de fraude BEC."
        )

    if dmarc_status in ["FAIL", "PERMERROR"]:
        is_spoofed = True
        spoofing_flags.append("DMARC FALLIDO: Rechazado por la política de protección DMARC del dominio emisor.")

    if spf_status in ["FAIL", "SOFTFAIL"]:
        spoofing_flags.append(f"SPF {spf_status}: La IP emisora no está autorizada en los registros DNS SPF de {from_domain or 'este dominio'}.")

    # D. Heurística de BEC / Account Takeover (Cuando SPF/DKIM dan PASS pero el correo es un fraude)
    bec_keywords = [
        "transferencia", "wire transfer", "urgente", "cambio de cuenta", "factura pendiente",
        "invoice", "payroll", "tarjetas de regalo", "gift card", "actualización de datos bancarios",
        "bitcoin", "cryptocurrency", "urgent payment", "password expire"
    ]
    has_bec_intent = any(k in subject.lower() for k in bec_keywords)
    if (spf_status == "PASS" or dkim_status == "PASS") and has_bec_intent and (not spf_aligned or base_from != base_reply):
        spoofing_flags.append(
            "⚠️ POSIBLE BUSINESS EMAIL COMPROMISE (BEC): Aunque la autenticación técnica tiene firmas válidas, "
            "el asunto contiene patrones financieros urgentes con desvío de respuestas o remitente de terceros."
        )

    # 4. Extracción y Análisis Forense de URLs (Detección Living off the Cloud, Quoted-Printable & Redirecciones)
    import quopri

    url_pattern = r'https?://[^\s<>"\')]+'
    
    # Decodificar cuerpo si viene en quoted-printable (=3D, saltos de línea con =)
    try:
        decoded_qp = quopri.decodestring(raw_content.encode('utf-8', errors='ignore')).decode('utf-8', errors='ignore')
    except Exception:
        decoded_qp = ""

    raw_unquoted = urllib.parse.unquote(raw_content)
    raw_double_unquoted = urllib.parse.unquote(raw_unquoted)
    qp_unquoted = urllib.parse.unquote(decoded_qp) if decoded_qp else ""
    
    # También extraer payload directo del objeto MIME si tiene partes
    body_payloads = []
    try:
        for part in msg.walk():
            payload = part.get_payload(decode=True)
            if payload:
                body_payloads.append(payload.decode('utf-8', errors='ignore'))
    except Exception:
        pass
    body_joined = "\n".join(body_payloads)

    combined_content = (
        raw_content + "\n" +
        decoded_qp + "\n" +
        qp_unquoted + "\n" +
        raw_unquoted + "\n" +
        raw_double_unquoted + "\n" +
        body_joined
    )

    raw_matches = re.findall(url_pattern, combined_content)
    all_extracted_set = set()
    for m in raw_matches:
        all_extracted_set.add(m)
        for inner in re.findall(url_pattern, m[1:]):
            all_extracted_set.add(inner)

    extracted_urls = []
    has_high_risk_url = False

    cloud_abuse_keywords = [
        "storage.googleapis.com", "blob.core.windows.net", "s3.amazonaws.com",
        "ipfs.io", "workers.dev", "pages.dev", "firebaseapp.com", "web.app",
        "canva.site", "formkeep.com", "glitch.me", "supabase.co"
    ]

    for u in list(all_extracted_set)[:40]:
        clean_u = u.rstrip(".,;>")
        domain_u = urllib.parse.urlparse(clean_u).netloc.lower().split(":")[0]
        if not domain_u:
            continue
        extracted_urls.append({
            "original": clean_u,
            "defanged": defang_url(clean_u),
            "domain": domain_u
        })
        for pattern in cloud_abuse_keywords:
            if pattern in clean_u.lower():
                has_high_risk_url = True
                flag_msg = f"URL DE ALTO RIESGO (Living off the Cloud): Enlace alojado en servicio cloud ({pattern}) frecuentemente abusado para redirecciones o cosecha de credenciales."
                if flag_msg not in spoofing_flags:
                    spoofing_flags.append(flag_msg)
                break

    # Veredicto general
    if is_spoofed or dmarc_status in ["FAIL", "PERMERROR"] or has_high_risk_url or bool(x_php_script):
        overall_verdict = "MALICIOSO / AMENAZA DETECTADA"
        verdict_color = "#ef4444"
    elif spoofing_flags or spf_status in ["SOFTFAIL", "NEUTRAL"]:
        overall_verdict = "SOSPECHOSO / ADVERTENCIA"
        verdict_color = "#f59e0b"
    else:
        overall_verdict = "AUTÉNTICO / ALINEADO"
        verdict_color = "#10b981"

    return {
        "subject": subject,
        "from": from_hdr,
        "from_domain": from_domain,
        "return_path": return_path,
        "return_domain": return_domain,
        "reply_to": reply_to,
        "reply_domain": reply_domain,
        "date": date_hdr,
        "message_id": message_id,
        "spf_status": spf_status,
        "dkim_status": dkim_status,
        "dmarc_status": dmarc_status,
        "spf_aligned": spf_aligned,
        "dkim_aligned": dkim_aligned,
        "dkim_domain": dkim_domain,
        "origin_ip": origin_ip or "No identificada",
        "hops": hops,
        "hops_count": len(received_headers),
        "x_php_script": x_php_script,
        "x_mailer": x_mailer,
        "x_originating_ip": x_originating_ip,
        "scl_val": scl_val,
        "compauth_val": compauth_val,
        "spoofing_flags": spoofing_flags,
        "extracted_urls": extracted_urls,
        "overall_verdict": overall_verdict,
        "verdict_color": verdict_color
    }


def pick_primary_unmask_target(data: Dict[str, Any]):
    """
    Identifica de forma heurística el observable prioritario (dominio de ataque o IP de origen)
    y compila una lista ordenada de todos los candidatos detectados para auditoría en consola.
    """
    cloud_services = {
        "storage.googleapis.com", "blob.core.windows.net", "s3.amazonaws.com",
        "ipfs.io", "workers.dev", "pages.dev", "firebaseapp.com", "web.app",
        "canva.site", "formkeep.com", "glitch.me", "supabase.co"
    }
    major_generic = {
        "google.com", "microsoft.com", "apple.com", "schema.org", "w3.org"
    }

    from_domain = data.get("from_domain", "").lower().strip()
    return_domain = data.get("return_domain", "").lower().strip()
    reply_domain = data.get("reply_domain", "").lower().strip()
    origin_ip = data.get("origin_ip", "").strip()

    seen_targets = set()
    url_candidates = []
    
    for u in data.get("extracted_urls", []):
        dom = u.get("domain", "").lower().strip()
        if dom and dom not in seen_targets and dom not in major_generic:
            seen_targets.add(dom)
            is_cloud = dom in cloud_services
            is_external = not (from_domain and (dom == from_domain or dom.endswith("." + from_domain))) and \
                          not (return_domain and (dom == return_domain or dom.endswith("." + return_domain)))
            url_candidates.append({
                "target": dom,
                "is_cloud": is_cloud,
                "is_external": is_external
            })

    # Heurística de selección de objetivo primario:
    # 1. Primer dominio externo extraído de URLs que no sea de almacenamiento genérico
    primary = None
    for cand in url_candidates:
        if cand["is_external"] and not cand["is_cloud"]:
            primary = cand["target"]
            break

    # 2. Si no hay ninguno, probar el primer dominio externo aunque sea cloud
    if not primary:
        for cand in url_candidates:
            if cand["is_external"]:
                primary = cand["target"]
                break

    # 3. Si las URLs pertenecen al mismo dominio de envío, verificar si el return_domain o from_domain están suplantados
    if not primary:
        if return_domain and return_domain != from_domain:
            primary = return_domain
        elif from_domain:
            primary = from_domain
        elif url_candidates:
            primary = url_candidates[0]["target"]
        elif origin_ip and origin_ip != "No identificada":
            primary = origin_ip

    # Compilar lista ordenada de candidatos para el QComboBox
    result_list = []
    if primary:
        is_ip = bool(re.match(r"^\d+\.\d+\.\d+\.\d+$", primary))
        result_list.append({
            "target": primary,
            "label": f"⭐ {primary} [Objetivo Prioritario]",
            "type": "ip" if is_ip else "domain"
        })

    for cand in url_candidates:
        t = cand["target"]
        if t != primary:
            tag = "Cloud Abuse" if cand["is_cloud"] else "URL Extraída"
            result_list.append({
                "target": t,
                "label": f"🔗 {t} [{tag}]",
                "type": "domain"
            })

    if return_domain and return_domain != primary:
        result_list.append({
            "target": return_domain,
            "label": f"📬 {return_domain} [Return-Path]",
            "type": "domain"
        })

    if from_domain and from_domain != primary and from_domain != return_domain:
        result_list.append({
            "target": from_domain,
            "label": f"✉️ {from_domain} [Remitente From]",
            "type": "domain"
        })

    if origin_ip and origin_ip != "No identificada" and origin_ip != primary:
        result_list.append({
            "target": origin_ip,
            "label": f"🌐 {origin_ip} [IP Origen Hop 0]",
            "type": "ip"
        })

    return primary, result_list


class PhishingHeaderAnalyzerDialog(QDialog):
    """Ventana Forense para el Triaje Rápido de Correos y Cabeceras de Phishing."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📬 DFIR Phishing Header Inspector - Cockpit SOC")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1180, 780)
        self.setMinimumSize(950, 600)
        self.setStyleSheet("""
            QDialog {
                background-color: #020617;
                color: #f8fafc;
                font-family: 'Segoe UI', Tahoma, sans-serif;
            }
        """)
        self._parsed_data = {}
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 10, 12, 10)
        main_layout.setSpacing(8)

        # Barra de Título y Controles de Archivo
        header_bar = QFrame()
        header_bar.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 6px;")
        layout_header = QHBoxLayout(header_bar)
        layout_header.setContentsMargins(8, 4, 8, 4)

        lbl_title = QLabel("📬 Analizador Forense de Phishing & Cabeceras (.eml)")
        lbl_title.setStyleSheet("color: #38bdf8; font-size: 14px; font-weight: bold; border: none;")

        btn_load_eml = QPushButton("📂 Cargar Archivo (.eml / .msg / .txt)")
        btn_load_eml.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; padding: 4px 10px; border-radius: 4px; font-weight: bold;")
        btn_load_eml.clicked.connect(self._load_eml_file)

        self.chk_auto_unmask = QCheckBox("⚡ Auto-Desemmascarar en Consola")
        self.chk_auto_unmask.setChecked(True)
        self.chk_auto_unmask.setToolTip(
            "Si está marcado, al analizar la cabecera se ejecutará automáticamente\n"
            "la auditoría de origen en la Consola SOC para el objetivo prioritario detectado."
        )
        self.chk_auto_unmask.setStyleSheet("""
            QCheckBox {
                color: #38bdf8;
                font-size: 11px;
                font-weight: bold;
                border: none;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
            }
        """)

        btn_analyze = QPushButton("🚀 Analizar Cabecera")
        btn_analyze.setStyleSheet("background-color: #0284c7; color: #ffffff; padding: 4px 14px; border-radius: 4px; font-weight: bold;")
        btn_analyze.clicked.connect(self._run_analysis)

        btn_clear = QPushButton("🧹 Limpiar")
        btn_clear.setStyleSheet("background-color: #1e293b; color: #94a3b8; border: 1px solid #334155; padding: 4px 10px; border-radius: 4px;")
        btn_clear.clicked.connect(self._clear_all)

        layout_header.addWidget(lbl_title)
        layout_header.addStretch()
        layout_header.addWidget(self.chk_auto_unmask)
        layout_header.addWidget(btn_load_eml)
        layout_header.addWidget(btn_analyze)
        layout_header.addWidget(btn_clear)
        main_layout.addWidget(header_bar)

        # Splitter Principal: Arriba Entrada de Cabeceras / Abajo Resultados Forenses
        splitter = QSplitter(Qt.Vertical)

        # Panel de Entrada
        input_widget = QWidget()
        input_layout = QVBoxLayout(input_widget)
        input_layout.setContentsMargins(0, 0, 0, 0)
        lbl_input = QLabel("Pegue las cabeceras completas de correo aquí (RFC 822 / MIME Headers):")
        lbl_input.setStyleSheet("color: #94a3b8; font-size: 11px;")
        self.txt_input = QTextEdit()
        self.txt_input.setPlaceholderText("From: CEO <spoofed@company.com>\nReturn-Path: <attacker@evil-vps.com>\nSubject: Pago Urgente Factura\nAuthentication-Results: spf=fail dkim=none dmarc=fail\nReceived: from 185.220.101.5 ...")
        self.txt_input.setStyleSheet("""
            QTextEdit {
                background-color: #090d16;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                border-radius: 4px;
                font-family: 'Consolas', monospace;
                font-size: 11px;
            }
        """)
        input_layout.addWidget(lbl_input)
        input_layout.addWidget(self.txt_input)
        splitter.addWidget(input_widget)

        # Panel de Resultados
        results_widget = QWidget()
        results_layout = QVBoxLayout(results_widget)
        results_layout.setContentsMargins(0, 0, 0, 0)

        # Banner de Veredicto de Spoofing
        self.frame_verdict = QFrame()
        self.frame_verdict.setStyleSheet("background-color: #0b1120; border-left: 4px solid #38bdf8; border-radius: 4px; padding: 6px;")
        layout_verd = QHBoxLayout(self.frame_verdict)
        self.lbl_verdict = QLabel("Esperando análisis de cabeceras...")
        self.lbl_verdict.setStyleSheet("color: #94a3b8; font-size: 12px; font-weight: bold; border: none;")
        
        self.btn_copy_report = QPushButton("📋 Copiar Informe SOC")
        self.btn_copy_report.setStyleSheet("background-color: #1e293b; color: #10b981; border: 1px solid #059669; padding: 4px 10px; border-radius: 4px; font-weight: bold;")
        self.btn_copy_report.clicked.connect(self._copy_soc_report)
        self.btn_copy_report.setEnabled(False)

        self.btn_copy_nist = QPushButton("🚨 Copiar Evidencia NIST (Ticket)")
        self.btn_copy_nist.setToolTip("Copia un sumario estructurado según el estándar NIST SP 800-61r3 / Incident Response listo para Jira o tickets L2/L3.")
        self.btn_copy_nist.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #0284c7; padding: 4px 10px; border-radius: 4px; font-weight: bold;")
        self.btn_copy_nist.clicked.connect(self._copy_nist_report)
        self.btn_copy_nist.setEnabled(False)

        layout_verd.addWidget(self.lbl_verdict)
        layout_verd.addStretch()
        layout_verd.addWidget(self.btn_copy_report)
        layout_verd.addWidget(self.btn_copy_nist)
        results_layout.addWidget(self.frame_verdict)

        # Barra de Objetivos y Disparo hacia la Consola
        self.frame_actions = QFrame()
        self.frame_actions.setStyleSheet("background-color: #090d16; border: 1px solid #1e293b; border-radius: 4px; padding: 4px;")
        layout_actions = QHBoxLayout(self.frame_actions)
        layout_actions.setContentsMargins(6, 4, 6, 4)
        layout_actions.setSpacing(6)

        lbl_target_icon = QLabel("🎯 Objetivo de Auditoría:")
        lbl_target_icon.setStyleSheet("color: #38bdf8; font-size: 11px; font-weight: bold; border: none;")

        self.combo_targets = QComboBox()
        self.combo_targets.setMinimumWidth(280)
        self.combo_targets.setStyleSheet("""
            QComboBox {
                background-color: #0b1120;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 8px;
                font-family: 'Consolas', monospace;
                font-size: 11px;
            }
            QComboBox QAbstractItemView {
                background-color: #090d16;
                color: #e2e8f0;
                selection-background-color: #0284c7;
                selection-color: #ffffff;
            }
        """)

        self.btn_unmask_action = QPushButton("🕵️ Desemmascarar Origen (Consola)")
        self.btn_unmask_action.setStyleSheet("""
            QPushButton {
                background-color: #0284c7;
                color: #ffffff;
                border: 1px solid #38bdf8;
                border-radius: 4px;
                padding: 4px 10px;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover { background-color: #0369a1; }
            QPushButton:disabled { background-color: #1e293b; color: #64748b; border-color: #334155; }
        """)
        self.btn_unmask_action.clicked.connect(self._trigger_unmask_from_combo)
        self.btn_unmask_action.setEnabled(False)

        self.btn_triscan_action = QPushButton("⚡ Tri-Scan CTI")
        self.btn_triscan_action.setStyleSheet("""
            QPushButton {
                background-color: #1e293b;
                color: #38bdf8;
                border: 1px solid #0284c7;
                border-radius: 4px;
                padding: 4px 10px;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover { background-color: #334155; }
            QPushButton:disabled { background-color: #0f172a; color: #475569; border-color: #1e293b; }
        """)
        self.btn_triscan_action.clicked.connect(self._trigger_triscan_from_combo)
        self.btn_triscan_action.setEnabled(False)

        self.lbl_action_status = QLabel("Listo para auditar observables en consola.")
        self.lbl_action_status.setStyleSheet("color: #64748b; font-size: 10px; border: none;")

        layout_actions.addWidget(lbl_target_icon)
        layout_actions.addWidget(self.combo_targets)
        layout_actions.addWidget(self.btn_unmask_action)
        layout_actions.addWidget(self.btn_triscan_action)
        layout_actions.addStretch()
        layout_actions.addWidget(self.lbl_action_status)

        results_layout.addWidget(self.frame_actions)

        # Visor de Detalles Forenses con soporte interactivo de pivotes y enlaces
        self.txt_results = QTextBrowser()
        self.txt_results.setOpenExternalLinks(False)
        self.txt_results.anchorClicked.connect(self._handle_anchor_click)
        self.txt_results.setStyleSheet("""
            QTextBrowser {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #1e293b;
                border-radius: 4px;
                font-family: 'Consolas', monospace;
                font-size: 11px;
                line-height: 1.4;
            }
        """)
        results_layout.addWidget(self.txt_results)
        splitter.addWidget(results_widget)

        splitter.setSizes([220, 480])
        main_layout.addWidget(splitter, 1)

    def _load_eml_file(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo de correo", "", "Archivos de Correo (*.eml *.msg *.txt);;Todos los archivos (*.*)"
        )
        if filepath:
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                self.txt_input.setText(content)
                self._run_analysis()
            except Exception as e:
                QMessageBox.critical(self, "Error al Cargar", f"No se pudo leer el archivo: {e}")

    def _run_analysis(self):
        content = self.txt_input.toPlainText().strip()
        if not content:
            QMessageBox.warning(self, "Cabeceras Vacías", "Ingrese o cargue las cabeceras de un correo para analizar.")
            return

        data = parse_email_headers_forensic(content)
        self._parsed_data = data

        # Actualizar Banner de Veredicto
        v_col = data["verdict_color"]
        self.frame_verdict.setStyleSheet(f"background-color: #0b1120; border: 1px solid #1e293b; border-left: 5px solid {v_col}; border-radius: 4px; padding: 6px;")
        self.lbl_verdict.setText(f"VEREDICTO FORENSE: {data['overall_verdict']}")
        self.lbl_verdict.setStyleSheet(f"color: {v_col}; font-size: 13px; font-weight: bold; border: none;")
        self.btn_copy_report.setEnabled(True)
        self.btn_copy_nist.setEnabled(True)

        # Poblar Candidatos para Auditoría en Consola
        primary_target, candidates = pick_primary_unmask_target(data)
        self.combo_targets.clear()
        for cand in candidates:
            self.combo_targets.addItem(cand["label"], cand["target"])

        has_candidates = bool(candidates)
        self.btn_unmask_action.setEnabled(has_candidates)
        self.btn_triscan_action.setEnabled(has_candidates)

        # Auto-Desemmascarar si el checkbox está activo
        if self.chk_auto_unmask.isChecked() and primary_target:
            self._dispatch_unmask_target(primary_target, auto=True)
        elif primary_target:
            self.lbl_action_status.setText(
                f"<span style='color: #38bdf8;'>🎯 Objetivo seleccionado: <b>{he(primary_target)}</b>. Haga clic en [🕵️ Desemmascarar Origen]</span>"
            )

        # Generar Reporte HTML Estilizado
        html = self._build_report_html(data)
        self.txt_results.setHtml(html)

    def _trigger_unmask_from_combo(self):
        target = self.combo_targets.currentData()
        if target:
            self._dispatch_unmask_target(target, auto=False)

    def _trigger_triscan_from_combo(self):
        target = self.combo_targets.currentData()
        if target:
            self._dispatch_triscan_target(target)

    def _handle_anchor_click(self, qurl: QUrl):
        url_str = qurl.toString()
        if url_str.startswith("action:unmask:"):
            target = url_str.split("action:unmask:")[1]
            self._dispatch_unmask_target(target, auto=False)
        elif url_str.startswith("action:triscan:"):
            target = url_str.split("action:triscan:")[1]
            self._dispatch_triscan_target(target)
        elif url_str.startswith("action:abuse:"):
            target = url_str.split("action:abuse:")[1]
            self._dispatch_abuse_target(target)
        elif url_str.startswith("action:vt:"):
            target = url_str.split("action:vt:")[1]
            self._dispatch_vt_target(target)
        else:
            QDesktopServices.openUrl(qurl)

    def _dispatch_unmask_target(self, target: str, auto: bool = False):
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        if not clean_target:
            return
        parent = self.parent()
        if parent and hasattr(parent, "input_term_target") and hasattr(parent, "run_preset_unmask_origin"):
            if hasattr(parent, "_term_process") and hasattr(parent._term_process, "state") and parent._term_process.state() == QProcess.Running:
                self.lbl_action_status.setText(
                    f"<span style='color: #f59e0b;'>⚠️ Consola ocupada: Ya hay un proceso ejecutándose. Deténgalo o espere.</span>"
                )
                return

            parent.input_term_target.setText(clean_target)
            if hasattr(parent, "tabs") and hasattr(parent, "tab5"):
                parent.tabs.setCurrentWidget(parent.tab5)
            parent.run_preset_unmask_origin()
            pfx = "⚡ [AUTO] " if auto else "🎯 "
            self.lbl_action_status.setText(
                f"<span style='color: #10b981;'>{pfx}Auditoría de Origen ejecutándose en Consola para: <b>{he(clean_target)}</b></span>"
            )
        else:
            self.lbl_action_status.setText(
                f"<span style='color: #94a3b8;'>ℹ️ Objetivo listo: {he(clean_target)} (Consola no conectada)</span>"
            )

    def _dispatch_triscan_target(self, target: str):
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        if not clean_target:
            return
        parent = self.parent()
        if parent and hasattr(parent, "input_term_target") and hasattr(parent, "run_preset_triscan"):
            if hasattr(parent, "_term_process") and hasattr(parent._term_process, "state") and parent._term_process.state() == QProcess.Running:
                self.lbl_action_status.setText(
                    f"<span style='color: #f59e0b;'>⚠️ Consola ocupada: Ya hay un proceso ejecutándose.</span>"
                )
                return
            parent.input_term_target.setText(clean_target)
            if hasattr(parent, "tabs") and hasattr(parent, "tab5"):
                parent.tabs.setCurrentWidget(parent.tab5)
            parent.run_preset_triscan()
            self.lbl_action_status.setText(
                f"<span style='color: #38bdf8;'>🎯 Tri-Scan CTI ejecutándose en Consola para: <b>{he(clean_target)}</b></span>"
            )

    def _dispatch_abuse_target(self, target: str):
        clean_target = target.strip()
        if not clean_target:
            return
        parent = self.parent()
        if parent and hasattr(parent, "input_term_target") and hasattr(parent, "run_preset_abuseipdb"):
            parent.input_term_target.setText(clean_target)
            if hasattr(parent, "tabs") and hasattr(parent, "tab5"):
                parent.tabs.setCurrentWidget(parent.tab5)
            parent.run_preset_abuseipdb()
            self.lbl_action_status.setText(
                f"<span style='color: #34d399;'>🛡️ AbuseIPDB ejecutándose en Consola para: <b>{he(clean_target)}</b></span>"
            )

    def _dispatch_vt_target(self, target: str):
        clean_target = target.strip()
        if not clean_target:
            return
        parent = self.parent()
        if parent and hasattr(parent, "input_term_target") and hasattr(parent, "run_preset_virustotal"):
            parent.input_term_target.setText(clean_target)
            if hasattr(parent, "tabs") and hasattr(parent, "tab5"):
                parent.tabs.setCurrentWidget(parent.tab5)
            parent.run_preset_virustotal()
            self.lbl_action_status.setText(
                f"<span style='color: #fb923c;'>🦠 VirusTotal ejecutándose en Consola para: <b>{he(clean_target)}</b></span>"
            )

    def _build_report_html(self, d: Dict[str, Any]) -> str:
        def _badge(val: str) -> str:
            val_u = val.upper()
            if "PASS" in val_u:
                bg, fg = "#064e3b", "#34d399"
            elif "FAIL" in val_u:
                bg, fg = "#7f1d1d", "#fca5a5"
            elif "SOFTFAIL" in val_u or "NEUTRAL" in val_u:
                bg, fg = "#78350f", "#fcd34d"
            else:
                bg, fg = "#1e293b", "#94a3b8"
            return f"<span style='background-color: {bg}; color: {fg}; padding: 2px 6px; border-radius: 3px; font-weight: bold;'>{he(val)}</span>"

        def _align_badge(is_aligned: bool) -> str:
            if is_aligned:
                return "<span style='background-color: #064e3b; color: #34d399; padding: 2px 5px; border-radius: 3px; font-weight: bold;'>ALINEADO ✅</span>"
            return "<span style='background-color: #7f1d1d; color: #fca5a5; padding: 2px 5px; border-radius: 3px; font-weight: bold;'>DESALINEADO 🚨</span>"

        flags_html = ""
        if d["spoofing_flags"]:
            flags_html = "<div style='background-color: #450a0a; border: 1px solid #dc2626; border-radius: 4px; padding: 8px; margin-bottom: 8px;'>"
            flags_html += "<b style='color: #fca5a5; font-size: 12px;'>🚨 INDICADORES DE SUPLANTACIÓN Y RIESGO DFIR:</b><br>"
            for f in d["spoofing_flags"]:
                flags_html += f"<span style='color: #fee2e2;'>• {he(f)}</span><br>"
            flags_html += "</div>"
        else:
            flags_html = "<div style='background-color: #064e3b; border: 1px solid #059669; border-radius: 4px; padding: 6px; margin-bottom: 8px;'>"
            flags_html += "<span style='color: #34d399;'>✅ No se detectaron discrepancias evidentes entre 'From' y 'Return-Path'.</span></div>"

        # Hop 0 Actions
        origin = d["origin_ip"]
        if origin and origin != "No identificada":
            origin_console_actions = (
                f"&nbsp;&nbsp;[ <a href='action:triscan:{origin}' style='color: #38bdf8; font-weight: bold; text-decoration: none;'>⚡ Tri-Scan en Consola</a> | "
                f"<a href='action:abuse:{origin}' style='color: #34d399; font-weight: bold; text-decoration: none;'>🛡️ AbuseIPDB en Consola</a> ]"
            )
            origin_pivots = (
                f"<br><span style='font-size: 10px; color: #64748b;'>Enlaces Externos: </span>"
                f"[ <a href='https://talosintelligence.com/reputation_center/lookup?search={origin}' style='color: #38bdf8; text-decoration: none;'><b>🦊 Cisco Talos</b></a> | "
                f"<a href='https://www.abuseipdb.com/check/{origin}' style='color: #34d399; text-decoration: none;'><b>🛡️ AbuseIPDB</b></a> | "
                f"<a href='https://www.virustotal.com/gui/ip-address/{origin}' style='color: #fb923c; text-decoration: none;'><b>🦠 VirusTotal</b></a> | "
                f"<a href='https://ipinfo.io/{origin}' style='color: #a78bfa; text-decoration: none;'><b>🔍 IPinfo</b></a> ]"
            )
        else:
            origin_console_actions = ""
            origin_pivots = ""
        origin_display = f"<b style='color: #38bdf8; font-size: 12px;'>{he(origin)}</b>{origin_console_actions}{origin_pivots}"

        from_action = f"&nbsp;&nbsp;<a href='action:unmask:{he(d['from_domain'])}' style='color: #38bdf8; text-decoration: none; font-weight: bold;'>[🕵️ Desemmascarar]</a>" if d['from_domain'] else ""
        return_action = f"&nbsp;&nbsp;<a href='action:unmask:{he(d['return_domain'])}' style='color: #38bdf8; text-decoration: none; font-weight: bold;'>[🕵️ Desemmascarar]</a>" if d['return_domain'] else ""

        # X-Headers Box si se detectaron scripts o gateways
        x_headers_rows = []
        if d.get("x_php_script"):
            x_headers_rows.append(f"<tr><td style='padding: 4px; color: #f87171;'><b>X-PHP-Originating-Script:</b></td><td style='padding: 4px; color: #fca5a5;'><b>{he(d['x_php_script'])}</b> <span style='color: #f87171;'>(Inyección de script PHP)</span></td></tr>")
        if d.get("x_originating_ip"):
            x_headers_rows.append(f"<tr><td style='padding: 4px; color: #38bdf8;'><b>X-Originating-IP:</b></td><td style='padding: 4px; color: #e2e8f0;'>{he(d['x_originating_ip'])}</td></tr>")
        if d.get("scl_val") is not None:
            scl_c = "#ef4444" if int(d['scl_val']) >= 5 else "#10b981"
            x_headers_rows.append(f"<tr><td style='padding: 4px; color: #94a3b8;'><b>Spam Confidence Level (SCL):</b></td><td style='padding: 4px; color: {scl_c}; font-weight: bold;'>{he(d['scl_val'])} / 9</td></tr>")
        if d.get("compauth_val"):
            x_headers_rows.append(f"<tr><td style='padding: 4px; color: #94a3b8;'><b>Microsoft compauth:</b></td><td style='padding: 4px;'>{_badge(d['compauth_val'])}</td></tr>")
        if d.get("x_mailer"):
            x_headers_rows.append(f"<tr><td style='padding: 4px; color: #94a3b8;'><b>X-Mailer:</b></td><td style='padding: 4px; color: #cbd5e1;'>{he(d['x_mailer'])}</td></tr>")

        x_section_html = ""
        if x_headers_rows:
            x_section_html = f"""
            <br><b style='color: #f59e0b; font-size: 11px;'>⚙️ CABECERAS ESPECIALES & GATEWAY TELEMETRY (X-HEADERS):</b>
            <table style='width: 100%; border-collapse: collapse; margin-top: 4px; font-family: Consolas; font-size: 11px; background-color: #0b1120; border: 1px solid #1e293b;'>
                {''.join(x_headers_rows)}
            </table>
            """

        # Matriz de Alineación DMARC (RFC 7489)
        alignment_html = f"""
        <table style='width: 100%; border-collapse: collapse; margin-top: 6px; font-family: Consolas; font-size: 11px; background-color: #090d16; border: 1px solid #1e293b;'>
            <tr style='background-color: #0f172a; color: #94a3b8;'>
                <th style='padding: 4px; border: 1px solid #1e293b; text-align: left;'>Mecanismo</th>
                <th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Autenticación Técnica</th>
                <th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Dominio Evaluado</th>
                <th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Alineación DMARC (RFC 7489)</th>
            </tr>
            <tr>
                <td style='padding: 4px; border: 1px solid #1e293b; color: #38bdf8;'><b>SPF</b></td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>{_badge(d['spf_status'])}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center; color: #cbd5e1;'>{he(d['return_domain'] or 'N/A')}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>{_align_badge(d.get('spf_aligned', False))}</td>
            </tr>
            <tr>
                <td style='padding: 4px; border: 1px solid #1e293b; color: #38bdf8;'><b>DKIM</b></td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>{_badge(d['dkim_status'])}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center; color: #cbd5e1;'>{he(d.get('dkim_domain') or 'N/A')}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>{_align_badge(d.get('dkim_aligned', False))}</td>
            </tr>
            <tr>
                <td style='padding: 4px; border: 1px solid #1e293b; color: #38bdf8;'><b>DMARC</b></td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>{_badge(d['dmarc_status'])}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center; color: #cbd5e1;'>{he(d['from_domain'] or 'N/A')}</td>
                <td style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>
                    <span style='color: {"#34d399" if d["dmarc_status"] == "PASS" else ("#f87171" if d["dmarc_status"] in ["FAIL", "PERMERROR"] else ("#34d399" if d.get("spf_aligned") and d.get("spf_status") == "PASS" else "#f59e0b"))}; font-weight: bold;'>
                        {"CUMPLE POLÍTICA ✅" if d["dmarc_status"] == "PASS" or (d.get("spf_aligned") and d.get("spf_status") == "PASS") else ("DESALINEADO / RECHAZO DMARC 🚨" if d["dmarc_status"] in ["FAIL", "PERMERROR"] else "NO DEFINIDO")}
                    </span>
                </td>
            </tr>
        </table>
        """

        # Tabla de Saltos Temporales RFC 5322 (Hop Table)
        hops_html = ""
        if d.get("hops"):
            hops_html = "<br><b style='color: #38bdf8; font-size: 11px;'>📡 MATRIZ DE SALTOS DE RED RFC 5322 (HOP TABLE - CRONOLÓGICA BOTTOM-UP):</b><br>"
            hops_html += "<table style='width: 100%; border-collapse: collapse; margin-top: 4px; font-family: Consolas; font-size: 11px;'>"
            hops_html += "<tr style='background-color: #0f172a; color: #94a3b8; text-align: left;'>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b; width: 45px; text-align: center;'>Salto</th>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b;'>Servidor Emisor (From)</th>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b;'>Servidor Receptor (By)</th>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b;'>IP Extraída</th>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b; width: 55px; text-align: center;'>Delay</th>"
            hops_html += "<th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Frontera / Confianza</th>"
            hops_html += "</tr>"
            for h in d["hops"]:
                hop_ip = h["ip"]
                ip_link = hop_ip
                if hop_ip and hop_ip not in ["Privada/Interna", "No identificada"]:
                    ip_link = f"<a href='action:triscan:{hop_ip}' style='color: #38bdf8; text-decoration: none;'><b>{he(hop_ip)}</b></a>"
                b_color = "#f87171" if "🚨" in h["boundary"] else ("#34d399" if "Gateway" in h["boundary"] else "#94a3b8")
                hops_html += f"""<tr>
                    <td style='padding: 3px; border: 1px solid #1e293b; text-align: center; color: #f59e0b;'><b>#{h['hop']}</b></td>
                    <td style='padding: 3px; border: 1px solid #1e293b; color: #cbd5e1;'>{he(h['from'])}</td>
                    <td style='padding: 3px; border: 1px solid #1e293b; color: #94a3b8;'>{he(h['by'])}</td>
                    <td style='padding: 3px; border: 1px solid #1e293b;'>{ip_link}</td>
                    <td style='padding: 3px; border: 1px solid #1e293b; text-align: center; color: #fbbf24;'>{h['delay']}</td>
                    <td style='padding: 3px; border: 1px solid #1e293b; text-align: center; color: {b_color};'><b>{he(h['boundary'])}</b></td>
                </tr>"""
            hops_html += "</table>"

        # URLs con botones interactivos hacia la Consola SOC
        urls_html = ""
        if d["extracted_urls"]:
            urls_html = "<br><b style='color: #38bdf8; font-size: 11px;'>🔗 URLs Y ENLACES EXTRAÍDOS (DEFANGED) & PIVOTES SANDBOX:</b><br>"
            urls_html += "<table style='width: 100%; border-collapse: collapse; margin-top: 4px; font-size: 11px;'>"
            urls_html += "<tr style='background-color: #0f172a; color: #94a3b8; text-align: left;'>"
            urls_html += "<th style='padding: 4px; border: 1px solid #1e293b;'>Dominio</th>"
            urls_html += "<th style='padding: 4px; border: 1px solid #1e293b;'>Enlace Desofuscado (Defanged)</th>"
            urls_html += "<th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Acciones Consola SOC</th>"
            urls_html += "<th style='padding: 4px; border: 1px solid #1e293b; text-align: center;'>Pivotes Sandboxes / CTI</th>"
            urls_html += "</tr>"
            for u in d["extracted_urls"][:15]:
                raw_url = u['original']
                dom_u = u['domain']
                encoded_url = urllib.parse.quote(raw_url)
                actions_cell = (
                    f"<a href='action:unmask:{he(dom_u)}' style='background-color: #0369a1; color: #ffffff; padding: 2px 6px; border-radius: 3px; text-decoration: none; font-weight: bold;'>🕵️ Desemmascarar</a>&nbsp;"
                    f"<a href='action:triscan:{he(dom_u)}' style='background-color: #1e293b; color: #38bdf8; border: 1px solid #0284c7; padding: 2px 6px; border-radius: 3px; text-decoration: none; font-weight: bold;'>⚡ Tri-Scan</a>"
                )
                pivots_cell = (
                    f"<a href='https://urlscan.io/search/#page.url%3A%22{encoded_url}%22' style='color: #38bdf8; text-decoration: none;'>[🌐 URLScan]</a>&nbsp;"
                    f"<a href='https://www.virustotal.com/gui/search/{encoded_url}' style='color: #fb923c; text-decoration: none;'>[🦠 VT]</a>&nbsp;"
                    f"<a href='https://www.browserling.com/browse/win/7/chrome/90/{encoded_url}' style='color: #34d399; text-decoration: none;'>[🌐 Browserling]</a>&nbsp;"
                    f"<a href='https://app.any.run/' style='color: #c084fc; text-decoration: none;'>[⚡ Any.Run]</a>"
                )
                urls_html += f"<tr><td style='padding: 3px; border: 1px solid #1e293b; color: #f59e0b;'><b>{he(dom_u)}</b></td><td style='padding: 3px; border: 1px solid #1e293b; color: #94a3b8;'>{he(u['defanged'])}</td><td style='padding: 3px; border: 1px solid #1e293b; text-align: center;'>{actions_cell}</td><td style='padding: 3px; border: 1px solid #1e293b; text-align: center;'>{pivots_cell}</td></tr>"
            urls_html += "</table>"
            if len(d["extracted_urls"]) > 15:
                urls_html += f"<span style='color: #64748b;'>... ({len(d['extracted_urls']) - 15} enlaces adicionales omitidos por brevedad)</span><br>"
        else:
            urls_html = "<br><span style='color: #64748b;'>🔗 No se encontraron URLs en las cabeceras analizadas.</span><br>"

        html = f"""
        {flags_html}
        <table style='width: 100%; border-collapse: collapse; font-family: Consolas; font-size: 11px;'>
            <tr style='background-color: #0b1120;'>
                <td style='padding: 5px; width: 140px; color: #94a3b8;'><b>Asunto:</b></td>
                <td style='padding: 5px; color: #ffffff;'><b>{he(d['subject'])}</b></td>
            </tr>
            <tr>
                <td style='padding: 5px; color: #94a3b8;'><b>Remitente (From):</b></td>
                <td style='padding: 5px; color: #38bdf8;'>{he(d['from'])}{from_action}</td>
            </tr>
            <tr style='background-color: #0b1120;'>
                <td style='padding: 5px; color: #94a3b8;'><b>Return-Path:</b></td>
                <td style='padding: 5px; color: {'#ef4444' if not d.get('spf_aligned') and d['return_domain'] else '#10b981'};'>
                    {he(d['return_path'] or 'No especificado')}{return_action}
                </td>
            </tr>
            <tr>
                <td style='padding: 5px; color: #94a3b8;'><b>Reply-To:</b></td>
                <td style='padding: 5px; color: {'#f59e0b' if d['from_domain'] != d['reply_domain'] and d['reply_domain'] else '#e2e8f0'};'>
                    {he(d['reply_to'] or 'Mismo que remitente')}
                </td>
            </tr>
            <tr style='background-color: #0b1120;'>
                <td style='padding: 5px; color: #94a3b8;'><b>Fecha / Hora:</b></td>
                <td style='padding: 5px; color: #94a3b8;'>{he(d['date'])}</td>
            </tr>
            <tr>
                <td style='padding: 5px; color: #94a3b8;'><b>Message-ID:</b></td>
                <td style='padding: 5px; color: #64748b;'>{he(d['message_id'])}</td>
            </tr>
            <tr style='background-color: #0b1120;'>
                <td style='padding: 5px; color: #94a3b8;'><b>IP Origen (Hop 0):</b></td>
                <td style='padding: 5px;'>
                    {origin_display} &nbsp;&nbsp;
                    <span style='color: #64748b;'>(Total saltos Received: {d['hops_count']})</span>
                </td>
            </tr>
        </table>
        {x_section_html}
        <br><b style='color: #38bdf8; font-size: 11px;'>🛡️ MATRIZ DE AUTENTICACIÓN Y ALINEACIÓN DMARC (RFC 7489):</b>
        {alignment_html}
        {hops_html}
        {urls_html}
        """
        return html

    def _copy_soc_report(self):
        if not self._parsed_data:
            return
        d = self._parsed_data
        report = f"""### 🛡️ INFORME FORENSE DE TRIAJE PHISHING (SOC)
- **Veredicto:** {d['overall_verdict']}
- **Asunto:** {d['subject']}
- **Remitente Visible (From):** `{d['from']}`
- **Ruta de Retorno (Return-Path):** `{d['return_path']}`
- **Reply-To:** `{d['reply_to']}`
- **IP Origen (Hop 0):** `{d['origin_ip']}`
- **Autenticación:** SPF={d['spf_status']} | DKIM={d['dkim_status']} | DMARC={d['dmarc_status']}
- **Alineación DMARC (RFC 7489):** SPF Aligned={'SÍ' if d.get('spf_aligned') else 'NO'} | DKIM Aligned={'SÍ' if d.get('dkim_aligned') else 'NO'}

**Indicadores de Riesgo / Spoofing:**
"""
        if d['spoofing_flags']:
            for f in d['spoofing_flags']:
                report += f"- ⚠️ {f}\n"
        else:
            report += "- No se detectaron discrepancias entre 'From' y 'Return-Path'.\n"

        if d.get('x_php_script'):
            report += f"\n**Inyección de Scripts (X-Headers):**\n- `{d['x_php_script']}`\n"

        if d['extracted_urls']:
            report += "\n**URLs Detectadas (Defanged):**\n"
            for u in d['extracted_urls'][:10]:
                report += f"- `{u['defanged']}`\n"

        clipboard = QApplication.clipboard()
        clipboard.setText(report)
        QMessageBox.information(self, "Informe SOC", "Informe de triaje de phishing copiado al portapapeles en formato Markdown.")

    def _copy_nist_report(self):
        """Exporta un resumen formal de evidencia según NIST SP 800-61r3 para tickets Jira/Escalación."""
        if not self._parsed_data:
            return
        d = self._parsed_data
        
        # Buscar primer salto sospechoso
        first_hop = d["hops"][0] if d.get("hops") else {}
        first_hop_info = f"{first_hop.get('ip', d['origin_ip'])} ({first_hop.get('from', 'N/A')})"

        nist_ticket = f"""======================================================================
INCIDENT ESCALATION EVIDENCE - NIST SP 800-61r3 (PHISHING / SPOOFING)
======================================================================
1. RESUMEN EJECUTIVO DEL INCIDENTE
   - Clasificación: {d['overall_verdict']}
   - Vector de Entrada: Correo Electrónico (Phishing / Brand Impersonation)
   - Asunto del Correo: {d['subject']}
   - Remitente Declarado (From): {d['from']}
   - Remitente Técnico (Return-Path): {d['return_path'] or 'N/A'}
   - Buzón de Desvío (Reply-To): {d['reply_to'] or 'Mismo que From'}

2. TRAZABILIDAD DE INFRAESTRUCTURA (HOP 0 FORENSICS)
   - IP Origen Real (First Ingestion Hop): {d['origin_ip']}
   - Servidor Host Inyector: {first_hop_info}
   - Total de Nodos en Tránsito (Received): {d['hops_count']} saltos
   - X-Originating-IP: {d.get('x_originating_ip') or 'No reportada'}
   - Script Web Inyector: {d.get('x_php_script') or 'Ninguno identificado'}

3. POSTURA CRIPTOGRÁFICA Y DE AUTENTICACIÓN (RFC 7489)
   - Estado SPF: {d['spf_status']} (Alineado: {'SÍ' if d.get('spf_aligned') else 'NO - Desalineado'})
   - Estado DKIM: {d['dkim_status']} (Dominio d={d.get('dkim_domain') or 'N/A'} | Alineado: {'SÍ' if d.get('dkim_aligned') else 'NO'})
   - Estado DMARC: {d['dmarc_status']}
   - Gateway SCL Score: {d.get('scl_val') or 'N/A'} | compauth: {d.get('compauth_val') or 'N/A'}

4. EVIDENCIAS CRÍTICAS IDENTIFICADAS
"""
        if d['spoofing_flags']:
            for flag in d['spoofing_flags']:
                nist_ticket += f"   [!] {flag}\n"
        else:
            nist_ticket += "   [-] No se evidenciaron discrepancias críticas de remitente.\n"

        if d['extracted_urls']:
            nist_ticket += "\n5. OBSERVABLES DE AMENAZA / IOCs EXTRAÍDOS (DEFANGED):\n"
            for u in d['extracted_urls'][:8]:
                nist_ticket += f"   - URL: {u['defanged']} [Host: {u['domain']}]\n"

        nist_ticket += f"""
6. ACCIONES DE CONTENCIÓN RECOMENDADAS (PLAYBOOK SOC L1/L2)
   1. Bloqueo Perimetral: Aislar la IP {d['origin_ip']} en el Firewall / IPS perimetral.
   2. Purga de Mensajería: Purgar mensajes con Subject '{d['subject']}' y Message-ID '{d['message_id']}'.
   3. Remediación de Cuentas: Si la cuenta pertenece al tenant, forzar cambio de credenciales y revocación de tokens OAuth.
======================================================================
"""
        clipboard = QApplication.clipboard()
        clipboard.setText(nist_ticket)
        QMessageBox.information(
            self,
            "Evidencia NIST Copiada",
            "La evidencia forense estructurada bajo el estándar NIST SP 800-61r3 fue copiada al portapapeles lista para escalación a L2/L3 o ticket."
        )

    def _clear_all(self):
        self.txt_input.clear()
        self.txt_results.clear()
        self._parsed_data = {}
        self.lbl_verdict.setText("Esperando análisis de cabeceras...")
        self.lbl_verdict.setStyleSheet("color: #94a3b8; font-size: 12px; font-weight: bold; border: none;")
        self.frame_verdict.setStyleSheet("background-color: #0b1120; border-left: 4px solid #38bdf8; border-radius: 4px; padding: 6px;")
        self.btn_copy_report.setEnabled(False)
        self.btn_copy_nist.setEnabled(False)
        self.combo_targets.clear()
        self.btn_unmask_action.setEnabled(False)
        self.btn_triscan_action.setEnabled(False)
        self.lbl_action_status.setText("Listo para auditar observables en consola.")

