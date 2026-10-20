@echo off
:: =============================================================================
::      STELLAR CYBER OpenXDR Command Center - INSTALADOR DE ENTORNO SEGURO
::      Technoma SOC - Cierre y Registro Permanente de Credenciales
:: =============================================================================
title STELLAR CYBER COMMAND CENTER - SETUP ENTORNO SEGURO

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando privilegios de Administrador...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b 0
)

echo ============================================================================
echo   STELLAR CYBER COMMAND CENTER - CONFIGURACION DE ENTORNO SEGURO
echo ============================================================================
echo.
echo [*] Cargando variables desde archivo .env hacia el entorno de Windows...
echo.
if not exist "%~dp0.env" (
    echo [!] ERROR: No se encontro el archivo .env en %~dp0
    echo     Copie .env.example a .env y complete sus credenciales antes de continuar.
    pause
    exit /b 1
)

for /f "usebackq tokens=1,* delims==" %%A in ("%~dp0.env") do (
    echo %%A | findstr /r "^[^#]" >nul
    if not errorlevel 1 (
        if not "%%B"=="" (
            setx %%A "%%B" /M >nul
            echo   [+] Registrada: %%A
        )
    )
)

echo.
echo ----------------------------------------------------------------------------
echo [+] Exito: Las variables de entorno de .env han sido registradas.
echo [+] ADVERTENCIA: Debe reiniciar su sesion de Windows o las consolas activas
echo     para que el Cockpit reconozca las nuevas variables.
echo ----------------------------------------------------------------------------
echo.
pause