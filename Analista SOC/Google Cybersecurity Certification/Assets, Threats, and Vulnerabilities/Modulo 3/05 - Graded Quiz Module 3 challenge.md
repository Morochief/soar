# Graded Quiz: Module 3 challenge

**1. Una aplicación tiene controles de acceso rotos que no logran restringir a ningún usuario de crear nuevas cuentas. Esto permite que cualquier persona agregue nuevas cuentas con privilegios completos de administrador. Los controles de acceso rotos de la aplicación son un ejemplo de ¿qué?**
*(An application has broken access controls that fail to restrict any user from creating new accounts. This allows anyone to add new accounts with full admin privileges. The application’s broken access controls are an example of what?)*
- [x] Una vulnerabilidad *(A vulnerability)*
- [ ] Un control de seguridad *(A security control)*
- [ ] Un exploit *(An exploit)*
- [ ] Una amenaza *(A threat)*

**2. Completa el espacio en blanco: Las cinco capas del modelo de defensa en profundidad (*defense in depth*) son: perímetro, red, endpoint, aplicación y _____.**
*(Fill in the blank: The five layers of the defense in depth model are: perimeter, network, endpoint, application, and _____.)*
- [ ] física *(physical)*
- [x] datos *(data)*
- [ ] transporte *(transport)*
- [ ] sesión *(session)*

