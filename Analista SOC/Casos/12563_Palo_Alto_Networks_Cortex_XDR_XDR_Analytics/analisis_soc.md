### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `XDR Analytics`, `LOLBIN`, `DLL Hijacking`, `False Positive`, `Palo Alto Cortex XDR`.

### Análisis Eventos 1, 2 y 3 (Lote Agrupado por Actividad de Instalación)
*Nota del analista: Los tres eventos documentan una cadena de procesos originada por la instalación del software NanoCAD en el equipo del usuario.*

### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Host IP:** `192.168.169.50`
* **Hostname:** `NB-ALPIZZUTI`
* **User Name:** `TECHNOMA\alfredopizzuti`
* **Threat Names:** `An uncommon LOLBIN added to startup-related Registry keys` y `A rare DLL, signed by a rarely seen vendor, was hijacked into a Microsoft process`.
* **Description:** Palo Alto Networks Cortex XDR Analytics BIOC detectó modificaciones inusuales en el registro (RunOnce) y la carga de DLLs raras (`MSI3A1E.tmp` y `MSI6D3B.tmp`) por parte del instalador de Windows (`msiexec.exe`) y el instalador `.NET Desktop Runtime` (`windowsdesktop-runtime-6.0.11-win-x64.exe`).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Observación Forense |
| :--- | :--- | :--- | :--- |
| 2026-07-23T16:05:27Z | N/A | Ejecución de Proceso 1 | `nci_x64_26.0_7476.4950.305.exe` lanza `windowsdesktop-runtime-6.0.11-win-x64.exe`, que a su vez registra una clave en `RunOnce`. |
| 2026-07-23T16:11:39Z | N/A | Carga de DLL (1) | `msiexec.exe` carga la librería temporal `MSI3A1E.tmp` firmada por CSOFT AS. |
| 2026-07-23T16:12:57Z | N/A | Carga de DLL (2) | `msiexec.exe` carga la librería temporal `MSI6D3B.tmp` firmada por OOO Nanosoft Razrabotka. |

### 🔬 Desglose Técnico y Disección Forense
* El motor BIOC de Cortex XDR identificó un comportamiento anómalo. La actividad raíz fue iniciada por `nci_x64_26.0_7476.4950.305.exe`, que es el instalador del software **NanoCAD** (un software de diseño CAD legítimo desarrollado por Nanosoft).
* Durante la instalación, NanoCAD despliega dependencias como el `.NET Desktop Runtime 6.0`. Este instalador registra una clave de registro `RunOnce` con el parámetro `/burn.runonce` para continuar la configuración tras un posible reinicio. El motor Analytics lo marcó como *"Uncommon LOLBIN added to startup"*.
* Posteriormente, el instalador MSI nativo de Windows (`msiexec.exe`) desempaquetó DLLs temporales (`.tmp`) necesarias para el asistente de instalación. Estas DLLs temporales están firmadas por los desarrolladores de NanoCAD ("CSOFT AS" y "OOO Nanosoft Razrabotka").
* Como este software (NanoCAD) no es común en toda la flota de la empresa (o es la primera vez que se instala en el mes), el motor de Analytics clasifica estas firmas y hashes como "raros", disparando la alerta heurística de posible DLL Hijacking.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de Comportamiento (Instalación de Software Legítimo)**.
Toda la actividad detectada es el comportamiento esperado de un instalador MSI de Windows (NanoCAD) al desempaquetar archivos temporales y configurar dependencias `.NET`. Las librerías están firmadas digitalmente por sus proveedores de software. No hay evidencia de escalamiento de privilegios malicioso ni secuestro real de DLLs.

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta.",
  "Integridad": "Intacta. (Modificaciones esperadas por instalador)",
  "Disponibilidad": "Intacta."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo de Ataque (Instalador NanoCAD)",
  "Confianza": "100%",
  "Justificacion": "Los procesos, llaves de registro y DLLs reportados corresponden a la instalación legítima de NanoCAD y el runtime de .NET. Las detecciones de BIOC se deben a la rareza del software en el entorno, no a un comportamiento malicioso."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Se correlacionó el árbol de procesos, confirmando que la raíz es un instalador legítimo y firmado (`nci_x64...exe`). Se descarta la hipótesis de DLL Hijacking o persistencia maliciosa. |
| Erradicación y Recuperación | N/A. |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-FP-01 | Falsos Positivos Analíticos/Heurísticos | Aplicable a detecciones de BIOC por rareza de instaladores no estándar. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Actividad de instalación de software autorizado (NanoCAD).

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-23 16:05 | Antigravity | technoma | 12563 | palo_alto_cortex_xdr | N/A | Low | Analytics BIOC | FP Instalación NanoCAD (RunOnce y DLLs) | 192.168.169.50 (NB-ALPIZZUTI) | El motor BIOC de Cortex alertó sobre modificaciones RunOnce y carga de DLLs raras por parte de msiexec.exe. El análisis confirmó que la actividad proviene del instalador nci_x64_26.0_7476.4950.305.exe (NanoCAD). Las DLL temporales están firmadas por Nanosoft/CSOFT. Falso positivo heurístico por instalación de software. | Árbol de procesos y Firmas Digitales | Ninguna. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
Falso Positivo de Heurística Analítica (BIOC). Las tres alertas agrupadas para el host `NB-ALPIZZUTI` corresponden a la instalación legítima del software de diseño NanoCAD por parte del usuario `alfredopizzuti`. El ejecutable principal (`nci_x64_26.0_7476.4950.305.exe`) despliega el instalador de `.NET Desktop Runtime` que genera una entrada legítima en `RunOnce` para continuar el proceso post-reinicio. Adicionalmente, el instalador de Windows (`msiexec.exe`) desempaqueta DLLs temporales necesarias firmadas digitalmente por Nanosoft y CSOFT. Cortex XDR generó las alertas de "Uncommon LOLBIN" y "DLL Hijacking" basándose únicamente en la rareza estadística de estos binarios en nuestro entorno durante los últimos 30 días, no por tratarse de un ataque real. Actividad benigna confirmada. Se procede al cierre.
