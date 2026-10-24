# 🛡️ PROCEDIMIENTO SOC: CONTROL CRUZADO, SINCRONIZACIÓN Y CIERRE MASIVO DE CASOS (CORTEX XDR ➔ STELLAR CYBER)

**Fecha de Actualización:** 24 de Octubre de 2026  
**Área:** SOC Technoma / Automatización e Integración SOAR  
**Ubicación de Scripts:** `c:\Users\kevinmoraes\Desktop\SOC\soar\`  

---

## 1. Contexto y Objetivos Operativos

En el SOC Technoma se realiza el **control cruzado estricto** entre las detecciones e incidentes generados en **Palo Alto Networks Cortex XDR** y los Casos gestionados en **Stellar Cyber**:

1. **Verificación y Detección**: Localizar en el Data Lake de Stellar Cyber (`aella-ser-*` e índice `Syslog`) todas las alertas enviadas por Cortex XDR que contengan un `palo_alto_networks.case_id` o `palo_alto_networks.incident_id` válido.
2. **Creación Automática de Casos**: Cuando una alerta de Cortex trae `case_id` o `incident_id` pero aún no tiene Caso en Stellar, crear el caso inmediatamente vía API (`POST /connect/api/v1/cases`) estandarizando su nombre con el formato:
   `Palo Alto Networks Cortex XDR: <descripción> - CASE <id>`
3. **Vinculación Forense Atómica**: Asociar todos los documentos de alertas forenses (`_index` y `_id`) en la creación del caso (`alerts: [{"_id": ..., "_index": ...}]`) para que la consola web de Stellar Cyber refleje la línea de tiempo completa, trazabilidad y evidencia técnica.
4. **Cierre Masivo con Justificación Forense**: Cerrar casos calificados como `Resolved` asignando las resoluciones oficiales (`Benign`, `False Positive`, `True Positive`) junto con el motivo/dictamen técnico emitido por el analista SOC.

---

## 2. Herramientas Desarrolladas

### Script A: [`auto_create_cortex_cases.py`](file:///c:/Users/kevinmoraes/Desktop/SOC/soar/auto_create_cortex_cases.py)
*Motor automatizado de control cruzado, generación de casos y vinculación forense atómica.*
- Detecta tanto `palo_alto_networks.case_id` como `palo_alto_networks.incident_id`.
- Consulta la lista de casos existentes en Stellar para evitar duplicados.
- Respeta la estricta validación del endpoint `POST /connect/api/v1/cases` (los incidentes deben enviarse en el array `alerts`, sin campo `description` en el cuerpo principal).

#### Parámetros soportados:
- `--month YYYY-MM`: Filtra exclusivamente las alertas correspondientes a un mes (ej. `--month 2026-10`).
- `--dry-run`: Simula la ejecución mostrando qué casos se crearían y qué alertas se vincularían sin hacer modificaciones en producción.
- `--tenant ID`: Permite cambiar el ID de Tenant (por defecto usa `e511c3fc54cd4d668bb67612c2ef4b04` de `.env`).

#### Comandos de uso rápido:
```bash
# 1. Simular creación de casos faltantes de octubre
python c:\Users\kevinmoraes\Desktop\SOC\soar\auto_create_cortex_cases.py --month 2026-10 --dry-run

# 2. Ejecutar creación automática y vinculación en producción
python c:\Users\kevinmoraes\Desktop\SOC\soar\auto_create_cortex_cases.py --month 2026-10
```

---

### Script B: [`check_missing_cortex_cases.py`](file:///c:/Users/kevinmoraes/Desktop/SOC/soar/check_missing_cortex_cases.py)
*Auditor rápido de paridad y diagnóstico de alertas Cortex vs Casos Stellar.*

```bash
# Auditar estado de incidentes del mes
python c:\Users\kevinmoraes\Desktop\SOC\soar\check_missing_cortex_cases.py --month 2026-10
```

---

### Script C: [`close_cases_bulk.py`](file:///c:/Users/kevinmoraes/Desktop/SOC/soar/close_cases_bulk.py)
*Herramienta de remediación y cierre masivo de casos en Stellar Cyber.*

#### Parámetros soportados:
- `--resolution`: Resolución formal obligatoria. Opciones válidas en la API de Stellar Cyber:
  - `"Benign"` (Actividad autorizada o utilitarios corporativos).
  - `"False Positive"` (Falsas alarmas de scripts, desarrollo o telemetría interna).
  - `"True Positive"` (Amenaza confirmada remediada).
- `--reason`: Justificación técnica o forense del cierre.
- `--cortex-cases`: Lista de IDs de casos de Cortex separados por comas (ej. `610,604,601`).
- `--stellar-cases`: Lista de Object IDs nativos de Stellar Cyber (ej. `6ad37e84e4fb8b7307d83837`).
- `--month`: Cierra todos los casos correspondientes a un mes determinado (ej. `2026-10`).
- `--dry-run`: Simula el cierre sin impactar en producción.

#### Comandos de uso rápido:
```bash
# 1. Simular cierre de casos específicos de Cortex
python c:\Users\kevinmoraes\Desktop\SOC\soar\close_cases_bulk.py --cortex-cases 610,604 --resolution "False Positive" --dry-run

