---
name: soc-bitacora
description: Genera instantáneamente el registro de 18 columnas para la Bitácora de Turno, Despliegues y Triaje SOC en formato TSV de 1-clic para Excel/Google Sheets con apoyo visual.
risk: low
source: workspace
date_added: '2026-09-20'
---

# Skill: Generador de Bitácora SOC (18 Columnas - 1 Clic TSV)

Esta skill se activa siempre que el analista desee documentar una actividad, cierre de turno, despliegue técnico o resolución de incidente en la Bitácora Oficial del SOC.

## 🎯 Palabras de Invocación / Triggers
Se activa automáticamente con cualquiera de las siguientes palabras o comandos:
- `/bitacora` o `/bitácora`
- `bitacora:` o `bitácora:`
- `/turno` o `cierre de turno`
- `registrar bitácora` o `anotar en bitácora`
- Ejemplos de uso rápido:
  - `/bitacora 18-09-2026 apoyo despliegue secops-vascol en Security Onion, apareció en el grid`
  - `/bitacora cierre turno mañana sin alertas en Technoma y Caja Ande`
  - `/bitacora falso positivo en Sophos WebControl para equipo PC-01`

---

## 📋 Estructura Estricta de las 18 Columnas (Excel / Google Sheets)

La hoja de cálculo del SOC requiere obligatoriamente estas 18 columnas separadas por tabuladores (`\t`):

| Columna | Encabezado Oficial | Descripción | Valor por Defecto / Ejemplo |
| :---: | :--- | :--- | :--- |
| **A (1)** | **Fecha y Hora** | Formato `D/M/AAAA HH:mm:ss` | Fecha actual o indicada por el analista |
| **B (2)** | **Analista** | Nombre del operador SOC | `Kevin Moraes` |
| **C (3)** | **Tenant** | Clientes involucrados | `Technoma`, `Caja Ande`, `Vascol`, etc. |
| **D (4)** | **ID del caso** | Identificador de alerta o caso | `N/A` o `#CASE-XXXX` |
| **E (5)** | **Fuente de Detección** | Plataforma o tipo de tarea | `Cierre de Turno`, `Despliegue de Sensor`, `Stellar Cyber`, `Security Onion`, `Sophos` |
| **F (6)** | **Nro. Ticket** | Ticket de soporte / ITSM | `N/A` o `#TICKET-123` |
| **G (7)** | **Prioridad** | Severidad operativa | `Informativo`, `Baja`, `Media`, `Alta`, `Crítica` |
| **H (8)** | **Tipo de evento** | Título breve de la actividad | `Cierre de Turno Mañana`, `Despliegue Inicial secops-vascol` |
| **I (9)** | **Asunto** | Título descriptivo completo | `Reporte de Cierre de Turno Mañana...` |
| **J (10)**| **Activos** | Servidores, endpoints o nodos | `Infraestructura general...` o `Nodo secops-vascol` |
| **K (11)**| **Descripción** | Narrativa técnica detallada | Entrecomillada `""` para soportar saltos de línea |
| **L (12)**| **Evidencia (Logs, etc.)** | Estado de consolas / resolución | Estado de consolas, filtros aplicados, resultado |
| **M (13)**| **Solicitud de Acción** | Acciones pendientes / escalado | `N/A` |
| **N (14)**| **Estado** | Estado del ticket/registro | `Cerrado`, `En Proceso`, `En Seguimiento` |
| **O (15)**| **URL** | Enlace al caso o telemetría | `N/A` |
| **P (16)**| **Generación de Ticket** | ¿Se abrió ticket de escalado? | `NO` o `SI` |
| **Q (17)**| **TICKET** | Enlace o código de ticket externo | `N/A` |
| **R (18)**| **Playbook** | Playbook SOC aplicado | `N/A`, `PB-1.1`, `PB-6.1`, etc. |

---

## 🔒 Regla Obligatoria para Cierres de Turno (Baseline Estándar)

Cada vez que el analista reporte un **Cierre de Turno**, se debe incorporar **OBLIGATORIAMENTE** como base el monitoreo estándar de consolas sobre los tenants fijos (`Caja Ande, Technoma`) y a ese bloque base **sumarle** todo lo que el analista indique que realizó durante la guardia.

