Cebolla de seguridad
Documentación
3.2.0
Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
Tabla de contenidos
1. Alrededor de 8
1.1 Cebolla de seguridad 8
1.2 Seguridad Onion Solutions, LLC 8
1.3 Documentación 8
2. Introducción 10
2.1 Visibilidad de la red 12
2.2 Visibilidad del host 12
2.3 Herramientas de análisis 12
2.4 Flujo de trabajo 16
2.5 Escenarios de implementación 16
2.6 Conclusión 16
3. Licencia 17
4. Usuarios nuevos 18
5. Primeros pasos 39
5.1 Descripción general de cómo empezar 39
5.2 Mejores prácticas 40
5.3 Casos de uso 41
5.4 Arquitectura 43
5.5 Hardware 54
5.6 Descargar 60
5.7 VMware 61
5.8 VirtualBox 63
5.9 Proxmox 64
5.10 Problemas de inicio 66
5.11 Entrehierro 67
5.12 Instalación 68
5.13 Imagen de la nube de Amazon 70
5.14 Imagen de la nube de Azure 76
5.15 Imagen de la nube de Google 81
5.16 Configuración 87
5.17 Instalación posterior 89
6. Consola de seguridad Onion 91
6.1 Descripción general de la consola Security Onion 91
6.2 Alertas 93
- 2/402 - Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
6.3 Paneles de control 99
6.4 Caza 106
6.5 Casos 107
6.6 Detecciones 114
6.7 PCAP 122
6.8 Cuadrícula 126
6.9 Descargas 133
6.10 Administración 134
6.11 Kibana 139
6.12 Flota Elástica 142
6.13 Administrador de Osquery 147
6.14 AfluenciaDB 148
6.15 PostgreSQL 150
6.16 CiberChef 154
6.17 Navegador ATT&CK 155
7. Seguridad Onion Desktop 156
7.1 Descripción general de Security Onion Desktop 156
7.2 Cromo 158
7.3 Minero de red 159
7.4 Wireshark 160
8. Visibilidad de la red 161
8.1 Descripción general de la visibilidad de la red 161
8.2 PAQUETE AF 162
8.3 BPF 163
8.4 Captura de paquetes completos 165
8.5 Suricata 168
8.6 Zeek 174
8.7 Strelka 179
8.8 Honeypot de detección de intrusiones 181
9. Visibilidad de red adicional 184
9.1 Descripción general adicional de la visibilidad de la red 184
9.2 Flujo neto 185
9.3 MCE 186
9.4 iptables 187
9.5 UniFi 188
9,6 pfSense 190
9.7 OPNsense 192
- 3/402 - Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
10. Visibilidad del anfitrión 195
10.1 Descripción general de la visibilidad del host 195
10.2 Agente elástico 196
10.3 Registro del sistema 199
10.4 Sysmon 200
11. Integraciones de terceros 201
11.1 Agregar una integración 201
11.2 Agregar una integración personalizada 201
11.3 Gestión de actualizaciones de integración 202
11.4 Gestión de plantillas de índices de integración de terceros 202
11.5 Integraciones admitidas 202
11.6 Más información 202
12. Reglas 203
12.1 Descripción general de las reglas 203
12.2 NIDS 204
12.3 Sigma 216
12.4 YARA 220
13. Registros 222
13.1 Descripción general de los registros 222
13.2 Ingerir 223
13.3 Almacenamiento de registros 225
13.4Redis 229
13.5 Búsqueda elástica 231
13.6 ElastAlert 2 239
13.7 Campos de datos 242
13.8 Campos de datos de alerta 243
13.9 Campos ElastAlert 244
13.10 Campos Zeek 245
13.11 ID de comunidad 246
13.12 Registros de la consola Security Onion 247
14. Actualización 248
14.1 Descripción general de la actualización 248
14.2 sopa 249
14.3 Fin de vida 255
15. Cuentas 256
15.1 Descripción general de cuentas 256
15.2 Agregar cuentas 257
- 4/402 - Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
15.3 Deshabilitar cuentas 259
15.4 Listado de cuentas 260
15.5 Contraseñas 262
15,6 AMF 264
15.7 Control de acceso basado en roles (RBAC) 266
15.8 Kratos 271
16. Servicios 272
17. Personalización 273
17.1 Descripción general de la personalización 273
17.2 Personalización de la consola Security Onion 274
17.3 nginx 277
17.4 Representante 279
17.5 Cortafuegos 281
17.6 Correo electrónico 285
17.7 NTP 286
17.8 SSH 287
17.9 Nombre de host 288
17.10 Dirección IP 289
17.11 DNS 290
17.12 URL de acceso web 291
18. Trucos y consejos 292
18.1 Descripción general de trucos y consejos 292
18.2 Copia de seguridad 293
18.3 Ventana acoplable 295
18.4 Cuaderno Jupyter 298
18.5 Agregar espacio en disco 301
18.6 Instalación de red 303
18.7 PCAP para pruebas 305
18.8 Ajuste de alto rendimiento 306
18.9 Eliminación de un nodo 307
18.10 Sal 309
18.11 Salida de Syslog 311
18.12 Zonas horarias 312
19. Servicios públicos 313
19.1 Descripción general de los servicios públicos 313
19,2 jq 314
19.3 así permitir 315
- 5/402 - Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
19.4 restablecimiento de contraseña de autenticación tan elástica 316
19.5 consulta de búsqueda tan elástica 317
19.6 entonces-importar-pcap 318
19.7 entonces-importar-evtx 319
19.8 entonces-monitorear-agregar 320
19.9 estado así 321
19.10 prueba así 322
19.11 so-usuario 323
20. Ayuda 324
20.1 Descripción general de la ayuda 324
20.2 Preguntas frecuentes 325
20.3 Estructura del directorio 329
20.4 Apoyo comunitario 330
20.5 Soporte 331
20.6 Se busca ayuda 332
21. Cebolla de seguridad Pro 334
21.1 Descripción general de Security Onion Pro 334
21.2 Conexión OpenID (OIDC) 335
21.3 LUCAS 349
21,4 FIPS 350
21.5 ESTIG 351
21.6 Notificaciones 353
21.7Kafka 358
21.8 Seguridad Cebolla API 361
21.9 Gestión de consultas activas 363
21.10 Gerente de Gerentes 364
21.11 Servidor MCP 367
Aplicación Security Onion 21.12 para Splunk 368
21.13 Hipervisor 369
21.14. Directorio bajo / 372
21.15. Paso del disco a través de 372
21.16. Disco virtual 372
21.17 Informes 380
21.18 Cebolla AI 385
22. Telemetría 390
22.1 Telemetría SOC 390
22.2 Actualizaciones del sistema operativo Telemetría 391
- 6/402 - Soluciones de cebolla de seguridad, LLC

Tabla de contenidos
22.3 Entrehierro 391
23. Seguridad 392
23.1 Divulgación de vulnerabilidad 392
23.2 Pedir recompensas 392
23.3 Integridad del producto y de la cadena de suministro 392
24. Lista de materiales del software 394
25. Notas de la versión 397
25.1 3.1.0 Revisión [20260528] Cambios 397
25.2 3.1.0 [20260521] Cambios 397
25.3 3.0.0 [20260331] Cambios 398
26. Apéndice 400
26.1 Verificar copia de seguridad 400
26.2 Implementaciones de Internet 400
26.3 Despliegues de espacios aéreos 400
27. Hoja de trucos 402
- 7/402 - Soluciones de cebolla de seguridad, LLC

1. Acerca de
1. Acerca de
1.1 Cebolla de seguridad
Security Onion es una plataforma abierta y gratuita creada por defensores para defensores. Incluye visibilidad de la red, visibilidad del host, detección de intrusiones.
honeypots, gestión de registros y gestión de casos. Security Onion se ha descargado más de 2 millones de veces y está siendo utilizado por seguridad
equipos en todo el mundo para monitorear y defender sus empresas. Nuestro asistente de configuración fácil de usar le permite crear una red distribuida para su
empresa en minutos!
1.2 Soluciones de seguridad Onion, LLC
Doug Burks inició Security Onion como un proyecto abierto y gratuito en 2008 y luego fundó Security Onion Solutions, LLC en 2014.
importante
Security Onion Solutions, LLC es el único proveedor oficial de dispositivos de hardware, capacitación y servicios profesionales para Security Onion.
Para obtener más información sobre estos productos y servicios, consulte el sitio de nuestra empresa en https://securityonionsolutions.com.
1.3 Documentación
Advertencia
La documentación es siempre un trabajo en progreso y es posible que falte alguna documentación o que sea incorrecta. Háganos saber si nota algún problema.
1.3.1 Licencia
Esta documentación tiene licencia CC BY 4.0. Puede leer más sobre esta licencia en https://creativecommons.org/licenses/by/4.0/.
1.3.2 Formatos
Esta documentación se publica en línea en https://securityonion.net/docs. Si está viendo una versión sin conexión de esta documentación pero tiene
Acceso a Internet, es posible que desee cambiar a la versión en línea en https://securityonion.net/docs para ver la última versión.
Esta documentación también está disponible en formato PDF en https://securityonion.net/docs/securityonion-docs.pdf.
Mucha gente ha pedido una versión impresa de nuestra documentación. Ya sea que trabaje en redes aisladas o simplemente quiera un dispositivo portátil
Referencia que no requiere conexión a Internet ni pilas, esto es lo que estabas pidiendo. Gracias a Richard Bejtlich por escribir el
prólogo inspirador! ¡Las ganancias se destinan al Fondo de Tecnología Rural! Puede comprar su copia en https://securityonion.net/book.
1.3.3 Autores
Security Onion Solutions es el autor principal y mantenedor de esta documentación. Parte del contenido ha sido aportado por miembros de nuestro
comunidad. ¡Gracias a todas las personas que han contribuido a esta documentación a lo largo de los años!
1.3.4 Contribuir
¡Agradecemos sus contribuciones a nuestra documentación! Revisaremos cualquier sugerencia y la aplicaremos si procede.
- 8/402 - Soluciones de cebolla de seguridad, LLC

1.3.5 Convención de nomenclatura
Si está accediendo a la versión en línea de la documentación y nota que una página en particular tiene información incorrecta, puede enviar
correcciones haciendo clic en el botón Editar en GitHub en la esquina superior derecha de cada página. Una vez que haya hecho sus correcciones, podrá
Debe enviar su solicitud de extracción (PR) a la rama de desarrollo.
Para enviar una nueva página, puede enviar una solicitud de extracción (PR) a la rama 3/dev del repositorio de documentos en https://github.com/Security-Onion-
Soluciones/documentos.
Las páginas están escritas en formato Markdown y puede encontrar varias guías de Markdown en Internet, incluida https://www.markdownguide.org/
sintaxis básica/.
1.3.5 Convención de nomenclatura
Las nuevas páginas de documentación deben utilizar la siguiente convención de nomenclatura:
• todo en minúsculas
• Extensión de archivo .md
• Lo ideal es que el nombre de la página sea una palabra simple (por ejemplo: suricata.md)
• si es necesario, el nombre de la página puede dividirse con guiones (por ejemplo: network-visibility.md)
- 9/402 - Soluciones de cebolla de seguridad, LLC

2. Introducción
2. Introducción
Security Onion es una plataforma abierta y gratuita creada por defensores para defensores. Incluye visibilidad de la red, visibilidad del host, detección de intrusiones.
honeypots, gestión de registros y gestión de casos.
Para visibilidad de la red, ofrecemos detección basada en firmas a través de Suricata, metadatos de protocolo enriquecidos y extracción de archivos utilizando Zeek o Suricata.
captura de paquetes completos usando Suricata y análisis de archivos. Para visibilidad del host, ofrecemos Elastic Agent que proporciona recopilación de datos y consultas en vivo.
a través de Osquery y gestión centralizada mediante Elastic Fleet. Se pueden agregar honeypots de detección de intrusos basados en OpenCanary a su
implementación para una visibilidad empresarial aún mayor. Todos estos registros fluyen hacia Elasticsearch y hemos creado nuestras propias interfaces de usuario para alertas,
Paneles de control, búsqueda de amenazas, gestión de casos y gestión de redes.
Nota
¡Vea nuestro video de Introducción a Security Onion en https://securityonion.com/demo!
En el siguiente diagrama, vemos Security Onion en una red empresarial tradicional con firewall, estaciones de trabajo y servidores. Puedes usar Seguridad
Cebolla para monitorear el tráfico norte/sur para detectar un adversario que ingresa a un entorno, estableciendo comando y control (C2), o quizás datos
exfiltración. Probablemente también desees monitorear el tráfico de este a oeste para detectar movimiento lateral. A medida que más y más tráfico de nuestra red
se cifra, es importante llenar esos puntos ciegos con visibilidad adicional en forma de telemetría de punto final. Lata de cebolla de seguridad
consuma registros de sus servidores y estaciones de trabajo para que luego pueda buscar en toda su red y registros de host al mismo tiempo.
- 10/402 - Soluciones de cebolla de seguridad, LLC

2. Introducción
- 11/402 - Soluciones de cebolla de seguridad, LLC

2.1 Visibilidad de la red
2.1 Visibilidad de la red
Desde el punto de vista de la visibilidad de la red, Security Onion combina a la perfección la detección de intrusiones, los metadatos de la red, la captura completa de paquetes,
análisis de archivos y honeypots de detección de intrusiones.
2.1.1 Detección de intrusiones
Security Onion genera alertas NIDS (Sistema de detección de intrusiones en la red) al monitorear el tráfico de su red y buscar señales específicas.
huellas dactilares e identificadores que coinciden con el tráfico malicioso, anómalo o sospechoso conocido. Esta es una detección basada en firmas, por lo que
Se podría decir que es similar a las firmas antivirus para la red, pero es un poco más profundo y flexible que eso. Las alertas NIDS son generadas por
Suricata.
2.1.2 Metadatos de la red
A diferencia de la detección de intrusiones basada en firmas que busca agujas específicas en el pajar de datos, los metadatos de red le proporcionan registros de
Conexiones y protocolos estándar como DNS, HTTP, FTP, SMTP, SSH y SSL. Esto proporciona una profundidad real y visibilidad en el contexto de los datos.
y eventos en su red. Security Onion proporciona metadatos de red utilizando su elección de Zeek o Suricata.
2.1.3 Captura de paquetes completos
La captura de paquetes completos es como una cámara de vídeo para su red, pero mejor porque no sólo puede decirnos quién entró y quién salió, sino también exactamente
adónde fueron y qué trajeron o se llevaron (cargas útiles de exploits, correos electrónicos de phishing, exfiltración de archivos). Es una grabadora de la escena del crimen que
puede decirnos mucho sobre la víctima y el contorno de tiza blanca de un huésped comprometido en el suelo. Ciertamente hay evidencia valiosa que
se encuentran en el cuerpo de la víctima, pero las pruebas en el huésped pueden destruirse o manipularse; la cámara no miente, es difícil de engañar y puede
capturar una bala en tránsito. La captura de paquetes completos se escribe en el disco mediante Suricata.
2.1.4 Análisis de archivos
Como Zeek y Suricata monitorean el tráfico de su red, pueden extraer archivos transferidos a través de la red. Strelka puede entonces analizar esos
archivos y proporcionar metadatos adicionales.
2.1.5 Honeypot de detección de intrusiones (IDH)
También tenemos un nodo IDH que le permite construir un nodo que imita servicios. Las conexiones a estos servicios generan alertas automáticamente.
2.2 Visibilidad del anfitrión
Además de la visibilidad de la red, Security Onion proporciona visibilidad de los terminales a través de Elastic Agent, que proporciona recopilación de datos y consultas en vivo a través de
Osquery y gestión centralizada mediante Elastic Fleet.
Para dispositivos como firewalls y enrutadores que no admiten la instalación de agentes, Security Onion puede consumir syslog estándar.
2.3 Herramientas de análisis
Con todas las fuentes de datos mencionadas anteriormente, hay una increíble cantidad de datos disponibles al alcance de su mano. Afortunadamente, Security Onion
integra estrechamente las siguientes herramientas para ayudar a dar sentido a estos datos.
2.3.1 Consola cebolla de seguridad
La consola Security Onion es lo primero que ve cuando inicia sesión en Security Onion. Incluye nuestra interfaz de Alertas que le permite ver todas
de sus alertas NIDS de Suricata.
- 12/402 - Soluciones de cebolla de seguridad, LLC

2.3.1 Consola cebolla de seguridad
Security Onion Console también incluye nuestra interfaz de Paneles que le brinda una buena descripción general no solo de sus alertas NIDS sino también de la red.
registros de metadatos de Zeek o Suricata y cualquier otro registro que pueda estar recopilando.
Hunt es similar a Dashboards, pero sus consultas predeterminadas se centran más en la búsqueda de amenazas.
- 13/402 - Soluciones de cebolla de seguridad, LLC

2.3.1 Consola cebolla de seguridad
Casos es la interfaz de gestión de casos. Mientras trabaja en Alertas, Paneles o Búsqueda, puede encontrar alertas o registros que sean interesantes.
suficiente para enviar a Casos y crear un caso. Otros analistas pueden colaborar con usted mientras trabaja para cerrar ese caso.
Security Onion Console también incluye una interfaz para la recuperación de captura completa de paquetes (PCAP).
- 14/402 - Soluciones de cebolla de seguridad, LLC

2.3.2 CiberChef
Security Onion Console también incluye Detecciones, lo que hace que sea rápido y fácil ajustar sus reglas NIDS, Sigma y YARA.
2.3.2 CiberChef
CyberChef le permite decodificar, descomprimir y analizar artefactos. Alertas, Paneles, Búsqueda y PCAP le permiten acceder rápida y fácilmente
enviar datos a CyberChef para su posterior análisis.
- 15/402 - Soluciones de cebolla de seguridad, LLC

2.4 Flujo de trabajo
2.4 Flujo de trabajo
Todas estas herramientas de análisis trabajan juntas para proporcionar capacidades de análisis eficientes e integrales. Por ejemplo, aquí hay un potencial
flujo de trabajo:
• Vaya a la página Alertas y revise las alertas no reconocidas.
• Utilice Detecciones para ajustar sus reglas y aumentar la relación señal-ruido.
• Revise los paneles para detectar cualquier cosa que parezca sospechosa.
• Una vez que haya encontrado algo que desee investigar, es posible que desee pasar a Hunt para ampliar su búsqueda y buscar información adicional.
registros relacionados con las direcciones IP de origen y destino.
• Si alguna de esas alertas o registros parece interesante, es posible que desee pasar a PCAP para revisar la captura completa de paquetes de toda la transmisión.
• Dependiendo de lo que vea en la transmisión, es posible que desee enviarla a CyberChef para su posterior análisis y decodificación.
• Escalar alertas y registros a Casos y documentar cualquier observable. Gire hacia Hunt para lanzar una red más amplia para esos observables.
• Si tiene implementado el Agente elástico, es posible que desee buscar registros de host adicionales o ejecutar consultas en vivo en sus puntos finales.
utilizando Osquery.
• Finalmente, regrese a Casos.
• Finalmente, regrese a Casos, documente toda la investigación y cierre el caso.
2.5 Escenarios de implementación
Analistas de todo el mundo utilizan Security Onion hoy en día para muchas arquitecturas diferentes. El asistente de configuración de Security Onion le permite
Configure fácilmente el mejor escenario de implementación para satisfacer sus necesidades.
2.6 Conclusión
Después de instalar Security Onion, tendrá una visibilidad completa de la red y del host para su empresa. Nuestras herramientas de análisis le permitirán
utilizar todos esos datos para detectar intrusos más rápidamente y pintar una imagen más completa de lo que están haciendo en su entorno. Prepárate
¡Para quitar las capas de tu empresa y hacer llorar a tus adversarios!
- 16/402 - Soluciones de cebolla de seguridad, LLC

3. Licencia
3. Licencia
Security Onion es una plataforma abierta y gratuita. La mayor parte del software incluido en Security Onion tiene licencias de código abierto.
Los componentes Elastic y Security Onion tienen licencia Elastic License 2.0 (ELv2). Durante la instalación, usted será
Se le solicitará que acepte la licencia Elastic:
Nota
Puede encontrar el texto completo de la Licencia Elastic 2.0 (ELv2) en: https://securityonion.net/license
Puede encontrar el anuncio de Security Onion ELv2 en: https://blog.securityonion.net/2022/08/security-onion-enterprise-features-and.html
- 17/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
4. Usuarios nuevos
¡Bienvenidos usuarios nuevos! ¡Estarás eliminando las capas de tu red en solo unos minutos!
Primero, tenga en cuenta que Security Onion solo admite la arquitectura x86-64 (procesadores Intel o AMD estándar de 64 bits). Si no tienes un x86-64
casilla disponible, entonces una opción puede ser ejecutar Security Onion en la nube. Para obtener más información, consulte la nube de Amazon, la nube de Azure,
y secciones de Google Cloud.
De lo contrario, si tiene una caja x86-64 para su instalación Security Onion IMPORT, verifique que cumpla con el hardware MÍNIMO
Requisitos de 4 GB de RAM, 2 núcleos de CPU y 100 GB de almacenamiento. Si va a instalar Security Onion en una máquina virtual, entonces la VM
Necesita esas especificaciones como mínimo y la máquina host tendrá requisitos de hardware más altos ya que ejecutará el sistema operativo host.
sistema y posiblemente otras máquinas virtuales o aplicaciones. Para obtener más información sobre virtualización, consulte VMware, VirtualBox y Proxmox.
secciones. Una vez que haya verificado que tiene un destino de instalación apropiado, puede proceder a descargar nuestra imagen ISO como se muestra en la
Descargue la sección y luego instale la imagen ISO como se muestra en la sección Instalación.
Una vez que haya instalado Security Onion, ya sea en la nube o localmente, puede configurar IMPORTAR como se muestra a continuación (consulte también la
apartado de configuración).
Una vez que se sienta cómodo con su instalación IMPORT, podrá pasar a instalaciones más avanzadas como se muestra en Arquitectura.
sección.
Después de iniciar la imagen ISO, aparece el menú de inicio:
Cuando se le solicite, ingrese el nombre de usuario y la contraseña que desee:
- 18/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Una vez completada la instalación, se le solicitará que reinicie:
Después de reiniciar, inicie sesión con el nombre de usuario y la contraseña que especificó y luego la instalación se iniciará automáticamente:
- 19/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Realice una instalación estándar:
Cuando se le solicite el tipo de instalación, seleccione IMPORTAR:
- 20/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Si su máquina Security Onion tiene acceso completo a Internet como se describe en la sección Firewall, seleccione Estándar. De lo contrario, seleccione Airgap:
Revise la licencia y acepte:
- 21/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Establezca el nombre de host:
Si utiliza el nombre de host predeterminado de securityonion, verá una advertencia:
- 22/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Seleccione su interfaz de gestión:
Seleccione una dirección IP estática (recomendada) o DHCP:
- 23/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Especifique la dirección IP y la máscara CIDR:
Establecer dirección de puerta de enlace:
- 24/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Ingrese a los servidores DNS:
Configurar el dominio de búsqueda DNS:
- 25/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Si es necesario, puede cambiar el rango de IP predeterminado de Docker:
Si estás conectado a Internet selecciona si es directo o vía proxy:
- 26/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Cree un nombre de usuario para Security Onion Console:
Establecer contraseña para Security Onion Console:
- 27/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Confirme la contraseña para Security Onion Console:
Seleccione cómo acceder a Security Onion Console:
- 28/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Permita conexiones a través del firewall basado en host si es necesario:
Especifique una dirección IP o un rango para permitir el paso del firewall basado en host:
- 29/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Confirme todas las opciones:
Configuración completa:
- 30/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Inicie sesión en la consola Security Onion:
Después de iniciar sesión, verá la página Descripción general de la consola Security Onion:
- 31/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Vaya a la página Grid, haga clic en el botón para expandir el nodo y luego verifique que todos los servicios se estén ejecutando correctamente:
Mientras está en la página Grid, puede importar un archivo PCAP o EVTX usando el botón de carga en la parte inferior de la pantalla:
- 32/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Una vez que se completa la importación, la página Grid debería mostrar un mensaje en la parte superior de la página y proporcionar un enlace a los Paneles para ver todos
alertas y registros de la importación:
Si desea ver solo las alertas, puede ir a la página Alertas, aunque es posible que deba ajustar manualmente el rango de tiempo:
- 33/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Si encuentra algo interesante en las páginas Alertas o Paneles, es posible que desee utilizar las acciones Correlacionar o Buscar para buscar registros relacionados en
la página de caza:
Si encuentra tráfico de red interesante, puede pasar a la captura de paquetes completos mediante la acción PCAP:
- 34/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Puede cambiar la vista a transcripción ASCII para obtener una vista del tráfico más legible para los humanos:
Si necesita consultar trabajos de PCAP anteriores, puede encontrarlos en la página de PCAP:
- 35/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
Las instalaciones IMPORT no admiten agentes remotos, pero si estuviera ejecutando una instalación de producción, podría descargar Elastic Agent
instalador desde Descargas:
La sección Administración le permite administrar cuentas de usuario:
- 36/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
También le permite administrar miembros de Grid:
La sección Administración también le permite configurar varios aspectos del sistema:
- 37/402 - Soluciones de cebolla de seguridad, LLC

4. Usuarios nuevos
También le permite cargar una clave de licencia para funciones empresariales adicionales:
Si llegó al final de esta sección para usuarios nuevos, ¡felicidades! Si tiene alguna pregunta o problema, consulte la sección de Ayuda.
Si le gusta Security Onion, considere compartir en las redes sociales sobre Security Onion para ayudar a correr la voz. ¡Gracias!
- 38/402 - Soluciones de cebolla de seguridad, LLC

5. Primeros pasos
5. Primeros pasos
5.1 Descripción general de cómo empezar
Si está listo para comenzar con Security Onion, es posible que tenga preguntas como:
¿Cuáles son las mejores prácticas recomendadas?
Consulte la sección Mejores prácticas.
¿Cuántas máquinas necesito?
Dependiendo de lo que intente hacer, es posible que necesite desde una máquina hasta miles de máquinas. Los casos de uso y
Las secciones de arquitectura te ayudarán a decidir.
¿Qué tipo de hardware necesita cada una de esas máquinas?
Esto podría ser cualquier cosa, desde una pequeña máquina virtual hasta un gran servidor montado en bastidor con muchos núcleos de CPU, mucha RAM y mucho almacenamiento. el
La sección de hardware proporciona más detalles.
Si solo quiero probar Security Onion en una máquina virtual, ¿cómo creo una máquina virtual?
Consulte las secciones VMware, VirtualBox y Proxmox.
¿Cómo implemento Security Onion en la nube?
Consulte las secciones Amazon Cloud, Azure Cloud y Google Cloud.
¿Qué pasa si tengo problemas para iniciar la imagen ISO?
Consulte la sección Problemas de arranque.
¿Qué pasa si estoy en una red Airgap?
Revise la sección Airgap.
Una vez que he iniciado la imagen ISO, ¿cómo la instalo?
Consulte la sección Instalación.
Después de la instalación, ¿cómo configuro Security Onion?
La sección Configuración cubre muchos casos de uso diferentes.
¿Hay algo que deba hacer después de la configuración?
Consulte la sección posterior a la instalación.
- 39/402 - Soluciones de cebolla de seguridad, LLC

5.2 Mejores prácticas
5.2 Mejores prácticas
Security Onion ofrece muchas opciones y flexibilidad, pero para obtener mejores resultados recomendamos las siguientes mejores prácticas.
5.2.1 Instalación
• Descargue y verifique nuestra imagen ISO como se muestra en la sección Descargar.
• Para implementaciones de producción, prefiera hardware dedicado a máquinas virtuales cuando sea posible (consulte la sección Hardware).
• Si se deben utilizar máquinas virtuales, asegúrese de que los recursos estén dedicados adecuadamente a las máquinas virtuales para evitar la contención de recursos.
• Utilice almacenamiento local y evite NFS, NAS, iSCSI, etc.
• Especifique adecuadamente su hardware para satisfacer su uso actual y permitir el crecimiento con el tiempo.
• Cuando sea posible, recomendamos utilizar un TAP dedicado en lugar de puertos SPAN.
• Asegúrese de que todos los firewalls de red tengan implementadas las reglas de firewall adecuadas para permitir el funcionamiento y las actualizaciones continuas (consulte la sección Firewall
sección).
5.2.2 Configuración
• Asegúrese de que tanto el nombre de host como la dirección IP sean correctos durante la instalación.
• Evite cambiar el nombre de host y la dirección IP después de la instalación.
• Linux distingue entre mayúsculas y minúsculas, mientras que otros sistemas operativos podrían no hacerlo, por lo que recomendamos usar minúsculas para cosas como nombres de host,
nombres de usuario, etc
5.2.3 Evite software y modificaciones de terceros
• Security Onion es una plataforma gratuita y abierta basada en distribuciones estándar de Linux, pero recomendamos tratarla como un dispositivo y evitar
instalar software de terceros, ya que esto puede entrar en conflicto con nuestros componentes y causar problemas al actualizar.
• Evite instalar herramientas de automatización como Puppet y Chef, ya que pueden entrar en conflicto con nuestra automatización de Salt existente.
• Evite instalar herramientas de monitoreo como Zabbix, ya que esto puede entrar en conflicto con nuestro monitoreo Influxdb existente.
• Evite instalar agentes de seguridad de terminales de terceros, ya que pueden interrumpir la funcionalidad o introducir una sobrecarga de rendimiento inaceptable.
• Evite cambiar los permisos de archivos o la configuración de umask.
• Las pautas de refuerzo pueden alterar la funcionalidad, por lo que si debe aplicar esas pautas de refuerzo, le recomendamos realizar pruebas exhaustivas antes.
implementar en producción.
5.2.4 Manténgase actualizado
• Únase a nuestro foro de discusión en https://securityonion.net/discuss o suscríbase a uno de nuestros canales de redes sociales para recibir notificaciones sobre Seguridad.
Actualizaciones de cebolla.
• Mantenga su implementación actualizada ya que frecuentemente solucionamos errores y agregamos nuevas características.
• Si es posible, pruebe las actualizaciones en una implementación de prueba antes de implementarlas en producción.
- 40/402 - Soluciones de cebolla de seguridad, LLC

5.3 Casos de uso
5.3 Casos de uso
Si va a implementar Security Onion, primero debe decidir cuál es su caso de uso. En esta sección, analizaremos algunos casos de uso comunes.
y cómo se corresponden con nuestros diferentes tipos de arquitectura. Esto podría ser cualquier cosa, desde una instalación de importación temporal en un pequeño archivo virtual.
máquina en su computadora portátil personal hasta una implementación empresarial grande y escalable que consta de un nodo administrador, múltiples nodos de búsqueda,
y muchos nodos sensores.
5.3.1 Importación mínima
Suponga que solo desea importar archivos PCAP o EVTX o que tiene hardware limitado y solo desea realizar una instalación mínima.
algo de experiencia con Security Onion. Instale Security Onion y elija la opción Importar. Esto se puede hacer en una máquina virtual mínima.
con tan solo 4 GB de RAM. Puede leer más sobre la opción Importar en la sección Usuarios nuevos y en la sección Arquitectura.
5.3.2 Visibilidad mínima de la red
Suponga que tiene una red pequeña en la que solo desea una visibilidad básica de la red. Esto podría estar monitoreando el tráfico desde un TAP o SPAN.
puerto en un laboratorio doméstico u otra red pequeña que no requiera una instalación de producción. Instale Security Onion y elija la Evaluación
opción. Puede leer más sobre la opción Evaluación en la sección Arquitectura.
5.3.3 Visibilidad mínima de la red con OPNsense Firewall en lugar de TAP o SPAN
Suponga que tiene un segmento de red pequeño en el que solo desea cierta visibilidad básica de la red pero no tiene la capacidad de recopilar tráfico.
a través del puerto TAP o SPAN pero tiene un firewall OPNsense. Instale Security Onion, elija la opción ManagerSearch y luego siga las instrucciones
Sección OPNsense para recopilar registros de firewall, datos de Netflow y alertas de Suricata NIDS. Puede leer más sobre la opción ManagerSearch en el
Sección de arquitectura.
5.3.4 Recolector de flujo de red mínimo
Suponga que tiene una red pequeña donde solo desea recopilar algunos datos de Netflow. Instale Security Onion, elija ManagerSearch
y luego siga la sección Netflow. Puede leer más sobre la opción ManagerSearch en la sección Arquitectura.
5.3.5 Gestión mínima de registros
Suponga que tiene una red pequeña en la que solo desea una visibilidad básica del host. Esto podría implicar desplegar agentes en un pequeño número de
escritorios y servidores y/o recopilar syslog desde firewall u otros dispositivos. Instale Security Onion, elija la opción ManagerSearch y
luego implemente Elastic Agent en sus hosts y revise las secciones Integraciones de hosts y terceros. Puedes leer más sobre el
Opción ManagerSearch en la sección Arquitectura.
5.3.6 Visibilidad mínima de red y host
Suponga que tiene una red pequeña en la que desea visibilidad tanto de la red como del host. Instale Security Onion y elija el
Opción independiente. Luego, esta máquina detectará el tráfico de red desde su puerto TAP o SPAN y también admitirá la implementación del Elastic Agent en
otros anfitriones. Puede leer más sobre la opción Independiente en la sección Arquitectura.
- 41/402 - Soluciones de cebolla de seguridad, LLC

5.3.7 Implementación empresarial mínima
5.3.7 Implementación empresarial mínima
Suponga que tiene una red pequeña o mediana en la que desea cierta visibilidad tanto para la red como para los hosts. Una implementación empresarial mínima
se vería así:
• Instale la primera instancia de Security Onion y elija la opción ManagerSearch.
• Implementar el Agente Elastic en los hosts.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos de sensores. Analizarán el tráfico de red desde
su puerto TAP o SPAN.
Puede leer más sobre implementaciones distribuidas en la sección Arquitectura.
5.3.8 Implementación empresarial más escalable
Suponga que tiene una red mediana o grande en la que desea cierta visibilidad tanto para la red como para los hosts. Una empresa más escalable
La implementación se vería así:
• Instale la primera instancia de Security Onion y elija la opción Administrador.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos de búsqueda. Almacenarán registros y le permitirán
buscarlos.
• Implementar el Agente Elastic en los hosts. Recopilarán registros y los enviarán a la red.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos de sensores. Analizarán el tráfico de red desde
su puerto TAP o SPAN.
Puede leer más sobre implementaciones distribuidas en la sección Arquitectura.
5.3.9 Implementación empresarial integral
Suponga que tiene una red grande en la que desea máxima visibilidad tanto para la red como para los hosts. Una implementación distribuida integral
se vería así:
• Instale la primera instancia de Security Onion y elija la opción Administrador.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos de búsqueda. Almacenarán registros y le permitirán
buscarlos.
• Instale Security Onion en una máquina en su DMZ y únala a la red como un nodo Fleet. Este nodo administrará sus agentes Elastic ya sea
están dentro o fuera del sitio.
• Implementar el Agente Elastic en los hosts. Recopilarán registros y los enviarán a la red.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos de sensores. Analizarán el tráfico de red desde
su puerto TAP o SPAN.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos receptores. Esto proporciona equilibrio de carga y
Redundancia de tuberías.
• Instale Security Onion en una o más máquinas adicionales y únalas a la red como nodos IDH. Proporcionarán honeypot y
capacidades de engaño.
Puede leer más sobre implementaciones distribuidas en la sección Arquitectura.
- 42/402 - Soluciones de cebolla de seguridad, LLC

5.4 Arquitectura
5.4 Arquitectura
En la sección Casos de uso, analizamos algunos de los casos de uso más comunes. Esta sección analizará cómo se ven esos diferentes casos de uso.
como desde una perspectiva arquitectónica.
5.4.1 Importar
La arquitectura más simple es un nodo Importar. Un nodo de importación es una única caja independiente que ejecuta los componentes suficientes para poder
importe archivos PCAP o evtx utilizando la página Grid. No admite la adición de agentes Elastic ni nodos Security Onion adicionales. por un completo
Para obtener un tutorial sobre la opción Importar, consulte la sección Usuarios nuevos.
5.4.2 Evaluación
La siguiente arquitectura es Evaluación. Es un poco más complicado que Importar porque tiene una interfaz de red dedicada a olfatear en vivo
tráfico desde un puerto TAP o SPAN. Los procesos monitorean el tráfico en esa interfaz de rastreo y generan registros. Elastic Agent recopila esos registros
y los envía directamente a Elasticsearch donde se analizan e indexan. El modo de evaluación está diseñado para una instalación rápida para
Pruebe temporalmente Security Onion. No está diseñado para uso en producción en absoluto y no admite la adición de agentes Elastic ni
Nodos de cebolla de seguridad.
- 43/402 - Soluciones de cebolla de seguridad, LLC

5.4.3 Independiente
5.4.3 Independiente
Independiente es similar a Evaluación en que todos los componentes se ejecutan en una sola caja. Sin embargo, en lugar de que Elastic Agent envíe registros directamente a
Elasticsearch los envía a Logstash, que a su vez los envía a Redis para ponerlos en cola. Una segunda canalización de Logstash extrae los registros de Redis y
los envía a Elasticsearch, donde se analizan e indexan.
Este tipo de implementación se utiliza normalmente para pruebas, laboratorios, pruebas de concepto o entornos de muy bajo rendimiento. No es tan escalable como distribuido.
despliegue.
- 44/402 - Soluciones de cebolla de seguridad, LLC

5.4.4 Seguridad del escritorio Onion
5.4.4 Seguridad del escritorio Onion
El instalador incluye una opción de Security Onion Desktop que crea un entorno de escritorio simple. Este entorno incluye un navegador web.
que le permite iniciar sesión en una implementación de Security Onion existente. También incluye algunas utilidades de analista como Wireshark y NetworkMiner.
Para obtener más información, consulte la sección Security Onion Desktop.
5.4.5 Distribuido
Una implementación distribuida estándar incluye un nodo administrador, uno o más nodos sensores que ejecutan componentes de sensores de red y uno o más
más nodos de búsqueda que ejecutan componentes de búsqueda elásticos. Esta arquitectura puede costar más por adelantado, pero proporciona una mayor escalabilidad y
rendimiento, ya que simplemente puede agregar más nodos para manejar más tráfico o fuentes de registro.
• Tipo de implementación recomendado
• Consta de un nodo administrador, uno o más nodos sensores y uno o más nodos de búsqueda.
Nota
Si instala un nodo de administrador dedicado, también debe implementar uno o más nodos de búsqueda. De lo contrario, todos los registros se pondrán en cola en el administrador y tendrán
No hay lugar para guardarlo. Si tiene un número limitado de nodos que puede implementar, puede instalar un nodo de búsqueda de administrador para que su administrador
El nodo puede actuar como un nodo de búsqueda y almacenar esos registros. Sin embargo, tenga en cuenta que el rendimiento general y la escalabilidad de una búsqueda de administrador
El nodo será menor en comparación con nuestra arquitectura recomendada de nodo administrador dedicado y nodos de búsqueda separados.
- 45/402 - Soluciones de cebolla de seguridad, LLC

5.4.5 Distribuido
- 46/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
5.4.6 Tipos de nodos
Gestión
El nodo administrador ejecuta Security Onion Console y Kibana. Tiene su propia instancia local de Elasticsearch, pero se usa principalmente para
administrar el clúster de Elasticsearch una vez que los nodos de búsqueda se unen al clúster. Un analista se conecta al nodo administrador desde una estación de trabajo cliente
(quizás Security Onion Desktop) para ejecutar consultas y recuperar datos.
Tenga en cuenta que un nodo de administrador dedicado requiere nodos de búsqueda separados. También tenga en cuenta que un nodo administrador dedicado tiene que comenzar con
el rol del nodo de datos. Cuando más tarde se una a un nodo de búsqueda independiente, es posible que desee migrar los datos del administrador al nodo de búsqueda.
y luego elimine la función del nodo de datos del administrador. Para obtener más información, consulte la sección Elasticsearch.
El nodo administrador ejecuta los siguientes componentes:
• Consola cebolla de seguridad
• Búsqueda elástica
• Almacenamiento de registros
• Kibana
• ElastAlert
• Redis
Nodo de búsqueda
Los nodos de búsqueda extraen registros de la cola de Redis en el nodo administrador y luego analizan e indexan esos registros. Cuando un usuario consulta al administrador
nodo, el nodo administrador consulta los nodos de búsqueda y estos devuelven resultados de búsqueda.
Los nodos de búsqueda ejecutan los siguientes componentes:
• Búsqueda elástica
• Almacenamiento de registros
Búsqueda de administrador
Un nodo de búsqueda de administrador es al mismo tiempo un nodo de administrador y un nodo de búsqueda. Dado que analiza, indexa y busca datos, tiene
Requisitos de hardware más altos que un nodo administrador normal.
Un nodo de búsqueda de administrador ejecuta los siguientes componentes:
• Consola cebolla de seguridad
• Búsqueda elástica
• Almacenamiento de registros
• Kibana
• ElastAlert
• Redis
Nodo sensor
Un nodo sensor reenvía alertas y registros de Suricata y Zeek a través de Elastic Agent a Logstash en el nodo administrador, donde se almacenan
Elasticsearch en el nodo administrador o en un nodo de búsqueda (si el nodo administrador se ha configurado para usar un nodo de búsqueda). Captura de paquetes completos
registrado por Suricata permanece en el propio nodo sensor.
Los nodos sensores ejecutan los siguientes componentes:
• Zeek
• Suricata
- 47/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
Nodo independiente de flota elástica
Un nodo independiente de Elastic Fleet es ideal cuando hay una gran cantidad de puntos finales Elastic implementados. Reduce la cantidad de gastos generales en
el nodo Manager transfiriendo la carga de trabajo asociada con la gestión de puntos finales a un sistema dedicado. También es útil para fuera de la red.
Puntos finales de Elastic Agent que no tienen acceso remoto al nodo Manager, ya que se puede implementar en DMZ y TCP/8220 (Elastic Agent
Tráfico de red de administración) y TCP/5055 (trasvase de registros de Elastic Agent) accesibles para sus puntos finales fuera de la red.
Nodo receptor
Los nodos receptores fueron diseñados con 2 propósitos en mente:
• reducir la carga sobre el administrador
• ofrecer redundancia de canalización
Cada nodo receptor ejecuta Logstash y Redis y permite que los nodos de búsqueda continúen procesando eventos en caso de que el administrador
El nodo está fuera de línea. Cuando un nodo receptor se une al grid, Elastic Agent en todos los nodos agrega esta nueva dirección como una salida de Logstash con carga equilibrada.
Los nodos de búsqueda agregan este nuevo nodo como otra entrada de Logstash. Los nodos receptores son "activos-activos" y puedes agregar tantos como quieras
(dentro de lo razonable) y los eventos se equilibrarán entre ellos.
- 48/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
- 49/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
Si no tiene ningún nodo receptor y el administrador deja de funcionar, los nodos de búsqueda no indexan nada porque no pueden conectarse
Redis. Los agentes no pueden conectarse a Logstash, por lo que la canalización comienza a realizar copias de seguridad de los agentes.
En este mismo escenario con un nodo receptor, los agentes no podrían conectarse a Logstash en el administrador y, por lo tanto, intentarían
conectarse al nodo receptor. Una vez conectados, enviarían sus registros al receptor.
Los nodos de búsqueda se conectan a los nodos administrador y receptor y extraen eventos de la cola de Redis. Si el manager cae, busca
Los nodos seguirán extrayendo los eventos de registro de la cola en el nodo receptor. Esto permite el escalamiento de la tubería. Más receptores + más
nodos de búsqueda = más volumen de ingesta de eventos.
Si tiene un administrador o managersearch que está bajo una gran carga debido al manejo de un gran volumen de eventos, entonces los recursos del sistema pueden ser
se libera al indicarle al Agente elástico que solo envíe eventos a los nodos receptores en el entorno. Una vez todo configurable y avanzado
Los ajustes están habilitados, esta función se puede configurar en la interfaz de usuario de configuración de SOC en elasticfleet > enable_manager_output. Estableciendo esto en Falso
evitará que Elastic Agent envíe eventos al administrador, a la búsqueda del administrador o a los nodos independientes.
Los nodos receptores deben estar cerca de los nodos de búsqueda porque cuando agrega un nuevo nodo receptor a la cuadrícula, los nodos de búsqueda agregan Redis.
servicio como entrada en sus configuraciones automáticamente. Si colocara un nodo receptor en un sitio remoto, entonces TODOS sus nodos de búsqueda
Intentará acceder a esa cola de Redis de forma remota. No se ahorra ancho de banda al colocar un nodo receptor en un sitio remoto.
Hay un par de cosas que se deben tener en cuenta con respecto a los nodos receptores y los agentes elásticos. El primero es Fleet, que se encarga de cosas como la actualización.
los agentes y programar búsquedas. El otro es la salida del registro de Elastic Agent, que en este caso es Logstash ejecutándose en el administrador o
nodo receptor. Debido a las limitaciones de las licencias de Elastic, solo podemos tener una única política de salida. Eso significa que cuando agregas un receptor o un
nodo de flota se agrega a una lista que se distribuye a los agentes. Los agentes bajan por esa lista y se detienen después de una conexión exitosa. el
La única forma de dirigir agentes a receptores específicos es utilizar reglas de firewall para bloquear agentes a ciertos receptores. Nuevamente tenga en cuenta que no hay
Aquí se ahorra ancho de banda porque los nodos de búsqueda aún necesitan vaciar la cola de Redis en los nodos receptores.
Nodo Honeypot de detección de intrusiones (IDH)
El nodo IDH imita servicios comunes como HTTP, FTP y SSH. Cualquier interacción con estos servicios falsos resultará automáticamente en una
alerta.
- 50/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
- 51/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
Nodo pesado
También existe la opción de tener un nodo administrador y uno o más nodos pesados.
Advertencia
Los nodos pesados NO se recomiendan para la mayoría de los usuarios debido a razones de rendimiento y solo deben usarse con fines de prueba o en entornos de baja potencia.
entornos de rendimiento.
• Recomendado solo si no es posible una implementación distribuida estándar
• Consta de un nodo administrador y uno o más nodos pesados.
• Cada nodo pesado es un clúster elástico independiente al que el administrador consulta mediante una búsqueda entre clústeres.
- 52/402 - Soluciones de cebolla de seguridad, LLC

5.4.6 Tipos de nodos
Nota
Los nodos pesados no consumen de la cola de Redis en el administrador. Esto significa que si sólo tienes un administrador y nodos pesados, entonces Redis
La cola en el administrador crecerá y nunca se agotará. Para evitar esto, tienes dos opciones. Si está iniciando una nueva implementación, puede hacer
su administrador realice una búsqueda de administrador para vaciar su propia cola de Redis. Alternativamente, si tiene una implementación existente con un administrador y
Si desea evitar la reconstrucción, puede agregar un nodo de búsqueda separado (NO un nodo pesado) para consumir desde la cola de Redis en el administrador.
Los nodos pesados ​​realizan tareas de sensores y almacenan sus propios registros en su propia instancia local de Elasticsearch. Esto da como resultado un mayor hardware.
requisitos y menor rendimiento. Los nodos pesados ​​NO extraen registros de la cola de Redis en el administrador como lo hacen los nodos de búsqueda.
Los nodos pesados ejecutan los siguientes componentes:
• Búsqueda elástica
• Zeek
• Suricata
Hay dos instancias de Elastic Agent que se ejecutan en un Nodo Pesado:
Instancia 1: no está conectado a Fleet (se ejecuta de forma independiente), se ejecuta en un contenedor, recoge registros /nsm/ y otros registros locales (SOC) y los envía a
el clúster local de Heavy Node ES.
Instancia 2: conectada al servidor Grid Fleet, se ejecuta directamente en el nodo pesado. Actualmente no estoy recogiendo ningún registro, pero tiene Osquery
integración instalada.
- 53/402 - Soluciones de cebolla de seguridad, LLC

5.5 Hardware
5.5 Hardware
La sección Arquitectura debería haberle ayudado a determinar cuántas máquinas necesitará para su implementación. Esta sección te ayudará
determine qué tipo de especificaciones de hardware necesitará cada una de esas máquinas.
5.5.1 Arquitectura de la CPU
Security Onion solo admite la arquitectura x86-64 (procesadores Intel o AMD estándar de 64 bits).
Advertencia
¡No admitimos ARM ni ningún otro procesador que no sea x86-64!
5.5.2 Especificaciones mínimas
| Tipo de nodo | Núcleos de CPU | RAM | Almacenamiento | NIC |
| ------------- | --------- | ---- | ------- | ---- |
| Escritorio | 2 | 4 GB | 50 GB | 1 |
| Importar | 2 | 4 GB | 100 GB | 1 |
| evaluación | 4 | 8 GB | 200GB | 2 |
| Independiente | 4 | 24GB | 200 GB | 2 |
| Gerente | 4 | 16GB | 200 GB | 1 |
| Administrador de búsqueda | 8 | 16 GB | 200GB | 1 |
| Nodo de búsqueda | 4 | 16GB | 200 GB | 1 |
| Sensores | 4 | 12GB | 200GB | 2 |
| Nodo pesado | 4 | 16GB | 200GB | 2 |
| Nodo IDH | 2 | 1 GB | 12 GB | 1 |
| Nodo de flota | 4 | 4GB | 200GB | 1 |
| Nodo receptor | 2 | 8GB | 200GB | 1 |
Advertencia
Tenga en cuenta que estos son los requisitos mínimos absolutos. Sus requisitos pueden aumentar drásticamente a medida que habilite más servicios,
monitorear más tráfico y consumir más registros. Para obtener más información, consulte las secciones detalladas a continuación.
5.5.3 Importar
Una instalación de importación ejecuta los procesos mínimos necesarios para importar archivos PCAP o EVTX y ver los resultados. Puedes leer más sobre
Importar en la sección Usuarios nuevos.
5.5.4 Evaluación
Una instalación de Eval ejecuta los procesos mínimos necesarios para que una sola máquina detecte el tráfico de red en vivo desde un puerto TAP o SPAN y vea
los resultados. Por lo tanto, sus requisitos de hardware son superiores a los de Importación, como se muestra en la tabla anterior. Eval está diseñado para temporal
Instalaciones o instalaciones de homelab con un presupuesto. A diferencia de una instalación independiente completa, la evaluación NO está diseñada para uso en producción. en
Para minimizar el uso de RAM, Eval no ejecuta Logstash o Redis en absoluto.
5.5.5 Implementaciones de producción
Para obtener mejores resultados, recomendamos comprar hardware nuevo que cumpla con los requisitos de hardware que se detallan a continuación.
- 54/402 -
Soluciones de cebolla de seguridad, LLC

5.5.6 Almacenamiento
consejo
Si planea comprar hardware nuevo, considere los dispositivos Security Onion oficiales de Security Onion Solutions en https://
seguridadonionsolutions.com. Nuestros dispositivos personalizados ya han sido diseñados para ciertos roles y niveles de tráfico y tienen Security Onion pre-
instalado. Comprar en Security Onion Solutions le ahorrará tiempo y esfuerzo y le ayudará a respaldar el desarrollo de Security Onion como una aplicación gratuita y
plataforma abierta!
5.5.6 Almacenamiento
Solo admitimos almacenamiento local. El almacenamiento remoto como SAN/iSCSI/FibreChannel/NFS aumenta la complejidad y los puntos de falla, y tiene serios problemas.
implicaciones de rendimiento. Es posible que pueda hacer que el almacenamiento remoto funcione, pero no brindamos ningún soporte para ello. Al utilizar el almacenamiento local,
mantiene todo autónomo y no tiene que preocuparse por competir por los recursos. El almacenamiento local suele ser el más costoso
solución eficiente también.
5.5.7 tarjeta de red
Necesitará una interfaz de red cableada dedicada a la administración (preferiblemente conectada a una red de administración dedicada). nosotros
Recomendamos utilizar direcciones IP estáticas siempre que sea posible. Para simplificar las cosas, recomendamos solo una interfaz de red con una dirección IP.
Si tiene varias interfaces de red con direcciones IP, el tráfico de Security Onion se dirigirá de forma predeterminada a la interfaz con la puerta de enlace predeterminada.
Si planea rastrear el tráfico de red desde un puerto TAP o SPAN, necesitará una o más interfaces dedicadas a rastrear (sin dirección IP).
El instalador desactivará automáticamente las funciones de descarga de NIC, como tso, gso y gro en las interfaces de detección para garantizar que Suricata
y Zeek obtienen una visión precisa del tráfico.
Asegúrese de obtener tarjetas de red de buena calidad, especialmente para olfatear. La mayoría de los usuarios reportan buenas experiencias con las tarjetas Intel.
Security Onion está diseñado para utilizar interfaces cableadas. Es posible que puedas hacer que las interfaces inalámbricas funcionen, pero no lo recomendamos ni lo admitimos.
5.5.8 SAI
Como ocurre con la mayoría de los sistemas informáticos, querrás evitar cortes de energía u otros apagados desagradables. Por favor considere un UPS (Ininterrumpible
Power Supply) para implementaciones de producción.
5.5.9 Pila elástica
Recomendamos colocar todo el almacenamiento elástico (/nsm/elasticsearch) en un SSD o en un disco de giro rápido en una configuración RAID 10.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.10 Implementaciones independientes
En una implementación independiente, los componentes del administrador y los componentes del sensor se ejecutan en una sola caja, por lo que sus requisitos de hardware serán
reflejar eso. Necesitará como mínimo 24 GB de RAM, 4 núcleos de CPU y 200 GB de almacenamiento. Con un mínimo de 24 GB de RAM, es posible que necesites cambiar
espacio para evitar problemas. Considere 32 GB de RAM o más si planea monitorear incluso una pequeña cantidad de tráfico de red. Más tráfico de red
significa mayores requisitos de hardware.
- 55/402 - Soluciones de cebolla de seguridad, LLC

5.5.11 Nodo administrador con almacenamiento y búsqueda de registros locales
Este tipo de implementación se recomienda para fines de evaluación, POC (prueba de concepto) y sensor único de tamaño pequeño a mediano.
implementaciones. Aunque puede implementar Security Onion de esta manera, se recomienda separar los componentes backend y
componentes de los sensores.
• CPU: se utiliza para analizar eventos entrantes, indexar eventos entrantes, buscar metadatos, capturar PCAP, analizar paquetes y ejecutar la interfaz.
componentes. A medida que aumente el consumo de datos y eventos, se requerirá una mayor cantidad de CPU.
• RAM: Se utiliza para Logstash, Elasticsearch, caché de disco para Lucene, Suricata, Zeek, etc. La cantidad de RAM disponible afectará directamente la búsqueda.
velocidades y confiabilidad, así como capacidad para procesar y capturar tráfico.
• Disco: Se utiliza para el almacenamiento de metadatos indexados. Una mayor cantidad de almacenamiento permite un período de retención más prolongado. Normalmente se recomienda
retener no más de 30 días de índices calientes de Elasticsearch.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.11 Nodo administrador con almacenamiento y búsqueda de registros locales
En una implementación distribuida empresarial, un nodo administrador almacenará registros de sí mismo y de los nodos sensores. También puede actuar como destino de syslog.
para que otras fuentes de registros se indexen en Elasticsearch. Un nodo de administrador empresarial debe tener 8 núcleos de CPU como mínimo, 16-128 GB de RAM,
y suficiente espacio en disco (se recomiendan varios terabytes) para cumplir con sus requisitos de retención.
• CPU: se utiliza para analizar eventos entrantes, indexar eventos entrantes y buscar metadatos. A medida que aumenta el consumo de datos y eventos, más
Se requerirá CPU.
• RAM: Se utiliza para Logstash, Elasticsearch y caché de disco para Lucene. La cantidad de RAM disponible afectará directamente las velocidades de búsqueda y
confiabilidad.
• Disco: Se utiliza para el almacenamiento de metadatos indexados. Una mayor cantidad de almacenamiento permite un período de retención más prolongado. Normalmente se recomienda
retener no más de 30 días de índices calientes de Elasticsearch.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.12 Nodo administrador con nodos de búsqueda separados
Este tipo de implementación utiliza nodos de búsqueda para analizar e indexar eventos. Como resultado, los requisitos de hardware del nodo administrador son
reducido. Un nodo de administrador empresarial debe tener al menos entre 4 y 8 núcleos de CPU, 16 GB de RAM y entre 200 GB y 1 TB de espacio en disco. Mucha gente elige
alojar su nodo administrador en su granja de VM, ya que tiene menores requisitos de hardware que los sensores, pero necesita mayor confiabilidad y disponibilidad.
• CPU: Se utiliza para recibir eventos entrantes y colocarlos en Redis. Se utiliza para ejecutar todos los componentes web front-end y búsqueda agregada.
resultados de los nodos de búsqueda.
• RAM: Se utiliza para Logstash y Redis.
• Disco: Se utiliza para fines generales del sistema operativo.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.13 Nodo de búsqueda
Los nodos de búsqueda aumentan la capacidad de búsqueda y retención con respecto a Elasticsearch. Estos nodos analizan e indexan eventos y proporcionan la
capacidad de escalar horizontalmente a medida que aumenta la ingesta general de datos. Los nodos de búsqueda deben tener al menos entre 4 y 8 núcleos de CPU, entre 16 y 64 GB de RAM y 200 GB de
espacio en disco o más dependiendo de sus requisitos de registro.
• CPU: Se utiliza para analizar eventos entrantes e indexar eventos entrantes. A medida que aumente el consumo de datos y eventos, se requerirá más CPU.
• RAM: Se utiliza para Logstash, Elasticsearch y caché de disco para Lucene. La cantidad de RAM disponible afectará directamente las velocidades de búsqueda y
confiabilidad.
• Disco: Se utiliza para el almacenamiento de metadatos indexados. Una mayor cantidad de almacenamiento permite un período de retención más prolongado. Normalmente se recomienda
retener no más de 30 días de índices calientes de Elasticsearch.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
- 56/402 - Soluciones de cebolla de seguridad, LLC

5.5.14 Nodo sensor
5.5.14 Nodo sensor
Un nodo sensor ejecuta únicamente componentes del sensor y envía metadatos al nodo administrador. Todo PCAP permanece local al sensor y es
se accede mediante el uso de un agente.
• CPU: Se utiliza para analizar y almacenar el tráfico de la red. A medida que aumenta el ancho de banda monitoreado, se requerirá una mayor cantidad de CPU. Vea abajo.
• RAM: Se utiliza para escribir caché y procesar tráfico.
• Disco: Se utiliza para el almacenamiento de PCAP y metadatos. Una mayor cantidad de almacenamiento permite un período de retención más prolongado.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.15 Nodo pesado (Sensor con componentes Elasticsearch)
Un nodo pesado ejecuta todos los componentes del sensor Y los componentes elásticos localmente. Esto aumenta drásticamente los requisitos de hardware. en esto
En este caso, todos los metadatos indexados y PCAP se conservan localmente. Cuando se realiza una búsqueda a través de Kibana, el nodo administrador consulta la información de este nodo.
Instancia de búsqueda elástica. Necesitará como mínimo 16 GB de RAM, 4 núcleos de CPU y 200 GB de almacenamiento. Con un mínimo de 16 GB de RAM, podrás
Necesita espacio de intercambio para evitar problemas. Recomendamos un mínimo de 24 GB de RAM si planea monitorear el tráfico. Cuanto más tráfico planees
El seguimiento de este requisito de RAM también aumentará.
• CPU: se utiliza para analizar eventos entrantes, indexar eventos entrantes y buscar metadatos. Como ancho de banda monitoreado (y la cantidad de ancho de banda total)
datos/eventos) aumenta, se requerirá una mayor cantidad de CPU.
• RAM: Se utiliza para Logstash, Elasticsearch y caché de disco para Lucene. La cantidad de RAM disponible afectará directamente las velocidades de búsqueda y
confiabilidad.
• Disco: Se utiliza para el almacenamiento de metadatos indexados. Una mayor cantidad de almacenamiento permite un período de retención más prolongado. Normalmente se recomienda
retener no más de 30 días de índices calientes de Elasticsearch.
Consulte la sección Arquitectura para conocer escenarios de implementación detallados.
5.5.16 Nodo receptor
Dado que los nodos receptores solo ejecutan Logstash y Redis, no requieren mucha CPU ni espacio en disco. Sin embargo, más RAM significa que puedes configurar un
tamaño de cola más grande para Redis.
5.5.17 Nodo Honeypot de detección de intrusiones (IDH)
Para un nodo IDH, los requisitos generales del sistema son bajos: 1 GB de RAM, 2 núcleos de CPU, 1 NIC y 100 GB de espacio en disco.
5.5.18 Consideraciones sobre el hardware del sensor
Las siguientes consideraciones de hardware se aplican a los sensores. Si está utilizando un tipo de implementación independiente o de nodo pesado, tenga en cuenta que
aumentar drásticamente los requisitos de CPU/RAM/almacenamiento.
Virtualización
Recomendamos hardware físico dedicado (especialmente si está monitoreando mucho tráfico) para evitar competir por los recursos. Los sensores pueden ser
virtualizados, pero deberá asegurarse de que se les asignen recursos suficientes.
CPU
Suricata y Zeek consumen mucha CPU. Cuanto más tráfico esté monitoreando, más núcleos de CPU necesitará. Una estimación aproximada
Serían 200Mbps por trabajador de Suricata o trabajador de Zeek. Entonces, si tiene un enlace de 1 Gbps completamente saturado y está ejecutando Suricata para alertas NIDS
y Zeek para metadatos, entonces necesitarás al menos 5 trabajadores de Suricata y 5 trabajadores de Zeek. Esto significa que necesitarás al menos 10 núcleos de CPU para
Suricata y Zeek con núcleos de CPU adicionales para captura completa de paquetes y/u otros servicios. Si está monitoreando una gran cantidad de tráfico y/
- 57/402 - Soluciones de cebolla de seguridad, LLC

5.5.18 Consideraciones sobre el hardware del sensor
o tiene una pequeña cantidad de núcleos de CPU, podría considerar usar Suricata tanto para alertas como para metadatos. Esto elimina la necesidad de que Zeek y
permite un uso más eficiente de la CPU.
RAM
El uso de RAM depende en gran medida de varias variables:
• los servicios que usted habilita
• los tipos de tráfico que estás monitoreando
• la cantidad real de tráfico que estás monitoreando (ejemplo: puedes estar monitoreando un enlace de 1 Gbps pero solo usa 200 Mbps la mayor parte del tiempo)
• la cantidad de pérdida de paquetes que es "aceptable" para su organización
Para obtener el mejor rendimiento, sobreaprovisione RAM para poder desactivar completamente el intercambio.
Las siguientes estimaciones de RAM son una guía aproximada y suponen que ejecutará Suricata (incluida la captura de paquetes completos) y
Zeek y desea minimizar/eliminar la pérdida de paquetes. ¡Su kilometraje puede variar!
• Si sólo desea evaluar rápidamente Security Onion en una máquina virtual, la cantidad mínima de RAM necesaria es 12 GB. ¡Obviamente más es mejor!
• Si está implementando Security Onion en producción en una red pequeña (100 Mbps o menos), debe planificar 16 GB de RAM o más. De nuevo, más
¡Obviamente es mejor!
• Si está implementando Security Onion en producción en una red mediana (100 Mbps - 1000 Mbps), debe planificar entre 16 GB y 128 GB de RAM o
más.
• Si está implementando Security Onion en producción en una red grande (1000 Mbps - 10 Gbps), debe planificar 128 GB - 256 GB de RAM o más.
• Si está comprando un servidor nuevo, considere maximizar la RAM si es posible.
Almacenamiento
Los sensores que tienen habilitada la captura completa de paquetes necesitan MUCHO almacenamiento. Por ejemplo, suponga que está monitoreando un enlace que tiene un promedio de 50 Mbps,
Aquí hay algunos cálculos rápidos: 50 Mb/s = 6,25 MB/s = 375 MB/minuto = 22.500 MB/hora = 540.000 MB/día. Entonces vas a necesitar aproximadamente
540 GB para un día de pcaps (multiplique esto por la cantidad de días de PCAP que desea conservar). Cuanto más espacio en disco tenga, más
Tendrás retención de PCAP para realizar investigaciones posteriores al hecho.
Paquetes
Necesitará alguna forma de introducir paquetes en las interfaces de su sensor. Si solo estás evaluando Security Onion, puedes reproducir pcaps. por un
Para la implementación de producción, necesitará un puerto SPAN en un conmutador existente o un TAP dedicado. Recomendamos utilizar un TAP dedicado donde
posible. Si recopila tráfico cerca de un límite NAT, asegúrese de hacerlo desde dentro del límite NAT para poder ver la verdadera IP interna.
direcciones.
Opciones TAP/SPAN económicas (enumeradas alfabéticamente):
• Doble comunicación
• SharkTap de bit medio
• Netgear GS105Ev2
- 58/402 - Soluciones de cebolla de seguridad, LLC

5.5.18 Consideraciones sobre el hardware del sensor
Opciones de TAP empresarial (enumeradas alfabéticamente):
•APCON
• Arista
• cpaquete
• Guirnalda
• Gigamon
• KeySight/Ixia/Net Óptica
• Beneficio
Lectura adicional
Nota
Para redes y/o implementaciones grandes, consulte también https://github.com/pevma/SEPTun.
- 59/402 - Soluciones de cebolla de seguridad, LLC

5.6 Descargar
5.6 Descargar
Antes de descargar, le recomendamos encarecidamente que revise la sección Notas de la versión para estar al tanto de todos los cambios recientes.
Advertencia
¡SIEMPRE verifique la suma de verificación de la imagen ISO antes de iniciar! Esto garantiza que la imagen ISO no haya sido alterada ni dañada durante
descargar. Si no se puede verificar, intente descargar nuevamente. Si aún no se puede verificar, intente descargar desde otra computadora u otra red.
Descargue y verifique nuestra imagen ISO como se muestra en https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/
DOWNLOAD_AND_VERIFY_ISO.md.
Advertencia
El software antivirus puede alertar sobre la imagen ISO, pero lo más probable es que cualquier alerta sea falso positivo. Si observa los detalles del análisis antivirus, lo más probable es que
Probablemente le diga que alertó sobre un archivo en SecurityOnion\agrules\. Estas son reglas que buscan actividad maliciosa pero las reglas en sí no lo son.
realmente malicioso.
Nota
Si va a crear un USB de arranque a partir de la imagen ISO, hay muchas formas de hacerlo. Una opción popular que parece funcionar bien para
Mucha gente es Balena Etcher, que se puede descargar en https://www.balena.io/etcher/.
- 60/402 - Soluciones de cebolla de seguridad, LLC

5.7 VMware
5.7 VMware
5.7.1 Descripción general
En esta sección, cubriremos la creación de una máquina virtual (VM) para nuestra imagen ISO en VMware Workstation Pro y VMware Fusion. Estos pasos
debería ser bastante similar para la mayoría de las instalaciones de VMware.
Nota
Si desea rastrear el tráfico en vivo, necesitará una segunda interfaz de red dedicada a rastrear. Deberá configurar esta interfaz de rastreo para
husmear desde cualquier red que desee monitorear. Con la interfaz de rastreo en modo puente, debería poder ver todo el tráfico hacia y desde
la NIC física de la máquina host. Si desea ver TODO el tráfico en su red, necesitará un método para reenviar ese tráfico al
interfaz a la que se conecta el adaptador virtual. Esto se puede lograr con un puerto TAP o SPAN. Si desea detectar el tráfico de otras máquinas virtuales, entonces
la interfaz de rastreo virtual debe configurarse en la misma red virtual en la que están configuradas esas máquinas virtuales (esto puede ser NAT o puenteado dependiendo de
cómo están configurados).
5.7.2 Estación de trabajo profesional
VMware Workstation está disponible para muchos sistemas operativos host diferentes, incluidos Windows y varias distribuciones populares de Linux. Sigue el
pasos a continuación para crear una VM en VMware Workstation Pro para nuestra imagen ISO:
• Desde la ventana principal de VMware, seleccione Archivo >> Nueva máquina virtual.
• Seleccione Instalación típica >> Haga clic en Siguiente.
• Archivo de imagen del disco de instalación >> Ruta del archivo SO ISO >> Haga clic en Siguiente.
• Elija Linux, luego elija la distribución de Linux más cercana y haga clic en Siguiente.
• Especifique el nombre de la máquina virtual y haga clic en Siguiente.
• Especifique el tamaño del disco (mínimo 200 GB), guárdelo como un solo archivo y haga clic en Siguiente.
• Personalice el hardware y aumente la memoria y los procesadores según la sección Hardware.
• Adaptador de red (NAT o puenteado): si desea poder acceder a su máquina Security Onion desde otros dispositivos en la red, entonces
elija Bridged; de lo contrario, elija NAT para dejarlo detrás del host). Esta será la interfaz de gestión.
• Agregar >> Adaptador de red (NAT o puenteado). Esta será la interfaz de rastreo (monitoreo).
• Haga clic en Cerrar.
• Haga clic en Finalizar.
• Encienda la máquina virtual y luego siga los pasos de instalación para el tipo de instalación que desee en la sección Instalación.
5.7.3 Fusión
VMware Fusion está disponible para Mac OS. Para obtener más información sobre VMware Fusion, consulte https://www.vmware.com/products/
fusión.html.
- 61/402 - Soluciones de cebolla de seguridad, LLC

5.7.4 ESXi
Siga los pasos a continuación para crear una VM en VMware Fusion para nuestra imagen ISO:
• Desde la ventana principal de VMware Fusion, haga clic en Archivo y luego haga clic en Nuevo.
• Aparece Seleccione el método de instalación. Haga clic en Instalar desde disco o imagen y haga clic en Continuar.
• Aparece Crear una nueva máquina virtual. Haga clic en Usar otro disco o imagen de disco..., seleccione nuestra imagen ISO, haga clic en Abrir, luego haga clic en
Continuar.
• Aparece Elegir sistema operativo. Haga clic en Linux, elija la distribución de Linux más cercana y luego haga clic en Continuar.
• Aparece Elegir tipo de firmware. Haga clic en BIOS heredado y luego haga clic en Continuar.
• Aparece la pantalla de finalización. Haga clic en el botón Personalizar configuración.
• Aparece la pantalla Guardar como. Asigne un nombre a la máquina virtual y haga clic en el botón Guardar.
• Aparece la ventana de configuración. Haga clic en Procesadores y memoria.
• Aparece la pantalla Procesadores y memoria. Aumente los procesadores y la memoria según la sección Hardware. Haga clic en Agregar dispositivo...
botón.
• Aparece la pantalla Agregar dispositivo. Haga clic en Adaptador de red y haga clic en el botón Agregar....
• Aparece la pantalla Adaptador de red 2. Esta será la interfaz de rastreo (monitoreo). Seleccione la configuración del adaptador de red que desee. Haga clic
el botón Mostrar todo.
• Aparece la pantalla de configuración. Haga clic en Disco duro (SCSI).
• Aparece la pantalla Disco duro (SCSI). Aumente el tamaño del disco a al menos 200 GB según su caso de uso. Haga clic en el botón Aplicar.
• Cierre la ventana Configuración.
• En la ventana de su nueva máquina virtual, haga clic en el botón Reproducir para encender la máquina virtual.
• Siga los pasos de instalación para el tipo de instalación que desee en la sección Instalación.
5.7.4 ESXi
Si está utilizando VMware ESXi, probablemente esté familiarizado con la creación e instalación de VM, por lo que no lo detallaremos aquí. Hay algunos
cosas específicas de ESXi que quizás quieras tener en cuenta:
• Es posible que necesite configurar su interfaz de monitoreo en el vSwitch en VLAN ID 4095 para permitir el paso de todo el tráfico. Puedes leer más sobre esto en
https://github.com/Security-Onion-Solutions/securityonion/discussions/7185.
• Si está intentando monitorear múltiples interfaces de red, es posible que necesite habilitar la opción Permitir cambios de MAC en el vSwitch
y niveles de grupo de puertos. Puede leer más sobre esto en https://github.com/Security-Onion-Solutions/securityonion/discussions/2676.
• Si después de reiniciar notas que el Agente Elastic tarda mucho más de 15 minutos en inicializarse, es posible que tengas que volver a iniciarlo.
habilite la siguiente opción en ESXi: Configuración > Opciones de VM > Herramientas de VMWare > Sincronizar hora del invitado. Puedes leer más sobre esto en
https://github.com/Security-Onion-Solutions/securityonion/discussions/13285.
5.7.5 Herramientas de VMware
Si utiliza un escritorio gráfico, es posible que desee instalar open-vm-tools-desktop para habilitar más opciones de resolución de pantalla y otras funciones.
Por ejemplo, usando nuestra imagen ISO o el estándar Oracle Linux 9:
sudo dnf instalar open-vm-tools-desktop
- 62/402 - Soluciones de cebolla de seguridad, LLC

5.8 VirtualBox
5.8 VirtualBox
En esta sección, cubriremos la instalación de Security Onion en VirtualBox. Puede descargar una copia de VirtualBox para Windows, Mac OS X o Linux en
https://www.virtualbox.org.
5.8.1 Creación de máquina virtual
• Inicie VirtualBox y haga clic en el botón Nuevo.
• Proporcione un nombre para la máquina virtual (Security Onion, por ejemplo) y luego seleccione la imagen ISO. Debería establecer automáticamente el tipo en
Linux y versión a Oracle Linux 9.x. Haga clic en la casilla de verificación para Omitir instalación desatendida y luego haga clic en el botón Siguiente.
• Especifique la RAM y los procesadores según sea necesario en la sección Hardware y luego haga clic en el botón Siguiente.
• Especifique el tamaño del disco duro virtual según sea necesario en la sección Hardware y luego haga clic en el botón Siguiente.
• Confirme las opciones y luego haga clic en el botón Finalizar.
• Virtualbox debería haber habilitado automáticamente un adaptador de red conectado a la red NAT. Dependiendo del tipo de instalación que usted
está haciendo, es posible que desee conservarlo como NAT o cambiarlo a otra cosa. Si desea una interfaz de red adicional para rastrear desde un
Puerto TAP o SPAN, luego haga clic en el botón Configuración, haga clic en Red y luego vaya al Adaptador 2. Habilite el adaptador, configure la red.
debe adjuntar, y luego lo más probable es que desee ir a Avanzado y configurar el Modo promiscuo en Permitir máquinas virtuales o Permitir todo.
Haga clic en el botón Aceptar.
• Haga clic en el botón Inicio para iniciar la VM.
• Siga los pasos de instalación para el tipo de instalación que desee en la sección Instalación.
5.8.2 Adiciones de invitados
Si desea instalar VirtualBox Guest Additions, consulte https://www.virtualbox.org/manual/ch04.html.
- 63/402 - Soluciones de cebolla de seguridad, LLC

5.9 Proxmox
5.9 Proxmox
Proxmox Virtual Environment es una plataforma de virtualización similar a VMware o VirtualBox. Puede leer más sobre Proxmox VE en https://
www.proxmox.com/en/proxmox-ve. Si desea ejecutar Security Onion en una máquina virtual Proxmox, aquí hay algunas cosas adicionales que necesita
estar consciente de.
5.9.1 CPU
Proxmox utiliza de forma predeterminada una CPU de VM que puede no incluir todas las funciones de su CPU host. Es posible que tengas que cambiar esto a host para aprobar
a través del tipo de CPU del host.
5.9.2 Pantalla
Si planea usar NetworkMiner u otras aplicaciones basadas en Mono en una máquina virtual Proxmox, es posible que deba configurar la pantalla de la máquina virtual en VMware.
compatible (vmware).
5.9.3 Tarjeta de red
Si va a instalar Security Onion en Proxmox y detectar el tráfico de red en vivo, es posible que deba realizar alguna configuración adicional en
El propio Proxmox. Puede pasar una NIC física a la VM o puede usar una NIC virtual.
NIC física de paso
La primera opción es detectar el tráfico desde una NIC física que se ha pasado a la VM. Para más información sobre Proxmox
paso a paso, consulte:
https://www.servethehome.com/how-to-pass-through-pcie-nics-with-proxmox-ve-on-intel-and-amd/
https://pve.proxmox.com/wiki/PCI_Passthrough
https://pve.proxmox.com/wiki/PCI(e)_Passthrough
Una vez que la NIC física se pasa a la máquina virtual Security Onion, Security Onion debería poder configurar correctamente la NIC para
olfateando.
Tarjeta de red virtual
La segunda opción es detectar el tráfico desde una NIC virtual de Proxmox. Para obtener más detalles, consulte la discusión en https://github.com/Security-
Onion-Solutions/securityonion/discussions/8245.
Tenga en cuenta que es posible que deba desactivar manualmente las funciones de descarga de NIC en cualquier NIC de Proxmox utilizada para rastrear (la interfaz física y cualquier
interfaz de puente relacionada). Una forma de hacer esto es agregar un comando de publicación a cada interfaz de rastreo en /etc/network/interfaces en el
Anfitrión de Proxmox.
Por ejemplo, si tiene una interfaz física de Proxmox llamada enp2s0 con una interfaz puente llamada vmbr1, entonces puede iniciar sesión en Proxmox.
y edite /etc/network/interfaces agregando lo siguiente a la sección enp2s0:
post-up para i en rx tx sg tso ufo gso gro lro; hacer ethtool -K enp2s0 $i apagado; hecho
y lo siguiente a la sección vmbr1:
post-up para i en rx tx sg tso ufo gso gro lro; hacer ethtool -K vmbr1 $i apagado; hecho
Para obtener más información sobre la descarga de NIC, consulte https://blog.securityonion.net/2011/10/when-is-full-packet-capture-not-full.html.
- 64/402 - Soluciones de cebolla de seguridad, LLC

5.9.3 Tarjeta de red
Si está ejecutando Proxmox 9 o superior, es posible que también necesite configurar mtu 9000 para la interfaz de rastreo físico de Proxmox y su
interfaz de puente correspondiente.
Una vez que su Security Onion VM esté recibiendo el tráfico esperado, si Grid informa Capture Loss pero no Zeek Loss y está seguro de que la pérdida
no ocurre en su puerto tap o span, entonces puede estar relacionado con la interfaz física del host Proxmox. Ciertas NIC como la Intel X710 pueden
Tiene canales preestablecidos y puede verificar con el comando ethtool -l. Para obtener más información, consulte la página de manual de ethtool en
https://man7.org/linux/man-pages/man8/ethtool.8.html.
Si este es el caso de la interfaz física de su host, entonces puede agregar un comando de publicación adicional para ejecutar ethtool -L con el 1 combinado
opción. Por ejemplo, si tiene una interfaz física llamada enp3s0f1np1, entonces la sección correspondiente de /etc/network/interfaces
lucir así:
post-up ethtool -L enp3s0f1np1 combinado 1; para i en rx tx sg tso ufo gso gro lro; hacer ethtool -K enp3s0f1np1 $i desactivado; hecho
- 65/402 - Soluciones de cebolla de seguridad, LLC

5.10 Problemas de arranque
5.10 Problemas de arranque
Si tiene problemas para iniciar la imagen ISO, aquí hay algunos pasos para solucionarlo:
• Si está intentando crear un USB de arranque a partir de una imagen ISO, intente usar Balena Etcher, que se puede descargar en https://www.balena.io/
grabador/.
• Ciertos adaptadores de pantalla pueden requerir que la opción nomodeset se pase al kernel (consulte https://unix.stackexchange.com/questions/353896/
La instalación de Linux pasa a la pantalla en blanco).
• Si aún tiene problemas con nuestra imagen ISO de 64 bits, intente descargar la imagen ISO x86-64 estándar para Oracle Linux 9. Si no se ejecuta,
entonces deberías volver a verificar tu compatibilidad con 64 bits.
consejo
Si todo lo demás falla pero el estándar x86-64 Oracle Linux 9 se instala normalmente, entonces puede instalar nuestros componentes encima como se describe en Red.
Sección de instalación. Sin embargo, tenga en cuenta que las instalaciones de red no son compatibles.
- 66/402 - Soluciones de cebolla de seguridad, LLC

5.11 Entrehierro
5.11 Entrehierro
Security Onion se compromete a permitir a los usuarios ejecutar una instalación completa en redes que no tienen acceso a Internet. Nuestra imagen ISO incluye
todo lo que necesitas para ejecutar sin acceso a Internet. Asegúrese de elegir la opción de espacio de aire durante la configuración.
Si su red tiene acceso a Internet pero tiene servidores proxy, firewalls u otros dispositivos de red demasiado restrictivos que podrían impedir que Security Onion
de conectarse a los sitios que se muestran en la sección Firewall, entonces es posible que desee considerar la opción airgap ya que todo se instalará desde el
Imagen ISO en sí.
El modo Airgap funciona de la siguiente manera:
• Durante la instalación, todos los paquetes RPM necesarios se copian de la imagen ISO a un nuevo repositorio ubicado en /nsm/repo/. Todos los dispositivos en
el grid ahora usará este repositorio para actualizaciones de paquetes.
• Las reglas NIDS para Suricata se copian en /nsm/rules/suricata.
• Las reglas de YARA para Strelka se copian en /nsm/rules/yara.
• Las reglas de Sigma para ElastAlert se copian en /nsm/repo/rules/sigma.
• Al actualizar el sistema, la sopa solicitará la ubicación del medio ISO más reciente y luego actualizará usando ese medio en lugar de extraerlo.
desde Internet.
5.11.1 Actualizaciones de reglas
Nuestra imagen ISO incluye la última versión de varios conjuntos de reglas y los instalará automáticamente cuando un sistema de espacio de aire se SOUP a través de ISO:
• NIDS: Amenazas Emergentes (ETOPEN). Si desea cambiar a un conjunto de reglas diferente como Emerging Threats Pro (ETPRO), consulte nuestro Conjunto de reglas
documentación de configuración NIDS
• YARA: reglas más recientes de nuestro repositorio
• Sigma: paquetes de reglas más recientes del repositorio de SigmaHQ
- 67/402 - Soluciones de cebolla de seguridad, LLC

5.12 Instalación
5.12 Instalación
Advertencia
Asegúrese de que su nombre de host sea correcto durante la instalación. El programa de instalación genera certificados basados en el nombre de host y no admitimos
cambiar el nombre de host después de la instalación.
Nota
Si desea realizar la implementación en la nube utilizando una de nuestras imágenes de nube oficiales, puede pasar a Amazon Cloud, Azure Cloud o Google Cloud.
secciones.
Después de descargar nuestra imagen ISO como se muestra en la sección Descargar, ¡es el momento de instalarla!
- 68/402 - Soluciones de cebolla de seguridad, LLC

5.12 Instalación
• Revise las secciones Hardware y Notas de la versión.
• Descargue y verifique nuestra imagen ISO como se muestra en la sección Descargar.
• Inicie el ISO en una máquina que cumpla con las especificaciones mínimas de hardware.
• Siga las indicaciones para completar la instalación y reiniciar.
• Es posible que necesite expulsar la imagen ISO o cambiar el orden de inicio de la máquina para iniciar desde el sistema operativo recién instalado.
• Inicie sesión con el nombre de usuario y la contraseña que estableció en el instalador.
• La configuración de Security Onion se iniciará automáticamente. Si por alguna razón tiene que salir de la Configuración y necesita reiniciarla, puede cerrar sesión en su
cuenta y luego vuelva a iniciar sesión y debería iniciarse automáticamente. Si eso no funciona, puede ejecutarlo manualmente de la siguiente manera:
sudo SecurityOnion/setup/so-setup iso
• Proceda a la sección Configuración.
- 69/402 - Soluciones de cebolla de seguridad, LLC

5.13 Imagen de la nube de Amazon
5.13 Imagen de la nube de Amazon
Si desea implementar Security Onion en Amazon Web Services (AWS), tenemos una imagen de máquina de Amazon (AMI) que ya está creada para
usted: https://securityonion.net/aws/?ref=_ptnr_soc_docs_260311
Advertencia
Las instalaciones existentes de imágenes en la nube de Security Onion deben usar el comando sopa para actualizar. Si su grid todavía ejecuta 2.4.x, use sopa para
actualice a 2.4.210 y luego use sopato3 para continuar con Security Onion 3, luego de lo cual continúe usando sopa nuevamente. Intentar cambiar a un
la nueva imagen de Security Onion del mercado de la nube podría provocar la pérdida de datos y requerir la reinstalación completa de Grid; Utilice el procedimiento de sopa para
actualizar en su lugar.
Nota
Esta sección no cubre la conectividad de red al nodo Security Onion. Esto se puede lograr mediante la configuración de una IP externa para el
interfaz de gestión del nodo, o mediante el uso de una conexión VPN a través de OpenVPN. Para obtener más detalles sobre las conexiones VPN, consulte https://
medium.com/@svfusion/setup-site-to-site-vpn-to-aws-with-pfsense-1cac16623bd6.
Nota
Esta sección no cubre cómo configurar una VPC en AWS. Para obtener más detalles sobre la configuración de una VPC, consulte https://docs.aws.amazon.com/
directorioservicio/latest/admin-guide/gsg_create_vpc.html. Asegúrese de que todos los nodos de Security Onion puedan acceder al nodo administrador a través de la ruta necesaria.
puertos. Esto podría requerir agregar reglas a sus grupos de seguridad de AWS para cumplir con la comunicación del nodo Security Onion Firewall.
requisitos.
5.13.1 Requisitos
Antes de continuar, determine la arquitectura de red deseada. Elija entre un Grid de un solo nodo o un Grid distribuido de varios nodos. Además,
determinar si se necesita la latencia más baja del almacenamiento de instancias efímeras (normalmente cuando se monitorea un gran volumen de tráfico, lo que
(es la mayoría de los escenarios de producción), o si se puede utilizar el almacenamiento basado en red, EBS, para aumentar la redundancia.
5.13.2 Cuadrícula de un solo nodo
Para un monitoreo de producción simple y de bajo volumen, se puede utilizar un Grid de un solo nodo. EBS debe usarse para el almacenamiento de datos de Elasticsearch si se usa para
fines de producción. Las grillas de un solo nodo no pueden utilizar almacenamiento de instancias efímeras sin correr el riesgo de perder datos. Sin embargo, de forma temporal
En instalaciones de evaluación, donde hay poca preocupación por la pérdida de datos, se puede utilizar el almacenamiento de instancias efímeras.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para instancias de un solo nodo, ya sea para evaluación o de forma independiente.
instalaciones (elija una, no ambas). Tenga en cuenta que cuando utilice máquinas virtuales con los requisitos mínimos de RAM, es posible que necesite habilitar
intercambio de memoria.
Independiente:
• Cantidad: 1
• Tipo: t3a.2xlarge
• Almacenamiento: 256 GB EBS (optimizado) gp3
- 70/402 - Soluciones de cebolla de seguridad, LLC

5.13.3 Red Distribuida
Evaluación
• Cantidad: 1
• Tipo: t3a.2xlarge
• Almacenamiento: 256 GB EBS (optimizado) gp3
• Almacenamiento: Almacenamiento de instancia de 100 GB (SSD/NVMe)
5.13.3 Red Distribuida
Para monitoreo de producción de gran volumen, elija una arquitectura Grid de múltiples nodos. En esta arquitectura se deben utilizar al menos dos nodos de búsqueda.
Esto es necesario debido al uso de almacenamiento de instancias efímeras para el almacenamiento de datos de Elasticsearch, donde cada uno de los nodos de búsqueda retiene una réplica.
de otro nodo de búsqueda, para recuperación ante desastres.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para las instancias distribuidas de Grid. Prefiere aumentar la memoria de la máquina virtual
en lugar de habilitar la memoria de intercambio, para obtener el mejor rendimiento. Las redes de gran volumen necesitarán tipos de máquinas virtuales más potentes y con más almacenamiento que aquellas.
enumerados a continuación.
Nodo VPN
• Cantidad: 1
• Tipo: t3a.micro (elegible para Nitro)
• Almacenamiento: 50 GB EBS (optimizado) gp3
Gerente
• Cantidad: 1
• Tipo: m5a.2xgrande
• Almacenamiento: 300 GB EBS (optimizado) gp3
Buscar nodos
• Cantidad: 2 o más
• Tipo: m5ad.2xlarge
• Almacenamiento: 200 GB EBS (optimizado) gp3
• Almacenamiento: Almacenamiento de instancias de 150 GB (SSD/NVMe)
Sensor que monitorea el ingreso de VPN
• Cantidad: 1
• Tipo: c5a.2xlarge
• Almacenamiento: 500 GB EBS (optimizado) gp3
5.13.4 Crear interfaz de monitoreo
Para configurar la configuración del espejo de VPC y AMI de Security Onion, siga los pasos a continuación.
- 71/402 - Soluciones de cebolla de seguridad, LLC

5.13.5 Crear un grupo de seguridad para la interfaz de rastreo
5.13.5 Crear un grupo de seguridad para la interfaz de rastreo
Los grupos de seguridad actúan como un firewall para sus instancias Amazon EC2 y controlan el tráfico entrante y saliente. Necesitará crear un
grupo de seguridad específicamente para la interfaz que utilizará para detectar el tráfico. Este grupo de seguridad deberá ser lo más abierto posible a
asegúrese de que se permita el paso de todo el tráfico destinado a la interfaz de rastreo. Para crear un grupo de seguridad, siga estos pasos:
• Desde el Panel de EC2, seleccione: Grupos de seguridad en las secciones Red y seguridad en el panel izquierdo de la ventana.
• Seleccione: Crear grupo de seguridad
• Proporcione un nombre y una descripción del grupo de seguridad.
• Seleccione la VPC adecuada para el grupo de seguridad.
• Con la pestaña de entrada seleccionada, seleccione: Agregar regla
• Agregue las reglas de entrada adecuadas para garantizar que se permita todo el tráfico deseado destinado a la interfaz de rastreo.
• Presione el botón Crear grupo de seguridad.
5.13.6 Crear interfaz de rastreo
Antes de iniciar la AMI de Security Onion, deberá crear la interfaz que se utilizará para monitorear su VPC. Esta interfaz será
conectado a la AMI de Security Onion como interfaz secundaria. Para crear una interfaz de rastreo, siga estos pasos:
• Desde el Panel de EC2, seleccione: Interfaces de red en la sección Red y seguridad en el panel izquierdo de la ventana.
• Seleccione: Crear interfaz de red
• Proporcione una descripción y elija la subred adecuada que desea monitorear.
• Seleccione el grupo de seguridad que creó para la interfaz de rastreo.
• Seleccionar: Crear
5.13.7 Crear instancias de seguridad Onion
5.13.8 Creación de instancia
Para configurar una instancia de Security Onion (repita para cada nodo en un Grid distribuido), siga estos pasos:
• Desde el panel de EC2, seleccione: Iniciar instancia
• Busque Security Onion en AWS Marketplace y asegúrese de obtener la última versión de la AMI oficial de Security Onion.
• Elija el tipo de instancia adecuado según los requisitos de hardware deseados y seleccione Siguiente: Configurar detalles de la instancia. Para
Para obtener ayuda para determinar los requisitos de recursos, revise la sección Requisitos de AWS anterior.
• Desde el menú de subred, seleccione la misma subred que la interfaz de rastreo.
• En la sección Interfaces de red, configure la interfaz eth0 (administración).
• (Solo nodo "Sensor" distribuido o cuadrícula de nodo único) En la sección Interfaces de red, seleccione: Agregar dispositivo para adjuntar el dispositivo previamente
creó una interfaz de rastreo para la instancia.
• (Solo nodo "Sensor" distribuido o cuadrícula de nodo único) En el menú Interfaz de red para eth1, elija la interfaz de rastreo que creó
para esta instancia. Tenga en cuenta que si tiene varias interfaces en la lista, puede verificar la interfaz correcta navegando a Red
Sección de interfaces en el Panel de control de EC2.
• Seleccione: Siguiente: Agregar almacenamiento y configure los ajustes del volumen.
• Seleccione: Siguiente: Agregar etiquetas y agregue etiquetas adicionales para la instancia.
• Seleccione: Siguiente: Configurar grupo de seguridad y agregue las reglas de entrada apropiadas.
• Seleccione: Revisar y ejecutar
• Si se le solicita, seleccione el par de claves SSH adecuado que se utilizará para acceder mediante ssh a la instancia de Security Onion para su administración.
• El nombre de usuario predeterminado para la AMI de Security Onion es: cebolla
- 72/402 - Soluciones de cebolla de seguridad, LLC

5.13.9 Preparar nodos con almacenamiento efímero
5.13.9 Preparar nodos con almacenamiento efímero
Para nodos de búsqueda distribuidos, o un nodo de evaluación si usa almacenamiento efímero, ingrese SSH al nodo y cancele la configuración. preparar el
partición efímera ejecutando el siguiente comando:
sudo so-prepare-fs
De forma predeterminada, este comando espera que el dispositivo efímero esté ubicado en /dev/nvme1n1 y montará ese dispositivo en /nsm/elasticsearch.
Si esto falla, ejecute lsblk para determinar qué disco usar. Para anular cualquiera de esos dos valores predeterminados, especifíquelos como argumentos. Por ejemplo:
sudo so-prepare-fs /dev/nvme3n0 /nsm/elasticsearch
Reinicie la configuración de Security Onion ejecutando el siguiente comando:
cd / cebolla de seguridad
sudo ./so-setup-network
5.13.10 Configuración del administrador
Si se trata de un nodo de evaluación efímero, asegúrese de que el nodo se haya preparado como se describe en la sección anterior.
Después de ingresar mediante SSH al nodo, la configuración comenzará automáticamente. Siga las indicaciones y seleccione las opciones de instalación adecuadas. Más distribuido
las instalaciones utilizarán el nombre de host u otro método de acceso web, debido a la necesidad de que ambos nodos del clúster estén dentro de la red privada, y
usuarios analistas a través de la Internet pública para comunicarse con el gerente. Esto permite que las entradas DNS personalizadas definan la IP correcta (privada o pública)
dependiendo de si se trata de un nodo del clúster o de un usuario analista. Los usuarios que evalúan Security Onion por primera vez deberían considerar elegir el
otra opción y especificando la IP de la nube pública del nodo.
AWS proporciona un servidor NTP integrado en IP 169.254.169.123. Esto se puede especificar en la pantalla de configuración de SOC una vez completada la configuración. Por
De forma predeterminada, el servidor utilizará los servidores de hora en ntp.org.
Para nodos de administrador distribuido que utilizan almacenamiento efímero, vaya a Configuración de SOC. Busque number_of_replicas y cambie a 1. Esto
duplicará el costo de almacenamiento, pero garantizará que al menos dos máquinas virtuales tengan los datos, en caso de una pérdida efímera del disco.
Opcionalmente, ajuste los índices de ElastAlert para que tengan una réplica. Esto hará que se vuelvan amarillos, pero eso se solucionará cuando se busquen nodos.
entra en línea:
so-elasticsearch-query ElastAlert*/_settings -X PUT -d '{"índice": { "número_de_réplicas": 1 }}'
Este es un paso opcional debido a que los índices de ElastAlert se utilizan principalmente para el historial de alertas recientes o de corto plazo. En caso de pérdida de datos cuando
ElastAlert 2 se reinicia y los índices se regenerarán.
5.13.11 Configuración del nodo de búsqueda
Siga la instalación estándar del nodo de búsqueda de Security Onion y responda las indicaciones de configuración según corresponda. Si está utilizando almacenamiento efímero, tenga en cuenta
asegúrese de preparar primero la instancia como se indicó anteriormente en esta sección.
5.13.12 Configuración del sensor AWS
SSH en el nodo del sensor y ejecute la configuración para configurar este nodo como sensor. Elija eth0 como interfaz principal y eth1 como interfaz
interfaz de monitoreo.
5.13.13 Configuración del sensor remoto
Configure la VPN (fuera del alcance de esta guía) y conecte el nodo del sensor a la VPN. Durante la configuración de Security Onion del sensor, cuando
Cuando se le solicite elegir la interfaz de administración, seleccione la interfaz del túnel VPN, generalmente tun0.
- 73/402 - Soluciones de cebolla de seguridad, LLC

5.13.14 Duplicación de tráfico de AWS
Si conecta sensores a través de la instancia VPN, deberá agregar la interfaz interna de su concentrador VPN al firewall del sensor.
grupo anfitrión. Por ejemplo, suponiendo la siguiente arquitectura:
Sensor SO -> Punto final VPN -> Internet -> Punto final VPN -> Administrador SO
Ubicación: Ubicación remota: Ubicación remota: Ubicación de AWS: AWS
192.168.33.13 192.168.33.10 10.55.1.10 10.55.1.20
Para agregar el nodo de sensor de red remota a la red, deberá agregar 10.55.1.10 al grupo de hosts del firewall del sensor.
Este cambio se puede realizar en la pantalla de Configuración de SOC. Luego, espere hasta 15 minutos para que se ejecute la sincronización de configuración programada, o
fuerce una sincronización inmediatamente a través de las Opciones de configuración de SOC. Una vez sincronizada la configuración del grupo de hosts del firewall
su Administrador estará listo para que los minions remotos comiencen a conectarse.
5.13.14 Duplicación de tráfico de AWS
La duplicación de tráfico le permite copiar el tráfico hacia/desde una instancia y enviarlo a la interfaz de rastreo de un monitoreo de seguridad de red.
sensor o un grupo de interfaces que utilizan un equilibrador de carga de red. Para obtener más detalles sobre AWS Traffic Mirroring, consulte: https://
docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html
consejo
Solo puede reflejar el tráfico de una instancia EC2 que funcione con el sistema AWS Nitro. Para obtener una lista de sistemas Nitro compatibles, consulte
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances.
5.13.15 Crear objetivo espejo
Un destino reflejado en AWS se refiere al destino del tráfico reflejado. Puede ser una única interfaz o un grupo de interfaces que utilizan una red.
equilibrador de carga. Para configurar un destino espejo, siga estos pasos:
• Desde el panel de control de VPC, seleccione: Reflejar objetivos en la sección Reflejo de tráfico en el panel izquierdo de la ventana.
• Seleccione: Crear objetivo espejo de tráfico
• En la sección Elegir objetivo, seleccione el tipo de objetivo apropiado y elija la interfaz de rastreo conectada a Security Onion.
instancia. Para obtener más detalles sobre los objetivos de espejo de tráfico, consulte: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-
objetivos.html
• Seleccionar: Crear
5.13.16 Crear filtro espejo
Un filtro espejo le permite definir el tráfico que se copia en la sesión reflejada y es útil para desconectar el tráfico ruidoso o no deseado. a
configurar un filtro espejo, siga estos pasos:
• Desde el panel de control de VPC, seleccione: Filtros de duplicación en la sección Duplicación de tráfico en el panel izquierdo de la ventana.
• Seleccione: Crear filtro espejo de tráfico
• Agregue las reglas de entrada y salida apropiadas. Para obtener más detalles sobre los filtros de espejo de tráfico, consulte: https://docs.aws.amazon.com/
vpc/latest/mirroring/traffic-mirroring-filters.html
• Seleccionar: Crear
- 74/402 - Soluciones de cebolla de seguridad, LLC

5.13.17 Crear sesión espejo
5.13.17 Crear sesión espejo
Una sesión de espejo de tráfico define el origen del tráfico que se va a reflejar en función de los filtros de espejo de tráfico seleccionados y envía ese tráfico al
objetivo de espejo de tráfico deseado. Para obtener más detalles sobre las sesiones de espejo de tráfico, consulte: https://docs.aws.amazon.com/vpc/latest/mirroring/
sesión-de-espejo-de-tráfico.html
• Desde el panel de VPC, seleccione: Duplicar sesiones en la sección Duplicación de tráfico en el panel izquierdo de la ventana.
• Seleccione: Crear sesión espejo de tráfico
• En la sección Reflejar fuente, elija la interfaz que desea reflejar.
• En la sección Destino reflejado, elija la interfaz o el equilibrador de carga al que desea enviar el tráfico reflejado.
• Asigne un número de sesión en la sección Configuración adicional para la sesión espejo.
• En la sección de filtros en Configuración adicional, elija el filtro espejo que desea aplicar al tráfico reflejado.
• Seleccionar: Crear
5.13.18 Verificar duplicación de tráfico
Para verificar que la sesión reflejada esté enviando los datos correctos a la interfaz de rastreo, ejecute el siguiente comando en el sensor Security Onion AWS
instancia:
sudo tcpdump -nni <interfaz>
Debería ver el tráfico etiquetado VXLAN reflejado desde la interfaz que seleccionó como origen espejo.
Para verificar que Zeek esté decapsulando y analizando correctamente el tráfico VXLAN, puede verificar que los registros se estén generando en /nsm/zeek/logs/
directorio actual:
ls -la /nsm/zeek/logs/current/
- 75/402 - Soluciones de cebolla de seguridad, LLC

5.14 Imagen de nube de Azure
5.14 Imagen de nube de Azure
Los usuarios de Azure pueden implementar una imagen de máquina virtual oficial de Security Onion que se encuentra en Azure Marketplace: https://securityonion.net/azure
Advertencia
Las instalaciones existentes de imágenes en la nube de Security Onion deben usar el comando sopa para actualizar. Si su grid todavía ejecuta 2.4.x, use sopa para
actualice a 2.4.210 y luego use sopato3 para continuar con Security Onion 3, luego de lo cual continúe usando sopa nuevamente. Intentar cambiar a un
la nueva imagen de Security Onion del mercado de la nube podría provocar la pérdida de datos y requerir la reinstalación completa de Grid; Utilice el procedimiento de sopa para
actualizar en su lugar.
Nota
En septiembre de 2025, Azure lanzó una vista previa de su función Virtual TAP. Vea más información aquí: https://docs.microsoft.com/en-us/
azure/virtual-network/virtual-network-tap-overview
Nota
Esta sección no cubre la conectividad de red al nodo Security Onion. Esto se puede lograr mediante la configuración de una IP externa para el
interfaz de administración del nodo, o mediante el uso de una conexión VPN a través de OpenVPN.
Nota
Esta sección no cubre cómo configurar una red virtual en Azure. Para obtener más detalles sobre cómo configurar una red virtual, consulte https://
docs.microsoft.com/en-us/azure/virtual-network/. Asegúrese de que todos los nodos de Security Onion puedan acceder al nodo administrador a través de los puertos necesarios.
Esto podría requerir agregar reglas a su red virtual de Azure y/o máquinas virtuales para satisfacer la comunicación del nodo de Security Onion Firewall.
requisitos.
5.14.1 Requisitos
Antes de continuar, determine la arquitectura de red deseada. Elija entre un Grid de un solo nodo o un Grid distribuido de varios nodos.
Security Onion recomienda utilizar discos SSD Premium o discos Ultra SSD más caros, con IOPS y rendimiento adecuados.
adaptado a sus requisitos esperados de monitoreo de red.
5.14.2 Cuadrícula de nodo único
Para un monitoreo de producción simple y de bajo volumen, se puede utilizar un Grid de un solo nodo.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para instancias de un solo nodo, ya sea para evaluación o de forma independiente.
instalaciones (elija una, no ambas). Tenga en cuenta que cuando utilice máquinas virtuales con los requisitos mínimos de RAM, es posible que necesite habilitar
intercambio de memoria.
Independiente
• Cantidad: 1
• Tipo: Estándar_D8as_v4
• Almacenamiento: SSD premium de 256 GB
- 76/402 - Soluciones de cebolla de seguridad, LLC

5.14.3 Red Distribuida
Evaluación
• Cantidad: 1
• Tipo: Estándar_D8as_v4
• Almacenamiento: SSD premium de 256 GB
5.14.3 Red Distribuida
Para monitoreo de producción de gran volumen, elija una arquitectura Grid de múltiples nodos. Se recomiendan al menos dos nodos de búsqueda para lograr redundancia
propósitos.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para las instancias distribuidas de Grid. Prefiere aumentar la memoria de la máquina virtual
en lugar de habilitar la memoria de intercambio, para obtener el mejor rendimiento. Las redes de gran volumen necesitarán tipos de máquinas virtuales más potentes y con más almacenamiento que aquellas.
enumerados a continuación.
Nodo VPN
• Cantidad: 1
• Tipo: Opción 1: Standard_B1s: menor costo para uso con bajo volumen de tráfico VPN
• Tipo: Opción 2: Standard_D4as_v4 con red acelerada: mayor costo para un alto volumen de tráfico VPN
• Almacenamiento: SSD prémium de 64 GB
Gerente
• Cantidad: 1
• Tipo: Estándar_D8as_v4
• Almacenamiento: SSD premium de 256 GB
Buscar nodos
• Cantidad: 2 o más
• Tipo: Estándar_D8as_v4
• Almacenamiento: SSD premium de 256 GB
Sensor que monitorea el ingreso de VPN
• Cantidad: 1
• Tipo: Estándar_D4as_v4
• Almacenamiento: SSD prémium de 512 GB
5.14.4 Crear interfaz de monitoreo
Para configurar un nodo sensor de Security Onion en Azure, siga los pasos de requisitos previos que se indican a continuación antes de crear la máquina virtual del sensor.
5.14.5 Crear un grupo de seguridad para la interfaz de rastreo
Los grupos de seguridad actúan como un firewall para sus máquinas virtuales de Azure, controlando el tráfico entrante y saliente. Deberías considerar
si se necesita un grupo de seguridad para su red virtual y específicamente para la interfaz que utilizará para detectar el tráfico. esto
- 77/402 - Soluciones de cebolla de seguridad, LLC

5.14.6 Crear interfaz de rastreo
El grupo de seguridad deberá ser lo más abierto posible para garantizar que se permita el paso de todo el tráfico destinado a la interfaz de rastreo. para crear un
grupo de seguridad, siga estos pasos:
• En el Panel de Azure, busque: Grupos de seguridad de red.
• Seleccionar: Crear
• Proporcione un nombre, como grupo-de-seguridad-de-supervisión.
• Seleccione el grupo de recursos y la región adecuados.
• Seleccione Revisar + Crear
• Revisar el resumen
• Seleccionar: Crear
• Seleccionar: Ir al recurso
• Ajuste las reglas de seguridad entrantes para garantizar que se permita todo el tráfico de monitoreo entrante.
5.14.6 Crear interfaz de rastreo
Antes de iniciar la máquina virtual del sensor Security Onion, deberá crear la interfaz que se utilizará para monitorear su máquina virtual.
red. Esta interfaz se conectará a la máquina virtual del sensor Security Onion como interfaz secundaria. Para crear una interfaz de rastreo,
sigue estos pasos:
• En el Panel de Azure, busque: Interfaces de red.
• Seleccionar: Crear
• Proporcione un nombre, como so-monitoring-interface.
• Elija el grupo de recursos, la región, la red virtual, la subred, el grupo de seguridad de los pasos anteriores y la configuración de IP.
• Seleccione: Revisar + Crear
• Revisar el resumen
• Seleccionar: Crear
5.14.7 Configurar TAP de red virtual
Para realizar la supervisión del tráfico en Azure, se debe crear un TAP de red virtual. Esto se puede crear en cualquier grupo de recursos, pero debe existir en
la misma región que las interfaces de origen y destino. Ubique la pantalla VTAP en Azure Portal buscando vtap y una lista de
Los resultados incluirán "Puntos de acceso de terminación de red virtual". Elija eso y luego haga clic en el botón Crear. Elija la región que
coincide con sus máquinas virtuales de origen y destino. Elija el destino localizando la interfaz de rastreo creada anteriormente. Mostrará el puerto 4789
ya que el tráfico monitoreado llegará a la interfaz de rastreo como tráfico VxLAN. Finalmente, elija las interfaces de red de origen a monitorear.
Se pueden seleccionar varias interfaces si es necesario monitorear varias máquinas virtuales.
Revise la documentación de Azure VTAP ubicada en https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview para
asegurarse de que se hayan satisfecho todos los demás requisitos.
- 78/402 - Soluciones de cebolla de seguridad, LLC

5.14.8 Crear instancias cebolla de seguridad
5.14.8 Crear instancias cebolla de seguridad
5.14.9 Creación de instancia
Para configurar una instancia de Security Onion (repita para cada nodo en un Grid distribuido), siga estos pasos:
• En Azure Dashboard busque: Máquinas virtuales
• Seleccione: Crear y luego Máquina virtual
• Elija o cree un nuevo grupo de recursos.
• Introduzca un nombre adecuado para esta máquina virtual, como so-vm-manager.
• Elija las opciones de Región y Disponibilidad que desee. (Utilice East US 2 para compatibilidad con Ultra SSD, si es necesario).
• Elija la imagen de VM Security Onion. Si esta opción no aparece en el menú desplegable Imagen, seleccione Ver todas las imágenes y busque cebolla.
• Elija el tamaño apropiado según los requisitos de hardware deseados. Para obtener ayuda para determinar los requisitos de recursos, por favor
revise la sección Requisitos anterior.
• Cambie el nombre de usuario a cebolla. Tenga en cuenta que esto no es obligatorio: si accidentalmente se lo deja al usuario azure predeterminado, está bien,
simplemente use el nombre de usuario azureuser en cualquier lugar donde la documentación indique usar el nombre de usuario cebolla.
• Seleccione una clave pública SSH existente si ya existe una; de lo contrario, seleccione la opción para Generar un nuevo par de claves.
• Elija Otro para Tipo de licencia.
• Seleccione Siguiente: Discos
• Asegúrese de que esté seleccionado Premium SSD.
• Para grillas de un solo nodo, nodos de sensores distribuidos o nodos de búsqueda distribuidos: si desea separar la partición /nsm en su propia
disco, cree y adjunte un disco de datos para este fin, con un tamaño mínimo de 100 GB o más, según las necesidades de almacenamiento previstas. Nota
que el tamaño de la partición /nsm determina la velocidad a la que se eliminan los datos de eventos y paquetes antiguos. Separar la partición /nsm puede proporcionar
Más flexibilidad para ampliar los tamaños de los nodos de la cuadrícula, pero requiere un poco más de configuración, que se describe más adelante.
• Seleccione Siguiente: Redes
• Elija la red virtual para esta máquina virtual.
• Elija una IP pública si desea acceder a esta máquina virtual directamente (no recomendado para grids de producción).
• Elija la configuración adecuada del grupo de seguridad. Tenga en cuenta que normalmente este no es el mismo grupo de seguridad utilizado para el monitoreo del sensor.
interfaz.
• Las redes aceleradas se habilitarán automáticamente si el tamaño de la máquina virtual lo admite.
• Seleccione: Revisar + crear
• Revisar el resumen. Si aparece un mensaje de error de validación, corrija las entradas que faltan en cada sección de pestaña que contenga un punto rojo para
a la derecha del nombre de la pestaña.
• Seleccionar. Cree y descargue la nueva clave pública, si elige generar una nueva clave.
• Si esta VM es una Grid de un solo nodo o es un nodo sensor:
• Detenga la nueva VM una vez completada la implementación.
• Edite la VM y conecte la interfaz de red de monitoreo creada anteriormente.
• Inicie la máquina virtual.
Tenga en cuenta que deberá hacer referencia a la clave pública SSH cuando utilice SSH para acceder a las nuevas máquinas virtuales. Por ejemplo:
chmod 600 ~/Descargas/onion.pem
ssh -i ~/Descargas/onion.pem cebolla@11.22.33.44
5.14.10 Configuración del administrador
Después de ingresar mediante SSH al nodo, la configuración comenzará automáticamente. Siga las indicaciones y seleccione las opciones de instalación adecuadas. Más distribuido
las instalaciones utilizarán el nombre de host u otro método de acceso web, debido a la necesidad de que ambos nodos del clúster estén dentro de la red privada, y
- 79/402 - Soluciones de cebolla de seguridad, LLC

5.14.11 Configuración del nodo de búsqueda
usuarios analistas a través de la Internet pública para comunicarse con el gerente. Esto permite que las entradas DNS personalizadas definan la IP correcta (privada o pública)
dependiendo de si se trata de un nodo del clúster o de un usuario analista. Los usuarios que evalúan Security Onion por primera vez deberían considerar elegir el
otra opción y especificando la IP de la nube pública del nodo.
5.14.11 Configuración del nodo de búsqueda
Siga la instalación estándar del nodo de búsqueda de Security Onion y responda las indicaciones de configuración según corresponda.
5.14.12 Configuración del sensor remoto
Configure la VPN (fuera del alcance de esta guía) y conecte el nodo del sensor a la VPN. Cuando se le solicite elegir la interfaz de administración,
seleccione la interfaz del túnel VPN, como tun0. Utilice la dirección IP interna del administrador dentro de Azure cuando se le solicite la IP del administrador.
5.14.13 Configuración del sensor de Azure
SSH en el nodo del sensor y ejecute la configuración para configurar este nodo como sensor. Elija eth0 como interfaz principal y eth1 como interfaz
interfaz de monitoreo.
5.14.14 Verificar el tráfico de monitoreo
Para verificar que el sensor de Azure esté recibiendo los datos correctos en la interfaz de rastreo, ejecute el siguiente comando en Security Onion Azure
instancia del sensor:
sudo tcpdump -nni eth1
Para verificar que Zeek esté decapsulando y analizando correctamente el tráfico, puede verificar que se estén generando registros en /nsm/zeek/logs/current.
directorio:
ls -la /nsm/zeek/logs/current/
- 80/402 - Soluciones de cebolla de seguridad, LLC

5.15 Imagen de la nube de Google
5.15 Imagen de la nube de Google
Si desea implementar Security Onion en Google Cloud Platform (GCP), elija la imagen de Security Onion que aparece en Google
Mercado: https://securityonion.net/google/?ref=_ptnr_soc_docs_260311
Advertencia
Las instalaciones existentes de Security Onion AMI deben usar el comando sopa para actualizar. Si su grid todavía ejecuta 2.4.x, use sopa para actualizar a
2.4.210, y luego use sopato3 para continuar con Security Onion 3, luego continúe usando sopa nuevamente. Intentando cambiar a una seguridad más nueva
La imagen cebolla del mercado en la nube podría provocar la pérdida de datos y requerir una reinstalación completa de Grid; Utilice el procedimiento de sopa para actualizar.
en cambio.
Nota
Esta sección no cubre la conectividad de red al nodo Security Onion. Esto se puede lograr mediante la configuración de una IP externa para el
interfaz de administración del nodo, o mediante el uso de una conexión VPN a través de OpenVPN.
Nota
Esta sección no cubre todos los aspectos de cómo configurar una VPC en GCP, ya que cada implementación suele ser única para el usuario. Para más detalles
Para obtener información sobre cómo configurar una VPC, consulte https://cloud.google.com/vpc/docs/vpc. Asegúrese de que todos los nodos de Security Onion puedan acceder al nodo administrador
sobre los puertos necesarios. Esto podría requerir agregar reglas a su nube privada virtual de GCP y/o a sus máquinas virtuales para cumplir con Security Onion.
Requisitos de comunicación del nodo de firewall.
5.15.1 Requisitos
Antes de continuar, determine la arquitectura de red deseada. Elija entre un Grid de un solo nodo o un Grid distribuido de varios nodos. Además,
determinar si se necesita una latencia más baja del almacenamiento de instancia local (generalmente cuando se monitorea un gran volumen de tráfico, lo cual es
en la mayoría de los escenarios de producción) o si se pueden utilizar discos persistentes para aumentar la redundancia.
5.15.2 Cuadrícula de un solo nodo
Para un monitoreo de producción simple y de bajo volumen, se puede utilizar un Grid de un solo nodo. Se deben utilizar discos persistentes para el almacenamiento de datos de Elasticsearch
si se utiliza con fines de producción. Las grillas de un solo nodo no pueden usar discos locales sin correr el riesgo de perder datos de Elasticsearch. Sin embargo, para
En instalaciones de evaluación temporal, donde hay poca preocupación por la pérdida de datos, se pueden utilizar discos locales.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para instancias de un solo nodo, ya sea para evaluación o de forma independiente.
instalaciones (elija una, no ambas). Tenga en cuenta que cuando utilice máquinas virtuales con los requisitos mínimos de RAM, es posible que necesite habilitar
intercambio de memoria.
Independiente
• Cantidad: 1
• Tipo: n2-estándar-8
• Almacenamiento: disco persistente equilibrado de 256 GB
Evaluación
• Cantidad: 1
• Tipo: n2-estándar-8
- 81/402 - Soluciones de cebolla de seguridad, LLC

5.15.3 Red Distribuida
• Almacenamiento: disco persistente SSD de 256 GB
• Se asume una evaluación del rendimiento y de la funcionalidad, por lo tanto, mínimos más altos en comparación con el sistema independiente.
5.15.3 Red Distribuida
Para monitoreo de producción de gran volumen, elija una arquitectura Grid de múltiples nodos. En esta arquitectura se deben utilizar al menos dos nodos de búsqueda.
Esto es necesario debido al uso de discos locales para el almacenamiento de datos de Elasticsearch, donde cada uno de los nodos de búsqueda conserva una réplica de otro.
nodo de búsqueda, para recuperación ante desastres.
A continuación se enumeran las cantidades, los tamaños y los requisitos de almacenamiento mínimos sugeridos para las instancias distribuidas de Grid. Prefiere aumentar la memoria de la máquina virtual
en lugar de habilitar la memoria de intercambio, para obtener el mejor rendimiento. Las redes de gran volumen necesitarán tipos de máquinas virtuales más potentes y con más almacenamiento que aquellas.
enumerados a continuación.
Nodo VPN
• Cantidad: 1
• Tipo: e2.micro
• Almacenamiento: disco persistente equilibrado de 50 GB
Gerente
• Cantidad: 1
• Tipo: n2-estándar-8
• Almacenamiento: disco persistente equilibrado de 300 GB
Buscar nodos
• Cantidad: 2 o más
• Tipo: n2-estándar-8
• Almacenamiento: disco persistente equilibrado de 256 GB
• Almacenamiento: Disco local de 375 GB (NVMe) [opcional]
Sensor que monitorea el ingreso de VPN
• Cantidad: 1
• Tipo: n2-estándar-4
• Almacenamiento: disco persistente equilibrado de 500 GB
5.15.4 Configurar duplicación de tráfico
Para lograr la duplicación del tráfico en GCP, se debe crear una política de duplicación de paquetes y asignarla a un equilibrador de carga interno. Google apoya
Múltiples métodos para seleccionar qué tráfico reflejar. Por ejemplo, se puede configurar una palabra clave de etiqueta especial en la política espejo, como "so-
mirror", y cualquier VM cuyo tráfico deba ser monitoreado puede recibir esa etiqueta especial. El tráfico reflejado se reenviará al sistema interno.
balanceador de carga, y una VM con sensor Security Onion será miembro del grupo de instancias de ese balanceador de carga.
Siga los pasos a continuación para configurar una configuración de duplicación de tráfico. Deberá iniciar sesión en Google Cloud Console y algo
familiarizado con GCP y cómo se utilizan las zonas y regiones. Tenga en cuenta que estos pasos son sólo una de muchas formas de hacerlo. Por ejemplo, tu
Este escenario puede requerir una configuración más avanzada, como filtrado de paquetes o VPC adicionales.
- 82/402 - Soluciones de cebolla de seguridad, LLC

5.15.5 Crear una VPC para la red monitoreada
5.15.5 Crear una VPC para la red monitoreada
Cree una nueva red de nube privada virtual (VPC) para recopilar el tráfico de red monitoreado. A esto nos referiremos a continuación como Monitoreado
Red VPC. Defina una subred dentro de esta VPC que se dedicará a recibir tráfico monitoreado.
Agregue una nueva regla de firewall a esta red de VPC para permitir todo el tráfico reflejado entrante. Especifique una etiqueta de destino de so-collector y una etiqueta de origen de
tan-espejo. Esto permitirá que todo el tráfico reflejado que se origina en una NIC de VM etiquetada con so-mirror y que reside en esta misma red VPC
se entregará a la NIC de monitoreo de la máquina virtual del sensor etiquetada con so-collector.
5.15.6 Crear una VPC para Security Onion Network
Cree una nueva red de nube privada virtual (VPC) donde se comunicará Security Onion Grid. Configure las subredes como desee,
sin embargo, se requiere al menos una subred y esta VPC no puede superponer el espacio IP con la red de VPC monitoreada mencionada anteriormente. Asegúrese de que SSH
El acceso (puerto TCP/22) y HTTPS (puerto TCP/443) están habilitados para que pueda conectarse a máquinas virtuales desde su red externa. Para
Por motivos de seguridad, se recomienda limitar el acceso entrante desde IP confiables.
Agregue una nueva regla de firewall para permitir todo el tráfico que se origine desde cualquier instancia de VM dentro de la red Security Onion VPC. Elija un rango de IP de origen
que encapsula los rangos de IP de las subredes creadas anteriormente. Esto es necesario para la conectividad entre el administrador y los nodos subordinados.
También puede optar por ser más específico sobre el tráfico dentro de la VPC; sin embargo, las reglas deben satisfacer el nodo Security Onion Firewall.
Requisitos de comunicación.
5.15.7 Crear grupo de instancias de sensores
Cree un grupo de instancias no administrado. Esto se encuentra en la sección Compute Engine de Google Cloud Console. Utilice la cebolla de seguridad
VPC como red seleccionada. Deje las instancias de VM en blanco; Más adelante en este documento, el nodo sensor Security Onion se agregará a este
grupo. La asignación de puertos no es necesaria para este grupo.
5.15.8 Crear balanceador de carga interno
En Servicios de red, dentro de Google Cloud Console, cree un equilibrador de carga. Elija TCP Load Balancer y seleccione Sólo entre
opción de mis máquinas virtuales. Haga clic en Continuar y luego seleccione Monitorear la red VPC.
Para la configuración del backend, elija el grupo de instancias creado anteriormente. Ignore el cuadro informativo que explica la necesidad de utilizar información adicional.
NIC en las instancias del grupo. Especifique que el backend sea un grupo de conmutación por error para realizar copias de seguridad. Cree una nueva comprobación de estado que utilice el puerto TCP/22 (SSH)
como prueba de salud, con las siguientes configuraciones de tiempo:
• Intervalo de verificación: 300
• Tiempo de espera: 1
• Umbral saludable: 1
• Umbral no saludable: 1
Tenga en cuenta que esta verificación de estado se implementa solo para satisfacer el requisito de GCP de que todos los backends tengan una verificación de estado asignada. desde el
El grupo backend está marcado como de conmutación por error, siempre reenviará el tráfico, independientemente del resultado de la comprobación de estado.
Para la configuración de Frontend, seleccione la subred en la red de VPC de monitoreo que creó específicamente para recibir tráfico monitoreado.
Elija IP no compartida. Si desea reenviar todo el tráfico, elija Todos los puertos y habilite el acceso global. En avanzado
Configuraciones, habilite la casilla de verificación Load Balancer for Packet Mirroring.
5.15.9 Crear política de duplicación de paquetes
La duplicación de tráfico le permite copiar el tráfico hacia/desde una instancia (o varias instancias) y enviarlo a la interfaz de detección de una red.
sensor de monitoreo de seguridad o un grupo de interfaces que utilizan un equilibrador de carga de red. Para obtener más detalles sobre GCP Traffic Mirroring, consulte:
https://cloud.google.com/vpc/docs/packet-mirroring
- 83/402 - Soluciones de cebolla de seguridad, LLC

5.15.10 Crear instancias de seguridad Onion
Cree una política de duplicación de paquetes. Esto se puede encontrar en Google Cloud Console en la sección de red VPC. Al seleccionar la VPC
red, elija la opción que indica que el origen reflejado y el destino del recopilador están en la misma red VPC y seleccione la opción Reflejado
Red VPC creada anteriormente.
En Seleccionar fuente reflejada, marque la casilla junto a la etiqueta "Seleccionar con etiqueta de red". Luego ingrese una etiqueta llamada so-mirror. Una vez completado
Con la configuración de grid, luego puede etiquetar todas sus máquinas virtuales, cuyo tráfico desea monitorear, con la misma etiqueta so-mirror.
En Seleccionar destino del recopilador, elija la regla de reenvío de front-end que se creó anteriormente durante la configuración del equilibrador de carga.
Finalmente, elija reflejar todo el tráfico, a menos que prefiera filtrar tráfico específico para duplicar.
5.15.10 Crear instancias de seguridad Onion
5.15.11 Creación de instancia
Para configurar una instancia de Security Onion (repita para cada nodo en un Grid distribuido), siga estos pasos:
• Acceda a Google Cloud Marketplace en https://console.cloud.google.com/marketplace.
• Asegúrese de tener un medio para autenticarse en instancias de VM a través de SSH. Un método para autenticarse es a través de una clave SSH para todo el proyecto, que
se puede definir en Compute Engine -> Metadatos -> Claves SSH.
• Busque Security Onion en Marketplace e inicie la última versión de la imagen oficial de VM de Security Onion. Esto puede requerir
haciendo clic en el botón "Comenzar".
• Elija el tipo de máquina apropiado según los requisitos de hardware deseados. Para obtener ayuda para determinar los requisitos de recursos
revise la sección Requisitos anterior.
• En la sección Interfaces de red, expanda la interfaz de red preagregada y seleccione la red Security Onion VPC y la red deseada.
subred. Una IP efímera externa es suficiente, a menos que planee utilizar una VPN para acceder a Security Onion Console, en cuyo caso no
Es necesaria una propiedad intelectual efímera externa. Se recomienda utilizar una VPN, pero la configuración de una VPN en GCP está fuera del alcance de esta guía.
• (Solo nodo "Sensor" distribuido o Grid de un solo nodo) Agregue una segunda interfaz de red y seleccione la red VPC de monitoreo y el
subred adecuada. No es necesaria ninguna IP efímera externa para esta interfaz.
• (Solo nodo "Administrador" distribuido o Grid de nodo único) Si no utiliza una VPN, habilite la opción Permitir tráfico SSH y HTTPS desde las direcciones IP/IP deseadas.
CIDR.
• Ajuste el tamaño y el tipo del disco de arranque según sea necesario, siguiendo las instrucciones de la sección Requisitos anterior y de otras secciones de Seguridad.
Documentación de cebolla.
• (Solo nodo de "búsqueda" distribuida o cuadrícula de evaluación) Si se necesitan discos NVMe locales de alta velocidad, se realizará una implementación manual de Terraform.
requerido, con discos locales agregados a la instancia informática. Tenga en cuenta que los discos locales solo admiten 375 GB, por lo que si se requieren volúmenes mayores
será necesario configurar el sistema para presentar los múltiples discos locales como un disco virtual. Esto está fuera del alcance de este documento. Además, ser
Tenga en cuenta que los discos locales no se replican y provocarán la pérdida de datos si se elimina la instancia.
• Si se le solicita, revise los términos de GCP Marketplace y, si es aceptable, haga clic en la casilla de verificación correspondiente.
• Seleccionar: Crear
5.15.12 Preparar nodos con almacenamiento en disco local efímero
Para nodos de búsqueda distribuidos, o un nodo de evaluación si usa almacenamiento en disco local, ingrese SSH al nodo y cancele la configuración. preparar el
partición del disco local ejecutando el siguiente comando:
Nota
Esto supone que se utilizará un único disco NVMe para almacenar todos los datos de búsqueda. Combinar varios discos en un montaje de partición única está fuera de alcance
de este documento.
sudo so-prepare-fs
- 84/402 - Soluciones de cebolla de seguridad, LLC

5.15.13 Configuración del administrador
De forma predeterminada, este comando espera que el dispositivo de disco local esté ubicado en /dev/nvme1n1 y montará ese dispositivo en /nsm/elasticsearch. si
esto falla al ejecutar lsblk para determinar qué disco usar. Para anular cualquiera de esos dos valores predeterminados, especifíquelos como argumentos. Por ejemplo:
sudo so-prepare-fs /dev/nvme0n1 /nsm/elasticsearch
Reinicie la configuración de Security Onion ejecutando el siguiente comando:
cd / cebolla de seguridad
sudo ./so-setup-network
5.15.13 Configuración del administrador
Si se trata de un nodo de evaluación con un disco local, asegúrese de que el nodo se haya preparado como se describe en la sección anterior.
Después de ingresar mediante SSH al nodo, la configuración comenzará automáticamente. Siga las indicaciones y seleccione las opciones de instalación adecuadas. Más distribuido
las instalaciones utilizarán el nombre de host u otro método de acceso web, debido a la necesidad de que ambos nodos del clúster estén dentro de la red privada, y
usuarios analistas a través de la Internet pública para comunicarse con el gerente. Esto permite que las entradas DNS personalizadas definan la IP correcta (privada o pública)
dependiendo de si se trata de un nodo del clúster o de un usuario analista. Los usuarios que evalúan Security Onion por primera vez deberían considerar elegir el
otra opción y especificando la IP de la nube pública del nodo.
GCP proporciona un servidor NTP integrado en el nombre de host metadata.google.internal. Esto se puede especificar en la pantalla Configuración SOC después de
se completa la configuración. De forma predeterminada, el servidor utilizará los servidores de hora en ntp.org.
Para nodos de administrador distribuido que utilizan almacenamiento efímero, vaya a Configuración de SOC. Busque number_of_replicas y cambie a 1. Esto
duplicará el costo de almacenamiento, pero garantizará que al menos dos máquinas virtuales tengan los datos, en caso de una pérdida efímera del disco.
Opcionalmente, ajuste los índices de ElastAlert para que tengan una réplica. Esto hará que se vuelvan amarillos, pero eso se solucionará cuando se busquen nodos.
entra en línea:
so-elasticsearch-query ElastAlert*/_settings -X PUT -d '{"índice": { "número_de_réplicas": 1 }}'
Este es un paso opcional debido a que los índices de ElastAlert se utilizan principalmente para el historial de alertas recientes o de corto plazo. En caso de pérdida de datos cuando
ElastAlert 2 se reinicia y los índices se regenerarán.
5.15.14 Configuración del nodo de búsqueda
Siga la instalación estándar del nodo de búsqueda de Security Onion y responda las indicaciones de configuración según corresponda. Si está utilizando almacenamiento en disco local,
asegúrese de preparar primero la instancia como se indicó anteriormente en esta sección.
5.15.15 Configuración del sensor GCP
En la consola de GCP, en Compute Engine, vaya a la página Grupo de instancias y edite el grupo de instancias que se creó anteriormente. Utilice el
lista desplegable para agregar la nueva instancia de VM del sensor a este grupo.
SSH en el nodo del sensor y ejecute la configuración para configurar este nodo como sensor. Elija ens4 como interfaz principal y ens5 como interfaz
interfaz de monitoreo.
5.15.16 Configuración del sensor remoto
Configure la VPN (fuera del alcance de esta guía) y conecte el nodo del sensor a la VPN. Cuando se le solicite elegir la interfaz de administración,
seleccione la interfaz del túnel VPN, como tun0. Utilice la dirección IP interna (no la IP efímera) del administrador dentro de GCP cuando se le solicite
para la IP del administrador.
Si conecta sensores a través de la instancia VPN, deberá agregar la interfaz interna de su concentrador VPN al firewall del sensor.
grupo anfitrión. Por ejemplo, suponiendo la siguiente arquitectura:
Sensor SO -> Punto final VPN -> Internet -> Punto final VPN -> Administrador SO
Ubicación: Ubicación remota: Ubicación remota: Ubicación de Google: Google
192.168.33.13 192.168.33.10 10.55.1.10 10.55.1.20
- 85/402 - Soluciones de cebolla de seguridad, LLC

5.15.17 Verificación de duplicación de tráfico
Para agregar el nodo de sensor de red remota a la red, deberá agregar 10.55.1.10 al grupo de hosts del firewall del sensor.
Este cambio se puede realizar en la pantalla de Configuración de SOC. Luego, espere hasta 15 minutos para que se ejecute la sincronización de configuración programada, o
fuerce una sincronización inmediatamente a través de las Opciones de configuración de SOC. Una vez sincronizada la configuración del grupo de hosts del firewall
su Administrador estará listo para que los minions remotos comiencen a conectarse.
5.15.17 Verificación de duplicación de tráfico
Implemente una instancia de VM de prueba temporal, utilizando una instancia e2.micro basada en Debian en la red de VPC monitoreada y en la misma región utilizada en
el resto de esta guía. Agregue la etiqueta de red so-mirror a la VM.
SSH en el nodo sensor creado anteriormente en esta guía y ejecute el siguiente comando para observar el tráfico reflejado:
tcpdump -nni ens5
Mientras se ejecuta, en otra terminal, conecte SSH a esta nueva máquina virtual de prueba y ejecute un comando curl en un sitio web popular. deberías ver eso
El tráfico HTTP/HTTPS aparece en la salida de tcpdump.
Inicie sesión en Security Onion y verifique que el tráfico también aparezca en la interfaz de usuario de Hunt.
Elimine la instancia de VM de prueba temporal cuando se complete la verificación.
- 86/402 - Soluciones de cebolla de seguridad, LLC

5.16 Configuración
5.16 Configuración
Ahora que ha instalado Security Onion, ¡es hora de configurarlo!
Security Onion está diseñado para muchos casos de uso diferentes. ¡Aquí hay sólo algunos ejemplos!
consejo
Si es la primera vez que utilizas Security Onion y solo quieres probarlo, te recomendamos la opción Importar, ya que es la forma más rápida y sencilla.
para empezar.
Advertencia
Si la parte de configuración de red muestra un mensaje como La IP que está enrutando Linux no es la dirección IP asignada al
interfaz de administración, entonces tendrá múltiples interfaces de red con direcciones IP. En la mayoría de los casos, las interfaces de rastreo no deberían tener IP.
direcciones y solo debe haber una dirección IP en la propia interfaz de administración. A veces esto se debe a una interfaz de rastreo.
conectado a un puerto de conmutador normal (no a un puerto TAP/SPAN) y adquiriendo una dirección IP a través de DHCP. Vuelva a verificar sus interfaces de red, cableado,
y configuración.
5.16.1 Importar
Una de las formas más sencillas de empezar a utilizar Security Onion es utilizarlo para analizar PCAP y archivos de registro de forma forense. Simplemente seleccione IMPORTAR
opción, siga las instrucciones y luego importe archivos PCAP o registros de eventos de Windows en formato EVTX usando la página Grid.
5.16.2 Evaluación
El modo de evaluación es ideal para aulas o entornos de laboratorio pequeños. La evaluación no está diseñada para uso en producción. Elija la opción EVAL,
siga las instrucciones y luego continúe con la sección Post instalación.
- 87/402 - Soluciones de cebolla de seguridad, LLC

5.16.3 Servidor de producción: independiente
5.16.3 Servidor de producción: independiente
Standalone es similar a Evaluación en que solo requiere una caja, pero Standalone está más preparado para su uso en producción. elegir
INDEPENDIENTE, siga las indicaciones y luego proceda a la sección Postinstalación.
5.16.4 Servidor de producción: implementación distribuida
Si implementa un entorno distribuido, primero instale y configure el nodo administrador y luego una los demás nodos. Para obtener el mejor rendimiento,
el nodo administrador debe dedicarse simplemente a ser un administrador para los otros nodos (el nodo administrador no debe rastrear la red,
que deberían ser manejados por nodos de sensores dedicados).
Cree el administrador ejecutando la instalación, seleccionando la opción de implementación DISTRIBUIDA y eligiendo la opción Nueva implementación. tu puedes
elija MANAGER o MANAGERSEARCH. Si elige MANAGER, debe unirse a uno o más nodos de búsqueda (esto es opcional si
elija MANAGERSEARCH) y querrá hacer esto antes de comenzar a unirse a otros tipos de nodos.
Cree nodos ejecutando la instalación, seleccionando la opción de implementación DISTRIBUIDA, eligiendo Implementación existente y seleccionando la opción adecuada.
opción. Tenga en cuenta que todos los nodos deberán poder conectarse al nodo administrador en varios puertos y el administrador deberá conectarse
para buscar nodos y nodos pesados. Deberá asegurarse de que todos los firewalls de red tengan reglas de firewall para permitir este tráfico como se define en el
Sección de cortafuegos. Además de los firewalls de red, deberá asegurarse de que el firewall basado en host del administrador permita las conexiones. tu puedes
Haz esto de dos maneras. La primera opción es ir a Administración --> Configuración --> firewall --> grupos de hosts, seleccionando el nodo apropiado
escriba y agregue la dirección IP. La segunda opción es esperar hasta que el nodo intente unirse y le pedirá que ejecute un comando específico en
el gerente. Independientemente de cuál de las dos opciones elija, eventualmente le pedirá que vaya a Administración --> Miembros de la Red, busque
el nodo en la lista de Miembros pendientes, haga clic en el botón Revisar y luego haga clic en el botón Aceptar.
Continúe con la sección Postinstalación.
- 88/402 - Soluciones de cebolla de seguridad, LLC

5.17 Postinstalación
5.17 Postinstalación
5.17.1 Ajustar las reglas del firewall
Dependiendo del tipo de instalación que haya realizado, es posible que el asistente de configuración ya le haya guiado para agregar reglas de firewall para permitir que su
direcciones IP del analista. Si necesita realizar otros ajustes a las reglas del firewall, puede hacerlo yendo a Administración --> Configuración -->
cortafuegos --> grupos de hosts.
Si por alguna razón no puede acceder al SOC, puede usar el comando so-firewall para permitir que la dirección IP de su navegador web se conecte
(reemplazando <DIRECCIÓN IP> con la dirección IP real de su navegador web):
sudo so-firewall includehost analista <DIRECCIÓN IP>
Para obtener más información, consulte la sección Cortafuegos.
5.17.2 Servicios
Puede consultar la página Grid para ver si todos los servicios se están ejecutando correctamente.
- 89/402 - Soluciones de cebolla de seguridad, LLC

5.17.3 SSH
Nota
Tenga en cuenta que los nodos nuevos comienzan mostrando una falla roja y pueden tardar unos minutos en inicializarse por completo antes de que muestren una señal verde OK.
También puede verificar que los servicios se estén ejecutando desde la línea de comando con el comando so-status:
sudo so-status
5.17.3 SSH
Debería poder realizar la mayor parte de la administración desde SOC, pero si necesita acceso a la línea de comando, puede usar SSH.
5.17.4 Datos
• Revise la sección Elasticsearch para ver si necesita cambiar alguna de las configuraciones predeterminadas. En particular, si tiene una implementación de múltiples nodos
con uno o más nodos de búsqueda, recomendamos ALTAMENTE configurar ILM para eliminar índices antes de que Elasticsearch alcance su marca de agua.
configuración y deja de ingerir nuevos datos.
• Revise las secciones Captura completa de paquetes y Suricata para ver si necesita cambiar la configuración de retención de PCAP.
5.17.5 Otros
• Vaya a Administración y luego haga clic en Configuración para ver algunas de las opciones que quizás desee configurar. Por ejemplo, es posible que desee
para habilitar búsquedas de DNS inversas al visualizar direcciones IP en SOC. Para obtener más información, consulte la sección Personalización de SOC.
• Mientras esté en la página de Administración, es posible que desee configurar su servidor NTP preferido.
• Es posible que los analistas de tiempo completo quieran conectarse utilizando un Security Onion Desktop dedicado.
• Cualquier sistema IDS/NSM debe ajustarse a la red que está monitoreando. Consulte las secciones Detecciones y Reglas.
- 90/402 - Soluciones de cebolla de seguridad, LLC

6. Consola cebolla de seguridad
6. Consola cebolla de seguridad
6.1 Descripción general de la consola Security Onion
Una vez completada toda la configuración, podrá conectarse a Security Onion Console (SOC) con su navegador web. Recomendamos cromo-
navegadores basados en Google Chrome. Es posible que funcionen otros navegadores, pero los navegadores basados en Chrome completamente actualizados ofrecen lo mejor
compatibilidad.
Dependiendo de las opciones que elija en el instalador, conéctese a la dirección IP o al nombre de host de su instalación de Security Onion. Luego inicia sesión
utilizando la dirección de correo electrónico y la contraseña que especificó en el instalador.
- 91/402 - Soluciones de cebolla de seguridad, LLC

6.1 Descripción general de la consola Security Onion
Una vez que haya iniciado sesión, verá el menú de usuario en la esquina superior derecha. Esto le permite administrar su configuración de usuario y acceder a la documentación.
y otros recursos.
En el lado izquierdo de la página, verá enlaces a herramientas de analistas como Alertas, Paneles, Búsqueda, Casos, Detecciones, PCAP, Kibana, CyberChef y
Navegador de ataques. Si bien las alertas, los paneles, la búsqueda, los casos, las detecciones y el PCAP están integrados en el propio SOC, las herramientas restantes son externas y
generará pestañas separadas del navegador.
Si desea personalizar SOC, consulte la sección Personalización de SOC. Si desea obtener más información sobre los registros SOC, consulte Registros SOC.
sección.
- 92/402 - Soluciones de cebolla de seguridad, LLC

6.2 Alertas
6.2 Alertas
Security Onion Console incluye una interfaz de Alertas que le brinda una descripción general de las alertas que Security Onion está generando. entonces puedes
profundice rápidamente en los detalles, cambie a Hunt o la interfaz PCAP y escale alertas a Casos.
6.2.1 Opciones
En la parte superior de la página, hay un menú de Opciones que le permite configurar varias opciones diferentes para la página de Alertas.
- 93/402 - Soluciones de cebolla de seguridad, LLC

6.2.2 Barra de consulta
Alterna
La primera opción está etiquetada como Habilitar funciones de interfaz avanzadas. Si habilita esta opción, la interfaz se mostrará más avanzada
características similares a Dashboards y Hunt. Esto incluye una opción adicional denominada Aplicar filtros, agrupaciones y fecha automáticamente.
rangos.
Al habilitar la opción Reconocido solo se mostrarán las alertas que hayan sido reconocidas previamente por un analista.
Al habilitar la opción Escalada solo se mostrarán las alertas que un analista haya escalado previamente a Casos.
Finalmente, la palanca Mostrar panel de detalles controla el panel Detalles en el lado derecho. Para obtener más información, consulte la sección Panel de detalles.
abajo.
Intervalo de actualización automática
Otra opción es la configuración del Intervalo de actualización automática. Cuando está habilitada, la página de Alertas se actualizará automáticamente en el intervalo de tiempo que usted
seleccione.
Zona horaria
Las alertas intentarán detectar su zona horaria local a través de su navegador. Puede especificar manualmente su zona horaria si es necesario.
6.2.2 Barra de consulta
La barra de consulta tiene como valor predeterminado Agrupar por nombre, Módulo, que agrupa las alertas por regla.nombre y evento.módulo. Puedes hacer clic en el menú desplegable
para seleccionar otras consultas que se agruparán por otros campos.
En el lado derecho de la barra de consulta hay un botón de búsqueda que iniciará una nueva búsqueda basada en la consulta actual.
Si desea guardar sus consultas personales, puede marcarlas en su navegador. Si desea personalizar el valor predeterminado
consultas para todos los usuarios, consulte la sección Personalización de SOC.
- 94/402 - Soluciones de cebolla de seguridad, LLC

6.2.3 Selector de hora
6.2.3 Selector de hora
De forma predeterminada, Alertas busca en las últimas 24 horas. Si desea buscar un período de tiempo diferente, puede cambiarlo en la esquina superior derecha del
pantalla.
6.2.4 Panel de detalles
El panel de detalles en el lado derecho muestra detalles de la alerta seleccionada actualmente. Esto incluye un resumen de IA (si está disponible) y opciones para
ajustando la regla que generó la alerta. Esta funcionalidad es parte de Detecciones por lo que puedes leer más en esa sección. Este panel puede ser
deshabilitado en el menú desplegable Opciones (ver arriba).
6.2.5 Tabla de datos
El resto de la página es una tabla de datos que comienza en la vista agrupada y se puede cambiar a la vista detallada. Ambas visiones tienen algunas
funcionalidad en común:
• Al hacer clic en los encabezados de la tabla, podrá ordenarlas de forma ascendente o descendente.
• Comenzando desde el lado izquierdo de cada fila, hay una flecha que expandirá la fila para mostrar más detalles.
• A la derecha de esa flecha hay un ícono de campana que reconoce la alerta. Luego, esa alerta se puede ver seleccionando el interruptor Reconocido en
la parte superior de la página. En la vista Reconocido, al hacer clic en el ícono de campana se elimina el reconocimiento.
• A la derecha hay un icono de exclamación azul que escala la alerta a Casos y le permite crear un caso nuevo o agregarlo a uno existente.
caso. Si necesita encontrar esa alerta escalada original en la página Alertas, puede habilitar la opción Escalada (que automáticamente
active también la opción Reconocido).
• A la derecha hay un ícono de información que completa el Panel de detalles a la derecha con información sobre la alerta.
• Los usuarios de Security Onion Pro encontrarán un botón más. El último es el icono de un chip de computadora que investiga la alerta con OnionAI.
• Al hacer clic en un valor de la tabla, aparece un menú contextual de acciones para ese valor. Esto le permite refinar su búsqueda existente, iniciar una nueva
buscar o incluso pasar a sitios externos como Google y VirusTotal.
• Puede ajustar la configuración de Filas por página en la parte inferior derecha y utilizar los iconos de flecha izquierda y derecha para desplazarse por la tabla.
Nota
Si está en la vista agrupada y ve una alerta que tiene varias instancias (la columna Recuento es mayor que 1) y luego hace clic en la flecha
para expandir la alerta, le mostrará los detalles de la instancia más reciente de esa alerta. Si necesita ver detalles de las otras instancias del
alerta, deberá cambiar de la vista agrupada a la vista detallada.
Análisis guiado
Cuando hace clic en la flecha para expandir la alerta, comienza en la pestaña DETALLES DE LA ALERTA, pero puede cambiar a la pestaña ANÁLISIS GUIADO que
aprovecha los Playbooks para mostrarle las jugadas asociadas con la alerta. Estas obras incluyen preguntas que ayudan a guiar su investigación. tu puedes
expanda todas las preguntas a la vez usando el botón maximizar en el lado derecho de la pestaña ANÁLISIS GUIADO.
Cada pregunta tiene una consulta asociada y los resultados de esa consulta se mostrarán para ayudarle a responder la pregunta. Un máximo de 5 consultas.
Se mostrarán los resultados, pero si desea ver más, puede hacer clic en el icono de la mira para abrir la consulta en Hunt. Esto también le permite
modifique la consulta si es necesario. Si no obtiene ningún resultado, puede intentar cambiar el rango de fechas u otros parámetros de consulta. En algunos casos, el
La consulta puede estar buscando datos que no recopila actualmente. Por ejemplo, la consulta puede buscar datos de punto final y, por lo tanto, es posible que necesite
implementar el Agente Elastic para comenzar a recopilar esta información.
Nota
Para ver el análisis guiado en acción, vea nuestro vídeo de adelanto en https://youtu.be/SLGRB3PxB-o.
- 95/402 - Soluciones de cebolla de seguridad, LLC

6.2.5 Tabla de datos
Para obtener más información sobre los Playbooks, consulte la sección Detecciones.
Advertencia
Algunos manuales fueron generados por IA y es posible que no sean 100% precisos. Háganos saber si ve algún problema.
Vista agrupada
De forma predeterminada, las alertas se agrupan según el criterio seleccionado en la barra de consulta. Hacer clic en un valor de campo y luego seleccionar la opción Explorar detalles
le permite profundizar en ese valor que cambia a la vista detallada. También puede hacer clic en el valor de la columna Recuento para realizar una
desglose rápido. Tenga en cuenta que esta función de desglose rápido solo está habilitada para determinadas consultas.
Si desea eliminar un campo en particular de la vista agrupada, puede hacer clic en el icono de papelera en la parte superior de la tabla a la derecha del nombre del campo.
Vista detallada
Si hace clic en un valor en la vista agrupada y luego selecciona la opción Explorar, la pantalla cambiará a la vista detallada. Esto muestra todas las búsquedas.
resultados y le permite profundizar en los resultados de búsqueda individuales según sea necesario. Al hacer clic en los encabezados de la tabla, podrá ordenar de forma ascendente o
descendiendo. Comenzando desde el lado izquierdo de cada fila, hay una flecha que expandirá el resultado para mostrar todos sus campos. A la derecha de eso
La flecha es el campo Marca de tiempo. A continuación, se muestran algunos campos estándar: regla.nombre, evento.etiqueta_gravedad, fuente.ip, fuente.puerto,
destino.ip y destino.puerto. Dependiendo del tipo de datos que estés viendo, puede haber algunos datos adicionales específicos.
campos también.
Cuando hace clic en la flecha para expandir una fila en la tabla Eventos, se mostrarán todos los campos individuales de ese evento. Los nombres de los campos se muestran en
a la izquierda y los valores de campo a la derecha. Al mirar los nombres de los campos, hay dos íconos a la izquierda. El ícono Groupby, el ícono más a la izquierda,
agregue una nueva tabla groupby para ese campo. El ícono Alternar columna, a la derecha del ícono Groupby, alternará esa columna en la tabla Eventos,
y el icono será de color azul si la columna está visible. Puede hacer clic en los valores a la derecha para abrir el menú contextual y refinar su búsqueda.
o pasar a otras páginas.
- 96/402 - Soluciones de cebolla de seguridad, LLC

6.2.6 Menú contextual
6.2.6 Menú contextual
Al hacer clic en un valor en la página, aparece un menú contextual que le permite refinar su búsqueda existente, iniciar una nueva búsqueda o incluso pasar a
sitios externos como Google y VirusTotal.
incluir
Al hacer clic en la opción Incluir se agregará el par campo:valor seleccionado a su búsqueda existente con un AND. Esto sólo mostrará resultados de búsqueda que
incluya ese valor en ese campo.
excluir
Al hacer clic en la opción Excluir, se agregará el par campo:valor seleccionado a su búsqueda existente con un Y NO. Esto solo mostrará resultados de búsqueda.
que no incluyen ese valor en ese campo.
Sólo
Al hacer clic en la opción Sólo se iniciará una nueva búsqueda del valor seleccionado en cualquier campo. Eliminará los filtros existentes pero conservará los existentes.
términos de grupo.
Desglose
Al hacer clic en la opción Profundizar, se profundizará en un grupo de alertas para mostrar cada alerta individual.
Detección de melodías
Al hacer clic en la opción Detección de melodías, accederá a Detecciones y le permitirá desactivar o modificar la detección que disparó la alerta.
Agrupar por
Al hacer clic en la opción Agrupar por, se actualizará la consulta existente y se agregarán los resultados según el campo seleccionado.
Nuevo grupo por
Al hacer clic en la opción Nuevo grupo por se creará una nueva tabla de datos para el campo seleccionado.
Operaciones numéricas
Si el valor en el que hizo clic es numérico, entonces el submenú Numeric Ops le permite elegir operaciones como menor que, menor que o igual,
mayor que, mayor o igual, o Entre. Al elegir la opción Entre se muestra una ventana para que pueda especificar un rango de valores.
portapapeles
El submenú Portapapeles tiene varias opciones que le permiten copiar datos seleccionados a su portapapeles de diferentes maneras.
- 97/402 - Soluciones de cebolla de seguridad, LLC

6.2.6 Menú contextual
Acciones
El submenú Acciones tiene varias opciones diferentes. Tenga en cuenta que algunas de estas acciones solo se mostrarán en el menú Acciones si
haga clic en un tipo de registro específico.
• Al hacer clic en la opción Buscar, se iniciará una nueva búsqueda del valor seleccionado y se obtendrá una buena descripción general de los tipos de datos que se encuentran.
disponible para ese indicador.
• Al hacer clic en la opción Agregar al caso, se agregará un observable a un caso nuevo o existente.
• Al hacer clic en la opción Correlacionar, encontrará registros relacionados basados en ID de comunidad, uid, fuid, etc.
• Al hacer clic en la opción PCAP, se pasará a la interfaz PCAP para recuperar la captura completa del paquete para la secuencia seleccionada. Esta opción sólo aparecerá
si hace clic en un registro que contiene IP de origen, puerto de origen, IP de destino, puerto de destino, etc.
• Al hacer clic en la opción Google, se buscará en Google el valor seleccionado.
• Al hacer clic en la opción VirusTotal, se buscará en VirusTotal el valor seleccionado.
• Al hacer clic en la opción Información del proceso se mostrarán todos los registros que incluyen el id_entidad de este proceso en el campo id_entidad_proceso. Esta opción
solo aparece si hace clic en un registro que contiene el campo Process.entity_id.
• Al hacer clic en la opción Información del proceso y del niño se mostrarán todos los registros que incluyen el id_entidad de este proceso en el proceso.id_entidad o
campos Process.parent.entity_id. Dependiendo del proceso, esto puede mostrar los mismos registros que la opción Información del proceso o puede mostrar
más. Esta opción solo aparecerá si hace clic en un registro que contiene el campo Process.entity_id.
• Al hacer clic en la opción Procesar toda la información se mostrarán todos los registros que incluyen el id_entidad de este proceso en cualquier campo. Dependiendo del proceso, este
puede mostrar los mismos registros que la opción Proceso e información del niño o puede mostrar más. Esta opción solo aparecerá si haces clic en un registro.
que contiene el campo Process.entity_id.
• Al hacer clic en la opción Procesar antecesores se mostrarán todos los procesos principales para el proceso seleccionado. Esta opción sólo aparecerá si haces clic en
un registro que contiene el campo proceso.Ext.ancestry.
Si desea agregar sus propias acciones personalizadas, consulte la sección Personalización de SOC.
- 98/402 - Soluciones de cebolla de seguridad, LLC

6.3 Paneles de control
6.3 Paneles de control
Security Onion Console incluye una interfaz de Paneles que incluye un conjunto completo de paneles prediseñados para nuestros tipos de datos estándar.
Nota
¡Mira nuestro video de paneles en https://youtu.be/xUBhyF7se8s!
6.3.1 Opciones
En la parte superior de la página, hay un menú de Opciones que le permite configurar opciones como Aplicar automáticamente, Excluir datos de casos, Excluir detecciones.
datos, excluir registros SOC, intervalo de actualización automática y zona horaria.
- 99/402 - Soluciones de cebolla de seguridad, LLC

6.3.2 Barra de consulta
Aplicar automáticamente
La opción Aplicar automáticamente está habilitada de forma predeterminada y enviará automáticamente su consulta cada vez que cambie filtros, agrupaciones o rangos de fechas.
Excluir datos del caso
Los paneles excluyen los datos de Casos de forma predeterminada. Si desactiva esta opción, podrá utilizar los paneles para consultar los datos de sus casos.
Excluir datos de detecciones
Los paneles excluyen los datos de detecciones de forma predeterminada. Si desactiva esta opción, podrá utilizar los paneles para consultar sus datos de detecciones.
Excluir registros SOC
Los paneles también excluyen los registros de diagnóstico SOC de forma predeterminada. Si desactiva esta opción, podrá utilizar los paneles para consultar su SOC.
registros de diagnóstico.
Intervalo de actualización automática
La configuración del Intervalo de actualización automática actualizará automáticamente su consulta en el intervalo de tiempo que seleccione.
Zona horaria
Los paneles intentarán detectar su zona horaria local a través de su navegador. Puede especificar manualmente su zona horaria si es necesario.
6.3.2 Barra de consulta
La forma más sencilla de comenzar es hacer clic en el cuadro desplegable de consultas y seleccionar uno de los paneles predefinidos. Estos predefinidos
Los paneles cubren la mayoría de los principales tipos de datos que esperaría ver en una implementación de Security Onion: alertas NIDS de Suricata,
registros de metadatos de protocolo de Zeek o Suricata, registros de Elastic Agent y registros de firewall.
- 100/402 - Soluciones de cebolla de seguridad, LLC

6.3.3 Selector de hora
En el lado derecho de la barra de consulta hay dos botones. El primer botón es una elipsis (tres puntos) que alterna entre mostrar la consulta completa o
sólo el filtro de búsqueda. El segundo botón es un botón de búsqueda que iniciará una nueva búsqueda basada en los filtros actuales.
Debajo de la barra de consulta, verá burbujas de colores que representan los componentes individuales de la consulta. Si desea eliminar parte del
consulta, puede hacer clic en la X en la burbuja correspondiente para eliminarla y ejecutar una nueva búsqueda.
Si desea guardar sus consultas personales, puede marcarlas en su navegador. Si desea personalizar el valor predeterminado
consultas para todos los usuarios, consulte la sección Personalización de SOC.
6.3.3 Selector de hora
De forma predeterminada, Dashboards busca en las últimas 24 horas. Si desea buscar un período de tiempo diferente, puede cambiarlo en la esquina superior derecha de
la pantalla. Puede utilizar la hora relativa predeterminada o hacer clic en el icono del reloj para cambiar a la hora absoluta.
6.3.4 Métricas básicas
La sección Métricas básicas de la página contiene una visualización de mayor número de ocurrencias, una visualización de línea de tiempo y una menor cantidad de ocurrencias.
visualización. Se puede hacer clic en los gráficos de barras, por lo que puede hacer clic en un valor para actualizar sus criterios de búsqueda. La agregación tiene por defecto 10 valores, por lo que Most
Las ocurrencias están entre las 10 principales y las de menos ocurrencias están entre las 10 inferiores (cola larga). El número de valores de agregación está controlado por Fetch
Configuración de límites en la sección Métricas del grupo.
6.3.5 Métricas de grupo
La sección Métricas de grupo de la página consta de una o más tablas de datos o visualizaciones que le permiten apilar (agregar) datos arbitrarios.
campos.
Las métricas del grupo están controladas por el parámetro groupby en la barra de búsqueda. Puede leer más sobre el parámetro groupby en el OQL
sección siguiente.
Al hacer clic en los encabezados de la tabla, podrá ordenarlas de forma ascendente o descendente. Al actualizar la página se mantendrá la clasificación, pero solo para la primera tabla.
Al hacer clic en un valor en la tabla Métricas de grupo, aparece un menú contextual de acciones para ese valor. Esto le permite refinar su búsqueda existente,
inicie una nueva búsqueda o incluso acceda a sitios externos como Google y VirusTotal. El límite de recuperación predeterminado para la tabla Métricas de grupo es 10. Si
Si necesita ver más de los 10 primeros, puede aumentar el límite de recuperación y luego revisar la salida usando los íconos de flecha izquierda y derecha o
aumente la configuración de Filas por página.
Puede utilizar los botones en el encabezado de la columna Recuento para convertir la tabla de datos en un gráfico circular o de barras. Si la tabla de datos está agrupada por más
de un campo, verá un botón adicional que convertirá la tabla de datos en un diagrama de Sankey. Hay un botón Maximizar vista
eso maximizará la tabla para llenar el panel (puede presionar la tecla Esc para volver a la vista normal). Cada uno de los encabezados de campo groupby tiene una papelera.
botón que eliminará el campo de la tabla.
Una vez que haya cambiado a un gráfico, verá diferentes botones en la parte superior del gráfico. Puede utilizar el botón Mostrar tabla para volver a la
tabla de datos, el botón Alternar leyenda para alternar la leyenda y el botón Eliminar para eliminar el gráfico por completo. Hay una vista Maximizar
que maximizará el gráfico para llenar el panel (puede presionar la tecla Esc para volver a la vista normal).
6.3.6 Eventos
La tercera y última sección de la página es una tabla de datos que contiene todos los resultados de búsqueda y le permite profundizar en los resultados de búsqueda individuales como
necesario. Al hacer clic en las etiquetas del encabezado de la tabla, podrá ordenar de forma ascendente o descendente. También puede mover una columna hacia la derecha o hacia la izquierda, o
elimine la columna haciendo clic en los iconos correspondientes que rodean las etiquetas del encabezado de la columna. Comenzando desde el lado izquierdo de cada fila, hay
una flecha que expandirá el resultado para mostrar todos sus campos. A la derecha de esa flecha está el campo Marca de tiempo. A continuación, se muestran algunos campos estándar.
mostrado: fuente.ip, fuente.puerto, destino.ip, destino.puerto, log.id.uid (identificador único de Zeek), network.community_id
(ID de comunidad) y event.dataset. Dependiendo del tipo de datos que esté viendo, puede haber algunos campos adicionales específicos de datos como
Bueno.
Al hacer clic en un valor en la tabla Eventos, aparece un menú contextual de acciones para ese valor. Esto le permite refinar su búsqueda existente, iniciar una
nueva búsqueda, o incluso pasar a sitios externos como Google y VirusTotal.
- 101/402 - Soluciones de cebolla de seguridad, LLC

6.3.7 Estadísticas
El límite de recuperación predeterminado para la tabla de eventos es 100. Si necesita ver más de 100 eventos, puede aumentar el límite de recuperación y luego buscar en la página.
a través de la salida usando los íconos de flecha izquierda y derecha o aumente la configuración de Filas por página.
Cuando hace clic en la flecha para expandir una fila en la tabla Eventos, se mostrarán todos los campos individuales de ese evento. Los nombres de los campos se muestran en
a la izquierda y los valores de campo a la derecha. Al mirar los nombres de los campos, hay dos íconos a la izquierda. El ícono Groupby, el ícono más a la izquierda,
agregue una nueva tabla groupby para ese campo. El ícono Alternar columna, a la derecha del ícono Groupby, alternará esa columna en la tabla Eventos,
y el icono será de color azul si la columna está visible. Además, al hacer clic en el icono Alternar columna se agregará un nuevo | mesa xxx yyy zzz
segmento a la consulta activa. Puede hacer clic en los valores a la derecha para abrir el menú contextual y refinar su búsqueda o pasar a otras páginas.
6.3.7 Estadísticas
La esquina inferior izquierda de la página muestra estadísticas sobre la consulta actual, incluida la velocidad de obtención de datos del backend y la ronda total.
tiempo de viaje.
6.3.8 Menú contextual
Al hacer clic en un valor en la página, aparece un menú contextual que le permite refinar su búsqueda existente, iniciar una nueva búsqueda o incluso pasar a
sitios externos como Google y VirusTotal.
incluir
Al hacer clic en la opción Incluir se agregará el par campo:valor seleccionado a su búsqueda existente con un AND. Esto sólo mostrará resultados de búsqueda que
incluya ese valor en ese campo.
excluir
Al hacer clic en la opción Excluir, se agregará el par campo:valor seleccionado a su búsqueda existente con un Y NO. Esto solo mostrará resultados de búsqueda.
que no incluyen ese valor en ese campo.
Sólo
Al hacer clic en la opción Sólo se iniciará una nueva búsqueda del valor seleccionado en cualquier campo. Eliminará los filtros existentes pero conservará los existentes.
términos de grupo.
Agrupar por
Si ya existen una o más tablas de datos Agrupar por, al hacer clic en la opción Agrupar por se agregará el campo a la tabla de datos más reciente. si hay
Si no existen tablas de datos Agrupar por, al hacer clic en la opción Agrupar por se creará una nueva tabla de datos para el campo seleccionado.
Nuevo grupo por
Al hacer clic en la opción Nuevo grupo por se creará una nueva tabla de datos para el campo seleccionado.
Operaciones numéricas
Si el valor en el que hizo clic es numérico, entonces el submenú Numeric Ops le permite elegir operaciones como menor que, menor que o igual,
mayor que, mayor o igual, o Entre. Al elegir la opción Entre se muestra una ventana para que pueda especificar un rango de valores.
portapapeles
El submenú Portapapeles tiene varias opciones que le permiten copiar datos seleccionados a su portapapeles de diferentes maneras.
- 102/402 - Soluciones de cebolla de seguridad, LLC

6.3.9 OQL
Acciones
El submenú Acciones tiene varias opciones diferentes. Tenga en cuenta que algunas de estas acciones solo se mostrarán en el menú Acciones si
haga clic en un tipo de registro específico.
• Al hacer clic en la opción Buscar, se iniciará una nueva búsqueda del valor seleccionado y se obtendrá una buena descripción general de los tipos de datos que se encuentran.
disponible para ese indicador.
• Al hacer clic en la opción Agregar al caso, se agregará un observable a un caso nuevo o existente.
• Al hacer clic en la opción Correlacionar, encontrará registros relacionados basados en ID de comunidad, uid, fuid, etc.
• Al hacer clic en la opción PCAP, se pasará a la interfaz PCAP para recuperar la captura completa del paquete para la secuencia seleccionada. Esta opción sólo aparecerá
si hace clic en un registro que contiene IP de origen, puerto de origen, IP de destino, puerto de destino, etc.
• Al hacer clic en la opción Google, se buscará en Google el valor seleccionado.
• Al hacer clic en la opción VirusTotal, se buscará en VirusTotal el valor seleccionado.
• Al hacer clic en la opción Información del proceso se mostrarán todos los registros que incluyen el id_entidad de este proceso en el campo id_entidad_proceso. Esta opción
solo aparece si hace clic en un registro que contiene el campo Process.entity_id.
• Al hacer clic en la opción Información del proceso y del niño se mostrarán todos los registros que incluyen el id_entidad de este proceso en el proceso.id_entidad o
campos Process.parent.entity_id. Dependiendo del proceso, esto puede mostrar los mismos registros que la opción Información del proceso o puede mostrar
más. Esta opción solo aparecerá si hace clic en un registro que contiene el campo Process.entity_id.
• Al hacer clic en la opción Procesar toda la información se mostrarán todos los registros que incluyen el id_entidad de este proceso en cualquier campo. Dependiendo del proceso, este
puede mostrar los mismos registros que la opción Proceso e información del niño o puede mostrar más. Esta opción solo aparecerá si haces clic en un registro.
que contiene el campo Process.entity_id.
• Al hacer clic en la opción Procesar antecesores se mostrarán todos los procesos principales para el proceso seleccionado. Esta opción sólo aparecerá si haces clic en
un registro que contiene el campo proceso.Ext.ancestry.
Si desea agregar sus propias acciones personalizadas, consulte la sección Personalización de SOC.
6.3.9 OQL
Onion Query Language (OQL) comienza con la sintaxis de consulta estándar de Lucene y luego le permite agregar segmentos opcionales que controlan qué
Dashboards lo hace con los resultados de la consulta.
ordenar
El segmento de clasificación se puede agregar al final de una consulta de búsqueda. Esto puede ayudar a garantizar que vea los datos más recientes, por ejemplo, cuando
ordenar por marca de tiempo descendente. De lo contrario, si la búsqueda arroja un conjunto de datos mayor que el tamaño del límite X seleccionado en la interfaz de usuario, solo obtendrá
los primeros X registros y luego se ordenarán en el navegador web.
Puede especificar un campo para ordenar o varios campos separados por espacios. El orden predeterminado es descendente, pero si desea forzar la clasificación
Para que sea ascendente, puede agregar el símbolo de intercalación opcional (^) al final del nombre del campo.
| ordenar por algún.campo otro.campo^
grupo
El segmento groupby le indica a Dashboards que agrupe (agregue) un campo en particular. Entonces, por ejemplo, si desea agrupar por IP de destino
dirección, puede agregar lo siguiente a su búsqueda:
| grupopor destino.ip
El segmento groupby admite múltiples agregaciones, por lo que puede agregar más campos por los que desea agrupar, separando esos campos con
espacios. Por ejemplo, para agrupar por dirección IP de destino y luego por puerto de destino en la misma tabla de datos, podría usar:
| grupopor destino.ip destino.puerto
OQL admite múltiples segmentos groupby, por lo que si desea que cada uno de esos campos tenga sus propias tablas de datos independientes, puede hacer:
- 103/402 - Soluciones de cebolla de seguridad, LLC

6.3.9 OQL
| grupopor destino.ip | grupopor destino.puerto
Además de representar tablas de datos estándar, opcionalmente puede representar los datos como un gráfico circular, un gráfico de barras o un diagrama de Sankey.
• El gráfico circular se especifica mediante la opción -pie:
| groupby -pie destino.ip
• El gráfico de barras se especifica mediante la opción -bar:
| groupby -bar destino.ip
• El diagrama sankey se especifica usando la opción -sankey, pero tenga en cuenta que esto requiere al menos dos campos:
| groupby -sankey destino.ip destino.puerto
La opción -maximize maximizará la tabla o el gráfico para llenar el panel. Después de ver el resultado maximizado, puede presionar la tecla Esc para regresar
a la vista normal.
De forma predeterminada, la agrupación por un campo en particular no mostrará ningún valor si ese campo falta. Si desea incluir valores faltantes, puede agregar
un asterisco después del nombre del campo. Por ejemplo, supongamos que desea buscar tráfico que no sea HTTP en el puerto 80 mediante una consulta como
event.dataset:conn Y destino.puerto:80 | groupby red.protocolo destino.puerto. Si había tráfico no HTTP en el puerto
80, el campo network.protocol puede ser nulo y, por lo tanto, esta consulta solo devolverá tráfico del puerto 80 identificado como HTTP. Para solucionar este problema, agregue el asterisco.
después del protocolo de red:
event.dataset:conn Y destino.puerto:80 | grupopor red.protocolo* destino.puerto
Tenga en cuenta que es posible que agregar el asterisco a un campo que no sea una cadena no funcione como se esperaba. Como alternativa, es posible que puedas utilizar el asterisco.
con el campo de palabra clave equivalente si está disponible. Por ejemplo, source.geo.ip* puede devolver 0 resultados o un error de consulta, pero
source.geo.ip.keyword* puede funcionar como se esperaba.
mesa
El segmento de tabla le indica a Dashboards que incluya los nombres de los campos dados como columnas en la tabla Eventos en la parte inferior de los paneles.
pantalla. Las columnas se ordenarán dentro de la tabla Eventos siguiendo el mismo orden utilizado en la tabla | tabla xxx yyy zzz segmento. cuando no
segmento de tabla se proporciona en la consulta, Dashboards analizará los valores event.dataset y event.module de los resultados de la consulta para
determine qué columnas predeterminadas serían las más apropiadas para representar esos eventos. Esas columnas predeterminadas están definidas en el SOC.
Configuración.
Ejemplos:
event.dataset:conexión | tabla evento.módulo fuente.ip fuente.protocolo
O, combinado con otros segmentos:
event.dataset:conexión | módulo de evento groupby | grupopor destino.ip | ordenar por fuente.puerto | tabla evento.módulo fuente.ip fuente.puerto
protocolo.fuente
Nota
Actualmente, OQL solo admite un segmento de tabla. Si se proporcionan varios en la consulta, solo se utilizará uno y los segmentos no utilizados pueden
ser eliminado automáticamente.
Recursión del diagrama de Sankey
Existe una limitación conocida con los diagramas de Sankey donde el diagrama no puede representar todos los datos cuando varios campos del diagrama contienen
el mismo valor. Esto provoca un problema de recursividad. Por ejemplo, esto puede ocurrir si se utiliza una consulta OQL de * | groupby -sankey fuente.ip
destino.ip y los eventos incluidos tienen una IP específica que aparece en los campos origen.ip y destino.ip. SOC intentará
para evitar el problema de la recursividad omitiendo cualquier dato que introduzca recursividad. Esto puede dar lugar a que algunos diagramas muestren datos parciales sobre el
- 104/402 - Soluciones de cebolla de seguridad, LLC

6.3.9 OQL
diagrama, y cuando esto ocurra, el diagrama de Sankey tendrá la frase (parcial) adjunta al título. En casos excepcionales, es posible que
el diagrama esté completamente en blanco, como si todos los resultados de datos tuvieran el mismo valor en cada campo. Siguiendo el ejemplo mencionado anteriormente, este
podría suceder si el source.ip y el destino.ip fueran siempre iguales.
- 105/402 - Soluciones de cebolla de seguridad, LLC

6.4 Caza
6.4 Caza
Security Onion Console incluye una interfaz Hunt que es similar a nuestra interfaz Dashboards, pero está más adaptada a la búsqueda de amenazas.
La principal diferencia entre Hunt y Dashboards es que las consultas predeterminadas de Hunt están más enfocadas que las consultas de descripción general en Dashboards.
Una segunda diferencia es que la mayoría de las consultas predeterminadas de Dashboards muestran una tabla separada para cada campo agregado, mientras que muchas de las
Las consultas predeterminadas en Hunt agregan varios campos en una sola tabla, lo que puede resultar beneficioso a la hora de buscar actividades más oscuras.
Aparte de estas dos diferencias, Hunt y Dashboards son muy similares, por lo que para obtener más información, consulte la sección Dashboards.
- 106/402 - Soluciones de cebolla de seguridad, LLC

6.5 Casos
6.5 Casos
Security Onion Console incluye nuestra interfaz de Casos para la gestión de casos. Le permite escalar registros desde Alertas, Paneles y Búsqueda,
y luego asigne analistas, agregue comentarios y archivos adjuntos, y realice un seguimiento de los observables.
En una nueva implementación, los Casos estarán vacíos hasta que cree un nuevo caso. Una vez que tenga uno o más casos, puede usar la página principal de Casos.
para obtener una visión general de todos los casos.
Nota
¡Mira nuestro video de Casos en https://youtu.be/y_kr_hrtqVc!
- 107/402 - Soluciones de cebolla de seguridad, LLC

6.5.1 Opciones
6.5.1 Opciones
Comenzando en la parte superior de la página principal de Casos, el menú Opciones le permite configurar opciones como Intervalo de actualización automática y Zona horaria.
También hay una palanca denominada Habilitar funciones de interfaz avanzadas. Si habilita esta opción, la interfaz se mostrará más avanzada
características similares a Dashboards y Hunt.
6.5.2 Barra de consulta
La barra de consulta tiene como valor predeterminado Casos abiertos. Al hacer clic en el cuadro desplegable se muestran otras opciones, como Casos cerrados, Mis casos abiertos, Mis casos cerrados.
Casos y plantillas. Si desea enviar su consulta actual a Hunt, puede hacer clic en el icono de la cruz a la derecha de la barra de consulta.
Debajo de la barra de consulta, verá burbujas de colores que representan los componentes individuales de la consulta y los campos por los que agrupar. si quieres
Para eliminar parte de la consulta, puede hacer clic en la X en la burbuja correspondiente para eliminarla y ejecutar una nueva búsqueda.
Si desea guardar sus consultas personales, puede marcarlas en su navegador. Si desea personalizar el valor predeterminado
consultas para todos los usuarios, consulte la sección Personalización de SOC.
6.5.3 Selector de hora
El selector de hora está a la derecha de la barra de consulta. De forma predeterminada, Casos busca en los últimos 12 meses. Si desea buscar un período de tiempo diferente,
puedes cambiarlo aquí.
- 108/402 - Soluciones de cebolla de seguridad, LLC

6.5.4 Tabla de datos
6.5.4 Tabla de datos
El resto de la página principal de Casos es una tabla de datos que muestra una descripción general de alto nivel de los casos que coinciden con los criterios de búsqueda actuales.
• Al hacer clic en los encabezados de la tabla, podrá ordenarlas de forma ascendente o descendente.
• Al hacer clic en un valor de la tabla, aparece un menú contextual de acciones para ese valor. Esto le permite refinar su búsqueda existente, iniciar una nueva
buscar o incluso pasar a sitios externos como Google y VirusTotal.
• Puede ajustar la configuración de Filas por página en la parte inferior derecha y utilizar los iconos de flecha izquierda y derecha para desplazarse por la tabla.
• Cuando hace clic en la flecha para expandir una fila en la tabla de datos, se mostrarán los campos de alto nivel de ese caso. Los nombres de los campos se muestran en la
valores de campo a la izquierda y a la derecha. Al mirar los nombres de los campos, hay un ícono a la izquierda que agregará ese campo a la sección groupby
de tu consulta. Puede hacer clic en los valores a la derecha para abrir el menú contextual y refinar su búsqueda.
• A la derecha de la flecha hay un icono de binoculares. Al hacer clic aquí se mostrará el caso completo, incluidos Comentarios, Adjuntos, Observables,
Pestañas Eventos e Historial.
6.5.5 Creación de un nuevo caso
Para crear un nuevo caso, haga clic en el ícono + y luego complete el Título y la Descripción y, opcionalmente, los campos en el lado derecho, incluido el Cesionario,
Estado, gravedad, prioridad, TLP, PAP, categoría y etiquetas. Al hacer clic en los campos del lado derecho, se muestran cuadros desplegables con opciones estándar. el
El campo Cesionario solo enumerará las cuentas de usuario que están actualmente habilitadas.
Alternativamente, si encuentra eventos de interés en Alertas, Paneles o Búsqueda, puede escalar directamente a Casos usando el botón escalar (azul
triángulo con signo de exclamación). Al hacer clic en el botón escalar, se escalarán los datos de la fila tal como se muestran. Esto significa que si estás
Al observar una vista agregada, obtendrá detalles limitados en el caso escalado resultante. Si desea que se incluyan más detalles en el caso,
luego, primero profundice en la agregación y escale uno de los elementos individuales de esa agregación. Una vez que haga clic en el botón escalar, podrá
elegir escalar a un caso nuevo o a un caso existente.
6.5.6 Comentarios
En la pestaña Comentarios, puede agregar comentarios sobre el caso. El campo Comentarios utiliza sintaxis de rebajas y puede leer más sobre eso.
en https://www.markdownguide.org/cheat-sheet/.
- 109/402 - Soluciones de cebolla de seguridad, LLC

6.5.7 Adjuntos
Si ha habilitado Security Onion Pro, al agregar un comentario también puede especificar cuántas horas pasó trabajando en esa actividad.
Luego podrá ver el tiempo total dedicado por todos los analistas en el Resumen en la esquina superior derecha.
6.5.7 Adjuntos
En la pestaña Adjuntos, puede cargar archivos adjuntos. Para cada archivo adjunto, opcionalmente puede definir TLP y agregar etiquetas. Los casos serán
Genera automáticamente valores hash SHA256, SHA1 y MD5 para cada archivo adjunto. Los botones al lado de los valores hash le permiten copiar el
valorarlo o agregarlo como observable.
6.5.8 Observables
En la pestaña Observables, puede rastrear observables como direcciones IP, nombres de dominio, hashes, etc. Puede agregar observables directamente en esta
o también puede agregarlos desde la pestaña Eventos.
Puede agregar múltiples observables del mismo tipo seleccionando la opción etiquetada
Habilite esta casilla de verificación para agregar un observable separado para cada línea del valor proporcionado anteriormente.
Para cada observable, puede hacer clic en el icono en el extremo izquierdo de la fila para profundizar en el observable y ver más información al respecto. a la derecha
De eso está el ícono de búsqueda que iniciará una nueva búsqueda de lo observable. Al hacer clic en el icono del rayo se analizará lo observable (consulte la
sección de analizadores más adelante).
También puede agregar observables directamente desde Alertas, Paneles o Hunt. Haga clic en el observable y seleccione la opción Agregar al caso. entonces tu
tiene la opción de agregar el observable a un caso nuevo o a un caso existente.
6.5.9 Eventos
En la pestaña Eventos, puede ver los eventos que se han escalado al caso. Podrían ser alertas de Suricata, metadatos de red de
Suricata o Zeek, o registros de puntos finales.
Para cada evento, puede hacer clic en el icono en el extremo izquierdo de la fila para profundizar y ver todos los campos incluidos en ese evento.
Si encuentra algo que le gustaría rastrear como Observable, puede hacer clic en el ícono del ojo en el extremo izquierdo de la fila para agregarlo al
Pestaña Observables. Intentará identificar automáticamente tipos de datos conocidos, como direcciones IP.
A la derecha del ícono del ojo hay un ícono de Búsqueda que se puede usar para iniciar una nueva búsqueda de ese valor en particular.
6.5.10 Historia
En la pestaña Historial, puede ver el historial del caso en sí, incluidos los cambios realizados por cada usuario. Para cada fila del historial, puede hacer clic
Haga clic en el icono en el extremo izquierdo de la fila para profundizar y ver más información.
6.5.11 Datos
Los datos de los casos se almacenan en Elasticsearch. Puede verlo en Paneles o Hunt haciendo clic en el menú Opciones y desactivando el caso Excluir.
opción de datos. Luego puede buscar el índice de casos con la siguiente consulta:
_index:"*:así es el caso"
También puede utilizar esta consulta en Kibana.
Es posible que desee hacer una copia de seguridad de estos datos como se describe en la sección de copia de seguridad.
6.5.12 Analizadores
Hemos incluido analizadores que le permiten recopilar rápidamente el contexto en torno a un observable.
- 110/402 - Soluciones de cebolla de seguridad, LLC

6.5.12 Analizadores
Nota
¡Mira nuestro video de Analizadores en https://youtu.be/99LXr7UmtKI!
Analizadores y tipos de datos admitidos
El siguiente es un resumen de los analizadores integrados y los tipos de datos admitidos:
| Nombre Dominio | Hash EML | Correo IP | Otro URI | Agente de usuario URL |
| ---------------- | -------- | ------- | --------- | -------------- |
| Alienvault OTX ✓ | ✓ |         |           | ✓ |
Ecotrail ✓
| Búsqueda elástica ✓ | ✓ ✓ | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| --------------- | --- | --- | --- | --- |
| Representante de correo electrónico |     | ✓ |     |     |
| Ruido gris |     | ✓ |     |     |
| Archivo local ✓ | ✓ ✓ |     | ✓ | ✓ |
Bazar de malware ✓
Hash de malware ✓
Registro
| Buceo pulsado ✓ | ✓ ✓ |     | ✓ | ✓ ✓ |
| ---------------- | --- | --- | --- | --- |
| Spamhaus |     | ✓ |     |     |
| Plataforma sublime | ✓ |     |     |     |
| Zorro amenazador ✓ | ✓ ✓ |     |     |     |
Casa URL ✓
Exploración de URL ✓
| Total de virus ✓ | ✓ ✓ |     |     | ✓ |
| ------------ | --- | --- | --- | --- |
Búsqueda Whois ✓
Nota
El analizador de malwarehashregistry ya no funciona. Esto se debe a una biblioteca de terceros obsoleta que es incompatible con la última versión de Python.
versión. Ver #13571
Analizadores en ejecución
Para poner en cola un trabajo del analizador, haga clic en el icono del rayo en el lado izquierdo del menú observable. Todos los analizadores configurados que admitan el
El tipo de datos observable se ejecutará y devolverá su análisis.
Nota
Los valores observables deben formatearse para que coincidan correctamente con el tipo observable para que los analizadores se ejecuten correctamente en ellos. Para
Por ejemplo, un tipo de IP observable no debe contener más de una dirección IP.
Salida del analizador
La vista de trabajo contraída de un analizador devolverá una vista resumida del análisis. Al expandir la fila contraída se mostrará una información más detallada.
vista del análisis.
Advertencia
Si intenta ejecutar el analizador de Malware Hash Registry pero genera un error de "Nombre o servicio desconocido", entonces puede ser un problema de DNS. gente que usa
8.8.4.4 o 8.8.8.8 como su solucionador de DNS han informado de este problema. Una posible solución es cambiar a otro solucionador de DNS como 1.1.1.1.
Configuración de analizadores
Algunos analizadores requieren que se configuren autenticación u otros detalles antes de su uso. Si se solicita análisis para un observable y un analizador
admite ese tipo observable pero el analizador no está configurado, entonces no se ejecutará.
- 111/402 -
Soluciones de cebolla de seguridad, LLC

6.5.13 Plantillas
Los siguientes analizadores requieren que los usuarios configuren la autenticación u otros parámetros para que el analizador funcione correctamente:
• AlienVault OTX
• Ecotrail
• Búsqueda elástica
• Representante de correo electrónico
• Ruido gris
• Archivo local
• Bazar de malware
• Buceo pulsado
• Zorro amenazador
• Exploración de URL
• Total de virus
Para configurar un analizador, navegue hasta Administración --> Configuración --> sensoroni.
En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada. Luego navega a sensoroni -->
analizadores.
Desarrollo de analizadores
Si desea desarrollar un analizador personalizado, consulte la guía para desarrolladores en https://github.com/Security-Onion-Solutions/securityonion/
árbol/3/main/salt/sensoroni/files/analyzers.
6.5.13 Plantillas
SOC puede usar plantillas de casos para completar automáticamente los valores predeterminados de nuevos casos. Una plantilla es en sí misma un caso, con su categoría establecida en plantilla. a
utilizar ese caso de plantilla, el nuevo caso debe especificar el ID del caso de plantilla en el campo de plantilla del objeto de caso.
- 112/402 - Soluciones de cebolla de seguridad, LLC

6.5.13 Plantillas
SOC completa automáticamente nuevos campos de plantilla de caso con el valor almacenado en el campo rule.case_template de la alerta que se está escalando.
Esto permite asignar plantillas específicas a determinadas reglas de detección. Por ejemplo, si se sabe que las alertas activadas por una determinada regla
requieren un conjunto consistente de pasos de resolución, entonces la descripción de una plantilla de caso se puede completar previamente con esa lista de verificación (en Markdown).
formato). Luego, la regla de respaldo que activó la alerta puede tener su campo case_template establecido en ese ID de plantilla de caso.
- 113/402 - Soluciones de cebolla de seguridad, LLC

6.6 Detecciones
6.6 Detecciones
Security Onion Console incluye nuestra interfaz de Detecciones para administrar todas sus reglas:
• Reglas NIDS que se cargan en Suricata
• Reglas Sigma que se cargan en ElastAlert
• Reglas de YARA que se cargan en Strelka
Nota
¡Mira nuestro video de Detecciones en https://youtu.be/DelAmqtU2hg!
6.6.1 Estado del motor de reglas
La esquina superior derecha muestra un recuento de detecciones que coincidieron con la consulta de búsqueda. A la izquierda hay un indicador de estado para cada uno de los
motores de detección. El estado puede mostrar si hay una sincronización en proceso, así como si el motor ha detectado errores.
- 114/402 - Soluciones de cebolla de seguridad, LLC

6.6.2 Opciones
Aquí está la lista de posibles mensajes de estado y su significado:
• Pendiente: el navegador está esperando que el servidor envíe un informe de estado inicial.
• Importación pendiente: la importación comenzará una vez que el sistema se estabilice, generalmente dentro de veinte minutos.
• Importación: La versión anterior de las reglas de Security Onion se está importando al nuevo sistema de Detecciones. Esto puede tardar una hora o
más en algunos sistemas.
• Migración: las reglas se migrarán entre versiones de Security Onion después de las actualizaciones del sistema. Esto puede llevar algún tiempo si se actualiza desde
una versión mucho más antigua.
• Error de migración: se produjo un error durante la migración. La migración se detendrá ante el primer error y no intentará migrar a una versión más nueva.
versiones hasta que se resuelva el problema.
• Sincronizando: hay una sincronización de reglas en curso. Esto ocurre a diario, para garantizar que Security Onion Grid tenga las reglas más recientes.
• Error de sincronización: se produjo un error durante el procedimiento de sincronización. La próxima sincronización se reintentará en unos minutos.
• Sincronización bloqueada: la sincronización de reglas está actualmente bloqueada.
• Discrepancia de reglas: un proceso de verificación de integridad detectó una discrepancia entre las reglas implementadas y las reglas habilitadas. El registro SOC anotará
las reglas específicas no coincidentes. Una posible razón es que Elasticsearch ha alcanzado su configuración de marca de agua de disco y ya no permite
actualizaciones de los índices de Detecciones.
• Correcto: no se conocen problemas con el motor de reglas.
consejo
Al hacer clic en el texto de estado, se navegará hasta Hunt e intentará encontrar registros relacionados. Si el estado informa algún tipo de error, es posible que desee
Utilice Hunt para centrarse en aspectos como la comprobación de integridad fallida u otros errores.
Como parte del proceso de sincronización, Detecciones busca duplicados. Si se encuentran duplicados, Detecciones registrará información sobre el duplicado.
La opción del menú Detecciones en el lado izquierdo de la aplicación mostrará un signo de exclamación si hay una falla reciente en cualquiera de las
motores de detección. En esta situación, la pestaña del navegador web también mostrará un indicador de exclamación. Si no se detectan fallos y si alguno de los
Los motores de detección tienen una importación pendiente o están realizando una importación, sincronización o migración de reglas, luego aparecerá un reloj de arena azul a continuación.
a la opción de menú Detecciones.
6.6.2 Opciones
El menú Opciones le permite sincronizar un motor de detección particular como ElastAlert, Strelka o Suricata.
- 115/402 - Soluciones de cebolla de seguridad, LLC

6.6.3 Barra de consulta
Una vez que haya seleccionado el motor de detección que desea sincronizar, puede hacer clic en ACTUALIZACIÓN DIFERENCIAL o ACTUALIZACIÓN COMPLETA.
botón.
La actualización diferencial es una sincronización ligera que omitirá la sincronización y comparación exhaustiva de cada regla individual. Por ejemplo, con
Suricata calculará y comparará el hash de la lista de reglas de origen con el hash de las reglas implementadas, y solo si hay una discrepancia lo hará.
realizar la sincronización completa.
Una sincronización completa puede implicar inspeccionar y comparar reglas individuales, de las cuales puede haber miles. Esta sincronización más completa puede llevar mucho
más largo que la sincronización diferencial. Tenga en cuenta que cada motor tiene su propio proceso de sincronización exclusivo.
6.6.3 Barra de consulta
La barra de consulta tiene como valor predeterminado Todas las detecciones. Al hacer clic en el cuadro desplegable se muestran otras opciones, como Detecciones personalizadas,
Todas las detecciones: habilitadas y Todas las detecciones: deshabilitadas.
Debajo de la barra de consulta, verá burbujas de colores que representan los componentes individuales de la consulta. Si desea eliminar parte del
consulta, puede hacer clic en la X en la burbuja correspondiente para eliminarla y ejecutar una nueva búsqueda.
Si desea guardar sus consultas personales, puede marcarlas en su navegador. Si desea personalizar el valor predeterminado
consultas para todos los usuarios, consulte la sección Personalización de SOC.
6.6.4 Métricas de grupo
La sección de resultados de Métricas de grupo consta de una o más tablas de datos o visualizaciones que le permiten apilar (agregar) campos arbitrarios.
- 116/402 - Soluciones de cebolla de seguridad, LLC

6.6.5 Tabla de datos
6.6.5 Tabla de datos
El resto de la página principal de Detecciones es una tabla de datos que muestra una descripción general de alto nivel de las detecciones que coinciden con la búsqueda actual.
criterios.
• Al hacer clic en los encabezados de la tabla, podrá ordenarlas de forma ascendente o descendente.
• Al hacer clic en un valor de la tabla, aparece un menú contextual de acciones para ese valor. Esto le permite refinar su búsqueda existente o copiar texto a
el portapapeles.
• Puede ajustar la configuración de Filas por página en la parte inferior derecha y utilizar los iconos de flecha izquierda y derecha para desplazarse por la tabla.
• Cuando hace clic en la flecha para expandir una fila en la tabla de datos, se mostrarán los campos de alto nivel de esa detección. Los nombres de los campos se muestran en
a la izquierda y los valores de campo a la derecha. Puede hacer clic en los valores a la derecha para abrir el menú contextual y refinar su búsqueda.
• A la derecha de la flecha hay un icono de binoculares. Al hacer clic aquí, accederá a la página de detalles de la detección.
6.6.6 Detalles de detección
Hay dos formas de llegar a la página de detalles de una detección individual:
• Desde la interfaz principal de Detecciones, puede buscar la detección deseada y hacer clic en el icono de binoculares.
• Desde la interfaz de Alertas, puede hacer clic en una alerta y luego hacer clic en el elemento del menú Detección de melodía.
Una vez que haya utilizado uno de estos métodos para llegar a la página de detalles de la detección, puede verificar el campo Estado en la esquina superior derecha y usar
el control deslizante para habilitar o deshabilitar la detección.
A la izquierda del campo Estado hay varias pestañas.
La pestaña DESCRIPCIÓN GENERAL muestra el resumen, las referencias y la lógica de detección para la detección. El campo Resumen puede contener un resumen de IA
de la regla si hay uno disponible. Estos resúmenes de IA se generan previamente, por lo que nunca se envía nada desde su sistema para generar esta información.
Eso también significa que los resúmenes de IA solo existen para nuestras reglas predeterminadas y no existirán para ninguna de sus reglas personalizadas.
La pestaña NOTAS OPERACIONALES le permite agregar sus propias notas locales a la detección en formato de rebajas.
- 117/402 - Soluciones de cebolla de seguridad, LLC

6.6.6 Detalles de detección
La pestaña FUENTE DE DETECCIÓN muestra el contenido completo de la detección.
La pestaña TUNING le permite ajustar la detección. Para las reglas NIDS, puede modificarlas, suprimirlas o establecer un umbral. Para las reglas Sigma, puede crear un
filtro personalizado.
- 118/402 - Soluciones de cebolla de seguridad, LLC

6.6.6 Detalles de detección
La pestaña PLAYBOOKS muestra las jugadas aplicables para esta detección. Estos manuales se utilizan para la pestaña Análisis guiado en Alertas.
Advertencia
Algunos manuales fueron generados por IA y es posible que no sean 100% precisos. Háganos saber si ve algún problema.
La pestaña HISTORIAL muestra el historial de detección desde que se agregó a su implementación.
- 119/402 - Soluciones de cebolla de seguridad, LLC

6.6.7 Más información
6.6.7 Más información
Para obtener más información sobre cómo administrar las reglas NIDS para Suricata, consulte la sección NIDS.
Para obtener más información sobre cómo administrar las reglas de Sigma para ElastAlert, consulte la sección Sigma.
Para obtener más información sobre cómo administrar las reglas de YARA para Strelka, consulte la sección YARA.
6.6.8 Antecedentes técnicos
Las detecciones abstraen el motor de alertas subyacente y simplifican la escritura de detecciones para diferentes tipos de reglas. Esto es lo que sucede detrás del
escenas.
Habilitar y deshabilitar operaciones (masivas e individuales)
ElastAlert/Sigma: cambio inmediato en la interfaz de usuario y en el disco
Suricata/NIDS - UI masiva e individual: cambio inmediato en la UI y en el disco - Regex: la UI y el disco cambian una vez que el motor Suricata se sincroniza
Strelka/YARA: cambio inmediato en la interfaz de usuario, cambio de disco una vez que el estado de Strelka se ejecuta nuevamente
Sintonización
ElastAlert/Sigma: cambio inmediato en la interfaz de usuario y en el disco
Suricata/NIDS: cambio inmediato en la interfaz de usuario y en el disco
Strelka/YARA - N/A
Cambios en el conjunto de reglas
ElastAlert/Sigma - Paquetes de conjunto de reglas Sigma: la interfaz de usuario y el disco cambian una vez que el estado del SOC se ejecuta nuevamente y el motor ElastAlert se sincroniza - Git repo
(https o disco): la interfaz de usuario y el disco cambian una vez que el estado SOC se ejecuta nuevamente y el motor ElastAlert se sincroniza
- 120/402 - Soluciones de cebolla de seguridad, LLC

6.6.8 Antecedentes técnicos
Suricata/NIDS: todas las fuentes del conjunto de reglas (ETOPEN, ETPRO, URL personalizada, directorio local): la interfaz de usuario y el disco cambian una vez que el motor Suricata se sincroniza
Strelka/YARA: repositorio de Git (https o disco): la interfaz de usuario y el disco cambian una vez que el estado SOC se ejecuta nuevamente y el motor Strelka se sincroniza
- 121/402 - Soluciones de cebolla de seguridad, LLC

6.7 PCAP
6.7 PCAP
Security Onion Console incluye una interfaz PCAP que le permite acceder a la captura completa de paquetes escrita en el disco por Suricata.
Puede acceder a PCAP de dos formas diferentes. La primera y más común opción es pasar a PCAP desde un evento particular en Alertas,
Paneles o Buscar eligiendo la acción PCAP en el menú de acciones.
La segunda opción, menos común, es ir directamente a la interfaz PCAP, hacer clic en el botón azul + y luego ingresar sus criterios de búsqueda para
buscar una secuencia en particular.
- 122/402 - Soluciones de cebolla de seguridad, LLC

6.7 PCAP
Independientemente de cuál de estas dos opciones elija, Security Onion debería localizar la transmisión y generar una descripción general de alto nivel de la misma.
paquetes.
Si hay muchos paquetes en la secuencia, puede usar el botón CARGAR MÁS, la configuración de Filas por página y las flechas para navegar por la lista.
de paquetes.
Puede profundizar en filas individuales para ver los datos de carga útil reales. Hay botones en la parte superior de la tabla que controlan qué datos se muestran en
las filas individuales. Si desactiva los botones Mostrar todos los datos del paquete y HEX, obtendrá una transcripción ASCII.
- 123/402 - Soluciones de cebolla de seguridad, LLC

6.7 PCAP
Puede seleccionar texto con el mouse y luego usar el menú contextual para enviar ese texto seleccionado a CyberChef, Google u otros destinos.
definido en la lista de acciones.
Hay dos botones en el lado derecho del encabezado de la tabla. El primero enviará todos los datos del paquete visible a CyberChef. Tenga en cuenta que esto sólo
envía paquetes de datos que se están mostrando actualmente, por lo que si está viendo una secuencia grande, es posible que necesite usar el botón CARGAR MÁS para
mostrar todos los paquetes en la secuencia. El segundo botón en el extremo derecho le permite descargar el archivo PCAP completo. Luego puede abrir el PCAP
archivo usando NetworkMiner, Wireshark o cualquier otra herramienta libpcap estándar. Por lo general, debería evitar realizar el análisis PCAP en su rutina normal.
entorno de escritorio, por lo que es posible que desee considerar abrir el archivo PCAP en una instancia de Security Onion Desktop.
Una vez que haya visto uno o más PCAP, los verá enumerados en la página principal de PCAP.
- 124/402 - Soluciones de cebolla de seguridad, LLC

6.7.1 Solución de problemas
Cuando haya terminado con un PCAP, es posible que desee eliminarlo usando el botón X en el extremo derecho. Esto elimina el archivo PCAP en caché guardado en /
nsm/soc/trabajos/.
6.7.1 Solución de problemas
Si tiene problemas para recuperar PCAP, aquí hay algunas cosas que debe verificar:
• Verifique que la captura completa de paquetes esté habilitada a través de Suricata.
• Verifique si tiene alguna configuración de BPF que pueda hacer que Suricata ignore el tráfico.
• Verifique Grid y verifique que todos los servicios estén funcionando correctamente.
• Verifique InfluxDB y verifique que la retención de PCAP sea lo suficientemente larga para incluir la transmisión que está buscando.
• Asegúrese de que haya suficiente espacio libre en /nsm para dividir la secuencia y escribir la salida en el disco.
- 125/402 - Soluciones de cebolla de seguridad, LLC

6.8 Cuadrícula
6.8 Cuadrícula
Security Onion Console incluye una interfaz de grid que le permite comprobar rápidamente el estado de todos los nodos de su grid.
Comenzando en la parte superior de la página, hay un valor de EPS de cuadrícula en la esquina superior derecha que muestra la suma de todos los EPS de consumo.
mediciones en toda la Red. Debajo encontrará una lista de todos los nodos en su cuadrícula.
Advertencia
Tenga en cuenta que los nodos nuevos comienzan mostrando una falla roja y pueden tardar unos minutos en inicializarse por completo antes de que muestren una señal verde OK.
Nota
La columna EPS representa eventos por segundo consumidos, por lo que solo será relevante en los nodos que ingieren datos. Los sensores puros no ingieren
eventos, por lo que esos nodos mostrarán 0 EPS. Si desea identificar sensores que generan grandes volúmenes de eventos, puede ordenarlos por Mgmt Out
columna, que muestra el rendimiento del tráfico saliente en la interfaz de red de administración.
El menú desplegable de opciones cerca de la parte superior de la página incluye una casilla de verificación que mostrará columnas adicionales relacionadas con sensores en la tabla. tu puedes
Utilice estas columnas ordenables para ayudar a identificar sensores que puedan tener un rendimiento deficiente o que necesiten una actualización de hardware. Como estos adicionales
Las columnas ocupan un área importante de la pantalla, solo serán visibles en pantallas anchas donde se encuentre la ventana del navegador web de Security Onion Console.
lo suficientemente ancho como para mostrar una gran cantidad de columnas tabulares.
- 126/402 - Soluciones de cebolla de seguridad, LLC

6.8.1 Estado del nodo
Puede profundizar en nodos individuales para ver información detallada, incluido el estado del nodo, el estado del contenedor y las imágenes del dispositivo.
6.8.1 Estado del nodo
La sección Estado del nodo muestra muchos campos diferentes relacionados con el estado de cada nodo.
Nota
Si un nodo no se ha registrado recientemente, las métricas y los estados de ese nodo aparecerán ligeramente atenuados para indicar que los valores están obsoletos.
identificación
El campo ID muestra el nombre de host asignado al nodo.
Rol
El campo Función muestra el tipo de nodo de Security Onion que se seleccionó durante la configuración de Security Onion.
Dirección
El campo Dirección muestra la dirección IP de la red asignada a la interfaz de administración del nodo.
Versión
El campo Versión muestra la versión de Security Onion instalada en este nodo.
modelo
El campo Modelo muestra el número de modelo oficial del dispositivo Security Onion Solutions. Para dispositivos que no son SOS, este campo mostrará N/A.
- 127/402 - Soluciones de cebolla de seguridad, LLC

6.8.1 Estado del nodo
Fecha de creación
El campo Fecha de creación muestra la fecha en que se creó el nodo. Esta fecha se basa en las marcas de tiempo del sistema de archivos del nodo, por lo que reemplazar la partición
Los datos o la recreación manual de áreas centrales del sistema de archivos pueden interferir con la evaluación de la edad real de un nodo.
PCAP más temprano
El campo PCAP más antiguo muestra el PCAP más antiguo que está disponible en un nodo de sensor y solo es visible en nodos de sensor que capturan en vivo.
datos del paquete.
Última noticia desde
El campo Última escucha de muestra la última vez que el nodo se registró con el administrador. Tenga en cuenta que un check-in no siempre incluye
Métricas de nodo actualizadas.
edad
El campo Edad muestra cuánto tiempo el nodo ha sido parte de la cuadrícula y se basa en el valor de Fecha de creación.
Tiempo de actividad del sistema operativo
El campo Tiempo de actividad del sistema operativo muestra cuánto tiempo ha estado ejecutándose el nodo desde el último evento de encendido o reinicio.
Si es necesario reiniciar el nodo para aplicar las actualizaciones del kernel, aparecerá un mensaje junto al valor de tiempo de actividad que lo indica. El reinicio
El botón en la parte inferior de la página Grid permite a los administradores reiniciar de forma remota un nodo a través de la interfaz web de Security Onion Console.
Última sincronización
El campo Última sincronización muestra cuánto tiempo hace que se sincronizó el nodo con el nodo administrador. Esto equivale a la última sal.
carrera por el alto estado. Conocer este valor puede ser útil al realizar cambios de configuración en la red y determinar si un nodo específico tiene
recibió esos cambios.
Estado del proceso
Si el campo Estado del proceso muestra Fallo, puede verificar los otros indicadores de estado así como la sección Estado del contenedor para determinar
qué proceso ha fallado.
Estado de conexión
El campo Estado de conexión muestra si el nodo está actualmente conectado a la red.
Estado de búsqueda elástica
Si el nodo ejecuta Elasticsearch, el campo Estado de Elasticsearch mostrará su estado. Si el estado no es OK, entonces
consulte la sección Elasticsearch para solucionar problemas.
Estado de RAID
Si está utilizando un dispositivo oficial de Security Onion Solutions con soporte RAID, verá aparecer el estado correspondiente en este
campo.
EPS de consumo
El campo EPS de consumo es la cantidad de eventos por segundo consumidos.
- 128/402 - Soluciones de cebolla de seguridad, LLC

6.8.1 Estado del nodo
Uso de la memoria
El campo Uso de memoria muestra el porcentaje de memoria del sistema utilizado, así como la memoria total, en gigabytes. Si este valor está consistentemente en
el rojo, entonces puede que sea el momento de agregar más memoria al sistema. El uso constante del rojo probablemente terminará causando fallas en los nodos debido a algunos servicios.
se apaga automáticamente para recuperar memoria para procesos más críticos.
Uso de intercambio
El campo Uso de intercambio muestra el porcentaje de intercambio del sistema utilizado, así como el intercambio total, en gigabytes. Sistemas que no tienen swap
habilitado permanecerá en 0,0%. Si este valor está constantemente en rojo, entonces puede ser el momento de aumentar la memoria del sistema y potencialmente la
tamaño de intercambio.
Uso de CPU
El campo Uso de CPU muestra el porcentaje de CPU del sistema utilizado en todos los núcleos. Si este valor está constantemente en números rojos, entonces puede ser el momento de
actualice el hardware del nodo o distribuya la carga entre nodos adicionales.
Espera de E/S
El campo Espera de E/S muestra el porcentaje de espera de E/S del sistema. Los valores más altos indican que el sistema pasa más tiempo esperando la red o
transferencia de datos del disco. Si este valor está constantemente en números rojos, entonces puede ser el momento de reemplazar los discos lentos o ampliar la capacidad de rendimiento de la red.
Pérdida de captura
El campo Pérdida de captura muestra el porcentaje de pérdida de captura de paquetes reportada por Zeek. Los valores más altos indican una visibilidad reducida en
paquetes que atraviesan la red. Si Zeek informa pérdida de captura pero no pérdida de paquetes, esto generalmente significa que se está produciendo una pérdida de captura.
aguas arriba en el propio puerto TAP o SPAN.
Pérdida de Zeek
El campo Zeek Loss muestra el porcentaje de paquetes descartados debido a que Zeek no pudo mantener el ritmo del flujo de datos de la red.
Pérdida de Suricata
El campo Pérdida de Suricata muestra el porcentaje de paquetes descartados debido a que Suricata no pudo mantener el ritmo del flujo de datos de la red.
Uso de la partición raíz
El campo Uso de la partición raíz muestra el porcentaje de utilización del disco del sistema operativo raíz, así como la capacidad total de ese disco (o partición).
Si este valor está constantemente en rojo, puede provocar problemas, como la imposibilidad de actualizar los paquetes del sistema operativo y Security Onion, el
incapacidad para guardar registros del sistema y otros problemas críticos.
Uso de la partición NSM
El campo Uso de partición NSM muestra el porcentaje de utilización del disco NSM, así como la capacidad total de ese disco (o partición). si
Si este valor está constantemente en rojo, puede provocar problemas como la imposibilidad de ingerir nuevos eventos, almacenar PCAP en el disco, detectar
eventos anómalos y otros problemas críticos.
Almacenamiento elástico utilizado
El campo Almacenamiento elástico utilizado muestra el total de gigabytes utilizados por Elasticsearch para almacenar los eventos ingeridos, en todos los índices.
- 129/402 - Soluciones de cebolla de seguridad, LLC

6.8.1 Estado del nodo
Almacenamiento InfluxDB utilizado
El campo Almacenamiento utilizado de InfluxDB muestra el total de gigabytes utilizados por InfluxDB para almacenar los datos de métricas actuales e históricos recopilados de todos
nodos en la red.
Retención de PCAP
El campo Retención de PCAP muestra el número de días históricos de datos de captura de paquetes disponibles que los analistas pueden ver mediante el
Herramienta PCAP de la consola Security Onion.
Carga promedio
El campo Promedio de carga muestra los promedios de carga de 1 minuto, 5 minutos y 15 minutos para el nodo. Tenga en cuenta que en sistemas con un gran número de
Núcleos de CPU, este promedio puede ser igualmente alto. Por ejemplo, si un sistema tiene 128 núcleos, entonces una carga promedio de 128 generalmente indica que todos
128 núcleos están trabajando a su máxima capacidad. Superar ese número puede indicar que algunos núcleos tienen cuellos de botella debido a la espera en E/S.
Tamaño de la cola de Redis
El campo Tamaño de cola de Redis muestra la cantidad de eventos en cola en Redis esperando ser absorbidos en Elasticsearch. Si este número es
estable o decreciente, indica que el sistema puede mantenerse al día con el flujo de tráfico actual. Si este número aumenta continuamente, entonces puede
indican un problema con los tiempos de ingesta que tardan demasiado para la cantidad de eventos que se generan. Se esperan aumentos ocasionales
durante las ráfagas de tráfico, pero eventualmente debería comenzar a disminuir una vez que finalice el período de alto flujo de tráfico.
Tráfico entrante del monitor
El campo Tráfico de monitor entrante muestra el rendimiento de los bytes entrantes que llegan a la interfaz de monitoreo del sensor.
Tráfico de monitor eliminado
El campo Tráfico de monitor descartado muestra el rendimiento de los bytes entrantes destinados a la interfaz de monitoreo del sensor, pero que en su lugar son
caído, generalmente debido a una capacidad de red insuficiente.
Gestión de tráfico entrante
El campo Tráfico de gestión entrante muestra el rendimiento de los bytes entrantes destinados a la interfaz de gestión del nodo. este es el interno
interfaz que el nodo utiliza para comunicarse con otros nodos en Security Onion Grid.
Tráfico de gestión saliente
El campo Tráfico de gestión saliente muestra el rendimiento de los bytes salientes que se transmiten desde la interfaz de gestión del nodo. esto es
la interfaz interna que el nodo utiliza para comunicarse con otros nodos en Security Onion Grid.
Filtrar palabras clave
Los campos Filtrar palabras clave muestran la lista de palabras clave asociadas con este tipo de nodo. Estas palabras clave son útiles para filtrar
solo muestra nodos de un cierto tipo.
Descripción
El campo Descripción muestra la descripción opcional que puede haber ingresado durante la Configuración o establecido en Administración --> Configuración -->
sensoroni --> configuración --> nodo_descripción.
- 130/402 - Soluciones de cebolla de seguridad, LLC

6.8.2 Estado del contenedor
Iconos en la esquina inferior izquierda
Hay algunos íconos en la parte inferior izquierda de la sección Estado del nodo dependiendo del tipo de nodo que esté mirando:
• Al hacer clic en el primer ícono, accederá al panel de InfluxDB para ese nodo en particular, para ver tendencias y métricas de estado históricas.
• Si el nodo es un sensor de red, habrá un ícono adicional para enviar tráfico de prueba al sensor.
• Dependiendo del tipo de nodo, puede haber un ícono adicional para cargar su propio archivo PCAP o EVTX. Al hacer clic en este icono se obtiene un
subir formulario. Una vez que haya seleccionado un archivo e iniciado la carga, aparecerá un mensaje de estado. Los archivos PCAP cargados se
importados a través de so-import-pcap y los archivos EVTX se importan automáticamente a través de so-import-evtx. Una vez completada la importación, aparecerá un mensaje.
Aparecerá un mensaje que contiene un hipervínculo para ver los registros de la importación. Tenga en cuenta que la importación no se admite en nodos pesados. También tenga en cuenta que
Este método de importación está diseñado para archivos más pequeños. Si necesita importar archivos más grandes que el tamaño máximo de carga predeterminado, deberá
cambie el tamaño máximo de carga a través de la pantalla de Configuración o importe manualmente a través de so-import-pcap o so-import-evtx.
• El botón de reinicio permite reiniciar de forma remota un nodo de grid. Esto puede ser necesario cuando las actualizaciones programadas del sistema operativo/kernel se realizan automáticamente.
aplicado y requiere un reinicio para que surta efecto. Revise detenidamente las notas del cuadro de diálogo de confirmación antes de confirmar un reinicio. Reiniciando
un nodo administrador probablemente hará que la interfaz web de Security Onion Console deje de estar disponible temporalmente.
• Al hacer clic en el botón del signo de interrogación accederá a este documento de ayuda.
6.8.2 Estado del contenedor
Nota
Reiniciar un nodo puede tardar varios minutos hasta que todos los contenedores vuelvan a estar en ejecución.
Si algún contenedor muestra algo más que en ejecución, haga clic en el ícono de cruz al lado del nombre del contenedor. Esto abrirá la pantalla de búsqueda.
muestra registros específicos de ese contenedor y puede ayudar a determinar por qué el contenedor no se está ejecutando.
- 131/402 - Soluciones de cebolla de seguridad, LLC

6.8.3 Imágenes del aparato
6.8.3 Imágenes del aparato
Si un nodo se está ejecutando en un dispositivo oficial de Security Onion Solutions, la página Grid mostrará imágenes de la parte delantera y trasera del
aparato. Esto resulta útil para analizar las conversaciones sobre conectividad con el personal del centro de datos. Cuando no se utiliza la seguridad oficial
Los electrodomésticos Onion Solutions simplemente mostrarán un mensaje a tal efecto.
6.8.4 Otras páginas de cuadrícula
Nota
Puede administrar los miembros de Grid y la configuración de Grid en la sección Administración.
- 132/402 - Soluciones de cebolla de seguridad, LLC

6.9 Descargas
6.9 Descargas
Security Onion Console incluye una interfaz de Descargas que le permite descargar Elastic Agent para varios sistemas operativos.
Advertencia
Tenga en cuenta que las instalaciones de evaluación y las instalaciones de importación no admiten agentes elásticos remotos, por lo que en esos casos se muestran los enlaces para
Sólo con fines de demostración.
Nota
Al instalar Elastic Agent en sistemas remotos, asegúrese de permitir el acceso a la red a través del Firewall.
- 133/402 - Soluciones de cebolla de seguridad, LLC

6.10 Administración
6.10 Administración
Security Onion Console incluye una sección de Administración que le permite administrar Usuarios, Miembros de Grid, Configuración y
Clave de licencia.
6.10.1 Usuarios
La página Usuarios muestra todas las cuentas de usuario que se han creado para el grid.
La columna Nota permite a los administradores incluir una nota breve en la cuenta de un usuario.
La columna Función enumera las funciones asignadas al usuario según se define en la sección RBAC.
La columna Estado mostrará diferentes iconos según el estado de la cuenta:
• signo de exclamación naranja: cuenta habilitada pero aún no ha cambiado su contraseña y no tiene MFA habilitado
• ícono azul con escudo: cuenta habilitada con MFA habilitado
• sin ícono: cuenta habilitada y ha cambiado su contraseña pero no tiene MFA habilitado
• usuario gris con barra diagonal: cuenta bloqueada
Al pasar el cursor sobre el ícono en la columna Estado, también se mostrarán estos detalles.
6.10.2 Miembros de la red
La página Miembros de la red muestra los nodos que han intentado unirse a la red y si han sido aceptados o no en la red por un
administrador.
- 134/402 - Soluciones de cebolla de seguridad, LLC

6.10.3 Configuración
Los miembros no aceptados se muestran en el lado izquierdo y se dividen en tres secciones: Miembros pendientes, Miembros denegados y Rechazados.
Miembros. Cuando acepte a un miembro, se moverá al lado derecho debajo de Miembros aceptados.
Para los miembros aceptados, pueden hacer clic en el botón REVISAR para mostrar información adicional sobre el miembro de la red. Si desea eliminar el
miembro, luego puede hacer clic en el botón ELIMINAR y revisar la confirmación.
6.10.3 Configuración
La página Configuración le permite configurar varios componentes de su red.
- 135/402 - Soluciones de cebolla de seguridad, LLC

6.10.3 Configuración
Las opciones de configuración más comunes se muestran en los enlaces rápidos del lado derecho. En el lado izquierdo, haga clic en un componente en la vista de árbol
para profundizar en él y mostrar todas las configuraciones disponibles para ese componente. Luego puede hacer clic en una configuración para mostrar la configuración actual o modificarla si
necesario. Si comete un error, puede volver fácilmente al valor predeterminado. Si aparece un signo de interrogación azul en la página de configuración, haga clic en él
para ir a la documentación de ese componente.
Si no está seguro de a qué componente puede pertenecer una configuración en particular, use el filtro en la parte superior de la lista para buscar una configuración en particular. a la derecha
del campo Filtro hay botones que hacen lo siguiente:
• aplicar el filtro de búsqueda
• expandir todas las configuraciones
• colapsar todas las configuraciones
• mostrar la configuración que se ha modificado desde el valor predeterminado
• mostrar configuraciones que tienen un valor único especificado para uno o más nodos en la cuadrícula
Nota
Las claves que incluyen _x_ indican un valor de marcador de posición utilizado para representar un punto (.).
Algunas configuraciones se pueden aplicar en toda la cuadrícula o en nodos específicos. Aplicar una configuración a un nodo específico anulará la configuración de la cuadrícula.
Configuración avanzada
De forma predeterminada, la página Configuración excluye las configuraciones que la mayoría de los administradores de Grid no deben ajustar. Estos avanzados
La configuración puede causar pérdida de datos y otros problemas si se ajusta incorrectamente. Para ver la configuración avanzada, vaya a la barra de Opciones en la parte superior de la
y luego haga clic en el botón Mostrar configuración avanzada.
Habilitar la configuración avanzada dará como resultado tiempos de carga más prolongados al visualizar la pantalla de Configuración.
Advertencia
No se admite cambiar la configuración avanzada y podría requerir una reinstalación completa del clúster.
- 136/402 - Soluciones de cebolla de seguridad, LLC

6.10.3 Configuración
Configuraciones duplicadas
Algunas configuraciones se pueden duplicar para crear nuevas configuraciones más fácilmente. Si una configuración es elegible para duplicación, entonces tendrá un DUPLICADO
en el lado derecho de la página, siempre que la opción Mostrar configuración avanzada esté habilitada en la parte superior de la pantalla. Creando un duplicado
La configuración es un proceso de DOS PASOS.
1. Haga clic en el botón DUPLICAR, proporcione un nombre para la nueva configuración y luego haga clic en el botón CREAR CONFIGURACIÓN.
2. La nueva configuración se mostrará automáticamente en la pantalla de Configuración. En este punto aún no se ha guardado en el servidor. El valor de la configuración.
debe modificarse explícitamente para conservar esta nueva configuración. Una vez que se haya modificado el valor, haga clic en el botón de marca de verificación verde para guardarlo.
Nota
Las configuraciones duplicadas no conservan el comportamiento completo de su configuración original. Por ejemplo, si la configuración original solo permitía valores CIDR, esta nueva
La configuración no tendrá las mismas protecciones en vistas posteriores en la pantalla de Configuración. Además, las configuraciones duplicadas se marcan como avanzadas.
ajustes. Para ver la nueva configuración más adelante, la opción Mostrar configuración avanzada debe estar habilitada en Opciones de configuración en
la parte superior de la pantalla de Configuración. Por último, tenga en cuenta que las configuraciones duplicadas no se pueden eliminar ni cambiar de nombre a través de la interfaz de usuario de SOC.
- 137/402 - Soluciones de cebolla de seguridad, LLC

6.10.4 Clave de licencia
6.10.4 Clave de licencia
La pantalla Clave de licencia le permite agregar una clave de licencia para Security Onion Pro. Una vez que haya agregado una clave de licencia, la pantalla mostrará detalles
sobre su clave de licencia.
- 138/402 - Soluciones de cebolla de seguridad, LLC

6.11 Kibana
6.11 Kibana
Security Onion Console incluye un enlace en la barra lateral que lo lleva a Kibana.
6.11.1 Autenticación
Inicie sesión en Kibana con el mismo nombre de usuario y contraseña que utiliza para SOC.
Puede agregar nuevas cuentas de usuario tanto a Kibana como a SOC al mismo tiempo, como se muestra en la sección Agregar cuentas.
Advertencia
Si crea cuentas directamente en Kibana (en lugar de en SOC), esas cuentas NO podrán iniciar sesión en SOC.
6.11.2 Paneles de Kibana
Hemos incluido un conjunto simple de paneles en Kibana. Estos paneles de Kibana no son tan completos como los de los paneles SOC.
Una vez que inicie sesión en Kibana, debe comenzar en el panel de inicio de Security Onion. Observe que la visualización en la parte superior izquierda está etiquetada
Cebolla de seguridad - Navegación. Este panel de navegación contiene enlaces a otros paneles y cambiará según el panel
estás viendo actualmente. Por ejemplo, cuando esté en el panel de inicio de Security Onion y haga clic en el enlace Alerta, irá a la
Security Onion: el panel de alertas y el panel de navegación contendrán enlaces a paneles de alerta más específicos para Suricata. cuando
Cuando haya terminado de ver las alertas, puede hacer clic en el enlace Inicio en el panel de navegación para volver al panel principal de Security Onion - Inicio.
Si alguna vez necesita recargar los paneles de Kibana, puede ejecutar el siguiente comando en su administrador:
sudo so-kibana-config-carga
Si eso no resuelve el problema, es posible que deba ejecutar lo siguiente:
sudo salt-call state.apply Kibana.so_savedobjects_defaults -l info queue=True
Si intenta modificar un panel de Kibana predeterminado, su cambio se sobrescribirá. En lugar de modificar, copie el panel deseado y edítelo
la copia. También puedes considerar configurar Kibana Spaces, ya que esto te permitirá realizar los cambios que quieras sin ellos.
siendo sobrescrito. Esto incluye no solo paneles sino también ciertas configuraciones de Kibana. Puede leer más sobre Kibana Spaces en https://
www.elastic.co/guide/en/kibana/current/xpack-spaces.html.
6.11.3 Resultados de la búsqueda
En Kibana, los resultados de búsqueda se limitan a los primeros 100 resultados de una consulta en particular. Si no cree que esto sea adecuado después de reducir su
búsqueda, puede ajustar el valor de discover:sampleSize en Kibana navegando a Stack Management --> Configuración avanzada y
cambiando el valor. Quizás sea mejor cambiar este valor de forma incremental para ver cómo afecta el rendimiento de su implementación.
6.11.4 Marcas de tiempo
De forma predeterminada, Kibana mostrará marcas de tiempo en la zona horaria de su navegador local. Si prefiere marcas de tiempo en UTC, puede ir a
Gestión --> Configuración avanzada y establezca dateFormat:tz en UTC.
6.11.5 Configuración
La mayoría de los ajustes de configuración de Kibana se encuentran en el propio Kibana. Sin embargo, los ajustes de configuración que tradicionalmente se establecerían en Kibana
El archivo de configuración se puede configurar yendo a Administración --> Configuración --> Kibana.
- 139/402 - Soluciones de cebolla de seguridad, LLC

6.11.6 Registro de diagnóstico
6.11.6 Registro de diagnóstico
Kibana inicia sesión en /opt/so/log/kibana/kibana.log. Dependiendo de lo que esté buscando, es posible que también necesite consultar los registros de Docker para
contenedor:
sudo docker registra so-kibana
Si intenta acceder a Kibana y dice que el servidor Kibana aún no está listo, incluso después de esperar unos minutos hasta que se inicialice por completo, verifique
/opt/so/log/kibana/kibana.log. Es posible que vea algo como:
Otra instancia de Kibana parece estar migrando el índice. Esperando a que se complete esa migración. Si ninguna otra instancia de Kibana está intentando
migraciones, puede superar este mensaje eliminando el índice .kibana_6 y reiniciando Kibana
Si ese es el caso, puede hacer lo siguiente (reemplazando .kibana_6 con el nombre de índice real que se mencionó en el registro):
curl -k -XDELETE https://localhost:9200/.kibana_6
sudo so-kibana-restart
Si luego puede iniciar sesión en Kibana pero sus paneles no se ven bien, puede recargarlos de la siguiente manera:
entonces-kibana-config-carga
6.11.7 Funciones
Puede habilitar o deshabilitar funciones específicas haciendo clic en el menú principal en la esquina superior izquierda, luego haciendo clic en Administración de pila, luego haga clic en
Espacios y luego haga clic en Predeterminado. Para obtener más información, consulte https://www.elastic.co/guide/en/kibana/current/xpack-spaces.html#spaces-
control-función-visibilidad.
- 140/402 - Soluciones de cebolla de seguridad, LLC

6.11.8 Más información
6.11.8 Más información
Nota
Para obtener más información sobre Kibana, consulte https://www.elastic.co/kibana.
- 141/402 - Soluciones de cebolla de seguridad, LLC

6.12 Flota elástica
6.12 Flota elástica
Security Onion Console incluye un enlace en la barra lateral que lo lleva a la página Fleet dentro de Kibana.
Elastic Fleet está preconfigurado durante la configuración de Security Onion. Si necesita realizar cambios en la configuración, puede hacerlo a través de la página Flota
en Kibana como se detalla a continuación.
La página Flota tiene varias pestañas en la parte superior: Agentes, Políticas de agentes, Tokens de inscripción, Tokens de desinstalación, Flujos de datos y Configuración. cada uno
de estas pestañas se describe a continuación.
6.12.1 Agentes
La pestaña Agentes muestra los agentes Elastic registrados.
Para ver los detalles del agente, haga clic en el nombre del anfitrión.
Para asignar el agente a una nueva política, cancelar su inscripción, actualizar el agente o realizar otras acciones, haga clic en el menú Acciones en el lado derecho de la
listado de agentes y seleccione la opción adecuada.
De forma predeterminada, Elastic Agent se instala en cada nodo de Security Onion Grid. Como resultado, todos los agentes del nodo Grid quedarán inscritos en los nodos so-grid.
política del agente.
Advertencia
No recomendamos eliminar la configuración de políticas para los agentes del nodo Security Onion Grid.
Agregar agentes
Para agregar un nuevo agente a su implementación, consulte la sección Agente elástico.
Agentes de actualización
Fleet comprueba automáticamente si los agentes tienen la última versión. De lo contrario, los agentes mostrarán Actualización disponible. Si desea actualizar
un agente, haga clic en el menú Acciones en el lado derecho y seleccione la opción Actualizar agente. Luego tendrás la oportunidad de seleccionar qué
versión a actualizar. Elija el número de versión que coincida con la versión de la pila elástica que está ejecutando actualmente. Para
Por ejemplo, si actualmente está ejecutando Elastic 8.18.4, debe seleccionar la versión del agente 8.18.4.
Advertencia
Si intenta actualizar a una versión del agente que sea más reciente que la versión de su pila Elastic, es posible que se produzcan errores. Por ejemplo, si usted
Si actualmente ejecuta Elastic 8.18.4 e intenta actualizar a la versión del agente 8.19.0 o 9.1.0, es posible que se produzcan errores.
Agentes de seguimiento
El estado del agente se puede monitorear en Elastic Fleet en la pestaña Agentes; sin embargo, es posible que desee generar alertas cuando un agente informe un
estado degradado o fuera de línea. A través de Administración --> Configuración --> administrador -> agente_monitoring puede habilitar un script que periódicamente
encuesta Flota Elástica. Los agentes en estado fuera de línea o degradado durante más tiempo que el umbral configurado (el valor predeterminado es 5 h) generarán una alerta en el
Interfaz de alertas del SOC.
Para obtener un control más granular sobre qué agentes generan una alerta, puede aprovechar las 'etiquetas' de flota para etiquetar a esos agentes. Luego en Administración -->
Configuración --> administrador -> agente_monitoring -> configuración -> custom_kquery puede ingresar una búsqueda kql como etiquetas: crítico. Entonces solo aquellos
Los agentes etiquetados como "críticos" generarían una alerta.
Para obtener más información sobre las etiquetas de Elastic Fleet, consulte https://www.elastic.co/docs/reference/fleet/filter-agent-list-by-tags#add-tags-in-fleet.
- 142/402 - Soluciones de cebolla de seguridad, LLC

6.12.2 Políticas de agentes
consejo
Los usuarios de Security Onion Pro pueden configurar notificaciones externas.
6.12.2 Políticas de agentes
Las políticas de los agentes dictan qué datos cada agente ingerirá y reenviará a Elasticsearch. Esto podría realizarse mediante el uso de un HTTP, un archivo de registro o
Entrada basada en TCP.
Los componentes individuales dentro de cada política de agente se denominan integraciones (denominadas políticas de paquete en el nivel API) y se refieren a un
entradas y configuraciones específicas pertinentes a una fuente de datos.
Por ejemplo, la política del agente so-grid-nodes se compone de las siguientes integraciones:
• elasticsearch-logs (integración de Elasticsearch)
• import-evtx-logs (integración de registros personalizados)
• import-suricata-logs (integración de registros personalizados)
• import-zeek-logs (integración de registros personalizados)
• kratos-logs (integración de registros personalizados)
• osquery-grid-nodes (integración de Osquery Manager)
• redis-logs (integración de Redis)
• strelka-logs (integración de registros personalizados)
• suricata-logs (integración de registros personalizados)
• syslog-tcp-514 (integración de registros personalizados)
• syslog-udp-514 (integración de registros personalizados)
• system-grid-nodes (integración del sistema)
• zeek-logs (integración de registros personalizados)
6.12.3 Políticas de agente: puntos finales iniciales
Los instaladores de agentes descargados desde Descargas se implementan utilizando la Política de agente inicial de los endpoints. Esta política incluye el elástico
Integraciones de Defender, Osquery Manager, sistema y Windows.
- 143/402 - Soluciones de cebolla de seguridad, LLC

6.12.3 Políticas de agente: puntos finales iniciales
puntos finales de defensa elástica (integración de Elastic Defend)
La integración de Elastic Defend tiene funciones gratuitas y de pago. De forma predeterminada, solo están habilitadas las siguientes funciones gratuitas:
• Colección de eventos: Windows
• Acceso a credenciales
• DLL y carga de controladores
• DNS
• Archivo
• Red
• Proceso
• Registro
• Seguridad
• Colección de eventos: macOS
• DNS
• Archivo
• Proceso
• Red
• Colección de eventos: Linux
• Archivo
• Red
• Proceso
Osquery-endpoints (integración de Osquery Manager)
La integración de Osquery Manager ejecuta Osquery como un demonio en el punto final y hace que el punto final esté disponible para Live o Scheduled.
consultas a través de la interfaz del administrador de Osquery en Kibana.
puntos finales del sistema (integración del sistema)
La integración del sistema recopila los siguientes registros del punto final, cuando corresponda:
• Registros de autenticación del sistema
• /var/log/auth.log*
• /var/log/secure*
• Registros de syslog
• /var/log/mensajes*
• /var/log/syslog*
• /var/log/sistema*
• Registro de eventos de Windows: canal de aplicación
• Registro de eventos de Windows: canal de seguridad
• Registro de eventos de Windows: canal del sistema
- 144/402 - Soluciones de cebolla de seguridad, LLC

6.12.4 Fichas de inscripción
puntos finales de Windows (integración de Windows)
La integración de Windows recopila los siguientes registros del punto final, cuando corresponda:
• Registro de eventos de Windows:
• Canal ForwardedEvents
• Canal de Windows Powershell
• Microsoft-Windows-Powershell/canal operativo
• Microsoft-Windows-Sysmon/canal operativo
6.12.4 Fichas de inscripción
Un token de inscripción permite a un agente inscribirse en Fleet, suscribirse a una política de agente particular y enviar datos.
Cada política de agente suele utilizar su propio token de inscripción. Se recomienda NO cambiar estos tokens, especialmente aquellos
generado por las políticas predeterminadas del agente Security Onion.
6.12.5 Flujos de datos
Los datos recopilados por Elastic Agent se envían a un flujo de datos de forma predeterminada. Esto permite categorizar y gestionar los datos de manera eficiente en todo un
variedad de conjuntos de datos. Esta sección dentro de la interfaz de usuario de Fleet permite una revisión rápida de los flujos de datos generados por los datos de Elastic Agent.
6.12.6 Configuración
La sección proporciona detalles como:
• Hosts de servidores de flota en su implementación
• Salidas configuradas
• especifica dónde se enviarán los datos
• esto debería incluir Elasticseach para el servidor Fleet y Logstash para Elastic Agent
• Método en el que se descargarán los binarios del agente
• este será un repositorio de artefactos local si se ejecuta una implementación con espacio aéreo
Advertencia
NO recomendamos cambiar estas configuraciones, ya que las administra Security Onion.
Si desea un control más detallado sobre a qué servidor de flota enviará registros un agente, existen dos opciones:
• La primera opción es utilizar reglas de firewall para permitir sólo ciertos agentes. Suponga que tiene dos nodos de servidor de flota, uno en 192.168.55.25 y
el otro al 192.168.58.25. Si desea que sus puntos finales en la subred 192.168.58.0/24 solo se conecten al servidor Fleet en 192.168.58.25,
agregaría reglas de firewall personalizadas a través de Administración --> Configuración --> firewall --> grupos de host --> elastic_agent_endpoint. Seleccione el
192.168.58.25 Nodo de flota y agregue 192.168.58.0/24. Los puntos finales en esa subred aún intentarán conectarse al nodo del servidor de flota en
192.168.55.25, pero como no es accesible (no hay reglas de firewall que permitan la comunicación), se conectarán al nodo Fleet en
192.168.58.25.
• La segunda opción es comprar una licencia Elastic. Una licencia Elastic paga ofrece la posibilidad de personalizar diferentes Salidas por Agente
Política.
6.12.7 Integraciones
Elastic Fleet admite integraciones y puede leer más en la sección de integraciones de terceros.
- 145/402 - Soluciones de cebolla de seguridad, LLC

6.12.8 URL FQDN personalizada
6.12.8 URL FQDN personalizada
Puede agregar un FQDN personalizado para que los agentes se conecten (tanto para controlar el tráfico en el puerto TCP/8220 como para el tráfico de datos en el puerto TCP/5055) editando
la configuración de la siguiente manera.
Primero, vaya a Administración --> Configuración --> elasticfleet.
En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada. Luego, navega a elasticfleet --> config
--> servidor --> custom_fqdn y configure su FQDN personalizado. Dentro de 15 minutos, la cuadrícula aplicará estas nuevas configuraciones y deberías ver la nueva
Los FQDN aparecen en la configuración de Elastic Fleet. Los nuevos instaladores de agentes también se regenerarán para usar esta nueva configuración.
6.12.9 Más información
Nota
Para obtener más información sobre Fleet, consulte https://www.elastic.co/guide/en/kibana/current/fleet.html.
- 146/402 - Soluciones de cebolla de seguridad, LLC

6.13 Administrador de Osquery
6.13 Administrador de Osquery
Security Onion Console incluye un enlace en la barra lateral que lo lleva a la página de Osquery Manager dentro de Kibana.
6.13.1 Más información
Nota
Para obtener más información sobre Osquery Manager, consulte https://docs.elastic.co/en/integrations/osquery_manager.
- 147/402 - Soluciones de cebolla de seguridad, LLC

6.14 InflujoDB
6.14 InflujoDB
Security Onion Console incluye un enlace en la barra lateral que lo lleva a InfluxDB.
Desde https://github.com/influxdata/influxdb:
InfluxDB es una plataforma de series temporales de código abierto. Esto incluye API para almacenar y consultar datos, procesándolos en segundo plano para ETL.
o con fines de monitoreo y alerta, paneles de usuario, visualización y exploración de datos y más.
6.14.1 Autenticación
Inicie sesión en InfluxDB con el mismo nombre de usuario y contraseña que utiliza para SOC.
Si necesita restablecer su contraseña de InfluxDB, puede restablecer su contraseña SOC a través de la interfaz de administración que también actualizará su
Contraseña de InfluxDB.
6.14.2 Configuración
Puede configurar InfluxDB yendo a Administración --> Configuración --> influxdb.
Puede configurar Telegraf yendo a Administración --> Configuración --> telegraf.
- 148/402 - Soluciones de cebolla de seguridad, LLC

6.14.3 Más información
6.14.3 Más información
Nota
Para obtener más información sobre InfluxDB, consulte https://github.com/influxdata/influxdb.
- 149/402 - Soluciones de cebolla de seguridad, LLC

6.15 PostgreSQL
6.15 PostgreSQL
De https://www.postgresql.org/:
PostgreSQL es un potente sistema de base de datos relacional de objetos de código abierto con más de 35 años de desarrollo activo que le ha valido un
sólida reputación por su confiabilidad, solidez de funciones y rendimiento.
Security Onion utiliza PostgreSQL como su plataforma de datos central, ejecutándose en nodos administradores. Respalda el almacén de conversaciones Onion AI y
recibe métricas de Telegraf junto con InfluxDB.
6.15.1 Almacenamiento
• Datos: /nsm/postgres/
• Configuración: /opt/so/conf/postgres/
• Secretos (0600 montados en el contenedor): /opt/so/conf/postgres/secrets/
• Registros: /opt/so/log/postgres/
Advertencia
No modifique manualmente los archivos en /nsm/postgres/ ya que esto podría dañar la base de datos.
6.15.2 Autenticación
PostgreSQL utiliza un modelo de autenticación de tres niveles:
• superusuario de postgres: sólo operaciones administrativas (inicio de esquema, gestión de roles durante la actualización). La contraseña se genera automáticamente.
y entregado al contenedor a través del archivo montado en /run/secrets/postgres_password usando POSTGRES_PASSWORD_FILE.
• Usuario de la aplicación so_postgres: utilizada por la plataforma Security Onion (la tienda del asistente SOC) para el acceso diario a la base de datos. el
La contraseña se genera automáticamente y se entrega a través de /run/secrets/so_postgres_pass usando SO_POSTGRES_PASS_FILE.
• so_telegraf_<minion> usuarios por minion: una función de inicio de sesión por minion de la red, todos los miembros del grupo so_telegraf compartido. cada siervo
solo ve su propia credencial a través de su archivo pilar por minion.
Salt genera y administra automáticamente todas las credenciales. Las contraseñas se entregan al contenedor como archivos montados en lugar de texto sin formato.
variables de entorno para que no aparezcan en la salida de Docker Inspect.
6.15.3 Cifrado
Todas las conexiones TCP a PostgreSQL se cifran con TLS mediante un certificado firmado por Security Onion CA en /etc/pki/
postgres.crt / /etc/pki/postgres.key.
pg_hba.conf sólo permite:
• Conexiones locales de socket Unix (utilizadas por los propios scripts de administración del contenedor).
• Conexiones TCP envueltas en TLS hostssl con autenticación SCRAM-SHA-256.
Las conexiones TCP de host de texto sin formato se rechazan, por lo que un cliente que utilice sslmode=disable no puede establecer una sesión incluso si tiene credenciales válidas.
6.15.4 Configuración
Puede configurar PostgreSQL yendo a Administración --> Configuración --> postgres.
- 150/402 - Soluciones de cebolla de seguridad, LLC

6.15.5 Cortafuegos
Configuraciones comúnmente ajustadas:
Configuración predeterminada Descripción
max_connections 100 Máximo de conexiones PostgreSQL simultáneas.
Shared_buffers 256 MB de memoria para el caché del búfer compartido. Aumentar esto mejora el caché de lectura
tasa de aciertos a costa de la RAM.
log_min_messages advertencia Gravedad mínima escrita en el registro de PostgreSQL.
telegraf.retention_days 14 días de métricas de Telegraf retenidas en la base de datos so_telegraf. mayor
pg_partman elimina las particiones cada hora.
Las configuraciones de infraestructura (rutas TLS, hba_file, listening_addresses, extensiones precargadas, etc.) están marcadas como avanzadas y están administradas por Salt.
y no debe cambiarse durante el funcionamiento normal.
Selector de salida de telégrafo
Los backends en los que Telegraf escribe métricas se configuran en Administración --> Configuración --> Telegraf --> salida:
Comportamiento de valor
INFLUXDB Telegraf escribe solo en InfluxDB.
POSTGRES Telegraf escribe solo en PostgreSQL (base de datos so_telegraf).
AMBOS Telegraf escribe dualmente en ambos (útil durante la validación de la migración).
6.15.5 Cortafuegos
Solo se puede acceder a PostgreSQL desde el propio administrador y, dentro del puente acoplable, desde los pares del contenedor. El acceso es impuesto por el
Firewall Security Onion a través de la cadena DOCKER-USER iptables: postgres (5432) se otorga solo al administrador, managerhype, managersearch,
eval y grupos de hosts independientes. Los sensores, nodos pesados, nodos de búsqueda, receptores y otras funciones no pueden llegar al puerto.
6.15.6 Comandos de gestión
Security Onion proporciona herramientas de línea de comandos para administrar PostgreSQL. Estas herramientas ejecutan psql dentro del contenedor Docker para que PostgreSQL
No es necesario instalar los archivos binarios del cliente en el host.
Carcasa interactiva
Abra una sesión psql interactiva como superusuario:
sudo so-postgres-manage shell
Ejecutar SQL
Ejecute un comando SQL directamente:
sudo so-postgres-manage sql "SELECCIONAR versión();"
Ejecutar archivo SQL
Ejecute un script SQL:
sudo so-postgres-manage sqlfile /ruta/a/script.sql
Listar bases de datos
sudo so-postgres-manage dblist
Listar funciones de base de datos
sudo so-postgres-manage lista de usuarios
- 151/402 - Soluciones de cebolla de seguridad, LLC

6.15.7 Métricas de Telegraf
Ciclo de vida del contenedor
sudo so-postgres-inicio
sudo so-postgres-parar
sudo so-postgres-restart
Instantánea de métricas de cuadrícula
so-stats-show imprime las métricas de carga, memoria, disco y CPU más recientes para cada host que informa al backend de Telegraf PostgreSQL.
Útil para verificar que Telegraf esté obteniendo métricas correctamente antes de consumirlas en un panel.
sudo so-stats-show # todos los hosts
sudo so-stats-show <nombre de host> # un solo host
Esta herramienta requiere que telegraf.output sea POSTGRES o AMBOS.
6.15.7 Métricas de Telegraf
Cuando telegraf.output es POSTGRES o AMBOS, cada grid minion escribe sus métricas directamente en una base de datos so_telegraf compartida dentro
PostgreSQL utiliza su propia función de inicio de sesión por minion.
• Las tablas viven en el esquema de Telegraf y pg_partman las divide diariamente.
• La retención está impulsada por el valor de configuración postgres.telegraf.retention_days; pg_partman elimina particiones caducadas cada hora a través de
página_cron.
• Las etiquetas y los campos se almacenan como jsonb, por lo que el límite de columnas fijas por tabla (1600) no limita las entradas de alta cardinalidad.
• Cada conexión TCP se verifica mediante TLS con la CA Security Onion (sslmode=verify-full).
Las credenciales por minion se aprovisionan automáticamente cuando se acepta la clave de un minion: un reactor de Salt crea la función de la base de datos y escribe
la contraseña en el archivo pilar del propio minion. No se requiere intervención del administrador.
6.15.8 Extensiones
Las siguientes extensiones de PostgreSQL están instaladas y disponibles:
Descripción de la extensión
pgvector Búsqueda de similitud de vectores para incrustaciones de AI/ML.
pg_cron Programación de trabajos dentro de PostgreSQL. Impulsa el mantenimiento de pg_partman.
pg_partman Partición de tablas automatizada basada en el tiempo. Impulsa la retención de métricas de Telegraf.
pgcrypto Funciones criptográficas para cifrado a nivel de columna.
6.15.9 Copia de seguridad
Se realiza una copia de seguridad automática de PostgreSQL diariamente a las 00:05. La copia de seguridad utiliza pg_dumpall para capturar todas las bases de datos y roles, comprimidos con
gzip y se almacenó en modo 0600 en /nsm/backup/so-postgres-backup-YYYY_MM_DD.sql.gz con una retención de 7 días.
Consulte la página de Copia de seguridad para obtener más información.
Para crear manualmente una copia de seguridad:
docker exec so-postgres pg_dumpall -U postgres | gzip > /nsm/backup/so-postgres-manual-backup.sql.gz
Para restaurar desde una copia de seguridad:
zcat /nsm/backup/so-postgres-backup-2026_04_21.sql.gz | docker exec -i so-postgres psql -U postgres
- 152/402 - Soluciones de cebolla de seguridad, LLC

6.15.10 Registro de diagnóstico
6.15.10 Registro de diagnóstico
Los registros del servidor PostgreSQL llegan a /opt/so/log/postgres/. Para problemas a nivel de contenedor (problemas de inicio, OOM, fallas), consulte también Docker
registros:
sudo docker registra so-postgres
6.15.11 Más información
Nota
Para obtener más información sobre PostgreSQL, consulte https://www.postgresql.org/docs/.
- 153/402 - Soluciones de cebolla de seguridad, LLC

6.16 CiberChef
6.16 CiberChef
Security Onion Console incluye un enlace en la barra lateral que lo lleva a CyberChef.
De https://github.com/gchq/CyberChef:
La navaja suiza cibernética
CyberChef es una aplicación web sencilla e intuitiva para realizar todo tipo de operaciones "cibernéticas" dentro de un navegador web. Estas operaciones incluyen
codificación simple como XOR o Base64, cifrado más complejo como AES, DES y Blowfish, creación de volcados binarios y hexadecimal, compresión
y descompresión de datos, cálculo de hashes y sumas de verificación, análisis de IPv6 y X.509, cambio de codificaciones de caracteres y mucho más.
La herramienta está diseñada para permitir a los analistas técnicos y no técnicos manipular datos de formas complejas sin tener que lidiar con
herramientas o algoritmos complejos.
Hay cuatro áreas principales en CyberChef:
1. El cuadro de entrada en la parte superior derecha, donde puede pegar, escribir o arrastrar el texto o archivo que desea operar.
2. El cuadro de salida en la parte inferior derecha, donde se mostrará el resultado de su procesamiento.
3. La lista de operaciones en el extremo izquierdo, donde puede encontrar todas las operaciones que CyberChef es capaz de realizar en listas categorizadas, o por
buscando.
4. El área de recetas en el medio, donde puede arrastrar las operaciones que desea utilizar y especificar argumentos y opciones.
6.16.1 Acceso
Para acceder a CyberChef, inicie sesión en SOC y haga clic en el hipervínculo CyberChef.
Puede enviar texto resaltado desde PCAP a CyberChef. Cuando se abra la pestaña CyberChef, verá el texto resaltado tanto en la entrada
y el cuadro Salida.
Puede enviar todos los datos de paquetes visibles desde PCAP a CyberChef. Cuando se abra la pestaña CyberChef, aplicará automáticamente el archivo From Hexdump
receta para renderizar el volcado hexadecimal que se envió.
6.16.2 Extracción de archivos
Supongamos que está viendo una descarga de archivo HTTP interesante en PCAP y desea extraer el archivo usando CyberChef:
• Haga clic en el botón PCAP CyberChef y CyberChef se iniciará en una nueva pestaña. Luego mostrará el volcado hexadecimal en el cuadro de Entrada, automáticamente
aplique la receta Desde Hexdump y muestre la transcripción HTTP en el cuadro Salida.
• Es posible que desee aplicar una operación de la columna de la izquierda. Una opción es utilizar la operación Extraer archivos y, opcionalmente, especificar ciertos
tipos de archivos para extracción. Otra opción es eliminar los encabezados HTTP mediante la operación Eliminar encabezados HTTP.
• Si aparece una varita mágica en el cuadro Salida, entonces CyberChef ha detectado algunas operaciones aplicables y puede hacer clic en la varita mágica para
aplicar automáticamente esas operaciones. Por ejemplo, CyberChef podría aplicar automáticamente los encabezados Strip HTTP y luego procesar el archivo.
6.16.3 Más información
Nota
Para obtener más información sobre CyberChef, consulte https://github.com/gchq/CyberChef.
- 154/402 - Soluciones de cebolla de seguridad, LLC

6.17 Navegador ATT&CK
6.17 Navegador ATT&CK
Security Onion Console incluye un enlace en la barra lateral que lo lleva a ATT&CK Navigator.
De https://github.com/mitre-attack/attack-navigator:
El Navegador ATT&CK está diseñado para proporcionar navegación básica y anotaciones de matrices ATT&CK, algo que la gente ya está haciendo.
haciendo hoy en herramientas como Excel. Lo hemos diseñado para que sea simple y genérico: puedes usar el Navegador para visualizar tu cobertura defensiva,
la planificación de tu equipo rojo/azul, la frecuencia de las técnicas detectadas o cualquier otra cosa que quieras hacer. Al Navegante no le importa, simplemente
le permite manipular las celdas de la matriz (codificación de colores, agregar un comentario, asignar un valor numérico, etc.). Pensamos tener un
Una herramienta simple que todos podrían usar para visualizar la matriz ayudaría a facilitar el uso de ATT&CK.
La característica principal del Navegador es la capacidad de los usuarios de definir capas (vistas personalizadas de la base de conocimientos de ATT&CK), p. mostrando
solo aquellas técnicas para una plataforma en particular o técnicas de resaltado que se sabe que utiliza un adversario específico. Las capas pueden ser
creado de forma interactiva dentro del Navegador o generado mediante programación y luego visualizado a través del Navegador.
6.17.1 Acceso
Para acceder a Navigator, inicie sesión en SOC y luego haga clic en el hipervínculo de Navigator en el lado izquierdo.
6.17.2 Configuración
Navigator lee su configuración desde /opt/so/conf/navigator/. Sin embargo, tenga en cuenta que si realiza algún cambio aquí,
puede sobrescribirse ya que la configuración se administra con Salt.
6.17.3 Más información
Nota
Para obtener más información sobre ATT&CK Navigator, consulte: https://github.com/mitre-attack/attack-navigator
- 155/402 - Soluciones de cebolla de seguridad, LLC

7. Escritorio cebolla de seguridad
7. Escritorio cebolla de seguridad
7.1 Descripción general de Security Onion Desktop
Es posible que los analistas de tiempo completo quieran utilizar un escritorio Security Onion dedicado. Esto le permite investigar pcaps, malware y otros posibles
artefactos maliciosos sin afectar su implementación de Security Onion o su entorno de escritorio habitual.
Nota
Security Onion Desktop solo es compatible con Oracle Linux 9, por lo que necesitará usar nuestra imagen ISO (recomendada) o una instalación de red en la parte superior
de Oracle Linux 9 (no compatible).
Security Onion Desktop consta de un entorno de escritorio completo que incluye Chromium, NetworkMiner, Wireshark y otras herramientas de análisis.
Instalación
Hay algunas formas diferentes de instalar Security Onion Desktop:
• Nuestra imagen ISO incluye una opción de menú de inicio para instalaciones de escritorio que particionará su disco de manera adecuada y realizará inmediatamente una
Instalación de escritorio. El tamaño mínimo del disco es de 50 GB.
• El comando so-desktop-install es totalmente independiente del proceso de instalación estándar, por lo que puede ejecutarlo antes o después de la instalación o no ejecutarlo.
configuración si lo único que realmente desea es el escritorio del analista.
• Si está realizando una instalación de red en Oracle Linux 9 (NO usando nuestra imagen ISO), en nuestro asistente de configuración normal, puede elegir OTRO
y luego elija ANALISTA. Tenga en cuenta que las instalaciones de red en general no son compatibles.
Nota
Dependiendo de cómo realice la instalación, es posible que sea necesario un ciclo completo de Salt antes de que todos los componentes del escritorio estén instalados y listos para su uso.
Unirse a la red
Opcionalmente, puedes unir tu instalación de escritorio a tu grid. Esto le permite extraer actualizaciones de la red y confiar automáticamente en la red.
Certificado HTTPS. También actualiza el firewall del administrador para permitir que se conecte la instalación de escritorio. Los nodos del escritorio se muestran en la página Grid
junto con los otros nodos de Grid.
Si elige no unir su instalación de escritorio a su red, es posible que deba permitir el tráfico a través del firewall basado en host yendo
a Administración --> Configuración --> firewall --> grupos de hosts --> analista.
- 156/402 - Soluciones de cebolla de seguridad, LLC

7.1 Descripción general de Security Onion Desktop
Deshabilitar
El escritorio del analista se controla a través del pilar Salt. Si necesita deshabilitar el entorno de Security Onion Desktop, busque la configuración de la estación de trabajo
en su pilar de Salt y cambie habilitado: verdadero a habilitado: falso:
estación de trabajo:
interfaz gráfica de usuario:
habilitado: falso
- 157/402 - Soluciones de cebolla de seguridad, LLC

7.2 Cromo
7.2 Cromo
Chromium es el navegador web incluido en nuestra instalación de Security Onion Desktop.
7.2.1 Más información
Nota
Para obtener más información sobre Chromium, consulte: https://www.chromium.org/Home/
- 158/402 - Soluciones de cebolla de seguridad, LLC

7.3 Minero de red
7.3 Minero de red
De https://www.netresec.com/?page=NetworkMiner:
NetworkMiner es una herramienta de análisis forense de red (NFAT) de código abierto para Windows (pero también funciona en Linux/Mac OS X/FreeBSD).
NetworkMiner se puede utilizar como una herramienta pasiva de captura de paquetes/rastreador de red para detectar sistemas operativos, sesiones, nombres de host,
abrir puertos, etc. sin poner tráfico en la red. NetworkMiner también puede analizar archivos PCAP para análisis fuera de línea y regenerarlos/
volver a ensamblar archivos transmitidos y certificados a partir de archivos PCAP.
NetworkMiner facilita la realización de análisis de tráfico de red (NTA) avanzado al proporcionar artefactos extraídos en un usuario intuitivo
interfaz. La forma en que se presentan los datos no sólo simplifica el análisis, sino que también ahorra tiempo valioso al analista o al forense.
investigador.
7.3.1 Uso
NetworkMiner es parte de nuestra instalación de Security Onion Desktop.
7.3.2 Extracción de archivos
Supongamos que está viendo una descarga de archivo HTTP interesante en PCAP y desea extraer el archivo. Haga clic en el botón de descarga de PCAP y luego
Abra el archivo PCAP con NetworkMiner. NetworkMiner intentará automáticamente detectar y extraer cualquier archivo transferido. Puedes acceder
estos archivos extraídos en la pestaña Archivos. Si algún archivo es imagen, se puede ver en la pestaña Imágenes.
7.3.3 Más información
Nota
Para obtener más información sobre NetworkMiner, consulte: https://www.netresec.com/?page=NetworkMiner
- 159/402 - Soluciones de cebolla de seguridad, LLC

7.4 Uso de cables
7.4 Uso de cables
De https://www.wireshark.org/:
Wireshark es el analizador de protocolos de red más importante y ampliamente utilizado del mundo. Le permite ver lo que está sucediendo en su red en un
nivel microscópico y es el estándar de facto (y a menudo de jure) en muchas empresas comerciales y sin fines de lucro, gobiernos
agencias e instituciones educativas. El desarrollo de Wireshark prospera gracias a las contribuciones voluntarias de expertos en redes de todo el mundo.
todo el mundo y es la continuación de un proyecto iniciado por Gerald Combs en 1998.
7.4.1 Uso
Wireshark es parte de nuestra instalación de Security Onion Desktop.
7.4.2 Extracción de archivos
Supongamos que está viendo una descarga de archivo HTTP interesante en PCAP y desea extraer el archivo. Haga clic en el botón de descarga de PCAP y luego
Abra el archivo PCAP con Wireshark. Para extraer archivos del tráfico HTTP, haga clic en Archivo - Exportar objetos - HTTP. Luego seleccione el archivo(s) para guardar y
especifique dónde guardarlos.
7.4.3 Más información
Nota
Para obtener más información sobre Wireshark, consulte https://www.wireshark.org/.
- 160/402 - Soluciones de cebolla de seguridad, LLC

8. Visibilidad de la red
8. Visibilidad de la red
8.1 Descripción general de la visibilidad de la red
Cuando inicia sesión en Security Onion Console, puede ver alertas de Suricata o IDH, registros de metadatos de protocolo de Zeek o Suricata, archivos
registros de análisis de Strelka o captura de paquetes completos de Suricata. ¿Cómo se generan y almacenan esos datos? Esta sección cubre los diversos
procesos que utiliza Security Onion para analizar y registrar el tráfico de red.
- 161/402 - Soluciones de cebolla de seguridad, LLC

8.2 PAQUETE AF
8.2 PAQUETE AF
Security Onion utiliza AF-PACKET para recopilar tráfico de las interfaces de red. AF-PACKET está integrado en el kernel de Linux e incluye distribución en abanico
capacidades que le permiten actuar como un equilibrador de carga basado en flujo. Esto significa, por ejemplo, que si configura Suricata para 4 subprocesos AF-PACKET, entonces
cada hilo recibiría aproximadamente el 25% del tráfico total que ve AF-PACKET.
Advertencia
Si intenta probar la distribución de AF-PACKET utilizando tcpreplay localmente, tenga en cuenta que el equilibrio de carga no funcionará correctamente y todo (o la mayor parte) del tráfico se bloqueará.
manejado por el primer trabajador en el clúster AF-PACKET. Si necesita probar correctamente el equilibrio de carga de AF-PACKET, puede ejecutar tcpreplay en otro
máquina conectada a su máquina AF-PACKET.
Los siguientes procesos utilizan AF-PACKET para la recopilación de tráfico:
• Suricata
• Zeek
8.2.1 Más información
Nota
Para obtener más información sobre AF-PACKET, consulte: https://www.kernel.org/doc/Documentation/networking/packet_mmap.txt
- 162/402 - Soluciones de cebolla de seguridad, LLC

8.3 BPF
8.3 BPF
BPF significa filtro de paquetes Berkeley. De https://en.wikipedia.org/wiki/Berkeley_Packet_Filter:
BPF admite el filtrado de paquetes, lo que permite que un proceso de espacio de usuario proporcione un programa de filtrado que especifique qué paquetes desea recibir.
Por ejemplo, es posible que un proceso tcpdump desee recibir solo paquetes que inicien una conexión TCP. BPF devuelve sólo paquetes que pasan el
filtro que suministra el proceso. Esto evita copiar paquetes no deseados del kernel del sistema operativo al proceso, mejorando enormemente
rendimiento.
8.3.1 Configuración
Puede modificar su configuración de BPF yendo a Administración --> Configuración --> bpf. Puede aplicar la configuración BPF a Suricata o
Zeek. Si configura un BPF para Suricata, entonces puede aplicarse a alertas, metadatos y/o captura completa de paquetes.
Múltiples condiciones
Si su BPF contiene varias condiciones, puede unirlas con un y o lógico o.
A continuación se muestra un ejemplo de cómo unir condiciones con una lógica y:
no hospedar 192.168.1.2 y no hospedar 192.168.1.3
A continuación se muestra un ejemplo de cómo unir condiciones con una lógica o:
anfitrión 192.168.1.2 o anfitrión 192.168.1.3
VLAN
Si tiene tráfico que tiene etiquetas VLAN, puede crear un BPF de la siguiente manera:
<your filter> or (vlan and <your filter>)
- 163/402 - Soluciones de cebolla de seguridad, LLC

8.3.2 Más información
Tenga en cuenta que debe incluir su filtro en ambos lados de la etiqueta vlan.
Por ejemplo:
(no (host 192.168.1.2 o host 192.168.1.3 o host 192.168.1.4)) o (vlan y (no (host 192.168.1.2 o host 192.168.1.3 o host 192.168.1.4)))
Agregar comentarios
Para proporcionar más contexto a sus filtros, puede agregar comentarios. Por ejemplo:
# laboratorio-este
no hospedar 192.168.1.2 y no hospedar 192.168.1.3 &&
# laboratorio-oeste
no hospedar 192.168.1.4 o no hospedar 192.168.1.5 &&
# laboratorio central
no hospedar 192.168.1.6 o no hospedar 192.168.1.27
Solución de problemas de BPF mediante tcpdump
Si necesita solucionar problemas de BPF, puede usar tcpdump como se muestra en los siguientes artículos:
https://taosecurity.blogspot.com/2004/09/understanding-tcpdumps-d-option-have.html
https://taosecurity.blogspot.com/2004/12/understanding-tcpdumps-d-option-part-2.html
https://taosecurity.blogspot.com/2008/12/bpf-for-ip-or-vlan-traffic.html
8.3.2 Más información
Nota
Para obtener más información sobre BPF, consulte:
https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
https://biot.com/capstats/bpf.html
- 164/402 - Soluciones de cebolla de seguridad, LLC

8.4 Captura de paquetes completos
8.4 Captura de paquetes completos
Security Onion escribe el tráfico de red en el disco para capturar paquetes completos utilizando Suricata.
Suricata escribe archivos PCAP estándar que pueden copiarse a otro sistema y luego abrirse con cualquier herramienta libpcap estándar.
8.4.1 Análisis
Puede acceder a la captura completa de paquetes a través de la interfaz PCAP:
Las alertas, los paneles y la búsqueda le permiten pasar fácilmente a la interfaz PCAP.
8.4.2 Configuración
Puede configurar la captura de paquetes completos yendo a Administración --> Configuración --> Suricata --> config --> pcap.
- 165/402 - Soluciones de cebolla de seguridad, LLC

8.4.3 Etiquetas VLAN
PCAP condicional
De forma predeterminada, Suricata escribe todo el tráfico de la red en PCAP. Si desea limitar a Suricata a escribir PCAP únicamente cuando se cumplan ciertas condiciones,
puede ir a Administración --> Configuración --> Suricata -> config -> pcap -> condicional y cambiarlo a alertas o etiqueta:
• todos: captura todos los paquetes vistos por Suricata (predeterminado).
• alertas: Capture sólo paquetes asociados con una alerta NIDS.
• etiqueta: captura paquetes basándose en una regla etiquetada.
Opciones de configuración de PCAP
Aquí hay algunas otras opciones de configuración de PCAP que se pueden encontrar en Administración --> Configuración --> Suricata -> config -> pcap. algunos
Las configuraciones se consideran configuraciones avanzadas, por lo que solo las verá si habilita la opción Mostrar configuración avanzada.
• habilitado: haga clic en el control deslizante para habilitar o deshabilitar la captura de paquetes Suricata.
• compresión: establezca en ninguno para desactivar la compresión. Configúrelo en lz4 para habilitar la compresión lz4, pero tenga en cuenta que esto requiere más ciclos de CPU.
• lz4-level: nivel de compresión lz4 de archivos PCAP. Establezca en 0 para que no haya compresión. Establezca en 16 para una compresión máxima.
• maxsize: Tamaño máximo en GB para el uso total del disco de todos los archivos PCAP escritos por Suricata. Es posible que necesite ajustar este valor según su
espacio en disco y retención de PCAP deseada.
• tamaño de archivo: Tamaño máximo de archivo para archivos PCAP individuales escritos por Suricata. Aumentar este número podría mejorar el rendimiento de escritura en el
costo del tiempo de recuperación del PCAP.
• use-stream- Depth: establezca en no para ignorar la profundidad de la corriente y capturar todo el flujo. Establezca en sí para truncar el flujo según la secuencia
profundidad.
8.4.3 Etiquetas VLAN
Si el tráfico de su red tiene etiquetas VLAN, Suricata las registrará. Para obtener más información, consulte la sección Suricata.
- 166/402 - Soluciones de cebolla de seguridad, LLC

8.4.4 Registro de diagnóstico
8.4.4 Registro de diagnóstico
El registro de diagnóstico para Suricata se puede encontrar en /opt/so/log/suricata/suricata.log. Dependiendo de lo que estés buscando, también puedes
Necesito mirar los registros de Docker para el contenedor:
sudo docker logs so-suricata
- 167/402 - Soluciones de cebolla de seguridad, LLC

8.5 Suricata
8.5 Suricata
De https://suricata.io:
Suricata es un motor de detección de amenazas de red maduro, rápido y robusto, gratuito y de código abierto. Suricata inspecciona el tráfico de la red utilizando un
reglas y lenguaje de firma potentes y extensos, y tiene un potente soporte de secuencias de comandos Lua para la detección de amenazas complejas.
Las alertas de Suricata NIDS se pueden encontrar en Alertas, Paneles, Hunt y Kibana.
Aquí hay un ejemplo de alertas NIDS de Suricata en Alertas:
Si está habilitado, los metadatos de Suricata (registros de protocolo) se pueden encontrar en Dashboards, Hunt y Kibana.
8.5.1 ID de comunidad
Security Onion habilita el soporte integrado de Suricata para Community ID.
8.5.2 Etiquetas VLAN
Si el tráfico de su red tiene etiquetas VLAN, Suricata las registrará. Dashboards tiene un panel de VLAN que mostrará estos datos.
Si el tráfico de su red tiene etiquetas VLAN mixtas (etiquetas VLAN en una dirección pero no en la otra), es posible que deba hacer lo siguiente:
• Navegue a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• Navegue a Suricata > config > vlan > use-for-tracking y configúrelo en falso.
8.5.3 Configuración
Puede configurar Suricata yendo a Administración --> Configuración --> Suricata.
- 168/402 - Soluciones de cebolla de seguridad, LLC

8.5.4 INICIO_NET
Si desea configurar reglas NIDS, eche un vistazo a la interfaz de Detecciones.
8.5.4 INICIO_NET
La variable HOME_NET define las redes que se consideran redes domésticas (aquellas redes que estás monitoreando y defendiendo).
El valor predeterminado es el espacio de direcciones privado RFC1918 (10.0.0.0/8, 192.168.0.0/16 y 172.16.0.0/12). Puede modificar este valor predeterminado mediante
yendo a Administración --> Configuración --> Suricata --> config --> vars --> grupos de direcciones --> HOME_NET.
8.5.5 RED_EXTERNA
De forma predeterminada, EXTERNAL_NET está configurado en cualquiera (que incluye HOME_NET) para detectar movimiento lateral dentro de su entorno. Puedes modificar
este valor predeterminado yendo a Administración --> Configuración --> Suricata --> config --> vars --> grupos de direcciones --> EXTERNAL_NET.
8.5.6 Estadísticas
Para obtener estadísticas de Suricata, consulte Grid, InfluxDB y /opt/so/log/suricata/stats.log.
8.5.7 Rendimiento
Si Grid muestra que Suricata está experimentando una pérdida de paquetes, es posible que deba realizar una o más de las siguientes acciones:
• Ajustar el conjunto de reglas NIDS.
• Aplicar un BPF.
• Ajuste el máximo de paquetes pendientes en Administración --> Configuración --> Suricata --> config --> máximo de paquetes pendientes.
• Ajustar los trabajadores AF-PACKET en Administración --> Configuración --> Suricata --> config --> af-packet --> threads.
Nota
Para otras consideraciones de ajuste, consulte: https://suricata.readthedocs.io/en/latest/performance/tuning-considerations.html
- 169/402 - Soluciones de cebolla de seguridad, LLC

8.5.8 Metadatos
Si tiene varias CPU físicas, lo más probable es que desee fijar procesos de rastreo a una CPU en el mismo acceso a memoria no uniforme.
(NUMA) al que está vinculada su NIC de rastreo. Acceder a una CPU en el mismo dominio NUMA es más rápido que a través de un dominio NUMA.
Nota
Para obtener más información sobre cómo determinar dominios NUMA usando lscpu y lstopo, consulte: https://github.com/brokenscripts/cpu_pinning
8.5.8 Metadatos
De forma predeterminada, Security Onion utiliza Zeek para registrar metadatos de protocolo. Si no necesita toda la cobertura de protocolo que proporciona Zeek, entonces
Puede cambiar a los metadatos de Suricata para guardar algunos ciclos de CPU. Si elige hacer esto, estos son algunos de los tipos de metadatos que puede
Espere ver en Dashboards o Hunt:
• Conexiones
•DHCP
• DNS
• Archivos
•FTP
•HTTP
•SSL
Si luego descubre que algunos de esos metadatos son innecesarios, puede habilitar el conjunto de reglas SO_FILTERS para filtrar metadatos innecesarios.
Navegue a Administración --> Configuración --> SOC --> config --> servidor --> módulos --> suricataengine --> reglassetSources y habilite el
Conjunto de reglas SO_FILTERS.
Para cambiar el motor de metadatos de su grid de Zeek a Suricata, vaya a Administración --> Configuración --> global --> mdengine y cambie el
valor de Zeek a Suricata:
- 170/402 - Soluciones de cebolla de seguridad, LLC

8.5.9 Extracción de archivos
8.5.9 Extracción de archivos
Si elige Suricata para los metadatos, extraerá archivos del tráfico de la red y Strelka luego analizará esos archivos extraídos. el
El conjunto de reglas SO_EXTRACTIONS controla qué tipos de archivos se extraen y está habilitado de forma predeterminada cuando Suricata es el motor de metadatos. tu puedes
personalice la extracción de archivos modificando las reglas en este conjunto de reglas.
8.5.10 PCAP
Security Onion utiliza Suricata para la captura de paquetes completos. Para obtener más información, consulte la sección Captura completa de paquetes.
8.5.11 Registro de diagnóstico
Si necesita solucionar problemas de Suricata, consulte /opt/so/log/suricata/suricata.log. Dependiendo de lo que estés buscando, es posible que también necesites
para ver los registros de Docker para el contenedor:
sudo docker logs so-suricata
8.5.12 Pruebas
La primera y más sencilla forma de probar Suricata es acceder a http://testmynids.org/uid/index.html desde una máquina que esté siendo monitoreada por su
Implementación de Security Onion. Puedes hacerlo a través de la línea de comando usando curl:
rizo testmynids.org/uid/index.html
Si todo funciona correctamente, debería ver la alerta correspondiente (la verificación de identificación de GPL ATTACK_RESPONSE devolvió la raíz) en Alertas. tu
También debería poder encontrar la alerta en Dashboards o Hunt.
Si no ve esta alerta, intente verificar si la regla está habilitada yendo a Detecciones y buscando el SID de la regla, que es
2100498. Una forma de buscar esta regla es especificarla en la URL de la siguiente manera:
#/detecciones?q=2100498
Otra forma de probar Suricata es con una utilidad llamada tmNIDS. Puede ejecutar la herramienta en modo interactivo de esta manera:
curl -sSL https://raw.githubusercontent.com/0xtf/testmynids.org/master/tmNIDS -o /tmp/tmNIDS && chmod +x /tmp/tmNIDS && /tmp/tmNIDS
Finalmente, también puede probar las alertas de Suricata reproduciendo algunos archivos PCAP de prueba mediante so-test.
- 171/402 - Soluciones de cebolla de seguridad, LLC

8.5.13 Alertas de solución de problemas
8.5.13 Alertas de solución de problemas
Si no ve las alertas de Suricata que espera ver, aquí hay algunas cosas que puede verificar:
• Si tiene metadatos habilitados, verifique si tiene metadatos para las conexiones. Dependiendo de su configuración, esto podría ser
Metadatos de Suricata o metadatos de Zeek. Vaya a Paneles, haga clic en el menú desplegable, seleccione las Conexiones vistas por Zeek o Suricata
panel de control y vea si las conexiones que espera ver en el tráfico de su red aparecen allí.
• Si tiene metadatos habilitados pero no ve ninguno, es posible que algo esté impidiendo que el proceso vea el tráfico.
Verifique si tiene alguna configuración de BPF que pueda hacer que el proceso ignore el tráfico. Si estás husmeando el tráfico de la red,
verifique que el tráfico llegue a la NIC mediante tcpdump. Si importa un archivo PCAP, verifique que el archivo contenga el tráfico que espera y que el
El proceso Suricata puede leer el archivo y cualquier directorio principal.
• Verifique si tiene etiquetas VLAN mezcladas (etiquetas VLAN en una dirección pero no en la otra). Si es así, consulte la sección Etiquetas VLAN anterior para
configurar Suricata apropiadamente.
• Verifique su configuración HOME_NET para asegurarse de que incluya las redes para las que está observando el tráfico.
• Verifique si tiene un conjunto de reglas NIDS completo con reglas que deberían alertar específicamente sobre el tráfico y que esas reglas estén habilitadas.
• Verifique si tiene algún umbral o configuración de supresión que pueda estar impidiendo las alertas.
• Consulte el registro de Suricata para obtener pistas adicionales.
• Verifique los registros de Elastic Agent, Logstash y Elasticsearch para detectar cualquier problema de canalización que pueda estar impidiendo que se escriban las alertas.
Búsqueda elástica.
• Intente instalar un nodo de importación simple (quizás en una máquina virtual) siguiendo los pasos de la sección Usuarios nuevos y vea si recibe alertas allí. si
entonces, compare el sistema que funciona con el sistema que no funciona y determine dónde están las diferencias.
8.5.14 Reglas de prueba
Para probar una nueva regla, utilice la siguiente utilidad en un nodo que ejecute Suricata (es decir, Sensor o Import).
sudo so-suricata-testrule <Nombre de archivo> /ruta/a/pcap/test.PCAP
El archivo debe contener la nueva regla que desea probar. El PCAP debe contener datos de red que activarán la regla.
8.5.15 Variables
Para agregar o modificar variables de Suricata, navegue hasta Suricata > config > vars > grupos de direcciones o grupos de puertos.
Puede asignar una lista de hosts, redes u otras personalizaciones a una variable de Suricata. Luego, la variable se puede reutilizar dentro de las reglas de Suricata.
y/o Anulaciones. Esto permite un ajuste único a la variable que afectará a todas las reglas que hacen referencia a ella.
Grupos de direcciones
Los grupos de direcciones definen direcciones IP o rangos de red. Suricata viene con una serie de grupos de direcciones comunes ya definidos.
SINTAXIS DEL GRUPO DE DIRECCIONES
Los valores se pueden especificar utilizando los siguientes formatos (una o varias líneas):
• IP única: 192.168.1.100
• Notación CIDR: 192.168.1.0/24
• Rango de IP: 192.168.1.1-192.168.1.50
• Múltiples valores: 192.168.1.0/24,10.0.0.0/8
• Negación: !192.168.1.100 o !$OTHER_VAR
• Referencia de variable: $HOME_NET
- 172/402 - Soluciones de cebolla de seguridad, LLC

8.5.16 Deshabilitar
Grupos de puertos
Los grupos de puertos definen puertos TCP/UDP para servicios específicos. Suricata viene con una serie de grupos de puertos comunes ya definidos.
SINTAXIS DEL GRUPO DE PUERTOS
Los valores se pueden especificar utilizando los siguientes formatos (una o varias líneas):
• Puerto único: 80
• Rango de puertos: 1024:65535
• Múltiples puertos: 80,443,8080
• Negación: !80
• Cualquier puerto: cualquiera
Variables personalizadas
Cree variables personalizadas seleccionando un grupo de direcciones o un grupo de puertos existente y haciendo clic en "Duplicar". Ingrese un nombre usando mayúsculas
convención de nomenclatura, luego haga clic en "Crear configuración".
Nota: La nueva variable no se guarda hasta que modifique su valor y haga clic en la marca de verificación verde "Guardar cambios".
Nota: Las variables del grupo de puertos personalizado tienen algunas limitaciones sintácticas, por ejemplo, no poder utilizar la negación.
8.5.16 Deshabilitar
Si necesita deshabilitar Suricata, puede hacerlo a través de Administración --> Configuración --> Suricata --> habilitado.
8.5.17 Más información
Nota
Para obtener más información sobre Suricata, consulte https://suricata.io.
- 173/402 - Soluciones de cebolla de seguridad, LLC

8.6 Zeek
8.6 Zeek
Security Onion incluye Zeek para metadatos y análisis de protocolos de red. De https://zeek.org:
Zeek es un potente marco de análisis de red que es muy diferente del típico IDS que quizás conozcas. (Zeek es el nuevo nombre del
Sistema Bro de larga data. Tenga en cuenta que algunas partes del sistema conservan el nombre "Bro" y, a menudo, también aparece en la documentación y
distribuciones.)
Los registros de Zeek se envían a Elasticsearch para su análisis y almacenamiento y luego se pueden encontrar en Dashboards, Hunt y Kibana. He aquí un ejemplo de
Zeek inicia sesión en Hunt:
8.6.1 ID de comunidad
Security Onion habilita el soporte integrado de Zeek para Community ID.
8.6.2 Pérdida de paquetes y pérdida de captura
Zeek informa tanto la pérdida de paquetes como la pérdida de captura y puede encontrar gráficos de estas en InfluxDB. Si Zeek informa pérdida de paquetes, lo más probable es que
Es necesario ajustar el número de trabajadores de Zeek como se muestra a continuación o filtrar el tráfico utilizando BPF. Si Zeek informa pérdida de captura pero no pérdida de paquetes,
Esto generalmente significa que la pérdida de captura ocurre aguas arriba en el propio puerto TAP o SPAN.
8.6.3 Configuración
Puede configurar Zeek yendo a Administración --> Configuración --> Zeek.
- 174/402 - Soluciones de cebolla de seguridad, LLC

8.6.4 INICIO_NET
Los registros de Zeek son consumidos por Elastic Agent (administrado por Elastic Fleet), por lo que si desea configurar qué registros de Zeek se excluyen, puede ir
a Administración --> Configuración --> elasticfleet --> registro --> Zeek --> excluido.
8.6.4 INICIO_NET
La variable HOME_NET define las redes que se consideran redes domésticas (aquellas redes que estás monitoreando y defendiendo).
El valor predeterminado es el espacio de direcciones privado RFC1918 (10.0.0.0/8, 192.168.0.0/16 y 172.16.0.0/12). Puede modificar este valor predeterminado mediante
yendo a Administración --> Configuración --> Zeek --> config --> redes --> HOME_NET.
- 175/402 - Soluciones de cebolla de seguridad, LLC

8.6.5 Rendimiento
8.6.5 Rendimiento
Zeek utiliza AF-PACKET para que pueda activar varios trabajadores de Zeek para manejar más tráfico.
Si tiene varias CPU físicas, lo más probable es que desee fijar procesos de rastreo a una CPU en el mismo acceso a memoria no uniforme.
(NUMA) al que está vinculada su NIC de rastreo. Acceder a una CPU en el mismo dominio NUMA es más rápido que a través de un dominio NUMA.
Nota
Para obtener más información sobre cómo determinar dominios NUMA usando lscpu y lstopo, consulte https://github.com/brokenscripts/cpu_pinning.
Puede modificar el recuento de trabajadores de Zeek yendo a Administración --> Configuración --> Zeek --> configuración --> nodo --> trabajadores.
8.6.6 Deshabilitar
Zeek se puede desactivar yendo a Administración --> Configuración --> Zeek --> habilitado.
8.6.7 Registro del sistema
Para reenviar registros de Zeek a un recopilador de syslog externo, consulte la sección de salida de syslog.
8.6.8 Registros
Los registros de Zeek se almacenan en /nsm/zeek/logs. Son recopilados por Elastic Agent, analizados y almacenados en Elasticsearch, y visibles en
Paneles, Hunt y Kibana.
Configuramos Zeek para generar registros en formato JSON. Si necesita analizar esos registros JSON desde la línea de comando, puede usar jq.
Zeek monitorea el tráfico de su red y registra los metadatos del protocolo. Éstos son sólo algunos ejemplos.
conn.log
• Conexiones TCP/UDP/ICMP
• Para conexiones ICMP, el tipo ICMP se registra como puerto de origen y el código ICMP como puerto de destino.
• Para obtener más información, consulte https://docs.zeek.org/en/latest/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info.
dns.log
• Actividad DNS
• Para obtener más información, consulte https://docs.zeek.org/en/latest/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info.
http.log
• Solicitudes y respuestas HTTP
• Para obtener más información, consulte https://docs.zeek.org/en/latest/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info.
ssl.log
• Información de protocolo de enlace SSL/TLS
• Para obtener más información, consulte https://docs.zeek.org/en/latest/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info.
- 176/402 - Soluciones de cebolla de seguridad, LLC

8.6.9 Extracción de archivos
aviso.log
• Avisos Zeek
• Para obtener más información, consulte https://docs.zeek.org/en/latest/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info.
Otros registros de Zeek
Zeek también proporciona otros registros de forma predeterminada y puede leer más sobre ellos en https://docs.zeek.org/en/latest/script-reference/log-files.html.
Además de los registros predeterminados de Zeek, también incluimos analizadores de protocolos para el tráfico STUN, TDS y Wireguard. También incluimos soporte para ICS/
Protocolos SCADA como BACnet, BSAP, CIP, COTP, DNP3, ECAT, ENIP, Modbus, OPC UA, Profinet y S7. Todos estos analizadores están habilitados.
de forma predeterminada y puede encontrar los paneles correspondientes para cada uno de ellos en Paneles.
También incluimos scripts de MITRE BZAR y puede leer más sobre ellos en https://github.com/mitre-attack/bzar. Tenga en cuenta que el MITRE
Los scripts BZAR están deshabilitados de forma predeterminada. Si desea habilitarlos, puede hacerlo a través de Administración --> Configuración --> Zeek. una vez
habilitado, luego puede verificar las detecciones de BZAR yendo a Paneles y seleccionando el panel de Avisos de Zeek.
Como puede ver, los datos de registro de Zeek pueden proporcionar una gran cantidad de información al analista, a la que se puede acceder fácilmente a través de Dashboards, Hunt o Kibana.
8.6.9 Extracción de archivos
De forma predeterminada, Zeek extraerá archivos del tráfico de la red y Strelka luego analizará esos archivos extraídos.
8.6.10 Etiquetas VLAN
Si el tráfico de su red tiene etiquetas VLAN, Zeek las registrará en conn.log. Dashboards incluye un panel de VLAN que muestra estos datos.
8.6.11 Intel
Puede agregar su propia información a /opt/so/saltstack/local/salt/zeek/policy/intel/intel.dat en el administrador y automáticamente
replicarse en todos los nodos sensores. Si el directorio /opt/so/saltstack/local/salt/zeek/policy/intel/ está vacío, puede copiar los archivos predeterminados
(tanto intel.dat como __load__.Zeek) de /opt/so/saltstack/default/salt/zeek/policy/intel/ de la siguiente manera:
sudo cp /opt/so/saltstack/default/salt/zeek/policy/intel/* /opt/so/saltstack/local/salt/zeek/policy/intel/
Tenga en cuenta que Zeek es muy estricto con el formato de intel.dat. Al editar este archivo, siga estas pautas:
• sin espacios ni líneas iniciales
• campos separados con un único carácter de tabulación literal
• sin espacios ni líneas finales
El archivo intel.dat predeterminado sigue estas pautas para que pueda consultarlo como ejemplo del formato adecuado.
Cuando termine de editar intel.dat, ejecute sudo salt $SENSORNAME_$ROLE state.highstate para sincronizar /opt/so/saltstack/local/salt/zeek/
política/intel/ a /opt/so/conf/zeek/policy/intel/. Si tiene una implementación distribuida con nodos de sensores separados, puede tardar hasta
15 minutos para que la información se sincronice con los nodos sensores.
Si experimenta un error o no nota que se genera /nsm/zeek/logs/current/intel.log, intente echar un vistazo en /nsm/zeek/logs/
current/reporter.log para obtener pistas. También es posible que desees reiniciar Zeek después de realizar cambios ejecutando sudo so-zeek-restart.
Para obtener más información, consulte https://docs.zeek.org/en/latest/frameworks/intel.html.
8.6.12 Paquetes personalizados
Puede instalar paquetes Zeek personalizados usando zkg. Coloque cada paquete como un subdirectorio en /opt/so/saltstack/local/salt/zeek/zkg/ en
el gerente. Por ejemplo, si tiene un paquete personalizado llamado mi-paquete, la estructura del directorio sería:
/opt/so/saltstack/local/salt/zeek/zkg/mi-paquete/
- 177/402 - Soluciones de cebolla de seguridad, LLC

8.6.13 Registro de diagnóstico
El directorio del paquete debe contener una estructura de paquete Zeek válida (incluido un archivo zkg.meta).
Nota
zkg requiere que los paquetes de los repositorios de git sean un clon del repositorio. El árbol de trabajo debe estar limpio, de lo contrario no se instalará el paquete. git
El estado le dirá si está limpio o no.
Después de colocar el paquete, ejecute sudo salt $SENSORNAME_$ROLE state.highstate para sincronizar los paquetes con los nodos del sensor. los paquetes
se instalará automáticamente con zkg cada vez que se inicie el contenedor Zeek. Si tiene una implementación distribuida con sensor independiente
nodos, los paquetes pueden tardar hasta 15 minutos en sincronizarse con los nodos sensores.
Puede verificar que se instaló un paquete personalizado verificando los registros del contenedor Zeek:
sudo docker registra tan-zeek
8.6.13 Registro de diagnóstico
Los registros de diagnóstico de Zeek se pueden encontrar en /nsm/zeek/logs/. Busque archivos como reporter.log, stats.log, stderr.log y stdout.log.
Dependiendo de lo que esté buscando, es posible que también deba consultar los registros de Docker para el contenedor:
sudo docker registra tan-zeek
8.6.14 Más información
Nota
Para obtener más información sobre Zeek, consulte https://zeek.org.
- 178/402 - Soluciones de cebolla de seguridad, LLC

8.7 Strelka
8.7 Strelka
Desde https://github.com/target/strelka:
Strelka es un sistema de escaneo de archivos en tiempo real que se utiliza para la búsqueda y detección de amenazas y la respuesta a incidentes. En base al diseño establecido
por Laika BOSS de Lockheed Martin y proyectos similares (ver: proyectos relacionados), el propósito de Strelka es realizar extracción de archivos y metadatos
colección a gran escala.
Si está monitoreando el tráfico de la red, entonces Zeek o Suricata deberían extraer ciertos archivos detectados en el tráfico de la red no cifrado.
Strelka luego analiza esos archivos y terminan en /nsm/strelka/processed/.
Security Onion verifica los hashes de los archivos antes de enviarlos a Strelka para evitar analizar el mismo archivo varias veces en un período de 48 horas.
8.7.1 Alertas
Strelka escanea archivos usando reglas YARA. Si detecta una coincidencia, generará una alerta que se puede encontrar en Alertas, Paneles o Búsqueda. tu
Puede configurar reglas YARA a través de Detecciones.
8.7.2 Registros
Incluso si Strelka no detecta una coincidencia de YARA, seguirá registrando metadatos sobre el archivo. Puede encontrar registros de Strelka en Dashboards y Hunt.
8.7.3 Configuración
Puede configurar Strelka yendo a Administración --> Configuración --> Strelka.
- 179/402 - Soluciones de cebolla de seguridad, LLC

8.7.4 Registro de diagnóstico
8.7.4 Registro de diagnóstico
Los registros de diagnóstico de Strelka se encuentran en /nsm/strelka/log/. Dependiendo de lo que esté buscando, es posible que también deba consultar los registros de Docker para
contenedores:
sudo docker registra so-strelka-backend
sudo docker logs coordinador-so-strelka
sudo docker registra so-strelka-filestream
sudo docker registra so-strelka-frontend
sudo docker logs so-strelka-manager
8.7.5 Más información
Nota
Para obtener más información sobre Strelka, consulte https://github.com/target/strelka.
- 180/402 - Soluciones de cebolla de seguridad, LLC

8.8 Honeypot de detección de intrusiones
8.8 Honeypot de detección de intrusiones
Security Onion incluye una opción de nodo Honeypot de detección de intrusiones (IDH). Esto le permite construir un nodo que imite los servicios comunes.
como HTTP, FTP y SSH. Cualquier interacción con estos servicios falsos generará automáticamente una alerta.
Del libro Honeypots de detección de intrusiones (Sanders, C):
Un Honeypot de detección de intrusiones (IDH) es un recurso de seguridad ubicado dentro del perímetro de su red que genera alertas cuando se sondea o
atacado. Estos sistemas, servicios y tokens se basan en el engaño para atraer a los atacantes y convencerlos de interactuar. Sin que el
atacante, recibirá una alerta cuando se produzca esa interacción y podrá comenzar a investigar el compromiso.
Chris Sanders y Josh Brower presentaron el concepto IDH en Security Onion Conference 2021 y puedes ver la grabación en https://
www.youtube.com/watch?v=NzUhfARVfJk&list=PLljFlTO9rB17mESq7Z9OeFKvVh39vJW34&index=5.
8.8.1 Instalación
Los nodos IDH están dedicados a ser simplemente nodos IDH y no pueden ejecutar ningún otro servicio. Por lo tanto, debe tener un administrador independiente para conectarse.
a. Puede unir un nuevo nodo IDH a una implementación independiente existente o a una implementación distribuida completa. Nuestra imagen ISO incluye un menú de inicio.
opción para instalaciones IDH que particionará su disco adecuadamente con requisitos más bajos que una instalación completa.
Advertencia
¡El nodo IDH está diseñado para colocarse dentro del perímetro de su red! ¡No debería ser accesible desde Internet!
8.8.2 Configuración
• Ejecute la instalación y seleccione la opción de implementación DISTRIBUIDA.
• Seleccione la opción Implementación existente.
• Seleccione la opción IDH.
• Opcionalmente, puede evitar que los servicios IDH escuchen en la interfaz de administración.
• Una vez que se completa la configuración y el nodo IDH está completamente unido a la red, puede realizar una configuración adicional yendo a Administración -->
Configuración --> IDH.
• Una vez completada la configuración, las conexiones a los servicios de honeypot generarán alertas SO IDH que se pueden ver en Alertas.
8.8.3 Antecedentes técnicos
El nodo IDH utiliza OpenCanary, que es un honeypot modular de código abierto de Thinkst. Puedes leer más al respecto en https://github.com/
thinkst/opencanario.
Los registros de OpenCanary se pueden encontrar a través de Dashboards, Hunt o Kibana mediante las siguientes consultas:
módulo.evento: opencanary
evento.conjunto de datos: IDH
Las reglas de Sigma dentro de Detecciones buscan ciertos registros emitidos por OpenCanary para generar alertas, que se pueden ver en la interfaz de Alertas.
- 181/402 - Soluciones de cebolla de seguridad, LLC

8.8.4 Configuración de servicios
8.8.4 Configuración de servicios
Los siguientes servicios están disponibles para su uso con el nodo IDH. Preste especial atención a cómo se activa una alerta para un servicio, ya que algunos de
requieren más que una simple solicitud de conexión para activarse.
• FTP: un servidor de protocolo de transferencia de archivos que alerta sobre intentos de inicio de sesión
• Git: un servidor Git que alerta sobre la clonación de repositorios.
• HTTP: un servidor web HTTP que alerta sobre intentos de inicio de sesión
• Proxy HTTP: un proxy web HTTP que alerta cuando hay un intento de realizar un proxy a otra página.
• MSSQL: un servidor MS SQL que alerta sobre intentos de inicio de sesión
• MySQL: un servidor MySQL que alerta sobre intentos de inicio de sesión
• Telnet: un servidor Telnet que alerta sobre intentos de inicio de sesión
• SNMP: un servidor SNMP que alerta sobre solicitudes de OID
• SSH: un servidor Secure Shell que alerta sobre intentos de inicio de sesión
• SIP: un servidor SIP que alerta sobre solicitudes SIP
• VNC: un servidor VNC que alerta sobre intentos de inicio de sesión
• Redis: un servidor Redis que alerta sobre acciones
• TFTP: un servidor TFTP que alerta sobre solicitudes
• NTP: un servidor NTP que alerta sobre solicitudes NTP
Esto se basa en la lista en https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration. RDP y PYMES
actualmente no están disponibles para su uso dentro de un nodo IDH.
Además de cambiar los puertos predeterminados, algunos de estos servicios tienen más opciones de configuración. Por ejemplo, el servidor HTTP tiene la
capacidad de utilizar páginas HTML personalizadas ("skins"). Para obtener más información, consulte la documentación de OpenCanary en https://
opencanary.readthedocs.io/en/latest/starting/configuration.html#default-configuration.
Estos tipos de cambios de configuración se pueden realizar modificando el pilar minion (consulte la sección Configuración personalizada a continuación).
8.8.5 disco duro
Para los nodos IDH, el sshd local está configurado para escuchar en TCP/2222 y solo se aceptan conexiones desde el nodo Manager. Esto permite
TCP/22 se utilizará para servicios de honeypot.
8.8.6 Configuración personalizada
Puede configurar IDH yendo a Administración --> Configuración --> IDH.
- 182/402 - Soluciones de cebolla de seguridad, LLC

8.8.7 Ejemplo de configuración personalizada
8.8.7 Ejemplo de configuración personalizada
Por ejemplo, supongamos que ya tenemos el servicio HTTP ejecutándose pero queremos cambiar el puerto predeterminado de 80 a 8080.
Advertencia
¡Tenga mucho cuidado al realizar cambios!
• Vaya a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y habilite la opción Mostrar configuración avanzada.
• En el lado izquierdo, navegue hasta IDH --> opencanary --> config --> http_x_port.
• En el lado derecho, cambie el valor del puerto y luego haga clic en la marca de verificación para guardar el cambio.
• En la parte superior de la página, haga clic en el botón SINCRONIZAR CUADRICULA en el menú Opciones.
8.8.8 Activación de interfaces de red adicionales
Si desea activar interfaces de red adicionales después de unir su nodo IDH a su grid, puede hacerlo utilizando la red Linux estándar.
herramientas como nmtui. Puede leer más sobre nmtui en https://docs.oracle.com/en/operating-systems/oracle-linux/9/network/network-
NetworkConfigurationTools.html.
- 183/402 - Soluciones de cebolla de seguridad, LLC

9. Visibilidad de red adicional
9. Visibilidad de red adicional
9.1 Descripción general adicional de la visibilidad de la red
En la sección Visibilidad de la red, analizamos la visibilidad de la red proporcionada por el propio Security Onion. La situación ideal sería contar con Seguridad.
Sensores de red Onion que cubren todos y cada uno de los segmentos de su red. Si eres capaz de lograr esa situación ideal, entonces es posible que no puedas
necesita visibilidad de red adicional. Sin embargo, puede haber ocasiones en las que simplemente no puedas cubrir ciertos segmentos de red con Seguridad.
Sensores de red cebolla y es entonces cuando estas opciones adicionales pueden resultar beneficiosas. Sin embargo, tenga en cuenta que los datos que proporcionan son
no es tan completo como un sensor de red completo de Security Onion.
Una opción para obtener visibilidad adicional de la red serían los registros de NetFlow de firewalls, conmutadores o enrutadores que muestren qué tráfico fue observado por
el dispositivo de red. Otra opción serían los registros del firewall que muestren qué tráfico se permitió a través del firewall y qué tráfico se denegó.
Los registros del firewall pueden estar en diferentes formatos, como CEF, iptables o una combinación de ambos (como en los firewalls UniFi). También contamos con soporte para
firewalls pfSense y OPNsense y puede encontrar otras integraciones de firewall en la sección Integraciones de terceros.
- 184/402 - Soluciones de cebolla de seguridad, LLC

9.2 Flujo de red
9.2 Flujo de red
Es posible que tenga dispositivos en su red, como firewalls, enrutadores y conmutadores, que sean capaces de exportar registros de NetFlow. Si quisieras
Si desea recopilar estos registros de NetFlow, agregue la integración elástica para registros de NetFlow y luego permita el tráfico de Netflow a través del firewall.
9.2.1 Agregar la integración de NetFlow Records
Primero, agregue la integración Elastic para NetFlow Records.
Nota
Para obtener más información sobre la integración de NetFlow Records, consulte https://docs.elastic.co/en/integrations/netflow.
1. Vaya a Elastic Fleet, haga clic en la pestaña Políticas del agente y luego haga clic en la política deseada (por ejemplo, so-grid-nodes_general).
2. Haga clic en el botón Agregar integración.
3. Busque netflow y luego haga clic en la integración de NetFlow Records.
4. La página de Integración elástica mostrará una descripción general de la integración de NetFlow. Revise toda la información en la página y luego haga clic en Agregar
Botón Registros de NetFlow.
5. En la pantalla de integración Agregar registros NetFlow, vaya al campo host UDP para escuchar y cambie localhost a 0.0.0.0. verificar
el puerto UDP para escuchar en el campo coincide con el que enviará su exportador NetFlow. Haga clic en el botón Guardar y continuar y luego
Haga clic en Guardar e implementar cambios.
9.2.2 Permitir el tráfico NetFlow a través del firewall
A continuación, permita el tráfico desde el exportador de NetFlow a través del firewall hasta el puerto de escucha de NetFlow.
Nota
Las siguientes instrucciones asumen que este es el primer cambio de firewall que ha realizado y, por lo tanto, se refieren a customhostgroup0 y
grupo de puerto personalizado0. Si ya se han utilizado, puede seleccionar el siguiente grupo de hosts y grupo de puertos disponibles.
1. Navegue a Administración --> Configuración.
2. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
3. En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y haga clic en el grupo customhostgroup0. En el lado derecho, ingrese la dirección IP del
Exportador NetFlow y haga clic en la marca de verificación para guardar.
4. En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione el grupo customportgroup0 y luego haga clic en udp. En el lado derecho, ingresa tu
Puerto de escucha NetFlow deseado (2055 por defecto) y haga clic en la marca de verificación para guardar.
5. En el lado izquierdo, vaya al firewall, seleccione función y luego seleccione el tipo de nodo que recibirá los registros de NetFlow. Luego taladre la cadena -->
ENTRADA --> grupos de hosts --> grupo de hosts personalizado0 --> grupos de puertos. En el lado derecho, ingrese customportgroup0 y haga clic en la marca de verificación para
guardar.
6. Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
9.2.3 Panel de control de NetFlow
Una vez que se complete toda la configuración, debería poder ir a Paneles y seleccionar el panel de NetFlow para ver sus registros de NetFlow.
- 185/402 - Soluciones de cebolla de seguridad, LLC

9.3 MCE
9.3 MCE
Si tiene dispositivos en su red que pueden enviar registros en formato CEF, puede enviar esos registros a Security Onion. Para obtener esos registros CEF
Elasticsearch, deberá agregar la integración de Elastic para CEF y luego configurar el firewall Security Onion para permitir que el dispositivo remoto
enviar sus registros.
9.3.1 Agregar la integración CEF
Primero, agregue la integración Elastic para CEF.
Nota
Para obtener más información sobre la integración de CEF, consulte https://www.elastic.co/docs/reference/integrations/cef.
1. Vaya a Elastic Fleet, haga clic en la pestaña Políticas del agente y luego haga clic en la política deseada (por ejemplo, so-grid-nodes_general).
2. Haga clic en el botón Agregar integración.
3. Busque cef y luego haga clic en la integración del formato de evento común (CEF).
4. La página de Integración elástica mostrará una descripción general de la integración de CEF. Revise toda la información en la página y luego haga clic en Agregar
Botón Formato de evento común (CEF).
5. En la pantalla de integración Agregar formato de evento común (CEF), deshabilite las opciones etiquetadas Recopilar registros de aplicaciones CEF (entrada:
logfile) y recopilar registros de aplicaciones CEF (entrada: tcp). Asegúrese de que la opción Recopilar registros de aplicaciones CEF (entrada: udp) esté
habilitado y luego cambie la configuración de Syslog Host de localhost a 0.0.0.0. El puerto Syslog debe configurarse en 9003 de forma predeterminada.
Haga clic en el botón Guardar y continuar y luego haga clic en Guardar e implementar cambios.
9.3.2 Permitir registros CEF a través del firewall
A continuación, permita el tráfico desde el host CEF a través del firewall hasta el puerto de integración CEF.
Nota
Las siguientes instrucciones asumen que este es el primer cambio de firewall que ha realizado y, por lo tanto, se refieren a customhostgroup0 y
grupo de puerto personalizado0. Si ya se han utilizado, puede seleccionar el siguiente grupo de hosts y grupo de puertos disponibles.
1. Navegue a Administración --> Configuración.
2. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
3. En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y haga clic en el grupo customhostgroup0. En el lado derecho, ingrese la dirección IP del
Host CEF y haga clic en la marca de verificación para guardar.
4. En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione el grupo customportgroup0 y luego haga clic en udp. En el lado derecho, ingresa tu
puerto de escucha deseado (9003 por defecto) y haga clic en la marca de verificación para guardar.
5. En el lado izquierdo, vaya al firewall, seleccione función y luego seleccione el tipo de nodo que recibirá los registros CEF. Luego taladre la cadena --> ENTRADA
--> grupos de host --> grupo de host personalizado0 --> grupos de puertos. En el lado derecho, ingrese customportgroup0 y haga clic en la marca de verificación para guardar.
6. Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
9.3.3 Panel de control del MCE
Una vez que se complete toda la configuración, debería poder ir a Paneles y seleccionar el panel de CEF para ver sus registros de CEF.
- 186/402 - Soluciones de cebolla de seguridad, LLC

9.4 iptables
9.4 iptables
Si tiene firewalls iptables de Linux en su red, puede enviar esos registros a Security Onion. Para obtener esos registros de iptables en Elasticsearch,
deberá agregar la integración elástica para iptables y luego configurar el firewall Security Onion para permitir que el firewall remoto envíe sus
registros.
9.4.1 Agregar la integración de iptables
Primero, agregue la integración Elastic para iptables.
Nota
Para obtener más información sobre la integración de iptables, consulte https://www.elastic.co/docs/reference/integrations/iptables.
1. Vaya a Elastic Fleet, haga clic en la pestaña Políticas del agente y luego haga clic en la política deseada (por ejemplo, so-grid-nodes_general).
2. Haga clic en el botón Agregar integración.
3. Busque iptables y luego haga clic en la integración de iptables.
4. La página de Integración elástica mostrará una descripción general de la integración de iptables. Revise toda la información en la página y luego haga clic en Agregar
botón iptables.
5. En la pantalla Agregar integración de iptables, deshabilite las opciones etiquetadas Recopilar registros de aplicaciones de iptables (entrada: archivo de registro) y
Recopile registros de aplicaciones de iptables (entrada: journald). Asegúrese de que la opción Recopilar registros de la aplicación iptables (entrada: udp) esté
habilitado y luego cambie la configuración del host Syslog de localhost a 0.0.0.0. El puerto Syslog debe configurarse en 9001 de forma predeterminada.
Haga clic en el botón Guardar y continuar y luego haga clic en Guardar e implementar cambios.
9.4.2 Permitir registros de iptables a través del firewall
A continuación, permita el tráfico desde el host de iptables a través del firewall hasta el puerto de integración de iptables.
Nota
Las siguientes instrucciones asumen que este es el primer cambio de firewall que ha realizado y, por lo tanto, se refieren a customhostgroup0 y
grupo de puerto personalizado0. Si ya se han utilizado, puede seleccionar el siguiente grupo de hosts y grupo de puertos disponibles.
1. Navegue a Administración --> Configuración.
2. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
3. En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y haga clic en el grupo customhostgroup0. En el lado derecho, ingrese la dirección IP del
iptables host y haga clic en la marca de verificación para guardar.
4. En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione el grupo customportgroup0 y luego haga clic en udp. En el lado derecho, ingresa tu
puerto de escucha deseado (9001 por defecto) y haga clic en la marca de verificación para guardar.
5. En el lado izquierdo, vaya al firewall, seleccione rol y luego seleccione el tipo de nodo que recibirá los registros de iptables. Luego taladre la cadena -->
ENTRADA --> grupos de hosts --> grupo de hosts personalizado0 --> grupos de puertos. En el lado derecho, ingrese customportgroup0 y haga clic en la marca de verificación para
guardar.
6. Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
9.4.3 Panel de control de iptables
Una vez que se complete toda la configuración, debería poder ir a Paneles y seleccionar el panel Firewall - iptables para ver su
registros de iptables.
- 187/402 - Soluciones de cebolla de seguridad, LLC

9.5 UniFi
9.5 UniFi
Si tiene firewalls UniFi en su red, puede enviar sus registros a Security Onion. Normalmente, los cortafuegos UniFi pueden enviar dos tipos diferentes de
registros. El primero son los registros del firewall de iptables y el segundo son los registros del sistema en formato CEF. Para obtener todos estos registros en Elasticsearch, deberá
agregue las integraciones elásticas para iptables y CEF, configure el dispositivo UniFi para enviar esos registros y luego configure el firewall Security Onion
para permitir esos registros.
9.5.1 Agregar las integraciones de iptables y CEF
Primero, agregue las integraciones de Elastic para iptables y CEF.
Nota
Para obtener más información sobre la integración de iptables, consulte https://www.elastic.co/docs/reference/integrations/iptables.
Para obtener más información sobre la integración de CEF, consulte https://www.elastic.co/docs/reference/integrations/cef.
1. Vaya a Elastic Fleet, haga clic en la pestaña Políticas del agente y luego haga clic en la política deseada (por ejemplo, so-grid-nodes_general).
2. Haga clic en el botón Agregar integración.
3. Busque iptables y luego haga clic en la integración de iptables.
4. La página de Integración elástica mostrará una descripción general de la integración de iptables. Revise toda la información en la página y luego haga clic en Agregar
botón iptables.
5. En la pantalla Agregar integración de iptables, deshabilite las opciones etiquetadas Recopilar registros de aplicaciones de iptables (entrada: archivo de registro) y
Recopile registros de aplicaciones de iptables (entrada: journald). Asegúrese de que la opción Recopilar registros de la aplicación iptables (entrada: udp) esté
habilitado y luego cambie la configuración del host Syslog de localhost a 0.0.0.0. El puerto Syslog debe configurarse en 9001 de forma predeterminada.
Haga clic en el botón Guardar y continuar y luego haga clic en Guardar e implementar cambios.
6. De regreso a la pantalla de política deseada, haga clic en el botón Agregar integración.
7. Busque cef y luego haga clic en la integración del formato de evento común (CEF).
8. La página de Integración elástica mostrará una descripción general de la integración de CEF. Revise toda la información en la página y luego haga clic en Agregar
Botón Formato de evento común (CEF).
9. En la pantalla de integración Agregar formato de evento común (CEF), deshabilite las opciones etiquetadas Recopilar registros de aplicaciones CEF (entrada:
logfile) y recopilar registros de aplicaciones CEF (entrada: tcp). Asegúrese de que la opción Recopilar registros de aplicaciones CEF (entrada: udp) esté
habilitado y luego cambie la configuración de Syslog Host de localhost a 0.0.0.0. El puerto Syslog debe configurarse en 9003 de forma predeterminada.
Haga clic en el botón Guardar y continuar y luego haga clic en Guardar e implementar cambios.
9.5.2 Configurar UniFi
A continuación, configure UniFi para enviar ambos tipos de registros a Security Onion.
Nota
La configuración de UniFi puede ser diferente según el dispositivo UniFi específico que tenga y el software que esté ejecutando. Estas instrucciones son
basado en un dispositivo Cloud Gateway Fiber que ejecuta la versión 4.2.12 del plano de control y la versión 9.3.43 de la aplicación de red.
- 188/402 - Soluciones de cebolla de seguridad, LLC

9.5.3 Permitir registros de UniFi a través del firewall Security Onion
Para configurar UniFi para enviar registros de firewall de iptables a la integración elástica para iptables:
1. En la interfaz web de UniFi, navegue hasta Configuración --> CyberSecure --> Registro de tráfico.
2. Junto a Registro de actividad (Syslog), elija la opción Servidor SIEM.
3. Configure la Dirección del servidor en la dirección IP del nodo Security Onion al que enviar los registros.
4. Configure el Puerto en 9001.
5. Haga clic en el botón Aplicar cambios.
Para configurar UniFi para enviar registros del sistema a la integración Elastic para CEF:
1. En la interfaz web de UniFi, navegue hasta Configuración --> Plano de control --> Integraciones.
2. Junto a Registro de actividad (Syslog), elija la opción Servidor SIEM.
3. Configure la Dirección del servidor en la dirección IP del nodo Security Onion al que enviar los registros.
4. Configure el Puerto en 9003.
5. Haga clic en el botón Aplicar cambios.
Mientras esté en UniFI, verifique las reglas de su firewall UniFi y actualícelas si es necesario:
1. En la interfaz web de UniFi, navegue hasta Configuración --> Motor de políticas.
2. Para cualquier regla de firewall que desee ver en Security Onion, asegúrese de que Syslog Logging esté habilitado y que la descripción comience con
ya sea Bloquear o Permitir.
9.5.3 Permitir registros de UniFi a través del firewall Security Onion
Finalmente, permita el tráfico desde el dispositivo UniFi a través del firewall Security Onion hacia los puertos de integración Elastic.
Nota
Las siguientes instrucciones asumen que este es el primer cambio de firewall que ha realizado y, por lo tanto, se refieren a customhostgroup0 y
grupo de puerto personalizado0. Si ya se han utilizado, puede seleccionar el siguiente grupo de hosts y grupo de puertos disponibles.
1. Navegue a Administración --> Configuración.
2. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
3. En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y haga clic en el grupo customhostgroup0. En el lado derecho, ingrese la dirección IP del
Host UniFi y haga clic en la marca de verificación para guardar.
4. En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione el grupo customportgroup0 y luego haga clic en udp. En el lado derecho, ingrese
9001 y 9003 y luego haga clic en la marca de verificación para guardar.
5. En el lado izquierdo, vaya al firewall, seleccione función y luego seleccione el tipo de nodo que recibirá los registros de UniFi. Luego taladre la cadena -->
ENTRADA --> grupos de hosts --> grupo de hosts personalizado0 --> grupos de puertos. En el lado derecho, ingrese customportgroup0 y haga clic en la marca de verificación para
guardar.
6. Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
9.5.4 Paneles UniFi
Una vez completada toda la configuración, debería poder ir a Paneles y seleccionar uno de los paneles de Firewall - UniFi para ver su
Registros de UniFi.
- 189/402 - Soluciones de cebolla de seguridad, LLC

9.6 pfSentido
9.6 pfSentido
pfSense es un firewall abierto y gratuito que se puede encontrar en https://www.pfsense.org/. Hay algunas formas diferentes en las que puedes integrar
pfSense en su implementación de Security Onion.
El método más simple para integrar pfSense en su implementación de Security Onion es configurar pfSense para que envíe sus registros de firewall a Seguridad.
Cebolla. Security Onion tiene un par de opciones para ingerir registros de los firewalls pfSense: un analizador simple y el Elastic más completo
Integración para pfSense. Recomendamos utilizar la opción más completa siguiendo los pasos de la sección Integración elástica a continuación.
También puede seguir nuestro video en https://www.youtube.com/watch?v=aoH8qZwAxek.
También puede configurar pfSense para enviar datos de NetFlow a su implementación de Security Onion. Esto puede proporcionar cierta visibilidad adicional si
no puede implementar un sensor de red Security Onion completo para monitorear ese segmento de red.
9.6.1 Analizador sencillo
La primera opción para recopilar registros del firewall de pfSense es utilizar nuestro sencillo analizador. Tenga en cuenta que esto solo admite filterlog (firewall real
logs) y ningún otro registro.
Advertencia
Este sencillo analizador se eliminará con el tiempo en favor de la integración elástica más completa para pfSense que aparece a continuación.
Para utilizar el analizador simple, primero vaya a Administración --> Configuración --> firewall --> grupos de hosts.
Una vez allí, seleccione la opción syslog, especifique la dirección IP del firewall pfSense y haga clic en la marca de verificación para guardar. Luego haga clic en
botón SINCRONIZAR GRID en el menú Opciones en la parte superior de la página.
A continuación, configure su firewall pfSense para enviar syslog a la dirección IP de su equipo Security Onion. Si está utilizando pfSense 2.6.0 o superior,
asegúrese de que el formato de mensaje de registro esté configurado en BSD (RFC 3164, predeterminado).
Una vez que se complete toda la configuración, debería poder ir a Paneles y seleccionar el panel de Firewall para ver los registros de su firewall.
- 190/402 - Soluciones de cebolla de seguridad, LLC

9.6.2 Integración elástica para pfSense
9.6.2 Integración elástica para pfSense
La segunda opción para recopilar registros de firewall de pfSense es utilizar Elastic Integration para pfSense (https://docs.elastic.co/integrations/
pfsentido). Esta integración es más completa que el analizador simple anterior y admite más tipos de registros.
Primero, agregue la integración de pfSense y configure el firewall de pfSense:
1. Vaya a Elastic Fleet, haga clic en la pestaña Políticas del agente y luego haga clic en la política deseada (por ejemplo, so-grid-nodes_general).
2. Haga clic en el botón Agregar integración.
3. Busque pfSense y luego haga clic en la integración de pfSense.
4. La página de Integración elástica mostrará instrucciones para configurar pfSense. Siga estas instrucciones pero tenga en cuenta que el elástico
La integración espera recibir registros de pfSense en el puerto 9001 de forma predeterminada.
5. Una vez que haya configurado pfSense, regrese a la pantalla Elastic y haga clic en el botón Agregar pfSense.
6. En la pantalla Editar integración de pfSense, vaya al campo Syslog Host y cambie localhost a 0.0.0.0.
7. Haga clic en el botón Guardar y continuar y luego haga clic en Guardar e implementar cambios.
A continuación, permita el tráfico desde el firewall pfSense al puerto 9001. Estas instrucciones asumen que este es el primer cambio de firewall que ha realizado.
y por lo tanto haga referencia a customhostgroup0 y customportgroup0. Si ya se han utilizado, seleccione el siguiente grupo de host disponible y
grupo de puertos.
1. Navegue a Administración --> Configuración.
2. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
3. En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y haga clic en el grupo customhostgroup0. En el lado derecho, ingrese la dirección IP del
pfSense firewall y haga clic en la marca de verificación para guardar.
4. En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione el grupo customportgroup0 y luego haga clic en udp. En el lado derecho, ingrese
9001 y haga clic en la marca de verificación para guardar.
5. En el lado izquierdo, vaya al firewall, seleccione función y luego seleccione el tipo de nodo que recibirá los registros de pfSense. Luego taladre la cadena -->
ENTRADA --> grupos de hosts --> grupo de hosts personalizado0 --> grupos de puertos. En el lado derecho, ingrese customportgroup0 y haga clic en la marca de verificación para
guardar.
6. Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
Una vez que se complete toda la configuración, debería poder ir a Paneles y seleccionar el panel Firewall - pfSense para ver su
registros del cortafuegos.
- 191/402 - Soluciones de cebolla de seguridad, LLC

9.7 OPNsense
9.7 OPNsense
OPNsense es un firewall abierto y gratuito que se puede encontrar en https://opnsense.org/. Al igual que pfSense, hay algunas formas diferentes en las que
puede integrar OPNsense en su implementación de Security Onion. Primero, puede configurar OPNsense para enviar registros de firewall a su
Despliegue de cebolla. También puede configurar OPNsense para enviar datos de NetFlow a su implementación de Security Onion. Finalmente, una tercera opción es
integre Suricata de OPNsense en Security Onion para que extraiga las reglas NIDS de su implementación de Security Onion y luego las envíe
Suricata alerta a Cebolla Seguridad. Las tres opciones se detallan a continuación.
9.7.1 Envío de registros de firewall de OPNsense a Security Onion
Centralice su registro enviando registros del firewall de OPNsense a su grid.
Pasos:
1. Navegue a Sistema → Configuración → Iniciar sesión en la GUI de OPNsense.
2. Haga clic en la pestaña Registro remoto.
3. Haga clic en el botón + para agregar un nuevo destino de registro remoto.
4. Configurar el registro remoto:
5. Transporte: seleccione TCP.
6. Niveles de aplicación: déjelo como predeterminado para enviar todos los registros o especifique según sea necesario.
7. Instalaciones: Deje el valor predeterminado para incluir todas las instalaciones o especifique según sea necesario.
8. Nombre de host/Dirección IP: Ingrese la dirección IP del sistema de red donde configuró la entrada de registro.
9. Puerto: Ingrese el número de puerto configurado en el sistema de red.
10. Formato: elija el formato apropiado (por ejemplo, Syslog).
11. Haga clic en Guardar para aplicar la configuración.
9.7.2 Envío de datos de OPNsense NetFlow a Security Onion
Para recopilar datos de flujo de red (similar a los registros de conexión de Zeek), configure NetFlow en OPNsense para enviar datos a su red.
Pasos:
1. Prepare su red para recibir datos de NetFlow:
2. Consulte la sección NetFlow para configurar su red para recibir datos de NetFlow.
3. Configure NetFlow en OPNsense:
4. Navegue hasta Informes → NetFlow en la GUI de OPNsense.
5. En Captura, seleccione las interfaces internas que desea monitorear.
6. Además, seleccione su interfaz WAN para monitorear el tráfico externo.
7. En Destinos, agregue un nuevo destino:
• Nombre de host/Dirección IP: ingrese la dirección IP del nodo de la red configurado para aceptar datos de NetFlow.
• Puerto: ingrese el número de puerto que configuró en el nodo de la red.
• Formato: elija la versión de NetFlow adecuada (por ejemplo, NetFlow v5 o v9).
8. Haga clic en Aplicar para guardar la configuración.
- 192/402 - Soluciones de cebolla de seguridad, LLC

9.7.3 Integración de OPNsense Suricata en Security Onion
9.7.3 Integración de OPNsense Suricata en Security Onion
Puede integrar su firewall OPNsense con su sistema Security Onion Grid para utilizarlo como un sensor improvisado, permitiendo la administración de
Suricata NIDS gobierna a través de Detecciones. Esto es particularmente útil para organizaciones a las que les resulta difícil instalar un TAP de red en su
conexión de salida.
Nota
Cuando OPNsense descarga reglas de Security Onion, solo puede habilitar y deshabilitar reglas. Se ignoran los ajustes de umbral.
Requisitos previos
• Acceso Security Onion Manager: Accede al administrador de tu grid.
• Derechos administrativos: capacidad de modificar la configuración en la GUI de OPNsense.
• Acceso SSH: debe tener acceso SSH a su firewall OPNsense.
Compartir reglas NIDS
El módulo Detecciones ahora puede administrar reglas NIDS para instancias externas de Suricata. Consulte la sección NIDS para obtener instrucciones detalladas.
sobre cómo configurar esto.
Importar cebolla de seguridad CA
Para establecer una conexión segura entre su firewall OPNsense y el administrador de grid, su firewall deberá confiar en el certificado de grid.
Certificado de autoridad (CA).
Pasos:
1. Copie el certificado CA de la grilla:
2. SSH en su administrador de red.
3. Ejecute el comando cat /etc/pki/ca.crt para mostrar el certificado de CA.
4. Copie el resultado completo de ese comando.
5. Importe el certificado CA a OPNsense:
6. Inicie sesión en la GUI de OPNsense.
7. Vaya a Sistema → Confianza → Autoridades.
8. Haga clic en el botón + para agregar una nueva autoridad de certificación.
9. Establezca el Método para importar una autoridad de certificación existente.
10. Nombre descriptivo: ingrese un nombre como "Security Onion CA".
11. Datos del certificado: pegue el contenido del certificado de CA copiado.
12. Haga clic en Guardar.
Configurar el repositorio de reglas de Suricata
Dado que OPNsense no permite habilitar repositorios de terceros a través de la GUI, deberá modificar la configuración manualmente.
- 193/402 - Soluciones de cebolla de seguridad, LLC

9.7.3 Integración de OPNsense Suricata en Security Onion
Pasos:
1. Eliminar repositorios de reglas existentes:
2. Ingrese mediante SSH a su firewall OPNsense y ejecute lo siguiente:
rm -rf /usr/local/opnsense/scripts/suricata/metadata/rules/*
1. Cree un nuevo archivo de repositorio:
2. Cree y edite el archivo cebolla.xml:
vi /usr/local/opnsense/scripts/suricata/metadata/rules/onion.xml
• Pegue el siguiente contenido en el archivo, reemplazando YOURMANAGER con el nombre de host o la dirección IP de su administrador de grid:
<?xml version="1.0"?>
<ruleset documentation_url="http://docs.opnsense.org/">
<location url="https://YOURMANAGER:7789/" prefix="SecurityOnion"/>
<files>
<file description="SecurityOnion rules">all.rules</file>
<file description="SecurityOnion" url="inline::all.rules">all.rules</file>
</files>
</ruleset>
• Guarde y salga del editor.
• Actualizar conjuntos de reglas en OPNsense:
• Navegue a Servicios → Detección de intrusiones → Administración → Descargar en la GUI de OPNsense.
• Debería ver Security Onion listado como un conjunto de reglas.
• Seleccione Security Onion y haga clic en Descargar y actualizar reglas.
• Una vez actualizadas, las reglas aparecerán en la pestaña Reglas.
Actualizaciones de reglas de programación
Para mantener actualizadas sus reglas de Suricata, programe actualizaciones periódicas.
Pasos:
1. Navegue a Servicios → Detección de intrusiones → Administración → Programación.
2. Haga clic en el botón + para agregar un nuevo horario.
3. Configure el horario:
4. Descripción: Ingrese un nombre como "Actualización de la regla Suricata".
5. Expresión Cron: establezca la frecuencia cada 15 minutos.
6. Escriba: elija Actualizar y recargar reglas de detección de intrusiones.
7. Haga clic en Guardar.
OPNsense ahora descargará y recargará automáticamente las reglas cada 15 minutos.
- 194/402 - Soluciones de cebolla de seguridad, LLC

10. Visibilidad del anfitrión
10. Visibilidad del anfitrión
10.1 Descripción general de la visibilidad del host
Hoy en día, cada vez más tráfico de nuestra red está cifrado y eso es bueno para la privacidad, pero es un punto ciego para nosotros como
defensores. La visibilidad del anfitrión puede ayudar a llenar esos puntos ciegos. Puede enviar registros de host a Security Onion a través de su elección de Elastic Agent o
Registro del sistema:
• Elija Elastic Agent para obtener telemetría completa si puede instalar un agente en el host.
• Elija Syslog si no puede instalar un agente pero el dispositivo admite el envío de syslog estándar. Los ejemplos incluyen firewalls, conmutadores, enrutadores,
y otros dispositivos de red.
Para los puntos finales de Windows, opcionalmente puede aumentar el registro estándar de Windows con Sysmon.
- 195/402 - Soluciones de cebolla de seguridad, LLC

10.2 Agente elástico
10.2 Agente elástico
De https://www.elastic.co/elastic-agent:
Con Elastic Agent puedes recopilar todo tipo de datos desde cualquier lugar con un único agente unificado por host. Una cosa es instalar, configurar y
escala. Cada nodo de Security Onion utiliza Elastic Agent para transportar registros a Elasticsearch. También puede implementar Elastic Agent en su
puntos finales para transportar registros a su implementación de Security Onion.
Nota
Para recibir registros del Elastic Agent, Security Onion debe ejecutar Logstash. El modo de evaluación y el modo de importación no ejecutan Logstash,
por lo que necesitará una implementación independiente o distribuida completa. En una implementación distribuida, los nodos sensores no ejecutan Logstash, por lo que deberá
configure agentes para enviar a su administrador o nodos receptores. Para obtener más información, consulte la sección Arquitectura.
Para implementar un agente Elastic en un endpoint, vaya a la página SOCDownloads y descargue el agente Elastic adecuado para el sistema operativo de
ese punto final.
Advertencia
Dentro de la interfaz de Elastic Fleet, hay un botón Agregar agente; no se recomienda utilizar este método en particular para instalar Elastic Agent.
ya que requiere mucha más configuración manual.
No olvide permitir que el agente se conecte a través del firewall yendo a Administración --> Configuración --> firewall --> grupos de hosts.
Una vez allí, seleccione la opción elastic_agent_endpoint.
- 196/402 - Soluciones de cebolla de seguridad, LLC

10.2.1 Opciones de agente elástico (no MSI)
Nota
¡Mira nuestro video de Elastic Agent en https://youtu.be/cGmQMsFuAvw!
10.2.1 Opciones de agente elástico (no MSI)
Hay opciones adicionales de tiempo de ejecución del instalador:
-token=$TOKEN
Esta opción le permite anular la política del agente que el instalador utiliza de forma predeterminada. El token proviene de la interfaz de Elastic Fleet en
Fichas de inscripción.
-flota=$FLEETHOST
Esta opción le permite anular el host de flota predeterminado utilizado para la inscripción.
-delay-enroll=verdadero|falso
El valor predeterminado es falso. Si se establece en verdadero, agrega el indicador de inscripción retrasada incorporado al inscribir al agente.
-tiempo de espera=$MINUTOS
El valor predeterminado es 5 minutos.
10.2.2 Opciones de agente elástico (MSI)
Cuando se utiliza el tiempo de ejecución del instalador MSI, las opciones son:
TOKEN=$TOKEN
Esta opción le permite anular la política del agente que el instalador utiliza de forma predeterminada. El token proviene de la interfaz de Elastic Fleet en
Fichas de inscripción.
FLOTA=$FLEETHOST
Esta opción le permite anular el host de flota predeterminado utilizado para la inscripción.
DELAYENROLL=verdadero|falso
Esta opción por defecto es falsa. Si se establece en verdadero, agrega el indicador de inscripción retrasada incorporado al inscribir al agente.
TIEMPO DE ESPERA=$MINUTOS
El valor predeterminado es 5 minutos.
10.2.3 Instalación del Agente elástico en Linux
Si implementa Elastic Agent en un host Linux, haga que el archivo sea ejecutable y luego ejecútelo usando sudo:
chmod +x ./so-elastic-agent_linux_amd64
sudo ./so-elastic-agent_linux_amd64
10.2.4 Instalación del Agente Elastic en macOS
Si implementa Elastic Agent en macOS, deberá seguir algunos pasos. Primero, elimine el atributo de cuarentena. Luego, crea el archivo.
ejecutable. Finalmente, ejecute el archivo usando sudo:
xattr -d com.apple.quarantine ./so-elastic-agent_darwin_amd64
chmod +x ./so-elastic-agent_darwin_amd64
sudo ./so-elastic-agent_darwin_amd64
- 197/402 - Soluciones de cebolla de seguridad, LLC

10.2.5 Instalación de Elastic Agent en Windows a través de MSI
Una vez que se haya completado el instalador, revise los documentos de Elastic para su versión de macOS y apruebe la configuración requerida (extensión del sistema y
acceso completo al disco) como se muestra en https://www.elastic.co/guide/en/security/current/elastic-endpoint-deploy-reqs.html.
10.2.5 Instalación de Elastic Agent en Windows a través de MSI
Al implementar a través de MSI, la instalación puede ser tan simple como hacer doble clic en el instalador de MSI. Si necesita indicadores de tiempo de ejecución adicionales, utilice
msiexec /i:
msiexec /i so-elastic-agent_windows_amd64_msi TOKEN=$TOKEN TIMEOUT=10m
10.2.6 Registros
Una vez que el agente comience a enviar registros, debería poder encontrarlos en Dashboards, Hunt o Kibana.
10.2.7 Gestión
Puede administrar sus agentes usando Elastic Fleet.
10.2.8 Consultas en vivo
Puede consultar a sus agentes en tiempo real utilizando Osquery Manager.
10.2.9 Integraciones
Puede leer más sobre integraciones en la sección Elastic Fleet y en https://docs.elastic.co/integrations.
10.2.10 Reinstalación
Si por algún motivo necesita desinstalar y reinstalar Elastic Agent en uno de sus miembros de Security Onion Grid, puede hacerlo de la siguiente manera:
desinstalación de sudo elastic-agente
sudo salt-call state.apply elasticfleet.install_agent_grid
10.2.11 Más información
Nota
Para obtener más información sobre Elastic Agent, consulte https://www.elastic.co/guide/en/fleet/current/fleet-overview.html.
- 198/402 - Soluciones de cebolla de seguridad, LLC

10.3 Registro del sistema
10.3 Registro del sistema
Si desea enviar syslog desde otros dispositivos, debe verificar si el dispositivo tiene una integración de Elastic Agent existente. Si es así, utilizando el
La integración de Elastic Agent debería proporcionar cierto análisis de forma predeterminada.
Si su dispositivo no tiene una integración de Elastic Agent existente, aún puede recopilar syslog estándar. Comience yendo a Administración -->
Configuración --> firewall --> grupos de hosts.
Luego elija la opción syslog para permitir que el puerto atraviese el firewall. Si envía syslog a un sensor, consulte los ejemplos en el firewall
sección. Si necesita agregar un análisis personalizado para esos registros de syslog, le recomendamos utilizar el análisis de ingesta de Elasticsearch.
También tenga en cuenta que si está monitoreando el tráfico de red con Zeek, de forma predeterminada detectará cualquier syslog en ese tráfico de red y lo registrará incluso si
ese syslog no estaba destinado a ese nodo Security Onion en particular.
- 199/402 - Soluciones de cebolla de seguridad, LLC

10.4 Sistema
10.4 Sistema
Desde https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon:
System Monitor (Sysmon) es un servicio del sistema de Windows y un controlador de dispositivo que, una vez instalado en un sistema, permanece residente en todo el sistema.
se reinicia para monitorear y registrar la actividad del sistema en el registro de eventos de Windows. Proporciona información detallada sobre la creación de procesos, la red
conexiones y cambios en el tiempo de creación del archivo. Al recopilar los eventos que genera utilizando Windows Event Collection o agentes SIEM y
analizándolos posteriormente, puede identificar actividades maliciosas o anómalas y comprender cómo operan los intrusos y el malware en su
red.
10.4.1 Descargas
Puede descargar Sysmon de Microsoft en https://download.sysinternals.com/files/Sysmon.zip.
Una vez que haya descargado Sysmon, probablemente también desee descargar una configuración de Sysmon para usarla como punto de partida. Aquí hay algunos
opciones para elegir:
• https://github.com/Neo23x0/sysmon-config
• https://github.com/SwiftOnSecurity/sysmon-config
• https://github.com/olafhartong/sysmon-modular
10.4.2 Transporte
Los registros de Sysmon se pueden recopilar y transportar mediante Elastic Agent. Confirma que tu configuración NO utiliza Elastic Sysmon
módulo. Security Onion hará todo el análisis necesario.
10.4.3 Visualizaciones
Una vez que Security Onion recibe y analiza los datos de Sysmon, puede buscar esos datos y visualizarlos a través de Dashboards, Hunt o Kibana. cada uno
de estas interfaces tienen al menos un panel o consulta diseñada específicamente para datos de Sysmon.
10.4.4 Más información
Nota
Para obtener más información sobre Sysmon, consulte: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
TrustedSec tiene una excelente guía comunitaria sobre Sysmon: https://github.com/trustedsec/SysmonCommunityGuide
- 200/402 - Soluciones de cebolla de seguridad, LLC

11. Integraciones de terceros
11. Integraciones de terceros
Además de la visibilidad de la red y del host, es posible que desee obtener datos de otros sistemas de terceros. Puedes hacerlo a través de Elastic
integraciones que soportan muchos de los productos y servicios más comunes. Puede leer más sobre las integraciones de Elastic en https://
docs.elastic.co/integrations.
Advertencia
Elastic proporciona las integraciones de terceros y el equipo de Security Onion no las prueba específicamente. Soporte proporcionado por Security Onion
El equipo para integraciones de terceros se considera el mejor esfuerzo.
11.1 Agregar una integración
Se pueden agregar nuevas integraciones a las políticas existentes para proporcionar una mayor visibilidad y un seguimiento más completo.
consejo
Al agregar una nueva integración, es importante que la agregue a una política adecuada.
Si una integración extrae los datos, debes agregarlos a la política de Fleet Server. Dependiendo de la complejidad y el volumen de registros, podría tener sentido
levante un nodo de flota y agréguele sus integraciones.
Si una integración recibe datos enviados (por ejemplo: recepción de syslog), considere agregarlos a la política de Fleet Server. Si eso no es factible, entonces
puede agregarlo a la política de Nodos de la red, pero asegúrese de configurar las reglas del firewall correctamente para no abrir puertos en todos sus nodos.
Para agregar una integración a una política existente:
• Desde la página principal de la Flota, haga clic en la pestaña Políticas del agente.
• Seleccione la política de agente deseada.
• Haga clic en el botón Agregar integración.
• Siga los pasos para agregar la integración.
Nota
Si la integración está diseñada para escuchar en un puerto para recibir datos, lo más probable es que de forma predeterminada escuche solo en el host local. Dependiendo de como tu
está enviando datos a la integración, es posible que deba cambiarlo a 0.0.0.0 para que pueda recibir datos de otros hosts.
Para ver ejemplos de este proceso, consulte las secciones NetFlow y pfSense. La sección pfSense incluye un enlace a un vídeo que ilustra
el proceso.
11.2 Agregar una integración personalizada
Se puede agregar una integración personalizada agregando una integración como la integración de Registros personalizados. Puede especificar varias configuraciones relativas
a la fuente de datos y definir acciones adicionales a realizar.
- 201/402 - Soluciones de cebolla de seguridad, LLC

11.3 Gestión de actualizaciones de integración
11.3 Gestión de actualizaciones de integración
consejo
De forma predeterminada, las integraciones no se mantienen actualizadas automáticamente. Esto evita posibles tiempos de inactividad en la ingesta de registros si hay un problema con la última versión.
paquete o si el paquete más reciente requiere una actualización manual de su configuración de integración. Si desea actualizar automáticamente
integraciones, puede cambiar este comportamiento a través de Administración -> Configuración -> elasticfleet -> config -> auto_upgrade_integrations.
Para buscar integraciones que tengan actualizaciones disponibles:
• Vaya a Elastic Fleet.
• En la esquina superior izquierda, haga clic en el menú.
• En Gestión, seleccione Integraciones.
• Haga clic en la pestaña Integraciones instaladas.
• Revise las integraciones enumeradas en Actualizaciones disponibles.
11.4 Gestión de plantillas de índice de integración de terceros
Las plantillas de índice para integraciones de terceros se pueden administrar como se describe en la sección Elasticsearch, pero primero las integraciones_administradas deben
actualizarse navegando a Administración --> Configuración --> administrador --> Managed_integrations.
11.5 Integraciones admitidas
La versión actual de Security Onion admite todas las integraciones de Elastic estándar, como se muestra en https://docs.elastic.co/integrations.
11.6 Más información
Nota
Puede leer más sobre las integraciones de Elastic en https://docs.elastic.co/integrations.
- 202/402 - Soluciones de cebolla de seguridad, LLC

12. Reglas
12. Reglas
12.1 Descripción general de las reglas
Security Onion admite tres tipos principales de reglas: NIDS, Sigma y YARA. Puede gestionar los tres tipos a través de Detecciones.
- 203/402 - Soluciones de cebolla de seguridad, LLC

12.2 NIDS
12.2 NIDS
Las reglas NIDS (Sistema de detección de intrusiones en la red) se cargan en Suricata para monitorear el tráfico de la red en busca de actividades sospechosas o dignas de mención.
Las reglas NIDS activas generan alertas que se pueden encontrar en Alertas.
12.2.1 Gestión de reglas NIDS existentes
Puede gestionar las reglas NIDS existentes mediante Detecciones. Hay dos maneras de hacerlo:
• Desde la interfaz principal de Detecciones, puede buscar la detección deseada y hacer clic en el icono de binoculares.
• Desde la interfaz de Alertas, puede hacer clic en una alerta y luego hacer clic en el elemento del menú Detección de melodía.
Una vez que haya utilizado uno de estos métodos para llegar a la página de detalles de la detección, puede verificar el campo Estado en la esquina superior derecha y usar
el control deslizante para habilitar o deshabilitar la detección.
Para ajustar la detección:
• Haga clic en la pestaña Sintonización
• Haga clic en el botón azul +
• Seleccione el tipo de sintonización (Modificar, Suprimir o Umbral)
• Complete los valores solicitados
• Haga clic en el botón CREAR
- 204/402 - Soluciones de cebolla de seguridad, LLC

12.2.2 Activación y desactivación con Regex
12.2.2 Activación y desactivación con Regex
Las reglas NIDS se pueden habilitar o deshabilitar en Detecciones usando patrones de expresiones regulares. Navegue hasta Administración de SOC - Configuración y filtre por
regex, luego profundice en SOC --> configuración --> servidor --> módulos --> suricataengine --> enableRegex o enableRegex.
El tipo de expresión regular es Google RE2: https://github.com/google/re2/wiki/Syntax
En ETOPEN, las categorías se anteponen al nombre de la regla. Por ejemplo, la regla ET EXPLOIT PHP-Live-Chat Get Shell Attempt Inbound está en
la categoría ET EXPLOIT. Supongamos que desea desactivar las categorías ET EXPLOIT y ET MALWARE pero NO ET EXPLOIT_KIT.
categoría. Utilizaría los siguientes patrones de expresiones regulares:
EXPLOTACIONES ET
ET MALWARE
\s es un atajo para espacios en blanco y es útil en esta situación para asegurarnos de que solo coincidamos con las categorías específicas que queremos.
desactivar.
Si una detección coincide con una expresión regular habilitada y deshabilitada, está habilitada. Si el estado de una detección se cambia a través de Detecciones
interfaz pero actualmente coincide con un patrón de expresiones regulares, el cambio iniciado desde la interfaz de Detecciones se revierte y se muestra un mensaje.
mostrado.
Las operaciones de activación y desactivación que se basan en patrones de expresiones regulares se activan durante la actualización diaria de la regla. Si ha realizado un cambio en el
patrones de expresiones regulares y me gustaría implementarlo más inmediatamente:
• En Configuración de red, haga clic en el botón SINCRONIZAR RED y espere unos 5 minutos hasta que se complete.
• Navegue hasta Detecciones, haga clic en el menú Opciones, seleccione Suricata en el menú desplegable, haga clic en el botón ACTUALIZACIÓN COMPLETA y luego espere.
para completar.
• Actualice la página Detecciones y debería ver que los estados de las reglas relevantes han cambiado.
Nota
Si se aplica una expresión regular deshabilitada a una regla de bit de flujo de establecimiento y esa regla aún es necesaria, se escribirá en el archivo de reglas como habilitada, pero no se generará ninguna alerta.
- 205/402 - Soluciones de cebolla de seguridad, LLC

12.2.3 Anulaciones de ajuste
12.2.3 Anulaciones de ajuste
Las anulaciones le permiten ajustar el comportamiento de las reglas sin modificar la regla misma. Security Onion admite tres tipos de anulaciones de reglas NIDS.
Anulación de umbral
La anulación de umbral limita la frecuencia con la que una regla genera alertas. Utilícelo cuando una regla genere demasiadas alertas y desee reducirlas.
volumen sin desactivar la detección.
Los umbrales se escriben en el archivo umbral.conf de Suricata y controlan la frecuencia de alerta según el recuento de ocurrencias y la ventana de tiempo.
• Tipo de umbral: límite, umbral o ambos
• límite: alerta como máximo N veces por ventana de tiempo
• umbral: alerta solo después de N ocurrencias por ventana de tiempo
• ambos: alerta una vez por ventana de tiempo después de N ocurrencias
• Seguimiento: by_src o by_dst: si se debe realizar el seguimiento por IP de origen o IP de destino
• Count: Número de ocurrencias para la lógica de umbral (debe ser > 0)
• Segundos: ventana de tiempo en segundos (debe ser > 0)
Ejemplo: limitar las alertas a una vez por hora por IP de origen:
Tipo de umbral: límite Pista: by_src Conteo: 1 Segundos: 3600
Resultado en umbral.conf:
umbral gen_id 1, sig_id 2001219, límite de tipo, seguimiento por_src, recuento 1, segundos 3600
Suprimir anulación
La anulación de supresión silencia las alertas de direcciones IP o redes específicas. Utilícelo cuando una regla genere falsos positivos a partir de datos conocidos.
buenas fuentes.
Las supresiones se escriben en el archivo umbral.conf de Suricata. Cuando el tráfico coincide con la regla y se origina (o tiene como destino) el
IP especificada, no se genera ninguna alerta.
• Seguimiento: by_src o by_dst: suprimir según la IP de origen o la IP de destino
• IP: dirección IP, red CIDR o variable Suricata (por ejemplo, 192.168.1.100, 10.0.0.0/8 o $SCANNERS)
Ejemplo: suprimir alertas de un escáner de vulnerabilidades:
Pista: by_src IP: 192.168.50.10
Resultado en umbral.conf:
suprimir gen_id 1, sig_id 2001219, seguimiento por_src, ip 192.168.50.10
Ejemplo: Suprimir usando una variable Suricata:
Pista: by_src IP: $SCANNERS
Resultado en umbral.conf:
suprimir gen_id 1, sig_id 2001219, seguimiento by_src, ip $SCANNERS
Modificar anulación
La anulación de modificación le permite cambiar el contenido de una regla de Suricata utilizando la coincidencia de patrones de expresiones regulares. Esto es útil para sintonizar
reglas sin crear copias personalizadas.
- 206/402 - Soluciones de cebolla de seguridad, LLC

12.2.3 Anulaciones de ajuste
Cómo funciona
La anulación de modificación aplica una búsqueda y reemplazo de expresiones regulares al contenido de la regla en el momento de la sincronización. La regla original en la base de datos no cambia; el
La modificación se aplica al escribir el archivo de reglas que lee Suricata.
• Regex: un patrón de expresión regular compatible con Go para igualar
• Valor: la cadena de reemplazo literal
Nota
La cadena de reemplazo se trata como texto literal. No se admiten referencias anteriores (\1, \2, etc.). Si necesita capturar parte del partido, utilice
en su lugar, múltiples anulaciones específicas.
Ejemplos
Excluir rango de IP de la variable
Para excluir $DC_SERVERS de $EXTERNAL_NET:
Regex: \$EXTERNAL_NET Valor: [$EXTERNAL_NET,!$DC_SERVERS]
Antes:
alerta tcp $EXTERNAL_NET cualquiera -> $HOME_NET cualquiera (msg:"Ejemplo"; sid:1001;)
Después:
alerta tcp [$EXTERNAL_NET,!$DC_SERVERS] cualquiera -> $HOME_NET cualquiera (msg:"Ejemplo"; sid:1001;)
Cambiar segundos de umbral
Para cambiar el umbral de una regla de 60 segundos a 3600:
Regex: segundos \d+ Valor: segundos 3600
Antes:
alerta http cualquiera cualquiera -> cualquiera cualquiera (msg:"Prueba"; umbral: límite de tipo, seguimiento por_src, recuento 1, segundos 60; sid:1001;)
Después:
alerta http cualquiera cualquiera -> cualquiera cualquiera (msg:"Prueba"; umbral: límite de tipo, seguimiento por_src, recuento 1, segundos 3600; sid:1001;)
Modificar coincidencia de contenido
Para cambiar un valor de coincidencia de contenido específico:
Regex: contenido:"67:98:30 Valor: contenido:"88:98:30
Antes:
alerta tls cualquiera cualquiera -> cualquiera cualquiera (msg:"Certificado SSL"; contenido:"67:98:30:81:90"; sid:1001;)
Después:
alerta tls cualquiera cualquiera -> cualquiera cualquiera (msg:"Certificado SSL"; contenido:"88:98:30:81:90"; sid:1001;)
- 207/402 - Soluciones de cebolla de seguridad, LLC

12.2.4 Agregar nuevas reglas NIDS
Limitaciones
• Sin referencias anteriores: no se admiten referencias anteriores de estilo Python (\1, \2) en la cadena de reemplazo. La sincronización fallará con un error si
estos son detectados.
• Excepción PCRE: Se permiten secuencias de barra invertida dentro de las secciones pcre:"...", ya que son una sintaxis PCRE válida.
• Reemplazo literal: el valor de reemplazo siempre se trata como texto literal. Los caracteres regex especiales en el reemplazo no tienen
significado especial.
12.2.4 Agregar nuevas reglas NIDS
Para agregar una nueva regla NIDS, vaya a la página principal de Detecciones y haga clic en el botón azul + entre Opciones y la barra de consulta. Aparecerá un formulario
donde podrás:
1. Haga clic en el menú desplegable Idioma y seleccione Suricata.
2. Opcionalmente, especifique una licencia.
3. Añade la firma.
4. Haga clic en el botón CREAR y la detección debería implementarse en su cuadrícula en el siguiente ciclo de 15 minutos.
12.2.5 Frecuencia de actualización
De forma predeterminada, Security Onion busca nuevas reglas NIDS cada 24 horas. Puede cambiar este valor de la siguiente manera:
• Navegue a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• Navegue a SOC --> configuración --> servidor --> módulos --> suricataengine --> communityRulesImportFrequencySeconds.
- 208/402 - Soluciones de cebolla de seguridad, LLC

12.2.6 Permitir acceso externo a las reglas NIDS
12.2.6 Permitir acceso externo a las reglas NIDS
Puede habilitar el acceso externo a las reglas NIDS administradas por Detecciones. Esto es útil al configurar OPNsense u otros dispositivos de red para
extraiga las reglas NIDS de su implementación de Security Onion. Puedes hacer esto de la siguiente manera:
• Navegue a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• Navegue a Nginx --> configuración --> external_suricata.
• En el lado derecho de la página, cambie el valor a verdadero y luego haga clic en la marca de verificación para guardar la nueva configuración.
• Puede esperar la próxima actualización de Grid o hacer clic en el botón SINCRONIZAR GRID en Opciones.
• Una vez que el grid esté completamente sincronizado, el Manager debe escuchar en el puerto 7789 las conexiones https de los hosts definidos en el
grupo de host external_suricata.
12.2.7 Configurar conjuntos de reglas
Security Onion le permite configurar múltiples conjuntos de reglas NIDS. Puede administrar estos conjuntos de reglas navegando a Administración -->
Configuración --> SOC --> configuración --> servidor --> módulos --> suricataengine --> reglassetSources. Esta configuración también está disponible a través del
Enlaces rápidos de configuración.
Hay dos perfiles de configuración:
• predeterminado: se utiliza para implementaciones estándar (sin Airgap)
• airgap: se utiliza para implementaciones de Airgap
Si su sistema está en modo Airgap, el perfil de configuración de Airgap se utilizará automáticamente; de lo contrario, se utilizará el valor predeterminado.
Dentro de esta configuración, puede habilitar conjuntos de reglas adicionales, agregar conjuntos de reglas personalizados o deshabilitar los existentes. Cuando guardas un conjunto de reglas
cambio de configuración y aplicar el estado SOC, Security Onion detectará el cambio y sincronizará automáticamente todos los conjuntos de reglas configurados dentro de 15
minutos.
Lista mantenida por OISF de conjuntos de reglas compatibles con Suricata: https://github.com/OISF/suricata-intel-index
Nota
Cada conjunto de reglas debe tener un nombre exclusivo. Los nombres duplicados provocarán errores de sincronización.
- 209/402 - Soluciones de cebolla de seguridad, LLC

12.2.7 Configurar conjuntos de reglas
Opciones de configuración del conjunto de reglas
Cada origen de conjunto de reglas tiene las siguientes opciones de configuración:
• Nombre del conjunto de reglas: obligatorio. El nombre único de este conjunto de reglas (por ejemplo, "Amenazas emergentes", "ABUSECH-SSLBL", "reglas locales"). este es el nombre
mostrado en la interfaz de usuario.
• Descripción: descripción opcional del conjunto de reglas.
• Habilitado: Requerido. Si se establece en falso, se eliminarán las reglas existentes y las anulaciones de este conjunto de reglas.
• Clave de Licencia: Opcional. Requerido para conjuntos de reglas comerciales como ET Pro.
• Tipo de fuente: Requerido. Ya sea URL (descarga reglas de HTTPS) o directorio (lee reglas del sistema de archivos local).
• Ruta de origen: obligatoria. La URL completa o la ruta del directorio/archivo según el tipo de fuente. Consulte Formatos de ruta de origen admitidos a continuación.
• Excluir archivos: opcional. Lista de nombres de archivos de reglas para excluir, separados por comas (por ejemplo, *eliminados*, *retirados*).
• Licencia de conjunto de reglas: obligatoria. El tipo de licencia para este conjunto de reglas (por ejemplo, "BSD", "Comercial", "CC0-1.0").
• Sólo lectura: opcional, el valor predeterminado es falso. Cuando está habilitado, evita la modificación del contenido de las reglas a través de la interfaz de usuario; los usuarios aún pueden habilitar/deshabilitar las reglas
y agregar anulaciones de ajuste (suprimir, umbral, modificar). Utilícelo para conjuntos de reglas administrados por el proveedor en los que desee conservar la regla original.
texto.
• Eliminar sin referencia: opcional, el valor predeterminado es falso. Controla lo que sucede con las reglas en Elasticsearch cuando se eliminan del origen.
• falso (predeterminado): las reglas eliminadas del origen permanecen en Elasticsearch. Esto preserva las modificaciones del usuario y evita datos accidentales.
pérdida.
• verdadero: las reglas eliminadas del origen se eliminan automáticamente de Elasticsearch. Úselo cuando la fuente tenga autoridad (por ejemplo, git-
conjuntos de reglas gestionados).
Advertencia
Cambiar esta configuración de falso a verdadero eliminará cualquier regla que ya no exista en la fuente. Si tiene reglas huérfanas (reglas en ES pero no
en la fuente), se eliminarán permanentemente en la siguiente sincronización.
Formatos de ruta de origen admitidos
Para tipo de fuente de URL:
• URL a un archivo .rules (por ejemplo, https://rules.emergingthreats.net/open/suricata-7.0.3/emerging-all.rules)
• URL a un archivo .tar.gz (por ejemplo, https://rules.emergingthreats.net/open/suricata-7.0.3/emerging-all.rules.tar.gz)
Para el tipo de fuente del directorio:
• Directorio que contiene múltiples archivos .rules (por ejemplo, /nsm/rules/custom-local-repos/local-Suricata-import/)
• Directorio que contiene un único archivo .rules
• Ruta directa a un archivo .rules (por ejemplo, /nsm/rules/custom-local-repos/local-Suricata-import/import.rule)
• Ruta directa a un archivo .tar.gz (por ejemplo, /nsm/rules/custom-local-repos/local-Suricata-import/import.tar.gz)
- 210/402 - Soluciones de cebolla de seguridad, LLC

12.2.8 Configuraciones de conjuntos de reglas comunes
Opciones de origen de URL
Cuando se utiliza URL como tipo de fuente, hay opciones adicionales disponibles:
• URL Hash: URL a un archivo hash (.md5 o .sha256) para verificar el conjunto de reglas descargado.
• URL de proxy: URL de proxy HTTP/HTTPS para descargar el conjunto de reglas. (por ejemplo, http://192.168.1.50:3128)
• Nombre de usuario de proxy: nombre de usuario de autenticación de proxy.
• Contraseña de proxy: Contraseña de autenticación de proxy.
• Ruta de CA de proxy: ruta al archivo de certificado de CA para la verificación del proxy MITM (por ejemplo, /opt/so/saltstack/local/salt/suricata/files/
conjunto de reglas_ca.crt)
Conjuntos de reglas predeterminados
Amenazas emergentes (ET Open / ET Pro) Security Onion incluye el conjunto de reglas Abiertas de amenazas emergentes de forma predeterminada. Para cambiar a ET Pro
(comercial), edite el conjunto de reglas de Amenazas emergentes e ingrese su clave de licencia en el campo Clave de licencia. Haga clic en la marca de verificación verde para guardar, luego
aplicar el estado SOC. Deje la clave de licencia vacía para las reglas ET Open (gratuitas).
• Optimizado para Suricata
• ET Open es gratuito, ET Pro requiere una tarifa de licencia por sensor
Para obtener más información, consulte: - https://rules.emergingthreats.net/open/ - https://www.proofpoint.com/us/threat-insight/et-pro-ruleset
Lista negra de SSL de Abuse.ch (ABUSECH-SSLBL) Lista negra de certificados SSL de Abuse.ch. Solo disponible en versiones que no son Airgap, deshabilitado de forma predeterminada.
Para obtener más información, consulte: - https://sslbl.abuse.ch/
Reglas locales Una fuente de conjunto de reglas basada en directorio para reglas locales personalizadas. Las reglas se leen desde /nsm/rules/custom-local-repos/local-Suricata.
Este conjunto de reglas está habilitado de forma predeterminada con Solo lectura configurado en falso, lo que le permite editar las reglas directamente una vez que se importan. Tenga en cuenta que si
el archivo .rules local permanece en el disco en esta ubicación, cada sincronización intentará volver a importar las reglas y potencialmente sobrescribir cualquier cambio realizado.
dentro de la interfaz web.
Conjuntos de reglas de metadatos de Suricata
Cuando Suricata se configura como motor de metadatos (en lugar de Zeek), dos conjuntos de reglas adicionales quedan disponibles:
SO_EXTRACTIONS Reglas de extracción que controlan qué tipos de archivos extrae Suricata del tráfico de red para que Strelka los analice. Este conjunto de reglas es
importado y habilitado de forma predeterminada cuando Suricata es el motor de metadatos.
SO_FILTERS Reglas de filtrado que controlan qué metadatos registra Suricata. Úselos para reducir el registro de metadatos innecesarios. Este conjunto de reglas es
importado pero deshabilitado de forma predeterminada cuando Suricata es el motor de metadatos.
12.2.8 Configuraciones de conjuntos de reglas comunes
Esta sección proporciona ejemplos de configuración para escenarios de implementación comunes.
12.2.9 ET Pro en entornos Airgap
Para implementaciones de Airgap que utilizan reglas ET Pro (comerciales), debe transferir manualmente el conjunto de reglas a su Security Onion Manager, ya que
No se puede descargar de Internet.
Requisitos previos:
• Clave de licencia ET PRO válida
• Un sistema con acceso a Internet para descargar el conjunto de reglas.
- 211/402 - Soluciones de cebolla de seguridad, LLC

12.2.9 ET Pro en entornos Airgap
Procedimiento:
• Descargue el conjunto de reglas ET PRO (en un sistema conectado a Internet)
Utilice su clave de licencia para descargar el conjunto de reglas más reciente:
# Reemplace YOUR_LICENSE_KEY con su clave de licencia ET PRO real
curl -o etpro.rules.tar.gz \
"https://rules.emergingthreatspro.com/YOUR_LICENSE_KEY/suricata-7.0.3/etpro.rules.tar.gz"
• Transferir al administrador Airgapped
Utilice su método de transferencia de archivos aprobado para copiar el archivo al nodo Manager.
• Colocar el conjunto de reglas en el Manager
Copie el archivo a un directorio accesible por SOC:
sudo cp etpro.rules.tar.gz /nsm/rules/custom-local-repos/local-etpro-Suricata/
sudo chown -R socore:socore /nsm/rules/custom-local-repos/local-etpro-Suricata
• Configurar la fuente del conjunto de reglas
Navegue a Administración --> Configuración --> SOC --> config --> servidor --> módulos --> suricataengine --> reglassetSources.
Modifique el conjunto de reglas existente sobre amenazas emergentes (recomendado):
• Clave de licencia: YOUR_LICENSE_KEY
También puede crear una nueva fuente de conjunto de reglas (asegúrese de deshabilitar el conjunto de reglas de amenazas emergentes existente):
• Nombre del conjunto de reglas: ETPRO-Airgap
• Tipo de fuente: directorio
• Ruta de origen: /nsm/rules/custom-local-repos/local-etpro-Suricata/etpro.rules.tar.gz
• Sólo lectura: verdadero (recomendado: conserva el contenido de las reglas del proveedor)
• Eliminar sin referencia: verdadero (recomendado: elimina las reglas obsoletas cuando actualiza el archivo)
• Licencia de conjunto de reglas: Comercial
• Habilitado: verdadero
• Aplicar configuración y sincronización
Guarde la configuración y aplique el estado SOC. Luego espera la siguiente sincronización automática (hasta 15 minutos) o activa una sincronización manual:
• Navegar a Detecciones
• Haga clic en el menú Opciones
• Seleccionar motor Suricata
• Haga clic en ACTUALIZACIÓN COMPLETA
Actualización de reglas:
Para actualizar sus reglas de ET Pro en un entorno Airgap:
• Descargue la última versión de etpro.rules.tar.gz en un sistema conectado a Internet
• Transferencia al Manager con espacio de aire
• Reemplazar el archivo existente:
sudo cp etpro.rules.tar.gz /nsm/rules/custom-local-repos/local-etpro-Suricata/
• Espere la siguiente sincronización automática o active una ACTUALIZACIÓN COMPLETA manual
- 212/402 - Soluciones de cebolla de seguridad, LLC

12.2.10 Manejo de dependencias de bits de flujo
Con Eliminar sin referencia: verdadero, las reglas que se eliminaron en la nueva versión se limpiarán automáticamente de Elasticsearch.
12.2.10 Manejo de dependencias de bits de flujo
Descripción general
Las reglas de Suricata pueden usar flowbits para compartir el estado entre reglas. Un patrón común es que una regla detecte una condición inicial y "establezca" un bit de flujo,
mientras que otras reglas verifican si ese bit de flujo está configurado antes de alertar. Esto crea una dependencia entre las reglas.
Security Onion administra automáticamente estas dependencias para garantizar que las reglas habilitadas funcionen correctamente, incluso cuando deshabilita las relacionadas.
reglas.
Cómo funcionan los bits de flujo
Los Flowbits permiten que las reglas se comuniquen dentro de un único flujo de red:
• Las reglas de establecimiento utilizan flowbits:set,name para marcar un flujo
• Las reglas de obtención utilizan flowbits:isset,<nombre> para comprobar si se marcó un flujo.
Por ejemplo, una detección de malware podría funcionar así:
• Regla A (establecedor): detecta el protocolo de enlace inicial de malware, establece flowbits:set,malware.detected
• Regla B (getter): detecta el comando de seguimiento, requiere flowbits:isset,malware.detected
La regla B solo alertará si la regla A ya coincidió en el mismo flujo. Si la regla A está deshabilitada, la regla B nunca podrá activarse.
Resolución automática de dependencia
Cuando deshabilita una regla que establece un bit de flujo necesario para otras reglas habilitadas, Security Onion maneja esto automáticamente:
• Se conserva su preferencia: la regla permanece marcada como "deshabilitada" en Elasticsearch y SOC.
• La regla aún se ejecuta: está incluida en el conjunto de reglas activo para que las reglas dependientes puedan funcionar.
• No se generan alertas: la opción noalert se agrega automáticamente para que la regla deshabilitada se ejecute silenciosamente.
Ejemplo
Considere estas reglas:
Nombre de regla SID Flowbit Su configuración
2012236 Bits de flujo de inicio x0Proto:set,et.x0proto deshabilitado
2012237 Bits de flujo de información del cliente x0Proto:isset,et.x0proto habilitado
2012238 x0Proto Pong flowbits:isset,et.x0proto habilitado
Aunque deshabilitó la regla 2012236, seguirá ejecutándose porque las reglas 2012237 y 2012238 dependen de ella. Sin embargo:
• La regla 2012236 no generará alertas
• Las reglas 2012237 y 2012238 alertarán normalmente cuando sus condiciones coincidan
En el archivo de reglas, verá un comentario que explica la inclusión automática:
# AUTO-ENABLED (flowbit: et.x0proto, requerido por 2 reglas): esta regla deshabilitada se ejecuta sin alerta
alerta tcp $EXTERNAL_NET cualquiera -> $HOME_NET cualquiera (msg:"x0Proto Init"; ... noalert; sid:2012236; ...)
Cuando se excluyen las reglas deshabilitadas
Una regla de establecimiento deshabilitada solo se habilita automáticamente si al menos una regla de obtención depende de ella. Si desactiva todas las reglas que verifican un bit de flujo en particular, el
La regla de establecimiento se excluirá por completo del conjunto de reglas activo.
- 213/402 - Soluciones de cebolla de seguridad, LLC

12.2.11 Bloque de sincronización
Usando el ejemplo anterior, si desactiva las tres reglas (2012236, 2012237 y 2012238), la regla 2012236 no se incluirá en las reglas.
archivo ya que ninguna regla habilitada necesita su flowbit.
12.2.11 Bloque de sincronización
Para la actualización a 2.4.200, se eliminó la dependencia de idstools y toda la funcionalidad se trasladó directamente al SOC. debido a
Debido a la complejidad de este cambio, si SOUP detecta una configuración de conjunto de reglas de Suricata no predeterminada, crea un archivo de bloque que se detiene en el futuro.
El conjunto de reglas de Suricata cambia hasta que se elimina el archivo de bloqueo.
Advertencia
Este bloque es fundamental porque si los conjuntos de reglas de Suricata se sincronizan sin que la configuración se migre correctamente, todas las reglas y anulaciones actuales en SOC
Las detecciones se eliminarán y será necesario volver a crearlas.
Para resolver este bloque, utilice el siguiente procedimiento:
• Revisar el archivo syncBlock
Inicie sesión en Manager y vea el archivo syncBlock para ver qué configuración no predeterminada se detectó:
sudo cat /opt/so/conf/soc/fingerprints/suricataengine.syncBlock
Ejemplo de salida que muestra que se detectó ET Pro:
La sincronización del conjunto de reglas de Suricata está bloqueada hasta que se elimine este archivo.
**CRÍTICO** Asegúrate de haber agregado manualmente cualquier Suricata personalizada
conjuntos de reglas a través de la configuración SOC antes de eliminar este archivo: revise la documentación
para más detalles: <https://securityonion.net/docs/nids#sync-block>
Actualización de regla so personalizada detectada (hash: 207d8918a2d963bb7dcc0f1ebf28d6f7b5778019fedf0cc36d5d0850cbd8a529)
Código ET Pro encontrado: YOUR_LICENSE_KEY
Anote los códigos de licencia o configuraciones personalizadas mencionadas; deberá ingresarlos en el siguiente paso.
• Configurar conjuntos de reglas de Suricata en SOC
Navegue a Configuración de SOC:
• Administración --> Configuración --> Enlaces Rápidos --> Configurar Conjuntos de Reglas NIDS
Hay dos perfiles de configuración:
• predeterminado: se utiliza para implementaciones estándar (sin Airgap)
• airgap: se utiliza para implementaciones de Airgap
Seleccione el perfil apropiado para su entorno.
Para configuraciones ET Pro - Sin Airgap:
• Encuentre la entrada del conjunto de reglas sobre amenazas emergentes
• Copie y pegue su código de licencia de ET Pro (que se muestra en el archivo syncBlock) en el campo Clave de licencia
Para configuraciones ET Pro - Airgap:
Siguiendo el procedimiento descrito aquí: ET Pro en entornos Airgap
Durante esta migración, es importante utilizar el perfil de configuración integrado de Emerging Threats Airgap.
Para configuraciones de proxy:
- 214/402 - Soluciones de cebolla de seguridad, LLC

12.2.11 Bloque de sincronización
Si su entorno requiere un proxy para descargar conjuntos de reglas, configure los ajustes del proxy en la entrada del conjunto de reglas:
• URL de proxy: la URL de su servidor proxy (por ejemplo, http://192.168.1.50:3128)
• Nombre de usuario de proxy/contraseña de proxy: si se requiere autenticación de proxy
• Ruta de CA de proxy: ruta al certificado de CA si se utiliza un proxy MITM
Para conjuntos de reglas personalizados:
Si tenía conjuntos de reglas personalizados configurados, agregue nuevas entradas de conjunto de reglas con el tipo de origen, la ruta de origen y otras configuraciones adecuadas. Ver
Configuración de conjuntos de reglas para más detalles.
• Guardar y sincronizar la configuración
• Haga clic en la marca de verificación verde para guardar los cambios.
• Haga clic en SINCRONIZAR SOC y espere a que se complete
• Eliminar el archivo syncBlock
Una vez guardada y sincronizada la configuración, elimine el archivo de bloqueo:
sudo rm /opt/so/conf/soc/fingerprints/suricataengine.syncBlock
• Activar una sincronización completa del conjunto de reglas
• Navegar a Detecciones
• Haga clic en el menú Opciones
• En el menú desplegable del motor, seleccione Suricata
• Haga clic en ACTUALIZACIÓN COMPLETA
• Verificar la sincronización exitosa
En aproximadamente un minuto, debería ver un mensaje de éxito: Reglas de Suricata sincronizadas correctamente.
El indicador de estado del motor debería pasar a OK.
Si la sincronización falla, haga clic en el icono en forma de cruz de falla de sincronización en la esquina superior derecha del motor Suricata para ver los detalles del error.
- 215/402 - Soluciones de cebolla de seguridad, LLC

12.3 sigma
12.3 sigma
Las reglas de Sigma se cargan en ElastAlert para monitorear los registros entrantes en busca de actividades sospechosas o dignas de mención. Las reglas Active Sigma generan alertas que
Luego se puede encontrar en Alertas.
De https://github.com/SigmaHQ/sigma:
Sigma es un formato de firma genérico y abierto que le permite describir eventos de registro relevantes de manera sencilla. El formato de la regla
es muy flexible, fácil de escribir y aplicable a cualquier tipo de archivo de registro. El objetivo principal de este proyecto es proporcionar una forma estructurada en la que
Los investigadores o analistas pueden describir los métodos de detección que alguna vez desarrollaron y hacerlos compartibles con otros. Sigma es para archivos de registro
qué es Snort para el tráfico de red y YARA es para archivos.
12.3.1 Gestión de reglas Sigma existentes
Puede administrar las reglas Sigma existentes a través de Detecciones. Hay dos maneras de hacerlo:
• Desde la interfaz principal de Detecciones, puede buscar la detección deseada y hacer clic en el icono de binoculares.
• Desde la interfaz de Alertas, puede hacer clic en una alerta y luego hacer clic en el elemento del menú Detección de melodía.
Una vez que haya utilizado uno de estos métodos para llegar a la página de detalles de la detección, puede verificar el campo Estado en la esquina superior derecha y usar
el control deslizante para habilitar o deshabilitar la detección.
Para ajustar la detección:
• Haga clic en la pestaña Sintonización
• Haga clic en el botón azul +
• Seleccione el tipo de sintonización (Filtro personalizado)
• Ingrese su filtro personalizado en el campo Filtro personalizado
• Haga clic en el botón CREAR para crear y habilitar la Anulación.
- 216/402 - Soluciones de cebolla de seguridad, LLC

12.3.2 Agregar nuevas reglas Sigma
Los filtros personalizados son identificadores de búsqueda de Sigma y se aplicarán así: "($ORIGINAL_CONDITION) y no 1 de sofilter*"
Por ejemplo, suponga que tiene un nodo IDH instalado con el servidor web HTTP habilitado. Su escaneo de vulnerabilidad nocturno se está conectando a
y generando una alerta desde Security Onion IDH - Detección de acceso HTTP. Para filtrar los intentos de conexión de este escáner, usted
agregaría el siguiente filtro personalizado a esta detección:
sofiltro:
src_ip|cidr: 192.168.55.45/32
Una vez que guarde este filtro, estará habilitado de forma predeterminada para esta detección. Al hacer clic en la pestaña Fuente de detección y luego en Convertir se mostrará
cómo se ve la nueva consulta EQL, que debería incluir un filtro para la dirección IP.
Para obtener más información sobre la sintaxis de las reglas de Sigma, consulte la documentación de Sigma en https://sigmahq.io/docs/basics/rules.html#detection.
12.3.2 Agregar nuevas reglas Sigma
Para agregar una nueva regla Sigma, vaya a la página principal de Detecciones y haga clic en el botón azul + entre Opciones y la barra de consulta. Aparecerá un formulario
donde podrás:
1. Haga clic en el menú desplegable Idioma y seleccione Sigma.
2. Opcionalmente, especifique una licencia.
3. Añade la firma.
4. Haga clic en el botón CREAR y la detección debería implementarse en su cuadrícula en el siguiente ciclo de 15 minutos.
- 217/402 - Soluciones de cebolla de seguridad, LLC

12.3.3 Configuración Sigma
12.3.3 Configuración Sigma
• Navegue a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• Navegue a SOC --> configuración --> servidor --> módulos --> elastalertengine.
Una vez que haya llegado a esta ubicación, aquí encontrará algunas configuraciones comunes.
Frecuencia de actualización de Sigma
De forma predeterminada, Security Onion busca nuevas reglas de Sigma cada 24 horas. Puede cambiar este valor en SOC --> configuración --> servidor --> módulos
--> elastalertengine --> communityRulesImportFrequencySeconds.
Paquetes Sigma
Puedes elegir entre diferentes paquetes Sigma:
https://github.com/SigmaHQ/sigma/blob/master/Releases.md
Puede modificar esta configuración a través de SOC --> config --> servidor --> módulos --> elastalertengine --> sigmaRulePackages.
Repositorios Sigma personalizados
Puede configurar Security Onion para extraer reglas Sigma de repositorios git personalizados a través de SOC --> configuración --> servidor --> módulos -->
elastalertengine --> reglasRepos --> predeterminado.
Se puede acceder a los repositorios a través de https o desde el sistema de archivos local. Por ejemplo:
archivo:///nsm/rules/detect-sigma/repos/my-custom-rep
- 218/402 - Soluciones de cebolla de seguridad, LLC

12.3.3 Configuración Sigma
Habilitar reglas Sigma al importar
`SOC` > `config` > `server` > `modules` > `elastalertengine` > `enabledSigmaRules` > `default`
Estas opciones de configuración le permiten especificar qué reglas se habilitan automáticamente en la importación inicial. El formato de este filtro es YAML.
lista que admite criterios de filtrado flexibles basados en una cantidad de campos en una regla Sigma. Una regla está habilitada solo si coincide con todos los filtros especificados.
Si hay más de un filtro para un campo, debe coincidir con al menos uno.
Formato de configuración
Cada elemento de la lista YAML representa un conjunto de filtros, utilizando los siguientes campos:
• conjunto de reglas: Lista de cadenas. Especifica el conjunto de reglas por el que filtrar (por ejemplo, "core", "securityonion-resources", "*" para cualquier conjunto de reglas).
• nivel: Lista de cadenas. Especifica los niveles de gravedad (por ejemplo, "crítico", "alto", "*" para cualquier nivel. Esta no es una verificación mayor o igual, solo una
coincidencia de cadena).
• producto: Lista de cadenas. Especifica los productos por los que filtrar (por ejemplo, "ventanas", "*" para cualquier producto).
• categoría: Lista de cadenas. Especifica la categoría o categorías del evento (por ejemplo, "process_creation", "registry_event", "*" para cualquier categoría).
• servicio: Lista de cadenas. Especifica los servicios por los que filtrar (por ejemplo, "seguridad", "cliente dns", "*" para cualquier servicio).
Por ejemplo:
# Habilite todas las reglas críticas y altas del conjunto de reglas "securityonion-resources"
- conjunto de reglas: ["securityonion-resources"]
nivel: ["crítico", "alto"]
producto: ["*"]
categoría: ["*"]
servicio: ["*"]
- 219/402 - Soluciones de cebolla de seguridad, LLC

12.4 YARA
12.4 YARA
Las reglas de YARA se cargan en Strelka para monitorear archivos en busca de características sospechosas o dignas de mención. Las reglas activas de YARA generan alertas que pueden ser
encontrado en Alertas.
De https://virustotal.github.io/yara/:
YARA es una herramienta destinada (pero no limitada a) a ayudar a los investigadores de malware a identificar y clasificar muestras de malware. Con YARA puedes
cree descripciones de familias de malware (o lo que quiera describir) basadas en patrones textuales o binarios. Cada descripción, también conocida como
regla, consta de un conjunto de cadenas y una expresión booleana que determinan su lógica.
12.4.1 Gestión de reglas YARA existentes
Puede administrar las reglas YARA existentes a través de Detecciones. Hay dos maneras de hacerlo:
• Desde la interfaz principal de Detecciones, puede buscar la detección deseada y hacer clic en el icono de binoculares.
• Desde la interfaz de Alertas, puede hacer clic en una alerta y luego hacer clic en el elemento del menú Detección de melodía.
Una vez que haya utilizado uno de estos métodos para llegar a la página de detalles de la detección, puede verificar el campo Estado en la esquina superior derecha y usar
el control deslizante para habilitar o deshabilitar la detección.
12.4.2 Agregar nuevas reglas YARA
Para agregar una nueva regla YARA, vaya a la página principal de Detecciones y haga clic en el botón azul + entre Opciones y la barra de consulta. Aparecerá un formulario
donde podrás:
1. Haga clic en el menú desplegable Idioma y seleccione YARA.
2. Opcionalmente, especifique una licencia.
3. Añade la firma.
4. Haga clic en el botón CREAR y la detección debería implementarse en su cuadrícula en el siguiente ciclo de 15 minutos.
- 220/402 - Soluciones de cebolla de seguridad, LLC

12.4.3 Opciones de las reglas YARA
12.4.3 Opciones de las reglas YARA
Puede configurar las opciones de reglas de YARA de la siguiente manera:
• Navegue a Administración --> Configuración.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• Navegue a SOC --> configuración --> servidor --> módulos --> strelkaengine.
Una vez que haya llegado a esta ubicación, aquí encontrará algunas configuraciones comunes.
Frecuencia de actualización de YARA
De forma predeterminada, Security Onion busca nuevas reglas YARA cada 24 horas. Puede cambiar este valor en SOC --> configuración --> servidor --> módulos --
> strelkaengine --> communityRulesImportFrequencySeconds.
Repositorios YARA personalizados
Puede configurar Security Onion para extraer reglas YARA de repositorios de git personalizados a través de SOC --> configuración --> servidor --> módulos --> strelkaengine --
> reglasRepos --> predeterminado.
Se puede acceder a los repositorios a través de https o desde el sistema de archivos local. Por ejemplo:
archivo:///nsm/rules/detect-yara/repos/my-custom-rep
- 221/402 - Soluciones de cebolla de seguridad, LLC

13. Registros
13. Registros
13.1 Descripción general de registros
Una vez que los procesos de rastreo de red o los puntos finales generan los registros, ¿adónde van? ¿Cómo se analizan? ¿Cómo se almacenan? eso es
lo que discutiremos en esta sección.
- 222/402 - Soluciones de cebolla de seguridad, LLC

13.2 Ingerir
13.2 Ingerir
A continuación se ofrece una descripción general de cómo se incorporan los registros en varios tipos de implementación.
13.2.1 Importar
Canalización principal: Agente elástico [Nodo IMPORTAR] --> Ingesta de Elasticsearch [Nodo IMPORTAR]
Troncos: Zeek, Suricata
13.2.2 Evaluación
Canalización principal: Agente elástico [Nodo EVAL] --> Ingesta de Elasticsearch [Nodo EVAL]
Troncos: Zeek, Suricata
13.2.3 Independiente
Canalización principal: Agente elástico [Nodo SA] --> Logstash [Nodo SA] --> Redis [Nodo SA] <--> Logstash [Nodo SA] --> Ingesta de Elasticsearch [Nodo SA]
Registros: Zeek, Suricata, syslog
Agente elástico: Agente elástico [punto final de Windows] --> Logstash [Nodo SA] --> Redis [Nodo SA] <--> Logstash [Nodo SA] --> Ingesta de Elasticsearch
[Nodo SA]
Registros: WEL, Sysmon
13.2.4 Flota independiente
Canalización: Agente elástico [Nodo de flota] --> Logstash [M | MS] --> Ingesta de Elasticsearch [S | EM]
Registros: Agente elástico
13.2.5 Administrador (nodos de búsqueda separados)
Tubería principal: Agente elástico [Flota | Sensor] --> Logstash [Administrador] --> Redis [Administrador]
Registros: Zeek, Suricata, syslog
Agente elástico: Agente elástico [punto final de Windows] --> Logstash [Administrador] --> Redis [Administrador]
Registros: WEL, Sysmon
13.2.6 Búsqueda de administrador
Tubería principal: Agente elástico [Flota | Sensor] --> Logstash [MS] --> Redis [MS] <--> Logstash [MS] --> Elasticsearch Ingest [MS]
Registros: Zeek, Suricata, syslog
Canalización: Agente elástico [MS] --> Logstash [MS] --> Ingesta de Elasticsearch [MS]
Registros: Agente elástico local
Agente elástico: Agente elástico [punto final de Windows] --> Logstash [MS] --> Elasticsearch Ingest [MS]
Registros: WEL, Sysmon
- 223/402 - Soluciones de cebolla de seguridad, LLC

13.2.7 Pesado
13.2.7 Pesado
Canalización: Agente elástico [Nodo pesado] --> Ingesta de Elasticsearch [Pesado]
Registros: Zeek, Suricata, syslog
13.2.8 Buscar
Canalización: Redis [Administrador] --> Logstash [Buscar] --> Elasticsearch Ingest [Buscar]
Registros: Zeek, Suricata, syslog
13.2.9 Sensores
Tubería: Agente elástico [Sensor] --> Logstash [M | MS] --> Ingesta de Elasticsearch [S | EM]
Registros: Zeek, Suricata, syslog
- 224/402 - Soluciones de cebolla de seguridad, LLC

13.3 Almacenamiento de registros
13.3 Almacenamiento de registros
De https://www.elastic.co/products/logstash:
Logstash es un canal de procesamiento de datos del lado del servidor abierto y gratuito que ingiere datos de una multitud de fuentes, los transforma y luego
lo envía a tu "alijo" favorito.
Cuando Security Onion se ejecuta en modo independiente o en una implementación completamente distribuida, Logstash transporta registros no analizados a Elasticsearch
que luego analiza y almacena esos registros. Es importante tener en cuenta que Logstash NO se ejecuta cuando Security Onion está configurado para Importar o
Modo de evaluación. Puedes leer más sobre eso en la sección Arquitectura.
13.3.1 Configuración
Puede configurar Logstash yendo a Administración --> Configuración --> Logstash.
ls_pipeline_batch_size
La cantidad máxima de eventos que un subproceso de trabajo individual recopilará de las entradas antes de intentar ejecutar sus filtros y salidas.
Los tamaños de lote más grandes son generalmente más eficientes, pero tienen el costo de una mayor sobrecarga de memoria. Está configurado en 125 de forma predeterminada.
ls_pipeline_workers
El número de trabajadores que, en paralelo, ejecutarán las etapas de filtración y salida del ducto. Si descubre que los eventos están retrocediendo, o
Para que la CPU no esté saturada, considere aumentar este número para utilizar mejor la potencia de procesamiento de la máquina. Por defecto, este valor se establece en el
número de núcleos en el sistema.
Para obtener más información, consulte https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html.
montón
Si la memoria total disponible es de 8 GB o más, el programa de instalación establece el tamaño del montón de Logstash en el 25 % de la memoria disponible, pero no más de 4 GB.
- 225/402 - Soluciones de cebolla de seguridad, LLC

13.3.2 Análisis
Para obtener más información, consulte https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops.
Es posible que deba ajustar el valor según el rendimiento de su sistema. Los cambios se aplicarán la próxima vez que el minion se registre.
Puede forzar que esto suceda inmediatamente ejecutando sudo salt-call state.apply Logstash en el nodo real o ejecutando sudo salt
$SENSORNAME_$ROLE state.apply Logstash en el nodo administrador.
13.3.2 Análisis
Logstash no analiza registros en Security Onion, por lo que la modificación de los analizadores existentes o la adición de nuevos analizadores se deben realizar a través de Elasticsearch.
13.3.3 Reenvío de eventos a un destino externo
Tenga en cuenta que no brindamos soporte gratuito para sistemas de terceros, por lo que esta sección será solo una breve introducción a cómo
enviaría syslog a recopiladores de syslog externos. Si necesita soporte comercial, consulte https://www.securityonionsolutions.com.
13.3.4 Reenvío de eventos originales
Para reenviar eventos a un destino externo con modificaciones mínimas al evento original, cree un nuevo archivo de configuración personalizado en el
manager en /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/ para obtener la salida aplicable. Recomendamos usar cualquiera de los dos
el complemento de salida http, tcp, udp o syslog. En este momento, solo admitimos los complementos de salida de Logstash incluidos de forma predeterminada.
Por ejemplo, para reenviar todos los eventos Zeek desde el conjunto de datos dns, podríamos usar una configuración como la siguiente:
salida {
if [evento][módulo] == "Zeek" y [pipeline] == "dns" {
udp {
id => "cloned_events_out"
anfitrión => "192.168.x.x"
puerto => 1001
códec => "json_lines"
}
}
}
Advertencia
Cuando se utiliza el complemento de salida tcp, si el host o el puerto de destino está inactivo, se bloqueará la canalización de Logstash. Para evitar esto, intente usar
Las otras opciones de salida o considerar la posibilidad de reenviar registros utilizan una canalización de Logstash separada.
También tenga en cuenta que al reenviar registros desde el administrador, es posible que algunos campos no estén configurados como se esperaba, ya que los eventos aún no se han
procesado por la configuración del nodo de ingesta.
En SOC, navegue hasta Administración --> Configuración. En la parte superior de la página, haga clic en el menú Opciones y luego habilite Mostrar avanzado
opción de configuración. Luego navegue hasta Logstash --> define_pipelines --> administrador y agregue el nombre de su archivo recién creado a la lista de
Archivos de configuración utilizados para la canalización del administrador:
personalizado/miarchivo.conf
La configuración se aplicará en el siguiente intervalo de 15 minutos o puede aplicarla inmediatamente haciendo clic en el botón SINCRONIZAR GRID
en el menú Opciones.
Puede monitorear los eventos que fluyen a través de la salida ejecutando el siguiente comando en el administrador:
curl -s localhost:9600/_node/stats | jq .pipelines.manager
13.3.5 Reenvío de eventos modificados
Para reenviar eventos a un destino externo DESPUÉS de que hayan atravesado las canalizaciones de Logstash (NO las canalizaciones del nodo de ingesta), realice lo siguiente
Los mismos pasos que los anteriores, pero en lugar de agregar la referencia de su salida de Logstash a la canalización del administrador, agréguela a la canalización de búsqueda.
- 226/402 - Soluciones de cebolla de seguridad, LLC

13.3.6 Cola
La configuración se aplicará en el siguiente intervalo de 15 minutos o puede aplicarla inmediatamente haciendo clic en el botón SINCRONIZAR GRID
en el menú Opciones.
Puede monitorear los eventos que fluyen a través de la salida ejecutando el siguiente comando en los nodos de búsqueda:
curl -s localhost:9600/_node/stats | jq .pipelines.búsqueda
Tenga en cuenta que los eventos se reenviarán desde todos los nodos de búsqueda aplicables, y no solo desde el administrador.
13.3.6 Cola
Respaldado por la memoria
De https://www.elastic.co/guide/en/logstash/current/persistent-queues.html:
De forma predeterminada, Logstash utiliza colas limitadas en memoria entre las etapas de la canalización (entradas → trabajadores de la canalización) para almacenar eventos en buffer. el tamaño de
Estas colas en memoria son fijas y no configurables.
persistente
Si experimenta efectos adversos al utilizar la cola respaldada en memoria predeterminada, podría considerar una cola persistente basada en disco. Desde https://
www.elastic.co/guide/en/logstash/current/persistent-queues.html:
Para protegerse contra la pérdida de datos durante una terminación anormal, Logstash tiene una función de cola persistente que almacenará el mensaje.
cola en el disco. Las colas persistentes proporcionan durabilidad de los datos dentro de Logstash.
Bytes máximos de cola
La capacidad total de la cola en número de bytes. Asegúrese de que la capacidad de su unidad de disco sea mayor que el valor que especifique aquí. si
Se especifican tanto queue.max_events como queue.max_bytes, Logstash utiliza el criterio que se alcance primero.
Cola de mensajes fallidos
Si desea comprobar si hay eventos descartados, puede habilitar la cola de mensajes no entregados. Esto escribirá todos los registros que no puedan ingresar
Elasticsearch en un archivo numerado secuencialmente (para cada inicio/reinicio de Logstash).
Esto se puede lograr agregando lo siguiente a la configuración de Logstash:
dead_letter_queue.enable: verdadero
y reiniciando Logstash:
sudo so-logstash-reiniciar
Los archivos de la cola de mensajes no entregados se encuentran en /nsm/logstash/dead_letter_queue/main/.
Más información: - https://www.elastic.co/guide/en/logstash/current/dead-letter-queues.html
Redis
Cuando se utilizan nodos de búsqueda, Logstash en el nodo administrador genera salida a Redis (que también se ejecuta en el nodo administrador). Redis pone en cola eventos
desde la salida de Logstash (en el nodo administrador) y la entrada de Logstash en los nodos de búsqueda extraídos de Redis. Si notas nuevos eventos
no ingresan a Elasticsearch, es posible que desee verificar primero Logstash en el nodo del administrador y luego en la cola de Redis.
- 227/402 - Soluciones de cebolla de seguridad, LLC

13.3.7 Registro de diagnóstico
13.3.7 Registro de diagnóstico
El archivo de registro de Logstash se encuentra en /opt/so/log/logstash/logstash.log. La configuración del archivo de registro se puede ajustar en /opt/so/conf/logstash/etc/
log4j2.properties. De forma predeterminada, los registros están configurados para transferirse diariamente y eliminarse después de 7 días. Dependiendo de lo que estés buscando, también puedes
Necesito mirar los registros de Docker para el contenedor:
sudo docker registra so-logstash
13.3.8 Errores
Sólo lectura
[INFO ][Logstash.outputs.Elasticsearch] reintentando la acción fallida con el código de respuesta: 403 ({"type"=>"cluster_block_exception", "reason"=>"bloqueado por:
[PROHIBIDO/12/índice de solo lectura/permitir eliminación (api)];"})
Este error generalmente se debe a que se excedió el cluster.routing.allocation.disk.watermark (bajo, alto).
Es posible que desee consultar /opt/so/log/elasticsearch/<hostname>.log para ver específicamente qué índices se han marcado como de solo lectura.
Además, puede ejecutar el siguiente comando para permitir la escritura en los índices afectados:
curl -k -XPUT -H 'Tipo de contenido: aplicación/json' https://localhost:9200/<your_index>/_settings -d'{ "index.blocks.read_only": false }'
13.3.9 Más información
Nota
Para obtener más información sobre Logstash, consulte https://www.elastic.co/products/logstash.
- 228/402 - Soluciones de cebolla de seguridad, LLC

13.4 Redis
13.4 Redis
De https://redis.io/:
Redis es un almacén de estructura de datos en memoria de código abierto (con licencia BSD), que se utiliza como base de datos, caché y intermediario de mensajes. Soporta datos
estructuras como cadenas, hashes, listas, conjuntos, conjuntos ordenados con consultas de rango, mapas de bits, hiperloglogs e índices geoespaciales con radio
consultas.
En instalaciones independientes (no Eval) e implementaciones distribuidas, Logstash en el nodo administrador genera salida a Redis. Los nodos de búsqueda pueden entonces
consumir de Redis.
13.4.1 Cola
Para ver cuántos registros hay en la cola de Redis:
sudo so-redis-count
Si la cola tiene una copia de seguridad y no parece estar drenando, intente detener Logstash en el nodo administrador:
sudo so-logstash-parada
Luego monitoree la cola para ver si se drena:
mira 'sudo so-redis-count'
Si la cola de Redis se ve bien, pero aún tiene problemas con la indexación de los registros en Elasticsearch, querrá verificar Logstash
estadísticas sobre los nodos de búsqueda.
13.4.2 Sintonización
Security Onion configura Redis para utilizar 812 MB de la memoria total del sistema. Si tiene suficiente RAM disponible, es posible que desee aumentar
la configuración de redis_maxmemory yendo a Administración --> Configuración --> Redis. Este valor está en Megabytes, por lo que debe configurarlo para que utilice 8 gigas de
ram, establecerías el valor en 8192.
- 229/402 - Soluciones de cebolla de seguridad, LLC

13.4.3 Registro de diagnóstico
Logstash en el nodo administrador está configurado para enviar a Redis. Para obtener el mejor rendimiento, es posible que desees ajustar ls_pipeline_batch_size
valor en Administración --> Configuración --> logstash_settings para encontrar el punto ideal para su implementación.
Nota
Para obtener más información sobre el complemento de salida de Logstash para Redis, consulte: https://www.elastic.co/guide/en/logstash/current/plugins-outputs-
Redis.html
Logstash en los nodos de búsqueda extrae de Redis. Para obtener el mejor rendimiento, es posible que desees ajustar ls_pipeline_batch_size y ls_input_threads
en Administración --> Configuración --> logstash_settings para encontrar el punto ideal para su implementación.
Nota
Para obtener más información sobre el complemento de entrada de Logstash para Redis, consulte: https://www.elastic.co/guide/en/logstash/current/plugins-inputs-
Redis.html
13.4.3 Registro de diagnóstico
Los registros de Redis se pueden encontrar en /opt/so/log/redis/. Dependiendo de lo que esté buscando, es posible que también necesite consultar los registros de Docker para
contenedor:
sudo docker registra so-redis
13.4.4 Más información
Nota
Para obtener más información sobre Redis, consulte https://redis.io/.
- 230/402 - Soluciones de cebolla de seguridad, LLC

13.5 Búsqueda elástica
13.5 Búsqueda elástica
De https://www.elastic.co/products/elasticsearch:
Elasticsearch es un motor de análisis y búsqueda RESTful distribuido capaz de abordar un número creciente de casos de uso. Como el corazón de
Elastic Stack, almacena de forma centralizada tus datos para realizar búsquedas ultrarrápidas, relevancia ajustada y análisis potentes que escalan con facilidad.
13.5.1 Almacenamiento
Todos los datos que recopila Elasticsearch se almacenan en /nsm/elasticsearch/.
Advertencia
¡No elimine manualmente ningún archivo en /nsm/elasticsearch! Si necesita eliminar índices de Elasticsearch, debe hacerlo a través de Elasticsearch.
en lugar de eliminar archivos del sistema de archivos.
13.5.2 Esquema
Security Onion intenta cumplir con Elastic Common Schema (ECS) siempre que sea posible. En algunos casos, campos adicionales o ligeras modificaciones a
Las asignaciones de campos elásticos nativos se pueden encontrar dentro de los datos. Puede obtener más información sobre ECS en https://www.elastic.co/elasticsearch/common-
esquema.
13.5.3 Consulta
Puede consultar Elasticsearch mediante interfaces web como Alertas, Paneles, Hunt y Kibana. También puede consultar Elasticsearch desde el
línea de comando usando so-elasticsearch-query.
13.5.4 Autenticación
Puede autenticarse en Elasticsearch utilizando el mismo nombre de usuario y contraseña que utiliza para SOC.
Puede agregar nuevas cuentas de usuario tanto a Elasticsearch como a SOC al mismo tiempo, como se muestra en la sección Agregar cuentas. Por favor tenga en cuenta que
Si, en cambio, crea cuentas directamente en Elastic, esas cuentas solo tendrán acceso a Elastic y no a SOC.
13.5.5 Indexación
La mayoría de los datos están asociados con un flujo de datos, que es una abstracción de los índices tradicionales que aprovecha uno o más índices de respaldo para
gestionar y representar los datos dentro del flujo de datos. El uso de flujos de datos permite una mayor flexibilidad en la gestión de datos.
Los flujos de datos pueden orientarse durante la búsqueda u otras operaciones directamente, de forma similar a cómo se orientan los índices.
Por ejemplo, una consulta basada en CLI sobre registros de conexión de Zeek tendría el siguiente aspecto:
registros de consulta de búsqueda tan elástica-zeek-so/_search?q=event.dataset:conn
Cuando esta consulta se ejecuta en los datos del backend, en realidad se dirige a uno o más índices de respaldo, como por ejemplo:
.ds-logs-zeek-so-2022-03-07.0001
.ds-logs-zeek-so-2022-03-08.0001
.ds-logs-zeek-so-2022-03-08.0002
De manera similar, puede apuntar a un único índice de respaldo con la siguiente consulta:
so-elasticsearch-query .ds-logs-zeek-so-2022-03-08.001/_search?q=event.dataset:conn
Puede obtener más información sobre los flujos de datos en https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html.
- 231/402 - Soluciones de cebolla de seguridad, LLC

13.5.6 Configuración
13.5.6 Configuración
Puede configurar Elasticsearch yendo a Administración --> Configuración --> Elasticsearch.
13.5.7 Análisis
Elasticsearch recibe registros no analizados de Logstash o Elastic Agent. Luego, Elasticsearch analiza y almacena esos registros. Los analizadores se almacenan en
/opt/so/conf/elasticsearch/ingest/. Los analizadores de ingesta personalizados se pueden colocar en /opt/so/saltstack/local/salt/elasticsearch/files/
ingerir/. Para que estos cambios surtan efecto, reinicie Elasticsearch usando so-elasticsearch-restart.
Elastic Agent puede analizar previamente o actuar sobre los datos antes de que lleguen a Elasticsearch, alterando el flujo de datos o el índice en el que están escritos, o
otras características como el conjunto de datos del evento u otra información pertinente. Esta configuración se mantiene en la política del agente o
Configuración de integración en Elastic Fleet.
Nota
Puede obtener más información sobre el análisis de ingesta de Elasticsearch en: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html
13.5.8 Clúster
En una implementación distribuida con un administrador y uno o más nodos de búsqueda, el administrador y los nodos de búsqueda se unen como una multi-
Nodo Clúster elástico.
Para obtener más información, consulte la información del clúster en https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-
node.html#modules-node.
13.5.9 Funciones del nodo Elasticsearch
Consulte la documentación de roles del nodo Elasticsearch en https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-
nodo.html.
- 232/402 - Soluciones de cebolla de seguridad, LLC

13.5.10 Plantillas
Al crear una implementación distribuida, el administrador de Security Onion debe comenzar con la función de nodo de datos. Si luego te unes a un grupo separado
nodo de búsqueda, es posible que desee migrar los datos del administrador al nodo de búsqueda y luego eliminar la función del nodo de datos del
gerente. Para obtener más información, consulte:
https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cluster.html#cluster-shard-allocation-filtering
Si desea configurar ciertos nodos de búsqueda para las funciones data_hot, data_warm o data_cold, asegúrese de eliminarles la función de datos.
También querrás asegurarte de que data_content esté asignado a tus nodos activos.
Advertencia
Los roles de nodo de Elasticsearch son una configuración avanzada y debes tener cuidado para evitar interrupciones en tu clúster.
Para ver y modificar los roles de los nodos de Elasticsearch, primero navegue a Administración --> Configuración, haga clic en el menú Opciones en la parte superior de la página.
y habilite la opción Mostrar configuración avanzada. Luego navegue hasta Elasticsearch --> so_roles y seleccione el rol deseado. Finalmente, navegue hasta
config --> nodo --> roles y la lista de roles deberían aparecer en el lado derecho de la página.
13.5.10 Plantillas
Los campos se asignan a su tipo de datos apropiado mediante plantillas. Al realizar cambios para el análisis, es necesario asegurarse de que los campos estén
asignado a un tipo de datos para permitir la indexación, lo que a su vez permite una agregación y búsqueda efectivas en Dashboards, Hunt y Kibana.
Elasticsearch aprovecha las plantillas de índice y de componentes.
Nota
Para administrar plantillas para integraciones de terceros, consulte la sección integraciones de terceros.
Plantillas de componentes
De https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html:
Las plantillas de componentes son bloques de construcción reutilizables que configuran asignaciones, configuraciones y alias. Si bien puedes usar el componente
plantillas para construir plantillas de índice, no se aplican directamente a un conjunto de índices. Ver también https://www.elastic.co/guide/en/
elasticsearch/reference/current/indices-component-template.html.
Plantillas de índice
De https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html:
Una plantilla de índice es una forma de indicarle a Elasticsearch cómo configurar un índice cuando se crea. Las plantillas se configuran antes del índice.
creación. Cuando se crea un índice, ya sea manualmente o indexando un documento, la configuración de la plantilla se utiliza como base para
creando el índice. Las plantillas de índice pueden contener una colección de plantillas de componentes, así como especificar directamente configuraciones, asignaciones y
alias.
En Security Onion, las plantillas de componentes se almacenan en /opt/so/saltstack/default/salt/elasticsearch/templates/component/.
Estas plantillas se especifican para usarse en las definiciones de plantillas de índice en /opt/so/saltstack/default/salt/elasticsearch/
valores predeterminados.yml.
13.5.11 ID de comunidad
Para los registros que naturalmente no incluyen ID de comunidad, utilizamos el procesador de ID de comunidad de Elasticsearch: https://www.elastic.co/guide/en/
elasticsearch/referencia/actual/community-id-processor.html
- 233/402 - Soluciones de cebolla de seguridad, LLC

13.5.12 La expansión de campo coincide con demasiados campos
13.5.12 La expansión de campo coincide con demasiados campos
Si recibe errores como No se pudo crear la consulta: la expansión del campo para [*] coincide con demasiados campos, límite: 3500, obtuvo: XXXX, entonces esto
Por lo general, significa que está enviando registros adicionales y, por lo tanto, tiene más campos que nuestro valor predeterminado max_clause_count. Para resolver esto,
puede ir a Administración --> Configuración --> Elasticsearch --> config --> índices --> consulta --> bool --> max_clause_count y ajustar el
valor para cualquier casilla que ejecute Elasticsearch en su implementación.
13.5.13 Fragmentos
Aquí hay algunos consejos de https://www.elastic.co/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster:
SUGERENCIA: Evite tener fragmentos muy grandes, ya que esto puede afectar negativamente la capacidad del clúster para recuperarse de una falla. No hay un límite fijo sobre cómo
Los fragmentos grandes pueden serlo, pero un tamaño de fragmento de 50 GB a menudo se cita como un límite que se ha visto que funciona para una variedad de casos de uso.
SUGERENCIA: Los fragmentos pequeños dan como resultado segmentos pequeños, lo que aumenta la sobrecarga. Trate de mantener el tamaño promedio de fragmento entre unos pocos GB y unos pocos
decenas de GB. Para casos de uso con datos basados ​​en el tiempo, es común ver fragmentos de entre 20 GB y 40 GB de tamaño.
SUGERENCIA: La cantidad de fragmentos que puede contener en un nodo será proporcional a la cantidad de montón que tenga disponible, pero no hay un límite fijo.
aplicado por Elasticsearch. Una buena regla general es asegurarse de mantener la cantidad de fragmentos por nodo por debajo de 20 a 25 por GB de montón que tenga.
configurado. Por lo tanto, un nodo con un montón de 30 GB debería tener un máximo de 600-750 fragmentos, pero cuanto más por debajo de este límite podrá conservarlo.
cuanto mejor. En general, esto ayudará a que el grupo se mantenga en buena salud.
Para ver sus fragmentos existentes, ejecute el siguiente comando y la cantidad de fragmentos se mostrará en la quinta columna:
sudo so-elasticsearch-indices-list
Si desea ver los detalles de cada uno de esos fragmentos:
sudo so-elasticsearch-shards-list
Teniendo en cuenta los consejos de tamaño anteriores, si alguno de sus índices tiene un promedio de más de 50 GB por fragmento, entonces probablemente debería aumentar el número de fragmentos.
hasta llegar por debajo del máximo recomendado de 50 GB por fragmento.
El número de fragmentos para un índice se puede ajustar yendo a Administración --> Configuración --> Elasticsearch --> index_settings --> entonces-
NOMBRE-ÍNDICE --> plantilla_índice --> plantilla --> configuración --> índice --> número_de_fragmentos.
Tenga en cuenta que los índices antiguos conservarán la configuración de fragmentos anterior y la configuración anterior solo se aplicará a los índices recién creados.
13.5.14 Tamaño del montón
Si la memoria total disponible es de 8 GB o más, el programa de instalación configura el tamaño del montón para que sea el 33 % de la memoria disponible, pero no superior a 25 GB. usted puede
Es necesario ajustar el valor del tamaño del montón según el rendimiento de su sistema. Puedes modificar esto yendo a Administración -->
Configuración --> Elasticsearch --> esheap.
Para obtener más información, consulte:
• https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops
• https://www.elastic.co/guide/en/elasticsearch/reference/current/important-settings.html#heap-size-settings
13.5.15 Límite de campo
Security Onion actualmente tiene por defecto un límite de campos de 5000. Si recibe mensajes de error de Logstash o simplemente desea aumentar
esto, puede hacerlo yendo a Administración --> Configuración --> Elasticsearch --> index_settings --> so-INDEX-NAME --> index_template -->
plantilla --> configuración --> índice --> mapeo --> total_fields --> límite.
Tenga en cuenta que el cambio en el límite de campos no se producirá inmediatamente, solo en la creación del índice.
- 234/402 - Soluciones de cebolla de seguridad, LLC

13.5.16 Reindización
13.5.16 Reindización
Es posible que sea necesario volver a indexar si los tipos de datos de campo han cambiado y surgen conflictos. Este proceso puede llevar MUCHO tiempo y solo
Lo recomiendo si conservar los datos es absolutamente crítico.
Para obtener más información sobre la reindexación, consulte: https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html
13.5.17 Limpieza
Si desea borrar todos los datos de Elasticsearch, incluidos documentos e índices, puede ejecutar el comando so-elastic-clear.
13.5.18 GeoIP
Elasticsearch 8 ya no incluye bases de datos GeoIP de forma predeterminada. Incluimos bases de datos GeoIP para Elasticsearch para que todos los usuarios tengan
Funcionalidad GeoIP. Si sus nodos de búsqueda tienen acceso a Internet y pueden llegar a geoip.elastic.co y Storage.googleapis.com, entonces puede optar por
Acceda a las actualizaciones de la base de datos si desea información más reciente. Para hacerlo, ejecute el siguiente comando en su administrador:
sudo so-elasticsearch-query _cluster/settings -d '{"persistent":{"ingest.geoip.downloader.enabled":true}}' -XPUT
13.5.19 Salud
Para verificar el estado de Elasticsearch, vaya a la interfaz Grid y verifique el campo Estado de Elasticsearch. Si muestra algo más que OK, ejecute
el siguiente comando desde la CLI en el nodo administrador para buscar pistas adicionales:
sudo so-elasticsearch-query _cluster/health?pretty
13.5.20 Estado Pendiente
Si la interfaz de Grid muestra el estado de Elasticsearch como Pendiente, verifique si hay fragmentos no asignados ejecutando el siguiente comando desde la CLI
en el nodo administrador:
sudo so-elasticsearch-query _cat/shards | grep ONU
El resultado de la consulta debería mostrar los índices afectados. Es posible que a los índices de métricas más antiguos para los registros de Elastic Endpoint se les haya asignado una réplica, por lo que si
Si está ejecutando un clúster elástico de un solo nodo, no habrá ningún lugar donde exista la réplica. Para resolver el problema, ejecute el siguiente comando para
cada índice afectado (reemplazando $index con el nombre del índice real):
sudo so-elasticsearch-query $index/_settings -d '{"número_de_réplicas":0}' -XPUT
Después de ejecutar el comando, el índice ya no debería usar réplicas y el estado debería cambiar de "Pendiente" a "OK" una vez que todos los índices
han sido modificados exitosamente.
13.5.21 Gestión de índices
Los índices de Elasticsearch son administrados tanto por la utilidad so-elasticsearch-indices-delete como por Index Lifecycle Management (ILM).
Nota
¡Vea nuestro video sobre Gestión del ciclo de vida del índice en https://youtu.be/Y6HVein7nP8!
- 235/402 - Soluciones de cebolla de seguridad, LLC

13.5.21 Gestión de índices
Advertencia
so-elasticsearch-indices-delete está diseñado principalmente para implementaciones de un solo nodo (IMPORT, EVAL y STANDALONE). Ejecutándolo en un
La implementación de múltiples nodos con uno o más nodos de búsqueda tiene la posibilidad de llegar a un estado de caso de esquina donde se eliminan más datos que los
previsto. Por lo tanto, este script está deshabilitado en implementaciones de múltiples nodos. Si tiene una implementación de múltiples nodos, deberá asegurarse de que ILM
está configurado correctamente para eliminar índices antes de que el uso del disco alcance la configuración de marca de agua de Elasticsearch. De lo contrario, Elasticsearch puede detenerse
ingiriendo nuevos datos.
índices-de-búsqueda-tan-elásticos-eliminar
so-elasticsearch-indices-delete gestiona la eliminación basada en el tamaño de los índices de Elasticsearch según el valor del
Configuración de Elasticsearch.retention.retention_pct. Esta configuración se compara con el espacio total en disco disponible para /nsm/elasticsearch
en todos los nodos del clúster de Elasticsearch. Si sus índices utilizan más que retención_pct, entonces so-elasticsearch-indices-delete
eliminará los índices antiguos hasta que el espacio en disco consumido por los índices vuelva a estar bajo retención_pct. El valor predeterminado para esta configuración es 50 por ciento, por lo que
que las implementaciones independientes tengan suficiente espacio no solo para Elasticsearch sino también para la captura completa de paquetes y otros registros. Para distribuido
En implementaciones con nodos de búsqueda dedicados donde Elasticsearch es el principal consumidor de espacio en disco, es posible que desee aumentar este valor predeterminado.
Para modificar el valor de retención_pct, primero navegue a Administración --> Configuración. En la parte superior de la página, haga clic en el menú Opciones y
luego habilite la opción Mostrar configuración avanzada. Luego navegue a Elasticsearch --> retención --> retención_pct. Una vez que hagas el cambio
y guárdelo, la nueva configuración entrará en vigor en el siguiente intervalo de 15 minutos. Si desea realizar el cambio inmediatamente, puede hacer clic en el
botón SINCRONIZAR GRID en el menú Opciones en la parte superior de la página.
ILM
Index Lifecycle Management (ILM) gestiona lo siguiente:
• Rollover de índice basado en tamaño
• renovación del índice basada en el tiempo
• niveles de contenido basados en el tiempo
• eliminación de índice basada en el tiempo
La eliminación del índice basada en el tiempo se basa en la configuración min_age dentro de la política global o en la política individual del índice mismo. Por favor tenga en cuenta
que la eliminación basada en el tamaño mediante so-elasticsearch-indices-delete tiene prioridad sobre la eliminación basada en el tiempo, ya que el uso del disco puede alcanzar
retención_pct y los índices se eliminarán antes de que se alcance el valor min_age.
La configuración de ILM se puede encontrar navegando a Administración --> Configuración --> Elasticsearch --> index_settings:
• Para editar la política global que se aplica a TODOS los índices, navegue a global_overrides --> política --> fases y allí verá las opciones fría, eliminar,
Fases ILM caliente y cálida.
• Para editar la política de un índice individual, primero haga clic en el menú Opciones en la parte superior de la página y luego habilite la opción
Mostrar la opción de configuración avanzada. Luego navegue hasta $index --> política --> fases. Allí verá el ILM frío, eliminado, caliente y tibio.
fases para ese índice en particular.
• Es importante tener en cuenta que configuraciones como min_age se calculan en relación con la fecha de renovación (NO la fecha de creación original del índice). Para
Por ejemplo, si tiene un índice que está configurado para renovarse después de 30 días y eliminar min_age está configurado en 30, entonces habrá 30 días desde el índice.
creación hasta la renovación y luego 30 días adicionales antes de la eliminación.
• Al modificar la configuración de ILM, tenga en cuenta que algunas configuraciones solo tendrán efecto después de que se cree un nuevo índice.
- 236/402 - Soluciones de cebolla de seguridad, LLC

13.5.21 Gestión de índices
Ahora que tiene una descripción general de todo lo que ILM puede hacer, aquí le presentamos una descripción general de muy alto nivel de cómo configuraría la eliminación de ILM para su
despliegue:
• Determine sus requisitos de retención de datos. Esto podría ser 1 semana, 1 mes o más. También puede ser diferente para distintos tipos de datos.
• Determine su ingesta diaria actual. Una forma de hacer esto es ir a Kibana, seleccionar el menú de la izquierda, seleccionar Administración de pila y
luego vaya a Gestión de índices para ver cómo son sus índices actuales. Otra opción es ejecutar
sudo so-elasticsearch-indices-growth desde la línea de comando.
• Ahora que tiene sus requisitos de retención de datos y la ingesta diaria actual, utilice esos valores para determinar sus requisitos de almacenamiento.
Tenga en cuenta que la configuración de marca de agua predeterminada de Elasticsearch del 80% significa que querrá mantener libre el 20% de su disco y esto
deben tenerse en cuenta en sus requisitos de almacenamiento. Si sus requisitos de almacenamiento son mayores que la cantidad de almacenamiento que tiene
disponible, es posible que deba agregar nodos de búsqueda adicionales.
• Configure ILM Deletion para eliminar registros antes de alcanzar la marca de agua del 80 % de Elasticsearch. Esto se puede hacer globalmente para todos los índices yendo a
Administración -> Configuración -> Elasticsearch > index_settings > global_overrides > política > fases > eliminar > min_age. De nuevo, sigue en
Tenga en cuenta que la configuración min_age se calcula en relación con la fecha de renovación del índice y NO con la fecha de creación original del índice. Si quieres
para especificar diferentes valores de eliminación para diferentes tipos de datos, luego puede habilitar la configuración avanzada y luego profundizar en políticas específicas para
hazlo.
Consejo
Es posible que desee ejecutar sudo so-elasticsearch-indices-growth de forma regular para controlar el tamaño de sus índices.
Además de sudo so-elasticsearch-indices-growth, también puedes ejecutar sudo so-elasticsearch-retention-estimate que te dará
una aproximación de cuántos días de registros puede almacenar. Por ejemplo:
DESCARGO DE RESPONSABILIDAD: La salida del script se basa en patrones de datos actuales, pero son aproximaciones únicamente.
destinado a ayudar a configurar una política general de ILM.
================ Descripción general del almacenamiento =================
Tamaño de datos indexados: 141,12 GB (Elasticsearch)
Capacidad del clúster: 498,69 GB en total
Clúster utilizado: 245,32 GB
Marca de agua baja: 80 % (umbral de 398,96 GB)
Espacio restante: 153,63 GB antes de la marca de agua baja
Fragmentos de clúster: 498/4000 (12,4%)
Nodos de datos del clúster: 4
ejemplo-búsqueda1: data_hot,data_warm,data_content
ejemplo-búsqueda2: data_hot,data_warm,data_content
ejemplo-búsqueda3: datos_cold
hombre de ejemplo: contenido_datos
================ Crecimiento ES =================
Tasa de crecimiento diario: 4,08 GB/día
Tasa de eliminación de ILM: 0,47 GB/día (programada)
Tasa de crecimiento neto: 3,62 GB/día
Creación diaria de fragmentos: ~3 fragmentos/día
Almacenamiento a liberar (30d): 2 índices (~13,97 GB, 4 fragmentos)
================ Proyección de retención =================
Índice más antiguo: ~55 días (.ds-logs-auditd_manager.auditd-default-2025.09.30-000001)
Retención estimada: ~98 días (hasta que se configure la marca de agua baja)
Incumplimiento de marca de agua baja estimado en ~42,47 días (2026-01-06)
Para lograr la máxima retención, nuestro objetivo es equilibrar el grupo lo más cerca posible de la configuración de marca de agua baja. En este ejemplo, aparece
el clúster está ganando alrededor de 4 GB de registros por día. Sin embargo, ILM actualmente elimina aproximadamente 0,5 GB por día, por lo que el uso general de almacenamiento es
creciente. Sin modificar la configuración de ILM, este clúster alcanzará la marca de agua en aproximadamente 42 días (la retención total será de aproximadamente 98 días).
Para combatir esto, una opción es establecer global_overrides para la fase de eliminación como se describió anteriormente, estableciendo la fase de eliminación en algo así como 90
días. Esto nos da un poco de espacio entre la retención estimada y nuestra fase de eliminación real.
Además de las anulaciones globales, que se aplican a todos los índices, es posible modificar las políticas ILM por índice. Por ejemplo, quizás la alerta de Suricata
Los datos son algo que debes mantener almacenado durante 120 días. Puede configurar la política so-suricata.alerts para que tenga una fase de eliminación de 120d.
Esto tiene el costo de tener que reducir la retención en otros índices para liberar el almacenamiento necesario para las alertas de Suricata.
- 237/402 - Soluciones de cebolla de seguridad, LLC

13.5.22 Registro de diagnóstico
consejo
Una vez que haya configurado ILM, puede considerar aumentar la configuración de marca de agua alta/baja del clúster para permitir que Elasticsearch use más
espacio disponible en disco. Esto se puede hacer yendo a Administración --> Configuración --> Elasticsearch --> configuración --> clúster --> enrutamiento --> asignación
--> disco --> marca de agua.
Nota
Puede obtener más información sobre ILM en: https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html
13.5.22 Registro de diagnóstico
• Los registros de Elasticsearch se pueden encontrar en /opt/so/log/elasticsearch/.
• La configuración de registro se puede encontrar en /opt/so/conf/elasticsearch/log4j2.properties.
Dependiendo de lo que esté buscando, es posible que también deba consultar los registros de Docker para el contenedor:
sudo docker registra so-elasticsearch
13.5.23 Más información
Nota
Para obtener más información sobre Elasticsearch, consulte: https://www.elastic.co/products/elasticsearch
- 238/402 - Soluciones de cebolla de seguridad, LLC

13.6 ElastAlert 2
13.6 ElastAlert 2
De https://elastalert2.readthedocs.io/en/latest/elastalert.html#overview:
ElastAlert 2 es un marco simple para alertar sobre anomalías, picos u otros patrones de interés a partir de datos en Elasticsearch.
ElastAlert consulta Elasticsearch y proporciona un mecanismo de alerta con múltiples tipos de resultados, como Slack, Email, JIRA, OpsGenie y
muchos más.
13.6.1 Reglas Sigma
El módulo Detecciones generará automáticamente reglas compatibles con ElastAlert 2 para todas las detecciones de Sigma. No es necesario hacerlo manualmente
modificar las reglas generadas en el disco. Además, cualquier modificación se sobrescribirá durante la próxima sincronización de reglas Sigma.
El ajuste de una regla Sigma siempre debe realizarse a través de la pantalla Detecciones.
Consulte la sección de notificaciones para obtener información sobre cómo habilitar las notificaciones salientes a través del módulo Detecciones.
13.6.2 Reglas personalizadas
Las reglas personalizadas de ElastAlert 2, que no están asociadas al módulo Detecciones, se pueden agregar al nodo Security Onion Manager dentro de un
subdirectorio personalizado en el directorio /opt/so/rules/elastalert/rules/. Por ejemplo, cree un subdirectorio llamado /opt/so/rules/
elastalert/rules/custom/ y coloque reglas personalizadas dentro de ese directorio.
Advertencia
No modifique ni agregue reglas al directorio /opt/so/rules/elastalert/rules/, ya que el módulo Detecciones sobrescribe esas reglas.
Consulte la documentación de ElastAlert 2, vinculada anteriormente, para obtener información detallada sobre cómo escribir reglas personalizadas. Tenga en cuenta que escribir reglas
requiere una comprensión profunda de los registros de documentos de Elasticsearch, su estructura de datos y otros conceptos relacionados.
13.6.3 Registro de diagnóstico
Los registros de diagnóstico de ElastAlert están en /opt/so/log/elastalert/ y también pueden aparecer en los registros de Docker para el contenedor. Para ver registros de contenedores
Ejecute el siguiente comando en el Administrador:
sudo docker registra so-elastalert
ElastAlert 2 almacena información del estado de las reglas, como el número de visitas, la última vez que se ejecutó cada regla, etc., en los índices de Elasticsearch. Estos datos pueden ser
útil para ayudar a solucionar problemas de reglas personalizadas. Puede buscar estos datos en Dashboards, Hunt o Kibana. SOC no
Incluye automáticamente los índices de ElastAlert de forma predeterminada. Si desea incluirlos, puede ajustar la configuración adecuada
configuración. En SOC, navegue hasta Administración --> Configuración. En la parte superior de la página, haga clic en el menú Opciones y luego habilite Mostrar
opción de configuración avanzada. Luego filtre por elastic.index para localizar la configuración. En el lado derecho de la pantalla, agregue *:Elastalert* al
configuración de índice existente. La configuración actualizada debería parecerse a la siguiente:
*:so-*,*:endgame-*,*:logs-*,*:ElastAlert*
so-elastalert-crea
so-elastalert-create se puede utilizar para ayudar a aliviar la molestia de garantizar la sintaxis correcta y crear reglas de ElastAlert desde cero. caminará
le guiará a través de varias preguntas y, finalmente, generará un archivo de reglas de ElastAlert que puede implementar en su entorno para comenzar a generar alertas rápidamente.
y fácilmente.
- 239/402 - Soluciones de cebolla de seguridad, LLC

13.6.4 Configuración
prueba-so-elastalert
so-elastalert-test es un script contenedor para la herramienta elastalert-test-rule de ElastAlert. El script le permite probar una regla ElastAlert y obtener
resultados inmediatamente. Simplemente ejecute so-elastalert-test y siga las instrucciones.
Nota
so-elastalert-test aún no incluye todas las opciones disponibles para elastalert-test-rule.
Rendimiento
Para obtener un mejor rendimiento, evite escribir reglas que devuelvan una gran cantidad de registros. En su lugar, utilice use_count_query: true en cada archivo de reglas.
Esto solo devolverá recuentos de registros coincidentes y no los registros en sí.
Plazo
Para consultas que abarcan más de un minuto en el tiempo, es posible que desee agregar los siguientes campos a su regla para garantizar que la búsqueda se realice como
planeado (por ejemplo, durante 10 minutos):
tiempo_búfer:
minutos: 10
enable_buffer_time_overlap: verdadero
Para obtener más información, consulte: - https://elastalert2.readthedocs.io/en/latest/ruletypes.html#buffer-time - https://github.com/Yelp/
elastalert/problemas/805
13.6.4 Configuración
Puede modificar la configuración de ElastAlert 2 yendo a Administración --> Configuración --> ElastAlert.
- 240/402 - Soluciones de cebolla de seguridad, LLC

13.6.5 Más información
13.6.5 Más información
Nota
Para obtener más información sobre ElastAlert, consulte https://elastalert2.readthedocs.io/en/latest/.
- 241/402 - Soluciones de cebolla de seguridad, LLC

13.7 Campos de datos
13.7 Campos de datos
Esta página hace referencia a los diversos tipos de campos de datos utilizados por Elastic Stack en Security Onion.
13.7.1 ECS
Intentamos alinearnos con Elastic Common Schema (ECS) siempre que sea posible.
Nota
Para obtener más información sobre ECS, consulte https://www.elastic.co/guide/en/ecs/current/ecs-reference.html.
13.7.2 Campos
• Campos de datos de alerta
• Campos ElastAlert
• Campos Zeek
13.7.3 Archivos de plantilla
Los campos se asignan al tipo adecuado utilizando archivos de plantilla que se encuentran en /opt/so/conf/elasticsearch/templates/.
- 242/402 - Soluciones de cebolla de seguridad, LLC

13.8 Campos de datos de alerta
13.8 Campos de datos de alerta
Elasticsearch recibe alertas NIDS de Suricata a través de Elastic Agent o Logstash y las analiza usando:
• /opt/so/conf/elasticsearch/ingest/suricata.alert
• /opt/so/conf/elasticsearch/ingest/common.NIDS
• /opt/so/conf/elasticsearch/ingest/common
Puede encontrarlos en línea en:
• https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest/suricata.alert
• https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest/common.nids
• https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest-dynamic/common
Puede encontrar alertas NIDS analizadas en Alertas, Paneles, Hunt y Kibana a través de sus consultas y paneles predefinidos o manualmente
buscando:
• evento.módulo: "Suricata"
• event.dataset: "alerta"
Esas alertas deben tener los siguientes campos:
• fuente.ip
• puerto.fuente
• destino.ip
• destino.puerto
• red.transporte
• regla.gid
• nombre.regla
• regla.regla
• regla.rev
• regla.severidad
• regla.uuid
• regla.versión
- 243/402 - Soluciones de cebolla de seguridad, LLC

13.9 Campos ElastAlert
13.9 Campos ElastAlert
La siguiente lista incluye nombres de campos tal como están formateados en Elasticsearch. ElastAlert proporciona su propia plantilla para usar en el mapeo
ElastAlert, por lo que actualmente no utilizamos un archivo de configuración para analizar datos de ElastAlert.
índice:*:elastalert_status
• alerta_info.tipo
• alerta_enviada
• tiempo_alerta
• tiempo final
• historia
• partidos
• match_body.@marca de tiempo
• match_body.num_hits
• match_body.num_matches
• nombre_regla
• hora de inicio
• tiempo_tomado
- 244/402 - Seguridad Cebolla Soluciones, LLC

13.10 Campos Zeek
13.10 Campos Zeek
Los registros de Zeek se envían a Elasticsearch, donde se analizan mediante el análisis de ingesta. La mayoría de los registros de Zeek tienen algunos campos estándar y son
analizado de la siguiente manera:
• ts => @marca de tiempo
• uid => registro.id.uid
• id.orig_h => fuente.ip
• id.orig_p => fuente.puerto
• id.resp_h => destino.ip
• id.resp_p => destino.puerto
Los campos restantes en cada registro son específicos del tipo de registro. Para ver cómo se asignan los campos para un registro de Zeek específico, eche un vistazo a su ingesta.
analizador.
Puede encontrar analizadores de ingesta en su sistema de archivos local en /opt/so/conf/elasticsearch/ingest/ o puede encontrarlos en línea en:
https://github.com/Security-Onion-Solutions/securityonion/tree/3/main/salt/elasticsearch/files/ingest
Por ejemplo, supongamos que desea saber cómo se analiza Zeek conn.log. Podrías echar un vistazo a /opt/so/conf/elasticsearch/ingest/
zeek.conn o véalo en línea en:
https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest/zeek.conn
Verá que Zeek.conn luego llama a la canalización Zeek.common (/opt/so/conf/elasticsearch/ingest/zeek.common):
https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest/zeek.common
que a su vez llama al canal común (/opt/so/conf/elasticsearch/ingest-dynamic/common):
https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/salt/elasticsearch/files/ingest-dynamic/common
- 245/402 - Soluciones de cebolla de seguridad, LLC

13.11 Identificación de la comunidad
13.11 Identificación de la comunidad
Desde https://github.com/corelight/community-id-spec:
Al procesar datos de flujo de una variedad de aplicaciones de monitoreo (como Zeek y Suricata), a menudo es deseable pasar rápidamente de
un conjunto de datos a otro. Si bien la información de tupla de flujo requerida generalmente está presente en los conjuntos de datos, los detalles de tales "uniones" pueden ser
tedioso, especialmente en los casos extremos. Esta especificación describe el hash de flujo de "ID de comunidad", estandarizando la producción de un identificador de cadena.
que representa un flujo de red determinado, para reducir el pivote a una simple comparación de cadenas.
Security Onion habilita el soporte integrado de ID de comunidad tanto en Zeek como en Suricata.
Para los registros que naturalmente no incluyen ID de comunidad, utilizamos el procesador de ID de comunidad de Elasticsearch: https://www.elastic.co/guide/en/
elasticsearch/referencia/actual/community-id-processor.html
Los paneles incluyen un panel de ID de comunidad que mostrará todos los registros con ese valor.
13.11.1 Más información
Nota
Para obtener más información sobre Community ID, consulte: https://github.com/corelight/community-id-spec
- 246/402 - Soluciones de cebolla de seguridad, LLC

13.12 Registros de la consola Security Onion
13.12 Registros de la consola Security Onion
Los registros estándar de Security Onion Console se pueden encontrar en /opt/so/log/soc/.
13.12.1 Registros de autenticación SOC
Kratos maneja la autenticación SOC y puede leer más sobre eso en https://github.com/ory/kratos. Los registros de autenticación SOC se pueden encontrar en /opt/so/
iniciar sesión/kratos/. Esos registros se incorporan a Elasticsearch y están disponibles para realizar búsquedas en Dashboards, Hunt y Kibana. Tanto los paneles como
Hunt tiene consultas predefinidas para registros de autenticación SOC.
- 247/402 - Soluciones de cebolla de seguridad, LLC

14. Actualización
14. Actualización
14.1 Descripción general de la actualización
En esta sección, cubriremos cómo mantener Security Onion actualizado mediante sopa y enumeraremos fechas importantes de EOL para versiones anteriores de Security Onion.
- 248/402 - Soluciones de cebolla de seguridad, LLC

14.2 sopa
14.2 sopa
sopa significa Security Onion UPdater y puede usarlo para actualizar su implementación de Security Onion.
14.2.1 SSH
Advertencia
Si ejecuta sopa a través de una sesión SSH y esa sesión SSH finaliza, cualquier proceso que se ejecute en esa sesión finalizará. deberías
Evite dejar la sopa desatendida, especialmente si la máquina desde la que está realizando SSH está configurada para dormir después de un período de tiempo. tu también podrías
considere usar algo como screen o tmux para que, si su sesión SSH finaliza, los procesos continúen ejecutándose en el servidor.
14.2.2 Implementaciones de producción
Advertencia
Si tiene una implementación de producción, le recomendamos que pruebe el proceso de actualización en una implementación de prueba, si es posible, antes de implementarla en
producción.
14.2.3 Actualización
Para actualizar su implementación de Security Onion, ejecute el comando sopa con sudo:
sopa sudo
Si es necesario, la sopa se actualizará sola y luego le pedirá que la ejecute nuevamente. Una vez que la sopa esté completamente actualizada, buscará otras actualizaciones.
Esto incluye actualizaciones de la versión de Security Onion, revisiones de Security Onion y actualizaciones del sistema operativo (SO).
Después de ejecutar la sopa o reiniciar un nodo Security Onion, los servicios pueden tardar unos minutos en mostrar un estado OK en la pantalla Grid.
Esto puede deberse a la ejecución inicial del estado alto de Salt en el arranque. Si los servicios no parecen estar completamente operativos en 15 minutos, intente ejecutar
el siguiente comando:
sudo so-checkin
14.2.4 Actualizaciones de la versión Security Onion
Cuando lanzamos una nueva versión de Security Onion, actualizamos la sección Notas de la versión y publicamos una publicación de blog en https://
blog.securityonion.net. Querrá revisarlos para obtener información relevante sobre las actualizaciones individuales.
Si la sopa encuentra una actualización de la versión completa, actualizará la versión de Security Onion en /etc/soversion, todo el código Salt y todas las imágenes de Docker.
La sopa mantiene automáticamente la versión anterior de las imágenes de Docker. Estas imágenes de Docker más antiguas y no utilizadas se eliminarán automáticamente en el momento
próxima actualización de la versión. Si necesita eliminar estas imágenes antiguas de Docker inmediatamente, primero verifique que la actualización se haya completado correctamente y
que todo esté funcionando correctamente. Luego puedes eliminar las imágenes más antiguas individualmente o todas a la vez usando un comando como:
sistema sudo docker podar -a
Sin embargo, tenga en cuenta que esta es una opción agresiva y debe tener cuidado si tiene imágenes o archivos Docker no estándar.
configuración. Es posible que desee probarlo primero en un sistema de prueba.
- 249/402 - Soluciones de cebolla de seguridad, LLC

14.2.5 Correcciones de seguridad de Onion
14.2.5 Correcciones de seguridad de Onion
comprobaciones de sopa para las revisiones de Security Onion. Las revisiones suelen incluir actualizaciones del código Salt y pequeños cambios de configuración que no
garantiza una actualización de la versión completa. Esto no incluye imágenes de Docker, ya que requeriría una actualización de la versión completa.
Después de aplicar una revisión, puede notar que la versión de Security Onion en /etc/soversion sigue siendo la misma. La aplicación de la revisión es
rastreado en el administrador en el archivo /etc/sohotfix.
14.2.6 Actualizaciones del sistema operativo
Además de las actualizaciones de imágenes de la ventana acoplable Security Onion, la sopa también busca actualizaciones del sistema operativo que falten y le pregunta si desea instalarlas.
Actualizaciones automáticas del sistema operativo
Puede configurar actualizaciones automáticas del sistema operativo yendo a Administración --> Configuración --> parche.
Mantener actualizaciones del sistema operativo
Si desea evitar que ciertos paquetes se actualicen automáticamente (comúnmente denominados paquetes "bloqueados" o "retenidos"),
entonces puedes hacerlo a través de la configuración de espera. El caso de uso más frecuente es mantener el kernel para evitar reinicios frecuentes del sistema. para sostener un
paquete, agregue el nombre del paquete a la lista de retención en Administración --> Configuración --> bloqueo de versión --> retención.
- 250/402 - Soluciones de cebolla de seguridad, LLC

14.2.7 Configuraciones locales
14.2.7 Configuraciones locales
Soup buscará configuraciones locales en /opt/so/saltstack/local/ que puedan causar problemas y las marcará con el mensaje
Cambios potencialmente importantes encontrados en los siguientes archivos. Examine la salida de la sopa y revise cualquier configuración local.
para posibles problemas.
14.2.8 Registro
Si la sopa muestra algún error, puede consultar /root/soup.log para obtener pistas adicionales.
14.2.9 Entrehierro
Para actualizar una implementación de Airgap, deberá obtener la imagen ISO más reciente para el administrador de Airgapped y luego ejecutar una sopa que le preguntará dónde
encuéntralo:
• grabar la imagen ISO más reciente en un DVD e insertarla en la unidad de DVD del administrador (ejemplo: /dev/cdrom)
• flashear la imagen ISO en una unidad USB y conectar esa unidad USB al administrador (ejemplo: /dev/sdb)
• simplemente copie el archivo ISO al administrador (ejemplo: /home/SuUsuario/securityonion-3.X.Y-AAAAMMDD.iso)
En lugar de esperar a que la sopa solicite la ubicación, también puede especificar la ruta en la línea de comando usando la opción -f. por ejemplo
(cambie esto para reflejar la ruta real al archivo ISO o al dispositivo de disco que contiene el medio ISO):
sudo sopa -y -f /home/YourUser/securityonion-3.X.Y-YYYYMMDD.iso
- 251/402 - Soluciones de cebolla de seguridad, LLC

14.2.10 Elástico
14.2.10 Elástico
Si la sopa se actualizó a una nueva versión de la pila Elastic, entonces querrás ir a Elastic Fleet y:
• Profundice en cada una de sus políticas de agente activo, verifique la configuración de Descarga binaria del agente y ajústela si es necesario para su implementación.
• comprobar si hay integraciones que deban actualizarse
• comprobar si hay agentes que deban actualizarse (los agentes del nodo Grid deberían actualizarse automáticamente, por lo que solo debería necesitar buscar cualquier
agentes de punto final adicionales que haya implementado)
14.2.11 Kibana
Después de que se complete la sopa, si Kibana dice que el servidor Kibana aún no está listo incluso después de esperar unos minutos para que se inicialice por completo, entonces realice una prueba.
Mire la sección Registro de diagnóstico de la página de Kibana.
Si Kibana se carga pero los paneles muestran errores que no aparecían antes de la actualización, primero vuelva a cargar su navegador para asegurarse de que no haya errores.
problemas de caché. Si eso no resuelve el problema, es posible que deba volver a cargar los paneles en su administrador:
sudo rm /opt/so/state/kibana_*.txt
sudo salt-call state.apply Kibana.so_savedobjects_defaults -l info queue=True
14.2.12 Automatización
La sopa se puede automatizar de la siguiente manera:
sopa sudo -y
Esto hará que la sopa continúe sin supervisión y responda automáticamente sí a cualquier mensaje. Si tiene una instalación con espacio de aire, puede especificar el
ruta a la imagen ISO usando la opción -f de la siguiente manera:
sopa sudo -y -f /home/user/securityonion.iso
14.2.13 Errores
No se pudieron compilar los datos
Ocasionalmente, la sopa puede generar un error de datos que no se pudieron compilar que dice algo como
Error al renderizar SLS: la variable Jinja 'Ninguno' no tiene atributo. En la mayoría de los casos, este error se corrige solo en la siguiente ejecución de Salt.
Pilares y limas sls
La sopa revisará los pilares de sal para asegurarse de que puedan fundirse. De lo contrario, generará un mensaje como este:
Hay un problema al representar los pilares del administrador. Corrija los problemas en los archivos sls que se mencionan a continuación antes de ejecutar SOUP nuevamente.
Esto generalmente significa que alguien modificó los archivos Salt sls e introdujo un error tipográfico.
Descargando imágenes
Como Soup descarga imágenes del contenedor, puede encontrar errores si hay problemas de conexión a Internet o si el disco se queda sin espacio libre.
espacio. Una vez que haya resuelto la condición subyacente, puede actualizar manualmente las imágenes de su contenedor usando so-docker-refresh.
Registro Docker
Si ve errores relacionados con so-dockerregistry (Registro Docker), eche un vistazo a las siguientes discusiones para ver si su
Los síntomas coinciden y si sus soluciones pueden ayudarle:
https://github.com/Security-Onion-Solutions/securityonion/discussions/12078
- 252/402 - Soluciones de cebolla de seguridad, LLC

14.2.14 Implementaciones distribuidas
https://github.com/Security-Onion-Solutions/securityonion/discussions/12635
Highstate ya está funcionando
Aquí hay algunos otros errores que puede ver al ejecutar sopa:
locales:
Los datos no se pudieron compilar:
----------
Error al renderizar SLS 'base:common': la variable Jinja 'objeto de lista' no tiene el atributo 'valores'
y/o
Hay un problema al descargar la imagen so-xyz:3.X.Y. Detalles:
gpg: Firma realizada el jueves 18 de febrero de 2021 a las 02:26:10 p. m. UTC con el ID de clave RSA FE507013 gpg: Firma MALA de "Security Onion Solutions, LLC
<info@securityonionsolutions.com>"
Si ve estos errores, lo más probable es que ya se estuviera ejecutando un proceso de estado alto de sal cuando comenzó la sopa. Puedes esperar unos minutos.
y luego prueba la sopa nuevamente. Alternativamente, puede ejecutar Sudo so-checkin y esperar a que se complete antes de ejecutar sopa nuevamente.
14.2.14 Implementaciones distribuidas
Si tiene una implementación distribuida con un nodo administrador y nodos de sensores y/o nodos de búsqueda separados, solo necesita ejecutar sopa en
el gerente. Una vez que se haya completado la sopa, otros nodos deberían actualizarse en el siguiente estado alto de Salt (normalmente en 15 minutos).
Advertencia
El hecho de que la actualización se haya completado en el administrador NO significa que la actualización se haya completado en otros nodos de la red. No reiniciar manualmente
cualquier cosa hasta que sepa que todos los nodos de búsqueda y los nodos pesados están actualizados.
Cada minion se encuentra en un período de registro aleatorio de 15 minutos y cosas como el ancho de banda de la red pueden ser un factor en el tiempo que demora la actualización real. si
Si tiene un nodo pesado en un enlace lento, llevará un tiempo enviarle los contenedores. Dependiendo de los cambios ocurridos entre los
versiones, es posible que Elasticsearch no pueda comunicarse con dicho nodo pesado hasta que se complete la actualización.
Si parece que le faltan datos después de la actualización, evite reiniciar los servicios y en su lugar asegúrese de que al menos un nodo de búsqueda tenga
completó su actualización. La mejor manera de hacerlo es ejecutar Sudo so-checkin desde un nodo de búsqueda y asegurarse de que no haya errores. Normalmente si
funciona en un nodo, funcionará en el resto. Los nodos de sensores son menos complejos y se actualizarán a medida que se registren para que pueda monitorearlos desde el
Sección de cuadrícula de SOC.
- 253/402 - Soluciones de cebolla de seguridad, LLC

14.2.14 Implementaciones distribuidas
Cuando ejecuta sopa en el administrador, hace lo siguiente:
• Comprueba si se está ejecutando en un administrador.
• Comprueba si la red está en modo Airgap. Si es así, le pedirá la ubicación del ISO o del punto de montaje.
• Comprueba si estamos ejecutando la última versión de sopa. De lo contrario, colocará la última versión en el lugar correcto y le pedirá que vuelva a preparar la sopa.
• Compara la versión instalada con la disponible en github o la imagen ISO.
• Comprueba si es necesario actualizar Salt (más sobre esto más adelante).
• Descarga las nuevas imágenes de Docker o, si no hay espacio, las copia desde la imagen ISO.
• Detiene el maestro y el minion de Salt y los reinicia en un modo restringido. Este modo sólo permite que el administrador se conecte a él para que hagamos
Asegúrese de que el administrador haya terminado antes de que se actualice cualquiera de los minions.
• Actualiza Salt si es necesario. Esto hará que los servicios maestro y minion se reinicien pero aún en modo restringido.
• Realiza los cambios necesarios en los pilares, como agregar nuevas configuraciones o cambiar el nombre de los valores. Esto varía de una versión a otra.
• Si la grilla está en modo Airgap, copia las últimas reglas de ET Open y yara al administrador.
• El nuevo código Salt se implementa en el administrador.
• Ejecuta un estado alto en el administrador, que es la actualización real donde utilizará el nuevo código Salt y los contenedores Docker.
• Desbloquea el servicio maestro de Salt y permite que los minions se conecten nuevamente.
• Emite un comando a todos los minions para que actualicen Salt si es necesario. Es importante tener esto en cuenta, ya que lleva tiempo actualizar el minion de Salt en todos
minions. Si el minion no responde por cualquier motivo, no se actualizará en este momento. Esto no es un problema porque lo primero
Lo que se verifica cuando un minion habla con el maestro es si Salt necesita actualizarse y aplicará la actualización si es así.
• Los nodos se vuelven a conectar con el administrador y realmente realizan la actualización a la nueva versión.
- 254/402 - Soluciones de cebolla de seguridad, LLC

14.3 Fin de vida
14.3 Fin de vida
Esta página enumera las fechas de fin de vida útil (EOL) para versiones anteriores de Security Onion y componentes anteriores.
• Security Onion 2.4 alcanza su EOL el 1 de octubre de 2026 (migre a Security Onion 3)
• Security Onion 2.3 alcanzó su EOL el 6 de abril de 2024:
https://blog.securityonion.net/2023/10/6-month-eol-notice-for-security-onion-23.html
• Ubuntu 18.04 alcanzó el fin del soporte estándar de Ubuntu en abril de 2023:
https://blog.securityonion.net/2023/02/ubuntu-1804-reaches-end-of-ubuntu.html
• TheHive 3 alcanzó el EOL el 31 de diciembre de 2021. TheHive y Cortex se eliminaron por completo de Security Onion en Security Onion 2.3.120:
https://blog.securityonion.net/2022/04/security-onion-23120-now-available.html
• Security Onion 16.04 alcanzó el EOL el 16 de abril de 2021:
https://blog.securityonion.net/2021/04/security-onion-1604-has-reached-end-of.html
• Security Onion 14.04 alcanzó el EOL el 30 de noviembre de 2018:
https://blog.securityonion.net/2018/06/6-month-eol-notice-for-security-onion.html
- 255/402 - Soluciones de cebolla de seguridad, LLC

15. Cuentas
15. Cuentas
15.1 Descripción general de cuentas
En Security Onion, existen dos tipos principales de cuentas:
• cuentas del sistema operativo (SO)
• cuentas de aplicación utilizadas al autenticarse en SOC
Las cuentas del sistema operativo están controladas por utilidades de cuentas estándar de Linux. Las cuentas SOC se mantienen a través de la interfaz de administración. si por algunos
Por esta razón no puede iniciar sesión en SOC, puede usar so-user desde la línea de comando.
- 256/402 - Soluciones de cebolla de seguridad, LLC

15.2 Agregar cuentas
15.2 Agregar cuentas
15.2.1 SO
Si necesita agregar una nueva cuenta de usuario del sistema operativo, puede usar el comando adduser. Por ejemplo, para agregar una nueva cuenta llamada tom:
sudo adduser tom
consejo
Recomendamos crear nombres de usuario del sistema operativo en minúsculas para mantener la coherencia.
Para obtener más información sobre cómo agregar cuentas de usuario del sistema operativo, consulte el manual de adduser escribiendo man adduser.
15.2.2 SOC
Si necesita agregar una nueva cuenta al SOC, navegue hasta la interfaz de Administración y luego haga clic en Usuarios.
Haga clic en el botón +, complete la información necesaria y luego haga clic en el botón AGREGAR.
- 257/402 - Soluciones de cebolla de seguridad, LLC

15.2.2 SOC
consejo
Recomendamos especificar las direcciones de correo electrónico en minúsculas para mantener la coherencia.
Para obtener más información sobre la página Usuarios, consulte la sección Administración.
- 258/402 - Soluciones de cebolla de seguridad, LLC

15.3 Deshabilitar cuentas
15.3 Deshabilitar cuentas
15.3.1 SO
Si necesita deshabilitar una cuenta de usuario del sistema operativo, puede caducar la cuenta usando usermod --expiredate 1. Por ejemplo, para deshabilitar la cuenta
para el usuario tom:
sudo usermod --expiredate 1 tom
Para obtener más información, consulte el manual de contraseña escribiendo man passwd y el manual de usermod escribiendo man usermod.
15.3.2 SOC
Si necesita deshabilitar una cuenta en SOC, puede ir a Administración --> Usuarios, expandir la cuenta de usuario y hacer clic en el botón BLOQUEAR USUARIO.
Después de deshabilitar una cuenta de usuario, se mostrará con un ícono de deshabilitado en la columna Estado.
Para obtener más información sobre la página Usuarios, consulte la sección Administración.
- 259/402 - Soluciones de cebolla de seguridad, LLC

15.4 Listing Accounts
15.4 Listing Accounts
15.4.1 OS
Operating System (OS) user accounts are stored in /etc/passwd. You can get a list of all OS accounts using the following command:
cut -d: -f1 /etc/passwd
If you want a list of user accounts (not service accounts), then you can filter /etc/passwd for accounts with a UID greater than 999 like this:
cat /etc/passwd | awk -F: '$3 > 999 {print ;}' | cut -d: -f1
15.4.2 SOC
You can get a list of users in SOC by navigating to the Administration interface and then clicking Users:
To see detail on an individual user account, click the button on the left side of the row to expand the user account:
- 260/402 - Security Onion Solutions, LLC

15.4.2 SOC
Para obtener más información sobre la página Usuarios, consulte la sección Administración.
- 261/402 - Soluciones de cebolla de seguridad, LLC

15.5 Contraseñas
15.5 Contraseñas
15.5.1 Cuenta de usuario del sistema operativo
Cuando instala Security Onion por primera vez, crea una cuenta de usuario de sistema operativo estándar para usted. Si necesita cambiar la contraseña de usuario de su sistema operativo,
puedo usar el comando passwd:
contraseña
15.5.2 Cuenta raíz del sistema operativo
Su cuenta de usuario predeterminada debe tener permisos sudo. Las utilidades de línea de comandos que requieren acceso administrativo pueden tener el prefijo
sudo. Por ejemplo, el comando so-status requiere acceso administrativo para poder ejecutarlo con sudo de la siguiente manera:
sudo so-status
15.5.3 Inicios de sesión con contraseña en SOC
Inicie sesión en SOC utilizando el nombre de usuario y la contraseña que creó en el asistente de configuración o el nombre de usuario y la contraseña proporcionados por su
administrador.
Puede cambiar su contraseña en SOC haciendo clic en el ícono de usuario en la esquina superior derecha, haciendo clic en Configuración y luego yendo a Seguridad
pestaña. Tenga en cuenta que, debido a limitaciones técnicas, si cambia su contraseña de SOC aquí, no actualizará su contraseña en InfluxDB.
Sin embargo, restablecer su contraseña a través de Administración restablecerá su contraseña de InfluxDB.
Si olvidó su contraseña SOC, un administrador puede cambiarla usando la interfaz de administración.
15.5.4 Inicios de sesión sin contraseña en SOC
Una vez que hayan iniciado sesión en SOC utilizando el método de nombre de usuario y contraseña, los usuarios pueden opcionalmente habilitar inicios de sesión sin contraseña, siempre que la configuración sea
habilitado. La pantalla de inicio de sesión mostrará una sección separada para inicios de sesión sin contraseña, si está habilitada. Tenga en cuenta que está habilitado de forma predeterminada en nuevos
instalaciones.
- 262/402 - Soluciones de cebolla de seguridad, LLC

15.5.4 Inicios de sesión sin contraseña en SOC
Active el inicio de sesión sin contraseña para su usuario de SOC haciendo clic en el icono de usuario en la esquina superior derecha, haciendo clic en Configuración y luego yendo a
Pestaña de seguridad. Desplácese hacia abajo hasta la sección Claves de seguridad y siga las instrucciones proporcionadas.
De manera similar, deshabilite los inicios de sesión sin contraseña regresando a la pestaña Seguridad y haciendo clic en el ícono de eliminar al lado de cualquier Seguridad creada previamente.
Clave.
Nota
Si bien es posible utilizar TOTP MFA como segundo factor de autenticación en combinación con inicios de sesión sin contraseña, no es posible utilizar un
segunda clave de seguridad como segundo factor de autenticación con inicios de sesión sin contraseña.
importante
La especificación webbautn requiere que se acceda al servidor web a través de un nombre de host. Por lo tanto, las direcciones IP no se pueden utilizar para acceder al SOC.
al utilizar webautn. Además, el certificado TLS del servidor no debe tener ningún error. En consecuencia, sólo se permitirán certificados autofirmados
siempre que la autoridad de certificación (CA) también se haya importado a los navegadores y/o sistemas operativos del analista y se haya marcado como confiable.
- 263/402 - Soluciones de cebolla de seguridad, LLC

15,6 AMF
15,6 AMF
Puede habilitar la autenticación multifactor (MFA) para proteger aún más su cuenta. Esto se puede habilitar en SOC haciendo clic en el icono de usuario en el
esquina superior derecha, haga clic en Configuración y luego vaya a la pestaña Seguridad.
15.6.1 TOTP
Las contraseñas de un solo uso basadas en tiempo (TOTP) se pueden activar en una cuenta de usuario. TOTP requiere el uso de una aplicación de autenticación. Actualmente solo
Google Authenticator ha sido probado; sin embargo, otras aplicaciones de autenticación que implementan la contraseña de un solo uso basada en el tiempo (TOTP)
La especificación también podría funcionar.
Para exigir que todos los usuarios configuren TOTP al iniciar sesión, habilite la opción Requerir configuración de TOTP, ubicada en la pantalla Configuración: SOC >
config > servidor > Requerir TOTP.
Advertencia
Tenga en cuenta que TOTP requiere que tanto el administrador de Security Onion como el dispositivo que proporciona el código TOTP tengan configurada la hora del sistema.
correctamente. De lo contrario, el código TOTP puede considerarse inválido y rechazado.
Nota
Si pierde el acceso a su aplicación de autenticación, un administrador puede restablecer su contraseña usando la interfaz de administración, que también eliminará
el TOTP de su cuenta.
Personalización del nombre de MFA
Si utiliza varios entornos de Security Onion, como uno para pruebas y otro para producción, y ambos están configurados con TOTP MFA, SOC
los usuarios pueden tener problemas para distinguirlos en su aplicación de autenticación. Hay dos opciones para manejar esta situación:
1. La mayoría de las aplicaciones de autenticación permiten al usuario editar o cambiar el nombre de la entrada. Por ejemplo, en Google Authenticator en Android, al deslizar el dedo hacia la derecha en el
La entrada proporciona una pantalla de edición. Esto es útil si solo afecta a uno o dos usuarios.
2. Edite el emisor de TOTP a través de la pantalla de configuración de SOC, específicamente kratos > config > selfservice > métodos > totp > config >
configuración del emisor. Esto debe hacerse antes de habilitar TOTP, ya que no ayudará a los usuarios que ya configuraron TOTP.
15.6.2 Claves de seguridad de WebAuthn
WebAuthn permite el uso de sensores biométricos integrados en dispositivos móviles, dispositivos de seguridad USB y otros dispositivos de seguridad basados en PKI para
autenticar a los usuarios durante el proceso de inicio de sesión.
Si la instalación de Security Onion se ha configurado para usar claves de seguridad para MFA en lugar de inicios de sesión sin contraseña, puede agregar una o
más claves de seguridad para su cuenta como segundo factor de autenticación.
Nota
Si pierde el acceso a su dispositivo de clave de seguridad, un administrador puede restablecer su contraseña usando la interfaz de administración, que también eliminará
las claves de seguridad de su cuenta.
- 264/402 - Seguridad Cebolla Soluciones, LLC

15.6.2 Claves de seguridad de WebAuthn
importante
La especificación webbautn requiere que se acceda al servidor web a través de un nombre de host. Por lo tanto, las direcciones IP no se pueden utilizar para acceder al SOC.
al utilizar webautn. Además, el certificado TLS del servidor no debe tener ningún error. En consecuencia, sólo se permitirán certificados autofirmados
siempre que la autoridad de certificación (CA) también se haya importado a los navegadores y/o sistemas operativos del analista y se haya marcado como confiable.
- 265/402 - Soluciones de cebolla de seguridad, LLC

15.7 Control de acceso basado en roles (RBAC)
15.7 Control de acceso basado en roles (RBAC)
La capacidad de restringir u otorgar privilegios específicos a un subconjunto de usuarios está cubierta por el control de acceso basado en roles, o "RBAC" para abreviar. RBAC es un
Técnica de autorización en la que a los usuarios se les asigna uno de un pequeño conjunto de roles, y luego los roles se asocian a muchos roles de bajo nivel.
privilegios. Esto proporciona la capacidad de crear software con control de acceso detallado, pero sin la necesidad de mantener asociaciones complejas.
de usuarios a un gran número de privilegios. A los usuarios se les asigna tradicionalmente un único rol, uno que se correlaciona estrechamente con su rol en el
organización. Sin embargo, es posible asignar un usuario a múltiples roles, si es necesario.
RBAC en Security Onion cubre tanto los privilegios de Security Onion como los privilegios de Elastic Stack. Los privilegios de Security Onion solo están relacionados con
funcionalidad proporcionada específicamente por los componentes desarrollados por Security Onion, mientras que los privilegios de pila elástica solo están involucrados con el
Elasticsearch, Kibana y pila Elastic relacionada. Por ejemplo, Security Onion comprobará si un usuario tiene permiso para crear una solicitud PCAP,
mientras que Elastic comprobará si el mismo usuario tiene permiso para ver un índice o documento en particular almacenado en Elasticsearch.
15.7.1 Funciones predeterminadas
Security Onion viene con los siguientes roles de usuario: superusuario, analista, analista limitado, auditor y auditor limitado.
Consulte la siguiente tabla que explica los privilegios específicos de Security Onion otorgados a cada función.
|                                    | superusuario | analista | analista limitado | auditor | auditor limitado |
| ---------------------------------- | --------- | ------- | --------------- | ------- | --------------- |
| Ver alertas | X | X | X | X | X |
| Confirmar alertas | X | X | X |         |                 |
| Escalar alertas y eventos | X | X | X |         |                 |
| Ver detecciones | X | X | X | X | X |
| Modificar (y eliminar) detecciones | X | X |                 |         |                 |
| Ver eventos en Hunt | X | X | X | X | X |
| Ver propios trabajos de PCAP | X | X | X | O | O |
| Ver todos los trabajos de PCAP | X | X |                 | X |                 |
| Pivote al trabajo PCAP desde el evento | X | X | X |         |                 |
| Solicitar trabajos PCAP arbitrarios | X | X |                 |         |                 |
| Eliminar el propio trabajo PCAP | X | X | X | O | O |
| Eliminar cualquier trabajo PCAP | X | X |                 |         |                 |
| Ver todos los nodos en Grid | X | X | X | X | X |
| Ver todos los usuarios | X | X |                 | X |                 |
| Ver todos los roles de los usuarios | X | X |                 | X |                 |
| Ver usuario propio | X | X | X | X | X |
| Ver roles de usuario propios | X | X | X | X | X |
| Cambiar propia contraseña | X | X | X | X | X |
| Agregar, actualizar y restablecer usuarios de SOC | X |         |                 |         |                 |
| Modificar y sincronizar la configuración de Grid | X |         |                 |         |                 |
| Administrar la membresía de nodos en Grid | X |         |                 |         |                 |
| Iniciar acciones de nodo (Ej.: reiniciar) | X |         |                 |         |                 |
| Administrar clientes API | X |         |                 |         |                 |
| Ver y enumerar clientes API existentes | X |         | X |         |                 |
| Administrar consultas activas | X |         |                 |         |                 |
| Ver guías | X | X | X | X | X |
| Chatea con Onion AI | X | X |                 |         |                 |
| Eliminar sesiones propias de Onion AI | X | X |                 |         |                 |
| Ver el historial de IA de Onion | X | X |                 |         |                 |
| Ver el historial de IA de Onion de todos los usuarios | X |         |                 |         |                 |
Nota
Tanto el rol de auditor como el de auditor limitado pueden interactuar con PCAP creados previamente si se crearon antes de que un usuario se convirtiera a ese.
rol (por ejemplo, el usuario fue degradado de analista a auditor). Esto se indica con O en la tabla anterior.
Nota
El agente Security Onion utiliza una función del sistema llamada agente que se ejecuta en cada nodo de Security Onion Grid. Este papel especial se le da a
permisos de trabajos/proceso, nodos/lectura y nodos/escritura (definidos en la parte inferior de esta página). Evite crear roles personalizados que compartan los mismos
nombre como roles proporcionados por Security Onion.
- 266/402 -
Soluciones de cebolla de seguridad, LLC

15.7.2 Superusuarios
15.7.2 Superusuarios
Una vez completada una nueva instalación de Security Onion, se creará un único usuario administrador y se le asignará la función de superusuario. Adicional
A los usuarios también se les puede asignar la función de superusuario, si lo desean.
15.7.3 Agregar un usuario con una función específica
En la interfaz de Administración, navegue hasta la pantalla Usuarios y haga clic en el ícono + para agregar un nuevo usuario. En el cuadro de diálogo emergente puede comprobar el
roles que le gustaría asignar al nuevo usuario.
15.7.4 Modificación de roles de usuario
En la interfaz de Administración, navegue hasta la pantalla Usuarios y haga clic en el ícono > a la izquierda de la dirección de correo electrónico que necesita ajuste. comprobar o
desmarque los roles deseados.
15.7.5 Asignación de roles predeterminada
Cuando se crea un usuario, opcionalmente se le puede asignar automáticamente una función específica. Para habilitar esta asignación automática, localice el
configuración defaultRole y especifique el nombre de función predeterminado deseado. Esta asignación automática se producirá cuando el usuario inicie sesión
SOC por primera vez.
Advertencia
Si un administrador elimina todas las asignaciones de roles de un usuario y el usuario vuelve a iniciar sesión, a ese usuario se le asignará automáticamente nuevamente el valor predeterminado.
papel. Bloquee siempre a los usuarios inactivos en lugar de eliminar las asignaciones de roles de un usuario.
15.7.6 Creación de roles personalizados
Advertencia
La creación de roles RBAC personalizados es una característica avanzada que se recomienda solo para administradores experimentados.
Estos pasos lo guiarán a través de un ejemplo en el que deseamos introducir un nuevo rol llamado Eastcoast-analyst, que heredará el mismo
Permisos de Security Onion como analista limitado, pero estarán restringidos para ver solo un subconjunto de documentos en la pila Elastic. basamos esto
rol en el rol de analista limitado en lugar del rol de analista para que el usuario no tenga la capacidad de crear PCAP arbitrarios en ningún sensor.
1. Para la función Security Onion: siga las instrucciones de la siguiente sección titulada "Definición de funciones Security Onion" para crear una nueva función denominada
analista de la costa este.
2. Para la función de pila elástica: cree un nuevo archivo de función json llamado eastcoast-analyst.json en /opt/so/saltstack/local/salt/
búsqueda elástica/roles. En este ejemplo definiremos el nuevo rol que solo permite el acceso a documentos desde sensores en la costa este.
de los Estados Unidos. Específicamente, la función incluirá un filtro de consulta que limite los resultados de búsqueda para incluir solo documentos que se originen en
sensores que tienen un nombre con el prefijo nyc (Nueva York) o atl (Atlanta).
analista-costa-este.json:
{
"grupo": [
"cancelar_tarea",
"crear_instantánea",
"supervisar",
"monitor_data_frame_transforms",
"monitor_ml",
"monitor_rollup",
"monitor_instantánea",
"monitor_text_structure",
"monitor_transformar",
"monitor_watcher",
- 267/402 - Seguridad Cebolla Soluciones, LLC

15.7.6 Creación de roles personalizados
"leer_ccr",
"read_ilm",
"read_pipeline",
"read_slm"
],
"índices": [
{
"nombres": [
"entonces-*"
],
"privilegios": [
"índice",
"mantenimiento",
"supervisar",
"leer",
"read_cross_cluster",
"view_index_metadatos"
],
"query": "{ \"bool\": { \"debería\": [ { \"prefix\": { \"observer.name\": \"nyc\" }}, { \"prefix\": { \"observer.name\": \"atl\" }} ]}}"
}
],
"aplicaciones": [
{
"aplicación": "Kibana-.Kibana",
"privilegios": [
"feature_discover.all",
"feature_dashboard.all",
"feature_canvas.all",
"feature_maps.all",
"feature_ml.all",
"feature_logs.read",
"feature_visualize.all",
"feature_infrastructure.read",
"feature_apm.read",
"feature_uptime.read",
"feature_siem.read",
"feature_dev_tools.read",
"feature_advancedSettings.read",
"feature_indexPatterns.read",
"feature_savedObjectsManagement.read",
"feature_savedObjectsTagging.read",
"feature_fleet.all",
"feature_actions.read",
"feature_stackAlerts.read"
],
"recursos": [
"*"
]
}
],
"ejecutar_as": []
}
Nota
Elasticsearch requiere la compra de una suscripción para poder utilizar la seguridad a nivel de campo o documento, como se menciona en el ejemplo anterior.
Nota
El formato del json en este archivo debe coincidir con el cuerpo de la solicitud descrito en los documentos de Elastic aquí: https://www.elastic.co/guide/en/elasticsearch/
referencia/current/security-api-put-role.html#security-api-put-role-request-body.
Los permisos de índices y clústeres disponibles se explican en los documentos de Elastic aquí: https://www.elastic.co/guide/en/elasticsearch/reference/
actual/privilegios-de-seguridad.html.
Los permisos de Kibana disponibles se pueden obtener ejecutando el siguiente comando en el nodo administrador:
sudo so-elasticsearch-query _security/privilege/kibana-.Kibana | jq'. | valores_map(claves)'
1. Ejecute so-checkin desde el administrador:
sudo so-checkin
- 268/402 - Soluciones de cebolla de seguridad, LLC

15.7.7 Definición de roles cebolla de seguridad
15.7.7 Definición de roles cebolla de seguridad
Hay dos formas de definir un rol personalizado de Security Onion:
• Construirlo desde cero utilizando los permisos integrados y las funciones predeterminadas disponibles como se describe más adelante en este documento, o
• Heredar los permisos de otra función y, opcionalmente, agregar más permisos a la nueva función personalizada.
Nota
El archivo custom_roles contiene más instrucciones sobre cómo modificar roles que no están dentro del alcance de esta documentación.
La sintaxis común para cualquiera de los métodos de definir un rol es la siguiente:
<existing role or permission>:<new role>
1. La creación del rol para el analista de la costa este mencionado anteriormente utilizando el primer método, creando el rol personalizado desde cero, se escribiría así:
2. administrador de casos: analista de la costa este
3. administrador de eventos: analista de la costa este
4. monitor de nodo: analista de la costa este
5. monitor de usuario: analista de la costa este
6. usuario del trabajo: analista de la costa este
7. Alternativamente, el rol de analista de la costa este podría crearse heredando los permisos del rol de analista:
8. analista limitado: analista de la costa este
PRIVILEGIOS DE SECURITY ONION Y FUNCIONES PREDETERMINADAS
Los privilegios de Security Onion de bajo nivel disponibles se enumeran en la siguiente tabla:
casos/leer Leer toda la información relacionada con el caso para todos los casos
casos/escritura Crear y actualizar casos, y escalar eventos a casos
clientes/leer Lista y ver clientes API existentes. Los secretos del cliente son inaccesibles.
clientes/escritura Crear y actualizar clientes API y regenerar secretos
clientes/eliminar Eliminar clientes API
config/read Leer los parámetros de configuración del sistema
config/write Actualiza y en algunos casos duplica los parámetros de configuración del sistema.
detecciones/lectura Leer todos los detalles relacionados con la detección
detecciones/escritura Crear y actualizar detecciones y anulaciones
eventos/lectura Lectura de Elasticsearch
eventos/lectura Lectura de Elasticsearch
eventos/escritura Escribir en Elasticsearch
events/ack Reconocer alertas
Grid/read Leer información sobre el grid y sus membresías de nodos
Grid/write Aceptar y rechazar membresías de Grid de nodos nuevos y existentes
trabajos/lectura Ver todos los trabajos de PCAP
jobs/pivot Pivotar al trabajo PCAP desde el evento
trabajos/escritura Solicitar trabajos PCAP arbitrarios
trabajos/eliminar Eliminar cualquier trabajo PCAP
trabajos/proceso Actualizar, leer y adjuntar paquetes a todos los trabajos PCAP pendientes †
nodos/lectura Ver todos los nodos en Grid
nodos/escritura Actualizar información del nodo †
roles/read Ver todos los roles de los usuarios
roles/write Cambiar el rol de cualquier usuario
consultas/eliminar Cancelar consultas activas
consultas/lectura Ver consultas activas
usuarios/leer Ver todos los usuarios
usuarios/escribir Cambiar la contraseña de cualquier usuario
usuarios/eliminar Eliminar cualquier usuario
libros de jugadas/leer Ver todos los libros de jugadas
libros de jugadas/escritura Actualmente sin usar
libros de jugadas/eliminar Actualmente sin usar
asistente/read_authored Ver el propio historial de conversaciones de Onion AI
asistente/write_authored Chat con Onion AI
asistente/delete_authored Eliminar el propio historial de conversaciones de Onion AI
asistente/read_shared Ver el historial de conversaciones compartidas de Onion AI
asistente/read_all Ver todo el historial de conversaciones de Onion AI
asistente/write_all Actualmente sin uso
asistente/delete_all Actualmente sin uso
- 269/402 - Soluciones de cebolla de seguridad, LLC

15.7.7 Definición de roles cebolla de seguridad
Estos privilegios discretos luego se recopilan en grupos de privilegios como se define a continuación:
case-admin casos/lectura, casos/escritura
caso-monitor casos/lectura
cliente-admin clientes/lectura, clientes/escritura, clientes/eliminar
cliente-monitor clientes/lectura
config-admin configuración/lectura, configuración/escritura
config-monitor configuración/lectura
detecciones-admin detecciones/lectura, detecciones/escritura
detecciones-monitor detecciones/lectura
event-admin eventos/lectura, eventos/escritura, eventos/ack
eventos de monitor de eventos/lectura
Grid-admin Cuadrícula/lectura, Cuadrícula/escritura
Monitor de red Cuadrícula/lectura
job-admin trabajos/lectura, trabajos/pivote, trabajos/escritura, trabajos/eliminar
trabajos de supervisión de trabajos/lectura
trabajos de usuario de trabajo/pivote
trabajos/proceso del procesador de trabajos †
nodo-admin nodos/lectura, nodos/escritura
nodos de monitor de nodo/lectura
query-admin consultas/leer, consultas/eliminar
consultas de seguimiento de consultas/lectura
roles de administrador de usuario/lectura, roles/escritura, usuarios/lectura, usuarios/escritura, usuarios/eliminar
roles de monitor de usuario/lectura, usuarios/lectura
libro de jugadas-monitorear libros de jugadas/leer
playbook-admin playbooks/leer, playbooks/escribir, playbooks/eliminar
asistente-usuario asistente/read_authored, asistente/write_authored, asistente/delete_authored, asistente/read_shared
asistente-administrador asistente/read_authored, asistente/write_authored, asistente/delete_authored, asistente/read_shared, asistente/
leer_todo, asistente/escribir_todo, asistente/eliminar_todo
asistente-monitor asistente/read_authored, asistente/read_shared, asistente/read_all
† destinado para uso exclusivo de agentes Sensoroni
- 270/402 - Soluciones de cebolla de seguridad, LLC

15.8 Kratos
15.8 Kratos
La autenticación SOC está a cargo de Kratos. Puedes leer más sobre Kratos en https://github.com/ory/kratos.
15.8.1 Configuración
Puede configurar Kratos yendo a Administración --> Configuración --> kratos.
15.8.2 Más información
Nota
Para obtener más información sobre Kratos, consulte https://github.com/ory/kratos.
- 271/402 - Soluciones de cebolla de seguridad, LLC

16. Servicios
16. Servicios
Puede controlar servicios individuales con los scripts so-<componente>-<verbo>. Puede ver una lista de todos estos scripts con lo siguiente
comando:
ls /usr/sbin/so-*
Los siguientes ejemplos son para Zeek, pero puedes sustituirlos por cualquier servicio que estés intentando controlar (Logstash, Elasticsearch, etc.).
Iniciar Zeek:
sudo so-zeek-inicio
Detener a Zeek:
sudo so-zeek-parada
Reiniciar Zeek:
sudo so-zeek-reiniciar
- 272/402 - Soluciones de cebolla de seguridad, LLC

17. Personalización
17. Personalización
17.1 Descripción general de la personalización
Esta sección cubre cómo personalizar Security Onion para su entorno.
- 273/402 - Soluciones de cebolla de seguridad, LLC

17.2 Personalización de la consola Security Onion
17.2 Personalización de la consola Security Onion
Puede personalizar Security Onion Console yendo a Administración --> Configuración --> SOC.
A continuación se muestran algunas formas en las que puede personalizar SOC. Una vez completadas todas las personalizaciones, puede hacer que los cambios surtan efecto al
haciendo clic en la barra de Opciones en la parte superior y luego haciendo clic en el botón SINCRONIZAR CUADRICULA.
- 274/402 - Soluciones de cebolla de seguridad, LLC

17.2.1 Página de inicio de sesión
17.2.1 Página de inicio de sesión
Puede personalizar la página de inicio de sesión de SOC con un banner de inicio de sesión yendo a Administración --> Configuración --> SOC --> archivos --> SOC --> Iniciar sesión
Pancarta. El banner de inicio de sesión utiliza el formato común Markdown (.md) y puede obtener más información al respecto en https://markdownguide.org.
17.2.2 Página de descripción general
Después de iniciar sesión en SOC, comenzará en la página principal de descripción general de SOC, que también se puede personalizar. Puedes personalizar esto yendo a
Administración --> Configuración --> SOC --> archivos --> SOC --> Página de descripción general. Esto utiliza el formato Markdown como se mencionó anteriormente. puedes agregar
imágenes, pero deben estar alojadas desde otro host al que pueda acceder el navegador del usuario.
17.2.3 Enlaces
También puedes personalizar los enlaces en el lado izquierdo. Para hacerlo, vaya a Administración --> Configuración --> SOC --> servidor --> cliente --> herramientas.
17.2.4 DNS inverso
Cuando visualiza direcciones IP en Alertas, Paneles o Búsqueda, es posible que desee habilitar las búsquedas DNS inversas automáticas para proporcionar más
información. Puede hacerlo yendo a Administración --> Configuración --> SOC --> configuración --> servidor --> enableReverseLookup.
17.2.5 Búsquedas locales
Si no desea habilitar las búsquedas DNS inversas para todas las direcciones IP pero tiene un subconjunto de direcciones IP que le gustaría resolver
nombres de host en SOC, luego puede crear un archivo CSV en /nsm/custom-mappings/ip-descriptions.csv en su Administrador y completar el archivo
con direcciones IP y descripciones de la siguiente manera:
propiedad intelectual, descripción
Luego, Elasticsearch ingerirá el CSV y utilizará el contenido para completar un nuevo índice llamado so-ip-mappings.
Cuando esté viendo direcciones IP en Alertas, Paneles o Búsqueda, Security Onion Console verificará primero las asignaciones locales. Si no encuentra
una coincidencia, intentará una búsqueda DNS inversa (si está habilitada).
Si más adelante necesita realizar cambios en sus asignaciones de IP/Descripciones locales, realice los cambios en /nsm/custom-mappings/ip-
descripciones.csv y Elasticsearch actualizarán automáticamente el índice so-ip-mappings.
17.2.6 Casos
Cases viene con ajustes preestablecidos para cosas como categoría, gravedad, TLP, PAP, etiquetas y estado. Puede modificar estos ajustes preestablecidos yendo a
Administración --> Configuración --> SOC --> servidor --> cliente --> caso --> ajustes preestablecidos.
17.2.7 Tiempo de espera de sesión
El tiempo de espera predeterminado para las sesiones de inicio de sesión de los usuarios es de 24 horas. Este es un período de tiempo fijo y caducará independientemente de si el usuario está activo o inactivo.
en SOC. Puede configurar esto yendo a Administración --> Configuración --> kratos --> configuración --> sesión --> vida útil.
17.2.8 Consultas personalizadas
Si desea agregar sus propias consultas personalizadas a Alertas, Casos, Paneles, Detecciones o Búsqueda, puede ir a Administración --> Configuración
--> SOC --> configuración --> servidor --> cliente y luego seleccione la aplicación específica que desea modificar.
- 275/402 - Soluciones de cebolla de seguridad, LLC

17.2.9 Menú Acción
Advertencia
Cuando guarda sus consultas personalizadas, SOC guarda la lista completa de consultas (incluidas nuestras consultas predeterminadas incluidas en el producto). Así que si actualizas
a una nueva versión que incluye consultas predeterminadas nuevas o actualizadas, no verá las consultas predeterminadas nuevas o actualizadas ya que su lista de consultas personalizadas es
anulando el valor predeterminado.
Para ver todos los campos disponibles para sus consultas, vaya a la tabla Eventos y luego haga clic en la flecha para expandir una fila. Mostrará todos los
campos individuales de ese evento en particular.
Por ejemplo, suponga que desea agregar información GeoIP como source.geo.region_iso_code o destino.geo.region_iso_code a
Alertas. Iría a Administración --> Configuración --> SOC --> config --> servidor --> cliente --> alertas --> consultas e insertaría la siguiente línea
donde quieras que aparezca en la lista de consultas:
{ "name": "Agrupar por IP de origen/Puerto/Geo, IP de destino/Puerto/Geo, Nombre", "query": "* | groupby source.ip source.port source.geo.region_iso_code
destino.ip destino.puerto destino.geo.región_iso_código regla.nombre" },
Tenga en cuenta que es posible que algunos eventos no tengan información GeoIP y esta consulta solo mostrará aquellas alertas que sí tengan información GeoIP.
17.2.9 Menú Acción
Alertas, Paneles y Búsqueda tienen un menú de acciones con varias acciones predeterminadas. Si desea agregar su propio HTTP GET o POST personalizado
acciones, puede ir a Administración --> Configuración --> SOC --> acciones y hacer clic en el signo más en la parte inferior de la lista. Luego complete el
y guarde la nueva acción.
17.2.10 Escalamiento
Las alertas, los paneles y la búsqueda muestran registros con un triángulo azul que le permite escalar el evento. Esto está predeterminado en nuestra interfaz de Casos. si por
Por algún motivo desea escalar a un sistema de administración de casos diferente, puede cambiar esta configuración. Puedes ir a Administración -->
Configuración --> SOC --> servidor --> módulos --> casos y especifique uno de los siguientes valores:
• SOC: habilita la gestión de casos integrada, con nuestro menú de escalamiento (predeterminado).
• elasticcases: permite escalar a la herramienta Elastic Cases. Las escaladas siempre abrirán un nuevo caso; no habrá un avanzado
menú emergente de escalada. Este módulo utilizará el mismo usuario/contraseña que utiliza SOC para hablar con Elastic. Tenga en cuenta, sin embargo, que los casos elásticos son
en realidad es una característica de Kibana, por lo tanto, cuando se utiliza esta configuración, SOC se comunicará con el servicio local de Kibana (a través de su API) para
escaladas de casos.
- 276/402 - Soluciones de cebolla de seguridad, LLC

17.3 nginx
17.3 nginx
nginx es el servidor web principal de Security Onion.
17.3.1 Configuración
Puede modificar la configuración de nginx yendo a Administración --> Configuración --> nginx.
17.3.2 Reemplazo del certificado predeterminado
Si desea reemplazar el certificado predeterminado con su propio certificado, puede hacerlo como se muestra a continuación.
Advertencia
¡Tenga mucho cuidado al modificar configuraciones avanzadas como esta!
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• En el lado izquierdo, vaya a nginx, expanda ssl y luego seleccione la configuración Reemplazar certificado predeterminado.
• En el lado derecho, cambie la configuración a verdadero y luego haga clic en la marca de verificación para guardar el valor.
• En el lado izquierdo, seleccione la configuración Archivo de certificado SSL/TLS.
• En el lado derecho, pegue su nuevo archivo de certificado y luego haga clic en la marca de verificación para guardarlo.
• En el lado izquierdo, seleccione la configuración Archivo de clave SSL/TLS.
• En el lado derecho, pegue su nuevo archivo de clave y luego haga clic en la marca de verificación para guardarlo.
- 277/402 - Soluciones de cebolla de seguridad, LLC

17.3.3 Más información
17.3.3 Más información
Nota
Para obtener más información sobre nginx, consulte https://nginx.org/.
- 278/402 - Soluciones de cebolla de seguridad, LLC

17.4 Representante
17.4 Representante
El programa de instalación le preguntará si desea conectarse a través de un servidor proxy y, de ser así, configurará automáticamente el sistema.
Si tiene problemas para instalar a través de su servidor proxy, puede considerar la opción Airgap ya que todo se instalará a través de la imagen ISO.
17.4.1 Configuración
Si necesita realizar cambios después de la instalación, consulte la configuración del proxy en Administración --> Configuración --> administrador.
- 279/402 - Soluciones de cebolla de seguridad, LLC

17.4.2 Información general
Una vez allí, seleccione las opciones proxy o no_proxy.
17.4.2 Información general
No hay forma de configurar un proxy global en Linux, pero varias herramientas enrutarán su tráfico a través de un proxy si se agregan las siguientes líneas a
/etc/entorno:
http_proxy=<proxy_url>
https_proxy=<proxy_url>
ftp_proxy=<proxy_url>
no_proxy="host local, 127.0.0.1, <ip_administración>, <nombre de host>"
donde:
• <proxy_url> es la URL del servidor proxy. (Por ejemplo, http://10.0.0.2:3128 o https://usuario:contraseña@tu.proxy.url)
• <management_ip> es la dirección IP del cuadro Security Onion.
• <nombre de host> es el nombre de host del cuadro Security Onion.
Nota
Es posible que también deba incluir la dirección IP y el nombre de host del administrador en la variable no_proxy anterior si configura el proxy en un sensor.
nodo.
Para configurar los ajustes del proxy de Docker, consulte https://docs.docker.com/network/proxy/.
Para configurar git para que use un proxy para todos los usuarios, agregue lo siguiente a /etc/gitconfig:
[http]
proxy = <proxy_url>
17.4.3 sudo
Si va a ejecutar algo usando sudo, recuerde usar la opción -i para forzarlo a procesar las variables de entorno. Por ejemplo:
sudo -i so-suricata-restart
Advertencia
El uso de sudo su ignorará /etc/environment; en su lugar, use sudo su si necesita operar como root.
17.4.4 Reglas NIDS
Si está utilizando un proxy y necesita descargar conjuntos de reglas NIDS, también deberá configurar los ajustes del proxy para las descargas del conjunto de reglas NIDS.
Estas configuraciones son independientes de la configuración de proxy de todo el sistema anterior. Consulte la documentación de NIDS para obtener detalles sobre la configuración del
URL de proxy, nombre de usuario de proxy, contraseña de proxy y ruta de CA de proxy para descargas de conjuntos de reglas.
- 280/402 - Soluciones de cebolla de seguridad, LLC

17.5 Cortafuegos
17.5 Cortafuegos
Esta sección cubrirá tanto los firewalls de red fuera de Security Onion como el firewall basado en host integrado en Security Onion.
17.5.1 Cortafuegos de red
Esta primera subsección analizará los firewalls de red fuera de Security Onion.
comunicación por Internet
Al configurar firewalls de red para implementaciones conectadas a Internet (no Airgap), querrá asegurarse de que la implementación pueda conectarse
saliente (TCP/443) a lo siguiente:
• raw.githubusercontent.com (clave pública de Security Onion)
• sigs.securityonion.net (archivos de firma para contenedores Security Onion)
• ghcr.io (descargas de contenedores)
• pkg-containers.githubusercontent.com (descargas de contenedores)
• reglas.emergingthreatspro.com (reglas IDS de amenazas emergentes)
• reglas.emergingthreats.net (reglas abiertas de IDS de amenazas emergentes)
• github.com (actualizaciones de reglas de Strelka y Sigma)
• objects.githubusercontent.com (actualizaciones de reglas de Strelka y Sigma)
Si está utilizando nuestra imagen ISO, también necesitará acceso a lo siguiente:
• repo.securityonion.net (repositorio principal para actualizaciones de paquetes de Oracle Linux)
• repo-alt.securityonion.net (repositorio secundario para actualizaciones de paquetes de Oracle Linux)
• so-repo-east.s3.us-east-005.backblazeb2.com (repositorio secundario para actualizaciones de paquetes de Oracle Linux)
Si elige habilitar las actualizaciones de GeoIP para Elasticsearch, también necesitará acceso a lo siguiente:
• geoip.elastic.co
• almacenamiento.googleapis.com
Si elige habilitar el conjunto de reglas de Snort Talos, también necesitará acceso a lo siguiente:
• www.snort.org
- 281/402 - Soluciones de cebolla de seguridad, LLC

17.5.2 Cortafuegos del host
Comunicación de nodo
Al configurar firewalls de red para implementaciones distribuidas, querrá asegurarse de que los nodos puedan conectarse como se muestra en la siguiente tabla.
Tenga en cuenta que algunas de las fuentes y destinos enumerados en la tabla tienen definiciones específicas:
• Los nodos de Security Onion Grid incluyen cualquier nodo unido a su administrador. Esto incluye nodos de búsqueda, sensores, nodos de flota, nodos receptores,
y nodos IDH.
• Los nodos de búsqueda son nodos de Grid que ejecutan Elasticsearch y se unen al administrador para ampliar su clúster Elastic.
• Los nodos del clúster elástico incluyen los nodos de búsqueda y el propio administrador.
• Endpoint Elastic Agents incluye cualquier punto final en el que haya implementado el Elastic Agent y desee enviar los datos a su equipo de seguridad.
Rejilla de cebolla.
Origen (SRC) Destino (DST) Puerto(s) de destino (TCP) Descripción
Administrador de nodos Security Onion Grid 443, 4505, 4506, 5000, 5055, 8086, 8220, 8443 Gestión, Registro, Salt, Actualizaciones
Nodos Security Onion Grid Nodo Fleet 5055, 8220 Gestión y datos del agente elástico
Nodos Security Onion Grid Nodo receptor 5055 Datos del agente elástico
Administrador de nodos de búsqueda 443, 4505, 4506, 5000, 5055, 8086, 8220, 8443, 9696 Gestión, Registro, Salt, Actualizaciones, Redis
Nodos del clúster elástico Nodos del clúster elástico 9200, 9300 Logstash a Elasticsearch y Elasticsearch de nodo a
nodo
Endpoint Elastic Agents Manager 8220, 8443, 5055 Gestión de agentes elásticos, actualizaciones binarias, datos
Endpoint Elastic Agents Fleet nodo 5055, 8220 Administración y datos de Elastic Agent
Endpoint Elastic Agents Nodo receptor 5055 Datos del Elastic Agent
Nodo de flota Nodo receptor 5056 Logstash a Logstash
Administrador de nodos de flota 5056, 9200 Logstash-to-Logstash y Elasticsearch de nodo a nodo
Administrador del nodo IDH 2222 SSH para administración
17.5.2 Cortafuegos del host
El resto de esta sección cubrirá el firewall del host integrado en Security Onion.
Nota
Security Onion bloquea el firewall de forma predeterminada.
17.5.3 Configuración del firewall del host
Puede configurar el firewall yendo a Administración --> Configuración --> firewall --> grupos de hosts.
- 282/402 - Soluciones de cebolla de seguridad, LLC

17.5.4 Revisión del firewall del host
Si por alguna razón no puede acceder al SOC, puede usar el comando so-firewall para permitir que la dirección IP de su navegador web se conecte
(reemplazando <DIRECCIÓN IP> con la dirección IP real de su navegador web):
sudo so-firewall includehost analista <DIRECCIÓN IP>
17.5.4 Revisión del firewall del host
Puede ver toda la configuración del firewall desde la línea de comando usando el comando iptables de esta manera:
sudo iptables-nvL
Advertencia
Puede usar este comando para ver la configuración de iptables, pero no modifique el firewall manualmente usando iptables ya que lo administra
Sal. Sólo debe realizar cambios a través de la pantalla de Configuración como se muestra arriba.
17.5.5 Grupos de puertos
Los grupos de puertos son una forma de agrupar puertos similares a un alias de puerto/servicio de firewall. Por ejemplo, si tiene un servidor web, puede agregar
los puertos 80 y 443 en un grupo de puertos.
17.5.6 Grupos de anfitriones
Los grupos de hosts son similares a los grupos de puertos, pero para almacenar listas de hosts a los que se les permitirá conectarse a los grupos de puertos asociados.
17.5.7 Función
El estado del firewall está diseñado con la idea de crear grupos de puertos y grupos de hosts, cada uno con su propio alias o nombre, y asociar el
dos para crear una regla de permiso. Un nodo que tiene un grupo de puertos y una asociación de grupo de hosts asignados permitirá que esos hosts se conecten.
a esos puertos en ese nodo.
- 283/402 - Soluciones de cebolla de seguridad, LLC

17.5.8 Configuración avanzada del firewall
Las reglas de permiso predeterminadas para cada nodo están definidas por su función (administrador, nodo de búsqueda, sensor, nodo pesado, etc.) en la cuadrícula. Grupos de hosts y puerto
Los grupos se pueden crear o modificar desde el nodo administrador yendo a Administración --> Configuración --> firewall --> grupos de hosts. Cuando se configura
se ejecuta en un nuevo nodo, le pedirá al administrador que se agregue a los grupos de host apropiados. Todos los tipos de nodos se agregan al grupo de host minion para
permitir la comunicación con Salt. Si agregara un nodo de búsqueda, vería su IP aparecer tanto en el servidor minion como en el host search_node.
grupos.
17.5.8 Configuración avanzada del firewall
Cuando vaya a Administración --> Configuración --> firewall, solo verá grupos de hosts de forma predeterminada. Si necesita modificar grupos de puertos, entonces
deberá hacer clic en el menú Opciones y luego habilitar la opción Mostrar configuración avanzada.
Modificar un grupo de puertos predeterminado
El grupo de hosts del analista tiene permiso para acceder a los puertos nginx, que son 80 y 443 de forma predeterminada. En este ejemplo, ampliaremos el nginx predeterminado.
grupo de puertos para incluir un puerto personalizado.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, ubique el grupo de puertos nginx y luego seleccione tcp.
• En el lado derecho, seleccione el nodo del administrador, especifique el puerto personalizado que desea agregar y luego haga clic en la marca de verificación para guardar el valor.
• Si desea aplicar las reglas inmediatamente, haga clic en el botón SINCRONIZAR CUADRICULA debajo del menú Opciones en la parte superior de la página.
Crear un grupo de host personalizado con un grupo de puertos personalizado
En este ejemplo, agregaremos un nuevo grupo de hosts personalizado para permitir que un conjunto personalizado de hosts se conecte a un puerto personalizado en un nodo IDH.
• En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada.
• En el lado izquierdo, vaya al firewall, seleccione grupos de hosts y luego seleccione customhostgroup0.
• En el lado derecho, seleccione el nodo IDH al que desea permitir el acceso, agregue la lista de hosts que requieren acceso y luego haga clic en
marque la casilla para guardar el valor.
• En el lado izquierdo, vaya al firewall, seleccione grupos de puertos, seleccione customportgroup0 y luego seleccione el protocolo apropiado.
• En el lado derecho, seleccione el nodo IDH al que desea permitir el acceso, agregue su puerto personalizado y luego haga clic en la marca de verificación para guardar el
valor.
• En el lado izquierdo, vaya a firewall, rol y luego seleccione IDH, cadena, DOCKER-USER, hostgroups, customhostgroup0, portgroups.
• En el lado derecho, seleccione el nodo IDH al que desea permitir el acceso, agregue el grupo de puertos customportgroup0 y luego haga clic en
marque la casilla para guardar el valor.
• La próxima vez que el nodo IDH se registre, debería obtener las reglas de firewall adecuadas.
- 284/402 - Soluciones de cebolla de seguridad, LLC

17.6 Correo electrónico
17.6 Correo electrónico
Algunas aplicaciones dependen de tener un servidor de correo en el propio sistema operativo y otras aplicaciones tienen su propia configuración de correo, por lo que no dependen
en un servidor de correo en el propio sistema operativo.
17.6.1 Sistema operativo
Puedes instalar y configurar tu servidor de correo favorito. Dependiendo de sus necesidades, esto podría ser algo simple como nullmailer o
algo más complejo como exim4.
17.6.2 Alerta Elast
Siga los pasos en la sección ElastAlert.
- 285/402 - Soluciones de cebolla de seguridad, LLC

17,7 NTP
17,7 NTP
Dependiendo de cómo lo instaló, el sistema operativo subyacente puede estar configurado para obtener actualizaciones de tiempo del proyecto NTP Pool y
quizás otros como alternativa. Es posible que desee cambiar esta configuración NTP predeterminada a su proveedor NTP preferido yendo a Administración -->
Configuración --> ntp.
Para una implementación distribuida, es de vital importancia que todos los nodos tengan su reloj sincronizado. De lo contrario, puede encontrarse con problemas donde los registros
u otros tipos de datos parecen faltar.
Para obtener más información sobre la hora del sistema operativo, consulte la sección Zonas horarias.
- 286/402 - Soluciones de cebolla de seguridad, LLC

17.8 SSH
17.8 SSH
Security Onion utiliza los últimos paquetes SSH. No gestiona la configuración SSH en /etc/ssh/sshd_config con Salt. Esto te permite
para agregar cualquier módulo PAM o habilitar la autenticación de dos factores (2FA) de su elección.
- 287/402 - Soluciones de cebolla de seguridad, LLC

17.9 Nombre de host
17.9 Nombre de host
El programa de instalación genera certificados basados en el nombre de host y no admitimos cambiar el nombre de host después de la instalación. Por favor asegúrese de que su
El nombre de host es correcto durante la instalación, como se menciona en la sección Mejores prácticas.
- 288/402 - Soluciones de cebolla de seguridad, LLC

17.10 Dirección IP
17.10 Dirección IP
La sección Mejores prácticas recomienda evitar cambiar las direcciones IP después de la instalación. Si por alguna razón debes hacerlo, puedes
Pruebe la utilidad experimental so-ip-update.
Advertencia
so-ip-update es una utilidad experimental y solo admite máquinas independientes, no implementaciones distribuidas.
Advertencia
Es posible que aún necesites actualizar manualmente la dirección IP en algunas configuraciones, como la configuración de Descarga binaria de Elastic Fleet Agent.
- 289/402 - Soluciones de cebolla de seguridad, LLC

17.11 DNS
17.11 DNS
El DNS normalmente se configura durante la configuración inicial. Si luego necesita cambiar su configuración de DNS, puede usar la consola de NetworkManager
utilidades, nmtui (interfaz de usuario basada en texto) y nmcli (interfaz de línea de comandos). Puede obtener más información en https://docs.oracle.com/en/operating-
sistemas/oracle-linux/9/network/network-NetworkConfigurationTools.html.
- 290/402 - Soluciones de cebolla de seguridad, LLC

17.12 URL de acceso web
17.12 URL de acceso web
Si necesita cambiar la URL para el acceso web a Security Onion (por ejemplo, de IP a FQDN), vaya a Administración --> Configuración -->
global --> url_base. Ingrese la nueva URL en el campo de la derecha y luego haga clic en la marca de verificación para guardar la nueva configuración.
- 291/402 - Soluciones de cebolla de seguridad, LLC

18. Trucos y consejos
18. Trucos y consejos
18.1 Descripción general de trucos y consejos
Esta sección es una colección de trucos y consejos diversos para Security Onion.
- 292/402 - Soluciones de cebolla de seguridad, LLC

18.2 Copia de seguridad
18.2 Copia de seguridad
Security Onion realiza una copia de seguridad diaria de algunos archivos críticos para que puedas recuperar tu grid de una falla catastrófica del administrador.
Las copias de seguridad diarias crean un archivo tar ubicado en el directorio /nsm/backup/ ubicado en el administrador. Es posible que desee replicar este directorio de respaldo
a una ubicación fuera de su administrador en caso de que alguna vez sea necesario reconstruir el administrador.
Esto es lo que se respalda automáticamente de forma predeterminada:
• /etc/pki/: todos los certificados, incluida la CA.
• /etc/salt/: configuración para el administrador de Salt y los minions.
• /nsm/kratos/ - Configuración para Kratos.
• /nsm/hydra/: configuración para Hydra (utilizada para el acceso a la API de Security Onion).
• /opt/so/saltstack/local/: personalizaciones realizadas a través de Administración --> Configuración.
Si necesita restaurar uno o más archivos desde la copia de seguridad, ubique el archivo de copia de seguridad tar de la fecha deseada y use el comando tar estándar para
expandir el archivo. Por ejemplo, para expandir el archivo de respaldo del 17 de marzo de 2025:
tar xvf so-config-backup-2025_03_17.tar
Esto extraerá los archivos de configuración del archivo tar a los subdirectorios para etc, nsm y opt. Luego puede copiar los archivos necesarios de esos
subdirectorios expandidos a los directorios reales.
18.2.1 Configuración
Puede configurar las copias de seguridad yendo a Administración --> Configuración --> copia de seguridad.
18.2.2 Búsqueda elástica
Los datos de Elasticsearch no se respaldan automáticamente. Esto incluye cosas que pueden ser importantes para usted, como personalizaciones y casos de Kibana.
datos. Las personalizaciones de Kibana se encuentran en los índices .Kibana y los datos de Casos se almacenan en los índices so-case y so-casehistory. si
- 293/402 - Soluciones de cebolla de seguridad, LLC

18.2.3 PostgreSQL
Si tiene una implementación distribuida con agrupación en clústeres de Elasticsearch, puede habilitar las réplicas para que tengan redundancia en el caso de un solo nodo.
fracaso. Por supuesto, tenga en cuenta que habilitar réplicas duplica sus necesidades de almacenamiento.
Otra opción es utilizar el soporte integrado de Elasticsearch para instantáneas: https://www.elastic.co/guide/en/elasticsearch/reference/current/
instantánea-restaurar.html
Esta opción requiere que configure Elasticsearch con una configuración de path.repo donde pueda almacenar las instantáneas. Una vez que Elasticsearch tenga la
configuración path.repo, debería poder iniciar sesión en Kibana y configurar instantáneas como se muestra en el enlace anterior. Esas instantáneas serán luego
accesible en /nsm/elasticsearch/repo/.
18.2.3 PostgreSQL
Se realiza una copia de seguridad automática de PostgreSQL diariamente a las 00:05. La copia de seguridad utiliza pg_dumpall para capturar todas las bases de datos y roles, comprimidos con
zip. Los archivos de respaldo se almacenan en /nsm/backup/so-postgres-backup-YYYY_MM_DD.sql.gz con retención de 7 días y modo 0600.
Para restaurar desde una copia de seguridad:
zcat /nsm/backup/so-postgres-backup-2026_04_21.sql.gz | docker exec -i so-postgres psql -U postgres
- 294/402 - Soluciones de cebolla de seguridad, LLC

18.3 Ventana acoplable
18.3 Ventana acoplable
De https://www.docker.com/what-docker:
Docker es la plataforma de contenedores de software líder en el mundo. Los desarrolladores utilizan Docker para eliminar los problemas de "funciona en mi máquina" cuando
colaborar en código con compañeros de trabajo. Los operadores usan Docker para ejecutar y administrar aplicaciones en paralelo en contenedores aislados para mejorar
densidad de cálculo. Las empresas utilizan Docker para crear canales de entrega de software ágiles para ofrecer nuevas funciones de forma más rápida, segura y con
Confianza para aplicaciones Linux, Windows Server y Linux en mainframe.
18.3.1 Descargar
Nuestra imagen ISO incluye el motor Docker y todas nuestras imágenes Docker.
18.3.2 Seguridad
Para evitar manipulaciones, nuestras imágenes de Docker están firmadas mediante claves GPG. Soup verifica las firmas GPG cada vez que se actualizan las imágenes de Docker.
18.3.3 Elástico
Para mantener un alto nivel de estabilidad, confiabilidad y soporte, nuestras imágenes de Elastic Docker se basan en las imágenes de Docker proporcionadas por Elastic.co.
18.3.4 Imágenes
Después de la instalación, podrá ver todas las imágenes de Docker con el siguiente comando:
Imágenes de sudo-docker
18.3.5 Registros
Si un servicio no escribe sus registros en /opt/so/log, es posible que deba consultar los registros de Docker para obtener más detalles. Por ejemplo, para comprobar el
Registros de Docker para Kibana:
sudo docker registra so-kibana
18.3.6 Registro
El nodo administrador ejecuta un registro de Docker. De https://docs.docker.com/registry/recipes/mirror/:
Si tiene varias instancias de Docker ejecutándose en su entorno (por ejemplo, varias máquinas físicas o virtuales, todas ejecutando el demonio Docker),
cada vez que uno de ellos requiera una imagen que no tiene, se conectará a Internet y la buscará en el registro público de Docker. corriendo
Si utiliza un espejo de registro local, puede mantener la mayor parte del tráfico redundante de recuperación de imágenes en su red local.
Si ve errores relacionados con so-dockerregistry (Registro Docker), eche un vistazo a las siguientes discusiones para ver si su
Los síntomas coinciden y si sus soluciones pueden ayudarle:
https://github.com/Security-Onion-Solutions/securityonion/discussions/12078
https://github.com/Security-Onion-Solutions/securityonion/discussions/12635
18.3.7 Redes y puentes
De forma predeterminada, Docker configura su puente de red con una dirección IP 172.17.0.1. Esto funciona bien para redes que aún no están usando el
Rango 172.17.0.0/16. Si está utilizando este rango en su red, puede cambiar el rango de Docker durante la instalación.
- 295/402 - Soluciones de cebolla de seguridad, LLC

18.3.8 Contenedores
18.3.8 Contenedores
Todos nuestros contenedores Docker pertenecen a una red puente Docker común, llamada sobridge. Cada contenedor también tiene un alias, de modo que
La comunicación puede ocurrir entre los diferentes contenedores acoplables usando dicho alias. Por ejemplo, la comunicación a la búsqueda tan elástica.
El contenedor se produciría a través de un alias de Elasticsearch.
Es posible que encuentres interfaces en ifconfig con el formato veth*. Estas son las interfaces externas para cada uno de los contenedores Docker.
Estas interfaces corresponden a interfaces internas del contenedor Docker (dentro del propio contenedor Docker).
Para identificar qué interfaz externa pertenece a qué contenedor, podemos hacer algo como lo siguiente:
Desde el host, escriba:
sudo docker exec so-elasticsearch cat /sys/class/net/eth0/iflink
Esto debería proporcionarle un valor con el que pueda grep la clase de red del host ifindex(es):
Ejemplo:
grep 25 /sys/class/net/veth*/ifindex | cortar -d'/' -f5
Luego debería recibir un resultado similar al siguiente:
vethc5ff027
donde vethc5ff027 es la interfaz externa de eth0 dentro del contenedor so-elasticsearch.
18.3.9 Herramientas de VMware
Si tiene VMware Tools instalado y suspende y luego reanuda, las interfaces Docker ya no tendrán direcciones IP y Elastic
La pila ya no podrá comunicarse. Una solución es eliminar /etc/vmware-tools/scripts/vmware/network para evitar
VMware suspende/reanuda la modificación de la configuración de su red.
- 296/402 - Soluciones de cebolla de seguridad, LLC

18.3.10 Más información
18.3.10 Más información
Nota
Para obtener más información sobre Docker, consulte https://www.docker.com/what-docker.
- 297/402 - Soluciones de cebolla de seguridad, LLC

Cuaderno Jupyter 18.4
Cuaderno Jupyter 18.4
18.4.1 Descripción general
Esta sección es una breve descripción general de cómo conectar una instancia de notebook/servidor de Jupyter a Elasticsearch para dividir y desmenuzar los datos como desee. eso
no cubrirá la configuración de una instancia de Jupyter, que se ha documentado exhaustivamente (usando Docker) en https://jupyter-docker-
stacks.readthedocs.io/en/latest/index.html.
18.4.2 Configuración de cebolla de seguridad
Crear usuario de Jupyter
Como práctica recomendada, querrá crear un usuario de notebook Jupyter dedicado con acceso de solo lectura a los datos dentro de Elasticsearch. en
Kibana, navegue hasta Administración de pila -> Usuarios y cree el usuario con los permisos adecuados.
Cortafuegos de seguridad tipo cebolla
Para permitir el acceso basado en red a Elasticsearch, deberá permitir el tráfico a través del firewall basado en host yendo a
Administración --> Configuración --> firewall --> grupos de hosts.
En la parte superior de la página, haga clic en el menú Opciones y habilite la opción Mostrar configuración avanzada. En el lado izquierdo, seleccione el
Opción elasticsearch_rest. En el lado derecho, agregue su dirección IP o bloques CIDR y haga clic en la marca de verificación para guardar.
Una vez completado, debería poder conectarse a la instancia de Elasticsearch. Puede confirmar la conectividad utilizando herramientas como curl o Powershell
Prueba-NetConnection.
- 298/402 - Soluciones de cebolla de seguridad, LLC

18.4.3 Cuaderno Jupyter
18.4.3 Cuaderno Jupyter
Nota
Los siguientes pasos están fuertemente inspirados en la publicación de Roberto Rodríguez en Medium:
https://medium.com/threat-hunters-forge/jupyter-notebooks-from-sigma-rules-%EF%B8%8F-to-query-Elasticsearch-31a74cc59b99
El entorno Jupyter deberá tener instaladas al menos las siguientes bibliotecas de Python:
• Búsqueda elástica
• elasticsearch_dsl
• pandas
Puede instalarlos usando los siguientes comandos en el host de Jupyter o dentro del contenedor Docker de Jupyter:
instalación de pip3 Elasticsearch
pip3 instalar elasticsearch_dsl
pip3 instalar pandas
Una vez instalados los requisitos previos de Python, podemos comenzar a ejecutar comandos dentro de nuestro cuaderno.
Comenzaremos importando las bibliotecas que acabamos de mencionar. En la primera celda, pegaremos lo siguiente:
desde Elasticsearch importar Elasticsearch
desde elasticsearch_dsl importar búsqueda
importar pandas como pd
Luego, presionaremos Shift+ENTER para ejecutar los comandos dentro de la celda (también podemos hacer clic para ejecutar la celda desde el menú Ejecutar).
En la siguiente celda, especificaremos la dirección y el puerto de la instancia de Elasticsearch (192.168.6.100:9200) y el nombre de usuario (jupyter) y la contraseña.
(contraseña) que creamos dentro de Security Onion, así como el filtro de índice que nos gustaría usar para la búsqueda (*:so-*):
es = Elasticsearch(['https://192.168.6.100:9200'],
ca_certs=False,verify_certs=False, http_auth=('jupyter','contraseña'))
searchContext = Buscar(usando=es, index='*:so-*', doc_type='doc')
Nota
Elegimos utilizar verificar_certs=False aquí para evitar complicaciones con los certificados autofirmados durante las pruebas. Lo ideal sería que quisiéramos
asegúrese de que estemos realizando la verificación siempre que sea posible.
Nuevamente, ejecutaremos el código dentro de la celda, presionando Shift+ENTER.
Es posible que veamos una advertencia de certificado debido a que no estamos realizando la verificación de los certificados.
Para mayor comodidad durante nuestras pruebas, podemos desactivar la advertencia en ejecuciones futuras, pegando lo siguiente en la siguiente celda y ejecutándolo con
Mayús+ENTRAR:
importar urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
En la siguiente celda, pegaremos lo siguiente:
s = searchContext.query('query_string', consulta='event.module:sysmon')
En este ejemplo, buscamos registros que contengan un campo llamado event.module y un valor de sysmon (registros de Sysmon). Una vez más, lo haremos
presione Shift+ENTER y continúe.
- 299/402 - Soluciones de cebolla de seguridad, LLC

18.4.3 Cuaderno Jupyter
Finalmente, enviaremos nuestra consulta en la siguiente celda usando lo siguiente:
respuesta = s.ejecutar()
si respuesta.éxito():
df = pd.DataFrame((d.to_dict() para d en s.scan()))
df
El código anterior simplemente toma los resultados y los convierte en un dictado de Python.
Podemos seleccionar algunos campos y modificar los valores de las columnas si lo deseamos:
respuesta = s.ejecutar()
si respuesta.éxito():
df = pd.DataFrame(([d['evento']['conjunto de datos'], d['proceso']['ejecutable'], d['archivo']['objetivo']] para d en s))
df.columns=['Conjunto de datos','Ejecutable', 'Destino']
df
Luego terminamos con algo un poco más específico (es posible que necesites ajustar pd.options.display.max_colwidth para que se muestre
apropiadamente).
Obviamente, podemos hacer mucho más con estos datos además de simplemente ejecutar el código de ejemplo anterior. ¡Feliz caza!
- 300/402 - Soluciones de cebolla de seguridad, LLC

18.5 Agregar espacio en disco
18.5 Agregar espacio en disco
Si alguna vez necesita agregar espacio en disco para expandir sus particiones, existen diferentes formas de hacerlo.
Advertencia
Antes de hacer esto en producción, asegúrese de practicarlo en un sistema que no sea de producción.
18.5.1 Método recomendado: LVM (gestión de volumen lógico)
Si su disco está particionado usando LVM (el valor predeterminado para nuestra imagen ISO de Security Onion), entonces debería poder usar LVM para agregar nuevo espacio en disco.
a sus particiones LVM.
Nota
Para obtener más información sobre LVM, consulte https://docs.oracle.com/en/operating-systems/oracle-linux/9/stordev/stordev-
WorkingWithLogicalVolumeManager.html#using-lvm.
Ejemplo de LVM
Para un ejemplo simple de LVM, supongamos que ha instalado nuestra imagen ISO de Security Onion en una máquina virtual (VM) usando un sistema de virtualización.
solución como Proxmox que le permite aumentar el almacenamiento sobre la marcha. Nuestra imagen ISO de Security Onion usa automáticamente LVM y debería usar el
Sistema de archivos XFS para /nsm, por lo que si desea agregar espacio a /nsm, aquí hay una breve descripción general de los pasos que seguiría.
Primero, expanda el almacenamiento. Si usa Proxmox, seleccione la VM, seleccione Hardware, seleccione el Disco duro, haga clic en Acción del disco, haga clic en Cambiar tamaño, ingrese
la cantidad que desea agregar al tamaño del disco existente y luego haga clic en el botón Cambiar tamaño del disco.
Luego, inicie sesión en la VM, conviértase en root y use una herramienta de partición como cfdisk para cambiar el tamaño de la partición LVM y aprovechar las ventajas adicionales gratuitas.
espacio:
disco duro
Ahora que la partición LVM es más grande, necesitamos ampliar el volumen físico (PV) de LVM. Comience obteniendo una lista de todos los PV:
pantalla pv
Determine el PV que desea ampliar y luego use el comando pvresize (reemplazando /dev/sda3 con el PV deseado):
pvresize /dev/sda3
Verifique que el PV deseado se haya ampliado:
pantalla pv
Verifique que el grupo de volúmenes (VG) ahora muestre espacio libre:
pantallavg
Ahora que el VG tiene espacio libre, necesitamos ampliar el volumen lógico (LV). Comience obteniendo una lista de todos los LV:
pantalla lv
Determine el LV que desea ampliar y luego use el comando lvresize (reemplazando /dev/system/nsm con el LV deseado):
lvresize /dev/system/nsm -l +100%GRATIS
- 301/402 - Soluciones de cebolla de seguridad, LLC

18.5.2 Métodos no admitidos
Verifique que el VI deseado se haya ampliado:
pantalla lv
Ahora que el LV es más grande, necesitamos ampliar el sistema de archivos. Comience obteniendo una lista de todos los sistemas de archivos:
df-th
Determine el sistema de archivos que desea ampliar y luego use el comando apropiado (reemplazando xfs_growfs con la herramienta adecuada basada en
el tipo de sistema de archivos y reemplazando /dev/mapper/system-nsm con el sistema de archivos apropiado):
xfs_growfs /dev/mapper/system-nsm
Finalmente, verifique que el sistema de archivos se haya ampliado:
df-th
18.5.2 Métodos no admitidos
Advertencia
Existen otros métodos para expandir sus particiones, pero NO SON COMPATIBLES. Sólo deberías probar estos métodos si realmente sabes
lo que estás haciendo.
Si no está utilizando LVM pero necesita expandir su partición /nsm, puede montar una unidad física separada directamente en /nsm. si haciendo
Esto, después de la instalación, deberá detener los servicios, mover los datos a la nueva unidad y luego reiniciar los servicios.
Una variación de este método es hacer de /nsm un enlace simbólico a la nueva ubicación de registro. Ciertos servicios como AppArmor pueden necesitar servicios especiales.
configuración para manejar el enlace simbólico.
- 302/402 - Soluciones de cebolla de seguridad, LLC

18.6 Instalación de red
18.6 Instalación de red
Advertencia
Las instalaciones de red NO son compatibles y solo deben usarse como último recurso en caso de que haya algún motivo por el que no pueda usar nuestra seguridad oficial.
Imágenes de cebolla como se muestra en la sección Instalación.
Nuestras imágenes oficiales de Security Onion (imagen ISO e imágenes en la nube) son el ÚNICO método de instalación admitido y debe utilizarlas, si corresponde.
de lo siguiente se aplica a usted:
• Está implementando en un entorno empresarial.
• Está implementando en un entorno con espacio de aire.
• Está realizando una implementación distribuida.
• Quiere la instalación más rápida y sencilla con el menor número de problemas.
• Necesita algún tipo de apoyo.
Si NINGUNO de los anteriores se aplica a usted, entonces PUEDE poder instalar Oracle Linux 9 y luego realizar una instalación de red.
18.6.1 Partición
Nuestras imágenes oficiales de Security Onion se encargan de realizar la partición por usted. Sin embargo, si elige realizar una instalación de red, entonces es su
Es responsabilidad de asegurarse de que las particiones estén configuradas correctamente para evitar llenar una partición.
Almacenamiento mínimo
Como menciona la sección Hardware, el requisito MÍNIMO es 200 GB de almacenamiento. Esto es para permitir 100 GB para /nsm y 100 GB para el resto de
/.
LVM
Es posible que desee considerar la administración de volúmenes lógicos (LVM), ya que le permitirá cambiar más fácilmente su partición en el futuro si
necesito.
/arranque
Probablemente desee una partición /boot dedicada de al menos 1 GB al comienzo de la unidad.
/nsm
La gran mayoría de los datos se escribirán en /nsm, por lo que querrás dedicar la gran mayoría de tu espacio en disco a esa partición. Querrás en
menos 100 GB.
/
/ (la partición raíz) actualmente contiene /var/lib/docker/ (más sobre eso a continuación) y, por lo tanto, querrás al menos 100 GB.
acoplador
Las imágenes de Docker se almacenan en /var/lib/docker/. El conjunto actual de imágenes de Docker utiliza 30 GB en disco. Si estás planeando una producción
implementación, debe planear tener suficiente espacio para otro conjunto de esas imágenes de Docker para actualizaciones locales.
- 303/402 - Soluciones de cebolla de seguridad, LLC

18.6.2 Instalación a través de la red
Otro
El instalador del sistema operativo puede intentar dedicar una gran cantidad de espacio a /home. Es posible que deba ajustarlo para asegurarse de que no sea demasiado grande y
desperdiciar valioso espacio en disco.
Ejemplo
A continuación se muestra un ejemplo de cómo nuestra imagen ISO actual particiona un disco de 1 TB:
• 1 GB/partición de arranque al principio de la unidad
• el resto de la unidad es un volumen LVM que luego se particiona de la siguiente manera:
• 630 GB/nsm
• 300GB /
• 2 GB/tmp
• Intercambio de 8 GB
18.6.2 Instalación a través de la red
Advertencia
Tenga en cuenta que las instalaciones de red NO son compatibles y solo deben usarse como último recurso.
Si comprende todas las advertencias anteriores y aún desea realizar una instalación de red, puede seguir los pasos a continuación.
• Revise las secciones Hardware y Notas de la versión.
• Descargue la imagen ISO para el sistema operativo x86-64 que desee. Verifique la imagen ISO y luego inicie desde ella.
• Siga las indicaciones del instalador. Si está creando una implementación de producción, probablemente querrá usar LVM y dedicar la mayor parte de su
espacio en disco a /nsm como se explicó en la sección Particionamiento anterior.
• Reinicie en su nueva instalación.
• Inicie sesión con el nombre de usuario y la contraseña que especificó durante la instalación.
• Instalar requisitos previos:
sudo dnf -y instalar git
• Descargue nuestro repositorio e inicie el proceso de configuración:
git clone -b 3/main https://github.com/Security-Onion-Solutions/securityonion
cd seguridadcebolla
sudo bash so-setup-network
• Proceda a la sección Configuración.
- 304/402 - Soluciones de cebolla de seguridad, LLC

18.7 PCAP para pruebas
18.7 PCAP para pruebas
La forma más sencilla de descargar archivos PCAP para realizar pruebas es nuestra herramienta so-test. Alternativamente, puede descargar pcaps manualmente desde uno o más de
las siguientes ubicaciones:
• https://www.malware-traffic-analysis.net/
• https://digitalcorpora.org/corpora/network-packet-dumps
• https://www.netresec.com/?page=PcapFiles
• https://www.netresec.com/?page=MACCDC
• https://github.com/zeek/zeek/tree/master/testing/btest/Traces
• https://www.ll.mit.edu/r-d/datasets/2000-darpa-intrusion-detection-scenario-specific-datasets
• https://wiki.wireshark.org/SampleCaptures
• https://www.stratosphereips.org/datasets-overview
• https://ee.lbl.gov/anonymized-traces.html
• https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Public_Data_Sets
• https://forensicscontest.com/puzzles
• https://github.com/markofu/hackeire/tree/master/2011/pcap
• https://www.defcon.org/html/links/dc-ctf.html
• https://github.com/chrissanders/packets
Puede descargar archivos PCAP desde los enlaces anteriores utilizando un navegador web estándar o desde la línea de comandos utilizando una herramienta como wget o curl.
18.7.1 Repetición
Puede usar tcpreplay para reproducir cualquier PCAP estándar en la interfaz de rastreo de su sensor Security Onion.
18.7.2 Importar
Una desventaja de usar tcpreplay es que reproduce el PCAP como tráfico nuevo y, por lo tanto, las marcas de tiempo que se ven en SOC y otras interfaces.
no reflejan las marcas de tiempo originales del PCAP. Para evitar esto, puede importar el PCAP usando la página Grid.
- 305/402 - Soluciones de cebolla de seguridad, LLC

18.8 Ajuste de alto rendimiento
18.8 Ajuste de alto rendimiento
18.8.1 Afinidad/fijación de CPU
Para obtener el mejor rendimiento, los procesos con uso intensivo de CPU, como Zeek y Suricata, deben anclarse a CPU específicas. En la mayoría de los casos, querrás fijar
procesos de rastreo a la misma CPU a la que está vinculada su NIC de rastreo. Para obtener más información, consulte la subsección Rendimiento en la
secciones apropiadas de Suricata y Zeek.
18.8.2 Varios
Considere adoptar algunas de las sugerencias de aquí:
• https://suricata.readthedocs.io/en/latest/performance/packet-capture.html
• https://github.com/pevma/SEPTun
• https://github.com/pevma/SEPTun-Mark-II
18.8.3 Disco/Memoria
Si tiene suficiente RAM, desactive el intercambio por completo:
https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-configuration-memory.html#disable-swap-files
Utilice hdparm para recopilar estadísticas de la unidad y modificar la configuración, como se describe aquí:
https://www.linux-magazine.com/Online/Features/Tune-Your-Hard-Disk-with-hdparm
vm.dirty_ratio es la cantidad máxima de memoria del sistema que se puede llenar con páginas sucias antes de que todo se deba confirmar.
disco.
vm.dirty_background_ratio es el porcentaje de memoria del sistema que se puede llenar con páginas "sucias" o páginas de memoria que aún deben llenarse.
escrito en el disco, antes de que los procesos en segundo plano de pdflush/flush/kdmflush se activen para escribirlo en el disco.
Más información:
https://lonesysadmin.net/2013/12/22/better-linux-disk-caching-performance-vm-dirty_ratio/
18.8.4 Elástico
Querrá asegurarse de que cada parte de la tubería esté funcionando con la máxima eficiencia. Dependiendo de su configuración, esto puede
incluyen Elastic Agent, Logstash, Redis y Elasticsearch.
- 306/402 - Soluciones de cebolla de seguridad, LLC

18.9 Eliminación de un nodo
18.9 Eliminación de un nodo
Puede llegar un momento en el que necesite eliminar un nodo de su implementación distribuida. Para hacer esto, necesitarás quitar el nodo.
configuración a partir de algunos componentes diferentes.
18.9.1 Eliminación de un nodo de búsqueda
Para eliminar un nodo de búsqueda, los datos almacenados en el nodo deben migrarse antes de realizar otras acciones de eliminación del nodo.
Utilice el siguiente comando en Kibana Dev Tools para detener la asignación de fragmentos al nodo (reemplazando 10.0.0.1 con la dirección IP real del nodo).
nodo de búsqueda que se eliminará):
PUT _clúster/configuración
{
"persistente": {
"cluster.routing.allocation.exclude._ip": "10.0.0.1"
}
}
Para obtener más información sobre este comando, consulte https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-
cluster.html#filtrado-de-asignación-de-fragmentos-cluster.
Una vez que todos los datos hayan migrado fuera del nodo de búsqueda, podrá continuar con otras acciones de eliminación del nodo.
18.9.2 Quitar de la sal
Puede eliminar un nodo de Salt yendo a Administración --> Miembros de Grid.
Busque el miembro de la cuadrícula que desea eliminar, haga clic en el botón REVISAR y luego haga clic en el botón ELIMINAR.
- 307/402 - Soluciones de cebolla de seguridad, LLC

18.9.3 Eliminación del SOC
18.9.3 Eliminación del SOC
Para eliminar el nodo de la página SOC Grid, asegúrese de que el nodo esté apagado y luego reinicie SOC:
sudo so-soc-reiniciar
18.9.4 Eliminación de la flota
Para eliminar el nodo de Elastic Fleet, vaya a la pestaña Agentes y busque el nodo. Luego haga clic en la casilla de verificación a la izquierda del nodo. Haga clic en
Botón Acciones y luego haga clic en Cancelar inscripción de 1 agente. Seleccione la opción Eliminar agente inmediatamente y luego haga clic en Cancelar inscripción del agente.
botón.
- 308/402 - Soluciones de cebolla de seguridad, LLC

18.10 Sal
18.10 Sal
De https://docs.saltproject.io/en/latest/topics/about_salt_project.html#about-salt:
Salt, construido sobre Python, es un marco y una herramienta de automatización basada en eventos para implementar, configurar y administrar sistemas de TI complejos. Usa sal para
automatice las tareas comunes de administración de infraestructura y garantice que todos los componentes de su infraestructura estén funcionando de manera ordenada.
estado deseado consistente.
Nota
Salt es un componente central de Security Onion, ya que gestiona todos los procesos en todos los nodos. En una implementación distribuida, el nodo administrador controla todos
otros nodos a través de la sal. Estos nodos que no son administradores se conocen como minions de sal.
18.10.1 Requisitos del cortafuegos
Los minions de Salt deben poder conectarse al nodo administrador en los puertos 4505/tcp y 4506/tcp.
18.10.2 Comprobación del estado
Puede usar test.ping de salt para verificar que todos sus nodos estén activos:
sudo sal \* prueba.ping
18.10.3 Ejecución remota
De manera similar, puede usar cmd.run de salt para ejecutar un comando en todos sus nodos a la vez. Por ejemplo, para comprobar el espacio en disco en todos los nodos:
sudo sal \* cmd.run 'df'
18.10.4 Registro de nodo
Si desea forzar a un nodo a realizar una actualización completa de todos los estados de sal, puede ejecutar so-checkin. Esto ejecutará salt-call state.highstate -l
info que sale al terminal con el nivel de registro configurado en info para que puedas ver exactamente lo que está sucediendo:
sudo so-checkin
18.10.5 Configuración
Muchas de las opciones que se pueden configurar en Security Onion se realizan yendo a Administración y luego a Configuración.
18.10.6 Registros de diagnóstico
Los registros de diagnóstico se pueden encontrar en /opt/so/log/salt/.
18.10.7 Problemas conocidos
Es posible que vea el siguiente error en el registro de salt-master ubicado en /opt/so/log/salt/master:
[ERROR] [24983] Error en la iteración del evento con excepción: el objeto 'lista' no tiene el atributo 'elementos'
La causa principal de este error es un estado que intenta ejecutarse en un minion cuando ya se está ejecutando otro estado. Este error ahora ocurre en el registro debido a un
cambio en el manejo de excepciones dentro del módulo de eventos de Salt. Anteriormente, en el caso de una excepción, el código simplemente pasaba. Sin embargo, el
La excepción ahora está registrada. El error se puede ignorar ya que no es una indicación de ningún problema con los minions.
- 309/402 - Soluciones de cebolla de seguridad, LLC

18.10.8 Más información
18.10.8 Más información
Nota
Para obtener más información sobre Salt, consulte https://docs.saltproject.io/en/latest/contents.html.
- 310/402 - Soluciones de cebolla de seguridad, LLC

18.11 Salida de Syslog
18.11 Salida de Syslog
Si desea enviar registros a un sistema externo, puede configurar Logstash para enviarlos a syslog.
Nota
Para obtener más información sobre el complemento de salida syslog de Logstash, consulte: https://www.elastic.co/guide/en/logstash/current/plugins-outputs-
syslog.html
Tenga en cuenta que no brindamos soporte gratuito para sistemas de terceros.
- 311/402 - Soluciones de cebolla de seguridad, LLC

18.12 Zonas horarias
18.12 Zonas horarias
Cuando ejecuta Security Onion Setup, establece la zona horaria del sistema operativo en UTC/GMT. Iniciar sesión en UTC se considera una de las mejores prácticas en todo
la industria de la ciberseguridad porque hace que sea mucho más fácil correlacionar eventos entre diferentes sistemas, organizaciones o zonas horarias.
Además, evita problemas con las zonas horarias que tienen horario de verano, lo que daría lugar a un retraso de una hora dos veces al año.
Las interfaces web como Alertas, Paneles, Hunt y Kibana deberían intentar detectar la zona horaria de su navegador web y luego mostrar esas UTC.
marcas de tiempo en hora local. Alertas, Paneles y Búsqueda le permiten configurar manualmente su zona horaria en Opciones.
Para obtener más información sobre la hora del sistema operativo, consulte la sección NTP.
- 312/402 - Soluciones de cebolla de seguridad, LLC

19. Utilidades
19. Utilidades
19.1 Descripción general de las utilidades
Esta sección cubre algunas de las utilidades de Security Onion.
- 313/402 - Soluciones de cebolla de seguridad, LLC

19,2 jq
19,2 jq
De https://stedolan.github.io/jq/:
jq es como sed para datos JSON: puede usarlo para dividir, filtrar, mapear y transformar datos estructurados con la misma facilidad que sed, awk,
grep y amigos te permiten jugar con texto.
19.2.1 Uso
Configuramos Zeek y Suricata para escribir registros en /nsm/ en formato JSON. Si desea analizar esos registros desde la línea de comando, puede
utilizar jq. Aquí hay un ejemplo básico:
jq'.' /nsm/zeek/logs/current/conn.log
Este comando analizará todos los registros en /nsm/zeek/logs/current/conn.log. Para cada uno de los registros, generará cada campo y
su valor.
19.2.2 Más información
Nota
Para obtener más información sobre jq, consulte https://stedolan.github.io/jq/.
- 314/402 - Soluciones de cebolla de seguridad, LLC

19.3 así permitir
19.3 así permitir
En versiones anteriores de Security Onion, se usaba so-allow para permitir el tráfico a través del firewall basado en host. Esto ahora se hace yendo a
Administración --> Configuración --> firewall --> grupos de hosts.
- 315/402 - Soluciones de cebolla de seguridad, LLC

19.4 restablecimiento-de-contraseña-de-autenticación-so-elastic
19.4 restablecimiento-de-contraseña-de-autenticación-so-elastic
Las cuentas de servicio elástico utilizan contraseñas generadas aleatoriamente que tienen 72 caracteres de longitud. Si necesita restablecer estas contraseñas, puede
utilice la utilidad so-elastic-auth-password-reset.
- 316/402 - Soluciones de cebolla de seguridad, LLC

19.5 consulta de búsqueda tan elástica
19.5 consulta de búsqueda tan elástica
Puede utilizar so-elasticsearch-query para enviar una solicitud cURL al host local de Security Onion Elasticsearch desde la línea de comando.
19.5.1 Uso
consulta de búsqueda tan elástica <RUTA> [ARGS,...]
donde:
• PATH representa la función elástica que se solicita.
• ARGS se utiliza para especificar parámetros de curvatura opcionales adicionales.
19.5.2 Ejemplos
Aquí hay un ejemplo básico:
sudo so-elasticsearch-query /
Aquí hay un ejemplo más complicado que incluye canalizar la salida a jq:
sudo so-elasticsearch-query '*:so-*/_search' -d '{"query": {"match_all": {}},"size": 1}' | jq
- 317/402 - Soluciones de cebolla de seguridad, LLC

19.6 so-importar-pcap
19.6 so-importar-pcap
so-import-pcap importará uno o más archivos pcap a Security Onion y conservará las marcas de tiempo originales. Hará lo siguiente:
• generar alertas IDS utilizando Suricata
• generar metadatos de red usando Zeek
• almacenar alertas de IDS y metadatos de red en Elasticsearch con marcas de tiempo originales
• almacenar archivos pcap donde SOC pueda encontrarlos
• proporcionar un hipervínculo para que pueda ver todas las alertas y registros en SOC
consejo
Puede ejecutar este comando manualmente, pero para la mayoría de los casos de uso es más fácil cargar un archivo pcap a través de Grid y se ejecutará automáticamente so-import-pcap.
para ti.
19.6.1 Configuración
so-import-pcap requiere que ejecute la instalación y elija una configuración que admita so-import-pcap. Esto incluye Importar nodo y
otros nodos que incluyen servicios de sensores como Eval y Standalone. La opción más rápida y sencilla es elegir Importar nodo, que le ofrece
los servicios mínimos necesarios para importar un archivo pcap.
Advertencia
Tenga en cuenta que so-import-pcap no es compatible con nodos pesados.
19.6.2 Uso
Una vez que se completa la instalación, puede ejecutar Sudo so-import-pcap y proporcionar la ruta completa a al menos un archivo pcap. Por ejemplo, para importar un
archivo pcap único llamado import.pcap:
sudo so-import-pcap /full/path/to/import.pcap
Para importar varios archivos pcap:
sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap
Tenga en cuenta que si importa varios archivos pcap a la vez, so-import-pcap actualmente solo proporciona un hipervínculo para el último archivo pcap en el
lista. Si necesita un hipervínculo para cada archivo pcap, puede ejecutar un archivo pcap por so-import-pcap y usar un bucle for para iterar sobre su
colección de archivos pcap.
so-import-pcap calcula el hash MD5 del archivo pcap importado y crea un directorio en /nsm/import/ para ese hash. Aquí es donde tan-
import-pcap almacena las alertas y registros generados por el tráfico en el archivo pcap. Si intenta importar el mismo archivo pcap nuevamente, le dirá que
ya ha importado ese archivo pcap. Si por alguna razón realmente necesita importar ese archivo pcap nuevamente, puede eliminar ese archivo pcap.
directorio en /nsm/import/ y luego vuelva a intentarlo.
19.6.3 Ejemplos
Si aún no tiene algunos archivos pcap para importar, consulte PCAP para obtener una lista de sitios donde puede descargar archivos pcap de muestra.
Nuestra serie de Análisis rápido de malware en https://blog.securityonion.net/search/label/quick%20malware%20analysis utiliza so-import-pcap para
importe archivos pcap desde https://www.malware-traffic-analysis.net/ y otros sitios. Siguiendo estas publicaciones de blog en su propio modo-
import-pcap VM es una excelente manera de practicar tus habilidades.
- 318/402 - Soluciones de cebolla de seguridad, LLC

19.7 so-importar-evtx
19.7 so-importar-evtx
so-import-evtx importará uno o más archivos evtx a Security Onion.
consejo
Puede ejecutar este comando manualmente, pero para la mayoría de los casos de uso es más fácil cargar un archivo evtx a través de Grid y se ejecutará automáticamente.
so-import-evtx para usted.
19.7.1 Uso
Ejecute sudo so-import-evtx y proporcione la ruta completa a al menos un archivo evtx. Por ejemplo, para importar un único archivo evtx denominado import.evtx:
sudo so-import-evtx /full/path/to/import.evtx
Para importar varios archivos evtx:
sudo so-import-evtx /full/path/to/import2.evtx /full/path/to/import2.evtx
so-import-evtx luego proporciona un hipervínculo para que pueda ver todos los registros en SOC.
- 319/402 - Soluciones de cebolla de seguridad, LLC

19.8 so-monitor-agregar
19.8 so-monitor-agregar
Si ya ejecutó la configuración pero luego descubre que necesita agregar una nueva interfaz de monitor (de rastreo), puede ejecutar so-monitor-add. esto
le permitirá agregar interfaces de red a bond0 para que su tráfico sea monitoreado.
Advertencia
Las imágenes de la nube detectan directamente desde las interfaces de red en lugar de utilizar bond0, por lo que esta utilidad no funcionará en esos entornos.
- 320/402 - Soluciones de cebolla de seguridad, LLC

19.9 estado-so
19.9 estado-so
Para verificar el estado de los servicios de Security Onion, puede ejecutar sudo so-status o simplemente ver el panel Estado en la página Grid.
so-status lee la lista de servicios habilitados de /opt/so/conf/so-status/so-status.conf y verifica el estado de cada uno. si alguna vez
deshabilita un servicio, es posible que deba eliminarlo de ese archivo.
19.9.1 Modo silencioso
so-status admite un modo silencioso:
entonces-estado -h
Uso: /usr/sbin/so-status [OPCIONES]
Opciones:
-h: imprime esta información de uso
-q - Suprime la salida; útil para la automatización del valor del código de salida
-j - Salida en formato JSON
-i: considere el resultado de la instalación independientemente de si el sistema parece saludable
Códigos de salida:
0 - Éxito, el sistema parece estar funcionando correctamente
1 - Error, uno o más subsistemas no se están ejecutando
2 - El sistema se está iniciando
99 - Instalación en curso
100 - La instalación del sistema encontró errores
sudo so-status -q
eco $?
0
- 321/402 - Soluciones de cebolla de seguridad, LLC

19.10 prueba así
19.10 prueba así
so-test ejecutará so-tcpreplay para reproducir algunas muestras de PCAP en su interfaz de rastreo.
Advertencia
Tenga en cuenta que esta acción podría activar alertas en otros sistemas de monitoreo empresarial, según su red y la configuración de su interfaz.
Advertencia
Necesitará tener acceso a Internet para poder descargar los ejemplos de PCAP. Además, si tiene una implementación distribuida, asegúrese de ejecutar lo siguiente:
tcpreplay en el administrador primero para descargar la imagen de Docker necesaria.
así que prueba
Funcionalidad de reproducción no habilitada; intentando habilitarlo ahora (puede requerir acceso a Internet)...
Extrayendo la imagen so-tcpreplay
==========================================================================
Iniciando tcpreplay...
Esto podría tardar un poco si se está ejecutando otro trabajo de Salt.
Ejecute este comando con --force para detener todos los trabajos de Salt antes de continuar.
==========================================================================
locales:
----------
ID: so-tcpreplay
Función: docker_container.running
Resultado: Verdadero
Comentario: Contenedor creado 'so-tcpreplay'
Iniciado: 15:55:48.390107
Duración: 1460,452 ms
Cambios:
----------
contenedor_id:
----------
añadido:
f035103cd8bf43134b56d4b19d77a0ae9e7c09fcb54ef6da67cf89bef5fc4019
estado:
----------
nuevo:
corriendo
viejo:
Ninguno
Resumen para locales
------------
Tuvo éxito: 1 (cambiado=1)
Fallido: 0
------------
Total de estados ejecutados: 1
Tiempo total de ejecución: 1.460 s
Reproducción de PCAP a 10 Mbps en la interfaz bond0...
Real: 111557 paquetes (12981286 bytes) enviados en 10,38 segundos
Clasificado: 1249997,6 Bps, 9,99 Mbps, 10742,07 pps
Flujos: 4102 flujos, 394,99 fps, 2074477 paquetes de flujo, 45106 sin flujo
Estadísticas para dispositivo de red: bond0
Paquetes exitosos: 55304
Paquetes fallidos: 444
Paquetes truncados: 0
Paquetes reintentados (ENOBUFS): 0
Paquetes reintentados (EAGAIN): 0
Reproducción completada. Normalmente se esperan las advertencias que se muestran arriba.
Una vez que esto se complete, puede ir a Alertas, Paneles y Búsqueda para revisar los datos.
- 322/402 - Soluciones de cebolla de seguridad, LLC

19.11 so-usuario
19.11 so-usuario
La gestión de usuarios de SOC normalmente debe realizarse a través de Administración, como se muestra en la sección Cuentas. Sin embargo, si por alguna razón no puedes
inicie sesión en SOC, puede usar so-user desde la línea de comando para administrar las cuentas de usuario de SOC.
el usuario tiene muchas operaciones diferentes. Puedes verlos todos ejecutando so-user sin opciones:
sudo so-usuario
19.11.1 Listado de usuarios de SOC
Para ver una lista de todos los usuarios de SOC, utilice la operación de lista:
sudo lista de usuarios
19.11.2 Cambiar la contraseña del usuario SOC
Si olvidó su contraseña, puede restablecerla usando la operación de contraseña:
sudo so-contraseña de usuario --correo electrónico usuariocebolla@ejemplo.com
Una vez que haya restablecido su contraseña, debería poder iniciar sesión en SOC y volver a administrar cuentas de usuario a través de Administración como se muestra en
la sección Cuentas.
- 323/402 - Soluciones de cebolla de seguridad, LLC

20. Ayuda
20. Ayuda
20.1 Descripción general de la ayuda
¿Tienes problemas? Pruebe las sugerencias a continuación.
• ¿Ha ejecutado sopa para asegurarse de tener la última versión?
• Consulte las preguntas frecuentes.
• Busque en el foro de soporte comunitario.
• Buscar en la documentación y foros de soporte de las herramientas contenidas en Security Onion.
• Verifique los archivos de registro en /opt/so/log/ u otras ubicaciones para detectar errores o posibles pistas:
• Configurar /root/sosetup.log
• Suricata /opt/so/log/suricata/suricata.log
• Zeek /nsm/zeek/logs/current/
• Elasticsearch /opt/so/log/elasticsearch/<nombre de host>.log
• Kibana /opt/so/log/kibana/kibana.log
• Logstash /opt/so/log/logstash/logstash.log
• ElastAlert /opt/so/log/elastalert/elastalert_stderr.log
• ¿Puede duplicar el problema en una instalación nueva de Security Onion?
• Verifique los Problemas conocidos para ver si se trata de un problema conocido en el que estamos trabajando.
• Si todo lo demás falla, no dude en solicitar ayuda.
- 324/402 - Seguridad Cebolla Soluciones, LLC

20.2 Preguntas frecuentes
20.2 Preguntas frecuentes
20.2.1 Tabla de contenidos
• Instalar / Actualizar / Actualizar
• Usuarios / Contraseñas
• Soporte / Ayuda
• Motores IDS
• Elementos internos de Security Onion
• Sintonización
• Problemas comunes
• Varios
20.2.2 Instalar/Actualizar/Actualizar
¿Por qué la imagen ISO no arranca en mi máquina?
Por favor consulte la sección de Ayuda.
¿Cuál es el procedimiento recomendado para instalar Security Onion?
Consulte la sección Instalación.
¿Cuál es el procedimiento recomendado para configurar Security Onion?
Consulte la sección Configuración.
¿Qué sucede si recibo un mensaje de error La IP que Linux enruta no es la dirección IP asignada a la interfaz de administración?
Consulte la advertencia sobre esto en la sección Configuración.
¿Qué idiomas son compatibles?
Solo admitimos el idioma inglés en este momento.
¿Cómo instalo las actualizaciones de Security Onion?
Consulte la sección de sopas.
¿Qué conectividad necesita Security Onion para mantenerse actualizado?
Consulte la sección Cortafuegos.
¿Qué debo hacer si estoy detrás de un proxy?
Consulte la sección Proxy.
¿Puedo ejecutar Security Onion en Raspberry Pi o alguna otra caja que no sea x86?
No, solo admitimos x86-64 (arquitecturas Intel/AMD estándar de 64 bits). Consulte la sección Hardware.
Volver al principio
- 325/402 - Soluciones de cebolla de seguridad, LLC

20.2.3 Usuarios / Contraseñas
20.2.3 Usuarios / Contraseñas
¿Cuál es la contraseña?
Consulte la sección Contraseñas.
¿Cómo agrego una nueva cuenta de usuario?
Consulte la sección Agregar cuentas.
Volver al principio
20.2.4 Soporte / Ayuda
¿A dónde envío preguntas/problemas/sugerencias?
Consulte la sección Soporte comunitario.
¿Hay soporte comercial disponible para Security Onion?
Sí, ofrecemos soporte comercial en https://securityonionsolutions.com.
Volver al principio
20.2.5 Motores IDS
¿Se puede ejecutar Security Onion en modo IPS?
No, Security Onion no admite el bloqueo de tráfico. La mayoría de las organizaciones tienen algún tipo de Firewall de Próxima Generación (NGFW) con IPS
características y ese es el lugar adecuado para que ocurra el bloqueo. Security Onion está diseñado para monitorear el tráfico que atraviesa su firewall.
Volver al principio
20.2.6 Elementos internos de Security Onion
¿Dónde puedo leer más sobre las herramientas contenidas en Security Onion?
Consulte la sección Lista de materiales del software.
¿Cuál es la estructura de directorios de/nsm?
Consulte la sección Directorio.
¿Por qué Security Onion utiliza UTC?
Consulte la sección Zonas horarias.
¿Por qué las marcas de tiempo en Kibana no están en UTC?
Consulte la sección Zonas horarias.
¿Por qué mi disco se está llenando?
En general, Security Onion intenta utilizar todo el espacio en disco que le proporcione. Dependiendo del tipo de instalación, se debe continuar
escribir datos en el disco hasta que el uso del disco alcance el 80-90%, momento en el cual debería comenzar a eliminar los datos antiguos. Elasticsearch utiliza la mayor parte del espacio en disco
o Captura de paquetes completos escritos en el disco a través de Suricata.
- 326/402 - Soluciones de cebolla de seguridad, LLC

20.2.7 Sintonización
¿Cómo se mantienen seguros mis datos?
Las conexiones de red estándar hacia o desde Security Onion están cifradas. Esto incluye SSH, HTTPS, consultas de red Elasticsearch y Salt.
tráfico de minions. Todo el tráfico del agente de punto final (Elastic Agent) está cifrado, excepto las actualizaciones binarias, que se entregan desde el Administrador a través de http.
Estos archivos de actualización están firmados criptográficamente por Elastic y se verifican antes de su uso. También existe la opción de extraer estas actualizaciones.
a través de https directamente desde Elastic. Las contraseñas de las cuentas de usuario de SOC se codifican a través de bcrypt en Kratos y puede leer más sobre esto en https://
github.com/ory/kratos.
Volver al principio
20.2.7 Sintonización
¿Cómo configuro el correo electrónico para alertas e informes?
Consulte la sección de correo electrónico.
¿Cómo configuro un BPF?
Consulte la sección BPF.
¿Cómo filtro el tráfico?
Consulte la sección BPF.
¿Cómo excluyo el tráfico?
Consulte la sección BPF.
¿Cuáles son las configuraciones predeterminadas del firewall y cómo las cambio?
Consulte la sección Cortafuegos.
¿Qué necesito modificar para tener los archivos de registro almacenados en un punto de montaje diferente?
Consulte la sección Nuevo disco.
Volver al principio
20.2.8 Problemas comunes
¿Por qué se pierden los contenedores?
Los contenedores Docker que dejan de ejecutarse debido a errores de salida u otros motivos se eliminarán automáticamente mediante la limpieza programada.
proceso.
La mayoría de los registros de contenedores se redirigen al directorio de registros de su aplicación, ubicado en /opt/so/log. En algunos casos, es posible que los registros no se escriban en
disco y, en su lugar, debe verse a través de los registros de Docker <nombre-contenedor> antes de limpiar el contenedor.
¿Por qué ElastAlert suele desaparecer en mi Grid?
ElastAlert 2 se cerrará si encuentra errores de sintaxis con las reglas o cuando Elasticsearch no esté en buen estado.
¿Por qué Elasticsearch pasa a un estado no saludable?
Elasticsearch dejará de funcionar por diversas razones, pero las razones más comunes son quedarse sin espacio en disco y tener índices.
con fragmentos no asignados.
- 327/402 - Soluciones de cebolla de seguridad, LLC

20.2.9 Varios
Volver al principio
20.2.9 Varios
¿Dónde puedo encontrar pcaps interesantes para reproducir?
Consulte la sección PCAP.
¿Por qué Security Onion se conecta a una dirección IP en Internet a través del puerto 123?
Consulte la sección NTP.
¿Debo hacer una copia de seguridad de mi caja Security Onion?
Security Onion realiza automáticamente una copia de seguridad de algunas configuraciones importantes como se describe en la sección Copia de seguridad. Sin embargo, no hay ningún sistema automatizado.
copia de seguridad de datos. La supervisión de la seguridad de la red en su conjunto se considera el "mejor esfuerzo". No es un recurso de "misión crítica" como un servidor de archivos o un sitio web.
servidor. Dado que estamos tratando con "grandes datos" (potencialmente terabytes de captura de paquetes completos) de naturaleza transitoria, hacer una copia de seguridad de los datos sería
prohibitivamente caro. La mayoría de las organizaciones no realizan copias de seguridad de los datos y, en cambio, simplemente reconstruyen las cajas cuando es necesario.
¿Qué pasó con Filebeat?
Filebeat ha sido reemplazado por Elastic Agent.
¿Qué pasó con Grafana?
Grafana ha sido reemplazada por Grid.
¿Qué pasó con el libro de jugadas?
Playbook ha sido reemplazado por Detecciones.
¿Qué pasó con Wazuh?
Wazuh ha sido reemplazado por Elastic Agent.
¿Qué pasó con la taquígrafa?
La taquígrafa ha sido reemplazada por la captura completa de paquetes de Suricata.
¿Cómo puedo agregar reglas locales?
Consulte la sección Detecciones.
¿Puedo conectar Security Onion a Active Directory u otro proveedor de OIDC?
Consulte la sección OIDC.
Volver al principio
- 328/402 - Soluciones de cebolla de seguridad, LLC

20.3 Estructura del directorio
20.3 Estructura del directorio
20.3.1 /opt/so/conf
Las aplicaciones leen su configuración desde /opt/so/conf/. Sin embargo, tenga en cuenta que la mayoría de los archivos de configuración se administran con Salt, por lo que si
Si modifica manualmente esos archivos de configuración, es posible que sus cambios se sobrescriban en la próxima actualización de Salt.
20.3.2 /opt/so/log
Los registros de depuración se almacenan en /opt/so/log/.
20.3.3 /opt/so/reglas
Las reglas de ElastAlert y Suricata se almacenan en /opt/so/rules/.
20.3.4 /opt/so/saltstack/local
Se pueden agregar configuraciones personalizadas de Salt a /opt/so/saltstack/local/.
20.3.5 /nsm
La gran mayoría de los datos se almacenan en /nsm/.
20.3.6 /nsm/zeek
Zeek escribe sus registros de protocolo en /nsm/zeek/.
20.3.7 /nsm/elasticsearch
Elasticsearch almacena sus datos en /nsm/elasticsearch/.
20.3.8 /nsm/suripcap
Suricata almacena la captura de paquetes completos en /nsm/suripcap/.
- 329/402 - Soluciones de cebolla de seguridad, LLC

20.4 Soporte comunitario
20.4 Soporte comunitario
20.4.1 Verificar la documentación primero
Primero, verifique si su pregunta ya ha sido respondida en las secciones de Ayuda o Preguntas frecuentes.
20.4.2 Directrices del foro
Antes de publicar, revise las pautas del foro en https://github.com/Security-Onion-Solutions/securityonion/discussions/1720.
20.4.3 Foro
Una vez que haya leído y comprendido todo lo anterior, puede publicar su pregunta en el foro de soporte de la comunidad en https://securityonion.net/
discutir.
- 330/402 - Soluciones de cebolla de seguridad, LLC

20.5 Soporte
20.5 Soporte
20.5.1 Soporte pagado
Si necesita soporte privado o prioritario, considere comprar dispositivos de hardware o soporte de Security Onion Solutions:
https://securityonionsolutions.com/support
consejo
¡Comprar en Security Onion Solutions ayuda a respaldar el desarrollo de Security Onion como una plataforma abierta y gratuita!
20.5.2 Soporte comunitario
Si necesita soporte gratuito, puede comunicarse con nuestro soporte comunitario.
- 331/402 - Soluciones de cebolla de seguridad, LLC

20.6 Se busca ayuda
20.6 Se busca ayuda
La gente pregunta con frecuencia cómo pueden contribuir a la comunidad de Security Onion. Estos son algunos de nuestros equipos comunitarios con los que puede ayudar.
20.6.1 Equipo de marketing
Necesitamos más personas que ayuden a correr la voz sobre Security Onion a través de blogs, tweets y otras redes sociales.
20.6.2 Equipo de soporte
Si desea ayudar a otros usuarios de Security Onion, únase al foro y comience a responder preguntas.
https://securityonion.net/discuss
20.6.3 Equipo de documentación
Si encuentra que alguna información en nuestra documentación es incorrecta o falta, no dude en enviar solicitudes de extracción a la rama 3/dev.
del repositorio de documentos en https://github.com/Security-Onion-Solutions/docs.
20.6.4 Desarrollo central
La mayor parte de nuestro código está en GitHub. ¡No dudes en enviar solicitudes de extracción!
https://github.com/Security-Onion-Solutions
- 332/402 - Soluciones de cebolla de seguridad, LLC

20.6.5 Gracias
20.6.5 Gracias
Las siguientes personas han hecho importantes contribuciones a Security Onion a lo largo de los años. ¡Gracias!
•Lawrence Abrams
• Jack Blanchard
• Kevin Rama
•Josh Brower
•Pete Di Giorgio
• Dennis Distler
•Jason Ertel
• Seth Hall
•Paul Halliday
•Joe Hargis
• Mark Hillick
• Wes Lambert
• Dustin Lee
• Josh Más
• Corey Ogburn
• Eric Ooi
•Josh Patterson
• Phil Plantamura
• Liam Randall
•Mike Reeves
• Jorge Reyes
• Scott Runnels
• Jon Schipp
• Brad Shoop
• Melaza Bryant
• William Wernert
• Mateo Wright
- 333/402 - Seguridad Cebolla Soluciones, LLC

21. Cebolla de seguridad Pro
21. Cebolla de seguridad Pro
21.1 Descripción general de Security Onion Pro
Nota
Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para obtener más información sobre la compra de Security Onion.
Licencia Pro para habilitar estas funciones.
- 334/402 - Seguridad Cebolla Soluciones, LLC

21.2 Conexión OpenID (OIDC)
21.2 Conexión OpenID (OIDC)
SOC admite la autenticación de inicio de sesión único (SSO) a través de OpenID Connect (OIDC) a uno de varios proveedores de identidad compatibles con OIDC. Para
Por ejemplo, los usuarios pueden iniciar sesión en Security Onion utilizando un usuario de Active Directory, un usuario de GitHub, una cuenta de Google, una cuenta Auth0, etc. Solo uno
El proveedor de OIDC puede estar activo a la vez.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
Advertencia
No se admiten integraciones LDAP y SAML.
Advertencia
Generalmente no se recomienda integrar Security Onion en la plataforma global de gestión de identidades de una organización. Si un atacante compromete
la plataforma de gestión de identidades, que suele ser un objetivo de alta prioridad, entonces el atacante podría utilizar credenciales SSO comprometidas para acceder
Security Onion y potencialmente socavar los beneficios proporcionados por Security Onion. Esta integración está disponible para aquellos que entienden
estos riesgos y contar con las mitigaciones adecuadas.
21.2.1 Configuración
La configuración de OIDC puede ser compleja y recomendamos aprovechar el equipo de soporte oficial de Security Onion. Tenga en cuenta que las compras de
una licencia de Security Onion incluye cierto nivel de soporte. Esto ayudará a evitar problemas que pueden consumir mucho tiempo al configurar OIDC.
El primer paso en la configuración de OIDC es determinar qué proveedor utilizará la red y recopilar las entradas de configuración necesarias.
para ese proveedor específico.
A continuación, en Security Onion Console, mientras está conectado como administrador, navegue hasta la pantalla Administración -> Configuración e ingrese oidc.
en el campo del filtro. Luego haga clic en el ícono Expandir todo.
Revise las siguientes instrucciones para el proveedor correspondiente.
MICROSOFT ENTRA ID (Azure Active Directory)
Localice la configuración del proveedor en la pantalla de configuración de SOC. Especifique el valor de Microsoft para esta configuración.
En una pestaña separada del navegador, inicie sesión en la cuenta de Microsoft Azure que planea usar para la integración. Navegue hasta el servicio Microsoft Entra ID
y busque el ID del inquilino, que se parecerá a un UUID similar a abcdef12-1234-abcd-5678-a1b2c3d4e5f6.
- 335/402 - Soluciones de cebolla de seguridad, LLC

21.2.1 Configuración
Ubique la configuración microsoft_tenant en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el valor UUID para esta configuración.
De nuevo en la pestaña Azure, en el inquilino de Azure deseado, registre una nueva aplicación denominada Security Onion. La mayoría de las organizaciones sólo desearán
cuentas de organización para tener acceso a Security Onion, así que asegúrese de elegir la opción de tipo de cuenta correcta. No elegir esto correctamente
podría exponer su instalación de Security Onion a usuarios fuera de su organización. Especifique la aplicación como Web, con URI de redireccionamiento usando
la URL que los analistas utilizarán para acceder a SOC después de finalizar su inicio de sesión en Azure. Por lo general, esto se parecerá al siguiente patrón:
https://<my-SOC-base-url>/auth/self-service/methods/oidc/callback/SSO. Omit the /SSO suffix if forcing PKCE (Proof Key Code
Intercambio). Haga clic en Registrarse y, en la pantalla resultante, busque el ID de la aplicación para el registro de esta nueva aplicación. También se parecerá a un UUID.
- 336/402 - Seguridad Cebolla Soluciones, LLC

21.2.1 Configuración
Ubique la configuración client_id en la pantalla de configuración de SOC nuevamente en la pestaña del navegador SOC. Especifique el ID de la aplicación anterior para esta configuración.
Agregue un nuevo secreto de cliente al registro de la aplicación creado anteriormente. Especifique el nombre secreto como so-oidc y elija la caducidad que hace que el
más sentido para su organización. Si opta por utilizar un vencimiento a corto o medio plazo, una buena práctica es hacerlo muy corto, de modo que
obliga a que sus procesos de rotación sean bien conocidos y documentados. Elegir un vencimiento medio de dos años probablemente causará más problemas
cuando el secreto caduca y el equipo administrativo pierde el conocimiento de cómo resolverlo. Copie el secreto generado a su
portapapeles. Sólo tendrás esta única oportunidad de copiar el secreto. Volver a este secreto más tarde no proporcionará acceso al secreto original.
- 337/402 - Soluciones de cebolla de seguridad, LLC

21.2.1 Configuración
Localice la configuración client_secret en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el secreto de cliente anterior para esto
configuración.
Si fuerza la habilitación de PKCE (intercambio de código de clave de prueba), establezca la configuración de pkce en la pantalla de configuración de SOC para forzar. al forzar
PKCE, el URI de redireccionamiento debe omitir el sufijo /SSO final.
A continuación, pase a la sección Habilitación de OIDC para habilitar la autenticación OIDC recién configurada.
DIRECTORIO ACTIVO (AUTOHOSPEDADO)
Póngase en contacto con el equipo de soporte de Security Onion Solutions para determinar los cambios de configuración específicos necesarios para integrar su Security Onion.
Grid con la instalación de Active Directory de su organización. Revisarán su versión actual de Windows Server y le ayudarán con el certificado TLS.
configuraciones aplicables a su organización y le guiará a través de los pasos necesarios para completar la integración.
La integración con Active Directory local tiene varios requisitos previos:
• Instalación completamente funcional de Active Directory en Windows Server 2022
• Acceso de administrador al servidor Windows Active Directory
• Acceso de administrador al administrador de Security Onion a través de SSH y SOC
• Capacidad de obtener certificados TLS confiables en sistemas cliente y SO.
• Capacidad de activar los Servicios Federados de Active Directory (ADFS) en el servidor de Active Directory
• Acceso HTTPS desde los navegadores de los analistas de Security Onion al servidor ADFS.
• Acceso HTTPS desde el administrador de Security Onion al servidor ADFS
GOOGLE
Localice la configuración del proveedor en la pantalla de configuración de SOC. Especifique el valor de Google para esta configuración.
En una pestaña separada del navegador, inicie sesión en Google Cloud Console y seleccione o cree un proyecto en su organización de Google que contenga el
usuarios del espacio de trabajo que planea utilizar para la integración. Navegue a la pantalla Credenciales y agregue una nueva ID de cliente OAuth 2.0 denominada Seguridad
Cebolla, de tipo web. Especifique el URI de redireccionamiento web mediante la dirección URL que los analistas usarán para acceder al SOC después de finalizar su inicio de sesión en Azure.
Por lo general, esto se parecerá al siguiente patrón: https://<my-SOC-base-url>/auth/self-service/methods/oidc/callback/SSO.
- 338/402 - Soluciones de cebolla de seguridad, LLC

21.2.1 Configuración
Cuando se agrega la ID del cliente, aparecerá una ventana emergente con la nueva ID del cliente y el secreto. Estos valores deben ingresarse en la configuración del SOC.
pantalla.
Ubique la configuración client_id en la pantalla de configuración de SOC nuevamente en la pestaña del navegador SOC. Especifique el ID de cliente anterior para esta configuración.
Localice la configuración client_secret en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el secreto de cliente anterior para esto
configuración.
A continuación, pase a la sección Habilitación de OIDC para habilitar la autenticación OIDC recién configurada.
GITHUB
Localice la configuración del proveedor en la pantalla de configuración de SOC. Especifique el valor github para esta configuración.
En una pestaña separada del navegador, inicie sesión en la cuenta de GitHub que planea usar para la integración. Vaya a Configuración de la organización y luego
Configuración de desarrollador -> Aplicaciones OAuth. Haga clic en el botón Nueva aplicación OAuth de organización. Ingrese Security Onion para el nombre de la aplicación, la URL de inicio de sesión para
su SOC Grid para la URL de la página de inicio y una descripción opcional, y luego la URL de devolución de llamada de autorización, que se parecerá a la siguiente
patrón: https://<my-SOC-base-url>/auth/self-service/methods/oidc/callback/SSO. Haga clic en Registrar solicitud.
- 339/402 - Soluciones de cebolla de seguridad, LLC

21.2.1 Configuración
Una vez creada la aplicación, una nueva pantalla mostrará la configuración de la aplicación OAuth recién creada, incluido el ID y el secreto del cliente generado.
- 340/402 - Soluciones de cebolla de seguridad, LLC

21.2.1 Configuración
Asegúrese de copiar el secreto antes de actualizar o salir de esta pantalla. Estos dos valores deben ingresarse en el SOC.
pantalla de configuración.
Ubique la configuración client_id en la pantalla de configuración de SOC nuevamente en la pestaña del navegador SOC. Especifique el ID de cliente anterior para esta configuración.
Localice la configuración client_secret en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el secreto de cliente anterior para esto
configuración.
A continuación, pase a la sección Habilitación de OIDC para habilitar la autenticación OIDC recién configurada.
AUTORIZACIÓN0
Localice la configuración del proveedor en la pantalla de configuración de SOC. Especifique el valor auth0 para esta configuración.
En una pestaña separada del navegador, inicie sesión en la cuenta Auth0 que planea usar para la integración. Cree una nueva aplicación llamada Security Onion.
Una vez creado, navegue hasta la pestaña Configuración. Desplácese hacia abajo hasta la sección URI de aplicación e ingrese https://<my-SOC-base-url> para
URI de inicio de sesión de la aplicación y URL de cierre de sesión, y luego ingrese la URL de devolución de llamada, que se parecerá al siguiente patrón: https://<my-SOC-base-
url>/auth/self-service/methods/oidc/callback/SSO. Haga clic en Guardar cambios.
- 341/402 - Seguridad Cebolla Soluciones, LLC

21.2.1 Configuración
Desplácese hacia atrás hasta la parte superior de la página Configuración de Auth0 donde se muestran el ID del cliente y el secreto.
- 342/402 - Seguridad Cebolla Soluciones, LLC

21.2.1 Configuración
Asegúrese de copiar el secreto antes de actualizar o salir de esta pantalla. Estos dos valores deben ingresarse en el SOC.
pantalla de configuración.
Ubique la configuración client_id en la pantalla de configuración de SOC nuevamente en la pestaña del navegador SOC. Especifique el ID de cliente anterior para esta configuración.
Localice la configuración client_secret en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el secreto de cliente anterior para esto
configuración.
De vuelta en la pestaña Auth0, desplácese hacia abajo hasta la sección Configuración avanzada y haga clic en Puntos finales. Copie la URL de autorización de OAuth, pero sin el
/autorizar ruta. Ubique la configuración de Issuer_url en la pantalla de configuración de SOC en la pestaña del navegador SOC. Pegue la URL copiada en
esta configuración. Debería parecerse al siguiente: https://dev-xyz123abc456.us.auth0.com
A continuación, pase a la sección Habilitación de OIDC para habilitar la autenticación OIDC recién configurada.
GENÉRICO (EJ.: PING)
Security Onion puede funcionar con la mayoría de los proveedores de OIDC, incluso si no se menciona anteriormente como un proveedor con soporte explícito. Para mostrar un ejemplo de
cómo configurar un proveedor genérico, las siguientes instrucciones mostrarán cómo se puede utilizar [Ping SSO](https://pingone.com) como OIDC
proveedor de Security Onion.
Localice la configuración del proveedor en la pantalla de configuración de SOC. Especifique el valor genérico para esta configuración.
- 343/402 - Seguridad Cebolla Soluciones, LLC

21.2.1 Configuración
En una pestaña separada del navegador, inicie sesión en una consola Ping Identity y, en el entorno del espacio de trabajo deseado, cree una nueva aplicación llamada
Cebolla de seguridad. Elija la aplicación web OIDC y haga clic en Guardar. En la pestaña Configuración, especifique un URI de redireccionamiento utilizando el siguiente patrón:
https://<my-SOC-base-url>/auth/self-service/methods/oidc/callback/SSO.
Ubique la configuración client_id en la pantalla de configuración de SOC nuevamente en la pestaña del navegador SOC. Especifique el ID del cliente de Ping para esta configuración.
Esa ID se puede ubicar en la pestaña de configuración de Ping, como se muestra arriba.
Genere un nuevo secreto de cliente en el campo Ping Client ID. Copie el secreto generado a su portapapeles.
- 344/402 - Seguridad Cebolla Soluciones, LLC

21.2.1 Configuración
Localice la configuración client_secret en la pantalla de configuración de SOC en la pestaña del navegador SOC. Especifique el secreto de cliente anterior para esto
configuración.
En la pestaña del navegador de la consola Ping, en la pestaña de configuración, expanda la sección URL, cerca de la parte superior. Copie y pegue las tres URL siguientes
en los ajustes de pantalla de configuración de SOC correspondientes:
• URL de autorización -> auth_url
• Emisor -> URL_emisor
• Punto final del token -> token_url
Si fuerza la habilitación de PKCE (Intercambio de código de clave de prueba), establezca la configuración de Aplicación de PKCE en la pestaña de configuración de la consola Ping en
S256_REQUIRIDO.
En la pestaña del navegador de la consola Ping, navegue hasta la pestaña Recursos y agregue el correo electrónico como alcance adicional.
Ubique la configuración del alcance en la pantalla de configuración de SOC en la pestaña del navegador SOC. Cambie el alcance del perfil predeterminado a openid.
Ahora deberían aparecer tanto el alcance de correo electrónico como el de openid.
A continuación, pase a la sección Habilitación de OIDC para habilitar la autenticación OIDC recién configurada.
HABILITACIÓN DE OIDC
Finalmente, habilite OIDC ubicando la configuración habilitada en la configuración SOC y especifique el valor verdadero para esta configuración.
- 345/402 - Soluciones de cebolla de seguridad, LLC

21.2.2 Inicio de sesión inicial
Nota
No habilite OIDC hasta que se hayan ingresado todos los ajustes de configuración requeridos y se haya verificado su precisión. Una vez habilitado el backend
El sistema sincronizará automáticamente la configuración en toda la red, normalmente en 15 minutos. Si algunas configuraciones son incorrectas o faltan
Los servicios de autenticación de backend podrían quedar en un estado de error y hacer que sea imposible solucionarlos a través de la pantalla de Configuración, ya que es posible que la interfaz de usuario del SOC no funcione.
ya no será accesible. Si esto ocurre, se requerirá una sesión SSH para acceder a los archivos de configuración subyacentes en el nodo administrador. Contacto
soporte para asistencia si es necesario.
Advertencia
Una vez que OIDC esté habilitado, cualquier usuario del proveedor de identidad externo seleccionado podrá iniciar sesión en SOC, siempre que tenga acceso a la red para hacerlo.
Sin embargo, una vez que haya iniciado sesión, el nuevo usuario no tendrá roles asignados y no podrá ver ni modificar datos SOC confidenciales. Consulte la sección Funciones a continuación para
más información.
21.2.2 Inicio de sesión inicial
Tras el primer inicio de sesión a través de OIDC, es probable que el usuario regrese a la pantalla de inicio de sesión. Sin embargo, al hacer clic en Continuar con la segunda vez
llevará al usuario recién vinculado a la interfaz SOC. Este clic de inicio de sesión adicional solo es necesario una vez.
21.2.3 Funciones
Cuando un nuevo usuario de OIDC inicia sesión en SOC, a ese usuario no se le asignará ninguna función, a menos que se haya configurado una función predeterminada del sistema. Esto en gran medida
limita qué funciones el usuario será capaz de realizar dentro del SOC. Por ejemplo, los nuevos usuarios no podrán ver ninguna alerta, buscar
eventos, ver datos del panel, ver o crear casos, administrar la cuadrícula o ver otros usuarios. Intentar ver esas pantallas protegidas por roles
resultará en un mensaje de error.
Si no se configura una función predeterminada del sistema, un administrador deberá iniciar sesión en SOC y asignar funciones a los usuarios de OIDC a través de Administración ->
Pantalla de usuarios. Esta es una operación única por usuario.
- 346/402 - Seguridad Cebolla Soluciones, LLC

21.2.4 Gestión de usuarios de OIDC
21.2.4 Gestión de usuarios de OIDC
Los usuarios creados mediante un inicio de sesión OIDC no deben tener sus credenciales administradas dentro del SOC. Cuando un administrador ve un usuario OIDC en el
Administración -> Pantalla de usuarios, notarán que aparece un mensaje cerca del panel de control de acceso y les advierte contra cambios
configuración de autenticación para ese usuario.
Nota
La autenticación se relaciona con la obtención de acceso a un sistema, mientras que la autorización se relaciona con los permisos que tiene un usuario dentro del sistema. mientras
La configuración de autenticación de los usuarios de OIDC no debe administrarse dentro del SOC, la configuración de autorización se puede administrar dentro del SOC para los usuarios de OIDC. Ver
Consulte la sección Roles anterior para obtener más información sobre cómo otorgar roles a los usuarios de OIDC.
21.2.5 Autoservicio OIDC
Los usuarios seguirán teniendo acceso a su propia configuración de seguridad a través de la pantalla Configuración de usuario -> Seguridad. Un usuario podría configurar un SOC local
contraseña a través de esta pantalla, lo que permitiría iniciar sesión en SOC para ese usuario sin usar SSO. Después de establecer una contraseña local, un usuario podría entonces
desvincular la cuenta SSO, lo que no permitiría al usuario iniciar sesión a través de SSO pero aún le permitiría iniciar sesión a través de la contraseña local.
Por el contrario, los usuarios que han iniciado sesión localmente y que aún no han iniciado sesión a través de SSO pueden vincularse a su usuario de SSO.
- 347/402 - Seguridad Cebolla Soluciones, LLC

21.2.6 Herramientas externas
Si desea asegurarse de que todos los inicios de sesión se realicen a través del proveedor OIDC externo, puede desactivar los inicios de sesión con contraseña. En SOC, navegue hasta
Administración --> Configuración. En la parte superior de la página, haga clic en el menú Opciones y luego habilite la opción Mostrar configuración avanzada. entonces
filtre por contraseña. habilitado para localizar la configuración.
De manera similar, las opciones TOTP MFA y Sin contraseña también se pueden desactivar, si se desea evitar que los usuarios alteren todos los datos locales.
métodos de autenticación. Busque totp.enabled y webauthn.enabled, respectivamente, para desactivar esos métodos de autenticación.
Cuando se hayan desactivado todos los métodos de autenticación local, los usuarios no tendrán ninguna configuración de seguridad que modificar en su pantalla de autoservicio:
21.2.6 Herramientas externas
Las herramientas incluidas con Security Onion, pero proporcionadas por otros proveedores, no utilizarán el inicio de sesión único SOC. Esto incluye herramientas como InfluxDB,
Kibana y otras herramientas proporcionadas por Elastic. Si los usuarios necesitan acceder a estas herramientas, el método de autenticación de contraseña debe estar habilitado y un
configuración de contraseña local. Luego, los usuarios pueden iniciar sesión en esas herramientas utilizando su dirección de correo electrónico SSO y la contraseña SOC local.
- 348/402 - Seguridad Cebolla Soluciones, LLC

21.3 LUCAS
21.3 LUCAS
LUKS significa Configuración de clave unificada de Linux y puede leer más al respecto en https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup.
El cifrado de disco LUKS es una función que requiere el uso de la licencia Security Onion Pro.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.3.1 Habilitación de LUKS durante la instalación ISO
La forma recomendada de utilizar LUKS con Security Onion es instalarlo a través de nuestra imagen ISO de Security Onion. En el menú de inicio ISO, deberás
modificar el comando de arranque. Esto se puede hacer usando la tecla e en el modo de inicio UEFI o la tecla Tab en el modo de inicio BIOS antes de que se inicie automáticamente.
botas. Luego agregue luks=1 (y posiblemente otras opciones como FIPS y STIG) a los parámetros de arranque y continúe con el proceso de arranque.
21.3.2 Instalación de LUKS sin TPM
Durante la instalación inicial de ISO, se le pedirá al usuario que ingrese una contraseña para cifrar las particiones LUKS. Si hay varias unidades
detectado entonces el usuario tiene la opción de simplemente cifrar /nsm. Tenga en cuenta que esta contraseña será necesaria en cada inicio.
21.3.3 Opciones de instalación de LUKS con un TPM
Si hay un módulo TPM instalado en el sistema, tendrá la opción de almacenar la clave en el TPM para desbloquear las unidades automáticamente en el arranque.
Este proceso utiliza horquilla para gestionar este proceso.
21.3.4 Inscripción/reinscripción de LUKS TPM
Puede haber un caso en el que ya haya instalado Security Onion con LUKS habilitado, pero no optó por usar su TPM para la configuración automática.
descifrado en el arranque. En este caso, puede utilizar el script so-luks-tpm-regen para inscribir el TPM y configurarlo para el descifrado automático.
SSH al nodo Security Onion y ejecute el siguiente comando:
sudo so-luks-tpm-regen --enroll-tpm
De manera similar, si por alguna razón el descifrado automático estaba previamente habilitado usando la ISO y ahora dejó de funcionar, puede volver a registrar el
TPM.
sudo so-luks-tpm-regen
- 349/402 - Soluciones de cebolla de seguridad, LLC

21.4 FIPS
21.4 FIPS
FIPS significa Estándares Federales de Procesamiento de Información y puede leer más al respecto en https://en.wikipedia.org/wiki/
Estándares_federales_de_procesamiento_de_información.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.4.1 Habilitación de FIPS durante la instalación ISO
La forma recomendada de utilizar FIPS con Security Onion es instalarlo a través de nuestra imagen ISO de Security Onion. En el menú de inicio ISO, deberás
modificar el comando de arranque. Esto se puede hacer usando la tecla e en el modo de inicio UEFI o la tecla Tab en el modo de inicio BIOS antes de que se inicie automáticamente.
botas. Luego agregue fips=1 (y posiblemente otras opciones como LUKS y STIG) a los parámetros de arranque y continúe con el proceso de arranque.
- 350/402 - Soluciones de cebolla de seguridad, LLC

21.5 STIG
21.5 STIG
STIG significa Guía de implementación técnica de seguridad. Para obtener más información sobre STIG, consulte https://public.cyber.mil/stigs/.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.5.1 STIG durante la instalación ISO
La forma recomendada de utilizar STIG con Security Onion es instalar a través de nuestra imagen ISO de Security Onion. Desde el menú de instalación seleccionarás
la opción Instalar Security Onion Pro.
La instalación utilizando las opciones del menú de Security Onion Pro creará particiones adicionales en su sistema para cumplir con los requisitos de STIG. el
Las particiones creadas incluyen:
Almacenamiento de particiones
/casa 25GB
/tmp 2GB
/var 50GB
/var/log 5GB
/var/log/auditoría 2GB
/var/tmp 2GB
Además de las particiones requeridas, el uso de la opción de menú STIG también configurará el sistema para usar el modo FIPS y habilitará el disco LUKS.
cifrado. Ambas opciones se pueden utilizar independientemente de la opción del menú STIG según sus requisitos.
21.5.2 Habilitación de STIG
Advertencia
Antes de habilitar STIG en su implementación de producción de Security Onion, recomendamos realizar pruebas en un entorno de desarrollo. Con diferentes
entornos y configuraciones, puede haber errores inesperados.
Actualmente, no todos los tipos de nodos admiten completamente la habilitación de STIG. Estos incluyen lo siguiente:
• Nodos de hipervisor
• Las máquinas virtuales creadas dentro de un nodo de hipervisor admiten la habilitación de STIG
• Nodos pesados
• Nodos IDH
Para habilitar STIG, primero deberá configurar su Security Onion Grid y aplicar su licencia Security Onion Pro. Luego puede navegar a
Administración --> Configuración --> stig --> habilitado y establezca el valor en verdadero.
Nota
Deberá habilitar la opción Administración --> Mostrar configuración avanzada para modificar esta configuración.
21.5.3 OpenSCAP
Para aplicar STIG en Security Onion utilizamos una combinación de nuestra gestión de configuración Saltstack existente y OpenSCAP.
Actualmente, OpenSCAP está utilizando una versión borrador de STIG para Oracle Linux 9.
- 351/402 - Soluciones de cebolla de seguridad, LLC

21.5.4 Más información
OpenSCAP se puede configurar para ejecutarse en diferentes intervalos de tiempo. De forma predeterminada, OpenSCAP ejecutará una corrección cada 12 horas, lo que significa que cualquier
Los cambios realizados en el sistema que lo dejen fuera de cumplimiento se revertirán al estado compatible con STIG. Esta configuración se puede reducir o
aumentado modificando la configuración run_interval que se encuentra en Administración --> Configuración --> stig
Con la función STIG habilitada, puede encontrar informes de OpenSCAP en /opt/so/log/stig. Actualmente, el puntaje de cumplimiento esperado es del 86%.
21.5.4 Más información
Para obtener más información sobre OpenSCAP, consulte: https://www.open-scap.org/.
Para obtener más información sobre STIG, consulte: https://public.cyber.mil/stigs/.
- 352/402 - Soluciones de cebolla de seguridad, LLC

21.6 Notificaciones
21.6 Notificaciones
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
El módulo Detecciones, específicamente las reglas de Sigma, se puede habilitar para enviar notificaciones salientes al crearse una alerta. Por defecto, no
las notificaciones salientes están habilitadas en una instalación de Security Onion. Sin embargo, con la licencia Pro aplicada a una cuadrícula, las notificaciones pueden ser rápidamente
configurado a través de la pantalla de Configuración.
21.6.1 Configuración
Configurar notificaciones implica ajustar la configuración en dos áreas:
1. Alertas ElastAlert 2
2. Detecciones de SOC
Alertas ElastAlert 2
ElastAlert incluye una gran cantidad de alertas que pueden llegar a sistemas remotos para enviar notificaciones. Como cada alerta admite un único
protocolo, el alertador requiere su propio conjunto de parámetros de soporte para que sepa cómo comunicarse con el punto final remoto.
Por ejemplo, para enviar una notificación a un canal de Slack, se debe proporcionar una URL de webhook.
Navegue a la pantalla Administración -> Configuración. A continuación, ubique la configuración de ElastAlert.
Observe que hay configuraciones especiales para las notificaciones de Jira y SMTP. Estos son únicos porque ElastAlert requiere que esas dos alertas lean sus
credenciales de un archivo. Security Onion ha simplificado este proceso presentando estos campos de Configuración para ingresar la credencial opcional
datos y el proceso backend se encargará de generar los archivos necesarios para ElastAlert.
- 353/402 - Soluciones de cebolla de seguridad, LLC

21.6.1 Configuración
El subárbol de archivos incluye una lista de varias configuraciones de archivos, lo que permite completar el contenido de ciertos archivos que las alertas pueden opcionalmente
utilizar. La mayoría de los alertadores utilizan los archivos para especificar una autoridad de certificación personalizada, de modo que ElastAlert pueda conectarse de forma segura y confiable a
servidores remotos que pueden estar utilizando certificados SSL/TLS personalizados. Nuevamente, el proceso backend de Security Onion se encargará de generar estos archivos.
a partir de los datos de configuración proporcionados en la interfaz de usuario.
A continuación, la configuración SOC > config > servidor > módulos > elastalertengine > Notificaciones: Sev 0/Parámetros predeterminados se utiliza para personalizar cada
parámetros propios de la alerta. Como ElastAlert ya proporciona documentación detallada sobre los parámetros requeridos para cada alertador, este
La documentación no cubrirá la misma información, sino que se centrará en dos alertas populares: Slack y SMTP.
Nota
Consulte los parámetros de alerta en https://elastalert2.readthedocs.io/en/latest/alerts.html#alert-types.
flojo
Para que las reglas de Sigma envíen notificaciones a Slack, agregue la siguiente línea a SOC > config > server > module > elastalertengine >
Notificaciones: Gravedad 0/Configuración de parámetros predeterminados:
slack_webhook_url: "[https://hooks.slack.com/services/YOUR_WEBHOOK_URI](https://hooks.slack.com/services/YOUR_WEBHOOK_URI)"
Correo electrónico (SMTP)
Para que las reglas de Sigma envíen notificaciones por correo electrónico, agregue las siguientes líneas al SOC > config > server > module > elastalertengine >
Notificaciones: Gravedad 0/Configuración de parámetros predeterminados:
correo electrónico: sucorreo electrónico@suempresa.com
smtp_host: "su_empresa_smtp_server"
from_addr: "ElastAlert@tuempresa.com"
Si el servidor SMTP requiere autenticación, asegúrese de que también estén configurados los ajustes de configuración especiales de Nombre de usuario SMTP y Contraseña SMTP.
especificado.
Detecciones de SOC
Una vez configurados los parámetros de alerta, como se describe anteriormente, el siguiente paso es configurar las Detecciones para activar una o más
alertas de notificación.
Navegue a la pantalla Administración -> Configuración. A continuación, ubique SOC > config > server > module > elastalertengine settings.
En la configuración de Notificaciones: Gravedad 0/Alertas predeterminadas, agregue el nombre de cada alerta que debe activarse, un nombre de alerta por
línea. Por ejemplo, para agregar tanto slack como correo electrónico:
correo electrónico flojo
- 354/402 - Seguridad Cebolla Soluciones, LLC

21.6.1 Configuración
¡Importante! Después de activar (o eliminar) una alerta de esta configuración, el motor ElastAlert debe actualizarse por completo. Esto se puede hacer a través del
Pantalla Detecciones, en el menú desplegable Opciones.
Notificaciones basadas en gravedad
Las instrucciones anteriores configuran la configuración de notificación predeterminada para todas las notificaciones salientes. Sin embargo, la configuración de notificaciones se puede personalizar.
para niveles de gravedad más altos. Las gravedades se especifican en Detecciones Sigma.
- 355/402 - Soluciones de cebolla de seguridad, LLC

21.6.1 Configuración
Los niveles de gravedad progresan de la siguiente manera, comenzando con la gravedad más baja y menos significativa:
1. Gravedad desconocida
2. Severidad Informativa
3. Baja gravedad
4. Gravedad media
5. Alta gravedad
6. Gravedad crítica
Si la configuración de notificación no se especifica para un nivel de gravedad particular, se utilizará cualquier configuración especificada en el siguiente nivel de gravedad inferior.
Si tampoco se especifica esa gravedad, continúa buscando configuraciones de gravedad más bajas.
Nota
Los niveles de gravedad más altos no heredan parámetros ni alertas de niveles de gravedad más bajos. En consecuencia, si se especifica el correo electrónico como predeterminado (gravedad 0)
alertador, y se desea que tanto las notificaciones por correo electrónico como las de Slack se envíen con gravedad Alta/Severo 4 o superior, entonces tanto el correo electrónico como el Slack se enviarán
deben especificarse para la configuración Notificaciones: Gravedad 4/Alertas predeterminadas, una por línea. Este mismo principio se aplica a los parámetros,
que tampoco se heredan. Para heredar los parámetros predeterminados en todas las gravedades, los parámetros se pueden especificar en ElastAlert >
Configuración de parámetros de configuración personalizados.
Notificaciones definidas por el usuario
Las detecciones de Sigma individuales se pueden etiquetar para cambiar el comportamiento de alerta de la detección. Las etiquetas se establecen dentro de la fuente de detección. Etiqueta
Los detalles se definen a continuación:
• so.notification: Cuando esta etiqueta está presente dentro de una lista de etiquetas Sigma, la detección solo realizará notificaciones salientes. No agregará
una alerta a la pantalla Alertas SOC.
• so.alerters.customAlerters: cuando esta etiqueta está presente dentro de una lista de etiquetas Sigma, la detección realizará notificaciones para una alternativa.
conjunto de alertas ElastAlert 2. A continuación se proporciona más información sobre cómo elegir estas alertas.
• so.params.customAlertersParams: cuando esta etiqueta está presente dentro de una lista de etiquetas Sigma, y cuando la etiqueta anterior también está incluida, entonces se
Se aplicará un conjunto alternativo de parámetros personalizados a las alertas ElastAlert 2.
Para personalizar las alertas y los parámetros que se utilizarán cuando estas etiquetas se especifiquen en una detección Sigma, navegue hasta la pantalla Configuración.
Busque SOC > configuración > servidor > módulos > elastalertengine > adicionalUserDefinedNotifications > configuración de alertas personalizadas
y agregue las alertas personalizadas, una por línea, similar a lo que se hace para las notificaciones basadas en gravedad anteriores. Del mismo modo, busque la configuración de hermanos
para definir parámetros de alerta personalizados:
SOC > configuración > servidor > módulos > elastalertengine > adicionalUserDefinedNotifications > customAlertersParams.
Nota
Las alertas definidas por el usuario anularán las alertas basadas en la gravedad, siempre que estén configuradas correctamente. Si las etiquetas Sigma especifican
alertas personalizadas pero la configuración correspondiente no existe en la Configuración, se seguirán utilizando las notificaciones basadas en la gravedad.
Para crear configuraciones de alertas adicionales definidas por el usuario, habilite el modo avanzado y navegue hasta las mismas alertas personalizadas y
configuración customAlertersParams mencionada anteriormente. Con el modo avanzado habilitado, habrá un botón "Crear duplicado" que permitirá
duplicar estas configuraciones. Siga las instrucciones en pantalla para crear la configuración duplicada. Luego, para hacer uso de estas nuevas configuraciones, en el
La lista de etiquetas Sigma reemplaza el sufijo de la etiqueta so.alerters.customAlerters con el nombre (distingue entre mayúsculas y minúsculas) de la configuración duplicada. Por ejemplo, si
las configuraciones duplicadas se denominan SysAdminAlerters y SysAdminParams, luego las dos etiquetas para especificar en la fuente de detección de Sigma son
so.alerters.SysAdminAlerters y so.params.SysAdminParams. Solo se utilizará una configuración de parámetros y alertas definidas por el usuario si
varias etiquetas coinciden con so.alerters. y así.params. prefijos. En otras palabras, intentar especificar múltiples alertas definidas por el usuario dentro
una sola detección de Sigma dará como resultado un resultado ambiguo.
- 356/402 - Seguridad Cebolla Soluciones, LLC

21.6.2 Formato de notificación
Ejemplo:
título: Security Onion: error de inicio de sesión en el nodo de red (SSH) (copia)
identificación: 0c880a39-f2cc-4e80-af26-eb08e2fe4b0a
estado: experimental
Descripción: Detecta cuando un usuario no puede iniciar sesión en un nodo de grid a través de SSH. Revise los registros asociados para el nombre de usuario y la IP de origen.
autor: Soluciones Onion de Seguridad
fecha: 2024/08/27
fuente de registro:
producto: linux
servicio: autenticación
detección:
selección:
evento.resultado: fracaso
nombre.proceso: sshd
etiquetas|contiene: nodo-so-grid
filtro:
sistema.auth.ssh.método: '*'
condición: selección y no filtro
etiquetas:
- so.alerters.SysAdminAlerters
- so.params.SysAdminParams
- entonces.notificación
falsos positivos:
- ninguno
nivel: alto
licencia: Elastic-2.0
21.6.2 Formato de notificación
Existe una amplia gama de capacidades para formatear mensajes de notificación a los diversos puntos finales admitidos por ElastAlert 2. Consulte la
Documentación de ElastAlert 2 para todos los parámetros de formato disponibles: https://elastalert2.readthedocs.io/en/latest/alerts.html#alert-subject.
A continuación se muestra un ejemplo de cómo personalizar el mensaje de notificación. Este formato es compatible con la mayoría de las alertas ElastAlert 2 pero solo puede
trabajar con alertas específicas relacionadas con la conexión, debido a que hace referencia a campos de conexión específicos. Para usar, pegue estas configuraciones en el lugar deseado
campo de parámetros de alerta de configuración, como se analizó anteriormente en esta sección. Cambie el nombre de host según sea necesario en las URL incluidas.
alert_subject: "Alerta: {0} {1}"
alert_subject_args:
- regla.nombre
- "@marca de tiempo"
texto_alerta: |
Los detalles de la alerta están disponibles en Security Onion Console: https://manager/#/hunt?q=log.id.uid%3A{0}&rt=1&rtu=days
Fuente: {1}:{2}
Destino: {3}:{4}
Investigue el ID de la comunidad de red: https://manager/#/hunt?q=network.community_id%3A"{5}"&rt=1&rtu=days
alert_text_type: alerta_text_only
alert_text_args: ["log.id.uid", "fuente.ip", "fuente.puerto", "destino.ip", "destino.puerto", "network.community_id"]
21.6.3 Aplicar cambios
Para que las alertas y los parámetros surtan efecto, deben ocurrir múltiples sincronizaciones. Estos se realizan automáticamente según un cronograma establecido, pero
es posible forzarlos antes, si es necesario. Específicamente, para que los cambios se apliquen a las reglas de ElastAlert 2 debe ocurrir lo siguiente:
1. El administrador de SOC guarda los cambios en la pantalla de configuración.
2. La configuración se sincroniza en toda la red. Para forzar manualmente una sincronización de grid, vaya a la pantalla Configuración, abra el menú desplegable Opciones
en la parte superior y haga clic en Sincronizar.
3. Las ediciones de Sigma Detección se guardan, como agregar etiquetas de notificación definidas por el usuario o cambiar la gravedad.
4. Las detecciones Sigma están sincronizadas. Haga clic en Sincronización completa para las reglas de ElastAlert o, para forzar una sincronización de detección única, vaya a Detección.
pestaña Fuente, realice una edición en la fuente y haga clic en Actualizar.
Nota
Es posible que el proceso de ElastAlert 2 tarde uno o dos minutos en detectar las reglas modificadas y luego unos minutos más para que ElastAlert 2 ejecute esa regla.
- 357/402 - Seguridad Cebolla Soluciones, LLC

21.7 Kafka
21.7 Kafka
De https://kafka.apache.org:
Apache Kafka es una plataforma de transmisión de eventos distribuida de código abierto utilizada por miles de empresas para obtener datos de alto rendimiento.
canalizaciones, análisis de streaming, integración de datos y aplicaciones de misión crítica.
Si necesita una entrega de mensajes garantizada, puede habilitar Kafka, que reemplaza a Redis y Logstash en el nodo Security Onion Manager.
y nodos receptores.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.7.1 Entrega de mensajes garantizada
Al aprovechar Kafka, puede asegurarse de que los mensajes enviados al clúster de Kafka se escriban en el disco en el líder de la partición y se repliquen en otros.
intermediarios físicos antes de acusar recibo al productor.
Para obtener más información, consulte https://kafka.apache.org/documentation/#producerconfigs_acks.
21.7.2 Alta disponibilidad
Con un clúster de Kafka configurado correctamente, la integridad y la disponibilidad de los datos se mantienen incluso en el caso de que intervenga un corredor o controlador de Kafka.
fracaso. Para empezar a aprovechar Kafka, recomendamos tres controladores Kafka y un mínimo de tres corredores Kafka. con esto
configuración, puede aumentar el factor de replicación para garantizar que los mensajes se repliquen en varios intermediarios.
Para obtener más información sobre la replicación, consulte https://kafka.apache.org/documentation/#replication.
21.7.3 Configuración
importante
Antes de configurar Kafka, se recomienda construir su grilla como lo haría normalmente. Esto incluye agregar cualquier nodo receptor que luego será
reutilizados como intermediarios o controladores de Kafka.
También tenga en cuenta que la entrega de mensajes garantizada que aprovecha Kafka requiere una licencia válida de Security Onion Pro. Ver el Security Onion Pro
sección.
Puede modificar su configuración de Kafka yendo a Administración --> Configuración --> Kafka.
- 358/402 - Soluciones de cebolla de seguridad, LLC

21.7.3 Configuración
Controladores
Los controladores son responsables de administrar el clúster de Kafka. Esto incluye elegir un líder y administrar los metadatos del clúster.
Los controladores pueden ser máquinas virtuales o físicas relativamente livianas. Un sistema con 4 núcleos de CPU, 8 GB de RAM y 200 GB de almacenamiento
debería ser suficiente para un solo controlador Kafka.
Los controladores se asignan agregando los nombres de host a la opción de configuración de los controladores separados por una coma.
nombre de host1, nombre de host2, nombre de host3
Le recomendamos que tenga al menos tres controladores. Esto permite que falle un solo controlador y que el clúster continúe funcionando.
Para obtener más información sobre los controladores, consulte https://kafka.apache.org/documentation/#kraft_voter.
Corredores
Los corredores son responsables del almacenamiento y replicación de mensajes. Con Kafka habilitado, Elastic Agent comenzará a actuar como productor y
escribe sus mensajes en temas almacenados en los corredores de Kafka.
Los corredores requieren muchos más recursos que los controladores, ya que son responsables de gestionar los datos y proporcionarlos a los consumidores.
El tamaño de los corredores depende en gran medida del volumen de mensajes esperado. Debería ser un sistema con 8 núcleos de CPU, 32 GB de RAM y 500 GB de almacenamiento.
suficiente para un único broker Kafka.
Advertencia
Las recomendaciones de hardware anteriores deben utilizarse como mínimo. Aumentar el número de corredores y los recursos disponibles para cada uno
El corredor aumentará el rendimiento general del clúster Kafka. Además, sin suficiente espacio de almacenamiento en cada corredor, el clúster puede ejecutar
sin espacio y dejar de aceptar mensajes. La configuración de brokers log.retention.hours se puede configurar para eliminar mensajes después de un cierto
cantidad de tiempo para evitar que esto suceda.
La configuración del corredor se puede modificar yendo a Administración --> Configuración --> Kafka --> config --> corredor.
- 359/402 - Soluciones de cebolla de seguridad, LLC

21.7.4 Más información
Para obtener más información sobre la configuración del agente, consulte https://kafka.apache.org/documentation/#brokerconfigs.
Habilitando a Kafka
Una vez que tenga la configuración adecuada, puede habilitar Kafka navegando a Administración --> Configuración --> global -->
canalización y estableciendo el valor en KAFKA.
No es necesario hacer clic en el botón SINCRONIZAR CUADRICULA. Una vez que haya establecido el valor de canalización global en KAFKA, los cambios comenzarán a realizarse.
tendrá efecto en segundo plano antes de cambiar finalmente la red a la nueva tubería.
Nota
Para cambiar la canalización global, deberá habilitar la opción Administración --> Mostrar configuración avanzada.
21.7.4 Más información
Nota
| Para obtener más información sobre Kafka, consulte: https://kafka.apache.org/documentation/#gettingStarted
- 360/402 - Soluciones de cebolla de seguridad, LLC

21.8 API de cebolla de seguridad
21.8 API de cebolla de seguridad
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
La API de Security Onion permite que otros servidores se integren con Security Onion y accedan a la misma funcionalidad que Security Onion.
Proporciona la interfaz de usuario de la consola. El acceso a la API de Security Onion se permite a través de Clientes API, que pueden ser creados por SOC
administradores a través de la interfaz de usuario de SOC -> Administración -> pantalla Clientes API.
La API Security Onion actualmente proporciona funcionalidad expuesta por el servidor Security Onion Console. No proporciona acceso completo a terceros.
aplicaciones de terceros incluidas con la plataforma Security Onion. Específicamente, si bien puedes leer eventos de Elasticsearch, no puedes
manipular la configuración de Kibana a través de la API Security Onion, a menos que esas configuraciones ya estén expuestas a través del sistema de configuración SOC.
21.8.1 Referencia de API
Advertencia
Las nuevas versiones de Security Onion pueden contener campos adicionales en las respuestas de la API. En consecuencia, es importante que la salida de la API se realice correctamente.
analizado por bibliotecas oficiales que pueden manejar estos escenarios. El uso de un análisis personalizado de los resultados de la API puede provocar fallos de funcionamiento relacionados con la actualización.
Hay una vista API interactiva disponible para visualización basada en navegador: API interactiva
Para conectarse a la API, deberá seguir los pasos a continuación.
21.8.2 Habilitación de la API Security Onion
De forma predeterminada, las grids recién configuradas no se configurarán para el acceso de clientes API. Para habilitar el acceso del cliente API, se deben seguir los siguientes pasos:
1. Se debe aplicar una clave de licencia a la red. La clave de licencia debe incluir la función API.
2. La función Hydra debe habilitarse a través de la configuración Hydra > habilitada en la pantalla de Configuración.
3. Sincronice el grid para aplicar la clave de licencia y los cambios de configuración. Esto se puede hacer a través del menú desplegable de opciones de la pantalla de Configuración.
21.8.3 Credenciales de cliente API
Para comunicarse con la API de Security Onion, se debe crear un cliente API. Navegue al menú Administración usando un superusuario
cuenta. En el menú Administración, haga clic en la opción de menú Clientes API. Cree un nuevo cliente API utilizando un nombre corto que refleje la
uso previsto de este cliente. Utilice el campo Notas para proporcionar más información, si lo desea. Al guardar el nuevo cliente, se generará un secreto.
ser emitido. Este par de ID de cliente y secreto es necesario para autenticarse en la API Security Onion. Proteja estas credenciales utilizando lo mejor de la industria
prácticas.
21.8.4 Autorización/RBAC
Los clientes API pueden acceder a varios componentes dentro de Security Onion utilizando el mismo sistema RBAC para los usuarios. Sin embargo, en lugar de
Cuanto más asigne roles a los clientes API, más permisos granulares se asignarán. Por ejemplo, si bien a un usuario se le puede asignar el rol de analista, una API
Al cliente se le asignarían los eventos/lectura, eventos/escritura, casos/lectura, etc. Esto garantiza que los sistemas remotos solo tendrán acceso al
permisos mínimos necesarios requeridos para la integración.
Actualmente, los alcances de OAuth 2.0 no se utilizan, ya que estos permisos se asignan fuera del flujo de OAuth 2.0.
- 361/402 - Seguridad Cebolla Soluciones, LLC

21.8.5 Flujo de autenticación de OAuth 2.0
21.8.5 Flujo de autenticación de OAuth 2.0
Los clientes API deben utilizar el flujo de credenciales del cliente OAuth 2.0 para autenticarse en el nodo administrador de Security Onion.
Intercambiar credenciales de cliente por un token de acceso
Obtenga un token de acceso enviando una solicitud POST a https://BASE_URL/oauth2/token y proporcionando el ID y el secreto del cliente a través de
Esquema de autenticación básico. El cuerpo de la solicitud debe contener Grant_type=client_credentials.
Ejemplo:
curl --cacert ca.crt -X POST -u socl_my_new_client:hwKHspsX2bMuoIs7kGwN https://BASE_URL/oauth2/token -d Grant_type=client_credentials
Dónde reemplazarás:
• ca.crt con la autoridad certificadora de su administrador. Si se aplicó un certificado personalizado a su red después de completar la configuración, puede
acceda a él a través de la pantalla de Configuración (requiere rol de superusuario) desde la configuración de configuración nginx > ssl > SSL/TLS Cert File [adv], o si
utilizando la autoridad de certificación generada predeterminada, recupere el archivo de certificado /etc/pki/ca.crt a través de SSH desde el nodo del administrador.
• socl_my_new_client con su ID de cliente (generado por SOC durante la creación del cliente API)
• hwKHspsX2bMuoIs7kGwN con el secreto generado por su cliente API
• BASE_URL con la IP o el nombre de host de su administrador, según la opción que seleccionó durante la configuración de Security Onion
La respuesta será similar a la siguiente:
{"access_token":"ory_at_xI1_2FVvoWR60GHAXZXAcDW7V3qEi2mIB8RKnpqN0fk.Hy5LaHPqh9sfWVEtDXDhs8Gj-9YZ85FJHp6pyD0eeNw","expires_in":
3599,"alcance":"","token_type":"portador"}
El token de acceso caducará en 2 horas, de forma predeterminada, después de lo cual se deberá solicitar un nuevo token de acceso utilizando este mismo intercambio de credenciales.
método nuevamente.
Autorizar solicitudes de API con un token de acceso
Ahora que se ha recuperado el token de acceso, se pueden enviar las solicitudes de API. Estas solicitudes utilizarán el token de acceso a través de HTTP.
Encabezado de autorización, utilizando el esquema Portador.
Ejemplo:
curl --cacert ca.crt -X GET --oauth2-bearer ory_at_U74544Scqho5KGOci-qemWsOjxOU8TALqddAnrfxAGg.7GlO4SYPUAllO23LVqs9e_FXl0tAdRlUk3AH9IplWRU https://
BASE_URL/conectar/información
Donde el token de portador proporcionado anteriormente debe reemplazarse con el token de acceso extraído de la respuesta de intercambio de credenciales del cliente.
21.8.6 Gerente de Gerentes
Para interactuar con los datos de la subcuadrícula, mientras aún se comunica con el nodo principal del Administrador de administradores (MoM), incluya una consulta adicional
parámetro de cadena en la URL de API. La clave del parámetro es gridId y el valor debe establecerse en el ID de subcuadrícula deseado.
- 362/402 - Seguridad Cebolla Soluciones, LLC

21.9 Gestión de consultas activas
21.9 Gestión de consultas activas
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
Los clientes de Security Onion Pro ahora pueden ver y cancelar consultas de Elasticsearch de larga duración.
Esta pantalla se encuentra en el menú Administración en el lado izquierdo de Security Onion Console. Esta opción de menú sólo será visible para
usuarios que tienen el rol de superusuario.
21.9.1 Visualización de consultas activas
De forma predeterminada, la lista de consultas activas filtrará las consultas internas, no cancelables y secundarias. Por lo tanto, en la mayoría de las situaciones será normal que el
lista esté vacía. Si desea ver todas las consultas activas sin ningún filtrado, el superusuario puede hacer clic en la barra de Opciones en la parte superior de la página.
pantalla y se expandirá para mostrar un control deslizante de filtro que se puede desactivar. Tenga en cuenta que la consulta para mostrar esta lista se mostrará en la consulta activa.
lista. Sin embargo, cuando la lista se muestre en la pantalla, la consulta ya habrá finalizado.
Si bien sería fantástico mostrar al usuario que inició la consulta en esta lista de consultas activas, lamentablemente Elasticsearch no proporciona esto.
información.
Nota
Tenga en cuenta que las consultas no iniciadas por un usuario pueden aparecer en la lista filtrada. El filtro solo filtra un tipo específico de consulta que siempre se conoce.
iniciarse internamente.
21.9.2 Cancelación de consultas activas
A veces, una consulta mal escrita o un problema de indexación pueden hacer que una consulta se ejecute durante un tiempo anormalmente largo. Esta consulta de larga duración
puede afectar negativamente la experiencia de Security Onion de otros analistas, ya que sus consultas comenzarán a funcionar más lentamente de lo habitual. Si es de larga duración
Es necesario detener la consulta, el superusuario puede hacer clic en el ícono X en el lado derecho de la lista de consultas activas. Aparecerá una ventana emergente pidiendo
confirmación.
Cancelar consultas puede tardar varios segundos. En consecuencia, al actualizar las consultas activas es posible que aún se muestre esa consulta en la lista durante un breve período de tiempo.
Nota
No todas las consultas son cancelables. Si una consulta no se puede cancelar, no aparecerá ningún icono de cancelación junto a la lista de consultas.
Advertencia
La cancelación de consultas internas del sistema puede interrumpir los procesos internos de Elasticsearch. Evite cancelar consultas que no estén confirmadas como usuario-
creado.
- 363/402 - Seguridad Cebolla Soluciones, LLC

21.10 Gerente de Gerentes
21.10 Gerente de Gerentes
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
Más información sobre la compra de una licencia de Security Onion Pro con las asignaciones de subcuadrícula necesarias para utilizar esta función.
Si es un cliente empresarial responsable de administrar múltiples grids, ¡puede beneficiarse de la función Administrador de administradores!
Esta característica le permite elegir un administrador de red especial (MoM) para configurarlo con conocimiento de redes remotas (subredes), lo que permite que MoM
para comunicarse con la subcuadrícula para consultar y/o modificar el estado de la cuadrícula, eventos, configuración, etc.
Los usuarios con los privilegios adecuados que inicien sesión en MoM podrán interactuar con esas subcuadrículas desde una única interfaz de usuario. Una subred
La lista de selección estará disponible en la parte superior derecha de la interfaz de usuario de SOC. Los usuarios pueden elegir con qué Grid les gustaría interactuar. Además, la culpa
Los estados se propagarán automáticamente hasta la interfaz de usuario de MoM, brindando a esos usuarios actualizaciones rápidas de nuevos estados de falla dentro de las subredes.
independientemente de qué subcuadrícula esté seleccionada actualmente. Si la lista de subcuadrícula se desactiva, eso indicará que la pantalla actual no es compatible
interacción de subred.
Los usuarios que inicien sesión en una interfaz de usuario SOC de subred no tendrán conocimiento ni visibilidad de otras redes hermanas o de MoM Grid.
21.10.1 Requisitos mensuales
La función Administrador de administradores se ha diseñado de manera que solo el nodo MoM Grid requiera acceso de red al administrador de subred.
nodos. Esto simplifica la configuración de la red y del firewall al garantizar que las conexiones del usuario final estén aisladas en un único punto final. Por lo tanto, los usuarios
Los usuarios que hayan iniciado sesión en MoM SOC solo necesitan acceso web al administrador de MoM.
Tenga en cuenta que Manager of Managers está destinado a implementaciones de producción, por lo que solo se admite en MANAGER, MANAGERSEARCH y
Instalaciones AUTÓNOMAS. No es compatible con instalaciones IMPORT o EVAL.
21.10.2 Aislamiento de datos
En una configuración de Administrador de administradores, los datos de cada subcuadrícula residen en reposo dentro de la subcuadrícula únicamente. Si un usuario MoM solicita
información de una subcuadrícula, los datos devueltos transitarán a través del nodo MoM y desde allí se trasladarán al navegador web del usuario.
Nota
Actualmente, Manager of Managers no intenta fusionar datos de varias cuadrículas en una única vista SOC.
El método sugerido para acceder a datos en múltiples cuadrículas, como cuando se buscan alertas en todas las cuadrículas, es utilizar clústeres cruzados.
búsqueda (CCS). Tenga en cuenta que esto debe configurarse de manera que los índices internos de Security Onion queden excluidos del CCS; de lo contrario, habrá un
riesgo de duplicación de datos y/o corrupción de entidades SOC internas como Casos, Detecciones, etc.
21.10.3 Interrupciones de la subred
El nodo MoM esperará que todas las subredes sean accesibles. En caso de que no se pueda acceder a una subred o se encuentre en un estado en el que no pueda responder
correctamente a las solicitudes MoM entrantes, la interfaz MoM SOC mostrará un error notificando a los usuarios que han iniciado sesión que no puede completar el proceso.
solicitud. Las interrupciones de las subredes podrían retrasar la recuperación de información sobre el estado de otras subredes.
Si se espera que una subred permanezca desconectada durante un período más largo, se recomienda desactivar esa subred en la Configuración.
pantalla y luego sincronizar el estado de MoM Grid. Este escenario puede ocurrir con mayor frecuencia con los "kits" de subred que se transportan entre
ubicaciones de campo para fines de recolección forense.
- 364/402 - Seguridad Cebolla Soluciones, LLC

21.10.4 Configuración
21.10.4 Configuración
Advertencia
No continúe con el paso de configuración hasta que se haya aplicado una licencia Security Onion Pro adecuada a cada Grid. Configurar subcuadrículas en
una licencia de Security Onion Pro que no tiene suficientes asignaciones de subred puede hacer que se exceda esa licencia, lo que puede desactivar todas las demás
Funciones profesionales.
La configuración del Administrador de Administradores requiere dos pasos:
1. Cliente API: Creación de un Cliente API en cada administrador de subcuadrícula a través de la pantalla Cliente API de la subcuadrícula
2. Subgrid Config: Configuración de las subgrids en la pantalla MoM Configuration
Cliente API
Cree un cliente API nuevo y dedicado en cada subcuadrícula y asigne todos los permisos que MoM necesitará para realizar las funciones deseadas. Para
Por ejemplo, si los usuarios de MoM necesitarán administración y visibilidad completas (efectivamente, acceso de superusuario), entonces otorgue todos los permisos.
Sin embargo, si los usuarios de MoM solo monitorearán el estado de la subred, entonces los permisos del Cliente API se pueden limitar al permiso de lectura en
recursos específicos, como Grid, nodos, etc.
El ID del cliente API y el secreto serán necesarios en el siguiente paso, así que asegúrese de que estén registrados para cada una de las subcuadrículas.
Mientras esté en la pantalla del Cliente API, haga clic en el ícono ⤓ para descargar el archivo de certificado de la Autoridad de certificación (CA). Este archivo está en formato de texto y el
El contenido se pegará en la configuración de la subcuadrícula en el siguiente paso.
Nota
Tenga en cuenta que cualquier usuario de MoM Grid podrá conectarse a la subcuadrícula utilizando los permisos definidos para el cliente API. Para
Por ejemplo, supongamos que crea un ID de cliente API en la subcuadrícula llamada supermom y le otorga todos los permisos. Una vez que el MoM esté configurado para
conectarse a la subcuadrícula como se muestra en la siguiente sección, luego cualquier usuario en MoM Grid se conectará a la subcuadrícula como supermamá y tendrá todos
permisos a la subcuadrícula independientemente de si el usuario tiene permisos equivalentes en el MoM.
Configuración de subcuadrícula
Una vez que se conocen las credenciales del cliente API de la subcuadrícula, dicha subcuadrícula se puede agregar a la pantalla de configuración de cuadrículas subordinadas del MoM.
- 365/402 - Seguridad Cebolla Soluciones, LLC

21.10.5 Licencias
• Como superusuario, inicie sesión en la interfaz MoM SOC y navegue hasta Administración -> Configuración.
• Busque la configuración SOC > config > servidor > Redes subordinadas.
• Haga clic en el icono + para agregar una nueva subcuadrícula.
• Asigne a la nueva subcuadrícula un ID único que describa con precisión esta subcuadrícula desde la perspectiva del MoM.
• Ingrese la URL del administrador de la subcuadrícula (haga referencia al valor base_url de la subcuadrícula en esta URL completamente formada). Ej: https://mysubgrid. Tenga en cuenta que
esta URL debe ser accesible desde el nodo MoM Grid.
• Pegue o ingrese las credenciales del Cliente API de la subcuadrícula. Esto se refiere al ID de la API del cliente y al secreto generado.
• Pegue el contenido de la Autoridad de certificación del cliente (CA) API de la subcuadrícula en el campo Certificado de CA de la subcuadrícula.
• Si esta subcuadrícula está lista, habilítela.
Agregue subcuadrículas adicionales según lo permita su licencia de Security Onion Pro y luego haga clic en la marca de verificación verde para guardar la configuración.
La configuración se aplicará en el siguiente intervalo de 15 minutos o puede aplicarla inmediatamente en MoM Grid haciendo clic en el
botón SINCRONIZAR GRID en el menú Opciones.
21.10.5 Licencias
La función Administrador de administradores requiere que todos los grids involucrados tengan aplicada una licencia Security Onion Pro válida.
MoM Grid requerirá una licencia especial de Security Onion Pro con una asignación de subgrids codificadas en la licencia que cumpla o supere
el número de subredes configuradas. Exceder la asignación de subred con licencia hará que MoM SOC muestre un estado de licencia "Excedido"
lo que deshabilitará las funciones de Security Onion Pro.
Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para obtener más información sobre la compra de un Security
Licencia Onion Pro con las asignaciones de subred adecuadas.
- 366/402 - Seguridad Cebolla Soluciones, LLC

Servidor MCP 21.11
Servidor MCP 21.11
Los clientes empresariales que utilizan su propia plataforma AI/LLM ahora pueden conectar esa plataforma directamente a su Security Onion Grid utilizando el
Servidor de protocolo de contexto de modelo de cebolla (MCP) de seguridad.
El servidor MCP le brinda a la IA la capacidad de consultar alertas, guías, eventos, etc., lo que proporciona al LLM información adicional necesaria para
tomar decisiones informadas.
Nota
El servidor MCP utiliza la API Security Onion, que es una característica de nivel empresarial de Security Onion. Póngase en contacto con Security Onion Solutions, LLC a través de
visite nuestro sitio web en https://securityonion.com/pro para obtener más información sobre cómo comprar una licencia de Security Onion Pro para habilitar esta función.
21.11.1 Configuración
El servidor MCP es una aplicación de servidor de baja sobrecarga que se mantiene por separado del software Security Onion. Está disponible en GitHub.
repositorio, que incluye las instrucciones de instalación y configuración.
Consulte https://github.com/Security-Onion-Solutions/securityonion-mcp para comenzar.
Nota
Se debe crear un cliente API de Security Onion en la pantalla Clientes API de Security Onion. Al cliente API se le deben conceder permisos suficientes
necesario para realizar las tareas que el LLM deberá ejecutar.
Por ejemplo, si el LLM consultará eventos y guías, entonces el cliente API necesitará eventos/lectura, guías/lectura y detecciones/lectura.
permisos.
21.11.2 Capacidades
El servidor MCP actualmente admite las siguientes operaciones:
• Consultar eventos a través del lenguaje de consulta Onion (OQL)
• Guías de consulta
Es probable que las versiones futuras traigan más funciones, como la capacidad de reconocer alertas.
- 367/402 - Seguridad Cebolla Soluciones, LLC

Aplicación Security Onion 21.12 para Splunk
Aplicación Security Onion 21.12 para Splunk
Los clientes empresariales que utilizan Splunk ahora pueden instalar la aplicación Security Onion para Splunk.
Advertencia
La aplicación Security Onion para Splunk no cuenta con soporte oficial en este momento.
21.12.1 Requisitos
Nota
La aplicación Security Onion para Splunk utiliza la API Security Onion, que es una característica de nivel empresarial de Security Onion. Contacto Seguridad Cebolla
Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para obtener más información sobre cómo comprar una licencia de Security Onion Pro para habilitar esto.
característica.
21.12.2 Configuración
Consulte https://splunkbase.splunk.com/app/7887 para comenzar.
Nota
Se debe crear un cliente API de Security Onion en la pantalla Clientes API. Al Cliente API se le deben otorgar los permisos suficientes necesarios para realizar
las tareas que la aplicación Splunk deberá ejecutar.
- 368/402 - Seguridad Cebolla Soluciones, LLC

21.13 Hipervisor
21.13 Hipervisor
Los clientes de Security Onion Pro pueden crear un nodo hipervisor que pueda ejecutar instancias virtualizadas de Security Onion. Si tiene máquinas elegibles
Con potencia adicional, puede usar esta función para activar máquinas virtuales (VM) Security Onion adicionales para aprovechar ese extra
poder. Esto es compatible con la mayoría de los principales tipos de nodos de Security Onion y es especialmente útil si desea optimizar el potencial de su hardware y
amplíe su rendimiento y retención de Elastic. Comuníquese con su administrador de cuentas para ver si su hardware es compatible.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.13.1 Requisitos mínimos
Tenga en cuenta los siguientes requisitos MÍNIMOS para un nodo Hypervisor o Managerhype:
• 32 núcleos de CPU
• 64 GB de RAM
21.13.2 Reserva de hardware del host
Los siguientes recursos se reservarán para la máquina host y se restarán de la fila Disponible en Resumen de recursos:
• Hipervisor
• 8 núcleos de CPU
• 16 GB de RAM
• Exageración del gerente
• 16 núcleos de CPU
• 32 GB de RAM
21.13.3 Entrehierro
Si se encuentra en un entorno Airgap, deberá realizar estos pasos antes de aceptar el nuevo nodo de hipervisor en los miembros de SOC Grid:
1. Descargue la imagen de Oracle 9 Qcow2 desde https://download.securityonion.net/file/securityonion/OL9U5_x86_64-kvm-b253.qcow2
2. Coloque OL9U5_x86_64-kvm-b253.qcow2 en /nsm/libvirt/boot/ en su nodo administrador
21.13.4 Agregar un administrador + hipervisor
Los nodos de administrador pueden tener capacidades de hipervisor. Este tipo de nodo se llama managerhype.
Instale un nuevo nodo, seleccione la opción de implementación DISTRIBUIDA, elija Nueva implementación y luego seleccione la opción Managerhype:
- 369/402 - Seguridad Cebolla Soluciones, LLC

21.13.5 Agregar un hipervisor
Una vez que se haya completado la instalación, el nuevo nodo actuará como nodo administrador hasta que se agregue una clave de licencia en SOC. Después de agregar la licencia,
La parte del hipervisor del managerhype tardará aproximadamente 45 minutos en estar lista. Esto se debe a los tres estados altos que se requieren.
para completar la configuración del nodo.
Si se trata de una instalación con espacio de aire, será necesario seguir las instrucciones anteriores antes de agregar la licencia al SOC. El usuario necesitará
ejecute mkdir -p /nsm/libvirt/boot.
Los detalles en Agregar un hipervisor, sobre cuándo el dominio base está listo y se pueden crear máquinas virtuales, se aplican al managerhype
nodo, así como agregar una máquina virtual cebolla de seguridad.
21.13.5 Agregar un hipervisor
Instale un nuevo nodo, seleccione la opción de implementación DISTRIBUIDA, elija Implementación existente y luego seleccione la opción Hipervisor:
El administrador deberá poder conectarse al nodo del hipervisor por su nombre, por lo que necesitará una entrada DNS o podrá agregar manualmente una
entrada en /etc/hosts en el administrador.
- 370/402 - Soluciones de cebolla de seguridad, LLC

21.13.5 Agregar un hipervisor
Una vez que el nuevo nodo del hipervisor haya sido aceptado en la red, vaya a Configuración SOC, haga clic en el menú Opciones, habilite la configuración avanzada,
y luego navegue hasta la configuración del hipervisor. Debería verse así:
Una vez que se haya configurado el dominio base en el hipervisor (permitiendo la creación de máquinas virtuales), debería verse así:
- 371/402 - Seguridad Cebolla Soluciones, LLC

21.13.6 Opciones de almacenamiento de VM para /nsm
21.13.6 Opciones de almacenamiento de VM para /nsm
La gran mayoría de los datos, para todos los tipos de nodos, se almacenan en /nsm/. Para una máquina virtual, hay tres opciones disponibles para el almacenamiento /nsm.
21.14. Directorio bajo /
Esta opción utiliza una estructura de directorios simple dentro del sistema de archivos raíz. Esta es la opción predeterminada si ni el disco pasa ni el disco virtual.
están seleccionados. La imagen predeterminada utilizada para las máquinas virtuales es de 220 GB, por lo que quedan aproximadamente 200 GB para almacenamiento en una máquina virtual nueva.
21.15. paso del disco
Este método pasa un disco físico directamente a la VM, proporcionando un disco dedicado al nodo. Proporciona un rendimiento de disco casi nativo y es
ideal para entornos de producción con requisitos de alto rendimiento.
21.16. disco virtual
Se crea un disco virtual según el tamaño especificado por el usuario en la configuración de SOC Grid y el espacio se asigna previamente en el
hipervisor. El archivo de imagen del disco no se elimina cuando se elimina la VM. Un usuario puede decidir dejar estos datos por un tiempo o eliminarlos.
manualmente desde el hipervisor donde está almacenado en /nsm/libvirt/volumes.
Nota
Si un usuario selecciona un paso de disco y asigna un tamaño para el disco virtual, entonces el paso de disco se utilizará para /nsm y el disco virtual.
El disco será ignorado.
- 372/402 - Seguridad Cebolla Soluciones, LLC

21.16.1 Agregar una máquina virtual cebolla de seguridad
21.16.1 Agregar una máquina virtual cebolla de seguridad
Tenga en cuenta que el hardware de una máquina virtual no se puede modificar una vez que se crea la máquina virtual.
Para crear una nueva VM, haga clic en el signo más. Deberías ver un formulario como este. Si utiliza DHCP, preste especial atención a las notas de DHCP:
Complete el formulario y luego haga clic en la marca verde para guardar y crear la VM:
- 373/402 - Seguridad Cebolla Soluciones, LLC

21.16.1 Agregar una máquina virtual cebolla de seguridad
Una vez que se crea la VM y se inicia el primer estado alto, debería verse así:
- 374/402 - Seguridad Cebolla Soluciones, LLC

21.16.2 Estado de creación de VM
21.16.2 Estado de creación de VM
Después de que un usuario haya creado una máquina virtual completando el formulario y haciendo clic en la marca de verificación verde, el navegador web se puede actualizar periódicamente para
verifique el estado de la creación de la VM. Esto se muestra en la columna de estado de la captura de pantalla anterior que muestra el estado alto iniciado.
Procesando Detectamos que el usuario ha solicitado crear una VM.
Disco NSM del hipervisor lleno Si el usuario solicitó un disco virtual para /nsm y no hay suficiente espacio en /nsm del hipervisor, entonces aparece este error
será visto. El usuario debe eliminar esta máquina virtual de la configuración de SOC Grid y liberar espacio en el hipervisor o crear una nueva máquina virtual.
con un /nsm más pequeño.
Configuración de IP Estática o DHCP se está configurando dentro de la imagen de VM antes de la creación.
Iniciando Crear El hipervisor ha clonado la imagen base y ha creado la nueva imagen de VM.
Ejecutando el script de implementación. La máquina virtual se está aprovisionando y el salt-minion se está iniciando.
Inicializar los pilares de Minion La VM le ha dicho al administrador de Security Onion que cree sus pilares de Minion.
Instancia creada El proceso de creación de VM está completo.
Creación de volumen Si el usuario elige un disco virtual para /nsm, este proceso lo crea y asigna completamente el espacio en el hipervisor. esto
El paso puede tardar un poco dependiendo del tamaño de /nsm que se solicitó.
Configuración del volumen El disco se está asignando a la VM.
Configuración de hardware El hardware solicitado se ha asignado a la VM.
Highstate Initiated La máquina virtual se inició y el primer Highstate se está ejecutando actualmente. Los estados altos posteriores no actualizarán el último
Columna actualizada.
- 375/402 - Soluciones de cebolla de seguridad, LLC

21.16.3 Detener o iniciar una VM
Instancia destruida La instancia ha sido destruida. Esta VM se eliminará de la tabla de Máquinas virtuales después de 48 horas.
21.16.3 Detener o iniciar una VM
Si necesita detener o iniciar una VM, puede usar el menú Ejecutar operaciones de energía de VM en la parte inferior del formulario de VM:
Aquí está la lista de operaciones de energía de VM y lo que realmente hacen:
• Reiniciar: reinicia correctamente la VM (virt.reboot)
• Restablecer: restablece forzosamente la VM (virt.reset)
• Apagar: apaga correctamente la VM (virt.shutdown)
• Inicio: inicia la VM (virt.start)
• Detener: detiene forzadamente la VM (virt.stop)
21.16.4 Eliminación de una máquina virtual
Para eliminar una VM, haga clic en el icono de la papelera:
- 376/402 - Seguridad Cebolla Soluciones, LLC

21.16.4 Eliminación de una máquina virtual
Le pedirá confirmación:
- 377/402 - Seguridad Cebolla Soluciones, LLC

21.16.4 Eliminación de una máquina virtual
Una vez que hayas confirmado, mostrará que está pendiente de eliminación:
- 378/402 - Seguridad Cebolla Soluciones, LLC

21.16.4 Eliminación de una máquina virtual
Luego, el backend elimina la VM, libera el hardware utilizado por la VM y actualiza la anotación del hipervisor utilizada por el SOC. este proceso
debería tomar menos de 30 segundos.
Luego deberá actualizar su navegador web para ver que la CPU, la memoria y el hardware libre se han actualizado. La VM eliminada debería entonces
aparecerá como Instancia destruida.
Advertencia
Si elimina una VM e intenta crear inmediatamente una nueva VM antes de que el backend libere el hardware, no podrá aprobar
a través del hardware que fue utilizado previamente por la VM eliminada.
- 379/402 - Soluciones de cebolla de seguridad, LLC

21.17 Informes
21.17 Informes
Los clientes de Security Onion Pro pueden producir informes y exportar datos con fines analíticos. Esto no es una migración de datos ni una exportación completa de datos.
característica, sino que está destinado a que los analistas presenten datos relevantes al equipo más amplio. En consecuencia, las exportaciones están limitadas en la cantidad de
datos que se producirán.
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro para habilitar esta función.
21.17.1 Informes
Los informes se generan en formato de documento portátil (PDF) en segundo plano. Una vez que se solicita un informe, aparecerá un mensaje de confirmación.
Aparece para notificar al usuario que el informe se está generando y estará disponible para descargar en la pantalla Informes.
Hay dos tipos de informes disponibles: estándar y personalizado.
Informes estándar
Los informes estándar son informes prediseñados proporcionados por el equipo de Security Onion.
Un informe de productividad proporciona métricas generales de productividad del equipo. Esto incluye:
• Métricas de eventos ingeridos
• Métricas de alerta (total, reconocida, escalada, por gravedad, etc.)
• Métricas de casos (total, por estado, por asignado, comentarios por usuario, etc.)
• Seguimiento del tiempo (horas totales de casos, horas de casos por usuario)
Los informes de productividad se pueden generar navegando a la interfaz de Informes y haciendo clic en el botón Agregar trabajo cerca de la parte superior de la pantalla. un
Aparecerá una ventana emergente que permitirá al usuario seleccionar el informe de productividad.
Un informe de caso proporciona información detallada sobre un caso específico. Esto incluye:
• ID, título, descripción
• Estado actual, cesionario, etc.
• Horas registradas en el caso
• Todos los comentarios del caso y la fecha y el autor.
• Todas las detecciones involucradas en el caso.
• Todos los archivos adjuntos (excluido el contenido real del archivo)
• Datos observables
• Eventos relacionados
• Historial de auditoría de casos
Los informes de casos se pueden generar abriendo un caso y haciendo clic en el icono Exportar encima del título del caso.
Nota
Los comentarios de los clientes ayudarán al equipo de Security Onion a determinar qué informes adicionales se proporcionarán en futuras versiones. Proporcionar comentarios por
comunicándose con nuestro equipo de soporte.
- 380/402 - Soluciones de cebolla de seguridad, LLC

21.17.1 Informes
Los informes estándar se pueden personalizar ligeramente a través de la pantalla de Configuración. Busque el nombre del informe, como "Informe de caso". Personalizaciones
incluyen cambiar el formato del diseño, el contenido del texto y ocultar o mostrar datos adicionales. La capacidad de mostrar datos adicionales se limita a lo que
el informe integrado ya ha consultado. Por ejemplo, el Informe de caso integrado muestra el TLP de cada observable, pero no el PAP. Así que si tu
Si desea ver el PAP y no el TLP, puede personalizarlo para hacerlo. Recuerde sincronizar la cuadrícula después de guardar las personalizaciones.
Informes personalizados
Si bien los informes estándar se pueden personalizar ligeramente, algunos clientes pueden necesitar más flexibilidad para personalizar los informes. Para ello, Seguridad
Onion Pro ofrece tipos de informes personalizados.
Los informes personalizados se generan navegando a la interfaz de Informes y haciendo clic en el botón Agregar trabajo. La ventana emergente mostrará una lista de disponibles
informes personalizados.
Los clientes pueden crear una cantidad limitada de informes personalizados abriendo la pantalla de Configuración y buscando un informe personalizado. Costumbre
Los informes permiten a los usuarios diseñar su propio diseño de informe y elegir qué datos se consultan y luego se representan en el informe. Personalizando estos
Los informes requieren una comprensión del formato Markdown (https://www.markdownguide.org/) y una comprensión general de la sintaxis OQL. Para
Para obtener mejores resultados, los diseñadores de informes deben crear consultas en la interfaz de Hunt para garantizar que los datos devueltos sean los que desean para su informe. Entonces
el diseñador del informe copiará esa misma consulta OQL en el informe personalizado.
Se proporciona un informe de muestra en la instalación estándar de Security Onion Pro. Aquí está el contenido de este archivo de informe seguido de una breve revisión de
cada sección.
{{- /* query.myDocEvents.Oql = metadatos.tipo: _doc | groupby evento.módulo, evento.conjunto de datos | ordenar por @timestamp desc */ -}}
{{- /* query.myDocEvents.MetricLimit = 10 */ -}}
{{- /* consulta.myDocEvents.EventLimit = 100 */ -}}
Informe personalizado de cebolla de seguridad
=============================
{{ si .Error }}
**NOTA: Este informe encontró un problema al extraer los datos relevantes y es posible que no esté completo.**
**Error:** {{.Error}}
{{ fin }}
Los registros deben haber sido creados o actualizados durante el siguiente período de tiempo para que se reflejen en este informe.
**Fecha de inicio del informe:** {{formatDateTime "Mon Jan 02 15:04:05 -0700 2006" .BeginDate}}
**Fecha de finalización del informe:** {{formatDateTime "Mon Jan 02 15:04:05 -0700 2006" .EndDate}}
## Eventos de documentos de muestra
**Total de eventos:** {{ formatNumber "%d" "en" .Results.myDocEvents.TotalEvents}}
### Recuentos de eventos por módulo y conjunto de datos
| Contar | Proporción | Módulo | Conjunto de datos |
| ----- | ---------- | ------ | ------- |
{{ rango sortMetrics "Valor" "desc" .Results.myDocEvents.Metrics.groupby_0_event_module_event_dataset -}}
| {{ formatNumber "%.0f" "es" .Value}} | {{ formatNumber "%.1f" "es" .Percentage}}% | {{índice .Claves 0}} | {{índice .Claves 1}} |
{{fin}}
### Eventos individuales (Limitado al primer {{.Results.myDocEvents.Criteria.EventLimit}})
| Hora del evento | Módulo | Conjunto de datos | Categoría |
| ---------- | ------ | ------- | -------- |
{{ rango .Resultados.myDocEvents.Events -}}
| {{.Marca de tiempo}} | {{.carga útil.event_module}} | {{.Payload.event_dataset}} | {{.carga útil.event_category}} |
{{fin}}
Comenzando desde arriba: las primeras tres líneas son instrucciones internas para el generador de informes. Le dicen al generador de informes que ejecute la consulta OQL.
tipo.metadatos: _doc | groupby evento.módulo, evento.conjunto de datos | ordenar por @timestamp desc y almacenar los resultados en el
.Variable Results.myDocEvents, para referencia posterior en el informe. El parámetro MetricLimit = 10 limita las métricas de grupo a las 10 primeras
cuenta, y EventLimit = 100 limita los resultados sin procesar del evento a 100 como máximo. Estos son parámetros importantes porque sin ellos
podría terminar con un documento PDF de cientos de páginas, y es poco probable que esa cantidad de datos sea útil al presentar datos relacionados con la seguridad.
hallazgos a otros.
Preste mucha atención a la sintaxis tradicional de la plantilla {{... }}, así como a la sintaxis de instrucciones del informe interno {{- /* ... */ -}}. A
El carácter omitido hará que falle la generación del informe.
- 381/402 - Soluciones de cebolla de seguridad, LLC

21.17.2 Exportaciones tabulares
El siguiente es el título del informe. Observe cómo la longitud total del título va seguida de una serie igualmente larga de caracteres = iguales. Esto denota
que la línea anterior es el título del informe y será el nombre que aparecerá en la lista emergente Agregar trabajo en la interfaz de Informes. Consulte el
Consulte la guía de Markdown anteriormente en esta sección para obtener más ayuda con la definición de títulos, encabezados, secciones y otros estilos dentro de su informe.
documento.
Después del título hay un bloque {{ if .Error }} ... {{ end }}. Esto es útil para presentar errores encontrados durante la renderización del
informe. Si no hay ningún error, esta sección no será visible en el informe final generado.
El siguiente es el contenido del informe en sí. Verá el contenido del texto del informe mezclado con salidas de datos. Por ejemplo, si 12 eventos coincidieron con el OQL
consulta proporcionada en la parte superior de este informe, la línea que contiene **Eventos totales:** se representará como:
Eventos totales: 12
Finalmente, se incluyen dos resultados tabulares. El primero muestra "Recuentos de eventos por módulo y conjunto de datos" y, según la rebaja
formato, se representará en una estructura de tabla que incluye los encabezados de columna "Recuento, proporción, módulo y conjunto de datos". Tenga en cuenta que esos |
Los caracteres se utilizan para separar los datos de la columna. La primera columna generará el valor del primer grupo por métrica (referido como
groupby_0_event_module_event_dataset), que será un valor de "recuento". %.0f le indica a la salida que oculte los valores decimales,
y el en indica que el número se formatee en la configuración regional inglesa (1220 frente a 1,220). La segunda columna mostrará la proporción de
eventos que coincidieron con esta fila del conjunto completo de eventos, la tercera columna mostrará el módulo de evento para esa fila y la última columna
muestra el conjunto de datos del evento para esa fila.
La segunda salida tabular muestra la lista de eventos (hasta 100 como se indicó anteriormente en la parte superior del archivo). Esta no es una métrica, por lo que
No hay ninguna columna de recuento de valores en esta tabla. En cambio, la columna mostrará los valores reales del campo de evento. Observe cómo la primera columna es el evento.
marca de tiempo, que es útil para mostrar listas de eventos ordenadas cronológicamente. Las columnas restantes pueden ser cualquier campo asociado
con ese evento. Utilice Hunt para determinar qué campos están disponibles para esa consulta.
Nota
Personalizar informes puede resultar intimidante para quienes no están familiarizados con este nivel de detalle. Los clientes profesionales con horas de servicio profesionales pueden utilizar
La experiencia del equipo de soporte de Security Onion para ayudarlo a comenzar.
Recuerde sincronizar la cuadrícula después de guardar los informes personalizados.
21.17.2 Exportaciones tabulares
También se incluye con esta característica la capacidad de exportar datos desde varias de las pantallas SOC, que incluyen:
• Alertas
• Paneles de control
• Cazar
• Casos (listado)
• Detecciones (listado)
Los datos exportados se guardarán en un archivo CSV e incluirán los encabezados como la primera línea del CSV. El CSV se generará en segundo plano.
y luego estará disponible para descargar en la interfaz de Informes.
Los datos de grupos y eventos se pueden exportar haciendo clic en el ícono de exportación de datos, que generalmente se encuentra en la esquina superior izquierda de la tabla de métricas del grupo o
gráfico o la tabla de eventos. Aunque el icono de exportación esté visible en el modo gráfico de una métrica de grupo, seguirá exportando los datos subyacentes en CSV.
formato. No intenta exportar la visualización del gráfico. Sin embargo, los usuarios pueden utilizar la función Imprimir del navegador para enviar esos gráficos.
visualizaciones y paneles a una impresora o archivo PDF.
Las exportaciones CSV exportarán todos los datos subyacentes, hasta un máximo configurado. Por lo tanto, si bien la interfaz de Dashboards podría mostrar 10 entradas en un
Métrica de grupo debido a cómo se establecen los límites del grupo, el CSV podría contener más de 10, si los datos de respaldo tienen más agregados
métricas disponibles.
- 382/402 - Seguridad Cebolla Soluciones, LLC

21.17.3 Referencia de personalización de informes
Advertencia
Exportar datos CSV en el modo de tiempo relativo, como 24 horas, a menudo resultará en datos CSV exportados que son diferentes de los que están en el
pantalla en el momento en que se inició la exportación. Esto se debe a que la exportación vuelve a ejecutar la misma consulta, utilizando el mismo tiempo relativo pero
comenzando en el momento de la exportación, en comparación con cuando se consultó el panel anteriormente. Para exportar primero los datos idénticos que se muestran en la interfaz SOC
cambie el rango de tiempo al modo absoluto y defina las horas de inicio y finalización antes de actualizar los resultados y hacer clic en el icono de exportación.
Las exportaciones CSV están limitadas a 10.000 registros de forma predeterminada.
Nota
Esta función de exportación CSV no está diseñada para fines de migración de datos de Elasticsearch.
21.17.3 Referencia de personalización de informes
Instrucciones de renderizado en PDF
• Generar una tabla de contenidos al comienzo del informe exportado:
{{- /* pdf_param: -generate-toc */ -}}
• Deshabilite la verificación TLS cuando solicite extraer imágenes externas para incluirlas en el informe:
{{- /* pdf_param: -insecure */ -}}
• Agregue un salto de página cada vez que encuentre una etiqueta de regla horizontal (HR) en el informe, como ---:
{{- /* pdf_param: -nueva-página-en-hr */ -}}
• Cambie el diseño de salida del informe de vertical (predeterminado) a horizontal:
{{- /* pdf_param: -orientación */ -}}
{{- /* pdf_param: paisaje */ -}}
Instrucciones de consulta OQL
• Definir una nueva consulta OQL que filtre por algún.campo y otro.campo, e incluya una única métrica agregada de recuentos por ambos.
event.modules y event.dataset con un límite máximo de no más de 10 agregaciones por grupo y no más de 25 eventos en total
registros devueltos:
{{- /* query.mySpecialQuery.Oql = algún.campo: 123 Y otro.campo: "Jason" | groupby evento.módulo, evento.conjunto de datos */ -}}
{{- /* consulta.mySpecialQuery.MetricLimit = 10 */ -}}
{{- /* consulta.mySpecialQuery.EventLimit = 25 */ -}}
Acceder a los resultados de la consulta
• Recorrer los resultados del evento de una consulta. Tenga en cuenta que todos los campos que contienen un punto tendrán sus puntos reemplazados con un guión bajo para evitar
chocando con la sintaxis de la plantilla:
- 383/402 - Seguridad Cebolla Soluciones, LLC

21.17.3 Referencia de personalización de informes
{{ rango .Resultados.miConsultaEspecial.Eventos -}}
{{.Marca de tiempo}} | {{.some_field}} | {{ .otro_campo }}
{{ fin }}
• Recorrer los resultados de agregación de una consulta. Tenga en cuenta que las agregaciones tienen campos especiales disponibles:
• .Value La agregación calculada, normalmente un recuento sumado.
• .Porcentaje La proporción calculada * 100 de las ocurrencias de este grupo en comparación con el número total de grupos para esta agregación.
• .Keys[#index] Donde está el índice basado en 0 de los campos groupby. En este ejemplo, .Keys 0 será el valor event.module y
.Keys 1 será el valor event.dataset para este grupo.
{{ rango sortMetrics "Valor" "desc" .Results.mySpecialQuery.Metrics.groupby_0_event_module_event_dataset -}}
{{ formatNumber "%.0f" "es" .Value }} | {{ formatNumber "%.1f" "es" .Percentage }}% | {{ índice .Claves 0 }} | {{ índice .Claves 1 }} |
{{ fin }}
Si hubiera habido una segunda cláusula groupby, se habría hecho referencia a ella como groupby_1_fieldx.
Formateadores
• Formatee una fecha y hora en un formato específico de lunes 02 de enero 15:04:05 -0700 2006. Siempre reutilice la misma fecha y hora como se muestra a continuación.
para la plantilla de formato:
{{ formatDateTime "lunes 02 de enero 15:04:05 -0700 2006" .SomeDataField }}
• Formatee un valor numérico a una salida entera, decimal, etc., siguiendo la configuración regional dada, en este caso inglés:
{{ formatNumber "%.2f" "es" .SomeNumericField }}
Clasificadores
• Ordene las métricas proporcionadas por el campo .Value en orden descendente:
{{ range sortMetrics .Value "desc" .Results.mySpecialQuery.Metrics.groupby_1_fieldx }}
• Ordene los datos del caso dado por el campo .CreateTime (o marca de tiempo del evento) en orden ascendente (aplicable al Informe de caso):
{{ rango sortComments .CreateTime "asc" .Comments }}
{{ rango sortDetections .CreateTime "asc" .Detections }}
{{ rango sortArtifacts .CreateTime "asc" .Attachments }}
{{ rango sortArtifacts .CreateTime "asc" .Observables }}
{{ rango sortRelatedEvents "fields:soc_timestamp" "asc" .RelatedEvents }}
{{ rango sortHistory .CreateTime "asc" .History }}
Filtros
• Convertir el ID de usuario proporcionado en la dirección de correo electrónico del usuario. Se aplica a cualquier campo de evento de ID de usuario válido o campo de métrica indexada:
{{ .Algún campo | getUserDetail "correo electrónico" }}
• Convertir el valor a mayúsculas:
{{ .Algún campo | superior }}
• Convertir el valor a minúsculas:
{{ .Algún campo | inferior }}
• Unir un valor de matriz en una cadena, separado por comas:
{{ .Algún campo | unirse "," }}
- 384/402 - Seguridad Cebolla Soluciones, LLC

21.18 IA de cebolla
21.18 IA de cebolla
Nota
Esta es una característica de nivel empresarial de Security Onion. Comuníquese con Security Onion Solutions, LLC a través de nuestro sitio web en https://securityonion.com/pro para
más información sobre la compra de una licencia de Security Onion Pro.
Nota
La IA de cebolla está desactivada de forma predeterminada. Para habilitarlo para su implementación de Security Onion Pro, vaya a la página Administración --> Configuración y navegue
a soc --> configuración --> servidor --> cliente --> asistente --> habilitado.
Onion AI Assistant es su asistente personal de IA diseñado para ayudarlo con una variedad de tareas y brindarle información a pedido. nosotros
Admite el acceso a LLM de una variedad de fuentes. Se han puesto a disposición varias herramientas a medida que interactúa con el asistente para que pueda acceder
información y recursos actualizados.
21.18.1 Adaptadores
Hay una variedad de adaptadores disponibles para conectarse a diferentes proveedores de LLM. Al configurar un adaptador, le está indicando a SOC cómo
conectarse a un proveedor de LLM. Usted configura los modelos por separado en Modelos disponibles y le indica a cada modelo qué adaptador usar. Esto permite
le permite conectarse a varios proveedores al mismo tiempo y elegir qué modelos desea utilizar de cada proveedor. Los adaptadores disponibles
son:
• SOAI: El adaptador Security Onion AI se conecta a nuestra propia puerta de enlace alojada y proporciona acceso a una variedad de modelos. Este es el valor predeterminado
adaptador y está alojado en la nube con una cantidad asignada de créditos por grid con licencia de Security Onion Pro.
• Gemini: se puede acceder a los modelos Gemini de Google a través de este adaptador. Puede conectarse a través de la API de desarrollador de Gemini o a través de
API de vértice. Estos modelos están alojados en la nube de Google y requieren el uso de su propia clave de Google Cloud o clave API de Gemini.
• OpenAI Responses: este adaptador puede conectarse a las API más recientes compatibles con OpenAI que admiten el protocolo Responses. Este adaptador
permite que las redes de Security Onion se conecten a LLM alojados localmente.
• OpenAI Chat: este adaptador puede conectarse a cualquier API compatible con OpenAI Chat, un protocolo más antiguo que aún admiten muchos proveedores de IA. esto
El adaptador permite que las redes Security Onion se conecten a LLM alojados localmente.
La mayoría de las funciones son compatibles con todos los adaptadores, pero las capacidades pueden cambiar según el modelo o proveedor al que se conecte. Los créditos son
exclusivo de SOAI, es el único adaptador que responde con un saldo acreedor. Se pueden configurar varios adaptadores al mismo tiempo.
Configuración
Una nueva instalación vendrá con el adaptador SOAI preconfigurado y listo para usar. Para conectarse a otros proveedores o modificar el adaptador SOAI, vaya
Vaya a Administración --> página Configuración, asegúrese de que "Mostrar configuración avanzada" esté activado en las Opciones en la parte superior de la página y verifique en
soc --> configuración --> servidor --> módulos --> asistente --> adaptadores. Aquí puedes agregar tantos adaptadores como necesites. Cada adaptador define cómo
conectarse a un proveedor. Diferentes adaptadores tienen diferentes requisitos de configuración. Cada adaptador necesita un nombre único, el protocolo que utiliza,
y un tiempo de espera de salud medido en segundos. A continuación se muestra una tabla con los campos necesarios para cada adaptador:
Nombre del adaptador Protocolo URL de API Clave de API Cuenta de servicio Cuenta de servicio JSON Ubicación Estado Tiempo de espera Segundos
SOAI R R R -- -- -- R
Géminis R R -- O O O R
Respuestas de OpenAI R R R O -- -- R
Chat OpenAI R R R O -- -- R
R = Requerido, O = Opcional, -- = No utilizado
- 385/402 - Seguridad Cebolla Soluciones, LLC

21.18.1 Adaptadores
SOAI
Este adaptador no debería requerir ninguna configuración, aparte de la URL de API, que será diferente para los clientes de Security Onion Pro ubicados en
diferentes regiones. Para cambiar la URL de la API SOAI, vaya a la página Administración --> Configuración y navegue hasta soc --> config --> servidor -->
módulos --> asistente --> adaptadores. Seleccione el adaptador SOAI y actualice el campo URL de API. Si su licencia está configurada para usar una nube alternativa
región, la URL API correcta se incluirá con su clave de licencia de Security Onion. Si no se especifica una URL alternativa, utilice la URL de API predeterminada.
Cualquier campo proporcionado adicionalmente se ignora. Generalmente se debe configurar como máximo una instancia de este adaptador a la vez.
CRÉDITOS
El uso de modelos sobre el adaptador SOAI consumirá créditos de su licencia Security Onion Pro. Los créditos solo son aplicables a la SOAI
adaptador. Si utiliza un modelo local u otro proveedor externo (como Gemini u OpenAI), los créditos SOAI no se consumen.
La licencia Security Onion Pro incluye una cantidad inicial de créditos para comenzar. Para una planificación de uso a largo plazo, comuníquese con su Security Onion
representante de cuenta. Ayudarán a estimar las tasas de uso de crédito, así como al aprovisionamiento de créditos adicionales. Los créditos son
consumido en función de la cantidad de tokens utilizados en la conversación, incluida la entrada del usuario, la salida del asistente y el uso de herramientas. de su organización
El saldo se puede ver en la parte superior derecha de la página del asistente o en la página de administración en Administración --> Métricas de IA.
Géminis
Security Onion admite la conexión a los modelos Gemini de Google a través de Gemini Developer API o Vertex API.
Para conectarse a través de la API para desarrolladores de Gemini, deberá generar una clave API en Google Cloud Console o Google AI Studio y proporcionar
en el campo Clave API. Para conectarse a través de Vertex API, deberá crear una cuenta de servicio con los permisos adecuados para el
modelos a los que desea acceder, genere una clave JSON para esa cuenta, pegue el JSON en el campo JSON de la cuenta de servicio y deberá
También especifique la ubicación de la cuenta de servicio. Es posible que algunos modelos Gemini solo estén disponibles en determinadas ubicaciones, como en todo el mundo. El campo URL de API
no se utiliza para conexiones Gemini.
Si se proporcionan una clave API y una cuenta de servicio JSON + ubicación de la cuenta de servicio, SOC intentará conectarse utilizando el servicio.
Se ignorarán la cuenta y la clave API.
Este adaptador no utilizará ningún crédito de su licencia de Security Onion Pro, pero Google le cobrará según su precio. Cebolla de seguridad
Solutions, LLC no brinda soporte para Google Gemini, aparte de ayudar con la configuración del adaptador al que se hace referencia en esta página.
Respuestas de OpenAI
El adaptador OpenAI Responses puede conectarse a las API compatibles con OpenAI más nuevas que admiten el protocolo Responses. Para conectarse, deberá
Es necesario proporcionar una URL de API. La URL de API debe ser la URL base del proveedor al que se está conectando, por ejemplo https://api.openai.com/
v1/. Es posible que se requiera o no una clave API según el proveedor al que se conecte. Si no está seguro de si su proveedor admite el
Protocolo de respuestas, consulte con su soporte o intente conectarse con este adaptador. Si no funciona, puedes probar el adaptador OpenAI Chat que
admite un protocolo más antiguo que todavía se utiliza ampliamente.
consejo
Algunos proveedores requieren que los parámetros de URL se pasen junto con las llamadas a la API. Por ejemplo, Azure requiere un parámetro de versión de API. para apoyar
Esto, a partir de Security Onion 3.1.0, puede agregar los parámetros al campo URL de API. Por ejemplo:
https://api.someprovider.invalid/v1/?api-version=2024-08-01-preview
Chat abierto de IA
El adaptador OpenAI Chat puede conectarse a cualquier API compatible con OpenAI que admita el protocolo Chat. Para conectarse, deberá proporcionar un
URL de API. La URL de API debe ser la URL base del proveedor al que se está conectando, por ejemplo https://api.openai.com/v1/. Una clave API
Puede ser necesario o no según el proveedor al que se conecte.
- 386/402 - Seguridad Cebolla Soluciones, LLC

21.18.2 Modelos disponibles
consejo
Algunos proveedores requieren que los parámetros de URL se pasen junto con las llamadas a la API. Para respaldar esto, a partir de Security Onion 3.1.0, puede agregar el
parámetros al campo URL de API. Por ejemplo:
https://api.someprovider.invalid/v1/?api-version=2024-08-01-preview
21.18.2 Modelos disponibles
Para controlar qué modelos están disponibles dentro del SOC, se deben configurar modelos individuales. Para configurar un modelo, vaya a la
Administración --> Página de configuración, asegúrese de que "Mostrar configuración avanzada" esté activado en las Opciones en la parte superior de la página y verifique en
soc --> configuración --> servidor --> cliente --> asistente --> modelos disponibles. Aquí podrás añadir tantos modelos como necesites. Cada modelo necesita un
nombre único, el adaptador que utiliza y un identificador de modelo que le indica al adaptador a qué modelo conectarse en el proveedor.
Nota
Si un proveedor ofrece modelos que no figuran en los modelos disponibles, no se podrá acceder a ellos dentro del SOC.
21.18.3 Consideraciones del modelo local
Security Onion ahora admite modelos locales a través de cualquier punto final compatible con OpenAI. Debido a que el asistente se basa en grandes ventanas contextuales,
La longitud de contexto mínima recomendada es de 128 000 tokens. Se han probado los siguientes modelos de código abierto con OnionAI:
• GPT OSS 120B -- (EE.UU.) Inferencia rápida pero limitada a una ventana de contexto de 128k. La precisión es justa.
• Kimi 2.5 -- (China) Un modelo capaz con precisión promedio y una ventana de contexto de 256k suficiente para la mayoría de las tareas. Tenga en cuenta que este modelo
Requiere una cantidad significativa de VRAM para mantener el rendimiento.
• GLM 5 -- (China) Precisión promedio con una ventana de contexto de 200k.
• Qwen 3.5 -- (China) Precisión promedio con una ventana de contexto de 200k.
Nota
Los modelos locales no igualarán el rendimiento de los modelos fundamentales propietarios, como los de Anthropic, Google u OpenAI.
21.18.4 Alojamiento de modelos locales
Alojar sus propios modelos requiere hardware potente y costoso. Para principiantes recomendamos utilizar una herramienta como LM Studio. tu
Necesita al menos 96 GB de VRAM para alojar sus propios modelos localmente. La velocidad y precisión de OnionAI cuando se aloja localmente se basa en la
hardware que está utilizando. Para obtener resultados más precisos, recomendamos utilizar créditos con OnionAI.
- 387/402 - Seguridad Cebolla Soluciones, LLC

21.18.5 Herramientas disponibles
21.18.5 Herramientas disponibles
Actualmente el asistente se ejecuta en la nube. Para referenciar información local, SOC pone a disposición del asistente las siguientes herramientas:
• query_events: esta herramienta de solo lectura permite al asistente consultar eventos de seguridad desde su instancia local de Security Onion de forma similar a como usted
Usaría la página de caza.
• query_cases: esta herramienta le permite al asistente consultar casos desde su instancia local de Security Onion de manera similar a cómo usaría Casos.
página.
• query_detections: esta herramienta permite al asistente consultar detecciones desde su instancia local de Security Onion de forma similar a cómo usaría
la página Detecciones.
• get_playbooks: cuando el asistente usa esta herramienta de solo lectura, SOC recopilará los libros de jugadas, ejecutará sus consultas y devolverá todos los datos.
listo para el análisis. Esta herramienta es de sólo lectura.
• ack_alerts: el asistente puede utilizar esta herramienta para consultar y reconocer alertas en su instancia local de Security Onion.
• escalate_alerts: similar a la herramienta de confirmación, esta herramienta permite al asistente consultar alertas y escalarlas a un nuevo caso.
• create_detection: el asistente utilizará esta herramienta para crear nuevas detecciones en su instancia local de Security Onion.
• add_overrides: esta herramienta permite al asistente ajustar las detecciones existentes agregándoles anulaciones.
• toggle_detections: el asistente puede usar esta herramienta para habilitar o deshabilitar detecciones existentes en su instancia local de Security Onion.
• update_detection_content: si una detección necesita actualizar su contenido, el asistente puede usar esta herramienta para actualizar el contenido y mantener el
mismos metadatos, anulaciones y estado habilitado.
• update_overrides: esta herramienta permite al asistente actualizar las anulaciones existentes para las detecciones.
Permisos
Cuando el asistente solicite cualquiera de estas herramientas, se le pedirá al usuario que apruebe o rechace el uso. La aprobación hará que la herramienta se ejecute y
el resultado entró en la conversación seguido de una respuesta de la IA. El rechazo notificará al asistente y le permitirá responder.
Aprobar automáticamente herramientas de solo lectura
El asistente puede utilizar las siguientes herramientas de solo lectura sin requerir la aprobación explícita del usuario:
• eventos_consulta
• casos_consulta
• consultas_detecciones
• get_playbooks
De forma predeterminada, se debe otorgar permiso para cada solicitud de herramienta. Sin embargo, los usuarios pueden habilitar la aprobación automática para herramientas de solo lectura alternando el
control deslizante en el menú desplegable Opciones en la parte superior de la página del asistente. Con la opción habilitada, las herramientas de sólo lectura se aprobarán automáticamente, mientras que las herramientas que
modificar datos seguirá solicitando la aprobación explícita del usuario.
Nota
Los datos de la conversación se almacenan localmente y no se utilizan para entrenar ningún modelo. Sin embargo, tenga cuidado al compartir información confidencial o personal durante
sus interacciones, ya que otras personas de su organización pueden tener acceso al historial de conversaciones.
21.18.6 Personalización del mensaje del sistema
El mensaje del sistema establece el comportamiento y el contexto del asistente de IA. Los usuarios pueden personalizar este mensaje para adaptar las respuestas del asistente a
sus necesidades específicas, como describir recursos de red, entornos o flujos de trabajo. El mensaje se incluye en cada sesión y puede ser
modificado en cualquier momento en la página Administración --> Configuración en SOC --> config --> servidor --> módulos --> asistente -->
systemPromptAddendum.
- 388/402 - Seguridad Cebolla Soluciones, LLC

21.18.7 Métricas
El anexo del mensaje del sistema se agregará después del mensaje del sistema predeterminado de Security Onion.
Nota
Tenga cuidado al personalizar el mensaje del sistema, ya que puede influir significativamente en el comportamiento y las respuestas del asistente. Un aviso más largo
También use más créditos.
21.18.7 Métricas
Los superusuarios pueden revisar el uso de tokens y el historial de conversaciones de todos los usuarios yendo a Administración --> Métricas de IA. Esta página proporciona el uso.
estadísticas para un rango de fechas determinado. La página comienza con una tabla de uso por usuario. Al hacer clic en el icono de binoculares de un usuario en el lado derecho,
muestra cualquier sesión con la que el usuario interactuó durante el rango de fechas seleccionado, incluso las sesiones eliminadas. Al hacer clic en el icono de binoculares de una sesión,
mostrar la conversación completa. Los administradores pueden ajustar quién tiene permisos a través de roles RBAC.
Para proporcionar un historial preciso, las sesiones eliminadas se conservan en la página de métricas incluso después de que el usuario las elimine.
- 389/402 - Seguridad Cebolla Soluciones, LLC

22. Telemetría
22. Telemetría
22.1 Telemetría SOC
Opcionalmente, SOC puede enviar datos de telemetría a Google Analytics. Esta telemetría ayuda al equipo de desarrollo de Security Onion a mejorar el producto.
Específicamente, al saber qué características de la interfaz de usuario se están utilizando y cómo interactúa el usuario con la interfaz de usuario SOC, el
El equipo de desarrollo puede priorizar mejor las nuevas funciones, las mejoras en la interfaz de usuario existente y comenzar a desaprobar funciones que ya no están disponibles.
raramente usado. Desaprobar funciones no utilizadas ayudará a los desarrolladores a evitar perder tiempo y esfuerzo manteniendo y actualizando áreas del
producto que no se usa mucho. Esto permite dedicar más tiempo a nuevas funciones y corrección de errores, lo que beneficia directamente a los usuarios de Security Onion.
22.1.1 Configuración
Durante la configuración, o durante las invocaciones de sopa no automatizadas, el usuario debe elegir habilitar o deshabilitar la recopilación de telemetría SOC.
Después de la instalación, los administradores de Grid pueden habilitar o deshabilitar la telemetría SOC a través de la interfaz de configuración. Busque telemetría SOC en el
Pantalla de configuración.
Después de cambiar la configuración de telemetría SOC, se debe resincronizar la red. Esto sucede automáticamente una vez cada 15
minutos, o manualmente si el administrador de la red hace clic en la opción Sincronizar cuadrícula, en la parte superior de la pantalla de Configuración. Sincronización de red
Puede tardar varios minutos en completarse.
Además, el navegador almacenará en caché la configuración anterior. Por lo tanto, para asegurarse de que el navegador esté utilizando el nuevo valor de configuración, asegúrese de
Se completa la sincronización de grid y luego realiza una actualización completa del navegador en la interfaz de usuario de SOC. Esto se puede realizar mediante CTRL+MAYÚS+R o
CMD+MAYÚS+R.
22.1.2 Datos incluidos
El objetivo principal de la recopilación de datos de telemetría SOC es comprender qué funciones se utilizan en SOC. En concreto, los datos que se
recopilados se relacionan con los flujos de navegación de la interfaz de usuario. Datos de contexto adicionales, como la versión del software, la ruta de la página vista, etc.
también puede incluirse.
Los datos específicos de la cuadrícula se excluyen intencionalmente de la recopilación de datos, siempre que sea posible.
Debido a la naturaleza de cómo funcionan las solicitudes web de Internet, la dirección IP de origen y la información del Agente de usuario del navegador web, así como
La información del referente del host se conoce en el momento de la recopilación de datos.
Consulte la sección Período de retención a continuación para obtener más información sobre cuánto tiempo se conservan estos datos.
22.1.3 Parámetros de la red
Los datos de telemetría SOC se originan en el navegador SOC que se ejecuta en la estación de trabajo del analista. Los dominios a los que se accede desde el SOC
navegador son:
• www.googletagmanager.com
• www.google-analytics.com
Los datos de telemetría se envían mediante cifrado TLS.
22.1.4 Período de retención
Los datos almacenados en Google Analytics están configurados para eliminarse automáticamente después de dos meses. Este es el intervalo más corto que Google
La analítica proporciona.
- 390/402 - Soluciones de cebolla de seguridad, LLC

22.2 Telemetría de actualizaciones del sistema operativo
22.2 Telemetría de actualizaciones del sistema operativo
Security Onion comprueba periódicamente si hay actualizaciones de paquetes para garantizar que el sistema operativo (SO) y las aplicaciones relacionadas se mantengan parcheados y
actualizado. Estas actualizaciones son fundamentales para proteger el sistema operativo y los paquetes instalados de vulnerabilidades expuestas recientemente. Esto es diferente de
Actualizaciones del producto Security Onion a través de sopa, que se invoca manualmente. Cuando comienzan las actualizaciones del paquete del sistema operativo, la solicitud a Security Onion
Los servidores de repositorio pueden incluir un conjunto limitado de datos de telemetría.
22.2.1 Configuración
Las actualizaciones automáticas de paquetes se pueden habilitar o deshabilitar a través de la interfaz de configuración. Busque el parche en la pantalla de Configuración.
Después de cambiar esta configuración, se debe resincronizar la red. Esto sucede automáticamente una vez cada 15 minutos, o manualmente si
el administrador de grid hace clic en la opción Sincronizar grid, en la parte superior de la pantalla de Configuración. La sincronización de la red puede tardar varios
minutos para completar.
22.2.2 Datos incluidos
El objetivo principal de los datos de telemetría incluidos es comprender qué versiones de Security Onion están implementadas y en qué plataformas.
Esta información ayuda al equipo de desarrollo de Security Onion a determinar cómo priorizar el soporte para versiones anteriores y si hay
justificación para comenzar a probar o detener las pruebas en varios sistemas operativos y arquitecturas.
Se pueden incluir datos adicionales para proporcionar al equipo de desarrollo información sobre qué funciones se han habilitado. Estos datos pueden
cambian de una versión a otra, ya que a menudo se relaciona con nuevos trabajos de desarrollo.
Además, los grids con claves de licencia instaladas incluirán el identificador de la clave de licencia. Los grids que utilizan la licencia estándar no aprovisionada no tienen una
identificador de clave de licencia.
Debido a la naturaleza de cómo funcionan las solicitudes web de Internet, la dirección IP de origen y la información del Agente de usuario del navegador web, así como
La información del referente del host se conoce en el momento de la recopilación de datos.
22.2.3 Parámetros de la red
Los datos de telemetría de actualizaciones del sistema operativo se originan en el nodo administrador. Los dominios a los que se accede desde el nodo administrador son:
• sigs.securityonion.net
• repositorio.securityonion.net
• repositorio-alt.securityonion.net
Los datos de telemetría se envían mediante cifrado TLS.
22.3 Entrehierro
Las redes instaladas dentro de entornos con espacio de aire desactivarán automáticamente la telemetría. En este escenario, la configuración de telemetría SOC
no tendrá ningún efecto y las actualizaciones automáticas de paquetes se desactivarán. Consulte la sección Airgap para obtener más información sobre entornos.
desconectado de internet.
Nota
Si una red se cambia de espacio aéreo a sin espacio aéreo, y si un administrador no desactiva explícitamente la telemetría SOC en la red, la aplicación SOC
ejecutarse en el navegador enviará telemetría.
- 391/402 - Soluciones de cebolla de seguridad, LLC

23. Seguridad
23. Seguridad
23.1 Divulgación de vulnerabilidad
Si tiene alguna inquietud de seguridad con respecto a Security Onion o cree que ha descubierto una vulnerabilidad, envíe un correo electrónico a
security@securityonion.net según las siguientes pautas:
• Incluir una descripción del problema y los pasos para reproducirlo.
• Utilice formato de texto sin formato en el correo electrónico (no documentos de Word ni archivos PDF)
NO lo divulgue públicamente hasta que hayamos tenido tiempo suficiente para resolver el problema.
Nota
Esta dirección de seguridad debe usarse solo para vulnerabilidades no reveladas. Tratar problemas solucionados o preguntas generales sobre cómo utilizar la seguridad
La cebolla debe gestionarse a través de los canales de soporte habituales.
23.2 Pedir recompensas
No participamos en "recompensas de mendicidad":
https://www.troyhunt.com/beg-bounties/
23.3 Integridad del producto y de la cadena de suministro
Security Onion se basa en software gratuito y abierto. Los componentes de terceros, así como el software que desarrolla el equipo de Security Onion, son
construido a partir de código fuente que está disponible para que el público lo revise. Los contribuyentes de la comunidad, o cualquier persona, pueden solicitar tener
Se les envían notificaciones cuando se acepta un cambio en los repositorios públicos. Esto es muy diferente del software de código cerrado ya que
esas bases de código fuente cerradas sólo son visibles para un grupo muy pequeño de desarrolladores. Además, si una base de código fuente cerrada no tiene
procedimientos formales de revisión de código implementados, o falta de infraestructura alrededor de la base del código para que otros estén al tanto de los nuevos cambios, esto aún más
restringe la visibilidad y revisión de los cambios. Estas deficiencias permiten a los atacantes que obtienen acceso no autorizado a una base de código fuente cerrada
realizar cambios sin que otros lo detecten.
Cuando los componentes de terceros se actualizan en Security Onion, el cambio requiere múltiples comprobaciones antes de que pueda fusionarse en el
rama maestra (liberada). Primero, todas las confirmaciones deben firmarse mediante criptografía antes de que se les permita ingresar a la rama maestra. Segundo, código
Se requieren revisiones y aprobaciones de varios miembros del equipo antes de que se puedan fusionar las solicitudes de extracción. Ambas restricciones son
aplicado por el propio repositorio de código fuente, lo que elimina el riesgo de un error humano que permita omitir el proceso. Además,
Los cambios en los repositorios de código fuente de Security Onion hacen que también se envíen notificaciones al equipo de desarrollo de Security Onion.
como cualquier persona del público que opte por ser notificada de dichos cambios. Además de esto, se requiere que los desarrolladores de Security Onion (impuestos por la
repositorio en sí) para utilizar la autenticación multifactor para aprobar cambios.
Además, la infraestructura de compilación de Security Onion ejecuta pruebas a nivel de unidad y pruebas de extremo a extremo totalmente automatizadas en cada versión, para garantizar
La plataforma Security Onion y sus componentes continúan funcionando como se esperaba. Cuando un cambio se fusiona en Security Onion, ya sea
para actualizar un componente ascendente o una modificación del código fuente mantenido por los desarrolladores de Security Onion, lo que rompe el
pruebas automatizadas, somos notificados y tomamos medidas para revisar la falla y la causa raíz. A menudo, esto resulta en que nuestros desarrolladores persigan
El código ascendente se compromete a descubrir por qué algo cambió y si fue intencionado o no. Afortunadamente, estas investigaciones suelen ser errores
relacionado, en lugar de malicioso, y nuestro equipo contribuirá con una solicitud de extracción para solucionar el proyecto inicial o presentará un problema para crear conciencia.
a los mantenedores del proyecto.
No hay garantía de que cualquier software, de código abierto o cerrado, esté siempre libre de ataques. Sin embargo, nuestro compromiso con el software abierto,
y nuestras inversiones en procesos repetibles y tecnologías de prueba y automatización de software mejoran la postura de Security Onion cuando
Se trata de proteger el producto y su base de usuarios.
- 392/402 - Soluciones de cebolla de seguridad, LLC

23.3 Integridad del producto y de la cadena de suministro
- 393/402 - Soluciones de cebolla de seguridad, LLC

24. Lista de materiales del software
24. Lista de materiales del software
La siguiente tabla enumera los principales proyectos de software integrados en la versión actual de Security Onion.
- 394/402 - Seguridad Cebolla Soluciones, LLC

24. Lista de materiales del software
Producto Versión Autor Proyecto URL Licencia Descripción
Alpine Linux 3.23.3 Equipo de desarrollo de Alpine Linux https://alpinelinux.org/ GNU GPL Versión 3 Alpine Linux está orientado a la seguridad,
distribución ligera de Linux
basado en musl libc y ocupadobox.
ATT&CK Navigator 5.3.0 MITRE https://github.com/mitre-attack/ Licencia Apache 2 El ATT&CK Navigator está diseñado
navegador de ataque para proporcionar navegación básica y
anotación de matrices ATT&CK,
algo que la gente ya es
haciendo hoy en herramientas como Excel.
CyberChef 11.0.0 GCHQ https://github.com/gchq/ Licencia Apache 2 La "navaja cibernética suiza": una
Aplicación web CyberChef para cifrado, codificación,
compresión y análisis de datos.
Docker 29.2.1 Docker https://github.com/docker Licencia Apache 2 Docker es un conjunto de plataformas como
productos de servicio que utilizan nivel de sistema operativo
virtualización para entregar software en
paquetes llamados contenedores.
ElastAlert 2.28.0 Jason Ertel https://github.com/jertel/ Licencia Apache 2 ElastAlert es un marco simple
elastalert2 para alertar sobre anomalías, picos,
u otros patrones de interés de
datos en Elasticsearch.
Elastic Agent 9.3.3 Elastic https://github.com/elastic/elastic- Licencia Elastic Versión 2 Beats es una plataforma abierta y gratuita
agente para remitentes de datos con un solo propósito.
Envían datos de cientos o
miles de máquinas y
sistemas a Logstash o
Búsqueda elástica.
Elasticsearch 9.3.3 Elastic https://github.com/elastic/ Licencia Elastic Versión 2 Elasticsearch es una versión distribuida y abierta
motor de análisis y búsqueda de fuentes elasticsearch
para todo tipo de datos, incluidos
textual, numérico, geoespacial,
estructurados y no estructurados.
evtx 0.11.0 Omer Benamram https://github.com/ Licencia MIT Un analizador multiplataforma para
omerbenamram/evtx Formato de registro de eventos XML de Windows.
evtx2es 1.8.0 Shinta Nakano https://github.com/Security-Onion- MIT License Una biblioteca rápida para analizar y
Soluciones/evtx2es importando registros de eventos de Windows
Búsqueda elástica.
ExifTool 12.60 Phil Harvey https://github.com/exiftool/exiftool GNU GPL Versión 3 ExifTool es una plataforma independiente
Biblioteca Perl más una línea de comandos
aplicación para lectura, escritura y
editar metainformación en una amplia
variedad de archivos.
Hydra 26.2.0 Ory https://github.com/ory/hydra Licencia Apache 2 Ory Hydra es un OpenID reforzado
Servidor OAuth 2.0 certificado y
Proveedor de conexión OpenID
optimizado para baja latencia, alta
rendimiento y bajos recursos
consumo
InfluxDB 2.7.12 InfluxData https://github.com/influxdata/ Licencia MIT InfluxDB es un tiempo de código abierto
Plataforma de la serie influxdb/tree/main-2.x. Esto incluye API
para almacenar y consultar datos,
procesándolo en segundo plano para
ETL o monitoreo y alerta
propósitos, paneles de usuario y
visualizar y explorar los datos
y más.
Kibana 9.3.3 Elastic https://github.com/elastic/kibana Licencia Elastic Versión 2 Kibana es una interfaz de código abierto
aplicación que se encuentra en la parte superior del
Elastic Stack, que proporciona búsqueda y
capacidades de visualización de datos para
datos indexados en Elasticsearch.
Kratos 26.2.0 Ory https://github.com/ory/kratos Licencia Apache 2 Ory Kratos es fácil de desarrollar,
seguridad reforzada y probada en batalla
Identidad, Gestión de Usuarios y
Sistema de autenticación para el
Nube.
Logstash 9.3.3 Elastic https://github.com/elastic/ Licencia Elastic Versión 2 Logstash es un servidor de datos
canalización de procesamiento logstash que ingiere
datos de multitud de fuentes
simultáneamente, lo transforma y
luego lo envía a tu favorito
"alijo."
NetworkMiner 2.8.1 Netresec https://www.netresec.com/? GNU GPL Versión 2 NetworkMiner es de código abierto
page=Herramienta de análisis forense de red NetworkMiner
(NFAT) y se puede utilizar como
rastreador/paquete de red pasivo
herramienta de captura para detectar
sistemas operativos, sesiones,
nombres de host, puertos abiertos, etc. sin
poner cualquier tráfico en la red.
NetworkMiner también puede analizar
Archivos PCAP para análisis fuera de línea y
regenerar/reensamblar
archivos y certificados transmitidos
de archivos PCAP. Sólo incluido en
Escritorio cebolla de seguridad.
Nginx 1.30.1 NGINX https://github.com/nginxinc/ Licencia BSD de 2 cláusulas Nginx es un servidor web que también puede
docker-nginx se puede utilizar como proxy inverso, cargar
equilibrador, proxy de correo y HTTP
cache.
OpenCanary 0.9.7 Thinkst Canary https://github.com/thinkst/ Licencia BSD de 3 cláusulas OpenCanary es un multiprotocolo
Honeypot de la red opencanary. Es su uso principal-
caso es atrapar a los piratas informáticos después
han violado la privacidad
redes.
Oracle Linux 9 9.7 Oracle Linux https://www.oracle.com/linux/ GNU GPL Versión 2 Oracle Linux es una distribución de Linux
empaquetado y distribuido gratuitamente por
Oracle, disponible parcialmente bajo el
Licencia Pública General GNU desde
finales de 2006. Está compilado de Red
Código fuente de Hat Enterprise Linux,
reemplazar la marca Red Hat con
El oráculo.
pcapfix 1.1.7 Robert Krause https://github.com/Rup0rt/pcapfix/ GNU GPL Versión 3 Pcapfix es una herramienta para reparar tu
pcap dañado o corrupto y
archivos pcapng.
PostgreSQL 17.9 PostgreSQL Global https://postgresql.org Licencia de PostgreSQL PostgreSQL es una potente y abierta
Base de datos relacional de objetos fuente del grupo de desarrollo
sistema que utiliza y amplía la
Lenguaje SQL combinado con muchos
características que almacenan y escalan de forma segura
los datos más complicados
cargas de trabajo.
Python 3.14.3 Fundación de software Python https://github.com/python/ Fundación de software Python
Versión de licencia 2
- 395/402 - Soluciones de cebolla de seguridad, LLC

24. Lista de materiales del software
Producto Versión Autor Proyecto URL Licencia Descripción
Python es un lenguaje de programación
que le permite trabajar de forma rápida y
integrar sistemas de manera más efectiva.
Redis 7.2.13 Redis https://github.com/redis/redis Licencia BSD de 3 cláusulas Redis es un código abierto en memoria
almacén de estructura de datos utilizado como
base de datos, caché y mensaje
corredor.
Salt 3006.19 Proyecto Salt https://github.com/saltstack/salt Licencia Apache 2 Salt es un control remoto distribuido
sistema de ejecución utilizado para ejecutar
comandos y consultar datos. fue
desarrollado para traer lo mejor
soluciones encontradas en el mundo de
ejecución remota juntos y
hacerlos mejores, más rápidos y más
maleable. La sal logra esto
gracias a su capacidad para manejar cargas más grandes
de información, y no sólo docenas,
pero cientos o incluso miles de
servidores individuales, manejarlos
rápidamente y a través de una forma sencilla y
interfaz manejable.
Security Onion Console 3.1.0 Security Onion Solutions https://github.com/Security-Onion- Elastic License Versión 2 Security Onion Console es una versión web
Interfaz Solutions/securityonion-soc para ver alertas, cazar,
y análisis PCAP.
Strelka 1.0.1 Target https://github.com/target/strelka Licencia Apache 2 Strelka es un escaneo de archivos en tiempo real
sistema utilizado para la caza de amenazas,
detección de amenazas e incidentes.
respuesta. El propósito de Strelka es
realizar la extracción de archivos y
recopilación de metadatos a gran escala.
Suricata 8.0.5 OISF https://github.com/OISF/suricata GNU GPL Versión 2 Suricata es un código abierto y gratuito,
red madura, rápida y robusta
Motor de detección de amenazas. suricata
inspecciona el tráfico de la red utilizando un
reglas poderosas y extensas y
lenguaje de firma.
Telegraf 1.38.0 InfluxData https://github.com/influxdata/ Licencia MIT Telegraf es un agente basado en servidor para
telegraf recopilando y enviando todas las métricas
y eventos de bases de datos,
sistemas y sensores de IoT. telégrafo
está escrito en Go y se compila en un
binario único sin externo
dependencias, y requiere una muy
huella de memoria mínima.
Ubuntu 22.04, 26.04 Canonical https://github.com/canonical Política de derechos de propiedad intelectual de Canonical El código abierto número 1
El sistema operativo impulsa a millones
de PC y portátiles en todo el mundo
mundo.
Yara 4.3.1 VirusTotal https://github.com/virustotal/yara Licencia BSD de 3 cláusulas YARA es una herramienta dirigida (pero no)
limitado a) ayudar al malware
investigadores para identificar y clasificar
muestras de malware.
Wireshark 3.4.10 Wireshark https://github.com/wireshark/ GNU GPL Versión 2 Wireshark es el más importante del mundo
Wirehark y protocolo de red ampliamente utilizado
analizador. Te permite ver lo que
sucediendo en su red en un
nivel microscópico y es el de
estándar de facto (y a menudo de jure)
en muchas empresas comerciales y no
empresas con fines de lucro, gobierno
agencias y centros educativos
instituciones. Sólo incluido en
Escritorio cebolla de seguridad.
Zeek 8.0.8 Zeek https://github.com/zeek/zeek/ Licencia BSD de 3 cláusulas Un potente marco para red
análisis de tráfico y seguridad
seguimiento.
- 396/402 - Soluciones de cebolla de seguridad, LLC

25. Notas de la versión
25. Notas de la versión
25.0.1 Problemas conocidos
Para todos los demás problemas conocidos, consulte https://github.com/Security-Onion-Solutions/securityonion/issues.
25.0.2 Historial de versiones
25.1 3.1.0 Revisión [20260528] Cambios
• REVISIÓN: Las grillas con múltiples nodos pesados fallan en la verificación de actualización de Elasticsearch para 3.1.0
• REVISIÓN: Las cuadrículas que utilizan canalizaciones de logstash personalizadas pueden tener entradas de pilar obsoletas #15932
25.2 3.1.0 [20260521] Cambios
• FUNCIÓN: Agregue compatibilidad con Postgres para funciones futuras
• FUNCIÓN: Agregue compatibilidad con NIC vinculada para interfaces de administración #15548
• FUNCIÓN: Agregar métrica de latencia de ingesta
• FUNCIÓN: Permite la configuración de bond1 para la gestión de instalaciones ISO #15865
• FUNCIÓN: Elastic Fleet valida continuamente la política de salida
• FUNCIÓN: Monitoreo RAID para máquinas virtuales de hipervisor #15809
• FUNCIÓN: Restaurar anulaciones de Suricata desde la copia de seguridad n.º 15881
• FUNCIÓN: Mapeos de Sigma - M365 y Fortigate #15882
• FUNCIÓN: Configuración simplificada de Onion AI para regiones fuera de EE. UU. #15773
• FUNCIÓN: Compatibilidad con puntos finales de Azure OpenAI #15841
• REVISIÓN: 'Investigar' utilizando un modelo local inaccesible muestra "créditos insuficientes"
• CORRECCIÓN: Agregar selección de opciones a las anotaciones #15744
• CORRECCIÓN: Imágenes de dispositivos en la cuadrícula SOC desalineadas #15713
• REVISIÓN: Considere configurar el nivel de salida del Agente elástico en solo advertencia #15431
• CORRECCIÓN: Ordenación determinista umbral.conf #15815
• REVISIÓN: Mejore el resultado de la instalación del agente elástico para verificar que la instalación esté en buen estado.
• REVISIÓN: Mejorar la validación de parámetros de consulta elástica y lucene #15860
• REVISIÓN: Mejorar la tasa de éxito de las búsquedas DNS inversas #15760
• REVISIÓN: Mejorar la usabilidad para usuarios con discapacidad visual
• REVISIÓN: Hipervínculo de licencia JA4+ #15717
• REVISIÓN: Hacer que las anotaciones habilitadas para SOC y Kratos sean de solo lectura #15827
• REVISIÓN: La modificación de las plantillas de detección en la configuración provoca que el SOC se bloquee en el bucle #15798
• CORRECCIÓN: Se necesitan mejores comentarios de los usuarios al adjuntar el chat del asistente al caso #15689
• CORRECCIÓN: Las descripciones de nodos que contienen espacios y números impiden la creación de pilares #15540
• REVISIÓN: Evitar una longitud excesiva de las consultas de OnionAI
• REVISIÓN: Reactor sominion_setup #15834
• REVISIÓN: Copia de seguridad de detecciones de refactorización #14992
- 397/402 - Soluciones de cebolla de seguridad, LLC

25.3 3.0.0 [20260331] Cambios
• REVISIÓN: Reinstalar #15811
• REVISIÓN: SOUP verifica que todos los nodos de Elasticsearch sean compatibles con la próxima versión de Elasticsearch #15908
• REVISIÓN: Suricata pcap-log max-files se redondea a 0 cuando el valor calculado está entre 0 y 1 #15740
• CORRECCIÓN: La interfaz de usuario debería mostrar el nombre del Panel actual #15703
• CORRECCIÓN: Utilice el enlace de acción de búsqueda para pivotes de búsqueda observables de casos #15752
• REVISIÓN: Utilice carga segura para cargar la configuración de comprobación de archivos #15859
• REVISIÓN: canalización de ingesta de Zeek para JA4d.log #15886
• ACTUALIZACIÓN: Axios a 1.15.0 en SOC #15774
• ACTUALIZACIÓN: CyberChef a 11.0.0 #15890
• ACTUALIZACIÓN: Elasticsearch a 9.3.3
• ACTUALIZACIÓN: Kratos e Hydra 26.2.0+pgx #15796
• ACTUALIZACIÓN: Dependencias de SOC Go #15795
• ACTUALIZACIÓN: Bibliotecas de dependencia de interfaz SOC #15848
• ACTUALIZACIÓN: Suricata a 8.0.5 #15903
• ACTUALIZACIÓN: Zeek a 8.0.8 #15794
• ACTUALIZACIÓN: nginx a 1.30.1 #15891
25.3 3.0.0 [20260331] Cambios
• FUNCIÓN: Configuración configurable de Elasticsearch vm.max_map_count
• FUNCIÓN: Cargue dinámicamente complementos de Zeek al iniciar Zeek #15546
• FUNCIÓN: Habilite la aceptación de licencia JA4+ #15560
• FUNCIÓN: Análisis de registros de websockets de Zeek #15657
• FUNCIÓN: Actualizar la página de inicio de sesión con una apariencia actualizada
• FUNCIÓN: Actualiza la interfaz de usuario de SOC con una apariencia actualizada
• FUNCIÓN: Admite nombres alternativos adicionales en el certificado web
• FUNCIÓN: Admite la personalización de Docker Ulimit #15581
• ARTÍCULO: Suricata PCAP reemplaza al taquígrafo
• CORRECCIÓN: Los errores API 401 ya no redireccionarán #15611
• REVISIÓN: Limpieza de archivos.absent y cron.absent
• REVISIÓN: Detecciones: "error al cerrar el desplazamiento" intermitente #14216
• REVISIÓN: Roles de usuario duplicados al actualizar la interfaz en Administración > Usuarios #15688
• REVISIÓN: Botones habilitados/deshabilitados para las opciones de configuración de red SOC #15649
• REVISIÓN: Corrección de validadores de reglas en SOC #15533
• REVISIÓN: Las configuraciones de anulación global no deberían aplicarse a ciertos índices #15601
• REVISIÓN: El transporte de red para alertas de suricata debe estar en minúscula #15668
• REVISIÓN: Los sensores no se registran mientras se procesan trabajos largos #15650
• CORRECCIÓN: secuencia de comandos so-suricata-testrule #15396
• CORRECCIÓN: STIG V1R3
• REVISIÓN: Las variables de grupos de direcciones de Suricata permiten la negación #15664
• REVISIÓN: No se pueden crear detecciones a través de Security Onion API #15673
• ACTUALIZACIÓN: Todos los departamentos frontend de terceros
- 398/402 - Soluciones de cebolla de seguridad, LLC

25.3 3.0.0 [20260331] Cambios
• ACTUALIZACIÓN: ATTACK Navigator a 5.3.0 #15680
• ACTUALIZACIÓN: CyberChef a 10.22.1 #15681
• ACTUALIZACIÓN: ElastAlert2 a 2.28.0 #15685
• ACTUALIZACIÓN: Departamentos de terceros de Golang #15647
• ACTUALIZACIÓN: Golang a 1.26.1 #15580
• ACTUALIZACIÓN: Hydra a 25.4.0 #15678
• ACTUALIZACIÓN: Kafka a 3.9.2 #15684
• ACTUALIZACIÓN: Kratos a 25.4.0 #15677
• ACTUALIZACIÓN: Nginx a 1.29.6 #15686
• ACTUALIZACIÓN: OpenCanary a 0.9.7 #15679
• ACTUALIZACIÓN: Redis a 7.2.13 #15682
• ACTUALIZACIÓN: Suricata a 8.0.4 #15625
• ACTUALIZACIÓN: Telegraf a 1.38.0 #15683
• ACTUALIZAR: actualice las imágenes base de Docker
- 399/402 - Soluciones de cebolla de seguridad, LLC

26. Apéndice
26. Apéndice
Este apéndice proporciona una descripción general del proceso de actualización del antiguo Security Onion 2.4 al nuevo Security Onion 3.
consejo
Si actualmente es cliente de Security Onion Solutions con servicios profesionales o cobertura de electrodomésticos, comuníquese con el soporte de SOS y podremos ayudarlo.
usted a través de este proceso.
Advertencia
Security Onion 3 solo es compatible con Oracle Linux 9. Si está ejecutando Security Onion 2.4 en alguna otra distribución no compatible, deberá
realice una nueva instalación de Security Onion 3.
Advertencia
Recomendamos probar este proceso en un entorno de prueba antes de intentarlo en su entorno de producción.
26.1 Verificar copia de seguridad
Si ha revisado todas las advertencias anteriores, asegúrese de que haya una copia de seguridad en /nsm/backup:
sudo ls -alh /nsm/backup
Una vez que haya verificado su copia de seguridad y esté listo para actualizar, debería poder hacer lo siguiente. Hay secciones separadas para
Implementaciones de Internet e implementaciones de Airgap.
26.2 Implementaciones de Internet
Si su implementación tiene acceso a Internet, primero asegúrese de que esté completamente actualizada a la versión 2.4.211 mediante sopa:
sopa sudo
Una vez que su implementación se haya actualizado a 2.4.211, ejecute el siguiente comando:
sudo sopato3
Este comando verificará algunas configuraciones en su sistema y luego descargará una nueva versión de sopa. Luego podrás ejecutar la nueva versión de sopa.
para realizar la actualización:
sopa sudo
26.3 Implementaciones de espacios aéreos
Si su implementación no tiene acceso a Internet y está en modo airgap, primero asegúrese de que esté completamente actualizada a la versión 2.4.211 usando sopa
y la imagen ISO 2.4.211.
- 400/402 - Soluciones de cebolla de seguridad, LLC

26.3 Implementaciones de espacios aéreos
Una vez hecho esto, deberá hacer manualmente algunas cosas para prepararse para la actualización:
• asegúrese de que la configuración de pcapengine esté configurada en SURICATA
• eliminar cualquier dato antiguo del taquígrafo
Finalmente, puede actualizar a la versión 3.0 usando sopa y la imagen ISO de Security Onion 3.
- 401/402 - Soluciones de cebolla de seguridad, LLC

27. Hoja de trucos
27. Hoja de trucos
Si está viendo la versión en línea de esta documentación, puede hacer clic aquí para obtener nuestra Hoja de referencia de Security Onion.
Esto se basó en una hoja de referencia creada originalmente por Chris Sanders que se puede encontrar aquí:
https://chrissanders.org/2017/06/security-onion-cheat-sheet/
- 402/402 - Soluciones de cebolla de seguridad, LLC
