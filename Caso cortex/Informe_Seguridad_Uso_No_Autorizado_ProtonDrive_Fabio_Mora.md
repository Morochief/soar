# 🔒 INFORME TÉCNICO DE SEGURIDAD DE LA INFORMACIÓN
**Referencia:** INC-SEC-2026-1015-FMORA  
**Fecha:** 15 de Octubre de 2026  
**Para:** Jefatura de Seguridad de la Información / Gerencia de TI  
**De:** Kevin Moraes — Analista SOC (Centro de Operaciones de Seguridad)  
**Asunto:** Notificación de Incumplimiento de Política de Seguridad: Instalación de Software No Autorizado (*Shadow IT*) y Transferencia Masiva a Nube Externa (*Proton Drive*)

---

## 1. Resumen Ejecutivo

El Centro de Operaciones de Seguridad (SOC), a través de la plataforma **Palo Alto Networks Cortex XDR**, identificó un comportamiento anómalo de transferencia masiva de datos originado en la estación de trabajo corporativa **`NB-FMORA`**, asignada al colaborador **Fabio Mora**.

Durante el fin de semana del **12 al 13 de octubre de 2026**, el endpoint transfirió **10.2 GB de datos** hacia los servidores de almacenamiento cifrado de **Proton AG** en Frankfurt, Alemania (`fra-storage.proton.me`). La auditoría pericial confirmó la instalación y ejecución local de un aplicativo de sincronización en la nube no corporativo (**Proton Drive**).

Si bien la revisión forense preliminar determinó que la información transferida consistía en archivos de laboratorios técnicos y máquinas virtuales (para estudio personal), **el incidente constituye una falta a las políticas corporativas de seguridad y protección de datos**, exponiendo a la organización a riesgos severos de fuga de información no supervisada (*Data Loss Prevention - DLP*).

---

## 2. Detalle del Activo y Telemetría Forense

| Parámetro | Detalle Técnico |
| :--- | :--- |
| **Colaborador / Usuario** | Fabio Mora (`TECHNOMA\fabiomora`) |
| **Equipo Involucrado** | Notebook Corporativa `NB-FMORA` |
| **Direcciones IP Asociadas** | `192.168.100.1` / `172.22.16.1` / `192.168.23.1` |
| **Software Identificado** | `ProtonDrive.exe` (Versión Windows Client) |
| **Ruta de Ejecución** | `C:\Users\fabiomora\AppData\Local\Proton\ProtonDrive\` |
| **Destino de Red** | `fra-storage.proton.me` (`185.205.70.10` - Proton AG, Alemania) |
| **Volumen Transferido** | **10.2 GB** en 608 sesiones TLS (Puerto 443) |
| **Carpeta Sincronizada** | `C:\Users\fabiomora\Downloads\Mis cosas\` |

### Conciliación Forense del Contenido:
1. **Evidencias en Disco:** Se constató la presencia de imágenes de disco `.iso` y plantillas de máquinas virtuales `.ova` dentro de la carpeta sincronizada, cuyo tamaño acumulado totalizó exactamente **10.2 GB**, cuadrando de manera unívoca con el tráfico auditado por Cortex XDR.
2. **Evidencia de Alta de Cuenta:** Se localizó en el mismo directorio el archivo `proton-recovery-phrase.pdf` (documento de clave de recuperación generado automáticamente por Proton al registrar una cuenta personal) con fecha de creación del **13/10/2026 a las 06:18 AM**.
3. **Resultado del Análisis de Datos:** No se hallaron indicios de exfiltración intencional de bases de datos, credenciales corporativas ni archivos clasificados de clientes en este lote en particular.

---

## 3. Vulneración de Políticas y Riesgos para la Empresa

A pesar de que el contenido analizado corresponde a material formativo, se enfatizan las siguientes **contingencias y faltas críticas**:

### A. Uso de Herramientas de *Shadow IT* (Software No Homologado)
La instalación de clientes de almacenamiento en la nube sin autorización explícita de TI evade los controles de inventario y gestión de activos. Los aplicativos instalados en `%LocalAppData%` representan un vector ciego que no puede ser gestionado centralizadamente.

### B. Riesgo Crítico de Fuga de Datos (DLP)
Los servicios de almacenamiento personal como **Proton Drive** emplean **cifrado de extremo a extremo (*zero-knowledge encryption*)**, lo que impide la inspección profunda de paquetes por parte de los firewalls corporativos. Si un endpoint tiene acceso a sincronizar carpetas arbitrarias hacia una nube privada:
* Se pierde la trazabilidad de qué información sale de la empresa.
* Se incrementa drásticamente el riesgo de exposición de datos confidenciales de clientes, proyectos, configuraciones de red o contratos.
* Se expone a la compañía a responsabilidades legales y regulatorias por custodia negligente de información sensible.

### C. Uso Indebido de Activos y Recursos Corporativos
Los equipos de cómputo y el ancho de banda empresarial están destinados con exclusividad a las funciones operativas y laborales del cargo. La sincronización masiva de archivos personales de gran volumen impacta negativamente en la capacidad de red y desvirtúa la finalidad del activo corporativo.

---

## 4. Medidas Requeridas y Acciones Correctivas

Para contener el riesgo y prevenir recurrencias, se solicita aplicar las siguientes disposiciones con carácter **inmediato**:

1. **Apercibimiento y Notificación al Colaborador:**
   * Notificar formalmente a **Fabio Mora** sobre la irregularidad detectada, recordando la vigencia irrestricta de las directivas de Confidencialidad y Uso Aceptable de Activos Tecnológicos.
   * Aclarar al colaborador que cualquier material de estudio o proyectos personales deben gestionarse en hardware y almacenamiento personal, no en la estación de trabajo de la empresa.
2. **Saneamiento Técnico del Endpoint (`NB-FMORA`):**
   * Desinstalación completa de `ProtonDrive.exe` y eliminación de residuos en `%LocalAppData%\Proton`.
   * Cierre y desvinculación de toda cuenta externa de almacenamiento en la nube personal.
3. **Medidas Técnicas de Bloqueo Global (SOC / TI):**
   * Creación de regla de bloqueo en Cortex XDR para impedir la ejecución de instaladores o ejecutables de sincronización de Proton, Mega, Telegram y plataformas no autorizadas.
   * Refuerzo de políticas perimetrales en el Firewall corporativo para denegar categorías de *Personal Cloud Storage*.

---

*Informe emitido de forma confidencial por el Área de Ciberseguridad / SOC para fines de gestión interna y cumplimiento normativo.*
