✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Log Parser Ports
Learn more at Stellar Cyber Academy.
The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lesson.
M03 Modular Sensor Concepts and Configuration (08h:56m)  
Parsers for Normalization Into Interflow (18m:00s)
Discover how parsers work to normalize telemetry and metadata into Interflow records.
Learn how to interpret logs from diverse sources, identify key data fields, and
understand their significance in threat analysis.
The first time you access a link on the portal during a session, you must log in to access
content.
Sections in this topic:
Choosing an Ingestion Port
Generic Log Parsers
Vendor-specific Log Parsers
Vendor-Specific CEF Parsers Introduced by Release
Parsers that Support Line Breaks in Messages Delivered over TCP
To receive and parse logs from devices on your network, Stellar Cyber Modular Sensors require
open inbound ports. These ports are already open on Modular Sensors by default. If there are
any firewalls in the data path between the log sources and a modular sensor, you must also open
the appropriate ports on the firewalls. This topic lists the supported log parsers and related
details, including the port each parser uses. Log parsers are organized in the following
categories:
Generic
Vendor-specific
Also see: Firewall Requirements and Common Log Formats

 Unless otherwise noted, the ports listed are applicable for both UDP and TCP.
 During installation, the timezone for sensors are automatically set to UTC+0. Since the logs
for some security products might only include the local time without a timezone, Stellar Cyber
recommends that you set the sensor timezone to the same timezone as your security
product.
Choosing an Ingestion Port
Modular Sensors listen on port 514 by default. They then analyze the logs to determine the
source device. In some cases, Stellar Cyber has specific ports to process industry standard log
formats, as well as specialized parsers to process vendor-specific logs in a more detailed
manner. Identifying a more specific port for a log type than port 514 provides the following
benefits:
It speeds up data ingestion and log parsing and increases sensor performance because
the sensor already knows the source device.
It retains the correct log source when the sensor forwards normalized logs as Interflow
records to the Stellar Cyber Open XDR platform.
Use the following as a guide:
If the logs are in standard Common Event Format (CEF), Log Event Extended
Format (LEEF), or JavaScript Object Notation (JSON) format, forward to the data to
the port specific to that standard as listed in Generic Log Parsers.
If the logs are in standard Syslog format use the port applicable for that vendor.
If the logs are in a specialized format such as a Syslog and use regular expressions,
key-value pairs, or comma-separated values (csv), use the Vendor-specific ports.
Generic Log Parsers
This table includes all supported generic log parser formats, the required firewall port, device
type, and the associated Stellar Cyber index.
Use the msg_origin.source field in the Interflow to find the logs when threat hunting in the
specified index.
 In the Interflow, there are also fields for msg_origin.processor.type, which is always
log_forwarder for log parsers, and msg_origin.processor.name, which stores specific
components of the parser, such as the parser type (cef, leef).
When the Stellar Cyber Platform processes logs, it decides the index based on the data in the
logs. For example, in the table the Index for LEEF is Traffic (srcip), Syslog (otherwise). This
means that the index will be Traffic if a source IP address is detected, or Syslog if not, in that
order.
Following are the firewall ports to open for generic log formats, along with other useful details.

S
t
a
| n    | msg_origin.so |       |          |
| ---- | ------------- | ----- | -------- |
| Port |               | Index | Comments |
| d    | urce          |       |          |
a
r
d
| C 5143 and | cef_device_vend |     |     |
| ---------- | --------------- | --- | --- |
Traffic (srcip, srcport, dstip, dstport, and proto), Syslog Stellar Cyber recommends using
| E 5870 | or  |             |                    |
| ------ | --- | ----------- | ------------------ |
|        |     | (otherwise) | CEF, if available. |
F (TCP)
The following vendor records are also indexed in TCP port 5870 is for CEF
IDPS/Malware Sandbox Events, with the threat field being messages that use octet counting
normalized from logs as indicated below: and port 5143 is for messages
|     |     | If cef_device_vendor: Check Point, then the threat | that don't. |
| --- | --- | -------------------------------------------------- | ----------- |
field is normalized from attack_information.
If cef_device_vendor: F5, then the threat field is
normalized from attack_type
If cef_device_vendor: SentinelOne, then the threat
field is normalized from classification
| C 5175 | cef_device_vend | Traffic (srcip), Syslog (otherwise) | -   |
| ------ | --------------- | ----------------------------------- | --- |
| E      | or              |                                     |     |
F
2
| G 5201 and | generic_capture | Syslog | TCP port 5871 is for log         |
| ---------- | --------------- | ------ | -------------------------------- |
| e 5871     |                 |        | messages that use octet counting |
| n (TCP)    |                 |        | and port 5201 is for messages    |
| e          |                 |        | that don't.                      |
ri
c
c
a
pt
u
r
e
| G 514 | -   | -   | Use only if you must use a log |
| ----- | --- | --- | ------------------------------ |
| e     |     |     | forwarder.                     |
n
e
ri
c
s
y
sl

S
t
a
| n    | msg_origin.so |       |          |
| ---- | ------------- | ----- | -------- |
| Port |               | Index | Comments |
| d    | urce          |       |          |
a
r
d
o
g
| H 5200  | httpjson | Syslog | When you configure your log    |
| ------- | -------- | ------ | ------------------------------ |
| T (TCP) |          |        | forwarding for the HTTP JSON   |
| T       |          |        | parser on this port, you must  |
| P       |          |        | append /httpjson at the end of |
| J       |          |        | the URL of the target sensor.  |
| S       |          |        | Example: http://<sensor-       |
| O       |          |        | ip>:5200/httpjson              |
N
| J 5142 | json | Syslog |     |
| ------ | ---- | ------ | --- |
S
O
N
st
r
e
a
m
| J 5044 | beats | Syslog | -   |
| ------ | ----- | ------ | --- |
S
O
N
b
e
at
s
L 5522 vendor Traffic (srcip), Syslog (otherwise) LEEF is primarily useful for logs
| E   |     |     | from QRadar, for which LEEF was |
| --- | --- | --- | ------------------------------- |
| E   |     |     | developed.                      |
F
| Li 5555 | linux_syslogs | Syslog | -   |
| ------- | ------------- | ------ | --- |
n
u
x
S

S
t
a
n msg_origin.so
Port Index Comments
d urce
a
r
d
y
sl
o
g
5140 syslog Syslog -
R
F
C
3
1
6
4
R syslog Syslog -
5141
F
C
5
4
2
4
R 5589 syslog_rfc5424 Syslog -
F
C
5
4
2
4
E
n
h
a
n
c
e
d
Vendor-specific Log Parsers

This table includes all supported vendor-specific parsers, the port on which parsers listen for log
messages, log formats, device types, message types, and their associated Stellar Cyber indices.
The Log Format column states the format that log sources use when sending data to Stellar
Cyber modular sensors. For information about the common log formats that Stellar Cyber
parsers support, see Common Log Formats.
The msg_origin.source column specifies the vendor's product. Use the field in the Interflow to
find the logs when threat hunting in the specified index. The msg_origin.category column
specifies the overall category. In the Interflow, there are also fields for
msg_origin.processor.type, which is always log_forwarder for log parsers, and
msg_origin.processor.name, which stores specific components of the parser, such as the
parser name.
The Index column indicates the fields that must be present (and not null) for the logged data to
be entered into the respective index. In some cases, no specific field is required, so just the
index name is listed. For many parsers, the remaining data that is not mapped to a specific index
is "otherwise" and mapped into the Syslog index. For example, for FortiAnalyzer logs received on
port 5542, data is added to the IDPS/Malware Sandbox Events index if the incoming field
vendor.attack_name is not null. Data is added to the Traffic index if dstip is not null. The
remaining data is added to the Syslog index. Use the dev_type field in the Interflow to find logs
when threat hunting in the specified index.
ICMP/IGMP Sent to Traffic Index
When using the table below, keep in mind that ICMP and IGMP traffic operates at Layer 3 in the
OSI model and does not include port numbers. Stellar Cyber treats this traffic as though it
includes all five tuples (source/destination addresses, source/destination ports, and protocol) and
sends it to the Traffic index.
Log Format Legend
RFC 3164 = RFC 3164: The BSD Syslog Protocol KVP = key-value pairs
RFC 5424 = RFC 5424: The Syslog Protocol JSON = JavaScript Object Notation
CEF = Common Event Format HTTP JSON = HTTP protocol headers followed by JSON
content
LEEF = Log Event Extended Format (used primarily for ( ) = optional
QRadar)
regex = regular expressions* + = and
Example: The log format RFC 3164 + (regex) means that logs include syslog messages
formatted as specified in RFC 3164: The BSD Syslog Protocol and that the parser can apply
regular expressions if needed. Log messages formatted according to RFC 3164 have a priority
value, which encodes facility and severity, a timestamp, a hostname, and the log message.
Regular expressions might optionally be applied to the log message to perform additional
operations such as parsing complex messages, filtering logs, and extracting specific fields.
*About regex: In Stellar Cyber parser documentation, “regex” indicates that a parser uses
regular expressions to extract fields from a log because the raw log is not in a fixed position or
standard delimiter-based structure. This does not mean the device outputs logs in a “regex
format”. The other elements in the format (such as CSV, KVP, JSON, RFC 3164, RFC 5424)

