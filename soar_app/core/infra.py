#!/usr/bin/python3
# =============================================================================
#      STELLAR CYBER 6.5.1s - UNIFIED XDR COMMAND CENTER WITH STREAM AI (GUI)
#      SLA NOC - EDR-Safe, Asynchronous Multi-Threaded PySide6 & Gemma Stream
# =============================================================================

import sys
import os
import re
import hashlib
import requests
from requests.adapters import HTTPAdapter
import time
import threading
import base64
import base64
import json
from typing import Any, Dict, List, Union, Optional, Tuple
import time
import random
import math
import logging as _logging
import ctypes
# Constantes de control de directiva de energia de Windows (SetThreadExecutionState)
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002
import urllib3
from collections import OrderedDict
from html import escape as he
from datetime import datetime
from stellar_gemini_orchestrator import StellarGeminiOrchestrator, SecurityMaskingEngine, clean_forensic_data
import subprocess
from PySide6.QtCore import Qt, QThread, Signal, QTimer, Slot, QRunnable, QThreadPool, QObject, QDateTime, QDate, QProcess, QEvent, QUrl
from PySide6.QtGui import QTextCursor, QDesktopServices, QColor, QAction
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QTextEdit, 
                             QLineEdit, QPushButton, QComboBox, QFrame, 
                             QMessageBox, QCheckBox, QFileDialog, QTabWidget,
                             QDateEdit, QDateTimeEdit, QSplitter,
                             QTableWidget, QTableWidgetItem, QHeaderView, QProgressBar,
                             QScrollArea, QTextBrowser, QToolButton, QMenu)
import pandas as pd
from playbook_engine import PlaybookEngine
from cti_engine import CtiEngine
import ui_theme

def format_local_ts(ts_str: Any) -> str:
    """Convierte un timestamp UTC (ISO 8601 con 'Z' o offset) a hora local de Paraguay/SO (YYYY-MM-DD HH:MM:SS)."""
    if not ts_str or ts_str == "N/A":
        return str(ts_str or "")
    s = str(ts_str).strip()
    try:
        clean_s = s.replace("Z", "+00:00")
        dt = datetime.fromisoformat(clean_s)
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return s

from so_engine import SecurityOnionEngine
from email_header_analyzer import PhishingHeaderAnalyzerDialog
from thn_ticket_generator import TechnomaTicketGeneratorDialog, TechnomaTicketEngine
from feeds_intel_module import FeedsIntelDialog
from abuse_report_dialog import AbuseReportDialog
from predpi_validator_module import PreDpiValidatorWidget
from cyber_telemetry_widgets import CyberTopProtocolsWidget, CyberInfrastructureHealthWidget

# Desactivar advertencias SSL de forma nativa e indestructible
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =============================================================================
# BLOQUE DE SEGURIDAD: CARGA DE CREDENCIALES DESDE VARIABLES DE ENTORNO
# NUNCA escribir tokens o API keys directamente en este archivo.
# Ejecute setup_env_seguro.bat (como Administrador) para registrarlos en el sistema.
# =============================================================================
def _cargar_env_seguro() -> Tuple[str, str, str, str]:
    """Carga y valida todas las credenciales desde variables de entorno del sistema o archivo .env."""
    try:
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")
        if os.path.exists(env_path):
            load_dotenv(env_path)
        else:
            load_dotenv()
    except Exception:
        pass

    errores = []
    host          = os.environ.get("STELLAR_HOST")
    email         = os.environ.get("STELLAR_EMAIL")
    stellar_token = os.environ.get("STELLAR_TOKEN")
    gemini_key    = os.environ.get("GEMINI_API_KEY")

    # Fallback resiliente a registro de Windows si faltan variables
    if not (host and email and stellar_token and gemini_key):
        try:
            import winreg
            for hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
                subkey = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment" if hive == winreg.HKEY_LOCAL_MACHINE else r"Environment"
                try:
                    with winreg.OpenKey(hive, subkey) as reg_key:
                        if not host:
                            try: host = str(winreg.QueryValueEx(reg_key, "STELLAR_HOST")[0]).strip()
                            except Exception: pass
                        if not email:
                            try: email = str(winreg.QueryValueEx(reg_key, "STELLAR_EMAIL")[0]).strip()
                            except Exception: pass
                        if not stellar_token:
                            try: stellar_token = str(winreg.QueryValueEx(reg_key, "STELLAR_TOKEN")[0]).strip()
                            except Exception: pass
                        if not gemini_key:
                            try: gemini_key = str(winreg.QueryValueEx(reg_key, "GEMINI_API_KEY")[0]).strip()
                            except Exception: pass
                except Exception:
                    pass
        except Exception:
            pass

    if not gemini_key:
        try:
            from soar_ai_client import is_antigravity_available
            if is_antigravity_available():
                gemini_key = "ANTIGRAVITY_OAUTH"
        except Exception:
            pass
        if not gemini_key and os.environ.get("NVIDIA_API_KEY"):
            gemini_key = os.environ.get("NVIDIA_API_KEY")

    if not host:          errores.append("STELLAR_HOST")
    if not email:         errores.append("STELLAR_EMAIL")
    if not stellar_token: errores.append("STELLAR_TOKEN")
    if not gemini_key:    errores.append("GEMINI_API_KEY (o Antigravity OAuth)")

    if errores:
        app_tmp = QApplication.instance() or QApplication(sys.argv)
        QMessageBox.critical(
            None,
            "ERROR CRÍTICO - Variables de Entorno No Configuradas",
            "Las siguientes variables de entorno no están configuradas en este sistema ni en el archivo .env:\n\n"
            + "\n".join(f"  • {e}" for e in errores)
            + "\n\nConfigure el archivo '.env' o ejecute 'setup_env_seguro.bat' como Administrador.\n"
            "El Cockpit no puede iniciarse sin credenciales seguras."
        )
        sys.exit(1)

    return host, email, stellar_token, gemini_key

