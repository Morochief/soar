---
name: stellar-api-interaction
description: "Estándar obligatorio para toda interacción, auditoría y consulta contra la API de Stellar Cyber. Prohíbe terminantemente el uso de 'python -c', exigiendo la creación y ejecución de scripts Python versionados y reproducibles."
risk: low
source: workspace
date_added: '2026-10-16'
---

# Skill: Interacción con la API de Stellar Cyber (Script-Driven Operations)

Esta skill establece la regla de oro operativa para la interacción técnica con la API de **Stellar Cyber OpenXDR**:

> ⚠️ **REGLA MANDATORIA DE ORO: NUNCA USAR `python -c`**  
> Está estrictamente prohibido ejecutar comandos one-liner efímeros o no reproducibles del tipo `python -c "..."` para consultar, probar o interactuar con la API.

---

## 🎯 Principios Operativos

1. **Scripts Dedicados y Persistentes:**  
   Toda interacción, auditoría, prueba o modificación contra la API debe materializarse en un archivo script Python (`.py`), ubicado preferentemente en la carpeta correspondiente (`auditoria_cuota_stellar/` o scripts de soporte).
2. **Autenticación Limpia y Robusta:**  
   Los scripts deben reutilizar las variables de entorno oficiales del sistema o valores seguros de fallback (`STELLAR_HOST`, `STELLAR_EMAIL`, `STELLAR_TOKEN`), obteniendo el JWT mediante Basic Auth contra `/connect/api/v1/access_token` con manejo de excepciones y desactivación de advertencias SSL (`urllib3.disable_warnings`).
3. **Herramienta Unificada Central (`stellar_cli.py`):**  
   Antes de crear cualquier script nuevo, utilizar siempre la herramienta definitiva de la raíz:
   `.\Scripts\python.exe stellar_cli.py --case <ID> | --list-cases | --quota | --search <QUERY> | --filters`
   Documentación completa: `Analista SOC/Stellar Documentacion/GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md`.
4. **Manejo Estructurado de Errores y Output Legible:**  
   No dejar volcados crudos incomprensibles. El script debe formatear tablas, listas y mensajes con prefijos claros (`[*]`, `[+]`, `[-]`, `[!]`).
5. **Reproducibilidad y Trazabilidad:**  
   Al crear un archivo `.py`, el analista puede volver a ejecutarlo directamente en cualquier momento desde su terminal o integrarlo al Command Center.
6. **Ejecución Vía Entorno Virtual:**  
   Siempre ejecutar utilizando el intérprete del entorno protegido del SOC:  
   `.\Scripts\python.exe ruta_del_script.py`
7. **Reglas del MCP Server de Stellar Cyber (`https://technoma.stellarcyber.cloud/mcp`):**
   - `ticket_id` DEBE ser string (ej: `"17813"`, NUNCA número `17813`).
   - Cada llamada al MCP requiere `access_token` en los argumentos del payload JSON-RPC.

---

## 📋 Estructura Base Canónica de un Script de API

Cada nuevo script debe seguir la siguiente plantilla probada:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Propósito del Script: [Descripción breve de la tarea]
Autor: Kevin Moraes / SOC Automation
"""

import os
import sys
import json
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")

def get_jwt() -> str:
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando contra Stellar Cyber ({r.status_code}): {r.text}")
        sys.exit(1)
    return r.json().get("access_token")

def main():
    print(f"[*] Conectando a Stellar Cyber: https://{HOST} con usuario {EMAIL}")
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }

    # Lógica específica de la operación (GET, POST, PUT, DELETE)
    # ...

if __name__ == "__main__":
    main()
```

---

## 🚫 Prácticas Prohibidas
* ❌ Ejecutar `python -c "import requests..."` en terminales de PowerShell o Bash.
* ❌ Hardcodear contraseñas en claro si ya están disponibles en el entorno.
* ❌ Modificar configuraciones críticas en producción sin imprimir y validar el payload antes de enviarlo.
