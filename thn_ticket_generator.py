#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
      TECHNOMA SOC - GENERADOR DE TICKETS DE ESCALACIÓN & BITÁCORA (DFIR)
=============================================================================
Módulo independiente e integrable en Master Cockpit para la generación
automática de Tickets de Escalación THN-SOC y su sincronización bidireccional
con la Bitácora de 18 columnas de Excel/Google Sheets, eliminando la dependencia
de fórmulas frágiles en hojas de cálculo.
"""

import sys
import os
import re
import json
from datetime import datetime
from typing import Dict, Any, Optional

from PySide6.QtCore import Qt, Signal, Slot, QSize, QRect, QMarginsF
from PySide6.QtGui import (
    QColor, QFont, QPixmap, QPainter, QClipboard, QIcon,
    QTextDocument, QPdfWriter, QPageSize, QPageLayout
)
from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel,
    QLineEdit, QTextEdit, QComboBox, QPushButton, QFrame, QSplitter,
    QScrollArea, QMessageBox, QFileDialog, QApplication, QGroupBox
)


class TechnomaTicketEngine:
    """Motor de conversión bidireccional entre formatos de tickets, hojas de cálculo y markdown."""

    PRIORITY_MAP = {
        "critica": "Crítica 🟣",
        "crítica": "Crítica 🟣",
        "critical": "Crítica 🟣",
        "alta": "Alta 🔴",
        "high": "Alta 🔴",
        "media": "Media 🟡",
        "medium": "Media 🟡",
        "baja": "Baja 🟢",
        "low": "Baja 🟢",
        "informativo": "Informativo ℹ️",
        "info": "Informativo ℹ️"
    }

    @classmethod
    def normalize_priority(cls, prio_str: str) -> str:
        clean = (prio_str or "").strip().lower()
        for k, v in cls.PRIORITY_MAP.items():
            if k in clean:
                return v
        return prio_str or "Media 🟡"

    @classmethod
    def parse_excel_ticket_card(cls, text: str) -> Dict[str, str]:
        """
        Parsea un volcado de 2 columnas de Excel (Columnas D y E) tal como se copia
        de la tarjeta de ticket de Technoma.
        """
        data = {
            "ticket_id": "",
            "prioridad": "Media 🟡",
            "asunto": "",
            "descripcion": "",
            "activos": "",
            "evidencia": "",
            "solicitud_accion": "",
            "tenant": "",
            "analista": "Kevin Moraes",
            "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        lines = text.splitlines()
        current_field = None
        buffer_lines = []

        for line in lines:
            # Detectar cabecera de ticket THN-SOC-XX
            match_id = re.search(r'(THN-SOC-\d+)', line, re.IGNORECASE)
            if match_id and not data["ticket_id"]:
                data["ticket_id"] = match_id.group(1).upper()

            # Separar por tabuladores
            parts = line.split('\t')
            label = parts[0].strip().lower() if len(parts) > 0 else ""
            val = parts[1].strip() if len(parts) > 1 else ""

            if label in ["prioridad", "asunto", "descripción", "descripcion", "activos", "evidencia", "solicitud de acción", "solicitud de accion"]:
                if current_field:
                    data[current_field] = "\n".join(buffer_lines).strip().strip('"')
                buffer_lines = [val] if val else []

                if label == "prioridad":
                    current_field = "prioridad"
                elif label == "asunto":
                    current_field = "asunto"
                elif label in ["descripción", "descripcion"]:
                    current_field = "descripcion"
                elif label == "activos":
                    current_field = "activos"
                elif label == "evidencia":
                    current_field = "evidencia"
                elif label in ["solicitud de acción", "solicitud de accion"]:
                    current_field = "solicitud_accion"
            else:
                if current_field and line.strip():
                    buffer_lines.append(line.strip())

        if current_field and buffer_lines:
            data[current_field] = "\n".join(buffer_lines).strip()

        def clean_excel_val(raw_val: str) -> str:
            v = raw_val.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            return v.replace('""', '"').strip()

        for k in ["descripcion", "activos", "evidencia", "solicitud_accion"]:
            if k in data:
                data[k] = clean_excel_val(data[k])

        # Normalizar prioridad
        data["prioridad"] = cls.normalize_priority(data.get("prioridad") or "Media 🟡")

        # Deducir Tenant si es posible
        if "cajaande" in data["activos"].lower() or "caja ande" in data["asunto"].lower():
            data["tenant"] = "Caja Ande"
        elif "technoma" in data["activos"].lower() or "technoma" in data["asunto"].lower():
            data["tenant"] = "Technoma"
        elif "vascol" in data["activos"].lower() or "vascol" in data["asunto"].lower():
            data["tenant"] = "Vascol"

        return data

    @classmethod
    def parse_bitacora_row(cls, tsv_row: str) -> Dict[str, str]:
        """
        Parsea una fila única de 18 columnas de la bitácora del SOC.
        """
        parts = tsv_row.strip().split('\t')
        data = {
            "fecha_hora": parts[0].strip() if len(parts) > 0 else datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "analista": parts[1].strip() if len(parts) > 1 else "Kevin Moraes",
            "tenant": parts[2].strip() if len(parts) > 2 else "",
            "id_caso": parts[3].strip() if len(parts) > 3 else "N/A",
            "fuente_deteccion": parts[4].strip() if len(parts) > 4 else "Sophos Central",
            "ticket_id": parts[5].strip() if len(parts) > 5 and parts[5].strip() != "N/A" else "",
            "prioridad": cls.normalize_priority(parts[6].strip() if len(parts) > 6 else "Media 🟡"),
            "tipo_evento": parts[7].strip() if len(parts) > 7 else "",
            "asunto": parts[8].strip() if len(parts) > 8 else "",
            "activos": parts[9].strip().strip('"') if len(parts) > 9 else "",
            "descripcion": parts[10].strip().strip('"') if len(parts) > 10 else "",
            "evidencia": parts[11].strip().strip('"') if len(parts) > 11 else "",
            "solicitud_accion": parts[12].strip().strip('"') if len(parts) > 12 else "",
            "estado": parts[13].strip() if len(parts) > 13 else "En Seguimiento",
            "url": parts[14].strip() if len(parts) > 14 else "N/A",
            "gen_ticket": parts[15].strip() if len(parts) > 15 else "SI",
            "ticket_ext": parts[16].strip() if len(parts) > 16 else "",
            "playbook": parts[17].strip() if len(parts) > 17 else "PB-1.2"
        }
        if not data["ticket_id"] and data.get("ticket_ext"):
            data["ticket_id"] = data["ticket_ext"]
        return data

    @classmethod
    def to_excel_ticket_card(cls, data: Dict[str, str]) -> str:
        """
        Genera el bloque exacto de 2 columnas (D y E) listo para pegar en Excel
        sobre las celdas de la tarjeta sin fórmulas.
        """
        ticket_id = (data.get("ticket_id") or "THN-SOC-XX").upper()
        prio = data.get("prioridad") or "Media 🟡"
        asunto = data.get("asunto") or ""
        
        # Escapado para Excel si contiene saltos de línea
        def escape_excel(val: str) -> str:
            v = val.replace('"', '""')
            if '\n' in v or '\t' in v or '"' in v:
                return f'"{v}"'
            return v

        desc = escape_excel(data.get("descripcion") or "")
        activos = escape_excel(data.get("activos") or "")
        evidencia = escape_excel(data.get("evidencia") or "")
        solicitud = escape_excel(data.get("solicitud_accion") or "")

        lines = [
            f"\t{ticket_id}",
            f"Prioridad\t{prio}",
            f"Asunto\t{asunto}",
            f"Descripción\t{desc}",
            f"Activos\t{activos}",
            f"Evidencia\t{evidencia}",
            f"Solicitud de Acción\t{solicitud}"
        ]
        return "\n".join(lines)

    @classmethod
    def to_bitacora_row(cls, data: Dict[str, str]) -> str:
        """
        Genera la fila oficial de 18 columnas separadas por tabuladores para la Bitácora.
        """
        def escape_tsv(val: str) -> str:
            v = (val or "").replace('"', '""').strip()
            if '\n' in v or '\t' in v:
                return f'"{v}\n\n"'
            return v

        fecha = data.get("fecha_hora") or datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        analista = data.get("analista") or "Kevin Moraes"
        tenant = data.get("tenant") or "Caja Ande"
        id_caso = data.get("id_caso") or "N/A"
        fuente = data.get("fuente_deteccion") or "Sophos Central"
        ticket = (data.get("ticket_id") or "THN-SOC-XX").upper()
        prio = data.get("prioridad") or "Media 🟡"
        tipo_ev = data.get("tipo_evento") or "MALWARE - PUA"
        asunto = data.get("asunto") or ""
        activos = escape_tsv(data.get("activos") or "")
        desc = escape_tsv(data.get("descripcion") or "")
        evid = escape_tsv(data.get("evidencia") or "")
        solicitud = escape_tsv(data.get("solicitud_accion") or "")
        estado = data.get("estado") or "En Seguimiento"
        url = data.get("url") or "N/A"
        gen_ticket = data.get("gen_ticket") or "SI"
        playbook = data.get("playbook") or "PB-1.2"

        cols = [
            fecha, analista, tenant, id_caso, fuente, ticket,
            prio, tipo_ev, asunto, activos, desc, evid,
            solicitud, estado, url, gen_ticket, ticket, playbook
        ]
        return "\t".join(cols)

    @classmethod
    def to_markdown_ticket(cls, data: Dict[str, str]) -> str:
        """
        Genera una tarjeta elegante en Markdown para enviar por Teams, Slack o correo.
        """
        ticket = (data.get("ticket_id") or "THN-SOC-XX").upper()
        return (
            f"### 🛡️ TECHNOMA SOC — TICKET DE ESCALACIÓN: `{ticket}`\n\n"
            f"| Campo | Detalle Operativo |\n"
            f"| :--- | :--- |\n"
            f"| **Prioridad** | **{data.get('prioridad', 'Media 🟡')}** |\n"
            f"| **Asunto** | {data.get('asunto', '')} |\n"
            f"| **Activos** | `{data.get('activos', '').replace(chr(10), ' | ')}` |\n"
            f"| **Descripción** | {data.get('descripcion', '')} |\n"
            f"| **Solicitud de Acción** | 🎯 **{data.get('solicitud_accion', '')}** |\n\n"
            f"#### 🔬 Evidencia Técnica (Payload / Telemetría):\n"
            f"```json\n{data.get('evidencia', '')}\n```\n"
        )

    @classmethod
    def to_html_ticket(cls, data: Dict[str, str]) -> str:
        """
        Genera una tarjeta en HTML enriquecido con la fuente Outfit en tamaño 12 y el logo oficial.
        """
        ticket = (data.get("ticket_id") or "THN-SOC-XX").upper()
        root_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(root_dir, "logo-technoma.png")
        if not os.path.exists(logo_path):
            logo_path = "logo-technoma.png"

        logo_html = ""
        if os.path.exists(logo_path):
            try:
                import base64
                with open(logo_path, "rb") as lf:
                    b64_logo = base64.b64encode(lf.read()).decode("utf-8")
                logo_html = f'<div style="text-align: center; margin-bottom: 8px;"><img src="data:image/png;base64,{b64_logo}" width="130" style="display: block; margin: 0 auto;"/></div>'
            except Exception:
                pass

        if not logo_html:
            logo_html = '<div style="text-align: center; margin-bottom: 6px; font-family: \'Outfit\', sans-serif; font-size: 22px; font-weight: bold; color: #a81c1c;">THN TECHNOMA</div>'

        rows = [
            ("Prioridad", data.get("prioridad") or "Media 🟡"),
            ("Asunto", data.get("asunto") or ""),
            ("Descripción", (data.get("descripcion") or "").replace("\n", "<br/>")),
            ("Activos", (data.get("activos") or "").replace("\n", "<br/>")),
            ("Evidencia", f"<pre style='font-family: \"Outfit\", Consolas, monospace; font-size: 11pt; margin: 0; white-space: pre-wrap;'>{data.get('evidencia') or ''}</pre>"),
            ("Solicitud de Acción", (data.get("solicitud_accion") or "").replace("\n", "<br/>"))
        ]

        tbody = ""
        for label, val in rows:
            tbody += f"""
            <tr>
                <td style="background-color: #d9d9d9; font-weight: bold; font-family: 'Outfit', sans-serif; font-size: 12pt; padding: 8px 10px; border: 1px solid #222222; vertical-align: top; width: 145px;">{label}</td>
                <td style="background-color: #ffffff; font-family: 'Outfit', sans-serif; font-size: 12pt; padding: 8px 12px; border: 1px solid #222222; vertical-align: top;">{val}</td>
            </tr>
            """

        html = f"""
        <div style="font-family: 'Outfit', sans-serif; font-size: 12pt; max-width: 650px; background-color: #ffffff; padding: 14px; border: 2px solid #222222;">
            {logo_html}
            <div style="background-color: #f2f2f2; color: #a81c1c; font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 14pt; text-align: center; padding: 6px; border: 1.5px solid #222222; border-bottom: none;">{ticket}</div>
            <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #222222;">
                <tbody>
                    {tbody}
                </tbody>
            </table>
        </div>
        """
        return html

    @classmethod
    def export_to_pdf(cls, data: Dict[str, str], output_path: str) -> str:
        """
        Exporta el ticket formal a un archivo PDF corporativo de alta calidad con membrete oficial.
        """
        html = cls.to_html_ticket(data)
        doc = QTextDocument()
        doc.setHtml(html)
        writer = QPdfWriter(output_path)
        writer.setPageSize(QPageSize(QPageSize.A4))
        layout = QPageLayout(QPageSize(QPageSize.A4), QPageLayout.Portrait, QMarginsF(12, 12, 12, 12))
        writer.setPageLayout(layout)
        doc.print_(writer)
        return output_path


def init_technoma_fonts():
    """Registra los archivos TTF de Outfit en la base de datos de fuentes de Qt si están presentes."""
    try:
        from PySide6.QtGui import QFontDatabase
        root_dir = os.path.dirname(os.path.abspath(__file__))
        for font_fn in ["Outfit-Regular.ttf", "Outfit-Bold.ttf", "Outfit-SemiBold.ttf", "Outfit-Medium.ttf"]:
            p = os.path.join(root_dir, font_fn)
            if os.path.exists(p):
                QFontDatabase.addApplicationFont(p)
    except Exception:
        pass


class TechnomaTicketCardWidget(QFrame):
    """
    Widget visual que renderiza la tarjeta del ticket idéntica a la hoja de Excel
    (con logo-technoma.png oficial de la raíz, cabecera roja THN-SOC-XX y fuente Outfit 12pt).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        init_technoma_fonts()
        self.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 2px solid #222222;
                border-radius: 4px;
                font-family: 'Outfit', 'Segoe UI', Arial, sans-serif;
                font-size: 12pt;
            }
        """)
        self._data = {}
        self._init_ui()

    def _set_fallback_logo(self):
        self.lbl_logo.setText(
            "<div style='text-align: center; margin-bottom: 4px;'>"
            "<span style='color: #a81c1c; font-family: Outfit, Segoe UI, sans-serif; font-size: 26px; font-weight: 900; letter-spacing: 2px;'>THN</span><br/>"
            "<span style='color: #222222; font-family: Outfit, Segoe UI, sans-serif; font-size: 13px; font-weight: bold; letter-spacing: 4px;'>TECHNOMA</span>"
            "</div>"
        )

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(0)

        # 1. Header con Logo TECHNOMA oficial desde la raíz del proyecto
        self.lbl_logo = QLabel()
        self.lbl_logo.setAlignment(Qt.AlignCenter)
        self.lbl_logo.setStyleSheet("background-color: #ffffff; padding: 6px 0px 4px 0px; margin: 0px;")

        root_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(root_dir, "logo-technoma.png")
        if not os.path.exists(logo_path):
            logo_path = "logo-technoma.png"

        if os.path.exists(logo_path):
            pix = QPixmap(logo_path)
            if not pix.isNull():
                # Escalar manteniendo proporción para coincidir con la plantilla Excel
                scaled = pix.scaled(130, 95, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.lbl_logo.setPixmap(scaled)
            else:
                self._set_fallback_logo()
        else:
            self._set_fallback_logo()

        layout.addWidget(self.lbl_logo)

        # 2. Barra de Título del Ticket (Rojo THN-SOC-XX en Outfit)
        self.lbl_ticket_header = QLabel("THN-SOC-XX")
        self.lbl_ticket_header.setAlignment(Qt.AlignCenter)
        self.lbl_ticket_header.setStyleSheet(
            "background-color: #f2f2f2; color: #a81c1c; font-family: 'Outfit', sans-serif; "
            "font-size: 14pt; font-weight: 800; border: 1.5px solid #222222; border-bottom: none; padding: 6px;"
        )
        layout.addWidget(self.lbl_ticket_header)

        # 3. Grilla de Campos (Columnas D y E en Outfit 12pt)
        grid_frame = QFrame()
        grid_frame.setStyleSheet("background-color: #ffffff; border: 1.5px solid #222222;")
        self.grid_layout = QGridLayout(grid_frame)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)

        # Filas de la tarjeta
        self.val_labels = {}
        fields = [
            ("Prioridad", "prioridad"),
            ("Asunto", "asunto"),
            ("Descripción", "descripcion"),
            ("Activos", "activos"),
            ("Evidencia", "evidencia"),
            ("Solicitud de Acción", "solicitud_accion")
        ]

        for row, (label_text, key) in enumerate(fields):
            lbl_title = QLabel(label_text)
            lbl_title.setFixedWidth(145)
            lbl_title.setStyleSheet(
                "background-color: #d9d9d9; color: #000000; font-family: 'Outfit', sans-serif; "
                "font-weight: 700; font-size: 12pt; padding: 8px 10px; border-bottom: 1px solid #222222; border-right: 1px solid #222222;"
            )
            lbl_title.setAlignment(Qt.AlignTop | Qt.AlignLeft)

            lbl_val = QLabel()
            lbl_val.setWordWrap(True)
            lbl_val.setStyleSheet(
                "background-color: #ffffff; color: #111111; font-family: 'Outfit', sans-serif; "
                "font-size: 12pt; font-weight: 400; padding: 8px 12px; border-bottom: 1px solid #222222;"
            )
            lbl_val.setTextInteractionFlags(Qt.TextSelectableByMouse)
            lbl_val.setAlignment(Qt.AlignTop | Qt.AlignLeft)

            if key == "evidencia":
                lbl_val.setStyleSheet(
                    "background-color: #ffffff; color: #111111; font-family: 'Outfit', Consolas, monospace; "
                    "font-size: 11pt; padding: 8px 12px; border-bottom: 1px solid #222222;"
                )

            # Quitar borde inferior a la última fila
            if row == len(fields) - 1:
                lbl_title.setStyleSheet(lbl_title.styleSheet().replace("border-bottom: 1px solid #222222;", ""))
                lbl_val.setStyleSheet(lbl_val.styleSheet().replace("border-bottom: 1px solid #222222;", ""))

            self.grid_layout.addWidget(lbl_title, row, 0)
            self.grid_layout.addWidget(lbl_val, row, 1)
            self.val_labels[key] = lbl_val

        layout.addWidget(grid_frame)

    def set_ticket_data(self, data: Dict[str, str]):
        """Actualiza la visualización de la tarjeta con nuevos datos."""
        self._data = data
        t_id = (data.get("ticket_id") or "THN-SOC-XX").upper()
        self.lbl_ticket_header.setText(t_id)

        self.val_labels["prioridad"].setText(data.get("prioridad") or "Media 🟡")
        self.val_labels["asunto"].setText(data.get("asunto") or "")
        self.val_labels["descripcion"].setText(data.get("descripcion") or "")
        self.val_labels["activos"].setText(data.get("activos") or "")
        self.val_labels["evidencia"].setText(data.get("evidencia") or "")
        self.val_labels["solicitud_accion"].setText(data.get("solicitud_accion") or "")

    def render_to_pixmap(self) -> QPixmap:
        """Renderiza este widget directamente a un mapa de bits (QPixmap)."""
        return self.grab()


class TechnomaTicketGeneratorDialog(QDialog):
    """
    Ventana interactiva de Generación y Sincronización de Tickets Technoma SOC
    y Bitácora de 18 Columnas.
    """

    def __init__(self, parent=None, initial_data=None):
        super().__init__(parent)
        self.setWindowTitle("🎫 Generador de Tickets de Escalación Technoma SOC (THN-SOC & Bitácora)")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1150, 800)
        self.setMinimumSize(950, 650)
        self.setStyleSheet("""
            QDialog {
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #cbd5e1;
                font-weight: 500;
            }
            QLineEdit, QTextEdit, QComboBox {
                background-color: #1e293b;
                color: #ffffff;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 6px;
                selection-background-color: #0369a1;
            }
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
                border: 1px solid #38bdf8;
            }
            QPushButton {
                background-color: #1e293b;
                color: #ffffff;
                border: 1px solid #475569;
                border-radius: 4px;
                padding: 7px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #334155;
                border-color: #94a3b8;
            }
        """)

        self._init_ui()

        if initial_data:
            self.load_data(initial_data)
        else:
            self.load_pua_sample()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(10)

        # 1. Barra de Herramientas Superior (Acciones Rápidas)
        top_bar = QFrame()
        top_bar.setStyleSheet("background-color: #1e293b; border-radius: 6px; padding: 4px;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(8, 6, 8, 6)
        top_layout.setSpacing(8)

        lbl_title = QLabel("🛡️ TECHNOMA SOC TICKET ENGINE")
        lbl_title.setStyleSheet("font-size: 13px; font-weight: bold; color: #38bdf8; letter-spacing: 1px;")
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()

        self.btn_paste_excel = QPushButton("📥 Pegar Tarjeta Excel (D:E)")
        self.btn_paste_excel.setStyleSheet("background-color: #0284c7; color: #ffffff;")
        self.btn_paste_excel.setToolTip("Lee el portapapeles y parsea la tarjeta copiada desde las columnas D y E de Excel")
        self.btn_paste_excel.clicked.connect(self.paste_from_excel_card)
        top_layout.addWidget(self.btn_paste_excel)

        self.btn_paste_bitacora = QPushButton("📥 Pegar Fila Bitácora (18 Col)")
        self.btn_paste_bitacora.setStyleSheet("background-color: #0d9488; color: #ffffff;")
        self.btn_paste_bitacora.setToolTip("Lee el portapapeles y extrae los campos de una fila completa de la bitácora")
        self.btn_paste_bitacora.clicked.connect(self.paste_from_bitacora_row)
        top_layout.addWidget(self.btn_paste_bitacora)

        self.btn_sample = QPushButton("✨ Cargar Ejemplo PUA")
        self.btn_sample.clicked.connect(self.load_pua_sample)
        top_layout.addWidget(self.btn_sample)

        self.btn_clear = QPushButton("✕ Limpiar")
        self.btn_clear.clicked.connect(self.clear_fields)
        top_layout.addWidget(self.btn_clear)

        main_layout.addWidget(top_bar)

        # 2. Panel Central Splitter (Izquierda: Formulario | Derecha: Visualizador en Vivo)
        splitter = QSplitter(Qt.Horizontal)

        # --- PANEL IZQUIERDO: FORMULARIO DE ENTRADA ---
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 8, 0)
        left_layout.setSpacing(8)

        scroll_form = QScrollArea()
        scroll_form.setWidgetResizable(True)
        scroll_form.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        form_container = QWidget()
        f_layout = QVBoxLayout(form_container)
        f_layout.setContentsMargins(4, 4, 8, 4)
        f_layout.setSpacing(8)

        # Fila 1: ID Ticket, Prioridad, Tenant
        row1 = QHBoxLayout()
        v_id = QVBoxLayout()
        v_id.addWidget(QLabel("Nro. Ticket (THN-SOC):"))
        self.txt_ticket_id = QLineEdit("THN-SOC-98")
        self.txt_ticket_id.textChanged.connect(self._update_preview)
        v_id.addWidget(self.txt_ticket_id)
        row1.addLayout(v_id, 1)

        v_prio = QVBoxLayout()
        v_prio.addWidget(QLabel("Prioridad:"))
        self.combo_prio = QComboBox()
        self.combo_prio.addItems(["Media 🟡", "Alta 🔴", "Crítica 🟣", "Baja 🟢", "Informativo ℹ️"])
        self.combo_prio.currentTextChanged.connect(self._update_preview)
        v_prio.addWidget(self.combo_prio)
        row1.addLayout(v_prio, 1)

        v_tenant = QVBoxLayout()
        v_tenant.addWidget(QLabel("Cliente / Tenant:"))
        self.txt_tenant = QLineEdit("Caja Ande")
        v_tenant.addWidget(self.txt_tenant)
        row1.addLayout(v_tenant, 1)
        f_layout.addLayout(row1)

        # Fila 2: Asunto
        f_layout.addWidget(QLabel("Asunto del Ticket:"))
        self.txt_asunto = QLineEdit()
        self.txt_asunto.textChanged.connect(self._update_preview)
        f_layout.addWidget(self.txt_asunto)

        # Fila 3: Activos Afectados
        f_layout.addWidget(QLabel("Activos Involucrados (Host / User / IP):"))
        self.txt_activos = QTextEdit()
        self.txt_activos.setFixedHeight(65)
        self.txt_activos.textChanged.connect(self._update_preview)
        f_layout.addWidget(self.txt_activos)

        # Fila 4: Descripción
        f_layout.addWidget(QLabel("Descripción Detallada:"))
        self.txt_descripcion = QTextEdit()
        self.txt_descripcion.setFixedHeight(95)
        self.txt_descripcion.textChanged.connect(self._update_preview)
        f_layout.addWidget(self.txt_descripcion)

        # Fila 5: Evidencia Forense / JSON
        h_evid = QHBoxLayout()
        h_evid.addWidget(QLabel("Evidencia Técnica (Logs / JSON):"))
        h_evid.addStretch()
        btn_format_json = QPushButton("🧹 Auto-Formatear JSON")
        btn_format_json.setFixedHeight(24)
        btn_format_json.setStyleSheet("font-size: 10px; padding: 2px 6px;")
        btn_format_json.clicked.connect(self._auto_format_evidence_json)
        h_evid.addWidget(btn_format_json)
        f_layout.addLayout(h_evid)

        self.txt_evidencia = QTextEdit()
        self.txt_evidencia.setFixedHeight(120)
        self.txt_evidencia.setStyleSheet("font-family: Consolas, monospace; font-size: 11px;")
        self.txt_evidencia.textChanged.connect(self._update_preview)
        f_layout.addWidget(self.txt_evidencia)

        # Fila 6: Solicitud de Acción
        f_layout.addWidget(QLabel("Solicitud de Acción (Instrucción al Cliente/IT):"))
        self.txt_solicitud = QTextEdit()
        self.txt_solicitud.setFixedHeight(65)
        self.txt_solicitud.textChanged.connect(self._update_preview)
        f_layout.addWidget(self.txt_solicitud)

        scroll_form.setWidget(form_container)
        left_layout.addWidget(scroll_form)
        splitter.addWidget(left_widget)

        # --- PANEL DERECHO: VISUALIZACIÓN EN VIVO (TARJETA EXCEL) ---
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(8, 0, 0, 0)
        right_layout.setSpacing(6)

        lbl_prev_title = QLabel("👁️ Vista Previa en Vivo (Tarjeta Technoma SOC - Columnas D y E)")
        lbl_prev_title.setStyleSheet("color: #94a3b8; font-size: 11px; font-weight: bold;")
        right_layout.addWidget(lbl_prev_title)

        scroll_card = QScrollArea()
        scroll_card.setWidgetResizable(True)
        scroll_card.setStyleSheet("QScrollArea { border: 1px solid #334155; background-color: #475569; border-radius: 4px; }")

        card_container = QWidget()
        card_container.setStyleSheet("background-color: #64748b;")
        c_layout = QVBoxLayout(card_container)
        c_layout.setContentsMargins(15, 15, 15, 15)

        self.card_preview = TechnomaTicketCardWidget()
        c_layout.addWidget(self.card_preview)
        c_layout.addStretch()

        scroll_card.setWidget(card_container)
        right_layout.addWidget(scroll_card)
        splitter.addWidget(right_widget)

        splitter.setStretchFactor(0, 5)
        splitter.setStretchFactor(1, 5)
        main_layout.addWidget(splitter, 1)

        # 3. Barra Inferior de Exportación (1-Clic Copy & Export)
        bottom_bar = QFrame()
        bottom_bar.setStyleSheet("background-color: #1e293b; border-radius: 6px; padding: 6px;")
        b_layout = QHBoxLayout(bottom_bar)
        b_layout.setContentsMargins(8, 6, 8, 6)
        b_layout.setSpacing(10)

        lbl_export = QLabel("📋 GENERACIÓN DE SALIDA:")
        lbl_export.setStyleSheet("font-weight: bold; color: #38bdf8;")
        b_layout.addWidget(lbl_export)

        self.btn_copy_excel = QPushButton("📋 Copiar para Excel D:E (Sin Fórmulas)")
        self.btn_copy_excel.setStyleSheet("background-color: #16a34a; color: #ffffff; font-weight: bold; padding: 8px 14px;")
        self.btn_copy_excel.setToolTip("Copia las celdas D y E para pegar con Ctrl+V directamente en Excel, eliminando la necesidad de fórmulas")
        self.btn_copy_excel.clicked.connect(self.copy_to_excel_card)
        b_layout.addWidget(self.btn_copy_excel)

        self.btn_copy_bitacora = QPushButton("📋 Copiar Fila Bitácora (18 Col TSV)")
        self.btn_copy_bitacora.setStyleSheet("background-color: #0284c7; color: #ffffff; font-weight: bold; padding: 8px 14px;")
        self.btn_copy_bitacora.setToolTip("Copia la fila única de 18 columnas para pegarla en la pestaña maestra de la Bitácora")
        self.btn_copy_bitacora.clicked.connect(self.copy_to_bitacora_row)
        b_layout.addWidget(self.btn_copy_bitacora)

        self.btn_copy_md = QPushButton("📝 Copiar Markdown")
        self.btn_copy_md.setToolTip("Copia el ticket en formato Markdown listo para Teams, Slack o correo")
        self.btn_copy_md.clicked.connect(self.copy_to_markdown)
        b_layout.addWidget(self.btn_copy_md)

        self.btn_copy_html = QPushButton("🌐 Copiar HTML")
        self.btn_copy_html.setToolTip("Copia la tarjeta en HTML enriquecido con la fuente Outfit 12pt y el logo oficial")
        self.btn_copy_html.clicked.connect(self.copy_to_html)
        b_layout.addWidget(self.btn_copy_html)

        self.btn_copy_img = QPushButton("🖼️ Copiar Imagen")
        self.btn_copy_img.setStyleSheet("background-color: #9333ea; color: #ffffff;")
        self.btn_copy_img.setToolTip("Copia la tarjeta visual directamente como imagen al portapapeles")
        self.btn_copy_img.clicked.connect(self.copy_as_image)
        b_layout.addWidget(self.btn_copy_img)

        self.btn_save_img = QPushButton("💾 Guardar PNG")
        self.btn_save_img.clicked.connect(self.save_as_image)
        b_layout.addWidget(self.btn_save_img)

        self.btn_export_pdf = QPushButton("📄 Exportar PDF")
        self.btn_export_pdf.setStyleSheet("background-color: #dc2626; color: #ffffff; font-weight: bold; padding: 8px 14px;")
        self.btn_export_pdf.setToolTip("Exporta el ticket formal como documento PDF corporativo con membrete oficial y fuente Outfit")
        self.btn_export_pdf.clicked.connect(self.export_as_pdf)
        b_layout.addWidget(self.btn_export_pdf)

        main_layout.addWidget(bottom_bar)

    def _collect_data(self) -> Dict[str, str]:
        return {
            "ticket_id": self.txt_ticket_id.text().strip(),
            "prioridad": self.combo_prio.currentText(),
            "tenant": self.txt_tenant.text().strip(),
            "asunto": self.txt_asunto.text().strip(),
            "activos": self.txt_activos.toPlainText().strip(),
            "descripcion": self.txt_descripcion.toPlainText().strip(),
            "evidencia": self.txt_evidencia.toPlainText().strip(),
            "solicitud_accion": self.txt_solicitud.toPlainText().strip(),
            "analista": "Kevin Moraes",
            "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def _update_preview(self):
        data = self._collect_data()
        self.card_preview.set_ticket_data(data)

    def load_data(self, data: Dict[str, str]):
        self.txt_ticket_id.setText(data.get("ticket_id") or "THN-SOC-98")
        prio = TechnomaTicketEngine.normalize_priority(data.get("prioridad") or "Media 🟡")
        idx = self.combo_prio.findText(prio)
        if idx >= 0:
            self.combo_prio.setCurrentIndex(idx)
        else:
            self.combo_prio.setCurrentText(prio)

        self.txt_tenant.setText(data.get("tenant") or "Caja Ande")
        self.txt_asunto.setText(data.get("asunto") or "")
        self.txt_activos.setPlainText(data.get("activos") or "")
        self.txt_descripcion.setPlainText(data.get("descripcion") or "")
        self.txt_evidencia.setPlainText(data.get("evidencia") or "")
        self.txt_solicitud.setPlainText(data.get("solicitud_accion") or "")
        self._update_preview()

    def load_pua_sample(self):
        sample = {
            "ticket_id": "THN-SOC-98",
            "prioridad": "Media 🟡",
            "tenant": "Caja Ande",
            "asunto": "MALWARE - Generic Reputation PUA detectado en CJPPA081",
            "descripcion": (
                "Se ha identificado que la amenaza 'Generic Reputation PUA' reside dentro de un contenedor comprimido (.rar) "
                "en la carpeta de descargas del usuario. Debido a que el motor de Sophos no pudo desinfectar o eliminar elementos "
                "dentro de archivos comprimidos protegidos o activos, el estado de la alerta ha cambiado a \"Limpieza manual necesaria\". "
                "El archivo 'C:\\Users\\mkt_sege\\Downloads\\CorelDRAW Graphics Suite 2022 v24.0.0.301.rar' permanece en el sistema."
            ),
            "activos": "Host: CJPPA081\nUser: CAJAANDE\\c3412949\nIP: 172.16.202.111",
            "evidencia": json.dumps({
                "appSha256": "7a8ecd90d68564f855bb96ab10ff3b1c57c50f33a189e900ee106c85e38d2e4b",
                "created_at": "2026-08-31T10:50:28.029Z",
                "customer_id": "37a6c0dc-b2ea-4fda-b641-456560f40ef1",
                "endpoint_id": "bbec545c-b266-4e5c-8f98-c884fdd92da6",
                "endpoint_type": "computer",
                "group": "PUA",
                "id": "dc011e16-cb02-461c-8aaa-7b3c5dba6879",
                "location": "CJPPA081",
                "name": "PUA detected: 'Generic Reputation PUA' at 'C:\\Users\\mkt_sege\\Downloads\\CorelDRAW Graphics Suite 2022 v24.0.0.301.rar'",
                "origin": "ML",
                "severity": "medium",
                "source": "CAJAANDE\\c3412949",
                "source_info": {"ip": "172.16.202.111"},
                "threat": "Generic Reputation PUA",
                "type": "Event::Endpoint::CorePuaDetection",
                "user_id": "6931c69758fc555f47173d20",
                "when": "2026-08-31T10:49:34.938Z"
            }, indent=2),
            "solicitud_accion": "Realizar la eliminación manual del archivo C:\\Users\\mkt_sege\\Downloads\\CorelDRAW Graphics Suite 2022 v24.0.0.301.rar"
        }
        self.load_data(sample)

    def clear_fields(self):
        self.txt_ticket_id.setText("THN-SOC-")
        self.combo_prio.setCurrentIndex(0)
        self.txt_tenant.clear()
        self.txt_asunto.clear()
        self.txt_activos.clear()
        self.txt_descripcion.clear()
        self.txt_evidencia.clear()
        self.txt_solicitud.clear()
        self._update_preview()

    def _auto_format_evidence_json(self):
        raw = self.txt_evidencia.toPlainText().strip()
        if not raw:
            return
        try:
            # Des-escapar comillas dobles repetidas de Excel si las trae
            if '""' in raw:
                raw = raw.replace('""', '"')
            parsed = json.loads(raw)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
            self.txt_evidencia.setPlainText(formatted)
        except Exception as e:
            QMessageBox.information(self, "Formato JSON", f"El contenido no es un JSON puro convertible: {e}")

    # --- ACCIONES DE IMPORTACIÓN ---
    def paste_from_excel_card(self):
        clipboard = QApplication.clipboard().text().strip()
        if not clipboard:
            QMessageBox.warning(self, "Portapapeles Vacío", "No hay texto en el portapapeles para importar.")
            return
        try:
            parsed = TechnomaTicketEngine.parse_excel_ticket_card(clipboard)
            self.load_data(parsed)
            QMessageBox.information(self, "Importación Exitosa", f"Se extrajeron los datos de la tarjeta de ticket ({parsed.get('ticket_id', 'THN-SOC')}).")
        except Exception as e:
            QMessageBox.critical(self, "Error de Importación", f"No se pudo parsear el contenido de Excel: {e}")

    def paste_from_bitacora_row(self):
        clipboard = QApplication.clipboard().text().strip()
        if not clipboard:
            QMessageBox.warning(self, "Portapapeles Vacío", "No hay texto en el portapapeles.")
            return
        try:
            parsed = TechnomaTicketEngine.parse_bitacora_row(clipboard)
            self.load_data(parsed)
            QMessageBox.information(self, "Importación Exitosa", f"Se cargó la fila de bitácora ({parsed.get('ticket_id', 'THN-SOC')}).")
        except Exception as e:
            QMessageBox.critical(self, "Error de Importación", f"No se pudo parsear la fila de la bitácora: {e}")

    # --- ACCIONES DE EXPORTACIÓN ---
    def copy_to_excel_card(self):
        data = self._collect_data()
        tsv = TechnomaTicketEngine.to_excel_ticket_card(data)
        QApplication.clipboard().setText(tsv)
        QMessageBox.information(
            self, "¡Copiado para Excel!",
            "El contenido de la tarjeta (Columnas D y E) fue copiado al portapapeles en formato TSV.\n\n"
            "👉 En Excel: Haz clic en la celda superior izquierda de la tarjeta (ej. celda D4) y presiona Ctrl + V.\n"
            "Cada valor caerá directamente en su celda SIN NECESIDAD DE FÓRMULAS."
        )

    def copy_to_bitacora_row(self):
        data = self._collect_data()
        row = TechnomaTicketEngine.to_bitacora_row(data)
        QApplication.clipboard().setText(row)
        QMessageBox.information(
            self, "¡Fila de Bitácora Copiada!",
            "La fila oficial de 18 columnas fue copiada al portapapeles en formato TSV.\n\n"
            "👉 En la hoja 'Bitácora': Selecciona la celda de Fecha (Columna A) de una fila vacía y presiona Ctrl + V."
        )

    def copy_to_markdown(self):
        data = self._collect_data()
        md = TechnomaTicketEngine.to_markdown_ticket(data)
        QApplication.clipboard().setText(md)
        QMessageBox.information(self, "Markdown Copiado", "Ticket copiado en formato Markdown para Teams, Slack o ITSM.")

    def copy_to_html(self):
        data = self._collect_data()
        html = TechnomaTicketEngine.to_html_ticket(data)
        from PySide6.QtCore import QMimeData
        mime = QMimeData()
        mime.setHtml(html)
        mime.setText(html)
        QApplication.clipboard().setMimeData(mime)
        QMessageBox.information(
            self, "¡HTML Enriquecido Copiado!",
            "La tarjeta del ticket fue copiada en formato HTML enriquecido con la fuente Outfit 12pt y el logo oficial.\n\n"
            "👉 Puedes pegarla con Ctrl + V directamente en un correo de Outlook o documento de Word con formato intacto."
        )

    def copy_as_image(self):
        pixmap = self.card_preview.render_to_pixmap()
        QApplication.clipboard().setPixmap(pixmap)
        QMessageBox.information(
            self, "¡Imagen Copiada!",
            "La imagen de la tarjeta del ticket fue copiada al portapapeles.\n\n"
            "👉 Puedes pegarla directamente con Ctrl + V en Teams, WhatsApp Web o correos de Outlook."
        )

    def save_as_image(self):
        ticket_id = (self.txt_ticket_id.text().strip() or "THN-SOC-TICKET").replace("/", "_")
        path, _ = QFileDialog.getSaveFileName(self, "Guardar Tarjeta de Ticket como Imagen", f"{ticket_id}.png", "Imágenes PNG (*.png)")
        if path:
            pixmap = self.card_preview.render_to_pixmap()
            pixmap.save(path, "PNG")
            QMessageBox.information(self, "Imagen Guardada", f"Tarjeta guardada exitosamente en:\n{path}")

    def export_as_pdf(self):
        ticket_id = (self.txt_ticket_id.text().strip() or "THN-SOC-TICKET").replace("/", "_")
        path, _ = QFileDialog.getSaveFileName(self, "Exportar Ticket como PDF", f"{ticket_id}.pdf", "Archivos PDF (*.pdf)")
        if path:
            try:
                data = self._collect_data()
                TechnomaTicketEngine.export_to_pdf(data, path)
                QMessageBox.information(self, "PDF Generado", f"El ticket formal fue exportado exitosamente a PDF:\n\n{path}")
            except Exception as e:
                QMessageBox.critical(self, "Error al Exportar PDF", f"No se pudo generar el archivo PDF: {e}")


# =============================================================================
# EJECUCIÓN STANDALONE
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = TechnomaTicketGeneratorDialog()
    dlg.show()
    sys.exit(app.exec())
