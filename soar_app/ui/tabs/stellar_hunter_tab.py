# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC — CENTRO VISUAL DE GOBERNABILIDAD DE QUERIES, FILTROS & HUNTING
=============================================================================
Integra de forma nativa y asíncrona en el Command Center los 3 nuevos motores:
  1. stellar_query_inspector.py (Saved Queries, Log Filters, Simulador de Cobertura
     de Dominios en Data Lake y agregado quirúrgico de dominios en 1 clic).
  2. stellar_threat_hunter.py (Caza directa de amenazas en Data Lake con 7 presets
     AD/Kerberoast/RDP/DNS y filtros personalizados).
  3. stellar_case_fetcher.py (Auditoría forense de casos cerrados hoy/24h y calidad
     de comentarios de cierre).
"""

import json
from typing import Dict, Any, List, Optional
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget,
    QLineEdit, QComboBox, QSpinBox, QTextEdit, QFrame,
    QMessageBox, QSplitter
)
import ui_theme


class InspectorAsyncWorker(QThread):
    """Ejecuta operaciones de stellar_query_inspector, stellar_threat_hunter y stellar_case_fetcher sin bloquear la UI."""
    finished_ok = Signal(str, dict)
    failed_err = Signal(str, str)

    def __init__(self, action: str, params: Optional[Dict[str, Any]] = None):
        super().__init__()
        self.action = action
        self.params = params or {}

    def run(self):
        try:
            if self.action == "load_governance":
                from stellar_query_inspector import (
                    get_jwt, list_saved_queries, list_ath_rules,
                    list_log_filters, get_in_use_query_ids
                )
                jwt = get_jwt()
                queries = list_saved_queries(jwt)
                ath_rules = list_ath_rules(jwt)
                filters = list_log_filters(jwt)
                in_use_map = get_in_use_query_ids(ath_rules, queries)
                self.finished_ok.emit(self.action, {
                    "queries": queries,
                    "ath_rules": ath_rules,
                    "filters": filters,
                    "in_use_map": in_use_map,
                })

            elif self.action == "audit_domains":
                from stellar_query_inspector import (
                    get_jwt, list_log_filters, get_log_filter_detail,
                    extract_filter_domains, analyze_top_domains
                )
                jwt = get_jwt()
                minutes = int(self.params.get("minutes", 30))
                filter_name = self.params.get("filter_name", "Drop_FW_Passthrough_Benign_Telemetry")
                filters = list_log_filters(jwt)
                target = next(
                    (f for f in filters if filter_name.lower() in (f.get("name") or "").lower() or filter_name == f.get("_id")),
                    None
                )
                filter_domains = []
                full_detail = {}
                if target:
                    fid = target.get("_id") or target.get("id")
                    full_detail = get_log_filter_detail(jwt, fid)
                    filter_domains = extract_filter_domains(full_detail)

                stats = analyze_top_domains(
                    jwt,
                    minutes=minutes,
                    msg_class="firewall_traffic",
                    action_val="passthrough",
                    size=100,
                    filter_domains=filter_domains
                )
                stats["filter_detail"] = full_detail
                stats["filter_domains"] = filter_domains
                self.finished_ok.emit(self.action, stats)

            elif self.action == "add_domain_to_filter":
                from stellar_query_inspector import (
                    get_jwt, list_log_filters, get_log_filter_detail,
                    extract_filter_domains, update_log_filter
                )
                jwt = get_jwt()
                filter_name = self.params.get("filter_name", "Drop_FW_Passthrough_Benign_Telemetry")
                new_domain = str(self.params.get("domain", "")).strip().lower().lstrip("*.")
                filters = list_log_filters(jwt)
                target = next(
                    (f for f in filters if filter_name.lower() in (f.get("name") or "").lower() or filter_name == f.get("_id")),
                    None
                )
                if not target:
                    raise RuntimeError(f"No se encontró el Log Filter '{filter_name}'")
                fid = target.get("_id") or target.get("id")
                detail = get_log_filter_detail(jwt, fid)
                existing = extract_filter_domains(detail)
                if new_domain not in existing:
                    existing.append(new_domain)
                    conds = detail.get("condition", {}).get("conditions", [])
                    for blk in conds:
                        rules = blk.get("rules", [])
                        if any(r.get("field") == "url" and r.get("operator") == "contains" for r in rules):
                            blk["rules"] = [
                                {"field": "url", "operator": "contains", "value": d, "type": "default"}
                                for d in existing
                            ]
                            break
                    update_log_filter(jwt, fid, detail)
                self.finished_ok.emit(self.action, {
                    "added": new_domain,
                    "total_domains": len(existing),
                    "filter_name": detail.get("name", filter_name)
                })

            elif self.action == "run_threat_hunt":
                from stellar_threat_hunter import get_jwt, build_es_query, query_datalake, PRESETS
                jwt = get_jwt()
                preset = self.params.get("preset") or None
                hours = float(self.params.get("hours", 24))
                limit = int(self.params.get("limit", 50))
                user = self.params.get("user") or None
                ip = self.params.get("ip") or None
                event_id = self.params.get("event_id") or None
                free_q = self.params.get("query") or None
                index = self.params.get("index", "stellar-event-*")
                if preset and preset in PRESETS:
                    index = PRESETS[preset].get("index", index)

                dsl = build_es_query(
                    preset=preset,
                    free_query=free_q,
                    user=user,
                    ip=ip,
                    event_id=event_id,
                    hours=hours,
                    limit=limit
                )
                res = query_datalake(jwt, index, dsl)
                hits_wrapper = res.get("hits", {})
                total_raw = hits_wrapper.get("total", 0)
                total = total_raw.get("value", 0) if isinstance(total_raw, dict) else int(total_raw or 0)
                hits = hits_wrapper.get("hits", [])
                self.finished_ok.emit(self.action, {
                    "total": total,
                    "hits": hits,
                    "aggs": res.get("aggregations", {}),
                    "index": index
                })

            elif self.action == "audit_closures":
                from datetime import datetime, timezone
                import time
                from stellar_case_fetcher import get_jwt, fetch_cases, fetch_case_comments, format_ts
                jwt = get_jwt()
                mode = self.params.get("mode", "today")
                if mode == "today":
                    now_local = datetime.now().astimezone()
                    midnight = now_local.replace(hour=0, minute=0, second=0, microsecond=0)
                    since_ms = int(midnight.timestamp() * 1000)
                else:
                    hours = float(self.params.get("hours", 24))
                    since_ms = int((time.time() - hours * 3600) * 1000)

                cases = fetch_cases(
                    jwt,
                    status="Closed,Resolved",
                    limit=100,
                    since_ms=since_ms,
                    time_field="closed_at"
                )
                if not cases:
                    cases = fetch_cases(
                        jwt,
                        status="Closed,Resolved",
                        limit=100,
                        since_ms=since_ms,
                        time_field="modified_at"
                    )
                rows = []
                for c in cases:
                    cid = c.get("_id", "")
                    comments = fetch_case_comments(jwt, cid)
                    last_comment = comments[-1].get("comment", "") if comments else "(Sin comentario)"
                    rows.append({
                        "ticket_id": c.get("ticket_id"),
                        "case_id": cid,
                        "name": c.get("name", ""),
                        "tenant": c.get("tenant_name", ""),
                        "severity": c.get("severity", ""),
                        "status": c.get("status", ""),
                        "resolution": c.get("resolution", "(Vacío)"),
                        "assignee": c.get("assignee_name") or c.get("assignee") or "Sin asignar",
                        "closed_at": format_ts(c.get("closed_at") or c.get("modified_at")),
                        "last_comment": last_comment,
                        "comments_count": len(comments),
                    })
                self.finished_ok.emit(self.action, {"cases": rows})

        except Exception as e:
            self.failed_err.emit(self.action, str(e))


class StellarHunterAndGovernanceWidget(QWidget):
    """
    Widget interactivo completo para:
      1. Gobernabilidad de Saved Queries, ATH y Simulador de Cobertura de Dominios en Log Filters.
      2. Threat Hunting Directo en Data Lake (Presets AD/Kerberoast/DNS + Filtros libres).
      3. Auditoría Forense de Casos Cerrados (Calidad de cierres y detección de candidatos a filtro).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._worker: Optional[InspectorAsyncWorker] = None
        self._last_gov_data: Dict[str, Any] = {}
        self._last_domain_stats: Dict[str, Any] = {}
        self._setup_ui()

    def _setup_ui(self):
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(10, 8, 10, 8)
        root_layout.setSpacing(8)

        # Banner Superior
        hdr = QFrame()
        hdr.setStyleSheet(
            f"background-color: {ui_theme.BG_SURFACE}; "
            f"border: 1px solid {ui_theme.BORDER_SUBTLE}; border-radius: 6px;"
        )
        hdr_layout = QHBoxLayout(hdr)
        hdr_layout.setContentsMargins(12, 8, 12, 8)

        lbl_title = QLabel("🔍 STELLAR HUNTER, AUDITORÍA DE COBERTURA DE DOMINIOS & GOBERNABILIDAD DE QUERIES")
        lbl_title.setStyleSheet(ui_theme.section_header_style(ui_theme.ACCENT_CYBER))
        hdr_layout.addWidget(lbl_title)

        hdr_layout.addStretch(1)

        self.lbl_status = QLabel("Listo para consultar API Stellar Cyber")
        self.lbl_status.setStyleSheet(
            f"color: {ui_theme.COLOR_SUCCESS}; font-size: 11px; font-weight: bold; "
            f"font-family: {ui_theme.FONT_MAIN}; border: none;"
        )
        hdr_layout.addWidget(self.lbl_status)

        root_layout.addWidget(hdr)

        # Sub-pestañas de los 3 motores nuevos
        self.sub_tabs = QTabWidget()
        root_layout.addWidget(self.sub_tabs, 1)

        self._build_subtab_domain_coverage()
        self._build_subtab_queries_and_filters()
        self._build_subtab_threat_hunter()
        self._build_subtab_closures_audit()

    # -------------------------------------------------------------------------
    # SUB-TAB 1: SIMULADOR DE COBERTURA DE DOMINIOS & LOG FILTERS
    # -------------------------------------------------------------------------
    def _build_subtab_domain_coverage(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        ctrl_bar = QHBoxLayout()
        ctrl_bar.addWidget(QLabel("Filtro Objetivo:"))
        self.txt_target_filter = QLineEdit("Drop_FW_Passthrough_Benign_Telemetry")
        self.txt_target_filter.setMinimumWidth(280)
        ctrl_bar.addWidget(self.txt_target_filter)

        ctrl_bar.addWidget(QLabel("Ventana Data Lake (min):"))
        self.spin_cov_mins = QSpinBox()
        self.spin_cov_mins.setRange(5, 1440)
        self.spin_cov_mins.setValue(30)
        ctrl_bar.addWidget(self.spin_cov_mins)

        btn_run_cov = QPushButton("📊 Auditar Top Dominios y Cobertura en Vivo")
        btn_run_cov.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        btn_run_cov.clicked.connect(self.run_domain_coverage_audit)
        ctrl_bar.addWidget(btn_run_cov)

        self.btn_add_selected_domain = QPushButton("➕ Agregar Dominio Seleccionado al Log Filter")
        self.btn_add_selected_domain.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_SUCCESS))
        self.btn_add_selected_domain.clicked.connect(self.add_selected_domain_to_filter)
        ctrl_bar.addWidget(self.btn_add_selected_domain)

        ctrl_bar.addStretch(1)
        layout.addLayout(ctrl_bar)

        self.lbl_cov_summary = QLabel(
            "Presione 'Auditar Top Dominios y Cobertura en Vivo' para medir el porcentaje exacto "
            "de ruido passthrough filtrado vs. tráfico visible en el Data Lake."
        )
        self.lbl_cov_summary.setStyleSheet(
            f"background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_PRIMARY}; "
            f"padding: 8px 12px; border-radius: 5px; border: 1px solid {ui_theme.BORDER_SUBTLE}; "
            f"font-family: {ui_theme.FONT_MONO}; font-size: 11px;"
        )
        layout.addWidget(self.lbl_cov_summary)

        self.tbl_domains = QTableWidget(0, 4)
        self.tbl_domains.setHorizontalHeaderLabels([
            "Dominio / Host (url.keyword)", "Eventos en Ventana", "% del Tráfico", "Estado frente al Log Filter"
        ])
        self.tbl_domains.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tbl_domains.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_domains.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_domains.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_domains.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbl_domains.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(self.tbl_domains, 1)

        self.sub_tabs.addTab(tab, "🌐 Cobertura de Dominios & Cuota (Log Filter)")

    # -------------------------------------------------------------------------
    # SUB-TAB 2: INVENTARIO DE SAVED QUERIES, ATH Y LOG FILTERS
    # -------------------------------------------------------------------------
    def _build_subtab_queries_and_filters(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        top_bar = QHBoxLayout()
        btn_load = QPushButton("🔄 Sincronizar Saved Queries, ATH Rules y Log Filters")
        btn_load.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_PRIMARY))
        btn_load.clicked.connect(self.load_governance_inventory)
        top_bar.addWidget(btn_load)
        top_bar.addStretch(1)
        layout.addLayout(top_bar)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Tabla Izquierda: Saved Queries + Estado ATH
        left_w = QWidget()
        l_lay = QVBoxLayout(left_w)
        l_lay.setContentsMargins(0, 0, 0, 0)
        l_lay.addWidget(QLabel("📋 SAVED QUERIES Y VÍNCULO CON REGLAS ATH:"))
        self.tbl_queries = QTableWidget(0, 4)
        self.tbl_queries.setHorizontalHeaderLabels(["Nombre de Query", "Índice", "Estado ATH", "ID"])
        self.tbl_queries.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tbl_queries.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbl_queries.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tbl_queries.itemSelectionChanged.connect(self._on_query_row_selected)
        l_lay.addWidget(self.tbl_queries, 1)

        # Tabla Derecha: Log Filters Activos + Inspector JSON
        right_w = QWidget()
        r_lay = QVBoxLayout(right_w)
        r_lay.setContentsMargins(0, 0, 0, 0)
        r_lay.addWidget(QLabel("🛡️ LOG FILTERS DE EXCLUSIÓN E INGESTA:"))
        self.tbl_log_filters = QTableWidget(0, 4)
        self.tbl_log_filters.setHorizontalHeaderLabels(["Orden", "Nombre del Log Filter", "Estado", "Creador"])
        self.tbl_log_filters.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tbl_log_filters.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbl_log_filters.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tbl_log_filters.itemSelectionChanged.connect(self._on_filter_row_selected)
        r_lay.addWidget(self.tbl_log_filters, 1)

        r_lay.addWidget(QLabel("🔎 DETALLE TÉCNICO / CONDICIONES DEL ELEMENTO SELECCIONADO:"))
        self.txt_gov_detail = QTextEdit()
        self.txt_gov_detail.setReadOnly(True)
        self.txt_gov_detail.setStyleSheet(f"font-family: {ui_theme.FONT_MONO}; font-size: 11px;")
        r_lay.addWidget(self.txt_gov_detail, 1)

        splitter.addWidget(left_w)
        splitter.addWidget(right_w)
        splitter.setSizes([560, 640])
        layout.addWidget(splitter, 1)

        self.sub_tabs.addTab(tab, "🗂️ Inventario Saved Queries & Log Filters")

    # -------------------------------------------------------------------------
    # SUB-TAB 3: THREAT HUNTING DIRECTO EN DATA LAKE
    # -------------------------------------------------------------------------
    def _build_subtab_threat_hunter(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        bar1 = QHBoxLayout()
        bar1.addWidget(QLabel("Preset de Caza:"))
        self.cmb_hunt_preset = QComboBox()
        self.cmb_hunt_preset.addItems([
            "(Personalizado / Libre)",
            "dc_logons — Logons Exitosos (4624) en Domain Controllers",
            "failed_logons — Fallos de Autenticación (4625 / 4776 / 4771)",
            "lockouts — Bloqueos de Cuenta en AD (4740)",
            "priv_groups — Cambios en Grupos Privilegiados AD (4728/4732/4756)",
            "rdp_lateral — Movimiento Lateral RDP (Logon Type 10)",
            "kerberoast — Solicitudes de Tickets Kerberos RC4 (4769)",
            "dns_anomalies — Tráfico DNS Sospechoso / Túneles"
        ])
        bar1.addWidget(self.cmb_hunt_preset, 1)

        bar1.addWidget(QLabel("Usuario:"))
        self.txt_hunt_user = QLineEdit()
        self.txt_hunt_user.setPlaceholderText("ej. HealthMailbox* o admin*")
        bar1.addWidget(self.txt_hunt_user)

        bar1.addWidget(QLabel("IP:"))
        self.txt_hunt_ip = QLineEdit()
        self.txt_hunt_ip.setPlaceholderText("ej. 10.20.70.3")
        bar1.addWidget(self.txt_hunt_ip)

        bar1.addWidget(QLabel("Event ID:"))
        self.txt_hunt_evid = QLineEdit()
        self.txt_hunt_evid.setPlaceholderText("ej. 4776")
        self.txt_hunt_evid.setMaximumWidth(90)
        bar1.addWidget(self.txt_hunt_evid)

        bar1.addWidget(QLabel("Horas:"))
        self.spin_hunt_hours = QSpinBox()
        self.spin_hunt_hours.setRange(1, 720)
        self.spin_hunt_hours.setValue(24)
        bar1.addWidget(self.spin_hunt_hours)

        btn_hunt = QPushButton("🎯 Ejecutar Caza en Data Lake")
        btn_hunt.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_HIGH))
        btn_hunt.clicked.connect(self.run_datalake_threat_hunt)
        bar1.addWidget(btn_hunt)

        layout.addLayout(bar1)

        bar2 = QHBoxLayout()
        bar2.addWidget(QLabel("Query Lucene / KQL Adicional:"))
        self.txt_hunt_free = QLineEdit()
        self.txt_hunt_free.setPlaceholderText("Opcional: ej. tenant_name:CAJAANDE AND NOT username:HealthMailbox*")
        bar2.addWidget(self.txt_hunt_free, 1)
        layout.addLayout(bar2)

        self.tbl_hunt_hits = QTableWidget(0, 7)
        self.tbl_hunt_hits.setHorizontalHeaderLabels([
            "Timestamp", "Tenant", "Host / Equipo", "Usuario", "Event ID / Clase", "IP Origen -> Destino", "Detalle"
        ])
        self.tbl_hunt_hits.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        self.tbl_hunt_hits.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbl_hunt_hits.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(self.tbl_hunt_hits, 1)

        self.sub_tabs.addTab(tab, "🎯 Threat Hunting Directo (Data Lake)")

    # -------------------------------------------------------------------------
    # SUB-TAB 4: AUDITORÍA FORENSE DE CASOS CERRADOS HOY / 24H
    # -------------------------------------------------------------------------
    def _build_subtab_closures_audit(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        bar = QHBoxLayout()
        btn_today = QPushButton("📅 Auditar Cierres de HOY (Desde 00:00 hs)")
        btn_today.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_SUCCESS))
        btn_today.clicked.connect(lambda: self.run_closures_audit("today"))
        bar.addWidget(btn_today)

        btn_24h = QPushButton("⏱️ Auditar Últimas 24 Horas")
        btn_24h.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        btn_24h.clicked.connect(lambda: self.run_closures_audit("24h"))
        bar.addWidget(btn_24h)

        self.lbl_closures_summary = QLabel("Sin auditoría ejecutada aún.")
        self.lbl_closures_summary.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; border: none;")
        bar.addWidget(self.lbl_closures_summary)
        bar.addStretch(1)
        layout.addLayout(bar)

        self.tbl_closures = QTableWidget(0, 7)
        self.tbl_closures.setHorizontalHeaderLabels([
            "Ticket", "Nombre del Caso", "Tenant", "Severidad", "Resolución", "Cerrado Por", "Último Comentario Forense"
        ])
        self.tbl_closures.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.tbl_closures.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        self.tbl_closures.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbl_closures.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(self.tbl_closures, 1)

        self.sub_tabs.addTab(tab, "✅ Auditoría de Cierres del Turno")

    # -------------------------------------------------------------------------
    # ACCIONES Y SLOTS ASÍNCRONOS
    # -------------------------------------------------------------------------
    def _start_worker(self, action: str, params: dict, status_msg: str):
        if self._worker and self._worker.isRunning():
            QMessageBox.information(self, "Operación en Curso", "Espere a que finalice la consulta actual.")
            return
        self.lbl_status.setText(f"⏳ {status_msg}...")
        self._worker = InspectorAsyncWorker(action, params)
        self._worker.finished_ok.connect(self._on_worker_ok)
        self._worker.failed_err.connect(self._on_worker_err)
        self._worker.start()

    def run_domain_coverage_audit(self):
        self._start_worker(
            "audit_domains",
            {
                "filter_name": self.txt_target_filter.text().strip(),
                "minutes": self.spin_cov_mins.value()
            },
            "Escaneando Data Lake y calculando cobertura del Log Filter"
        )

    def add_selected_domain_to_filter(self):
        row = self.tbl_domains.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Seleccione un Dominio", "Seleccione una fila de la tabla de dominios primero.")
            return
        domain = self.tbl_domains.item(row, 0).text().strip()
        if not domain or domain.startswith("("):
            QMessageBox.warning(self, "Dominio Inválido", "No se puede agregar un flujo sin nombre de dominio.")
            return
        filter_name = self.txt_target_filter.text().strip()
        ans = QMessageBox.question(
            self,
            "Confirmar Actualización de Log Filter en Producción",
            f"¿Desea agregar la condición:\n\n    url contains '{domain}'\n\n"
            f"al filtro '{filter_name}' directamente en Stellar Cyber?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if ans == QMessageBox.StandardButton.Yes:
            self._start_worker(
                "add_domain_to_filter",
                {"filter_name": filter_name, "domain": domain},
                f"Agregando '{domain}' al filtro '{filter_name}'"
            )

    def load_governance_inventory(self):
        self._start_worker("load_governance", {}, "Descargando Saved Queries, ATH Rules y Log Filters")

    def run_datalake_threat_hunt(self):
        raw_preset = self.cmb_hunt_preset.currentText()
        preset_key = raw_preset.split(" — ")[0].strip() if " — " in raw_preset else None
        self._start_worker(
            "run_threat_hunt",
            {
                "preset": preset_key,
                "user": self.txt_hunt_user.text().strip(),
                "ip": self.txt_hunt_ip.text().strip(),
                "event_id": self.txt_hunt_evid.text().strip(),
                "hours": self.spin_hunt_hours.value(),
                "query": self.txt_hunt_free.text().strip(),
                "limit": 100,
            },
            "Ejecutando caza de amenazas en Data Lake"
        )

    def run_closures_audit(self, mode: str):
        self._start_worker("audit_closures", {"mode": mode, "hours": 24}, "Auditando casos cerrados y comentarios")

    def _on_worker_err(self, action: str, err: str):
        self.lbl_status.setText(f"❌ Error en {action}: {err[:90]}")
        QMessageBox.warning(self, "Error en Consulta Stellar Cyber", f"Detalle técnico:\n{err}")

    def _on_worker_ok(self, action: str, data: dict):
        self.lbl_status.setText("✅ Consulta completada exitosamente")

        if action == "audit_domains":
            self._last_domain_stats = data
            total_ev = data.get("total_events", 0)
            with_url = data.get("with_url", 0)
            no_url = data.get("without_url", 0)
            cov = data.get("covered_in_top", 0)
            uncov = data.get("uncovered_in_top", 0)
            top_sum = cov + uncov
            pct_cov = (cov / top_sum * 100.0) if top_sum else 0.0
            f_doms = data.get("filter_domains", [])

            self.lbl_cov_summary.setText(
                f"📊 Total Eventos Passthrough ({self.spin_cov_mins.value()}m): {total_ev:,}  |  "
                f"Con URL/SNI: {with_url:,}  |  IP Cruda (Siempre Visible): {no_url:,}\n"
                f"🛡️ Dominios en '{self.txt_target_filter.text()}': {len(f_doms)} patrones  |  "
                f"✅ Ruido Cubierto en Top Dominios: {cov:,} ({pct_cov:.1f}%)  |  "
                f"👁️ Tráfico Visible Restante: {uncov:,} ({100.0 - pct_cov:.1f}%)"
            )

            buckets = data.get("top_domains", [])
            self.tbl_domains.setRowCount(len(buckets))
            for i, b in enumerate(buckets):
                dom = b.get("domain", "")
                cnt = b.get("count", 0)
                pct = b.get("pct", 0.0)
                covered = b.get("covered", False)

                it_dom = QTableWidgetItem(dom)
                it_cnt = QTableWidgetItem(f"{cnt:,}")
                it_pct = QTableWidgetItem(f"{pct:.2f}%")
                it_st = QTableWidgetItem("✅ FILTRADO (Benigno)" if covered else "👁️ VISIBLE (Inspeccionado)")
                it_st.setForeground(QColor("#10b981" if covered else "#38bdf8"))
                self.tbl_domains.setItem(i, 0, it_dom)
                self.tbl_domains.setItem(i, 1, it_cnt)
                self.tbl_domains.setItem(i, 2, it_pct)
                self.tbl_domains.setItem(i, 3, it_st)

        elif action == "add_domain_to_filter":
            QMessageBox.information(
                self,
                "Dominio Agregado Exitosamente",
                f"Se agregó '{data.get('added')}' al filtro '{data.get('filter_name')}'.\n"
                f"Total de patrones de dominio activos en el filtro: {data.get('total_domains')}."
            )
            self.run_domain_coverage_audit()

        elif action == "load_governance":
            self._last_gov_data = data
            queries = data.get("queries", [])
            filters = data.get("filters", [])
            in_use_map = data.get("in_use_map", {})

            self.tbl_queries.setRowCount(len(queries))
            for i, q in enumerate(queries):
                qid = q.get("_id") or q.get("id") or ""
                qname = q.get("name", "Sin nombre")
                idx = q.get("index", "")
                used_by = in_use_map.get(qid, [])
                st_txt = f"🟢 EN USO ({len(used_by)} ATH)" if used_by else "⚪ No vinculada"
                it_st = QTableWidgetItem(st_txt)
                it_st.setForeground(QColor("#10b981" if used_by else "#94a3b8"))

                self.tbl_queries.setItem(i, 0, QTableWidgetItem(qname))
                self.tbl_queries.setItem(i, 1, QTableWidgetItem(str(idx)))
                self.tbl_queries.setItem(i, 2, it_st)
                self.tbl_queries.setItem(i, 3, QTableWidgetItem(str(qid)))

            self.tbl_log_filters.setRowCount(len(filters))
            for i, lf in enumerate(filters):
                order = str(lf.get("order", i + 1))
                name = lf.get("name", "")
                st = str(lf.get("status", "Active"))
                by = lf.get("created_by_name") or lf.get("created_by") or "N/A"
                self.tbl_log_filters.setItem(i, 0, QTableWidgetItem(order))
                self.tbl_log_filters.setItem(i, 1, QTableWidgetItem(name))
                self.tbl_log_filters.setItem(i, 2, QTableWidgetItem(st))
                self.tbl_log_filters.setItem(i, 3, QTableWidgetItem(str(by)))

        elif action == "run_threat_hunt":
            hits = data.get("hits", [])
            total = data.get("total", 0)
            self.lbl_status.setText(f"✅ Threat Hunt finalizado: {total:,} eventos totales ({len(hits)} mostrados)")
            self.tbl_hunt_hits.setRowCount(len(hits))
            for i, h in enumerate(hits):
                src = h.get("_source", {})
                ts = str(src.get("timestamp") or src.get("@timestamp") or "")
                tenant = str(src.get("tenant_name") or "")
                host = str(src.get("hostname") or src.get("dev_name") or src.get("srcip_host") or "")
                win_ev = src.get("win_event", {}) if isinstance(src.get("win_event"), dict) else {}
                user = str(
                    src.get("username")
                    or win_ev.get("target_user_name")
                    or win_ev.get("subject_user_name")
                    or ""
                )
                ev_id = str(src.get("event_id") or win_ev.get("event_id") or src.get("msg_class") or "")
                ips = f"{src.get('srcip', '-')} -> {src.get('dstip', '-')}"
                detail = str(src.get("url") or src.get("event_name") or src.get("process_name") or src.get("appid_name") or "")

                self.tbl_hunt_hits.setItem(i, 0, QTableWidgetItem(ts))
                self.tbl_hunt_hits.setItem(i, 1, QTableWidgetItem(tenant))
                self.tbl_hunt_hits.setItem(i, 2, QTableWidgetItem(host))
                self.tbl_hunt_hits.setItem(i, 3, QTableWidgetItem(user))
                self.tbl_hunt_hits.setItem(i, 4, QTableWidgetItem(ev_id))
                self.tbl_hunt_hits.setItem(i, 5, QTableWidgetItem(ips))
                self.tbl_hunt_hits.setItem(i, 6, QTableWidgetItem(detail))

        elif action == "audit_closures":
            rows = data.get("cases", [])
            fp_cnt = sum(1 for r in rows if "false" in str(r.get("resolution", "")).lower())
            ben_cnt = sum(1 for r in rows if "benign" in str(r.get("resolution", "")).lower())
            tp_cnt = sum(1 for r in rows if "true" in str(r.get("resolution", "")).lower())
            self.lbl_closures_summary.setText(
                f"Casos Cerrados: {len(rows)}  |  False Positive: {fp_cnt}  |  Benign: {ben_cnt}  |  True Positive: {tp_cnt}"
            )
            self.tbl_closures.setRowCount(len(rows))
            for i, r in enumerate(rows):
                self.tbl_closures.setItem(i, 0, QTableWidgetItem(f"#{r.get('ticket_id')}"))
                self.tbl_closures.setItem(i, 1, QTableWidgetItem(str(r.get("name"))))
                self.tbl_closures.setItem(i, 2, QTableWidgetItem(str(r.get("tenant"))))
                self.tbl_closures.setItem(i, 3, QTableWidgetItem(str(r.get("severity"))))
                self.tbl_closures.setItem(i, 4, QTableWidgetItem(str(r.get("resolution"))))
                self.tbl_closures.setItem(i, 5, QTableWidgetItem(str(r.get("assignee"))))
                self.tbl_closures.setItem(i, 6, QTableWidgetItem(str(r.get("last_comment"))))

    def _on_query_row_selected(self):
        row = self.tbl_queries.currentRow()
        queries = self._last_gov_data.get("queries", [])
        if 0 <= row < len(queries):
            self.txt_gov_detail.setPlainText(json.dumps(queries[row], indent=2, ensure_ascii=False))

    def _on_filter_row_selected(self):
        row = self.tbl_log_filters.currentRow()
        filters = self._last_gov_data.get("filters", [])
        if 0 <= row < len(filters):
            self.txt_gov_detail.setPlainText(json.dumps(filters[row], indent=2, ensure_ascii=False))
