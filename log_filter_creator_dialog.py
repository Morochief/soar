#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
TECHNOMA SOC — CREADOR Y GESTOR DE LOG FILTERS QUIRÚRGICOS (STELLAR CYBER API)
=============================================================================
Diálogo interactivo para diseñar, previsualizar sintaxis y crear Log Filters
en Stellar Cyber directamente vía API REST oficial sin ceguera operativa.
"""

import os
import sys
import json
from typing import Dict, Any, List, Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QComboBox, QTextEdit,
    QMessageBox, QFrame, QSplitter, QScrollArea, QTabWidget,
    QGroupBox, QFormLayout
)

import ui_theme
from stellar_log_filter_manager import StellarLogFilterManager


class LogFilterCreatorDialog(QDialog):
    filter_created_signal = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🛡️ Creador de Log Filters Quirúrgicos — Stellar Cyber OpenXDR")
        self.resize(980, 680)
        self.mgr = StellarLogFilterManager()

        self._setup_ui()
        self._update_json_preview()

    def _setup_ui(self):
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {ui_theme.BG_PRIMARY};
                color: {ui_theme.TEXT_PRIMARY};
            }}
            QGroupBox {{
                background-color: {ui_theme.BG_SURFACE};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
                font-family: 'Consolas', monospace;
                font-weight: bold;
                color: {ui_theme.ACCENT_CYBER};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }}
            QLineEdit, QComboBox, QTextEdit {{
                background-color: {ui_theme.BG_INPUT};
                color: {ui_theme.TEXT_PRIMARY};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-radius: 4px;
                padding: 6px 8px;
                font-family: 'Consolas', monospace;
                font-size: 11px;
            }}
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {{
                border: 1px solid {ui_theme.ACCENT_CYBER};
            }}
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(14, 14, 14, 14)
        main_layout.setSpacing(10)

        # Header Card
        header_frame = QFrame()
        header_frame.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0f172a, stop:1 #1e1b4b);
            border: 1px solid {ui_theme.BORDER_SUBTLE};
            border-left: 4px solid {ui_theme.ACCENT_CYBER};
            border-radius: 6px;
            padding: 8px 12px;
        """)
        h_layout = QHBoxLayout(header_frame)
        h_layout.setContentsMargins(0, 0, 0, 0)
        
        lbl_title = QLabel("⚙️ GESTOR DE LOG FILTERS API — STELLAR CYBER OPENXDR")
        lbl_title.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 13px; font-weight: bold; font-family: 'Consolas';")
        h_layout.addWidget(lbl_title)
        h_layout.addStretch()

        lbl_tenant = QLabel(f"Tenant Cust ID: <code>{self.mgr.cust_id[:8]}...</code> | Host: <code>{self.mgr.host}</code>")
        lbl_tenant.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px; font-family: 'Consolas';")
        h_layout.addWidget(lbl_tenant)
        main_layout.addWidget(header_frame)

        # Tabs: Crear Nuevo Filtro vs Añadir IPs a Filtro Existente
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{ border: 1px solid {ui_theme.BORDER_SUBTLE}; background-color: {ui_theme.BG_SURFACE}; border-radius: 4px; }}
            QTabBar::tab {{ background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_MUTED}; padding: 6px 14px; font-size: 11px; font-weight: bold; }}
            QTabBar::tab:selected {{ background-color: #0284c7; color: #ffffff; border-bottom: 2px solid {ui_theme.ACCENT_CYBER}; }}
        """)

        tab_crear = QWidget()
        self._setup_tab_crear(tab_crear)
        self.tabs.addTab(tab_crear, "➕ Diseñar & Desplegar Nuevo Log Filter")

        tab_append = QWidget()
        self._setup_tab_append(tab_append)
        self.tabs.addTab(tab_append, "🌐 Ampliar Filtro Existente (Añadir IPs/Subredes)")

        main_layout.addWidget(self.tabs, 1)

    def _setup_tab_crear(self, parent: QWidget):
        layout = QHBoxLayout(parent)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(12)

        # Panel Izquierdo: Formulario de Parámetros
        left_pane = QWidget()
        form_layout = QVBoxLayout(left_pane)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(8)

        # Grupo 1: Identificación y Dispositivo
        grp_meta = QGroupBox("1. Identificación del Filtro")
        f_meta = QFormLayout(grp_meta)
        f_meta.setContentsMargins(8, 12, 8, 8)
        f_meta.setSpacing(6)

        self.txt_name = QLineEdit()
        self.txt_name.setPlaceholderText("Ej: Drop_FW_Passthrough_Benign_Telemetry")
        self.txt_name.textChanged.connect(self._update_json_preview)
        f_meta.addRow("Nombre del Filtro:", self.txt_name)

        self.cmb_dev_type = QComboBox()
        self.cmb_dev_type.addItem("Fortinet FortiGate (fw_fortigate)", "fw_fortigate")
        self.cmb_dev_type.addItem("Syslog Genérico (syslog)", "syslog")
        self.cmb_dev_type.addItem("Palo Alto Networks FW (fw_paloalto)", "fw_paloalto")
        self.cmb_dev_type.addItem("Windows Event Log (windows)", "windows")
        self.cmb_dev_type.currentIndexChanged.connect(self._update_json_preview)
        f_meta.addRow("Dispositivo:", self.cmb_dev_type)

        self.cmb_action = QComboBox()
        self.cmb_action.addItems(["passthrough", "deny", "accept", "drop", "close"])
        self.cmb_action.currentIndexChanged.connect(self._update_json_preview)
        f_meta.addRow("Acción Firewall / Log:", self.cmb_action)

        form_layout.addWidget(grp_meta)

        # Grupo 2: Dimensiones Quirúrgicas de Red
        grp_net = QGroupBox("2. Dimensiones de Red (Quirúrgico)")
        f_net = QFormLayout(grp_net)
        f_net.setContentsMargins(8, 12, 8, 8)
        f_net.setSpacing(6)

        self.txt_srcip = QLineEdit()
        self.txt_srcip.setPlaceholderText("Ej: 192.168.169.0/24, 192.168.100.0/24 (opcional)")
        self.txt_srcip.textChanged.connect(self._update_json_preview)
        f_net.addRow("IP/Subred Origen (srcip):", self.txt_srcip)

        self.txt_dstip = QLineEdit()
        self.txt_dstip.setPlaceholderText("Ej: 142.251.0.0/16, 20.0.0.0/11, 190.104.187.132")
        self.txt_dstip.textChanged.connect(self._update_json_preview)
        f_net.addRow("IP/Subred Destino (dstip):", self.txt_dstip)

        self.txt_dstport = QLineEdit()
        self.txt_dstport.setPlaceholderText("Ej: 443, 53, 7680 (vacío = cualquiera)")
        self.txt_dstport.textChanged.connect(self._update_json_preview)
        f_net.addRow("Puerto Destino (dstport):", self.txt_dstport)

        self.cmb_proto = QComboBox()
        self.cmb_proto.addItem("Cualquiera / No restringir", "")
        self.cmb_proto.addItem("TCP (6)", "6")
        self.cmb_proto.addItem("UDP (17)", "17")
        self.cmb_proto.addItem("ICMP (1)", "1")
        self.cmb_proto.currentIndexChanged.connect(self._update_json_preview)
        f_net.addRow("Protocolo IANA (proto):", self.cmb_proto)

        self.txt_appid = QLineEdit()
        self.txt_appid.setPlaceholderText("Ej: PING, SSL/TLS, Google.Services (opcional)")
        self.txt_appid.textChanged.connect(self._update_json_preview)
        f_net.addRow("Aplicación L7 (appid_name):", self.txt_appid)

        form_layout.addWidget(grp_net)
        form_layout.addStretch()

        # Botón de Creación
        self.btn_crear = QPushButton("🚀 Enviar y Desplegar Filtro en Stellar Cyber (API)")
        self.btn_crear.setStyleSheet("""
            QPushButton {
                background-color: #0284c7;
                color: #ffffff;
                font-family: 'Consolas';
                font-weight: bold;
                font-size: 12px;
                padding: 10px;
                border: 1px solid #38bdf8;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0369a1;
            }
            QPushButton:disabled {
                background-color: #334155;
                color: #94a3b8;
                border-color: #475569;
            }
        """)
        self.btn_crear.clicked.connect(self._on_deploy_filter)
        form_layout.addWidget(self.btn_crear)

        layout.addWidget(left_pane, 5)

        # Panel Derecho: Previsualizador y Validador de Ceguera
        right_pane = QWidget()
        right_layout = QVBoxLayout(right_pane)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(8)

        lbl_prev_title = QLabel("💻 PAYLOAD JSON EN TIEMPO REAL (API STELLAR CYBER):")
        lbl_prev_title.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 11px; font-weight: bold; font-family: 'Consolas';")
        right_layout.addWidget(lbl_prev_title)

        self.txt_json_preview = QTextEdit()
        self.txt_json_preview.setReadOnly(True)
        self.txt_json_preview.setStyleSheet(f"""
            background-color: {ui_theme.BG_INPUT};
            color: #38bdf8;
            font-family: 'Consolas', monospace;
            font-size: 11px;
            border: 1px solid {ui_theme.BORDER_MUTED};
        """)
        right_layout.addWidget(self.txt_json_preview, 1)

        # Indicador de Ceguera Operativa
        self.lbl_blind_indicator = QLabel("Evaluando ceguera operativa...")
        self.lbl_blind_indicator.setWordWrap(True)
        self.lbl_blind_indicator.setStyleSheet(f"""
            background-color: {ui_theme.BG_SURFACE};
            border: 1px solid {ui_theme.BORDER_MUTED};
            border-radius: 4px;
            padding: 8px 10px;
            font-size: 11px;
        """)
        right_layout.addWidget(self.lbl_blind_indicator)

        layout.addWidget(right_pane, 5)

    def _setup_tab_append(self, parent: QWidget):
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        lbl_info = QLabel("Seleccione un filtro existente para agregar quirúrgicamente nuevas IPs o subredes autorizadas sin sobreescribir las reglas preexistentes:")
        lbl_info.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 11px;")
        layout.addWidget(lbl_info)

        # Selector de filtro existente
        f_box = QHBoxLayout()
        f_box.addWidget(QLabel("Filtro Destino:"))
        self.cmb_existing_filters = QComboBox()
        self.cmb_existing_filters.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_PRIMARY}; font-family: 'Consolas'; font-size: 11px;")
        f_box.addWidget(self.cmb_existing_filters, 1)
        
        self.btn_refresh_list = QPushButton("🔄 Recargar Filtros")
        self.btn_refresh_list.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_refresh_list.clicked.connect(self._load_existing_filters)
        f_box.addWidget(self.btn_refresh_list)
        layout.addLayout(f_box)

        layout.addWidget(QLabel("Nuevas IPs o CIDRs a incorporar (separadas por coma o espacio):"))
        self.txt_append_ips = QTextEdit()
        self.txt_append_ips.setPlaceholderText("Ej:\n190.104.187.132\n142.251.0.0/16\n20.0.0.0/11")
        self.txt_append_ips.setMaximumHeight(150)
        layout.addWidget(self.txt_append_ips)

        self.btn_append_exec = QPushButton("⚡ Actualizar Filtro con Nuevas IPs en Producción")
        self.btn_append_exec.setStyleSheet("""
            QPushButton {
                background-color: #10b981;
                color: #ffffff;
                font-family: 'Consolas';
                font-weight: bold;
                font-size: 12px;
                padding: 10px;
                border: 1px solid #059669;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #059669;
            }
        """)
        self.btn_append_exec.clicked.connect(self._on_append_ips)
        layout.addWidget(self.btn_append_exec)
        layout.addStretch()

        self._load_existing_filters()

    def _load_existing_filters(self):
        try:
            self.cmb_existing_filters.clear()
            filters = self.mgr.list_filters()
            for f in filters:
                fid = f.get("_id")
                name = f.get("name")
                self.cmb_existing_filters.addItem(f"[{fid[:8]}] {name}", fid)
        except Exception as e:
            self.cmb_existing_filters.addItem(f"Error cargando filtros: {e}", "")

    def _build_rules_payload(self) -> Dict[str, Any]:
        rules = {}
        action_val = self.cmb_action.currentText().strip()
        if action_val:
            rules["action"] = {"type": "string", "op": "==", "value": [action_val]}

        # srcip
        raw_src = self.txt_srcip.text().strip()
        if raw_src:
            src_list = [x.strip() for x in raw_src.replace(" ", ",").split(",") if x.strip()]
            if src_list:
                rules["srcip"] = {"type": "ip", "op": "matches", "value": src_list}

        # dstip
        raw_dst = self.txt_dstip.text().strip()
        if raw_dst:
            dst_list = [x.strip() for x in raw_dst.replace(" ", ",").split(",") if x.strip()]
            if dst_list:
                rules["dstip"] = {"type": "ip", "op": "matches", "value": dst_list}

        # dstport
        raw_port = self.txt_dstport.text().strip()
        if raw_port:
            try:
                p_num = int(raw_port)
                rules["dstport"] = {"type": "number", "op": "==", "value": [p_num]}
            except ValueError:
                pass

        # proto
        proto_data = self.cmb_proto.currentData()
        if proto_data:
            try:
                proto_num = int(proto_data)
                rules["proto"] = {"type": "number", "op": "==", "value": [proto_num]}
            except ValueError:
                pass

        # appid_name
        raw_app = self.txt_appid.text().strip()
        if raw_app:
            rules["appid_name"] = {"type": "string", "op": "==", "value": [raw_app]}

        dev_type = self.cmb_dev_type.currentData()
        dev_label = self.cmb_dev_type.currentText().split("(")[0].strip()

        content = {
            "dev_type": dev_type,
            "dev_type_label": dev_label,
            "rules": rules
        }

        full_payload = {
            "name": self.txt_name.text().strip() or "Nuevo_Log_Filter",
            "cust_id": self.mgr.cust_id,
            "content": json.dumps(content, indent=2)
        }
        return full_payload

    def _update_json_preview(self):
        payload = self._build_rules_payload()
        try:
            content_dict = json.loads(payload["content"])
            rules = content_dict.get("rules", {})
            pretty_dict = {
                "name": payload["name"],
                "cust_id": payload["cust_id"],
                "dev_type": content_dict.get("dev_type"),
                "rules": rules
            }
            self.txt_json_preview.setText(json.dumps(pretty_dict, indent=2))
        except Exception:
            self.txt_json_preview.setText(json.dumps(payload, indent=2))

        # Evaluación de Ceguera
        dimensions = 0
        if "action" in rules: dimensions += 1
        if "dstip" in rules: dimensions += 1
        if "srcip" in rules: dimensions += 1
        if "dstport" in rules: dimensions += 1
        if "proto" in rules: dimensions += 1
        if "appid_name" in rules: dimensions += 1

        action_name = rules.get("action", {}).get("value", [""])[0]

        if not payload["name"] or payload["name"] == "Nuevo_Log_Filter":
            self.lbl_blind_indicator.setText("ℹ️ Ingrese un nombre descriptivo para el filtro (ej. Drop_FW_...).")
            self.lbl_blind_indicator.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_MUTED}; border-left: 4px solid {ui_theme.BORDER_MUTED}; padding: 6px;")
        elif action_name in ["drop", "deny", "passthrough"] and dimensions < 2:
            self.lbl_blind_indicator.setText("⚠️ RIESGO DE CEGUERA: Filtro con menos de 2 dimensiones. No filtre todo el tráfico de forma genérica.")
            self.lbl_blind_indicator.setStyleSheet("background-color: #451a1a; color: #f87171; border-left: 4px solid #ef4444; padding: 6px; font-weight: bold;")
        elif dimensions >= 3:
            self.lbl_blind_indicator.setText(f"✅ REGLA QUIRÚRGICA ({dimensions} Dimensiones): Cero ceguera. Solo descarta el tráfico benigno estrictamente acotado.")
            self.lbl_blind_indicator.setStyleSheet("background-color: #064e3b; color: #34d399; border-left: 4px solid #10b981; padding: 6px; font-weight: bold;")
        else:
            self.lbl_blind_indicator.setText(f"🟡 FILTRO EN CONSTRUCCIÓN ({dimensions} Dimensiones definidas).")
            self.lbl_blind_indicator.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; color: #fbbf24; border-left: 4px solid #f59e0b; padding: 6px;")

    def _on_deploy_filter(self):
        name = self.txt_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Validación", "Por favor ingrese un nombre descriptivo para el filtro.")
            return

        payload = self._build_rules_payload()
        content_dict = json.loads(payload["content"])
        rules = content_dict.get("rules", {})
        if not rules:
            QMessageBox.warning(self, "Validación", "Debe configurar al menos una condición en las reglas del filtro.")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar Despliegue API",
            f"¿Está seguro de enviar y desplegar el Log Filter en Stellar Cyber?\n\n"
            f"• Nombre: {name}\n"
            f"• Dispositivo: {content_dict.get('dev_type')}\n"
            f"• Condiciones: {len(rules)} reglas aplicadas\n\n"
            f"El filtro se activará inmediatamente en el pipeline de ingesta.",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        try:
            res = self.mgr.create_filter(
                name=name,
                rules_dict=rules,
                dev_type=content_dict.get("dev_type", "fw_fortigate"),
                dev_type_label=content_dict.get("dev_type_label", "Fortinet FortiGate")
            )
            created_id = res.get("_id") or res.get("id", "OK")
            QMessageBox.information(
                self,
                "Filtro Desplegado con Éxito",
                f"✅ El Log Filter fue creado exitosamente en Stellar Cyber.\n\n"
                f"ID del Filtro: {created_id}\n"
                f"Nombre: {name}\n\n"
                f"La cuota de ingesta y los eventos en Data Lake ya están protegidos por este filtro."
            )
            self.filter_created_signal.emit(res)
            self._load_existing_filters()
        except Exception as e:
            QMessageBox.critical(self, "Error API", f"Fallo al desplegar el filtro en Stellar Cyber:\n\n{e}")

    def _on_append_ips(self):
        filter_id = self.cmb_existing_filters.currentData()
        if not filter_id:
            QMessageBox.warning(self, "Validación", "Seleccione un filtro existente de la lista.")
            return

        raw_ips = self.txt_append_ips.toPlainText().strip()
        if not raw_ips:
            QMessageBox.warning(self, "Validación", "Ingrese las IPs o subredes que desea incorporar al filtro.")
            return

        ip_list = [x.strip() for x in raw_ips.replace("\n", ",").replace(" ", ",").split(",") if x.strip()]
        if not ip_list:
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar Incorporación de IPs",
            f"¿Desea agregar {len(ip_list)} IPs/subredes al filtro seleccionado?\n\n"
            f"Filtro ID: {filter_id}\n"
            f"IPs a añadir: {', '.join(ip_list[:5])}{'...' if len(ip_list) > 5 else ''}",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        try:
            res = self.mgr.add_ips_to_filter(filter_id, ip_list)
            QMessageBox.information(
                self,
                "Filtro Actualizado",
                f"✅ Se agregaron exitosamente {len(ip_list)} IPs al filtro '{res.get('name')}'.\n\n"
                f"Total de IPs ahora en el filtro: {res.get('total_ips')}"
            )
            self.txt_append_ips.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error API", f"Fallo al actualizar el filtro:\n\n{e}")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = LogFilterCreatorDialog()
    dlg.show()
    sys.exit(app.exec())
