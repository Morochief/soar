---
name: analyze_cortex_alert
description: "Analiza alertas de Palo Alto Cortex XDR / BIOC entregando exclusivamente el veredicto tecnico y la plantilla de cierre, sin reportes extensos ni generacion de documentos."
---

# Skill: Analisis Express de Alertas Palo Alto Cortex XDR

Esta skill se activa de forma prioritaria cuando el usuario proporciona logs, texto, capturas o volcados JSON provenientes de Palo Alto Networks Cortex XDR (tanto si proceden de eventos nativos de Cortex XDR como de alertas ingestadas en Stellar Cyber bajo `event_source: palo_alto_cortex_xdr` o `palo_alto_networks_cortex_xdr_alerts`).

## 1. Regla Mandatoria de Brevedad (Veredicto y Cierre Exclusivo)

El usuario ha definido como directriz innegociable que ante alertas de Palo Alto Cortex **no se debe profundizar ni generar reportes extensos**.

*   **PROHIBIDO** generar reportes de 200 lineas, tablas de lineas de tiempo o disecciones forenses multi-capa.
*   **PROHIBIDO** incluir matrices CIA extensas, fases del ciclo NIST 800-61, analisis de fatiga de alertas o playbooks CERT-PY detallados.
*   **PROHIBIDO** crear carpetas o archivos Markdown en la ruta `Casos/` (no generar `analisis_soc.md` ni mover archivos al disco), a menos que el usuario lo solicite explicitamente.
*   **PROHIBIDO** el uso de emojis en todas las respuestas, titulos o plantillas para mantener el perfil profesional y tecnico.
*   **RESPUESTA DIRECTA EN CHAT:** Toda la respuesta debe imprimirse directamente en la conversacion, conteniendo unicamente los datos de identificacion, veredicto tecnico justificado y la plantilla de cierre lista para copiar.

## 2. Pautas Rapidas de Evaluacion Forense

Antes de emitir el veredicto, realiza una evaluacion silenciosa y quirurgica de los observables:

1.  **Decodificacion de Cargas Utiles (Base64):**
    *   Si la alerta involucra reglas analiticas como `PowerShell runs suspicious base64-encoded commands` o parametros `-EncodedCommand`, decodifica silenciosamente la carga util en memoria.
    *   Si el payload corresponde a verificaciones sintacticas de desarrollo (ej. `[System.Management.Automation.Language.Parser]::ParseInput` ejecutado por `claude.exe` u otras herramientas de terminal), cataloga como **Falso Positivo** o **Benign True Positive**.
2.  **Cruce con Software Corporativo y Memoria SOC:**
    *   Revisa si el proceso padre es software administrativo, clientes VPN (ej. `openconnect-gui.exe` ejecutando `route print`), instaladores autorizados (WiX / Burn ejecutando claves temporales `RunOnce`), o actividades de pentesting/auditoria interna documentadas en `SOC_GEM_v2.md`.
3.  **Evaluacion de Proceso e Integridad:**
    *   Verifica firmas digitales si estan presentes (`Signed` por Anthropic, Microsoft, Palo Alto, etc.).
    *   Identifica usuario y equipo (ej. equipo de desarrollador o analista).

## 3. Estados Oficiales de Resolucion (Cortex XDR)

Al cerrar una alerta en la consola de Cortex XDR (`Resolve Issue Id`), se debe seleccionar estrictamente uno de los siguientes valores oficiales bajo el campo **Mark This Issue As**:

1. **`Resolved - False Positive`**: Actividad benigna, instaladores legitimos firmados (ej. Motorola Solutions, Anthropic Claude, instaladores WiX), o software corporativo que detona reglas BIOC por heuristica sin impacto real.
2. **`Resolved - Known Issue`**: Comportamiento operativo o de infraestructura recurrente ya validado y documentado en la memoria tecnica del SOC (`SOC_GEM_v2.md`).
3. **`Resolved - Security Testing`**: Escaneos de vulnerabilidades, herramientas de pentesting (ej. Nmap, OSINT por auditores) o pruebas de seguridad internas autorizadas.
4. **`Resolved - True Positive`**: Amenaza confirmada o ejecucion maliciosa real que requirio contencion o investigacion de incidente.
5. **`Resolved - Duplicate Issue`**: Alerta que reporta un evento identico ya gestionado en otra investigacion o ticket abierto.
6. **`Resolved - Other`**: Escenarios administrativos o atipicos no contemplados en las categorias anteriores.

## 4. Formato Estricto de Salida

La respuesta debe estructurarse exactamente con las siguientes secciones:

```markdown
### Resumen del Evento Cortex
- Regla / Alerta: [Nombre de la regla o ID de alerta de Cortex XDR]
- Activo / Usuario: `[HOSTNAME]` (`[IP]`) | `[DOMINIO\USUARIO]`
- Proceso Padre / Hijo: `[proceso_padre.exe]` -> `[proceso_hijo.exe]`
- Comando / Accion: `[Comando ejecutado o resumen decodificado]`

### Veredicto Tecnico
- Clasificacion: [Falso Positivo / Benign True Positive / True Positive]
- Justificacion: [Explicacion tecnica y sintetica de 2 a 4 lineas detallando la legitimidad del proceso, ausencia de impacto malicioso y causa de la deteccion heuristica/BIOC]

### Cierre en Plataforma (Cortex XDR)
- Mark This Issue As: [Resolved - False Positive | Resolved - Known Issue | Resolved - Security Testing | Resolved - Duplicate Issue | Resolved - True Positive | Resolved - Other]
- Resolution Tag (Stellar si aplica): [False Positive | Benign True Positive | True Positive]
- Comentario de Cierre:
> "[Comentario en prosa fluida, narrativa y profesional, listo para copiar y pegar en la consola de Cortex XDR o Stellar Cyber, indicando host, usuario, ejecutable, causa del disparo analitico y justificacion de cierre sin numeraciones mecanicas ni listas rigidas]"

### Bitacora de Excel (Fila Unica)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Deteccion | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripcion | Evidencia | Solicitud de Accion | Estado | URL | Generacion de Ticket | TICKET | Playbook |
| [Datos delimitados por pipes correspondientes a la fila de 18 columnas] |
```
