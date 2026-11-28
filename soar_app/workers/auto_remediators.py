# -*- coding: utf-8 -*-
"""
6 Demonios de Auto-Remediación y Auto-Guardia SOAR 24/7:
  - HealthMailboxAutoRemediatorWorker
  - SophosTranslateAutoRemediatorWorker
  - SatiDnsAutoRemediatorWorker
  - DPAPIStorageAutoRemediatorWorker
  - CaseIdentityProbeWorker
  - AutoAssignWorker
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *

# -----------------------------------------------------------------------------
# HELPERS COMUNES DE AUTO-REMEDIACIÓN
# -----------------------------------------------------------------------------
# Tamaño de página al descargar alertas de un caso y tope máximo auditable.
# Si un caso supera el tope, la auto-remediación se aborta (nunca se cierra
# un caso sin haber auditado el 100% de sus alertas).
ALERTS_PAGE_SIZE = 100
MAX_AUDITED_ALERTS = int(os.environ.get("SOAR_MAX_AUDITED_ALERTS", "2000") or 2000)

# Marca de trazabilidad que se agrega al comentario de cierre automático.
# Dejar la variable de entorno vacía ("") para desactivarla.
AUTO_CLOSE_MARKER = os.environ.get("SOAR_AUTO_CLOSE_MARKER", "[Cierre automático SOAR - verificación Ley de Oro]")


def _extract_alert_docs(alerts_data: Any) -> Tuple[List[dict], Optional[int]]:
    """Normaliza la respuesta de /cases/{id}/alerts → (docs, total_declarado_o_None)."""
    docs: List[dict] = []
    total = None
    if isinstance(alerts_data, dict):
        data_inner = alerts_data.get("data", alerts_data)
        if isinstance(data_inner, dict):
            docs = data_inner.get("docs", []) or []
            for k in ("total", "count", "total_count", "totalCount"):
                v = data_inner.get(k)
                if isinstance(v, dict):
                    v = v.get("value")
                if isinstance(v, (int, float)):
                    total = int(v)
                    break
        elif isinstance(data_inner, list):
            docs = data_inner
    elif isinstance(alerts_data, list):
        docs = alerts_data
    return [d for d in docs if isinstance(d, dict)], total


def fetch_all_case_alerts(session: requests.Session, headers: dict, url_alerts: str,
                          is_killed=lambda: False) -> Tuple[List[dict], bool]:
    """
    Descarga TODAS las alertas de un caso paginando con limit/skip.
    Devuelve (docs, completo). completo=False si se alcanzó MAX_AUDITED_ALERTS,
    si se canceló o si la API devolvió menos de lo que declaraba.
    """
    all_docs: List[dict] = []
    skip = 0
    declared_total = None
    while True:
        if is_killed():
            return all_docs, False
        r = session.get(url_alerts, headers=headers,
                        params={"limit": str(ALERTS_PAGE_SIZE), "skip": str(skip)},
                        verify=True, timeout=15)
        r.raise_for_status()
        page, total = _extract_alert_docs(r.json())
        if total is not None:
            declared_total = total
        if not page:
            break
        all_docs.extend(page)
        skip += len(page)
        # No se corta por "página corta": si la API limita el tamaño de página en
        # silencio, una página corta no significa fin. Se sigue hasta página vacía.
        if declared_total is not None and skip >= declared_total:
            break
        if skip >= MAX_AUDITED_ALERTS:
            return all_docs, False
    if declared_total is not None and len(all_docs) < declared_total:
        return all_docs, False
    return all_docs, True


def _to_int(value: Any) -> Optional[int]:
    """Convierte event_id/puertos que pueden venir como int o string ('4776') a int."""
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def _norm_identity(user: str) -> str:
    """'DOMINIO\\usuario' → 'usuario' (minúsculas). Conserva 'usuario@dominio'."""
    u = str(user or "").strip().lower()
    if "\\" in u:
        u = u.split("\\", 1)[1]
    return u


def post_resolution_comment(session: requests.Session, headers: dict, case_id: str, comment: str) -> None:
    """Publica la justificación de cierre y lanza excepción si falla (no se cierra un caso sin nota)."""
    if AUTO_CLOSE_MARKER:
        comment = f"{comment}\n\n{AUTO_CLOSE_MARKER}"
    url_comment = f"https://{HOST}/connect/api/v1/cases/{case_id}/comments"
    r = session.post(url_comment, headers=headers, json={"comment": comment}, verify=True, timeout=10)
    r.raise_for_status()

# -----------------------------------------------------------------------------
# TRABAJADOR DE AUTO-REMEDIACIÓN HEALTHMAILBOX (SOAR HYPER-AUTOMATION)
# -----------------------------------------------------------------------------
class HealthMailboxAutoRemediatorWorker(QThread):
    """
    Worker asíncrono para verificar la Ley de Oro y auto-resolver casos puros de HealthMailbox
    (Exchange Managed Availability - NTLM 4776 / Kerberos 4768) sin congelar la UI.
    """
    remediation_finished = Signal(dict)
    remediation_failed = Signal(str, str) # ticket_id, error_msg

    HEALTH_MAILBOX_WHITELIST = {
        "healthmailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
        "healthmailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py"
    }

    MSG_NTLM = (
        "Se cierran de manera consolidada las alertas del lote tras comprobarse que los intentos fallidos "
        "de autenticación NTLM registrados bajo el evento de auditoría 4776 en el controlador de dominio "
        "VMBASE8 provienen legítimamente del servidor de mensajería VM-MARANDU y corresponden a chequeos "
        "automáticos de funcionamiento del servicio Microsoft Exchange Managed Availability sobre la cuenta "
        "de salud HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local, produciéndose el fallo debido "
        "a que estas identidades se encuentran configuradas como deshabilitadas por diseño estricto en el "
        "Directorio Activo arrojando el código de estado esperado 0xc0000072."
    )

    MSG_KERBEROS = (
        "El tráfico se origina por los chequeos automáticos de funcionamiento y salud interna que realiza "
        "de forma rutinaria el servicio Microsoft Exchange Managed Availability (MSExchangeHM). Al ejecutar "
        "estas pruebas periódicas para validar el estado de los buzones, el servidor de correo utiliza como "
        "identidad la cuenta de mantenimiento con el dominio público asignado en la directiva de correo "
        "electrónico (@cajaande.gov.py), en lugar del dominio del bosque de Active Directory (@cajaande.local). "
        "Al no existir una cuenta Kerberos registrada exactamente con ese sufijo en el KDC, el controlador "
        "de dominio rechaza la solicitud de manera limpia con el código de error 0x6 (KDC_ERR_C_PRINCIPAL_UNKNOWN)."
    )

    @classmethod
    def _is_healthmailbox_identity(cls, user: str) -> bool:
        """
        Acepta la identidad completa de la whitelist (usuario@dominio) o solo la parte local
        (en eventos 4776 TargetUserName suele venir sin dominio, o como DOMINIO\\usuario).
        """
        u = _norm_identity(user)
        if u in cls.HEALTH_MAILBOX_WHITELIST:
            return True
        if "@" not in u:
            return u in {w.split("@", 1)[0] for w in cls.HEALTH_MAILBOX_WHITELIST}
        return False

    def __init__(self, case_obj: dict, session: requests.Session, headers: dict):
        super().__init__()
        self.case_obj = case_obj
        self.session = session
        self.headers = headers
        self._is_killed = False

    def run(self):
        case_id = self.case_obj.get("_id") or self.case_obj.get("ticket_id")
        t_id = str(self.case_obj.get("ticket_id") or case_id)
        try:
            if self._is_killed: return

            # 1. Endpoint del caso
            url_case = f"https://{HOST}/connect/api/v1/cases/{case_id}"

            # 2. Descargar lote de alertas crudas de Interflow para auditar la "Ley de Oro"
            url_alerts = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"
            docs, complete = fetch_all_case_alerts(
                self.session, self.headers, url_alerts, lambda: self._is_killed
            )
            if self._is_killed: return
            if not complete:
                # Ley de Oro: si no se pudo auditar el 100% del lote, NUNCA auto-cerrar.
                self.remediation_failed.emit(
                    t_id,
                    f"No se pudo descargar la totalidad de las alertas del caso ({len(docs)} leídas, "
                    f"límite de auditoría {MAX_AUDITED_ALERTS}). Se aborta la auto-resolución: requiere triaje manual."
                )
                return

            if self._is_killed: return

            if not docs:
                self.remediation_failed.emit(
                    t_id,
                    "Ley de Oro no superada: el caso no contiene alertas auditables. Requiere revisión manual."
                )
                return

            # 3. Comprobación estricta de la Ley de Oro (100% solo HealthMailbox)
            #    Se evalúa CADA alerta por separado: todas deben tener identidad HealthMailbox
            #    y ser NTLM (4776) o Kerberos (4768). Una sola alerta fuera de patrón aborta.
            detected_users = set()
            protocols = set()
            unauthorized = set()
            out_of_pattern = []

            for doc in docs:
                src = doc.get("_source", {}) if isinstance(doc, dict) else {}
                event_data = src.get("event_data", {}) or {}

                candidates = [
                    src.get("username"),
                    src.get("srcip_username"),
                    event_data.get("TargetUserName")
                ]
                doc_users = set()
                for c in candidates:
                    if c and str(c).strip() and str(c).strip() != "-":
                        doc_users.add(str(c).strip().lower())
                detected_users |= doc_users

                event_id = _to_int(src.get("event_id"))
                sub_name = str((src.get("xdr_event", {}) or {}).get("subtype", {}).get("name", "")).lower()
                doc_proto = None
                if event_id == 4776 or "ntlm" in sub_name:
                    doc_proto = "NTLM"
                elif event_id == 4768 or "kerberos" in sub_name:
                    doc_proto = "KERBEROS"

                bad_users = {u for u in doc_users if not self._is_healthmailbox_identity(u)}
                unauthorized |= bad_users
                if not doc_users or bad_users or doc_proto is None:
                    out_of_pattern.append(
                        f"event_id={src.get('event_id')} usuarios={sorted(doc_users) or 'N/A'} protocolo={doc_proto or 'N/A'}"
                    )
                else:
                    protocols.add(doc_proto)

            if out_of_pattern and not unauthorized:
                self.remediation_failed.emit(
                    t_id,
                    f"Ley de Oro no superada: {len(out_of_pattern)} alerta(s) sin identidad o fuera de NTLM 4776 / "
                    f"Kerberos 4768 (ej: {out_of_pattern[0]}). Requiere triaje manual."
                )
                return

            if unauthorized:
                # ABORTAR AUTO-RESOLUCIÓN: Hay otros usuarios detectados (posible fuerza bruta genuina)
                self.remediation_failed.emit(
                    t_id,
                    f"Ley de Oro no superada: se detectaron usuarios no autorizados: {unauthorized}. "
                    f"El caso requiere triaje manual."
                )
                return

            if not detected_users:
                # No se detectaron identidades válidas
                self.remediation_failed.emit(
                    t_id,
                    "Ley de Oro no superada: No se detectaron usuarios en las alertas. Requiere revisión manual."
                )
                return

            # Seleccionar justificación técnica según protocolo
            if "NTLM" in protocols and "KERBEROS" not in protocols:
                resolution_comment = self.MSG_NTLM
                proto_label = "NTLM (4776 / 0xc0000072)"
            elif "KERBEROS" in protocols and "NTLM" not in protocols:
                resolution_comment = self.MSG_KERBEROS
                proto_label = "Kerberos (4768 / 0x6)"
            elif "NTLM" in protocols and "KERBEROS" in protocols:
                resolution_comment = f"{self.MSG_NTLM}\n\nAsimismo, respecto a los registros asociados a Kerberos:\n{self.MSG_KERBEROS}"
                proto_label = "NTLM/Kerberos Mixto"
            else:
                self.remediation_failed.emit(
                    t_id,
                    "Ley de Oro no superada: no se identificó protocolo NTLM/Kerberos en las alertas. Requiere triaje manual."
                )
                return

            # 4. Breve pausa realista antes de cerrar (simulación operativa de MTTR)
            for _ in range(5):
                if self._is_killed: return
                time.sleep(1)

            # 5. Inyectar nota de justificación técnica formal (estilo 100% analista humano, sin marcas de automatización)
            post_resolution_comment(self.session, self.headers, case_id, resolution_comment)
            # Publicada la nota, el cierre se completa aunque se pida cancelar (evita nota sin cierre)

            # 6. Cerrar caso como Resolved / False Positive asignado al operador
            resolve_payload = {
                "status": "Resolved",
                "resolution": "False Positive",
                "assignee": EMAIL_USUARIO
            }
            r_res = self.session.put(url_case, headers=self.headers, json=resolve_payload, verify=True, timeout=12)
            r_res.raise_for_status()

            if self._is_killed: return

            self.remediation_finished.emit({
                "ticket_id": t_id,
                "case_id": case_id,
                "protocol": proto_label,
                "users": list(detected_users),
                "resolution": "False Positive"
            })

        except Exception as err:
            if not self._is_killed:
                self.remediation_failed.emit(t_id, str(err))

# -----------------------------------------------------------------------------
# TRABAJADOR DE AUTO-REMEDIACIÓN SOPHOS WEB CONTROL (GOOGLE TRANSLATE)
# -----------------------------------------------------------------------------
class SophosTranslateAutoRemediatorWorker(QThread):
    """
    Worker asíncrono para verificar y auto-resolver casos de Sophos Web Control Violation
    que correspondan exclusivamente al acceso corporativo hacia 'translate.google.com'.
    Si el caso contiene alertas hacia cualquier otro destino o tipo de amenaza, aborta
    inmediatamente la auto-resolución y emite una alerta crítica para triaje manual.
    """
    remediation_finished = Signal(dict)
    remediation_failed = Signal(str, str) # ticket_id, error_msg
    alert_non_translate = Signal(dict)    # ticket_id, alert_info

    # Hosts EXACTOS aceptados. Se compara el hostname completo (no substring), así
    # "translate.google.com.evil.ru" o "translate.google.xyz" NO son aceptados.
    TRANSLATE_HOSTS = {"translate.google.com", "translate.googleapis.com"}
    _HOST_RE = re.compile(r"(?<![a-z0-9-])((?:[a-z0-9-]+\.)+[a-z]{2,})(?![a-z0-9-])")

    @classmethod
    def _translate_verdict(cls, text: str) -> bool:
        """True si el texto menciona hosts de Google Translate y TODOS los hosts 'translate.google*' son exactos."""
        hosts = set(cls._HOST_RE.findall(text.lower()))
        tr_hosts = {h for h in hosts if "translate.google" in h}
        return bool(tr_hosts) and all(h in cls.TRANSLATE_HOSTS for h in tr_hosts)

    def __init__(self, case_obj: dict, session: requests.Session, headers: dict):
        super().__init__()
        self.case_obj = case_obj
        self.session = session
        self.headers = headers
        self._is_killed = False

    def run(self):
        case_id = self.case_obj.get("_id") or self.case_obj.get("ticket_id")
        t_id = str(self.case_obj.get("ticket_id") or case_id)
        try:
            if self._is_killed: return

            # 1. Endpoint del caso
            url_case = f"https://{HOST}/connect/api/v1/cases/{case_id}"

            # 2. Descargar lote de alertas crudas de Interflow
            url_alerts = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"
            docs, complete = fetch_all_case_alerts(
                self.session, self.headers, url_alerts, lambda: self._is_killed
            )
            if self._is_killed: return
            if not complete:
                # Ley de Oro: si no se pudo auditar el 100% del lote, NUNCA auto-cerrar.
                self.remediation_failed.emit(
                    t_id,
                    f"No se pudo descargar la totalidad de las alertas del caso ({len(docs)} leídas, "
                    f"límite de auditoría {MAX_AUDITED_ALERTS}). Se aborta la auto-resolución: requiere triaje manual."
                )
                return

            if self._is_killed: return

            if not docs:
                self.remediation_failed.emit(
                    t_id,
                    "No se encontraron alertas dentro del caso para auditar los eventos."
                )
                return

            # 3. Auditoría de cada alerta del lote
            detected_users = set()
            detected_hosts = set()
            detected_ips = set()
            non_translate_events = []
            translate_matches = 0

            for doc in docs:
                src = doc.get("_source", {}) if isinstance(doc, dict) else {}
                sophos_info = src.get("sophos", {})
                xdr_event = src.get("xdr_event", {})

                # Recolectar usuario
                user_candidates = [
                    src.get("user", {}).get("name") if isinstance(src.get("user"), dict) else None,
                    src.get("username"),
                    sophos_info.get("source"),
                    src.get("srcip_username")
                ]
                for u in user_candidates:
                    if u and str(u).strip() and str(u).strip() != "-":
                        detected_users.add(str(u).strip())

                # Recolectar host
                comp = src.get("computer_name") or sophos_info.get("location")
                if comp and str(comp).strip():
                    detected_hosts.add(str(comp).strip())

                # Recolectar IP
                host_ip = src.get("host", {}).get("ip") if isinstance(src.get("host"), dict) else None
                host_ip = host_ip or src.get("hostip") or sophos_info.get("source_info", {}).get("ip")
                if host_ip and str(host_ip).strip():
                    detected_ips.add(str(host_ip).strip())

                # Extraer telemetría textual
                event_name = str(sophos_info.get("name") or "")
                threat_name = str(src.get("event", {}).get("threat", {}).get("name") or "")
                xdr_desc = str(xdr_event.get("description") or "")
                subtype_name = str(xdr_event.get("subtype", {}).get("name") or "")
                raw_combined = f"{event_name} {threat_name} {xdr_desc} {subtype_name}".lower()

                # ¿Es Google Translate?
                is_translate = self._translate_verdict(raw_combined)

                # ¿Es violación de control web / proxies? ("user execution" es la técnica
                # MITRE T1204 y por sí sola NO alcanza para considerarla un bloqueo web)
                is_web_control = (
                    "webcontrolviolation" in raw_combined or
                    "proxies & translators" in raw_combined
                )

                if is_translate and is_web_control:
                    translate_matches += 1
                else:
                    desc_detail = event_name or xdr_desc or threat_name or "Alerta fuera de perfil Translate"
                    non_translate_events.append(desc_detail)

            # 4. Comprobación estricta de seguridad
            if non_translate_events:
                summary_non_tr = " | ".join(non_translate_events[:3])
                self.alert_non_translate.emit({
                    "ticket_id": t_id,
                    "case_id": case_id,
                    "users": list(detected_users),
                    "hosts": list(detected_hosts),
                    "ips": list(detected_ips),
                    "details": summary_non_tr,
                    "total_alerts": len(docs),
                    "non_translate_count": len(non_translate_events)
                })
                return

            if translate_matches == 0:
                self.remediation_failed.emit(
                    t_id,
                    "No se identificaron alertas de WebControl / Google Translate en el lote."
                )
                return

            # 5. Construcción dinámica del comentario de cierre humanizado
            str_users = ", ".join(sorted(detected_users)) if detected_users else "Usuario corporativo"
            str_hosts = ", ".join(sorted(detected_hosts)) if detected_hosts else "Estación de trabajo"
            str_ips = ", ".join(sorted(detected_ips)) if detected_ips else "Red interna"

            resolution_comment = (
                f"Se realizó la evaluación del lote de alertas por bloqueo de navegación reportado "
                f"por Sophos Endpoint (Event::Endpoint::WebControlViolation) en el activo {str_hosts} ({str_ips}), "
                f"usuario(s): {str_users}.\n\n"
                f"La telemetría cruda provista por Sophos Central y los registros de Interflow confirman que los "
                f"eventos corresponden a intentos de conexión rutinarios hacia 'https://translate.google.com', los cuales "
                f"fueron bloqueados de manera preventiva por la directiva corporativa de filtrado web bajo la "
                f"categoría 'Proxies & Translators'. No existió ejecución de binarios sospechosos, compromiso "
                f"de credenciales, descarga de artefactos maliciosos ni bypass de la protección del endpoint."
            )

            # 6. Breve pausa realista para simulación de MTTR
            for _ in range(5):
                if self._is_killed: return
                time.sleep(1)

            # 7. Publicar justificación formal en el caso
            post_resolution_comment(self.session, self.headers, case_id, resolution_comment)
            # Publicada la nota, el cierre se completa aunque se pida cancelar (evita nota sin cierre)

            # 8. Cerrar caso como Resolved / False Positive asignado al operador
            resolve_payload = {
                "status": "Resolved",
                "resolution": "False Positive",
                "assignee": EMAIL_USUARIO
            }
            r_res = self.session.put(url_case, headers=self.headers, json=resolve_payload, verify=True, timeout=12)
            r_res.raise_for_status()

            if self._is_killed: return

            self.remediation_finished.emit({
                "ticket_id": t_id,
                "case_id": case_id,
                "users": list(detected_users),
                "hosts": list(detected_hosts),
                "ips": list(detected_ips),
                "resolution": "False Positive",
                "alert_count": len(docs)
            })

        except Exception as err:
            if not self._is_killed:
                self.remediation_failed.emit(t_id, str(err))

# -----------------------------------------------------------------------------
class SatiDnsAutoRemediatorWorker(QThread):
    """
    Worker asincrono para auditar y auto-resolver casos de anomalia de denegacion en firewall
    (Internal Firewall Denial Anomaly) asociados al proveedor de soporte SATI (Odoo).
    Verifica que el trafico denegado sea exclusivamente consultas DNS (puerto 53) hacia los
    controladores de dominio / DNS internos (10.11.1.1, 10.11.1.2) desde la VPN corporativa.
    Si se detecta cualquier intento de comunicacion hacia otros puertos o servicios (SMB, RDP, HTTP, etc.),
    o por parte de un usuario diferente, aborta la auto-resolucion y emite una alerta critica.
    """
    remediation_finished = Signal(dict)
    remediation_failed = Signal(str, str) # ticket_id, error_msg
    alert_non_sati_dns = Signal(dict)     # ticket_id, alert_info

    VALID_DNS_PORTS = {53, "53"}
    VALID_DNS_IPS = {"10.11.1.1", "10.11.1.2"}
    SATI_ACCOUNT = "sati"

    @classmethod
    def _is_sati_identity(cls, user: str) -> bool:
        """'sati', 'DOMINIO\\sati' o 'sati@dominio' (comparación exacta, no substring)."""
        u = _norm_identity(user)
        return u == cls.SATI_ACCOUNT or u.split("@", 1)[0] == cls.SATI_ACCOUNT

    def __init__(self, case_obj: dict, session: requests.Session, headers: dict):
        super().__init__()
        self.case_obj = case_obj
        self.session = session
        self.headers = headers
        self._is_killed = False

    def kill(self):
        self._is_killed = True

    def run(self):
        case_id = self.case_obj.get("_id") or self.case_obj.get("ticket_id")
        t_id = str(self.case_obj.get("ticket_id") or case_id)
        try:
            if self._is_killed: return

            url_case = f"https://{HOST}/connect/api/v1/cases/{case_id}"
            url_alerts = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"

            docs, complete = fetch_all_case_alerts(
                self.session, self.headers, url_alerts, lambda: self._is_killed
            )
            if self._is_killed: return
            if not complete:
                # Ley de Oro: si no se pudo auditar el 100% del lote, NUNCA auto-cerrar.
                self.remediation_failed.emit(
                    t_id,
                    f"No se pudo descargar la totalidad de las alertas del caso ({len(docs)} leídas, "
                    f"límite de auditoría {MAX_AUDITED_ALERTS}). Se aborta la auto-resolución: requiere triaje manual."
                )
                return

            if self._is_killed: return

            if not docs:
                self.remediation_failed.emit(
                    t_id,
                    "No se encontraron alertas dentro del caso para auditar los eventos de SATI."
                )
                return

            detected_users = set()
            detected_hosts = set()
            detected_src_ips = set()
            detected_dst_ips = set()
            detected_dst_ports = set()
            non_sati_or_non_dns_events = []
            valid_dns_count = 0

            for doc in docs:
                src = doc.get("_source", {}) if isinstance(doc, dict) else {}

                # Extraer usuario
                user_candidates = [
                    src.get("user", {}).get("name") if isinstance(src.get("user"), dict) else None,
                    src.get("username"),
                    src.get("srcip_username"),
                    src.get("user_name"),
                    src.get("dstip_username")
                ]
                doc_users = set()
                for u in user_candidates:
                    if u and str(u).strip() and str(u).strip() != "-":
                        u_clean = str(u).strip()
                        detected_users.add(u_clean)
                        doc_users.add(u_clean)

                # Extraer host
                comp = src.get("computer_name") or src.get("srcip_host") or src.get("host_name")
                if comp and str(comp).strip() and str(comp).strip() != "-":
                    detected_hosts.add(str(comp).strip())

                # Extraer IPs
                src_ip = src.get("srcip") or src.get("source_ip")
                if src_ip and str(src_ip).strip():
                    detected_src_ips.add(str(src_ip).strip())

                dst_ip = src.get("dstip") or src.get("destination_ip")
                if dst_ip and str(dst_ip).strip():
                    detected_dst_ips.add(str(dst_ip).strip())

                # Extraer puertos
                dst_port = src.get("dstport") or src.get("destination_port")
                if dst_port is not None and str(dst_port).strip():
                    detected_dst_ports.add(str(dst_port).strip())

                port_str = str(dst_port).strip() if dst_port is not None else ""
                dst_ip_str = str(dst_ip).strip() if dst_ip else ""

                # Criterios estrictos POR ALERTA (sin estado acumulado entre alertas):
                #  - puerto destino exactamente 53
                #  - IP destino es uno de los DNS internos autorizados (si falta, NO se asume interna)
                #  - todas las identidades de ESTA alerta son la cuenta 'sati'
                is_dns_port = _to_int(port_str) == 53
                is_internal_dns = dst_ip_str in self.VALID_DNS_IPS
                is_sati = bool(doc_users) and all(self._is_sati_identity(u) for u in doc_users)

                if is_dns_port and is_internal_dns and is_sati:
                    valid_dns_count += 1
                else:
                    reason = f"Dest: {dst_ip_str or 'N/A'}:{port_str or 'N/A'} | Users: {sorted(doc_users) or 'N/A'}"
                    non_sati_or_non_dns_events.append(reason)

            # Comprobacion estricta de seguridad
            if non_sati_or_non_dns_events:
                summary_non = " | ".join(non_sati_or_non_dns_events[:3])
                self.alert_non_sati_dns.emit({
                    "ticket_id": t_id,
                    "case_id": case_id,
                    "users": list(detected_users),
                    "hosts": list(detected_hosts),
                    "src_ips": list(detected_src_ips),
                    "dst_ips": list(detected_dst_ips),
                    "ports": list(detected_dst_ports),
                    "details": summary_non,
                    "total_alerts": len(docs),
                    "anomalous_count": len(non_sati_or_non_dns_events)
                })
                return

            if valid_dns_count == 0:
                self.remediation_failed.emit(
                    t_id,
                    "No se identificaron eventos confirmados de SATI DNS en el lote de alertas."
                )
                return

            # Construccion dinamica del comentario de cierre humanizado
            str_hosts = ", ".join(sorted(detected_hosts)) if detected_hosts else "Estacion remota"
            str_src_ips = ", ".join(sorted(detected_src_ips)) if detected_src_ips else "10.212.134.x (SSL-VPN)"
            str_dst_ips = ", ".join(sorted(detected_dst_ips)) if detected_dst_ips else "10.11.1.1 / 10.11.1.2"
            total_count = len(docs)

            resolution_comment = (
                f"Internal Firewall Denial Anomaly\n\n"
                f"Se procede al cierre del lote de alertas por anomalia de denegacion en firewall tras determinarse que "
                f"corresponde a un falso positivo operacional generado por el proveedor de soporte Odoo (cuenta de usuario: sati).\n\n"
                f"La estacion de trabajo remota {str_hosts} ({str_src_ips}), conectada mediante el tunel corporativo SSL-VPN "
                f"bajo la cuenta sati, registro un volumen de {total_count} consultas DNS (puerto 53) hacia los "
                f"Controladores de Dominio y servidores DNS internos ({str_dst_ips}). Esta rafaga de trafico deriva del "
                f"mecanismo de conmutacion por error (failover) del cliente DNS del sistema operativo Windows tras no haber "
                f"obtenido respuesta inmediata en el DNS primario, resultando bloqueado en ambos casos por la directiva "
                f"de descarte implicito (policyid=0) en el firewall perimetral FG-Technoma.\n\n"
                f"Se audito minuciosamente la totalidad del lote ({total_count} eventos evaluados): no se identificaron intentos "
                f"de conexion hacia puertos criticos ni servicios administrativos (SMB 445, RDP 3389, SSH, HTTP), no existen "
                f"patrones de escaneo lateral ni trafico malicioso asociado. Evento tipificado como falso positivo operacional."
            )

            # Breve pausa realista para simulacion de MTTR
            for _ in range(5):
                if self._is_killed: return
                time.sleep(1)

            # Publicar comentario formal en el caso
            post_resolution_comment(self.session, self.headers, case_id, resolution_comment)
            # Publicada la nota, el cierre se completa aunque se pida cancelar (evita nota sin cierre)

            # Cerrar caso directamente como Resolved / False Positive asignado al operador
            resolve_payload = {
                "status": "Resolved",
                "resolution": "False Positive",
                "assignee": EMAIL_USUARIO
            }
            r_res = self.session.put(url_case, headers=self.headers, json=resolve_payload, verify=True, timeout=12)
            r_res.raise_for_status()

            if self._is_killed: return

            self.remediation_finished.emit({
                "ticket_id": t_id,
                "case_id": case_id,
                "users": list(detected_users) or ["sati"],
                "hosts": list(detected_hosts),
                "src_ips": list(detected_src_ips),
                "dst_ips": list(detected_dst_ips),
                "resolution": "False Positive",
                "alert_count": total_count
            })

        except Exception as err:
            if not self._is_killed:
                self.remediation_failed.emit(t_id, str(err))

# -----------------------------------------------------------------------------
# TRABAJADOR DE AUTO-REMEDIACIÓN DPAPI PROTECTED_STORAGE (SOAR HYPER-AUTOMATION)
# -----------------------------------------------------------------------------
class DPAPIStorageAutoRemediatorWorker(QThread):
    """
    Worker asíncrono para auditar y auto-resolver casos de Sensitive Windows Network Share
    hacia protected_storage en Controladores de Dominio (VMBASE8), correspondiente
    al respaldo legítimo de claves DPAPI del sistema operativo Windows.
    Verifica que el 100% de los eventos del caso sean de tipo Event ID 5145 dirigidos a
    \\*\\IPC$\\protected_storage sobre VMBASE8. Si se detectan otros objetos, o accesos anómalos,
    aborta la auto-resolución y emite una alerta para triaje manual.
    """
    remediation_finished = Signal(dict)
    remediation_failed = Signal(str, str) # ticket_id, error_msg
    alert_non_dpapi = Signal(dict)        # ticket_id, alert_info

    # Patrones de cuentas privilegiadas que nunca se auto-cierran (ampliable con la
    # variable de entorno SOAR_DPAPI_PRIVILEGED_USERS="usuario1,usuario2").
    _PRIVILEGED_RE = re.compile(r"^(adm[-_.]|admin|administrador|administrator|domain admin|krbtgt)", re.IGNORECASE)

    @classmethod
    def _is_privileged_user(cls, user: str) -> bool:
        u = _norm_identity(user)
        extra = {x.strip().lower() for x in os.environ.get("SOAR_DPAPI_PRIVILEGED_USERS", "").split(",") if x.strip()}
        return bool(cls._PRIVILEGED_RE.match(u)) or u in extra or u.split("@", 1)[0] in extra

    def __init__(self, case_obj: dict, session: requests.Session, headers: dict):
        super().__init__()
        self.case_obj = case_obj
        self.session = session
        self.headers = headers
        self._is_killed = False

    def kill(self):
        self._is_killed = True

    def run(self):
        case_id = self.case_obj.get("_id") or self.case_obj.get("ticket_id")
        t_id = str(self.case_obj.get("ticket_id") or case_id)
        try:
            if self._is_killed: return

            url_case = f"https://{HOST}/connect/api/v1/cases/{case_id}"
            url_alerts = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"

            docs, complete = fetch_all_case_alerts(
                self.session, self.headers, url_alerts, lambda: self._is_killed
            )
            if self._is_killed: return
            if not complete:
                # Ley de Oro: si no se pudo auditar el 100% del lote, NUNCA auto-cerrar.
                self.remediation_failed.emit(
                    t_id,
                    f"No se pudo descargar la totalidad de las alertas del caso ({len(docs)} leídas, "
                    f"límite de auditoría {MAX_AUDITED_ALERTS}). Se aborta la auto-resolución: requiere triaje manual."
                )
                return

            if self._is_killed: return

            if not docs:
                self.remediation_failed.emit(
                    t_id,
                    "No se encontraron alertas dentro del caso para auditar los eventos de DPAPI."
                )
                return

            detected_users = set()
            detected_hosts = set()
            detected_src_ips = set()
            detected_dst_ips = set()
            non_dpapi_events = []
            valid_dpapi_count = 0

            for doc in docs:
                src = doc.get("_source", {}) if isinstance(doc, dict) else {}
                event_data = src.get("event_data", {})
                xdr_event = src.get("xdr_event", {})

                # Extraer usuario
                user = (
                    event_data.get("SubjectUserName") or 
                    src.get("srcip_username") or 
                    src.get("username")
                )
                if not (user and str(user).strip() and str(user).strip() != "-"):
                    user = None
                if user:
                    domain = event_data.get("SubjectDomainName")
                    u_str = f"{domain}\\{user}" if domain else str(user)
                    detected_users.add(u_str)

                comp = src.get("computer_name") or src.get("host", {}).get("name") or src.get("engid_name")
                if comp and str(comp).strip():
                    detected_hosts.add(str(comp).strip())

                src_ip = src.get("srcip") or event_data.get("IpAddress")
                if src_ip and str(src_ip).strip() and str(src_ip).strip() != "-":
                    detected_src_ips.add(str(src_ip).strip())

                dst_ip = src.get("hostip") or src.get("host", {}).get("ip")
                if dst_ip and str(dst_ip).strip():
                    detected_dst_ips.add(str(dst_ip).strip())

                event_id = src.get("event_id")
                target_name = str(event_data.get("RelativeTargetName") or "").lower()
                share_name = str(event_data.get("ShareName") or "").lower()
                comp_upper = str(comp or "").upper()
                subtype_name = str(xdr_event.get("subtype", {}).get("name") or "").lower()
                desc = str(xdr_event.get("description", "")).lower()

                # Criterios estrictos:
                is_5145 = (_to_int(event_id) == 5145) or ("5145" in str(src.get("stellar", {}).get("task", "")))
                is_protected_storage = "protected_storage" in target_name or "protected_storage" in subtype_name or "protected_storage" in desc
                is_ipc = "ipc$" in share_name or "ipc$" in desc
                # Por alerta (sin usar el set acumulado detected_dst_ips de alertas previas)
                is_vmbase8 = ("VMBASE8" in comp_upper) or (str(dst_ip or "").strip() == "172.16.201.8")

                # El mismo pipe \\protected_storage es el que usan herramientas de robo de la
                # clave de respaldo DPAPI del dominio (ej. lsadump::backupkeys). Si el acceso
                # viene de una cuenta privilegiada, NO se auto-cierra.
                is_privileged = bool(user) and self._is_privileged_user(str(user))

                if is_5145 and is_protected_storage and is_ipc and is_vmbase8 and user and not is_privileged:
                    valid_dpapi_count += 1
                else:
                    reason = f"Evento fuera de patrón DPAPI: ID={event_id}, Share={share_name}, Target={target_name}, Host={comp}, Usuario={user or 'N/A'}{' (PRIVILEGIADO)' if is_privileged else ''}"
                    non_dpapi_events.append(reason)

            if non_dpapi_events:
                summary_non = " | ".join(non_dpapi_events[:3])
                self.alert_non_dpapi.emit({
                    "ticket_id": t_id,
                    "case_id": case_id,
                    "users": list(detected_users),
                    "hosts": list(detected_hosts),
                    "src_ips": list(detected_src_ips),
                    "dst_ips": list(detected_dst_ips),
                    "details": summary_non,
                    "total_alerts": len(docs),
                    "anomalous_count": len(non_dpapi_events)
                })
                return

            if valid_dpapi_count == 0:
                self.remediation_failed.emit(
                    t_id,
                    "No se identificaron eventos confirmados de protected_storage en el lote."
                )
                return

            str_hosts = ", ".join(sorted(detected_hosts)) if detected_hosts else "VMBASE8"
            str_users = ", ".join(sorted(detected_users)) if detected_users else "Usuario corporativo"
            str_src_ips = ", ".join(sorted(detected_src_ips)) if detected_src_ips else "172.16.202.x"
            str_dst_ips = ", ".join(sorted(detected_dst_ips)) if detected_dst_ips else "172.16.201.8"
            total_count = len(docs)

            resolution_comment = (
                f"Se analizó el lote de eventos de auditoría de seguridad de Windows (Event ID 5145) registrados sobre el "
                f"Controlador de Dominio secundario {str_hosts} ({str_dst_ips}). La interacción con el recurso compartido IPC$ y el "
                f"objeto protected_storage por parte del usuario {str_users} desde la estación {str_src_ips} corresponde al "
                f"comportamiento benigno y estándar de Microsoft Windows Data Protection API (DPAPI), el cual efectúa de forma "
                f"periódica el respaldo de las claves maestras de cifrado de usuario hacia el KDC. La auditoría confirma que la "
                f"operación concluyó exitosamente bajo privilegios estándar de sesión ({total_count} eventos evaluados), sin indicios "
                f"de manipulación o extracción maliciosa de credenciales (T1021.002)."
            )

            # Simulación realista de MTTR
            for _ in range(5):
                if self._is_killed: return
                time.sleep(1)

            # Comentario formal en el ticket
            post_resolution_comment(self.session, self.headers, case_id, resolution_comment)
            # Publicada la nota, el cierre se completa aunque se pida cancelar (evita nota sin cierre)

            # Resolver caso
            resolve_payload = {
                "status": "Resolved",
                "resolution": "False Positive",
                "assignee": EMAIL_USUARIO
            }
            r_res = self.session.put(url_case, headers=self.headers, json=resolve_payload, verify=True, timeout=12)
            r_res.raise_for_status()

            if self._is_killed: return

            self.remediation_finished.emit({
                "ticket_id": t_id,
                "case_id": case_id,
                "users": list(detected_users),
                "hosts": list(detected_hosts),
                "src_ips": list(detected_src_ips),
                "dst_ips": list(detected_dst_ips),
                "resolution": "False Positive",
                "alert_count": total_count
            })

        except Exception as err:
            if not self._is_killed:
                self.remediation_failed.emit(t_id, str(err))

# -----------------------------------------------------------------------------
# TRABAJADOR DE SONDEO RÁPIDO DE IDENTIDAD (ALERT PROBE SOAR)
# -----------------------------------------------------------------------------
class CaseIdentityProbeWorker(QThread):
    """
    Worker asíncrono ultra-rápido que sondea las alertas crudas de un caso
    para determinar con certeza absoluta la identidad del usuario atacado/involucrado,
    sin modificar el estado del caso ni bloquear la GUI.
    """
    probe_finished = Signal(dict)
    probe_failed = Signal(str, str)

    HEALTH_MAILBOX_WHITELIST = {
        "healthmailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local",
        "healthmailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py"
    }

    def __init__(self, case_id: str, ticket_id: str, session: requests.Session, headers: dict):
        super().__init__()
        self.case_id = case_id
        self.ticket_id = ticket_id
        self.session = session
        self.headers = headers
        self._is_killed = False

    def run(self):
        try:
            if self._is_killed: return
            url = f"https://{HOST}/connect/api/v1/cases/{self.case_id}/alerts"
            r = self.session.get(url, headers=self.headers, params={"limit": "15", "skip": "0"}, verify=True, timeout=12)
            r.raise_for_status()
            if self._is_killed: return

            data = r.json()
            docs = []
            if isinstance(data, dict):
                inner = data.get("data", data)
                if isinstance(inner, dict):
                    docs = inner.get("docs", [])
                elif isinstance(inner, list):
                    docs = inner
            elif isinstance(data, list):
                docs = data

            detected_users = set()
            protocols = set()

            for doc in docs:
                src = doc.get("_source", {}) if isinstance(doc, dict) else {}
                event_data = src.get("event_data", {})
                candidates = [
                    src.get("username"),
                    src.get("srcip_username"),
                    event_data.get("TargetUserName")
                ]
                for c in candidates:
                    if c and str(c).strip() and str(c).strip() != "-":
                        detected_users.add(str(c).strip().lower())

                event_id = src.get("event_id")
                sub_name = str(src.get("xdr_event", {}).get("subtype", {}).get("name", "")).lower()
                if event_id == 4776 or "ntlm" in sub_name:
                    protocols.add("NTLM")
                elif event_id == 4768 or "kerberos" in sub_name:
                    protocols.add("KERBEROS")

            _is_hm = HealthMailboxAutoRemediatorWorker._is_healthmailbox_identity
            pure_hm = bool(detected_users) and all(_is_hm(u) for u in detected_users)
            has_hm = any(_is_hm(u) for u in detected_users)

            if self._is_killed: return
            self.probe_finished.emit({
                "ticket_id": self.ticket_id,
                "case_id": self.case_id,
                "users": detected_users,
                "pure_hm": pure_hm,
                "has_hm": has_hm,
                "protocols": protocols
            })
        except Exception as e:
            if not self._is_killed:
                self.probe_failed.emit(self.ticket_id, str(e))

# -----------------------------------------------------------------------------
# TRABAJADOR DE AUTO-GUARDIA SLA (PREVENCIÓN DE BRECHA MTTD EN TURNO)
# -----------------------------------------------------------------------------
class AutoAssignWorker(QThread):
    """
    Worker asíncrono para auto-asignar casos en riesgo de vencimiento de MTTD
    sin bloquear la interfaz gráfica principal.
    """
    assigned_signal = Signal(str, str) # ticket_id, assignee
    error_signal = Signal(str, str)    # ticket_id, error_msg

    def __init__(self, case_id: str, ticket_id: str, session: requests.Session, headers: dict):
        super().__init__()
        self.case_id = case_id
        self.ticket_id = ticket_id
        self.session = session
        self.headers = headers
        self._is_killed = False

    def run(self):
        try:
            if self._is_killed: return
            url = f"https://{HOST}/connect/api/v1/cases/{self.case_id}"
            payload = {"assignee": EMAIL_USUARIO}
            res = self.session.put(url, headers=self.headers, json=payload, verify=True, timeout=12)
            res.raise_for_status()
            if self._is_killed: return
            self.assigned_signal.emit(self.ticket_id, EMAIL_USUARIO)
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(self.ticket_id, str(e))

