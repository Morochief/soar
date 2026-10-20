# -*- coding: utf-8 -*-
"""
Mixin Modular: Vulnerabilidades & CVE Intel (Tab 6 - NVD NIST 2.0 Batch Engine).
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
import datetime as _dt


class CveIntelMixin:
    # =========================================================================
    # TAB 6: VULNERABILIDADES & CVE INTEL (NVD NIST 2.0 BATCH ENGINE)
    # =========================================================================
    def _apply_cve_calendar_style(self, qdateedit: QDateEdit):
        """Aplica un tema oscuro de alto contraste al calendario desplegable evitando texto negro."""
        cal = qdateedit.calendarWidget()
        if not cal:
            return
        cal.setStyleSheet("""
            QCalendarWidget QWidget {
                background-color: #0b1120;
                color: #f8fafc;
                font-family: 'Consolas', 'Segoe UI', sans-serif;
                font-size: 11px;
            }
            QCalendarWidget #qt_calendar_navigationbar {
                background-color: #0f172a;
                border-bottom: 1px solid #1e293b;
                padding: 2px;
            }
            QCalendarWidget QToolButton {
                color: #38bdf8;
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 8px;
                font-weight: bold;
                font-size: 11px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #0284c7;
                color: #ffffff;
            }
            QCalendarWidget QSpinBox {
                background-color: #1e293b;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 2px;
                font-size: 11px;
                selection-background-color: #0284c7;
            }
            QCalendarWidget QMenu {
                background-color: #0f172a;
                color: #f8fafc;
                border: 1px solid #334155;
                padding: 4px;
            }
            QCalendarWidget QMenu::item:selected {
                background-color: #0284c7;
                color: #ffffff;
            }
            QCalendarWidget QTableView {
                background-color: #020617;
                alternate-background-color: #0b1120;
                color: #f8fafc;
                selection-background-color: #0284c7;
                selection-color: #ffffff;
                gridline-color: #1e293b;
                border: 1px solid #1e293b;
                font-size: 11px;
            }
            QCalendarWidget QTableView:enabled {
                color: #f8fafc;
            }
            QCalendarWidget QTableView:disabled {
                color: #475569;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: #f8fafc;
                background-color: #020617;
                selection-background-color: #0284c7;
                selection-color: #ffffff;
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #475569;
            }
            QCalendarWidget QHeaderView::section {
                background-color: #0f172a;
                color: #94a3b8;
                font-weight: bold;
                border: 1px solid #1e293b;
                padding: 2px;
            }
        """)

    def _init_tab6_cve_intel(self):
        """Inicializa la Pestana 6: Modulo Nativo SOAR de Vulnerabilidades & CVE Intel con Master-Detail e Inspector Forense."""
        self.tab6 = QWidget()
        self.tabs.addTab(self.tab6, "Vulnerabilidades & CVE Intel")
        layout_tab6 = QVBoxLayout(self.tab6)
        layout_tab6.setContentsMargins(10, 8, 10, 8)
        layout_tab6.setSpacing(6)

        self._cve_batch_list = []
        self._cve_parsed_items = []
        self._cve_current_filtered = []

        # 1. Marco Superior de Filtros y Configuracion NVD
        frame_cve_top = QFrame()
        frame_cve_top.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_cve_top = QVBoxLayout(frame_cve_top)
        layout_cve_top.setContentsMargins(10, 6, 10, 6)
        layout_cve_top.setSpacing(6)

        # Fila 1: Fechas, Severidades y Boton de Inicio
        layout_row1 = QHBoxLayout()
        layout_row1.setSpacing(8)

        lbl_rango = QLabel("Rango:")
        lbl_rango.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")

        self.dt_cve_start = QDateEdit()
        self.dt_cve_start.setCalendarPopup(True)
        self.dt_cve_start.setDisplayFormat("dd-MM-yyyy")
        self.dt_cve_start.setDate(QDate.currentDate().addDays(-7))
        self.dt_cve_start.setStyleSheet("""
            QDateEdit {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 6px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 95px;
            }
        """)
        self._apply_cve_calendar_style(self.dt_cve_start)

        lbl_a = QLabel("al")
        lbl_a.setStyleSheet("color: #64748b; border: none; font-size: 11px;")

        self.dt_cve_end = QDateEdit()
        self.dt_cve_end.setCalendarPopup(True)
        self.dt_cve_end.setDisplayFormat("dd-MM-yyyy")
        self.dt_cve_end.setDate(QDate.currentDate())
        self.dt_cve_end.setStyleSheet("""
            QDateEdit {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 6px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 95px;
            }
        """)
        self._apply_cve_calendar_style(self.dt_cve_end)

        lbl_sep1 = QLabel("|")
        lbl_sep1.setStyleSheet("color: #334155; border: none;")

        lbl_sevs = QLabel("Severidades:")
        lbl_sevs.setStyleSheet("color: #94a3b8; font-weight: bold; border: none; font-size: 11px;")

        self.chk_cve_critical = QCheckBox("Critica")
        self.chk_cve_critical.setChecked(True)
        self.chk_cve_critical.setStyleSheet("color: #ef4444; font-weight: bold; font-size: 11px; border: none;")

        self.chk_cve_high = QCheckBox("Alta")
        self.chk_cve_high.setChecked(True)
        self.chk_cve_high.setStyleSheet("color: #fb923c; font-weight: bold; font-size: 11px; border: none;")

        self.chk_cve_medium = QCheckBox("Media")
        self.chk_cve_medium.setChecked(False)
        self.chk_cve_medium.setStyleSheet("color: #f59e0b; font-size: 11px; border: none;")

        self.chk_cve_low = QCheckBox("Baja")
        self.chk_cve_low.setChecked(False)
        self.chk_cve_low.setStyleSheet("color: #10b981; font-size: 11px; border: none;")

        self.btn_cve_fetch = QPushButton("Iniciar Busqueda NVD")
        self.btn_cve_fetch.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_cve_fetch.clicked.connect(self.start_cve_batch_fetch)

        self.btn_cve_stop = QPushButton("Detener")
        self.btn_cve_stop.setEnabled(False)
        self.btn_cve_stop.setStyleSheet(ui_theme.danger_btn_style())
        self.btn_cve_stop.clicked.connect(self.stop_cve_batch_fetch)

        layout_row1.addWidget(lbl_rango)
        layout_row1.addWidget(self.dt_cve_start)
        layout_row1.addWidget(lbl_a)
        layout_row1.addWidget(self.dt_cve_end)
        layout_row1.addWidget(lbl_sep1)
        layout_row1.addWidget(lbl_sevs)
        layout_row1.addWidget(self.chk_cve_critical)
        layout_row1.addWidget(self.chk_cve_high)
        layout_row1.addWidget(self.chk_cve_medium)
        layout_row1.addWidget(self.chk_cve_low)
        layout_row1.addStretch()
        layout_row1.addWidget(self.btn_cve_fetch)
        layout_row1.addWidget(self.btn_cve_stop)

        # Fila 2: Webhook Slack y Acciones Globales
        layout_row2 = QHBoxLayout()
        layout_row2.setSpacing(8)

        lbl_slack = QLabel("Webhook Slack (Opcional):")
        lbl_slack.setStyleSheet("color: #94a3b8; border: none; font-size: 11px;")

        self.input_cve_slack = QLineEdit()
        self.input_cve_slack.setPlaceholderText("https://hooks.slack.com/services/...")
        self.input_cve_slack.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 3px 6px; font-family: 'Consolas'; font-size: 11px;")

        self.btn_cve_export_md = QPushButton("Exportar Markdown (.md)")
        self.btn_cve_export_md.setEnabled(False)
        self.btn_cve_export_md.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_cve_export_md.clicked.connect(self.export_cve_markdown)

        self.btn_cve_export_xlsx = QPushButton("Exportar Excel (.xlsx)")
        self.btn_cve_export_xlsx.setEnabled(False)
        self.btn_cve_export_xlsx.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_cve_export_xlsx.clicked.connect(self.export_cve_excel)

        self.btn_cve_clear = QPushButton("Limpiar")
        self.btn_cve_clear.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_cve_clear.clicked.connect(self.clear_cve_batch_data)

        layout_row2.addWidget(lbl_slack)
        layout_row2.addWidget(self.input_cve_slack, 1)
        layout_row2.addWidget(self.btn_cve_export_md)
        layout_row2.addWidget(self.btn_cve_export_xlsx)
        layout_row2.addWidget(self.btn_cve_clear)

        # Fila 3: Barra de Filtrado en Vivo y Control Dinamico
        layout_row3 = QHBoxLayout()
        layout_row3.setSpacing(8)

        lbl_filter = QLabel("Filtrar en vivo:")
        lbl_filter.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")

        self.input_cve_filter = QLineEdit()
        self.input_cve_filter.setPlaceholderText("Buscar por Fabricante, Producto, CVE, Debilidad CWE o Vector de Ataque...")
        self.input_cve_filter.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #0284c7; border-radius: 4px; padding: 3px 8px; font-family: 'Consolas'; font-size: 11px;")
        self.input_cve_filter.textChanged.connect(self._apply_cve_live_filter)

        self.combo_cve_filter_sev = QComboBox()
        self.combo_cve_filter_sev.addItems(["Todas las Severidades", "CRITICA", "ALTA", "MEDIA", "BAJA"])
        self.combo_cve_filter_sev.setStyleSheet("background-color: #020617; color: #f8fafc; border: 1px solid #334155; border-radius: 4px; padding: 3px 6px; font-size: 11px;")
        self.combo_cve_filter_sev.currentIndexChanged.connect(self._apply_cve_live_filter)

        self.chk_cve_only_kev = QCheckBox("Solo CISA KEV (En Explotacion)")
        self.chk_cve_only_kev.setStyleSheet("color: #f87171; font-weight: bold; font-size: 11px; border: none;")
        self.chk_cve_only_kev.toggled.connect(self._apply_cve_live_filter)

        self.lbl_cve_stats = QLabel("0 vulnerabilidades cargadas")
        self.lbl_cve_stats.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none; padding-left: 6px;")

        layout_row3.addWidget(lbl_filter)
        layout_row3.addWidget(self.input_cve_filter, 1)
        layout_row3.addWidget(self.combo_cve_filter_sev)
        layout_row3.addWidget(self.chk_cve_only_kev)
        layout_row3.addWidget(self.lbl_cve_stats)

        layout_cve_top.addLayout(layout_row1)
        layout_cve_top.addLayout(layout_row2)
        layout_cve_top.addLayout(layout_row3)
        layout_tab6.addWidget(frame_cve_top, 0)

        # 2. Barra de Progreso y Estado NVD
        self.progress_cve_batch = QProgressBar()
        self.progress_cve_batch.setFixedHeight(12)
        self.progress_cve_batch.setTextVisible(True)
        self.progress_cve_batch.setStyleSheet("""
            QProgressBar {
                background-color: #020617;
                border: 1px solid #1e293b;
                border-radius: 4px;
                text-align: center;
                color: #f8fafc;
                font-family: 'Consolas';
                font-size: 9px;
            }
            QProgressBar::chunk {
                background-color: #38bdf8;
                border-radius: 3px;
            }
        """)
        layout_tab6.addWidget(self.progress_cve_batch, 0)

        # 3. Vista Dividida Master-Detail (Splitter Vertical)
        self.splitter_cve = QSplitter(Qt.Vertical)
        self.splitter_cve.setStyleSheet("""
            QSplitter::handle {
                background-color: #1e293b;
                height: 5px;
            }
        """)

        # Panel Superior: Tabla Maestra de Vulnerabilidades (9 Columnas)
        frame_table_wrap = QFrame()
        frame_table_wrap.setStyleSheet("background-color: #080d1a; border: 1px solid #1e293b; border-radius: 6px;")
        layout_table_wrap = QVBoxLayout(frame_table_wrap)
        layout_table_wrap.setContentsMargins(6, 6, 6, 6)
        layout_table_wrap.setSpacing(4)

        lbl_tbl_title = QLabel("Catalogo de Vulnerabilidades Identificadas (NVD NIST 2.0):")
        lbl_tbl_title.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")
        layout_table_wrap.addWidget(lbl_tbl_title)

        self.table_cve_results = QTableWidget()
        self.table_cve_results.setColumnCount(9)
        self.table_cve_results.setHorizontalHeaderLabels([
            "CVE ID", "Fabricante", "Producto Afectado", "CVSS", "Severidad",
            "Debilidad (CWE)", "Vector Ataque", "CISA KEV", "Publicacion"
        ])
        self.table_cve_results.setStyleSheet("""
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
                padding: 5px 6px;
                font-weight: bold;
                border: 1px solid #1e293b;
                font-family: 'Consolas';
                font-size: 11px;
            }
        """)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.table_cve_results.horizontalHeader().setSectionResizeMode(8, QHeaderView.ResizeToContents)
        self.table_cve_results.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_cve_results.setSelectionMode(QTableWidget.SingleSelection)
        self.table_cve_results.setAlternatingRowColors(True)
        self.table_cve_results.itemSelectionChanged.connect(self._on_cve_selection_changed)
        self.table_cve_results.itemDoubleClicked.connect(self._on_cve_row_double_clicked)
        layout_table_wrap.addWidget(self.table_cve_results)

        # Panel Inferior: Pestañas de Detalle Forense y Registro de Logs
        self.tabs_cve_bottom = QTabWidget()
        self.tabs_cve_bottom.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #1e293b;
                background-color: #080d1a;
                border-radius: 6px;
            }
            QTabBar::tab {
                background-color: #0f172a;
                color: #94a3b8;
                border: 1px solid #1e293b;
                padding: 4px 12px;
                font-family: 'Consolas';
                font-size: 11px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #1e293b;
                color: #38bdf8;
                border-bottom: 2px solid #38bdf8;
            }
        """)

        # Sub-pestaña A: Ficha Forense de la Vulnerabilidad (Inspector Master-Detail)
        tab_cve_card = QWidget()
        layout_card = QVBoxLayout(tab_cve_card)
        layout_card.setContentsMargins(10, 8, 10, 8)
        layout_card.setSpacing(6)

        # Cabecera de la Tarjeta Forense
        frame_card_header = QFrame()
        frame_card_header.setStyleSheet("background-color: #020617; border: 1px solid #1e293b; border-radius: 4px; padding: 4px;")
        layout_card_header = QHBoxLayout(frame_card_header)
        layout_card_header.setContentsMargins(8, 4, 8, 4)
        layout_card_header.setSpacing(8)

        self.lbl_cve_card_title = QLabel("Seleccione una vulnerabilidad de la tabla superior para inspeccionar sus detalles.")
        self.lbl_cve_card_title.setStyleSheet("color: #f8fafc; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")

        self.lbl_cve_card_badge_sev = QLabel("SEVERIDAD: N/A")
        self.lbl_cve_card_badge_sev.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")

        self.lbl_cve_card_badge_vector = QLabel("VECTOR: N/A")
        self.lbl_cve_card_badge_vector.setStyleSheet("background-color: #1e293b; color: #38bdf8; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")

        self.lbl_cve_card_badge_kev = QLabel("CISA KEV: NO")
        self.lbl_cve_card_badge_kev.setStyleSheet("background-color: #1e293b; color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")

        layout_card_header.addWidget(self.lbl_cve_card_title, 1)
        layout_card_header.addWidget(self.lbl_cve_card_badge_sev)
        layout_card_header.addWidget(self.lbl_cve_card_badge_vector)
        layout_card_header.addWidget(self.lbl_cve_card_badge_kev)
        layout_card.addWidget(frame_card_header)

        # Grilla de Metadatos Tecnicos (CWE, Vector CVSS, Versiones Afectadas)
        frame_card_meta = QFrame()
        frame_card_meta.setStyleSheet("background-color: #020617; border: 1px solid #1e293b; border-radius: 4px;")
        layout_card_meta = QGridLayout(frame_card_meta)
        layout_card_meta.setContentsMargins(8, 6, 8, 6)
        layout_card_meta.setSpacing(6)

        lbl_m1 = QLabel("Vector CVSS 3.1:")
        lbl_m1.setStyleSheet("color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; border: none;")
        self.lbl_cve_card_cvss_vector = QLabel("N/A")
        self.lbl_cve_card_cvss_vector.setStyleSheet("color: #38bdf8; font-family: 'Consolas'; font-size: 10px; border: none;")

        lbl_m2 = QLabel("Debilidad CWE:")
        lbl_m2.setStyleSheet("color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; border: none;")
        self.lbl_cve_card_cwe = QLabel("N/A")
        self.lbl_cve_card_cwe.setStyleSheet("color: #fb923c; font-family: 'Consolas'; font-size: 10px; border: none;")

        lbl_m3 = QLabel("Versiones / CPEs:")
        lbl_m3.setStyleSheet("color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; border: none;")
        self.lbl_cve_card_cpes = QLabel("N/A")
        self.lbl_cve_card_cpes.setStyleSheet("color: #cbd5e1; font-family: 'Consolas'; font-size: 10px; border: none;")

        lbl_m4 = QLabel("Accion CISA KEV:")
        lbl_m4.setStyleSheet("color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; border: none;")
        self.lbl_cve_card_kev_due = QLabel("No catalogada")
        self.lbl_cve_card_kev_due.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 10px; border: none;")

        layout_card_meta.addWidget(lbl_m1, 0, 0)
        layout_card_meta.addWidget(self.lbl_cve_card_cvss_vector, 0, 1)
        layout_card_meta.addWidget(lbl_m2, 0, 2)
        layout_card_meta.addWidget(self.lbl_cve_card_cwe, 0, 3)
        layout_card_meta.addWidget(lbl_m3, 1, 0)
        layout_card_meta.addWidget(self.lbl_cve_card_cpes, 1, 1)
        layout_card_meta.addWidget(lbl_m4, 1, 2)
        layout_card_meta.addWidget(self.lbl_cve_card_kev_due, 1, 3)
        layout_card.addWidget(frame_card_meta)

        # Descripcion Tecnica Completa
        lbl_desc_title = QLabel("Descripcion Tecnica Oficial:")
        lbl_desc_title.setStyleSheet("color: #94a3b8; font-weight: bold; font-size: 10px; border: none;")
        layout_card.addWidget(lbl_desc_title)

        self.txt_cve_card_desc = QTextEdit()
        self.txt_cve_card_desc.setReadOnly(True)
        self.txt_cve_card_desc.setStyleSheet("""
            QTextEdit {
                background-color: #020617;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                font-family: 'Consolas', 'Segoe UI', sans-serif;
                font-size: 11px;
                padding: 6px;
                line-height: 1.4;
            }
        """)
        layout_card.addWidget(self.txt_cve_card_desc, 1)

        # Botones de Accion del Inspector
        layout_card_actions = QHBoxLayout()
        layout_card_actions.setSpacing(8)

        self.btn_cve_pivot_dfir = QPushButton("Investigar en Consola DFIR")
        self.btn_cve_pivot_dfir.setStyleSheet(ui_theme.primary_action_btn_style())
        self.btn_cve_pivot_dfir.clicked.connect(self._pivot_selected_cve_to_dfir)

        self.btn_cve_open_nvd = QPushButton("Abrir en Portal NVD NIST")
        self.btn_cve_open_nvd.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_cve_open_nvd.clicked.connect(self._open_selected_cve_nvd_url)

        self.btn_cve_copy_card = QPushButton("Copiar Ficha Forense")
        self.btn_cve_copy_card.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_cve_copy_card.clicked.connect(self._copy_selected_cve_card)

        layout_card_actions.addWidget(self.btn_cve_pivot_dfir)
        layout_card_actions.addWidget(self.btn_cve_open_nvd)
        layout_card_actions.addWidget(self.btn_cve_copy_card)
        layout_card_actions.addStretch()
        layout_card.addLayout(layout_card_actions)

        self.tabs_cve_bottom.addTab(tab_cve_card, "Ficha Forense de la Vulnerabilidad")

        # Sub-pestaña B: Registro de Red NVD NIST y Chunks
        tab_cve_log = QWidget()
        layout_tab_log = QVBoxLayout(tab_cve_log)
        layout_tab_log.setContentsMargins(6, 6, 6, 6)
        layout_tab_log.setSpacing(4)

        self.txt_cve_log = QTextEdit()
        self.txt_cve_log.setReadOnly(True)
        self.txt_cve_log.setStyleSheet("background-color: #020617; color: #cbd5e1; border: 1px solid #1e293b; font-family: 'Consolas'; font-size: 11px; padding: 6px;")
        layout_tab_log.addWidget(self.txt_cve_log)

        self.tabs_cve_bottom.addTab(tab_cve_log, "Registro de Red y Paginacion NVD")

        self.splitter_cve.addWidget(frame_table_wrap)
        self.splitter_cve.addWidget(self.tabs_cve_bottom)
        self.splitter_cve.setStretchFactor(0, 3)
        self.splitter_cve.setStretchFactor(1, 2)

        layout_tab6.addWidget(self.splitter_cve, 1)

    def _parse_cve_items(self) -> List[Dict[str, Any]]:
        """Procesa y enriquece integralmente el catalogo de vulnerabilidades NVD API 2.0."""
        nvd_source_vendor_map = {
            "psirt@fortinet.com": "Fortinet",
            "secure@microsoft.com": "Microsoft",
            "psirt@cisco.com": "Cisco Systems",
            "cve@checkpoint.com": "Check Point",
            "secalert@redhat.com": "Red Hat",
            "psirt@paloaltonetworks.com": "Palo Alto",
            "security@google.com": "Google",
            "product-security@apple.com": "Apple",
            "security@apache.org": "Apache",
            "security@vmware.com": "VMware",
            "security-alert@hpe.com": "HPE",
            "psirt@solarwinds.com": "SolarWinds",
            "security@zoom.us": "Zoom",
            "psirt@lenovo.com": "Lenovo",
            "psirt@sonicwall.com": "SonicWall",
            "psirt@f5.com": "F5 Networks",
            "security@ivanti.com": "Ivanti",
            "cve@gitlab.com": "GitLab",
            "security-advisories@github.com": "GitHub",
            "audit@patchstack.com": "WordPress / Patchstack",
            "security@wordfence.com": "WordPress / Wordfence",
            "cve-coordination@incibe.es": "INCIBE CNVD",
            "cert@cert.org": "CERT/CC",
            "cve@mitre.org": "MITRE",
            "vulnreport@tenable.com": "Tenable",
            "talos-cna@cisco.com": "Cisco Talos",
            "security@qualys.com": "Qualys"
        }

        cwe_labels = {
            "CWE-787": "CWE-787 (Corrupcion de Memoria / Out-of-bounds Write)",
            "CWE-125": "CWE-125 (Lectura Fuera de Limites / Out-of-bounds Read)",
            "CWE-89": "CWE-89 (Inyeccion SQL / SQLi)",
            "CWE-79": "CWE-79 (Cross-Site Scripting / XSS)",
            "CWE-20": "CWE-20 (Validacion Inadecuada de Entradas)",
            "CWE-22": "CWE-22 (Salto de Directorio / Path Traversal)",
            "CWE-352": "CWE-352 (Falsificacion de Peticion / CSRF)",
            "CWE-434": "CWE-434 (Subida de Archivos Peligrosos)",
            "CWE-862": "CWE-862 (Falta de Autorizacion)",
            "CWE-287": "CWE-287 (Fallo / Bypass de Autenticacion)",
            "CWE-798": "CWE-798 (Credenciales Hardcodeadas)",
            "CWE-306": "CWE-306 (Falta de Autenticacion en Funcion Critica)",
            "CWE-502": "CWE-502 (Deserializacion de Datos No Confiables)",
            "CWE-94": "CWE-94 (Inyeccion de Codigo / RCE)",
            "CWE-77": "CWE-77 (Inyeccion de Comandos del Sistema)",
            "CWE-416": "CWE-416 (Uso de Memoria Liberada / Use-After-Free)",
            "CWE-119": "CWE-119 (Manejo Inseguro de Buffers)",
            "CWE-269": "CWE-269 (Gestion Inadecuada de Privilegios / LPE)",
            "CWE-918": "CWE-918 (Server-Side Request Forgery / SSRF)",
            "CWE-362": "CWE-362 (Condicion de Carrera / Race Condition)",
            "CWE-611": "CWE-611 (Entidad Externa XML / XXE)",
            "CWE-200": "CWE-200 (Exposicion de Informacion Sensible)",
            "CWE-284": "CWE-284 (Control de Acceso Inadecuado)",
            "CWE-400": "CWE-400 (Consumo No Controlado de Recursos / DoS)"
        }

        av_map = {
            "NETWORK": "Red (Remoto)",
            "ADJACENT_NETWORK": "Red Adyacente",
            "LOCAL": "Local (Host)",
            "PHYSICAL": "Fisico"
        }

        parsed = []
        for item in self._cve_batch_list:
            cve_obj = item.get("cve", {})
            cve_id = cve_obj.get("id", "N/A")
            source_id = str(cve_obj.get("sourceIdentifier", "")).lower()
            published = cve_obj.get("published", "N/A")
            if "T" in published:
                published = published.replace("T", " ").split(".")[0]

            # 1. Extraer configuraciones CPE
            vendors_found = set()
            products_found = set()
            cpe_criteria_list = []

            configs = cve_obj.get("configurations", [])
            for cfg in configs:
                nodes = cfg.get("nodes", [])
                for node in nodes:
                    for cpe_m in node.get("cpeMatch", []):
                        crit = cpe_m.get("criteria", "")
                        if crit:
                            cpe_criteria_list.append(crit)
                            parts = crit.split(":")
                            if len(parts) >= 5 and parts[1] == "2.3":
                                v = parts[3].strip()
                                p = parts[4].strip()
                                if v and v != "*":
                                    vendors_found.add(v.replace("_", " ").title())
                                if p and p != "*":
                                    products_found.add(p.replace("_", " ").title())

            # Resolver Fabricante
            if vendors_found:
                vendor_str = ", ".join(sorted(vendors_found)[:2])
                if len(vendors_found) > 2:
                    vendor_str += f" (+{len(vendors_found)-2})"
            elif source_id in nvd_source_vendor_map:
                vendor_str = nvd_source_vendor_map[source_id]
            elif "@" in source_id:
                domain_part = source_id.split("@")[-1].split(".")[0]
                vendor_str = domain_part.replace("-", " ").title()
            else:
                vendor_str = "En analisis NVD"

            # Resolver Producto Afectado
            cisa_vname = cve_obj.get("cisaVulnerabilityName", "")
            if products_found:
                prod_str = ", ".join(sorted(products_found)[:2])
                if len(products_found) > 2:
                    prod_str += f" (+{len(products_found)-2})"
            elif cisa_vname:
                prod_str = cisa_vname[:35] + ("..." if len(cisa_vname) > 35 else "")
            else:
                prod_str = "Multiples / En evaluacion"

            # Resolver CISA KEV
            is_cisa_kev = False
            cisa_due = ""
            cisa_name = cve_obj.get("cisaVulnerabilityName", "")
            if cve_obj.get("cisaExploitAdd") or cve_obj.get("cisaActionDue") or cve_obj.get("cisaRequiredAction"):
                is_cisa_kev = True
                cisa_due = cve_obj.get("cisaActionDue", "Inmediato")

            # Resolver CWE
            weaknesses = cve_obj.get("weaknesses", [])
            cwe_list = []
            for w in weaknesses:
                for d in w.get("description", []):
                    val = d.get("value", "")
                    if val and val != "NVD-CWE-noinfo" and val != "NVD-CWE-Other":
                        cwe_list.append(val)
            if cwe_list:
                primary_cwe = cwe_list[0]
                cwe_label = cwe_labels.get(primary_cwe, primary_cwe)
            else:
                cwe_label = "No especificado"

            # Resolver Metricas CVSS
            metrics = cve_obj.get("metrics", {})
            cvss_list = metrics.get("cvssMetricV31", []) or metrics.get("cvssMetricV30", [])
            score = "N/A"
            sev = "DESCONOCIDO"
            vector_str = "N/A"
            attack_vec = "N/A"
            attack_comp = "N/A"
            priv_req = "N/A"
            user_int = "N/A"

            if cvss_list:
                cdata = cvss_list[0].get("cvssData", {})
                raw_score = cdata.get("baseScore", "N/A")
                score = raw_score
                vector_str = cdata.get("vectorString", "N/A")
                raw_av = cdata.get("attackVector", "")
                attack_vec = av_map.get(raw_av, raw_av or "N/A")
                attack_comp = cdata.get("attackComplexity", "N/A")
                priv_req = cdata.get("privilegesRequired", "N/A")
                user_int = cdata.get("userInteraction", "N/A")
                if isinstance(raw_score, (int, float)):
                    if raw_score >= 9.0: sev = "CRITICA"
                    elif raw_score >= 7.0: sev = "ALTA"
                    elif raw_score >= 4.0: sev = "MEDIA"
                    else: sev = "BAJA"
            elif metrics.get("cvssMetricV2"):
                v2_data = metrics.get("cvssMetricV2")[0].get("cvssData", {})
                score = v2_data.get("baseScore", "N/A")
                vector_str = v2_data.get("vectorString", "N/A")
                raw_sev = metrics.get("cvssMetricV2")[0].get("baseSeverity", "MEDIA").upper()
                if raw_sev == "HIGH": sev = "ALTA"
                elif raw_sev == "MEDIUM": sev = "MEDIA"
                elif raw_sev == "LOW": sev = "BAJA"

            # Descripcion
            descriptions = cve_obj.get("descriptions", [])
            desc_text = "Sin descripcion tecnica disponible."
            for d in descriptions:
                if d.get("lang") in ("es", "en"):
                    desc_text = d.get("value", "")
                    if d.get("lang") == "es":
                        break

            # Referencias
            references = [r.get("url", "") for r in cve_obj.get("references", []) if r.get("url")]

            parsed.append({
                "CVE": cve_id,
                "Fabricante": vendor_str,
                "Producto Afectado": prod_str,
                "Puntuacion CVSS v3": score,
                "Severidad": sev,
                "Debilidad (CWE)": cwe_label,
                "Vector de Ataque": attack_vec,
                "Vector Completo": vector_str,
                "Complejidad": attack_comp,
                "Privilegios Requeridos": priv_req,
                "Interaccion Usuario": user_int,
                "CISA KEV Activo": is_cisa_kev,
                "CISA Fecha Limite": cisa_due,
                "CISA Nombre": cisa_name,
                "Fecha Publicacion": published,
                "Descripcion": desc_text,
                "CPEs": cpe_criteria_list,
                "Referencias": references
            })
        return parsed

    def _populate_cve_table(self, vulnerabilidades: list = None):
        """Puebla la tabla maestra con las vulnerabilidades procesadas."""
        if vulnerabilidades is not None:
            self._cve_batch_list = vulnerabilidades
        self._cve_parsed_items = self._parse_cve_items()
        self._apply_cve_live_filter()

    def _apply_cve_live_filter(self):
        """Aplica filtros en memoria sobre la tabla sin reconsultar la API."""
        query = self.input_cve_filter.text().strip().lower()
        sev_filter = self.combo_cve_filter_sev.currentText()
        only_kev = self.chk_cve_only_kev.isChecked()

        filtered = []
        for item in self._cve_parsed_items:
            # Filtro Severidad
            if sev_filter != "Todas las Severidades" and item["Severidad"] != sev_filter:
                continue
            # Filtro CISA KEV
            if only_kev and not item["CISA KEV Activo"]:
                continue
            # Filtro Texto
            if query:
                search_haystack = (
                    f"{item['CVE']} {item['Fabricante']} {item['Producto Afectado']} "
                    f"{item['Debilidad (CWE)']} {item['Vector de Ataque']} {item['Descripcion']}"
                ).lower()
                if query not in search_haystack:
                    continue
            filtered.append(item)

        self._cve_current_filtered = filtered
        self.table_cve_results.setRowCount(len(filtered))

        for row, item in enumerate(filtered):
            cve_cell = QTableWidgetItem(str(item["CVE"]))
            vendor_cell = QTableWidgetItem(str(item["Fabricante"]))
            prod_cell = QTableWidgetItem(str(item["Producto Afectado"]))
            score_cell = QTableWidgetItem(str(item["Puntuacion CVSS v3"]))
            sev_cell = QTableWidgetItem(str(item["Severidad"]))
            cwe_cell = QTableWidgetItem(str(item["Debilidad (CWE)"]))
            vec_cell = QTableWidgetItem(str(item["Vector de Ataque"]))
            kev_cell = QTableWidgetItem("SI (En Explotacion)" if item["CISA KEV Activo"] else "-")
            pub_cell = QTableWidgetItem(str(item["Fecha Publicacion"]))

            # Tipografia y colores
            sev = item["Severidad"]
            if sev == "CRITICA":
                sev_cell.setForeground(QColor("#ef4444"))
                score_cell.setForeground(QColor("#ef4444"))
            elif sev == "ALTA":
                sev_cell.setForeground(QColor("#f97316"))
                score_cell.setForeground(QColor("#f97316"))
            elif sev == "MEDIA":
                sev_cell.setForeground(QColor("#eab308"))
                score_cell.setForeground(QColor("#eab308"))
            elif sev == "BAJA":
                sev_cell.setForeground(QColor("#22c55e"))
                score_cell.setForeground(QColor("#22c55e"))

            if item["CISA KEV Activo"]:
                kev_cell.setForeground(QColor("#ef4444"))
                kev_cell.setFont(self.font())

            cve_cell.setForeground(QColor("#38bdf8"))
            vendor_cell.setForeground(QColor("#f8fafc"))
            prod_cell.setForeground(QColor("#f8fafc"))
            cwe_cell.setForeground(QColor("#cbd5e1"))
            vec_cell.setForeground(QColor("#94a3b8"))
            pub_cell.setForeground(QColor("#64748b"))

            self.table_cve_results.setItem(row, 0, cve_cell)
            self.table_cve_results.setItem(row, 1, vendor_cell)
            self.table_cve_results.setItem(row, 2, prod_cell)
            self.table_cve_results.setItem(row, 3, score_cell)
            self.table_cve_results.setItem(row, 4, sev_cell)
            self.table_cve_results.setItem(row, 5, cwe_cell)
            self.table_cve_results.setItem(row, 6, vec_cell)
            self.table_cve_results.setItem(row, 7, kev_cell)
            self.table_cve_results.setItem(row, 8, pub_cell)

        total_all = len(self._cve_parsed_items)
        total_view = len(filtered)
        self.lbl_cve_stats.setText(f"Mostrando {total_view} de {total_all} vulnerabilidades")

        if total_view > 0:
            self.table_cve_results.selectRow(0)
        else:
            self._clear_cve_inspector_card()

    def _on_cve_selection_changed(self):
        """Actualiza la Ficha Forense del Inspector con el registro seleccionado."""
        selected_ranges = self.table_cve_results.selectedRanges()
        if not selected_ranges or not self._cve_current_filtered:
            return
        row = selected_ranges[0].topRow()
        if 0 <= row < len(self._cve_current_filtered):
            item = self._cve_current_filtered[row]
            self._update_cve_inspector_card(item)

    def _update_cve_inspector_card(self, item: Dict[str, Any]):
        """Rellena visualmente los componentes de la Ficha Forense."""
        cve_id = item.get("CVE", "N/A")
        vendor = item.get("Fabricante", "N/A")
        product = item.get("Producto Afectado", "N/A")
        score = item.get("Puntuacion CVSS v3", "N/A")
        sev = item.get("Severidad", "DESCONOCIDO")
        vector_txt = item.get("Vector de Ataque", "N/A")
        vector_full = item.get("Vector Completo", "N/A")
        cwe = item.get("Debilidad (CWE)", "N/A")
        cpes = item.get("CPEs", [])
        is_kev = item.get("CISA KEV Activo", False)
        kev_due = item.get("CISA Fecha Limite", "N/A")
        desc = item.get("Descripcion", "Sin descripcion disponible.")

        self.lbl_cve_card_title.setText(f"{cve_id}  |  Fabricante: {vendor}  |  Producto: {product}")

        # Estilo badge severidad
        sev_color = "#94a3b8"
        if sev == "CRITICA": sev_color = "#ef4444"
        elif sev == "ALTA": sev_color = "#f97316"
        elif sev == "MEDIA": sev_color = "#eab308"
        elif sev == "BAJA": sev_color = "#22c55e"

        self.lbl_cve_card_badge_sev.setText(f"CVSS {score} ({sev})")
        self.lbl_cve_card_badge_sev.setStyleSheet(f"background-color: #1e293b; color: {sev_color}; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px; border: 1px solid {sev_color};")

        self.lbl_cve_card_badge_vector.setText(f"VECTOR: {vector_txt.upper()}")

        if is_kev:
            self.lbl_cve_card_badge_kev.setText("CISA KEV ACTIVO (EXPLOTADO)")
            self.lbl_cve_card_badge_kev.setStyleSheet("background-color: #ef4444; color: #ffffff; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")
            self.lbl_cve_card_kev_due.setText(f"Mitigacion Requerida: {kev_due}")
            self.lbl_cve_card_kev_due.setStyleSheet("color: #ef4444; font-weight: bold; font-family: 'Consolas'; font-size: 10px; border: none;")
        else:
            self.lbl_cve_card_badge_kev.setText("CISA KEV: NO")
            self.lbl_cve_card_badge_kev.setStyleSheet("background-color: #1e293b; color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")
            self.lbl_cve_card_kev_due.setText("No catalogada")
            self.lbl_cve_card_kev_due.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 10px; border: none;")

        self.lbl_cve_card_cvss_vector.setText(vector_full)
        self.lbl_cve_card_cwe.setText(cwe)

        if cpes:
            cpe_disp = cpes[0]
            if len(cpes) > 1:
                cpe_disp += f" (+{len(cpes)-1} configuraciones adicionales)"
            self.lbl_cve_card_cpes.setText(cpe_disp)
        else:
            self.lbl_cve_card_cpes.setText("No se identificaron identificadores CPE especificos")

        self.txt_cve_card_desc.setPlainText(desc)

    def _clear_cve_inspector_card(self):
        """Limpia la tarjeta del inspector cuando no hay registros."""
        self.lbl_cve_card_title.setText("No hay vulnerabilidades que coincidan con los filtros actuales.")
        self.lbl_cve_card_badge_sev.setText("SEVERIDAD: N/A")
        self.lbl_cve_card_badge_sev.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")
        self.lbl_cve_card_badge_vector.setText("VECTOR: N/A")
        self.lbl_cve_card_badge_kev.setText("CISA KEV: NO")
        self.lbl_cve_card_badge_kev.setStyleSheet("background-color: #1e293b; color: #64748b; font-weight: bold; font-family: 'Consolas'; font-size: 10px; padding: 2px 8px; border-radius: 3px;")
        self.lbl_cve_card_cvss_vector.setText("N/A")
        self.lbl_cve_card_cwe.setText("N/A")
        self.lbl_cve_card_cpes.setText("N/A")
        self.lbl_cve_card_kev_due.setText("No catalogada")
        self.txt_cve_card_desc.clear()

    def _get_current_selected_cve_item(self) -> Optional[Dict[str, Any]]:
        """Retorna el item actualmente seleccionado en la tabla."""
        selected_ranges = self.table_cve_results.selectedRanges()
        if not selected_ranges or not self._cve_current_filtered:
            return None
        row = selected_ranges[0].topRow()
        if 0 <= row < len(self._cve_current_filtered):
            return self._cve_current_filtered[row]
        return None

    def _pivot_selected_cve_to_dfir(self):
        """Pivota el CVE seleccionado hacia la consola de investigacion DFIR."""
        item = self._get_current_selected_cve_item()
        if not item:
            QMessageBox.information(self, "Seleccion Requerida", "Seleccione una vulnerabilidad de la tabla.")
            return
        cve_id = item["CVE"]
        self.tabs.setCurrentIndex(4) # Pestaña 5: Consola DFIR
        self.input_term_target.setText(cve_id)
        self.run_preset_cve()

    def _open_selected_cve_nvd_url(self):
        """Abre la pagina oficial de la vulnerabilidad en el portal del NIST NVD."""
        item = self._get_current_selected_cve_item()
        if not item:
            QMessageBox.information(self, "Seleccion Requerida", "Seleccione una vulnerabilidad de la tabla.")
            return
        cve_id = item["CVE"]
        url = f"https://nvd.nist.gov/vuln/detail/{cve_id}"
        QDesktopServices.openUrl(QUrl(url))

    def _copy_selected_cve_card(self):
        """Copia al portapapeles un reporte forense formateado en Markdown de la vulnerabilidad."""
        item = self._get_current_selected_cve_item()
        if not item:
            QMessageBox.information(self, "Seleccion Requerida", "Seleccione una vulnerabilidad de la tabla.")
            return

        cpes_str = "\n".join(f"  - `{c}`" for c in item.get("CPEs", [])[:10]) or "  - No especificado"
        card_text = (
            f"### FICHA TECNICA DE VULNERABILIDAD — {item['CVE']}\n\n"
            f"- **Fabricante:** {item['Fabricante']}\n"
            f"- **Producto Afectado:** {item['Producto Afectado']}\n"
            f"- **Puntuacion CVSS v3:** {item['Puntuacion CVSS v3']} ({item['Severidad']})\n"
            f"- **Vector CVSS:** `{item['Vector Completo']}`\n"
            f"- **Vector de Ataque:** {item['Vector de Ataque']}\n"
            f"- **Debilidad CWE:** {item['Debilidad (CWE)']}\n"
            f"- **Estado CISA KEV:** {'ACTIVO (Explotacion en curso)' if item['CISA KEV Activo'] else 'No catalogada'}\n"
            f"- **Fecha Limite CISA:** {item['CISA Fecha Limite']}\n"
            f"- **Fecha Publicacion:** {item['Fecha Publicacion']}\n\n"
            f"#### Descripcion Tecnica\n{item['Descripcion']}\n\n"
            f"#### Configuraciones Afectadas (CPEs)\n{cpes_str}\n\n"
            f"**Enlace NIST NVD:** https://nvd.nist.gov/vuln/detail/{item['CVE']}\n"
        )
        QApplication.clipboard().setText(card_text)
        QMessageBox.information(self, "Copiado", f"La ficha tecnica de {item['CVE']} ha sido copiada al portapapeles.")

    def _on_cve_row_double_clicked(self, item: QTableWidgetItem):
        """Doble clic pivota directamente a la consola DFIR."""
        self._pivot_selected_cve_to_dfir()

    def start_cve_batch_fetch(self):
        """Dispara el hilo asincronico para la recoleccion masiva de CVEs."""
        if hasattr(self, '_worker_cve_batch') and self._worker_cve_batch and self._worker_cve_batch.isRunning():
            QMessageBox.warning(self, "Busqueda en Curso", "Ya existe un proceso de extraccion NVD activo.")
            return

        # Validar fechas
        q_start = self.dt_cve_start.date()
        q_end = self.dt_cve_end.date()
        if q_start > q_end:
            QMessageBox.warning(self, "Rango Invalido", "La fecha de inicio no puede ser posterior a la fecha de fin.")
            return

        import datetime as _dt
        start_dt = _dt.datetime(q_start.year(), q_start.month(), q_start.day(), 0, 0, 0)
        end_dt = _dt.datetime(q_end.year(), q_end.month(), q_end.day(), 23, 59, 59)

        sevs = []
        if self.chk_cve_critical.isChecked(): sevs.append("CRITICAL")
        if self.chk_cve_high.isChecked(): sevs.append("HIGH")
        if self.chk_cve_medium.isChecked(): sevs.append("MEDIUM")
        if self.chk_cve_low.isChecked(): sevs.append("LOW")

        if not sevs:
            QMessageBox.warning(self, "Seleccion Requerida", "Debe seleccionar al menos un nivel de severidad CVSS.")
            return

        # Preparar UI
        self._cve_batch_list = []
        self._cve_parsed_items = []
        self._cve_current_filtered = []
        self.table_cve_results.setRowCount(0)
        self.txt_cve_log.clear()
        self._clear_cve_inspector_card()
        self.progress_cve_batch.setValue(0)
        self.btn_cve_fetch.setEnabled(False)
        self.btn_cve_fetch.setText("Buscando...")
        self.btn_cve_stop.setEnabled(True)
        self.btn_cve_export_md.setEnabled(False)
        self.btn_cve_export_xlsx.setEnabled(False)

        slack_url = self.input_cve_slack.text().strip()
        nvd_key = os.environ.get("NVD_API_KEY", "")

        self._worker_cve_batch = CveBatchFetchWorker(start_dt, end_dt, sevs, nvd_key, slack_url)
        self._worker_cve_batch.progress_signal.connect(self._on_cve_progress)
        self._worker_cve_batch.finished_signal.connect(self._on_cve_finished)
        self._worker_cve_batch.error_signal.connect(self._on_cve_error)
        self._worker_cve_batch.start()

    def stop_cve_batch_fetch(self):
        """Detiene de forma cooperativa la busqueda de CVEs."""
        if hasattr(self, '_worker_cve_batch') and self._worker_cve_batch and self._worker_cve_batch.isRunning():
            self._worker_cve_batch._is_killed = True
            self.txt_cve_log.append("<span style='color: #ef4444;'>[CANCELACION] Solicitando parada segura del proceso NVD...</span>")
            self._worker_cve_batch.quit()
            self.btn_cve_fetch.setEnabled(True)
            self.btn_cve_fetch.setText("Iniciar Busqueda NVD")
            self.btn_cve_stop.setEnabled(False)

    def _on_cve_progress(self, pct: int, msg: str):
        self.progress_cve_batch.setValue(pct)
        if msg:
            self.txt_cve_log.append(msg)

    def _on_cve_finished(self, vulnerabilidades: list):
        self._cve_batch_list = vulnerabilidades
        self.btn_cve_fetch.setEnabled(True)
        self.btn_cve_fetch.setText("Iniciar Busqueda NVD")
        self.btn_cve_stop.setEnabled(False)
        self.progress_cve_batch.setValue(100)

        total = len(vulnerabilidades)
        self._populate_cve_table(vulnerabilidades)

        if total > 0:
            self.btn_cve_export_md.setEnabled(True)
            self.btn_cve_export_xlsx.setEnabled(True)
            QMessageBox.information(self, "Extraccion Completada", f"Se descargaron con exito {total} vulnerabilidades desde NVD NIST.")
        else:
            QMessageBox.information(self, "Sin Resultados", "No se encontraron vulnerabilidades en el rango de fechas y severidades seleccionadas.")

    def _on_cve_error(self, err_msg: str):
        self.btn_cve_fetch.setEnabled(True)
        self.btn_cve_fetch.setText("Iniciar Busqueda NVD")
        self.btn_cve_stop.setEnabled(False)
        self.txt_cve_log.append(f"<span style='color: #ef4444;'>[ERROR CRITICO]: {he(err_msg)}</span>")
        QMessageBox.critical(self, "Error en Busqueda NVD", f"Ocurrio un error al contactar la API de NVD:\n{err_msg}")

    def export_cve_markdown(self):
        """Exporta los CVEs descargados a un archivo Markdown (.md) estructurado."""
        if not self._cve_parsed_items:
            QMessageBox.warning(self, "Exportacion", "No hay datos de CVEs para exportar.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar reporte en Markdown",
            f"CVE_Intel_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
            "Archivos Markdown (*.md);;Todos los archivos (*.*)"
        )
        if not file_path:
            return

        data_list = self._cve_parsed_items
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("# Reporte de Inteligencia de Vulnerabilidades (NVD NIST 2.0)\n\n")
                f.write("**Generado por:** OpenXDR Unified Command Center — SOC Master Cockpit\n")
                f.write(f"**Fecha de generacion:** {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}\n")
                f.write(f"**Total vulnerabilidades:** {len(data_list)}\n\n")
                f.write("---\n\n")

                for item in data_list:
                    f.write(f"## [{item['CVE']}](https://nvd.nist.gov/vuln/detail/{item['CVE']})\n")
                    f.write(f"* **Fabricante:** {item['Fabricante']}\n")
                    f.write(f"* **Producto Afectado:** {item['Producto Afectado']}\n")
                    f.write(f"* **Puntuacion CVSS v3:** `{item['Puntuacion CVSS v3']}` ({item['Severidad']})\n")
                    f.write(f"* **Vector CVSS:** `{item['Vector Completo']}`\n")
                    f.write(f"* **Vector de Ataque:** `{item['Vector de Ataque']}`\n")
                    f.write(f"* **Debilidad CWE:** {item['Debilidad (CWE)']}\n")
                    f.write(f"* **Estado CISA KEV:** {'ACTIVO (Explotacion en Curso)' if item['CISA KEV Activo'] else 'No catalogada'}\n")
                    if item['CISA KEV Activo']:
                        f.write(f"* **Fecha Limite de Mitigacion CISA:** {item['CISA Fecha Limite']}\n")
                    f.write(f"* **Fecha de Publicacion:** {item['Fecha Publicacion']}\n\n")
                    f.write(f"### Descripcion Tecnica\n{item['Descripcion']}\n\n")
                    if item.get("CPEs"):
                        f.write("### Configuraciones y Versiones Afectadas (CPEs)\n")
                        for cpe in item["CPEs"][:15]:
                            f.write(f"- `{cpe}`\n")
                        f.write("\n")
                    f.write("---\n\n")

            QMessageBox.information(self, "Exportacion Exitosa", f"El reporte Markdown ha sido guardado exitosamente en:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error de Exportacion", f"No se pudo guardar el archivo Markdown:\n{e}")

    def export_cve_excel(self):
        """Exporta los CVEs descargados a una hoja de calculo Excel (.xlsx) estructurada."""
        if not self._cve_parsed_items:
            QMessageBox.warning(self, "Exportacion", "No hay datos de CVEs para exportar.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar reporte en Excel",
            f"CVE_Intel_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
            "Archivos de Excel (*.xlsx);;Todos los archivos (*.*)"
        )
        if not file_path:
            return

        try:
            export_rows = []
            for item in self._cve_parsed_items:
                export_rows.append({
                    "CVE ID": item["CVE"],
                    "Fabricante": item["Fabricante"],
                    "Producto Afectado": item["Producto Afectado"],
                    "CVSS v3": item["Puntuacion CVSS v3"],
                    "Severidad": item["Severidad"],
                    "Debilidad (CWE)": item["Debilidad (CWE)"],
                    "Vector de Ataque": item["Vector de Ataque"],
                    "Vector Completo": item["Vector Completo"],
                    "CISA KEV": "SI" if item["CISA KEV Activo"] else "NO",
                    "CISA Fecha Limite": item["CISA Fecha Limite"],
                    "Fecha Publicacion": item["Fecha Publicacion"],
                    "Descripcion Tecnica": item["Descripcion"],
                    "Total CPEs Identificados": len(item.get("CPEs", []))
                })
            df = pd.DataFrame(export_rows)
            df.to_excel(file_path, index=False)
            QMessageBox.information(self, "Exportacion Exitosa", f"El reporte Excel se ha generado y guardado exitosamente en:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error de Exportacion", f"No se pudo generar el archivo Excel:\n{e}")

    def clear_cve_batch_data(self):
        """Limpia la tabla, el inspector y los registros de la pestana de CVEs."""
        self._cve_batch_list = []
        self._cve_parsed_items = []
        self._cve_current_filtered = []
        self.table_cve_results.setRowCount(0)
        self.txt_cve_log.clear()
        self._clear_cve_inspector_card()
        self.progress_cve_batch.setValue(0)
        self.lbl_cve_stats.setText("0 vulnerabilidades cargadas")
        self.btn_cve_export_md.setEnabled(False)
        self.btn_cve_export_xlsx.setEnabled(False)