describe how the remaining portion of the log is structured when sent by the device. After
parsing, all logs are converted into Stellar Cyber Interflow records in JSON format.
Here's an example for which the log format is regex + KVP, shown before and after parsing it
using regex:
Raw log before parsing:
<134>1 1377449842.514782056 MX84 ids-alerts signature=129:4:1 priority=3
timestamp=1377449842.512569 direction=ingress protocol=tcp/ip src=74.125.140.132:80
Interflow record after parsing the log with regex:
priority: 134
version: 1
timestamp: 1377449842.514782056
hostname: MX84
log_type: ids-alerts
signature_id: 129:4:1
priority_level: 3
event_timestamp: 1377449842.512569
direction: ingress
protocol: tcp/ip
source_ip: 74.125.140.132
source_port: 80
|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y        |     |
| --- | --- | --- | -------- | --- |
|     | 5   |     | firewall |     |
(OpnSense) Zenarmor plugin Sunny Valley Networks sunny_vall Traffic (srcip,
| logs | 6 custom format | ey_network |     | srcport, |
| ---- | --------------- | ---------- | --- | -------- |
0
|     |     | s_zenarmo |     | dstip, |
| --- | --- | --------- | --- | ------ |
4
|     |     | r   |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| A10 vThunder Application | RFC 3164 + A10-specific |     | netlogs |                 |
| ------------------------ | ----------------------- | --- | ------- | --------------- |
|                          | 5                       |     |         | Traffic (srcip, |
a10_vthun
| Delivery Controller (ADC) | 8 log header + message |     |     | srcport, |
| ------------------------- | ---------------------- | --- | --- | -------- |
der_adc
|     | 8   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
AAA - Core (CEF)
|     | 5 CEF | netiq_adva | iam | Traffic (srcip, |
| --- | ----- | ---------- | --- | --------------- |
|     | 1     | nce_auth   |     | srcport,        |
|     | 4     |            |     | dstip,          |
|     | 3     |            |     | dstport, and    |
|     | or    |            |     | proto),         |
|     | 5     |            |     | Syslog          |
|     | 8     |            |     | otherwise       |
7
0
| Absolute Secure Endpoint | Absolute custom RFC    |            | endpoint |                 |
| ------------------------ | ---------------------- | ---------- | -------- | --------------- |
|                          | 6                      | absolute_s |          | Traffic (srcip, |
|                          | 0 5424 header + custom |            |          | srcport,        |
ecure_end
CEF payload
|     | 7   | point |     | dstip,       |
| --- | --- | ----- | --- | ------------ |
|     | 8   |       |     | dstport, and |
Vendor-Specific CEF Parsers Introduced by Release
proto),
Stellar Cyber Modular Sensors support parsing logs in Common Event Format S(yCslEogF) using built-
| in parsers. There are two types of CEF parsers: |     |     |     | otherwise |
| ----------------------------------------------- | --- | --- | --- | --------- |
Generic CEF Parser: Parses CEF logs from any device that does not match a known
| Accops | 5 Accops custom format | accops | vpn | Traffic |
| ------ | ---------------------- | ------ | --- | ------- |
vendor signature. Logs are normalized into general-purpose Interflow record fields
|     | 5   |     |     | (srcip), |
| --- | --- | --- | --- | -------- |
using standard key-value pair (KVP) mappings found in the CEF header and extension.
|     | 2   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
This parser is used for CEF logs from unknown vendors.
|     | 6   |     |     | otherwise |
| --- | --- | --- | --- | --------- |
AhnVlaebn AdIPoSr-Specific CEF P 5 ars c e u r s s to : m  P  L a E r E s F e  ( s R   F C C E  3 F 16  l 4 ogs ah  f n r l o ab m _a  r ip eco id g p n s ized ve T n r d af o fic rs  (s  w rci i p th ,
dedicated parsing logic for that vendor's formatting. Vendor-specific CEF parsers
|     | 6 or RFC 5424) | s   |     | srcport, |
| --- | -------------- | --- | --- | -------- |
support enriched field extraction, normalization, and mapping into targeted Interflow
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
record fields that reflect the semantics of the vendor's log structure.
|     | 7   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
When a new vendor-specific CEF parser is introduced in a sensor release, logsp rofrtoo)m,  that vendor
—previously handled by the generic CEF parser—are reclassified and parsed uSyssinlogg the new
vendor-specific logic. This can result in changes to field values in Interflow reco(ordthser,w inisec)luding
msg_origin.source, msg_origin.vendor, msg_class, and others.
| Ahnlab Cloud Protection | CEF |           | paas |                 |
| ----------------------- | --- | --------- | ---- | --------------- |
|                         | 5   | ahnlab_cp |      | Traffic (srcip, |
Such changes might affect how th7e following features behpave: srcport,
Platform
|     | 5   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
Queries using filters on msg_origin.source or similar fields
|     | 5   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
Alert rules and correlation logic
proto),
| Custom dashboards, reports, or threat hunting views |     |     |     | Syslog |
| --------------------------------------------------- | --- | --- | --- | ------ |
(otherwise)
To ensure consistent behavior after a sensor upgrade, refer to the table below for a list of vendor-
specificA hCnlEabF E pDaR r(sEendrspo iinnttroduced o 5 r uCpEdFa t+e JdS OinN each releas a e hn .  la F b o _ r e   d f r ull epnadrpsoiinntg be T h ra a ff v ic i   o (s r r   c c ip h , anges,
| follow tDheete clitniokn  atond t hRees preonlesev)ant rele | ase notes. |     |     |              |
| ----------------------------------------------------------- | ---------- | --- | --- | ------------ |
|                                                             | 8          |     |     | srcport,     |
|                                                             | 8          |     |     | dstip,       |
|                                                             | 3          |     |     | dstport, and |
proto),

Versio
|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
Vendor-specific CEF Parsers Introduced or Updated msg_oLriingki to Release Notes
| nParser Name | or Log Format |     | n.categor | Index |
| ------------ | ------------- | --- | --------- | ----- |
n.source
|       | t   |                              | y   |     |
| ----- | --- | ---------------------------- | --- | --- |
| 6.6.0 |     | Stellar Cyber 6.6.0s Release |     |     |
Trend Micro Worry-Free Business Security Service
Notes
Syslog
(otherwise)
6.5.0 CheckPoint VPN-1 & FireWall-1 (CEF) Stellar Cyber 6.5.0s Release
AhnLab EMS 5 regex + KVP ahnlab_Neomtes endpoint Traffic (srcip,
CrowdStrike (CEF)
|     | 6   | s   |     | srcport, |
| --- | --- | --- | --- | -------- |
DefensX - DefensX (CEF)
|     | 5   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
Fortinet Fortigate (Note: Th7is is the modular parser in Parser dstport, and
| Studio.) |     |     |     | proto), |
| -------- | --- | --- | --- | ------- |
Syslog
NetScout Omnis
(otherwise)
OpenText - Open Enterprise Server (CEF)
AhnLab EPP
|     | 5 regex + JSON | ahnlab_ep | endpoint | Traffic (srcip, |
| --- | -------------- | --------- | -------- | --------------- |
Salt Security
|                                   | 6   | p   |     | srcport,     |
| --------------------------------- | --- | --- | --- | ------------ |
| Trend Micro - Apex Central4 (CEF) |     |     |     | dstip,       |
|                                   | 0   |     |     | dstport, and |
Trend Micro - Deep Discovery Email Inspector (CEF)
proto),
Zecurion - DLP (CEF)
Syslog
| Zscaler ZIA Web |     |     |     | (otherwise) |
| --------------- | --- | --- | --- | ----------- |
A h n Lab  P o lic y  C e nt e r 5 AhnLab custom format ahnlab_ p o li lar eCnydbpeorin 6t.4.0s T ra f f ic   (s rcip,
| 6 .4 . 0 |     | S te | l   |  R e l e a s e |
| -------- | --- | ---- | --- | -------------- |
A b s o lu te  S e c ure Endpoint
|     | 5   | cy_center |     | srcport, |
| --- | --- | --------- | --- | -------- |
Notes
Check Point - SmartConso7le (CEF)
dstip,
|     | 1   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
Check Point - SmartDefense (CEF)
proto),
Darktrace - DCIP (CEF)
Syslog
| Imperva SecureSphere |                          |                              |          | (otherwise)     |
| -------------------- | ------------------------ | ---------------------------- | -------- | --------------- |
| AhnLab TrusGuard     | 5                        | ahnlab_tru                   |          | Traffic (srcip, |
|                      | grave accent-separated ( |                              | firewall |                 |
| 6.3.0 Akamai WAF     |                          | Stellar Cyber 6.3.0s Release |          |                 |
|                      | 5                        | sguard                       |          | srcport,        |
` ) KVP
Notes
| NetScout Omnis | 5   |     |     | dstip,       |
| -------------- | --- | --- | --- | ------------ |
|                | 8   |     |     | dstport, and |
SonicWall NSa
proto),
| 6.2.0 |     | Stellar Cyber 6.2.0sS Ryeslleoagse |     |     |
| ----- | --- | ---------------------------------- | --- | --- |
Barracuda WAF
|     |     | Notes |     | (otherwise) |
| --- | --- | ----- | --- | ----------- |
Check Point Firewall
|     | PSV (pipe-separated- |            | waf |                 |
| --- | -------------------- | ---------- | --- | --------------- |
|     | 5                    | aioncloud_ |     | Traffic (srcip, |
AIONCLOUD WAF
Cynet (CEF)
|     | 9 values) |     |     | srcport, |
| --- | --------- | --- | --- | -------- |
waf
Parsers thFaortt inSetu FportpiGoatret Line3 Breaks in Messages Delivered overds tTipC, P
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
Most syslogsF tohrtainte ta Froer tsiMeanilt over TCP use ASCII LF (represented as \n) as a TRAILER character
proto),
to terminate individual messages within the larger transmission. (This is the non-transparent-
IRONSCALES IronTraps
 in RFC 6587 - Transmission of Syslog Messages Syslog
framing method described in section 3.4.2
| Sangfor NDR |     |     |     | (otherwise) |
| ----------- | --- | --- | --- | ----------- |
over TCP .) Unfortunately, if a log uses LF (\n) as a line break within a message, parsers
recognize it aSse gau rTa R(CAEIFL)ER character and split it into multiple parts, depending on the number of
line breaks involved. This results in the erroneous creation of multiple “messages” that are really
just parts of one single message.

There are exceptions however. The following parsers can receive logs delivered over TCP with
Versio
|     |     |     |     | P   |     |     | msg_origi |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- |
LF (\n) line bVreenadokrs-s bpeecciaficu CseEF t hPearsseer slo Igntsro idnuccleudd oer  fUixpedadt eHdEADmsEgR_o Lariingnkid t oT RReAleIaLsEe RNo ctehsaracters, which
| nParser Name                         |     |     |     | or Log Format |     |                              | n.categor | Index |
| ------------------------------------ | --- | --- | --- | ------------- | --- | ---------------------------- | --------- | ----- |
| the parsers use to isolate messages: |     |     |     |               |     | n.source                     |           |       |
|                                      |     |     |     | t             |     |                              | y         |       |
| 6.1.0                                |     |     |     |               |     | Stellar Cyber 6.1.0s Release |           |       |
Aliyun/AliCloud on port 5545 Cynet (CEF)
Notes
AirGap RGaingsaommownare Kill Switch 5 AirGap custom format airgap_ran saas Traffic (srcip,
Avanan on port 5681
|     |     |     |     | 6   |     | somware_k |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- |
srcport,
Seqrite Endpoint Security
|     | BeyondTrust BeyondInsight on port 5621 |     |     | 0   |     | ill_switch |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- |
dstip,
6.0.0CheckPoint Firewall on 2port 5519 Stellar Cyber 6.0.0sd Rsetpleoarts, eand
Cisco
Notes
proto),
FortiADC on port 5725
Cisco Email Security Appliance (ESA)
Syslog
Indusface Web Application Firewall on port 5582
|     | Cisco IronPort |     |     |     |     |     |     | (otherwise) |
| --- | -------------- | --- | --- | --- | --- | --- | --- | ----------- |
Monitorapp on port 5535
CyberArk
| AirWatch |     |     |     | CEF |     | airwatch | iot |                 |
| -------- | --- | --- | --- | --- | --- | -------- | --- | --------------- |
|          |     |     |     | 5   |     |          |     | Traffic (srcip, |
Radware DefenseFlow on port 6082
F5 BIG-IP ASM
|     |     |     |     | 1   |     |     |     | srcport, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- |
Splunk Heavy Forwarder on port 5188
|     | Fortinet                                 |     |     | 4   |     |     |     | dstip,       |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ |
|     | Veeam Backup & Replic3ation on port 5751 |     |     |     |     |     |     | dstport, and |
McAfee Enterprise Security Manager (ESM) / Nitro SIEM
|     |     |     |     | or  |     |     |     | proto), |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
Windows System Security on port 5610
Progress Kemp LoadMaste5r
Syslog
The  f o ll o w i n g   H T T P   J S O e8n N   p a r s e rs that listen on TCP 5200 also suppo(ortth eLrFwi slein)e breaks
|     | S y | m a n te c  D a t a  | Lo s s  P re | v tio n   (D | L P ) |     |     |     |
| --- | --- | -------------------- | ------------ | ------------ | ----- | --- | --- | --- |
within syslog messages7.
Zscaler
0
 When only one product is sending logs to TCP 5200 on a sensor, the URL doesn’t
| 5.5.0 |     |     |     |     |     | Stellar Cyber 5.5.0s Release |     |     |
| ----- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
AIX A ru b a  C l e a r P a s s ude the 5proIdBuMc ctu nstaomm efo rtmoa ti dfoerntifya iitx. Howeveurn,i xwlohgsen thTerraeffi cis more than
|     | n   | e e d   t o   i n c | l   |     |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Notes
Coisncoe  Iraonnpdo rytou want to5 difAfeIXrentiate them, include the product name(.e vEexnta_mtimpel:e for
Avanan: https://<2sensor_ip_addr>:5200/httpjson or time format
CyberArk Privileged Threat Analytics (PTA)
|     | https://<sensor_3ip_addr>:5200/httpjson_avanan |     |     |     |     |     |     | of  |
| --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Fortinet - Fortigate
hour:minute:
|     |     | Avanan – httpjson or httpjson_avanan |     |     |     |     |     | second), |
| --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | -------- |
Trellix EX (FireEye) / Trellix Email eXecution (FireEye)
Syslog
Bitdefender – httpjson or httpjson_bitdefender_multiple_event
| 5.4.0 |                                            |     |     |     |     | Stellar Cyber 5.4.0s Release |     |             |
| ----- | ------------------------------------------ | --- | --- | --- | --- | ---------------------------- | --- | ----------- |
|       | CyberArk Privileged Threat Analytics (PTA) |     |     |     |     |                              |     | (otherwise) |
ECS Suricata – httpjson or httpjson_ecs  N o o r t   ehsttpjson_ecs_suricata
Akamai WInAcaFp sula SIEM Integration6 CEF akamai_wa waf Traffic (srcip,
ECS Windows – httpjson or httpjson_ecs or httpjson_ecs_windows
|     |     |     |     | 0   |     | f   |     | srcport, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- |
Snowflake
|     |          | Egnyte – httpj6son or httpjson_egnyte |     |     |     |     |     | dstip,       |
| --- | -------- | ------------------------------------- | --- | --- | --- | --- | --- | ------------ |
|     | Teramind |                                       |     | 0   |     |     |     | dstport, and |
Exium SASE – httpjson or httpjson_exium_sase
|     | Trellix FireEye |     |     |     |     |     |     | proto), |
| --- | --------------- | --- | --- | --- | --- | --- | --- | ------- |
FS BIG-IP Telemetry – httpjson or httpjson_fs_telemetry_streaming
Syslog
Central Management System (CMS)
(otherwise)
|     |     | K Em ub ai e l M rn | a e lw t a e r s e    P – | r   ohtetcttiopnj Sseorvnic |  o e  r (   ehMtPtSp)json_kubernetes |     |     |     |
| --- | --- | ------------------- | ------------------------- | --------------------------- | ------------------------------------ | --- | --- | --- |
Email Threat Prevention (ETP)
|     |     | T h r e atLocker Z |     | ero  T | r u s t  E P P   –   shtotmtpjs | o n   o r |     |     |
| --- | --- | ------------------ | --- | ------ | ------------------------------- | --------- | --- | --- |
Alcatel-Lucent S w it c h 5 A lc a te l- L uc en t  c u a l ca t e l_luc netlogs Traffic (srcip,
File Malware Prevention System (fMPS)
h t t p j s o n _ t h r 6e a t f_orlmoactker_zero_trus t _ e p p srcport,
|     |     | H o st -b a | se d  e X p | er t  (H X ) |     | e n t_ sw i tch |     |     |
| --- | --- | ----------- | ----------- | ------------ | --- | --------------- | --- | --- |
From 5.3.M0a, lwSatreel lAanra lCysyisb Se7yrs tseump (pMoArSt)s HTTP JSON on other ports besidedss t5ip2, 00. The
following Mpaalrwsaerer sP raoltsecoti orne7 Scyesitveem  l(oMgPsS )formatted for HTTP JSON that condtsatpino rtL, Fan dline
proto),
breaZkscsa lweri t-h Ninan solyosg lSotgre ammeinsgs Saegrveicse: (NSS) Weblog
Syslog
HTTP ThreatLocker Zero Trust on port 5754
| 5.3.0 |           |                              |     |     |     | Stellar Cyber 5.3.0s Release |     |             |
| ----- | --------- | ---------------------------- | --- | --- | --- | ---------------------------- | --- | ----------- |
|       | Fortigate |                              |     |     |     |                              |     | (otherwise) |
|       |           | HTTP Winlogbeat on port 5752 |     |     |     | Notes                        |     |             |
Minerva Labs

In addition to the non-transparent-framing method to separate log messages, section 3.4.1  in
Versio
|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
Ve nd o r -sp e c i fic  C E F  P a rs er s  I nt ro d u c ed   or   U p d a t ed ms gd_eoL sriin cgk   to  R e le as e   N o te s
RFC 6587 - T ra n s m is s i o n  o f  S y s lo g   M e s s a g e s   o v e r   T CP rii b e s  a n o t h e r  m ethod: octet
| nParser Name | or Log Format |     | n.categor | Index |
| ------------ | ------------- | --- | --------- | ----- |
counting. The threatER Enforce parser (port 6073) suppornt.ss ooucrcteet-counted framing as defined in
| Trellix FireEye - Central Matnagement System (CMS) |     |     | y   |     |
| -------------------------------------------------- | --- | --- | --- | --- |
this RFC.
A l iy un   /  AT lri eCl lloi x u  Fdi re E y e  -  M a lw a re  P 5r o te c t io n   S y s t e m  ( M P S ) a l iy u n I D PS / M a lw a r
The Fo r t in e t   F o r t i A n a l y z e r  o n  p o r t  5 5 R 4 F2 C    s3 u1 6p 4 p  oor  rR tsF  C T  5C4P24 mu lt i - li ne mespsaaasges in < P R I >   k e y -value
|     | 5   |     |     | e   S a n d b o x |
| --- | --- | --- | --- | ----------------- |
n) +tr areigleexr separation, the parsSetre lildare Cnytibfieer s5 .2a. 0nse
format5.. 2In.0stead of relying on LF (\  R w e l em a se e s sage by
Aruba ClearPass Policy Ma4nager
Events
detecting a leading priority marker followed by a key-value strinNgo.t eOslder line-delimited TCP
|     | 5   |     |     | (threat), |
| --- | --- | --- | --- | --------- |
variants are nFoortt inseut pFporotirgtaeted.
Traffic (srcip,
The Fortinet IFBoMr AtiSG4a00te parser also supports octet-counted framing as well as non-transparent
srcport,
framing, checking the first character in a frame to determine which method is being used. If a log
| Infocyte HUNT |     |     |     | dstip, |
| ------------- | --- | --- | --- | ------ |
sent to the Fortinet FortiGate parser on TCP port 5517 contains an LF (\n) line break, then the
| Trend Micro Apex Central |     |     |     | dstport, and |
| ------------------------ | --- | --- | --- | ------------ |
octet-counting method must be used. Otherwise, either method works.
proto),
In summary, only the parsers listed above can process logs that include \n andS yasrloeg sent over
TCP. All parsers support logs sent over UDP because a UDP datagram contain(sot hjuerswti soen) e syslog
message inside; therefore, parsers don’t need to separate multiple syslog messages from a
Amazon Web Services WAF 5 RFC 3164 + Logstash aws_waf waf Traffic (srcip,
single transmission.
|     | 7 header + JSON |     |     | srcport,     |
| --- | --------------- | --- | --- | ------------ |
|     | 3               |     |     | dstip,       |
|     | 5               |     |     | dstport, and |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
proto),
|     |     |     | Support |   |  Contact Us   |            |
| --- | --- | --- | ------- | -------------------------------- |
Syslog
(otherwise)
|         | 5 Google custom format |         | unixlogs |                 |
| ------- | ---------------------- | ------- | -------- | --------------- |
| Android |                        | android |          | Traffic (srcip, |
6 for Android
srcport,
|     | 0   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
5
dstport, and
proto),
Syslog
(otherwise)
|     | 5 RFC 5424 + regex | antaira_swi | netlogs | Traffic (srcip, |
| --- | ------------------ | ----------- | ------- | --------------- |
Antaira Switch
|     | 8   | tch |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Apache HTTP Server (HTTPD) 5 RFC 3164 + custom apache_htt weblogs Traffic (srcip,
|     | 6 header + regex | pd  |     | srcport,     |
| --- | ---------------- | --- | --- | ------------ |
|     | 6                |     |     | dstip,       |
|     | 3                |     |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
AQTRONiX WebKnight
|     | 5 AQTRONiX custom | aqtronix_w | waf | Traffic (srcip, |
| --- | ----------------- | ---------- | --- | --------------- |
|     | 6 format          |            |     | srcport,        |
ebknight
|     | 5   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|                               | 5 RFC 3164 + regex + |            | paas | Traffic (srcip, |
| ----------------------------- | -------------------- | ---------- | ---- | --------------- |
| Aqua Cloud Native Application |                      | aquasecuri |      |                 |
|                               | 6 KVP                |            |      | srcport,        |
| Protection Platform (CNAPP    |                      | ty_cnapp   |      |                 |
| 2022.4)                       | 5                    |            |      | dstip,          |
|                               | 6                    |            |      | dstport, and    |
proto),
Syslog
(otherwise)
Arbor Peakflow SP 5 Arbor Networks custom arbor_peak traffic Traffic (srcip,
|     | 5 format | flow_sp |     | srcport,     |
| --- | -------- | ------- | --- | ------------ |
|     | 9        |         |     | dstip,       |
|     | 8        |         |     | dstport, and |
proto),
Syslog
(otherwise)
|            | 5 JSON |           | iam | Traffic (srcip, |
| ---------- | ------ | --------- | --- | --------------- |
| Arcon PAM  |        | arcon_pam |     |                 |
|            | 8      |           |     | srcport,        |
|            | 8      |           |     | dstip,          |
|            | 7      |           |     | dstport, and    |
proto),
Syslog
(otherwise)
Arista Networks Data Center 5 RFC 3164 (with time arista_data netlogs Traffic (srcip,
|     | 7 zone and year in | _center_sw |     | srcport, |
| --- | ------------------ | ---------- | --- | -------- |
Switch Router
|     | 4 timestamp) | itch_router |     | dstip,       |
| --- | ------------ | ----------- | --- | ------------ |
|     | 7            |             |     | dstport, and |
proto),
Syslog
(otherwise)
Array Networks APV Series 5 regex (specific to log_id) Traffic (srcip,
|                               |     | array_netw | netlogs |          |
| ----------------------------- | --- | ---------- | ------- | -------- |
| Load Balancing & App Delivery | 6   |            |         | srcport, |
orks_apv
|     | 8   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 0   |     |     | dstport, and |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
Array Networks ASF 1800 5 regex + KVP array_netw waf Traffic (srcip,
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
orks_asf_1
|     | 7   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
800
|     | 5   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Array Networks Secure Access 5 RFC 3164 array_sag vpn Traffic
| Gateway                | 5   |            |     | (srcip),        |
| ---------------------- | --- | ---------- | --- | --------------- |
|                        | 3   |            |     | Syslog          |
|                        | 7   |            |     | (otherwise)     |
| Aruba ClearPass Policy | CEF | aruba_clea | iam | Traffic (srcip, |
5
| Manager (CEF) |     | r_pass |     | srcport, |
| ------------- | --- | ------ | --- | -------- |
1
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
| Aruba Switch | 5   | aruba_swit |     | Traffic (srcip, |
| ------------ | --- | ---------- | --- | --------------- |
netlogs
RFC 3164 or RFC 5424
|     | 5   | ch  |     | srcport, |
| --- | --- | --- | --- | -------- |
+ KVP
|     | 7   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Attrelogix EaziCloud | RFC 3164 |             | netlogs |                 |
| -------------------- | -------- | ----------- | ------- | --------------- |
|                      | 5        | attrelogix_ |         | Traffic (srcip, |
|                      | 9        | eazicloud   |         | srcport,        |
|                      | 0        |             |         | dstip,          |
|                      | 5        |             |         | dstport, and    |
proto),
Syslog
(otherwise)
| Automox | 5                     | automox |       | Syslog |
| ------- | --------------------- | ------- | ----- | ------ |
|         | Automox custom format |         | patch |        |
1

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
8
3
| Avanan | 5 RFC 5424 + custom | avanan | email | Traffic (srcip, |
| ------ | ------------------- | ------ | ----- | --------------- |
|        | 6 regex             |        |       | srcport,        |
|        | 8                   |        |       | dstip,          |
|        | 1                   |        |       | dstport, and    |
proto),
Syslog
(otherwise)
| Avanan (HTTP JSON) | 5 HTTP JSON | avanan | email | Syslog |
| ------------------ | ----------- | ------ | ----- | ------ |
2
0
0
(T
C
P
o
nl
y)
|     | RFC 3164 |            | voip |                 |
| --- | -------- | ---------- | ---- | --------------- |
|     | 6        | avaya_ip_o |      | Traffic (srcip, |
Avaya IP Office
|     | 0   | ffice |     | srcport,     |
| --- | --- | ----- | --- | ------------ |
|     | 9   |       |     | dstip,       |
|     | 9   |       |     | dstport, and |
proto),
Syslog
(otherwise)
|              | 5 Avaya custom format |            | netlogs |                 |
| ------------ | --------------------- | ---------- | ------- | --------------- |
| Avaya Switch |                       | avaya_swit |         | Traffic (srcip, |
|              | 6                     | ch         |         | srcport,        |
0
dstip,
7
dstport, and
proto),
Syslog
(otherwise)
|     | RFC 3164 |               | firewall |                 |
| --- | -------- | ------------- | -------- | --------------- |
|     | 5        | aviatrix_fire |          | Traffic (srcip, |
Aviatrix Firewall
|     | 7   | wall |     | srcport,     |
| --- | --- | ---- | --- | ------------ |
|     | 6   |      |     | dstip,       |
|     | 2   |      |     | dstport, and |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
|                 | 6 JSON | aws_cloud | saas |                 |
| --------------- | ------ | --------- | ---- | --------------- |
| AWS CloudWatch  |        |           |      | Traffic (srcip, |
|                 | 0      | watch     |      | srcport,        |
7
dstip,
1
dstport, and
proto),
Syslog
(otherwise)
| AWS WAF (HTTP JSON) | 5 HTTP JSON |         | waf |        |
| ------------------- | ----------- | ------- | --- | ------ |
|                     |             | aws_waf |     | Syslog |
2
0
0
(T
C
P
o
nl
y)
AXGATE Next Generation 5 RFC 3164 + KVP axgate_ngf firewall Traffic (srcip,
| Firewall | 7   |     |     |          |
| -------- | --- | --- | --- | -------- |
|          |     | w   |     | srcport, |
0
dstip,
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Azure ATP (CEF) | CEF | azure_atp | iam | Traffic (srcip, |
| --------------- | --- | --------- | --- | --------------- |
5
srcport,
1
dstip,
4
dstports, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                 | t               |            | y     |             |
| --------------- | --------------- | ---------- | ----- | ----------- |
| Azure MFA       | 5               | azure_mfa  |       | Traffic     |
|                 | custom RFC 3164 |            | iam   |             |
|                 | 5               |            |       | (srcip),    |
|                 | 2               |            |       | Syslog      |
|                 | 8               |            |       | (otherwise) |
| Barracuda email | 5               | barracuda_ |       | IDPS/Malwar |
|                 | JSON            |            | email |             |
|                 | 5               | email      |       | e Sandbox   |
|                 | 5               |            |       | Events      |
|                 | 9               |            |       | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Barracuda firewall | 5                  | barracuda_ |          | IDPS/Malwar |
| ------------------ | ------------------ | ---------- | -------- | ----------- |
|                    | Barracuda Networks |            | firewall |             |
|                    | 5                  | fw         |          | e Sandbox   |
custom format
|     | 2   |     |     | Events      |
| --- | --- | --- | --- | ----------- |
|     | 4   |     |     | (sub_dev_ty |
pe: fw_threat
or fw_av),
Traffic
(srcip),
Syslog
(otherwise)
| Barracuda WAF | 5                  | barracuda_ |     | IDPS/Malwar |
| ------------- | ------------------ | ---------- | --- | ----------- |
|               | Barracuda Networks |            | waf |             |
|               | 5 custom format    | waf        |     | e Sandbox   |
|               | 2                  |            |     | Events      |
|               | 4                  |            |     | (sub_dev_ty |
pe: fw_threat
or fw_av),
Traffic
(srcip),
Syslog
(otherwise)
|                | 5 RFC 5424 + regex |            | waf | Traffic (srcip, |
| -------------- | ------------------ | ---------- | --- | --------------- |
| Barracuda WAF  |                    | barracuda_ |     |                 |
|                | 8                  | waf        |     | srcport,        |
|                | 8                  |            |     | dstip,          |
|                | 0                  |            |     | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| BeyondTrust BeyondInsight | 5 regex + KVP |            | iam |                 |
| ------------------------- | ------------- | ---------- | --- | --------------- |
|                           |               | beyondtrus |     | Traffic (srcip, |
|                           | 6             | t_beyondin |     | srcport,        |
2
|     |     | sight |     | dstip, |
| --- | --- | ----- | --- | ------ |
1
dstport, and
proto),
Syslog
(otherwise)
| BeyondTrust PasswordSafe | 5 RFC 3164 + KVP |            |     | Traffic (srcip, |
| ------------------------ | ---------------- | ---------- | --- | --------------- |
|                          |                  | beyondtrus | iam |                 |
|                          | 6                |            |     | srcport,        |
t_password
|     | 9   | safe |     | dstip,       |
| --- | --- | ---- | --- | ------------ |
|     | 2   |      |     | dstport, and |
proto),
Syslog
(otherwise)
| BIO-key PortalGuard | RFC 5424 + regex |            | iam |                 |
| ------------------- | ---------------- | ---------- | --- | --------------- |
|                     | 5                | bio_key_po |     | Traffic (srcip, |
|                     | 9                | rtalguard  |     | srcport,        |
|                     | 5                |            |     | dstip,          |
|                     | 4                |            |     | dstport, and    |
proto),
Syslog
(otherwise)
Bitdefender (HTTP JSON) 5 HTTP JSON or syslog bitdefender endpoint
Traffic (srcip,
2 JSON
| (Syslog JSON) |     |     |     | srcport, |
| ------------- | --- | --- | --- | -------- |
|               | 0   |     |     | dstip,   |
Click here to configure log
0
| ingestion |     |     |     | dstport, and |
| --------- | --- | --- | --- | ------------ |
(T
proto),
C
Syslog
P
(otherwise)
o
nl
y)
5
1
4
2
| BlackBerry CylancePROTECT | 5   |         |          | Traffic  |
| ------------------------- | --- | ------- | -------- | -------- |
|                           | KVP | cylance | endpoint |          |
| & CylanceOPTICS           | 1   |         |          | (srcip), |
cylance_op

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |            | y   |             |
| --- | --- | ---------- | --- | ----------- |
|     | 7   | tics       |     | Syslog      |
|     | 7   | cylance_pr |     | (otherwise) |
otect
BlueCoat Proxy SG 5 Broadcom custom format bluecoat_p websec Traffic (srcip,
|     | 5   | roxysg |     | srcport,     |
| --- | --- | ------ | --- | ------------ |
|     | 7   |        |     | dstip,       |
|     | 6   |        |     | dstport, and |
proto),
Syslog
(otherwise)
| Brocade switch (system & | 5                | brocade_s |         | Traffic (srcip, |
| ------------------------ | ---------------- | --------- | ------- | --------------- |
|                          | RFC 3164 + regex |           | netlogs |                 |
| admin logs)              | 5                | witch     |         | srcport,        |
|                          | 4                |           |         | dstip,          |
|                          | 8                |           |         | dstport, and    |
proto),
Syslog
(otherwise)
| BullWall RansomCare | Timestamp + regex + |     | siem |     |
| ------------------- | ------------------- | --- | ---- | --- |
5
|     |     | bullwall_ra |     | Traffic (srcip, |
| --- | --- | ----------- | --- | --------------- |
9 HTML
|     |     | nsomcare |     | srcport, |
| --- | --- | -------- | --- | -------- |
|     | 2   |          |     | dstip,   |
8
dstport,
proto),
Syslog
(otherwise)
| Calyptix UTM | 5   | calyptix |          | IDPS/Malwar   |
| ------------ | --- | -------- | -------- | ------------- |
|              | KVP |          | firewall |               |
|              | 1   |          |          | e Sandbox     |
|              | 6   |          |          | Events        |
|              | 1   |          |          | (ids.signatur |
e), Traffic
(srcip),
Syslog
(otherwise)
Cato Networks Cato Security 6 Cato Networks custom cato_netwo cloudsec Traffic (srcip,
JSON
|     | 0   | rks_cato_s |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 9   | ecurity    |     | dstip,       |
|     | 4   |            |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|              | t     |           | y        |                 |
| ------------ | ----- | --------- | -------- | --------------- |
| Centos Audit | 5 KVP | centos_au | unixlogs | Traffic (srcip, |
|              | 6     | dit       |          | srcport,        |
|              | 7     |           |          | dstip,          |
|              | 3     |           |          | dstport, and    |
proto),
Syslog
(otherwise)
| Centrify | 5 KVP | centrify | iam | Syslog |
| -------- | ----- | -------- | --- | ------ |
1
6
5
Cerberus FTP Logs 5 regex cerverus_ft unixlogs Traffic (srcip,
|     | 6   | p   |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Check Point - Application |       |           |          | IDPS/Malwar |
| ------------------------- | ----- | --------- | -------- | ----------- |
|                           | 5 CEF | fw_checkp | firewall |             |
| Control (CEF)             |       | oint      |          | e Sandbox   |
1
Events
4
(threat,
3
normalized
or
from
5
attack_infor
8
mation),
7
Traffic (srcip,
0
srcport,dstip,
dstport, and
proto),
Syslog
(otherwise)
| Check Point - SmartConsole | CEF |            | netmgmt |             |
| -------------------------- | --- | ---------- | ------- | ----------- |
|                            | 5   | checkpoint |         | IDPS/Malwar |
_smart_co
| (CEF)  | 1   |     |     | e Sandbox |
| ------ | --- | --- | --- | --------- |
nsole
|     | 4   |     |     | Events       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | (threat_norm |
|     | or  |     |     | alized from  |
|     | 5   |     |     | attack_infor |
|     | 8   |     |     | mation),     |
Traffic (srcip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |          |
| --- | --- | --- | --- | -------- |
|     | 7   |     |     | srcport, |
|     | 0   |     |     | dstip,   |
dstport,
proto),
Syslog
(otherwise)
| Check Point - Smart Defense | CEF |            | idps |             |
| --------------------------- | --- | ---------- | ---- | ----------- |
|                             | 5   | checkpoint |      | IDPS/Malwar |
|                             | 1   | _smart_def |      | e Sandbox   |
(CEF)
ense
|     | 4   |     |     | Events          |
| --- | --- | --- | --- | --------------- |
|     | 3   |     |     | (threat_norm    |
|     | or  |     |     | alized from     |
|     | 5   |     |     | attack_infor    |
|     | 8   |     |     | mation),        |
|     | 7   |     |     | Traffic (srcip, |
|     | 0   |     |     | srcport,        |
dstip,
dstport,
proto),
Syslog
(otherwise)
| Check Point - URL Filtering |       |           |          | IDPS/Malwar |
| --------------------------- | ----- | --------- | -------- | ----------- |
|                             | 5 CEF | fw_checkp | firewall |             |
| (CEF)                       |       |           |          | e Sandbox   |
oint
1
Events
4
(threat,
3
normalized
or
from
5
attack_infor
8
mation),
7
Traffic (srcip,
0
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Check Point Harmony Mobile | priority + KVP |            | endpoint |                 |
| -------------------------- | -------------- | ---------- | -------- | --------------- |
|                            | 6              | checkpoint |          | Traffic (srcip, |
|                            | 0              | _harmony_  |          | srcport,        |
|                            | 6              | mobile     |          | dstip,          |
|                            | 7              |            |          | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
Check Point Quantum 5 Check Point custom checkpoint firewall Traffic (srcip,
syslog
|     | 9   | _quantum |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 2   |          |     | dstip,       |
|     | 0   |          |     | dstport, and |
proto),
Syslog
(otherwise)
| Check Point SandBlast | Check Point custom |     | idps |     |
| --------------------- | ------------------ | --- | ---- | --- |
5
|     |     | check_poin |     | IDPS/Malwar |
| --- | --- | ---------- | --- | ----------- |
9 syslog
| Appliance  |     | t_sandblast |     | e Sandbox |
| ---------- | --- | ----------- | --- | --------- |
|            | 1   | _appliance  |     | Events    |
5
(threat or
ips), Traffic
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
CheckPoint appliance 5 KVP fw_checkp firewall Traffic (srcip,
|     | 1   | oint_applia |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 7   | nce         |     | dstip,       |
|     | 4   |             |     | dstport, and |
proto),
Syslog
(otherwise)
| CheckPoint firewall | 5                     | fw_checkp |          | Traffic  |
| ------------------- | --------------------- | --------- | -------- | -------- |
|                     | RFC 5424 + KVP inside |           | firewall |          |
|                     | 5                     | oint      |          | (srcip), |
structured data (SD)
|                            | 1                       |             |       | Syslog          |
| -------------------------- | ----------------------- | ----------- | ----- | --------------- |
|                            | 9                       |             |       | (otherwise)     |
| CheckPoint Harmony Email & | checkpoint-specific RFC |             | email |                 |
|                            | 5                       | checkpoint  |       | Traffic (srcip, |
|                            | 8 5425-like syslog      |             |       | srcport,        |
| Collaboration              |                         | _harmony_   |       |                 |
|                            | 7                       | email_colla |       | dstip,          |
|                            | 9                       | boration    |       | dstport, and    |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
CheckPoint Harmony EP 5 regex + KVP checkpoint endpoint Traffic (srcip,
|     | 6   | _harmony_ |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 1   | ep        |     | dstip,       |
|     | 8   |           |     | dstport, and |
proto),
Syslog
(otherwise)
CheckPoint SmartCenter 5 RFC 5424 checkpoint saas Traffic (srcip,
|     | 7   | _smartcent |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 4   | er         |     | dstip,       |
|     | 1   |            |     | dstport, and |
proto),
Syslog
(otherwise)
IDPS/Malwar
| CheckPoint VPN-1 & FireWall-1 | 5 CEF | fw_checkp | firewall |     |
| ----------------------------- | ----- | --------- | -------- | --- |
e Sandbox
(CEF)
|     | 1   | oint |     |     |
| --- | --- | ---- | --- | --- |
Events
4
(threat,
3
normalized
or
from
5
attack_infor
8
mation),
7
Traffic (srcip,
0
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
Cisco ACI 5 two log formats cisco_aci netmgmt Traffic (srcip,
7
srcport,
|     | 1   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Cisco ASA | 5 Cisco Systems custom | fw_cisco_a | firewall | Traffic  |
| --------- | ---------------------- | ---------- | -------- | -------- |
|           | 5                      | sa         |          | (srcip), |
format
|     | 1   |     |     | Syslog      |
| --- | --- | --- | --- | ----------- |
|     | 8   |     |     | (otherwise) |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Cisco Catalyst Firewal l 5 regex + description cisco_catal firewall Traffic (srcip,
7
|     |     | yst_fw |     | srcport, |
| --- | --- | ------ | --- | -------- |
0
dstip,
|     | 2   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Cisco Catalyst SD-WAN 5 NetFlow v9 cisco_sd_ netmgmt Traffic (srcip,
|     | 7   | wan |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Cisco CUCM | 5              | cisco_cuc |      | Syslog |
| ---------- | -------------- | --------- | ---- | ------ |
|            | syslog + regex |           | voip |        |
|            | 5              | m         |      |        |
3
2
| Cisco ESA | 5                    | cisco_esa |       | IDPS/Malwar |
| --------- | -------------------- | --------- | ----- | ----------- |
|           | Cisco Systems custom |           | email |             |
|           | 5 format             |           |       | e Sandbox   |
|           | 6                    |           |       | Events      |
|           | 2                    |           |       | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Cisco ESA | 5                    | openldap_ |       | Syslog |
| --------- | -------------------- | --------- | ----- | ------ |
|           | Cisco Systems custom |           | email |        |
|           | 1                    | style     |       |        |
format
6
4
(d
e
pr
ec
at
e
d)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                 | t   |             | y        |             |
| --------------- | --- | ----------- | -------- | ----------- |
| Cisco Firepower | 5   | ips_fire_po |          | Traffic     |
|                 | KVP |             | firewall |             |
|                 | 1   | wer         |          | (srcip),    |
|                 | 6   |             |          | Syslog      |
|                 | 8   |             |          | (otherwise) |
| Cisco IKE       | 5   | ciscovpn    |          |             |
|                 | KVP |             | vpn      | Syslog      |
1
7
6
| Cisco IronPort | 5                    | cisco_ironp |       |        |
| -------------- | -------------------- | ----------- | ----- | ------ |
|                | Cisco Systems custom |             | email | Syslog |
|                | 1 format             | ort         |       |        |
6
3
| Cisco IronPort (CEF) | 5 CEF |     | email | Traffic (srcip, |
| -------------------- | ----- | --- | ----- | --------------- |
cisco_ironp
|     | 1   | ort |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| Cisco ISE | 5 KVP | ciscoise | asset | Syslog |
| --------- | ----- | -------- | ----- | ------ |
1
5
7
| Cisco MDS | 5                | cisco_mds |         | IDPS/Malwar |
| --------- | ---------------- | --------- | ------- | ----------- |
|           | RFC 3164 + regex |           | netlogs |             |
|           | 5                |           |         | e Sandbox   |
|           | 6                |           |         | Events      |
|           | 3                |           |         | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Cisco Meraki | 5 syslog + regex | meraki | firewall |     |
| ------------ | ---------------- | ------ | -------- | --- |
Traffic (srcip,
1
srcport,
7
dstip,
2

P msg_origi
msg_origi
Parser Name or Log Format n.categor Index
n.source
t y
dstport, and
proto)
IDPS/Malwar
e Sandbox
Events
(threat, or
device_event
_category,
msg,
signature,
and
event_severi
ty),
Syslog
(otherwise)
Cisco Meraki 5 Custom Cisco Meraki cisco_mera firewall Traffic
9 syslog format ki (src_ip,
3 src_port,
1 dst_ip,
dst_port,
protocol),
Syslog
(otherwise)
IDPS/Malwar
e Sandbox
Events
(threat, or
device_event
_category,
msg,
signature,
and
event_severi
ty)
Syslog
(otherwise)
Cisco NetFlow 2 NetFlow v5 and v9 netflow traffic Traffic
0
5

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
5
(U
D
P
o
nl
y)
| Cisco routers and switches | 5                    | cisco_route |         |        |
| -------------------------- | -------------------- | ----------- | ------- | ------ |
|                            | Cisco Systems custom |             | netlogs | Syslog |
|                            | 1                    | r_switch    |         |        |
format
5
8
Cisco Secure Network Analytics 5 RFC 3164 + KVP cisco_secu ndr Traffic (srcip,
| (Stealthwatch) | 7   |            |     |          |
| -------------- | --- | ---------- | --- | -------- |
|                |     | re_network |     | srcport, |
|                | 1   | _analytics |     | dstip,   |
9
dstport, and
proto),
Syslog
(otherwise)
| Cisco UCS | 5                  | cisco_ucs |          | Traffic (srcip, |
| --------- | ------------------ | --------- | -------- | --------------- |
|           | RFC 5424 + (regex) |           | unixlogs |                 |
|           | 5                  |           |          | srcport,        |
|           | 7                  |           |          | dstip,          |
|           | 9                  |           |          | dstport, and    |
proto),
Syslog
(otherwise)
| Cisco Umbrella | 5   | cisco_umbr |        |        |
| -------------- | --- | ---------- | ------ | ------ |
|                | CSV |            | dnssec | Syslog |
|                | 5   | ella       |        |        |
2
1
| Cisco VPN | 5                    | ciscovpn |     |        |
| --------- | -------------------- | -------- | --- | ------ |
|           | Cisco Systems custom |          | vpn | Syslog |
1 format
5
6
| Cisco WLC | 5 syslog (regex) | cisco_wlc | wireless | Syslog |
| --------- | ---------------- | --------- | -------- | ------ |
5
3
1
|     | 6 RFC 3164 | cisco_wsa | web | Traffic (srcip, |
| --- | ---------- | --------- | --- | --------------- |
Cisco WSA
|     | 0   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
dstip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
|     | 4   |     |     | proto),      |
Syslog
(otherwise)
|     | 6 RFC 5424 | citrix_adc | vpn | Traffic (srcip, |
| --- | ---------- | ---------- | --- | --------------- |
Citrix ADC
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Citrix Access Gateway 5 Citrix Systems custom citrix_acce iam Traffic (srcip,
|     | 6 format |     |     | srcport, |
| --- | -------- | --- | --- | -------- |
ss_gatewa
|     | 8   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
y
|     | 8   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Citrix NetScaler | 5 KVP | netscaler | netmgmt | Syslog |
| ---------------- | ----- | --------- | ------- | ------ |
1
6
6
| Citrix NetScaler (CEF) | CEF | netscaler | netmgmt | Traffic (srcip, |
| ---------------------- | --- | --------- | ------- | --------------- |
5
srcport,
1
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
|     | 5 RFC 3164 + regex | citrix_xens | paas | Traffic (srcip, |
| --- | ------------------ | ----------- | ---- | --------------- |
Citrix XenServer
|     | 7   | erver |     | srcport,     |
| --- | --- | ----- | --- | ------------ |
|     | 3   |       |     | dstip,       |
|     | 2   |       |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |     |
| --- | --- | --- | --------- | --- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |     |
| ----------- | ------------- | --- | --------- | ----- | --- |
n.source
|     | t           |             | y        |                 |     |
| --- | ----------- | ----------- | -------- | --------------- | --- |
|     | regex + KVP |             | firewall |                 |     |
|     | 5           | clavister_n |          | Traffic (srcip, |     |
Clavister NetWall
|     | 7   | etwall |     | srcport,     |     |
| --- | --- | ------ | --- | ------------ | --- |
|     | 6   |        |     | dstip,       |     |
|     | 0   |        |     | dstport, and |     |
proto),
Syslog
(otherwise)
|     | 5 Custom syslog + JSON | cloudflare | cloudsec | Traffic (srcip, |     |
| --- | ---------------------- | ---------- | -------- | --------------- | --- |
Cloudflare
|     | 9   |     |     | srcport,     |     |
| --- | --- | --- | --- | ------------ | --- |
|     | 4   |     |     | dstip,       |     |
|     | 5   |     |     | dstport, and |     |
proto),
Syslog
(otherwise)
|     | RFC 3164 header with |          | storage |                 |     |
| --- | -------------------- | -------- | ------- | --------------- | --- |
|     | 5                    | cohesity |         | Traffic (srcip, |     |
Cohesity
RFC 5424 timestamp
|     | 9   |     |     | srcport,     |     |
| --- | --- | --- | --- | ------------ | --- |
|     | 4   |     |     | dstip,       |     |
|     | 2   |     |     | dstport, and |     |
proto),
Syslog
(otherwise)
|     | 5 JSON | col |     | mis | For |
| --- | ------ | --- | --- | --- | --- |
ColorTokens
|     |     | orto |     | c (if | Xshie |
| --- | --- | ---- | --- | ----- | ----- |
8
|     |     | ken   |     | the | ld:    |
| --- | --- | ----- | --- | --- | ------ |
|     |     | s (if |     | pro |        |
|     | 8   | the   |     | duc | Traffi |
c (if
|     |     | pro |     | t_n |        |
| --- | --- | --- | --- | --- | ------ |
|     | 4   |     |     |     | srcip, |
|     |     | duc |     | am  |        |
dstip,
|     |     | t_n |     | e    |       |
| --- | --- | --- | --- | ---- | ----- |
|     |     | am  |     | fiel | dstpo |
|     |     | e   |     | d is | rt,   |
and
|     |     | fiel |     | em  |     |
| --- | --- | ---- | --- | --- | --- |
proto
|     |     | d is |     | pty |     |
| --- | --- | ---- | --- | --- | --- |
conta
|     |     | em  |     | or  |       |
| --- | --- | --- | --- | --- | ----- |
|     |     | pty |     | an  | in    |
|     |     | or  |     | uns | data) |
|     |     | an  |     | upp |       |
Syslo
|     |     | uns  |     | ort | g     |
| --- | --- | ---- | --- | --- | ----- |
|     |     | upp  |     | ed  | (othe |
|     |     | orte |     | val |       |
rwise
|     |     | d   |     | ue) |     |
| --- | --- | --- | --- | --- | --- |
)
val
fire
|     |     | ue) |     |     | For |
| --- | --- | --- | --- | --- | --- |
wal
all
|     |     | col  |     | l (if | other |
| --- | --- | ---- | --- | ----- | ----- |
|     |     | orto |     | pro   | s     |
|     |     | ken  |     | duc   |       |
(Gate
|     |     | s_x |     | t_n |     |
| --- | --- | --- | --- | --- | --- |
keep
|     |     | shi |     | am  |     |
| --- | --- | --- | --- | --- | --- |
er,
|     |     | eld |     | e is | Xprot |
| --- | --- | --- | --- | ---- | ----- |
|     |     | (if |     | xsh  | ect,  |
|     |     | pro |     | ield |       |
or
|     |     | duc |     | )   |     |
| --- | --- | --- | --- | --- | --- |
unide
t _ n
|     |     |     |     | e n d | n t i f ie |
| --- | --- | --- | --- | ----- | ---------- |
|     |     | a m |     |       | d          |
|     |     |     |     | p o i |            |
|     |     | e   | i s |       | s o u rc   |
|     |     | x s | h i | n t   |            |
e ) :
|     |     | e ld | )   | (if |     |
| --- | --- | ---- | --- | --- | --- |

)
|     | P   |     | msg_origi |     |     |
| --- | --- | --- | --------- | --- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |     |
| ----------- | ------------- | --- | --------- | ----- | --- |
n.source
|     | t   |      | y   |      |        |
| --- | --- | ---- | --- | ---- | ------ |
|     |     | col  |     | pro  | Traffi |
|     |     | orto |     | duc  | c (if  |
|     |     | ken  |     | t_n  | srcip, |
|     |     | s_g  |     | am   | srcpo  |
|     |     | ate  |     | e is | rt,    |
|     |     | kee  |     | gat  | dstip, |
|     |     | per  |     | eke  | dstpo  |
|     |     | (if  |     | epe  | rt,    |
|     |     | pro  |     | r)   | and    |
|     |     | duc  |     |      | proto  |
xdr
|     |     | t_n |     |     | conta |
| --- | --- | --- | --- | --- | ----- |
(if
|     |     | am  |     |     | in  |
| --- | --- | --- | --- | --- | --- |
pro
|     |     | e is |     |     | data) |
| --- | --- | ---- | --- | --- | ----- |
|     |     | gat  |     | duc |       |
|     |     | eke  |     | t_n | Syslo |
|     |     |      |     | am  | g     |
epe
|     |     |     |     | e is | (othe |
| --- | --- | --- | --- | ---- | ----- |
r)
|     |     |      |     | xpr | rwise |
| --- | --- | ---- | --- | --- | ----- |
|     |     | col  |     | ote | )     |
|     |     | orto |     | ct) |       |
ken
s_x
prot
ect
(if
pro
duc
t_n
am
e is
xpr
ote
ct)
Commvault Commserve 5 regex + KVP commvault paas Traffic (srcip,
|     | 7   | _commser |     | srcport,     |     |
| --- | --- | -------- | --- | ------------ | --- |
|     | 4   | ve       |     | dstip,       |     |
|     | 0   |          |     | dstport, and |     |
proto),
Syslog
(otherwise)
Commvault Metallic ThreatWise 5 RFC 3164 + regex commvault mdr Traffic (srcip,
|     | 7   | _metallic_t |     | srcport,     |     |
| --- | --- | ----------- | --- | ------------ | --- |
|     | 3   | hreatwise   |     | dstip,       |     |
|     | 6   |             |     | dstport, and |     |
proto),
Syslog
(otherwise)
| Comodo- CIS CCS (CEF) | CEF | comodo | endpoint | Traffic (srcip, |     |
| --------------------- | --- | ------ | -------- | --------------- | --- |
5
|     | 1   |     |     | srcport, |     |
| --- | --- | --- | --- | -------- | --- |
|     | 4   |     |     | dstip,   |     |
dstport, and
3
|     | or  |     |     | proto), |     |
| --- | --- | --- | --- | ------- | --- |
Syslog
5
(otherwise)
8

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
7
0
ConnectWise ScreenConnect 5 RFC 5424 (with custom connectwis remote_ac Traffic (srcip,
|     | 7 structured data using | e_screenc | cess | srcport,     |
| --- | ----------------------- | --------- | ---- | ------------ |
|     | 4 KVP)                  | onnect    |      | dstip,       |
|     | 4                       |           |      | dstport, and |
proto),
Syslog
(otherwise)
| Coraza WAF (HAProxy SPOA) | RFC 3164 |            | waf |                 |
| ------------------------- | -------- | ---------- | --- | --------------- |
|                           | 5        | coraza_waf |     | Traffic (srcip, |
|                           | 9        | _spoa      |     | srcport,        |
|                           | 1        |            |     | dstip,          |
|                           | 3        |            |     | dstport, and    |
proto),
Syslog
(otherwise)
|     | 5    | corelight_s |        | Traffic (srcip, |
| --- | ---- | ----------- | ------ | --------------- |
|     | JSON |             | websec |                 |
CoreLight Sensor
|     | 5   | ensor |     | srcport, |
| --- | --- | ----- | --- | -------- |
Click here to configure log
|           | 7   |     |     | dstip,       |
| --------- | --- | --- | --- | ------------ |
| ingestion | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
CoSoSys Endpoint Protection 5 RFC 5424 + custom KVP cososys endpoint Traffic (srcip,
|     | 6   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Cowrie SSH/Telnet Honeypot | JSON |            | honeypot |                 |
| -------------------------- | ---- | ---------- | -------- | --------------- |
|                            | 6    | cowrie_ssh |          | Traffic (srcip, |
|                            | 2    | _telnet_ho |          | srcport,        |
|                            | 0    | neypot     |          | dstip,          |
|                            | 6    |            |          | dstport, and    |
proto),
Syslog
(otherwise)
| Cribl default (Syslog JSON) | 5 JSON | json | xdr |     |
| --------------------------- | ------ | ---- | --- | --- |
Traffic (srcip,
|     | 1   |     |     | srcport, |
| --- | --- | --- | --- | -------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Cribl / NXLog | 5 JSON | microsoft | endpoint |     |
| ------------- | ------ | --------- | -------- | --- |
Windows
| (log -> NXLog ->Cribl) | 1   |     |     | Events |
| ---------------------- | --- | --- | --- | ------ |
| (Syslog JSON)          | 4   |     |     |        |
2
| CrowdStrike (Beats) | 5    |             |          |        |
| ------------------- | ---- | ----------- | -------- | ------ |
|                     | JSON | crowdstrike | endpoint | Syslog |
0
4
4
CrowdStrike (CEF)
|     | 5 CEF | crowd_strik | endpoint | Traffic (srcip, |
| --- | ----- | ----------- | -------- | --------------- |
|     | 1     | e_falcon_h  |          | srcport,        |
|     | 4     | ost         |          | dstip,          |
|     | 3     |             |          | dstport, and    |
|     | or    |             |          | proto),         |
|     | 5     |             |          | Syslog          |
|     | 8     |             |          | (otherwise)     |
7
0
| CTM360 Data Leakage | RFC 5424 |           | dlp |     |
| ------------------- | -------- | --------- | --- | --- |
|                     | 6        | ctm360_da |     |     |
Traffic (srcip,
| Protection  | 0   | ta_leakage  |     | srcport, |
| ----------- | --- | ----------- | --- | -------- |
|             | 8   | _protection |     | dstip,   |
4
dstport, and
proto),
Syslog
(otherwise)
| Custom Application JumpTo | JSON |              | miscs |                 |
| ------------------------- | ---- | ------------ | ----- | --------------- |
|                           | 6    | custom_ap    |       | Traffic (srcip, |
|                           | 0    | plication_ju |       | srcport,        |
|                           | 9    | mpto         |       | dstip,          |
|                           | 8    |              |       | dstport, and    |
proto),
Syslog
(otherwise)
| CyberArk PTA (CEF) | CEF | cyberark | iam |                 |
| ------------------ | --- | -------- | --- | --------------- |
|                    | 5   |          |     | Traffic (srcip, |
|                    | 1   |          |     | srcport,        |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                             | t   |     | y   |              |
| --------------------------- | --- | --- | --- | ------------ |
| Click here to configure log | 4   |     |     | dstip,       |
| ingestion                   | 3   |     |     | dstport, and |
|                             | or  |     |     | proto),      |
|                             | 5   |     |     | Syslog       |
|                             | 8   |     |     | (otherwise)  |
7
0
Cygna Labs Cygna Auditor 5 RFC 5424 + JSON cygna_labs paas Traffic (srcip,
7
|     |     | _cygna_au |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 1   | ditor     |     | dstip,       |
|     | 8   |           |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 5 RFC 5424 with syslog | cynerio | iot | Traffic (srcip, |
| --- | ---------------------- | ------- | --- | --------------- |
Cynerio
|     | 7 messages in structured |     |     | srcport,     |
| --- | ------------------------ | --- | --- | ------------ |
|     | 2 data (SD)              |     |     | dstip,       |
|     | 7                        |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Cynet (CEF) | CEF | cynet | xdr |                 |
| ----------- | --- | ----- | --- | --------------- |
|             | 5   |       |     | Traffic (srcip, |
|             | 1   |       |     | srcport,        |
|             | 4   |       |     | dstip,          |
|             | 3   |       |     | dstport, and    |
|             | or  |       |     | proto),         |
|             | 5   |       |     | Syslog          |
|             | 8   |       |     | (otherwise)     |
7
0
| D-Link                 | 5 D-Link custom format | dlink     | wireless | Traffic         |
| ---------------------- | ---------------------- | --------- | -------- | --------------- |
|                        | 1                      |           |          | (srcip),        |
|                        | 8                      |           |          | Syslog          |
|                        | 9                      |           |          | (otherwise)     |
| Darktrace - DCIP (CEF) | CEF                    |           | endpoint |                 |
|                        | 5                      | darktrace |          | Traffic (srcip, |
|                        | 1                      |           |          | srcport,        |
dstip,
4
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
or

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |             |
| --- | --- | --- | --- | ----------- |
|     | 5   |     |     | Syslog      |
|     | 8   |     |     | (otherwise) |
7
0
| Datto AP (Datto Wi-Fi) | RFC 3164 |          | wireless |                 |
| ---------------------- | -------- | -------- | -------- | --------------- |
|                        | 6        | datto_ap |          | Traffic (srcip, |
|                        | 0        |          |          | srcport,        |
|                        | 7        |          |          | dstip,          |
|                        | 5        |          |          | dstport, and    |
proto),
Syslog
(otherwise)
| DBSafer | 5 CSV | dbsafer | dlp | Syslog |
| ------- | ----- | ------- | --- | ------ |
1
8
1
| Deep Instinct | 5 regex + KVP | deep_instin | saas | Traffic (srcip, |
| ------------- | ------------- | ----------- | ---- | --------------- |
|               | 6             | ct          |      | srcport,        |
|               | 2             |             |      | dstip,          |
|               | 8             |             |      | dstport, and    |
proto),
Syslog
(otherwise)
|                         | CEF |         | websec |                 |
| ----------------------- | --- | ------- | ------ | --------------- |
| DefensX - DefensX (CEF) | 5   | defensx |        | Traffic (srcip, |
|                         | 1   |         |        | srcport,        |
|                         | 4   |         |        | dstip,          |
|                         | 3   |         |        | dstport, and    |
proto),
Syslog
(otherwise)
Dell EMC Data Domain 5 Modified RFC 3164 dell_emc_d unixlogs Traffic (srcip,
header + regex-parsable
|     | 8         | ata_domai |     | srcport,     |
| --- | --------- | --------- | --- | ------------ |
|     | 7 message | n         |     | dstip,       |
|     | 4         |           |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                            | t                    |            | y       |                 |
| -------------------------- | -------------------- | ---------- | ------- | --------------- |
| Dell EMC PowerScale Isilon | PSV (pipe-separated- |            | storage |                 |
|                            | 5                    | dell_emc_p |         | Traffic (srcip, |
values)
|     | 9   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
owerscale_
|     | 3   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
isilon
|     | 7   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Dell EMC Powerstore 5 RFC 3164 + local header Traffic (srcip,
|     |                        | dell_power | storage |          |
| --- | ---------------------- | ---------- | ------- | -------- |
|     | 6 (RFC 5424) + message |            |         | srcport, |
store
|     | 8   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Dell iDRAC | 5              | dell_idrac |      | Traffic (srcip, |
| ---------- | -------------- | ---------- | ---- | --------------- |
|            | RFC 5424 + KVP |            | saas |                 |
|            | 5              |            |      | srcport,        |
|            | 6              |            |      | dstip,          |
|            | 6              |            |      | dstport, and    |
proto),
Syslog
(otherwise)
| Dell Switch | 5                 | dell_switch |         | Traffic (srcip, |
| ----------- | ----------------- | ----------- | ------- | --------------- |
|             | Dell Technologies |             | netlogs |                 |
|             | 5 custom format   |             |         | srcport,        |
|             | 7                 |             |         | dstip,          |
|             | 8                 |             |         | dstport, and    |
proto),
Syslog
(otherwise)
Devolutions Remote Desktop 6 Devolutions custom devolutions remote_ac
Traffic (srcip,
|     | 0 format + JSON | _remote_d | cess | srcport, |
| --- | --------------- | --------- | ---- | -------- |
Manager
|     | 8   | esktop_ma |     | dstip, |
| --- | --- | --------- | --- | ------ |
|     | 7   | nager     |     |        |
dstport, and
proto),
Syslog
(otherwise)
| DHCP (Beats) | 5 JSON | dhcp | netmgmt | Traffic |
| ------------ | ------ | ---- | ------- | ------- |
0
(srcmac),
|     | 4   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
4
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                  | t                |       | y       |                 |
| ---------------- | ---------------- | ----- | ------- | --------------- |
| DHCPD (ISC DHCP) | 5                | dhcpd |         |                 |
|                  | RFC 3164 + regex |       | netmgmt | Traffic (srcip, |
5
srcport,
|     | 5   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
4
dstport, and
proto),
Syslog
(otherwise)
| DNSVault RPZdb | 5 regex + JSON | dnsvault_r | ndr | Traffic (srcip, |
| -------------- | -------------- | ---------- | --- | --------------- |
|                | 6              | pzdb       |     | srcport,        |
|                | 3              |            |     | dstip,          |
|                | 9              |            |     | dstport, and    |
proto),
Syslog
(otherwise)
| Dragos (CEF) | 5   | dragos |       | Traffic     |
| ------------ | --- | ------ | ----- | ----------- |
|              | CEF |        | otsec |             |
|              | 5   |        |       | (srcip),    |
|              | 3   |        |       | Syslog      |
|              | 9   |        |       | (otherwise) |
DrayTek Firewall 5 DrayTek custom format draytek_fw firewall Traffic (srcip,
|     | 5   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|                          | 5 HTTP JSON |          |     | IDPS/Malwar |
| ------------------------ | ----------- | -------- | --- | ----------- |
| ECS Suricata (HTTP JSON) |             | suricata | ndr |             |
e Sandbox
2
Events
0
|     | 0   |     |     | (threat), |
| --- | --- | --- | --- | --------- |
Traffic (srcip,
(T
srcport,
C
|     | P   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
o
|     | nl  |     |     | proto), |
| --- | --- | --- | --- | ------- |
Syslog
y)
(otherwise)
Windows
5 HTTP JSON
| ECS Windows (HTTP JSON) |     | microsoft_ | endpoint |        |
| ----------------------- | --- | ---------- | -------- | ------ |
|                         | 2   |            |          | Events |
windows
(winlogevent
0
)
0

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
(T
C
P
o
nl
y)
eDictionary - eDictionary (CEF)
|     | CEF | edictionary | endpoint | Traffic (srcip, |
| --- | --- | ----------- | -------- | --------------- |
5
srcport,
1
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
3
proto),
or
|     | 5   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
(otherwise)
8
7
0
EfficientIP SOLIDserver DDI 5 RFC 3164 (hostname) efficient_ip netmgmt Traffic (srcip,
|     | 7   | _solidserve |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 6   | r           |     | dstip,       |
|     | 1   |             |     | dstport, and |
proto),
Syslog
(otherwise)
Egnyte (Syslog JSON) 5 syslog JSON or HTTP egnyte endpoint Traffic (srcip,
|     | 1 JSON |     |     | srcport, |
| --- | ------ | --- | --- | -------- |
(HTTP JSON)
|     | 4   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstport, and |
proto),
5
|     | 2   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
(otherwise)
0
0
(T
C
P
o
nl
y)
|     | 5 (RFC 3164 header) + | elastic_sta | log_proces | Traffic (srcip, |
| --- | --------------------- | ----------- | ---------- | --------------- |
Elastic Stack
|     | JSON |     | sing |          |
| --- | ---- | --- | ---- | -------- |
|     | 9    | ck  |      | srcport, |
dstip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstport, and |
|     | 0   |     |     | proto),      |
Syslog
(otherwise)
|               | 5 Ericom Software custom |            | ndr | Traffic (srcip, |
| ------------- | ------------------------ | ---------- | --- | --------------- |
| Ericom ZTEdge |                          | ericom_zte |     |                 |
|               | 6 format                 |            |     | srcport,        |
dge
|     | 0   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Ericcson Cradlepoint Router | RFC 3164 |             | netlogs |                 |
| --------------------------- | -------- | ----------- | ------- | --------------- |
|                             | 5        | ericsson_cr |         | Traffic (srcip, |
|                             | 8        |             |         | srcport,        |
adlepoint_r
|     | 8   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
outer
|     | 6   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
ESET Cloud Office Security 5 RFC 5424 + JSON saas Traffic (srcip,
eset_cos
|     | 8   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
(COS)
|     | 9   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
ESET PROTECT
|     | 5 RFC 5424 + JSON | eset_prote | endpoint | Traffic (srcip, |
| --- | ----------------- | ---------- | -------- | --------------- |
|     | 6                 |            |          | srcport,        |
ct
|     | 5   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|                        | 5 HTTP JSON |           |      | Traffic (srcip, |
| ---------------------- | ----------- | --------- | ---- | --------------- |
| Exium SASE (HTTP JSON) |             | exium_sas | paas |                 |
|                        | 2           |           |      | srcport,        |
e
|     | 0   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 0   |     |     | dstport, and |
|     | (T  |     |     | proto),      |
|     | C   |     |     | Syslog       |
|     | P   |     |     | (otherwise)  |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
o
nl
y)
| ExtraHop (CEF) |       |          |     | Traffic (srcip, |
| -------------- | ----- | -------- | --- | --------------- |
|                | 5 CEF | extrahop | ndr |                 |
srcport,
1
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
| Extreme AirDefense | 5 regex + KVP | extreme_ai | idps |     |
| ------------------ | ------------- | ---------- | ---- | --- |
Traffic (srcip,
|     | 6   | rdefense |     | srcport, |
| --- | --- | -------- | --- | -------- |
1
dstip,
2
dstport, and
proto),
Syslog
(otherwise)
Extreme Controller 5 RFC 3164 extreme_c wireless Traffic (srcip,
|     | 6   | ontroller |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 6   |           |     | dstip,       |
|     | 6   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| ExtremeCloud IQ Site Engine | 5 regex + KVP | extreme_si | asset |     |
| --------------------------- | ------------- | ---------- | ----- | --- |
Traffic (srcip,
|     | 6   | te_engine |     | srcport, |
| --- | --- | --------- | --- | -------- |
1
dstip,
4
dstport, and
proto),
Syslog
(otherwise)
| Extreme Networks X690 | 5 regex |           |       |                 |
| --------------------- | ------- | --------- | ----- | --------------- |
|                       |         | extreme_x | asset | Traffic (srcip, |
6
|     |     | 690 |     | srcport, |
| --- | --- | --- | --- | -------- |
|     | 9   |     |     | dstip,   |
9
dstport, and
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
IDPS/Malwar
| F5 - ASM (CEF) | CEF | f5  | waf |     |
| -------------- | --- | --- | --- | --- |
5
e Sandbox
1
Events
4
(threat,
3
normalized
or
from
5
attack_type),
8
Traffic (srcip,
7
srcport,
0
dstip,
dstport, and
proto),
Syslog
(otherwise)
| F5 BIG-IP | 5                | f5_big_ip |          | IDPS/Malwar |
| --------- | ---------------- | --------- | -------- | ----------- |
|           | F5 custom format |           | firewall |             |
|           | 1                |           |          | e Sandbox   |
|           | 6                |           |          | Events (IDS |
|           | 2                |           |          | signature), |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
|                | CEF or KVP |            | waf |                 |
| -------------- | ---------- | ---------- | --- | --------------- |
| F5 Big-IP ASM  | 5          | f5_big_ip_ |     | Traffic (srcip, |
|                | 9          | asm        |     | srcport,        |
|                | 2          |            |     | dstip,          |
|                | 3          |            |     | dstport, and    |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                              | t           |        | y       |                 |
| ---------------------------- | ----------- | ------ | ------- | --------------- |
| F5 BIG-IP LTM (Local Traffic | regex + KVP |        | weblogs |                 |
|                              | 5           | f5_ltm |         | Traffic (srcip, |
|                              | 7           |        |         | srcport,        |
Manager)
|     | 6   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
F5 BIG-IP Telemetry (HTTP 5 HTTP JSON f5_big_ip firewall Syslog
| JSON) | 2   |     |     |     |
| ----- | --- | --- | --- | --- |
0
0
(T
C
P
o
nl
y)
F5 Big-IP Virtual Edition 5 CSV + F5 custom format websec Traffic (srcip,
f5_big_ip_v
|     | 9   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
irtual_editio
|     | 2   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
n
|     | 2   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| F5 IPI | 5                 | f5_threat_i |          | IDPS/Malwar |
| ------ | ----------------- | ----------- | -------- | ----------- |
|        | three log formats |             | firewall |             |
|        | 5                 | ntelligence |          | e Sandbox   |
|        | 3                 |             |          | Events      |
|        | 6                 |             |          | (dev_type:  |
/threat/),
Traffic
(dstip),
Syslog
(otherwise)
| F5 iRule | 5   | f5_irule | firewall | IDPS/Malwar |
| -------- | --- | -------- | -------- | ----------- |
three log formats
|     | 5   |     |     | e Sandbox  |
| --- | --- | --- | --- | ---------- |
|     | 3   |     |     | Events     |
|     | 6   |     |     | (dev_type: |
/threat/),
Traffic
(dstip),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| F5 L7 DDoS | 5   | f5_l7ddos | firewall | IDPS/Malwar |
| ---------- | --- | --------- | -------- | ----------- |
three log formats
|     | 5   |     |     | e Sandbox  |
| --- | --- | --- | --- | ---------- |
|     | 3   |     |     | Events     |
|     | 6   |     |     | (dev_type: |
/threat/),
Traffic
(dstip),
Syslog
(otherwise)
| F5 Mitigation | 5   | f5_ddos | firewall | IDPS/Malwar |
| ------------- | --- | ------- | -------- | ----------- |
three log formats
|     | 5   |     |     | e Sandbox  |
| --- | --- | --- | --- | ---------- |
|     | 3   |     |     | Events     |
|     | 6   |     |     | (dev_type: |
/threat/),
Traffic
(dstip),
Syslog
(otherwise)
| F5 NGINX | 5                | nginx |         |        |
| -------- | ---------------- | ----- | ------- | ------ |
|          | F5 custom format |       | weblogs | Syslog |
1
5
1
| F5 Silverline | 5                 | f5_silverlin |          | IDPS/Malwar |
| ------------- | ----------------- | ------------ | -------- | ----------- |
|               | three log formats |              | firewall |             |
|               | 5                 | e            |          | e Sandbox   |
|               | 3                 |              |          | Events      |
|               | 6                 |              |          | (dev_type:  |
/threat/),
Traffic
(dstip),
Syslog
(otherwise)
| F5 VPN | 5   | f5_vpn |     |        |
| ------ | --- | ------ | --- | ------ |
|        | CSV |        | vpn | Syslog |
1
8
7
|     | 2 JSON | f4_waap | websec | Traffic (srcip, |
| --- | ------ | ------- | ------ | --------------- |
F5 WAAP
|     | 8   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 4   |     |     | dstport, and |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
| F5 WAF | 5                 | f5_waf |     | IDPS/Malwar |
| ------ | ----------------- | ------ | --- | ----------- |
|        | three log formats |        | waf |             |
|        | 5                 |        |     | e Sandbox   |
|        | 3                 |        |     | Events      |
|        | 6                 |        |     | (dev_type:  |
/threat/),
Traffic
(dstip),
Syslog
(otherwise)
FatPipe Networks SD-WAN 5 FatPipe Networks fatpipe_sd netmgmt Traffic (srcip,
|     | 5 custom format | _wan |     |     |
| --- | --------------- | ---- | --- | --- |
srcport,
|     | 8   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Firepower Management Center 5 RFC 3164 + regex firepower_ saas Traffic (srcip,
|     | 7   | manageme  |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 5   | nt_center |     | dstip,       |
|     | 9   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| Forcepoint - DLP (CEF) | CEF | forcepoint_ | dlp |                 |
| ---------------------- | --- | ----------- | --- | --------------- |
|                        | 5   |             |     | Traffic (srcip, |
dlp
|     | 1   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
Forcepoint - Firewall (CEF) CEF forcepoint firewall Traffic (srcip,
5
|     | 1   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
dstip,
4
dstport, and
3

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |             |
| --- | --- | --- | --- | ----------- |
|     | or  |     |     | proto),     |
|     | 5   |     |     | Syslog      |
|     | 8   |     |     | (otherwise) |
7
0
| Forcepoint Next-Generation | (syslog priority) + JSON |             | firewall |                 |
| -------------------------- | ------------------------ | ----------- | -------- | --------------- |
|                            | 5                        | forcepoint_ |          | Traffic (srcip, |
| Firewall (NGFW)            | 8                        | ngfw        |          | srcport,        |
|                            | 9                        |             |          | dstip,          |
|                            | 1                        |             |          | dstport, and    |
proto),
Syslog
(otherwise)
Forcepoint Security (CEF)
|     | 5 CEF | forcepoint | paas | Traffic (srcip, |
| --- | ----- | ---------- | ---- | --------------- |
|     | 1     |            |      | srcport,        |
|     | 4     |            |      | dstip,          |
|     | 3     |            |      | dstport, and    |
|     | or    |            |      | proto),         |
|     | 5     |            |      | Syslog          |
|     | 8     |            |      | (otherwise)     |
7
0
| Forcepoint Web Security | RFC 5424 |            | websec |                 |
| ----------------------- | -------- | ---------- | ------ | --------------- |
|                         | 6        | beats_forc |        | Traffic (srcip, |
|                         | 1        | epoint_web |        | srcport,        |
(Filebeat)
|     | 0   | _security |     | dstip,       |
| --- | --- | --------- | --- | ------------ |
|     | 1-  |           |     | dstport, and |
|     | 6   |           |     | proto),      |
|     | 2   |           |     | Syslog       |
|     | 0   |           |     | (otherwise)  |
1
| Forescout | 5                      | forescout |       |        |
| --------- | ---------------------- | --------- | ----- | ------ |
|           | Forescout Technologies |           | asset | Syslog |
1 custom format
5
4
| Fortanix DSM (Data Security | RFC 5424 (description + |     | dlp |     |
| --------------------------- | ----------------------- | --- | --- | --- |
5
|     |     | fortanix_ds |     | Traffic (srcip, |
| --- | --- | ----------- | --- | --------------- |
9 fixed KVP)
| Manager)  |     | m   |     | srcport, |
| --------- | --- | --- | --- | -------- |
|           | 0   |     |     | dstip,   |
6
dstport,
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
|     | 5 syslog priority + KVP | fortinet_fort | netlogs | IDPS/Malwar |
| --- | ----------------------- | ------------- | ------- | ----------- |
FortiADC
|     | 7   | iadc |     | e Sandbox |
| --- | --- | ---- | --- | --------- |
|     | 2   |      |     | Events    |
|     | 5   |      |     | (threat), |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Fortinet FortiAnalyzer | 5   | forti_analyz |     | IDPS/Malwar   |
| ---------------------- | --- | ------------ | --- | ------------- |
|                        | KVP |              | ndr |               |
|                        | 5   | er           |     | e Sandbox     |
|                        | 4   |              |     | Events        |
|                        | 2   |              |     | (vendor.attac |
|                        | (U  |              |     | k_name),      |
|                        | D   |              |     | Traffic       |
|                        | P   |              |     | (dstip),      |
|                        | or  |              |     | Syslog        |
|                        | T   |              |     | (otherwise)   |
C
P)
Fortinet FortiAuthenticator 5 RFC 3164 fortinet_fort iam Traffic (srcip,
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
iauthenticat
|     | 7   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
or
|     | 1   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Fortinet FortiEDR 5 RFC 5424 + KVP fortinet_fort endpoint Traffic (srcip,
|     | 6   | iedr |     | srcport,     |
| --- | --- | ---- | --- | ------------ |
|     | 6   |      |     | dstip,       |
|     | 1   |      |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Fortinet Forticloud FortiClient 5 regex + KVP fortinet_fort endpoint Traffic (srcip,
| EMS Cloud Endpoint | 6   |     |     | srcport, |
| ------------------ | --- | --- | --- | -------- |
iclient_ems
| Management Services | 8   |     |     | dstip,       |
| ------------------- | --- | --- | --- | ------------ |
|                     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Fortinet FortiDeceptor 5 KVP fortinet_fort ndr Traffic (srcip,
|     | 9   | ideceptor |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 4   |           |     | dstip,       |
|     | 4   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| Fortinet FortiGate | 5                     | fw_fortigat   |          | Traffic         |
| ------------------ | --------------------- | ------------- | -------- | --------------- |
|                    | KVP                   |               | firewall |                 |
|                    | 5                     | e             |          | (action),       |
|                    | 1                     |               |          | Syslog          |
|                    | 7                     |               |          | (otherwise)     |
|                    | RFC 5424, or RFC3164, |               | firewall |                 |
|                    | 8                     | fortinet_fort |          | Traffic (srcip, |
Fortinet Fortigate
5 or only a priority header
|                    |            | igate |     | srcport, |
| ------------------ | ---------- | ----- | --- | -------- |
| Note: Requires EAP | 1 with KVP |       |     |          |
dstip,
| participation to use. | 7   |     |     |     |
| --------------------- | --- | --- | --- | --- |
dstport, and
(d
proto),
|     | ef  |     |     | IDPS/Malwar |
| --- | --- | --- | --- | ----------- |
a
e Sandbox
ult
Events
|     | )   |     |     | (threat), |
| --- | --- | --- | --- | --------- |
Syslog
(otherwise)
| Fortinet Fortigate (CEF) | CEF |             | firewall |                 |
| ------------------------ | --- | ----------- | -------- | --------------- |
|                          | 5   | fw_fortigat |          | Traffic (srcip, |
|                          | 1   | e           |          | srcport,        |
|                          | 4   |             |          | dstip,          |
|                          | 3   |             |          | dstport, and    |
|                          | or  |             |          | proto),         |
|                          | 5   |             |          | Syslog          |
|                          | 8   |             |          | (otherwise)     |
7
0

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                             | t                       |             | y        |                 |
| --------------------------- | ----------------------- | ----------- | -------- | --------------- |
| Fortinet Fortigate Firewall | Beats (message contains |             | firewall |                 |
|                             | 5                       | fw_fortigat |          | Traffic (srcip, |
syslog + KVP)
|     | 9   | e   |     | srcport, |
| --- | --- | --- | --- | -------- |
(Filebeat)
|     | 5   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
|     | (5  |     |     | proto),      |
|     | 9   |     |     | Syslog       |
|     | 5   |     |     | (otherwise)  |
7
–
6
0
5
7)
Fortinet FortiMail 5 regex + KVP, or CEF forti_mail email Traffic (srcip,
|     | 6   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | dstip,       |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Fortinet FortiManager | syslog priority + KVP |               | siem |        |
| --------------------- | --------------------- | ------------- | ---- | ------ |
|                       | 5                     | fortinet_fort |      | Syslog |
8
imanager
9
4
Fortinet FortiSandbox 5 Fortinet custom format fortinet_fort asset Traffic (srcip,
|     | 6   | isandbox |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 4   |          |     | dstip,       |
|     | 8   |          |     | dstport, and |
proto),
Syslog
(otherwise)
|     | Syslog + KVP |               | netlogs |                 |
| --- | ------------ | ------------- | ------- | --------------- |
|     | 5            | fortinet_fort |         | Traffic (srcip, |
Fortinet Fortiswitch
|     | 9   | iswitch |     | srcport,     |
| --- | --- | ------- | --- | ------------ |
|     | 0   |         |     | dstip,       |
|     | 4   |         |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Fortinet FortiWeb
|     | 5 sylog priority + KVP | fortinet_fort | waf | Traffic (srcip, |
| --- | ---------------------- | ------------- | --- | --------------- |
|     | 6                      | iweb          |     | srcport,        |
|     | 4                      |               |     | dstip,          |
|     | 2                      |               |     | dstport, and    |
proto),
Syslog
(otherwise)
|     | 6 Fortra custom format + | fortra_goan | miscs | Traffic (srcip, |
| --- | ------------------------ | ----------- | ----- | --------------- |
Fortra GoAnywhere MFT
|     | 0 RFC 5424 | ywhere_mf |     | srcport,     |
| --- | ---------- | --------- | --- | ------------ |
|     | 9          | t         |     | dstip,       |
|     | 1          |           |     | dstport, and |
proto),
Syslog
(otherwise)
|     | RFC 3164 + regex |            | iam |                 |
| --- | ---------------- | ---------- | --- | --------------- |
|     | 5                | freeradius |     | Traffic (srcip, |
FreeRADIUS
|     | 7   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 6 RFC 3164 | fudo_pam | pam | Traffic (srcip, |
| --- | ---------- | -------- | --- | --------------- |
Fudo PAM
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
FutureSystems WeGuardia SSL
|     | 5 regex + pipe-separated ( | future_syst | vpn | Traffic (srcip, |
| --- | -------------------------- | ----------- | --- | --------------- |
plus (SSL VPN)
|     | 6 | ) KVP |     |     | srcport, |
| --- | --------- | --- | --- | -------- |
ems_wegu
|     | 5   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
ardia_ssl_p
|     | 1   | lus |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | RFC 3164 + regex |           | saas |        |
| --- | ---------------- | --------- | ---- | ------ |
|     | 5                | ghx_excha |      | Threat |
GHX Exchange
|     | 9   | nge |     | (threat or ips, |
| --- | --- | --- | --- | --------------- |
|     | 3   |     |     | ids), Traffic   |
|     | 2   |     |     | (srcip,         |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
|                 | RFC 2164 + regex |           | iam |                 |
| --------------- | ---------------- | --------- | --- | --------------- |
|                 | 5                |           |     | Traffic (srcip, |
| GHX Vendormate  |                  | ghx_vendo |     |                 |
|                 | 9                |           |     | srcport,        |
rmate
|     | 4   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 5 CEF | gigamon | netmgmt | Traffic (srcip, |
| --- | ----- | ------- | ------- | --------------- |
Gigamon
|     | 9   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstip,       |
|     | 9   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|         | 5                     |         |          | Windows      |
| ------- | --------------------- | ------- | -------- | ------------ |
| Graylog | (RFC 3164) regex (for | graylog | endpoint |              |
|         | 5 Graylog format)     |         |          | Events       |
|         | 6                     |         |          | (winlogevent |
|         | 9                     |         |          | ),           |
IDPS/Malwar
e Sandbox
(threat),
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
|     | RFC 3164 + regex |         | dlp |                 |
| --- | ---------------- | ------- | --- | --------------- |
|     | 5                | gtb_dlp |     | Traffic (srcip, |
GTB DLP
|     | 9   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 1   |     |     | dstport, and |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Guardicore (CEF) |       |            | cloudsec |                 |
| ---------------- | ----- | ---------- | -------- | --------------- |
|                  | 5 CEF | guardicore |          | Traffic (srcip, |
|                  | 1     |            |          | srcport,        |
|                  | 4     |            |          | dstip,          |
|                  | 3     |            |          | dstport, and    |
|                  | or    |            |          | proto),         |
|                  | 5     |            |          | Syslog          |
|                  | 8     |            |          | (otherwise)     |
7
0
HanDreamnet VIPM 5 regex + KVP handreamn netlogs Traffic (srcip,
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
et_vipm
|     | 7   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| HAProxy | 5 RFC 5424 + JSON |         |        |                 |
| ------- | ----------------- | ------- | ------ | --------------- |
|         |                   | haproxy | websec | Traffic (srcip, |
|         | 7                 |         |        | srcport,        |
1
dstip,
3
dstport, and
proto),
Syslog
(otherwise)
|                 | RFC 3164 + JSON or |            | endpoint |             |
| --------------- | ------------------ | ---------- | -------- | ----------- |
|                 | 6                  | harfanglab |          |             |
| HarfangLab EDR  |                    |            |          | IDPS/Malwar |
|                 | 0 RFC 5424         | _edr       |          |             |
e Sandbox
|     | 6   |     |     | Events |
| --- | --- | --- | --- | ------ |
6
(threat,
threat_id),
Traffic (srcip,
srcport,
dstip,
dstport,
proto),
Syslog
(otherwise)s

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Hewlett Packard UNIX 5 regex + KVP hp-ux unixlogs Traffic (srcip,
5
srcport,
8
dstip,
|     | 5   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Hillstone 5 Hillstone Networks fw_hillston firewall IDPS/Malwar
|     | 5   | e   |     | e Sandbox |
| --- | --- | --- | --- | --------- |
custom format
|     | 1   |     |     | Events    |
| --- | --- | --- | --- | --------- |
|     | 4   |     |     | log_type: |
threat),
Traffic
(log_type:
traffic),
Syslog
(otherwise)
|     | Custom StoneOS remote |              | idps |                 |
| --- | --------------------- | ------------ | ---- | --------------- |
|     | 5                     | hillstone_ni |      | Traffic (src IP |
Hillstone NIPS
|     | 9 syslog | ps  |     | , src port, dst |
| --- | -------- | --- | --- | --------------- |
|     | 4        |     |     | IP, dst port,   |
|     | 9        |     |     | and proto),     |
Syslog
(otherwise)
or
Traffic
(hillstone_nip
s.log_type),
Syslog
(otherwise)
Hisun Global Core banking 6 Hisun custom header + { hisun_glob finance
Traffic (src IP
readable message or
|     | 0        | al_core_ba |     | , src port, dst |
| --- | -------- | ---------- | --- | --------------- |
|     | 5 JSON } | nking      |     |                 |
IP, dst port,
8
and proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                        | t                     |            | y       |                 |
| ---------------------- | --------------------- | ---------- | ------- | --------------- |
| Hisun Global E-banking | Hisun custom header + |            | finance |                 |
|                        | 5                     | hisun_glob |         | Traffic (src IP |
readable message, or {
7
|     |     | al_ebankin |     | , src port, dst |
| --- | --- | ---------- | --- | --------------- |
6 Hisun custom header +
|     |     | g   |     | IP, dst port, |
| --- | --- | --- | --- | ------------- |
JSON }
|     | 4   |     |     | and proto), |
| --- | --- | --- | --- | ----------- |
Syslog
(otherwise)
|              | RFC 3164 + regex |             | storage |                 |
| ------------ | ---------------- | ----------- | ------- | --------------- |
|              | 6                | hpe_alletra |         |                 |
| HPE Alletra  |                  |             |         | Traffic (src IP |
0
, src port, dst
|     | 7   |     |     | IP, dst port, |
| --- | --- | --- | --- | ------------- |
9
and proto),
Syslog
(otherwise)
HPE iLO Amplifier Pack 6 RFC 3164 hpe_ilo_a it_mgmt Traffic (src IP
|     | 0   | mplifier_pa |     | , src port, dst |
| --- | --- | ----------- | --- | --------------- |
|     | 8   | ck          |     | IP, dst port,   |
|     | 0   |             |     | and proto),     |
Syslog
(otherwise)
|     | RFC 3164 + KVP | hpe_nimbl | storage | Traffic (srcip, |
| --- | -------------- | --------- | ------- | --------------- |
5
HPE Nimble Storage
|     | 7   | e   |     | srcport, |
| --- | --- | --- | --- | -------- |
dstip,
3
|     | 1   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
HPE Switch 5 Hewlett Packard hpe_switch netlogs Traffic (srcip,
|     | 5 Enterprise custom format |     |     | srcport,     |
| --- | -------------------------- | --- | --- | ------------ |
|     | 9 for switches             |     |     | dstip,       |
|     | 5                          |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 5 JSON | http_datto_ | endpoint | Traffic (srcip, |
| --- | ------ | ----------- | -------- | --------------- |
HTTP Datto EDR
|     | 9   | edr |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstip,       |
|     | 7   |     |     | dstport, and |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| HTTP Google Cloud Armor | 5 JSON |     | saas | Traffic (srcip, |
| ----------------------- | ------ | --- | ---- | --------------- |
google_clo
|     | 8   | ud_armor |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 9   |          |     | dstip,       |
|     | 6   |          |     | dstport, and |
proto),
Syslog
(otherwise)
| HTTP Google Kubernetes | JSON |     | cloudsec |                 |
| ---------------------- | ---- | --- | -------- | --------------- |
|                        | 5    |     |          | Traffic (srcip, |
http_googl
|         | 9   |            |     | srcport,     |
| ------- | --- | ---------- | --- | ------------ |
| Engine  |     | e_kubernet |     |              |
|         | 0   | es_engine  |     | dstip,       |
|         | 7   |            |     | dstport, and |
proto),
Syslog
(otherwise)
| HTTP Scx SmartEDR | 5 JSON | scx_smart_ | endpoint | Traffic (srcip, |
| ----------------- | ------ | ---------- | -------- | --------------- |
|                   | 9      | edr        |          | srcport,        |
|                   | 0      |            |          | dstip,          |
|                   | 1      |            |          | dstport, and    |
proto),
Syslog
(otherwise)
HTTP ThreatLocker Zero Trust HTTP JSON (in an array) endpoint
|     | 5   | threat_lock |     | Traffic (srcip, |
| --- | --- | ----------- | --- | --------------- |
|     | 7   | er_zero_tru |     | srcport,        |
EPP
|     | 5   | st  |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 5 HTTP JSON | winlogbeat | endpoint | Winlogevent |
| --- | ----------- | ---------- | -------- | ----------- |
HTTP Winlogbeat
|     | 7   |     |     | (winlogevent |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | ), Syslog    |
|     | 2   |     |     | (otherwise)  |
IBM AS400
|     | 5 two log formats | ibm_i | ibm_os_lo | Traffic (srcip, |
| --- | ----------------- | ----- | --------- | --------------- |
|     | 6                 |       | gs        | srcport,        |
|     | 3                 |       |           | dstip,          |
|     | 2                 |       |           | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
|                 | 5 RFC 3164 + (regex) |            | endpoint |              |
| --------------- | -------------------- | ---------- | -------- | ------------ |
| IBM WinCollect  |                      | microsoft_ |          | Winlogevent  |
|                 | 8                    | windows_e  |          | (winlogevent |
6
|     |     | veventlog |     | ), Syslog |
| --- | --- | --------- | --- | --------- |
9
(otherwise)
|     | 6 Internet Initiative Japan |     | websec | Traffic (srcip, |
| --- | --------------------------- | --- | ------ | --------------- |
iij_swg
IIJ SWG
|     | 0 custom format |     |     | srcport,     |
| --- | --------------- | --- | --- | ------------ |
|     | 8               |     |     | dstip,       |
|     | 6               |     |     | dstport, and |
proto),
Syslog
(otherwise)
Impero ContentKeeper 5 syslog priority + JSON impero_co websec Traffic (srcip,
|     | 6   | ntentkeepe |     | srcport, |
| --- | --- | ---------- | --- | -------- |
|     | 7   |            |     | dstip,   |
r
|     | 0   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Imperva - SecureSphere | Imperva cusom CEF |           | ndr |                 |
| ---------------------- | ----------------- | --------- | --- | --------------- |
|                        | 6                 | imperva_s |     | Traffic (srcip, |
|                        | 0                 | ecure_sph |     | srcport,        |
|                        | 6                 | ere       |     | dstip,          |
|                        | 5                 |           |     | dstport, and    |
proto),
Syslog
(otherwise)
Imperva - SecureSphere (CEF) CEF imperva_s ndr Traffic (srcip,
5
|     | 1   | ecure_sph |     | srcport, |
| --- | --- | --------- | --- | -------- |
|     |     | ere       |     | dstip,   |
4
dstport, and
3
proto),
or
Syslog
5
|     | 8   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |
7
0
Incapsula SIEM Integration 5 CEF incapsula waf Traffic (srcip,
| (CEF) |     |     |     | srcport, |
| ----- | --- | --- | --- | -------- |
1

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| Indusface Web Application | 5 JSON | indusface_ | waf | IDPS/Malwar |
| ------------------------- | ------ | ---------- | --- | ----------- |
| Firewall                  | 5      | waf        |     |             |
e Sandbox
|     | 8   |     |     | Events    |
| --- | --- | --- | --- | --------- |
|     | 2   |     |     | (threat), |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Infoblox Data Connector (CEF) | CEF | infoblox | ndr |                 |
| ----------------------------- | --- | -------- | --- | --------------- |
|                               | 5   |          |     | Traffic (srcip, |
|                               | 1   |          |     | srcport,        |
|                               | 4   |          |     | dstip,          |
|                               | 3   |          |     | dstport, and    |
|                               | or  |          |     | proto),         |
|                               | 5   |          |     | Syslog          |
|                               | 8   |          |     | (otherwise)     |
7
0
Infoblox Network Identity OS 5 Infoblox custom format infoblox_ni dnssec
Traffic (srcip,
| (NIOS) | 5   | os  |     | srcport, |
| ------ | --- | --- | --- | -------- |
8
dstip,
7
dstport, and
proto),
Syslog
(otherwise)
| Infocyte HUNT (CEF) | CEF | infocyte | endpoint | Traffic (srcip, |
| ------------------- | --- | -------- | -------- | --------------- |
5
srcport,
1
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
3
|     | or  |     |     | proto), |
| --- | --- | --- | --- | ------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |             |
| --- | --- | --- | --- | ----------- |
|     | 5   |     |     | Syslog      |
|     | 8   |     |     | (otherwise) |
7
0
| Intrusion ATI (Applied Threat | RFC 3164 + (regex) |             | netlogs |                 |
| ----------------------------- | ------------------ | ----------- | ------- | --------------- |
|                               | 5                  | intrusion_a |         | Traffic (srcip, |
|                               | 8                  | ti          |         | srcport,        |
Intelligence)
|     | 6   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| IPFIX | 4 NetFlow v5, v9, v10 | ipfix | traffic | Traffic |
| ----- | --------------------- | ----- | ------- | ------- |
7
3
9
(U
D
P
o
nl
y)
| IRONSCALES (CEF) | 5 CEF | ironscales_ | email | Traffic (srcip, |
| ---------------- | ----- | ----------- | ----- | --------------- |
srcport,
|     | 1   | irontraps |     |              |
| --- | --- | --------- | --- | ------------ |
|     | 4   |           |     | dstip,       |
|     | 3   |           |     | dstport, and |
proto),
or
|     | 5   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
(otherwise)
8
7
0
|     | 5 RFC 3164 | ironwhale_ | miscs | Traffic (srcip, |
| --- | ---------- | ---------- | ----- | --------------- |
IronWhale Eguard
|     | 9   | eguard |     | srcport,     |
| --- | --- | ------ | --- | ------------ |
|     | 5   |        |     | dstip,       |
|     | 3   |        |     | dstport, and |
proto),
Syslog
(otherwise)
|     | RFC 3164 + KVP |          | dnssec |                 |
| --- | -------------- | -------- | ------ | --------------- |
|     | 5              | isc_bind |        | Traffic (srcip, |
ISC BIND
|     | 9   |     |     | srcport, |
| --- | --- | --- | --- | -------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | dstip,       |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Ivanti Connect Secure 5 RFC 5424 + regex ivanti_conn vpn Traffic (srcip,
|     | 7   | ect_secure |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 5   |            |     | dstip,       |
|     | 6   |            |     | dstport, and |
proto),
Syslog
(otherwise)
| Ivanti Endpoint Manager | RFC 5424 + regex |             | endpoint |                 |
| ----------------------- | ---------------- | ----------- | -------- | --------------- |
|                         | 5                | ivanti_endp |          | Traffic (srcip, |
|                         | 7                | oint_mana   |          | srcport,        |
|                         | 5                | ger         |          | dstip,          |
|                         | 7                |             |          | dstport, and    |
proto),
Syslog
(otherwise)
| Ivanti Pulse Secure | 5 RFC 5424 + JSON, or  |             |     |                 |
| ------------------- | ---------------------- | ----------- | --- | --------------- |
|                     |                        | ivanti_puls | iam | Traffic (srcip, |
|                     | 7 Ivanti custom format | e_secure    |     | srcport,        |
1
dstip,
|     | 2   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Jsonar Database Security Tool | 5 JSON | jsonar_db_ | dblogs |     |
| ----------------------------- | ------ | ---------- | ------ | --- |
Traffic (srcip,
|     | 5   | security_to |     |     |
| --- | --- | ----------- | --- | --- |
srcport,
|     | 8   | ol  |     |     |
| --- | --- | --- | --- | --- |
dstip,
6
dstport, and
proto),
Syslog
(otherwise)
| Judy Security Email Protection | CEF |             | email |                 |
| ------------------------------ | --- | ----------- | ----- | --------------- |
|                                | 5   | judy_securi |       | Traffic (srcip, |
|                                | 9   | ty_email_p  |       | srcport,        |
|                                | 1   | rotection   |       | dstip,          |
|                                | 9   |             |       | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Judy Security Password | 5 JSON |     | iam | Traffic (srcip, |
| ---------------------- | ------ | --- | --- | --------------- |
judy_securi
|     | 9   | ty_passwor |     | srcport, |
| --- | --- | ---------- | --- | -------- |
Manager
|     | 1   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
d_manager
|     | 7   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Juniper SRX | 5   | fw_juniper_ |          | Traffic     |
| ----------- | --- | ----------- | -------- | ----------- |
|             | KVP |             | firewall |             |
|             | 1   | srx         |          | (srcip),    |
|             | 7   |             |          | Syslog      |
|             | 3   |             |          | (otherwise) |
Juniper SSG 5 Juniper Networks custom fw_juniper_ firewall Traffic
|     | 5 format | ssg |     | (srcip),    |
| --- | -------- | --- | --- | ----------- |
|     | 1        |     |     | Syslog      |
|     | 6        |     |     | (otherwise) |
Juniper Switch 5 Juniper Networks custom juniper_swi netlogs Traffic (srcip,
srcport,
|     | 5 format | tch |     |     |
| --- | -------- | --- | --- | --- |
dstip,
9
|     | 1   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Traffic (srcip,
| KasperskyLab (CEF) | 5 CEF | kasperskyl | endpoint |     |
| ------------------ | ----- | ---------- | -------- | --- |
srcport,
|     | 1   | ab  |     |     |
| --- | --- | --- | --- | --- |
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
| Kaspersky Secure Mail | RFC 3164 |     | email | Traffic (srcip, |
| --------------------- | -------- | --- | ----- | --------------- |
6
kaspersky_
|          | 2   |           |     | srcport, |
| -------- | --- | --------- | --- | -------- |
| Gateway  |     | secure_ma |     |          |
dstip,
|     | 0   | il_gateway |     |     |
| --- | --- | ---------- | --- | --- |
dstport, and
5
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Kaspersky Security Center 5 RFC 5424 + KVP kaspersky_ endpoint Traffic (srcip,
7
|     |     | security_ce |     | srcport, |
| --- | --- | ----------- | --- | -------- |
2
|     |     | nter |     | dstip,       |
| --- | --- | ---- | --- | ------------ |
|     | 3   |      |     | dstport, and |
proto),
Syslog
(otherwise)
| KeeperSecurity Enterprise | 5 RFC5425 + JSON |             |     |                 |
| ------------------------- | ---------------- | ----------- | --- | --------------- |
|                           |                  | keeper_se   | iam | Traffic (srcip, |
|                           | 7                | curity_ente |     | srcport,        |
1
|     |     | rprise |     | dstip, |
| --- | --- | ------ | --- | ------ |
0
dstport, and
proto),
Syslog
(otherwise)
Kemp Technologies Load 5 RFC 5424 + Description Traffic (srcip,
|           |     | kemp_tech | weblogs |          |
| --------- | --- | --------- | ------- | -------- |
| Master LB | 6   |           |         | srcport, |
nologies_lo
|     | 9   | ad_master |     | dstip,       |
| --- | --- | --------- | --- | ------------ |
|     | 5   |           |     | dstport, and |
_lb
proto),
Syslog
(otherwise)
Traffic (srcip,
| Keycloak | 5 RFC 5424 + KVP (values | keycloak | iam |     |
| -------- | ------------------------ | -------- | --- | --- |
srcport,
6 can be JSON)
|     | 5   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
3
proto),
Syslog
(otherwise)
Traffic (srcip,
| Kubernetes | 5 JSON | kubernetes | paas |          |
| ---------- | ------ | ---------- | ---- | -------- |
|            | 2      |            |      | srcport, |
(HTTP JSON)
|     | 0   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
0
|     | (T  |     |     | proto), |
| --- | --- | --- | --- | ------- |
Syslog
C
(otherwise)
P
o
nl
y)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                          | t   |          | y   |                 |
| ------------------------ | --- | -------- | --- | --------------- |
| KVH CommBox Edge Gateway | KVP |          | ndr | Traffic (srcip, |
|                          | 6   | kvh_comm |     |                 |
srcport,
|     | 0   | box_edge_ |     |        |
| --- | --- | --------- | --- | ------ |
|     | 5   | gateway   |     | dstip, |
dstport, and
9
proto),
Syslog
(otherwise)
Lancope - StealthWatch (LEEF)
|     | 5 LEEF | lancope_st | firewall | Traffic     |
| --- | ------ | ---------- | -------- | ----------- |
|     | 5      | ealthwatch |          | (srcip),    |
|     | 2      |            |          | Syslog      |
|     | 2      |            |          | (otherwise) |
LanScope Cat 5 MOTEX custom format lanscope_c endpoint Syslog
|     | 5   | at  |     |     |
| --- | --- | --- | --- | --- |
8
8
Lepide 5 Lepide Software custom lepide endpoint Traffic (srcip,
6 parser
srcport,
0
dstip,
|     | 7   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
Libraesva Email Security 5 RFC 3164 + regex libraesva_e email Traffic (srcip,
|     | 7   | sg  |     | srcport, |
| --- | --- | --- | --- | -------- |
Gateway (ESG)
|     | 4   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise
|     | RFC 5424 + regex |            | websec |                 |
| --- | ---------------- | ---------- | ------ | --------------- |
|     | 5                | link11_waa |        | Traffic (srcip, |
Link11 WAAP
|     | 9   | p   |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Linux Audit | 5 Linux Audit custom |             |          |                 |
| ----------- | -------------------- | ----------- | -------- | --------------- |
|             |                      | linux_audit | unixlogs | Traffic (srcip, |
|             | 6 format             |             |          | srcport,        |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Linux Syslog | 5                    | linux_syslo |          | IDPS/Malwar |
| ------------ | -------------------- | ----------- | -------- | ----------- |
|              | RFC 3164 or RFC 5424 |             | unixlogs |             |
|              | 5                    | g           |          | e Sandbox   |
+ regex
|     | 5   |     |     | Events    |
| --- | --- | --- | --- | --------- |
|     | 5   |     |     | (threat), |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
|     | RFC 3164 + JSON |              | miscs |                 |
| --- | --------------- | ------------ | ----- | --------------- |
|     | 5               | liquid_files |       | Traffic (srcip, |
LiquidFiles
|     | 7   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Logstash Suricata 5 regex + KVP (JSON logstash_s ndr IDPS/Malwar
e Sandbox
|     | 6 values) | uricata |     |     |
| --- | --------- | ------- | --- | --- |
Events
2
|     | 9   |     |     | (threat), |
| --- | --- | --- | --- | --------- |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                    | t                |           | y   |                 |
| ------------------ | ---------------- | --------- | --- | --------------- |
| Mage Data Platform | Mage Data custom |           | dlp |                 |
|                    | 6                | mage_data |     | Traffic (srcip, |
format
|     | 0   | _platform |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 8   |           |     | dstip,       |
|     | 5   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| Mailboarder Agent | 5 RFC 3164 + regex | mailboarde | email |     |
| ----------------- | ------------------ | ---------- | ----- | --- |
Traffic (srcip,
|     | 5   | r_agent |     |     |
| --- | --- | ------- | --- | --- |
srcport,
|     | 8   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
0
dstport, and
proto),
Syslog
(otherwise)
| Mako Networks firewall    | 5                | mako_fw |          | Traffic     |
| ------------------------- | ---------------- | ------- | -------- | ----------- |
|                           | RFC 3164 + regex |         | firewall |             |
|                           | 5                |         |          | (dstip),    |
|                           | 4                |         |          | Syslog      |
|                           | 7                |         |          | (otherwise) |
| ManageEngine ADAudit Plus | 5 regex + KVP    |         | iam      | Windows     |
manageen
|     | 6   |     |     | Events |
| --- | --- | --- | --- | ------ |
gine_adau
|     | 7   | dit_plus |     |     |
| --- | --- | -------- | --- | --- |
9
| ManageEngine ADAuditPlus | CEF | manageen | iam | Windows |
| ------------------------ | --- | -------- | --- | ------- |
5
| (CEF) |     | gine |     | Events |
| ----- | --- | ---- | --- | ------ |
1
4
3
or
5
8
7
0
| ManageEngine Endpoint | RFC 5424 |           | endpoint |                 |
| --------------------- | -------- | --------- | -------- | --------------- |
|                       | 6        | manageen  |          | Traffic (srcip, |
|                       | 2        | gine_endp |          | srcport,        |
Central
|     | 0   | oint_centra |     | dstip,       |
| --- | --- | ----------- | --- | ------------ |
|     | 3   | l           |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
ManageEngine OpManager 6 RFC 5424 manageen it_mgmt Traffic (srcip,
|     | 0   | gine_opma |     | srcport, |
| --- | --- | --------- | --- | -------- |
Plus
|     | 9   | nager_plus |     | dstip,       |
| --- | --- | ---------- | --- | ------------ |
|     | 0   |            |     | dstport, and |
proto),
Syslog
(otherwise)
ManageEngine PAM360 6 RFC 3164 + regex manageen pam Traffic (srcip,
|     | 0   | gine_pam3 |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 6   | 60        |     | dstip,       |
|     | 2   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| ManageEngine Site24x7 | JSON |          | it_mgmt |                 |
| --------------------- | ---- | -------- | ------- | --------------- |
|                       | 5    | manageen |         | Traffic (srcip, |
|                       | 9    |          |         | srcport,        |
gine_site_2
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
4x7
|     | 8   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| McAfee (CEF) | CEF |        | ndr | Traffic (srcip, |
| ------------ | --- | ------ | --- | --------------- |
|              | 5   | If Web |     |                 |
srcport,
|     | 1   | Gateway is |     |        |
| --- | --- | ---------- | --- | ------ |
|     | 4   | in the     |     | dstip, |
dstport, and
|     | 3   | product |     |     |
| --- | --- | ------- | --- | --- |
proto),
|     | or  | name, |     |     |
| --- | --- | ----- | --- | --- |
Syslog
|     | 5   | dev_type is |     |     |
| --- | --- | ----------- | --- | --- |
(otherwise)
|     | 8   | set to:   |     |     |
| --- | --- | --------- | --- | --- |
|     | 7   | mcafee_we |     |     |
|     | 0   | b_gateway |     |     |
Otherwise
the value is
determined
from the
CEF
vendor
field
| McAfee Advanced Threat | 5 JSON | mcafee_at | ndr | Traffic (srcip, |
| ---------------------- | ------ | --------- | --- | --------------- |
| Defense                | 5      | d         |     |                 |
srcport,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstip,       |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| McAfee ePolicy Orchestrator | 5              | mcafee_ep |          | Traffic         |
| --------------------------- | -------------- | --------- | -------- | --------------- |
|                             | RFC 5424 + XML |           | endpoint |                 |
|                             | 5              | o         |          | (srcip),        |
|                             | 3              |           |          | Syslog          |
|                             | 3              |           |          | (otherwise)     |
| McAfee - ESM / Nitro SIEM   | 5 CEF          |           | siem     | Traffic (srcip, |
mcafee_nit
|     | 1   | ro  |     | srcport, |
| --- | --- | --- | --- | -------- |
(CEF)
|     | 4   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| McAfee Firewall         | 5                    | mcafee_fir |          | Traffic         |
| ----------------------- | -------------------- | ---------- | -------- | --------------- |
|                         | KVP                  |            | firewall |                 |
|                         | 1                    | ewall      |          | (srcip),        |
|                         | 6                    |            |          | Syslog          |
|                         | 9                    |            |          | (otherwise)     |
| McAfee Network Security | 5                    | mcafee_ns  |          | Traffic         |
|                         | McAfee custom format |            | ipds     |                 |
|                         | 5                    |            |          | (srcip),        |
|                         | 2                    |            |          | Syslog          |
|                         | 7                    |            |          | (otherwise)     |
|                         | 5 RFC 3164 + KVP     | mcafee_pr  | vpn      | Traffic (srcip, |
McAfee Proxy
|     | 7   | oxy |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 9   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| MCAS SIEM Agent (CEF) | CEF | mcas | firewall |         |
| --------------------- | --- | ---- | -------- | ------- |
|                       | 5   |      |          | Windows |
|                       | 1   |      |          | Events  |
4
3
or
5
8

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
7
0
Medigate
|     | 5 RFC 5424 + regex +  | medigate | iotsec | Traffic (srcip, |
| --- | --------------------- | -------- | ------ | --------------- |
|     | 6 JSON; or RFC 3164 + |          |        | srcport,        |
|     | 3 regex + JSON        |          |        | dstip,          |
|     | 1                     |          |        | dstport, and    |
proto),
Syslog
(otherwise)
Melapress WordPress 5 custom log format melapress websec Traffic (srcip,
|     | 7   | _wordpres |     | srcport, |
| --- | --- | --------- | --- | -------- |
1
|     |     | s   |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Menlo Security MS-XL50M 5 regex (RFC 5424) + KVP menlo websec Traffic (srcip,
|     | 6   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Microsoft Exchange Server | RFC 3164 + syslog, or |            | email |                 |
| ------------------------- | --------------------- | ---------- | ----- | --------------- |
|                           | 5                     | microsoft_ |       | Traffic (srcip, |
RFC 3164 + CSV
|     | 8   | exchange |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 7   |          |     | dstip,       |
|     | 6   |          |     | dstport, and |
proto),
Syslog
(otherwise)
Microsoft IIS
|     | 5 SSV | microsoft_ii | netmgmt | Traffic (srcip, |
| --- | ----- | ------------ | ------- | --------------- |
|     | 6     | s            |         | srcport,        |
|     | 3     |              |         | dstip,          |
|     | 6     |              |         | dstport, and    |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                             | t             |      | y       |        |
| --------------------------- | ------------- | ---- | ------- | ------ |
| Microsoft IIS (Syslog JSON) | 5             | json |         |        |
|                             | syslog + JSON |      | weblogs | Syslog |
1
4
2
| Microsoft Office 365 | 5 JSON | office365 | office_suit | Windows |
| -------------------- | ------ | --------- | ----------- | ------- |
|                      | 6      |           | e           |         |
Events
2
7
Microsoft RDWebAccess 6 JSON microsoft_r remote_ac Traffic (srcip,
cess
|     | 0   | dwebacces |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 6   | s         |     | dstip,       |
|     | 8   |           |     | dstport, and |
proto),
Syslog
(otherwise)
Microsoft Windows Event
|     | 5 regex + XML | microsoft_ | endpoint | Windows      |
| --- | ------------- | ---------- | -------- | ------------ |
|     | 6             | windows_e  |          | Events       |
|     | 4             | vent       |          | (winlogevent |
|     | 6             |            |          | ), Syslog    |
(otherwise)
Microsoft Windows via Graylog 5 (syslog header) + regex microsoft_ endpoint Windows
|     | 5 or JSON | windows |     | Events       |
| --- | --------- | ------- | --- | ------------ |
|     | 6         |         |     | (winlogevent |
|     | 9         |         |     | )            |
MicroWorld eScan
|     | 5 regex + KVP | microworld | endpoint | Traffic (srcip, |
| --- | ------------- | ---------- | -------- | --------------- |
|     | 6             | _escan     |          | srcport,        |
|     | 4             |            |          | dstip,          |
|     | 5             |            |          | dstport, and    |
proto),
Syslog
(otherwise)
MikroTik firewall and router 5 RFC 3164 + regex mikrotik firewall Traffic (srcip,
5
srcport,
|     | 5   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |            | y   |                 |
| --- | --- | ---------- | --- | --------------- |
|     | CEF |            | ndr |                 |
|     | 5   | minerva_la |     | Traffic (srcip, |
Minerva Labs (CEF)
|     |     | bs  |     | srcport, |
| --- | --- | --- | --- | -------- |
1
dstip,
4
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
or
Syslog
5
|     | 8   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |
7
0
MONITORAPP AI WAF 4.1 5 MONITORAPP custom monitorapp waf Traffic (srcip,
|     | 6 format | _ai_waf |     | srcport,     |
| --- | -------- | ------- | --- | ------------ |
|     | 1        |         |     | dstip,       |
|     | 3        |         |     | dstport, and |
proto),
Syslog
(otherwise)
| MONITORAPP WAF 1.0 | 5                      | monitor_ap |        | Traffic         |
| ------------------ | ---------------------- | ---------- | ------ | --------------- |
|                    | syslog (regex)         |            | websec |                 |
|                    | 5                      | p          |        | (srcip),        |
|                    | 3                      |            |        | Syslog          |
|                    | 5                      |            |        | (otherwise)     |
| Nasuni             | 5 Nasuni custom format | nasuni     | paas   | Traffic (srcip, |
|                    | 5                      |            |        | srcport,        |
|                    | 9                      |            |        | dstip,          |
|                    | 2                      |            |        | dstport, and    |
proto),
Syslog
(otherwise)
| NetApp | 5 NetApp custom format | netapp | dblogs | Traffic (srcip, |
| ------ | ---------------------- | ------ | ------ | --------------- |
|        | 6                      |        |        | srcport,        |
|        | 0                      |        |        | dstip,          |
|        | 8                      |        |        | dstport, and    |
proto),
Syslog
(otherwise)
| NetApp (Fabric Attached | RFC 3164 + ONTAP |            | storage |                 |
| ----------------------- | ---------------- | ---------- | ------- | --------------- |
|                         | 5                | netapp_fas |         | Traffic (srcip, |
description
|     | 9   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
Storage)
|     | 0   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstport, and |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Netfilter                     | 5 RFC 3164 + KVP | netfilter   | netlogs | Traffic         |
| ----------------------------- | ---------------- | ----------- | ------- | --------------- |
|                               | 5                |             |         | (dstip),        |
|                               | 4                |             |         | Syslog          |
|                               | 4                |             |         | (otherwise)     |
| Netgear Full Managed Switches | RFC 3164 + regex |             | netlogs |                 |
|                               | 5                | netgear_ful |         | Traffic (srcip, |
|                               | 7                | l_managed   |         | srcport,        |
M4300
|     | 4   | _switches |     | dstip,       |
| --- | --- | --------- | --- | ------------ |
|     | 9   |           |     | dstport, and |
proto),
Syslog
(otherwise)
Netgear Smart Switch 6 RFC 3164 + regex netgear_s netlog Traffic (srcip,
|     | 0   | mart_switc |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 6   | h          |     | dstip,       |
|     | 9   |            |     | dstport, and |
proto),
Syslog
(otherwise)
NetIQ - Identity Manager
|     | 5 CEF | netiq_identi | iam | Traffic (srcip, |
| --- | ----- | ------------ | --- | --------------- |
|     |       | ty_manage    |     | srcport,        |
1
|     |     | r   |     | dstip, |
| --- | --- | --- | --- | ------ |
4
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
or
Syslog
5
|     | 8   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |
7
0
| NetIQ Access Manager | 5    | access_ma |     |        |
| -------------------- | ---- | --------- | --- | ------ |
|                      | JSON |           | iam | Syslog |
|                      | 1    | nager     |     |        |
6
7
| NetIQ SSO | 5 KVP | netiqsso | iam | Syslog |
| --------- | ----- | -------- | --- | ------ |
1
7
1
Netman Smart NAC 5 regex + pipe-separated ( netman_s iam Traffic (srcip,
|     | 6 | ) values | mart_nac |     | srcport, |
| --- | ------------ | -------- | --- | -------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| NetMotion | 5 RFC 5424 | absolute_n | vpn | Traffic (srcip, |
| --------- | ---------- | ---------- | --- | --------------- |
|           | 6          | etmotion   |     | srcport,        |
|           | 4          |            |     | dstip,          |
|           | 1          |            |     | dstport, and    |
proto),
Syslog
(otherwise)
|     | (syslog priority) CEF |            | ndr |                 |
| --- | --------------------- | ---------- | --- | --------------- |
|     | 6                     | netscout_o |     | Traffic (srcip, |
NetScout Omnis
|     | 0   | mnis |     | srcport,     |
| --- | --- | ---- | --- | ------------ |
|     | 6   |      |     | dstip,       |
|     | 3   |      |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 9 (syslog priority) CEF | netscout_o | ndr | Traffic (srcip, |
| --- | ----------------------- | ---------- | --- | --------------- |
NetScout Omnis
|                       | 0   | mnis |     | srcport,     |
| --------------------- | --- | ---- | --- | ------------ |
| Note: Requires EAP    | 6   |      |     | dstip,       |
| participation to use. | 3   |      |     | dstport, and |
proto),
(d
Syslog
ef
|     | a   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |
ult
)
|     | 5 RFC 3164 + JSON | nextcloud | storage | Traffic (srcip, |
| --- | ----------------- | --------- | ------- | --------------- |
Nextcloud
|     | 9   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 5   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Nippon Electric Company Indoor | RFC-3164 header +   |         | netlogs |                 |
| ------------------------------ | ------------------- | ------- | ------- | --------------- |
|                                | 5                   | nec_idu |         | Traffic (srcip, |
|                                | 9 NEC custom syslog |         |         | srcport,        |
Unit
|     | 2   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | dstport, and |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
|     | 5 RFC 3164 + vendor | nutanix_nx | ndr | Traffic (srcip, |
| --- | ------------------- | ---------- | --- | --------------- |
Nutanix NX
|     | 7 header + KVP |     |     | srcport,     |
| --- | -------------- | --- | --- | ------------ |
|     | 2              |     |     | dstip,       |
|     | 4              |     |     | dstport, and |
proto),
Syslog
(otherwise)
NVIDIA Mellanox Switch 5 NVIDIA custom format nvidia_mell netlogs Traffic (srcip,
|     | 7   | anox_switc |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 3   | h          |     | dstip,       |
|     | 4   |            |     | dstport, and |
proto),
Syslog
(otherwise)
| NXLog | 5 JSON (regex) | nxlog | paas | Windows |
| ----- | -------------- | ----- | ---- | ------- |
|       | 6              |       |      | Events  |
(Also see Cribl, above)
|     | 0   |     |     | (winlogevent |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | ), Traffic   |
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| OneLogin | 5 JSON | one_login | iam | Traffic (srcip, |
| -------- | ------ | --------- | --- | --------------- |
5
srcport,
8
dstip,
|     | 1   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | 6 RFC 5424 | onv_switch | netlogs | Traffic (srcip, |
| --- | ---------- | ---------- | ------- | --------------- |
ONV Switch
|     | 1   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 0   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
OpenCanary
|     | 5 regex + JSON | opencanar | ndr | Traffic (srcip, |
| --- | -------------- | --------- | --- | --------------- |
|     | 6              | y         |     | srcport,        |
|     | 3              |           |     | dstip,          |
|     | 8              |           |     | dstport, and    |
proto),
Syslog
(otherwise)
|          | 5 RFC 3164 + KVP |         | iam | Syslog |
| -------- | ---------------- | ------- | --- | ------ |
| OpenIAM  |                  | openiam |     |        |
8
8
9
|          | 5               | openldap_ |       |        |
| -------- | --------------- | --------- | ----- | ------ |
| OpenLDAP | OpenLDAP custom |           | email | Syslog |
|          | 1               | style     |       |        |
format
(for Cisco ESA, use 5562)
6
4
| OpenShift | 5                  | redhat_ope |      | Traffic (srcip, |
| --------- | ------------------ | ---------- | ---- | --------------- |
|           | RFC 5424 + (regex, |            | paas |                 |
|           | 5 JSON values)     | nshift     |      | srcport,        |
|           | 7                  |            |      | dstip,          |
|           | 3                  |            |      | dstport, and    |
proto),
Syslog
(otherwise)
| OpenText - Open Enterprise | CEF |            | asset |                 |
| -------------------------- | --- | ---------- | ----- | --------------- |
|                            |     | opentext_o |       | Traffic (srcip, |
5
| Server (CEF)  | 1   | es  |     | srcport, |
| ------------- | --- | --- | --- | -------- |
|               | 4   |     |     | dstip,   |
dstport, and
3
|     | or  |     |     | proto), |
| --- | --- | --- | --- | ------- |
|     | 5   |     |     | Syslog  |
(otherwise)
8
7
0
OpenVPN
|     | 5 OpenVPN custom format | openvpn | vpn | Traffic (srcip, |
| --- | ----------------------- | ------- | --- | --------------- |
|     | 6                       |         |     | srcport,        |
|     | 4                       |         |     | dstip,          |
|     | 3                       |         |     | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| OPNsense | 5 RFC 3164 | opnsense | paas | Traffic (srcip, |
| -------- | ---------- | -------- | ---- | --------------- |
|          | 6          |          |      | srcport,        |
|          | 6          |          |      | dstip,          |
|          | 0          |          |      | dstport, and    |
proto),
Syslog
(otherwise)
|     | JSON |            | database |                 |
| --- | ---- | ---------- | -------- | --------------- |
|     | 6    | oracle_aud |          | Traffic (srcip, |
Oracle Audit Trail
|     | 2   | it_trail |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 0   |          |     | dstip,       |
|     | 4   |          |     | dstport, and |
proto),
Syslog
(otherwise)
| Oracle DB | 5 CSV | oracle | dblogs | Traffic     |
| --------- | ----- | ------ | ------ | ----------- |
|           | 1     |        |        | (srcip),    |
|           | 7     |        |        | Syslog      |
|           | 0     |        |        | (otherwise) |
Oracle Solaris 5 RFC 3164 or RFC 5424 oracle_sola unixlogs Traffic (srcip,
|     | 6 + regex | ris |     | srcport,     |
| --- | --------- | --- | --- | ------------ |
|     | 6         |     |     | dstip,       |
|     | 4         |     |     | dstport, and |
proto),
Syslog
(otherwise)
Traffic (srcip,
Ordr Connected Device Security 5 syslog + regex + JSON ordr_cds endpoint
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
dstip,
2
dstport, and
2
proto),
Syslog
(otherwise)
| PacketFence | 5 regex + description |            |         | Traffic (srcip, |
| ----------- | --------------------- | ---------- | ------- | --------------- |
|             |                       | packetfenc | netmgmt |                 |
|             | 6                     | e          |         | srcport,        |
|             | 8                     |            |         | dstip,          |
|             | 6                     |            |         | dstport, and    |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Palo Alto Networks Next    | 5 LEEF | fw_palo_alt | firewall | Traffic     |
| -------------------------- | ------ | ----------- | -------- | ----------- |
| Generation Firewall (LEEF) | 5      |             |          |             |
|                            |        | o           |          | (srcip),    |
|                            | 2      |             |          | Syslog      |
|                            | 2      |             |          | (otherwise) |
Palo Alto Networks - Traps
|             | 5 CEF | palo_alto_ | xdr | Traffic (srcip, |
| ----------- | ----- | ---------- | --- | --------------- |
| Agent (CEF) |       | networks_t |     | srcport,        |
1
|     |     | raps_agent |     | dstip, |
| --- | --- | ---------- | --- | ------ |
4
dstport, and
3
proto),
or
|     | 5   |     |     | Syslog |
| --- | --- | --- | --- | ------ |
(otherwise)
8
7
0
|     | 5 BSD syslog + CSV | fw_palo_alt | firewall | Traffic (type: |
| --- | ------------------ | ----------- | -------- | -------------- |
Palo Alto Networks Next-
|     | 5   | o   |     | traffic), |
| --- | --- | --- | --- | --------- |
Generation Firewall and
|     | 1   |     |     | IDPS/Malwar |
| --- | --- | --- | --- | ----------- |
Panorama (BSD syslog and
|     | 5   |     |     | e Sandbox |
| --- | --- | --- | --- | --------- |
CSV)
Events (type:
threat),
Syslog
(otherwise)
|                                 | 5 (syslog header) + regex | fw_palo_alt | firewall |                 |
| ------------------------------- | ------------------------- | ----------- | -------- | --------------- |
| Palo Alto Networks Firewall via |                           |             |          | Traffic (srcip, |
|                                 | 5 or JSON                 | o           |          |                 |
| Graylog                         |                           |             |          | srcport,        |
|                                 | 6                         |             |          | dstip,          |
9
dstport, and
proto),
Syslog
(otherwise)
| Palo Alto Networks - Prisma | 5 LEEF | palo_alto_ | firewall |     |
| --------------------------- | ------ | ---------- | -------- | --- |
Traffic (srcip,
|               | 5   | networks_p |     |          |
| ------------- | --- | ---------- | --- | -------- |
| Access (LEEF) |     |            |     | srcport, |
|               | 2   | risma_acce |     |          |
dstip,
|     | 2   | ss  |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
IDPS/Malwar
e Sandbox
Events (cat:
threat),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Palo Alto Networks Prisma | 5 RFC 3164 (with RFC    |            |          |                 |
| ------------------------- | ----------------------- | ---------- | -------- | --------------- |
|                           |                         | palo_alto_ | cloudsec | Traffic (srcip, |
| Cloud (Compute Edition)   | 7 5424 for timestamp) + |            |          |                 |
|                           |                         | networks_p |          | srcport,        |
|                           | 2 KVP                   | risma_clou |          | dstip,          |
0
|     |     | d   |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | RFC 5424 |           | miscs |                 |
| --- | -------- | --------- | ----- | --------------- |
|     | 6        | pci_mvapp |       | Traffic (srcip, |
PCI MVApp
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 6   |     |     | dstip,       |
|     | 1   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Penta Security WAPPLES WAF 5 KVP penta_sec waf Traffic (srcip,
|     | 5   | urity_wappl |     |     |
| --- | --- | ----------- | --- | --- |
srcport,
|     | 6   | es  |     |     |
| --- | --- | --- | --- | --- |
dstip,
|     | 0   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | 5 regex + KVP | pentera_ap | paas | Traffic (srcip, |
| --- | ------------- | ---------- | ---- | --------------- |
Pentera Appliance
|     | 7   | pliance |     | srcport,     |
| --- | --- | ------- | --- | ------------ |
|     | 3   |         |     | dstip,       |
|     | 7   |         |     | dstport, and |
proto),
Syslog
(otherwise)
| Peplink XDR | 5 RFC 5424 + KVP | peplink_xdr | xdr | Traffic (srcip, |
| ----------- | ---------------- | ----------- | --- | --------------- |
|             | 6                |             |     | srcport,        |
|             | 6                |             |     | dstip,          |
|             | 5                |             |     | dstport, and    |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Perception Point X-Ray 5 RFC 5424 + KVP perception saas Traffic (srcip,
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
point_xray
|     | 6   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| pfSense Firewall | 5   | pfsense_fw | firewall | Traffic (srcip, |
| ---------------- | --- | ---------- | -------- | --------------- |
RFC 3164 or RFC 5424
|     | 5   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
PIOLINK WEBFRONT-K regex + KVP piolink_we waf Traffic (srcip,
5
|     |     | bfront_k |     | srcport, |
| --- | --- | -------- | --- | -------- |
6
|     | 1   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
dstport, and
7
proto),
Syslog
(otherwise)
5 (syslog priority + version
| PNPSECURE NODESAFER |     | pnpsecure | dblogs | Traffic (srcip, |
| ------------------- | --- | --------- | ------ | --------------- |
7 + timestamp +
|     |     | _nodesafer |     | srcport, |
| --- | --- | ---------- | --- | -------- |
11 hostname) + JSON
dstip,
dstport, and
proto),
Syslog
(otherwise)
|     | 6 RFC 3164 | postgresql | database | Traffic (srcip, |
| --- | ---------- | ---------- | -------- | --------------- |
PostgreSQL
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| PrintChaser | 5   | printchaser |     |        |
| ----------- | --- | ----------- | --- | ------ |
|             | CSV |             | dlp | Syslog |
1
7
9

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t    |         | y   |                 |
| --- | ---- | ------- | --- | --------------- |
|     | JSON |         | vpn |                 |
|     | 5    | pritunl |     | Traffic (srcip, |
Pritunl
|     | 7   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 8   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Privacy-i | 5 CSV | privacy | dlp | Syslog |
| --------- | ----- | ------- | --- | ------ |
1
7
8
| Progress Kemp LoadMaster | 5 CEF |     | netlogs | Traffic (srcip, |
| ------------------------ | ----- | --- | ------- | --------------- |
progress_k
|     | 1   | emp_lm |     | srcport, |
| --- | --- | ------ | --- | -------- |
(CEF)
|     | 4   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| Proofpoint | Proofpoint custom format | proofpoint | email | Syslog |
| ---------- | ------------------------ | ---------- | ----- | ------ |
5
5
9
6
(5
1
6
0
is
d
e
pr
ec
at
e
d)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t                     |           | y   |                 |
| --- | --------------------- | --------- | --- | --------------- |
|     | 5 RFC 3164 + RFC 5424 | prophaze_ | waf | Traffic (srcip, |
Prophaze WAF
|     | 7 timestamp + JSON | waf |     | srcport,     |
| --- | ------------------ | --- | --- | ------------ |
|     | 3                  |     |     | dstip,       |
|     | 3                  |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Pulse Secure | 5 RFC 5424 + (regex) | pulse_secu | vpn | Syslog |
| ------------ | -------------------- | ---------- | --- | ------ |
|              | 5                    | re         |     |        |
3
4
|     | 5 RFC 3164 + log type + | qnap_qts | storage | Traffic (srcip, |
| --- | ----------------------- | -------- | ------- | --------------- |
QNAP QTS
|     | 7 KVP |     |     | srcport,     |
| --- | ----- | --- | --- | ------------ |
|     | 2     |     |     | dstip,       |
|     | 6     |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | Syslog |            | websec |        |
| --- | ------ | ---------- | ------ | ------ |
|     | 5      | qsan_stora |        | Syslog |
QSAN Storage
8
ge
9
8
| Qumulo Core | 5 RFC 5424 + CSV |           |         |                 |
| ----------- | ---------------- | --------- | ------- | --------------- |
|             |                  | qumulo_co | storage | Traffic (srcip, |
|             | 7                | re        |         | srcport,        |
0
dstip,
4
dstport, and
proto),
Syslog
(otherwise)
Radware Alteon 5 RFC 3164 or RFC 5424 radware_al netlogs Traffic (srcip,
7 + description
|     |     | teon |     | srcport, |
| --- | --- | ---- | --- | -------- |
|     | 0   |      |     | dstip,   |
0
dstport, and
proto),
Syslog
(otherwise)
| Radware Cyber Controller Plus | RFC 3164 + CSV |             | idps |                 |
| ----------------------------- | -------------- | ----------- | ---- | --------------- |
|                               | 5              | radware_c   |      | Traffic (srcip, |
|                               | 9              | ybercontrol |      | srcport,        |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |          | y   |              |
| --- | --- | -------- | --- | ------------ |
|     | 1   | ler_plus |     | dstip,       |
|     | 4   |          |     | dstport, and |
proto),
Syslog
(otherwise)
| Radware Defense Flow | RFC 3164 or RFC 5424 |            | ndr |                 |
| -------------------- | -------------------- | ---------- | --- | --------------- |
|                      | 6                    | radware_d  |     | Traffic (srcip, |
|                      | 0                    | efense_flo |     | srcport,        |
|                      | 8                    | w          |     | dstip,          |
|                      | 2                    |            |     | dstport, and    |
proto),
Syslog
(otherwise)
Radware DefensePro 5 Radware custom format radware_d idps Traffic (srcip,
|     | 6   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
efense_pro
|     | 1   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | JSON |           | waf |        |
| --- | ---- | --------- | --- | ------ |
|     | 6    | radware_w |     | Threat |
Radware WAF
|     | 2   | af  |     | (threat),       |
| --- | --- | --- | --- | --------------- |
|     | 0   |     |     | Traffic (srcip, |
|     | 8   |     |     | srcport,        |
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Rapid7 | 5 KVP | rapid7 | security_sc | Syslog |
| ------ | ----- | ------ | ----------- | ------ |
1
an
5
3
RazLeeSecurity - Audit (CEF) CEF ibm_raz_le endpoint Traffic (srcip,
5
|     | 1   | e_security |     | srcport, |
| --- | --- | ---------- | --- | -------- |
dstip,
4
dstport, and
3
proto),
or
Syslog
5
|     | 8   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
7
0
|     | 5 RFC 3164 + regex | relianoid_w | waf | Traffic (srcip, |
| --- | ------------------ | ----------- | --- | --------------- |
Relianoid WAF
|     | 7   | af  |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| RSA Authentication Manager | 5   | rsa_auth |     |        |
| -------------------------- | --- | -------- | --- | ------ |
|                            | CSV |          | nsa | Syslog |
1
8
4
| Ruckus SmartZone Network | RFC 3164 + KVP |            | netlogs |                 |
| ------------------------ | -------------- | ---------- | ------- | --------------- |
|                          | 5              | ruckus_sm  |         | Traffic (srcip, |
|                          | 8              | artzone_ne |         |                 |
| Controller               |                |            |         | srcport,        |
|                          | 7              | twork_cont |         |                 |
dstip,
|     | 5   | roller |     | dstport, and |
| --- | --- | ------ | --- | ------------ |
proto),
Syslog
(otherwise)
Ruckus ZoneDirector 5 RFC 3164 or RFC 5424 ruckus_zon wireless Traffic (srcip,
|     | 6   | e_director |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 6   |            |     | dstip,       |
|     | 2   |            |     | dstport, and |
proto),
Syslog
(otherwise)
RuiJie Switch 5 regex + (custom value) + ruijie_switc netlogs Traffic (srcip,
|     | 6 timestamp + (hostname) |     |     | srcport, |
| --- | ------------------------ | --- | --- | -------- |
h
|     | 8 + %facility-severity-  |     |     | dstip,       |
| --- | ------------------------ | --- | --- | ------------ |
|     | 9 mnemonic + description |     |     | dstport, and |
proto),
Syslog
(otherwise)
| SafePC | 5 CSV | safepc | cloudsec | Syslog |
| ------ | ----- | ------ | -------- | ------ |
1
8
0

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                               | t        |             | y   |                 |
| ----------------------------- | -------- | ----------- | --- | --------------- |
| Safetica Data Loss Prevention | RFC 5424 |             | dlp |                 |
|                               | 6        | safetica_dl |     | Traffic (srcip, |
|                               | 2        | p           |     | srcport,        |
|                               | 0        |             |     | dstip,          |
|                               | 2        |             |     | dstport, and    |
proto),
Syslog
(otherwise)
6 RFC 5424 + CEF
|     |     | salt_securit | cloudsec | IDPS/Malwar |
| --- | --- | ------------ | -------- | ----------- |
Salt Security
0
|     |     | y   |     | e Sandbox     |
| --- | --- | --- | --- | ------------- |
|     | 8   |     |     | Events (ids), |
8
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
Sangfor EDR 5 regex + (RFC 3164) + sangfor_ed endpoint Traffic (srcip,
7 JSON
|     |     | r   |     | srcport, |
| --- | --- | --- | --- | -------- |
|     | 0   |     |     | dstip,   |
1
dstport, and
proto),
Syslog
(otherwise)
| Sangfor Internet Access | syslog + RFC 3164 |            | websec |        |
| ----------------------- | ----------------- | ---------- | ------ | ------ |
|                         | 5                 | sangfor_ia |        | Syslog |
|                         | 8                 | g          |        |        |
Gateway (IAG)
9
0
|     | RFC 3614 + CEF |            | ndr |                 |
| --- | -------------- | ---------- | --- | --------------- |
|     | 5              | sangfor_nd |     | Traffic (srcip, |
Sangfor NDR
|     | 9   | r   |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 5   |     |     | dstip,       |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Sangfor NGAF 5 regex + (RFC 3164) + sangfor_ng firewall Traffic (srcip,
|     | 6 KVP | af  |     | srcport, |
| --- | ----- | --- | --- | -------- |
dstip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
|     | 7   |     |     | proto),      |
Syslog
(otherwise)
|     | 5 custom syslog | custom_ba | storage | Traffic (srcip, |
| --- | --------------- | --------- | ------- | --------------- |
SAP Backup
|     | 8   | ckup_app |     | srcport,     |
| --- | --- | -------- | --- | ------------ |
|     | 9   |          |     | dstip,       |
|     | 7   |          |     | dstport, and |
proto),
Syslog
(otherwise)
|     | RFC 3164 Time modified |             | ndr |                 |
| --- | ---------------------- | ----------- | --- | --------------- |
|     | 5                      | sap_securit |     | Traffic (srcip, |
SAP Security Audit
+ CSV
|     | 8   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
y_audit
|     | 8   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Sectona PAM | 5 regex + CSV |           |     |                 |
| ----------- | ------------- | --------- | --- | --------------- |
|             |               | sectona_p | iam | Traffic (srcip, |
7
|     |     | am  |     | srcport, |
| --- | --- | --- | --- | -------- |
|     | 2   |     |     | dstip,   |
1
dstport, and
proto),
Syslog
(otherwise)
| SECUi Bluemax NGF | regex (header) + CSV |            | firewall |                 |
| ----------------- | -------------------- | ---------- | -------- | --------------- |
|                   | 5                    | secui_blue |          | Traffic (srcip, |
|                   | 9 (payload)          | max_ngf    |          |                 |
srcport,
3
dstip,
8
dstport, and
proto),
Syslog
(otherwise)
SECUi Firewall 5 RFC 5424 + KVP secui_fw firewall Traffic (srcip,
|     | 5   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 6   |     |     | dstip,       |
|     | 1   |     |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                    | t                  |           | y        |                 |
| ------------------ | ------------------ | --------- | -------- | --------------- |
| SECUi MF2 Firewall | 5                  | secui_mf2 |          | Traffic (srcip, |
|                    | RFC 5424 + (regex) |           | firewall |                 |
|                    | 5                  |           |          | srcport,        |
|                    | 7                  |           |          | dstip,          |
|                    | 0                  |           |          | dstport, and    |
proto),
Syslog
(otherwise)
| SECUi MFD | 5                   | secui_mfd |      | Traffic (srcip, |
| --------- | ------------------- | --------- | ---- | --------------- |
|           | SECUi custom format |           | idps |                 |
|           | 6                   |           |      | srcport,        |
|           | 11                  |           |      | dstip,          |
dstport, and
proto),
Syslog
(otherwise)
| Secureki APPM | 5 RFC 3164 + regex |            |     | Traffic (srcip, |
| ------------- | ------------------ | ---------- | --- | --------------- |
|               |                    | secureki_a | iam |                 |
|               | 6                  | ppm        |     | srcport,        |
|               | 9                  |            |     | dstip,          |
|               | 3                  |            |     | dstport, and    |
proto),
Syslog
(otherwise)
|                            | 5                 | ssr_metiey |        | Traffic (srcip, |
| -------------------------- | ----------------- | ---------- | ------ | --------------- |
| Security Strategy Research | SSR custom format |            | websec |                 |
|                            | 5                 | e          |        | srcport,        |
(SSR) Metieye
|     | 7   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     |     |     | idps | Traffic (srcip, |
| --- | --- | --- | ---- | --------------- |
5
| SecurityGen IDS  | JSON | securitygen |     |          |
| ---------------- | ---- | ----------- | --- | -------- |
|                  | 9    |             |     | srcport, |
_ids
or
dstip,
11
dstport, and
RFC 3164 (optional
|     | priority) + JSON |     |     | proto), |
| --- | ---------------- | --- | --- | ------- |
Syslog
or
(otherwise)
syslog_appname +
syslog_procid + JSON
| SecurityGen NGFW | 5    |             | firewall | Traffic (srcip, |
| ---------------- | ---- | ----------- | -------- | --------------- |
|                  | JSON | securitygen |          |                 |
srcport,
|     | 9   | _ngfw |     |     |
| --- | --- | ----- | --- | --- |
or
dstip,
dstport, and

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t                    |     | y   |         |
| --- | -------------------- | --- | --- | ------- |
|     | 1 RFC 3164 (optional |     |     | proto), |
|     | 0 priority) + JSON   |     |     | Syslog  |
(otherwise)
or
syslog_appname +
syslog_procid + JSON
Secuwiz Secuway SSLVPN 5 Secuwiz custom format secuwiz_s vpn Traffic (srcip,
srcport,
| (U v1.0 / M v3.0, v3.1) | 6   | ecuway_ss |     |        |
| ----------------------- | --- | --------- | --- | ------ |
|                         | 5   | lvpn      |     | dstip, |
dstport, and
2
proto),
Syslog
(otherwise)
|                    | 5   | cef_device |          |         |
| ------------------ | --- | ---------- | -------- | ------- |
| SentinelOne (CEF2) | CEF |            | endpoint | Traffic |
|                    | 1   | _vendor    |          |         |
(srcip),
Click here to configure log
7
Syslog
ingestion
5
(otherwise)
| SentinelOne Mgmt (CEF) | CEF | sentinelone | endpoint | IDPS/Malwar |
| ---------------------- | --- | ----------- | -------- | ----------- |
5
e Sandbox
|     | 1   | _endpoint |     |     |
| --- | --- | --------- | --- | --- |
Events
4
(threat,
3
normalized
or
from
5
classification
8
), Traffic
7
(srcip,
0
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
IDPS/Malwar
| SentinelOne Security Center | 5 CEF | sentinelone | endpoint |     |
| --------------------------- | ----- | ----------- | -------- | --- |
e Sandbox
| (CEF) | 1   | _endpoint |     |     |
| ----- | --- | --------- | --- | --- |
Events
4
(threat,
3
normalized
or
from
5
classification
8
), Traffic
(srcip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |          |
| --- | --- | --- | --- | -------- |
|     | 7   |     |     | srcport, |
|     | 0   |     |     | dstip,   |
dstport, and
proto),
Syslog
(otherwise)
SentinelOne Singularity Mobile 5 syslog + regex + JSON sentineone endpoint Traffic (srcip,
srcport,
|     | 6   | _sm |     |     |
| --- | --- | --- | --- | --- |
dstip,
2
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Seqrite Endpoint Security | Custom CEF (missing |            | endpoint |                 |
| ------------------------- | ------------------- | ---------- | -------- | --------------- |
|                           | 5                   | seqrite_en |          | Traffic (srcip, |
last two fields)
|     | 9   | dpoint_sec |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 4   | urity      |     | dstip,       |
|     | 3   |            |     | dstport, and |
proto),
Syslog
(otherwise)
|     | CEF |        | pam |                 |
| --- | --- | ------ | --- | --------------- |
|     | 5   | segura |     | Traffic (srcip, |
Segura (CEF)
|     | 1   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
ServiceNow Now Platform 5 RFC 3164 + KVP servicenow paas Traffic (srcip,
|     | 6   | _nowplatfo |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 6   | rm         |     | dstip,       |
|     | 8   |            |     | dstport, and |
proto),
Syslog
(otherwise)
Traffic (srcip,
| ShareTech Firewall | 5 ShareTech custom | sharetech_ | firewall |     |
| ------------------ | ------------------ | ---------- | -------- | --- |
srcport,
|     | 6 format or KVP | fw  |     |        |
| --- | --------------- | --- | --- | ------ |
|     | 0               |     |     | dstip, |
dstport, and
9

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
| Skyhigh Secure Web Gateway | 6 RFC 3164 | skyhigh_se | websec |     |
| -------------------------- | ---------- | ---------- | ------ | --- |
IDPS/Malwar
|     | 0   | cure_web_ |     | e Sandbox |
| --- | --- | --------- | --- | --------- |
|     | 7   | gateway   |     | Events    |
6
(threat, ids),
Traffic (srcip,
srcport,
dstip,
dstport,
proto),
Syslog
(otherwise)
| Snare Agent | 5 Prophecy International | snare_age | paas | Windows      |
| ----------- | ------------------------ | --------- | ---- | ------------ |
|             | 5 Holdings custom format | nt        |      | Events       |
|             | 9                        |           |      | (winlogevent |
|             | 0                        |           |      | ), Traffic   |
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Sniper IPS | 5 KVP | sniperips  | idps | Traffic         |
| ---------- | ----- | ---------- | ---- | --------------- |
|            | 1     |            |      | (srcip),        |
|            | 8     |            |      | Syslog          |
|            | 2     |            |      | (otherwise)     |
|            | 5 CEF | snowflake_ | mscs | Traffic (srcip, |
Snowflake (CEF)
|     | 1   | ghx |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
|     | RFC 3614 + JSON |          | ndr |                 |
| --- | --------------- | -------- | --- | --------------- |
|     | 5               | socradar |     | Traffic (srcip, |
SOCRadar
|     | 8   |     |     | srcport, |
| --- | --- | --- | --- | -------- |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstip,       |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 6 SoftEther custom format | softether_v | vpn | Traffic (srcip, |
| --- | ------------------------- | ----------- | --- | --------------- |
SoftEther VPN Server
|     | 0   | pn_server |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 8   |           |     | dstip,       |
|     | 9   |           |     | dstport, and |
proto),
Syslog
(otherwise)
|     | SolarWinds |            | weblogs |                 |
| --- | ---------- | ---------- | ------- | --------------- |
|     | 5          | solarwinds |         | Traffic (srcip, |
SolarWinds Serv-U
|     | 9   | _serv_u |     | srcport,     |
| --- | --- | ------- | --- | ------------ |
|     | 2   |         |     | dstip,       |
|     | 4   |         |     | dstport, and |
proto),
Syslog
(otherwise)
SonicWall Firewall 5 syslog + KVP sonicfw firewall IDPS/Malwar
|     | 1   |     |     | e Sandbox   |
| --- | --- | --- | --- | ----------- |
|     | 5   |     |     | Events (IDS |
|     | 2   |     |     | signature), |
Traffic
(srcip),
Syslog
(otherwise)
SonicWall Firewall (Filebeat) Beats (message contains firewall
|     | 5   | sonicfw |     |     |
| --- | --- | ------- | --- | --- |
Threat (IDS),
syslog + KVP)
|     | 7   |     |     | Threat    |
| --- | --- | --- | --- | --------- |
|     | 6   |     |     | (threat), |
7
Traffic (src
|     | wi  |     |     | IP), Syslog |
| --- | --- | --- | --- | ----------- |
|     | th  |     |     | (otherwise) |
5
7
6
7
–
5
8

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
6
7
re
se
rv
e
d
SonicWall NSa 6 SonicWall custom CEF sonicwall_ firewall Traffic (srcip,
|     | 0   | nsa |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 6   |     |     | dstip,       |
|     | 4   |     |     | dstport, and |
proto),
Syslog
(otherwise)
SonicWall - NSA 2400 (CEF)
|     | 5 CEF | sonicwall_ | firewall | Traffic (srcip, |
| --- | ----- | ---------- | -------- | --------------- |
srcport,
|     | 1   | nsa |     |     |
| --- | --- | --- | --- | --- |
dstip,
4
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
or
|     | 5   |     |     | Syslog      |
| --- | --- | --- | --- | ----------- |
|     | 8   |     |     | (otherwise) |
7
0
SonicWall VPN 5 RFC 3164 + regex sonicwall_v vpn Traffic (srcip,
|     | 5   | pn  |     | srcport, |
| --- | --- | --- | --- | -------- |
5
dstip,
|     | 6   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Sophos (CEF) | 5 CEF | sophos | endpoint | Traffic (srcip, |
| ------------ | ----- | ------ | -------- | --------------- |
srcport,
1
dstip,
4
|     | 3   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
or
Syslog
5
|     | 8   |     |     | (otherwise) |
| --- | --- | --- | --- | ----------- |
7
0

P msg_origi
msg_origi
Parser Name or Log Format n.categor Index
n.source
t y
Sophos endpoint 5 regex + KVP endpoint_s endpoint Traffic (srcip,
5 srcport,
ophos
6 dstip,
5 dstport, and
proto),
Syslog
(otherwise)
Sophos endpoint (beats) 5 JSON (Beats) endpoint_s endpoint Traffic
0 ophos (srcip),
4 Syslog
4 (otherwise)
Sophos firewall 5 KVP fw_sophos firewall Data goes to
5
the indicated
2
index based
0
on the
log_type:
If
Firew
all,
then
Traffi
c
index
If any
one
of
IDP,
Anti-
Virus,
Anti-
Spa
m, or
Cont
ent
Filter
it
goes
to
IDPS
/Mal
ware
Sand
box
Event
s
Index
For
any
other
log_t
ype,
if
srcip
exists
then
it
goes
to the
Traffi
c
Index

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
All
other
data
goes
to the
Syslo
g
index
|     | RFC 3164 + syslog |           | netlogs |        |
| --- | ----------------- | --------- | ------- | ------ |
|     | 5                 | sophos_sw |         | Syslog |
Sophos Switch
|     | 8   | itch |     |     |
| --- | --- | ---- | --- | --- |
8
8
Sophos Web Appliance 5 Sophos custom format or sophos_we websec Traffic (srcip,
|     | 6 KVP | b_app |     | srcport,     |
| --- | ----- | ----- | --- | ------------ |
|     | 2     |       |     | dstip,       |
|     | 6     |       |     | dstport, and |
proto),
Syslog
(otherwise)
| Spica Access Control | Spica custom format + |            | iam |                 |
| -------------------- | --------------------- | ---------- | --- | --------------- |
|                      | 6                     | spica_acce |     | Traffic (srcip, |
JSON
|     | 0   | ss_control |     | srcport,     |
| --- | --- | ---------- | --- | ------------ |
|     | 9   |            |     | dstip,       |
|     | 2   |            |     | dstport, and |
proto),
Syslog
(otherwise)
| Splashtop | 5 regex + JSON |           |       |                 |
| --------- | -------------- | --------- | ----- | --------------- |
|           |                | splashtop | asset | Traffic (srcip, |
6
srcport,
|     | 9   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
8
dstport, and
proto),
Syslog
(otherwise)
| Splunk Heavy Forwarder | 5                    | splunk_for |         |        |
| ---------------------- | -------------------- | ---------- | ------- | ------ |
|                        | Splunk custom format |            | netmgmt | Syslog |
|                        | 1                    | warder     |         |        |
8
8
Traffic (srcip,
Stormshield Net Security 5 Stormshield custom stormshield firewall
| Firewall | 6 format or KVP | _fw |     | srcport, |
| -------- | --------------- | --- | --- | -------- |
dstip,
2
dstport, and
5
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
| Symantec Endpoint Protection | 5                      | symantec_ |          | Traffic     |
| ---------------------------- | ---------------------- | --------- | -------- | ----------- |
|                              | Symantec custom format |           | endpoint |             |
|                              | 5                      | ep        |          | (dstip),    |
|                              | 2                      |           |          | Syslog      |
|                              | 5                      |           |          | (otherwise) |
| Symantec Firewal             | 5                      | symantec  |          |             |
|                              | Symantec custom format |           | firewall | Syslog      |
1
5
5
Symantec Messaging Gateway 5 Symantec custom format symantec_ email Traffic (srcip,
|     | 5   | messaging |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 6   | _gateway  |     | dstip,       |
|     | 7   |           |     | dstport, and |
proto),
Syslog
(otherwise)
| Symantec DLP (CEF) | CEF | symantec | symantec_ | Traffic (srcip, |
| ------------------ | --- | -------- | --------- | --------------- |
5
srcport,
dlp
1
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
Synology Directory Server 5 Synology custom format synology_d asset Traffic (srcip,
|     | 5   | irectory_se |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 9   | rver        |     | dstip,       |
|     | 7   |             |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                              | t        |            | y       |                 |
| ---------------------------- | -------- | ---------- | ------- | --------------- |
| Synology DiskStation Manager | RFC 3164 |            | storage |                 |
|                              | 6        | synology_d |         | Traffic (srcip, |
|                              | 0        | sm         |         | srcport,        |
(DSM)
|     | 7   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 2   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Syslog4Net | 5 syslog (regex) |            |            |         |
| ---------- | ---------------- | ---------- | ---------- | ------- |
|            |                  | syslog4net | log_proces | Windows |
7
|     |     |     | sing | Events       |
| --- | --- | --- | ---- | ------------ |
|     | 1   |     |      | (winlogevent |
5
), Syslog
(otherwise)
| Tait Communications P25 Base | Tait Communications |     | miscs |                 |
| ---------------------------- | ------------------- | --- | ----- | --------------- |
|                              | 5                   |     |       | Traffic (srcip, |
taitcommu
custom syslog
| Station  | 9   | nications_p |     | srcport,     |
| -------- | --- | ----------- | --- | ------------ |
|          | 1   | 25_basest   |     | dstip,       |
|          | 2   |             |     | dstport, and |
ation
proto),
Syslog
(otherwise)
| Tait Communications RFSS | RFC 3164 |              | miscs |                 |
| ------------------------ | -------- | ------------ | ----- | --------------- |
|                          | 5        | taitcommu    |       | Traffic (srcip, |
|                          | 9        | nications_rf |       | srcport,        |
Controller
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
ss_controll
|     | 1   | er  |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Tait Communications Tait | RFC 5424 |     | miscs |     |
| ------------------------ | -------- | --- | ----- | --- |
5
|     |     | taitcommu |     | Traffic (src IP |
| --- | --- | --------- | --- | --------------- |
9
| Dynamic Analysis  |     | nications_t |     | , src port, dst |
| ----------------- | --- | ----------- | --- | --------------- |
|                   | 4   | ait_dynami  |     | IP, dst port,   |
0
|     |     | c_analysis |     | and proto), |
| --- | --- | ---------- | --- | ----------- |
Syslog
(otherwise)
| Tait Communications Tait | 6 RFC 5424 |     | netmgmt | Traffic (src IP |
| ------------------------ | ---------- | --- | ------- | --------------- |
taitcommu
|     | 0   | nications_t |     | , src port, dst |
| --- | --- | ----------- | --- | --------------- |
EnableFleet
|     | 8   |     |     | IP, dst port, |
| --- | --- | --- | --- | ------------- |
ait_enable
|     | 1   |     |     | and proto), |
| --- | --- | --- | --- | ----------- |
_fleet
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                          | t        |             | y   |                 |
| ------------------------ | -------- | ----------- | --- | --------------- |
| Tait Communications Tait | RFC 5424 |             | iam |                 |
|                          | 6        | taitcommu   |     | Traffic (src IP |
|                          | 0        | nications_t |     | , src port, dst |
EnableProtect
|     | 7   | ait_enable |     | IP, dst port, |
| --- | --- | ---------- | --- | ------------- |
|     | 7   | _protect   |     | and proto),   |
Syslog
(otherwise)
|     | RFC 3164 + regex |            | iam |                 |
| --- | ---------------- | ---------- | --- | --------------- |
|     | 5                | tenable_ad |     | Traffic (src IP |
Tenable AD
|     | 9   |     |     | , src port, dst |
| --- | --- | --- | --- | --------------- |
|     | 5   |     |     | IP, dst port,   |
|     | 5   |     |     | and proto),     |
Syslog
(otherwise)
|     | CEF |          | saas |                 |
| --- | --- | -------- | ---- | --------------- |
|     | 5   | teramind |      | Traffic (src IP |
Teramind CEF
|     | 1   |     |     | , src port, dst |
| --- | --- | --- | --- | --------------- |
|     | 4   |     |     | IP, dst port,   |
|     | 3   |     |     | and proto),     |
|     | or  |     |     | Syslog          |
|     | 5   |     |     | (otherwise)     |
8
7
0
Thales Group CipherTrust 5 RFC 3164 + local header iam Traffic (srcip,
thales_ciph
| Manager | 6 + CEF header +    | er_trust_m |     | srcport, |
| ------- | ------------------- | ---------- | --- | -------- |
|         | 7 message with JSON |            |     | dstip,   |
anager
|     | 4   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | RFC 5424 |             | threat_intel |                 |
| --- | -------- | ----------- | ------------ | --------------- |
|     | 6        | threater_en |              | Traffic (srcip, |
threatER Enforce
|     | 0   | force |     | srcport,     |
| --- | --- | ----- | --- | ------------ |
|     | 7   |       |     | dstip,       |
|     | 3   |       |     | dstport, and |
proto),
Syslog
(otherwise)
ThreatLocker Zero Trust EPP 5 JSON (in an array) Traffic (srcip,
|     |     | threat_lock | endpoint |          |
| --- | --- | ----------- | -------- | -------- |
|     | 2   | er_zero_tru |          | srcport, |
|     | 0   |             |          | dstip,   |
st_epp
|     | 0   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |             |
| --- | --- | --- | --- | ----------- |
|     | (T  |     |     | proto),     |
|     | C   |     |     | Syslog      |
|     | P   |     |     | (otherwise) |
o
nl
y)
|     | regex + JSON |         | saas |                 |
| --- | ------------ | ------- | ---- | --------------- |
|     | 6            | threatx |      | Traffic (srcip, |
ThreatX
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 7   |     |     | dstip,       |
|     | 0   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|                  | 5 JSON | tmaxsoft_w | weblogs |                 |
| ---------------- | ------ | ---------- | ------- | --------------- |
| TmaxSoft WebtoB  |        |            |         | Traffic (src IP |
|                  | 8      | ebtob      |         | , src port, dst |
7
IP, dst port,
7
and proto),
Syslog
(otherwise)
|     | RFC 5424 + XML |             | endpoint |                 |
| --- | -------------- | ----------- | -------- | --------------- |
|     | 5              | trellix_epo |          | Traffic (src IP |
Trellix EPO
|     | 9   |     |     | , src port, dst |
| --- | --- | --- | --- | --------------- |
|     | 0   |     |     | IP, dst port,   |
|     | 2   |     |     | and proto),     |
Syslog
(otherwise)
| Trellix ESM (Enterprise Security | RFC 3164 + syslog |             | siem |                 |
| -------------------------------- | ----------------- | ----------- | ---- | --------------- |
|                                  | 5                 | trellix_esm |      | Traffic (src IP |
8
| Manager)  |     |     |     | , src port, dst |
| --------- | --- | --- | --- | --------------- |
7
IP, dst port,
3
and proto),
Syslog
(otherwise)
Trellix FireEye - CMS (CEF) 5 CEF fireeye_cm ndr Traffic (srcip,
|     | 1   | s           |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 4   | trellix_cms |     | dstip,       |
|     | 3   |             |     | dstport, and |
|     | or  |             |     | proto),      |
|     | 5   |             |     | Syslog       |
|     | 8   |             |     | (otherwise)  |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
7
0
Trellix FireEye - eMPS (CEF) 5 CEF fireeye_em mdr Traffic (srcip,
|     | 1   | ps          |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 4   | trellix_emp |     | dstip,       |
|     | 3   | s           |     | dstport, and |
|     | or  |             |     | proto),      |
|     | 5   |             |     | Syslog       |
|     | 8   |             |     | (otherwise)  |
7
0
| Trellix FireEye - ETP (CEF) | CEF |             | email |                 |
| --------------------------- | --- | ----------- | ----- | --------------- |
|                             | 5   | fireeye_cm  |       | Traffic (srcip, |
|                             | 1   | s           |       | srcport,        |
|                             | 4   | trellix_cms |       | dstip,          |
|                             | 3   |             |       | dstport, and    |
|                             | or  |             |       | proto),         |
|                             | 5   |             |       | Syslog          |
|                             | 8   |             |       | (otherwise)     |
7
0
| Trellix FireEye - fMPS (CEF) | CEF |              | mdr |                 |
| ---------------------------- | --- | ------------ | --- | --------------- |
|                              | 5   | fireeye_fm   |     | Traffic (srcip, |
|                              | 1   | ps           |     | srcport,        |
|                              | 4   | trellix_fmps |     | dstip,          |
|                              | 3   |              |     | dstport, and    |
|                              | or  |              |     | proto),         |
|                              | 5   |              |     | Syslog          |
|                              | 8   |              |     | (otherwise)     |
7
0
Trellix FireEye HX
|     | 5 CEF + regex | fireeye_hx | endpoint | Traffic (srcip, |
| --- | ------------- | ---------- | -------- | --------------- |
|     | 6             |            |          | srcport,        |
|     | 4             |            |          | dstip,          |
|     | 4             |            |          | dstport, and    |
proto),
Syslog
(otherwise)
| Trellix FireEye - HX (CEF) | CEF |            | paas |                 |
| -------------------------- | --- | ---------- | ---- | --------------- |
|                            | 5   | fireeye_hx |      | Traffic (srcip, |
|                            | 1   | trellix_hx |      | srcport,        |
|                            | 4   |            |      | dstip,          |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 3   |     |     | dstport, and |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| Trellix FireEye - MAS (CEF) | CEF |             | xdr |                 |
| --------------------------- | --- | ----------- | --- | --------------- |
|                             | 5   | fireeye_ma  |     | Traffic (srcip, |
|                             | 1   | s           |     | srcport,        |
|                             | 4   | trellix_mas |     | dstip,          |
|                             | 3   |             |     | dstport, and    |
|                             | or  |             |     | proto),         |
|                             | 5   |             |     | Syslog          |
|                             | 8   |             |     | (otherwise)     |
7
0
| Trellix FireEye - MPS (CEF) | CEF |            | ndr |                 |
| --------------------------- | --- | ---------- | --- | --------------- |
|                             | 5   | fireeye_mp |     | Traffic (srcip, |
|                             | 1   | s          |     | srcport,        |
|                             | 4   |            |     | dstip,          |
|                             | 3   |            |     | dstport, and    |
|                             | or  |            |     | proto),         |
|                             | 5   |            |     | Syslog          |
|                             | 8   |            |     | (otherwise)     |
7
0
| Trend Micro Apex Central (CEF) | CEF |            | endpoint | Traffic (srcip, |
| ------------------------------ | --- | ---------- | -------- | --------------- |
|                                | 5   | trendmicro |          |                 |
|                                | 1   | _apex_cen  |          | srcport,        |
dstip,
|     | 4   | tral |     |     |
| --- | --- | ---- | --- | --- |
dstport, and
3
|     | or  |     |     | proto), |
| --- | --- | --- | --- | ------- |
Syslog
5
(otherwise)
8
7
0

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                              | t   |            | y     |                 |
| ---------------------------- | --- | ---------- | ----- | --------------- |
| Trend Micro - Deep Discovery | CEF |            | email |                 |
|                              | 5   | trendmicro |       | Traffic (srcip, |
Email Inspector (CEF)
|     | 1   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
_deep_disc
|     | 4   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
overy_ema
|     | 3   | il  |     | dstport, and |
| --- | --- | --- | --- | ------------ |
|     | or  |     |     | proto),      |
|     | 5   |     |     | Syslog       |
|     | 8   |     |     | (otherwise)  |
7
0
| Trend Micro Deep Security | LEEF (custom Trend |            | endpoint, |                 |
| ------------------------- | ------------------ | ---------- | --------- | --------------- |
|                           | 5                  | trendmicro |           | Traffic (srcip, |
|                           | 9 Micro format)    | _deep_sec  | asset,    | srcport,        |
miscs
|     | 5   | urity |     | dstip,       |
| --- | --- | ----- | --- | ------------ |
|     | 6   |       |     | dstport, and |
proto),
Syslog
(otherwise)
Trend Micro - Deep Security 5 LEEF trendmicro endpoint Traffic
| Agent (LEEF)          | 5     |            |      |                 |
| --------------------- | ----- | ---------- | ---- | --------------- |
|                       |       | _dsa       |      | (srcip),        |
|                       | 2     |            |      | Syslog          |
|                       | 2     |            |      | (otherwise)     |
| Trend Micro Interscan | 5 TSV | trend_micr | saas | Traffic (srcip, |
| Messaging             | 6     |            |      | srcport,        |
o_intersca
|     | 7   |     |     | dstip, |
| --- | --- | --- | --- | ------ |
n_messagi
|     | 8   | ng  |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
| Trend Micro Proxy | 5 syslog (regex) | trendmicro | websec | Traffic     |
| ----------------- | ---------------- | ---------- | ------ | ----------- |
|                   | 5                | _proxy     |        | (dstip),    |
|                   | 4                |            |        | Syslog      |
|                   | 0                |            |        | (otherwise) |
Trend Micro TippingPoint 5 syslog priority + syslog idps Traffic (srcip,
trend_micr
|     | 6 timestamp + TSV | o_tippingp |     | srcport, |
| --- | ----------------- | ---------- | --- | -------- |
|     | 7                 |            |     | dstip,   |
oint
|     | 2   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                        | t                   |            | y        |        |
| ---------------------- | ------------------- | ---------- | -------- | ------ |
| Trend Micro Worry-Free | Custom header + CEF |            | endpoint |        |
|                        | 6                   | trend_micr |          | Threat |
Business Security Service
2
|     |     | o_worry_fr |     | (threat), |
| --- | --- | ---------- | --- | --------- |
0
| Parser  |     | ee_busines  |     | Traffic (srcip, |
| ------- | --- | ----------- | --- | --------------- |
|         | 9   | s_security_ |     | srcport,        |
|         |     | service     |     | dstip,          |
dstport, and
proto),
Syslog
(otherwise)
| Tripwire Enterprise | 5   | tripwire |          |        |
| ------------------- | --- | -------- | -------- | ------ |
|                     | KVP |          | endpoint | Syslog |
1
8
6
|     | 6 RFC 5424 | ubika_waf | waf | Traffic (srcip, |
| --- | ---------- | --------- | --- | --------------- |
Ubika WAF
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 7   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Ubiquiti UAP-AC-Pro | 5                   | ubiquiti |         |                 |
| ------------------- | ------------------- | -------- | ------- | --------------- |
|                     | RFC 3164 (with      |          | netlogs | Traffic (srcip, |
|                     | 5 hostname) + regex |          |         | srcport,        |
|                     | 5                   |          |         | dstip,          |
2
dstport, and
proto),
Syslog
(otherwise)
|     | 5 RFC 3164 + regex + | ubiquiti_ud | cloudsec | Traffic (srcip, |
| --- | -------------------- | ----------- | -------- | --------------- |
Ubiquiti UDM Pro
KVP
|     | 9   | m_pro |     | srcport,     |
| --- | --- | ----- | --- | ------------ |
|     | 2   |       |     | dstip,       |
|     | 6   |       |     | dstport, and |
proto),
Syslog
(otherwise)
| Ubiquiti UniFi Security Gateway | RFC 3164 + regex + |             | netlogs |                 |
| ------------------------------- | ------------------ | ----------- | ------- | --------------- |
|                                 | 5                  | ubiquiti_us |         | Traffic (srcip, |
KVP
|     | 9   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
g
|     | 0   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 0   |     |     | dstport, and |
proto),

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Syslog
(otherwise)
UMV WSS (Web Server 5 RFC 3164 + regex umv_wss ndr Traffic (srcip,
|     | 7   |     |     | srcport, |
| --- | --- | --- | --- | -------- |
Safeguard)
|     | 0   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstport, and |
proto),
Syslog
(otherwise)
Unix
|     | 5 (RFC 3164) + regex | unix | unixlogs | Traffic (srcip, |
| --- | -------------------- | ---- | -------- | --------------- |
|     | 6                    |      |          | srcport,        |
|     | 3                    |      |          | dstip,          |
|     | 3                    |      |          | dstport, and    |
proto),
Syslog
(otherwise)
Untangle Firewall (Syslog 5 syslog + JSON json firewall IDPS/Malwar
e Sandbox
| JSON) | 1   |     |     |           |
| ----- | --- | --- | --- | --------- |
|       | 4   |     |     | Events    |
|       | 2   |     |     | (threat), |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Varonis DatAdvantage (CEF) |     | varonis_da |     | Traffic (srcip, |
| -------------------------- | --- | ---------- | --- | --------------- |
|                            | CEF |            | dlp |                 |
5
|     |     | tadvantage |     | srcport, |
| --- | --- | ---------- | --- | -------- |
1
dstip,
4
dstport, and
3
proto),
or
Syslog
5
(otherwise)
8
7
0
|     | 5 RFC 3164 + KVP | vectra_ai_ | xdr | IDPS/Malwar |
| --- | ---------------- | ---------- | --- | ----------- |
Vectra AI Platform
|     | 7   | platform |     | e Sandbox |
| --- | --- | -------- | --- | --------- |
Events

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |                 |
| --- | --- | --- | --- | --------------- |
|     | 3   |     |     | (threat),       |
|     | 8   |     |     | Traffic (srcip, |
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Veeam Backup & Replication | RFC 5424 + regex, RFC |          | dlp |                 |
| -------------------------- | --------------------- | -------- | --- | --------------- |
|                            | 5                     | veeam_ba |     | Traffic (srcip, |
5424 + KVP
|     | 7   | ckup_replic |     | srcport,     |
| --- | --- | ----------- | --- | ------------ |
|     | 5   | ation       |     | dstip,       |
|     | 1   |             |     | dstport, and |
proto),
Syslog
(otherwise)
| Versa Networks Firewall | 5                    | versa_netw |          | IDPS/Malwar |
| ----------------------- | -------------------- | ---------- | -------- | ----------- |
|                         | RFC 3164 or RFC 5424 |            | firewall |             |
|                         | 5 + KVP              | orks_fw    |          | e Sandbox   |
|                         | 6                    |            |          | Events      |
|                         | 8                    |            |          | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Versa Networks Unified SASE | CEF |            | sase |                 |
| --------------------------- | --- | ---------- | ---- | --------------- |
|                             | 5   | versa_netw |      | Traffic (srcip, |
|                             | 7   | orks_sase  |      | srcport,        |
Platform
|     | 6   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 6   |     |     | dstport, and |
proto),
Syslog
(otherwise)
VMware - Carbon Black (LEEF) 5 LEEF vmware_cb endpoint Traffic
5
(srcip),
2
Syslog
|        | 2                    |        |          | (otherwise) |
| ------ | -------------------- | ------ | -------- | ----------- |
|        | 5                    | vmware |          |             |
| VMware | VMware custom format |        | unixlogs | Syslog      |
6

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
0
0
|     | Modified RFC 5424 + |           | paas |                 |
| --- | ------------------- | --------- | ---- | --------------- |
|     | 5                   | vmware_es |      | Traffic (srcip, |
VMware ESXi
|     | 8 plain text or JSON |     |     | srcport, |
| --- | -------------------- | --- | --- | -------- |
xi
|     | 7   |     |     | dstip,       |
| --- | --- | --- | --- | ------------ |
|     | 8   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| VMware Horizon | 5 RFC 5424 + description |          |      | Traffic (srcip, |
| -------------- | ------------------------ | -------- | ---- | --------------- |
|                |                          | vmware_h | paas |                 |
|                | 6                        | orizon   |      | srcport,        |
|                | 8                        |          |      | dstip,          |
|                | 7                        |          |      | dstport, and    |
proto),
Syslog
(otherwise)
| VMware NSX Edge Firewall | RFC 3164 + KVP (with |            | firewall |                 |
| ------------------------ | -------------------- | ---------- | -------- | --------------- |
|                          | 5                    | vmware_ns  |          | Traffic (srcip, |
|                          | Netfilter logs)      | x_edge_fir |          | srcport,        |
7
|     | 5   | ewall |     | dstip,       |
| --- | --- | ----- | --- | ------------ |
|     | 8   |       |     | dstport, and |
proto),
Syslog
(otherwise)
VMware NSX-T Data Center 5 regex + KVP (with JSON vmware_ns endpoint Traffic (srcip,
|     | 5       | x_t |             | srcport, |
| --- | ------- | --- | ----------- | -------- |
|     | values) |     | (unless log |          |
|     | 7       |     |             | dstip,   |
type is
|     | 4   |     | dfwpktlogs, | dstport, and |
| --- | --- | --- | ----------- | ------------ |
proto),
then
|     |     |     | category is | Syslog      |
| --- | --- | --- | ----------- | ----------- |
|     |     |     | firewall)   | (otherwise) |
Traffic (srcip,
| VMware UAG | 5 VMware custom format | vmware_u | iam |          |
| ---------- | ---------------------- | -------- | --- | -------- |
|            | 6                      | ag       |     | srcport, |
|            | 2                      |          |     | dstip,   |
dstport, and
0
proto),
Syslog
(otherwise)
Traffic (srcip,
| VMware Vcenter | 5 VMware custom format | vmware_vc | itsm |          |
| -------------- | ---------------------- | --------- | ---- | -------- |
|                | 6                      | enter     |      | srcport, |
dstip,

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |              |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | dstport, and |
|     | 5   |     |     | proto),      |
Syslog
(otherwise)
VMware VeloCloud SD-WAN 5 regex + KVP or message vmware_ve netmgmt Traffic (srcip,
|     | 6   | locloud_sd |     | srcport, |
| --- | --- | ---------- | --- | -------- |
|     | 8   |            |     | dstip,   |
wan
|     | 5   |     |     | dstport, and |
| --- | --- | --- | --- | ------------ |
proto),
Syslog
(otherwise)
|     | RFC 5424 |              | pan |                 |
| --- | -------- | ------------ | --- | --------------- |
|     | 5        | wallix_basti |     | Traffic (srcip, |
Wallix Bastion
|     | 9   | on  |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 8   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| WatchGuard - XTM | 5    |           |          |         |
| ---------------- | ---- | --------- | -------- | ------- |
|                  | LEEF | watchguar | firewall | Traffic |
5
|     |     | d_fw |     | (srcip), |
| --- | --- | ---- | --- | -------- |
|     | 2   |      |     | Syslog   |
2
(otherwise)
| WatchGuard firewall security | 5                | watchguar |          | Traffic (srcip, |
| ---------------------------- | ---------------- | --------- | -------- | --------------- |
|                              | RFC 3164 + regex |           | firewall |                 |
| appliance                    | 5                | d_fw      |          | srcport,        |
|                              | 5                |           |          | dstip,          |
|                              | 7                |           |          | dstport, and    |
proto),
Syslog
(otherwise)
| Wazuh SIEM | 5 (regex) + JSON | wazuh_sie | endpoint | Windows      |
| ---------- | ---------------- | --------- | -------- | ------------ |
|            | 6                | m         |          | Events       |
|            | 3                |           |          | (winlogevent |
|            | 4                |           |          | ) , Traffic  |
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
Windows DNS Server 5 Microsoft custom format windows_d weblogs Traffic (srcip,
|     | 5   | ns_server |     | srcport,     |
| --- | --- | --------- | --- | ------------ |
|     | 9   |           |     | dstip,       |
|     | 9   |           |     | dstport, and |
proto),
Syslog
(otherwise)
Windows Event NXLog 5 regex or JSON microsoft_ endpoint Windows
|     | 6   | windows |     | Events |
| --- | --- | ------- | --- | ------ |
Click here to configure HostIP
|     | 0   |     |     | (winlogevent |
| --- | --- | --- | --- | ------------ |
|     | 1   |     |     | ), Traffic   |
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
Windows System Security 5 Microsoft custom format windows_s endpoint Windows
|     | 6   | ystem_sec |     | Events       |
| --- | --- | --------- | --- | ------------ |
|     | 1   | urity     |     | (winlogevent |
|     | 0   |           |     | ), Traffic   |
(srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Wins IPS ONE-1 / Wins DDX | 5                  | winsips |      | IDPS/Malwar   |
| ------------------------- | ------------------ | ------- | ---- | ------------- |
|                           | syslog with Splunk |         | idps |               |
|                           | 5 header + (regex) |         |      | e Sandbox     |
|                           | 3                  |         |      | Events        |
|                           | 8                  |         |      | (vendor.attac |
k_name),
Syslog
(otherwise)
WINS Sniper NGFW 5 regex + KVP wins_snipe firewall Traffic (srcip,
|     | 6   | r_ngfw |     | srcport,     |
| --- | --- | ------ | --- | ------------ |
|     | 4   |        |     | dstip,       |
|     | 9   |        |     | dstport, and |

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|     | t   |     | y   |     |
| --- | --- | --- | --- | --- |
proto),
Syslog
(otherwise)
|     | KVP |           | weblogs |                 |
| --- | --- | --------- | ------- | --------------- |
|     | 6   | wordpress |         | Traffic (srcip, |
WordPress
|     | 0   |     |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
|     | 5 CEF | zecurion_dl | dlp | Traffic (srcip, |
| --- | ----- | ----------- | --- | --------------- |
Zecurion - DLP (CEF)
|     | 1   | p   |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 4   |     |     | dstip,       |
|     | 3   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Zeek (NXLog method) | JSON |      | json |        |
| ------------------- | ---- | ---- | ---- | ------ |
|                     | 5    | json |      | Syslog |
1
4
2
|     | 5 RFC 3164 + syslog | zimbra_em | email | Traffic (srcip, |
| --- | ------------------- | --------- | ----- | --------------- |
Zimbra Email
|     | 8   | ail |     | srcport,     |
| --- | --- | --- | --- | ------------ |
|     | 9   |     |     | dstip,       |
|     | 9   |     |     | dstport, and |
proto),
Syslog
(otherwise)
| Zix Mail | 5                 | zix_mail   |       | Traffic         |
| -------- | ----------------- | ---------- | ----- | --------------- |
|          | Zix custom format |            | email |                 |
|          | 1                 |            |       | (srcip),        |
|          | 8                 |            |       | Syslog          |
|          | 5                 |            |       | (otherwise)     |
|          | RFC 5424 + JSON   |            | ndr   |                 |
|          | 5                 | zscaler_de |       | Traffic (srcip, |
Zscaler Deception
|     | 9   | ception |     | srcport,     |
| --- | --- | ------- | --- | ------------ |
|     | 0   |         |     | dstip,       |
|     | 9   |         |     | dstport, and |
proto),
Syslog
(otherwise)

|     | P   |     | msg_origi |     |
| --- | --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format |     | n.categor | Index |
| ----------- | ------------- | --- | --------- | ----- |
n.source
|                         | t     |         | y      |        |
| ----------------------- | ----- | ------- | ------ | ------ |
| Zscaler NSSWeblog (CEF) | 5 CEF | zscaler | websec | Syslog |
1
4
3
or
5
8
7
0
| Zscaler ZIA Firewall | 5    | zscaler_zia |          | IDPS/Malwar |
| -------------------- | ---- | ----------- | -------- | ----------- |
|                      | JSON |             | firewall |             |
|                      | 5    | _fw         |          | e Sandbox   |
|                      | 4    |             |          | Events      |
|                      | 9    |             |          | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Zscaler ZIA Web | 5    | zscaler_zia |         | IDPS/Malwar |
| --------------- | ---- | ----------- | ------- | ----------- |
|                 | JSON |             | weblogs |             |
|                 | 5    | _web        |         | e Sandbox   |
|                 | 5    |             |         | Events      |
|                 | 0    |             |         | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),
Syslog
(otherwise)
| Zscaler ZPA | 5    | zscaler_zp |     | IDPS/Malwar |
| ----------- | ---- | ---------- | --- | ----------- |
|             | JSON |            | vpn |             |
|             | 5    | a          |     | e Sandbox   |
|             | 5    |            |     | Events      |
|             | 1    |            |     | (threat),   |
Traffic (srcip,
srcport,
dstip,
dstport, and
proto),

|     | P   | msg_origi |     |
| --- | --- | --------- | --- |
msg_origi
| Parser Name | or Log Format | n.categor | Index |
| ----------- | ------------- | --------- | ----- |
n.source
|     | t   | y   |     |
| --- | --- | --- | --- |
Syslog
(otherwise)
Zyxel Firewall 5 regex + KVP zyxel_fw firewall Traffic (srcip,
|     | 5   |     | srcport,     |
| --- | --- | --- | ------------ |
|     | 9   |     | dstip,       |
|     | 4   |     | dstport, and |
proto),
Syslog
(otherwise)