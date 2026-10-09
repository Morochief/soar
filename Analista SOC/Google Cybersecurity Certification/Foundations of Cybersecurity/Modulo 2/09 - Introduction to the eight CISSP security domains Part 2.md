# Introduction to the eight CISSP security domains, Part 2

## Los Ocho Dominios de CISSP (Parte 2)
¡Bienvenido de nuevo! En el apunte anterior cubrimos los primeros cuatro dominios. En este video, te presentaremos los últimos cuatro. 

Comprender en qué dominio encaja tu trabajo te ayudará enormemente en futuras entrevistas laborales. Dependiendo del tamaño de la empresa corporativa, tu rol como analista puede ubicarse en la intersección de múltiples dominios (en empresas pequeñas) o enfocarse con precisión láser en uno solo específico (en multinacionales).

## Dominio 5: Gestión de Identidad y Acceso (*Identity and Access Management - IAM*)
El quinto dominio se centra exclusivamente en el control de accesos. Garantiza que solo los usuarios autorizados tengan entrada a los activos lógicos (software, redes, bases de datos) y a los activos físicos (salas de servidores, oficinas privadas).

**Ejemplo de Rol:** Validar de forma estricta las identidades de los empleados. Como analista, tu tarea podría ser configurar tarjetas magnéticas (*keycards*) o *tokens* de seguridad para otorgar o revocar el acceso físico de los empleados al edificio corporativo tras un despido.

## Dominio 6: Evaluación y Pruebas de Seguridad (*Security Assessment and Testing*)
Este dominio se enfoca en auditar la red. Consiste en realizar pruebas periódicas de control, ejecutar escáneres de vulnerabilidades, y realizar **auditorías de seguridad** para confirmar que las defensas sigan siendo efectivas con el paso del tiempo.

> [!NOTE]
> **Ejemplo de Rol:** Realizar auditorías de permisos de usuario para aplicar el Principio de Privilegio Mínimo. Por ejemplo, el acceso al sistema de nóminas (*payroll*) debe limitarse estrictamente a Recursos Humanos. Un analista audita regularmente el sistema para garantizar que, por error o ataque, ningún otro empleado tenga permisos para ver los salarios de la compañía.

## Dominio 7: Operaciones de Seguridad (*Security Operations*)
El dominio siete es el hogar tradicional de los analistas SOC. Se centra en el día a día: el monitoreo continuo de la red, la investigación activa de amenazas y la respuesta a incidentes en tiempo real.

**Ejemplo de Rol:** Recibes una alerta crítica (*alert*) de que un dispositivo desconocido y no autenticado acaba de conectarse por cable a la red interna corporativa. Aplicando los procedimientos de operaciones de seguridad de tu organización, deberás investigar los registros de la red y aislar el dispositivo inmediatamente para detener una potencial brecha de datos.

## Dominio 8: Seguridad en el Desarrollo de Software (*Software Development Security*)
El octavo y último dominio busca introducir la ciberseguridad en la etapa de programación (*DevSecOps*). Se enfoca en exigir prácticas de codificación segura (*secure coding practices*) para crear aplicaciones blindadas contra vulnerabilidades antes de que salgan al mercado.

**Ejemplo de Rol:** Trabajar como puente entre el equipo de Seguridad y los Programadores. Si tu empresa está creando una nueva app bancaria para teléfonos, tu rol será asesorarlos en cómo almacenar las contraseñas criptográficamente en la base de datos o asegurar que ninguna información de tarjeta de crédito (SPII) viaje en texto plano por internet.

## Puntos Clave (Key Takeaways)
- **Dominio 5 (IAM):** Controla la autenticación y los permisos. Decide *quién* puede entrar a *dónde* (tanto en software como mediante puertas físicas con llaves magnéticas).
- **Dominio 6 (Auditoría y Pruebas):** Busca debilidades en la propia empresa mediante revisiones de permisos y pruebas de estrés (*pentesting*).
- **Dominio 7 (Operaciones / SOC):** El centro de mando de primera línea. Monitorea las herramientas defensivas, recibe alertas e investiga dispositivos sospechosos en la red.
- **Dominio 8 (Desarrollo):** Asegura que el código y el software que la empresa fabrica nazcan sin vulnerabilidades, asesorando a los programadores.
