# Lectura: Más sobre los Principios de Seguridad de OWASP

Anteriormente, aprendiste que los analistas de ciberseguridad ayudan a mantener a salvo los datos y a reducir los riesgos dentro de una organización mediante el uso de una variedad de frameworks, controles y principios de diseño. En esta lectura complementaria preparada por los expertos de Google, profundizaremos en otros principios fundamentales de OWASP —proyecto recientemente renombrado como **Open Worldwide Application Security Project®**— y analizaremos cómo los analistas de nivel inicial (*entry-level*) los aplican en el entorno laboral de manera cotidiana.

---

## Los Principios de Seguridad en el Día a Día

En el espacio de trabajo real, los principios de ciberseguridad no son solo teoría; están completamente integrados en tus tareas diarias. Ya sea que te encuentres analizando *logs*, monitoreando un panel de control de **Gestión de Información y Eventos de Seguridad** (*SIEM dashboard*) o ejecutando un escáner de vulnerabilidades (*vulnerability scanner*), estarás aplicando estos conceptos de manera directa o indirecta para proteger las operaciones comerciales.

Como breve recordatorio, los seis principios esenciales de OWASP que revisamos anteriormente son:
*   **Minimizar la superficie de ataque** (*Minimize attack surface area*)
*   **Principio del menor privilegio** (*Principle of least privilege*)
*   **Defensa en profundidad** (*Defense in depth*)
*   **Separación de funciones** (*Separation of duties*)
*   **Mantener la seguridad simple** (*Keep security simple*)
*   **Corregir los problemas de seguridad correctamente** (*Fix security issues correctly*)

---

## Cuatro Principios Adicionales de OWASP

A continuación, exploraremos cuatro directrices avanzadas de OWASP que los equipos de ciberseguridad utilizan para salvaguardar a los usuarios y la continuidad del negocio:

### 1. Establecer Valores por Defecto Seguros (*Establish secure defaults*)
Este principio establece que el estado de seguridad óptimo y más restrictivo de una aplicación debe ser también su configuración predeterminada de fábrica para todos los usuarios. En otras palabras, un usuario no debería tener que configurar activamente la seguridad para estar protegido; por el contrario, debería requerir un esfuerzo o trabajo adicional realizar una acción que vuelva a la aplicación insegura.

### 2. Fallar de Forma Segura (*Fail securely*)
Significa que cuando un control o mecanismo de seguridad experimenta una falla técnica, se corrompe o deja de funcionar, debe hacerlo de tal manera que el sistema elija automáticamente la opción más segura disponible para proteger la infraestructura.

> [!IMPORTANT]
> Un ejemplo clásico ocurre con los *firewalls*: si un *firewall* crítico llega a fallar o sufre una interrupción en sus servicios, su comportamiento por defecto seguro debe ser **cerrar por completo todas las conexiones activas y bloquear cualquier nueva solicitud de tráfico**, en lugar de abrirse y permitir que todo el tráfico pase sin supervisión a la red interna.

### 3. No Confiar en Servicios Externos (*Don't trust services*)
Hoy en día, la gran mayoría de las empresas colaboran estrechamente con socios comerciales y proveedores de servicios de terceros (*third-party vendors*). Estas organizaciones externas suelen manejar políticas y estándares de ciberseguridad completamente distintos a los de tu empresa. Por lo tanto, nunca se debe asumir explícitamente que los sistemas de un tercero son 100 % seguros.

*   **Caso práctico:** Si una aerolínea utiliza un proveedor externo para rastrear y gestionar los puntos de recompensa de sus clientes frecuentes, la aerolínea tiene la obligación de validar rigurosamente que el balance de puntos sea exacto y verídico mediante sus propios controles antes de mostrar y compartir esa información en su plataforma con los usuarios finales.

### 4. Evitar la Seguridad por Oscuridad (*Avoid security by obscurity*)
La seguridad de los sistemas clave y las aplicaciones críticas jamás debe depender de mantener ocultos sus detalles de diseño o funcionamiento interno. De acuerdo con las pautas de OWASP, el hecho de que un atacante no conozca cómo funciona un software no lo hace seguro.

> [!NOTE]
> La seguridad de una aplicación no debe basarse en mantener el código fuente (*source code*) en secreto. Su protección real debe sustentarse en la combinación de múltiples factores auditables y robustos, tales como políticas de contraseñas exigentes, una estrategia sólida de defensa en profundidad, límites en las transacciones comerciales, una arquitectura de red transparente y controles estrictos contra el fraude.

---

## Puntos Clave (Key Takeaways)

*   **Aplicación Continua:** Los profesionales de ciberseguridad aplican constantemente estos principios de diseño para salvaguardar la confidencialidad, integridad y disponibilidad de las empresas y las personas a las que sirven.
*   **Diseño Seguro por Defecto:** Configurar las aplicaciones con valores por defecto restrictivos garantiza que los usuarios finales estén protegidos desde el primer momento sin necesidad de realizar ajustes manuales.
*   **Resiliencia ante Fallas:** El principio de fallar de forma segura (como el bloqueo automático de un *firewall* ante una caída de servicio) evita que los problemas de disponibilidad comprometan la integridad de la red.
*   **Verificación de Terceros:** Adoptar una postura de desconfianza ante servicios externos mitiga los riesgos de la cadena de suministro y previene la propagación de datos corruptos o vulnerables.
*   **Transparencia Técnica:** Evitar la seguridad por oscuridad obliga a las organizaciones a construir infraestructuras sólidas que resistan ataques incluso si el código fuente o la arquitectura llegan a ser expuestos públicamente.
