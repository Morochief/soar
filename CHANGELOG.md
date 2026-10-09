# Registro de Cambios y Control de Versiones (CHANGELOG)
Todas las modificaciones notables realizadas en la plataforma **STELLAR CYBER OpenXDR - CENTRAL COMMAND MASTER COCKPIT** se documentan formalmente en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [6.5.1s] - 2026-09-25

### 🎯 Resumen Ejecutivo de la Versión
Esta versión introduce la alineación contractual total del motor de gobernanza SLA/SLO con la norma **TB-THN-POS-01 Rev. 01** (`PARAMETROS.html`), resuelve el bug de cálculo e interpretación de MTTR/MTTD en casos recién generados, añade la matriz de priorización 3x3 (Impacto $\times$ Urgencia), moderniza el módulo interactivo de Threat Feeds CTI con visor nativo de artículos, y elimina los bloqueos de tamaño fijo en ventanas emergentes de análisis forense.

---

### 🛡️ Gobernanza SLA / SLO y Motores de Triaje (`command_center.py`)

#### Añadido
* **Matriz de Priorización 3x3 (`SlaGovernanceEngine.calculate_priority_matrix`):**  
  Implementación formal de la tabla contractual de doble entrada Impacto $\times$ Urgencia definida en la Sección 1 de `PARAMETROS.html`:
  * `Alto x Alta` $\rightarrow$ **P1**
  * `Alto x Media` / `Medio x Alta` $\rightarrow$ **P2**
  * `Alto x Baja` / `Medio x Media` / `Bajo x Alta` $\rightarrow$ **P3**
  * `Medio x Baja` / `Bajo x Media` / `Bajo x Baja` $\rightarrow$ **P4**
* **Mapeo Híbrido de Prioridad en Casos:**  
  `SlaGovernanceEngine.get_priority(case)` ahora evalúa prioritariamente los campos explícitos de `impacto` y `urgencia` si están presentes en el caso.
* **Trazabilidad Completa en Alertas de Vencimiento:**  
  El estado visual de la tabla y del banner de triaje ahora desglosa simultáneamente:
  1. El tiempo exacto de exceso sobre el SLA (`remaining_str`, ej: `+2m 15s`).
  2. La edad total de vida del ticket (`elapsed_str`, ej: `Total: 1h 02m`).

#### Modificado / Corregido
* **Corrección del Vencimiento Falso de 1 Hora en MTTR (Bug Crítico):**  
  * **Causa Raíz Identificada:** La función `_render_cases_view` formateaba la celda como `f"MTTR VENCIDO (+{mttr_info['elapsed_str']})"`. Al anteponer el signo `+` a la duración total acumulada del caso (`1h 02m`), el operador leía que el caso ya llevaba *vencido* más de una hora, cuando en realidad el retraso real sobre el límite de 1h eran solo 2 minutos.
  * **Solución Aplicada:** Se sustituyó el formato por `f"MTTR VENCIDO ({mttr_info['remaining_str']} | Total: {mttr_info['elapsed_str']})"`. Idéntico ajuste de claridad se implementó en `MTTD VENCIDO` y en el banner superior de `launch_triage_action`.
* **Calibración de Score Numérico vs Severidad Textual de Stellar Cyber:**  
  * En la API en vivo de Stellar Cyber, alertas con score numérico de **79.2** recibían la etiqueta textual `"Critical"` por reglas genéricas de conectores externos. El SOAR forzaba estos casos a **P1 (MTTR: 1 hora)**.
  * Se recalibró `get_priority` para que cualquier caso con score numérico positivo respete estrictamente los rangos de `PARAMETROS.html` (75–89 pertenece a **P2 - Alta**, otorgando un MTTR contractual de **4 horas**). La severidad textual solo actúa como respaldo cuando el score numérico es 0.
* **Alineación Contractual de Prioridad P4:**  
  * Umbrales de P4 actualizados de 24h / 72h a **168 horas (7 días)** en `P4_MTTD_MS` y `P4_MTTR_MS`, cumpliendo la directiva de *«mejor esfuerzo / revisión semanal»* estipulada en la nota de `PARAMETROS.html`.
