@echo off
TITLE OpenXDR MASTER COCKPIT GUI v6.5.0s
:: =============================================================================
:: SLA NOC - Orquestador Gráfico Unificado de Ciberseguridad
:: Lanza la GUI de PySide6 absorbiendo las variables internas del soc-env
:: =============================================================================

echo [+] Sincronizando librerías del Centro de Operaciones...
echo [+] Activando entorno virtual aislado protegido (soc-env)...

:: 1. Activa de forma transparente el venv
call "%~dp0venv\Scripts\activate.bat" 2>nul || call "%~dp0Scripts\activate.bat" 2>nul || call "%USERPROFILE%\Documents\soc-env\Scripts\activate.bat"

echo [+] Entorno virtual activo de forma exitosa.
echo [+] Levantando interfaz gráfica PySide6 (EDR-Safe)...
echo -------------------------------------------------------------------------

:: 2. Lanza el panel de command center unificado
python "%~dp0command_center.py" 2>nul || python "%USERPROFILE%\Documents\soc-env\command_center.py"

:: 3. Mantiene la ventana abierta si el script de Python se estrella
echo.
echo -------------------------------------------------------------------------
echo [!] La interfaz gráfica se ha cerrado o ha fallado el proceso.
pause