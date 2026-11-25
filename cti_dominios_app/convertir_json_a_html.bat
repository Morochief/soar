@echo off
title Convertir Reporte JSON de n8n a Dashboard HTML
cd /d "%~dp0"
echo ========================================================
echo   Conversor de JSON de n8n a Dashboard HTML (0 Puertos)
echo ========================================================
if "%~1"=="" (
    python convertir_json_a_html.py
) else (
    python convertir_json_a_html.py "%~1"
)
echo.
echo ========================================================
echo Operacion completada. Se abrio el dashboard en tu navegador.
timeout /t 5
