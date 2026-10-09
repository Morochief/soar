# Herbert: Manage threats, risks, and vulnerabilities

Mi nombre es Herbert y soy Ingeniero de Seguridad en Google. Creo que siempre me ha interesado la seguridad. En la escuela secundaria, nos dieron unas computadoras portátiles Dell enormes. No había mucha seguridad dentro de esas computadoras, así que muchos de mis amigos tenían versiones *crackeadas* de videojuegos, como Halo. Ahí es realmente donde aprendí cómo empezar a manipular computadoras para que hicieran lo que yo quería.

Supongo que mi día a día corporativo consiste en analizar riesgos de seguridad y proporcionar soluciones técnicas a esos riesgos. 

## El Día a Día en el SOC
Una tarea típica para los analistas de ciberseguridad suele ser algo como gestionar las **solicitudes de excepciones** (*exceptions requests*). Esto significa analizar meticulosamente si un usuario de la empresa realmente necesita tener acceso especial a un dispositivo o documento, basándose en el rol que tiene esa persona o el proyecto en el que está trabajando (aplicando siempre el *Principio de Menor Privilegio*).

Una de las amenazas internas más comunes con las que nos encontramos son las **configuraciones erróneas** (*misconfigurations*) o los usuarios solicitando acceso corporativo para algo que realmente no necesitan.

> [!NOTE]
> **Ejemplo de la Vida Real (Revisión de Permisos):** Hace poco tuve un caso en el que un proveedor externo con el que estábamos trabajando había cambiado de la nada sus solicitudes de alcance de OAuth (*OAuth scope requests*). Básicamente, eso significaba que de repente estaban solicitando muchos más permisos para usar los servicios de Google de los que tenían en el pasado. No estábamos seguros de cómo abordar eso porque no era una situación con la que nos hubiéramos topado antes. Así que todavía está en curso, pero estamos trabajando activamente con equipos asociados para desarrollar una solución táctica para acotar esos permisos.

Creo que otra cosa que vemos constantemente son los **sistemas desactualizados**: máquinas que necesitan ser parcheadas con urgencia. Eso suena como un simple problema del departamento de TI, pero en realidad es *definitivamente* un problema crítico de ciberseguridad. Tener servidores desactualizados y no tener políticas adecuadas de gestión de dispositivos (MDM) abre brechas catastróficas.

## El Trabajo en Equipo es Clave
Trabajar con un equipo, o con múltiples equipos simultáneamente, es una parte enorme del trabajo en ciberseguridad. Para lograr hacer cualquier cosa, necesitas comunicarte fluidamente no solo con tu propio equipo del SOC, sino con equipos de infraestructura y otros departamentos.

Hace diez años estaba trabajando en una pizzería y diez años después, aquí estoy, en Google como Ingeniero de Seguridad. Si le hubiera dicho a mi yo de 16 años que estaría aquí, no me lo habría creído, pero es totalmente posible.