* **Fix de Crash por `KeyError: 'remaining_sec'`:**  
  En el ordenamiento de la tabla por `Orden: Urgencia SLA`, se corrigió una llamada a la clave inexistente `remaining_sec` por `mttd.get("remaining_ms", 0) / 1000.0`.

---

### 🌐 Módulo de Inteligencia de Amenazas (`feeds_intel_module.py`)

#### Añadido
* **Ventana Dinámica Redimensionable:**  
  Sustitución de dimensiones fijas por un contenedor inteligente con `QSplitter` proporcional, `setSizeGripEnabled(True)` y soporte completo de maximización de pantalla para monitores de alta resolución SOC (1080p / 2K / 4K).
* **Lector Nativo de Noticias / Artículos en la Consola SOAR:**  
  Incorporación de un visor lateral con `QTextBrowser`, renderizado de tipografía ejecutiva, badges de severidad, fecha, autor y enlace externo seguro con `QDesktopServices`. Permite al analista evaluar de inmediato si una noticia amerita análisis o hunting sin abandonar la aplicación.
* **Monitor de Salud y Actividad de Fuentes CTI:**  
  Diagnóstico automático de las 10 fuentes RSS (CISA, BleepingComputer, TheHackerNews, CERT-PY, SANS ISC, etc.) que detecta si el feed continúa activo o si presenta estancamiento temporal en sus publicaciones.
* **Filtros Temporales y Ordenamiento Multicriterio:**  
  Selectores en tiempo real para filtrar noticias por antigüedad (**Últimas 24h**, **7 días**, **30 días**, **90 días**, **Todo el historial**) y ordenamiento cruzado por fecha o por criticidad de la amenaza.

---

### 🎨 Interfaz de Usuario y Herramientas Auxiliares

#### Modificado / Corregido
* **Corrección de Contraste en Menús Desplegables (`command_center.py`):**  
  Solución al bug visual de letras oscuras ilegibles sobre fondo oscuro en los menús contextuales del cockpit (`QMenu`). Se estandarizó el tema oscuro con tipografía en `#f8fafc`, fondo `#1e293b`, borde `#334155` y resaltado violeta neón `#8b5cf6` en estado hover.
* **Redimensionamiento en Analizador de Cabeceras (`email_header_analyzer.py`):**  
  Habilitación de agarre de redimensionamiento (`setSizeGripEnabled(True)`), tamaño mínimo ergonómico de 900x650 px y distribución responsiva de tablas de saltos SPF/DKIM/DMARC.

---

### 📁 Archivos Modificados / Impactados

| Archivo | Tipo de Cambio | Descripción Principal |
| :--- | :---: | :--- |
| [`command_center.py`](file:///c:/Users/kevinmoraes/Documents/soc-env/command_center.py) | **Core / SLA** | Bump a v6.5.1s, calibración de prioridades P1-P4, matriz Impacto $\times$ Urgencia, fix MTTR display y corrección de menús. |
| [`feeds_intel_module.py`](file:///c:/Users/kevinmoraes/Documents/soc-env/feeds_intel_module.py) | **Módulo CTI** | Rediseño a layout redimensionable con splitters, lector in-app, diagnóstico de fuentes y filtros de fecha. |
| [`email_header_analyzer.py`](file:///c:/Users/kevinmoraes/Documents/soc-env/email_header_analyzer.py) | **Forense** | Habilitación de redimensionamiento dinámico y layouts elásticos. |
| [`PARAMETROS.html`](file:///c:/Users/kevinmoraes/Documents/soc-env/PARAMETROS.html) | **Referencia** | Matriz contractual de referencia validada y correlacionada. |

---

### 🧪 Verificación y Pruebas
* **Pruebas de Unidad Automáticas:** `test_feeds_engine.py` (6 pruebas OK), `test_feeds_ai.py` (7 pruebas OK).
* **Pruebas de Gobernanza SLA:** Verificación con casos reales de la API de Stellar Cyber (Tickets `#16211`, `#16209`, `#16208`, `#16205`, `#16184`).
* **Integridad de Código:** Sintaxis validada en Python 3.12 y PySide6 sin errores de importación.
