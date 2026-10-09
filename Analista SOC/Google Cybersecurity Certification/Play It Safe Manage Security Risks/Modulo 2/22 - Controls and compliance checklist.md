# Botium Toys: Lista de Verificación de Controles y Cumplimiento (Controls and Compliance Checklist)

¡Hola de nuevo! Como analista de ciberseguridad, una vez que has comprendido el alcance, los objetivos estratégicas y el reporte de riesgos de **Botium Toys**, el siguiente paso operativo consiste en ejecutar formalmente la auditoría técnica. Para ello, completaremos la **Lista de Verificación de Controles y Cumplimiento** utilizando toda la telemetría e información recopilada en los análisis anteriores.

Esta lista de verificación te permitirá identificar con precisión las brechas lógicas, físicas y normativas de la organización, sirviendo como entregable clave para tu portafolio profesional del *Google Cybersecurity Certificate*.

---

## 1. Lista de Verificación de Evaluación de Controles (Controls Assessment Checklist)

A continuación, se presenta la clasificación técnica de las salvaguardas actuales de Botium Toys. Para cada control, se determina si se encuentra actualmente activo (`Sí`) o inactivo/ausente (`No`).

| ¿Implementado? | Control de Seguridad | Categoría del Control | Tipo de Control | Propósito Operativo |
| :---: | :--- | :--- | :--- | :--- |
| **[ ] Sí <br> [x] No** | **Menor Privilegio** (*Least Privilege*) | Administrativo | Preventivo | Restringir el acceso masivo de empleados a datos financieros y *PII/SPII*. |
| **[ ] Sí <br> [x] No** | **Planes de Recuperación ante Desastres** (*Disaster recovery*) | Administrativo | Correctivo | Asegurar la continuidad del negocio y resiliencia operativa tras un incidente grave. |
| **[x] Sí <br> [ ] No** | **Políticas de Contraseñas** (*Password policies*) | Administrativo | Preventivo | Cuenta con una política elemental (nominal), aunque requiere actualización urgente. |
| **[ ] Sí <br> [x] No** | **Separación de Funciones** (*Separation of duties*) | Administrativo | Preventivo | Evitar fraudes internos segmentando las responsabilidades y privilegios del sistema. |
| **[x] Sí <br> [ ] No** | **Firewall** | Técnico | Preventivo | Filtrar el tráfico de red entrante según reglas de seguridad validadas. |
| **[ ] Sí <br> [x] No** | **Sistema de Detección de Intrusos (IDS)** | Técnico | Detectivo | Monitorear proactivamente la red interna contra firmas de ataques o anomalías. |
| **[ ] Sí <br> [x] No** | **Copias de Seguridad** (*Backups*) | Técnico | Correctivo | Respaldar la información comercial crítica para permitir su restauración inmediata. |
| **[x] Sí <br> [ ] No** | **Software Antivirus** | Técnico | Preventivo | Escanear, aislar y poner en cuarentena amenazas de *malware* conocidas. |
| **[x] Sí <br> [ ] No** | **Monitoreo y Mantenimiento de Sistemas Heredados** | Técnico | Preventivo | Supervisión humana de plataformas *legacy* (vulnerables) sin calendario fijo. |
| **[ ] Sí <br> [x] No** | **Cifrado** (*Encryption*) | Técnico | Disuasorio | Proteger de forma matemática la confidencialidad de tarjetas de crédito locales. |
| **[ ] Sí <br> [x] No** | **Sistema de Gestión de Contraseñas** | Técnico | Preventivo | Centralizar credenciales, mitigar la fatiga de contraseñas y forzar la complejidad. |
| **[x] Sí <br> [ ] No** | **Cerraduras / Candados** (*Locks*) | Físico | Preventivo | Restringir el paso de personal no autorizado a oficinas, fachada y almacén. |
| **[x] Sí <br> [ ] No** | **Vigilancia por Circuito Cerrado (CCTV)** | Físico | Preventivo / Detectivo | Disuadir intrusiones físicas y aportar análisis forense post-incidente. |
| **[x] Sí <br> [ ] No** | **Detección y Prevención de Incendios** | Físico | Preventivo / Detectivo | Mitigar daños materiales en servidores e inventario mediante alarmas y aspersores. |

---

## 2. Lista de Verificación de Cumplimiento Normativo (Compliance Checklist)

Evaluación del estado de adhesión de Botium Toys frente a las leyes internacionales de privacidad de datos y los estándares de la industria de pagos electrónicos.

### Estándar de Seguridad de Datos para la Industria de Tarjetas de Pago (PCI DSS)
> [!IMPORTANT]
> Debido a que Botium Toys acepta y procesa pagos con tarjetas de crédito en su tienda en línea en expansión, este estándar técnico es de cumplimiento legal obligatorio.

