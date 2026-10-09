# 📘 Guía Oficial de Instalación: Stellar Cyber Windows Server Sensor en Active Directory

**Versión:** 1.0
**Entorno Objetivo:** Controlador de Dominio (Windows Server)
**Integraciones Asumidas:** Cortex XDR (Endpoint Protection)

---

## 🎯 1. Propósito y Beneficios
La instalación del agente nativo de Stellar Cyber (*Windows Server Sensor*) en un Controlador de Dominio (AD) es una de las configuraciones de mayor valor para un SOC. 

Al tener visibilidad directa sobre el AD, Stellar Cyber **enriquece automáticamente todos los flujos de red**. Esto significa que cuando veas una alerta de una IP (`ej. 192.168.169.103`), el XDR sabrá exactamente qué usuario del dominio está conectado a esa IP en ese instante, acelerando drásticamente la investigación.

### ⚠️ Consideración Arquitectónica: Cortex XDR vs Sysmon
Dado que el Controlador de Dominio ya está protegido por **Cortex XDR**, **NO ES NECESARIO instalar Sysmon**. 
* Cortex XDR ya intercepta y registra a nivel de kernel toda la telemetría avanzada (creación de procesos, conexiones de red por PID, comandos ofuscados, inyecciones de memoria) y proporciona capacidades de bloqueo activo.
* Instalar Sysmon de forma simultánea generaría duplicación de logs, consumo innecesario de CPU y fatiga de almacenamiento. El agente de Stellar Cyber se enfocará exclusivamente en los **Windows Event Logs de Seguridad** y dejará la telemetría cruda al EDR.

---

## 🛠️ 2. Prerrequisitos y Mejores Prácticas Previas

1. **Recursos Mínimos del AD:** 2 vCPU, 8 GB RAM, 5 GB SSD libre (Recomendado 8 GB).
2. **Actualización de Sistema:** Asegúrese de instalar todos los parches de *Windows Update* pendientes antes de iniciar.
3. **Energía (Crítico):** El servidor debe tener configurado el plan de energía para que **nunca hiberne ni entre en suspensión (Never sleep)**. Si el servidor suspende, el sensor pierde conexión y la recolección de datos se detiene.
4. **Firewall Perimetral/Local:** Asegúrese de que el AD tenga salida HTTPS (TCP 443) y TCP 8889 hacia el *Data Processor (DP)* de Stellar Cyber (la consola cloud/on-prem).

---

## 🛡️ 3. Fase Crítica: Exclusiones en Cortex XDR

Para evitar que Cortex XDR bloquee los servicios del agente de Stellar Cyber (lo cual es un falso positivo operativo muy común, conocido como *Fuego Amigo*), debe configurar **exclusiones de tipo "File or Folder"** en la política de Cortex antes de la instalación.

Agregue estas rutas exactas a las exclusiones globales de escaneo en tiempo real (Real-Time Protection):
* `C:\ProgramData\Stellarcyber\*`
* `C:\Program Files\Aella\*`

> [!NOTE]
> **Falso Positivo Esperado:** Durante la instalación, Cortex XDR o sistemas similares pueden lanzar una alerta de *"Attempted LSASS access by aella_conf_win_srv.exe detected"*. El fabricante (Stellar Cyber) confirma que esto es un falso positivo y que el servicio de configuración no compromete `lsass.exe`.

---

## 📥 4. Fase de Descarga y Preparación

1. Inicie sesión en la consola principal de Stellar Cyber.
2. Navegue a **System | DATA SOURCE MANAGEMENT | Sensors | Sensor Installation**.
3. En la pestaña **Download Image**:
   * Seleccione **Windows Server Sensor** en el menú desplegable.
   * Haga clic en **Download**. Esto bajará un archivo `.msi`.
4. Transfiera el archivo `.msi` de manera segura al servidor del Controlador de Dominio.
5. Haga clic derecho sobre el archivo `.msi` en el AD, seleccione **Propiedades**. Si en la pestaña General aparece un cuadro de seguridad que dice **"Desbloquear" (Unblock)**, márquelo y haga clic en Aplicar/Aceptar.

## 🔑 5. Generación del Token de Instalación

El agente necesita un "Token" para saber a qué Tenant pertenece y cómo autenticarse con la nube.

1. En la consola de Stellar Cyber, en la misma página de *Sensor Installation*, vaya a la pestaña **Tokens**.
2. Haga clic en **Generate**.
3. Complete el formulario:
   * **Tenant:** Seleccione el tenant correspondiente (ej. `technoma` o `cajaande`).
   * **Sensor Profile:** Seleccione el perfil de Windows Server si existe, o déjelo en `None`.
   * **Expiration:** Por seguridad, establezca una caducidad (ej. 2 semanas o 3 meses). El token solo se usa durante la instalación; si expira después, el agente sigue funcionando sin problemas.
4. **Copie el string del token** generado (Copy to clipboard).

---

## 🚀 6. Fase de Instalación en el Active Directory

1. Ejecute el archivo `.msi` en el servidor AD. Acepte cualquier prompt de seguridad de *User Account Control (UAC)*.
2. Haga clic en **Next** en la pantalla de bienvenida.
3. El instalador sugerirá la ruta `C:\Program Files\Aella\`. **No la cambie.** Las rutas personalizadas no están soportadas. Haga clic en **Next**.
4. En la pantalla de Autorización, elija la opción **Token**.
5. **Pegue el Token** que copió en la Fase 5 en el cuadro de texto. 
   *(Nota: No utilice las opciones "CM", son para infraestructuras legacy pre-v5.x).*
6. Si su red requiere pasar por un Aggregator, puede poner su IP en "Primary Aggregator" (Opcional). De lo contrario, déjelo en blanco.
7. Haga clic en **Install**.
8. **IMPORTANTE:** Es posible que se abra una ventana negra de consola (CMD) durante el proceso. **NO la cierre manualmente**, el wizard la cerrará sola al terminar.
9. Haga clic en **Finish**.

---

## ✅ 7. Verificación de Éxito

### En el Servidor AD local:
1. Abra los Servicios de Windows (`services.msc`).
2. Verifique que los servicios `Windows Agent Sensor Ctrl` y `Windows Agent Sensor Conf` estén en estado **Running (En ejecución)**.

### En la consola de Stellar Cyber:
1. Vaya a **System | DATA SOURCE MANAGEMENT | Sensors | Sensors**.
2. Busque el nombre de su servidor AD en la lista (ej. `ad.technoma.local`).
3. El estado general debe estar en **verde (Activo)**, confirmando que la telemetría de autenticación y seguridad ya está viajando hacia el Data Processor.

---

> [!TIP]
> **Mantenimiento a Futuro:** El agente de Stellar Cyber se actualiza de manera centralizada desde la consola cloud. Las exclusiones de carpetas configuradas en la Fase 3 garantizan que estas futuras actualizaciones automáticas no sean bloqueadas por Cortex XDR.
