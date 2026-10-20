# -*- coding: utf-8 -*-
"""
19 Workers Asincrónicos Multihilo (QThread y QRunnable) para Stellar Cyber,
IA (Gemini/Claude), CTI, CVE NIST Batch y Security Onion.
"""
from soar_app.core.infra import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime as _dt

class BaseApiWorker(QThread):
    finished_signal = Signal(dict)
    error_signal = Signal(str)

    def __init__(self, payload: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> None:
        super().__init__()
        self.payload = payload
        self.params = params
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        """Resetea _is_killed antes de cada ciclo de vida para workers persistentes."""
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            
            manager = RestSessionManager()
            headers = manager.get_headers()
            
            if self._is_killed: return
            try:
                self._do_work(manager.session, headers)
            except requests.exceptions.HTTPError as http_err:
                # Si Stellar Cyber devuelve 401 Unauthorized, forzamos re-autenticación y reintentamos 1 vez
                if http_err.response is not None and http_err.response.status_code == 401:
                    log_to_file(f"[AUTH AUTO-RETRY] 401 detectado en {self.__class__.__name__}. Renovando token y reintentando...")
                    headers = manager.get_headers(force_refresh=True)
                    if self._is_killed: return
                    self._do_work(manager.session, headers)
                else:
                    raise
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(str(e))

    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        pass

class HealthWorker(BaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        res_sens = session.get(f"https://{HOST}/connect/api/v1/data_sensors", headers=headers, verify=True, timeout=20)
        res_sens.raise_for_status()
        if self._is_killed: return
        
        res_usage = session.get(f"https://{HOST}/connect/api/v1/storage-usages/daily_and_monthly", headers=headers, verify=True, timeout=20)
        res_usage.raise_for_status()
        if self._is_killed: return
        
        res_tenants = session.get(f"https://{HOST}/connect/api/v1/tenants", headers=headers, verify=True, timeout=20)
        res_tenants.raise_for_status()
        if self._is_killed: return
        
        self.finished_signal.emit({"sensors": res_sens.json(), "usage": res_usage.json(), "tenants": res_tenants.json(), "action": "health"})

class CasesWorker(BaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        # Límite optimizado a 50 (reduce 50% la carga en Elasticsearch de Stellar Cyber)
        # Timeout extendido a 25s para enlaces WAN internacionales y picos de ingesta
        res = session.get(f"https://{HOST}/connect/api/v1/cases?limit=50", headers=headers, verify=True, timeout=25)
        res.raise_for_status()
        if self._is_killed: return
        self.finished_signal.emit({"cases": res.json(), "action": "cases"})

class ExtendedCasesWorker(BaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        # Petición on-demand de historial extendido (200 casos) para cálculo analítico de métricas
        res = session.get(f"https://{HOST}/connect/api/v1/cases?limit=200", headers=headers, verify=True, timeout=35)
        res.raise_for_status()
        if self._is_killed: return
        self.finished_signal.emit({"cases": res.json(), "action": "extended_cases"})



class WorkerSignals(QObject):
    finished_signal = Signal(dict)
    error_signal = Signal(str)

class RunnableBaseApiWorker(QRunnable):
    def __init__(self, payload=None, params=None):
        super().__init__()
        self.payload = payload
        self.params = params
        self.signals = WorkerSignals()
        self._is_killed = False

    def run(self):
        try:
            if self._is_killed: return
            manager = RestSessionManager()
            headers = manager.get_headers()
            if self._is_killed: return
            try:
                self._do_work(manager.session, headers)
            except requests.exceptions.HTTPError as http_err:
                # Si Stellar Cyber devuelve 401 Unauthorized, forzamos re-autenticación y reintentamos 1 vez
                if http_err.response is not None and http_err.response.status_code == 401:
                    log_to_file(f"[AUTH AUTO-RETRY] 401 detectado en {self.__class__.__name__}. Renovando token y reintentando...")
                    headers = manager.get_headers(force_refresh=True)
                    if self._is_killed: return
                    self._do_work(manager.session, headers)
                else:
                    raise
        except Exception as e:
            if not self._is_killed:
                self.signals.error_signal.emit(str(e))

    def _do_work(self, session, headers):
        pass
class TriageWorker(RunnableBaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        case_id = self.params.get("case_id")
        res_details = session.get(f"https://{HOST}/connect/api/v1/cases/{case_id}", headers=headers, verify=True, timeout=12)
        res_details.raise_for_status()
        if self._is_killed: return
        
        res_obs = session.get(f"https://{HOST}/connect/api/v1/cases/{case_id}/observables", headers=headers, verify=True, timeout=12)
        res_obs.raise_for_status()
        if self._is_killed: return
        
        details_text = json.dumps(res_details.json(), indent=4, ensure_ascii=False)
        obs_text = json.dumps(res_obs.json(), indent=4, ensure_ascii=False)
        
        self.signals.finished_signal.emit({"details_text": details_text, "observables_text": obs_text, "action": "triage"})

class GetCommentsWorker(RunnableBaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        case_uuid = str(self.params.get("case_id", "")).strip()
        clean_uuid = case_uuid.lstrip("#").strip()
        
        # Si no tiene formato UUID (con guiones), buscamos el UUID real
        if "-" not in case_uuid:
            search_url = f"https://{HOST}/connect/api/v1/cases?search={clean_uuid}"
            s_res = session.get(search_url, headers=headers, verify=True, timeout=12)
            if s_res.status_code == 200:
                data = s_res.json()
                casos = []
                if "data" in data and isinstance(data["data"], dict) and "cases" in data["data"]:
                    casos = data["data"]["cases"]
                elif "data" in data and isinstance(data["data"], list):
                    casos = data["data"]
                    
                for c in casos:
                    c_tid = str(c.get("ticket_id", "")).strip().lstrip("#")
                    if c_tid == clean_uuid:
                        case_uuid = c.get("_id", case_uuid)
                        break

        url = f"https://{HOST}/connect/api/v1/cases/{case_uuid}/comments"
        res = session.get(url, headers=headers, verify=True, timeout=10)
        res.raise_for_status()
        if self._is_killed: return
        self.signals.finished_signal.emit({"comments": res.json(), "action": "get_comments"})

class UpdateCaseWorker(BaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        case_id = self.params.get("case_id")
        justificacion = self.params.get("comment")
        if justificacion:
            comment_url = f"https://{HOST}/connect/api/v1/cases/{case_id}/comments"
            c_res = session.post(comment_url, headers=headers, json={"comment": justificacion}, verify=True, timeout=10)
            c_res.raise_for_status()
        if self._is_killed: return
        
        url = f"https://{HOST}/connect/api/v1/cases/{case_id}"
        res = session.put(url, headers=headers, json=self.payload, verify=True, timeout=12)
        res.raise_for_status()
        if self._is_killed: return
        self.finished_signal.emit({"status": res.status_code, "action": "update"})

class InterflowWorker(BaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        case_id = self.params.get("case_id")
        url = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"
        res = session.get(url, headers=headers, params=self.payload, verify=True, timeout=15)
        res.raise_for_status()
        if self._is_killed: return
        
        alerts_text = json.dumps(res.json(), indent=4, ensure_ascii=False)
        self.finished_signal.emit({"alerts_text": alerts_text, "action": "interflow"})


# -----------------------------------------------------------------------------
# ENTITY PROFILE WORKER — Búsqueda de entidad para Perfilamiento UEBA
# -----------------------------------------------------------------------------
class EntityProfileWorker(RunnableBaseApiWorker):
    def _do_work(self, session: requests.Session, headers: Dict[str, str]) -> None:
        base_url = f"https://{HOST}/connect/api/v1/cases"
        entity = self.params.get("entity", "")
        
        if not entity:
            self.signals.finished_signal.emit({
                "results_text": "Error: Entidad no provista.",
                "action": "entity_profile"
            })
            return

        # Fetch cases related to the entity
        res = session.get(base_url, headers=headers, params={"search": entity, "limit": "50"}, verify=True, timeout=20)
        res.raise_for_status()
        if self._is_killed: return

        data = res.json() or {}
        cases = (data.get("data") or {}).get("cases", [])
        
        if not cases:
            self.signals.finished_signal.emit({
                "results_text": f"No se encontró telemetría ni alertas para la entidad: {entity}",
                "action": "entity_profile",
                "entity": entity,
                "found": False
            })
            return
            
        # Collect raw alerts related to cases to pass to Gemini
        from concurrent.futures import ThreadPoolExecutor, as_completed
        all_alerts = []
        case_ids = [c.get("_id") for c in cases if c.get("_id")][:15] # Limitar a 15 casos max
        
        def fetch_alerts(case_id):
            if self._is_killed: return []
            try:
                alerts_url = f"https://{HOST}/connect/api/v1/cases/{case_id}/alerts"
                alerts_res = session.get(alerts_url, headers=headers, params={"limit": 20}, verify=True, timeout=10)
                if alerts_res.status_code == 200:
                    raw_data = (alerts_res.json() or {}).get("data", [])
                    return raw_data.get("docs", []) if isinstance(raw_data, dict) else (raw_data or [])
            except Exception:
                pass
            return []

        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_case = {executor.submit(fetch_alerts, cid): cid for cid in case_ids}
            for future in as_completed(future_to_case):
                if self._is_killed: break
                alerts = future.result()
                all_alerts.extend(alerts)

        # Build payload for Gemini
        entity_payload = {
            "entity_searched": entity,
            "total_cases_found": len(cases),
            "alerts_sampled": all_alerts
        }

        self.signals.finished_signal.emit({
            "results_text": json.dumps(entity_payload, indent=4, ensure_ascii=False),
            "action": "entity_profile",
            "entity": entity,
            "found": True
        })

# -----------------------------------------------------------------------------
# AUTO-TRIAGE STELLAR WORKER — IA Nativa (/autotriage/v1/case/{id}/summary)
# -----------------------------------------------------------------------------
class AutoTriageStellarWorker(RunnableBaseApiWorker):
    """Obtiene el resumen de IA generado por el propio motor de Stellar Cyber."""
    def _do_work(self, session, headers):
        case_id = self.params.get("case_id")
        url = f"https://{HOST}/connect/api/v1/autotriage/v1/case/{case_id}/summary"
        res = session.get(url, headers=headers, verify=True, timeout=20)
        res.raise_for_status()
        if self._is_killed: return
        data = res.json()
        
        # Intentamos extraer solo el texto del resumen, evitando el JSON crudo y los prompts del sistema
        summary_text = ""
        
        # 1. Si el API devuelve el texto directamente en alguna llave conocida
        if isinstance(data, dict):
            # Intentar extraer formato nativo v2 de Stellar Cyber (ai_case_triage)
            ai_triage = data.get("ai_case_triage", {})
            if "summary" in ai_triage and isinstance(ai_triage["summary"], dict):
                s_data = ai_triage["summary"]
                parts = []
                if "concise_summary" in s_data: parts.append(s_data["concise_summary"])
                if "hypothesis" in s_data: parts.append(s_data["hypothesis"])
                if "key_entities_and_relations" in s_data: parts.append(s_data["key_entities_and_relations"])
                if "recommendations" in s_data: parts.append(s_data["recommendations"])
                if parts:
                    summary_text = "\n\n".join(parts)
            
            # Buscar en keys comunes si no se encontró el formato ai_case_triage
            if not summary_text:
                if "summary" in data:
                    summary_text = data["summary"]
                elif "data" in data and isinstance(data["data"], dict) and "summary" in data["data"]:
                    summary_text = data["data"]["summary"]
                elif "data" in data and isinstance(data["data"], str):
                    summary_text = data["data"]
            else:
                # Fallback: Extraer valores string ignorando listas u otros dicts
                strings = [str(v) for k, v in data.items() if isinstance(v, str) and len(str(v)) > 50]
                if strings:
                    summary_text = "\n".join(strings)
                else:
                    state = data.get("triage_state", "UNKNOWN")
                    if state in ["ELIGIBLE", "PENDING"]:
                        summary_text = f"El resumen de IA Nativa de Stellar Cyber aún no ha sido generado o está en proceso (Estado: {state})."
                    else:
                        summary_text = f"No se encontró un resumen de texto. Estado actual: {state}\n\nDatos crudos:\n{json.dumps(data, indent=4, ensure_ascii=False)}"
        else:
            summary_text = str(data)
            

        self.signals.finished_signal.emit({"summary_text": summary_text, "action": "stellar_autotriage"})

# -----------------------------------------------------------------------------
# ASSIGNEES WORKER — Carga dinámica de analistas (/cases/assignees)
# -----------------------------------------------------------------------------
class AssigneesWorker(RunnableBaseApiWorker):
    """Se ejecuta una vez al arrancar para poblar el combo de analistas."""
    def _do_work(self, session, headers):
        url = f"https://{HOST}/connect/api/v1/cases/assignees"
        res = session.get(url, headers=headers, verify=True, timeout=10)
        res.raise_for_status()
        if self._is_killed: return
        self.signals.finished_signal.emit({"assignees_raw": res.json(), "action": "assignees_loaded"})

# -----------------------------------------------------------------------------
# OPERADOR DE COGNICIÓN INTELIGENTE DIRECTO (GOOGLE GEMINI COGNITIVE WORKER)
# -----------------------------------------------------------------------------
class AiAnalysisWorker(QThread):
    """Hilo asincrónico aislado conectado en streaming SSE al núcleo de Gemini 3.8 + RAG."""
    analysis_finished = Signal(str)
    analysis_failed = Signal(str)
    analysis_chunk = Signal(str)
    analysis_status = Signal(str)

    def __init__(self, context_json_text: str) -> None:
        super().__init__()
        self.context_json_text = context_json_text
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        """Resetea _is_killed antes de cada invocación."""
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            orchestrator = StellarGeminiOrchestrator(api_key=AI_API_KEY)

            def _on_chunk(chunk_text: str) -> None:
                if not self._is_killed and chunk_text:
                    self.analysis_chunk.emit(chunk_text)

            def _on_status(status_text: str) -> None:
                if not self._is_killed and status_text:
                    self.analysis_status.emit(status_text)

            reporte_final = orchestrator.enviar_a_gemini_stream(
                self.context_json_text,
                on_chunk=_on_chunk,
                on_status=_on_status,
            )

            if self._is_killed: return
            if reporte_final:
                self.analysis_finished.emit(reporte_final)
            else:
                self.analysis_failed.emit("Google devolvió una estructura vacía.")
        except Exception as e:
            if not self._is_killed:
                self.analysis_failed.emit(str(e))

# -----------------------------------------------------------------------------
# TRABAJADOR CTI ASINCRÓNICO (THREAT INTELLIGENCE WORKER)
# -----------------------------------------------------------------------------
class CtiQueryWorker(QThread):
    """Hilo asincrónico para consultas CTI (VirusTotal, AbuseIPDB, URLScan, Tri-Scan) sin congelar la UI."""
    query_finished = Signal(dict)
    query_failed = Signal(str)

    def __init__(self, mode: str, observable: str) -> None:
        super().__init__()
        self.mode = mode.lower().strip() # 'triscan', 'virustotal', 'abuseipdb', 'urlscan'
        self.observable = observable.strip()
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            res = {}
            if self.mode in ("triscan", "cti", "tri"):
                res = CtiEngine.tri_scan(self.observable)
                res["mode"] = "triscan"
            elif self.mode in ("virustotal", "vt"):
                r = CtiEngine.query_virustotal(self.observable)
                res = {
                    "mode": "virustotal",
                    "observable": self.observable,
                    "type": CtiEngine.detect_observable_type(self.observable),
                    "virustotal": r
                }
            elif self.mode in ("abuseipdb", "abuse"):
                r = CtiEngine.query_abuseipdb(self.observable)
                res = {
                    "mode": "abuseipdb",
                    "observable": self.observable,
                    "type": CtiEngine.detect_observable_type(self.observable),
                    "abuseipdb": r
                }
            elif self.mode in ("urlscan", "url"):
                r = CtiEngine.query_urlscan(self.observable)
                res = {
                    "mode": "urlscan",
                    "observable": self.observable,
                    "type": CtiEngine.detect_observable_type(self.observable),
                    "urlscan": r
                }
            elif self.mode in ("mxtoolbox", "phishing", "email"):
                r = CtiEngine.query_phishing_email_defense(self.observable)
                res = {
                    "mode": "mxtoolbox_phishing",
                    "observable": self.observable,
                    "type": "domain",
                    "mxtoolbox": r
                }
            elif self.mode in ("spf", "dmarc", "mx"):
                r = CtiEngine.query_mxtoolbox(self.observable, command=self.mode)
                res = {
                    "mode": "mxtoolbox_cmd",
                    "command": self.mode,
                    "observable": self.observable,
                    "type": "domain",
                    "mxtoolbox": r
                }
            elif self.mode in ("cve", "nvd"):
                r = CtiEngine.query_cve(self.observable)
                res = {
                    "mode": "cve",
                    "observable": self.observable,
                    "type": "cve",
                    "cve": r
                }
            else:
                res = CtiEngine.tri_scan(self.observable)
                res["mode"] = "triscan"

            if self._is_killed: return
            self.query_finished.emit(res)
        except Exception as e:
            if not self._is_killed:
                self.query_failed.emit(str(e))

# -----------------------------------------------------------------------------
# TRABAJADOR DE DESCARGA MASIVA DE CVEs ASINCRÓNICO (NVD NIST 2.0)
# -----------------------------------------------------------------------------
class CveBatchFetchWorker(QThread):
    """Hilo de fondo para recolectar y segmentar lotes de CVEs de NVD NIST 2.0 sin congelar el Cockpit."""
    progress_signal = Signal(int, str)
    finished_signal = Signal(list)
    error_signal = Signal(str)

    def __init__(self, start_date: datetime, end_date: datetime,
                 severities: List[str], nvd_api_key: str = "", slack_webhook: str = ""):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.severities = severities
        self.nvd_api_key = nvd_api_key or os.environ.get("NVD_API_KEY", "")
        self.slack_webhook = slack_webhook.strip()
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        self._is_killed = False
        super().start(priority)

    def chunk_dates(self, start: datetime, end: datetime, delta_days: int = 100):
        chunks = []
        curr = start
        while curr < end:
            next_date = curr + datetime.resolution * delta_days * 86400000000 if False else (curr + pd.Timedelta(days=delta_days).to_pytimedelta() if 'pd' in globals() else curr + (end - curr))
            import datetime as _dt
            next_date = curr + _dt.timedelta(days=delta_days)
            if next_date > end:
                next_date = end
            chunks.append((curr, next_date))
            curr = next_date + _dt.timedelta(seconds=1)
        return chunks

    def run(self) -> None:
        try:
            if self._is_killed: return
            vulnerabilidades = []
            headers = {
                "User-Agent": "StellarCyber-OpenXDR-Cockpit",
            }
            if self.nvd_api_key:
                headers["apiKey"] = self.nvd_api_key

            date_chunks = self.chunk_dates(self.start_date, self.end_date)
            total_steps = max(1, len(self.severities) * len(date_chunks))
            current_step = 0

            self.progress_signal.emit(0, f"[INICIO] Iniciando extracción de vulnerabilidades NVD NIST 2.0...")
            self.progress_signal.emit(2, f"[RANGO] {self.start_date.strftime('%d-%m-%Y')} al {self.end_date.strftime('%d-%m-%Y')} | Niveles: {', '.join(self.severities)}")

            for severidad in self.severities:
                if self._is_killed: return
                self.progress_signal.emit(int((current_step / total_steps) * 100), f"\n[NVD API] Consultando nivel de severidad CVSS: {severidad}")

                for start_chunk, end_chunk in date_chunks:
                    if self._is_killed: return
                    str_inicio = start_chunk.strftime("%Y-%m-%dT%H:%M:%S.000")
                    str_fin = end_chunk.strftime("%Y-%m-%dT%H:%M:%S.000")

                    url = (
                        f"https://services.nvd.nist.gov/rest/json/cves/2.0?"
                        f"pubStartDate={str_inicio}&pubEndDate={str_fin}&cvssV3Severity={severidad}"
                    )
                    self.progress_signal.emit(int((current_step / total_steps) * 100), f"  -> Ventana: {start_chunk.strftime('%d-%m-%Y')} a {end_chunk.strftime('%d-%m-%Y')}")

                    max_retries = 4
                    chunk_success = False
                    for attempt in range(max_retries):
                        if self._is_killed: return
                        try:
                            resp = requests.get(url, headers=headers, timeout=40)
                            if resp.status_code == 200:
                                data = resp.json()
                                nuevos = data.get("vulnerabilities", [])
                                vulnerabilidades.extend(nuevos)
                                self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [OK] {len(nuevos)} CVEs descargados en este bloque.")
                                chunk_success = True
                                break
                            elif resp.status_code == 429:
                                self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [RATE-LIMIT] Servidor NVD saturado (429). Esperando 6s...")
                                time.sleep(6)
                            elif resp.status_code in (401, 403):
                                self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [WARN] Código de autenticación NVD {resp.status_code}. Reintentando sin apiKey o con delay...")
                                time.sleep(4)
                            else:
                                self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [WARN] NVD respondió HTTP {resp.status_code}. Intento {attempt+1}/{max_retries}")
                                time.sleep(3)
                        except Exception as req_err:
                            self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [NET-ERR] Intento {attempt+1}/{max_retries}: {req_err}")
                            time.sleep(4)

                    if not chunk_success:
                        self.progress_signal.emit(int((current_step / total_steps) * 100), f"     [ALERTA] Bloque {start_chunk.strftime('%d-%m-%Y')} omitido tras reintentos.")

                    current_step += 1
                    pct = min(98, int((current_step / total_steps) * 100))
                    self.progress_signal.emit(pct, "")
                    time.sleep(2) # Respetar ritmo de la API de NVD

            # Notificación Slack opcional
            if self.slack_webhook and vulnerabilidades and not self._is_killed:
                try:
                    self.progress_signal.emit(99, "[SLACK] Enviando notificación de resumen al canal de ciberseguridad...")
                    payload = {
                        "text": (
                            f"🛡️ *OpenXDR SOAR — Reporte de Vulnerabilidades NVD*\n"
                            f"📅 *Período:* {self.start_date.strftime('%d-%m-%Y')} al {self.end_date.strftime('%d-%m-%Y')}\n"
                            f"⚡ *Niveles:* `{', '.join(self.severities)}`\n"
                            f"🔥 *Total CVEs Identificados:* `{len(vulnerabilidades)}`\n"
                            f"💻 _Descarga disponible en Cockpit Central Master._"
                        )
                    }
                    requests.post(self.slack_webhook, json=payload, timeout=8)
                    self.progress_signal.emit(99, "   [SLACK OK] Notificación enviada con éxito.")
                except Exception as s_err:
                    self.progress_signal.emit(99, f"   [SLACK ERR] No se pudo enviar notificación: {s_err}")

            if self._is_killed: return
            self.progress_signal.emit(100, f"\n[COMPLETADO] Proceso finalizado. Total registros CVE recuperados: {len(vulnerabilidades)}")
            self.finished_signal.emit(vulnerabilidades)
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(str(e))

# -----------------------------------------------------------------------------
# TRABAJADORES DE INTEGRACIÓN CON SECURITY ONION (GRID & THREAT HUNTING)
# -----------------------------------------------------------------------------
class SecurityOnionHealthWorker(QThread):
    """Verifica el estado del Grid de Security Onion de forma asíncrona sin bloquear la UI."""
    health_signal = Signal(dict)
    error_signal = Signal(str)

    def __init__(self, engine: Any) -> None:
        super().__init__()
        self.engine = engine
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            health = self.engine.get_grid_health()
            if not self._is_killed:
                self.health_signal.emit(health)
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(str(e))


class SecurityOnionHuntWorker(QThread):
    """Ejecuta búsquedas forenses de IOCs en Security Onion (Zeek, Suricata, Syslog)."""
    hunt_signal = Signal(dict)
    progress_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, engine: Any, ioc: str, days: int = 7) -> None:
        super().__init__()
        self.engine = engine
        self.ioc = ioc.strip()
        self.days = days
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            self.progress_signal.emit(f"Consultando Grid Security Onion para IOC: {self.ioc} (Ventana: {self.days} días)...")
            res = self.engine.hunt_ioc(self.ioc, days=self.days)
            if not self._is_killed:
                self.hunt_signal.emit(res)
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(str(e))


class SecurityOnionTelemetryWorker(QThread):
    """Recupera telemetría reciente de auditoría y syslog de nodos específicos (ej: secops-vascol)."""
    telemetry_signal = Signal(dict)
    progress_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, engine: Any, node_name: str = "secops-vascol", limit: int = 50) -> None:
        super().__init__()
        self.engine = engine
        self.node_name = node_name
        self.limit = limit
        self._is_killed = False

    def start(self, priority: int = QThread.InheritPriority) -> None:
        self._is_killed = False
        super().start(priority)

    def run(self) -> None:
        try:
            if self._is_killed: return
            self.progress_signal.emit(f"Recuperando registros de auditoría y syslog del nodo '{self.node_name}'...")
            res = self.engine.get_node_telemetry_summary(host_name=self.node_name, limit=self.limit)
            if not self._is_killed:
                self.telemetry_signal.emit(res)
        except Exception as e:
            if not self._is_killed:
                self.error_signal.emit(str(e))

# -----------------------------------------------------------------------------
