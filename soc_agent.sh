#!/usr/bin/env bash
# =============================================================================
# Wrapper para ejecutar soc_agent.py desde Linux / WSL / Bash
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Si estamos en WSL y existe el venv de Windows, podemos usar el python del venv o python3 de Linux
if command -v wslpath >/dev/null 2>&1 && [ -f "$SCRIPT_DIR/Scripts/python.exe" ]; then
    WIN_SCRIPT=$(wslpath -w "$SCRIPT_DIR/soc_agent.py")
    "$SCRIPT_DIR/Scripts/python.exe" "$WIN_SCRIPT" "$@"
elif [ -f "$SCRIPT_DIR/Scripts/python.exe" ]; then
    "$SCRIPT_DIR/Scripts/python.exe" "$SCRIPT_DIR/soc_agent.py" "$@"
else
    python3 "$SCRIPT_DIR/soc_agent.py" "$@"
fi
