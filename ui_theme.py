# =============================================================================
# TECHNOMA SOC — DESIGN SYSTEM & UI THEME (ui_theme.py)
# Paleta de grado enterprise (Slate / Cyber Blue), tipografía Outfit y QSS unificado
# =============================================================================

import os
from PySide6.QtGui import QFontDatabase, QFont

# -----------------------------------------------------------------------------
# 1. TOKENS DE COLOR (DESIGN TOKENS - SLATE DARK CYBER SUITE)
# -----------------------------------------------------------------------------
BG_BASE        = "#0a0e17"   # Fondo base general (Slate Dark neutro, no negro puro)
BG_SURFACE     = "#111827"   # Superficie de contenedores, tarjetas y paneles
BG_ELEVATED    = "#1e293b"   # Elementos elevados, hover y cabeceras
BG_INPUT       = "#0b1120"   # Cajas de texto, visores de consola y búsqueda

BORDER_SUBTLE  = "#1f293d"   # Bordes base de bajo contraste
BORDER_MUTED   = "#334155"   # Bordes de inputs y botones secundarios
BORDER_FOCUS   = "#38bdf8"   # Borde de foco reactivo
BORDER_ACCENT  = "#0284c7"   # Borde de acento activo

ACCENT_PRIMARY = "#0284c7"   # Azul cobalto principal
ACCENT_CYBER   = "#38bdf8"   # Azul cian tecnológico
ACCENT_HOVER   = "#0369a1"   # Hover de botones de acción
ACCENT_GLOW    = "rgba(56, 189, 248, 0.15)"

# Alertas Semánticas
COLOR_CRITICAL = "#f43f5e"   # P1 / Crítico / Alerta Roja
COLOR_HIGH     = "#f97316"   # P2 / Alta / Naranja
COLOR_MEDIUM   = "#eab308"   # P3 / Media / Amarillo
COLOR_LOW      = "#38bdf8"   # P4 / Baja / Azul Cielo
COLOR_SUCCESS  = "#10b981"   # Resuelto / Online / Verde Esmeralda
COLOR_PURPLE   = "#a855f7"   # IA / Notificaciones Móviles / Morado
COLOR_INDIGO   = "#6366f1"   # Forense / Terminal / Índigo

# Jerarquía Tipográfica
TEXT_PRIMARY   = "#f8fafc"   # Texto principal de alta legibilidad
TEXT_SECONDARY = "#cbd5e1"   # Texto de lectura estándar
TEXT_MUTED     = "#94a3b8"   # Etiquetas secundarias y placeholders
TEXT_FAINT     = "#64748b"   # Texto deshabilitado o de relleno

FONT_MAIN = "'Outfit', 'Segoe UI', -apple-system, sans-serif"
FONT_MONO = "'Consolas', 'Cascadia Code', 'JetBrains Mono', monospace"

# -----------------------------------------------------------------------------
# 2. INICIALIZADOR DE FUENTES CORPORATIVAS
# -----------------------------------------------------------------------------
def init_soc_fonts(base_dir: str = None) -> bool:
    """Registra dinámicamente las fuentes Outfit en QFontDatabase sin requerir instalación administrativa en Windows."""
    if not base_dir:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    font_files = [
        "Outfit-Regular.ttf",
        "Outfit-Medium.ttf",
        "Outfit-SemiBold.ttf",
        "Outfit-Bold.ttf"
    ]
    
    loaded = 0
    for f in font_files:
        full_path = os.path.join(base_dir, f)
        if os.path.exists(full_path):
            fid = QFontDatabase.addApplicationFont(full_path)
            if fid != -1:
                loaded += 1
    return loaded > 0

