#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilidades para manejar QThreads de forma segura en los diálogos del SOAR.

Problema que resuelve: varios diálogos hacían `self.worker = NuevoWorker(...)` mientras
el worker anterior seguía corriendo. Python liberaba el objeto viejo y Qt abortaba con
"QThread: Destroyed while thread is still running" (crash). Lo mismo al cerrar un
diálogo con un worker activo.

Uso:
    self.th_worker = replace_worker(self.th_worker, NuevoWorker(...), ("finished", "error"))
    ...
    def closeEvent(self, event):
        retire_workers([self.th_worker, self.drill_worker], ("finished", "error"))
        super().closeEvent(event)
"""

from typing import Iterable, Optional, Sequence

# Workers retirados que todavía corren: se guarda la referencia hasta que terminen,
# para que Python no destruya el QThread en medio de su ejecución.
_RETIRED = []


def _prune():
    _RETIRED[:] = [w for w in _RETIRED if _is_running(w)]


def _is_running(worker) -> bool:
    try:
        return bool(worker.isRunning())
    except RuntimeError:  # objeto C++ ya destruido
        return False


def retire_worker(worker, signal_names: Sequence[str] = ("finished", "error")) -> None:
    """Desconecta las señales del worker (sus resultados ya no importan) y lo mantiene vivo hasta que termine."""
    if worker is None:
        return
    for name in signal_names:
        sig = getattr(worker, name, None)
        if sig is None:
            continue
        try:
            sig.disconnect()
        except (RuntimeError, TypeError, AttributeError):
            pass
    cancel = getattr(worker, "cancel", None)
    if callable(cancel):
        try:
            cancel()
        except Exception:
            pass
    _prune()
    if _is_running(worker):
        try:
            # Sin padre: que no lo destruya el diálogo al cerrarse
            worker.setParent(None)
        except Exception:
            pass
        _RETIRED.append(worker)


def retire_workers(workers: Iterable, signal_names: Sequence[str] = ("finished", "error")) -> None:
    for w in workers:
        retire_worker(w, signal_names)


def replace_worker(old, new, signal_names: Sequence[str] = ("finished", "error")):
    """Retira el worker anterior (si sigue corriendo) y devuelve el nuevo, listo para conectar y arrancar."""
    retire_worker(old, signal_names)
    return new