HOST, EMAIL_USUARIO, ALL_ACCESS_TOKEN, AI_API_KEY = _cargar_env_seguro()


# -----------------------------------------------------------------------------
# MOTOR DE CACHÉ CON EVICTION LRU (LAST RECENTLY USED) - THREAD-SAFE
# -----------------------------------------------------------------------------
import threading
class LRUCache:
    def __init__(self, maxsize: int = 50, ttl_seconds: int = 300) -> None:
        self._store = OrderedDict()
        self._maxsize = maxsize
        self._ttl_seconds = ttl_seconds
        self._lock = threading.Lock()

    def get(self, key: str, default: Any = None) -> Any:
        with self._lock:
            if key not in self._store:
                return default
            
            timestamp, value = self._store[key]
            if time.time() - timestamp > self._ttl_seconds:
                # El dato expiró por TTL
                del self._store[key]
                return default
                
            self._store.move_to_end(key)
            return value

    def set(self, key: str, value: Any) -> None:
        with self._lock:
            if key in self._store:
                self._store.move_to_end(key)
            else:
                if len(self._store) >= self._maxsize:
                    self._store.popitem(last=False)
            self._store[key] = (time.time(), value)

    def __contains__(self, key: str) -> bool:
        with self._lock:
            if key not in self._store:
                return False
            timestamp, _ = self._store[key]
            if time.time() - timestamp > self._ttl_seconds:
                # Evict silencioso al comprobar contains
                del self._store[key]
                return False
            return True

    def __getitem__(self, key):
        val = self.get(key, default=_LRUCACHE_SENTINEL)
        if val is _LRUCACHE_SENTINEL:
            raise KeyError(key)
        return val

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        with self._lock:
            self._store.pop(key, None)

# Sentinel privado para LRUCache — evita falsos KeyError cuando el valor almacenado es None
_LRUCACHE_SENTINEL = object()

# -----------------------------------------------------------------------------
# INFRAESTRUCTURA CORE CONFIG
# -----------------------------------------------------------------------------
CUOTA_POOL_GLOBAL = 10.0

# Archivo histórico de auditoría local (solo registra códigos de error, NO payloads)
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCHIVO_LOG = os.path.join(SCRIPT_DIR, "historial_caidas.log")

# Logger persistente: mantiene el fd abierto — elimina ~4.800 open/close syscalls por turno de 8hs
_audit_logger = _logging.getLogger("soc_cockpit")
if not _audit_logger.handlers:
    _audit_logger.setLevel(_logging.INFO)
    _audit_fh = _logging.FileHandler(ARCHIVO_LOG, mode="a", encoding="utf-8")
    _audit_fh.setFormatter(_logging.Formatter("%(message)s"))
    _audit_logger.addHandler(_audit_fh)
    _audit_logger.propagate = False

# CONFIGURACIÓN DEL ENGINE DE INTELIGENCIA ARTIFICIAL (ESTRUCTURA DE PRODUCCIÓN INTACTA)
AI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

# =============================================================================
# BLOQUE DE SEGURIDAD: INTEGRIDAD DE SCRIPTS DEL COCKPIT
# SHA256 esperado de cada sub-módulo al momento del despliegue.
# =============================================================================
HASHES_INTEGRIDAD = {}

