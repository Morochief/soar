# 🚀 Stellar Cyber 7.0.0s — Novedades, Cambios de API e Impacto en el SOC

> **Versión:** Stellar Cyber 7.0.0s (Release: Agosto 2026 / Actualizado: Octubre 2026)  
> **Referencia Oficial:** [Stellar Cyber 7.0.0s Release Notes](https://docs.stellarcyber.ai/prod-docs/7.0.xs/Release-Notes/Stellar-Cyber-7.0.0-Release-Notes.htm)  
> **Destinatarios:** Analistas SOC, Ingenieros de Detección y Desarrolladores del Cockpit/SOAR.

---

## ⚠️ 1. Cambios de Comportamiento y Rompimiento de API (Breaking Changes)

| Identificador | Cambio Técnico | Impacto y Acción en Nuestro Código |
| :--- | :--- | :--- |
| **`AELDEV-67525`** | **Renombrado de `requestId` a `request_id`** en respuestas de error de la API (5xx). | Se alinea con la convención `snake_case`. Si algún script o diálogo del Cockpit busca `requestId` en el JSON de error, debe actualizarse a `request_id` (o soportar ambos con `.get("request_id", res.get("requestId"))`). |
| **`AELDEV-67820`** | **Privilegios RBAC forzosos en endpoints de sensores** (`/data_sensors`). | Llamadas públicas para listar o gestionar sensores ahora devuelven `403 Forbidden` si el usuario de la API no tiene el rol exacto configurado en la UI. |
| **`AELDEV-28743`** | **Eliminación de `tgrp_logo` en `/tenant_groups`**. | La lista de grupos de tenants ya no entrega el logo embebido. Si se requiere la imagen del tenant, debe llamarse a `/tenant_group/{id}/logo`. |
| **`DATA-3634`** | **Corrección en Log Filters numéricos (`==` y `!=`)**. | **[CORRECCIÓN CLAVE]** Anteriormente los filtros que comparaban campos numéricos con `==` o `!=` fallaban porque comparaban string con int. Ahora sí hacen match correctamente y descartan los logs según la regla. |

---

## 🌟 2. Nuevas Capacidades de Alto Valor para Nuestro `command_center.py` y `stellar_cli.py`

### 2.1. Bloqueo de Dominios y URLs en FortiGate (`AELDEV-67465`)
* **Novedad:** Ahora el responder de FortiGate no se limita solo a bloquear direcciones IP; **soporta bloqueo y desbloqueo de URLs y Dominios completos** a través de Web Filter integrado en las políticas del firewall.
* **Oportunidad en Command Center:**
  * Podemos agregar en el menú contextual de observables del Cockpit la opción directa:  
    👉 `[FortiGate] Bloquear Dominio Malicioso` y `[FortiGate] Bloquear URL de Phishing`.

### 2.2. Métricas de Caso y SLAs (`AELDEV-66747`)
* **Novedad:** Stellar Cyber 7.0.0s incluye un motor de cronómetros configurables dentro del objeto `details.metrics` del caso:
  * `Time to Acknowledge` (TTA): Tiempo desde la creación del ticket hasta que un analista lo reclama.
  * `Time to Resolve` (TTR): Tiempo total hasta el cierre o resolución.
* **Oportunidad en Command Center:**
  * Ya extraemos esto en `stellar_cli.py` (ej. en el caso `#17813` medimos `1427.2s / 23.8 min`). Podemos agregar una columna o tag de SLA directamente en la tabla de casos del Cockpit.

### 2.3. Payload Imprimible en Alertas IDS (`AELDEV-72713`)
* **Novedad:** En las alertas de red de sensores modulares, ahora se incluye el campo `ids.payload_details.payload_printable`.
* **Beneficio Operativo:** Permite inspeccionar el payload exacto del paquete HTTP/TCP que disparó la regla IDS sin necesidad de descargar y abrir el archivo `.pcap` en Wireshark.

### 2.4. Resumen de Casos Autónomo por Colas (`ASOC-152`)
* **Novedad:** Las colas de casos ahora admiten configuración de `Case Summary` (IA) y `Auto-Triage`, con una nueva cola por defecto llamada `AI Analyst` para casos críticos.

---

## 🎯 3. Nuevas Detecciones Analíticas y Machine Learning (Añadir a Playbooks)

1. **`Possible Pass-the-Ticket Attack` (`AELDEV-59279`):**
   * Detecta solicitudes Kerberos TGS desde una dirección IP que nunca tramitó un TGT legítimo para esa cuenta. Detección directa de robo y reutilización de tickets en Active Directory.
2. **`MS365 Login From New ASN` (`AELDEV-68306`):**
   * Alerta cuando una cuenta de Microsoft 365 / Entra ID inicia sesión desde un Autonomous System Number (ASN) nunca antes visto en el histórico del usuario.
3. **`Aborted SSH Sessions in Brute Force` (`AELDEV-68309`):**
   * Ahora las anomalías de login fallido evalúan conexiones SSH que son abortadas por escáneres automatizados antes de completar el handshake de autenticación.
4. **Detalles en `Office 365 Multiple Users Deleted` (`AELDEV-67557`):**
   * La alerta ahora puebla nativamente los campos `deleted_user_count` y `deleted_user_list` (hasta 50 usuarios) sin necesidad de hacer queries complejas al Data Lake.

---

## 🔧 4. Mejoras Técnicas en Integraciones

* **Cisco AMP & Ironscales (`AELDEV-69344`, `AELDEV-68929`):** Integración nativa de alertas de endpoint y correo phishing.
* **Sesiones de FortiGate Limpias (`AELDEV-70760`):** Se corrigió la fuga de sesiones administrativas en FortiGate; ahora cierra la sesión HTTP inmediatamente tras aplicar una acción de bloqueo/desbloqueo.
* **Timeouts en ATH (`AELDEV-72281`):** Las reglas de Automated Threat Hunting pesadas ya no se re-disparan en bucle infinito cada 2 minutos si dan timeout.
