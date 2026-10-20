#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — AI FORENSIC COPILOT (GUI DESKTOP APP)
=============================================================================
Aplicación nativa de escritorio con PySide6 (Qt) en modo oscuro:
- Motor de IA: NVIDIA NIM (z-ai/glm-5.3).
- 0-Latency Local Context: Pre-extracción instantánea (<10ms) de IPs,
  usuarios en Active Directory, activos e inventario.
- Streaming en tiempo real (tokens visibles al instante sin congelamiento).
- Selector de Modos:
    * ⚡ Modo Rápido (Turbo Stream · 0-Latency)
    * 🔬 Modo Profundo (Correlación Completa & Playbooks Maestros)
- Pestañas con separación quirúrgica:
    1. 🔍 Dictamen Forense (Markdown completo y estructurado en 4 fases)
    2. 💬 Cierre para Consola (Párrafo humanizado listo para Stellar Cyber)
    3. 📊 Bitácora TSV (Fila oficial de 18 columnas para Excel con 1 clic)
=============================================================================
"""

import os
import sys
import re
import json
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning)

try:
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QLabel, QTextEdit, QPushButton, QTabWidget, QSplitter, QFrame,
        QFileDialog, QMessageBox, QProgressBar, QStatusBar, QComboBox,
        QSizePolicy
    )
    from PySide6.QtCore import Qt, QThread, Signal
    from PySide6.QtGui import QFont, QIcon, QColor, QPalette, QTextCursor
    from abuse_report_dialog import AbuseReportWidget, AbuseReportEngine
except ImportError:
    class QThread:  # type: ignore
        def __init__(self, *a, **kw): pass
    class QMainWindow:  # type: ignore
        pass
    def Signal(*a, **kw):  # type: ignore
        class _Dummy:
            def emit(self, *x, **y): pass
        return _Dummy()

# Cargar variables de entorno
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from openai import OpenAI

# Importar enriquecimiento local y herramientas
BASE_DIR = Path(__file__).resolve().parent
import time
from soc_agent import auto_enriquecer_contexto, ejecutar_herramienta_local, preparar_entrada

# Configuración NVIDIA NIM
NVIDIA_BASE_URL = os.environ.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
NVIDIA_MODEL_FAST = os.environ.get("NVIDIA_MODEL_FAST", "meta/llama-3.2-11b-vision-instruct")
NVIDIA_MODEL_DEEP = os.environ.get("NVIDIA_MODEL_DEEP", "meta/llama-3.2-90b-vision-instruct")
NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", NVIDIA_MODEL_FAST)


# =============================================================================
# EXTRACTORES DE PESTAÑAS (CIERRE PARA CONSOLA & TSV)
# =============================================================================

def extraer_cierre_consola(texto: str) -> str:
    """Extrae quirúrgicamente el Comentario de Cierre Maestro de la Fase 3."""
    if not texto:
        return ""

    # 1. Buscar sección de Fase 3
    pos_fase3 = texto.find("### Fase 3")
    if pos_fase3 == -1:
        pos_fase3 = texto.find("Fase 3")

    sub = texto[pos_fase3:] if pos_fase3 != -1 else texto

    # 2. Localizar 'Comentario de Cierre Maestro'
    pos_marcador = -1
    longitud_marcador = 0
    for marker in [
        "Comentario de Cierre Maestro",
        "Comentario de Cierre",
        "Cierre Maestro",
        "Justificación Técnica de Cierre",
        "Justificación Técnica"
    ]:
        p = sub.find(marker)
        if p != -1:
            pos_marcador = p
            longitud_marcador = len(marker)
            break

    if pos_marcador != -1:
        bloque = sub[pos_marcador + longitud_marcador:]
        lineas = bloque.splitlines()
        parrafos = []

        for l in lineas:
            linea_limpia = l.strip()
            if not linea_limpia:
                if parrafos:
                    break
                continue

            # Detectar cabeceras o siguientes secciones de la fase
            if any(linea_limpia.startswith(sw) for sw in [
                "###", "##", "Fase 4",
                "- **Recomendación", "**Recomendación",
                "Recomendación de Tuning", "Regla de Supresión",
                "- **Estado", "- **Resolution"
            ]):
                if parrafos:
                    break
                continue

            # Quitar marcas de cita (>), viñetas (-) o comillas
            limpio = linea_limpia.lstrip(">").strip().strip('"')
            if limpio.startswith(":") or limpio.startswith("-"):
                limpio = limpio.lstrip(":- ").strip().strip('"')

            if limpio:
                parrafos.append(limpio)

        if parrafos:
            return " ".join(parrafos)

    # 3. Fallback inteligente: buscar bloques de cita `> ...` de más de 80 caracteres
    citas = re.findall(r"^>\s*(.+)$", texto, re.M)
    for c in citas:
        c_limpio = c.strip().strip('"')
        if len(c_limpio) > 80 and not c_limpio.startswith("[") and not c_limpio.startswith("!"):
            return c_limpio

    # 4. Fallback final seguro
    return (
        "El dictamen fue generado. Revise la sección 'Fase 3: Instrucción de Cierre' "
        "en la pestaña 'Dictamen Forense' para copiar el Comentario Maestro."
    )


def extraer_tsv_bitacora(texto: str) -> str:
    """Extrae la fila oficial de 18 columnas delimitada por tabuladores (TSV)."""
    if not texto:
        return ""

    # 1. Bloque explícito ```tsv ... ```
    if "```tsv" in texto:
        partes = texto.split("```tsv")
        if len(partes) > 1:
            tsv_candidate = partes[1].split("```")[0].strip()
            lineas = [l for l in tsv_candidate.splitlines() if "\t" in l]
            if lineas:
                return "\n".join(lineas)

    # 2. Cualquier bloque de código que contenga tabs
    for bloque in re.findall(r"```(?:tsv|text|tab)?(.*?)```", texto, re.S):
        if "\t" in bloque:
            lineas = [l.strip() for l in bloque.splitlines() if "\t" in l]
            if lineas:
                return "\n".join(lineas)

    # 3. Buscar líneas en el texto con 5 o más tabuladores
    lineas_con_tabs = [l.strip() for l in texto.splitlines() if l.count("\t") >= 5]
    if lineas_con_tabs:
        return "\n".join(lineas_con_tabs)

    return "No se detectó bloque TSV de 18 columnas en la respuesta. Revise la Fase 4 del Dictamen Forense."


# =============================================================================
# WORKER EN SEGUNDO PLANO (QThread Con Streaming en Tiempo Real)
# =============================================================================

class AgentWorker(QThread):
    token_received = Signal(str)
    tool_invoked = Signal(str, str)
    finished_success = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, prompt: str, mode: str = "fast"):
        super().__init__()
        self.prompt = prompt
        self.mode = mode

    def run(self):
        try:
            self.tool_invoked.emit("Motor Local", "Pre-extrayendo entidades e inventario en <10ms...")

            # 1. Pre-extracción ultra rápida de entidades
            evidencias_locales = auto_enriquecer_contexto(self.prompt)

            # 2. Contexto adicional según el modo seleccionado
            contexto_adicional = ""
            if self.mode == "deep":
                self.tool_invoked.emit("Playbooks & Bitácora", "Modo Profundo: Cruzando catálogo maestro de playbooks...")
                pb_path = BASE_DIR / "00_Playbooks" / "SOC_Incident_Response_Playbooks_Master.md"
                if pb_path.exists():
                    try:
                        with open(pb_path, "r", encoding="utf-8", errors="ignore") as f:
                            pb_content = f.read()[:2000]
                            contexto_adicional += f"\n\n### RESUMEN PLAYBOOKS DISPONIBLES:\n{pb_content}"
                    except Exception:
                        pass

            # 3. Compactación inteligente del JSON para evitar congelamientos
            prompt_compacto = preparar_entrada(self.prompt)
            if len(self.prompt) > len(prompt_compacto):
                self.tool_invoked.emit("Optimizador JSON", f"Entrada compactada de {len(self.prompt):,} a {len(prompt_compacto):,} caracteres.")

            # 4. Montar prompt enriquecido
            bloque_evidencias = ""
            if evidencias_locales:
                bloque_evidencias += f"\n\n---\n### EVIDENCIAS TÉCNICAS VERIFICADAS LOCALMENTE EN TECHNOMA (0-LATENCY):\n{evidencias_locales}"
            if contexto_adicional:
                bloque_evidencias += contexto_adicional
            if bloque_evidencias:
                bloque_evidencias += "\n---\nUtiliza obligatoriamente estas evidencias verificadas en tu dictamen consolidado."

            prompt_final = f"{prompt_compacto}{bloque_evidencias}"

            # 5. Instrucción del sistema unificada y canónica
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

            messages = [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt_final}
            ]

            from soar_ai_client import is_antigravity_available, SoarUnifiedOpenAIClient

            antigravity_ok = is_antigravity_available()
            if not antigravity_ok and not NVIDIA_API_KEY:
                raise RuntimeError("Falta autenticación IA: ni Google Antigravity OAuth ni NVIDIA_API_KEY están disponibles.")

            if antigravity_ok:
                target_model = os.environ.get("SOAR_AI_MODEL", "gemini-3.8-flash-high")
                self.tool_invoked.emit("Google Antigravity OAuth", f"Generando dictamen forense con {target_model}...")
            else:
                target_model = NVIDIA_MODEL_DEEP if self.mode == "deep" else NVIDIA_MODEL_FAST
                self.tool_invoked.emit("NVIDIA NIM", f"Generando streaming en vivo con modelo {target_model}...")

            client = SoarUnifiedOpenAIClient(
                base_url=NVIDIA_BASE_URL,
                api_key=NVIDIA_API_KEY,
                timeout=120.0,
                max_retries=1
            )

            kwargs = dict(
                model=target_model,
                messages=messages,
                temperature=0.25,
                max_tokens=8192,
                stream=True
            )

            # Intentar streaming con fallback automático si el modelo rechaza parámetros
            try:
                stream = client.chat.completions.create(**kwargs)
            except Exception as ex_init:
                if target_model != NVIDIA_MODEL_FAST and NVIDIA_API_KEY:
                    self.tool_invoked.emit("Fallback Automático", f"Cambiando a {NVIDIA_MODEL_FAST} por indisponibilidad de cola...")
                    kwargs["model"] = NVIDIA_MODEL_FAST
                    stream = client.chat.completions.create(**kwargs)
                else:
                    raise ex_init

            full_chunks = []
            razonamiento_chars = 0
            t0 = time.time()
            ultimo_aviso = 0.0

            for chunk in stream:
                if not chunk.choices:
                    continue
                delta = chunk.choices[0].delta

                # Detección y notificación en vivo de tokens de razonamiento
                r = getattr(delta, "reasoning_content", None) or getattr(delta, "reasoning", None)
                if r:
                    razonamiento_chars += len(r)
                    if time.time() - ultimo_aviso > 1.2:
                        ultimo_aviso = time.time()
                        self.tool_invoked.emit("Modelo Razonando", f"{int(time.time() - t0)}s · {razonamiento_chars:,} caracteres analizados...")

                # Tokens visibles de respuesta
                if delta.content:
                    self.token_received.emit(delta.content)
                    full_chunks.append(delta.content)

            full_text = "".join(full_chunks)
            if not full_text:
                if razonamiento_chars:
                    full_text = f"El modelo completó su razonamiento ({razonamiento_chars:,} caracteres) pero no emitió texto final. Utilice el Modo Rápido (Llama 3.2 11B)."
                else:
                    full_text = "Análisis completado sin texto retornado por la API."

            self.finished_success.emit(full_text)

        except Exception as e:
            self.error_occurred.emit(str(e))


# =============================================================================
# VENTANA PRINCIPAL DE ESCRITORIO
# =============================================================================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Technoma SOC — AI Forensic Copilot")
        self.adaptar_tamano_pantalla()
        self.worker = None
        self.apply_theme()
        self.init_ui()

    def adaptar_tamano_pantalla(self):
        """Calcula resolución y posición proporcional según la pantalla activa."""
        screen = QApplication.primaryScreen()
        if screen:
            avail = screen.availableGeometry()
            target_w = min(1440, max(940, int(avail.width() * 0.90)))
            target_h = min(920, max(580, int(avail.height() * 0.88)))
            self.resize(target_w, target_h)
            self.setMinimumSize(880, 520)
            self.move(
                avail.x() + (avail.width() - target_w) // 2,
                avail.y() + (avail.height() - target_h) // 2
            )
        else:
            self.resize(1220, 800)
            self.setMinimumSize(880, 520)

    def apply_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0b0e14;
                color: #e6edf3;
            }
            QWidget {
                background-color: #0b0e14;
                color: #e6edf3;
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
                font-size: 13px;
            }
            #headerFrame {
                background-color: #161b22;
                border-bottom: 1px solid #30363d;
            }
            QFrame.card {
                background-color: #121721;
                border: 1px solid #232c3d;
                border-radius: 8px;
            }
            QLabel.brandTitle {
                font-size: 16px;
                font-weight: 700;
                color: #f0f6fc;
                letter-spacing: 0.3px;
            }
            QLabel.brandBadge {
                background-color: #1f293d;
                color: #58a6ff;
                border: 1px solid #388bfd40;
                border-radius: 4px;
                padding: 2px 7px;
                font-size: 10px;
                font-weight: 600;
            }
            QLabel.statusPill {
                background-color: #23863625;
                color: #3fb950;
                border: 1px solid #2ea04360;
                border-radius: 13px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 600;
            }
            QLabel.cardTitle {
                font-size: 14px;
                font-weight: 600;
                color: #58a6ff;
            }
            QComboBox {
                background-color: #1c2333;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 4px 10px;
                font-size: 12px;
                font-weight: 500;
            }
            QComboBox:hover {
                border-color: #58a6ff;
            }
            QComboBox QAbstractItemView {
                background-color: #161b22;
                color: #e6edf3;
                selection-background-color: #1f6feb;
                selection-color: #ffffff;
                border: 1px solid #30363d;
            }
            QTextEdit {
                background-color: #0d1117;
                border: 1px solid #232c3d;
                border-radius: 6px;
                color: #e6edf3;
                font-family: 'Consolas', 'Cascadia Code', monospace;
                font-size: 12px;
                line-height: 1.4;
                padding: 8px;
            }
            QTextEdit:focus {
                border: 1px solid #58a6ff;
            }
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
                border-color: #8b949e;
                color: #f0f6fc;
            }
            QPushButton.primary {
                background-color: #1f6feb;
                color: #ffffff;
                border: 1px solid #388bfd;
                font-weight: 600;
            }
            QPushButton.primary:hover {
                background-color: #388bfd;
            }
            QPushButton.primary:disabled {
                background-color: #1f293d;
                color: #6e7681;
                border-color: #30363d;
            }
            QPushButton.success {
                background-color: #238636;
                color: #ffffff;
                border: 1px solid #2ea043;
                font-weight: 600;
            }
            QPushButton.success:hover {
                background-color: #2ea043;
            }
            QTabWidget::pane {
                border: 1px solid #232c3d;
                background-color: #121721;
                border-radius: 6px;
            }
            QTabBar::tab {
                background: #0d1117;
                color: #8b949e;
                padding: 8px 16px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                font-weight: 500;
            }
            QTabBar::tab:selected {
                background: #121721;
                color: #58a6ff;
                border-bottom: 2px solid #58a6ff;
                font-weight: 600;
            }
            QProgressBar {
                border: 1px solid #30363d;
                border-radius: 3px;
                background-color: #0d1117;
                color: #8b949e;
                height: 4px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #58a6ff;
            }
            QStatusBar {
                background-color: #161b22;
                border-top: 1px solid #232c3d;
                color: #8b949e;
                font-size: 11px;
                padding: 2px 8px;
            }
        """)

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------------------------------------------------------------------
        # 1. HEADER BAR (ALTURA FIJA Y MODERNA - SIN BLOQUES EXPANDIDOS)
        # ---------------------------------------------------------------------
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_frame.setFixedHeight(54)
        header_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(18, 0, 18, 0)
        header_layout.setSpacing(12)

        # Branding Izquierda
        brand_icon = QLabel("🛡️")
        brand_icon.setStyleSheet("font-size: 18px;")
        header_layout.addWidget(brand_icon)

        brand_title = QLabel("Technoma SOC — AI Forensic Copilot")
        brand_title.setProperty("class", "brandTitle")
        header_layout.addWidget(brand_title)

        brand_badge = QLabel("OpenXDR v2.5")
        brand_badge.setProperty("class", "brandBadge")
        header_layout.addWidget(brand_badge)

        header_layout.addStretch()

        # Selector de Modo
        mode_label = QLabel("Modo:")
        mode_label.setStyleSheet("color: #8b949e; font-size: 12px; font-weight: 500;")
        header_layout.addWidget(mode_label)

        self.mode_combo = QComboBox()
        self.mode_combo.setFixedHeight(28)
        self.mode_combo.addItem("⚡ Modo Rápido (Llama 3.2 11B · <1s Latencia)", "fast")
        self.mode_combo.addItem("🔬 Modo Profundo (Llama 3.2 90B · Correlación)", "deep")
        header_layout.addWidget(self.mode_combo)

        # Indicador de Estado Conectado (Pill sutil)
        status_pill = QLabel("● Online (NVIDIA Llama 3.2 · AD · PB)")
        status_pill.setProperty("class", "statusPill")
        status_pill.setFixedHeight(26)
        header_layout.addWidget(status_pill)

        main_layout.addWidget(header_frame, 0)

        # ---------------------------------------------------------------------
        # 2. CUERPO PRINCIPAL CON SPLITTER
        # ---------------------------------------------------------------------
        body_container = QWidget()
        body_layout = QVBoxLayout(body_container)
        body_layout.setContentsMargins(16, 14, 16, 12)
        body_layout.setSpacing(10)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(8)
        splitter.setChildrenCollapsible(False)

        # --- PANEL IZQUIERDO: ENTRADA ---
        left_card = QFrame()
        left_card.setProperty("class", "card")
        left_layout = QVBoxLayout(left_card)
        left_layout.setContentsMargins(14, 14, 14, 14)
        left_layout.setSpacing(10)

        input_title = QLabel("📥 Entrada de Alerta / Caso Operativo")
        input_title.setProperty("class", "cardTitle")
        left_layout.addWidget(input_title)

        input_hint = QLabel("Pega el volcado JSON de Interflow, log de firewall o escribe tu consulta:")
        input_hint.setStyleSheet("color: #8b949e; font-size: 11px;")
        left_layout.addWidget(input_hint)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText(
            "Ejemplo 1:\n"
            "El firewall FortiGate reportó 1,000 bloqueos en 5 minutos desde NB-NOC1 "
            "(alexiscandia) hacia 192.168.15.23 puerto 3000.\n\n"
            "Ejemplo 2:\nPega aquí el JSON completo de Interflow con {\"data\": {\"docs\": [...]}}"
        )
        left_layout.addWidget(self.input_text)

        btn_row = QHBoxLayout()
        self.btn_load_file = QPushButton("📂 Cargar Archivo (.json / .txt)")
        self.btn_load_file.clicked.connect(self.load_file_dialog)
        btn_row.addWidget(self.btn_load_file)

        self.btn_clear = QPushButton("🗑️ Limpiar")
        self.btn_clear.clicked.connect(self.clear_all)
        btn_row.addWidget(self.btn_clear)

        left_layout.addLayout(btn_row)

        self.btn_analyze = QPushButton("🚀 Ejecutar Triaje Forense")
        self.btn_analyze.setProperty("class", "primary")
        self.btn_analyze.setFixedHeight(40)
        self.btn_analyze.clicked.connect(self.run_analysis)
        left_layout.addWidget(self.btn_analyze)

        self.btn_abuse_fast = QPushButton("📧 Formatear Correo de Abuso (Instantáneo)")
        self.btn_abuse_fast.setStyleSheet("""
            QPushButton {
                background-color: #162638;
                color: #58a6ff;
                border: 1px solid #388bfd80;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1f354f;
                border-color: #58a6ff;
                color: #ffffff;
            }
        """)
        self.btn_abuse_fast.setFixedHeight(36)
        self.btn_abuse_fast.setToolTip("Parsea el JSON de Interflow/Stellar Cyber en <5ms y prepara el correo formal de notificación de abuso")
        self.btn_abuse_fast.clicked.connect(self.format_abuse_report_instant)
        left_layout.addWidget(self.btn_abuse_fast)

        # Trazas de herramientas en vivo
        tools_box = QFrame()
        tools_box.setStyleSheet("background-color: #0d1117; border: 1px solid #232c3d; border-radius: 6px; padding: 6px;")
        tools_layout = QVBoxLayout(tools_box)
        tools_layout.setContentsMargins(8, 8, 8, 8)
        tools_layout.setSpacing(4)

        tools_lbl = QLabel("⚡ Actividad de Análisis en Tiempo Real:")
        tools_lbl.setStyleSheet("color: #8b949e; font-size: 11px; font-weight: 600;")
        tools_layout.addWidget(tools_lbl)

        self.tools_log = QLabel("Listo para recibir alertas del SOC.")
        self.tools_log.setStyleSheet("color: #58a6ff; font-family: monospace; font-size: 11px;")
        self.tools_log.setWordWrap(True)
        tools_layout.addWidget(self.tools_log)

        left_layout.addWidget(tools_box)
        splitter.addWidget(left_card)

        # --- PANEL DERECHO: ENTREGABLES Y PESTAÑAS ---
        right_card = QFrame()
        right_card.setProperty("class", "card")
        right_layout = QVBoxLayout(right_card)
        right_layout.setContentsMargins(14, 14, 14, 14)
        right_layout.setSpacing(10)

        output_title = QLabel("📋 Dictamen Forense y Entregables del SOC")
        output_title.setProperty("class", "cardTitle")
        right_layout.addWidget(output_title)

        self.tabs = QTabWidget()

        # Tab 1: Dictamen Forense Completo
        self.out_full = QTextEdit()
        self.out_full.setReadOnly(True)
        self.tabs.addTab(self.out_full, "🔍 Dictamen Forense")

        # Tab 2: Cierre para Consola
        tab2_widget = QWidget()
        tab2_layout = QVBoxLayout(tab2_widget)
        tab2_layout.setContentsMargins(10, 10, 10, 10)
        tab2_layout.setSpacing(10)

        hint_closing = QLabel("Comentario de Cierre Maestro (Listo para auditoría / modal Stellar Cyber):")
        hint_closing.setStyleSheet("color: #8b949e; font-size: 11px;")
        tab2_layout.addWidget(hint_closing)

        self.out_closing = QTextEdit()
        self.out_closing.setReadOnly(True)
        tab2_layout.addWidget(self.out_closing)

        btn_copy_closing = QPushButton("📋 Copiar Justificación al Portapapeles")
        btn_copy_closing.setProperty("class", "success")
        btn_copy_closing.setFixedHeight(34)
        btn_copy_closing.clicked.connect(lambda: self.copy_to_clipboard(self.out_closing.toPlainText(), "Justificación de cierre copiada"))
        tab2_layout.addWidget(btn_copy_closing)
        self.tabs.addTab(tab2_widget, "💬 Cierre para Consola")

        # Tab 3: Bitácora TSV (Excel)
        tab3_widget = QWidget()
        tab3_layout = QVBoxLayout(tab3_widget)
        tab3_layout.setContentsMargins(10, 10, 10, 10)
        tab3_layout.setSpacing(10)

        hint_tsv = QLabel("Fila oficial de 18 columnas (A-R) delimitada por tabuladores (1-clic para pegar en Excel):")
        hint_tsv.setStyleSheet("color: #8b949e; font-size: 11px;")
        tab3_layout.addWidget(hint_tsv)

        self.out_tsv = QTextEdit()
        self.out_tsv.setReadOnly(True)
        tab3_layout.addWidget(self.out_tsv)

        btn_copy_tsv = QPushButton("📋 Copiar Bloque TSV (1-Clic para Excel)")
        btn_copy_tsv.setProperty("class", "success")
        btn_copy_tsv.setFixedHeight(34)
        btn_copy_tsv.clicked.connect(lambda: self.copy_to_clipboard(self.out_tsv.toPlainText(), "Fila TSV copiada"))
        tab3_layout.addWidget(btn_copy_tsv)
        self.tabs.addTab(tab3_widget, "📊 Bitácora TSV (Excel)")

        # Tab 4: Reportes de Abuso (OpenXDR)
        self.tab_abuse = AbuseReportWidget(self)
        self.tabs.addTab(self.tab_abuse, "📧 Reporte de Abuso")

        right_layout.addWidget(self.tabs)
        splitter.addWidget(right_card)

        # Proporciones equilibradas: 40% izquierda, 60% derecha
        splitter.setStretchFactor(0, 4)
        splitter.setStretchFactor(1, 6)

        body_layout.addWidget(splitter, 1)

        # Barra de progreso sutil
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        body_layout.addWidget(self.progress_bar, 0)

        main_layout.addWidget(body_container, 1)

        # Barra de estado inferior
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Listo para operar. Ingrese una alerta y presione 'Ejecutar Triaje Forense' o 'Formatear Correo de Abuso'.")

    # -------------------------------------------------------------------------
    # ACCIONES Y FLUJO OPERATIVO
    # -------------------------------------------------------------------------
    def clear_all(self):
        self.input_text.clear()
        self.out_full.clear()
        self.out_closing.clear()
        self.out_tsv.clear()
        self.tab_abuse.cargar_datos_desde_texto("")
        self.tools_log.setText("Listo para recibir alertas del SOC.")
        self.status.showMessage("Área de trabajo restablecida.")

    def format_abuse_report_instant(self):
        """Procesa el JSON en memoria en <5ms y formatea el correo oficial de abuso."""
        text = self.input_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Entrada Vacía", "Por favor pega primero el volcado JSON en la entrada de alerta.")
            return
        cant = self.tab_abuse.cargar_datos_desde_texto(text)
        if cant > 0:
            self.tabs.setCurrentWidget(self.tab_abuse)
            self.tools_log.setText(f"✓ Formateado correo de abuso para {cant} IP(s) en 0ms.")
            self.status.showMessage(f"✓ Correo de abuso preparado para {cant} IP(s).", 4000)
        else:
            QMessageBox.information(
                self, "Sin IPs de Escaneo",
                "No se detectaron IPs públicas o logs de firewall en el texto ingresado.\nVerifique que contenga el JSON de Stellar Cyber / Interflow o FortiGate."
            )

    def load_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo de alerta", str(BASE_DIR),
            "Archivos de Alerta (*.json *.txt *.log *.md);;Todos (*.*)"
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    self.input_text.setText(f.read())
                self.status.showMessage(f"Archivo cargado: {Path(file_path).name}")
            except Exception as e:
                QMessageBox.critical(self, "Error al abrir archivo", str(e))

    def run_analysis(self):
        prompt = self.input_text.toPlainText().strip()
        if not prompt:
            QMessageBox.warning(self, "Entrada vacía", "Por favor ingresa un texto de consulta o pega un volcado JSON de Interflow.")
            return

        selected_mode = self.mode_combo.currentData()

        # Preparar UI para ejecución en streaming
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setText("⏳ Generando dictamen forense...")
        self.progress_bar.setVisible(True)
        self.out_full.clear()
        self.out_closing.clear()
        self.out_tsv.clear()
        self.tabs.setCurrentIndex(0)

        self.tools_log.setText("Iniciando motor NVIDIA NIM y preparando evidencias locales...")
        self.status.showMessage(f"Ejecutando análisis en {self.mode_combo.currentText()}...")

        self.worker = AgentWorker(prompt, mode=selected_mode)
        self.worker.token_received.connect(self.on_token_received)
        self.worker.tool_invoked.connect(self.on_tool_invoked)
        self.worker.finished_success.connect(self.on_analysis_finished)
        self.worker.error_occurred.connect(self.on_analysis_error)
        self.worker.start()

    def on_token_received(self, chunk: str):
        """Streaming de tokens en tiempo real directamente en la pestaña de dictamen."""
        cursor = self.out_full.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(chunk)
        self.out_full.setTextCursor(cursor)
        self.out_full.ensureCursorVisible()

    def on_tool_invoked(self, tool_name: str, detail: str):
        self.tools_log.setText(f"⚡ [{tool_name}] {detail}")
        self.status.showMessage(f"Procesando: {detail}")

    def on_analysis_finished(self, result_text: str):
        self.progress_bar.setVisible(False)
        self.btn_analyze.setEnabled(True)
        self.btn_analyze.setText("🚀 Ejecutar Triaje Forense")
        self.tools_log.setText("✅ Análisis completado con éxito (NVIDIA NIM).")
        self.status.showMessage("Dictamen forense y entregables generados satisfactoriamente.")

        # Asegurar que el dictamen completo esté visible
        if not self.out_full.toPlainText().strip():
            self.out_full.setPlainText(result_text)

        # Extracción quirúrgica de Fase 3 y Fase 4
        cierre_limpio = extraer_cierre_consola(result_text)
        tsv_limpio = extraer_tsv_bitacora(result_text)

        self.out_closing.setPlainText(cierre_limpio)
        self.out_tsv.setPlainText(tsv_limpio)

        # Auto-poblar también la pestaña de reporte de abuso si la entrada contenía IPs de escaneo
        try:
            raw_input = self.input_text.toPlainText().strip()
            if raw_input:
                self.tab_abuse.cargar_datos_desde_texto(raw_input)
        except Exception:
            pass

    def on_analysis_error(self, err_msg: str):
        self.progress_bar.setVisible(False)
        self.btn_analyze.setEnabled(True)
        self.btn_analyze.setText("🚀 Ejecutar Triaje Forense")
        self.tools_log.setText(f"❌ Error: {err_msg}")
        self.status.showMessage("Ocurrió un error en el análisis.")
        QMessageBox.critical(self, "Error de Ejecución", f"No se pudo completar el triaje forense:\n\n{err_msg}")

    def copy_to_clipboard(self, text: str, msg: str):
        if text.strip() and "No se detectó" not in text and "Revise la sección" not in text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text.strip())
            self.status.showMessage(f"✅ {msg} en el portapapeles.")
        elif text.strip():
            clipboard = QApplication.clipboard()
            clipboard.setText(text.strip())
            self.status.showMessage(f"ℹ️ Contenido copiado al portapapeles.")
        else:
            self.status.showMessage("El contenido a copiar está vacío.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
