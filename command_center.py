#!/usr/bin/python3
# -*- coding: utf-8 -*-
# =============================================================================
#      STELLAR CYBER 6.5.2 - UNIFIED XDR COMMAND CENTER (MODULAR ARCHITECTURE)
#      SLA NOC - EDR-Safe, Asynchronous Multi-Threaded PySide6 & SOCWindowManager
# =============================================================================
"""
Punto de entrada principal y fachada de compatibilidad 100% retrocompatible.
Toda la arquitectura vive modularizada en el paquete `soar_app/`:
  - `soar_app.core.infra`: Credenciales .env, LRUCache, RestSessionManager, MobileAlertsNotifier
  - `soar_app.workers.api_workers`: 19 Workers QThread / QRunnable de API, IA, CTI, CVE y Security Onion
  - `soar_app.workers.auto_remediators`: 6 Demonios Auto-Remediadores 24/7
  - `soar_app.ui.window_manager`: SOCWindowManager (Ventanas independientes + Acoplamiento en pestañas)
  - `soar_app.ui.tabs.*`: Mixins modulares por dominio y nuevo módulo Stellar Hunter & Gobernabilidad
  - `soar_app.ui.main_window`: XdrDashboard principal
"""

import sys
from PySide6.QtWidgets import QApplication

# Re-exportar absolutamente todo para mantener compatibilidad 100% con tests y scripts externos
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
from soar_app.workers.auto_remediators import *
from soar_app.ui.window_manager import SOCWindowManager, SOCManagedWindow
from soar_app.ui.main_window import XdrDashboard


def main():
    app = QApplication.instance() or QApplication(sys.argv)
    window = XdrDashboard()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
