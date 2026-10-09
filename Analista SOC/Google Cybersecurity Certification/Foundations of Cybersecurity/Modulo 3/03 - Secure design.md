# Secure design

## Diseño Seguro: La Tríada CIA y NIST CSF
Anteriormente, discutimos la teoría de los marcos y controles en general. En este apunte, aprenderás sobre un framework muy específico y un modelo matemático fundamental que todas las organizaciones utilizan para guiar el diseño seguro de su infraestructura de red.

### El Modelo Fundacional: La Tríada CIA
La tríada CIA es el modelo fundamental absoluto de la ciberseguridad. Ayuda a dictaminar cómo las organizaciones deben considerar el riesgo al configurar sistemas y políticas. **CIA** significa Confidencialidad, Integridad y Disponibilidad (*Confidentiality, Integrity, and Availability*).

1. **Confidencialidad:** Significa que *solo los usuarios autorizados* pueden leer o acceder a datos específicos.
Por ejemplo, se deben establecer controles de acceso estrictos que definan quién debe y quién no debe tener acceso a las carpetas de recursos humanos para garantizar que la información salarial permanezca confidencial.
2. **Integridad:** Significa que los datos son correctos, auténticos y confiables (es decir, garantizan que nadie los haya modificado ni borrado sin permiso).
Para mantener la integridad de un archivo, los profesionales de seguridad utilizan mecanismos de protección como el cifrado criptográfico (*encryption*) o firmas *hash* para salvaguardar los datos y evitar que un atacante los altere durante el tránsito.
3. **Disponibilidad:** Significa que los datos están accesibles ininterrumpidamente (los servidores nunca se caen ni se apagan) para que el personal autorizado pueda consultarlos exactamente en el momento que los necesiten.

> [!NOTE]
> **Activo (*Asset*):** Durante la discusión de la tríada CIA siempre surge el concepto de proteger los "activos". Un activo es cualquier elemento tangible o digital que tenga valor para una organización. Su criticidad está determinada por el daño financiero que causaría perderlo. Una base de datos con cuentas bancarias es un activo crítico que requiere controles de seguridad inmensos, en comparación con un blog de noticias públicas de la empresa.

### El Estándar de Oro: NIST CSF
Ahora discutiremos un marco de trabajo (*framework*) de diseño seguro específico desarrollado por el Instituto Nacional de Estándares y Tecnología del gobierno de EE. UU. (NIST): el **Marco de Ciberseguridad del NIST**, conocido globalmente en la industria como el **NIST CSF**.

El NIST CSF es un marco gratuito y voluntario que consiste en un compendio exhaustivo de los mejores estándares, pautas y prácticas comprobadas del mundo para estructurar defensas de ciberseguridad. Es vital familiarizarse con este marco porque casi el 100% de los equipos SOC y empresas occidentales lo utilizan como plano base (*baseline*) para estructurar su defensa corporativa a largo plazo.

### Mitigación Práctica de Riesgos (Amenazas Internas)
Gestionar los riesgos para proteger los activos más valiosos de tu organización es tu objetivo diario como analista. Para ello, es clave comprender la psicología de los actores de amenazas.

Y los atacantes más letales para una corporación son las Amenazas Internas (*Insider Threats*), específicamente los **empleados descontentos** (*disgruntled employees*). Son los más peligrosos porque ya sortearon tus barreras externas, están sentados dentro de tu oficina, poseen credenciales válidas y saben exactamente dónde encontrar las bases de datos sensibles de la empresa.

Para reducir la amenaza de los empleados resentidos, los analistas de seguridad deben utilizar el Principio de Privilegio Mínimo (apoyándose en el pilar de la "Confidencialidad" de la Tríada CIA y las directrices administrativas del marco NIST). Esto asegura que a cada empleado se le restrinja el acceso por defecto y solo pueda acceder a los datos estrictamente necesarios para su tarea diaria.

---

## Puntos Clave (Key Takeaways)
- La **Tríada CIA** es el núcleo indiscutible de la ciberseguridad corporativa. Todo incidente busca destruir, y toda política busca proteger, al menos uno de sus pilares: Confidencialidad (evitar robo), Integridad (evitar alteración) o Disponibilidad (evitar caída del sistema).
- El **NIST CSF** es el framework defensivo más respetado y adoptado a nivel mundial. Es literalmente la receta oficial sobre cómo proteger una corporación.
- Un **Insider Threat** (como un administrador de TI que es despedido) es tu mayor riesgo de seguridad técnica, porque sus credenciales legítimas vuelven ciegos a tus *firewalls*.
