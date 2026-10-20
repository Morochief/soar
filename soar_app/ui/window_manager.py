# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC — GESTOR UNIFICADO DE VENTANAS Y MÓDULOS (SOCWindowManager)
=============================================================================
Resuelve de raíz las inconsistencias de apertura, bloqueo modal (.exec()),
minimizado defectuoso de QDialog(parent=self) en Windows y falta de
estandarización visual entre módulos satélites del Command Center.

Características:
  1. Cero Bloqueo Modal: Ningún módulo bloquea la ventana principal.
  2. Minimizado Nativo Windows 10/11: Las ventanas flotantes usan parent=None
     con banderas nativas Qt.Window | WindowMinMaxButtonsHint | WindowSystemMenuHint,
     apareciendo en la barra de tareas de Windows y Alt+Tab sin deformarse.
  3. Modo Dual Instantáneo (📌 Acoplar en Pestaña <-> ↗ Desacoplar a Ventana):
     Cualquier módulo satélite puede acoplarse como pestaña dentro del Cockpit
     o desacoplarse a un segundo monitor en 1 clic sin perder su estado en RAM.
  4. Taskbar Interna del SOC: Barra inferior en el Cockpit que muestra el estado
     en vivo de cada módulo (Abierto, Minimizado, Acoplado) para restaurarlo en 1 clic.
  5. Persistencia de Geometría (QSettings): Recuerda posición y tamaño por módulo.
