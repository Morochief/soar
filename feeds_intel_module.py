#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC - FEEDS INTEL GUI DIALOG (CTI & VULNERABILITY ADVISORIES)
=============================================================================
Ventana interactiva de Inteligencia de Amenazas (CTI) para el OpenXDR SOAR.
Gestiona 15 fuentes RSS/Atom de primer nivel, deduplicación SQLite, visor in-app
de noticias web completas, filtros por fuente, estado y fecha, paginación
profesional, ordenamiento interactivo y formateo de reportes con IA (Google
Gemini / NVIDIA NIM / OpenAI) sincronizado con Technoma Tickets.
"""

import sys
import os
import re
import html
from datetime import datetime
from typing import Dict, Any, List, Optional

import requests
from bs4 import BeautifulSoup

from PySide6.QtCore import Qt, QSize, QThreadPool, QThread, Signal, Slot, QUrl
from PySide6.QtGui import QColor, QFont, QIcon, QDesktopServices, QClipboard
from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView,
    QTextEdit, QTextBrowser, QProgressBar, QSplitter, QFrame, QTabWidget,
    QMessageBox, QApplication, QSizePolicy
)

from feeds_engine import (
    FeedsDatabase, FeedItem, FEEDS_CONFIG, RSSFetchTask,
    FEED_TIER_MAPPING, CTI_TIERS, TIER_TACTICAL, TIER_RESEARCH, TIER_NEWS
)
from feeds_ai_orchestrator import FeedsAIWorker, FeedsAIOrchestrator


class WebReaderWorker(QThread):
    """
    Worker asíncrono para descargar y limpiar artículos completos desde la web
    sin bloquear la interfaz gráfica del SOAR.
    """
    article_fetched = Signal(int, str, str)  # item_id, html_content, plain_text
    fetch_failed = Signal(int, str)          # item_id, error_message

    def __init__(self, item_id: int, url: str):
        super().__init__()
        self.item_id = item_id
        self.url = url

    def run(self):
        if not self.url or not self.url.startswith("http"):
            self.fetch_failed.emit(self.item_id, "URL no válida para extracción web.")
            return

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
        }

        try:
            resp = requests.get(self.url, headers=headers, timeout=12, verify=False)
            if resp.status_code != 200:
                self.fetch_failed.emit(self.item_id, f"El servidor web respondió con código HTTP {resp.status_code}")
                return

            soup = BeautifulSoup(resp.text, "html.parser")

            # Eliminar elementos no deseados
            for tag in soup(["script", "style", "nav", "header", "footer", "aside", "noscript", "iframe", "form", "svg"]):
                tag.decompose()

            # Buscar contenedor principal de la noticia
            container = (
                soup.find(id=re.compile(r"(articlebody|article-body|post-content|story-body|entry-content|main-content)", re.I)) or
                soup.find(class_=re.compile(r"(articlebody|article-body|post-content|story-body|entry-content|main-content)", re.I)) or
                soup.find("article") or
                soup.find("main") or
                soup.body
            )

            if not container:
                self.fetch_failed.emit(self.item_id, "No se encontró el cuerpo del artículo en la página.")
                return

            paragraphs: List[str] = []
            plain_lines: List[str] = []

            for elem in container.find_all(["h2", "h3", "h4", "p", "ul", "ol", "blockquote"]):
                raw_txt = elem.get_text(" ", strip=True)
                if not raw_txt:
                    continue

                if len(raw_txt) < 30 and elem.name == "p":
                    continue

                # Resaltar CVEs en el texto
                highlighted_txt = re.sub(
                    r"\b(CVE-\d{4}-\d{4,7})\b",
                    r'<span style="background-color: #78350f; color: #fef08a; padding: 2px 6px; border-radius: 4px; font-weight: bold; border: 1px solid #ca8a04;">\1</span>',
                    raw_txt
                )

                if elem.name in ["h2", "h3"]:
                    paragraphs.append(f'<h3 style="color: #38bdf8; margin-top: 14px; margin-bottom: 6px; font-size: 14px;">{highlighted_txt}</h3>')
                    plain_lines.append(f"\n### {raw_txt}\n")
                elif elem.name == "h4":
                    paragraphs.append(f'<h4 style="color: #93c5fd; margin-top: 10px; margin-bottom: 4px; font-size: 13px;">{highlighted_txt}</h4>')
                    plain_lines.append(f"\n#### {raw_txt}\n")
                elif elem.name == "p":
                    paragraphs.append(f'<p style="margin-bottom: 10px; line-height: 1.6; font-size: 12px; color: #e2e8f0;">{highlighted_txt}</p>')
                    plain_lines.append(raw_txt)
                elif elem.name in ["ul", "ol"]:
                    items = [f'<li style="margin-bottom: 4px; color: #cbd5e1;">{li.get_text(" ", strip=True)}</li>' for li in elem.find_all("li")]
                    if items:
                        paragraphs.append(f'<ul style="margin-left: 20px; margin-bottom: 10px;">{"".join(items)}</ul>')
                        plain_lines.append("- " + "\n- ".join(li.get_text(" ", strip=True) for li in elem.find_all("li")))
                elif elem.name == "blockquote":
                    paragraphs.append(f'<blockquote style="border-left: 3px solid #38bdf8; margin: 10px 0; padding-left: 12px; color: #94a3b8; font-style: italic;">{highlighted_txt}</blockquote>')
                    plain_lines.append(f"> {raw_txt}")

            if not paragraphs:
                self.fetch_failed.emit(self.item_id, "No se pudieron extraer párrafos legibles del portal.")
                return

            full_html = "\n".join(paragraphs)
            plain_text = "\n\n".join(plain_lines)
            self.article_fetched.emit(self.item_id, full_html, plain_text)

        except Exception as e:
            self.fetch_failed.emit(self.item_id, f"Error durante la extracción web: {str(e)}")


class FeedsIntelDialog(QDialog):
    """
    Diálogo principal de CTI Feeds integrado en OpenXDR Master Cockpit SOAR.
    Permite maximización completa, lectura in-app, paginación, filtros temporales y ordenamiento.
    """

    SEVERITY_COLORS = {
        "Crítica 🟣": "#9333ea",
        "Alta 🔴": "#dc2626",
        "Media 🟡": "#d97706",
        "Baja 🟢": "#16a34a",
        "Informativo ℹ️": "#2563eb",
        "PENDIENTE": "#64748b"
    }

    STATUS_COLORS = {
        "NUEVO": "#0284c7",
        "ANALIZADO": "#10b981",
        "ESCALADO": "#a855f7",
        "IGNORADO": "#64748b"
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📡 Technoma SOC - Módulo de Feeds CTI & Alertas de Vulnerabilidad")

        # Habilitar Maximizar, Minimizar y Cerrar estándar en Windows
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1360, 850)
        self.setMinimumSize(1020, 660)

        self.db = FeedsDatabase()
        self.thread_pool = QThreadPool.globalInstance()
        self.active_sync_tasks = 0
        self.current_selected_item: Optional[Dict[str, Any]] = None
        self.ai_worker: Optional[FeedsAIWorker] = None
        self.web_worker: Optional[WebReaderWorker] = None

        # Estado de paginación
        self.current_page = 1
        self.page_size = 50
        self.total_pages = 1
        self.total_matching_items = 0

        self._apply_dark_style()
        self._init_ui()
        self.load_items_from_db(reset_page=True)

    def _apply_dark_style(self):
        """Aplica el diseño visual institucional Dark Mode del SOC."""
        self.setStyleSheet("""
            QDialog {
                background-color: #0b1120;
                color: #e2e8f0;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QFrame#topBar {
                background-color: #111827;
                border-radius: 6px;
                border: 1px solid #1f2937;
            }
            QFrame#filterBar, QFrame#bottomBar {
                background-color: #131d2e;
                border-radius: 6px;
                border: 1px solid #1e293b;
            }
            QFrame#paginationBar {
                background-color: #0d1527;
                border: 1px solid #1e293b;
                border-radius: 4px;
            }
            QLabel {
                color: #cbd5e1;
                font-size: 11px;
            }
            QLineEdit, QComboBox {
                background-color: #0f172a;
                color: #ffffff;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 5px 8px;
                font-size: 11px;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #38bdf8;
            }
            QComboBox QAbstractItemView {
                background-color: #0f172a;
                color: #ffffff;
                border: 1px solid #334155;
                selection-background-color: #1e3a8a;
                selection-color: #ffffff;
                outline: none;
            }
            QTableWidget {
                background-color: #090e17;
                color: #e2e8f0;
                gridline-color: #1e293b;
                border: 1px solid #1e293b;
                border-radius: 6px;
                selection-background-color: #1e3a8a;
                selection-color: #ffffff;
                font-size: 11px;
                alternate-background-color: #0f172a;
            }
            QHeaderView::section {
                background-color: #1e293b;
                color: #94a3b8;
                font-weight: bold;
                padding: 6px 8px;
                border: 1px solid #334155;
                font-size: 11px;
            }
            QHeaderView::section:hover {
                background-color: #334155;
                color: #38bdf8;
            }
            QTabWidget::pane {
                border: 1px solid #1e293b;
                background-color: #090e17;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #131d2e;
                color: #94a3b8;
                padding: 7px 14px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                font-weight: 600;
                font-size: 11px;
            }
            QTabBar::tab:selected {
                background-color: #090e17;
                color: #38bdf8;
                border-bottom: 2px solid #38bdf8;
            }
            QTabBar::tab:hover:!selected {
                background-color: #1e293b;
                color: #cbd5e1;
            }
            QTextEdit, QTextBrowser {
                background-color: #070c14;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                border-radius: 4px;
                padding: 10px;
                font-size: 12px;
                line-height: 1.5;
            }
            QPushButton {
                background-color: #1e293b;
                color: #ffffff;
                border: 1px solid #475569;
                border-radius: 4px;
                padding: 5px 12px;
                font-weight: 600;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #334155;
                border-color: #94a3b8;
            }
            QPushButton:disabled {
                background-color: #131d2e;
                color: #475569;
                border-color: #1e293b;
            }
        """)

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 8, 10, 8)
        main_layout.setSpacing(6)

        # =====================================================================
        # 1. BARRA SUPERIOR (HEADER COMPACTO & KPI PILLS)
        # =====================================================================
        top_bar = QFrame()
        top_bar.setObjectName("topBar")
        top_bar.setFixedHeight(48)
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(10, 6, 10, 6)
        top_layout.setSpacing(10)

        lbl_title = QLabel("📡 CTI INTEL FEEDS & VULN ADVISORIES")
        lbl_title.setStyleSheet("font-size: 12px; font-weight: bold; color: #38bdf8; letter-spacing: 0.8px;")
        top_layout.addWidget(lbl_title)

        # KPI Badges
        self.badge_total = QLabel("Total: 0")
        self.badge_total.setStyleSheet("background-color: #1e293b; color: #cbd5e1; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;")
        top_layout.addWidget(self.badge_total)

        self.badge_nuevos = QLabel("Nuevos: 0 ⚪")
        self.badge_nuevos.setStyleSheet("background-color: #082f49; color: #38bdf8; border: 1px solid #0284c7; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;")
        top_layout.addWidget(self.badge_nuevos)

        self.badge_analizados = QLabel("Analizados: 0 🟢")
        self.badge_analizados.setStyleSheet("background-color: #064e3b; color: #34d399; border: 1px solid #059669; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;")
        top_layout.addWidget(self.badge_analizados)

        self.badge_escalados = QLabel("Escalados: 0 🎫")
        self.badge_escalados.setStyleSheet("background-color: #4c1d95; color: #c084fc; border: 1px solid #7c3aed; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;")
        top_layout.addWidget(self.badge_escalados)

        top_layout.addStretch()

        self.btn_osint = QPushButton("🌐 Canales OSINT / Redes")
        self.btn_osint.setFixedHeight(30)
        self.btn_osint.setStyleSheet("background-color: #334155; color: #e2e8f0; font-weight: bold; padding: 4px 12px; border: 1px solid #475569;")
        self.btn_osint.setToolTip("Acceso directo a analistas, monitoreo de Dark Web y fuentes comunitarias sin RSS (Gaspar, Krassas, VCERTAnalyzer, Abuse.ch)")
        self.btn_osint.clicked.connect(self.show_osint_channels_dialog)
        top_layout.addWidget(self.btn_osint)

        self.btn_sync = QPushButton(f"🔄 Sincronizar {len(FEEDS_CONFIG)} Feeds")
        self.btn_sync.setFixedHeight(30)
        self.btn_sync.setStyleSheet("background-color: #0284c7; color: #ffffff; font-weight: bold; padding: 4px 12px; border: none;")
        self.btn_sync.setToolTip(f"Descarga concurrentemente las {len(FEEDS_CONFIG)} fuentes CTI (RSS/Atom/JSON) y deduplica en SQLite")
        self.btn_sync.clicked.connect(self.sync_all_feeds)
        top_layout.addWidget(self.btn_sync)

        main_layout.addWidget(top_bar)

        # =====================================================================
        # 2. BARRA DE FILTROS, FECHAS Y BÚSQUEDA (COMPACTA)
        # =====================================================================
        filter_bar = QFrame()
        filter_bar.setObjectName("filterBar")
        filter_bar.setFixedHeight(44)
        filter_layout = QHBoxLayout(filter_bar)
        filter_layout.setContentsMargins(10, 4, 10, 4)
        filter_layout.setSpacing(6)

        # Filtro Nivel CTI
        lbl_tier = QLabel("Nivel CTI:")
        lbl_tier.setStyleSheet("font-weight: 600; color: #94a3b8;")
        filter_layout.addWidget(lbl_tier)

        self.combo_filter_tier = QComboBox()
        self.combo_filter_tier.setFixedWidth(160)
        self.combo_filter_tier.addItems(["Todos los Niveles", TIER_TACTICAL, TIER_RESEARCH, TIER_NEWS])
        self.combo_filter_tier.currentIndexChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        filter_layout.addWidget(self.combo_filter_tier)

        # Filtro Fuente
        lbl_f = QLabel("Fuente:")
        lbl_f.setStyleSheet("font-weight: 600; color: #94a3b8;")
        filter_layout.addWidget(lbl_f)

        self.combo_filter_source = QComboBox()
        self.combo_filter_source.setFixedWidth(145)
        self.combo_filter_source.addItem("Todas las Fuentes")
        for f in FEEDS_CONFIG:
            self.combo_filter_source.addItem(f["name"])
        self.combo_filter_source.currentIndexChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        filter_layout.addWidget(self.combo_filter_source)

        # Filtro Estado
        lbl_e = QLabel("Estado:")
        lbl_e.setStyleSheet("font-weight: 600; color: #94a3b8;")
        filter_layout.addWidget(lbl_e)

        self.combo_filter_status = QComboBox()
        self.combo_filter_status.setFixedWidth(95)
        self.combo_filter_status.addItems(["Todos", "NUEVO", "ANALIZADO", "ESCALADO", "IGNORADO"])
        self.combo_filter_status.currentIndexChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        filter_layout.addWidget(self.combo_filter_status)

        # Filtro Fecha
        lbl_d = QLabel("Fecha:")
        lbl_d.setStyleSheet("font-weight: 600; color: #94a3b8;")
        filter_layout.addWidget(lbl_d)

        self.combo_filter_date = QComboBox()
        self.combo_filter_date.setFixedWidth(120)
        self.combo_filter_date.addItems([
            "Cualquier Fecha",
            "Últimas 24h",
            "Últimos 7 días",
            "Últimos 30 días",
            "Últimos 90 días"
        ])
        self.combo_filter_date.currentIndexChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        filter_layout.addWidget(self.combo_filter_date)

        # Búsqueda
        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("🔍 Buscar por CVE, malware, tecnología o palabra clave...")
        self.txt_search.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.txt_search.textChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        filter_layout.addWidget(self.txt_search)

        btn_clear = QPushButton("🧹")
        btn_clear.setToolTip("Restablecer todos los filtros de búsqueda")
        btn_clear.setFixedWidth(28)
        btn_clear.clicked.connect(self._clear_filters)
        filter_layout.addWidget(btn_clear)

        # Motor IA
        lbl_ia = QLabel("Motor IA:")
        lbl_ia.setStyleSheet("font-weight: 600; color: #94a3b8;")
        filter_layout.addWidget(lbl_ia)

        self.combo_ai_provider = QComboBox()
        self.combo_ai_provider.setFixedWidth(210)
        self.combo_ai_provider.addItems([
            "Google Gemini 2.5 Flash (SOC Nativo)",
            "NVIDIA NIM - DeepSeek v4.1-flash",
            "OpenAI GPT-4o-mini"
        ])
        filter_layout.addWidget(self.combo_ai_provider)

        main_layout.addWidget(filter_bar)

        # Barra de progreso delgada para tareas concurrentes
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(3)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar { background-color: #1e293b; border: none; }
            QProgressBar::chunk { background-color: #38bdf8; }
        """)
        self.progress_bar.hide()
        main_layout.addWidget(self.progress_bar)

        # =====================================================================
        # 3. PANEL CENTRAL CON SPLITTER PROPORCIONAL
        # =====================================================================
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)

        # --- Panel Izquierdo: Tabla de Alertas CTI con Paginación ---
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 4, 0)
        left_layout.setSpacing(4)

        self.table_items = QTableWidget()
        self.table_items.setColumnCount(7)
        self.table_items.setHorizontalHeaderLabels(["ID", "Nivel CTI", "Fuente", "Severidad", "Título / Alerta", "Fecha", "Estado"])
        self.table_items.verticalHeader().setVisible(False)
        self.table_items.verticalHeader().setDefaultSectionSize(28)
        self.table_items.setAlternatingRowColors(True)

        header = self.table_items.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents) # ID
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents) # Nivel CTI
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents) # Fuente
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents) # Severidad
        header.setSectionResizeMode(4, QHeaderView.Stretch)          # Título
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents) # Fecha
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents) # Estado

        self.table_items.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_items.setSelectionMode(QTableWidget.SingleSelection)
        self.table_items.itemSelectionChanged.connect(self._on_table_selection_changed)
        self.table_items.setSortingEnabled(True)
        left_layout.addWidget(self.table_items)

        # --- Barra de Paginación Compacta ---
        pagination_bar = QFrame()
        pagination_bar.setObjectName("paginationBar")
        pagination_bar.setFixedHeight(34)
        pagination_layout = QHBoxLayout(pagination_bar)
        pagination_layout.setContentsMargins(8, 2, 8, 2)
        pagination_layout.setSpacing(6)

        self.btn_first_page = QPushButton("⏮")
        self.btn_first_page.setFixedWidth(28)
        self.btn_first_page.setToolTip("Primera página")
        self.btn_first_page.clicked.connect(self._go_first_page)
        pagination_layout.addWidget(self.btn_first_page)

        self.btn_prev_page = QPushButton("◀")
        self.btn_prev_page.setFixedWidth(28)
        self.btn_prev_page.setToolTip("Página anterior")
        self.btn_prev_page.clicked.connect(self._go_prev_page)
        pagination_layout.addWidget(self.btn_prev_page)

        self.lbl_page_info = QLabel("Página 1 de 1")
        self.lbl_page_info.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 11px;")
        pagination_layout.addWidget(self.lbl_page_info)

        self.btn_next_page = QPushButton("▶")
        self.btn_next_page.setFixedWidth(28)
        self.btn_next_page.setToolTip("Página siguiente")
        self.btn_next_page.clicked.connect(self._go_next_page)
        pagination_layout.addWidget(self.btn_next_page)

        self.btn_last_page = QPushButton("⏭")
        self.btn_last_page.setFixedWidth(28)
        self.btn_last_page.setToolTip("Última página")
        self.btn_last_page.clicked.connect(self._go_last_page)
        pagination_layout.addWidget(self.btn_last_page)

        pagination_layout.addStretch()

        self.lbl_pagination_stats = QLabel("Mostrando 0 de 0 alertas")
        self.lbl_pagination_stats.setStyleSheet("color: #94a3b8; font-size: 10px;")
        pagination_layout.addWidget(self.lbl_pagination_stats)

        lbl_per_page = QLabel("Por pág:")
        lbl_per_page.setStyleSheet("color: #64748b; font-size: 10px;")
        pagination_layout.addWidget(lbl_per_page)

        self.combo_page_size = QComboBox()
        self.combo_page_size.setFixedWidth(65)
        self.combo_page_size.addItems(["25", "50", "100", "200"])
        self.combo_page_size.setCurrentText("50")
        self.combo_page_size.currentIndexChanged.connect(lambda: self.load_items_from_db(reset_page=True))
        pagination_layout.addWidget(self.combo_page_size)

        left_layout.addWidget(pagination_bar)
        splitter.addWidget(left_widget)

        # --- Panel Derecho: 3 Pestañas (Lectura In-App, Reporte IA, IOCs) ---
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(4, 0, 0, 0)
        right_layout.setSpacing(4)

        self.tabs_right = QTabWidget()

        # -------------------------------------------------------------
        # PESTAÑA 1 (PREDETERMINADA): LECTURA DE NOTICIA (IN-APP READER)
        # -------------------------------------------------------------
        tab_reader = QWidget()
        tab_reader_layout = QVBoxLayout(tab_reader)
        tab_reader_layout.setContentsMargins(6, 6, 6, 6)
        tab_reader_layout.setSpacing(6)

        # Tarjeta de cabecera de la noticia seleccionada
        self.card_article_header = QFrame()
        self.card_article_header.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
                border: 1px solid #1e293b;
                border-radius: 6px;
                padding: 6px;
            }
        """)
        header_box = QVBoxLayout(self.card_article_header)
        header_box.setContentsMargins(8, 6, 8, 6)
        header_box.setSpacing(4)

        self.lbl_reader_title = QLabel("Seleccione una alerta de la tabla para leer la noticia")
        self.lbl_reader_title.setStyleSheet("font-size: 13px; font-weight: bold; color: #38bdf8;")
        self.lbl_reader_title.setWordWrap(True)
        header_box.addWidget(self.lbl_reader_title)

        meta_row = QHBoxLayout()
        meta_row.setSpacing(6)

        self.lbl_reader_source = QLabel("Fuente: -")
        self.lbl_reader_source.setStyleSheet("color: #94a3b8; font-size: 11px;")
        meta_row.addWidget(self.lbl_reader_source)

        self.lbl_reader_date = QLabel("Fecha: -")
        self.lbl_reader_date.setStyleSheet("color: #94a3b8; font-size: 11px;")
        meta_row.addWidget(self.lbl_reader_date)

        self.lbl_reader_category = QLabel("Categoría: -")
        self.lbl_reader_category.setStyleSheet("color: #94a3b8; font-size: 11px;")
        meta_row.addWidget(self.lbl_reader_category)

        meta_row.addStretch()

        self.lbl_reader_link = QLabel("")
        self.lbl_reader_link.setOpenExternalLinks(True)
        self.lbl_reader_link.setStyleSheet("color: #60a5fa; font-size: 11px; text-decoration: underline;")
        meta_row.addWidget(self.lbl_reader_link)

        header_box.addLayout(meta_row)
        tab_reader_layout.addWidget(self.card_article_header)

        # Barra de acciones de lectura
        reader_actions = QHBoxLayout()
        reader_actions.setSpacing(6)

        self.btn_fetch_full_web = QPushButton("🌐 Cargar Noticia Completa de la Web")
        self.btn_fetch_full_web.setStyleSheet("background-color: #0369a1; color: #ffffff; font-weight: bold;")
        self.btn_fetch_full_web.setToolTip("Descarga y extrae los párrafos íntegros del portal de noticias original")
        self.btn_fetch_full_web.clicked.connect(self.fetch_full_article_from_web)
        reader_actions.addWidget(self.btn_fetch_full_web)

        self.btn_reader_ai_analyze = QPushButton("⚡ Analizar esta Noticia con IA")
        self.btn_reader_ai_analyze.setStyleSheet("background-color: #7c3aed; color: #ffffff; font-weight: bold;")
        self.btn_reader_ai_analyze.setToolTip("Genera el reporte de detección de vulnerabilidad para clientes usando la IA")
        self.btn_reader_ai_analyze.clicked.connect(self.process_selected_with_ai)
        reader_actions.addWidget(self.btn_reader_ai_analyze)

        self.btn_copy_article_text = QPushButton("📋 Copiar Texto")
        self.btn_copy_article_text.clicked.connect(self.copy_article_content_to_clipboard)
        reader_actions.addWidget(self.btn_copy_article_text)

        reader_actions.addStretch()

        self.lbl_fetch_status = QLabel("")
        self.lbl_fetch_status.setStyleSheet("color: #38bdf8; font-size: 11px; font-style: italic;")
        reader_actions.addWidget(self.lbl_fetch_status)

        tab_reader_layout.addLayout(reader_actions)

        # Visor de texto enriquecido / editorial de la noticia
        self.txt_reader_view = QTextBrowser()
        self.txt_reader_view.setOpenExternalLinks(True)
        self.txt_reader_view.setPlaceholderText(
            "Seleccione cualquier artículo o alerta en la tabla izquierda para comenzar a leer...\n\n"
            "• Aquí se renderizará el texto completo de la noticia.\n"
            "• Podrá leer todos los detalles técnicos para evaluar si la amenaza afecta a sus clientes antes de lanzar la IA."
        )
        tab_reader_layout.addWidget(self.txt_reader_view)

        self.tabs_right.addTab(tab_reader, "📰 1. Lectura de Noticia (In-App Reader)")

        # -------------------------------------------------------------
        # PESTAÑA 2: REPORTE CLIENTE (IA MARKDOWN)
        # -------------------------------------------------------------
        tab_report = QWidget()
        tab_report_layout = QVBoxLayout(tab_report)
        tab_report_layout.setContentsMargins(6, 6, 6, 6)
        tab_report_layout.setSpacing(6)

        # Barra de herramientas del reporte de cliente
        report_tools = QHBoxLayout()
        report_tools.setSpacing(6)

        self.btn_tab_reanalyze = QPushButton("⚡ Procesar con IA")
        self.btn_tab_reanalyze.setStyleSheet("background-color: #7c3aed; color: #ffffff; font-weight: bold;")
        self.btn_tab_reanalyze.clicked.connect(self.process_selected_with_ai)
        report_tools.addWidget(self.btn_tab_reanalyze)

        self.btn_tab_copy = QPushButton("📋 Copiar Reporte Cliente")
        self.btn_tab_copy.setStyleSheet("background-color: #0284c7; color: #ffffff;")
        self.btn_tab_copy.clicked.connect(self.copy_report_to_clipboard)
        report_tools.addWidget(self.btn_tab_copy)

        self.btn_tab_ticket = QPushButton("🎫 Crear Ticket Technoma")
        self.btn_tab_ticket.setStyleSheet("background-color: #b91c1c; color: #ffffff; font-weight: bold;")
        self.btn_tab_ticket.clicked.connect(self.create_technoma_ticket)
        report_tools.addWidget(self.btn_tab_ticket)

        report_tools.addStretch()
        tab_report_layout.addLayout(report_tools)

        self.txt_report_view = QTextEdit()
        self.txt_report_view.setReadOnly(True)
        self.txt_report_view.setPlaceholderText(
            "Esta noticia aún no ha sido analizada por Inteligencia Artificial.\n\n"
            "Lanza '⚡ Procesar con IA' para generar automáticamente el Reporte Formal de Detección de Vulnerabilidades:\n"
            "• 1. Resumen Ejecutivo (Fecha, Severidad, Impacto en Negocio)\n"
            "• 2. Detalles Técnicos (CVE, Vector de Ataque, Sistemas Afectados)\n"
            "• 3. Plan de Mitigación Inmediato y a Mediano Plazo\n"
            "• 4. Asunto formal listo para correo corporativo a clientes."
        )
        tab_report_layout.addWidget(self.txt_report_view)

        self.tabs_right.addTab(tab_report, "📋 2. Reporte Cliente (IA Markdown)")

        # -------------------------------------------------------------
        # PESTAÑA 3: IOCS & TELEMETRÍA TÉCNICA
        # -------------------------------------------------------------
        tab_iocs = QWidget()
        tab_iocs_layout = QVBoxLayout(tab_iocs)
        tab_iocs_layout.setContentsMargins(6, 6, 6, 6)
        tab_iocs_layout.setSpacing(6)

        self.txt_iocs_view = QTextBrowser()
        self.txt_iocs_view.setOpenExternalLinks(True)
        self.txt_iocs_view.setPlaceholderText("Indicadores de Compromiso (CVEs, IPs, Hashes, Dominios) y telemetría original del feed...")
        tab_iocs_layout.addWidget(self.txt_iocs_view)

        self.tabs_right.addTab(tab_iocs, "🔍 3. IOCs & Telemetría Técnica")

        right_layout.addWidget(self.tabs_right)
        splitter.addWidget(right_widget)

        # Proporción equilibrada: 600px tabla izquierda, 760px visor derecho
        splitter.setSizes([600, 760])
        main_layout.addWidget(splitter, 1)

        # =====================================================================
        # 4. BARRA INFERIOR DE ACCIONES RÁPIDAS (COMPACTA)
        # =====================================================================
        bottom_bar = QFrame()
        bottom_bar.setObjectName("bottomBar")
        bottom_bar.setFixedHeight(46)
        bottom_layout = QHBoxLayout(bottom_bar)
        bottom_layout.setContentsMargins(10, 6, 10, 6)
        bottom_layout.setSpacing(8)

        self.btn_process_ia = QPushButton("⚡ Procesar con IA")
        self.btn_process_ia.setStyleSheet("background-color: #7c3aed; color: #ffffff; font-weight: bold; padding: 6px 14px;")
        self.btn_process_ia.setToolTip("Genera el reporte dual para cliente usando el modelo LLM seleccionado")
        self.btn_process_ia.clicked.connect(self.process_selected_with_ai)
        bottom_layout.addWidget(self.btn_process_ia)

        self.btn_copy_report = QPushButton("📋 Copiar Reporte")
        self.btn_copy_report.setStyleSheet("background-color: #0284c7; color: #ffffff;")
        self.btn_copy_report.setToolTip("Copia el reporte en Markdown/texto plano al portapapeles para envío por correo")
        self.btn_copy_report.clicked.connect(self.copy_report_to_clipboard)
        bottom_layout.addWidget(self.btn_copy_report)

        self.btn_create_ticket = QPushButton("🎫 Crear Ticket Technoma")
        self.btn_create_ticket.setStyleSheet("background-color: #b91c1c; color: #ffffff; font-weight: bold;")
        self.btn_create_ticket.setToolTip("Traspasa la vulnerabilidad analizada al Generador de Tickets THN-SOC")
        self.btn_create_ticket.clicked.connect(self.create_technoma_ticket)
        bottom_layout.addWidget(self.btn_create_ticket)

        self.btn_open_browser = QPushButton("🌐 Abrir Noticia")
        self.btn_open_browser.clicked.connect(self.open_current_in_browser)
        bottom_layout.addWidget(self.btn_open_browser)

        self.btn_mark_ignore = QPushButton("🧹 Ignorar")
        self.btn_mark_ignore.clicked.connect(self.mark_current_ignored)
        bottom_layout.addWidget(self.btn_mark_ignore)

        bottom_layout.addStretch()

        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.close)
        bottom_layout.addWidget(btn_close)

        main_layout.addWidget(bottom_bar)

    def _clear_filters(self):
        """Restablece los filtros de búsqueda y vuelve a la primera página."""
        self.combo_filter_source.setCurrentIndex(0)
        self.combo_filter_status.setCurrentIndex(0)
        self.combo_filter_date.setCurrentIndex(0)
        self.txt_search.clear()
        self.load_items_from_db(reset_page=True)

    # =========================================================================
    # LÓGICA DE PAGINACIÓN
    # =========================================================================
    def _go_first_page(self):
        if self.current_page > 1:
            self.current_page = 1
            self.load_items_from_db(reset_page=False)

    def _go_prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.load_items_from_db(reset_page=False)

    def _go_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.load_items_from_db(reset_page=False)

    def _go_last_page(self):
        if self.current_page < self.total_pages:
            self.current_page = self.total_pages
            self.load_items_from_db(reset_page=False)

    # =========================================================================
    # LÓGICA DE CARGA Y RENDERIZADO DE DATOS (CON PAGINACIÓN Y FILTROS)
    # =========================================================================
    def load_items_from_db(self, reset_page: bool = False):
        """Consulta la base de datos con filtros de fuente, estado, fecha y paginación."""
        if reset_page:
            self.current_page = 1

        tier = self.combo_filter_tier.currentText()
        if tier == "Todos los Niveles":
            tier = "Todos"

        source = self.combo_filter_source.currentText()
        if source == "Todas las Fuentes":
            source = "Todas"

        status = self.combo_filter_status.currentText()
        search = self.txt_search.text().strip()

        # Filtro de fecha
        date_text = self.combo_filter_date.currentText()
        days: Optional[int] = None
        if "24" in date_text:
            days = 1
        elif "7" in date_text:
            days = 7
        elif "30" in date_text:
            days = 30
        elif "90" in date_text:
            days = 90

        # Conteo total para paginación
        total_count = self.db.get_items_count(feed_name=source, status=status, search=search, days=days, tier=tier)
        self.total_matching_items = total_count

        # Configurar tamaño de página
        page_size_str = self.combo_page_size.currentText()
        self.page_size = int(page_size_str) if page_size_str.isdigit() else 50
        self.total_pages = max(1, (total_count + self.page_size - 1) // self.page_size)

        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
        if self.current_page < 1:
            self.current_page = 1

        offset = (self.current_page - 1) * self.page_size

        # Desactivar temporalmente ordenamiento visual mientras se puebla la tabla
        self.table_items.setSortingEnabled(False)

        items = self.db.get_items(
            limit=self.page_size,
            offset=offset,
            feed_name=source,
            status=status,
            search=search,
            days=days,
            tier=tier,
            order_by="id DESC"
        )
        stats = self.db.get_statistics()

        self.badge_total.setText(f"Total: {stats['total']}")
        self.badge_nuevos.setText(f"Nuevos: {stats['nuevos']} ⚪")
        self.badge_analizados.setText(f"Analizados: {stats['analizados']} 🟢")
        self.badge_escalados.setText(f"Escalados: {stats['escalados']} 🎫")

        self.table_items.setRowCount(len(items))
        for row_idx, it in enumerate(items):
                        # Col 0: ID numérico
            item_id = QTableWidgetItem()
            item_id.setData(Qt.DisplayRole, it["id"])
            item_id.setTextAlignment(Qt.AlignCenter)
            self.table_items.setItem(row_idx, 0, item_id)

            # Col 1: Nivel CTI (Diferenciado por color y semántica)
            tier_val = it.get("tier") or FEED_TIER_MAPPING.get(it.get("feed_id", ""), TIER_NEWS)
            tier_item = QTableWidgetItem(tier_val)
            tier_item.setTextAlignment(Qt.AlignCenter)
            if tier_val == TIER_TACTICAL:
                tier_item.setForeground(QColor("#fb923c")) # Naranja brillante
                tier_item.setToolTip("CTI Técnico: Avisos Críticos y Exploits de CISA, SANS y 0dayfans")
            elif tier_val == TIER_RESEARCH:
                tier_item.setForeground(QColor("#c084fc")) # Púrpura DFIR
                tier_item.setToolTip("Investigación DFIR: Análisis Forense y Malware de Kaspersky, Sophos y ESET")
            else:
                tier_item.setForeground(QColor("#38bdf8")) # Azul cian noticias
                tier_item.setToolTip("Noticias y Ciberdelito: Brechas, Ransomware y Actualidad")
            self.table_items.setItem(row_idx, 1, tier_item)

            # Col 2: Fuente
            src_item = QTableWidgetItem(it["feed_name"])
            src_item.setForeground(QColor("#e2e8f0"))
            self.table_items.setItem(row_idx, 2, src_item)

            # Col 3: Severidad
            sev_text = it.get("severity") or "PENDIENTE"
            sev_item = QTableWidgetItem(sev_text)
            sev_item.setTextAlignment(Qt.AlignCenter)
            sev_color = self.SEVERITY_COLORS.get(sev_text, "#94a3b8")
            sev_item.setForeground(QColor(sev_color))
            self.table_items.setItem(row_idx, 3, sev_item)

            # Col 4: Título
            title_item = QTableWidgetItem(it["title"])
            self.table_items.setItem(row_idx, 4, title_item)

            # Col 5: Fecha
            pub_date = it.get("published_date") or ""
            date_clean = pub_date[:10] if len(pub_date) >= 10 else pub_date
            date_item = QTableWidgetItem(date_clean)
            date_item.setTextAlignment(Qt.AlignCenter)
            date_item.setForeground(QColor("#94a3b8"))
            self.table_items.setItem(row_idx, 5, date_item)

            # Col 6: Estado
            status_text = it.get("status") or "NUEVO"
            stat_item = QTableWidgetItem(status_text)
            stat_item.setTextAlignment(Qt.AlignCenter)
            stat_color = self.STATUS_COLORS.get(status_text, "#94a3b8")
            stat_item.setForeground(QColor(stat_color))
            self.table_items.setItem(row_idx, 6, stat_item)

            # Guardar referencia al dict en el item de la columna 0
            item_id.setData(Qt.UserRole, it)

        # Reactivar ordenamiento interactivo
        self.table_items.setSortingEnabled(True)

        # Actualizar indicadores de la barra de paginación
        start_idx = offset + 1 if total_count > 0 else 0
        end_idx = min(offset + self.page_size, total_count)
        self.lbl_page_info.setText(f"Página {self.current_page} de {self.total_pages}")
        self.lbl_pagination_stats.setText(f"Mostrando {start_idx}-{end_idx} de {total_count} alertas")

        self.btn_first_page.setEnabled(self.current_page > 1)
        self.btn_prev_page.setEnabled(self.current_page > 1)
        self.btn_next_page.setEnabled(self.current_page < self.total_pages)
        self.btn_last_page.setEnabled(self.current_page < self.total_pages)

        # Seleccionar la primera fila si no hay selección previa
        if len(items) > 0 and not self.current_selected_item:
            self.table_items.selectRow(0)

    def _on_table_selection_changed(self):
        """Muestra la noticia en el visor in-app y el reporte de IA si existe."""
        selected_rows = self.table_items.selectedItems()
        if not selected_rows:
            self.current_selected_item = None
            return

        row = selected_rows[0].row()
        id_item = self.table_items.item(row, 0)
        if not id_item:
            return

        item_data = id_item.data(Qt.UserRole)
        self.current_selected_item = item_data

        if not item_data:
            return

        # 1. Actualizar Tarjeta de Cabecera del Lector In-App
        self.lbl_reader_title.setText(item_data["title"])
        self.lbl_reader_source.setText(f"<b>Fuente:</b> {item_data['feed_name']}")
        pub_d = item_data.get("published_date") or "N/A"
        self.lbl_reader_date.setText(f"<b>Fecha:</b> {pub_d}")
        cat = item_data.get("category") or "CTI Threat Intel"
        tier_val = item_data.get("tier") or FEED_TIER_MAPPING.get(item_data.get("feed_id", ""), TIER_NEWS)
        tier_color = "#fb923c" if tier_val == TIER_TACTICAL else ("#c084fc" if tier_val == TIER_RESEARCH else "#38bdf8")
        self.lbl_reader_category.setText(
            f"<b>Nivel CTI:</b> <span style='color: {tier_color}; font-weight: bold;'>[{tier_val}]</span> "
            f"&nbsp;|&nbsp; <b>Especialidad:</b> {cat}"
        )
        link = item_data.get("link") or ""
        if link:
            self.lbl_reader_link.setText(f'<a style="color: #60a5fa;" href="{link}">🔗 Abrir Enlace Original</a>')
        else:
            self.lbl_reader_link.setText("")

        self.lbl_fetch_status.setText("")

        # 2. Renderizar Contenido en el Lector In-App
        full_content = item_data.get("full_content") or ""
        summary = item_data.get("summary") or ""

        # Resaltar CVEs en el resumen
        summary_highlighted = re.sub(
            r"\b(CVE-\d{4}-\d{4,7})\b",
            r'<span style="background-color: #78350f; color: #fef08a; padding: 2px 6px; border-radius: 4px; font-weight: bold; border: 1px solid #ca8a04;">\1</span>',
            summary
        )

        if full_content:
            self.btn_fetch_full_web.setText("🔄 Actualizar Noticia desde Web")
            body_html = f"""
            <div style="font-family: Segoe UI, sans-serif; line-height: 1.65; color: #e2e8f0;">
                <div style="background-color: #064e3b; color: #34d399; padding: 6px 12px; border-radius: 4px; margin-bottom: 12px; font-size: 11px; font-weight: bold; border: 1px solid #059669;">
                    ✓ Noticia completa extraída de la web del autor ({item_data['feed_name']})
                </div>
                {full_content}
            </div>
            """
            self.txt_reader_view.setHtml(body_html)
        else:
            self.btn_fetch_full_web.setText("🌐 Cargar Noticia Completa de la Web")
            body_html = f"""
            <div style="font-family: Segoe UI, sans-serif; line-height: 1.65; color: #e2e8f0;">
                <div style="background-color: #1e293b; color: #94a3b8; padding: 6px 12px; border-radius: 4px; margin-bottom: 12px; font-size: 11px; border: 1px solid #334155;">
                    ℹ️ <b>Resumen inicial del Feed RSS:</b> Pulse <i>'🌐 Cargar Noticia Completa de la Web'</i> arriba para extraer todos los párrafos y detalles técnicos del portal original.
                </div>
                <div style="font-size: 13px; color: #cbd5e1; margin-bottom: 16px;">
                    {summary_highlighted if summary_highlighted else '<i>Sin descripción disponible en el canal RSS.</i>'}
                </div>
            </div>
            """
            self.txt_reader_view.setHtml(body_html)

        # 3. Renderizar Reporte de IA (Pestaña 2)
        ai_report = item_data.get("ai_report") or ""
        if ai_report:
            self.txt_report_view.setMarkdown(ai_report)
        else:
            self.txt_report_view.clear()
            self.txt_report_view.setPlaceholderText(
                f"El artículo '{item_data['title'][:60]}...' aún no ha sido analizado por IA.\n\n"
                f"Haga clic en '⚡ Analizar esta Noticia con IA' para generar el reporte corporativo de vulnerabilidades para el cliente."
            )

        # 4. Renderizar IOCs y Telemetría Forense (Pestaña 3)
        self._render_iocs_and_telemetry(item_data)

        # Mantener en la pestaña 1 (Lectura de noticia) de forma predeterminada
        if self.tabs_right.currentIndex() != 1 or not ai_report:
            self.tabs_right.setCurrentIndex(0)

    def _render_iocs_and_telemetry(self, item_data: Dict[str, Any]):
        """Extrae automáticamente IOCs (CVEs, IPs, Hashes, URLs) del texto."""
        full_text = f"{item_data.get('title', '')} {item_data.get('summary', '')} {item_data.get('full_content', '')} {item_data.get('ai_report', '')}"

        # Regex de IOCs
        cves = sorted(list(set(re.findall(r"CVE-\d{4}-\d{4,7}", full_text, re.IGNORECASE))))
        ips = sorted(list(set(re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", full_text))))
        ips = [ip for ip in ips if not (ip.startswith("127.") or ip.startswith("0.") or ip.startswith("255."))]
        hashes = sorted(list(set(re.findall(r"\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b", full_text))))

        html_out = [
            '<div style="font-family: Segoe UI, sans-serif; color: #e2e8f0;">',
            '<h3 style="color: #38bdf8; margin-bottom: 6px;">🔍 Detección Forense de IOCs & Pivot Intelligence</h3>'
        ]

        # CVEs
        if cves:
            html_out.append('<h4 style="color: #f59e0b; margin-top: 12px; margin-bottom: 6px;">Vulnerabilidades Detectadas (CVEs):</h4>')
            html_out.append('<ul>')
            for cve in cves:
                cve_upper = cve.upper()
                nvd_url = f"https://nvd.nist.gov/vuln/detail/{cve_upper}"
                cve_mitre = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve_upper}"
                html_out.append(
                    f'<li><b>{cve_upper}</b> &nbsp;|&nbsp; '
                    f'<a style="color: #38bdf8;" href="{nvd_url}">NVD NIST</a> &nbsp;|&nbsp; '
                    f'<a style="color: #60a5fa;" href="{cve_mitre}">MITRE CVE</a></li>'
                )
            html_out.append('</ul>')
        else:
            html_out.append('<p style="color: #94a3b8; font-size: 11px;"><i>No se detectaron identificadores CVE explícitos en el texto preliminar.</i></p>')

        # IPs
        if ips:
            html_out.append('<h4 style="color: #ef4444; margin-top: 12px; margin-bottom: 6px;">Direcciones IP Detectadas:</h4>')
            html_out.append('<ul>')
            for ip in ips:
                vt_url = f"https://www.virustotal.com/gui/ip-address/{ip}"
                abuse_url = f"https://www.abuseipdb.com/check/{ip}"
                html_out.append(
                    f'<li><code>{ip}</code> &nbsp;|&nbsp; '
                    f'<a style="color: #38bdf8;" href="{vt_url}">VirusTotal</a> &nbsp;|&nbsp; '
                    f'<a style="color: #f87171;" href="{abuse_url}">AbuseIPDB</a></li>'
                )
            html_out.append('</ul>')

        # Hashes
        if hashes:
            html_out.append('<h4 style="color: #a855f7; margin-top: 12px; margin-bottom: 6px;">Hashes de Archivo / Malware:</h4>')
            html_out.append('<ul>')
            for h in hashes:
                vt_url = f"https://www.virustotal.com/gui/file/{h}"
                html_out.append(f'<li><code>{h}</code> &nbsp;|&nbsp; <a style="color: #c084fc;" href="{vt_url}">VirusTotal</a></li>')
            html_out.append('</ul>')

        # Telemetría de Base de Datos
        html_out.append('<hr style="border: 1px solid #1e293b; margin: 16px 0;" />')
        html_out.append('<h4 style="color: #94a3b8; margin-bottom: 6px;">Telemetría Cruda del Feed:</h4>')
        html_out.append(f'<p style="font-size: 11px; color: #cbd5e1;"><b>ID Interno SQLite:</b> {item_data["id"]}<br/>')
        html_out.append(f'<b>SHA-256 Deduplicación:</b> <code>{item_data["content_hash"]}</code><br/>')
        html_out.append(f'<b>Hora de Ingesta:</b> {item_data.get("ingested_at", "N/A")}<br/>')
        html_out.append(f'<b>URL Original:</b> <a style="color: #38bdf8;" href="{item_data["link"]}">{item_data["link"]}</a></p>')

        html_out.append('</div>')
        self.txt_iocs_view.setHtml("".join(html_out))

    # =========================================================================
    # EXTRACCIÓN WEB ASÍNCRONA DE ARTÍCULOS COMPLETOS
    # =========================================================================
    def fetch_full_article_from_web(self):
        """Descarga el artículo completo directamente de la web."""
        if not self.current_selected_item:
            QMessageBox.information(self, "Seleccionar Artículo", "Por favor seleccione un artículo primero.")
            return

        item = self.current_selected_item
        url = item.get("link")
        if not url or not url.startswith("http"):
            QMessageBox.warning(self, "URL Inválida", "El artículo no contiene un enlace web válido.")
            return

        self.btn_fetch_full_web.setEnabled(False)
        self.lbl_fetch_status.setText("📥 Extrayendo noticia completa desde la web...")
        self.progress_bar.setRange(0, 0)
        self.progress_bar.show()

        self.web_worker = WebReaderWorker(item["id"], url)
        self.web_worker.article_fetched.connect(self._on_article_fetched)
        self.web_worker.fetch_failed.connect(self._on_fetch_failed)
        self.web_worker.start()

    @Slot(int, str, str)
    def _on_article_fetched(self, item_id: int, full_html: str, plain_text: str):
        self.progress_bar.hide()
        self.btn_fetch_full_web.setEnabled(True)
        self.lbl_fetch_status.setText("✅ Noticia completa cargada")

        self.db.update_full_content(item_id, full_html)

        if self.current_selected_item and self.current_selected_item["id"] == item_id:
            self.current_selected_item["full_content"] = full_html

            body_html = f"""
            <div style="font-family: Segoe UI, sans-serif; line-height: 1.65; color: #e2e8f0;">
                <div style="background-color: #064e3b; color: #34d399; padding: 6px 12px; border-radius: 4px; margin-bottom: 12px; font-size: 11px; font-weight: bold; border: 1px solid #059669;">
                    ✓ Noticia completa extraída de la web del autor ({self.current_selected_item['feed_name']})
                </div>
                {full_html}
            </div>
            """
            self.txt_reader_view.setHtml(body_html)
            self._render_iocs_and_telemetry(self.current_selected_item)

    @Slot(int, str)
    def _on_fetch_failed(self, item_id: int, error_msg: str):
        self.progress_bar.hide()
        self.btn_fetch_full_web.setEnabled(True)
        self.lbl_fetch_status.setText("⚠️ Falló extracción web")
        QMessageBox.warning(
            self, "Aviso de Extracción Web",
            f"No se pudo extraer la noticia completa automáticamente:\n{error_msg}\n\n"
            "Puede leer el resumen del feed o abrir el artículo en su navegador con el botón '🌐 Abrir Noticia'."
        )

    def copy_article_content_to_clipboard(self):
        """Copia el texto del artículo al portapapeles."""
        text = self.txt_reader_view.toPlainText().strip()
        if not text:
            QMessageBox.information(self, "Sin Contenido", "No hay texto para copiar.")
            return

        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Copiado", "✅ Texto del artículo copiado al portapapeles.")

    # =========================================================================
    # SINCRONIZACIÓN ASÍNCRONA DE FEEDS CON QThreadPool
    # =========================================================================
    def show_osint_channels_dialog(self):
        """Muestra ventana modal con accesos directos a analistas y canales OSINT sin RSS."""
        dlg = QDialog(self)
        dlg.setWindowTitle("Vigilancia CTI & Canales OSINT / Dark Web")
        dlg.resize(720, 480)
        dlg.setStyleSheet("background-color: #0f172a; color: #e2e8f0; font-family: 'Segoe UI', sans-serif;")
        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        header = QLabel("Canales Estratégicos de Vigilancia, Dark Web y Referentes Locales")
        header.setStyleSheet("font-size: 14px; font-weight: bold; color: #38bdf8;")
        layout.addWidget(header)

        desc = QLabel(
            "Fuentes críticas de inteligencia en redes sociales, analistas independientes y plataformas de IoCs "
            "que no ofrecen sindicación RSS estándar pero forman parte del monitoreo permanente del SOC."
        )
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #94a3b8; font-size: 11px;")
        layout.addWidget(desc)

        channels = [
            ("Miguel Ángel Gaspar (Paraguay Ciberseguro)", "https://x.com/miguelgaspar", "Referente local clave en Paraguay. Alertas de fraude, incidentes locales y campañas bancarias."),
            ("Nicolas Krassas (@Dinosn)", "https://x.com/Dinosn", "Head de Threat & Vuln Mgmt. Avisos diarios de 0-days, exploits activos y parches."),
            ("VCERTAnalyzer", "https://x.com/vcertanalyzer", "Ciberinteligencia en LATAM, alertas de brechas estatales y fugas gubernamentales."),
            ("Daily Dark Web (Monitor)", "https://dailydarkweb.net", "Rastreador en vivo de víctimas de Ransomware y data leaks."),
            ("Dark Web Informer", "https://darkwebinformer.com", "Inteligencia de Dark Web, foros clandestinos y mercados de accesos iniciales."),
            ("Abuse.ch - ThreatFox / URLhaus", "https://threatfox.abuse.ch/browse/", "Plataforma comunitaria de IoCs de malware y botnets en tiempo real."),
            ("AbuseIPDB (Consola de Búsqueda)", "https://www.abuseipdb.com/", "Búsqueda comunitaria de reputación de direcciones IP maliciosas.")
        ]

        table = QTableWidget(len(channels), 3)
        table.setHorizontalHeaderLabels(["Canal / Fuente", "Descripción", "Acción"])
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        table.verticalHeader().setVisible(False)
        table.setStyleSheet("background-color: #1e293b; border: 1px solid #334155; font-size: 11px;")

        for row, (name, url, info) in enumerate(channels):
            item_name = QTableWidgetItem(name)
            item_name.setForeground(QColor("#f8fafc"))
            item_name.setFont(QFont("Segoe UI", 9, QFont.Bold))
            table.setItem(row, 0, item_name)

            item_desc = QTableWidgetItem(info)
            item_desc.setForeground(QColor("#94a3b8"))
            table.setItem(row, 1, item_desc)

            btn_open = QPushButton("Abrir Enlace")
            btn_open.setStyleSheet("background-color: #0284c7; color: #ffffff; padding: 3px 8px; border-radius: 3px; font-weight: bold;")
            btn_open.clicked.connect(lambda checked=False, target_url=url: QDesktopServices.openUrl(QUrl(target_url)))
            table.setCellWidget(row, 2, btn_open)

        layout.addWidget(table)

        btn_close = QPushButton("Cerrar")
        btn_close.setFixedHeight(30)
        btn_close.setStyleSheet("background-color: #475569; color: #ffffff; font-weight: bold; border-radius: 4px;")
        btn_close.clicked.connect(dlg.accept)
        layout.addWidget(btn_close)

        dlg.exec()

    def sync_all_feeds(self):
        """Lanza tareas concurrentes de descarga para los 15 feeds en segundo plano."""
        self.btn_sync.setEnabled(False)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.show()

        self.active_sync_tasks = len(FEEDS_CONFIG)
        self.new_items_accumulated = 0

        for feed in FEEDS_CONFIG:
            task = RSSFetchTask(feed, self.db)
            if task:
                task.signals.feed_completed.connect(self._on_feed_completed)
                task.signals.feed_error.connect(self._on_feed_error)
                self.thread_pool.start(task)

    @Slot(str, int, int)
    def _on_feed_completed(self, feed_name: str, new_items: int, total_fetched: int):
        self.new_items_accumulated += new_items
        self.active_sync_tasks -= 1
        self._check_sync_finish()

    @Slot(str, str)
    def _on_feed_error(self, feed_name: str, error_msg: str):
        self.active_sync_tasks -= 1
        self._check_sync_finish()

    def _check_sync_finish(self):
        if self.active_sync_tasks <= 0:
            self.progress_bar.hide()
            self.btn_sync.setEnabled(True)
            self.load_items_from_db(reset_page=True)

    # =========================================================================
    # ANÁLISIS COGNITIVO CON IA (QThread)
    # =========================================================================
    def process_selected_with_ai(self):
        """Dispara el análisis de IA para el artículo actualmente seleccionado."""
        if not self.current_selected_item:
            QMessageBox.information(self, "Seleccionar Artículo", "Por favor seleccione un artículo de la tabla.")
            return

        item = self.current_selected_item
        provider_text = self.combo_ai_provider.currentText()
        if "NVIDIA" in provider_text or "DeepSeek" in provider_text:
            provider_choice = "nvidia"
        elif "OpenAI" in provider_text:
            provider_choice = "openai"
        else:
            provider_choice = "gemini"

        self.btn_process_ia.setEnabled(False)
        self.btn_tab_reanalyze.setEnabled(False)
        self.btn_reader_ai_analyze.setEnabled(False)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.show()

        self.tabs_right.setCurrentIndex(1)
        self.txt_report_view.setMarkdown(f"⏳ La IA ({provider_choice.upper()}) está estructurando el Reporte Formal de Vulnerabilidad...")

        summary_to_send = item.get("full_content") or item.get("summary") or item["title"]

        self.ai_worker = FeedsAIWorker(
            item_id=item["id"],
            feed_title=item["title"],
            feed_source=item["feed_name"],
            feed_url=item["link"],
            feed_summary=summary_to_send,
            provider=provider_choice
        )
        self.ai_worker.report_ready.connect(self._on_ai_report_ready)
        self.ai_worker.error_occurred.connect(self._on_ai_error)
        self.ai_worker.start()

    @Slot(int, str, dict)
    def _on_ai_report_ready(self, item_id: int, report_markdown: str, metadata: dict):
        self.progress_bar.hide()
        self.btn_process_ia.setEnabled(True)
        self.btn_tab_reanalyze.setEnabled(True)
        self.btn_reader_ai_analyze.setEnabled(True)

        severity = metadata.get("severity") or "Alta 🔴"
        self.db.update_ai_report(item_id, report_markdown, severity, status="ANALIZADO")

        self.txt_report_view.setMarkdown(report_markdown)
        self.tabs_right.setCurrentIndex(1)
        self.load_items_from_db(reset_page=False)

    @Slot(int, str)
    def _on_ai_error(self, item_id: int, error_msg: str):
        self.progress_bar.hide()
        self.btn_process_ia.setEnabled(True)
        self.btn_tab_reanalyze.setEnabled(True)
        self.btn_reader_ai_analyze.setEnabled(True)
        self.txt_report_view.setText(f"❌ Error al consultar el modelo de IA:\n{error_msg}")
        QMessageBox.warning(self, "Error de IA", f"No se pudo estructurar el reporte con IA:\n{error_msg}")

    # =========================================================================
    # ACCIONES: COPIAR, TICKET TECHNOMA, NAVEGADOR
    # =========================================================================
    def copy_report_to_clipboard(self):
        """Copia el texto del reporte al portapapeles para envío rápido a clientes."""
        text = self.txt_report_view.toPlainText().strip()
        if not text:
            QMessageBox.information(self, "Reporte Vacío", "No hay ningún reporte generado para copiar.")
            return

        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Copiado", "✅ Reporte de vulnerabilidad copiado al portapapeles listo para enviar.")

    def create_technoma_ticket(self):
        """Abre el Generador de Tickets Technoma (THN-SOC) prellenado con la alerta."""
        if not self.current_selected_item:
            QMessageBox.information(self, "Seleccionar Alerta", "Seleccione una alerta para escalar.")
            return

        item = self.current_selected_item
        report_text = item.get("ai_report") or ""
        meta = FeedsAIOrchestrator.parse_metadata_from_report(report_text) if report_text else {}

        prio = meta.get("severity") or item.get("severity") or "Alta 🔴"
        cve = meta.get("cve") or "N/A"
        tech = meta.get("affected_technology") or "Software Afectado"

        ticket_data = {
            "ticket_id": f"THN-SOC-VULN-{item['id']}",
            "prioridad": prio,
            "tenant": "General / Institucional",
            "asunto": f"VULNERABILIDAD - {cve if cve != 'N/A' else tech}: {item['title'][:60]}",
            "descripcion": (
                f"Alerta de seguridad detectada vía CTI Feed ({item['feed_name']}).\n\n"
                f"Resumen de la amenaza:\n{item.get('summary', '')[:400]}"
            ),
            "activos": f"Tecnología afectada: {tech}\nFuente: {item['feed_name']}\nEnlace oficial: {item['link']}",
            "evidencia": report_text if report_text else item.get("summary", ""),
            "solicitud_accion": meta.get("mitigation_immediate") or "Evaluar presencia en el perímetro y aplicar mitigación."
        }

        try:
            from thn_ticket_generator import TechnomaTicketGeneratorDialog
            ticket_dlg = TechnomaTicketGeneratorDialog(self, initial_data=ticket_data)
            self.db.update_ticket(item["id"], ticket_data["ticket_id"], status="ESCALADO")
            self.load_items_from_db(reset_page=False)
            ticket_dlg.exec()
        except Exception as e:
            QMessageBox.critical(self, "Error al Abrir Ticket", f"No se pudo instanciar el Generador Technoma:\n{e}")

    def open_current_in_browser(self):
        """Abre el enlace original del feed en el navegador web predeterminado."""
        if self.current_selected_item and self.current_selected_item.get("link"):
            QDesktopServices.openUrl(QUrl(self.current_selected_item["link"]))
        else:
            QMessageBox.information(self, "Sin Enlace", "El elemento seleccionado no tiene un enlace web válido.")

    def mark_current_ignored(self):
        """Marca el artículo seleccionado como IGNORADO."""
        if not self.current_selected_item:
            return
        item_id = self.current_selected_item["id"]
        self.db.mark_status(item_id, "IGNORADO")
        self.load_items_from_db(reset_page=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = FeedsIntelDialog()
    dlg.show()
    sys.exit(app.exec())
