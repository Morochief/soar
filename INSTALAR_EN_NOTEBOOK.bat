@echo off
chcp 65001 >nul
title TECHNOMA SOC - Instalador Portatil para Notebook / Nuevo Equipo
cd /d "%~dp0"

echo ============================================================================
echo   🛡️ TECHNOMA SOC — SETUP AUTOMATICO PARA NOTEBOOK / OFICINA
echo ============================================================================
echo.

:: 1. Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] ERROR: Python no esta instalado o no esta en el PATH de Windows.
    echo     Instale Python 3.11+ desde python.org marcando "Add Python to PATH".
    pause
    exit /b 1
)

:: 2. Instalar dependencias del Cockpit (PySide6, requests, dotenv, etc.)
echo [1/4] Instalando librerias requeridas de requirements.txt...
python -m pip install -r requirements.txt --quiet
echo       [OK] Librerias base instaladas.

:: 3. Instalar el puente OAuth de Antigravity (si existe la carpeta hermes-antigravity-auth al lado)
if exist "%~dp0..\hermes-antigravity-auth\pyproject.toml" (
    echo [2/4] Instalando conector OAuth Google Antigravity local...
    python -m pip install -e "%~dp0..\hermes-antigravity-auth" --quiet
    echo       [OK] Conector Antigravity OAuth instalado.
) else (
    echo [2/4] Instalando conector OAuth Google Antigravity desde GitHub...
    python -m pip install "git+https://github.com/Morochief/hermes-antigravity-auth.git" --quiet 2>nul
)

:: 4. Verificar o construir el Cerebro RAG de 2.081 Markdowns (.rag_index_cache.pkl)
echo [3/4] Verificando Cerebro RAG de 7 Capas (2.081 Markdowns)...
python soar_cli.py rag-stats
echo       [OK] Cerebro RAG listo.

:: 5. Verificar autenticacion de IA (Antigravity OAuth o GEMINI_API_KEY)
echo [4/4] Verificando conexion con Inteligencia Artificial...
python -c "from soar_ai_client import is_antigravity_available; import os; print('      [OK] Google Antigravity OAuth ACTIVO.' if is_antigravity_available() else ('      [OK] GEMINI_API_KEY / NVIDIA_API_KEY ACTIVA.' if (os.environ.get('GEMINI_API_KEY') or os.environ.get('NVIDIA_API_KEY')) else '      [!] AVISO: Ejecute: python -m antigravity_auth login para iniciar sesion con Google.'))"

echo.
echo ============================================================================
echo   ✅ LISTO PARA OPERAR EN ESTA NOTEBOOK
echo   Para abrir tu Cockpit ejecuta: INICIAR_COMMAND_CENTER.bat
echo ============================================================================
pause
