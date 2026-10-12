@echo off
title Technoma SOC - AI Forensic Copilot
cd /d "%~dp0"

echo ========================================================
echo   Iniciando Technoma SOC - AI Forensic Copilot (GUI)
echo ========================================================

if exist "venv\Scripts\pythonw.exe" (
    start "" "venv\Scripts\pythonw.exe" "soc_agent_gui.py"
) else if exist "venv\Scripts\python.exe" (
    start "" "venv\Scripts\python.exe" "soc_agent_gui.py"
) else if exist "Scripts\pythonw.exe" (
    start "" "Scripts\pythonw.exe" "soc_agent_gui.py"
) else if exist "Scripts\python.exe" (
    start "" "Scripts\python.exe" "soc_agent_gui.py"
) else (
    start "" python "soc_agent_gui.py"
)

exit
