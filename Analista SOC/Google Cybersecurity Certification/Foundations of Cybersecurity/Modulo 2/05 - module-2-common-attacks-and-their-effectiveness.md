# Lectura: Common attacks and their effectiveness

Anteriormente, aprendiste sobre ataques pasados y presentes que ayudaron a dar forma a la industria. Estos incluyeron el ataque *LoveLetter* y el gusano *Morris*. Uno de los resultados históricos de estos ataques fue el establecimiento de equipos de respuesta, que hoy se conocen comúnmente como equipos de respuesta a incidentes de seguridad informática (**CSIRT**). 

En esta lectura, aprenderemos a clasificar los métodos de ataque y *malware* contemporáneos. Familiarizarte con estas tácticas en evolución te ayudará a proteger mejor a tu organización.

## Phishing
El **Phishing** es el uso de comunicaciones digitales para engañar a las personas y hacer que revelen datos confidenciales o desplieguen software malicioso. Las subcategorías de *phishing* más comunes hoy en día incluyen:

- **Business Email Compromise (BEC):** Un ataque donde el criminal envía un correo que parece provenir de una fuente conocida interna (ej. el CEO o un proveedor) para hacer una solicitud financiera urgente o pedir un cambio de cuenta bancaria, con el fin de robar dinero directamente.
- **Spear phishing:** Un ataque de correo electrónico malicioso altamente **dirigido a un usuario específico** (o grupo muy pequeño). A diferencia del phishing masivo, el atacante investiga a su víctima y el correo está completamente personalizado.
- **Whaling:** Una forma avanzada de *spear phishing*. Se dirige exclusivamente a **"ballenas" (*whales*)**, es decir, altos ejecutivos (CEOs, CFOs) para obtener acceso a datos ultra-sensibles.
- **Vishing:** La explotación de la comunicación de voz electrónica (**llamadas telefónicas**) para obtener información confidencial o hacerse pasar por soporte técnico.
- **Smishing:** El uso de mensajes de texto (**SMS**) para engañar a los usuarios.

## Malware
El *Malware* es cualquier software diseñado para dañar dispositivos o redes con el propósito de obtener dinero o inteligencia corporativa. Los tipos de *malware* más comunes incluyen:

- **Virus:** Código malicioso escrito para dañar datos. Requiere ser **iniciado por un usuario** (por ejemplo, al ejecutar un archivo adjunto). Se oculta inyectando su código en archivos sanos.
- **Gusanos (*Worms*):** Malware que puede duplicarse y propagarse por los sistemas **por sí solo**. No necesita ser descargado o ejecutado por un usuario humano. Aprovecha vulnerabilidades para saltar automáticamente por toda la red.
- **Ransomware:** Un ataque malicioso de secuestro donde los actores de amenazas **cifran (encriptan)** los datos de una organización y exigen un pago económico (rescate) para entregar la clave de descifrado y restaurar el acceso.
- **Spyware:** Malware diseñado para espiar y recopilar información sin el consentimiento del usuario (pulsaciones del teclado, correos, micrófonos, cámaras) para venderla.

## Ingeniería Social (*Social Engineering*)
La ingeniería social es la técnica de manipulación psicológica que explota el error humano para hackear a la persona en lugar del sistema. Formas comunes de ingeniería social no digital:

- **Social media phishing:** Un actor de amenazas recopila información muy detallada sobre su objetivo en sitios de redes sociales (OSINT) para luego iniciar un ataque de *spear phishing* altamente creíble.
- **Watering hole attack:** El atacante compromete un sitio web legítimo que es visitado frecuentemente por un grupo específico de usuarios que desea hackear (como un foro del sector industrial al que pertenece la víctima).
- **USB baiting:** El atacante deja estratégicamente una memoria USB infectada (marcada como "Nóminas 2024") en el estacionamiento para que un empleado curioso la encuentre, la conecte a su PC e infecte la red corporativa sin saberlo.
- **Ingeniería social física:** El atacante se hace pasar por el personal de limpieza, mantenimiento de internet o proveedor de café para ingresar físicamente al edificio corporativo.

## Principios Psicológicos de la Ingeniería Social
La ingeniería social es increíblemente efectiva porque explota "parches" faltantes en el cerebro humano. Los atacantes utilizan estos principios psicológicos comprobados:

- **Autoridad:** Impersonan a individuos con poder (el jefe, el FBI, un administrador de red) porque las personas están condicionadas biológicamente a no contradecir a figuras de autoridad.
- **Urgencia:** Persuaden a las víctimas para que respondan rápidamente ("Tu cuenta será bloqueada en 5 minutos"), anulando su capacidad de cuestionar lógicamente la situación.
- **Intimidación:** Utilizan tácticas de acoso o persuasión agresiva para asustar a la víctima.
- **Consenso/Prueba Social:** Usan la presión grupal (ej. "Todos tus compañeros del área de Marketing ya me dieron sus contraseñas para la actualización").
- **Escasez:** Sugieren que hay un tiempo límite o un bien escaso ("Últimos 10 cupos para el bono corporativo").
- **Familiaridad/Confianza:** Establecen una conexión emocional durante semanas o meses antes de lanzar el ataque y pedir credenciales.

> [!TIP]
> **CSIRT** significa *Computer Security Incident Response Team*. Recuerda que los conceptos como BEC (*Business Email Compromise*) y *Watering hole* son escenarios fijos en las preguntas de certificación.

## Puntos Clave (Key Takeaways)
- El **Phishing** general es enviar una red al mar a ver qué pez muerde. El **Spear Phishing** es pescar con arpón a un empleado específico. El **Whaling** es usar el arpón contra el CEO.
- **Vishing** = Phishing por Voz (Llamadas). **Smishing** = Phishing por SMS.
- El **Ransomware** secuestra los datos mediante el cifrado, exigiendo un rescate monetario.
- Los ataques de Ingeniería Social siempre apalancan fallas psicológicas, siendo la **Autoridad** y la **Urgencia** las más efectivas y utilizadas por cibercriminales.
