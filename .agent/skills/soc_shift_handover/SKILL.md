---
name: soc_shift_handover
description: "Genera el reporte resumido de entrega de turno (handover) en formato informal de WhatsApp y línea de Bitácora para el cierre de guardia según las directivas de Ivan Centurión."
---

# Skill: Reporte de Entrega de Turno (SOC Shift Handover)

Esta skill permite al analista (Kevin, Angel o Igor) generar un reporte de novedades al finalizar su guardia para enviarlo rápidamente por WhatsApp Web al grupo de la oficina y registrar los datos correspondientes en la bitácora general.

## 🔴 REGLAS DE ESTRUCTURA Y TONO (Directivas de Ivan Centurión):
1. **Brevedad Extrema:** El mensaje de WhatsApp debe ser conciso, informal y estructurado para lectura rápida en móvil. **No agregues detalles técnicos excesivos** como direcciones IP, hashes de archivos o payloads complejos.
2. **Resumen Personal:** Se enfoca en el trabajo realizado por el analista durante su guardia y en las novedades de sistemas o infraestructura que experimentó.
3. **Eventualidades de Sistemas:** Debe documentar cualquier inconveniente con:
   - Sistemas internos: Conectividad de la oficina, cortes de energía, Odoo, Cortex XDR, sensores sin telemetría, actualizaciones de agentes.
   - Sistemas de clientes e interacciones con el NOC.
4. **Cierre e Hilo Continuo:** Debe identificar claramente qué queda pendiente para el relevo entrante para evitar vacíos de cobertura.
5. **Ventana de Solapamiento (Overlap):** Se debe mantener una comunicación o revisión verbal/chat breve de 10-15 minutos entre el analista saliente y el entrante antes de desconectarse, revisando la cola de alertas conjunta.
6. **Guardias sin Novedad:** Si la guardia fue silenciosa, el reporte debe generarse igualmente, confirmando la revisión del entorno y marcando "sin incidentes activos" para asegurar la auditoría de la consola.
7. **Puntos Ciegos y Pendientes de Terceros:** Registrar cortes de telemetría de sensores, mantenimientos programados o respuestas pendientes de proveedores/NOC para evitar la pérdida de visibilidad o de tickets en espera.


---

## FORMATO DEL REPORTE DE WHATSAPP (Listo para copiar y pegar):

```text
*REPORT DE GUARDIA SOC - [TURNO]*
*Fecha:* [Fecha actual] | *Analista de Guardia:* [Nombre del Analista]

*Casos Procesados e Incidentes:*
• [ID_CASO] - [Nombre Resumido] -> [Veredicto/Estado]
• [ID_CASO] - [Nombre Resumido] -> [Veredicto/Estado]

*Novedades de Infraestructura y Herramientas:*
• [Ej. Sensores caídos, reinstalación de agentes, cortes de internet de oficina, problemas con Odoo o electricidad]

*Pendientes para el Relevo:*
• [Tareas prioritarias que debe seguir o verificar el analista del siguiente turno]
```


---

## 📊 REGISTRO DE BITÁCORA GENERAL (Excel)
El analista también debe asegurarse de haber completado la bitácora Excel del SOC. Esta skill recordará y recopilará la línea consolidada para cada uno de los casos procesados durante la guardia en el formato estándar:

`Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc.) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook`

---

## 🛠️ INSTRUCCIONES DE EJECUCIÓN (Para el Agente):
1. **Recopilación Automática:** Escanea el directorio `Casos/` del workspace y extrae los casos procesados con fecha del día actual o durante el turno.
2. **Entrevista de Guardia:** Pregunta al usuario si existieron novedades de infraestructura (caída de odoo, problemas de red, reinstalaciones de Sophos/Cortex, cortes de luz) o algún pendiente crítico para el relevo.
3. **Generación de Entregables:** 
   - Genera el reporte de WhatsApp listo para copiar en un bloque markdown y una bitácora consolidada.
   - Guarda el reporte final de la guardia en un archivo markdown en `Novedades/reporte_[fecha]_[turno].md` para mantener la persistencia y trazabilidad de los relevos.
