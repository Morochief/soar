#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Acceso desde cti_dominios_app/ a ../convertir_json_a_html.py (antes era una copia idéntica).
El código vive solo en la raíz del repo; este archivo lo ejecuta con los mismos argumentos.
"""
import os
import sys
import runpy

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

if __name__ == "__main__":
    runpy.run_path(os.path.join(_ROOT, "convertir_json_a_html.py"), run_name="__main__")
