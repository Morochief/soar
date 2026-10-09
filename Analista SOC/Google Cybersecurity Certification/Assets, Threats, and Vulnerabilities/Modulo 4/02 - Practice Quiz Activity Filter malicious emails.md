# Practice Quiz: Activity: Filter malicious emails

## Resumen de la Actividad
En esta actividad, analizarás un correo electrónico sospechoso e identificarás las señales de un ataque de phishing. Luego, determinarás si el correo electrónico debe permitirse o ponerse en cuarentena.

El *Phishing* es una de las formas más comunes y peligrosas de ingeniería social que encontrarás en el campo. Identificar intentos de phishing te ayudará a prevenir amenazas y a encontrar formas de mejorar los procedimientos de seguridad de tu SOC.

---

## Escenario
Eres un analista de seguridad en una firma de inversiones llamada *Imaginary Bank*. Un ejecutivo de la firma recibió recientemente un correo electrónico de *Spear Phishing* (Phishing dirigido) que parece provenir de la junta directiva. En este caso, se le pide al ejecutivo que instale un nuevo software de colaboración, *ExecuTalk*.

El ejecutivo sospecha que este correo podría ser un intento de phishing porque *ExecuTalk* nunca fue mencionado durante la última reunión de la junta. Ha reenviado el mensaje a tu equipo para verificar si es legítimo. Tu supervisor te ha encargado investigar el mensaje y determinar si debe ponerse en cuarentena.

### Paso 1 y 2: Analizar el encabezado y remitente del correo
Investiga las pistas en el encabezado (*header*) del correo:

> **From:** imaginarybank@gmail.org
> **Sent:** Saturday, December 21, 2019 15:05:05
> **To:** cfo@imaginarybank.com
> **Subject:** RE: You are been added to an ecsecutiv's groups

**1. ¿Cuáles dos pistas en el encabezado del mensaje te indican que se trata de un intento de phishing? (Selecciona dos respuestas)**
*(Which two clues in the message header indicate to you that this is a phishing attempt? Select two answers.)*
- [x] El remitente está usando un dominio diferente (gmail.org en lugar de imaginarybank.com). *(The sender is using a different domain.)*
- [x] Hay un error de ortografía en la línea de asunto ("ecsecutiv's"). *(There is a misspelling in the subject line.)*
- [ ] La línea de asunto parece ser una respuesta (RE:). *(The subject line appears to be a reply.)*
- [ ] La marca de tiempo va más allá de las 12 PM. *(The time stamp goes beyond 12 PM.)*

### Paso 3: Revisar el cuerpo del mensaje en busca de pistas
Analiza el cuerpo del mensaje para identificar cómo el atacante intenta disfrazarlo como un correo legítimo:

> Conglaturations! You have been added to a collaboration group ‘Execs.’
> Downlode ExecuTalk to your computer.
> Mac® | Windows® | Android™
> You're team needs you! This invitation will expire in 48 hours so act quickly.
> Sincerely,
> ExecuTalk©
> All rights reserved.

**2. ¿Qué detalles hacen que este mensaje "parezca" legítimo a primera vista? (Selecciona tres respuestas)**
*(What details make this message appear legitimate? Select three answers.)*
- [ ] El límite de tiempo de la invitación (Esto genera urgencia, no legitimidad). *(The invitation time limit)*
- [x] El título del grupo ("Execs" suena a un grupo directivo real). *(The title of the group)*
- [x] Las opciones de descarga para los principales sistemas operativos (con símbolos registrados ® y ™). *(The download options for major operating systems)*
- [x] El etiquetado de la marca (Símbolo de copyright © y "Todos los derechos reservados"). *(The brand labeling)*

### Paso 4: Investigar las opciones de descarga
**3. Las opciones de descarga abren una página web que contiene un formulario de inicio de sesión donde alguien puede ingresar un nombre de usuario y contraseña. Al revisar cuidadosamente la página web, ¿cuál es la pista principal que indica que este formulario es malicioso?**
*(The download options open a webpage that contains a login form where someone can enter a username and password. Carefully review the webpage. What is the main clue that indicates this form is malicious?)*
- [ ] Opciones de inicio de sesión *(Sign-in options)*
- [ ] Marca / Branding *(Branding)*
- [x] La URL (La dirección web real) *(The URL)*
- [ ] Tipo de fuente *(Font type)*
> [!NOTE]
> Los atacantes pueden clonar pixel por pixel la interfaz gráfica de inicio de sesión de Microsoft, Google o tu propio banco. La única característica que **no pueden falsificar** perfectamente es el dominio oficial (URL) que aparece en la barra superior del navegador.

### Conclusión
**4. Después de completar tu investigación, ¿debería este correo electrónico ser puesto en cuarentena?**
*(After completing your investigation, should this email be quarantined?)*
- [x] Sí *(Yes)*
- [ ] No *(No)*
