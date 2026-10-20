# 📄 FÓRMULAS Y FUNCIONES CON NOMBRE DE GOOGLE SHEETS / EXCEL (SOC TECHNOMA)

> **CLASIFICACIÓN:** USO INTERNO SOC TECHNOMA — BASE DE CONOCIMIENTO  
> **ÁREA:** Automatización de Hojas de Cálculo / Generación de Tarjetas de Ticket  
> **DOCUMENTO:** `Formulas_Funciones_GoogleSheets_SOC.md`  
> **REFERENCIA OFICIAL:** [`Analista SOC/Bitácora de Eventos - 2026-10 Octubre.xlsx`](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Bit%C3%A1cora%20de%20Eventos%20-%202026-10%20Octubre.xlsx) (Hojas `TICKET_GENERADO` y `VISTA_TICKET_MANUAL`)  

---

## 1. Arquitectura de la Hoja `TICKET_GENERADO`

La hoja `TICKET_GENERADO` actúa como un **renderizador dinámico** que detecta automáticamente el último evento del día en el que se haya marcado `Generó Ticket = "SI"` (en la columna `P`), trayendo de forma instantánea todos los campos para generar la tarjeta gráfica visual del ticket.

---

## 2. Fórmulas Maestras de la Hoja `TICKET_GENERADO`

### 1. Fecha Dinámica de la Pestaña Activa (Celda `B1`)
Genera la fecha actual con el formato exacto del nombre de las pestañas diarias (ej. `18-10-2026`):
```excel
=TEXT(TODAY(), "dd-mm-yyyy")
```

---

### 2. Detección Automática de la Última Fila con Ticket "SI" (Celda `B4`)
Escanea en la pestaña del día (`B1`) la columna `P` (donde se marca si genera ticket) y calcula dinámicamente el **número máximo de fila** que contenga `^SI`:
```excel
=IFERROR(MAX(FILTER(ROW(INDIRECT("'" & TEXT(B1, "dd-mm-yyyy") & "'!P:P")), REGEXMATCH(TO_TEXT(INDIRECT("'" & TEXT(B1, "dd-mm-yyyy") & "'!P:P")), "^SI"))), 3)
```
> **Nota de compatibilidad:** Si no hay ningún ticket marcado con `"SI"`, retorna por defecto la fila `3`.

---

### 3. Código y Número de Ticket (Celda `D5`)
Concatena el prefijo oficial con el número de ticket ubicado en la columna `F` de la fila calculada en `B4`:
```excel
="THN-SOC-" & INDIRECT("'" & $B$1 & "'!F" & $B$4)
```

---

### 4. Prioridad con Emoticono Condicional (Celda `E6`)
Extrae la prioridad de la columna `G` y le añade un indicador visual `🔴` si es Alta o Crítica:
```excel
=IFERROR(INDIRECT("'" & $B$1 & "'!G" & $B$4) & IF(REGEXMATCH(INDIRECT("'" & $B$1 & "'!G" & $B$4), "(?i)Alta|Critica"), " 🔴", ""), "Informativo")
```

---

### 5. Campos Dinámicos del Incidente (Celdas `E7` a `E11`)

| Celda | Etiqueta | Fórmula Maestra (Google Sheets) | Columna Origen en Pestaña Diaria |
| :---: | :--- | :--- | :---: |
| **`E7`** | **Asunto** | `=INDIRECT("'" & $B$1 & "'!I" & $B$4)` | Columna **I** (Asunto / Título) |
| **`E8`** | **Descripción** | `=INDIRECT("'" & $B$1 & "'!K" & $B$4)` | Columna **K** (Descripción y Causa Raíz) |
| **`E9`** | **Activos** | `=INDIRECT("'" & $B$1 & "'!J" & $B$4)` | Columna **J** (Activos / Host / IP / Usuario) |
| **`E10`** | **Evidencia** | `=INDIRECT("'" & $B$1 & "'!L" & $B$4)` | Columna **L** (Evidencia Técnica / Hashes) |
| **`E11`** | **Solicitud de Acción** | `=INDIRECT("'" & $B$1 & "'!M" & $B$4)` | Columna **M** (Recomendación / Cierre) |

---

## 3. Función con Nombre: `GENERAR_TICKET_SOC` (Google Sheets)

Para generar la tarjeta completa en una sola celda como bloque de texto con saltos de línea (`CARACTER(10)`):

### 📌 Parámetros de la Función con Nombre:
* **Nombre:** `GENERAR_TICKET_SOC`
* **Descripción:** `Genera la tarjeta de ticket formateada del SOC a partir de las columnas de la bitácora si P4 es SI, o N/A si no requiere ticket.`
* **Argumentos:** `generar_ticket, ticket_id, prioridad, descripcion, activos, evidencia, solicitud_accion`

```excel
=SI(generar_ticket="SI"; "THN-SOC-" & ticket_id & CARACTER(10) & "PRIORIDAD: " & prioridad & CARACTER(10) & "----------------------------------------------------------------" & CARACTER(10) & "DESCRIPCIÓN DEL EVENTO:" & CARACTER(10) & descripcion & CARACTER(10) & CARACTER(10) & "ACTIVOS:" & CARACTER(10) & activos & CARACTER(10) & CARACTER(10) & "EVIDENCIA:" & CARACTER(10) & evidencia & CARACTER(10) & CARACTER(10) & "SOLICITUD DE ACCIÓN:" & CARACTER(10) & solicitud_accion; "N/A")
```

#### Uso Directo en Hoja Diaria (Fila por Fila):
```excel
=SI(P5="SI"; "THN-SOC-" & F5 & CARACTER(10) & "PRIORIDAD: " & G5 & CARACTER(10) & "----------------------------------------------------------------" & CARACTER(10) & "DESCRIPCIÓN DEL EVENTO:" & CARACTER(10) & I5 & CARACTER(10) & CARACTER(10) & "ACTIVOS:" & CARACTER(10) & J5 & CARACTER(10) & CARACTER(10) & "EVIDENCIA:" & CARACTER(10) & L5 & CARACTER(10) & CARACTER(10) & "SOLICITUD DE ACCIÓN:" & CARACTER(10) & M5; "N/A")
```
