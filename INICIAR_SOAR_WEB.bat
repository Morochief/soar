@echo off
chcp 65001 >nul
title TECHNOMA SOAR — Web Command Center
cd /d "%~dp0"
echo ============================================================================
echo   🛡️  INICIANDO TECHNOMA SOAR WEB COMMAND CENTER (http://localhost:8090)
echo ============================================================================
python soar_web.py --port 8090
pause
