# -*- coding: utf-8 -*-
"""
Ventana Principal Unificada (XdrDashboard) del Command Center v6.5.2 Modular.
Integra todos los Mixins de pestañas, el SOCWindowManager estandarizado
y la barra inferior de ventanas/módulos activos.
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
from soar_app.workers.auto_remediators import *
from soar_app.ui.window_manager import SOCWindowManager
from soar_app.ui.tabs.triage_ops_mixin import TriageOpsMixin
from soar_app.ui.tabs.analytics_playbooks_mixin import AnalyticsPlaybooksMixin
from soar_app.ui.tabs.terminal_cti_mixin import TerminalCtiMixin
from soar_app.ui.tabs.cve_intel_mixin import CveIntelMixin
from soar_app.ui.tabs.security_onion_mixin import SecurityOnionMixin


class XdrDashboard(
    QMainWindow,
    TriageOpsMixin,
    AnalyticsPlaybooksMixin,
    TerminalCtiMixin,
    CveIntelMixin,
    SecurityOnionMixin
):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STELLAR CYBER OpenXDR - CENTRAL COMMAND MASTER COCKPIT v6.5.1s")
        self.resize(1550, 920)
        self.dict_casos_activos = {}
        
        self.estados_anteriores = {}
        self.pool_excedido_anterior = False
        self.primer_ciclo = True

        # Playbook 6.3 - Gestor de Anomalías de Ingesta & Bitácora Automática
        self.last_ingestion_ticket_data = None
        self.last_ingestion_bitacora_row = ""
        self.last_ingestion_alert_dispatched_date = ""
        self.last_ingestion_pdf_path = ""
        
        # Sistema de caché local RAM SOAR con límites LRU
        self.cache_triage = LRUCache(maxsize=30)
        self.cache_interflow = LRUCache(maxsize=50)
        self.cache_ai = LRUCache(maxsize=30)
        
        # Bandera de relanzamiento de análisis IA asíncrono
        self.pending_ai_after_triage = False

        # Variables de estado para filtrado y paginacion de casos SOAR
        self._cases_current_page = 1
        self._cases_filtered_list = []

        # Modulo Anti-Sleep nativo para prevencion continua de suspension de Windows
        self._antisleep_active = True
        self._timer_antisleep = QTimer(self)
        self._timer_antisleep.timeout.connect(self._refresh_antisleep)

        # Inicialización del sistema de diseño (fuentes Outfit y QSS unificado)
        ui_theme.init_soc_fonts(SCRIPT_DIR)
        self.setStyleSheet(ui_theme.MASTER_QSS)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Base layout for main widget
        base_layout = QVBoxLayout(main_widget)
        base_layout.setContentsMargins(0, 0, 0, 0)
        base_layout.setSpacing(0)

        # =========================================================================
        # BARRA SUPERIOR GLOBAL DE NAVEGACIÓN Y SUITE DE SEGURIDAD (GLOBAL HEADER)
        # =========================================================================
        top_header = QFrame()
        top_header.setObjectName("topHeaderFrame")
        layout_header = QHBoxLayout(top_header)
        layout_header.setContentsMargins(14, 8, 14, 8)
        layout_header.setSpacing(12)

        # Branding: Logo y Nombre
        layout_brand = QHBoxLayout()
        layout_brand.setSpacing(8)
        lbl_logo = QLabel()
        logo_path = os.path.join(SCRIPT_DIR, "logo-technoma.png")
        if os.path.exists(logo_path):
            from PySide6.QtGui import QPixmap
            pixmap = QPixmap(logo_path)
            if not pixmap.isNull():
                lbl_logo.setPixmap(pixmap.scaledToHeight(24, Qt.SmoothTransformation))
                layout_brand.addWidget(lbl_logo)

        lbl_app_title = QLabel("TECHNOMA SOC")
        lbl_app_title.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 13px; font-weight: bold; border: none; font-family: {ui_theme.FONT_MAIN}; letter-spacing: 0.5px;")
        lbl_app_badge = QLabel("OpenXDR Cockpit")
        lbl_app_badge.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; background-color: #0f2438; border: 1px solid #0369a1; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 600; font-family: {ui_theme.FONT_MAIN};")
        layout_brand.addWidget(lbl_app_title)
        layout_brand.addWidget(lbl_app_badge)
        layout_header.addLayout(layout_brand)

        layout_header.addStretch(1)

        # Acceso Directo a Satélites de la Suite (1-Click Launchers)
        layout_suite_tools = QHBoxLayout()
        layout_suite_tools.setSpacing(6)

        btn_h_phishing = QPushButton("✉️ Phishing Headers")
        btn_h_phishing.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        btn_h_phishing.setToolTip("Abrir Analizador Forense de Cabeceras (.eml)")
        btn_h_phishing.clicked.connect(self.open_email_header_analyzer)

        btn_h_ticket = QPushButton("🎫 Ticket Oficial THN")
        btn_h_ticket.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_HIGH))
        btn_h_ticket.setToolTip("Abrir Generador Oficial de Tickets Technoma (FL-THN-POS-01)")
        btn_h_ticket.clicked.connect(self.open_thn_ticket_generator)

        btn_h_abuse = QPushButton("🚨 Reporte de Abuso")
        btn_h_abuse.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_CRITICAL))
        btn_h_abuse.setToolTip("Abrir Generador y Despachador de Reportes de Abuso")
        btn_h_abuse.clicked.connect(self.open_abuse_report_dialog)

        btn_h_feeds = QPushButton("🌐 CTI Feeds & IOCs")
        btn_h_feeds.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_PURPLE))
        btn_h_feeds.setToolTip("Abrir Módulo de Inteligencia de Amenazas y Feeds")
        btn_h_feeds.clicked.connect(self.open_feeds_intel_module)

        btn_h_ingesta = QPushButton("📊 Ingesta & Cuota")
        btn_h_ingesta.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_PRIMARY))
        btn_h_ingesta.setToolTip("Abrir Centro de Auditoría Forense de Ingesta, Control de Cuota Stellar Cyber y Log Filters")
        btn_h_ingesta.clicked.connect(self._abrir_auditoria_ingesta_dialog)

        btn_h_hunter = QPushButton("🔍 Queries & Dominios")
        btn_h_hunter.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        btn_h_hunter.setToolTip("Abrir Inspector de Queries, Simulador de Cobertura de Dominios en Log Filters y Threat Hunter")
        btn_h_hunter.clicked.connect(self.open_stellar_hunter_window)

        btn_h_logfilter = QPushButton("➕ Creador Filtros")
        btn_h_logfilter.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_SUCCESS))
        btn_h_logfilter.setToolTip("Abrir Creador y Gestor de Log Filters Quirúrgicos (API Stellar Cyber)")
        btn_h_logfilter.clicked.connect(self.open_log_filter_creator)

        btn_h_agent = QPushButton("🤖 Agente SOC IA")
        btn_h_agent.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_MEDIUM))
        btn_h_agent.setToolTip("Abrir Agente Autónomo SOC con Ventana Estandarizada Acoplable")
        btn_h_agent.clicked.connect(self.open_soc_agent_window)

        layout_suite_tools.addWidget(btn_h_phishing)
        layout_suite_tools.addWidget(btn_h_ticket)
        layout_suite_tools.addWidget(btn_h_abuse)
        layout_suite_tools.addWidget(btn_h_feeds)
        layout_suite_tools.addWidget(btn_h_ingesta)
        layout_suite_tools.addWidget(btn_h_hunter)
        layout_suite_tools.addWidget(btn_h_logfilter)
        layout_suite_tools.addWidget(btn_h_agent)
        layout_header.addLayout(layout_suite_tools)

        layout_header.addStretch(1)

        # Telemetría de Estado en Vivo (Anti-Sleep)
        layout_header_status = QHBoxLayout()
        layout_header_status.setSpacing(8)

        lbl_hdr_antisleep = QLabel("🛡️ ANTI-SLEEP")
        lbl_hdr_antisleep.setStyleSheet(f"color: {ui_theme.COLOR_SUCCESS}; background-color: #064e3b; border: 1px solid #10b981; border-radius: 4px; padding: 3px 8px; font-size: 10px; font-weight: bold; font-family: {ui_theme.FONT_MAIN};")
        lbl_hdr_antisleep.setToolTip("Prevención activa de suspensión de pantalla de Windows en turnos 24/7")

        layout_header_status.addWidget(lbl_hdr_antisleep)
        layout_header.addLayout(layout_header_status)

        base_layout.addWidget(top_header)
        
        # Tabs principales + Gestor Unificado de Ventanas y Módulos (SOCWindowManager)
        self.tabs = QTabWidget()
        base_layout.addWidget(self.tabs, 1)
        self.window_manager = SOCWindowManager(self, self.tabs)
        self.soc_taskbar_widget = self.window_manager.create_taskbar_widget()
        base_layout.addWidget(self.soc_taskbar_widget)
        
        # --- TAB 1: DASHBOARD & TRIAGE ---
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "🛡️ Triaje & Operaciones")
        
        tab1_layout = QVBoxLayout(self.tab1)
        tab1_layout.setContentsMargins(10, 8, 10, 8)
        tab1_layout.setSpacing(8)

        # =========================================================================
        # BANNER DE KPIS EN TIEMPO REAL (100% EN MEMORIA / CERO LLAMADAS API EXTRA)
        # =========================================================================
        frame_kpis = QFrame()
        frame_kpis.setStyleSheet(f"background-color: {ui_theme.BG_SURFACE}; border: 1px solid {ui_theme.BORDER_SUBTLE}; border-radius: 6px;")
        layout_kpis = QHBoxLayout(frame_kpis)
        layout_kpis.setContentsMargins(8, 6, 8, 6)
        layout_kpis.setSpacing(8)

        def _create_kpi_card(title: str, default_val: str, accent_color: str):
            card = QFrame()
            card.setStyleSheet(ui_theme.kpi_card_style(accent_color))
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(10, 6, 10, 6)
            card_layout.setSpacing(2)
            
            lbl_title = QLabel(title)
            lbl_title.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px; font-weight: 600; border: none; font-family: {ui_theme.FONT_MAIN};")
            
            lbl_val = QLabel(default_val)
            lbl_val.setStyleSheet(f"color: {accent_color}; font-size: 18px; font-weight: bold; border: none; font-family: {ui_theme.FONT_MAIN};")
            
            card_layout.addWidget(lbl_title)
            card_layout.addWidget(lbl_val)
            return card, lbl_val

        card_crit, self.kpi_crit_high = _create_kpi_card("🔴 CRÍTICOS & ALTOS", "-", ui_theme.COLOR_CRITICAL)
        card_unass, self.kpi_unassigned = _create_kpi_card("🟡 SIN ASIGNAR", "-", ui_theme.COLOR_MEDIUM)
        card_inprog, self.kpi_in_progress = _create_kpi_card("🔵 EN CURSO", "-", ui_theme.ACCENT_CYBER)
        card_resolv, self.kpi_resolved = _create_kpi_card("🟢 RESUELTOS (24H)", "-", ui_theme.COLOR_SUCCESS)
        card_mttd, self.kpi_avg_mttd = _create_kpi_card("⏱️ MTTD PROM.", "-", ui_theme.ACCENT_CYBER)
        card_sla, self.kpi_sla_compliance = _create_kpi_card("🎯 SLA CUMPLIDO", "-", ui_theme.COLOR_SUCCESS)
        card_score, self.kpi_risk_score = _create_kpi_card("⚡ SCORE RIESGO", "-", ui_theme.COLOR_PURPLE)
        card_alerts, self.kpi_total_alerts = _create_kpi_card("🛡️ TOTAL ALERTAS", "-", ui_theme.COLOR_INDIGO)

        layout_kpis.addWidget(card_crit)
        layout_kpis.addWidget(card_unass)
        layout_kpis.addWidget(card_inprog)
        layout_kpis.addWidget(card_resolv)
        layout_kpis.addWidget(card_mttd)
        layout_kpis.addWidget(card_sla)
        layout_kpis.addWidget(card_score)
        layout_kpis.addWidget(card_alerts)

        tab1_layout.addWidget(frame_kpis)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        tab1_layout.addLayout(grid_layout)

        # PANEL 0: TOP PROTOCOLS (COLUMNA IZQUIERDA ARRIBA) - WIDGET CYBER MODERNO
        self.txt_protocols = CyberTopProtocolsWidget()
        grid_layout.addWidget(self.txt_protocols, 0, 0, 1, 1)

        # PANEL 1: MONITOR DE SALUD E INGESTA TOTAL - WIDGET CYBER MODERNO
        frame_health = QFrame()
        frame_health.setStyleSheet("background-color: transparent; border: none;")
        layout_h = QVBoxLayout(frame_health)
        layout_h.setContentsMargins(0, 0, 0, 0)
        layout_h.setSpacing(6)
        self.txt_health = CyberInfrastructureHealthWidget()
        layout_h.addWidget(self.txt_health, 1)

        # BARRA DE CONTROL AUTOMÁTICO PLAYBOOK 6.3 (GESTIÓN DE INGESTA & BITÁCORA)
        bar_pb63 = QFrame()
        bar_pb63.setStyleSheet(f"background-color: {ui_theme.BG_INPUT}; border: 1px solid {ui_theme.BORDER_SUBTLE}; border-radius: 5px;")
        layout_pb63 = QHBoxLayout(bar_pb63)
        layout_pb63.setContentsMargins(6, 4, 6, 4)
        layout_pb63.setSpacing(6)

        self.lbl_ingestion_badge = QLabel("INGESTA: CALCULANDO...")
        self.lbl_ingestion_badge.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; font-size: 11px; background-color: {ui_theme.BG_ELEVATED}; padding: 4px 8px; border-radius: 4px; border: 1px solid {ui_theme.BORDER_MUTED}; font-family: {ui_theme.FONT_MAIN};")
        layout_pb63.addWidget(self.lbl_ingestion_badge)

        self.btn_copiar_bitacora_ingesta = QPushButton("📋 Copiar Bitácora (PB 6.3)")
        self.btn_copiar_bitacora_ingesta.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_SUCCESS))
        self.btn_copiar_bitacora_ingesta.setToolTip("Copia al portapapeles la fila de 18 columnas de Playbook 6.3 lista para pegar en Excel/Sheets")
        self.btn_copiar_bitacora_ingesta.clicked.connect(self._copiar_bitacora_ingesta_clip)
        self.btn_copiar_bitacora_ingesta.setEnabled(False)
        layout_pb63.addWidget(self.btn_copiar_bitacora_ingesta)

        self.btn_abrir_ticket_ingesta = QPushButton("🎫 Abrir Ticket Escalación (N2)")
        self.btn_abrir_ticket_ingesta.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_CRITICAL))
        self.btn_abrir_ticket_ingesta.setToolTip("Abre la ventana interactiva de ticket con los datos del sobreconsumo pre-cargados para escalación a N2")
        self.btn_abrir_ticket_ingesta.clicked.connect(self._abrir_ticket_ingesta_dialog)
        self.btn_abrir_ticket_ingesta.setEnabled(False)
        layout_pb63.addWidget(self.btn_abrir_ticket_ingesta)

        self.btn_export_pdf_ingesta = QPushButton("📄 Ver / Exportar PDF")
        self.btn_export_pdf_ingesta.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_HIGH))
        self.btn_export_pdf_ingesta.setToolTip("Abre o exporta el ticket formal de Playbook 6.3 en documento PDF corporativo con membrete oficial")
        self.btn_export_pdf_ingesta.clicked.connect(self._abrir_pdf_ingesta)
        self.btn_export_pdf_ingesta.setEnabled(False)
        layout_pb63.addWidget(self.btn_export_pdf_ingesta)

        self.btn_auditoria_ingesta = QPushButton("🔍 Telemetría & Log Filters")
        self.btn_auditoria_ingesta.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_PURPLE))
        self.btn_auditoria_ingesta.setToolTip("Abre el Centro de Auditoría Forense de Ingesta, Monitoreo de Conectores Cloud e Inventario de Log Filters con Detección de Cegueras SOC")
        self.btn_auditoria_ingesta.clicked.connect(self._abrir_auditoria_ingesta_dialog)
        layout_pb63.addWidget(self.btn_auditoria_ingesta)

        self.btn_creador_log_filters = QPushButton("➕ Creador Log Filters (API)")
        self.btn_creador_log_filters.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        self.btn_creador_log_filters.setToolTip("Diseña, valida sintaxis sin ceguera y despliega Log Filters en Stellar Cyber vía API")
        self.btn_creador_log_filters.clicked.connect(self.open_log_filter_creator)
        layout_pb63.addWidget(self.btn_creador_log_filters)

        layout_h.addWidget(bar_pb63)
        grid_layout.addWidget(frame_health, 1, 0)

        # PANEL 2: QUEUE SOAR DE CASOS VIVOS CON RE-ACTIVACIÓN DE REFRESH (DERECHA ROW 0)
        frame_cases = QFrame()
        layout_c = QVBoxLayout(frame_cases)
        
        layout_c_header = QHBoxLayout()
        lbl_c_title = QLabel("  COLA DE INCIDENTES ACTIVOS (SOAR QUEUE)")
        lbl_c_title.setStyleSheet(ui_theme.section_header_style(ui_theme.ACCENT_CYBER))
        self.btn_manual_refresh = QPushButton("Refrescar Cola")
        self.btn_manual_refresh.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_manual_refresh.clicked.connect(self.trigger_cases_refresh)
        layout_c_header.addWidget(lbl_c_title)
        layout_c_header.addWidget(self.btn_manual_refresh)
        
        self.lbl_api_health = QLabel("API EN LÍNEA")
        self.lbl_api_health.setStyleSheet(f"color: {ui_theme.COLOR_SUCCESS}; font-size: 11px; font-weight: bold; padding: 2px 8px; background-color: #064e3b; border-radius: 4px; border: 1px solid #10b981; font-family: {ui_theme.FONT_MAIN};")
        layout_c_header.addWidget(self.lbl_api_health)

        # Menu desplegable unificado para motores SOAR (Auto-Guardia y Auto-Remediadores)
        self.btn_soar_menu = QToolButton()
        self.btn_soar_menu.setPopupMode(QToolButton.InstantPopup)
        self.btn_soar_menu.setStyleSheet("""
            QToolButton {
                background-color: #0f172a;
                color: #38bdf8;
                border: 1px solid #0284c7;
                border-radius: 4px;
                padding: 4px 10px;
                font-family: 'Consolas';
                font-size: 11px;
                font-weight: bold;
            }
            QToolButton:hover {
                background-color: #1e293b;
                border-color: #38bdf8;
            }
            QToolButton::menu-indicator {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                padding-right: 4px;
            }
            QMenu {
                background-color: #0b1120;
                border: 1px solid #0284c7;
                border-radius: 6px;
                color: #f8fafc;
                font-family: 'Consolas';
                font-size: 11px;
                padding: 6px 4px;
            }
            QMenu::item {
                background-color: transparent;
                color: #f8fafc;
                padding: 6px 28px 6px 28px;
                border-radius: 4px;
                margin: 2px 4px;
            }
            QMenu::item:selected {
                background-color: #1e293b;
                color: #38bdf8;
            }
            QMenu::item:checked {
                color: #38bdf8;
                font-weight: bold;
            }
            QMenu::item:disabled {
                color: #64748b;
            }
        """)

        self.soar_menu = QMenu(self.btn_soar_menu)
        self.soar_menu.setStyleSheet("""
            QMenu {
                background-color: #0b1120;
                border: 1px solid #0284c7;
                border-radius: 6px;
                color: #f8fafc;
                font-family: 'Consolas';
                font-size: 11px;
                padding: 6px 4px;
            }
            QMenu::item {
                background-color: transparent;
                color: #f8fafc;
                padding: 6px 28px 6px 28px;
                border-radius: 4px;
                margin: 2px 4px;
            }
            QMenu::item:selected {
                background-color: #1e293b;
                color: #38bdf8;
            }
            QMenu::item:checked {
                color: #38bdf8;
                font-weight: bold;
            }
            QMenu::item:disabled {
                color: #64748b;
            }
        """)

        self.action_soar_guardia = QAction("Auto-Guardia SLA (Proteccion Turno)", self)
        self.action_soar_guardia.setCheckable(True)
        self.action_soar_guardia.setChecked(False)
        self.action_soar_guardia.setToolTip("Auto-asigna casos libres antes de vencer el MTTD si nadie del turno los tomo")
        self.action_soar_guardia.toggled.connect(self._update_soar_menu_label)

        self.action_soar_hm = QAction("Auto-Cierre HealthMailbox (Ley de Oro)", self)
        self.action_soar_hm.setCheckable(True)
        self.action_soar_hm.setChecked(False)
        self.action_soar_hm.setToolTip("Auto-toma y resuelve como False Positive los casos de HealthMailbox bajo la Ley de Oro")
        self.action_soar_hm.toggled.connect(self._update_soar_menu_label)

        self.action_soar_translate = QAction("Auto-Cierre Sophos Translate", self)
        self.action_soar_translate.setCheckable(True)
        self.action_soar_translate.setChecked(False)
        self.action_soar_translate.setToolTip("Auto-toma y resuelve como False Positive los casos de Sophos WebControl hacia translate.google.com")
        self.action_soar_translate.toggled.connect(self._update_soar_menu_label)

        self.action_soar_sati = QAction("Auto-Cierre SATI VPN (DNS 53 Failover)", self)
        self.action_soar_sati.setCheckable(True)
        self.action_soar_sati.setChecked(False)
        self.action_soar_sati.setToolTip("Auto-toma y resuelve como False Positive las denegaciones en firewall de consultas DNS desde VPN del proveedor SATI")
        self.action_soar_sati.toggled.connect(self._update_soar_menu_label)

        self.action_soar_dpapi = QAction("Auto-Cierre DPAPI (protected_storage)", self)
        self.action_soar_dpapi.setCheckable(True)
        self.action_soar_dpapi.setChecked(False)
        self.action_soar_dpapi.setToolTip("Auto-toma y resuelve como False Positive accesos legítimos de Windows DPAPI a protected_storage en VMBASE8")
        self.action_soar_dpapi.toggled.connect(self._update_soar_menu_label)

        self.soar_menu.addAction(self.action_soar_guardia)
        self.soar_menu.addAction(self.action_soar_hm)
        self.soar_menu.addAction(self.action_soar_translate)
        self.soar_menu.addAction(self.action_soar_sati)
        self.soar_menu.addAction(self.action_soar_dpapi)
        self.btn_soar_menu.setMenu(self.soar_menu)

        # Alias retrocompatibles para mantener intacto cualquier acceso existente
        self.check_auto_guardia = self.action_soar_guardia
        self.check_auto_healthmailbox = self.action_soar_hm
        self.check_auto_sophos_translate = self.action_soar_translate
        self.check_auto_sati = self.action_soar_sati
        self.check_auto_dpapi = self.action_soar_dpapi

        self._update_soar_menu_label()

        self.check_mobile_alerts = QCheckBox("Notif. Movil (ntfy)")
        self.check_mobile_alerts.setChecked(True)
        self.check_mobile_alerts.setToolTip("Enviar notificaciones push a tu celular via ntfy (POE, MTTD, MTTR, Nuevos Casos, Asignaciones)")
        self.check_mobile_alerts.setStyleSheet("color: #a855f7; font-family: 'Consolas'; font-size: 11px; font-weight: bold;")

        self.btn_test_mobile = QPushButton("Probar Movil")
        self.btn_test_mobile.setToolTip("Enviar notificacion push de prueba a la app ntfy en tu celular")
        self.btn_test_mobile.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_test_mobile.clicked.connect(self.test_mobile_notification_action)

        layout_c_header.addWidget(self.btn_soar_menu)
        layout_c_header.addWidget(self.check_mobile_alerts)
        layout_c_header.addWidget(self.btn_test_mobile)

        # Barra de Filtros, Estado y Ordenamiento de Casos
        frame_cases_tools = QFrame()
        frame_cases_tools.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 4px;")
        layout_cases_tools = QHBoxLayout(frame_cases_tools)
        layout_cases_tools.setContentsMargins(6, 4, 6, 4)
        layout_cases_tools.setSpacing(6)

        lbl_f = QLabel("Filtro:")
        lbl_f.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 11px; border: none;")

        self.input_cases_search = QLineEdit()
        self.input_cases_search.setPlaceholderText("Buscar por Ticket ID, Alerta, Tenant, Analista (Enter p/ On-Demand)...")
        self.input_cases_search.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.input_cases_search.textChanged.connect(self._on_cases_filter_changed)
        self.input_cases_search.returnPressed.connect(self._on_cases_search_return_pressed)

        self.combo_cases_status = QComboBox()
        self.combo_cases_status.addItems(["Activos", "Cerrados", "Todos"])
        self.combo_cases_status.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_status.currentIndexChanged.connect(self._on_cases_filter_changed)

        self.combo_cases_time = QComboBox()
        self.combo_cases_time.addItems([
            "Tiempo: 24 Horas",
            "Tiempo: 1 Hora",
            "Tiempo: 12 Horas",
            "Tiempo: 7 Días",
            "Tiempo: 30 Días (1M)",
            "Tiempo: Todo el Historial"
        ])
        self.combo_cases_time.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_time.currentIndexChanged.connect(self._on_cases_filter_changed)

        self.combo_cases_priority = QComboBox()
        self.combo_cases_priority.addItems(["Prioridad: Todas", "P1 (Critica)", "P2 (Alta)", "P3 (Media)", "P4 (Baja)"])
        self.combo_cases_priority.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_priority.currentIndexChanged.connect(self._on_cases_filter_changed)

        self.combo_cases_assignee = QComboBox()
        self.combo_cases_assignee.addItems(["Asignacion: Todas", "Solo Libres", "Asignados a Mi", "Asignados a Otros"])
        self.combo_cases_assignee.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_assignee.currentIndexChanged.connect(self._on_cases_filter_changed)

        self.combo_cases_sort = QComboBox()
        self.combo_cases_sort.addItems([
            "Orden: Mayor Score", 
            "Orden: Menor Score", 
            "Orden: Mas Recientes", 
            "Orden: Mas Antiguos", 
            "Orden: Urgencia SLA", 
            "Orden: Ticket ID"
        ])
        self.combo_cases_sort.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_sort.currentIndexChanged.connect(self._on_cases_filter_changed)

        self.btn_load_more_cases = QPushButton("+ Historial (200)")
        self.btn_load_more_cases.setToolTip("Descargar 200 casos adicionales desde la API para auditar historico")
        self.btn_load_more_cases.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_load_more_cases.clicked.connect(self.trigger_extended_cases_fetch)

        layout_cases_tools.addWidget(lbl_f)
        layout_cases_tools.addWidget(self.input_cases_search, 1)
        layout_cases_tools.addWidget(self.combo_cases_status)
        layout_cases_tools.addWidget(self.combo_cases_time)
        layout_cases_tools.addWidget(self.combo_cases_priority)
        layout_cases_tools.addWidget(self.combo_cases_assignee)
        layout_cases_tools.addWidget(self.combo_cases_sort)
        layout_cases_tools.addWidget(self.btn_load_more_cases)

        self.txt_cases = QTextEdit()
        self.txt_cases.setReadOnly(True)
        self.txt_cases.cursorPositionChanged.connect(self._on_cases_cursor_changed)

        # Barra de Paginacion Inferior
        frame_cases_pag = QFrame()
        frame_cases_pag.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 4px;")
        layout_cases_pag = QHBoxLayout(frame_cases_pag)
        layout_cases_pag.setContentsMargins(6, 2, 6, 2)
        layout_cases_pag.setSpacing(6)

        self.lbl_cases_count_info = QLabel("Mostrando 0 de 0 casos")
        self.lbl_cases_count_info.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none;")

        self.combo_cases_page_size = QComboBox()
        self.combo_cases_page_size.addItems(["25 por pagina", "50 por pagina", "100 por pagina", "Todos"])
        self.combo_cases_page_size.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px;")
        self.combo_cases_page_size.currentIndexChanged.connect(self._on_cases_page_size_changed)

        self.btn_cases_first_page = QPushButton("<<")
        self.btn_cases_first_page.setFixedWidth(30)
        self.btn_cases_first_page.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 3px; font-weight: bold; font-family: 'Consolas';")
        self.btn_cases_first_page.clicked.connect(self._on_cases_first_page)

        self.btn_cases_prev_page = QPushButton("<")
        self.btn_cases_prev_page.setFixedWidth(30)
        self.btn_cases_prev_page.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 3px; font-weight: bold; font-family: 'Consolas';")
        self.btn_cases_prev_page.clicked.connect(self._on_cases_prev_page)

        self.lbl_cases_page_indicator = QLabel("Pagina 1 de 1")
        self.lbl_cases_page_indicator.setStyleSheet("color: #f8fafc; font-family: 'Consolas'; font-size: 11px; font-weight: bold; border: none; padding: 0 4px;")

        self.btn_cases_next_page = QPushButton(">")
        self.btn_cases_next_page.setFixedWidth(30)
        self.btn_cases_next_page.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 3px; font-weight: bold; font-family: 'Consolas';")
        self.btn_cases_next_page.clicked.connect(self._on_cases_next_page)

        self.btn_cases_last_page = QPushButton(">>")
        self.btn_cases_last_page.setFixedWidth(30)
        self.btn_cases_last_page.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 3px; font-weight: bold; font-family: 'Consolas';")
        self.btn_cases_last_page.clicked.connect(self._on_cases_last_page)

        layout_cases_pag.addWidget(self.lbl_cases_count_info)
        layout_cases_pag.addStretch()
        layout_cases_pag.addWidget(self.combo_cases_page_size)
        layout_cases_pag.addWidget(self.btn_cases_first_page)
        layout_cases_pag.addWidget(self.btn_cases_prev_page)
        layout_cases_pag.addWidget(self.lbl_cases_page_indicator)
        layout_cases_pag.addWidget(self.btn_cases_next_page)
        layout_cases_pag.addWidget(self.btn_cases_last_page)

        layout_c.addLayout(layout_c_header)
        layout_c.addWidget(frame_cases_tools)
        layout_c.addWidget(self.txt_cases)
        layout_c.addWidget(frame_cases_pag)
        grid_layout.addWidget(frame_cases, 0, 1)

        # PANEL 3: ÁREA DE INVESTIGACIÓN Y ACCIONES SOAR EN TRES FILAS (DERECHA ROW 1)
        frame_triage = QFrame()
        layout_t = QVBoxLayout(frame_triage)
        lbl_t_title = QLabel("  CASE TRIAGE & COGNITIVE IA INVESTIGATION AREA")
        lbl_t_title.setStyleSheet(ui_theme.section_header_style(ui_theme.COLOR_MEDIUM))
        
        self.lbl_triage_sla_status = QLabel("  ⏱️ SLA / SLO STATUS: En espera de selección de caso...")
        self.lbl_triage_sla_status.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; background-color: {ui_theme.BG_ELEVATED}; padding: 6px 10px; border-radius: 5px; font-weight: bold; font-family: {ui_theme.FONT_MAIN}; font-size: 12px; border: 1px solid {ui_theme.BORDER_MUTED};")
        
        self.txt_triage = QTextEdit()
        self.txt_triage.setReadOnly(True)
        
        layout_soar_grid = QVBoxLayout()
        layout_soar_grid.setSpacing(6)
        
        # Fila 1: Investigación Forense & Telemetría
        row1 = QHBoxLayout()
        row1.setSpacing(6)

        lbl_ticket = QLabel("Ticket:")
        lbl_ticket.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; font-family: {ui_theme.FONT_MAIN};")
        self.input_case_ticket = QLineEdit()
        self.input_case_ticket.setPlaceholderText("ID")
        self.input_case_ticket.setFixedWidth(75)
        
        btn_take = QPushButton("1. Tomar Caso")
        btn_take.setStyleSheet(ui_theme.primary_action_btn_style())
        btn_take.clicked.connect(self.take_case_action)

        self.btn_reassign = QToolButton()
        self.btn_reassign.setPopupMode(QToolButton.InstantPopup)
        self.btn_reassign.setText("👤 Reasignar ▾")
        self.btn_reassign.setStyleSheet(ui_theme.reassign_btn_style())
        self.btn_reassign.setToolTip("Reasignar este caso a un compañero del equipo SOC o liberarlo")
        self.menu_reassign = QMenu(self.btn_reassign)
        self.menu_reassign.setStyleSheet("""
            QMenu {
                background-color: #0b1120;
                border: 1px solid #0284c7;
                border-radius: 6px;
                color: #f8fafc;
                font-family: 'Segoe UI', 'Consolas';
                font-size: 11px;
                padding: 6px 4px;
            }
            QMenu::item {
                background-color: transparent;
                color: #f8fafc;
                padding: 6px 20px;
                border-radius: 4px;
                margin: 2px 4px;
            }
            QMenu::item:selected {
                background-color: #1e293b;
                color: #38bdf8;
            }
            QMenu::separator {
                height: 1px;
                background-color: #1e293b;
                margin: 4px 8px;
            }
        """)
        self.btn_reassign.setMenu(self.menu_reassign)
        self._populate_reassign_menu()
        
        btn_triage = QPushButton("2. Ver Triage/Obs")
        btn_triage.clicked.connect(self.launch_triage_action)

        btn_comments = QPushButton("💬 Comentarios")
        btn_comments.clicked.connect(self.view_comments_action)

        # Separador visual
        sep1 = QFrame()
        sep1.setFrameShape(QFrame.VLine)
        sep1.setStyleSheet(f"color: {ui_theme.BORDER_MUTED};")

        lbl_logs = QLabel("Logs:")
        lbl_logs.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; font-family: {ui_theme.FONT_MAIN};")
        self.input_case_limit = QLineEdit()
        self.input_case_limit.setPlaceholderText("Cant")
        self.input_case_limit.setFixedWidth(55)
        
        btn_interflow = QPushButton("3. Ver Interflow")
        btn_interflow.clicked.connect(self.extract_interflow_action)

        btn_quick_terminal = QPushButton("🔬 Consola")
        btn_quick_terminal.setToolTip("Abrir investigación interactiva profunda en consola terminal")
        btn_quick_terminal.clicked.connect(self.trigger_quick_terminal_investigation)

        btn_quick_playbook = QPushButton("📖 Playbook")
        btn_quick_playbook.setToolTip("Ver playbook sugerido para este incidente")
        btn_quick_playbook.clicked.connect(self.trigger_quick_playbook_action)

        # Menú Desplegable Unificado del Copiloto IA (elimina la congestión de 4 botones sueltos)
        btn_ai_copilot = QToolButton()
        btn_ai_copilot.setPopupMode(QToolButton.InstantPopup)
        btn_ai_copilot.setText("🧠 Copiloto IA ▾")
        btn_ai_copilot.setStyleSheet(ui_theme.ai_action_btn_style())
        btn_ai_copilot.setToolTip("Seleccionar motor de Inteligencia Artificial para dictamen forense")
        
        ai_menu = QMenu(btn_ai_copilot)
        act_ai_normal = ai_menu.addAction("🟢 3B. Análisis IA Normal")
        act_ai_normal.triggered.connect(self.trigger_ai_normal)
        act_ai_forced = ai_menu.addAction("🔄 Forzar Re-análisis IA")
        act_ai_forced.triggered.connect(self.trigger_ai_forced)
        act_ai_stellar = ai_menu.addAction("🌐 3C. IA Stellar Cyber (Autotriage)")
        act_ai_stellar.triggered.connect(self.trigger_stellar_autotriage)
        ai_menu.addSeparator()
        act_ai_mask = ai_menu.addAction("🛡️ Ver JSON Ofuscado (Masking)")
        act_ai_mask.triggered.connect(self.show_obfuscated_json_action)
        btn_ai_copilot.setMenu(ai_menu)

        row1.addWidget(lbl_ticket)
        row1.addWidget(self.input_case_ticket)
        row1.addWidget(btn_take)
        row1.addWidget(self.btn_reassign)
        row1.addWidget(btn_triage)
        row1.addWidget(btn_comments)
        row1.addWidget(sep1)
        row1.addWidget(lbl_logs)
        row1.addWidget(self.input_case_limit)
        row1.addWidget(btn_interflow)
        row1.addWidget(btn_quick_terminal)
        row1.addWidget(btn_quick_playbook)
        row1.addWidget(btn_ai_copilot)
        row1.addStretch()

        # Fila 2: Dictamen, Justificación Obligatoria y Cierre Formal (SLA-Compliant)
        row2 = QHBoxLayout()
        row2.setSpacing(6)

        lbl_comment = QLabel("Justificación:")
        lbl_comment.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; font-family: {ui_theme.FONT_MAIN};")
        self.input_case_comment = QLineEdit()
        self.input_case_comment.setPlaceholderText("Escriba la justificación analítica obligatoria del veredicto...")
        self.input_case_comment.textChanged.connect(self.validar_justificacion)
        
        lbl_verdict = QLabel("Veredicto:")
        lbl_verdict.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-weight: bold; font-family: {ui_theme.FONT_MAIN};")
        self.combo_verdict = QComboBox()
        self.combo_verdict.addItems(["False Positive", "True Positive", "Benign"])
        self.combo_verdict.setFixedWidth(135)
        
        self.btn_resolve = QPushButton("🚀 4. Resolver Caso")
        self.btn_resolve.setEnabled(False)
        self.btn_resolve.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_resolve.clicked.connect(self.resolve_case_action)
        
        btn_copy = QPushButton("📋 Copiar")
        btn_copy.setToolTip("Copiar texto del visor forense al portapapeles")
        btn_copy.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_copy.clicked.connect(self.copy_triage_pane_text)
        
        btn_download = QPushButton("💾 Descargar .MD")
        btn_download.setToolTip("Descargar expediente forense en formato Markdown")
        btn_download.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_download.clicked.connect(self.download_triage_pane_text)
        
        row2.addWidget(lbl_comment)
        row2.addWidget(self.input_case_comment, 1)
        row2.addWidget(lbl_verdict)
        row2.addWidget(self.combo_verdict)
        row2.addWidget(self.btn_resolve)
        row2.addWidget(btn_copy)
        row2.addWidget(btn_download)
        
        layout_soar_grid.addLayout(row1)
        layout_soar_grid.addLayout(row2)
        
        layout_t.addWidget(lbl_t_title)
        layout_t.addWidget(self.lbl_triage_sla_status)
        layout_t.addWidget(self.txt_triage)
        layout_t.addLayout(layout_soar_grid)
        grid_layout.addWidget(frame_triage, 1, 1)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 2)

        # --- TAB 2: UEBA ENTITY PROFILING ---
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "👤 UEBA Perfil de Riesgo")
        
        layout_ueba = QVBoxLayout(self.tab2)
        
        lbl_ueba_title = QLabel("  UEBA ASSET & USER PROFILING")
        lbl_ueba_title.setStyleSheet("color: #a855f7; font-weight: bold; font-size: 14px; border: none;")
        layout_ueba.addWidget(lbl_ueba_title)
        
        # Control bar for Tab 2
        layout_ueba_controls = QHBoxLayout()
        lbl_ueba_input = QLabel("Entidad (Usuario, IP, Hostname):")
        self.input_ueba = QLineEdit()
        self.input_ueba.setPlaceholderText("Ej. johndoe, 192.168.1.50, WinServer2019...")
        self.btn_ueba_search = QPushButton("🔍 Generar Perfil de Riesgo")
        self.btn_ueba_search.setStyleSheet("background-color: #7e22ce; font-weight: bold;")
        self.btn_ueba_search.clicked.connect(self.trigger_ueba_profiling)
        
        layout_ueba_controls.addWidget(lbl_ueba_input)
        layout_ueba_controls.addWidget(self.input_ueba)
        layout_ueba_controls.addWidget(self.btn_ueba_search)
        
        layout_ueba.addLayout(layout_ueba_controls)
        
        # Output area
        self.txt_ueba = QTextEdit()
        self.txt_ueba.setReadOnly(True)
        self.txt_ueba.setHtml("<br><span style='color: #6b7280;'>Ingrese una entidad para generar su perfil de riesgo basado en el comportamiento histórico.</span>")
        layout_ueba.addWidget(self.txt_ueba)

        # --- TAB 3: 📊 MÉTRICAS & RENDIMIENTO SOC ---
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "📊 Métricas & Rendimiento SOC")
        layout_tab3 = QVBoxLayout(self.tab3)
        layout_tab3.setContentsMargins(10, 8, 10, 8)
        layout_tab3.setSpacing(8)

        # 1. Barra superior de Controles y Filtros (Diseño fino y ultra-compacto)
        frame_metrics_controls = QFrame()
        frame_metrics_controls.setFixedHeight(44)
        frame_metrics_controls.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_m_controls = QHBoxLayout(frame_metrics_controls)
        layout_m_controls.setContentsMargins(8, 2, 8, 2)
        layout_m_controls.setSpacing(6)

        lbl_m_period = QLabel("Período:")
        lbl_m_period.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")
        self.combo_metrics_period = QComboBox()
        self.combo_metrics_period.setStyleSheet("background-color: #0f172a; color: #f8fafc; border: 1px solid #334155; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px; border-radius: 3px;")
        self.combo_metrics_period.addItems([
            "Turno Actual (8h)",
            "Últimas 24 Horas",
            "Últimos 7 Días",
            "Últimos 30 Días",
            "Todo el Lote en Memoria",
            "Rango Personalizado..."
        ])
        self.combo_metrics_period.currentIndexChanged.connect(self._on_metrics_period_changed)

        self.dt_metrics_start = QDateTimeEdit(QDateTime.currentDateTime().addDays(-1))
        self.dt_metrics_start.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.dt_metrics_start.setCalendarPopup(True)
        self.dt_metrics_start.setStyleSheet("background-color: #020617; color: #38bdf8; border: 1px solid #334155; padding: 2px 4px; font-size: 11px;")
        self.dt_metrics_start.setVisible(False)

        self.dt_metrics_end = QDateTimeEdit(QDateTime.currentDateTime())
        self.dt_metrics_end.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.dt_metrics_end.setCalendarPopup(True)
        self.dt_metrics_end.setStyleSheet("background-color: #020617; color: #38bdf8; border: 1px solid #334155; padding: 2px 4px; font-size: 11px;")
        self.dt_metrics_end.setVisible(False)

        lbl_m_analyst = QLabel("Analista:")
        lbl_m_analyst.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")
        self.combo_metrics_analyst = QComboBox()
        self.combo_metrics_analyst.setStyleSheet("background-color: #0f172a; color: #f8fafc; border: 1px solid #334155; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px; border-radius: 3px;")
        self.combo_metrics_analyst.addItem("Kevin Moraes (kevinmoraes@technoma.com.py)", "kevinmoraes@technoma.com.py")
        self.combo_metrics_analyst.addItem("Todos / Equipo Completo SOC", "TODOS")
        self.combo_metrics_analyst.currentIndexChanged.connect(self.recalculate_executive_metrics)

        lbl_m_priority = QLabel("Prioridad:")
        lbl_m_priority.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")
        self.combo_metrics_priority = QComboBox()
        self.combo_metrics_priority.setStyleSheet("background-color: #0f172a; color: #f8fafc; border: 1px solid #334155; padding: 2px 6px; font-family: 'Consolas'; font-size: 11px; border-radius: 3px;")
        self.combo_metrics_priority.addItems(["Todas", "P1 - Crítica", "P2 - Alta", "P3 - Media", "P4 - Baja"])
        self.combo_metrics_priority.currentIndexChanged.connect(self.recalculate_executive_metrics)

        self.dt_metrics_start.dateTimeChanged.connect(self.recalculate_executive_metrics)
        self.dt_metrics_end.dateTimeChanged.connect(self.recalculate_executive_metrics)

        self.btn_metrics_recalc = QPushButton("🔄 Recalcular")
        self.btn_metrics_recalc.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_metrics_recalc.clicked.connect(self.recalculate_executive_metrics)

        self.btn_metrics_load_extended = QPushButton("📊 Cargar Historial (200)")
        self.btn_metrics_load_extended.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_metrics_load_extended.clicked.connect(self.trigger_extended_cases_fetch)

        self.btn_metrics_export_md = QPushButton("📥 Descargar .MD")
        self.btn_metrics_export_md.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_metrics_export_md.clicked.connect(self.export_metrics_markdown_action)

        self.btn_metrics_copy_md = QPushButton("📋 Copiar Markdown")
        self.btn_metrics_copy_md.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_metrics_copy_md.clicked.connect(self.copy_metrics_markdown_action)

        layout_m_controls.addWidget(lbl_m_period)
        layout_m_controls.addWidget(self.combo_metrics_period)
        layout_m_controls.addWidget(self.dt_metrics_start)
        layout_m_controls.addWidget(self.dt_metrics_end)
        layout_m_controls.addWidget(lbl_m_analyst)
        layout_m_controls.addWidget(self.combo_metrics_analyst)
        layout_m_controls.addWidget(lbl_m_priority)
        layout_m_controls.addWidget(self.combo_metrics_priority)
        layout_m_controls.addWidget(self.btn_metrics_recalc)
        layout_m_controls.addWidget(self.btn_metrics_load_extended)
        layout_m_controls.addWidget(self.btn_metrics_export_md)
        layout_m_controls.addWidget(self.btn_metrics_copy_md)
        layout_m_controls.addStretch()

        layout_tab3.addWidget(frame_metrics_controls, 0)

        # 2. Bloque de 8 Tarjetas KPI Ejecutivas (Diseño fino y ultra-compacto de 96px)
        frame_metrics_kpis = QFrame()
        frame_metrics_kpis.setFixedHeight(96)
        frame_metrics_kpis.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_m_kpis = QGridLayout(frame_metrics_kpis)
        layout_m_kpis.setContentsMargins(6, 3, 6, 3)
        layout_m_kpis.setSpacing(4)

        def _create_exec_kpi_card(title: str, default_val: str, subtitle: str, accent_color: str):
            card = QFrame()
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: #0f172a;
                    border: 1px solid #1e293b;
                    border-left: 3px solid {accent_color};
                    border-radius: 4px;
                }}
            """)
            card_l = QVBoxLayout(card)
            card_l.setContentsMargins(6, 2, 6, 2)
            card_l.setSpacing(0)

            lbl_t = QLabel(title)
            lbl_t.setStyleSheet("color: #94a3b8; font-size: 9px; font-weight: bold; border: none; font-family: 'Consolas';")
            lbl_v = QLabel(default_val)
            lbl_v.setStyleSheet(f"color: {accent_color}; font-size: 15px; font-weight: bold; border: none; font-family: 'Consolas';")
            lbl_s = QLabel(subtitle)
            lbl_s.setStyleSheet("color: #64748b; font-size: 8px; border: none; font-family: 'Consolas';")

            card_l.addWidget(lbl_t)
            card_l.addWidget(lbl_v)
            card_l.addWidget(lbl_s)
            return card, lbl_v, lbl_s

        card_mttd, self.lbl_m_mttd_val, self.lbl_m_mttd_sub = _create_exec_kpi_card("MTTD PROMEDIO", "--", "Obj: <20m (P1) / <2h (P2)", "#38bdf8")
        card_mttr, self.lbl_m_mttr_val, self.lbl_m_mttr_sub = _create_exec_kpi_card("MTTR PROMEDIO", "--", "Obj: <1h (P1) / <4h (P2)", "#a855f7")
        card_triage, self.lbl_m_triage_val, self.lbl_m_triage_sub = _create_exec_kpi_card("DURACIÓN TRIAJE L1", "--", "POE: <= 15 min", "#f59e0b")
        card_sla, self.lbl_m_sla_val, self.lbl_m_sla_sub = _create_exec_kpi_card("SLA COMPLIANCE", "--%", "Meta: >= 95.0%", "#10b981")
        card_cases, self.lbl_m_cases_val, self.lbl_m_cases_sub = _create_exec_kpi_card("CASOS AUDITADOS", "--", "Total en Período", "#f8fafc")
        card_alerts, self.lbl_m_alerts_val, self.lbl_m_alerts_sub = _create_exec_kpi_card("ALERTAS MITIGADAS", "--", "Volumen Interflow", "#ec4899")
        card_prec, self.lbl_m_prec_val, self.lbl_m_prec_sub = _create_exec_kpi_card("PRECISIÓN TRIAJE", "--%", "FP vs TP Detectados", "#06b6d4")
        card_vel, self.lbl_m_vel_val, self.lbl_m_vel_sub = _create_exec_kpi_card("VELOCIDAD OPERATIVA", "--", "Casos / Hora", "#84cc16")

        layout_m_kpis.addWidget(card_mttd, 0, 0)
        layout_m_kpis.addWidget(card_mttr, 0, 1)
        layout_m_kpis.addWidget(card_triage, 0, 2)
        layout_m_kpis.addWidget(card_sla, 0, 3)
        layout_m_kpis.addWidget(card_cases, 1, 0)
        layout_m_kpis.addWidget(card_alerts, 1, 1)
        layout_m_kpis.addWidget(card_prec, 1, 2)
        layout_m_kpis.addWidget(card_vel, 1, 3)

        layout_tab3.addWidget(frame_metrics_kpis, 0)

        # 3. Vista Dividida (Splitter Horizontal - Ocupa todo el espacio vertical disponible)
        self.splitter_metrics = QSplitter(Qt.Horizontal)
        self.splitter_metrics.setStyleSheet("""
            QSplitter::handle {
                background-color: #1e293b;
                width: 4px;
            }
        """)

        # Lado Izquierdo: Tablas Analíticas HTML
        self.txt_metrics_analytics = QTextEdit()
        self.txt_metrics_analytics.setReadOnly(True)
        self.txt_metrics_analytics.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #1e293b; padding: 8px; font-family: 'Consolas';")
        self.txt_metrics_analytics.setHtml("<span style='color: #64748b;'>Seleccione los filtros deseados y presione 'Recalcular' para visualizar las tablas analíticas...</span>")

        # Lado Derecho: Reporte Ejecutivo en Formato Markdown (Monoespaciado / Exportable)
        self.txt_metrics_markdown = QTextEdit()
        self.txt_metrics_markdown.setReadOnly(True)
        self.txt_metrics_markdown.setStyleSheet("background-color: #090d16; color: #38bdf8; border: 1px solid #1e293b; padding: 8px; font-family: 'Consolas'; font-size: 11px;")
        self.txt_metrics_markdown.setPlainText("# Informe Ejecutivo de Rendimiento SOC\\n\\nPresione 'Recalcular' para generar la vista previa del reporte en Markdown...")

        self.splitter_metrics.addWidget(self.txt_metrics_analytics)
        self.splitter_metrics.addWidget(self.txt_metrics_markdown)
        self.splitter_metrics.setStretchFactor(0, 3)
        self.splitter_metrics.setStretchFactor(1, 2)

        layout_tab3.addWidget(self.splitter_metrics, 1)
        layout_tab3.setStretch(0, 0)
        layout_tab3.setStretch(1, 0)
        layout_tab3.setStretch(2, 1)

        # --- TAB 4: 📖 PLAYBOOKS & GUÍAS DE RESPUESTA (NIST / MITRE) ---
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4, "📖 Playbooks & Guías")
        layout_tab4 = QVBoxLayout(self.tab4)
        layout_tab4.setContentsMargins(10, 8, 10, 8)
        layout_tab4.setSpacing(8)

        # Barra superior de Controles de Playbooks
        frame_pb_controls = QFrame()
        frame_pb_controls.setFixedHeight(44)
        frame_pb_controls.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_pb_controls = QHBoxLayout(frame_pb_controls)
        layout_pb_controls.setContentsMargins(8, 2, 8, 2)
        layout_pb_controls.setSpacing(6)

        lbl_pb_select = QLabel("Procedimiento SOC:")
        lbl_pb_select.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")
        self.combo_playbooks = QComboBox()
        self.combo_playbooks.setStyleSheet("""
            QComboBox {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 8px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 320px;
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #0f172a;
                color: #f8fafc;
                selection-background-color: #1e293b;
                selection-color: #38bdf8;
                border: 1px solid #334155;
            }
        """)

        # Cargar lista de playbooks
        self._all_playbooks = PlaybookEngine.load_catalog()
        for pb in self._all_playbooks:
            prio = pb.get("priority", "P2")
            self.combo_playbooks.addItem(f"[{prio}] {pb.get('title')}", pb.get("id"))
        self.combo_playbooks.currentIndexChanged.connect(self.on_playbook_combo_changed)

        self.btn_pb_recommend = QPushButton("🎯 Auto-Detectar para Ticket Activo")
        self.btn_pb_recommend.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_pb_recommend.clicked.connect(self.trigger_recommend_active_ticket)

        self.btn_pb_apply_hitl = QPushButton("🛡️ Aplicar Playbook al Caso (HITL)")
        self.btn_pb_apply_hitl.setStyleSheet(ui_theme.primary_action_btn_style(bg="#065f46", border="#059669", hover_bg="#047857"))
        self.btn_pb_apply_hitl.clicked.connect(self.trigger_apply_playbook_hitl)

        btn_pb_copy = QPushButton("📋 Copiar Guía")
        btn_pb_copy.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_pb_copy.clicked.connect(self.copy_current_playbook_text)

        layout_pb_controls.addWidget(lbl_pb_select)
        layout_pb_controls.addWidget(self.combo_playbooks)
        layout_pb_controls.addWidget(self.btn_pb_recommend)
        layout_pb_controls.addWidget(self.btn_pb_apply_hitl)
        layout_pb_controls.addWidget(btn_pb_copy)
        layout_pb_controls.addStretch()

        layout_tab4.addWidget(frame_pb_controls)

        # Splitter central de Playbooks
        self.splitter_pb = QSplitter(Qt.Horizontal)
        self.splitter_pb.setStyleSheet("QSplitter::handle { background-color: #1e293b; width: 4px; }")

        # Lado Izquierdo: Vista HTML enriquecida del Playbook
        self.txt_pb_html = QTextEdit()
        self.txt_pb_html.setReadOnly(True)
        self.txt_pb_html.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #1e293b; padding: 10px; font-family: 'Segoe UI', Tahoma, sans-serif;")

        # Lado Derecho: Bitácora Táctica & Checklist de Remediación
        frame_pb_right = QFrame()
        layout_pb_right = QVBoxLayout(frame_pb_right)
        layout_pb_right.setContentsMargins(0, 0, 0, 0)
        layout_pb_right.setSpacing(4)

        lbl_pb_notes_title = QLabel("📝 REGISTRO TÁCTICO & EVIDENCIAS DEL CASO (HITL):")
        lbl_pb_notes_title.setStyleSheet("color: #10b981; font-weight: bold; font-size: 11px; font-family: 'Consolas';")
        self.txt_pb_evidence_notes = QTextEdit()
        self.txt_pb_evidence_notes.setStyleSheet("background-color: #090d16; color: #38bdf8; border: 1px solid #1e293b; padding: 8px; font-family: 'Consolas'; font-size: 11px;")
        self.txt_pb_evidence_notes.setPlaceholderText("Bitácora de investigación: detalle aquí las IPs bloqueadas, hashes contrastados en VirusTotal, y acciones ejecutadas bajo este Playbook...")

        layout_pb_right.addWidget(lbl_pb_notes_title)
        layout_pb_right.addWidget(self.txt_pb_evidence_notes)

        self.splitter_pb.addWidget(self.txt_pb_html)
        self.splitter_pb.addWidget(frame_pb_right)
        self.splitter_pb.setStretchFactor(0, 3)
        self.splitter_pb.setStretchFactor(1, 2)

        layout_tab4.addWidget(self.splitter_pb, 1)

        # Inicializar visor de playbook con el primero
        if self._all_playbooks:
            self.txt_pb_html.setHtml(PlaybookEngine.format_playbook_html(self._all_playbooks[0]))

        # --- TAB 5: 🔬 CONSOLA & THREAT HUNTING (POWERSHELL + WSL) ---
        self._init_tab5_terminal()

        # --- TAB 6: 🛡️ VULNERABILIDADES & CVE INTEL (NVD NIST BATCH) ---
        self._worker_cve_batch = None
        self._cve_batch_list = []
        self._init_tab6_cve_intel()

        # --- TAB 7: 🧅 SECURITY ONION (GRID & NETWORK INTEL) ---
        self._so_engine = SecurityOnionEngine()
        self._worker_so_health = None
        self._worker_so_hunt = None
        self._worker_so_telemetry = None
        self._so_telemetry_items = []
        self._init_tab7_security_onion()
        self._init_tab8_predpi_validator()
        self._init_tab9_stellar_hunter()

        # Memoria interna para casos extendidos (Pool en RAM)
        self._extended_cases_pool = []
        self._last_metrics_result = None
        self._worker_extended_cases = None


        # Workers persistentes de monitoreo — se crean UNA vez y se reusan en cada ciclo
        # QThread.start() sobre un hilo terminado lo reinicia sin reinstanciar el objeto
        self.worker_health = HealthWorker()
        self.worker_health.finished_signal.connect(self.display_health_results)
        self.worker_health.error_signal.connect(self.master_error_router)

        self.worker_cases = CasesWorker()
        self.worker_cases.finished_signal.connect(self.display_cases_results)
        self.worker_cases.error_signal.connect(self.master_error_router)

        # Peticiones dinámicas iniciales
        self.trigger_health_refresh()
        self.trigger_cases_refresh()

        # Polling dinámico balanceado para no saturar la API:
        # - Incidentes vivos SOAR: cada 60 segundos (intervalo saludable anti-saturación)
        self.timer_cases = QTimer()
        self.timer_cases.timeout.connect(self.trigger_cases_refresh)
        self.timer_cases.start(60000)

        # - Salud de infraestructura / Sensores / Pozo: cada 3 minutos (180s)
        self.timer_health = QTimer()
        self.timer_health.timeout.connect(self.trigger_health_refresh)
        self.timer_health.start(180000)

        # - Salud de Grid Security Onion (Fail-safe, no intrusivo): cada 5 minutos
        QTimer.singleShot(2500, self.trigger_so_health_refresh)
        self.timer_so_health = QTimer()
        self.timer_so_health.timeout.connect(self.trigger_so_health_refresh)
        self.timer_so_health.start(300000)
        
        # Carga de analistas al inicio (una sola vez, fallo silencioso si la API no responde)
        QTimer.singleShot(3000, self._load_assignees_on_startup)

        # - Sincronización automática de Feeds CTI & TweetFeed (SOAR Background Sync)
        # Se lanza a los 8 segundos del inicio y luego cada 12 horas (43,200,000 ms)
        QTimer.singleShot(8000, self._auto_sync_feeds_background)
        self.timer_feeds_daily = QTimer()
        self.timer_feeds_daily.timeout.connect(self._auto_sync_feeds_background)
        self.timer_feeds_daily.start(43200000)

        # Gobernanza SLA/SLO en RAM y Temporizador de Triaje L1 (15 min POE)
        self.triage_active_case_id = None
        self.triage_active_ticket = None
        self.triage_poe_deadline = 0
        self.triage_sla_deadline = 0
        self.triage_priority = "P1"
        self._poe_warning_sounded = False
        self._poe_breach_sounded = False
        self._prev_sla_breached_count = 0
        
        self.timer_triage_countdown = QTimer()
        self.timer_triage_countdown.setInterval(1000)
        self.timer_triage_countdown.timeout.connect(self._update_triage_countdown_tick)

        # Módulos de Auto-Guardia SLA y Auto-Remediación (HealthMailbox, WebControl Translate y SATI VPN DNS)
        self._auto_assigned_cases = set()
        self._remediated_cases = set()
        self._worker_hm_remediator = None
        self._remediated_translate_cases = set()
        self._worker_sophos_translate_remediator = None
        self._remediated_sati_cases = set()
        self._worker_sati_remediator = None
        self._remediated_dpapi_cases = set()
        self._worker_dpapi_remediator = None
        self._auto_guardia_workers = []
        self._case_identity_cache = {}
        self._active_probe_workers = {}

        # Módulo de Notificaciones Push Móviles (ntfy.sh)
        self._seen_case_ids = set()
        self._mobile_notified_assigned = set()
        self._mobile_notified_mttd_risk = set()
        self._mobile_notified_mttr_risk = set()
        self._mobile_notified_auto_closed = set()
        self._mobile_poe_warning_sent = False
        self._mobile_poe_breach_sent = False
        self._mobile_initial_sync_done = False
        self._case_history_status = {}
        
        # Inicializar modulo Anti-Sleep nativo para que permanezca activo durante toda la sesion
        self._init_antisleep()


    def closeEvent(self, event):
        """Destructor coordinado. Activa la cancelación cooperativa y libera sockets."""
        if hasattr(self, '_term_process') and self._term_process and self._term_process.state() == QProcess.Running:
            try:
                self._term_process.kill()
                self._term_process.waitForFinished(1000)
            except Exception:
                pass

        if hasattr(self, 'timer_cases'): self.timer_cases.stop()
        if hasattr(self, 'timer_health'): self.timer_health.stop()
        if hasattr(self, 'timer_live'): self.timer_live.stop()
        if hasattr(self, 'timer_triage_countdown'): self.timer_triage_countdown.stop()
        if hasattr(self, 'timer_so_health'): self.timer_so_health.stop()

        # Cerrar limpiamente todas las ventanas satélites del SOCWindowManager
        if hasattr(self, 'window_manager') and self.window_manager:
            self.window_manager.close_all()

        # Restaurar politicas de energia de Windows y detener timer Anti-Sleep
        self._restore_system_sleep()

        # --- Workers PERSISTENTES: siempre existen, cancelar sin destruir ---
        for w_name in ('worker_health', 'worker_cases'):
            w = getattr(self, w_name)
            if w.isRunning():
                w._is_killed = True
                w.quit()
                if not w.wait(4000):
                    log_to_file(f"[SYS ENFORCEMENT] Worker persistente {w_name} forzado.")
                    w.terminate()
                    w.wait(1000)

        # --- Workers EFÍMEROS: pueden ser None si ya fueron destruidos por _safe_kill_worker ---
        for w_name in ('worker_triage', 'worker_take', 'worker_interflow',
                       'worker_resolve', 'worker_ai', '_worker_extended_cases', '_worker_cti', '_worker_cve_batch', '_worker_hm_remediator', '_worker_sophos_translate_remediator', '_worker_sati_remediator', '_worker_dpapi_remediator',
                       '_worker_so_health', '_worker_so_hunt', '_worker_so_telemetry'):
            w = getattr(self, w_name, None)
            if w:
                w._is_killed = True
                if hasattr(w, 'isRunning') and w.isRunning():
                    w.quit()
                    if hasattr(w, 'wait') and not w.wait(4000):
                        log_to_file(f"[SYS ENFORCEMENT] Hilo {w_name} no respondio a tiempo. Forzando terminacion.")
                        if hasattr(w, 'terminate'):
                            w.terminate()
                        if hasattr(w, 'wait'):
                            w.wait(1000)

        # Cleanup de workers de auto-guardia
        if hasattr(self, '_auto_guardia_workers'):
            for gw in self._auto_guardia_workers:
                if gw and hasattr(gw, 'isRunning') and gw.isRunning():
                    gw._is_killed = True
                    gw.quit()
                    if hasattr(gw, 'wait'):
                        gw.wait(1000)

        # Cleanup de workers de sondeo de identidad
        if hasattr(self, '_active_probe_workers'):
            for pw in list(self._active_probe_workers.values()):
                if pw and hasattr(pw, 'isRunning') and pw.isRunning():
                    pw._is_killed = True
                    pw.quit()
                    if hasattr(pw, 'wait'):
                        pw.wait(500)

        event.accept()

