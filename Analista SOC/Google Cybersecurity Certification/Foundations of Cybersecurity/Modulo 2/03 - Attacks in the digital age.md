# Attacks in the digital age

## El Inicio de la Ingeniería Social: El Ataque LoveLetter (2000)
Con la expansión masiva de Internet, la cantidad de computadoras interconectadas aumentó dramáticamente. Como el *malware* ahora podía propagarse de forma remota, los atacantes ya no necesitaban depender de discos físicos infectados para propagar virus. 

Para comprender la magnitud de los ataques en la era digital, repasaremos el ataque **LoveLetter** y la infame **brecha de datos de Equifax**.

En el año 2000, un atacante creó el *malware* **LoveLetter** (conocido mundialmente como el virus *ILOVEYOU*) para robar credenciales. Este ataque se propagó a una velocidad sin precedentes porque se aprovechó de un factor clave: en el año 2000, la gente aún no había desarrollado una sospecha natural ante los correos electrónicos.

Las víctimas recibían un correo con el asunto *"I Love You"* y un archivo adjunto llamado *"Love Letter For You.txt.vbs"*. Al abrir el archivo, el *malware* se ejecutaba silenciosamente y **escaneaba la libreta de direcciones** del usuario. Luego, se reenviaba automáticamente a todos los contactos de esa libreta e instalaba un programa espía en segundo plano. Los nuevos destinatarios abrían el correo sin dudarlo porque **creían que venía de un amigo o familiar**. 

El ataque LoveLetter infectó a más de **45 millones de computadoras a nivel mundial** y se estima que causó $10 mil millones de dólares en daños globales.

> [!NOTE]
> El ataque LoveLetter es un claro ejemplo temprano de la **ingeniería social**. La ingeniería social (*social engineering*) es una técnica de manipulación psicológica que explota el factor humano (curiosidad, confianza, miedo) para obtener acceso a sistemas o información.

Después del éxito de *LoveLetter*, los atacantes comprendieron el poder destructivo de hackear al ser humano en lugar de a la máquina. Hoy en día, capacitar a los empleados para identificar estos ataques es vital, específicamente para detectar intentos de **Phishing**.

> [!IMPORTANT]
> El **Phishing** es una táctica específica de la ingeniería social. Consiste en utilizar comunicaciones digitales fraudulentas (como correos electrónicos haciéndose pasar por un banco) para engañar a las víctimas y lograr que revelen credenciales o descarguen software malicioso.

## La Brecha de Datos de Equifax (2017)
Ahora, analicemos la brecha de datos de la agencia de informes crediticios **Equifax**. En 2017, un grupo de atacantes se infiltró con éxito en sus servidores centrales, resultando en una de las fugas de información más catastróficas de la historia.

Se robaron más de **143 millones de registros de clientes**, afectando al 40% de toda la población de EE.UU. ¿El problema real? Los datos robados no eran simplemente nombres, sino información **SPII** crítica: números de seguro social, fechas de nacimiento, licencias de conducir y números de tarjetas de crédito.

Desde el punto de vista del *Blue Team* (Defensa), la brecha ocurrió por negligencia. La empresa **fracasó en parchar (actualizar) múltiples vulnerabilidades de software ampliamente conocidas** durante los meses previos al ataque. Los *hackers* simplemente entraron por una puerta que la empresa olvidó cerrar.

Como resultado de esta negligencia, Equifax fue sancionada por el gobierno y se vio obligada a pagar **más de $575 millones de dólares** en multas. Esta colosal suma alertó a todas las corporaciones del mundo sobre el inmenso riesgo financiero que conlleva ignorar la ciberseguridad.

## Puntos Clave (Key Takeaways)
- La **Ingeniería Social (*Social Engineering*)** es la táctica más efectiva hoy en día. Consiste en engañar y manipular al usuario legítimo (eslabón más débil) para que él mismo abra la puerta del sistema.
- El **Phishing** es un tipo de ingeniería social llevada a cabo a través de medios digitales masivos (ej. emails falsos).
- El caso **Equifax (2017)** demostró las graves repercusiones legales y económicas de la negligencia corporativa. Subraya la regla de oro del analista SOC: nunca ignorar la gestión de vulnerabilidades conocidas y no emparchadas.