"""

from typing import Dict, Callable, Optional, Any
from PySide6.QtCore import Qt, QEvent, QSettings, Signal, QObject, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QApplication, QTabWidget, QDialog
)
import ui_theme


class SOCManagedWindow(QWidget):
    """
    Contenedor estandarizado de nivel superior (parent=None) para cualquier módulo del SOC.
    Envuelve tanto QDialog como QWidget existentes y les añade la barra de control
    universal (Acoplar/Desacoplar, Minimizar, Maximizar/Restaurar, Cerrar) y
    comportamiento nativo de ventana del sistema operativo Windows.
    """
    state_changed = Signal(str)  # Emite module_key cuando cambia estado (minimizado, activo, cerrado)
    dock_requested = Signal(str)
    undock_requested = Signal(str)

    def __init__(
        self,
        module_key: str,
        title: str,
        short_title: str,
        accent_color: str,
        content_widget: QWidget,
        default_size: tuple = (1280, 820)
    ):
        # IMPORTANTE: parent=None garantiza que Windows trate la ventana como Top-Level
        # independiente (con ícono propio en Taskbar, Alt+Tab y minimizado nativo real).
        super().__init__(None)
        self.module_key = module_key
        self.full_title = title
        self.short_title = short_title
        self.accent_color = accent_color
        self.content_widget = content_widget
        self.is_docked_in_tab = False
        self._default_size = default_size

        self.setWindowTitle(title)
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.WindowSystemMenuHint
            | Qt.WindowType.WindowMinimizeButtonHint
            | Qt.WindowType.WindowMaximizeButtonHint
            | Qt.WindowType.WindowCloseButtonHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)

        # Convertir el QDialog/QWidget interno en un widget embebido limpio
        self.content_widget.setParent(self)
        self.content_widget.setWindowFlags(Qt.WindowType.Widget)
        self.content_widget.show()

        # Si era un QDialog que llama a accept()/reject(), interceptar para ocultar la ventana contenedora
        if isinstance(self.content_widget, QDialog):
            self.content_widget.finished.connect(self._on_inner_dialog_finished)

        self.setStyleSheet(ui_theme.MASTER_QSS)
        self._build_wrapper_ui()
        self._restore_or_adapt_geometry()

    def _build_wrapper_ui(self):
        self.root_layout = QVBoxLayout(self)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)

        # Barra Superior Estandarizada de Control de Ventana / Módulo SOC
        self.control_bar = QFrame()
        self.control_bar.setObjectName("socModuleControlBar")
        self.control_bar.setStyleSheet(f"""
            QFrame#socModuleControlBar {{
                background-color: #060d1a;
                border-bottom: 1px solid {self.accent_color};
            }}
        """)
        bar_layout = QHBoxLayout(self.control_bar)
        bar_layout.setContentsMargins(12, 6, 12, 6)
        bar_layout.setSpacing(8)

        self.lbl_mode_badge = QLabel("🪟 VENTANA INDEPENDIENTE")
        self.lbl_mode_badge.setStyleSheet(
            f"color: {self.accent_color}; background-color: #0f172a; "
            f"border: 1px solid {self.accent_color}; border-radius: 4px; "
            f"padding: 2px 8px; font-size: 10px; font-weight: bold; font-family: {ui_theme.FONT_MAIN};"
        )
        bar_layout.addWidget(self.lbl_mode_badge)

        self.lbl_bar_title = QLabel(self.full_title)
        self.lbl_bar_title.setStyleSheet(
            f"color: {ui_theme.TEXT_PRIMARY}; font-size: 12px; font-weight: bold; "
            f"border: none; font-family: {ui_theme.FONT_MAIN};"
        )
        bar_layout.addWidget(self.lbl_bar_title)

        bar_layout.addStretch(1)

        # Botón Dual: Acoplar en Pestaña del Cockpit <-> Desacoplar a Ventana
        self.btn_toggle_dock = QPushButton("📌 Acoplar como Pestaña en Cockpit")
        self.btn_toggle_dock.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        self.btn_toggle_dock.setToolTip(
            "Integra este módulo como una pestaña dentro del Command Center principal "
            "o lo separa como ventana independiente para segundo monitor"
        )
        self.btn_toggle_dock.clicked.connect(self._on_toggle_dock_clicked)
        bar_layout.addWidget(self.btn_toggle_dock)

        # Controles explícitos de ventana (útiles tanto en multi-monitor como para claridad visual)
        self.btn_win_min = QPushButton("🗕 Minimizar")
        self.btn_win_min.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_win_min.setToolTip("Minimizar ventana a la barra de tareas de Windows y barra inferior del SOC")
        self.btn_win_min.clicked.connect(self.showMinimized)
        bar_layout.addWidget(self.btn_win_min)

        self.btn_win_max = QPushButton("🗖 Maximizar / Restaurar")
        self.btn_win_max.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_win_max.setToolTip("Alternar entre ventana maximizada y tamaño restaurado")
        self.btn_win_max.clicked.connect(self._toggle_maximize)
        bar_layout.addWidget(self.btn_win_max)

        self.btn_win_close = QPushButton("✕ Cerrar Vista")
        self.btn_win_close.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_CRITICAL))
        self.btn_win_close.setToolTip("Cerrar vista del módulo (conserva estado en caché para reapertura instantánea)")
        self.btn_win_close.clicked.connect(self._close_or_undock_hide)
        bar_layout.addWidget(self.btn_win_close)

        self.root_layout.addWidget(self.control_bar)
        self.root_layout.addWidget(self.content_widget, 1)

    def _restore_or_adapt_geometry(self):
        settings = QSettings("TechnomaSOC", "OpenXDR_WindowManager")
        saved_geom = settings.value(f"{self.module_key}/geometry")
        if saved_geom:
            self.restoreGeometry(saved_geom)
            return

        screen = QApplication.primaryScreen()
        if screen:
            avail = screen.availableGeometry()
            target_w = min(self._default_size[0], int(avail.width() * 0.90))
            target_h = min(self._default_size[1], int(avail.height() * 0.88))
            self.resize(target_w, target_h)
            self.setMinimumSize(min(820, target_w), min(520, target_h))
            self.move(
                avail.x() + (avail.width() - target_w) // 2,
                avail.y() + (avail.height() - target_h) // 2
            )
        else:
            self.resize(*self._default_size)

    def _save_geometry(self):
        if not self.is_docked_in_tab:
            try:
                settings = QSettings("TechnomaSOC", "OpenXDR_WindowManager")
                settings.setValue(f"{self.module_key}/geometry", self.saveGeometry())
            except Exception:
                pass

    def _toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.state_changed.emit(self.module_key)

    def _on_toggle_dock_clicked(self):
        if self.is_docked_in_tab:
            self.undock_requested.emit(self.module_key)
        else:
            self.dock_requested.emit(self.module_key)

    def _close_or_undock_hide(self):
        if self.is_docked_in_tab:
            self.undock_requested.emit(self.module_key)
        self.hide()
        self.state_changed.emit(self.module_key)

    def _on_inner_dialog_finished(self, _result: int):
        self._close_or_undock_hide()

    def set_docked_ui_mode(self, docked: bool):
        self.is_docked_in_tab = docked
        if docked:
            self.lbl_mode_badge.setText("📌 ACOPLADO EN COCKPIT")
            self.btn_toggle_dock.setText("↗ Desacoplar a Ventana Independiente")
            self.btn_win_min.setVisible(False)
            self.btn_win_max.setVisible(False)
        else:
            self.lbl_mode_badge.setText("🪟 VENTANA INDEPENDIENTE")
            self.btn_toggle_dock.setText("📌 Acoplar como Pestaña en Cockpit")
            self.btn_win_min.setVisible(True)
            self.btn_win_max.setVisible(True)

    def changeEvent(self, event: QEvent):
        super().changeEvent(event)
        if event.type() == QEvent.Type.WindowStateChange:
            self.state_changed.emit(self.module_key)

    def closeEvent(self, event: QEvent):
        self._save_geometry()
        event.ignore()
        self.hide()
        self.state_changed.emit(self.module_key)


class SOCWindowManager(QObject):
    """
    Orquestador centralizado de todas las ventanas satélites y módulos acoplables del Command Center.
    Garantiza un comportamiento 100% homogéneo al abrir, minimizar, maximizar, restaurar y acoplar.
    """

    def __init__(self, main_window, main_tabs: QTabWidget):
        super().__init__(main_window)
        self.main_window = main_window
        self.main_tabs = main_tabs
        self.modules: Dict[str, SOCManagedWindow] = {}
        self.taskbar_frame: Optional[QFrame] = None
        self.taskbar_buttons_layout: Optional[QHBoxLayout] = None
        self._pill_buttons: Dict[str, QPushButton] = {}

    def create_taskbar_widget(self) -> QFrame:
        """
        Crea la barra inferior de estado de ventanas/módulos activos del SOC.
        Permite ver de un vistazo qué herramientas están abiertas, minimizadas o acopladas
        y restaurarlas con un solo clic.
        """
        self.taskbar_frame = QFrame()
        self.taskbar_frame.setObjectName("socTaskbarFrame")
        self.taskbar_frame.setStyleSheet(f"""
            QFrame#socTaskbarFrame {{
                background-color: #050b14;
                border-top: 1px solid {ui_theme.BORDER_SUBTLE};
            }}
        """)
        layout = QHBoxLayout(self.taskbar_frame)
        layout.setContentsMargins(12, 4, 12, 4)
        layout.setSpacing(8)

        lbl_wm = QLabel("🎛️ GESTOR DE VENTANAS Y MÓDULOS:")
        lbl_wm.setStyleSheet(
            f"color: {ui_theme.TEXT_MUTED}; font-size: 10px; font-weight: bold; "
            f"font-family: {ui_theme.FONT_MAIN}; border: none;"
        )
        layout.addWidget(lbl_wm)

        self.taskbar_buttons_layout = QHBoxLayout()
        self.taskbar_buttons_layout.setSpacing(6)
        layout.addLayout(self.taskbar_buttons_layout)

        self.lbl_no_modules = QLabel("Ninguna ventana satélite abierta (100% listas en barra superior)")
        self.lbl_no_modules.setStyleSheet(
            f"color: #475569; font-size: 10px; font-style: italic; font-family: {ui_theme.FONT_MAIN}; border: none;"
        )
        layout.addWidget(self.lbl_no_modules)

        layout.addStretch(1)

        btn_dock_all = QPushButton("📌 Acoplar Todas al Cockpit")
        btn_dock_all.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_dock_all.setToolTip("Convierte todas las ventanas flotantes abiertas en pestañas dentro del Command Center")
        btn_dock_all.clicked.connect(self.dock_all_open_modules)
        layout.addWidget(btn_dock_all)

        btn_restore_all = QPushButton("🗖 Traer Ventanas al Frente")
        btn_restore_all.setStyleSheet(ui_theme.secondary_tool_btn_style())
        btn_restore_all.setToolTip("Restaura todas las ventanas minimizadas del SOC")
        btn_restore_all.clicked.connect(self.restore_all_minimized)
        layout.addWidget(btn_restore_all)

        return self.taskbar_frame

    def open_module(
        self,
        module_key: str,
        title: str,
        short_title: str,
        accent_color: str,
        factory_fn: Callable[[], QWidget],
        default_size: tuple = (1280, 820),
        force_recreate: bool = False,
        on_ready_callback: Optional[Callable[[QWidget], None]] = None,
        prefer_docked: bool = False
    ) -> QWidget:
        """
        Abre, restaura o enfoca un módulo de manera estandarizada y no bloqueante.
        """
        if force_recreate and module_key in self.modules:
            old_win = self.modules.pop(module_key)
            if old_win.is_docked_in_tab:
                idx = self.main_tabs.indexOf(old_win)
                if idx >= 0:
                    self.main_tabs.removeTab(idx)
            old_win.deleteLater()

        if module_key not in self.modules:
            inner_widget = factory_fn()
            managed = SOCManagedWindow(
                module_key=module_key,
                title=title,
                short_title=short_title,
                accent_color=accent_color,
                content_widget=inner_widget,
                default_size=default_size
            )
            managed.state_changed.connect(self._refresh_taskbar)
            managed.dock_requested.connect(self.dock_module)
            managed.undock_requested.connect(self.undock_module)
            self.modules[module_key] = managed

        managed = self.modules[module_key]

        if on_ready_callback is not None:
            try:
                on_ready_callback(managed.content_widget)
            except Exception as e:
                print(f"[SOCWindowManager] Advertencia en on_ready_callback ({module_key}): {e}")

        if prefer_docked or managed.is_docked_in_tab:
            self.dock_module(module_key)
        else:
            # Si estaba minimizado en Windows, restaurar su estado previo (Maximizado o Normal)
            if managed.isMinimized():
                managed.setWindowState(
                    (managed.windowState() & ~Qt.WindowState.WindowMinimized)
                    | Qt.WindowState.WindowActive
                )
            managed.show()
            managed.raise_()
            managed.activateWindow()

        self._refresh_taskbar()
        return managed.content_widget

    def dock_module(self, module_key: str):
        """Acopla una ventana independiente como una pestaña dentro de self.main_tabs."""
        managed = self.modules.get(module_key)
        if not managed:
            return

        managed._save_geometry()
        managed.hide()
        managed.set_docked_ui_mode(True)

        idx = self.main_tabs.indexOf(managed)
        if idx == -1:
            idx = self.main_tabs.addTab(managed, f"{managed.short_title} 📌")
        managed.show()
        self.main_tabs.setCurrentIndex(idx)
        self._refresh_taskbar()

    def undock_module(self, module_key: str):
        """Desacopla un módulo desde self.main_tabs hacia una ventana nativa independiente."""
        managed = self.modules.get(module_key)
        if not managed:
            return

        idx = self.main_tabs.indexOf(managed)
        if idx >= 0:
            self.main_tabs.removeTab(idx)

        managed.setParent(None)
        managed.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.WindowSystemMenuHint
            | Qt.WindowType.WindowMinimizeButtonHint
            | Qt.WindowType.WindowMaximizeButtonHint
            | Qt.WindowType.WindowCloseButtonHint
        )
        managed.set_docked_ui_mode(False)
        managed._restore_or_adapt_geometry()
        managed.show()
        managed.raise_()
        managed.activateWindow()
        self._refresh_taskbar()

    def dock_all_open_modules(self):
        for key, win in list(self.modules.items()):
            if win.isVisible() and not win.is_docked_in_tab:
                self.dock_module(key)

    def restore_all_minimized(self):
        for key, win in list(self.modules.items()):
            if not win.is_docked_in_tab and (win.isMinimized() or win.isVisible()):
                if win.isMinimized():
                    win.setWindowState(
                        (win.windowState() & ~Qt.WindowState.WindowMinimized)
                        | Qt.WindowState.WindowActive
                    )
                win.show()
                win.raise_()
                win.activateWindow()
        self._refresh_taskbar()

    def _on_pill_clicked(self, module_key: str):
        managed = self.modules.get(module_key)
        if not managed:
            return
        if managed.is_docked_in_tab:
            idx = self.main_tabs.indexOf(managed)
            if idx >= 0:
                self.main_tabs.setCurrentIndex(idx)
            else:
                self.dock_module(module_key)
        else:
            if managed.isMinimized() or not managed.isVisible():
                managed.setWindowState(
                    (managed.windowState() & ~Qt.WindowState.WindowMinimized)
                    | Qt.WindowState.WindowActive
                )
                managed.show()
            managed.raise_()
            managed.activateWindow()
        self._refresh_taskbar()

    def _refresh_taskbar(self, *_args):
        if not self.taskbar_buttons_layout:
            return

        # Limpiar botones anteriores
        while self.taskbar_buttons_layout.count():
            item = self.taskbar_buttons_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        active_count = 0
        for key, win in self.modules.items():
            is_in_tab = win.is_docked_in_tab and self.main_tabs.indexOf(win) >= 0
            is_win_open = (not win.is_docked_in_tab) and (win.isVisible() or win.isMinimized())
            if not (is_in_tab or is_win_open):
                continue

            active_count += 1
            if is_in_tab:
                state_tag = "📌 Pestaña"
                border_col = ui_theme.ACCENT_CYBER
                bg_col = "#0f2438"
            elif win.isMinimized():
                state_tag = "🗕 Minimizado"
                border_col = ui_theme.COLOR_MEDIUM
                bg_col = "#1e1b18"
            else:
                state_tag = "🪟 Ventana"
                border_col = win.accent_color
                bg_col = "#0f172a"

            btn = QPushButton(f"{win.short_title} [{state_tag}]")
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {bg_col};
                    color: {ui_theme.TEXT_PRIMARY};
                    border: 1px solid {border_col};
                    border-radius: 4px;
                    padding: 2px 10px;
                    font-size: 10px;
                    font-weight: bold;
                    font-family: {ui_theme.FONT_MAIN};
                }}
                QPushButton:hover {{
                    background-color: #1e293b;
                    border-color: #ffffff;
                }}
            """)
            btn.setToolTip(f"Clic para restaurar o traer al frente: {win.full_title}")
            btn.clicked.connect(lambda _checked=False, k=key: self._on_pill_clicked(k))
            self.taskbar_buttons_layout.addWidget(btn)

        if self.lbl_no_modules:
            self.lbl_no_modules.setVisible(active_count == 0)

    def close_all(self):
        """Cierra limpiamente todas las ventanas satélites al cerrar el Cockpit principal."""
        for key, win in list(self.modules.items()):
            try:
                win._save_geometry()
                cw = getattr(win, "content_widget", None)
                if cw is not None:
                    for attr in ("worker", "ai_worker", "web_worker", "_worker"):
                        th = getattr(cw, attr, None)
                        if th is not None and hasattr(th, "isRunning") and th.isRunning():
                            th.quit()
                            th.wait(500)
                win.hide()
            except Exception:
                pass
        self.modules.clear()

