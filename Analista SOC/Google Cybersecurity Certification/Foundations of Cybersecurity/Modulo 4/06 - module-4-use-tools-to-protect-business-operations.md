# Lectura: Use tools to protect business operations

Anteriormente te introdujimos a la programación, los sistemas operativos y las herramientas tácticas comúnmente utilizadas en ciberseguridad. En esta lectura técnica, exploraremos en detalle cómo los analistas de *Nivel 1* (*Tier 1*) implementan estas herramientas para proteger las operaciones comerciales y mitigar ataques en tiempo real.

## Herramientas y sus propósitos

### 1. Programación y Bases de Datos
La programación se utiliza para crear un conjunto específico de instrucciones que una computadora debe ejecutar. 
Los analistas SOC utilizan lenguajes como **Python** puramente para la automatización. La automatización es el uso de la tecnología para reducir el esfuerzo humano en la realización de tareas masivas. Esto ahorra tiempo valioso al investigar un ciberataque y reduce a cero el riesgo de error humano.

Otro lenguaje fundamental es el Lenguaje de Consulta Estructurado (**SQL**). SQL no sirve para hacer programas, sino que se utiliza para crear, interactuar y solicitar información específica a una **base de datos** corporativa. Un *Data Point* (punto de datos) es un fragmento específico de información, y como las bases de datos de seguridad (como los SIEM) contienen millones de puntos de datos, los analistas usan comandos SQL para filtrar todo ese océano de información en milisegundos.

### 2. Sistemas Operativos (Linux)
Un sistema operativo es el "traductor" entre el hardware físico de la computadora y el usuario humano (ej. macOS y Windows).

A diferencia de los sistemas operativos comerciales, **Linux** es un sistema de código abierto (*open-source*), lo que significa que su código fuente está disponible públicamente y cualquier persona puede auditarlo o mejorarlo. Linux es la columna vertebral de los servidores en la nube de todo el mundo.
Aunque Linux no es un lenguaje de programación, los servidores Linux carecen de entorno gráfico, por lo que su uso implica dominar la **Interfaz de Línea de Comandos (CLI)**. Una CLI es una pantalla negra de texto donde los analistas ingresan instrucciones directas (*comandos*) para hablar con el núcleo del sistema (*kernel*). Aprenderás más sobre el núcleo de Linux y el ecosistema GNU en el próximo curso.

### 3. Vulnerabilidades Web (*Web vulnerability*)
Una vulnerabilidad web es un defecto, error de código o falla en una aplicación web que un actor de amenazas (hacker) podría explotar mediante código malicioso para permitir el acceso no autorizado, robar las tarjetas de crédito de los clientes o inyectar *malware* en el servidor.

> [!TIP]
> **El estándar OWASP:** Para mantenerte actualizado sobre los 10 riesgos más críticos del mundo para las aplicaciones web, la industria confía ciegamente en el **OWASP Top 10** (*Open Web Application Security Project*). Es lectura obligatoria para cualquier profesional defensivo.

### 4. Software Antivirus
El software antivirus (también llamado *anti-malware*) es el escudo de primera línea de cualquier dispositivo. Su trabajo es escanear los archivos y la memoria RAM de un equipo para encontrar "firmas" (patrones conocidos) que indiquen la presencia de virus y bloquearlos antes de que se ejecuten.

### 5. Sistema de Detección de Intrusos (IDS)
Un **IDS** (*Intrusion Detection System*) es una aplicación o equipo de red que monitorea pasivamente la actividad de toda la red y alerta sobre posibles intrusiones. El IDS escanea y desarma los *paquetes de red* (los sobres de datos que viajan por el cable de internet) buscando anomalías, robos de datos o accesos no autorizados antes de que lleguen a los servidores centrales.

### 6. Cifrado Criptográfico (*Encryption*)
El cifrado hace que los datos sean ilegibles y difíciles de decodificar para un usuario no autorizado; su objetivo es garantizar la **Confidencialidad**.
El cifrado es el proceso de aplicar matemáticas extremas para convertir datos legibles (texto plano o *plaintext*) a un formato bloqueado criptográficamente (texto cifrado o *ciphertext*). Sin la llave digital (*key*), los datos cifrados son basura inútil para un hacker.

> [!WARNING]
> **Codificación vs. Cifrado:**
> Jamás los confundas. La **Codificación** (*Encoding*, como Base64) solo cambia el formato de los datos para que puedan viajar por internet sin corromperse; usa un algoritmo público que cualquiera puede revertir, *NO protege nada*. El **Cifrado** (*Encryption*, como AES) utiliza llaves secretas y matemáticas puras para ocultar la información; *SÍ protege los datos*.

### 7. Pruebas de Penetración (*Penetration testing / Pentesting*)
El *Pentesting* es el acto de organizar un hackeo ético y simulado contra tu propia empresa. Ayuda a identificar vulnerabilidades reales en los sistemas, redes y aplicaciones web antes de que un ciberdelincuente real las encuentre. Es una evaluación de riesgos agresiva que identifica debilidades de seguridad tanto externas (desde el internet público) como internas (desde adentro del edificio físico de la empresa).

---

## Puntos Clave (Key Takeaways)
- Usarás **Python** para crear *scripts* automáticos y **SQL** para hacerle preguntas a tu base de datos gigante.
- **Linux** es el rey de los servidores corporativos. No tiene botones; lo controlarás puramente escribiendo texto en la **CLI** (*Command-Line Interface*).
- Un **IDS** (*Intrusion Detection System*) huele el tráfico de tu red para avisarte si algo está intentando robar datos.
- El **OWASP Top 10** es la biblia mundial sobre los 10 hackeos web más peligrosos del año.
- **Cifrar** es ocultar datos con una llave secreta. **Codificar** es solo cambiarles el formato sin protegerlos.