# -----------------------------------------------------------------------------
# 3. HOJA DE ESTILOS MAESTRA (MASTER QSS)
# -----------------------------------------------------------------------------
MASTER_QSS = f"""
QMainWindow {{
    background-color: {BG_BASE};
}}

QWidget {{
    background-color: {BG_BASE};
    color: {TEXT_PRIMARY};
    font-family: {FONT_MAIN};
    font-size: 12px;
}}

/* PANELES Y CONTENEDORES */
QFrame {{
    background-color: {BG_SURFACE};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 6px;
}}

QFrame#topHeaderFrame {{
    background-color: #0d1322;
    border-bottom: 1px solid {BORDER_MUTED};
    border-top: none;
    border-left: none;
    border-right: none;
    border-radius: 0px;
}}

/* PESTAÑAS (QTabWidget & QTabBar) */
QTabWidget::pane {{
    border: 1px solid {BORDER_SUBTLE};
    background-color: {BG_BASE};
    top: -1px;
}}

QTabBar::tab {{
    background-color: {BG_SURFACE};
    color: {TEXT_MUTED};
    border: 1px solid {BORDER_SUBTLE};
    border-bottom: 2px solid {BG_SURFACE};
    padding: 8px 18px;
    font-family: {FONT_MAIN};
    font-size: 12px;
    font-weight: 600;
    margin-right: 4px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}}

QTabBar::tab:hover {{
    background-color: {BG_ELEVATED};
    color: {ACCENT_CYBER};
    border-color: {BORDER_MUTED};
}}

QTabBar::tab:selected {{
    background-color: {BG_ELEVATED};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-bottom: 3px solid {ACCENT_CYBER};
    font-weight: bold;
}}

/* BOTONES GLOBALES */
QPushButton {{
    background-color: {BG_ELEVATED};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 5px;
    padding: 6px 12px;
    font-family: {FONT_MAIN};
    font-size: 12px;
    font-weight: 600;
}}

QPushButton:hover {{
    background-color: #273549;
    border-color: {ACCENT_CYBER};
    color: {ACCENT_CYBER};
}}

QPushButton:pressed {{
    background-color: #1a2333;
}}

QPushButton:disabled {{
    background-color: #0e1524;
    color: {TEXT_FAINT};
    border-color: #172033;
}}

/* INPUTS Y TEXT EDITORS */
QLineEdit {{
    background-color: {BG_INPUT};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 5px;
    padding: 5px 8px;
    font-family: {FONT_MAIN};
    font-size: 12px;
}}

QLineEdit:focus {{
    border: 1px solid {BORDER_FOCUS};
    background-color: #0e162a;
}}

QTextEdit, QTextBrowser {{
    background-color: {BG_INPUT};
    color: {TEXT_SECONDARY};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 5px;
    font-family: {FONT_MONO};
    font-size: 12px;
    line-height: 1.4;
    padding: 6px;
}}

QTextEdit:focus, QTextBrowser:focus {{
    border: 1px solid {BORDER_MUTED};
}}

/* MENÚS DESPLEGABLES (QComboBox) */
QComboBox {{
    background-color: {BG_INPUT};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 5px;
    padding: 4px 10px;
    font-family: {FONT_MAIN};
    font-size: 12px;
    font-weight: 500;
}}

QComboBox:hover {{
    border-color: {ACCENT_CYBER};
}}

QComboBox:focus {{
    border: 1px solid {BORDER_FOCUS};
}}

QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 22px;
    border-left: 1px solid {BORDER_SUBTLE};
    background-color: {BG_ELEVATED};
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
}}

QComboBox QAbstractItemView {{
    background-color: {BG_SURFACE};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 6px;
    selection-background-color: #1e3a5f;
    selection-color: {ACCENT_CYBER};
    outline: none;
    font-family: {FONT_MAIN};
    font-size: 12px;
    padding: 4px;
}}

QComboBox QAbstractItemView::item {{
    padding: 6px 10px;
    min-height: 22px;
    border-radius: 4px;
}}

QComboBox QAbstractItemView::item:hover {{
    background-color: {BG_ELEVATED};
    color: {ACCENT_CYBER};
}}

/* CHECKBOX */
QCheckBox {{
    color: {TEXT_SECONDARY};
    font-family: {FONT_MAIN};
    font-size: 12px;
    spacing: 6px;
}}

QCheckBox::indicator {{
    width: 15px;
    height: 15px;
    border: 1px solid {BORDER_MUTED};
    border-radius: 3px;
    background-color: {BG_INPUT};
}}

QCheckBox::indicator:hover {{
    border-color: {ACCENT_CYBER};
}}

QCheckBox::indicator:checked {{
    background-color: {ACCENT_PRIMARY};
    border-color: {ACCENT_CYBER};
}}

/* MENÚS FLOTANTES (QMenu) */
QMenu {{
    background-color: #0e1526;
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 6px;
    padding: 5px 3px;
    font-family: {FONT_MAIN};
    font-size: 12px;
}}

QMenu::item {{
    background-color: transparent;
    color: {TEXT_PRIMARY};
    padding: 6px 26px 6px 14px;
    border-radius: 4px;
    margin: 1px 3px;
}}

QMenu::item:selected {{
    background-color: {BG_ELEVATED};
    color: {ACCENT_CYBER};
}}

QMenu::item:checked {{
    color: {ACCENT_CYBER};
    font-weight: bold;
}}

QMenu::item:disabled {{
    color: {TEXT_FAINT};
}}

QMenu::separator {{
    height: 1px;
    background-color: {BORDER_SUBTLE};
    margin: 4px 6px;
}}

/* BARRAS DE DESPLAZAMIENTO (QScrollBar) */
QScrollBar:vertical {{
    background: {BG_BASE};
    width: 8px;
    margin: 0px;
}}

QScrollBar::handle:vertical {{
    background: {BORDER_MUTED};
    min-height: 20px;
    border-radius: 4px;
}}

QScrollBar::handle:vertical:hover {{
    background: #475569;
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background: {BG_BASE};
    height: 8px;
    margin: 0px;
}}

QScrollBar::handle:horizontal {{
    background: {BORDER_MUTED};
    min-width: 20px;
    border-radius: 4px;
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0px;
}}

/* BOTÓN DE MENÚ (QToolButton) */
QToolButton {{
    background-color: {BG_ELEVATED};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_MUTED};
    border-radius: 5px;
    padding: 5px 12px;
    font-family: {FONT_MAIN};
    font-size: 12px;
    font-weight: 600;
}}

QToolButton:hover {{
    background-color: #273549;
    border-color: {ACCENT_CYBER};
    color: {ACCENT_CYBER};
}}

QToolButton::menu-indicator {{
    subcontrol-origin: padding;
    subcontrol-position: center right;
    padding-right: 4px;
}}

/* TABLAS (QTableWidget) */
QTableWidget {{
    background-color: {BG_INPUT};
    border: 1px solid {BORDER_SUBTLE};
    gridline-color: {BORDER_SUBTLE};
    font-family: {FONT_MONO};
    font-size: 11px;
}}

QHeaderView::section {{
    background-color: {BG_SURFACE};
    color: {TEXT_MUTED};
    padding: 5px;
    border: 1px solid {BORDER_SUBTLE};
    font-family: {FONT_MAIN};
    font-weight: bold;
    font-size: 11px;
}}
"""

