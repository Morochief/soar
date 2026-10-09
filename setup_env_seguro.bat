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
echo [*] Registrando credenciales seguras en las variables de entorno de Windows...
echo.

setx STELLAR_HOST "technoma.stellarcyber.cloud" /M
setx STELLAR_EMAIL "kevinmoraes@technoma.com.py" /M
setx STELLAR_TOKEN "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ" /M
setx GEMINI_API_KEY "AQ.Ab8RN6Lvk6AMc6-FFTT6ArRAKvmFruY9oeOY7exlcVwN_JJkng" /M
setx VIRUSTOTAL_API_KEY "6f21ffa2f287fee6c29090d96546648093f77bb4a2569bd92c46e0a659db586b" /M
setx ABUSEIPDB_API_KEY "c561b84d9edb984b134da2b0a89da35f1ef4752f15b03431a7fb2fbc0bf71b7aad9c1c5d3bbad716" /M
setx URLSCAN_API_KEY "019d698b-2d09-7490-9557-421d09b380d8" /M
setx MXTOOLBOX_API_KEY "3991dd4f-b601-477f-8e5e-c1a7232bc079" /M
setx NVD_API_KEY "ce79f233-34e5-4445-a3fd-84a8cd00beb6" /M
setx SO_ELASTIC_URL "https://172.17.10.25:9200" /M
setx SO_ELASTIC_API_KEY "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw==" /M

echo.
echo ----------------------------------------------------------------------------
echo [+] Exito: Las variables de entorno de produccion han sido registradas.
echo [+] ADVERTENCIA: Debe reiniciar su sesion de Windows o las consolas activas
echo     para que el Cockpit reconozca las nuevas variables.
echo ----------------------------------------------------------------------------
echo.
pause