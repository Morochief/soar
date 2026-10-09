# Graded Quiz: Module 2 challenge

**1. Completa el espacio en blanco: _____ describe la cantidad de datos que se mueven a través de una red.**
*(Fill in the blank: _____ describes the amount of data that moves across a network.)*
- [ ] Datos de red *(Network data)*
- [x] Tráfico de red *(Network traffic)*
- [ ] Flujo de tráfico *(Traffic flow)*
- [ ] Exfiltración de datos *(Data exfiltration)*

**2. ¿Cuáles son algunas de las medidas defensivas que se pueden utilizar para protegerse contra la exfiltración de datos? (Selecciona dos respuestas)**
*(What are some defensive measures that can be used to protect against data exfiltration? Select two answers.)*
- [x] Implementar autenticación multifactor (MFA). *(Deploy multi-factor authentication)*
- [x] Monitorear la actividad de la red (Revisar logs y tráfico). *(Monitor network activity)*
- [ ] Utilizar movimiento lateral (Táctica ofensiva). *(Utilize lateral movement)*
- [ ] Reducir el tamaño de los archivos. *(Reduce file sizes)*

**3. ¿Qué información contienen los encabezados (*headers*) de los paquetes? (Selecciona tres respuestas)**
*(What information do packet headers contain? Select three answers.)*
- [ ] Datos de carga útil / Payload (Van en el cuerpo, no en el encabezado). *(Payload data)*
- [x] Protocolos (TCP, UDP, ICMP). *(Protocols)*
- [x] Puertos (Origen y Destino). *(Ports)*
- [x] Direcciones IP (Origen y Destino). *(IP addresses)*

**4. Completa el espacio en blanco: Los analizadores de protocolos de red (como Wireshark o tcpdump) pueden guardar las comunicaciones de red en archivos conocidos como _____.**
*(Fill in the blank: Network protocol analyzers can save network communications into files known as a _____.)*
- [ ] protocolo *(protocol)*
- [ ] paquete de red *(network packet)*
- [ ] payload *(payload)*
- [x] captura de paquetes / PCAP *(packet capture)*

**5. ¿Cómo ayudan los analizadores de protocolos de red a los analistas de seguridad a investigar las comunicaciones de red? (Selecciona dos respuestas)**
*(How do network protocol analyzers help security analysts analyze network communications? Select two answers.)*
- [x] Proporcionan la capacidad de recopilar/capturar comunicaciones de red. *(They provide the ability to collect network communications.)*
- [x] Proporcionan la capacidad de filtrar y ordenar la información de captura de paquetes para encontrar datos relevantes. *(They provide the ability to filter and sort packet capture information to find relevant information.)*
- [ ] Toman medidas para mejorar el rendimiento de la red. *(They take action to improve network performance.)*
- [ ] Toman medidas para bloquear intrusiones en la red (Eso es un IPS). *(They take action to block network intrusions.)*

**6. ¿Qué versión de protocolo se considera la base de todas las comunicaciones de Internet?**
*(Which protocol version is considered the foundation for all internet communications?)*
- [ ] ICMP
- [ ] HTTP
- [ ] UDP
- [x] IPv4 *(IPv4)*

**7. ¿Qué se utiliza para determinar si se han producido errores o corrupción en el encabezado IPv4?**
*(What is used to determine whether errors have occurred in the IPv4 header?)*
- [ ] Encabezado *(Header)*
- [ ] Banderas *(Flags)*
- [ ] Protocolo *(Protocol)*
- [x] Suma de comprobación *(Checksum)*

**8. ¿Por qué los encabezados IP son valiosos para los analistas de seguridad durante las investigaciones?**
*(How are IP headers valuable for security analysts during investigations?)*
- [ ] Proporcionan la capacidad de visualizar (Gráficamente) las comunicaciones.
- [ ] Proporcionan la base para las comunicaciones a través de Internet.
- [ ] Proporcionan la capacidad de modificar las comunicaciones de red.
- [x] Proporcionan información detallada sobre los pormenores de las comunicaciones de red (IPs de origen/destino, puertos, tamaños). *(They provide insight into the details of network communications.)*

**9. ¿Qué opción/parámetro de `tcpdump` aplica verbosidad (muestra más detalles en la salida de texto)?**
*(Which tcpdump option applies verbosity?)*
- [ ] `-i` (Interface)
- [x] `-v` (Verbose)
- [ ] `-c` (Count)
- [ ] `-n` (No resolver nombres DNS)

**10. Examina la siguiente salida de `tcpdump`:**
`22:00:19.538395 IP (tos 0x10, ttl 64, id 33842, offset 0, flags [P], proto TCP (6), length 196) 198.168.105.1.41012 > 198.111.123.1.61012: Flags [P.], cksum 0x50af (correct), seq 169, ack 187, win 501, length 42`

**¿Cuál es el valor del campo Tipo de Servicio (Type of Service / ToS)?**
*(What is the value of the Type of Service field?)*
- [ ] 501
- [x] 0x10
- [ ] 0x50af
- [ ] 6
> [!NOTE]
> En la estructura de lectura de tcpdump, dentro de los paréntesis `IP (tos 0x10...` se especifica explícitamente el valor hexadecimal de Tipo de Servicio.