# 2. Cerrar casos por IDs de Cortex con dictamen
python c:\Users\kevinmoraes\Desktop\SOC\soar\close_cases_bulk.py --cortex-cases 599,596,586 --resolution "False Positive" --reason "Comportamiento headless legítimo de terminal IDE"

# 3. Cerrar masivamente todos los casos de un mes completo
python c:\Users\kevinmoraes\Desktop\SOC\soar\close_cases_bulk.py --month 2026-10 --resolution "False Positive" --reason "Actividad operacional y benigna validada por SOC Technoma"
```

---

## 3. Matriz de Estados de la API de Stellar Cyber

Para interactuar con la API `/connect/api/v1/cases` se debe respetar estrictamente el esquema de validación:
- **Estados de Caso (`status`)**:
  - `New` (Nuevo)
  - `In Progress` (En progreso)
  - `Escalated` (Escalado)
  - `Resolved` (Cerrado / Resuelto) ⚠️ *Nota: 'Closed' no es admitido por el validador estricto, siempre usar 'Resolved'.*
- **Resoluciones Admitidas (`resolution`)**:
  - `Benign`
  - `False Positive`
  - `True Positive`

---

## 4. Auditoría y Registro de Casos de Octubre 2026

Casos creados, vinculados forensemente y resueltos en producción:

| Cortex ID | Stellar Ticket | Endpoint | Descripción Resumida | Resolución Aplicada | Dictamen Registrado |
| :---: | :---: | :---: | :--- | :---: | :--- |
| **618** | #18168 | `NB-KMORAEZ` | OpenAI Codex / powershell invoke | **Resolved / False Positive** | Invocación de herramientas de build local |
| **617** | #18169 | `NB-MANUELALM` | LOLBIN scripting engine rare host | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **616** | #18170 | `NB-GVERA` | PowerShell invoke expression | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **615** | #18171 | `NB-KMORAEZ` | TOR domain file request | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **614** | #18172 | `NB-RALEMAN` | Super Productivity Dropbox sync | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **613** | #18173 | `NB-ODACOSTA` | 23 hosts connection attempts | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **612** | #18174 | `NB-EORLANDINI` | curl www.mastertech.com.py | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **611** | #18175 | `NB-GVERA` | PowerShell invoke expression | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **610** | #18176 | `NB-EORLANDINI` | LOLBIN rare host connection | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **609** | #18177 | `NB-KMORAEZ` | Upload daily-cloudcode-pa.googleapis.com | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **607** | #18178 | `NB-FMORA` | Upload fra-storage.proton.me | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **604** | #18179 | `NB-JTORALES` | AMSI obfuscation technique | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **601** | #18180 | `NB-GMARTINEZ` | Suspicious payload executable | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **599** | #18181 | `NB-FBENEGAS` | conhost powershell --headless | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **597** | #18182 | `NB-EDVELAZQUEZ`| BITS transfer execution | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **596** | #18183 | `NB-RBARRETO` | conhost powershell --headless | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **595** | #18184 | `NB-NOC2` | winget videolan.c3sl.ufpr.br | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **594** | #18185 | `NB-EORLANDINI` | curl huggingface.co | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **593** | #18186 | `NB-FBENEGAS` | winget videolan.c3sl.ufpr.br | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **588** | #18187 | `NB-IMAYOR` | conhost powershell --headless | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **586** | #18188 | `NB-FBENEGAS` | conhost powershell --headless | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
| **541** | #18189 | `NB-JTORALES` | 16 hosts connection attempts | **Resolved / False Positive** | Actividad operacional y benigna validada por SOC |