**3. El firewall de una organización está configurado para permitir el tráfico solo desde direcciones IP autorizadas. ¿Con qué capa del modelo de defensa en profundidad está asociado el firewall?**
*(An organization's firewall is configured to allow traffic only from authorized IP addresses. Which layer of the defense in depth model is the firewall associated with?)*
- [x] Red *(Network)*
- [ ] Datos *(Data)*
- [ ] Aplicación *(Application)*
- [ ] Endpoint *(Endpoint)*

**4. ¿Cuáles de los siguientes son criterios que una vulnerabilidad debe cumplir para calificar para un ID CVE® oficial? (Selecciona todas las que correspondan)**
*(Which of the following are criteria that a vulnerability must meet to qualify for a CVE® ID? Select all that apply.)*
- [x] Debe enviarse con evidencia de respaldo. *(It must be submitted with supporting evidence.)*
- [ ] Debe representar un riesgo financiero. *(It must pose a financial risk.)*
- [x] Debe ser reconocida como un riesgo potencial de seguridad. *(It must be recognized as a potential security risk.)*
- [x] Debe ser independiente de otros problemas (poder solucionarse por sí sola). *(It must be independent of other issues.)*
- [x] Solo puede afectar a un código base (si afecta a múltiples, recibe múltiples CVEs). *(It can only affect one codebase.)*

**5. Un equipo de seguridad está preparando nuevas estaciones de trabajo que se instalarán en una oficina. ¿Qué pasos de la gestión de vulnerabilidades deben tomar para preparar estas estaciones de trabajo? (Selecciona tres respuestas)**
*(A security team is preparing new workstations that will be installed in an office. Which vulnerability management steps should they take to prepare these workstations? Select three answers.)*
- [ ] Instalar un conjunto de herramientas de colaboración en cada estación de trabajo. *(Install a suite of collaboration tools on each workstation.)*
- [x] Descargar los últimos parches y actualizaciones para cada sistema. *(Download the latest patches and updates for each system.)*
- [x] Considerar quién utilizará cada computadora (Gestión de Identidad y Activos). *(Consider who will be using each computer.)*
- [x] Configurar el firewall de la empresa para permitirles acceso a la red de forma segura. *(Configure the company firewall to allow network access.)*

**6. Durante una evaluación de vulnerabilidades, un escáner identifica un servidor local (*onsite*) vulnerable. Después de analizar el servidor, descubres que a su sistema operativo le faltan actualizaciones críticas. ¿Cuál es el *siguiente* paso que debes tomar en el proceso de evaluación de vulnerabilidades?**
*(During a vulnerability assessment, a scanner identifies a vulnerable onsite server. After analyzing the server, you discover that its operating system is missing critical updates. What is the next step you should take in the vulnerability assessment process?)*
- [ ] Desactivar el servidor porque su sistema operativo está desactualizado. *(Deactivate the server because its operating system is outdated.)*
- [ ] Ignorar el sistema operativo desactualizado porque el dispositivo está operativo. *(Disregard the outdated operating system because the device is operational.)*
- [x] Realizar una evaluación de riesgos del sistema operativo antiguo (Analizar antes de Remediar). *(Perform a risk assessment of the old operating system.)*
- [ ] Escanear los millones de dispositivos que se conectan al servidor. *(Scan the millions of devices that connect to the server.)*

**7. ¿Cuáles de los siguientes son tipos de superficies de ataque? (Selecciona tres respuestas)**
*(Which of the following are types of attack surfaces? Select three answers.)*
- [ ] Software malicioso (Esto es un payload, no una superficie). *(Malicious software)*
- [x] Enrutadores de red *(Network routers)*
- [x] Servidores en la nube *(Cloud servers)*
- [x] Estaciones de trabajo / Computadoras *(Computer workstations)*

**8. Un gerente de proyectos en una empresa de servicios públicos recibe un correo electrónico sospechoso que contiene un archivo adjunto. Abre el archivo adjunto y este instala software malicioso en su computadora portátil. ¿Cuáles son los *vectores de ataque* utilizados en esta situación? (Selecciona dos respuestas)**
*(A project manager at a utility company receives a suspicious email that contains a file attachment. They open the attachment and it installs malicious software on their laptop. What are the attack vectors used in this situation? Select two answers.)*
- [ ] La estación de trabajo infectada (Esta es la Superficie). *(The infected workstation)*
- [x] El correo electrónico sospechoso. *(The suspicious email)*
- [x] El archivo adjunto. *(The file attachment)*
- [ ] El software malicioso (Este es el Payload). *(The malicious software)*

**9. ¿Cuáles de las siguientes son razones por las que los equipos de seguridad practican una *mentalidad de atacante*? (Selecciona tres respuestas)**
*(Which of the following are reasons that security teams practice an attacker mindset? Select three answers.)*
- [x] Para identificar vectores de ataque. *(To identify attack vectors)*
- [x] Para descubrir vulnerabilidades que deben ser monitoreadas. *(To uncover vulnerabilities that should be monitored)*
- [x] Para encontrar información (*insights*) sobre los mejores controles de seguridad a utilizar. *(To find insights into the best security controls to use)*
- [ ] Para explotar fallas en el código base de una aplicación (Esto es lo que hace un criminal real). *(To exploit flaws in an application's codebase)*

**10. Considera el siguiente escenario: Trabajas como profesional de seguridad para un distrito escolar. Un desarrollador de aplicaciones creó una aplicación que conecta a los estudiantes con recursos educativos. Se te ha asignado evaluar la seguridad de la aplicación. Utilizando la mentalidad de un atacante, ¿cuáles de los siguientes pasos tomarías para evaluar la aplicación? (Selecciona dos respuestas)**
*(Consider the following scenario: You are working as a security professional for a school district. An application developer with the school district created an app that connects students to educational resources. You’ve been assigned to evaluate the security of the app. Using an attacker mindset, which of the following steps would you take to evaluate the application? Select two answers.)*
- [x] Identificar los tipos de usuarios que interactuarán con la aplicación (Analizar el objetivo y quién tiene acceso). *(Identify the types of users who will interact with the app.)*
- [ ] Asegurarse de que el formulario de inicio de sesión de la aplicación funcione (Esto es QA, no Seguridad). *(Ensure the app's login form works.)*
- [ ] Integrar la aplicación con los recursos educativos existentes. *(Integrate the app with existing educational resources.)*
- [x] Evaluar cómo la aplicación maneja los datos del usuario (Buscar dónde está la información valiosa). *(Evaluate how the app handles user data.)*