def verificar_integridad_script(script_name):
    """
    Verifica el hash SHA256 del script antes de ejecutarlo.
    Si HASHES_INTEGRIDAD está vacío o el script no está en la tabla, 
    muestra una advertencia pero permite continuar (modo de transición).
    """
    if not HASHES_INTEGRIDAD:
        return True  # Modo transición: tabla vacía, no bloquear
    expected_hash = HASHES_INTEGRIDAD.get(script_name)
    if not expected_hash:
        return True  # Script no registrado: permitir con advertencia
    script_path = os.path.join(SCRIPT_DIR, script_name)
    try:
        with open(script_path, "rb") as f:
             actual_hash = hashlib.sha256(f.read()).hexdigest()
        return actual_hash == expected_hash
    except Exception:
        return False

# -----------------------------------------------------------------------------
# CORPUS ABSOLUTO DE MEMORIA INSTITUCIONAL (TEXTO INTEGRO SIN OMISIONES)
# --------------------------------------------------------# PROMPT_INSTITUCIONAL_COMPLETO importada como alias de SYSTEM_INSTRUCTIONS_MASTER | Tipo de evento | Activos | Descripción | Evidencia | Solicitud de Acción | Playbook |

# -----------------------------------------------------------------------------
# HELPERS DE HIGIENE ANALÍTICA (ANTI-CRASH PARSERS)
# -----------------------------------------------------------------------------
def safe_float(value):
    if value is None or value == "": return None
    try: return float(value)
    except (ValueError, TypeError): return None

def format_bytes(bytes_value):
    if bytes_value is None or bytes_value == "": return "0 B"
    try:
        b = float(bytes_value)
    except ValueError: return "0 B"
    if b == 0: return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while b >= 1024 and i < len(units) - 1:
        b /= 1024
        i += 1
    return f"{b:.2f} {units[i]}"

def get_bar(pct, width=10):
    if pct is None or pct < 0: pct = 0
    if pct > 100: pct = 100
    filled = int(round((pct / 100) * width))
    empty = width - filled
    return "[" + ("#" * filled) + ("-" * empty) + "]"

def ejecutar_beep(frecuencia=800, duracion=400):
    try: ctypes.windll.kernel32.Beep(frecuencia, duracion)
    except: pass

def log_to_file(message):
    """
    Logger de auditoria corporativo.
    REGLA DE SEGURIDAD: Registra SOLO metadatos operativos (timestamps, codigos HTTP,
    identificadores de caso). NUNCA registra payloads crudos, tokens, credenciales
    ni datos de telemetria de Interflow. Ver politica de logs Technoma SOC v2.
    Usa FileHandler persistente - cero open/close por llamada.
    """
    msg_seguro = message if len(message) <= 512 else message[:512] + "... [TRUNCADO POR POLITICA DE SEGURIDAD]"
    try:
        _audit_logger.info(msg_seguro)
    except Exception:
        pass


# =============================================================================
# MOTOR DE GOBERNANZA SLA / SLO, MTTD, MTTR Y TRIAJE POE L1 (SOCaaS TECHNOMA 24/7)
# =============================================================================
from sla_governance import SlaGovernanceEngine



# -----------------------------------------------------------------------------
# NOTIFICACIONES PUSH MÓVILES (ntfy.sh) - ASÍNCRONO & ANTI-SPAM
# -----------------------------------------------------------------------------
class MobileAlertsNotifier:
    """
    Gestor de notificaciones push móviles hacia ntfy.sh.
    Envío completamente asíncrono en segundo plano (daemon thread)
    con control anti-spam y deduplicación por ticket en memoria RAM.
    """
    DEFAULT_TOPIC = "technoma_soc_kevin_alerts_773"
    _current_topic = None

    @classmethod
    def get_topic(cls) -> str:
        if cls._current_topic:
            return cls._current_topic
        return os.environ.get("NTFY_TOPIC", cls.DEFAULT_TOPIC).strip()

    @classmethod
    def set_topic(cls, topic: str):
        if topic and str(topic).strip():
            cls._current_topic = str(topic).strip()

    @classmethod
    def send_notification(cls, title: str, message: str, priority: str = "default", tags: str = ""):
        """
        Envía una notificación push HTTP a ntfy.sh en un hilo daemon desacoplado.
        No bloquea el hilo principal de PySide6 bajo ninguna circunstancia.
        """
        def _worker():
            try:
                topic = cls.get_topic()
                url = f"https://ntfy.sh/{topic}"
                try:
                    str(title).encode("latin-1")
                    encoded_title = str(title)
                except UnicodeEncodeError:
                    b64_title = base64.b64encode(str(title).encode("utf-8")).decode("ascii")
                    encoded_title = f"=?utf-8?B?{b64_title}?="

                headers = {
                    "Title": encoded_title,
                    "Priority": str(priority),
                }
                if tags:
                    headers["Tags"] = str(tags)

                resp = requests.post(
                    url,
                    data=message.encode("utf-8"),
                    headers=headers,
                    timeout=5
                )
                if resp.status_code == 200:
                    log_to_file(f"[MOBILE NOTIFICATION OK] Título: '{title}' enviado al tópico '{topic}'")
                else:
                    log_to_file(f"[MOBILE NOTIFICATION WARN] Código HTTP {resp.status_code} desde ntfy.sh: {resp.text}")
            except Exception as ex:
                log_to_file(f"[MOBILE NOTIFICATION ERROR] Fallo al enviar push a ntfy.sh: {ex}")

        t = threading.Thread(target=_worker, daemon=True)
        t.start()

