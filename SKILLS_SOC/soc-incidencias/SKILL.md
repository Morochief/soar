---
name: soc-incidencias
description: Genera el registro formal de 40 columnas para el formulario oficial FL-THN-POS-01 Rev. 03 (Registro de Incidencias de Seguridad) en formato TSV de 1-clic y tabla estructurada concisa sin verbosidad.
risk: low
source: workspace
date_added: '2026-10-07'
---

# Skill: Registro Oficial de Incidencias SOC (Formato FL-THN-POS-01 - 40 Columnas)

Esta skill se activa cuando el analista necesita documentar formalmente un incidente de seguridad en el formulario maestro institucional:
📁 `Analista SOC/FL-THN-POS-01 Rev. 03 Registro de Incidencias de Seguridad (1) (1).xlsx`

---

## 🎯 Comando Principal y Palabras de Invocación / Triggers

El comando canónico para llamar a este formato es:

* **`/incidencia`** o **`/incidente`**
* Triggers alternativos: `/fl-thn`, `/pos-01`, `registrar incidencia`, `registro de incidencia`

> 💡 **Diferenciación Operativa en el SOC:**
> * `/bitacora` o `/turno` ➔ Llama al formato diario de **18 columnas** (Turnos, salud de ingesta, despliegues y triaje rápido).
> * `/incidencia` o `/incidente` ➔ Llama al formato oficial de **40 columnas** (`FL-THN-POS-01 Rev. 03` para gestión formal de incidentes de seguridad, cálculo de SLA P1-P4 y auditoría).

---

## 📋 Reglas de Redacción: Síntesis Estricta (Anti-Verbosidad)

1. **Brevedad por celda:** Máximo 1 o 2 oraciones concisas y directas para los campos de texto (`R`, `AC`, `AD`).
2. **Sin sobre-explicación teórica:** Redactar solo los hechos operacionales verificados (hora, causa confirmada, acción ejecutada y estado final).
3. **Fórmulas automáticas de Excel:** Las columnas **K** (Prioridad), **Z** (Tiempo notificación), **AE** (Tiempo resolución) y **AF** (Cumplió SLA) deben dejarse vacías en el bloque TSV para que la plantilla de Excel conserve sus fórmulas matriciales nativas.

---

## 📊 Estructura de las 40 Columnas (A a AN)

| Col | Encabezado Oficial | Tipo / Valores Válidos (Hoja PARAMETROS) |
| :-: | :--- | :--- |
| **A** | Número de ticket | ID de ticket en Odoo / Stellar Cyber / Cortex |
| **B** | Fecha apertura | Formato `DD/MM/AAAA` |
| **C** | Hora apertura | Formato `HH:mm:ss` |
| **D** | Tipo de Incidente | Breve título descriptivo del incidente |
| **E** | Notificado por | `Stellar Cyber`, `Cortex XDR`, `NOC`, `Oddo`, `Cliente`, etc. |
| **F** | Clasificación | `Disponibilidad`, `Intento de intrusión`, `Fraude`, `Contenido dañino`, `Intrusión`, `Compromiso de la información`, `Obtención de información`, `Vulnerable`, `APT`, `Otros` |
| **G** | Estado | `Nuevo`, `En investigación`, `En análisis`, `En respuesta`, `Escalado`, `Resuelto`, `Cerrado`, `Cancelado` |
| **H** | Impacto | `Alto`, `Medio`, `Bajo` |
| **I** | Urgencia | `Alta`, `Media`, `Baja` |
| **J** | Criticidad | `Alta`, `Media`, `Baja` |
| **K** | Prioridad | *Fórmula automática de Excel* (`P1`, `P2`, `P3`, `P4`) |
| **L** | Origen del Incidente | Activo o componente causante |
| **M** | Alcance | `N/A` o alcance específico |
| **N** | Objetivos | `N/A` |
| **O** | Responsable | `N/A` o asignado |
| **P** | Partes intervinientes | `N/A` o áreas participantes |
| **Q** | Recursos involucrados | Hostnames, IDs de sensores, IPs perimetrales o de gateway |
| **R** | Actividades a desarrollar | 1 o 2 oraciones con las tareas ejecutadas / validaciones con NOC o cliente |
| **S** | ¿Requiere escalamiento? | `Sí`, `No` |
| **T** | Nivel de escalamiento | `N1 - Mesa de servicio SOC (L1)`, `N2 - Analista de seguridad (L2_Queue)`, `N3 - Proveedor / Externo`, o `None` / `N/A` |
| **U** | Escalado a | Rol / Área o `N/A` |
| **V** | Fecha y hora escalamiento | `N/A` o fecha y hora |
| **W** | Motivo escalamiento | `N/A` |
| **X** | Fecha notificación cliente | Formato `DD/MM/AAAA` |
| **Y** | Hora notificación | Formato `HH:mm:ss` |
| **Z** | Tiempo notificación (h) | *Fórmula automática de Excel* |
| **AA**| Fecha resolución | Formato `DD/MM/AAAA` |
| **AB**| Hora resolución | Formato `HH:mm:ss` |
| **AC**| Causa raíz | 1 oración clara con el origen del problema (corte de enlace, fallo de energía, etc.) |
| **AD**| Solución aplicada | 1 o 2 oraciones con la normalización técnica y duración del corte |
| **AE**| Tiempo resolución (h) | *Fórmula automática de Excel* |
| **AF**| ¿Cumplió SLA? | *Fórmula automática de Excel* (`Sí` / `No`) |
| **AG**| Fecha Cierre | Formato `DD/MM/AAAA` |
| **AH**| Hora cierre | Formato `HH:mm:ss` |
| **AI**| Criterio de cierre | Condición técnica de verificación (ej. `Sensor y agente conectados y enviando telemetría normal`) |
| **AJ**| Conformidad del usuario | `Conforme`, `No conforme`, `Pendiente` |
| **AK**| Cerrado por | Nombre del Analista SOC (ej. `Kevin Moraes`) |
| **AL**| Lecciones Aprendidas | `N/A` |
| **AM**| Responsable Resolución | Nombre del Analista SOC (ej. `Kevin Moraes`) |
| **AN**| Observación | `N/A` |

---

## ⚡ Formato de Salida Obligatorio

Cada vez que el analista use `/incidencia` o `/incidente`, la respuesta debe presentar:
1. **Resumen ejecutivo conciso:** Tabla de parámetros clave (Ticket, Activos, Causa Raíz, Tiempos y SLA).
2. **Bloque TSV de 1-clic para Excel:** Línea cruda separada por tabuladores (`\t`) con saltos o comillas protegidas por comillas dobles `"..."` y con las columnas de fórmulas vacías para pegado directo en la fila correspondiente.
