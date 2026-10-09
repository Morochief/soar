# Manual Operativo de Soporte y Triaje Técnico: VASCOL S.A.C.I.
**Documento de Delegación Operativa para Analistas SOC / Helpdesk**  
**Autor:** Kevin Moraes (a partir de la sesión de soporte con Iván Centurión - SOC Manager)  
**Fecha:** Octubre 2026  
**Entorno del Cliente:** VASCOL S.A.C.I. (`vascol.com.py` / Dominio: `VASCOL`)

---

## 1. Topología y Servidores Críticos del Cliente

| Nombre del Servidor / Dispositivo | Dirección IP / ID | Sistema Operativo / Servicio | Rol y Puntos Críticos |
| :--- | :--- | :--- | :--- |
| **Acceso Remoto Inicial (AnyDesk)** | **`1 968 947 902`** | AnyDesk Client | **Punto de Entrada / Salto:** ID para conectarse remotamente desde afuera a la red del cliente VASCOL. |
| **Switch Core (`VAS-SWCORE`)** | **`192.168.210.1`** | **Allied Telesis x510L-28GT** (AlliedWare Plus 5.4.6) | **Switch Core Principal L3:** Acceso por Telnet/SSH. Usuario: `telenet`. MAC: `E0:1A:EA:0C:DF:AF`. S/N: `G24SG50YW`. |
| **`TERMINAL-DESK`** | `192.168.225.x` | Windows Server (RDS / Terminal Server) | Servidor de trabajo compartido para usuarios operativos. Conexión vía RDP. |
| **Servidor Precios / ERP (`IBManager`)** | **`192.168.225.20`** | Linux (Acceso SSH `root`) | **Servidor de Precios y Estaciones de Servicio:** Aloja la lógica y base de datos de precios de combustibles y convenios de estaciones de servicio. |
| **`vas-db-01`** | `192.168.210.210` | CentOS 7 (VMware VM) | Base de datos principal. **Cuidado:** `/mnt/mysql` suele estar al 98% de uso (355 GB / 372 GB). |
| **Servidor Zimbra** | `192.168.211.4` | Linux CentOS / RHEL (VMware VM) | Servidor de Correo Zimbra. **Cuidado:** Todo vive en `/opt/zimbra`. Si `/opt` llega al 100%, Zimbra se detiene automáticamente. |
| **Observium (Monitoreo)** | `192.168.225.21` | Observium CE | Monitor de red, uso de CPU, RAM, tráfico y almacenamiento de servidores. |
| **Perímetro de Red** | Red interna | FortiGate & UniFi Network Controller (`192.168.210.195`) | Firewall perimetral y switches/APs de la infraestructura. |

---

## 2. Inventario de Cuentas y Sesiones en `TERMINAL-DESK`

En este servidor conviven múltiples usuarios mediante sesiones remotas independientes. 

> [!IMPORTANT]
> **El ID de sesión es dinámico:** Cada vez que un usuario se desconecta y se vuelve a conectar, Windows le asigna un número de ID nuevo. Antes de cualquier soporte, **siempre** debes consultar el ID actualizado con `query user`.

