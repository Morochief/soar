# 📋 MINUTA TÉCNICA Y GUÍA DE CONFIGURACIÓN
## INTEGRACIÓN DE CONECTOR SOPHOS CENTRAL (VALORES CASA DE BOLSA) EN STELLAR CYBER

```
========================================================================================
[CONTROL DOCUMENTAL - TECHNOMA SOC]
Documento: Minuta de Conexión / Procedimiento Operativo Estándar (SOP)
Tenant Objetivo: Valores (Valores Casa de Bolsa)
Plataformas: Sophos Central ➔ Stellar Cyber Open XDR
Conector: VALORES-SOPHOS (Endpoint Security)
Estado Final: Healthy / Test Success !
Fecha de Ejecución: 29 de Octubre de 2026
Responsable: Kevin Moraes — Analista SOC Technoma
========================================================================================
```

---

### 🎯 1. Objetivo
Establecer y documentar el procedimiento paso a paso para la integración, recolección automatizada de telemetría y monitoreo de alertas de **Sophos Central** del cliente **Valores Casa de Bolsa** dentro de la plataforma **Stellar Cyber Open XDR**, asegurando la ingesta continua de eventos de endpoints en el Data Lake del SOC.

---

### 🛠️ 2. Procedimiento de Alta del Conector (Paso a Paso)

#### Paso 1: Pantalla "1 - General"
1. En la consola web de Stellar Cyber, navegar a: **System ➔ Integrations ➔ Connectors**.
2. Hacer clic en el botón superior derecho **Create** (o Add Connector).
3. Completar los campos de la sección inicial:
   * **Category \*:** Seleccionar `Endpoint Security` desde el menú desplegable.
   * **Type \*:** Seleccionar `Sophos Central`.
   * **Function \*:** 
     * `Collect`: **Marcar (Checked)** *(habilita la recolección periódica de logs)*.
     * `Respond`: **No marcar (Unchecked)** *(deshabilitado para este perfil de recolección)*.
   * **Name \*:** `VALORES-SOPHOS` *(nomenclatura estándar del tenant)*.
   * **Tenant Name \*:** `Valores` *(asignar al tenant oficial del cliente)*.
   * **Run On \*:** `Data Processor` *(ejecución en la arquitectura DP)*.
   * **Log Filters:** Dejar completamente **en blanco** *(permite la ingesta sin exclusiones previas)*.
4. Presionar **Next** para avanzar a la pestaña de configuración.

---

#### Paso 2: Pantalla "2 - Configuration"
Cargar los parámetros de autenticación obtenidos previamente desde la consola de Sophos Central (Access Control / API Credentials Management):
* **Auth Method:** Seleccionar `Client ID / Client Secret`.
* **Account Type:** Seleccionar `Tenant`.
* **Client ID:** Ingresar el *Client ID* oficial de la API de Sophos para Valores.
* **Client Secret:** Ingresar el *Client Secret* asociado a la credencial.
* **Interval (min):** `5` *(frecuencia de sondeo cada 5 minutos)*.
* **Content Type:** Marcar obligatoriamente ambas casillas:
  * `Alerts` *(detecciones e indicadores de compromiso)*.
  * `Events` *(telemetría de ejecución, usuarios y endpoints)*.
5. Presionar **Next**.

---

#### Paso 3: Pantalla "3 - Done" y Envío
* Revisar el resumen de parámetros configurados.
* Hacer clic en el botón **Submit** para persistir el conector en el sistema.

---

### 🧪 3. Verificación de Conectividad y Validación de Ingesta

1. **Prueba de Conectividad (Test Connection):**
   * En la tabla de **Connector Overview**, ubicar el conector `VALORES-SOPHOS`.
   * En la columna **Actions**, hacer clic sobre el botón **Test**.
   * **Resultado Esperado:** Debe desplegarse en la parte superior el banner verde de confirmación:
     ```text
     ✔ Test Success !
     ```
2. **Ciclo de Ingesta y Normalización de Estado:**
   * **Aviso Inicial (Transitorio):** Inmediatamente después de la creación, es normal que en la columna *Messages* aparezca una advertencia indicando que el conector no recibió eventos en las últimas 24 horas.
   * **Transición a Healthy:** Tan pronto transcurra el primer intervalo de 5 minutos y se sincronicen los primeros eventos desde la API de Sophos, el mensaje desaparece de forma automática y el campo **Status** pasa a estado **Healthy** con punto verde indicador de operatividad plena.
3. **Control de Switches Operativos:**
   * **Collect:** `Active` (Switch en verde).
   * **Respond:** `Disabled`.

---

### 📊 4. Evidencia Visual del Conector en Producción

```
+-------------------------------------------------------------------------------------------------------------------------+
|                                                   CONNECTOR OVERVIEW                                                    |
+-------------------+---------+-------------+-------------------+----------------+---------+----------+-------------------+
| Name              | Status  | Tenant Name | Category          | Type           | Collect | Respond  | Run On            |
+-------------------+---------+-------------+-------------------+----------------+---------+----------+-------------------+
| VALORES-SOPHOS    | Healthy | Valores     | Endpoint Security | Sophos Central | Active  | Disabled | Data Processor    |
+-------------------+---------+-------------+-------------------+----------------+---------+----------+-------------------+
```

* **Query de validación forense en Data Lake (Threat Hunting):**
  ```lucene
  tenantid: "1eca05ee87694961b66dcf96d774ece8" AND (msg_class: "sophos_events" OR msg_class: "sophos_alerts")
  ```
