# Controls

Mientras que los marcos (*frameworks*) se utilizan a nivel administrativo para crear planes estratégicos globales que abordan amenazas y vulnerabilidades, los **controles** son los mecanismos tácticos y reales que se instalan para reducir riesgos de seguridad *específicos* en la trinchera.

Si no se implementan los controles técnicos o administrativos adecuados, una organización corporativa podría enfrentar impactos financieros masivos y un daño permanente a su reputación debido a la exposición a incidentes cotidianos (incluyendo la intrusión física a oficinas, la creación de cuentas de empleados falsas o el fraude con beneficios corporativos).

Repasemos la definición exacta: **Los controles de seguridad son salvaguardas (*safeguards*) diseñadas para mitigar o reducir riesgos de seguridad específicos.**

En este video, discutiremos tres tipos comunes y vitales de controles lógicos de seguridad: el cifrado (*Encryption*), la autenticación (*Authentication*) y la autorización (*Authorization*).

## 1. Cifrado (Encryption)
El cifrado es el proceso matemático de convertir datos de un formato legible a un formato codificado de forma segura. Típicamente, el cifrado implica convertir datos de texto claro o texto sin formato (*plaintext*) a **texto cifrado** (*ciphertext*).

El texto cifrado es el mensaje crudo y ofuscado que resulta completamente ilegible tanto para los humanos como para las computadoras que intercepten el tráfico. Estos datos no pueden leerse hasta que hayan sido **descifrados** (*decrypted*) y devueltos a su forma original utilizando una llave criptográfica. El cifrado es la herramienta fundamental que se utiliza para garantizar la Confidencialidad (**C**) de datos altamente sensibles, como las bases de datos de tarjetas de crédito o los registros médicos (*HIPAA*).

## 2. Autenticación (Authentication)
Otro control clave que se puede utilizar para proteger la infraestructura es la autenticación. La autenticación es el proceso de verificar criptográfica o lógicamente **quién** es realmente alguien (o algo).

Un ejemplo cotidiano de autenticación es iniciar sesión en Active Directory o en un portal web con tu nombre de usuario y contraseña. Esta forma básica de autenticación asume que solo el usuario legítimo conoce la contraseña, otorgando el acceso inicial.

Sin embargo, los equipos SOC modernos exigen métodos mucho más robustos para frenar el compromiso de credenciales, como la **Autenticación Multifactor (MFA)**. El MFA desafía al usuario a demostrar que realmente es quien dice ser requiriendo *múltiples* métodos simultáneos (algo que sabe, algo que tiene o algo que es). Por ejemplo: una contraseña combinada con un token temporal (*Authenticator App*) o controles de biometría (huella dactilar o escaneo facial).
Los controles biométricos se basan en características físicas que, en teoría, son únicas e irrepetibles.

> [!CAUTION]
> **El Vishing y la Identidad:** Un ejemplo de ingeniería social moderna que puede explotar los sistemas de seguridad de voz corporativa es el **Vishing** (*Voice Phishing*). El *vishing* es la explotación de la comunicación por voz (llamadas telefónicas o VoIP) para obtener información confidencial o hacerse pasar por un alto ejecutivo. Utilizando tecnologías actuales (Deepfakes de voz), un actor de amenazas podría emplear el *vishing* para clonar la voz del CEO, solicitar transferencias bancarias fraudulentas o eludir verificaciones de identidad en Help Desk.

## 3. Autorización (Authorization)
Por último, otro control de seguridad crítico es la autorización (a menudo confundida con la autenticación). La autorización se refiere al concepto de otorgar un nivel específico de **acceso a recursos** dentro de un sistema *después* de haber autenticado exitosamente al usuario.

Esencialmente, la autorización se utiliza para auditar si una persona ya identificada tiene el **permiso** para visualizar un archivo corporativo puntual. 
*   **Ejemplo:** Si trabajas como analista SOC de nivel 1 para el gobierno federal, estás *autenticado* en la intranet al ingresar con tu placa. Sin embargo, tu rol determina tu *autorización*: no tendrás permisos técnicos para acceder a carpetas altamente clasificadas en la red interna a menos que tus privilegios en el Active Directory te lo permitan explícitamente (aplicando el *Principio de Menor Privilegio*).

Los controles de seguridad que discutimos hoy son solo un elemento táctico de un modelo de seguridad central conocido en la industria como la Tríada CIA (Confidencialidad, Integridad y Disponibilidad). A continuación, exploraremos en detalle este sagrado modelo y cómo los equipos del SOC lo utilizan como su máxima brújula defensiva.