# -----------------------------------------------------------------------------
# 4. GENERADORES DE ESTILOS REUTILIZABLES PARA COMPONENTES
# -----------------------------------------------------------------------------
def kpi_card_style(accent_color: str) -> str:
    """Retorna el estilo para una tarjeta KPI moderna con borde de acento sutil."""
    return f"""
        QFrame {{
            background-color: #0f1523;
            border: 1px solid {BORDER_SUBTLE};
            border-left: 3px solid {accent_color};
            border-radius: 6px;
        }}
        QFrame:hover {{
            background-color: #141c2e;
            border-color: {BORDER_MUTED};
            border-left: 3px solid {accent_color};
        }}
    """

def chip_button_style(accent_color: str = ACCENT_CYBER) -> str:
    """Estilo para los botones de acceso rápido de la Suite en la barra superior."""
    return f"""
        QPushButton {{
            background-color: #131c2e;
            color: {TEXT_PRIMARY};
            border: 1px solid {BORDER_MUTED};
            border-radius: 5px;
            padding: 5px 12px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: 600;
        }}
        QPushButton:hover {{
            background-color: #1e2b45;
            border-color: {accent_color};
            color: {accent_color};
        }}
        QPushButton:pressed {{
            background-color: #0f1726;
        }}
    """

def primary_action_btn_style(bg: str = "#0284c7", border: str = "#0369a1", hover_bg: str = "#0369a1", text_color: str = "#ffffff") -> str:
    """Botón de acción principal destacada (ej. Tomar Caso, Resolver Caso, Cazar IOC)."""
    return f"""
        QPushButton {{
            background-color: {bg};
            color: {text_color};
            border: 1px solid {border};
            border-radius: 5px;
            padding: 5px 14px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {hover_bg};
            border-color: {ACCENT_CYBER};
        }}
        QPushButton:pressed {{
            background-color: #075985;
        }}
        QPushButton:disabled {{
            background-color: #1e293b;
            color: #64748b;
            border-color: #334155;
        }}
    """

def danger_btn_style() -> str:
    """Botón de acción de parada o cancelación (ej. Detener Proceso, Cancelar)."""
    return f"""
        QPushButton {{
            background-color: #1e293b;
            color: {COLOR_CRITICAL};
            border: 1px solid #4c1d24;
            border-radius: 5px;
            padding: 5px 12px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: 600;
        }}
        QPushButton:hover {{
            background-color: #3b1219;
            border-color: {COLOR_CRITICAL};
            color: #ffffff;
        }}
        QPushButton:pressed {{
            background-color: #240a10;
        }}
        QPushButton:disabled {{
            background-color: #0e1524;
            color: {TEXT_FAINT};
            border-color: #1e293b;
        }}
    """