| Nombre de Usuario | Rol / Área Conocida | Comportamiento Típico / Notas |
| :--- | :--- | :--- |
| **`andrea.villanueva`** | Recursos Humanos (`rrhh1@vascol.com.py`) | Usa Mozilla Thunderbird para gestionar correos. Realiza archivado en *Carpetas locales*. |
| **`asistente.directorio`** | Asistencia de Dirección / Gerencia | Cuenta de alto perfil corporativo. |
| **`miguel.vallejos`** | Operaciones / Administrativo | Usuario activo en RDS. |
| **`pago.proveedores`** | Finanzas / Pagos | Manejo de facturación y transferencias bancarias. |
| **`cuenta.corriente`** | Contabilidad / Finanzas | Conciliación y estados de cuenta. |
| **`javier.leite`** | Operaciones | Usuario recurrente. |
| **`luis.ramirez`** | Operaciones | Usuario recurrente. |
| **`tania.cespedes`** | Administrativo | Usuario activo. |
| **`dario.diaz`** | Administrativo | Usuario activo. |
| **`rogelio.gonzalez`** | Operativo | Usuario activo. |
| **`viviana.gonzalez`** | Operativo | Suele quedar en estado *Desconectado (Desc)*. |
| **`laura.villalba`** | Operativo | Suele quedar en estado *Desconectado (Desc)*. |
| **`coordinacionfeteados`**| Planta / Producción | Sesión compartida de coordinación. |
| **`jose.morales`** | Operativo | Sesiones de larga duración. |
| **`acomercial`** | Área Comercial | Sesión intermitente. |
| **`yeni.vega`** | Administrativo | Sesión intermitente. |
| **`ivan.centurion`** | SOC Manager (Técnico / Administrador) | Sesión administrativa desde donde se brinda soporte. |

---

## 3. Procedimiento de Soporte Remoto en Vivo (RDP Shadowing)

Cuando un usuario de VASCOL reporte problemas o solicite asistencia en su escritorio, el soporte se realiza mediante **RDP Shadowing** para no cerrar su sesión.

### Paso 1: Abrir la consola con privilegios de Administrador
1. En el menú inicio, busca `cmd` o `PowerShell`.
2. Haz clic derecho y selecciona **"Ejecutar como administrador"** (obligatorio, de lo contrario dará *Acceso denegado*).

### Paso 2: Identificar el número de sesión del usuario
Ejecuta:
```cmd
query user
```
Busca en la columna **`ID`** el número correspondiente al usuario que necesita soporte:
* Si vas a asistir a **Miguel Vallejos** y su línea dice `miguel.vallejos rdp-tcp#4 3 Activo`, su ID actual es **`3`**.
* Si vas a asistir a **Andrea Villanueva** y su línea dice `andrea.villanueva rdp-tcp#8 9 Activo`, su ID es **`9`**.

### Paso 3: Tomar el control remoto de la sesión
Ejecuta el siguiente comando reemplazando `<ID>` por el número obtenido:
```cmd
mstsc /shadow:<ID> /control
```
* **`/shadow:<ID>`**: Se conecta a la pantalla de la sesión activa del usuario.
* **`/control`**: Permite mover el mouse y usar el teclado para resolver el problema.
* **¿Por qué NO usar `/noConsentPrompt`?**: La directiva de grupo (GPO) de VASCOL exige consentimiento por privacidad. Si agregas `/noConsentPrompt`, Windows devolverá **Acceso denegado**.

### Paso 4: Aceptación por parte del usuario
1. Al ejecutar el comando, aparecerá una barra verde: *"Conectándose a: TERMINAL-DESK"*.
2. En ese momento, en la pantalla del usuario aparecerá un cuadro de diálogo:
   > *"El administrador solicita ver y controlar su escritorio. ¿Desea permitirlo? [Sí] [No]"*
3. Pídele al usuario por teléfono/WhatsApp que haga clic en **"Sí"**.
4. La ventana se abrirá inmediatamente con el escritorio del usuario compartido en tiempo real.

---

## 4. Troubleshooting del Servidor de Correo Zimbra

### Síntoma: "El correo no envía/recibe", "Thunderbird da error de conexión" o "Zimbra se cayó"

#### Datos Técnicos de la Plataforma Zimbra (VASCOL):
* **Versión de Zimbra:** `8.8.15_GA_4372.FOSS` (Edición Open Source)
* **Cantidad de Cuentas:** 257 cuentas de correo en 3 dominios.
* **Métrica clave de recuperación (Consola Admin):**
  * **Servicio:** `Ejecutándose`
  * **Sesiones activas normales:** ~20-25 sesiones concurrentes.
  * **Longitud de la cola de correo:** Debe estar en **`0`**. *(Si este valor es alto, significa que los correos entrantes/salientes están represados por problemas de DNS, antispam o caída de servicios)*.

