import os
import sys

source_bak = r"C:\Users\kevinmoraes\Documents\soc-env\ingestion_audit_dialog.py.bak"
target_soc_env = r"C:\Users\kevinmoraes\Documents\soc-env\ingestion_audit_dialog.py"
target_soar = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\ingestion_audit_dialog.py"

with open(source_bak, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure QGridLayout is in imports
if "QGridLayout" not in content:
    content = content.replace(
        "QApplication, QScrollArea, QSizePolicy, QSpinBox, QToolTip",
        "QApplication, QScrollArea, QSizePolicy, QSpinBox, QToolTip, QGridLayout"
    )

# 2. Add THREAT_HUNTING_MODULES_DEF definition before IngestionAuditEngine
th_modules_code = '''
# =============================================================================
# DEFINICIÓN OFICIAL DE LOS 20 MÓDULOS DE THREAT HUNTING LIBRARY (STELLAR CYBER)
# =============================================================================
THREAT_HUNTING_MODULES_DEF = [
    {"id": "firewall", "name": "Firewall", "icon": "🛡️", "category": "Perímetro", "query": "msg_class:firewall OR dev_type:fw_fortigate"},
    {"id": "dns", "name": "DNS Analysis", "icon": "🌐", "category": "Red & Protocolos", "query": "dstport:53 OR msg_class:dns OR appid_name:DNS OR appid_name:Google-DNS"},
    {"id": "net_apps", "name": "Network Applications", "icon": "🚀", "category": "Red & Protocolos", "query": "msg_class:interflow_traffic OR msg_class:flow"},
    {"id": "gsuite", "name": "Google Workspace", "icon": "☁️", "category": "Cloud & SaaS", "query": "msg_class:gsuite"},
    {"id": "plain_pwd", "name": "Plain Text Passwords", "icon": "🔑", "category": "Identidad & Riesgo", "query": "dstport:389 OR dstport:21 OR dstport:23 OR alert_type:*password* OR msg_class:plain_text*"},
    {"id": "login_fail", "name": "All Login Failures", "icon": "❌", "category": "Identidad & Autenticación", "query": "action:failure OR action:failed OR msg_class:auth_failure OR event_name:*login*failure*"},
    {"id": "win_logins", "name": "Windows Logins", "icon": "🪟", "category": "Endpoint & Windows", "query": "win_event_id:4624 OR event_id:4624"},
    {"id": "win_priv_esc", "name": "Windows Privilege Escalations", "icon": "⚡", "category": "Endpoint & Windows", "query": "win_event_id:4672 OR event_id:4672"},
    {"id": "win_cmd", "name": "Windows Command Line", "icon": "💻", "category": "Endpoint & Windows", "query": "process_commandline:* OR process_cmd:*"},
    {"id": "win_procs", "name": "Windows New Processes", "icon": "⚙️", "category": "Endpoint & Windows", "query": "win_event_id:4688 OR event_id:4688 OR process_name:*"},
    {"id": "sophos", "name": "Sophos Endpoint", "icon": "🛡️", "category": "Endpoint & EDR", "query": "dev_type:endpoint_sophos OR msg_class:sophos*"},
    {"id": "non_std_ports", "name": "Non-Standard Port Usage", "icon": "🔌", "category": "Red & Protocolos", "query": "appid_stdport:no"},
    {"id": "tunnel_traffic", "name": "Tunneled Traffic", "icon": "🚇", "category": "Red & Protocolos", "query": "proto_name:gre OR proto_name:ipip OR dstport:4789"},
    {"id": "win_acct_chg", "name": "Windows Account Changes", "icon": "👤", "category": "Identidad & Windows", "query": "win_event_id:4720 OR win_event_id:4722 OR win_event_id:4724 OR win_event_id:4738 OR event_id:4720"},
    {"id": "win_lockouts", "name": "Windows Account Lockouts", "icon": "🔒", "category": "Identidad & Windows", "query": "win_event_id:4740 OR event_id:4740"},
    {"id": "win_ps", "name": "Windows PowerShell Startups", "icon": "📜", "category": "Endpoint & Windows", "query": "win_event_id:4104 OR event_id:4104 OR process_name:powershell.exe"},
    {"id": "file_storage", "name": "External File Storage Access", "icon": "📁", "category": "Data Leak & Cloud", "query": "appid_name:*drive* OR appid_name:*dropbox* OR appid_name:*onedrive*"},
    {"id": "cloud_email", "name": "Cloud Email Provider Access", "icon": "✉️", "category": "Cloud & SaaS", "query": "appid_name:*gmail* OR appid_name:*office365* OR appid_name:*outlook*"},
    {"id": "win_login_fail", "name": "Windows Login Failures", "icon": "🚫", "category": "Identidad & Windows", "query": "win_event_id:4625 OR event_id:4625"},
    {"id": "win_software", "name": "Windows Software Installed", "icon": "📦", "category": "Endpoint & Windows", "query": "win_event_id:11707 OR event_id:11707"}
]
'''

engine_marker = "class IngestionAuditEngine:"
if engine_marker in content:
    content = content.replace(engine_marker, th_modules_code + "\n" + engine_marker)

# 3. Add fetch_threat_hunting_matrix and fetch_threat_hunting_drilldown to IngestionAuditEngine
engine_methods = '''
    def fetch_threat_hunting_matrix(self, target_index: str = None) -> Dict[str, Any]:
        """Consulta en paralelo los 20 modulos de Threat Hunting Library mediante un solo request en <1 segundo."""
        headers = self.get_headers()
        cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
        if not target_index:
            today_str = datetime.now().strftime("%Y.%m.%d")
            target_index = f"*{today_str}*{cust_id}*"
            
        filters_map = {m["name"]: {"query_string": {"query": m["query"]}} for m in THREAT_HUNTING_MODULES_DEF}
        body = {
            "size": 0,
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"tenantid": cust_id}}
                    ]
                }
            },
            "aggs": {
                "th_matrix": {
                    "filters": {
                        "filters": filters_map
                    }
                }
            }
        }
        t0 = time.time()
        url = f"https://{self.host}/connect/api/data/{target_index}/_search"
        counts = {}
        total_matched = 0
        try:
            res = self.session.get(url, headers=headers, json=body, timeout=45, verify=False)
            elapsed = time.time() - t0
            if res.status_code == 200:
                buckets = res.json().get("aggregations", {}).get("th_matrix", {}).get("buckets", {})
                for m in THREAT_HUNTING_MODULES_DEF:
                    b_doc = buckets.get(m["name"], {})
                    cnt = b_doc.get("doc_count", 0) if isinstance(b_doc, dict) else 0
                    counts[m["name"]] = cnt
                    total_matched += cnt
                return {
                    "status": "success",
                    "counts": counts,
                    "total_matched": total_matched,
                    "elapsed": elapsed,
                    "target_index": target_index
                }
            else:
                return {"status": "error", "error": f"HTTP {res.status_code}: {res.text[:200]}", "counts": {}, "elapsed": elapsed}
        except Exception as e:
            return {"status": "error", "error": str(e), "counts": {}, "elapsed": 0}

    def fetch_threat_hunting_drilldown(self, module_name: str, query_str: str, target_index: str = None) -> Dict[str, Any]:
        """Realiza un drill-down forense sobre un modulo: top srcip, top dstip, top msg_class y muestra cruda."""
        headers = self.get_headers()
        cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
        if not target_index:
            today_str = datetime.now().strftime("%Y.%m.%d")
            target_index = f"*{today_str}*{cust_id}*"
            
        body = {
            "size": 5,
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"tenantid": cust_id}},
                        {"query_string": {"query": query_str}}
                    ]
                }
            },
            "aggs": {
                "top_src": {"terms": {"field": "srcip_host.keyword", "size": 8}},
                "top_dst": {"terms": {"field": "dstip_host.keyword", "size": 8}},
                "top_msg_class": {"terms": {"field": "msg_class.keyword", "size": 8}},
                "top_ports": {"terms": {"field": "dstport", "size": 8}}
            }
        }
        t0 = time.time()
        url = f"https://{self.host}/connect/api/data/{target_index}/_search"
        try:
            res = self.session.get(url, headers=headers, json=body, timeout=45, verify=False)
            elapsed = time.time() - t0
            if res.status_code == 200:
                data = res.json()
                total_hits = data.get("hits", {}).get("total", {})
                if isinstance(total_hits, dict):
                    total_docs = total_hits.get("value", 0)
                else:
                    total_docs = int(total_hits or 0)
                hits = [h.get("_source", {}) for h in data.get("hits", {}).get("hits", [])]
                aggs = data.get("aggregations", {})
                return {
                    "status": "success",
                    "module_name": module_name,
                    "query_str": query_str,
                    "total_docs": total_docs,
                    "hits": hits,
                    "top_src_buckets": aggs.get("top_src", {}).get("buckets", []),
                    "top_dst_buckets": aggs.get("top_dst", {}).get("buckets", []),
                    "top_msg_class_buckets": aggs.get("top_msg_class", {}).get("buckets", []),
                    "top_ports_buckets": aggs.get("top_ports", {}).get("buckets", []),
                    "elapsed": elapsed
                }
            else:
                return {"status": "error", "error": f"HTTP {res.status_code}: {res.text[:200]}"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
'''

audit_filter_marker = "    @classmethod\n    def audit_filters_for_blind_spots"
if audit_filter_marker in content:
    content = content.replace(audit_filter_marker, engine_methods + "\n" + audit_filter_marker)

# 4. Add Worker classes
workers_code = '''
class ThreatHuntingRadarWorker(QThread):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, target_index: str = None):
        super().__init__()
        self.target_index = target_index
        self.engine = IngestionAuditEngine()

    def run(self):
        try:
            data = self.engine.fetch_threat_hunting_matrix(self.target_index)
            if data.get("status") == "success":
                self.finished.emit(data)
            else:
                self.error.emit(data.get("error", "Error desconocido"))
        except Exception as e:
            self.error.emit(str(e))


class ThreatHuntingDrilldownWorker(QThread):
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, module_name: str, query_str: str, target_index: str = None):
        super().__init__()
        self.module_name = module_name
        self.query_str = query_str
        self.target_index = target_index
        self.engine = IngestionAuditEngine()

    def run(self):
        try:
            data = self.engine.fetch_threat_hunting_drilldown(self.module_name, self.query_str, self.target_index)
            if data.get("status") == "success":
                self.finished.emit(data)
            else:
                self.error.emit(data.get("error", "Error desconocido"))
        except Exception as e:
            self.error.emit(str(e))
'''

dialog_class_marker = "class IngestionAuditDialog(QDialog):"
if dialog_class_marker in content:
    content = content.replace(dialog_class_marker, workers_code + "\n\n" + dialog_class_marker)

# 5. Add Tab 6 in _init_ui
tab_init_marker = 'self.tabs.addTab(self.tab_interflow, "⚡ Tráfico Interflow & Diagnóstico de Cuota L7")'
tab_6_init_code = '''self.tabs.addTab(self.tab_interflow, "⚡ Tráfico Interflow & Diagnóstico de Cuota L7")

        # Pestaña 6: Radar y Matriz de Threat Hunting (20 Módulos Oficiales)
        self.tab_threat_hunting = QWidget()
        self._setup_tab_threat_hunting()
        self.tabs.addTab(self.tab_threat_hunting, "🎯 Radar Threat Hunting (20 Módulos)")'''

if tab_init_marker in content:
    content = content.replace(tab_init_marker, tab_6_init_code)

# 6. Hook into refrescar_datos
refresh_trigger_marker = "self.worker = IngestionAuditWorker(hours)\n        self.worker.finished.connect(self._on_data_loaded)"
refresh_trigger_replacement = """self.worker = IngestionAuditWorker(hours)
        self.worker.finished.connect(self._on_data_loaded)
        self._refresh_threat_hunting_radar()"""

if refresh_trigger_marker in content:
    content = content.replace(refresh_trigger_marker, refresh_trigger_replacement)

# 7. Add UI methods for Tab 6 before export / if __name__
th_ui_methods = '''
    # =========================================================================
    # PESTAÑA 6: RADAR THREAT HUNTING (20 MÓDULOS EN TIEMPO REAL)
    # =========================================================================
    def _setup_tab_threat_hunting(self):
        layout = QVBoxLayout(self.tab_threat_hunting)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(12)

        # 1. Barra de Control Superior
        ctrl_box = QFrame()
        ctrl_box.setStyleSheet(f"background-color: {ui_theme.BG_ELEVATED}; border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 6px; padding: 6px;")
        ctrl_l = QHBoxLayout(ctrl_box)
        ctrl_l.setContentsMargins(8, 6, 8, 6)
        ctrl_l.setSpacing(10)

        lbl_title = QLabel("🎯 RADAR DE THREAT HUNTING LIBRARY (20 MÓDULOS STELLAR CYBER)")
        lbl_title.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 12px; font-weight: bold;")
        ctrl_l.addWidget(lbl_title)
        ctrl_l.addStretch()

        lbl_scope = QLabel("Rango Temporal:")
        lbl_scope.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 11px;")
        ctrl_l.addWidget(lbl_scope)

        self.cmb_th_scope = QComboBox()
        self.cmb_th_scope.addItems(["📅 Hoy (Índice Activo)", "📆 Mes Actual (*2026.10*)", "🌐 Histórico Total (*)"])
        self.cmb_th_scope.setStyleSheet(get_dropdown_style())
        self.cmb_th_scope.currentIndexChanged.connect(self._refresh_threat_hunting_radar)
        ctrl_l.addWidget(self.cmb_th_scope)

        btn_radar_refresh = QPushButton("🔄 Actualizar Radar")
        btn_radar_refresh.setStyleSheet(ui_theme.primary_action_btn_style())
        btn_radar_refresh.clicked.connect(self._refresh_threat_hunting_radar)
        ctrl_l.addWidget(btn_radar_refresh)

        btn_copy_matrix = QPushButton("📋 Copiar Resumen")
        btn_copy_matrix.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_copy_matrix.clicked.connect(self._copiar_resumen_th_radar)
        ctrl_l.addWidget(btn_copy_matrix)

        layout.addWidget(ctrl_box)

        # Banner de Estado / Estadísticas Rápidas
        self.lbl_th_stats = QLabel("⚡ Inicializando Radar de Threat Hunting...")
        self.lbl_th_stats.setStyleSheet(f"color: {ui_theme.TEXT_SECONDARY}; font-size: 11px; padding: 2px 6px;")
        layout.addWidget(self.lbl_th_stats)

        # 2. Splitter Principal: Grid de 20 Módulos (Arriba) / Panel Forense de Drilldown (Abajo)
        splitter = QSplitter(Qt.Vertical)

        # Área Scrollable para las 20 Tarjetas
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"QScrollArea {{ border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 6px; background-color: {ui_theme.BG_SURFACE}; }}")

        self.grid_container = QWidget()
        self.grid_cards = QGridLayout(self.grid_container)
        self.grid_cards.setContentsMargins(10, 10, 10, 10)
        self.grid_cards.setSpacing(10)

        self.th_cards_map = {}
        for idx, mod in enumerate(THREAT_HUNTING_MODULES_DEF):
            card = self._create_th_module_card(mod)
            row = idx // 4
            col = idx % 4
            self.grid_cards.addWidget(card, row, col)
            self.th_cards_map[mod["name"]] = card

        scroll.setWidget(self.grid_container)
        splitter.addWidget(scroll)

        # Panel Inferior: Drilldown Forense Detallado
        drill_panel = QFrame()
        drill_panel.setStyleSheet(f"background-color: {ui_theme.BG_ELEVATED}; border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 6px; padding: 10px;")
        drill_layout = QVBoxLayout(drill_panel)
        drill_layout.setContentsMargins(10, 8, 10, 8)
        drill_layout.setSpacing(8)

        # Header de Drilldown
        drill_hdr = QHBoxLayout()
        self.lbl_drill_title = QLabel("🔍 Drilldown Forense: Selecciona un módulo arriba para ver detalles")
        self.lbl_drill_title.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 12px; font-weight: bold;")
        drill_hdr.addWidget(self.lbl_drill_title)
        drill_hdr.addStretch()

        self.btn_copy_th_query = QPushButton("📋 Copiar Query DSL")
        self.btn_copy_th_query.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_copy_th_query.clicked.connect(self._copiar_th_query_dsl)
        self.btn_copy_th_query.setEnabled(False)
        drill_hdr.addWidget(self.btn_copy_th_query)

        self.btn_jump_to_filter = QPushButton("⚡ Crear Filtro Quirúrgico")
        self.btn_jump_to_filter.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_jump_to_filter.clicked.connect(self._saltar_a_filtro_con_modulo)
        self.btn_jump_to_filter.setEnabled(False)
        drill_hdr.addWidget(self.btn_jump_to_filter)

        drill_layout.addLayout(drill_hdr)

        # Contenido de Drilldown: 3 columnas (Top IPs/Puertos, Muestra de Logs, Resumen)
        drill_content = QHBoxLayout()

        # Columna 1: Top Actores (IPs / Puertos)
        col_actors = QFrame()
        col_actors.setStyleSheet(f"background-color: {ui_theme.BG_SURFACE}; border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 4px; padding: 6px;")
        col_actors_l = QVBoxLayout(col_actors)
        lbl_act = QLabel("🌐 Top Orígenes / Destinos")
        lbl_act.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 11px; font-weight: bold;")
        col_actors_l.addWidget(lbl_act)
        self.txt_drill_actors = QTextEdit()
        self.txt_drill_actors.setReadOnly(True)
        self.txt_drill_actors.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_PRIMARY}; border: none; font-family: {ui_theme.FONT_MONO}; font-size: 10px;")
        col_actors_l.addWidget(self.txt_drill_actors)
        drill_content.addWidget(col_actors, 1)

        # Columna 2: Muestras Forenses Crudas
        col_samples = QFrame()
        col_samples.setStyleSheet(f"background-color: {ui_theme.BG_SURFACE}; border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 4px; padding: 6px;")
        col_samples_l = QVBoxLayout(col_samples)
        lbl_smp = QLabel("📜 Muestra de Eventos Crudos Recientes")
        lbl_smp.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 11px; font-weight: bold;")
        col_samples_l.addWidget(lbl_smp)
        self.txt_drill_samples = QTextEdit()
        self.txt_drill_samples.setReadOnly(True)
        self.txt_drill_samples.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; color: {ui_theme.TEXT_PRIMARY}; border: none; font-family: {ui_theme.FONT_MONO}; font-size: 10px;")
        col_samples_l.addWidget(self.txt_drill_samples)
        drill_content.addWidget(col_samples, 2)

        drill_layout.addLayout(drill_content)
        splitter.addWidget(drill_panel)

        # Proporción: 60% tarjetas, 40% drilldown
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)
        layout.addWidget(splitter)

        self.current_selected_module = None
        self.th_latest_data = {}

    def _create_th_module_card(self, mod: dict) -> QFrame:
        card = QFrame()
        card.setCursor(Qt.PointingHandCursor)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_ELEVATED};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-radius: 6px;
                padding: 6px;
            }}
            QFrame:hover {{
                border-color: {ui_theme.ACCENT_CYBER};
                background-color: #0b1a2d;
            }}
        """)
        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(8, 8, 8, 8)
        c_layout.setSpacing(4)

        # Top row: Icon + Name
        top_h = QHBoxLayout()
        lbl_name = QLabel(str(mod['icon']) + " " + str(mod['name']))
        lbl_name.setObjectName("mod_name")
        lbl_name.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 11px; font-weight: bold;")
        top_h.addWidget(lbl_name)
        top_h.addStretch()

        lbl_cat = QLabel(mod["category"])
        lbl_cat.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 9px;")
        top_h.addWidget(lbl_cat)
        c_layout.addLayout(top_h)

        # Count Label
        lbl_count = QLabel("---")
        lbl_count.setObjectName("mod_count")
        lbl_count.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 16px; font-weight: bold; font-family: {ui_theme.FONT_MONO};")
        c_layout.addWidget(lbl_count)

        # Subtitle / Pct
        lbl_sub = QLabel("Esperando escaneo...")
        lbl_sub.setObjectName("mod_sub")
        lbl_sub.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px;")
        c_layout.addWidget(lbl_sub)

        # Event filter or click event
        card.mousePressEvent = lambda e, m=mod: self._on_th_card_clicked(m)
        return card

    def _refresh_threat_hunting_radar(self):
        scope_idx = self.cmb_th_scope.currentIndex()
        cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
        if scope_idx == 0:
            today_str = datetime.now().strftime("%Y.%m.%d")
            target_index = f"*{today_str}*{cust_id}*"
            scope_desc = "Hoy"
        elif scope_idx == 1:
            month_str = datetime.now().strftime("%Y.%m")
            target_index = f"*{month_str}*{cust_id}*"
            scope_desc = "Mes Actual"
        else:
            target_index = f"*{cust_id}*"
            scope_desc = "Histórico Total"

        self.lbl_th_stats.setText(f"⚡ Escaneando 20 módulos en paralelo [{scope_desc}]...")
        self.th_worker = ThreatHuntingRadarWorker(target_index)
        self.th_worker.finished.connect(self._on_th_radar_finished)
        self.th_worker.error.connect(self._on_th_radar_error)
        self.th_worker.start()

    def _on_th_radar_finished(self, data: dict):
        self.th_latest_data = data
        counts = data.get("counts", {})
        total_matched = data.get("total_matched", 0)
        elapsed = data.get("elapsed", 0.0)

        self.lbl_th_stats.setText(
            f"⚡ Matriz sincronizada en {elapsed:.2f}s | Total Eventos Detectados: {total_matched:,} | Índice: {data.get('target_index', '')}"
        )

        for mod in THREAT_HUNTING_MODULES_DEF:
            m_name = mod["name"]
            card = self.th_cards_map.get(m_name)
            if not card:
                continue
            cnt = counts.get(m_name, 0)
            lbl_count = card.findChild(QLabel, "mod_count")
            lbl_sub = card.findChild(QLabel, "mod_sub")

            if lbl_count:
                lbl_count.setText(f"{cnt:,}")
                if cnt > 1000000:
                    lbl_count.setStyleSheet(f"color: {ui_theme.COLOR_CRITICAL}; font-size: 16px; font-weight: bold; font-family: {ui_theme.FONT_MONO};")
                elif cnt > 100000:
                    lbl_count.setStyleSheet(f"color: {ui_theme.COLOR_HIGH}; font-size: 16px; font-weight: bold; font-family: {ui_theme.FONT_MONO};")
                elif cnt > 0:
                    lbl_count.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 16px; font-weight: bold; font-family: {ui_theme.FONT_MONO};")
                else:
                    lbl_count.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 16px; font-weight: bold; font-family: {ui_theme.FONT_MONO};")

            if lbl_sub:
                pct = (cnt / total_matched * 100) if total_matched > 0 else 0
                lbl_sub.setText(f"{pct:.1f}% del volumen | Clic para drilldown")

        # Si hay un modulo seleccionado, actualizarlo
        if self.current_selected_module:
            self._on_th_card_clicked(self.current_selected_module)
        else:
            # Seleccionar por defecto el modulo con mas eventos
            top_mod = max(THREAT_HUNTING_MODULES_DEF, key=lambda m: counts.get(m["name"], 0))
            self._on_th_card_clicked(top_mod)

    def _on_th_radar_error(self, err_msg: str):
        self.lbl_th_stats.setText(f"❌ Error en radar: {err_msg}")

    def _on_th_card_clicked(self, mod: dict):
        self.current_selected_module = mod
        self.lbl_drill_title.setText(f"🔍 Drilldown Forense: {mod['icon']} {mod['name']} ({mod['category']})")
        self.btn_copy_th_query.setEnabled(True)
        self.btn_jump_to_filter.setEnabled(True)

        self.txt_drill_actors.setText(f"Consultando agregaciones para {mod['name']}...")
        self.txt_drill_samples.setText(f"Cargando muestra forense de eventos...")

        scope_idx = self.cmb_th_scope.currentIndex()
        cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
        if scope_idx == 0:
            today_str = datetime.now().strftime("%Y.%m.%d")
            target_index = f"*{today_str}*{cust_id}*"
        elif scope_idx == 1:
            month_str = datetime.now().strftime("%Y.%m")
            target_index = f"*{month_str}*{cust_id}*"
        else:
            target_index = f"*{cust_id}*"

        self.drill_worker = ThreatHuntingDrilldownWorker(mod["name"], mod["query"], target_index)
        self.drill_worker.finished.connect(self._on_th_drilldown_finished)
        self.drill_worker.error.connect(self._on_th_drilldown_error)
        self.drill_worker.start()

    def _on_th_drilldown_finished(self, data: dict):
        m_name = data.get("module_name", "")
        total_docs = data.get("total_docs", 0)
        elapsed = data.get("elapsed", 0.0)

        # 1. Formatear Actores Top
        actors_lines = [
            f"=== TOP ACTORES ({m_name}) ===",
            f"Total coincidente: {total_docs:,} (en {elapsed:.2f}s)",
            "",
            "[Top Direcciones IP / Hosts Origen]"
        ]
        top_src = data.get("top_src_buckets", [])
        if top_src:
            for b in top_src:
                actors_lines.append(f"  • {b.get('key'):<25} : {b.get('doc_count'):,}")
        else:
            actors_lines.append("  • (Sin datos de srcip_host)")

        actors_lines.append("")
        actors_lines.append("[Top Direcciones IP / Hosts Destino]")
        top_dst = data.get("top_dst_buckets", [])
        if top_dst:
            for b in top_dst:
                actors_lines.append(f"  • {b.get('key'):<25} : {b.get('doc_count'):,}")
        else:
            actors_lines.append("  • (Sin datos de dstip_host)")

        actors_lines.append("")
        actors_lines.append("[Top Puertos Destino]")
        top_ports = data.get("top_ports_buckets", [])
        if top_ports:
            for b in top_ports:
                actors_lines.append(f"  • Puerto {b.get('key'):<18} : {b.get('doc_count'):,}")

        actors_lines.append("")
        actors_lines.append("[Top Clases de Mensaje]")
        top_msg = data.get("top_msg_class_buckets", [])
        if top_msg:
            for b in top_msg:
                actors_lines.append(f"  • {b.get('key'):<25} : {b.get('doc_count'):,}")

        self.txt_drill_actors.setText(chr(10).join(actors_lines))

        # 2. Formatear Muestra Cruda
        hits = data.get("hits", [])
        if hits:
            samples_lines = [f"=== MUESTRA DE REGISTROS ({len(hits)} eventos recientes) ==="]
            for i, h in enumerate(hits, 1):
                ts = h.get("timestamp") or h.get("write_time") or "N/A"
                src = h.get("srcip_host") or h.get("srcip") or h.get("host_name") or "-"
                dst = h.get("dstip_host") or h.get("dstip") or "-"
                sp = h.get("srcport", "-")
                dp = h.get("dstport", "-")
                cls = h.get("msg_class") or h.get("dev_type") or "N/A"
                act = h.get("action") or h.get("event_name") or h.get("fw_policy_id") or "-"
                samples_lines.append(f"[{i}] {ts} | {cls} | {src}:{sp} -> {dst}:{dp} | {act}")
                raw_json = json.dumps(h, indent=2, ensure_ascii=False)
                samples_lines.append(raw_json)
                samples_lines.append("-" * 50)
            self.txt_drill_samples.setText(chr(10).join(samples_lines))
        else:
            self.txt_drill_samples.setText("No se encontraron registros crudos para los criterios seleccionados.")

    def _on_th_drilldown_error(self, err_msg: str):
        self.txt_drill_actors.setText(f"Error al consultar agregaciones: {err_msg}")
        self.txt_drill_samples.setText(f"Error al obtener muestras: {err_msg}")

    def _copiar_th_query_dsl(self):
        if not self.current_selected_module:
            return
        query = self.current_selected_module.get("query", "")
        clipboard = QApplication.clipboard()
        clipboard.setText(query)
        msg_txt = f"La sintaxis Lucene / DSL para '{self.current_selected_module['name']}' se copió al portapapeles:" + chr(10) + chr(10) + query
        QMessageBox.information(self, "Query Copiado", msg_txt)

    def _copiar_resumen_th_radar(self):
        if not self.th_latest_data:
            return
        counts = self.th_latest_data.get("counts", {})
        total = self.th_latest_data.get("total_matched", 0)
        lines = [
            "TECHNOMA SOC - RADAR DE THREAT HUNTING (20 MÓDULOS)",
            f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Eventos Evaluados: {total:,}",
            "",
            f"{'MÓDULO':<30} | {'CATEGORÍA':<22} | {'EVENTOS':<12} | {'IMPACTO'}",
            "-" * 80
        ]
        for m in THREAT_HUNTING_MODULES_DEF:
            cnt = counts.get(m["name"], 0)
            pct = (cnt / total * 100) if total > 0 else 0
            lines.append(f"{m['name']:<30} | {m['category']:<22} | {cnt:>12,} | {pct:>6.1f}%")

        summary_text = chr(10).join(lines)
        clipboard = QApplication.clipboard()
        clipboard.setText(summary_text)
        QMessageBox.information(self, "Resumen Copiado", "El resumen de los 20 módulos se ha copiado al portapapeles en formato tabular.")

    def _saltar_a_filtro_con_modulo(self):
        if not self.current_selected_module:
            return
        mod = self.current_selected_module
        # Navegar a la pestaña 4 (Filtros & Asistente IA)
        self.tabs.setCurrentIndex(3)
        msg_txt = (
            f"Has seleccionado el módulo '{mod['name']}'." + chr(10) + chr(10) +
            f"Se ha abierto la pestaña de Auditoría de Log Filters." + chr(10) +
            f"Regla base para análisis:" + chr(10) + f"{mod['query']}" + chr(10) + chr(10) +
            "Consulta al Asistente IA para generar el filtro de descarte seguro sin generar puntos ciegos."
        )
        QMessageBox.information(self, "Creación de Filtro Quirúrgico", msg_txt)
'''

export_marker = "    def _exportar_evidencias_json(self):"
if export_marker in content:
    content = content.replace(export_marker, th_ui_methods + "\n" + export_marker)

# Write to both destinations
with open(target_soc_env, "w", encoding="utf-8") as f:
    f.write(content)

with open(target_soar, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully regenerated dialogs with forensic drilldown enhancements!")
