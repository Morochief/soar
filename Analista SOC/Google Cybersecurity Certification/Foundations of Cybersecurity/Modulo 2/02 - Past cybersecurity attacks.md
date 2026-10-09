# Past cybersecurity attacks

## Evolución de los Ataques Informáticos
La industria de la ciberseguridad está en constante evolución, pero la mayoría de los ataques actuales no son del todo nuevos. A menudo, los atacantes simplemente alteran o mejoran el código de métodos de ataque del pasado. Comprender la historia de los incidentes históricos puede brindarte una excelente orientación sobre cómo manejar o investigar *malware* moderno en tu trabajo como analista.

Primero, repasemos las definiciones de las amenazas que formaron la industria:

> [!NOTE]
> Un **virus informático** (*computer virus*) es un código malicioso escrito para interferir con las operaciones de la computadora y causar daños. Su característica principal es que se **adosa** (*attaches*) a programas o documentos legítimos, y requiere de alguna acción humana (como ejecutar el archivo) para propagarse e infectar otros sistemas.
> 
> Hoy en día, los virus se engloban dentro del término general **Malware**, que es cualquier software diseñado específicamente para dañar dispositivos o redes.

Dos de los ejemplos más tempranos de ataques de *malware* masivos que cubriremos son el virus **Brain** y el gusano **Morris** (*Morris worm*). Paradójicamente, ambos fueron creados por desarrolladores para lograr tareas específicas, pero subestimaron drásticamente el impacto destructivo que tendría su propio código en la red global.

## El Virus Brain (1986)
En 1986, los hermanos Alvi crearon el virus **Brain**. Aunque la intención original del código era simplemente rastrear copias ilegales de su software médico y arruinar licencias pirateadas, lo que el virus hizo en la práctica fue algo inesperado.

Una vez que una persona usaba una copia pirateada del software, el virus infectaba el sector de arranque de la computadora. A partir de ahí, cualquier disquete (*floppy disk*) que se insertara en la máquina infectada, copiaba el virus automáticamente. El código se propagaba a una computadora nueva cada vez que alguien insertaba uno de esos disquetes infectados. Al pasar completamente desapercibido, el virus se propagó a nivel mundial en un par de meses.

Aunque la intención original de sus creadores no era destruir hardware ni formatear discos, el virus redujo severamente la productividad e impactó las operaciones comerciales del mundo entero. El virus Brain alteró fundamentalmente la industria informática, poniendo en evidencia por primera vez la necesidad crítica de implementar planes de ciberseguridad.

## El Gusano Morris (1988)
Otro ataque informático inmensamente influyente fue el gusano **Morris** (*Morris worm*). En 1988, Robert Morris desarrolló un programa con una intención benigna: evaluar el tamaño real de Internet. El programa rastreaba la web y se autoinstalaba en otras computadoras para llevar un recuento de cuántas máquinas existían conectadas a la red.

¿Suena inofensivo, verdad? El problema fue que el programa tenía un error crítico de diseño: no lograba llevar un registro exitoso de las computadoras en las que ya se había instalado. Por lo tanto, el gusano continuaba reinstalándose sobre sí mismo en la misma computadora una y otra vez hasta que el equipo se quedaba sin memoria RAM y colapsaba por completo (*crashed*).

Alrededor de 6.000 computadoras se vieron afectadas (lo que en ese momento representaba el **10% de todo el Internet mundial**). Este accidente costó millones de dólares en daños debido a la interrupción masiva de negocios.

> [!IMPORTANT]
> Después del caos ocasionado por el gusano Morris, los gobiernos se dieron cuenta de que necesitaban un grupo de expertos listos para actuar. Así se establecieron los **Equipos de Respuesta a Emergencias Informáticas**, conocidos por sus siglas en inglés como **CERT** (*Computer Emergency-Response Teams*). Los CERT existen hoy en día en casi todos los países y organizaciones grandes, y son la primera línea de defensa a nivel nacional y global.

## Puntos Clave (Key Takeaways)
- Un **Virus** requiere intervención manual o un medio de transporte (como ejecutar un archivo o pasar un disquete) para propagarse, ya que su código se "inyecta" en archivos legítimos.
- Un **Gusano (*Worm*)** es un *malware* superior que se propaga automáticamente por la red aprovechando vulnerabilidades, sin requerir ninguna intervención humana, a menudo colapsando las redes debido al tráfico que genera.
- El **Virus Brain (1986)** demostró lo rápido que un código puede salir de control a nivel mundial utilizando simplemente medios de almacenamiento físico (disquetes).
- El **Gusano Morris (1988)** provocó el primer colapso a gran escala en la historia de Internet, dando lugar a la fundación de los primeros equipos **CERT** (Equipos de Respuesta a Emergencias Informáticas).
