# -*- coding: utf-8 -*-
"""
Mixin Modular: Security Onion (Tab 7 - Grid & Network Intel),
Validador Pre-DPI BPF (Tab 8) y Centro Stellar Hunter & Gobernabilidad (Tab 9).
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
from soar_app.ui.tabs.stellar_hunter_tab import StellarHunterAndGovernanceWidget


class SecurityOnionMixin:
    # =========================================================================
    # TAB 7: 🧅 SECURITY ONION (GRID & NETWORK INTEL)
    # =========================================================================
    def _init_tab7_security_onion(self):
        """Inicializa la Pestana 7: Modulo Nativo de Inteligencia de Red y Caza Forense en Security Onion."""
        self.tab7 = QWidget()
        self.tabs.addTab(self.tab7, "🧅 Security Onion (Grid & Network Intel)")
        layout_tab7 = QVBoxLayout(self.tab7)
        layout_tab7.setContentsMargins(10, 8, 10, 8)
        layout_tab7.setSpacing(8)

        # ---------------------------------------------------------------------
        # 1. HEADER / ESTADO OPERATIVO DEL GRID (FAIL-SAFE & RESILIENTE)
        # ---------------------------------------------------------------------
        frame_so_top = QFrame()
        frame_so_top.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_so_top = QVBoxLayout(frame_so_top)
        layout_so_top.setContentsMargins(10, 8, 10, 8)
        layout_so_top.setSpacing(6)

        layout_top_row1 = QHBoxLayout()
        layout_top_row1.setSpacing(10)

        lbl_so_title = QLabel("🧅 SECURITY ONION OPENXDR GRID")
        lbl_so_title.setStyleSheet("color: #c084fc; font-weight: bold; font-size: 13px; font-family: 'Consolas'; border: none;")
        layout_top_row1.addWidget(lbl_so_title)

        self.lbl_so_grid_badge = QLabel("⚪ Verificando conectividad con el Grid de Security Onion...")
        self.lbl_so_grid_badge.setStyleSheet("""
            QLabel {
                background-color: #1e293b;
                color: #94a3b8;
                font-weight: bold;
                font-size: 11px;
                font-family: 'Consolas';
                padding: 3px 8px;
                border: 1px solid #334155;
                border-radius: 4px;
            }
        """)
        layout_top_row1.addWidget(self.lbl_so_grid_badge)
        layout_top_row1.addStretch()

        self.btn_so_refresh = QPushButton("🔄 Refrescar Grid")
        self.btn_so_refresh.setToolTip("Verifica el pulso de salud del cluster y nodos de Security Onion")
        self.btn_so_refresh.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_so_refresh.clicked.connect(self.trigger_so_health_refresh)
        layout_top_row1.addWidget(self.btn_so_refresh)

        layout_so_top.addLayout(layout_top_row1)

        # Fila 2: Detalles técnicos de topología y Circuit Breaker
        layout_top_row2 = QHBoxLayout()
        self.lbl_so_grid_details = QLabel("Elasticsearch: https://172.17.10.25:9200 | Malla ZeroTier: 10.92.248.0/24 (Nodo: secops-vascol)")
        self.lbl_so_grid_details.setStyleSheet("color: #64748b; font-size: 10px; font-family: 'Consolas'; border: none;")
        layout_top_row2.addWidget(self.lbl_so_grid_details)
        layout_top_row2.addStretch()

        lbl_cb_note = QLabel("⚡ Circuit Breaker Activo (1.0s fail-fast / 0ms en Home Office)")
        lbl_cb_note.setStyleSheet("color: #10b981; font-size: 10px; font-family: 'Consolas'; border: none;")
        layout_top_row2.addWidget(lbl_cb_note)
        layout_so_top.addLayout(layout_top_row2)

        layout_tab7.addWidget(frame_so_top)

        # ---------------------------------------------------------------------
        # 2. SUB-PESTAÑAS PRINCIPALES DEL MÓDULO SECURITY ONION
        # ---------------------------------------------------------------------
        self.tabs_so_main = QTabWidget()
        self.tabs_so_main.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #1e293b;
                background-color: #020617;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #0b1120;
                color: #94a3b8;
                border: 1px solid #1e293b;
                padding: 6px 14px;
                font-family: 'Consolas';
                font-size: 11px;
                font-weight: bold;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #020617;
                color: #c084fc;
                border-bottom: 2px solid #a855f7;
            }
            QTabBar::tab:hover:!selected {
                background-color: #1e293b;
                color: #f8fafc;
            }
        """)

        # Sub-pestaña 1: Caza Forense IOC
        tab_so_hunt = QWidget()
        self._build_so_hunt_subtab(tab_so_hunt)
        self.tabs_so_main.addTab(tab_so_hunt, "🎯 Caza Forense IOC (Zeek & Suricata)")

        # Sub-pestaña 2: Telemetría de Nodo Remoto
        tab_so_telemetry = QWidget()
        self._build_so_telemetry_subtab(tab_so_telemetry)
        self.tabs_so_main.addTab(tab_so_telemetry, "🖥️ Telemetría de Nodos (Syslog & Auditoría)")

        # Sub-pestaña 3: Topología & Arquitectura del Grid
        tab_so_arch = QWidget()
        self._build_so_architecture_subtab(tab_so_arch)
        self.tabs_so_main.addTab(tab_so_arch, "🌐 Arquitectura del Grid & Topología ZeroTier")

        layout_tab7.addWidget(self.tabs_so_main, 1)

    # -------------------------------------------------------------------------
    # CONSTRUCCIÓN: SUB-PESTAÑA 1 (CAZA FORENSE IOC)
    # -------------------------------------------------------------------------
    def _build_so_hunt_subtab(self, parent: QWidget):
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # Barra de control de búsqueda
        frame_hunt_ctrl = QFrame()
        frame_hunt_ctrl.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 4px;")
        layout_ctrl = QHBoxLayout(frame_hunt_ctrl)
        layout_ctrl.setContentsMargins(8, 6, 8, 6)
        layout_ctrl.setSpacing(8)

        lbl_ioc = QLabel("🔎 IOC Objetivo (IP / Dominio / Hash):")
        lbl_ioc.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_ctrl.addWidget(lbl_ioc)

        self.txt_so_hunt_ioc = QLineEdit()
        self.txt_so_hunt_ioc.setPlaceholderText("ej: 192.168.225.26, 10.92.248.156, bad-domain.com, sha256...")
        self.txt_so_hunt_ioc.setStyleSheet("""
            QLineEdit {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 4px 8px;
                font-family: 'Consolas';
                font-size: 11px;
            }
            QLineEdit:focus {
                border: 1px solid #a855f7;
            }
        """)
        self.txt_so_hunt_ioc.returnPressed.connect(self.trigger_so_hunt)
        layout_ctrl.addWidget(self.txt_so_hunt_ioc, 1)

        lbl_window = QLabel("Ventana:")
        lbl_window.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_ctrl.addWidget(lbl_window)

        self.cmb_so_hunt_days = QComboBox()
        self.cmb_so_hunt_days.addItems(["Últimas 24 Horas (1d)", "Últimos 7 Días (7d)", "Últimos 30 Días (30d)", "Últimos 90 Días (90d)"])
        self.cmb_so_hunt_days.setCurrentIndex(1)
        self.cmb_so_hunt_days.setStyleSheet("""
            QComboBox {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 6px;
                font-family: 'Consolas';
                font-size: 11px;
            }
        """)
        layout_ctrl.addWidget(self.cmb_so_hunt_days)

        self.btn_so_hunt_exec = QPushButton("🎯 Cazar en Security Onion")
        self.btn_so_hunt_exec.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_so_hunt_exec.clicked.connect(self.trigger_so_hunt)
        layout_ctrl.addWidget(self.btn_so_hunt_exec)

        self.btn_so_hunt_clear = QPushButton("🧹 Limpiar")
        self.btn_so_hunt_clear.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_so_hunt_clear.clicked.connect(self.clear_so_hunt_data)
        layout_ctrl.addWidget(self.btn_so_hunt_clear)

        layout.addWidget(frame_hunt_ctrl)

        # Marco de veredicto y métricas
        self.frame_so_verdict = QFrame()
        self.frame_so_verdict.setStyleSheet("background-color: #020617; border: 1px solid #1e293b; border-radius: 4px;")
        layout_verdict = QVBoxLayout(self.frame_so_verdict)
        layout_verdict.setContentsMargins(8, 6, 8, 6)
        layout_verdict.setSpacing(4)

        self.lbl_so_verdict_title = QLabel("Sin búsqueda activa. Ingrese un IOC y presione 'Cazar en Security Onion'.")
        self.lbl_so_verdict_title.setStyleSheet("color: #94a3b8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_verdict.addWidget(self.lbl_so_verdict_title)

        self.lbl_so_verdict_stats = QLabel("Zeek Hits: -- | Suricata Alerts: -- | Syslog Hits: -- | Hosts Internos Afectados: --")
        self.lbl_so_verdict_stats.setStyleSheet("color: #64748b; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_verdict.addWidget(self.lbl_so_verdict_stats)

        layout.addWidget(self.frame_so_verdict)

        # Splitter Vertical: Tablas de Eventos arriba / Ficha Forense abajo
        self.splitter_so_hunt = QSplitter(Qt.Vertical)
        self.splitter_so_hunt.setStyleSheet("QSplitter::handle { background-color: #1e293b; height: 3px; }")

        # Tablas de resultados en pestañas
        self.tabs_so_hunt_tables = QTabWidget()
        self.tabs_so_hunt_tables.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #1e293b;
                background-color: #020617;
            }
            QTabBar::tab {
                background-color: #0b1120;
                color: #94a3b8;
                border: 1px solid #1e293b;
                padding: 4px 10px;
                font-family: 'Consolas';
                font-size: 10px;
            }
            QTabBar::tab:selected {
                background-color: #020617;
                color: #38bdf8;
                border-bottom: 2px solid #0284c7;
            }
        """)

        # Tabla Zeek
        self.table_so_zeek = QTableWidget()
        self.table_so_zeek.setColumnCount(7)
        self.table_so_zeek.setHorizontalHeaderLabels(["Timestamp", "Protocolo / Stream", "IP Origen", "Puerto Orig", "IP Destino", "Puerto Dest", "Bytes"])
        self._apply_so_table_style(self.table_so_zeek)
        self.tabs_so_hunt_tables.addTab(self.table_so_zeek, "📡 Flujos de Red Zeek (.ds-logs-zeek-*)")

        # Tabla Suricata
        self.table_so_suricata = QTableWidget()
        self.table_so_suricata.setColumnCount(6)
        self.table_so_suricata.setHorizontalHeaderLabels(["Timestamp", "Severidad", "Firma de Detección (Signature)", "IP Origen", "IP Destino", "Puerto Dest"])
        self._apply_so_table_style(self.table_so_suricata)
        self.tabs_so_hunt_tables.addTab(self.table_so_suricata, "🚨 Detecciones NIDS Suricata (.ds-logs-suricata.alerts-*)")

        # Tabla Syslog / Firewall (FortiGate & Auditoría de Red)
        self.table_so_syslog = QTableWidget()
        self.table_so_syslog.setColumnCount(4)
        self.table_so_syslog.setHorizontalHeaderLabels(["Timestamp", "Host / Nodo", "Dataset / Fuente", "Mensaje / Registro Syslog Crudo"])
        self._apply_so_table_style(self.table_so_syslog)
        self.table_so_syslog.setColumnWidth(0, 180)
        self.table_so_syslog.setColumnWidth(1, 130)
        self.table_so_syslog.setColumnWidth(2, 120)
        self.table_so_syslog.setColumnWidth(3, 750)
        self.tabs_so_hunt_tables.addTab(self.table_so_syslog, "📜 Eventos Syslog & Firewall (.ds-logs-*syslog*)")

        self.splitter_so_hunt.addWidget(self.tabs_so_hunt_tables)

        # Panel inferior: Ficha Forense Markdown / Evidencia SOC
        frame_report = QFrame()
        frame_report.setStyleSheet("background-color: #020617; border: 1px solid #1e293b; border-radius: 4px;")
        layout_rep = QVBoxLayout(frame_report)
        layout_rep.setContentsMargins(6, 4, 6, 4)
        layout_rep.setSpacing(4)

        layout_rep_hdr = QHBoxLayout()
        lbl_rep_title = QLabel("📋 FICHA FORENSE DE EVIDENCIA (LISTA PARA CASO STELLAR CYBER):")
        lbl_rep_title.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_rep_hdr.addWidget(lbl_rep_title)
        layout_rep_hdr.addStretch()

        self.btn_so_copy_evidence = QPushButton("📋 Copiar Ficha al Portapapeles")
        self.btn_so_copy_evidence.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_so_copy_evidence.clicked.connect(self.copy_so_hunt_evidence)
        layout_rep_hdr.addWidget(self.btn_so_copy_evidence)
        layout_rep.addLayout(layout_rep_hdr)

        self.txt_so_hunt_report = QTextBrowser()
        self.txt_so_hunt_report.setOpenExternalLinks(True)
        self.txt_so_hunt_report.setStyleSheet("""
            QTextBrowser {
                background-color: #020617;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                font-family: 'Consolas';
                font-size: 11px;
                padding: 6px;
            }
        """)
        self.txt_so_hunt_report.setHtml("<span style='color: #64748b;'>Ejecute una consulta de IOC para generar la ficha forense estructurada...</span>")
        layout_rep.addWidget(self.txt_so_hunt_report, 1)

        self.splitter_so_hunt.addWidget(frame_report)
        self.splitter_so_hunt.setStretchFactor(0, 5)
        self.splitter_so_hunt.setStretchFactor(1, 5)

        layout.addWidget(self.splitter_so_hunt, 1)

    # -------------------------------------------------------------------------
    # CONSTRUCCIÓN: SUB-PESTAÑA 2 (TELEMETRÍA DE NODOS)
    # -------------------------------------------------------------------------
    def _build_so_telemetry_subtab(self, parent: QWidget):
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        frame_ctrl = QFrame()
        frame_ctrl.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 4px;")
        layout_ctrl = QHBoxLayout(frame_ctrl)
        layout_ctrl.setContentsMargins(8, 6, 8, 6)
        layout_ctrl.setSpacing(8)

        lbl_node = QLabel("Nodo:")
        lbl_node.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_ctrl.addWidget(lbl_node)

        self.cmb_so_telemetry_host = QComboBox()
        self.cmb_so_telemetry_host.addItems(["valores-ndr (Sensor NDR 192.168.40.232)", "secops-vascol (Sensor NDR 192.168.15.71)", "so-manager (Manager 172.17.10.25)"])
        self.cmb_so_telemetry_host.setStyleSheet("""
            QComboBox {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 6px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 240px;
            }
        """)
        layout_ctrl.addWidget(self.cmb_so_telemetry_host)

        lbl_limit = QLabel("Límite:")
        lbl_limit.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_ctrl.addWidget(lbl_limit)

        self.cmb_so_telemetry_limit = QComboBox()
        self.cmb_so_telemetry_limit.addItems(["25", "50", "100", "200"])
        self.cmb_so_telemetry_limit.setCurrentIndex(1)
        self.cmb_so_telemetry_limit.setStyleSheet("""
            QComboBox {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 6px;
                font-family: 'Consolas';
                font-size: 11px;
            }
        """)
        layout_ctrl.addWidget(self.cmb_so_telemetry_limit)

        self.btn_so_telemetry_fetch = QPushButton("📡 Cargar Telemetría de Sistema")
        self.btn_so_telemetry_fetch.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_so_telemetry_fetch.clicked.connect(self.trigger_so_telemetry)
        layout_ctrl.addWidget(self.btn_so_telemetry_fetch)

        layout_ctrl.addStretch()

        lbl_filter = QLabel("Filtrar:")
        lbl_filter.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none;")
        layout_ctrl.addWidget(lbl_filter)

        self.txt_so_telemetry_filter = QLineEdit()
        self.txt_so_telemetry_filter.setPlaceholderText("Filtrar por texto (ej: sudo, salt-minion, docker, iptables)...")
        self.txt_so_telemetry_filter.setStyleSheet("""
            QLineEdit {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 8px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 250px;
            }
        """)
        self.txt_so_telemetry_filter.textChanged.connect(self._filter_so_telemetry_table)
        layout_ctrl.addWidget(self.txt_so_telemetry_filter)

        layout.addWidget(frame_ctrl)

        self.table_so_telemetry = QTableWidget()
        self.table_so_telemetry.setColumnCount(4)
        self.table_so_telemetry.setHorizontalHeaderLabels(["Timestamp", "Host", "Proceso / Servicio", "Mensaje / Comando de Auditoría"])
        self._apply_so_table_style(self.table_so_telemetry)
        self.table_so_telemetry.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_so_telemetry.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table_so_telemetry.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table_so_telemetry.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        layout.addWidget(self.table_so_telemetry, 1)

        self.lbl_so_telemetry_stats = QLabel("Listo para consultar telemetría de nodos.")
        self.lbl_so_telemetry_stats.setStyleSheet("color: #64748b; font-family: 'Consolas'; font-size: 10px; border: none;")
        layout.addWidget(self.lbl_so_telemetry_stats)

    # -------------------------------------------------------------------------
    # CONSTRUCCIÓN: SUB-PESTAÑA 3 (ARQUITECTURA DEL GRID & TOPOLOGÍA)
    # -------------------------------------------------------------------------
    def _build_so_architecture_subtab(self, parent: QWidget):
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        scroll_content = QWidget()
        layout_scroll = QVBoxLayout(scroll_content)
        layout_scroll.setContentsMargins(0, 0, 0, 0)
        layout_scroll.setSpacing(10)

        # Tarjeta 1: Topología de Red y Componentes
        card_topo = QFrame()
        card_topo.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px;")
        layout_topo = QVBoxLayout(card_topo)
        layout_topo.setSpacing(6)

        lbl_t1 = QLabel("🌐 TOPOLOGÍA DEL GRID DE SEGURIDAD (SECURITY ONION + ZEROTIER)")
        lbl_t1.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_topo.addWidget(lbl_t1)

        txt_topo_desc = QLabel(
            "• <b>Manager Node (Local)</b>: <code>172.17.10.25</code> | Elasticsearch Clustered | 640 Shards Activos.<br>"
            "• <b>Remote Search Node (ZeroTier)</b>: <code>secops-vascol</code> (IP: <code>10.92.248.156</code>) | 225 Shards asignados | Heap 2GB | Sensoroni OK.<br>"
            "• <b>Elastic Agent Fleet Server</b>: Versión <code>9.3.3+build202604082258</code> con redirección DNAT por <code>172.17.10.25:8443</code> hacia <code>10.92.248.203</code>.<br>"
            "• <b>Túnel SD-WAN Seguro</b>: Red ZeroTier cifrada punto a punto con persistencia anti-highstate garantizada por systemd + crontab."
        )
        txt_topo_desc.setStyleSheet("color: #cbd5e1; font-family: 'Consolas'; font-size: 11px; border: none; line-height: 140%;")
        layout_topo.addWidget(txt_topo_desc)
        layout_scroll.addWidget(card_topo)

        # Tarjeta 2: Resiliencia Home Office y Modo Offline
        card_homeoffice = QFrame()
        card_homeoffice.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px;")
        layout_ho = QVBoxLayout(card_homeoffice)
        layout_ho.setSpacing(6)

        lbl_t2 = QLabel("🛡️ RESILIENCIA HOME OFFICE & POLÍTICA DE CERO BLOQUEO (CIRCUIT BREAKER)")
        lbl_t2.setStyleSheet("color: #10b981; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_ho.addWidget(lbl_t2)

        txt_ho_desc = QLabel(
            "• <b>Detección Instantánea</b>: Al trabajar desde casa sin VPN corporativa, el conector ejecuta un pre-vuelo no bloqueante de <b>1.0 segundo</b>.<br>"
            "• <b>Caché de Desconexión</b>: Tras detectar que <code>172.17.10.25</code> no responde, el conector entra en estado <code>OFFLINE</code> durante 45 segundos.<br>"
            "• <b>Cero Congelamiento</b>: Todas las llamadas a Security Onion responden en <b>0.0000 segundos</b> con un estado descriptivo, evitando que la GUI de PySide6 se cuelgue.<br>"
            "• <b>Independencia de Módulos</b>: Stellar Cyber, Gemini AI, Triaje, Playbooks, CTI (VirusTotal/AbuseIPDB) y CVE Intel siguen funcionando con el 100% de su rendimiento."
        )
        txt_ho_desc.setStyleSheet("color: #cbd5e1; font-family: 'Consolas'; font-size: 11px; border: none; line-height: 140%;")
        layout_ho.addWidget(txt_ho_desc)
        layout_scroll.addWidget(card_homeoffice)

        # Tarjeta 3: Protocolo Forense Zeek / Suricata
        card_forensic = QFrame()
        card_forensic.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px;")
        layout_fo = QVBoxLayout(card_forensic)
        layout_fo.setSpacing(6)

        lbl_t3 = QLabel("🔬 CAPACIDADES DE CAZA FORENSE EN DATALAKE DE SECURITY ONION")
        lbl_t3.setStyleSheet("color: #c084fc; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        layout_fo.addWidget(lbl_t3)

        txt_fo_desc = QLabel(
            "• <b>Flujos Zeek (.ds-logs-zeek-*)</b>: Búsqueda histórica de transacciones DNS, peticiones HTTP, handshakes TLS/SSL y sesiones TCP/UDP completas.<br>"
            "• <b>Firmas Suricata (.ds-logs-suricata.alerts-*)</b>: Correlación cruzada contra el motor de detección de intrusos de red NIDS y reglas ET Pro.<br>"
            "• <b>Pivoteo Dinámico desde Triaje</b>: Puede invocar la búsqueda de cualquier IP o dominio directamente desde la Ficha de Triaje usando el método <code>pivot_to_security_onion(ioc)</code>."
        )
        txt_fo_desc.setStyleSheet("color: #cbd5e1; font-family: 'Consolas'; font-size: 11px; border: none; line-height: 140%;")
        layout_fo.addWidget(txt_fo_desc)
        layout_scroll.addWidget(card_forensic)

        layout_scroll.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll, 1)

    # -------------------------------------------------------------------------
    # ESTILO COMÚN PARA TABLAS DE SECURITY ONION
    # -------------------------------------------------------------------------
    def _apply_so_table_style(self, table: QTableWidget):
        table.setStyleSheet("""
            QTableWidget {
                background-color: #020617;
                color: #f8fafc;
                gridline-color: #1e293b;
                border: 1px solid #1e293b;
                font-family: 'Consolas';
                font-size: 11px;
                selection-background-color: #1e293b;
                selection-color: #38bdf8;
            }
            QHeaderView::section {
                background-color: #0f172a;
                color: #94a3b8;
                padding: 4px 6px;
                font-weight: bold;
                border: 1px solid #1e293b;
                font-family: 'Consolas';
                font-size: 11px;
            }
        """)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setSelectionMode(QTableWidget.SingleSelection)
        table.setAlternatingRowColors(True)

    # -------------------------------------------------------------------------
    # GESTIÓN DE EVENTOS & WORKERS ASÍNCRONOS DE SECURITY ONION
    # -------------------------------------------------------------------------
    def trigger_so_health_refresh(self):
        """Dispara la verificación asíncrona del pulso de salud del Grid."""
        if hasattr(self, '_worker_so_health') and self._worker_so_health and self._worker_so_health.isRunning():
            return

        self.lbl_so_grid_badge.setText("⏳ Verificando pulso del Grid...")
        self.lbl_so_grid_badge.setStyleSheet("background-color: #1e293b; color: #f59e0b; font-weight: bold; font-family: 'Consolas'; padding: 3px 8px; border: 1px solid #334155; border-radius: 4px;")

        self._worker_so_health = SecurityOnionHealthWorker(self._so_engine)
        self._worker_so_health.health_signal.connect(self._on_so_health_finished)
        self._worker_so_health.error_signal.connect(self._on_so_health_error)
        self._worker_so_health.start()

    def _on_so_health_finished(self, data: dict):
        status = data.get("status", "offline")
        if status == "online":
            nodes_cnt = data.get("nodes_count", 0)
            shards_act = data.get("shards_active", 0)
            c_health = data.get("cluster_health", "green").upper()
            c_name = data.get("cluster_name", "so-elastic")

            self.lbl_so_grid_badge.setText(f"🟢 GRID ONLINE ({c_health}) — Nodos: {nodes_cnt} | Shards: {shards_act} | Cluster: {c_name}")
            self.lbl_so_grid_badge.setStyleSheet("background-color: #064e3b; color: #6ee7b7; font-weight: bold; font-family: 'Consolas'; padding: 3px 8px; border: 1px solid #059669; border-radius: 4px;")
            self.lbl_so_grid_details.setText(f"Elasticsearch: {self._so_engine.base_url} (ONLINE) | Nodos: Manager + secops-vascol + valores-ndr | Shards Asignados: {shards_act}")
        else:
            msg = data.get("message", "Fuera de red corporativa")
            self.lbl_so_grid_badge.setText(f"⚪ MODO HOME OFFICE / OFFLINE ({msg})")
            self.lbl_so_grid_badge.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; font-family: 'Consolas'; padding: 3px 8px; border: 1px solid #334155; border-radius: 4px;")
            self.lbl_so_grid_details.setText("Security Onion Desconectado: Modo Home Office detectado. Circuit Breaker activo (cero latencia en el Cockpit).")

    def _on_so_health_error(self, err: str):
        self.lbl_so_grid_badge.setText("⚪ SO GRID NO DISPONIBLE (HOME OFFICE)")
        self.lbl_so_grid_badge.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; font-family: 'Consolas'; padding: 3px 8px; border: 1px solid #334155; border-radius: 4px;")

    def trigger_so_hunt(self):
        """Ejecuta la caza forense del IOC ingresado en Security Onion."""
        ioc = self.txt_so_hunt_ioc.text().strip()
        if not ioc:
            QMessageBox.warning(self, "Caza en Security Onion", "Por favor ingrese un IOC (IP, Dominio o Hash) para consultar.")
            return

        # Parsear días de la ventana
        days = 7
        txt_combo = self.cmb_so_hunt_days.currentText()
        if "24 Horas" in txt_combo: days = 1
        elif "7 Días" in txt_combo: days = 7
        elif "30 Días" in txt_combo: days = 30
        elif "90 Días" in txt_combo: days = 90

        self.btn_so_hunt_exec.setEnabled(False)
        self.lbl_so_verdict_title.setText(f"🔎 Cazando IOC '{ioc}' en Zeek, Suricata y Syslog...")
        self.lbl_so_verdict_title.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        self.lbl_so_verdict_stats.setText("Consultando índices remotos en Security Onion Grid...")

        self._worker_so_hunt = SecurityOnionHuntWorker(self._so_engine, ioc, days=days)
        self._worker_so_hunt.hunt_signal.connect(self._on_so_hunt_finished)
        self._worker_so_hunt.error_signal.connect(self._on_so_hunt_error)
        self._worker_so_hunt.start()

    def _on_so_hunt_finished(self, res: dict):
        self.btn_so_hunt_exec.setEnabled(True)
        status = res.get("status")
        ioc = res.get("ioc", "")

        if status == "offline":
            self.lbl_so_verdict_title.setText("⚪ [MODO HOME OFFICE] Security Onion no disponible fuera de la red de oficina.")
            self.lbl_so_verdict_title.setStyleSheet("color: #94a3b8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
            self.lbl_so_verdict_stats.setText("El Circuit Breaker evitó el bloqueo de la GUI. Conéctese a la red corporativa para consultar Zeek/Suricata.")
            self.txt_so_hunt_report.setHtml(
                f"<div style='background-color: #0b1120; border: 1px solid #334155; padding: 10px; font-family: Consolas;'>"
                f"<b style='color: #f59e0b;'>⚠️ MODO REMOTO / HOME OFFICE DETECTADO</b><br><br>"
                f"El host <code>172.17.10.25</code> no es alcanzable desde su conexión actual.<br>"
                f"El Circuit Breaker de <b>so_engine</b> se activó para garantizar que su Cockpit responda a 60 FPS sin ningún congelamiento.<br>"
                f"<b>IOC solicitado:</b> <code>{he(ioc)}</code><br>"
                f"Cuando regrese a la oficina corporativa, esta consulta buscará automáticamente en más de 500,000 registros de Zeek y Suricata."
                f"</div>"
            )
            return

        if status != "online":
            self.lbl_so_verdict_title.setText(f"❌ Error al consultar Security Onion: {res.get('message', 'Error desconocido')}")
            self.lbl_so_verdict_title.setStyleSheet("color: #ef4444; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
            return

        # 1. Actualizar banner de veredicto
        v_label = res.get("verdict_label", "DESCONOCIDO")
        v_col = res.get("verdict_color", "#38bdf8")
        z_hits = res.get("zeek_hits", 0)
        s_hits = res.get("suricata_hits", 0)
        sys_hits = res.get("syslog_hits", 0)
        internal_hosts = res.get("internal_hosts", [])

        self.lbl_so_verdict_title.setText(f"VEREDICTO: {v_label} (IOC: {ioc})")
        self.lbl_so_verdict_title.setStyleSheet(f"color: {v_col}; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        self.lbl_so_verdict_stats.setText(
            f"Zeek Hits: {z_hits} | Suricata Alerts: {s_hits} | Syslog Hits: {sys_hits} | Hosts Internos Afectados: {len(internal_hosts)} {internal_hosts}"
        )

        # 2. Poblar tabla Zeek
        connections = res.get("connections", [])
        self.table_so_zeek.setRowCount(len(connections))
        for row, conn in enumerate(connections):
            self.table_so_zeek.setItem(row, 0, QTableWidgetItem(format_local_ts(conn.get("timestamp", ""))))
            self.table_so_zeek.setItem(row, 1, QTableWidgetItem(str(conn.get("protocol", ""))))
            self.table_so_zeek.setItem(row, 2, QTableWidgetItem(str(conn.get("src_ip", ""))))
            self.table_so_zeek.setItem(row, 3, QTableWidgetItem(str(conn.get("dest_port", ""))))
            self.table_so_zeek.setItem(row, 4, QTableWidgetItem(str(conn.get("dest_ip", ""))))
            self.table_so_zeek.setItem(row, 5, QTableWidgetItem(str(conn.get("dest_port", ""))))
            self.table_so_zeek.setItem(row, 6, QTableWidgetItem(str(conn.get("bytes", 0))))

        # 3. Poblar tabla Suricata
        alerts = res.get("alerts", [])
        self.table_so_suricata.setRowCount(len(alerts))
        for row, alt in enumerate(alerts):
            self.table_so_suricata.setItem(row, 0, QTableWidgetItem(format_local_ts(alt.get("timestamp", ""))))
            self.table_so_suricata.setItem(row, 1, QTableWidgetItem(str(alt.get("severity", ""))))
            self.table_so_suricata.setItem(row, 2, QTableWidgetItem(str(alt.get("signature", ""))))
            self.table_so_suricata.setItem(row, 3, QTableWidgetItem(str(alt.get("src_ip", ""))))
            self.table_so_suricata.setItem(row, 4, QTableWidgetItem(str(alt.get("dest_ip", ""))))
            self.table_so_suricata.setItem(row, 5, QTableWidgetItem(str(alt.get("dest_port", ""))))

        # 4. Poblar tabla Syslog / Firewall (FortiGate & Tráfico Perimetral)
        syslog_events = res.get("syslog_events", [])
        self.table_so_syslog.setRowCount(len(syslog_events))
        for row, ev in enumerate(syslog_events):
            self.table_so_syslog.setItem(row, 0, QTableWidgetItem(format_local_ts(ev.get("timestamp", ""))))
            self.table_so_syslog.setItem(row, 1, QTableWidgetItem(str(ev.get("host", ""))))
            self.table_so_syslog.setItem(row, 2, QTableWidgetItem(str(ev.get("dataset", ""))))
            self.table_so_syslog.setItem(row, 3, QTableWidgetItem(str(ev.get("message", ""))))

        # Auto-seleccionar la pestaña adecuada según los resultados
        if s_hits > 0:
            self.tabs_so_hunt_tables.setCurrentWidget(self.table_so_suricata)
        elif z_hits > 0:
            self.tabs_so_hunt_tables.setCurrentWidget(self.table_so_zeek)
        elif sys_hits > 0:
            self.tabs_so_hunt_tables.setCurrentWidget(self.table_so_syslog)

        # 5. Generar Ficha Forense HTML
        first_seen = format_local_ts(res.get("first_seen")) or "N/A"
        last_seen = format_local_ts(res.get("last_seen")) or "N/A"
        hosts_str = ", ".join(internal_hosts) if internal_hosts else "Ninguno identificado"

        report_html = (
            f"<div style='background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {v_col}; padding: 10px; font-family: Consolas; font-size: 11px;'>"
            f"<b style='color: #c084fc; font-size: 12px;'>FICHA DE CAZA FORENSE — SECURITY ONION OPENXDR</b><br>"
            f"<b>IOC Consultado:</b> <code>{he(ioc)}</code> ({res.get('ioc_type', '').upper()})<br>"
            f"<b>Veredicto de Red:</b> <b style='color: {v_col};'>{v_label}</b><br>"
            f"<b>Ventana Temporal Evaluada:</b> Últimos {res.get('query_window_days', 7)} días<br>"
            f"<b>Primera Detección (First Seen):</b> {first_seen}<br>"
            f"<b>Última Detección (Last Seen):</b> {last_seen}<br>"
            f"<b>Hosts Internos Comprometidos / Vinculados:</b> <code>{he(hosts_str)}</code><br>"
            f"<hr style='border: 0; border-top: 1px solid #1e293b; margin: 8px 0;'>"
            f"<b>Resumen de Métricas en DataLake:</b><br>"
            f"• Conexiones Zeek Registradas: <b>{z_hits}</b><br>"
            f"• Alertas NIDS Suricata Activas: <b>{s_hits}</b><br>"
            f"• Eventos de Syslog Vinculados: <b>{sys_hits}</b><br><br>"
            f"<b>Recomendación de Mitigación SOC:</b><br>"
        )

        if s_hits > 0:
            report_html += (
                f"<span style='color: #ef4444;'>🚨 <b>ACCION INMEDIATA:</b> Se detectaron firmas de intrusión activas en Suricata. "
                f"Bloquear el IOC en el Firewall de perímetro y aislar inmediatamente a los hosts internos vinculados: <code>{he(hosts_str)}</code>.</span>"
            )
        elif z_hits > 0:
            report_html += (
                f"<span style='color: #f59e0b;'>⚠️ <b>INVESTIGACIÓN REQUERIDA:</b> Existe tráfico de red en Zeek hacia este IOC, pero sin alertas de Suricata. "
                f"Verificar el volumen de bytes y tipo de servicio para descartar exfiltración o balizamiento (beaconing).</span>"
            )
        elif sys_hits > 0:
            samples_list = res.get("syslog_samples", [])
            samples_str = "<br>".join([f"• <code>{he(s)}</code>" for s in samples_list]) if samples_list else "Sin muestras disponibles"
            report_html += (
                f"<span style='color: #38bdf8;'>🛡️ <b>ACTIVIDAD DE FIREWALL / SYSLOG REGISTRADA ({sys_hits} eventos):</b><br>"
                f"Se detectaron trazas en los registros de auditoría o intentos de conexión bloqueados por el firewall (IPTables-dropped).<br>"
                f"<b>Muestras recientes:</b><br>{samples_str}</span>"
            )
        else:
            report_html += (
                f"<span style='color: #10b981;'>✅ <b>LIMPIO:</b> No se encontró tráfico ni alertas vinculadas a este IOC en el período analizado. "
                f"Es seguro considerar que no ha tenido impacto observable en la red local.</span>"
            )

        report_html += "</div>"
        self.txt_so_hunt_report.setHtml(report_html)

    def _on_so_hunt_error(self, err: str):
        self.btn_so_hunt_exec.setEnabled(True)
        self.lbl_so_verdict_title.setText(f"❌ Error durante la búsqueda: {err}")
        self.lbl_so_verdict_title.setStyleSheet("color: #ef4444; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")

    def clear_so_hunt_data(self):
        """Limpia todos los campos y tablas de la sub-pestaña de caza forense."""
        self.txt_so_hunt_ioc.clear()
        self.lbl_so_verdict_title.setText("Sin búsqueda activa. Ingrese un IOC y presione 'Cazar en Security Onion'.")
        self.lbl_so_verdict_title.setStyleSheet("color: #94a3b8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        self.lbl_so_verdict_stats.setText("Zeek Hits: -- | Suricata Alerts: -- | Syslog Hits: -- | Hosts Internos Afectados: --")
        self.table_so_zeek.setRowCount(0)
        self.table_so_suricata.setRowCount(0)
        self.table_so_syslog.setRowCount(0)
        self.txt_so_hunt_report.setHtml("<span style='color: #64748b;'>Ejecute una consulta de IOC para generar la ficha forense estructurada...</span>")

    def copy_so_hunt_evidence(self):
        """Copia el informe forense al portapapeles de Windows en texto plano."""
        text = self.txt_so_hunt_report.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Copiar Evidencia", "No hay evidencia forense generada para copiar.")
            return
        QApplication.clipboard().setText(text)
        QMessageBox.information(self, "Evidencia Copiada", "La ficha forense ha sido copiada exitosamente al Portapapeles.")

    def trigger_so_telemetry(self):
        """Dispara la recolección de telemetría reciente de auditoría y syslog."""
        raw_host = self.cmb_so_telemetry_host.currentText()
        host_name = "valores-ndr" if "valores-ndr" in raw_host else ("secops-vascol" if "secops-vascol" in raw_host else "so-manager")
        limit = int(self.cmb_so_telemetry_limit.currentText())

        self.btn_so_telemetry_fetch.setEnabled(False)
        self.lbl_so_telemetry_stats.setText(f"Recuperando los últimos {limit} eventos del nodo '{host_name}'...")

        self._worker_so_telemetry = SecurityOnionTelemetryWorker(self._so_engine, node_name=host_name, limit=limit)
        self._worker_so_telemetry.telemetry_signal.connect(self._on_so_telemetry_finished)
        self._worker_so_telemetry.error_signal.connect(self._on_so_telemetry_error)
        self._worker_so_telemetry.start()

    def _on_so_telemetry_finished(self, data: dict):
        self.btn_so_telemetry_fetch.setEnabled(True)
        status = data.get("status")
        if status == "offline":
            self.lbl_so_telemetry_stats.setText("⚪ Security Onion desconectado (Modo Home Office).")
            return
        if status != "online":
            self.lbl_so_telemetry_stats.setText(f"❌ Error al consultar telemetría: {data.get('message')}")
            return

        events = data.get("events", [])
        self._so_telemetry_items = events
        self.table_so_telemetry.setRowCount(len(events))
        for row, ev in enumerate(events):
            self.table_so_telemetry.setItem(row, 0, QTableWidgetItem(format_local_ts(ev.get("timestamp", ""))))
            self.table_so_telemetry.setItem(row, 1, QTableWidgetItem(str(data.get("host", ""))))
            self.table_so_telemetry.setItem(row, 2, QTableWidgetItem(str(ev.get("process", ""))))
            self.table_so_telemetry.setItem(row, 3, QTableWidgetItem(str(ev.get("message", ""))))

        self.lbl_so_telemetry_stats.setText(
            f"✅ Se cargaron {len(events)} eventos recientes del nodo '{data.get('host')}'. Total histórico en cluster: {data.get('count', 0):,} eventos."
        )

    def _on_so_telemetry_error(self, err: str):
        self.btn_so_telemetry_fetch.setEnabled(True)
        self.lbl_so_telemetry_stats.setText(f"❌ Error de comunicación: {err}")

    def _filter_so_telemetry_table(self, query: str):
        """Filtra la tabla de telemetría en tiempo real sin hacer consultas a la red."""
        query = query.strip().lower()
        for row in range(self.table_so_telemetry.rowCount()):
            match = False
            for col in range(self.table_so_telemetry.columnCount()):
                item = self.table_so_telemetry.item(row, col)
                if item and query in item.text().lower():
                    match = True
                    break
            self.table_so_telemetry.setRowHidden(row, not match if query else False)

    def pivot_to_security_onion(self, ioc: str):
        """
        Método de integración transversal: Permite a cualquier módulo del Cockpit
        pivotear inmediatamente a la pestaña de Security Onion para cazar un IOC.
        """
        if not ioc:
            return
        # Cambiar a la pestaña de Security Onion (índice de self.tab7)
        idx = self.tabs.indexOf(self.tab7)
        if idx >= 0:
            self.tabs.setCurrentIndex(idx)
        self.tabs_so_main.setCurrentIndex(0) # Sub-pestaña de Caza Forense
        self.txt_so_hunt_ioc.setText(ioc.strip())
        self.trigger_so_hunt()

    def _init_tab8_predpi_validator(self):
        """Inicializa la Pestana 8: Modulo de Auditoria y Validacion Sintactica Pre-DPI (BPF/eBPF)."""
        self.tab8 = QWidget()
        self.tabs.addTab(self.tab8, "🛡️ Pre-DPI BPF Validator")
        layout_tab8 = QVBoxLayout(self.tab8)
        layout_tab8.setContentsMargins(4, 4, 4, 4)
        layout_tab8.setSpacing(0)
        
        self.predpi_widget = PreDpiValidatorWidget(self)
        layout_tab8.addWidget(self.predpi_widget)


    def _init_tab9_stellar_hunter(self):
        """Inicializa la Pestaña 9: Centro Visual de Gobernabilidad de Queries, Cobertura de Dominios y Threat Hunting."""
        self.tab9 = QWidget()
        self.tabs.addTab(self.tab9, "🔍 Queries, Dominios & Hunter")
        layout_tab9 = QVBoxLayout(self.tab9)
        layout_tab9.setContentsMargins(4, 4, 4, 4)
        layout_tab9.setSpacing(0)

        self.stellar_hunter_widget = StellarHunterAndGovernanceWidget(self)
        layout_tab9.addWidget(self.stellar_hunter_widget)