### 1. Nomenclatura y Concatenación de Campos Base:
* **Tenant (Col C):** Siempre incluye `Caja Ande, Technoma` (si se trabajó en otros tenants como `VALORES`, `Vascol`, etc., se agregan: `Caja Ande, Technoma, VALORES`).
* **Fuente de Detección (Col E):** `Cierre de Turno`.
* **Tipo de Evento (Col H):** `Cierre de Turno Mañana` (06:00 a 14:00), `Cierre de Turno Tarde` (14:00 a 22:00) o `Cierre de Turno Noche` (22:00 a 06:00).
* **Asunto (Col I):** `Reporte de Cierre de Turno [Turno] - Technoma y Caja Ande` (+ otros clientes si hubo actividad específica).
* **Activos (Col J):** Siempre incluye `Infraestructura general Technoma / Endpoints y Servidores CAJA ANDE` (+ los activos específicos intervenidos, ej. sensores, firewalls, etc.).
* **Descripción (Col K) - Estructura Obligatoria:**
  Debe iniciar con el párrafo base de monitoreo y concatenar las actividades puntuales indicadas:
  ```text
  REPORTE SOC - TURNO [HH:mm a HH:mm]. Monitoreo continuo de consolas sobre Tenants Technoma y CAJA ANDE. Descarte de falsos positivos de rutina. Sin anomalías ni incidentes activos durante el periodo.

  [Novedades y tareas adicionales indicadas por el analista...]
  ```
* **Evidencia (Col L) - Estructura Obligatoria:**
  Debe iniciar con la verificación de consolas base y sumar las evidencias técnicas reportadas:
  ```text
  Stellar Cyber / Sophos: Consolas en estado VERDE sin alertas abiertas para Technoma y CAJA ANDE. Filtro de verificación [HH:mm-HH:mm] ejecutado con éxito (0 pendientes). [Evidencias de sensores, servicios, logs, etc.]
  ```
* **Solicitud de Acción (Col M):** `N/A` (o la solicitud pendiente indicada).
* **Estado (Col N):** `Cerrado` (o `En Seguimiento` si quedó un pendiente operativo).
* **Generación de Ticket (Col P):** `NO`.
* **TICKET (Col Q):** `N/A`.
* **Playbook (Col R):** `N/A` (o playbook específico si aplicó).

### 2. Control Diario de Ingesta y Licencias (Stellar Cyber / SIEM):
Como buena práctica operativa ante auditorías y reclamos de jefatura, cada vez que el analista reporte datos de consumo o cierre de guardia, se debe incluir un renglón sintético en **Descripción (Col K)** y **Evidencia (Col L)**:
* **Formato Sintético:**
  `CONTROL DE INGESTA STELLAR: Technoma: [X] GB (Límite [Y] GB) | CAJA ANDE: [X] GB (Límite [Y] GB) | Valores: [X] GB | Pozo Global: [Consumo] GB / [Límite] GB ([%] - [ESTADO]).`
* **Criterio de Alerta:** Si algún tenant o el pozo global supera el 100%, marcarlo explícitamente con `⚠️ ALERTA EXCESO DE CUOTA` o `🔴 POZO DESBORDADO` para que quede constancia fehaciente en la bitácora y deslinde al analista de omisión de reporte.

---

## ⚡ Reglas de Generación y Salida

Cada vez que se invoque la skill, la respuesta debe contener obligatoriamente **DOS BLOQUES**:

### Bloque 1: Apoyo Visual Desglosado (Tabla Markdown)
Una tabla limpia que muestre la correspondencia de las columnas **A a R** y tarjetas legibles con los textos largos de las columnas **K (Descripción)** y **L (Evidencia/Resolución)** para que el analista pueda validar la redacción técnica.

### Bloque 2: Bloque de Código TSV (1 Clic para Copiar y Pegar)
Un bloque de código etiquetado como ````tsv```` que contenga la línea cruda con campos delimitados exactamente por tabuladores (`\t`).
* **Regla de oro de Excel:** Si la columna K o L contiene saltos de línea o comillas, el contenido debe estar envuelto en comillas dobles `"..."` para que Excel lo pegue dentro de una sola celda sin desfasar las filas ni las columnas.
