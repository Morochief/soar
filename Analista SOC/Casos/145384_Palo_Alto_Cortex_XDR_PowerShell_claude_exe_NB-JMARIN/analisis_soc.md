# Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR / Palo Alto Cortex XDR

## 1. Identificación del Caso
- **ID de Caso:** `145384_Palo_Alto_Cortex_XDR_PowerShell_claude_exe_NB-JMARIN`
- **ID de Secuencia Stellar:** 19386, 19385, 19410, 19796, 19806
- **Cortex Alert IDs:** 145384, 145386, 145388, 145404, 145406
- **Tenant:** Technoma (`cf73a415c8794884a0c35b458b7c73ae`)
- **Regla Detectada:** `PowerShell runs suspicious base64-encoded commands` (Rule: `5daf5724-8e0a-4514-85d4-431bf4b193be`, BIOC Analytics)
- **Táctica / Técnica:** Execution (`TA0002`) / Command and Scripting Interpreter: PowerShell (`T1059.001`)
- **Fecha y Hora de Detección:** 24/09/2026 entre 14:34:08 y 16:06:37 UTC (11:34:08 a 13:06:37 Local)
- **Analista Responsable:** Kevin Moraes
- **Veredicto Técnico:** Falso Positivo (Actividad Legítima de Desarrollo / Herramienta Claude Code CLI de Anthropic)

---

## 2. Descripción y Actores Involucrados
| Parámetro | Detalle de Proceso Padre (Actor) | Detalle de Proceso Hijo (Acción) |
| :--- | :--- | :--- |
| **Proceso / Binario** | `claude.exe` (v2.1.280) | `powershell.exe` |
| **Ruta del Ejecutable** | `C:\Users\josemarin\AppData\Roaming\Claude\claude-code\2.1.280\claude.exe` | `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe` |
| **Firma Digital** | Válida (`Signed` - Anthropic, PBC) | Válida (`Signed` - Microsoft Corporation) |
| **Línea de Comandos** | Ejecución de sesión interactiva de desarrollo con MCPs | `-NoProfile -NonInteractive -NoLogo -EncodedCommand <Base64>` |
| **Host y Usuario** | `NB-JMARIN` (`192.168.169.69`) | `TECHNOMA\josemarin` |

---

## 3. Análisis de Causa Raíz
Se identificaron 5 alertas correlacionadas de Palo Alto Networks Cortex XDR BIOC ingestadas en Stellar Cyber. El motor analítico de Cortex XDR disparó la regla de comportamiento debido a que el proceso `claude.exe` ejecutó instancias de `powershell.exe` empleando comandos codificados en Base64 (`-EncodedCommand`).

La inspección forense del payload y la cadena de procesos revela lo siguiente:
1. **Legitimidad del Binario:** El proceso invocador corresponde a la herramienta de asistencia técnica y desarrollo Claude Code CLI, debidamente firmada por Anthropic PBC y ejecutada en el espacio de usuario del desarrollador `josemarin`.
2. **Naturaleza del Script Ejecutado:** La carga útil codificada en Base64 contiene rutinas estándar de validación sintáctica de PowerShell basadas en el analizador de lenguaje de Windows (`[System.Management.Automation.Language.Parser]::ParseInput`). Claude Code utiliza este mecanismo para parsear el árbol sintáctico abstracto (AST) de comandos de terminal antes de su ejecución, previniendo errores de escape y validando estructuras de comandos.
3. **Ausencia de Malicia:** No se observaron descargas externas anómalas, inyección de memoria, técnicas de persistencia ni comunicaciones C2. La detección responde exclusivamente a la heurística de seguridad que vigila la ejecución de PowerShell con comandos codificados.

---

## 4. Evaluación de Impacto (Triada CIA)
- **Confidencialidad:** 0/10 (Sin exfiltración ni acceso no autorizado a datos corporativos).
- **Integridad:** 0/10 (Sin alteración de archivos críticos del sistema ni configuraciones de seguridad).
- **Disponibilidad:** 0/10 (Estación de trabajo y servicios operando nominalmente).
- **Puntuación Global de Riesgo:** **0.0 / 10 (Insignificante / Falso Positivo)**.

---

## 5. Cierre en Plataforma Stellar Cyber
- **Estado:** `Closed`
- **Resolution Tag:** `False Positive`
- **Comentario de Cierre Condensado:**
> Cierre por Falso Positivo: Las 5 alertas de Cortex XDR (IDs 145384, 145386, 145388, 145404 y 145406) sobre NB-JMARIN (192.168.169.69, TECHNOMA\josemarin) corresponden a la ejecución legítima de la herramienta de desarrollo Claude Code de Anthropic PBC (claude.exe, firmado), la cual ejecuta powershell.exe con el argumento -EncodedCommand para la validación sintáctica mediante AST de instrucciones en el entorno local del desarrollador, descartándose cualquier actividad adversaria o vulneración de seguridad.
