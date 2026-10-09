Asunto: [Infecci¾n por Malware] - Anßlisis cronol¾gico de trß?co malicioso en
ip-192-168-3-65 (T·nel IPsec)

Resumen del incidente: El dÝa 03/07/2026, los sistemas de inspecci¾n y anßlisis de trß?co
perimetral detectaron m·ltiples anomalÝas crÝticas de seguridad originadas desde el host
interno 192.168.3.65. Este activo, ubicado en la red remota del cliente, utiliz¾ el t·nel de la VPN
IPsec hacia nuestro NOC como puente de trßnsito para descargar componentes ejecutables
maliciosos y realizar transmisiones de comando y control hacia un servidor externo alojado
en PaÝses Bajos (IP p·blica 188.72.243.72, bajo la organizaci¾n Webzilla B.V.).

Validaci¾n: Para aportar mßxima certidumbre tÚcnica y documentar de forma irrefutable el
comportamiento del vector, el motor de anßlisis del sistema de detecci¾n de intrusos
perimetral realiz¾ una reconstrucci¾n cronol¾gica y profunda de los paquetes de datos
interceptados en la capa de aplicaci¾n (Capa 7 - HTTP). Se determin¾ que los eventos
individuales corresponden a transacciones uni?cadas analizadas correlativamente.

1. LÝnea de tiempo de las transacciones HTTP

?  Fase A: Petici¾n de con?guraci¾n binaria

?  Explicaci¾n: En esta fase inicial, el host comprometido establece el primer

contacto de red con el servidor externo para descargar directrices operativas.
La solicitud se realiza mediante un mÚtodo GET apuntando al recurso
/kartos/kartos.bin. Este archivo .bin funciona como un componente de
con?guraci¾n dinßmica que le indica al malware c¾mo operar, quÚ dominios
alternativos contactar y quÚ tipo de informaci¾n local debe recolectar. El
sistema perimetral intercept¾ esta actividad identi?cando patrones de dise±o
web exclusivos de botnets conocidas.

?  Firma IDS 1: ET MALWARE Zbot Generic URI/Header Struct .bin (SID: 2018052

/ Clase: trojan-activity / Severidad: 1)

?  Firma IDS 2: ET MALWARE Possible Zbot Activity Common Download Struct

(SID: 2017836 / Clase: trojan-activity / Severidad: 1)

?  Evidencia de la petici¾n solicitada:

?  Fase B: Transferencia completa del primer ejecutable

?  Explicaci¾n: El host solicita el primer binario ejecutable bajo la ruta

/kartos/krt.exe. La petici¾n inicial del cliente activ¾ alertas por la estructura
hostil de su URL. El servidor malicioso responde con un estado 200 OK
entregando un ?ujo binario de 119,296 bytes (application/x-msdownload). Este
componente act·a como un Dropper o instalador compactado. El anßlisis de
los paquetes revel¾ que el archivo viaja empaquetado para evadir ?rmas
tradicionales y contiene llamadas a funciones crÝticas para asegurar la
infecci¾n local, tales como inyecci¾n de procesos en memoria
(WriteProcessMemory) y auto-reconocimiento de entornos de anßlisis
(IsDebuggerPresent), dise±ados para apagar el malware si nota que estß
siendo escaneado por herramientas de seguridad.

?  Firma 1: ET MALWARE Terse alphanumeric executable downloader high

likelihood of being hostile (SID: 2019714 / Clase: bad-unknown)

?  Firma 2: ET INFO PE EXE or DLL Windows ?le download HTTP (SID: 2018959 /

Clase: policy-violation)

?  Firma 3: ET INFO Packed Executable Download (SID: 2014819 / Clase:

misc-activity)

?  Firma 4: ET HUNTING Suspicious Windows Executable WriteProcessMemory

(SID: 2015588 / Clase: misc-activity)

?  Firma 5: ET INFO EXE IsDebuggerPresent (Used in Malware Anti-Debugging)

(SID: 2015744 / Clase: misc-activity)

?  Evidencia de Respuesta del Servidor (Descarga de /kartos/krt.exe):

?  Fase C: Solicitud y transferencia del segundo ejecutable

?  Explicaci¾n: En paralelo a la acci¾n anterior, el dispositivo interno genera una
nueva sesi¾n web para descargar el archivo /ser.exe. En esta transacci¾n, el
malware altera el destino l¾gico de la cabecera Host apuntando al dominio
simulado www[.]hostme[.]name. El servidor responde con un estado 200 OK
trans?riendo un archivo de gran tama±o (593,507 bytes). El escaneo
automatizado del motor perimetral analiz¾ el ?ujo binario completo en

