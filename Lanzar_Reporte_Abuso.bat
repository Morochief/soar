@echo off
title Technoma SOC - Generador de Reportes de Abuso OpenXDR
cd /d "%~dp0"

echo ========================================================
echo   Iniciando Technoma SOC - Módulo de Reportes de Abuso
echo ========================================================

if exist "venv\Scripts\pythonw.exe" (
    start "" "venv\Scripts\pythonw.exe" "abuse_report_dialog.py"
) else if exist "venv\Scripts\python.exe" (
    start "" "venv\Scripts\python.exe" "abuse_report_dialog.py"
) else if exist "Scripts\pythonw.exe" (
    start "" "Scripts\pythonw.exe" "abuse_report_dialog.py"
) else if exist "Scripts\python.exe" (
    start "" "Scripts\python.exe" "abuse_report_dialog.py"
) else (
    start "" python "abuse_report_dialog.py"
)

exit
