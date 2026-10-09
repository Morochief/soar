# Ticket RFA: Reinstalación de SO por Riesgo Persistente de Seguridad

**Para:** Equipo de Soporte Técnico / Mesa de Ayuda
**De:** Centro de Operaciones de Seguridad (SOC)
**Asunto:** [URGENTE] RFA - Reinstalación de Sistema Operativo por Sospecha de Compromiso (Credential Stuffing/Infostealer) - Usuaria: Yení Perez

**Prioridad:** Alta
**Usuario Afectado:** Yení Perez (yeniperez@technoma.com.py)

---

### Solicitud de Acción (RFA)

Por instrucción de la jefatura de Seguridad de la Información, se requiere la ejecución inmediata de las siguientes medidas de erradicación sobre el equipo asignado a la usuaria Yení Perez:

1. **Reinstalación de Sistema Operativo (Formateo Clean-Wipe):** Se debe formatear por completo el disco del equipo e instalar la imagen corporativa base desde cero. No se permite la recuperación de estado de sistema (System Restore) ni conservar perfiles antiguos de navegadores, debido a que el payload puede estar alojado en la caché o en extensiones del usuario.

2. **Revocación de Sesiones:** Asegurarse de que, posterior a la entrega del nuevo equipo, se cierren todas las sesiones activas vinculadas a su perfil de red.

---

### Justificación Técnica y Evidencia (SOC)

El análisis proactivo del SOC y la investigación en Fuentes Abiertas de Inteligencia (OSINT) arrojan los siguientes resultados críticos:

* **Patrón de Credential Stuffing:** El perfil y cuenta de la usuaria viene presentando actividad anómala compatible con *Credential Stuffing* desde hace meses. Esto indica que un tercero no autorizado está probando credenciales expuestas continuamente contra nuestros portales.
* **Confirmación de Leaks (OSINT):** Tras una revisión exhaustiva en repositorios de inteligencia de código abierto y foros de brechas de datos (Data Leaks), **se confirmó el registro y exposición de las credenciales de la usuaria** en filtraciones de terceros.
* **Sospecha de Persistencia Local:** Dada la recurrencia de los intentos y el nivel de exposición de los datos, existe una altísima probabilidad de que el equipo actual se encuentre comprometido por un *Adware* persistente o un malware de tipo *Infostealer*, el cual está extrayendo tokens de sesión y contraseñas guardadas directamente desde el navegador de la usuaria.

Favor confirmar respuesta sobre este ticket una vez que el equipo haya sido formateado y entregado, para que el SOC proceda con el cierre del incidente en el SIEM.

Atentamente,
**Equipo SOC (Antigravity)**
*Technoma Cybersecurity*
