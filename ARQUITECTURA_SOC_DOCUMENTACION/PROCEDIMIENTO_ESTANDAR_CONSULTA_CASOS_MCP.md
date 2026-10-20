# 📖 LECCIÓN APRENDIDA Y PROCEDIMIENTO ESTÁNDAR: CONSULTA DE CASOS VÍA MCP STELLAR CYBER

> **Fecha de Incidencia**: 16 de Octubre de 2026  
> **Contexto**: Consulta y cierre masivo de casos en vivo en Stellar Cyber 6.5.1s/7.0.0s.  
> **Capa RAG**: `PROCEDIMIENTO_ARQ` / `MEMORIA_SOC`  
> **Objetivo**: Evitar fallos de consulta, errores de encoding Unicode en Windows y bifurcaciones innecesarias a endpoints REST no estándar.

---

## ❌ 1. Errores Cometidos y Lecciones Técnicas

1. **Error de Tipo de Identificador (Ticket ID numérico vs Hex ID de MongoDB)**:
   - *Fallo*: Al consultar `getCaseDetail` o `/connect/api/v1/cases/{id}` pasando el Ticket ID visible del analista (ej. `17850`), Stellar Cyber rechazaba la petición con `Validation Failed: Invalid id`.
   - *Causa raíz*: El endpoint `getCaseDetail` del servidor MCP requiere estrictamente el identificador Hexadecimal de MongoDB de 24 caracteres (`_id`, ej. `6ad283d8a9a3e2ee2767154b`), mientras que el número de 5 dígitos (`ticket_id`: `17850`) es solo el alias visual del analista.
   - *Solución implementada*: El script [`stellar_case_fetcher.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_case_fetcher.py) implementa `resolve_case_hex_id()` que traduce automáticamente cualquier `#17850` a su `_id` hexadecimal sin intervención del usuario.

2. **Error de Encoding de Windows (`cp1252` vs `UnicodeEncodeError`)**:
   - *Fallo*: Al imprimir respuestas JSON enriquecidas con descripciones en español o caracteres especiales (ej. comillas tipográficas, tildes, caracteres ocultos como `\u200c`), la consola estándar de Windows arrojaba `UnicodeEncodeError: 'charmap' codec can't encode character`.
   - *Solución implementada*: Configuración global obligatoria `sys.stdout.reconfigure(encoding="utf-8")` y `ensure_ascii=False` en todas las salidas por terminal.

3. **Complicar el flujo cuando ya existía el MCP oficial**:
   - *Fallo*: Intentar armar scripts ad-hoc usando `requests` directos a endpoints REST internos cuando el servidor MCP (`call_mcp`) ya expone `listCases` y `getCaseDetail` de forma nativa con autenticación gestionada.
   - *Solución implementada*: Creación del script definitivo y único: [`stellar_case_fetcher.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_case_fetcher.py).

---

## ⚡ 2. Protocolo Oficial para Consultar Casos (Comandos Exactos)

A partir de ahora, para cualquier tarea de revisión de casos, se debe usar **exclusivamente**:

```powershell
# 1. Listar todos los casos abiertos en cola con formato tabular
python stellar_case_fetcher.py --open

# 2. Resumen forense completo de todos los casos abiertos (alertas, observables, hosts, usuarios)
python stellar_case_fetcher.py --all-open-summary

# 3. Detalle completo de un caso específico usando directamente el Ticket ID del analista
python stellar_case_fetcher.py --case 17850

# 4. Guardar el JSON crudo del caso en scratch/ para análisis profundo o auditoría
python stellar_case_fetcher.py --case 17850 --save
```

---

## 🛠️ 3. Resumen de Herramientas Oficiales de Conexión

| Tarea | Script a utilizar | Método de transporte |
| :--- | :--- | :--- |
| **Casos (Listado y Detalle)** | [`stellar_case_fetcher.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_case_fetcher.py) | Stellar Cyber MCP (`tools/call`) |
| **Búsqueda en Data Lake / Interflow** | [`stellar_cli.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_cli.py) `--search` | REST Data Lake Lucene Query |
| **Filtros de Log y Pre-DPI** | [`stellar_cli.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_cli.py) `--filters` | REST `/connect/api/v1/log_filters` |
| **Cuota y Licencias** | [`stellar_cli.py`](file:///g:/Hermes%20+%20Antigravity/soar/stellar_cli.py) `--quota` | REST `/licensing/usage` |
