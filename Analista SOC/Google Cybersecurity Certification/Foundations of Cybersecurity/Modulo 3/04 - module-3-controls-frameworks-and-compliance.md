# Lectura: Controls, frameworks, and compliance

Anteriormente, introdujimos los marcos de seguridad (*frameworks*) y cómo proporcionan un enfoque estructurado. En esta lectura, aprenderás más sobre cómo los marcos de seguridad, los controles y las regulaciones de **cumplimiento normativo** (*compliance*, es decir, las leyes) se entrelazan para gestionar la seguridad y minimizar el riesgo legal y técnico de la empresa.

## Cómo se relacionan: CIA, Frameworks, Controles y Compliance

- **La Tríada CIA:** Es el modelo matemático y filosófico base. Confidencialidad, Integridad y Disponibilidad son los tres principios rectores.
- **Controles:** Basándose en la tríada CIA, el analista instala controles de seguridad (salvaguardas físicas o lógicas, como un lector de huellas o un *firewall*) para reducir un riesgo específico.
- **Frameworks:** Los controles no se instalan al azar. Se instalan siguiendo los lineamientos de un Marco de Seguridad (*Framework*) para garantizar que se construya una defensa estructurada.
- **Compliance (Cumplimiento):** El objetivo final de seguir un framework e instalar controles es lograr el *Cumplimiento*. El cumplimiento es el acto legal de demostrar ante el gobierno que la empresa se adhiere a las leyes externas de privacidad de datos.

## Leyes, Estándares y Frameworks Específicos que debes conocer

El Instituto Nacional de Estándares y Tecnología (**NIST**) es la agencia de EE. UU. que desarrolla los marcos más famosos a nivel mundial, como el **NIST CSF** (Marco de Ciberseguridad) y el **NIST RMF** (Marco de Gestión de Riesgos).

Además de NIST, existen otras leyes y estándares obligatorios que todo analista SOC debe conocer de memoria:

### 1. GDPR (Reglamento General de Protección de Datos)
Es la ley de privacidad más estricta del mundo, dictada por la **Unión Europea (UE)**. Protege los datos de los residentes europeos. Tiene un peso inmenso porque aplica a *cualquier* empresa del mundo que maneje datos de europeos. Si ocurre una brecha de datos, el GDPR obliga a la corporación a notificar al ciudadano afectado en un **plazo máximo de 72 horas**. Ocultar el hackeo resulta en multas devastadoras.

### 2. PCI DSS (Estándar de Seguridad de Datos para la Industria de Tarjetas de Pago)
No es una ley gubernamental, sino un estándar internacional privado creado por Visa, Mastercard, etc. Regula estrictamente a cualquier organización que almacene, procese o transmita **información de tarjetas de crédito**. Su objetivo es erradicar la clonación y el fraude. Si una empresa no cumple PCI DSS, los bancos le cortan el derecho a procesar pagos electrónicos.

### 3. HIPAA (Ley de Responsabilidad y Portabilidad del Seguro Médico)
Es una severa ley federal de EE. UU. que protege la **Información de Salud Protegida (PHI)** de los pacientes (historiales médicos, tratamientos, pagos). Prohíbe compartir datos médicos sin consentimiento. Las bases de datos de los hospitales son un blanco hiper-lucrativo para los atacantes porque los historiales médicos se venden muy caros en la *Dark Web* para cometer fraude de seguros. 
*(Nota: El marco de trabajo que usan los hospitales para cumplir la ley HIPAA se llama **HITRUST**).*

### 4. FedRAMP
El Programa Federal de Gestión de Riesgos y Autorizaciones es un estándar del gobierno de EE. UU. que regula exclusivamente cómo se debe evaluar y asegurar la información que se almacena en **servicios en la Nube (*Cloud*)**.

### 5. CIS (Center for Internet Security)
*CIS* es una organización sin fines de lucro muy respetada. Proporciona los famosos **"Controles CIS"**, un conjunto táctico de medidas y controles de seguridad procesables (ej. "Desactivar puertos USB") que las empresas implementan directamente en sus sistemas operativos para bloquear ataques.

### 6. FERC-NERC
Regulación estricta que aplica a organizaciones que manejan redes e Infraestructura Crítica, específicamente **redes eléctricas y de energía** en Norteamérica, para evitar que un ciberataque apague el país.

### 7. SOC 1 y SOC 2 (System and Organizations Controls)
Desarrollados por el Instituto de Contadores Públicos de EE. UU. (AICPA), los informes SOC son auditorías profundas. Un reporte SOC 2 evalúa estrictamente las políticas de acceso de usuarios de una empresa, verificando que la Confidencialidad y Privacidad se cumplan a nivel financiero para evitar fraudes internos.

### 8. ISO (Organización Internacional de Normalización)
ISO establece estándares internacionales para todo tipo de industrias, cruzando fronteras para unificar procesos de tecnología y manufactura a nivel mundial (ej. las normas ISO 27001 para la seguridad de la información).

---

## Puntos Clave (Key Takeaways)
- **Compliance (Cumplimiento):** Es el acto de acatar las leyes. No es opcional. Un analista de seguridad trabaja para mantener a la empresa en *compliance* y evitar multas o el cierre del negocio.
- **GDPR = Europa.** Exige reportar los hackeos en menos de 72 horas.
- **PCI DSS = Tarjetas de Crédito.**
- **HIPAA = Hospitales y Salud.** Protege la PHI (Información de salud).
