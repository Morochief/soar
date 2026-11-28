#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Acceso desde tools_stellar/ a ../audit_yesterday_domains.py.

Antes este archivo era una copia idéntica del de la raíz y cada arreglo había que
hacerlo dos veces (y las copias se desincronizaban). Ahora el código vive solo en la
raíz del repo; este archivo lo ejecuta o lo re-exporta.
"""
import os
import sys
import runpy
import importlib.util

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
_TARGET = os.path.join(_ROOT, "audit_yesterday_domains.py")

if __name__ == "__main__":
    runpy.run_path(_TARGET, run_name="__main__")
else:
    _spec = importlib.util.spec_from_file_location("_root_audit_yesterday_domains", _TARGET)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    globals().update({k: v for k, v in vars(_mod).items() if not k.startswith("__")})