def ai_action_btn_style() -> str:
    """Botón unificado para el Copiloto IA con menú de modos."""
    return f"""
        QToolButton {{
            background-color: #065f46;
            color: #ecfdf5;
            border: 1px solid #059669;
            border-radius: 5px;
            padding: 6px 14px;
            font-family: {FONT_MAIN};
            font-size: 12px;
            font-weight: bold;
        }}
        QToolButton:hover {{
            background-color: #047857;
            border-color: #34d399;
            color: #ffffff;
        }}
        QToolButton:pressed {{
            background-color: #064e3b;
        }}
    """

def reassign_btn_style() -> str:
    """Botón con menú desplegable para reasignar casos a miembros del equipo SOC."""
    return f"""
        QToolButton {{
            background-color: #1e293b;
            color: #38bdf8;
            border: 1px solid #0284c7;
            border-radius: 5px;
            padding: 6px 12px;
            font-family: {FONT_MAIN};
            font-size: 12px;
            font-weight: 600;
        }}
        QToolButton:hover {{
            background-color: #0c4a6e;
            border-color: #38bdf8;
            color: #ffffff;
        }}
        QToolButton:pressed {{
            background-color: #075985;
        }}
        QToolButton::menu-indicator {{
            subcontrol-origin: padding;
            subcontrol-position: center right;
            padding-right: 4px;
        }}
    """

def section_header_style(color: str = ACCENT_CYBER) -> str:
    """Estilo para títulos de paneles y secciones forenses."""
    return f"""
        color: {color};
        font-family: {FONT_MAIN};
        font-size: 12px;
        font-weight: bold;
        border: none;
        letter-spacing: 0.3px;
    """

def preset_button_style(accent_hover: str = ACCENT_CYBER) -> str:
    """Estilo unificado para botones de presets y herramientas forenses (Slate oscuro elegante)."""
    return f"""
        QPushButton {{
            background-color: #111827;
            color: {TEXT_PRIMARY};
            border: 1px solid {BORDER_MUTED};
            border-radius: 4px;
            padding: 3px 8px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: 600;
        }}
        QPushButton:hover {{
            background-color: #1e293b;
            border-color: {accent_hover};
            color: {accent_hover};
        }}
        QPushButton:pressed {{
            background-color: #0b1120;
        }}
        QPushButton:disabled {{
            background-color: #0e1524;
            color: {TEXT_FAINT};
            border-color: #172033;
        }}
    """

def secondary_tool_btn_style() -> str:
    """Botón secundario neutro para barras de herramientas (Consola, utilidades)."""
    return f"""
        QPushButton {{
            background-color: #1e293b;
            color: {TEXT_SECONDARY};
            border: 1px solid {BORDER_MUTED};
            border-radius: 4px;
            padding: 4px 10px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: 600;
        }}
        QPushButton:hover {{
            background-color: #273549;
            border-color: {ACCENT_CYBER};
            color: {TEXT_PRIMARY};
        }}
        QPushButton:pressed {{
            background-color: #131c2e;
        }}
        QPushButton:disabled {{
            background-color: #0e1524;
            color: {TEXT_FAINT};
            border-color: #172033;
        }}
    """

def dropdown_style() -> str:
    """Estilo corporativo unificado para selectores QComboBox."""
    return f"""
        QComboBox {{
            background-color: {BG_INPUT};
            color: {TEXT_PRIMARY};
            border: 1px solid {BORDER_MUTED};
            border-radius: 4px;
            padding: 4px 10px;
            font-family: {FONT_MAIN};
            font-size: 11px;
            font-weight: 500;
        }}
        QComboBox:hover {{
            border-color: {ACCENT_CYBER};
        }}
        QComboBox:focus {{
            border-color: {ACCENT_CYBER};
        }}
        QComboBox::drop-down {{
            border: none;
            width: 20px;
        }}
        QComboBox QAbstractItemView {{
            background-color: {BG_ELEVATED};
            color: {TEXT_PRIMARY};
            selection-background-color: {ACCENT_PRIMARY};
            selection-color: #ffffff;
            border: 1px solid {BORDER_MUTED};
        }}
    """
