@echo off
title Technoma SOC - Centro de Auditoria Forense de Ingesta, Cuota y Log Filters
cd /d "%~dp0"

echo ==============================================================================
echo   Iniciando Technoma SOC - Centro de Auditoria Forense de Ingesta y Cuota
echo ==============================================================================

if exist "venv\Scripts\pythonw.exe" (
    start "" "venv\Scripts\pythonw.exe" "ingestion_audit_dialog.py"
) else if exist "venv\Scripts\python.exe" (
    start "" "venv\Scripts\python.exe" "ingestion_audit_dialog.py"
) else if exist "Scripts\pythonw.exe" (
    start "" "Scripts\pythonw.exe" "ingestion_audit_dialog.py"
) else if exist "Scripts\python.exe" (
    start "" "Scripts\python.exe" "ingestion_audit_dialog.py"
) else (
    start "" python "ingestion_audit_dialog.py"
)

exit