MobileNotificationDispatcher = MobileAlertsNotifier


# Patrón regex precompilado — cero re.compile() por invocación del fallback path de sanitizar_interflow
_JSON_FRAGMENT_PATTERN = re.compile(r'(\{(?:[^{}]|(?:\{[^{}]*\}))*\})', re.DOTALL)

# clean_forensic_data importada de stellar_gemini_orchestrator

def sanitizar_interflow(texto_crudo):
    if not texto_crudo:
        return ""

    # Fast path: el texto completo es un objeto/array JSON válido directo de la API
    try:
        data = json.loads(texto_crudo)
        cleaned = clean_forensic_data(data)
        # V4-07: preservar el tipo del dato raíz — lista vacía → [] no {}
        if cleaned is None:
            fallback = [] if isinstance(data, list) else {}
        else:
            fallback = cleaned
        return json.dumps(fallback, indent=4, ensure_ascii=False)
    except json.JSONDecodeError:
        pass

    # Fallback path: texto mixto con fragmentos JSON
    # Usa _JSON_FRAGMENT_PATTERN precompilado a nivel de módulo — cero re.compile() por llamada
    parts = []
    last_end = 0
    for match in _JSON_FRAGMENT_PATTERN.finditer(texto_crudo):
        if match.start() > last_end:
            parts.append(texto_crudo[last_end:match.start()])
        try:
            obj = json.loads(match.group())
            cleaned = clean_forensic_data(obj)
            parts.append(json.dumps(cleaned if cleaned is not None else {}, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            parts.append(match.group())
        last_end = match.end()
    parts.append(texto_crudo[last_end:])
    return "".join(parts)

# SecurityMaskingEngine importada de stellar_gemini_orchestrator

# -----------------------------------------------------------------------------
# TRABAJADORES ASINCRÓNICOS MULTIHILO (ANTI-FREEZE ENGINE)
# -----------------------------------------------------------------------------
class RestSessionManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(RestSessionManager, cls).__new__(cls)
                cls._instance.session = requests.Session()
                adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20, max_retries=1)
                cls._instance.session.mount('https://', adapter)
                cls._instance.jwt_token = None
                cls._instance.token_expiry = 0
                cls._instance.token_lock = threading.Lock()
            return cls._instance

    def get_headers(self, force_refresh: bool = False) -> Dict[str, str]:
        with self.token_lock:
            if force_refresh or not self.jwt_token or time.time() >= self.token_expiry:
                self._refresh_token()
            return {"Authorization": f"Bearer {self.jwt_token}", "Content-Type": "application/json"}

    def invalidate_token(self) -> None:
        with self.token_lock:
            self.jwt_token = None
            self.token_expiry = 0

    def _refresh_token(self) -> None:
        url = f"https://{HOST}/connect/api/v1/access_token"
        pair = f"{EMAIL_USUARIO}:{ALL_ACCESS_TOKEN}"
        b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
        headers = {"Authorization": f"Basic {b64}", "Content-Type": "application/json"}
        res = self.session.post(url, headers=headers, data="{}", verify=True, timeout=10)
        res.raise_for_status()
        data = res.json()
        self.jwt_token = data.get("access_token")
        exp = data.get("exp")
        now = time.time()
        # Stellar Cyber otorga tokens de 10 minutos (600s).
        # Renovación proactiva: renovar a los 7 minutos o con margen de seguridad de 120s antes de 'exp'.
        # Esto previene completamente que cualquier petición use un token a punto de caducar.
        if exp and isinstance(exp, (int, float)) and exp > now:
            self.token_expiry = max(now + 60, exp - 120)
        else:
            self.token_expiry = now + 420
        log_to_file(f"[AUTH] Token JWT renovado exitosamente. Válido por {int(self.token_expiry - now)}s.")

