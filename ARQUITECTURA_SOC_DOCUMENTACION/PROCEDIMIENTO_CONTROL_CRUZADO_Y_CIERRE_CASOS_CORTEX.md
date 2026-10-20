# 🛡️ PROCEDIMIENTO SOC: CONTROL CRUZADO, SINCRONIZACIÓN Y CIERRE MASIVO DE CASOS (CORTEX XDR ➔ STELLAR CYBER)

**Fecha:** 17 de Octubre de 2026  
**Área:** SOC Technoma / Automatización e Integración SOAR  
**Ubicación de Scripts:** `g:\Hermes + Antigravity\soar\`  

---

## 1. Contexto y Objetivos Operativos

En el SOC se requiere realizar el **control cruzado estricto** entre los incidentes detectados en **Palo Alto Networks Cortex XDR** y los Casos gestionados en **Stellar Cyber**:
1. **Verificación y Detección**: Localizar en el Data Lake de Stellar Cyber (`aella-ser-*`) todas las alertas enviadas por Cortex XDR que contengan un `palo_alto_networks.case_id` válido.
2. **Creación Automática de Casos**: Cuando una alerta de Cortex trae `case_id` pero aún no tiene Caso en Stellar, crear el caso inmediatamente (`POST /connect/api/v1/cases`) estandarizando su nombre con el formato `... - CASE <id>`.
3. **Vinculación Forense**: Asociar todos los documentos de alertas forenses (`_index` y `_id`) al caso (`POST /connect/api/v1/cases/{case_id}/alerts`) para que la consola web de Stellar Cyber refleje la línea de tiempo completa.
4. **Cierre Masivo**: Cerrar casos calificados como `Resolved` asignando las resoluciones oficiales (`Benign`, `False Positive`, `True Positive`).

---

## 2. Herramientas Desarrolladas

### Script A: [`sync_cortex_cases.py`](file:///g:/Hermes%20+%20Antigravity/soar/sync_cortex_cases.py)
*Sincronizador y verificador de casos Cortex XDR en Stellar Cyber.*

#### Parámetros soportados:
- `--dry-run`: Simula la ejecución mostrando qué casos se crearían y qué alertas se vincularían sin hacer modificaciones en el entorno de producción.
- `--month YYYY-MM`: Filtra exclusivamente las alertas correspondientes a un mes (ej. `--month 2026-10`).
- `--limit N`: Procesa hasta `N` casos más recientes.
- `--tenant ID`: Permite cambiar el ID de Tenant (por defecto usa `e511c3fc54cd4d668bb67612c2ef4b04` de `.env`).

#### Comandos de uso rápido:
```bash
# 1. Auditar en seco los casos de octubre
python sync_cortex_cases.py --month 2026-10 --dry-run

# 2. Sincronizar y crear casos faltantes de octubre en producción
python sync_cortex_cases.py --month 2026-10

# 3. Sincronizar los 5 casos más recientes de todo el historial
python sync_cortex_cases.py --limit 5
```

---

### Script B: [`close_cases_bulk.py`](file:///g:/Hermes%20+%20Antigravity/soar/close_cases_bulk.py)
*Herramienta de remediación y cierre masivo de casos en Stellar Cyber.*

#### Parámetros soportados:
- `--resolution`: Resolución formal obligatoria. Opciones válidas en la API de Stellar Cyber:
  - `"Benign"` (Actividad autorizada o utilitarios corporativos).
  - `"False Positive"` (Falsas alarmas de scripts o telemetría interna).
  - `"True Positive"` (Amenaza confirmada remediada).
- `--reason`: Justificación técnica o forense del cierre.
- `--cortex-cases`: Lista de IDs de casos de Cortex separados por comas (ej. `610,604,601`).
- `--stellar-cases`: Lista de Object IDs nativos de Stellar Cyber (ej. `6ad37e84e4fb8b7307d83837`).
- `--month`: Cierra todos los casos correspondientes a un mes determinado (ej. `2026-10`).
- `--dry-run`: Simula el cierre sin impactar en producción.

#### Comandos de uso rápido:
```bash
# 1. Simular cierre de casos específicos de Cortex
python close_cases_bulk.py --cortex-cases 610,604 --resolution "Benign" --dry-run

# 2. Cerrar casos por IDs de Cortex con dictamen
python close_cases_bulk.py --cortex-cases 599,596,586 --resolution "False Positive" --reason "Notificación WAU-Notify.ps1 legítima de Windows Update"

# 3. Cerrar masivamente todos los casos de un mes completo
python close_cases_bulk.py --month 2026-10 --resolution "Benign" --reason "Actividad administrativa benigna revisada por SOC"
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

## 4. Auditoría de Casos Procesados (Octubre 2026)

| Cortex ID | Stellar Ticket | Stellar ID | Endpoint | Amenaza | Resolución Aplicada |
|---|---|---|---|---|---|
| **610** | #17830 | `6ad2370de4fb8b7307d83193` | `NB-EORLANDINI` | curl hacia bacn.gov.py | **Resolved / Benign** |
| **604** | #17861 | `6ad37d44e4fb8b7307d8381a` | `NB-JTORALES` | Powershell Activity System PID 4 | **Resolved / False Positive** |
| **601** | #17862 | `6ad37e7ee4fb8b7307d83831` | `NB-GMARTINEZ` | LightscreenPortable.paf.exe | **Resolved / Benign** |
| **599** | #17863 | `6ad37e81e4fb8b7307d83834` | `NB-FBENEGAS` | WAU-Notify.ps1 conhost spawn | **Resolved / False Positive** |
| **597** | #17864 | `6ad37e84e4fb8b7307d83837` | Varios (7 hosts) | Start-BitsTransfer TeamsSetup | **Resolved / Benign** |
| **596** | #17865 | `6ad37e86e4fb8b7307d8383a` | `NB-RBARRETO` | WAU-Notify.ps1 | **Resolved / False Positive** |
| **595** | #17866 | `6ad37e88e4fb8b7307d8383d` | `NB-NOC2` | winget upgrade --all | **Resolved / Benign** |
| **594** | #17867 | `6ad37e8ae4fb8b7307d83840` | `NB-EORLANDINI` | curl descarga huggingface model | **Resolved / Benign** |
| **593** | #17868 | `6ad37e8ce4fb8b7307d83843` | `NB-FBENEGAS` | winget upgrade VLC | **Resolved / Benign** |
| **588** | #17869 | `6ad37e8fe4fb8b7307d83846` | `NB-IMAYOR` | WAU-Notify.ps1 | **Resolved / False Positive** |
| **586** | #17870 | `6ad37e92e4fb8b7307d83849` | `NB-FBENEGAS` | WAU-Notify.ps1 | **Resolved / False Positive** |