#### Causa Raíz Principal Detectada:
El disco virtual del servidor de correo (`192.168.211.4`) se queda sin espacio al 100% en la partición `/opt`:
1. Zimbra instala todo en `/opt/zimbra` (base de datos MySQL, LDAP, buzones, adjuntos y colas).
2. Cuando el disco llega al 100%, **MySQL/MariaDB y LDAP se apagan automáticamente por seguridad** para no corromper los archivos de correo.
3. Esto detiene en cadena a `mailboxd` (Java), Postfix (MTA) y los puertos IMAP/POP3.

#### Procedimiento de Verificación y Recuperación:
1. **Revisar Observium (`http://192.168.225.21`):**
   * Ir al dispositivo `192.168.211.4` (Zimbra) y revisar la sección **Storage** (`/opt`). Si está por encima del 95%, está en zona crítica.
   * Revisar el dispositivo `vas-db-01` (`192.168.210.210`) y comprobar `/mnt/mysql`.
2. **Acceso SSH al servidor Zimbra:**
   ```bash
   df -h /opt
   ```
   * Si está lleno, notificar a Infraestructura para agrandar el disco en VMware (como se hizo al subir de 496 GB a 596 GB) o purgar logs antiguos en `/opt/zimbra/log/` y `/opt/zimbra/redolog/archive/`.
3. **Comprobar estado de los servicios:**
   ```bash
   su - zimbra
   zmcontrol status
   ```
   Si servicios como `mailbox`, `ldap` o `mta` están en *Stopped*:
   ```bash
   zmcontrol restart
   ```

### Procedimiento de Cambio de Contraseñas en Zimbra Admin

Cuando un usuario tenga problemas de autenticación o solicite reseteo de clave de correo:

1. **Acceso a la Consola de Administración:**
   * **URL:** `https://mail.vascol.com.py:7071/zimbraAdmin/`
   * **Usuario:** `admin` (o `admin@vascol.com.py`)
2. **Política y Nomenclatura de Contraseñas del Cliente (VASCOL):**
   * **Regla general de reseteo:** `[Número de cédula invertida] + [Segundo nombre]`
   * **Contraseña asignada para `rrhh1@vascol.com.py` (Andrea Villanueva):**  
     `Clavevillanueva2026++`
3. **Paso a paso en la consola web:**
   1. En el buscador superior o menú izquierdo (*Administrar ➔ Cuentas*), buscar la cuenta (ej. `rrhh1` o `rrhh1@vascol.com.py`).
   2. Hacer clic derecho sobre la cuenta o hacer clic en la rueda dentada/engranaje superior y seleccionar **«Cambiar contraseña»**.
   3. Ingresar la nueva contraseña en los campos *Contraseña* y *Confirmar contraseña*.
   4. *Opcional:* Desmarcar la casilla *"Debe cambiar la contraseña"* si no se quiere forzar al usuario a renovarla en su primer inicio de sesión web.
   5. Clic en **«Aceptar»**.

> [!WARNING]
> **Paso Obligatorio Post-Cambio en Thunderbird:**  
> Inmediatamente después de cambiar la contraseña en Zimbra, debes ingresar a la sesión del usuario (vía RDP Shadowing) o pedirle que abra **Mozilla Thunderbird**.  
> Thunderbird mostrará una ventana pidiendo la nueva contraseña para:
> 1. El servidor de entrada **IMAP** (recibir correos).
> 2. El servidor de salida **SMTP** (enviar correos).  
> Marca la casilla **"Usar el Administrador de contraseñas para recordar esta contraseña"** para que el usuario no tenga que escribirla de nuevo cada vez que abra el programa.

---