*   **[ ] Sí <br> [x] No** | Únicamente los usuarios autorizados tienen acceso a la información de las tarjetas de crédito de los clientes.
*   **[ ] Sí <br> [x] No** | La información de las tarjetas de crédito se almacena, acepta, procesa y transmite internamente en un entorno seguro.
*   **[ ] Sí <br> [x] No** | Se implementan procedimientos de cifrado de datos (*data encryption*) para asegurar los puntos de contacto de las transacciones con tarjeta.
*   **[ ] Sí <br> [x] No** | Se adoptan políticas robustas y seguras de gestión de contraseñas corporativas.

### Reglamento General de Protección de Datos (GDPR)
> [!IMPORTANT]
> Al expandir su mercado hacia la Unión Europea (U.E.), Botium Toys debe salvaguardar obligatoriamente los derechos de privacidad de los ciudadanos europeos bajo esta ley internacional.

*   **[ ] Sí <br> [x] No** | Los datos de los clientes de la U.E. se mantienen completamente privados y asegurados.
*   **[x] Sí <br> [ ] No** | Existe un plan de contingencia implementado para notificar a los clientes de la U.E. dentro de las 72 horas en caso de una brecha de seguridad (*security breach*).
*   **[ ] Sí <br> [x] No** | Se garantiza que los datos estén clasificados e inventariados de manera adecuada (Función *Identify* de NIST CSF).
*   **[x] Sí <br> [ ] No** | Se aplican y hacen cumplir políticas, procedimientos y procesos de privacidad para documentar y mantener los datos correctamente.

### Controles de Sistemas y Organizaciones (SOC Tipo 1, SOC Tipo 2)
*   **[ ] Sí <br> [x] No** | Se han establecido formalmente políticas robustas de acceso de usuarios (*user access policies*).
*   **[ ] Sí <br> [x] No** | Los datos sensibles (información de identificación personal *PII* / información personal sensible *SPII*) son confidenciales y privados.
*   **[x] Sí <br> [ ] No** | La integridad de los datos garantiza que la información sea consistente, completa, precisa y validada.
*   **[x] Sí <br> [ ] No** | Los datos se encuentran totalmente disponibles para aquellas personas autorizadas a acceder a ellos.

---

## 3. Resumen de Recomendaciones Técnicas (Recommendations)

A continuación, se detallan las recomendaciones de ingeniería que la gerencia de IT puede comunicar formalmente a los *stakeholders* para mitigar los riesgos críticos y elevar la postura de seguridad corporativa:

*   **Implementación Inmediata de Controles de Acceso Lógicos:** Desplegar de forma prioritaria el principio del menor privilegio y la separación de funciones. Todo el personal administrativo y de almacén debe perder de inmediato el acceso masivo a la base de datos de tarjetas de crédito y *PII/SPII*.
*   **Adopción de un Gestor Centralizado de Contraseñas:** Integrar un sistema centralizado que fuerce de manera estricta los requisitos de complejidad modernos (mínimo 12 caracteres, alfanuméricos y caracteres especiales), erradicando la fatiga de contraseñas y optimizando los *tickets* de soporte de IT.
*   **Despliegue de Tecnologías de Cifrado (Encryption):** Implementar cifrado tanto para los datos en tránsito (protocolos HTTPS/TLS en el portal de *ecommerce*) como para los datos en reposo (cifrado de la base de datos local donde se procesa la información financiera).
*   **Activación de Resiliencia Operativa y Monitoreo:** Instalar un Sistema de Detección de Intrusos (IDS) en la red interna para ganar visibilidad ante amenazas latentes, trazar un plan formal de recuperación ante desastres (*disaster recovery plan*) y calendarizar copias de seguridad (*backups*) automatizadas y redundantes de los datos críticos de la empresa.

---

## Puntos Clave (Key Takeaways)

*   **Brecha Diagnosticada:** Botium Toys cuenta con controles físicos robustos (CCTV, cerraduras, sistemas contra incendios), pero adolece de controles lógicos y técnicos críticos en su infraestructura digital.
*   **Incumplimiento de PCI DSS:** La falta de cifrado local y el acceso masivo de empleados a datos financieros colocan a la empresa en una postura de alto riesgo de sanción económica.
*   **Riesgo Legal Internacional (GDPR):** Aunque existen políticas de privacidad y un plan de notificación de 72 horas, la falta de control técnico sobre los datos de ciudadanos de la U.E. representa un peligro inminente de penalización legal.
*   **Plan de Mitigación Urgente:** El enfoque a corto plazo debe centrarse en restringir privilegios, implementar cifrado y asegurar la disponibilidad de la información mediante un plan sólido de copias de seguridad.