trßnsito y determin¾ mediante ?rmas que se trata del componente ejecutable
principal (Payload), identi?cßndolo de forma especÝ?ca como un Troyano.
?  Firma IDS 1: ET MALWARE Terse alphanumeric executable downloader high
likelihood of being hostile (SID: 2019714 / Clase: bad-unknown / Severidad: 2)

?  Firma IDS 2: ET INFO PE EXE or DLL Windows ?le download HTTP (SID:

2018959 / Clase: policy-violation / Severidad: 1)

?  Evidencia de petici¾n y respuesta correlacionada (Descarga de /ser.exe):

?  Fase D: Actividad de comando y control (C2) y beaconing

?  Explicaci¾n TÚcnica: Los registros con?rman que la comunicaci¾n hacia el

servidor de comando y control (C2) se ejecut¾ de manera concurrente durante
el ciclo de descargas. El host interno transmiti¾ paquetes salientes utilizando el
mÚtodo POST contra el script /kartos/youyou.php. El primer envÝo ocurri¾ en
paralelo a las descargas (a las 19:01:58.153) transmitiendo una carga ·til de
271 bytes. Una segunda transmisi¾n ocurri¾ al ?nalizar la secuencia (a las
19:01:58.700) enviando 169 bytes. Esta actividad de balizamiento (beaconing)
representa el canal mediante el cual el equipo comprometido reporta
parßmetros bßsicos de control y estado tÚcnico hacia el atacante.

?  Firma IDS: ET MALWARE Zbot POST Request to C2 (SID: 2019141 / Clase:

command-and-control / Severidad: 1)

?  Evidencia de Carga ┌til en Petici¾n POST (Trß?co Saliente hacia

/kartos/youyou.php):

2. Matriz de Indicadores de Compromiso (IoCs) extraÝdos

Tipo de IoC

Valor tÚcnico detectado

Descripci¾n y contexto en red

Direcci¾n IPv4 (C2)

188[.]72[.]243[.]72

Servidor externo malicioso (Webzilla B.V. -
PaÝses Bajos).

Dominios de destino

ishi-bati[.]com

www[.]hostme[.]name

Direcciones mapeadas en las cabeceras
Host de las transacciones HTTP de forma
alternada.

Rutas de recursos
(URIs)

/kartos/kartos.bin

Archivos de con?guraci¾n binaria,
ejecutables de descarga y scripts PHP de
beaconing C2.

/kartos/krt.exe

/ser.exe

/kartos/youyou.php

Navegador falsi?cado

Mozilla/4.0 (compatible; MSIE
6.0; Windows NT 5.1; SV1)

Parßmetro User-Agent arti?cial inyectado
para simular entornos Windows XP
obsoletos.

Hash SHA256 (krt.exe
ôkrt-ETG.exeö)

68a7f7bd5627c5cc465373983ac
f21958746c12e3441cccd1dfbc23
4944b8cf2

Huella digital de red del componente
empaquetado inicial. Veredicto de motor
antivirus perimetral: VIRUS Mal/Resdro-A.

Hash SHA256 (ser.exe
ôStub.exeö)

282f463d7cdec977d6752312793
65dd890f1480dafa9d88473d5d
47574e007b0

Huella digital de red del componente
troyano principal. Veredicto del : VIRUS
Troj/VB-KVA.

Conclusi¾n: Los sistemas internos y activos de infraestructura propios de Technoma se
encuentran totalmente fuera de peligro y libres de intrusiones. A nivel corporativo, el
incidente estß contenido. Sin embargo, los registros demuestran de manera concluyente que
la mßquina interna del cliente (192.168.3.65) presenta un estado de compromiso activo,
compatible con un troyano con capacidades de inyecci¾n en memoria y beaconing hacia
servidores C2. La red perimetral con?rm¾ la transferencia completa de los componentes en
la capa de transporte y el posterior inicio de las transmisiones salientes (POST). Debido a que
las cabeceras HTTP registran parßmetros de terminaci¾n forzada (Connection: close), los
canales de descarga individuales se cerraron inmediatamente despuÚs de la entrega de
datos, por lo que se requiere una auditorÝa interna directa en el propio endpoint del cliente
para con?rmar el estado ?nal de almacenamiento o ejecuci¾n local de los archivos.


