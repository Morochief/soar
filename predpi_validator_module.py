#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STELLAR CYBER - PRE-DPI BPF SYNTAX & LOGIC VALIDATOR MODULE
Analizador Sintáctico BPF Atómico, Verificador de Compatibilidad Libpcap,
Optimizador de Reglas Elegantes (1-Línea) y Soporte Opcional de Auditoría con IA (Gemini).
"""

import re
from typing import Dict, List, Tuple, Any, Optional
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, 
    QPushButton, QFrame, QSplitter, QTableWidget, QTableWidgetItem, 
    QHeaderView, QMessageBox, QTabWidget
)

# Palabras clave y esquemas de pcap-filter y Stellar Cyber
DIRECTIONS = {'src', 'dst', 'src and dst', 'src or dst'}
TYPES = {'host', 'net', 'port', 'portrange'}
PROTOCOLS = {'ip', 'ip6', 'arp', 'rarp', 'tcp', 'udp', 'icmp', 'icmp6', 'vlan'}
LOGICAL_OPS = {'and', 'or', 'not', '&&', '||', '!'}

IP_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
CIDR_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/(?:[0-9]|[1-2][0-9]|3[0-2])$')


def audit_single_rule(rule: str) -> Dict[str, Any]:
    """
    Audita una regla individual de Pre-DPI.
    Aplica el estandar atomico libpcap / pcap_compile(3PCAP).
    """
    rule_clean = rule.strip()
    if not rule_clean or rule_clean.startswith('#'):
        return {"status": "SKIPPED", "original": rule_clean, "errors": [], "warnings": [], "fixed": rule_clean, "sem": None}

    errors = []
    warnings = []
    normalized = rule_clean

    # 1. Comprobar mayusculas en operadores logicos (Stellar exige minusculas estrictas)
    for op_upper in ['AND', 'OR', 'NOT']:
        if re.search(r'\b' + op_upper + r'\b', rule_clean):
            errors.append(f"Operador en mayusculas '{op_upper}'. Stellar Cyber exige '{op_upper.lower()}'.")

    normalized = re.sub(r'\bAND\b', 'and', normalized)
    normalized = re.sub(r'\bOR\b', 'or', normalized)
    normalized = re.sub(r'\bNOT\b', 'not', normalized)

    # 2. Deteccion de error clasico: 'tcp <puerto>' o 'udp <puerto>' sin 'port'
    tcp_udp_port_match = re.search(r'\b(tcp|udp)\s+(\d+)\b', normalized)
    if tcp_udp_port_match:
        proto, port_num = tcp_udp_port_match.groups()
        errors.append(f"Falta calificador 'port' en '{proto} {port_num}'. Debe ser '{proto} port {port_num}'.")
        normalized = re.sub(r'\b(tcp|udp)\s+(\d+)\b', r'\1 port \2', normalized)

    # 3. Deteccion de 'dst <IP>' o 'src <IP>' sin 'host'
    dst_src_no_host = re.findall(r'\b(src|dst)\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\b', normalized)
    for dir_kw, ip_val in dst_src_no_host:
        errors.append(f"Falta calificador 'host' tras '{dir_kw} {ip_val}'. Debe ser '{dir_kw} host {ip_val}'.")
        normalized = re.sub(r'\b' + dir_kw + r'\s+' + re.escape(ip_val) + r'\b', f'{dir_kw} host {ip_val}', normalized)

    # 4. Deteccion de 'dst <CIDR>' o 'src <CIDR>' sin 'net'
    dst_src_no_net = re.findall(r'\b(src|dst)\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3}\/\d+)\b', normalized)
    for dir_kw, cidr_val in dst_src_no_net:
        errors.append(f"Falta calificador 'net' tras '{dir_kw} {cidr_val}'. Debe ser '{dir_kw} net {cidr_val}'.")
        normalized = re.sub(r'\b' + dir_kw + r'\s+' + re.escape(cidr_val) + r'\b', f'{dir_kw} net {cidr_val}', normalized)

    # 5. Deteccion y soporte canonico de 'host A and host B'
    host_pair_match = re.search(r'\bhost\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+and\s+host\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\b', normalized)
    if host_pair_match:
        ip1, ip2 = host_pair_match.groups()
        if ip1 == ip2:
            errors.append(f"Contradiccion 'host {ip1} and host {ip2}': la misma IP no puede ser origen y destino. Usar 'host {ip1}'.")

    # 6. Deteccion de 'vlan and host' sin ID de VLAN
    if re.search(r'\bvlan\s+and\b', normalized):
        errors.append("Palabra 'vlan' sin numero ID seguida de 'and'. En libpcap 'vlan' desplaza los offsets y requiere ID (ej: 'vlan 1101 and ...').")

    # Analisis semantico para optimizacion
    sem = None
    m_canon = re.search(r'\bhost\s+(\S+)\s+and\s+host\s+(\S+)(?:\s+and\s+(?:(?:tcp\s+|udp\s+)?port\s+(\d+)|port\s+(\d+)))?\b', normalized)
    m_pair = re.search(r'\bsrc\s+host\s+(\S+)\s+and\s+dst\s+host\s+(\S+)(?:\s+and\s+(?:(?:src\s+|dst\s+)?port\s+(\d+)|port\s+(\d+)))?\b', normalized)
    m_hp_q = re.search(r'\bsrc\s+host\s+(\S+)\s+and\s+dst\s+port\s+(\d+)\b', normalized)
    m_hp_r1 = re.search(r'\bsrc\s+port\s+(\d+)\s+and\s+dst\s+host\s+(\S+)\b', normalized)
    m_hp_r2 = re.search(r'\bdst\s+host\s+(\S+)\s+and\s+src\s+port\s+(\d+)\b', normalized)

    if m_canon:
        h1, h2, p1, p2 = m_canon.groups()
        sem = ("canonical", h1, h2, p1 or p2)
    elif m_pair:
        s, d, p1, p2 = m_pair.groups()
        sem = ("dir_pair", s, d, p1 or p2)
    elif m_hp_q:
        h, p = m_hp_q.groups()
        sem = ("hp_query", h, p)
    elif m_hp_r1:
        p, h = m_hp_r1.groups()
        sem = ("hp_resp", h, p)
    elif m_hp_r2:
        h, p = m_hp_r2.groups()
        sem = ("hp_resp", h, p)

    status = "ERROR" if errors else ("WARNING" if warnings else "VALID")
    return {
        "status": status,
        "original": rule_clean,
        "errors": errors,
        "warnings": warnings,
        "fixed": normalized,
        "sem": sem
    }


def audit_rule_batch(rules_text: str) -> Tuple[List[Dict[str, Any]], List[str], List[str]]:
    """
    Audita un lote completo de reglas Pre-DPI.
    Detecta pares bidireccionales cruzados y genera tanto la lista saneada
    estándar como la lista optimizada con formato elegante de 1 sola línea.
    """
    lines = [l.strip() for l in rules_text.splitlines() if l.strip()]
    parsed_items = [audit_single_rule(l) for l in lines]

    paired_indices = set()
    consolidated_rules = []

    for i in range(len(parsed_items)):
        if i in paired_indices:
            continue
        item_a = parsed_items[i]
        sem_a = item_a.get("sem")

        if not sem_a or item_a["status"] == "ERROR":
            consolidated_rules.append(item_a["fixed"])
            continue

        if sem_a[0] == "canonical":
            h1, h2, port = sem_a[1], sem_a[2], sem_a[3]
            port_str = f" and port {port}" if port else ""
            item_a["status"] = "OPTIMAL"
            item_a["elegant_tip"] = f"✨ Sintaxis Canónica Óptima: Libpcap evalúa esto como tráfico bidireccional entre {h1} y {h2}{port_str} en 1 sola línea."
            consolidated_rules.append(item_a["fixed"])
            continue

        matched_j = None
        elegant_rule = None

        if sem_a[0] == "dir_pair":
            s_a, d_a, p_a = sem_a[1], sem_a[2], sem_a[3]
            for j in range(i + 1, len(parsed_items)):
                if j in paired_indices:
                    continue
                item_b = parsed_items[j]
                sem_b = item_b.get("sem")
                if sem_b and sem_b[0] == "dir_pair":
                    s_b, d_b, p_b = sem_b[1], sem_b[2], sem_b[3]
                    if s_a == d_b and d_a == s_b and p_a == p_b:
                        matched_j = j
                        port_str = f" and port {p_a}" if p_a else ""
                        elegant_rule = f"host {s_a} and host {d_a}{port_str}"
                        break

        elif sem_a[0] == "hp_query":
            h_a, p_a = sem_a[1], sem_a[2]
            for j in range(i + 1, len(parsed_items)):
                if j in paired_indices:
                    continue
                item_b = parsed_items[j]
                sem_b = item_b.get("sem")
                if sem_b and sem_b[0] == "hp_resp":
                    h_b, p_b = sem_b[1], sem_b[2]
                    if h_a == h_b and p_a == p_b:
                        matched_j = j
                        elegant_rule = f"host {h_a} and port {p_a}"
                        break

        if matched_j is not None:
            paired_indices.add(i)
            paired_indices.add(matched_j)
            item_b = parsed_items[matched_j]
            tip = f"✅ Par bidireccional detectado. 💡 Sugerencia Elegante (1 sola línea): '{elegant_rule}'"
            item_a["status"] = "VALID"
            item_b["status"] = "VALID"
            item_a["warnings"] = []
            item_b["warnings"] = []
            item_a["elegant_tip"] = tip
            item_b["elegant_tip"] = tip
            consolidated_rules.append(elegant_rule)
        else:
            if 'port 53' in item_a["fixed"] and sem_a[0] in ("hp_query", "hp_resp", "dir_pair"):
                item_a["warnings"].append("Regla de DNS unidireccional sin par de respuesta. Se recomienda completar el par o usar 'host X and port 53'.")
                item_a["status"] = "WARNING"
            consolidated_rules.append(item_a["fixed"])

    # Deduplicar preservando orden
    seen = set()
    unique_consolidated = []
    for r in consolidated_rules:
        if r not in seen:
            seen.add(r)
            unique_consolidated.append(r)

    standard_fixed = [item["fixed"] for item in parsed_items]
    return parsed_items, standard_fixed, unique_consolidated


class AiAdvisorWorker(QThread):
    """Hilo de analisis opcional con IA (Gemini) para auditoria heuristica."""
    finished_ai = Signal(str)
    error_ai = Signal(str)

    def __init__(self, rules_text: str):
        super().__init__()
        self.rules_text = rules_text

    def run(self):
        try:
            from stellar_gemini_orchestrator import StellarGeminiOrchestrator
            orchestrator = StellarGeminiOrchestrator()
            
            prompt = (
                "Actua como Ingeniero Senior de Redes y Experto en eBPF / Libpcap para Stellar Cyber OpenXDR. "
                "Audita la siguiente lista de reglas Pre-DPI configuradas con accion 'Drop'. "
                "Evalua: 1) Si alguna regla provocara fallo en pcap_compile() (PCAP_ERROR); "
                "2) Si hay riesgos de ceguera en el SOC; "
                "3) Oportunidades de consolidacion en expresiones canónicas elegantes de 1 sola línea ('host A and host B and port P').\n\n"
                f"Reglas a auditar:\n{self.rules_text}\n\n"
                "Entrega un dictamen tecnico quirurgico, breve, sin introducciones vacias, con viñetas claras."
            )
            respuesta = orchestrator.enviar_a_gemini(prompt)
            self.finished_ai.emit(respuesta)
        except Exception as e:
            self.error_ai.emit(str(e))


class PreDpiValidatorWidget(QWidget):
    """Widget de Interfaz Grafica para Validacion y Optimizacion de Reglas Pre-DPI."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._ai_worker = None
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)

        # Header
        header_frame = QFrame()
        header_frame.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 8px; padding: 10px;")
        layout_header = QHBoxLayout(header_frame)
        layout_header.setContentsMargins(8, 6, 8, 6)

        lbl_title = QLabel("🛡️ AUDITOR Y OPTIMIZADOR DE REGLAS PRE-DPI (BPF / LIBPCAP)")
        lbl_title.setStyleSheet("color: #38bdf8; font-family: 'Consolas'; font-size: 14px; font-weight: bold;")
        layout_header.addWidget(lbl_title)
        layout_header.addStretch()

        self.lbl_stats = QLabel("Reglas: 0 | Validas: 0 | Optimizadas: 0 | Errores: 0")
        self.lbl_stats.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 12px; font-weight: bold;")
        layout_header.addWidget(self.lbl_stats)

        layout.addWidget(header_frame)

        # Splitter Central
        splitter = QSplitter(Qt.Horizontal)

        # Panel Izquierdo: Entrada
        frame_left = QFrame()
        frame_left.setStyleSheet("background-color: #0f172a; border: 1px solid #1e293b; border-radius: 6px;")
        layout_left = QVBoxLayout(frame_left)
        layout_left.setContentsMargins(10, 10, 10, 10)
        layout_left.setSpacing(8)

        lbl_in = QLabel("📋 Reglas Pre-DPI a Evaluar (Una regla por linea):")
        lbl_in.setStyleSheet("color: #cbd5e1; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_left.addWidget(lbl_in)

        self.txt_rules_input = QTextEdit()
        self.txt_rules_input.setStyleSheet(
            "background-color: #020617; color: #f8fafc; font-family: 'Consolas', monospace; "
            "font-size: 12px; border: 1px solid #334155; border-radius: 4px; padding: 8px;"
        )
        self.txt_rules_input.setPlaceholderText(
            "Pegue aqui las expresiones tal como estan en Stellar Cyber. Ejemplos:\n\n"
            "host 10.11.1.1 and host 10.11.1.2 and port 53\n"
            "src host 10.11.1.1 and dst host 10.11.1.2 and port 53\n"
            "src host 10.11.1.2 and dst host 10.11.1.1 and port 53\n"
            "src host 192.168.15.23 and dst port 53\n"
            "src port 53 and dst host 192.168.15.23"
        )
        layout_left.addWidget(self.txt_rules_input)

        # Botones de Accion
        layout_btn_left = QHBoxLayout()
        self.btn_validate = QPushButton("⚡ Validar y Optimizar (Local)")
        self.btn_validate.setStyleSheet(
            "background-color: #0284c7; color: white; font-weight: bold; font-family: 'Consolas'; "
            "padding: 8px 14px; border-radius: 4px; border: none;"
        )
        self.btn_validate.clicked.connect(self.run_local_validation)
        layout_btn_left.addWidget(self.btn_validate)

        self.btn_ai_audit = QPushButton("🤖 Auditoria con IA (Opcional)")
        self.btn_ai_audit.setStyleSheet(
            "background-color: #7c3aed; color: white; font-weight: bold; font-family: 'Consolas'; "
            "padding: 8px 14px; border-radius: 4px; border: none;"
        )
        self.btn_ai_audit.clicked.connect(self.run_ai_audit)
        layout_btn_left.addWidget(self.btn_ai_audit)

        self.btn_clear = QPushButton("🗑️ Limpiar")
        self.btn_clear.setStyleSheet(
            "background-color: #334155; color: #cbd5e1; font-weight: bold; font-family: 'Consolas'; "
            "padding: 8px 12px; border-radius: 4px; border: none;"
        )
        self.btn_clear.clicked.connect(self.clear_all)
        layout_btn_left.addWidget(self.btn_clear)

        layout_left.addLayout(layout_btn_left)
        splitter.addWidget(frame_left)

        # Panel Derecho: Tabla de Diagnostico y Pestañas de Resultados
        frame_right = QFrame()
        frame_right.setStyleSheet("background-color: #0f172a; border: 1px solid #1e293b; border-radius: 6px;")
        layout_right = QVBoxLayout(frame_right)
        layout_right.setContentsMargins(10, 10, 10, 10)
        layout_right.setSpacing(8)

        lbl_diag = QLabel("🔍 Diagnostico y Sugerencias de Optimizacion Atomica:")
        lbl_diag.setStyleSheet("color: #cbd5e1; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_right.addWidget(lbl_diag)

        # Tabla de Hallazgos
        self.table_results = QTableWidget()
        self.table_results.setColumnCount(4)
        self.table_results.setHorizontalHeaderLabels(["#", "Estado", "Regla Original", "Diagnostico / Recomendacion"])
        self.table_results.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_results.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table_results.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.table_results.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.table_results.setStyleSheet(
            "background-color: #020617; color: #f8fafc; font-family: 'Consolas'; font-size: 11px; "
            "gridline-color: #1e293b; border: 1px solid #334155; border-radius: 4px;"
        )
        layout_right.addWidget(self.table_results, 2)

        # Pestañas para Salidas: Saneada vs Optimizada Elegante
        self.tabs_output = QTabWidget()
        self.tabs_output.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #1e293b; background-color: #020617; border-radius: 4px; }
            QTabBar::tab { background: #0f172a; color: #94a3b8; font-family: 'Consolas'; font-weight: bold; padding: 6px 12px; border: 1px solid #1e293b; }
            QTabBar::tab:selected { background: #1e293b; color: #38bdf8; border-bottom: 2px solid #38bdf8; }
        """)

        # Pestaña 1: Optimizada Elegante (Recomendada)
        tab_opt = QWidget()
        layout_tab_opt = QVBoxLayout(tab_opt)
        layout_tab_opt.setContentsMargins(6, 6, 6, 6)
        self.txt_optimized_output = QTextEdit()
        self.txt_optimized_output.setReadOnly(True)
        self.txt_optimized_output.setStyleSheet(
            "background-color: #020617; color: #38bdf8; font-family: 'Consolas', monospace; "
            "font-size: 12px; border: 1px solid #0284c7; border-radius: 4px; padding: 8px;"
        )
        layout_tab_opt.addWidget(self.txt_optimized_output)

        btn_copy_opt = QPushButton("✨ Copiar Lista Optimizada (1-Linea Elegante) al Portapapeles")
        btn_copy_opt.setStyleSheet(
            "background-color: #0284c7; color: white; font-weight: bold; font-family: 'Consolas'; "
            "padding: 8px; border-radius: 4px; border: none;"
        )
        btn_copy_opt.clicked.connect(self.copy_optimized_to_clipboard)
        layout_tab_opt.addWidget(btn_copy_opt)
        self.tabs_output.addTab(tab_opt, "✨ Lista Optimizada (1-Línea Elegante)")

        # Pestaña 2: Saneada Estándar
        tab_std = QWidget()
        layout_tab_std = QVBoxLayout(tab_std)
        layout_tab_std.setContentsMargins(6, 6, 6, 6)
        self.txt_fixed_output = QTextEdit()
        self.txt_fixed_output.setReadOnly(True)
        self.txt_fixed_output.setStyleSheet(
            "background-color: #020617; color: #34d399; font-family: 'Consolas', monospace; "
            "font-size: 12px; border: 1px solid #059669; border-radius: 4px; padding: 8px;"
        )
        layout_tab_std.addWidget(self.txt_fixed_output)

        btn_copy_std = QPushButton("📋 Copiar Lista Saneada Estándar al Portapapeles")
        btn_copy_std.setStyleSheet(
            "background-color: #059669; color: white; font-weight: bold; font-family: 'Consolas'; "
            "padding: 8px; border-radius: 4px; border: none;"
        )
        btn_copy_std.clicked.connect(self.copy_fixed_to_clipboard)
        layout_tab_std.addWidget(btn_copy_std)
        self.tabs_output.addTab(tab_std, "✅ Lista Saneada Estándar")

        layout_right.addWidget(self.tabs_output, 1)

        splitter.addWidget(frame_right)
        splitter.setSizes([430, 670])
        layout.addWidget(splitter, 1)

        # Area de Analisis IA (Colapsable/Opcional)
        self.frame_ai = QFrame()
        self.frame_ai.setVisible(False)
        self.frame_ai.setStyleSheet("background-color: #17112b; border: 1px solid #6b21a8; border-radius: 6px; padding: 8px;")
        layout_ai = QVBoxLayout(self.frame_ai)
        layout_ai.setSpacing(6)

        self.lbl_ai_status = QLabel("🧠 Analisis de Contexto eBPF con Inteligencia Artificial:")
        self.lbl_ai_status.setStyleSheet("color: #c084fc; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_ai.addWidget(self.lbl_ai_status)

        self.txt_ai_response = QTextEdit()
        self.txt_ai_response.setReadOnly(True)
        self.txt_ai_response.setStyleSheet("background-color: #0c081a; color: #e9d5ff; font-family: 'Consolas'; font-size: 11px; border: 1px solid #7e22ce;")
        layout_ai.addWidget(self.txt_ai_response)

        layout.addWidget(self.frame_ai)

    def run_local_validation(self):
        """Ejecuta la validacion sintactica y optimizacion elegante deterministica."""
        raw_text = self.txt_rules_input.toPlainText().strip()
        if not raw_text:
            QMessageBox.information(self, "Aviso", "Por favor ingrese al menos una regla para validar.")
            return

        parsed_items, standard_fixed, unique_consolidated = audit_rule_batch(raw_text)

        total = len(parsed_items)
        opt_count = sum(1 for r in parsed_items if r.get("status") == "OPTIMAL")
        val_count = sum(1 for r in parsed_items if r.get("status") in ("VALID", "OPTIMAL"))
        err_count = sum(1 for r in parsed_items if r.get("status") == "ERROR")

        self.lbl_stats.setText(f"Reglas: {total} | Validas: {val_count} | Optimizadas: {opt_count} | Errores: {err_count}")
        if err_count > 0:
            self.lbl_stats.setStyleSheet("color: #ef4444; font-family: 'Consolas'; font-size: 12px; font-weight: bold;")
        else:
            self.lbl_stats.setStyleSheet("color: #10b981; font-family: 'Consolas'; font-size: 12px; font-weight: bold;")

        # Cargar Tabla
        self.table_results.setRowCount(total)

        for idx, res in enumerate(parsed_items):
            # 0: Num
            item_num = QTableWidgetItem(str(idx + 1))
            item_num.setTextAlignment(Qt.AlignCenter)

            # 1: Estado
            st = res.get("status", "VALID")
            if st == "OPTIMAL":
                item_st = QTableWidgetItem("✨ OPTIMA")
                item_st.setForeground(QColor("#38bdf8"))
            elif st == "VALID":
                item_st = QTableWidgetItem("✅ VALIDA")
                item_st.setForeground(QColor("#10b981"))
            elif st == "ERROR":
                item_st = QTableWidgetItem("❌ ERROR")
                item_st.setForeground(QColor("#ef4444"))
            else:
                item_st = QTableWidgetItem("⚠️ ADVERTENCIA")
                item_st.setForeground(QColor("#f59e0b"))
            item_st.setTextAlignment(Qt.AlignCenter)

            # 2: Original
            item_orig = QTableWidgetItem(res["original"])

            # 3: Diagnostico
            if res.get("errors"):
                diag_text = " | ".join(res["errors"])
            elif res.get("elegant_tip"):
                diag_text = res["elegant_tip"]
            elif res.get("warnings"):
                diag_text = " | ".join(res["warnings"])
            else:
                diag_text = "Sintaxis atomica libpcap correcta."
            item_diag = QTableWidgetItem(diag_text)

            self.table_results.setItem(idx, 0, item_num)
            self.table_results.setItem(idx, 1, item_st)
            self.table_results.setItem(idx, 2, item_orig)
            self.table_results.setItem(idx, 3, item_diag)

        self.txt_fixed_output.setPlainText("\n".join(standard_fixed))
        self.txt_optimized_output.setPlainText("\n".join(unique_consolidated))

        # Seleccionar la pestaña optimizada si se generaron optimizaciones
        if len(unique_consolidated) < len(standard_fixed) or opt_count > 0:
            self.tabs_output.setCurrentIndex(0)
        else:
            self.tabs_output.setCurrentIndex(1)

    def run_ai_audit(self):
        """Ejecuta analisis de apoyo opcional con IA."""
        raw_text = self.txt_rules_input.toPlainText().strip()
        if not raw_text:
            QMessageBox.information(self, "Aviso", "Por favor ingrese reglas para la auditoria con IA.")
            return

        self.frame_ai.setVisible(True)
        self.lbl_ai_status.setText("🧠 Analizando reglas con IA (Gemini)... espere...")
        self.txt_ai_response.setPlainText("Consultando orquestador cognitivo de seguridad...")
        self.btn_ai_audit.setEnabled(False)

        self._ai_worker = AiAdvisorWorker(raw_text)
        self._ai_worker.finished_ai.connect(self._on_ai_success)
        self._ai_worker.error_ai.connect(self._on_ai_error)
        self._ai_worker.start()

    def _on_ai_success(self, response_text: str):
        self.btn_ai_audit.setEnabled(True)
        self.lbl_ai_status.setText("🧠 Dictamen Forense de IA (Auditoria de Apoyo):")
        self.txt_ai_response.setPlainText(response_text)

    def _on_ai_error(self, err_msg: str):
        self.btn_ai_audit.setEnabled(True)
        self.lbl_ai_status.setText("⚠️ No se pudo completar la consulta de IA (Modo Local Sigue Operativo)")
        self.txt_ai_response.setPlainText(f"Error de conexion con el proveedor de IA: {err_msg}\nNota: El motor de validacion sintactica BPF local es completamente autonomo y no requiere IA.")

    def copy_optimized_to_clipboard(self):
        text = self.txt_optimized_output.toPlainText().strip()
        if not text:
            return
        from PySide6.QtGui import QGuiApplication
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Copiado", "Lista de reglas optimizadas (1-línea elegante) copiada al portapapeles con éxito.")

    def copy_fixed_to_clipboard(self):
        text = self.txt_fixed_output.toPlainText().strip()
        if not text:
            return
        from PySide6.QtGui import QGuiApplication
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Copiado", "Lista de reglas saneadas estándar copiada al portapapeles con éxito.")

    def clear_all(self):
        self.txt_rules_input.clear()
        self.txt_fixed_output.clear()
        self.txt_optimized_output.clear()
        self.table_results.setRowCount(0)
        self.lbl_stats.setText("Reglas: 0 | Validas: 0 | Optimizadas: 0 | Errores: 0")
        self.lbl_stats.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 12px; font-weight: bold;")
        self.frame_ai.setVisible(False)