## 5. Gestión del Cliente de Correo (Mozilla Thunderbird)

* **Protocolo:** IMAP (puerto seguro 993 con SSL/TLS). Lo que se hace en Thunderbird se sincroniza en el servidor Zimbra.
* **Caché sin conexión:** Thunderbird descarga copias locales de los correos en `C:\Users\<usuario>\AppData\Roaming\Thunderbird\` para búsquedas instantáneas.
* **Liberación de cuota en Zimbra:**  
  Si la casilla de un usuario (como `rrhh1@vascol.com.py`) se llena en el servidor:
  1. En Thunderbird, crear una carpeta dentro de **"Carpetas locales"** (ej: `Archivos > 2026`).
  2. Mover los correos del año anterior desde la Bandeja de entrada hacia Carpetas locales.
  3. Esto descarga el correo al disco local de `TERMINAL-DESK` y lo borra de Zimbra, liberando cuota en el servidor.
  4. **Precaución:** Esos correos archivados localmente deben ser respaldados en los backups del servidor Windows.
* **Comportamiento transitorio tras caídas del servidor (*"Thunderbird No responde"*):**  
  Justo después de que Zimbra se levanta o se cambia la clave, es normal que Thunderbird muestre la barra de título como **`Mozilla Thunderbird (No responde)`** y abajo a la izquierda el mensaje **`rrhh1@vascol.com.py: Resolviendo mail.vascol.com.py...`** con una rueda de carga. Esto sucede porque el cliente intenta reconectar y resincronizar en masa miles de correos y carpetas pendientes.  
  **Recomendación:** No forzar el cierre del proceso (`taskkill`); esperar 1 a 2 minutos hasta que termine el handshake IMAP y la ventana vuelva a responder sola.
* **Truco de Soporte: Descongelar Thunderbird por apertura masiva de pestañas/correos:**  
  * **Problema:** En las capturas se vio que Andrea suele tener 6 u 8 pestañas de correos abiertas arriba (*RE: FACTURAS...*, *AVISO DE TRANSFERENCIA...*, etc.). Al abrir Thunderbird con tantas pestañas simultáneas, el programa intenta consultar todos los mensajes y adjuntos por IMAP al mismo tiempo, lo que satura el hilo de la interfaz y lo cuelga por completo.  
  * **Solución operativa (Iniciar sin conexión ➔ Sincronizar):**
    1. Si está colgado, cerrar el programa (o finalizar proceso en el Administrador de Tareas).
    2. Iniciar Thunderbird en **Modo Sin Conexión** (*Trabajar sin conexión*):  
       * Se puede alternar haciendo clic en el **icono de las dos pantallitas / conexión** en la esquina inferior izquierda de Thunderbird, o desde el menú *Archivo ➔ Sin conexión ➔ Trabajar sin conexión*.
    3. Esto hace que Thunderbird cargue la interfaz y todas las pestañas abiertas **usando únicamente la caché del disco local**, abriendo en 2 segundos sin congelarse.
    4. Una vez que la pantalla cargó y se estabilizó, volver a hacer clic en el icono inferior para **pasar a modo conectado**: Thunderbird comenzará a sincronizar los correos nuevos de forma ordenada y sin colgarse.

---

## 6. Organización del Llavero Centralizado de Contraseñas (KeePassXC)

Para mantener los accesos de VASCOL organizados y seguros entre todos los analistas del SOC:

* **Archivo base:** `VASCOL.kdbx` + archivo de clave obligatoria `vascol.key` (2FA nativo).
* **Configuración obligatoria en KeePassXC:**
  * *Herramientas ➔ Configuración ➔ Básico ➔ Seguridad:* Marcar **«Recargar automáticamente la base de datos cuando se modifique en disco»** para sincronizar cambios concurrentes sin pisar datos.

### Estructura de Grupos en KeePassXC:
```text
VASCOL S.A.C.I.
├── 01. Redes & Perímetro (FortiGate, UniFi Controller, Switches, VPNs)
├── 02. Servidores (TERMINAL-DESK RDP, vas-db-01 MySQL, Zimbra Linux)
├── 03. Correo & Servicios (Zimbra Web Admin https://192.168.211.4:7071, Postfix, SSH)
├── 04. Monitoreo & SOC (Observium http://192.168.225.21, Grafana, Security Onion)
└── 05. Cuentas de Dominio / AD (Dominio VASCOL, Administradores, Cuentas de Servicio)
```

---

## 7. Configuración Integral de Alertas en Observium (Storage, Procesador y Webhook)

Para evitar que vuelva a ocurrir una caída no advertida del servidor Zimbra (o de la base de datos `vas-db-01`) por falta de espacio o sobrecarga de recursos, se implementa el sistema de alertas de Observium (`http://192.168.225.21`) integrado con un **Webhook** hacia el equipo del SOC.

---

### 7.1 El Error Clásico en la Condición de Disco y el Mito de "Reinstalar Observium"

Durante la sesión de soporte se observó una **tormenta masiva de alertas rojas (*Alert Storm*)** sobre `/boot`, `/`, `/opt` y datastores VMFS de VMware, lo que llevó a pensar erróneamente que *«Observium tiene problemas y hay que reinstalarlo»*.

#### 🔍 Diagnóstico Forense del Error:
* **Lo que se configuró:** Se ingresó como condición `storage_free > 90%`.
* **La falla lógica:** En la arquitectura de Observium, `storage_free` mide el **Espacio LIBRE**, no el espacio ocupado.
* **El resultado:** Al ponerle `> 90%`, la regla decía: *«Dispara una alerta crítica si el disco tiene MÁS del 90% de espacio libre (es decir, cuando esté casi vacío)»*. Por eso Observium alertó inmediatamente sobre particiones recién creadas o con poco uso.

> [!CAUTION]
> **¡NO se debe reinstalar Observium!**  
> El software no está corrupto ni dañado. Una reinstalación borraría todo el historial de métricas RRD, las interfaces del Switch Core, los enlaces descubiertos y el inventario de servidores.  
> El problema se soluciona en **30 segundos** corrigiendo la métrica y pulsando el botón **`Rebuild`**.

---

### 7.2 Configuración del Alert Checker 1: Almacenamiento (Disco Duro Próximo a Llenarse)

Este checker vigila que ninguna partición crítica (como `/opt` en Zimbra o `/mnt/mysql` en la base de datos) alcance el umbral de bloqueo del 100%.

1. En Observium, ingresar al menú superior: **Alerting ➔ Alert Checkers ➔ Add Checker**.
2. **Formulario de Identificación (New Checker Details):**
   * **Entity Type:** `Storage` (Seleccionar en el desplegable).
   * **Alert Name:** `Alerta: Disco duro próximo a llenarse (>90%)`
   * **Alert Message:** `CRÍTICO: El volumen de almacenamiento {{ $entity_name }} en {{ $device_hostname }} ha superado el 90% de ocupación. Riesgo de bloqueo de servicios.`
   * **Severity:** `Critical`
   * **Delay:** `1` (Verificación en el siguiente ciclo).
3. **Condición de Evaluación (Test Conditions):**
   * **Métrica correcta:** **`storage_perc`** (*Storage Percentage Used*).
   * **Operador:** `>` (Mayor que).
   * **Valor:** `90`
   * *(Opcional para alerta temprana preventiva: crear un segundo checker con Severidad `Warning` en `storage_perc > 85`)*.
4. **Regla de Asociación (Association Ruleset):**
   Para aplicar esta vigilancia a los discos reales y evitar falsos positivos con unidades ópticas (CD-ROM) o memoria virtual compartida:
   * **Opción A (Recomendada para discos fijos):** `Storage Type equals hrStorageFixedDisk`
   * **Opción B (Servidores Linux de VASCOL):** `Device OS equals linux`
   * *(Cuidado: NUNCA usar `Storage Size > 90` porque en Observium el tamaño se calcula en Bytes enteros, no en porcentaje)*.
5. Hacer clic en **Add Checker**.

---

### 7.3 Configuración del Alert Checker 2: Procesador (Saturación Continua de CPU)

Vigila el uso excesivo de procesamiento en el servidor RDS (`TERMINAL-DESK`) o en servidores Linux causado por procesos bloqueados, bucles o ataques.

1. Ir a **Alerting ➔ Alert Checkers ➔ Add Checker**.
2. **Formulario de Identificación (New Checker Details):**
   * **Entity Type:** `Processor`
   * **Alert Name:** `Alerta: Alto consumo de CPU sostenido (>90%)`
   * **Alert Message:** `ADVERTENCIA: El procesador {{ $entity_name }} en {{ $device_hostname }} registra una carga superior al 90% de forma prolongada.`
   * **Severity:** `Warning` (o `Critical`)
   * **Delay (Obligatorio):** **`2`** o **`3`**  
     *(Configurar 2 o 3 ciclos de retraso es vital para CPU: evita falsos positivos por picos transitorios normales de 15 segundos al abrir programas o iniciar tareas programadas)*.
3. **Condición de Evaluación (Test Conditions):**
   * **Métrica:** **`processor_usage`**
   * **Operador:** `>`
   * **Valor:** `90`
4. **Regla de Asociación (Association Ruleset):**
   * Dejar en blanco para aplicar globalmente a todos los dispositivos, o configurar: `Device Type equals server`.
5. Hacer clic en **Add Checker**.

---

### 7.4 Creación del Contacto Webhook para Notificaciones

Observium **evalúa alertas pero NO las despacha** a menos que el Alert Checker tenga al menos un contacto asignado.

#### Paso a paso para crear el Webhook:
1. Ir al menú superior: **Alerting ➔ Contacts ➔ Add Contact**.
2. **Datos del Contacto:**
   * **Transport:** Seleccionar **`Webhook`** en la lista desplegable.
   * **Contact Title / Description:** `SOC-VASCOL-Alerts-Webhook`
   * **URL:** Pegar la dirección URL completa del Webhook generado en Discord, Microsoft Teams, Slack, Telegram o el webhook receptor del SOC / n8n:
     * *Ejemplo Discord:* `https://discord.com/api/webhooks/XXXXXX/YYYYYY/slack` *(agregar `/slack` al final si se usa el payload compatible)*.
     * *Ejemplo Teams / Slack:* `https://outlook.office.com/webhook/XXXXX...` o `https://hooks.slack.com/services/XXXXX...`
     * *Ejemplo Endpoint SOC / n8n:* `https://webhook.soc.technoma.local/vascol-alerts`
   * **HTTP Method:** `POST`
   * **HTTP Headers:** `Content-Type: application/json`
3. **Prueba de Entrega (Test Contact):**
   * Antes de cerrar la ventana, hacer clic en el botón **`Test Contact`**.
   * Verificar en el canal del SOC que ingrese el mensaje de prueba de Observium (`Test notification from Observium`).
4. Hacer clic en **Save Contact**.

---

### 7.5 Asociación Obligatoria: Vinculación Checker ➔ Contacto Webhook

Una vez creados los Checkers y el Contacto, **deben vincularse explícitamente**:

1. Ir a **Alerting ➔ Alert Checkers**.
2. Hacer clic sobre el Checker deseado (ej. `Alerta: Disco duro próximo a llenarse (>90%)`).
3. En las pestañas superiores del checker, entrar a **`Associations`**.
4. En el panel lateral derecho **Contacts**:
   * Abrir el menú desplegable y seleccionar: **`SOC-VASCOL-Alerts-Webhook`**.
   * Hacer clic en el botón verde **`+ Associate`**.
5. Confirmar que el contacto pase a listarse en la sección *Associated Contacts*.
6. Repetir el mismo paso para el checker de **CPU / Procesador**.

---

### 7.6 Procedimiento de "Rebuild" y Cierre de Alertas Falsas

Tras corregir la condición de `storage_free` a `storage_perc`:

1. Ir a la vista principal de **Alerting**.
2. En la barra superior derecha, hacer clic en el botón azul: **`Rebuild`**.  
   *Esto purga la tabla de condiciones mal evaluadas y regenera el mapa de dependencias de alertas*.
3. En el siguiente ciclo de sondeo del cron (*polling* programado cada 5 minutos), Observium:
   * Recalculará los porcentajes reales de cada partición.
   * Cerrará automáticamente todas las alertas rojas de `/boot` y datastores.
   * Dejará activa únicamente la alerta si un disco real supera el 90% (como `/opt` o `/mnt/mysql`).
4. **Comprobación manual inmediata por consola (Opcional):**  
   Si se tiene acceso SSH al servidor de Observium (`192.168.225.21`), se puede forzar el cálculo al instante sin esperar los 5 minutos:
   ```bash
   cd /opt/observium
   ./alerts.php -d
   ```
5. **Comportamiento ante Recuperación:** Cuando el equipo de infraestructura agrande el disco en VMware o se purguen logs, Observium detectará que el uso bajó del 90% y enviará automáticamente un webhook con estado **`RECOVERED`** (en verde), documentando el cierre del incidente en el canal del SOC.

---

## 8. Integración del Switch Core (`VAS-SWCORE`) en Observium

El Switch Core fue auditado directamente desde su archivo de configuración activa (*running-config*):

### Ficha Técnica y Credenciales del Switch Core:
* **Host:** `VAS-SWCORE`
* **IP de Gestión:** `192.168.210.1` (Puerto 23 Telnet / 22 SSH)
* **Modelo:** **Allied Telesis x510L-28GT** (AlliedWare Plus 5.4.6)
* **Cuentas Administrativas (Privilegio 15 / Root):**
  * `ivanc` | Contraseña: `elpasswordmassegurodel2026` (Confirmada y guardada en flash mediante `write memory`)
  * `telenet` | Contraseña existente en el switch
  * `admin` | Contraseña existente en el switch
* **Estado de Accesos por Consola:**
  * **Telnet (Puerto 23):** Activo y funcional.
  * **SSH (Puerto 22):** Deshabilitado temporalmente (`no service ssh`).
    * Al intentar activar con `service ssh`, el switch devuelve: `% SSHv2 host key does not exist. Try again after creating host key.`
    * **Para activar SSH correctamente:** Se debe generar primero el par de llaves criptográficas ejecutando `crypto key generate hostkey`, luego `service ssh` y finalmente `write memory`.
* **Comunidades SNMP Activas en el Switch:**
  * **`TELENET`** (Comunidad estándar de lectura)
  * **`Gp3b5_lK3xqxWv6`** (Comunidad alternativa activa)

### Segmentos de Red y DHCP Pools Descubiertos en el Core:
* **Red WiFi General:** `192.168.212.0/24` (Gateway: `192.168.212.1` | Rango DHCP: `.10` a `.253`)
* **Red Video / CCTV (Cámaras):** `192.168.214.0/24` (Gateway: `192.168.214.1` | Rango DHCP: `.20` a `.254`)
* **Red WiFi Directorio:** `192.168.220.0/24` (Gateway: `192.168.220.1` | Rango DHCP: `.100` a `.150`)
* **Red Invitados Directorio:** `192.168.215.0/24` (Gateway: `192.168.215.1` | Rango DHCP: `.100` a `.150`)
* **Servidor DNS Interno:** `192.168.225.2` (Controlador de Dominio Active Directory)

---

### Procedimiento para Darlo de Alta YA en Observium:

Como el switch **ya tiene el servicio SNMP habilitado y las comunidades creadas**, tu jefe no necesita tocar nada más en la consola del switch; solo debe agregarlo en la web de Observium:

1. En el navegador, ir a la pestaña **`Observium - Dashboard`** (`http://192.168.225.21`).
2. Menú superior: **Devices ➔ Add Device**.
3. Completar el formulario con estos datos exactos:
   * **Hostname / IP:** `192.168.210.1`
   * **SNMP Version:** `v2c`
   * **SNMP Community:** `TELENET` *(o probar con `Gp3b5_lK3xqxWv6`)*
   * **Transport:** `udp`
   * **Port:** `161`
4. Clic en **Add Device**.
5. Observium tardará unos segundos en realizar el *walk* SNMP, detectará el modelo **Allied Telesis x510L-28GT**, inventariará los 28 puertos de red físicos y comenzará a graficar tráfico de ancho de banda, CPU y temperatura.

---

## 9. Servidor de Precios y Estaciones de Servicio (`IBManager` - `192.168.225.20`)

Descubierto durante las tareas de administración y extracción de volcados de datos del negocio:

### 9.1 Ficha Técnica de Conexión
* **Dirección IP:** `192.168.225.20`
* **Sistema Operativo:** Linux
* **Acceso Administrativo:** SSH (Puerto 22)
* **Usuario:** `root`
* **Fingerprint ED25519 (SSH Key):**  
  `SHA256:KCFmo7I4U4dl59T1nvNIwHdOo82dchgtHjFKTn/l56s`
* **Software / ERP Asociado:** `IBManager` (Gestión comercial, precios y estaciones de servicio).

### 9.2 Volcados de Base de Datos y Estructura de Precios
El servidor genera volcados temporales de base de datos en `/tmp/` para tareas de mantenimiento, backups previos a cambios o sincronización masiva de precios de combustibles:

* **Archivo Maestro:** `/tmp/price.csv` (~61 MB).
* **Directorio de Tablas Comprimidas:** `/tmp/export_price/` (29 archivos `.csv.gz`):
  * `CustomerServiceStationPriceRow.csv.gz` y `CustomerServiceStationPrice.csv.gz`: Precios pactados por cliente y estación de servicio.
  * `ServiceStationsPriceRow.csv.gz`: Precios específicos de los servicentros.
  * `ThirdGasStationPriceList.csv.gz`: Listas de precios aplicables a estaciones tercerizadas.
  * `DeliveryNLTPrices.csv.gz` y `DeliveryNLTPricesRow.csv.gz`: Fletes y tarifas logísticas de entrega de combustible.
  * `ChangePrice.csv.gz` y `ChangePriceItemRow.csv.gz`: Trazabilidad y registros de cambios de precios.
  * `PriceFormula.csv.gz` y `BasePriceFormula.csv.gz`: Fórmulas matemáticas de cálculo de márgenes y precios.
  * `DiscountDealPriceDealRow.csv.gz`: Acuerdos de descuentos y condiciones de pago.

### 9.3 Procedimiento Operativo de Extracción (SCP)
Para transferir estos volcados de forma segura a una estación de trabajo de administración:

```powershell
# Descarga del archivo maestro de precios
scp root@192.168.225.20:/tmp/price.csv C:\Users\aliado\Desktop\

# Descarga recursiva del directorio completo de tablas comprimidas
scp -r root@192.168.225.20:/tmp/export_price C:\Users\aliado\Desktop\
```

> [!WARNING]
> **Higiene de Almacenamiento en `/tmp`:**  
> Debido a que los volcados en `/tmp/` superan los 75 MB entre archivos planos y comprimidos, se debe verificar periódicamente que los scripts de exportación purguen los temporales antiguos para evitar que la partición raíz `/` del servidor `192.168.225.20` se quede sin espacio disponible.
