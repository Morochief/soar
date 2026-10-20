# M03 - Modular Sensor Concepts And Configuration

> **Documento Original:** `m03-modular_sensor_concepts_and_configuration.pdf`  
> **Total Páginas:** 120  
> **Formato:** Transcripción / Manual de Curso Stellar Cyber Open XDR

---


<!-- Página 1 -->

 MODULAR SENSOR CONCEPTS AND 
 CONFIGURATION TRANSCRIPT 
 MODULAR  SENSOR  CONCEPTS  AND  CONFIGURATION  TRANSCRIPT  ..........................................  1 
 L00  -  INTRODUCTION  AND  AGENDA  ..................................................................................................................................  3 
 L00A-PRES:  Modular  Sensor  Module  Lessons  Agenda  (08m:52s)  ....................................................  3 
 L01  -  MODULAR  SENSORS  INTRODUCTION  ..................................................................................................................  7 
 L01A-PRES:  Modular  Sensors  Introduction  (06m:49s)  ..................................................................................  7 
 L02  -  ESSENTIAL  TERMINOLOGY  .............................................................................................................................................  9 
 L02A-PRES:  Essential  Terminology  (12m:58s)  ......................................................................................................  9 
 L03  -  COLLECTING  NETWORK  TRAFFIC  .........................................................................................................................  12 
 L03A-PRES:  Collecting  Network  Traffic  (08m:48s)  ........................................................................................  12 
 L04  -  FUNCTIONALITY  OVERVIEW  .......................................................................................................................................  14 
 L04A-PRES:  Functionality  Overview  (06m:15s)  .................................................................................................  14 
 L05  -  DATA  PROCESSING  .............................................................................................................................................................  16 
 L05A-PRES:  Data  Processing  (04m:49s)  .................................................................................................................  16 
 L06  -  MODULAR  SENSOR  PROFILES  ..................................................................................................................................  18 
 L06A-PRES:  Modular  Sensor  Proﬁles  (12m:49s)  ...............................................................................................  18 
 L07  -  MODULAR  SENSOR  CONFIGURATION  ...............................................................................................................  21 
 L07A-PRES:  Modular  Sensor  Conﬁguration  (03m:31s)  ...............................................................................  21 
 L07B-DEMO:  Modular  Sensor  Conﬁguration  (16m:18s)  .............................................................................  22 
 L08  -  PARSERS,  NORMALIZATION,  AND  INTERFLOW  ........................................................................................  26 
 L08A-PRES:  Parsers,  Normalization,  and  Interﬂow  (15m:06s)  ............................................................  26 
 L09  -  LOG  FORWARDER  AND  LOG  FILTER  CONFIGURATION  ....................................................................  30 
 L09A-PRES:  Log  Forwarder  and  Log  Filter  Conﬁguration  (12m:09s)  ...........................................  30 
 L10  -  LOG  FORWARDER  EXAMPLE  ......................................................................................................................................  33 
 L10A-PRES:  Log  Forwarder  Example  (05m:35s)  .............................................................................................  33 
 L10B-DEMO:  Log  Forwarder  Example  (28m:16s)  ...........................................................................................  34 
 L11  -  LOG  SOURCE  CONFIGURATION  FOR  SINGLE  TCP  OR  UDP  PORT  .............................................  40 
 L11A-PRES:  Log  Source  Conﬁguration  for  Single  TCP  or  UDP  Port  (05m:55s)  .....................  40 
 L11B-DEMO:  Log  Source  Conﬁguration  for  Single  TCP  or  UDP  Port  (05m:28s)  ....................  41 
 L12  -  VALIDATE  LOG  FORWARDER  .....................................................................................................................................  42 
 L12A-PRES:  Validate  Log  Forwarder  (07m:46s)  ..............................................................................................  42 
 L13  -  LOG  FORWARDER  PRESERVING  RAW  LOGS  ................................................................................................  44 
 L13A-PRES:  Log  Forwarder  Preserving  Raw  Logs  (05m:17s)  ..............................................................  44 
 L13B-DEMO:  Log  Forwarder  Preserving  Raw  Logs  (19m:26s)  ............................................................  46 
 ADM-03-01-224  1 


---

<!-- Página 2 -->

 L14  -  NETWORK  TRAFFIC  ANALYSIS  ..................................................................................................................................  50 
 L14A-PRES:  Network  Traffic  Analysis  (10m:22s)  .............................................................................................  50 
 L14B-DEMO:  Modular  Sensor  Network  Traffic  Analysis  (19m:01s)  ..................................................  53 
 L15  -  NETWORK  DETECTION  AND  RESPONSE  (NDR)  ........................................................................................  57 
 L15A-PRES: Network Detection and Response (NDR) in the Stellar Cyber Platform 
 (06m:45s)  ..........................................................................................................................................................................................  57 
 L16  -  OPTIMIZING  NETWORK  TRAFFIC  INGESTION  .............................................................................................  59 
 L16A-PRES:  Optimizing  Network  Traffic  Ingestion  (04m:30s)  .............................................................  59 
 L17  -  EXAMPLE  OF  OPTIMIZING  NETWORK  TRAFFIC  INGESTION  ............................................................  61 
 L17A-PRES:  Example  of  Optimizing  Network  Traffic  Ingestion  (09m:08s)  ................................  61 
 L17B-DEMO:  Example  of  Optimizing  Network  Traffic  Ingestion  (27m:07s)  .............................  63 
 L18  -  INTRUSION  DETECTION  SYSTEM  (IDS)  CONFIGURATION  ................................................................  69 
 L18A-PRES:  Intrusion  Detection  System  (IDS)  Conﬁguration  (07m:53s)  ....................................  69 
 L19  -  IDS  IN  THE  STELLAR  CYBER  PLATFORM  ...........................................................................................................  71 
 L19A-PRES:  IDS  in  the  Stellar  Cyber  Platform  (07m:05s)  ..........................................................................  71 
 L19B-DEMO:  IDS  in  the  Stellar  Cyber  Platform  (33m:35s)  .......................................................................  72 
 L20  -  MALWARE  SANDBOX  ........................................................................................................................................................  79 
 L20A-PRES:  Malware  Sandbox  Details  and  Conﬁguration  (06m:32s)  .........................................  79 
 L21  -  MALWARE  VISIBILITY  IN  THE  STELLAR  CYBER  PLATFORM  ..............................................................  81 
 L21A-PRES:  Malware  Visibility  in  the  Stellar  Cyber  Platform  (06m:33s)  ......................................  81 
 L21B-DEMO:  Malware  Visibility  in  the  Stellar  Cyber  Platform  (24m:12s)  ....................................  82 
 L22  -  MODULAR  SENSOR  Aggregator  ............................................................................................................................  85 
 L22A-PRES:  Modular  Sensor  Aggregator  (09m:32s)  ..................................................................................  85 
 L22B-DEMO:  Modular  Sensor  Aggregator  (07m:51s)  .................................................................................  87 
 L23  -  MODULAR  SENSOR  TENABLE  NESSUS  SCANNER  ..................................................................................  89 
 L23A-PRES:  Modular  Sensor  Tenable  Nessus  Scanner  (15m:27s)  ...................................................  89 
 L23B-DEMO:  Modular  Sensor  Tenable  Nessus  Scanner  (12m:47s)  .................................................  92 
 L24  -  MODULAR  SENSOR  PLATFORM  Connector  WITH  TENABLE  .........................................................  95 
 L24A-PRES:  Modular  Sensor  Platform  Connector  with  Tenable  (30m:26s)  ............................  95 
 L24B-DEMO:  Stellar  Cyber  Platform  Connectors  Example  with  Tenable.io  (17m:45s)  ..  101 
 L25  -  MODULAR  SENSOR  ACTIVE  DIRECTORY  (AD)  Connector  ............................................................  105 
 L25A-PRES:  Modular  Sensor  Active  Directory  (AD)  Connector  (13m:22s)  .............................  105 
 L26  -  AD  Connector  COLLECTION  OF  ASSET  &  USER  DETAILS  ...............................................................  108 
 L26A-PRES:  AD  Connector  Collection  of  Asset  &  User  Details  (09m:19s)  ..............................  108 
 L27  -  AD  Connector  RESPONSE  ACTIONS  TO  DISABLE  A  USER  ..............................................................  110 
 L27A-PRES:  AD  Connector  Response  Actions  to  Disable  a  User  (17m:42s)  ..........................  110 
 L27B-DEMO:  AD  Connector  Response  Actions  to  Disable  a  User  (20m:05s)  ......................  114 
 L28  -  MODULAR  SENSOR  BUFFERING  ...........................................................................................................................  118 
 ADM-03-01-224  2 


---

<!-- Página 3 -->

 L28A-PRES:  Modular  Sensor  Buffering  (04m:22s)  .......................................................................................  118 
 L29  -  MODULAR  SENSOR  LESSONS  SUMMARY  .....................................................................................................  119 
 L29A-PRES:  Modular  Sensor  Lessons  Summary  (02m:48s)  ................................................................  119 
 L00 - INTRODUCTION AND AGENDA 
 L00A-PRES: Modular Sensor Module Lessons Agenda (08m:52s) 
 00:00-01:00 
 Hi everyone. Welcome to the  Modular Sensor Concepts  and Conﬁguration  module. I'm Paul 
 Levasseur of the Stellar Cyber Enablement and Training teams. The lessons in this module 
 cover concepts, conﬁguration, examples, and demonstrations of how the Modular Sensor 
 and its features are used in the Stellar Cyber Open XDR architecture. Throughout this 
 module there'll be lots of new concepts and terms that you may not be familiar with. This is 
 deﬁnitely okay and expected. You may have even noticed I've said something similar to this 
 before in other modules. As you progress through the Stellar Cyber Open XDR training 
 curriculum, with repetition, iteration, and examples, you'll be able to understand and apply 
 what you have learned in becoming a cybersecurity superstar. Thank you. 
 Welcome to the  Stellar Cyber Modular Sensor Concepts  and Conﬁguration  module. Here is 
 an agenda of the lessons available in this module. 
 01:00-02:00 
 In the  Stellar Cyber Modular Sensors Concepts and  Conﬁguration  module, the following 
 lessons are covered. 
 Modular Sensors Introduction  . This lesson explains  how Modular Sensors are deployed 
 within the Stellar Cyber Open XDR architecture as well as the types of Modular Sensors 
 deployed as hardware or virtual appliances. 
 Essential Terminology  . This lesson gives deﬁnitions  of the key terms used within the Modular 
 Sensor Concepts and Conﬁguration training module. 
 Collecting Network Traffic  . This lesson explains the ﬂows of network traffic and how 
 Modular Sensors obtain network traffic from switch SPAN ports and TAP devices. 
 ADM-03-01-224  3 


---

<!-- Página 4 -->

 Functionality Overview  . This lesson provides an overview of each of the core features that 
 will be explained in detail throughout the  Modular  Sensors Concepts and Conﬁguration 
 training module. This will help you see the big picture of how the features work as a whole 
 before diving into each individual feature. 
 02:00-03:00 
 Stellar Cyber Platform Data Processing Overview  . This  lesson gives an overview from the 
 perspective of the Stellar Cyber Open XDR platform on how it processes the data received 
 from the Modular Sensors. 
 Modular Sensor Conﬁguration with Modular Sensor Proﬁles  .  This lesson explains the 
 concepts and tasks needed to conﬁgure Modular Sensor proﬁles used to conﬁgure Modular 
 Sensors. 
 Modular Sensor Speciﬁc Conﬁguration  . This lesson  goes through the parameters that are 
 conﬁgured on individual Modular Sensors. 
 Parsers for Normalization into Interﬂow  . This lesson  provides details for how parsers are 
 used on Modular Sensors to Normalize metadata and telemetry into Interﬂow records in 
 JSON format. 
 Log Forwarder and Log Filter Conﬁguration  . This lesson  explains the process and 
 conﬁguration steps to ingest logs from third-party security, identity, and interest structure 
 systems and tools as well as how to optimize ingestion by ﬁltering logs that are not 
 essential for security operations. 
 03:00-04:00 
 Log Forwarder Example  . This lesson uses a pfSense  ﬁrewall as an example to describe the 
 higher end-to-end process of conﬁguring log forwarding for the Modular Sensor to ingest 
 pfSense ﬁrewall logs in order to parse and Normalize into Interﬂow records and send to the 
 Stellar Cyber Open XDR platform. 
 Log Source Conﬁguration for Single TCP / UDP Port  .  This lesson shows how to conﬁgure the 
 Stellar Cyber platform to enable the Modular Sensor to receive logs from systems using a 
 single port such as the default syslog port 514. 
 Validate Log Forwarder  . This lesson provides the steps to validate the parsed and 
 Normalized logs are being enlisted by the Modular Sensor as Interﬂow records in the Stellar 
 Cyber Open XDR platform. 
 ADM-03-01-224  4 


---

<!-- Página 5 -->

 04:00-05:00 
 Log Forwarder Preserving Raw Logs  . This lesson shows how to conﬁgure Modular Sensors 
 to include the original raw log message in the Interﬂow record that is sent to the Stellar 
 Cyber Open XDR platform. 
 Network Traffic Analysis Details and Conﬁguration  .  This lesson explains how to conﬁgure 
 Modular Sensors to collect network traffic off SPAN ports or TAP devices and provides 
 details of how the Modular Sensor analyzes network traffic to create sessions and 
 metadata and forward it as Interﬂow records to the Stellar Cyber Open XDR platform. 
 Network Detection and Response (NDR) in the Stellar Cyber Platform.  This lesson explains 
 some key concepts of how data collected from Modular Sensors in the Stellar Cyber 
 platform is analyzed and utilized. 
 Optimizing Network Traffic Ingestion  . This lesson  provides explanations and conﬁguration 
 examples to optimize ingestion of network traffic by excluding network applications and 
 services that are not essential to ingest on the Stellar Cyber platform. 
 05:00-06:00 
 Example for Optimizing Network Traffic Ingestion  .  This lesson gives an end-to-end example 
 of conﬁguring traffic ﬁlters to exclude Modular Sensor conﬁguration management and 
 ingestion communication to the Stellar Cyber Open XDR platform from being ingested by 
 the platform. 
 Intrusion Detection System (IDS) Details and Conﬁguration  .  This lesson provides the 
 explanation and conﬁguration of the IDS module on Stellar Cyber Modular Sensor. 
 Intrusion Detection System (IDS) Stellar Cyber Platform Operations  . This lesson explains how 
 to view the IDS event data received from Modular Sensors and how the Stellar Cyber Open 
 XDR platform uses machine learning to create actionable Alerts from the IDS events events. 
 Malware Sandbox Details and Conﬁguration  . This lesson  provides the concepts and details 
 on how to conﬁgure the malware sandbox functionality on a Modular Sensor. 
 06:00-07:00 
 Malware Visibility in the Stellar Cyber Platform  . This lesson explains how to view details 
 about ﬁles collected and analyzed by the malware sandbox module in the Stellar Cyber 
 Open XDR platform. 
 ADM-03-01-224  5 


---

<!-- Página 6 -->

 Aggregator Details and Conﬁguration  . This lesson explains the concepts and conﬁguration 
 of Modular Sensors to be an Aggregator as well as how to conﬁgure other Stellar Cyber 
 sensors to use the Modular Sensor as an Aggregator. 
 Tenable Nessus Scanner Details and Conﬁguration  .  This lesson provides the concepts and 
 conﬁguration of how to enable the ability to initiate scans from the Tenable cloud website to 
 run all the Nessus vulnerability scanner module that can be enabled on Modular Sensors. 
 Stellar Cyber Platform Connectors Example with Tenable.io Cloud  . This lesson explains how 
 to conﬁgure a Tenable.io Connector on the Stellar Cyber platform to collect scan data and 
 reports as well as collect assets learned by the Tenable.io vulnerability scan. 
 07:00-08:00 
 Active Directory Connector Details and Conﬁguration.  This lesson provides details and 
 explanations how to conﬁgure an Active Directory Connector on Modular Sensors to collect 
 Windows event logs, user behavior and computer asset information, as well as perform 
 response actions from the Stellar Cyber platform to disable users in Active Directory. 
 Active Directory Connector Collection of Asset and User Details  . This lesson shows how to 
 view the asset and user behavior information collected by the Active Directory Connector in 
 the Stellar Cyber Open XDR platform. 
 Modular Sensor Active Directory Connector Response Actions to Disable a User  . This lesson 
 provides details on the many ways users can be disabled from the Stellar Cyber platform in 
 Active Directory to help mitigate threats. 
 08:00-09:00 
 Buffering  . This lesson provides a summary of the buffering  capabilities of the Modular 
 Sensors that are used in an event where connectivity is temporarily lost between a Modular 
 Sensor and the Stellar Cyber Open XDR platform, and how data is trickled back once the 
 connection is restored. 
 Modular Sensor Summary  . This lesson provides a brief  summary of Modular Sensors within 
 the Stellar Cyber Open XDR architecture and ends the  Stellar Cyber Modular Sensor 
 Concepts and Conﬁguration  module. 
 The lessons in this module provide explanations and conﬁguration for Modular Sensors and 
 the features that will enable you to take advantage of the capabilities the Stellar Cyber 
 Open XDR platform has to offer for security operations. Happy learning. 
 ADM-03-01-224  6 


---

<!-- Página 7 -->

 This lesson is complete. Thank you for watching. 
 L01 - MODULAR SENSORS INTRODUCTION 
 L01A-PRES: Modular Sensors Introduction (06m:49s) 
 00:00-01:00 
 The  Stellar Cyber Modular Sensor Concepts and Conﬁguration  module we'll start with the 
 lesson,  Modular Sensors Introduction  . This lesson,  Modular Sensors Introduction,  explains 
 how Modular Sensors are deployed within the Stellar Cyber Open XDR architecture, as well 
 as the types of Modular Sensors deployed as hardware or virtual appliances. 
 The focus of the next set of lessons will be on the Stellar Cyber Modular Sensors. Looking at 
 the Modular Sensors in the big picture, which is the big picture of the Stellar Cyber Open 
 XDR architecture, on the left-hand side I see the Stellar Cyber Modular Sensor and how it ﬁts 
 in within an organization. 
 01:00-02:00 
 We will cover in this set of lessons the Modular Sensor features including log forwarding, 
 network traffic analysis, IDS, Malware Sandbox, Aggregator, Tenable Nessus scanning 
 capabilities, Connectors, and how the sensors can buffer. I'll also describe in more detail how 
 the logs are sent to the Stellar Cyber Modular Sensors so that they can Normalize all the 
 data and send them to the Stellar Cyber platform. As well as how the Stellar Cyber Modular 
 Sensor can connect to Active Directory or ﬁrewalls or vulnerability scanners to grab data, 
 but also to perform response actions. Modular Sensors as virtual appliances can be installed 
 on VMware ESXi, AWS, Microsoft Azure, Google Cloud Platform, or GCP, HyperV, KVM, and 
 Oracle Cloud infrastructure, or OCI. 
 02:00-03:00 
 Stellar Cyber Modular Sensors also come as hardware appliances. The Photon-160 can 
 support up to 500 megabits per second and has 6-gigabit interfaces. The Photon-250 can 
 support up to one gigabit per second and has many different interface options, essentially 
 6-gigabit interfaces, and two more gigabit-pluggable interfaces that you can choose the 
 type of Connectors on them. The Photon-400 supports up to 10-gigabits per second. It has 
 6-gigabit RJ45 connections and two 10-gigabit SFP connections. So now for the big 
 question, where are Modular Sensors deployed? 
 03:00-04:00 
 Well, if your organization has one site, then you would have a Modular Sensor for that site, 
 or you may have multiple depending on you know how many security tools and how much 
 ADM-03-01-224  7 


---

<!-- Página 8 -->

 data you are trying to collect. A Modular Sensor again has different speeds. You can have 
 10-gig Modular Sensors, 1-gig Modular Sensors, and even smaller than that. The goal here is 
 if you need to collect or analyze traffic that's over a gig throughout your network, then you 
 can either install a larger Modular Sensor, or you can install multiple Modular Sensors. Each 
 Modular Sensor could be for different networks, for example. Maybe some of the VLANs in 
 the organization get spanned off to the Modular Sensor for analysis and for IDS detections, 
 or you have lots of different security tools. 
 04:00-05:00 
 Maybe you want to determine or break up the load with some security tools going to one 
 Modular Sensor and some going to another. It's all about speeds and feeds. Again, you 
 could have a Modular Sensor as an Aggregator and other Modular Sensors grabbing or 
 collecting data from other networks and then forwarding to that single Modular Sensor then 
 to send to the Stellar Cyber platform. It all depends on what you are trying to collect. But in 
 general, you have at lEast one Modular Sensor per site. The site could be a data center. The 
 site could be in a cloud environment if you are using virtual hosted servers and machines 
 and security tools. But in this picture, as an example, there are multiple sites and I have one 
 Modular Sensor at each site. 
 05:00-06:00 
 I might also have Windows Server sensors and Linux Server sensors at each site as well, 
 depending on what type of servers I have at each site. Each of these sites could be a 
 separate customer. If you are an MSSP, you would give a customer the Modular Sensor, or if 
 you're managing it for them, you would install a Modular Sensor for them at each site to 
 collect data. At that point, each of these Modular Sensors would be associated with its own 
 tenant for that speciﬁc customer. The Modular Sensors again at each site collect network 
 traffic. They collect logs. They have Connectors to connect to local security tools, and they 
 Normalize all that data into Interﬂow records, which are then sent to the Stellar Cyber 
 platform, either over the internet 
 06:00-06:50 
 depending on the type of Stellar Cyber Open XDR platform deployment, or through your 
 local network. Alright. Well, that's how Modular Sensors get deployed. The deployment 
 options are very ﬂexible and it's really up to your organizational needs to determine how 
 many you need based on the type of sensors that we have. The lessons in this module go 
 through the concepts and conﬁguration of the core components and features of Modular 
 Sensors. We have other lessons as well that go through the installation, including how to 
 conﬁgure the Modular Sensors in cloud environments to get them up and running. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  8 


---

<!-- Página 9 -->

 L02 - ESSENTIAL TERMINOLOGY 
 L02A-PRES: Essential Terminology (12m:58s) 
 00:00-01:00 
 The next lesson is  Essential Terminology  . This lesson,  Essential Terminology,  gives deﬁnitions 
 of the key terms used within the  Modular Sensor Concepts  and Conﬁguration  training 
 module. 
 Throughout these lessons on Modular Sensors, there's some terminology that will keep on 
 coming up. I want to make sure I cover it ahead of time. For example, I'll be talking about 
 telemetry. Telemetry is collected by Modular Sensors to create Interﬂow records. Telemetry 
 refers to the data collected about the behavior and actions within a network system. This 
 includes detailed records of events such as system logs, data collected via API Connectors 
 from security, identity and infrastructure systems, and user-activity logs. 
 01:00-02:00 
 Telemetry data is rich and comprehensive, providing a real-time or near-real-time stream of 
 information that can be analyzed to detect anomalies, track system performance, and 
 identify potential security threats or breaches. Collecting telemetry data allows security 
 analysts to conduct in-depth investigations and respond to incidents with a high degree of 
 precision. Here's a cool note for you. The roots of the word telemetry come from tele, which 
 is remote or distant, plus metria, which is the act of measuring. It literally means collecting 
 measurements about things from a distance. Metadata is another big term we'll be using a 
 lot. Metadata is created by Modular Sensors when creating Interﬂow records. Metadata is 
 data about data. 
 02:00-03:00 
 Metadata provides contextual information about other data being analyzed or stored, 
 including information about ﬁles, such as creation date, ﬁle size and type, network traffic 
 source and destination IP addresses, port numbers, protocol used bytes transmitted and 
 received, TCP connection status, and user activities including log in times, and resource 
 access logs. While metadata does not contain the content of the data itself, which is also 
 great for security reasons, collecting metadata is invaluable for security analysis because it 
 can help in identifying patterns, trends, and anomalies without the need to process the 
 entire content of the data streams. Telemetry and metadata are crucial for cybersecurity, 
 but they serve different roles. 
 ADM-03-01-224  9 


---

<!-- Página 10 -->

 03:00-04:00 
 Telemetry provides a granular view of events and behaviors within systems and networks, 
 enabling detailed analysis and response. Metadata offers contextual insights about data, 
 which can aid in analysis, organization, and sometimes preserving privacy while still 
 monitoring the security threats. Interﬂow records created by Stellar Cyber consist of both 
 telemetry and metadata from security, identity, and infrastructure systems. Let's test your 
 knowledge a little bit with the deﬁnitions I just provided. Modular Sensors create Interﬂow 
 records from telemetry and metadata. Which of the following is telemetry or metadata? 
 Data gathered through API Connectors from security, identity, and infrastructure systems. 
 04:00-05:00 
 You got it right, telemetry. Well, hopefully you got it right. Next, a network session summary 
 learned from network packets containing the source IP, destination IP protocol, source port 
 and destination port, bytes received and transmitted, and the TCP state which are all 
 Normalized into Interﬂow records. You guessed it, metadata. Some other important terms 
 are events. An event refers to a speciﬁc occurrence or incident that is being monitored or 
 analyzed within the Stellar Cyber platform. It can include various types of activities such as 
 security Alerts, system events, or network events. The term “event,” is often used to describe 
 non-Alert related Interﬂow records. 
 05:00-06:00 
 I'll describe what Alerts are coming up soon. Raw event in the context of Stellar Cyber, a raw 
 event refers to the original unprocessed log or data entry that is captured by the sensor. It 
 contains the raw information about a security event or activity, such as network traffic, 
 system logs, or user actions. Raw events are typically collected and stored for further 
 analysis and investigation by the Stellar Cyber platform. Now for Alerts. Alerts are a critical 
 component of Stellar Cyber's ability to discover important events in a sea of data. Using 
 machine learning, or ML, techniques, statistical analysis, heuristic rules, and automated 
 threat hunting playbooks, Stellar Cyber examines raw event data for evidence of potential 
 threats from anomalies or security violations. When threats are detected, Stellar Cyber 
 generates Alerts that are entered into the Alerts index and reported in the Stellar Cyber user 
 interface. 
 06:00-07:00 
 Later on I'll also cover what an index is. Alerts help drive the action in the home dashboard. 
 The Alert Types page and the Case interface. There are many different types of Alerts 
 available in Stellar Cyber, organized by XDR Kill Chain stage, tactic, and technique with each 
 focused on a speciﬁc type of security threat. Looking at the Stellar Cyber platform UI, 
 there's an Alerts page. On the Alerts page you can see there are many different types of 
 Alerts including uncommon application anomaly, external plain text password detected, 
 ADM-03-01-224  10 


---

<!-- Página 11 -->

 etcetera. Throughout the platform, you'll see the word JSON or J-S-O-N, which is JavaScript 
 object notation. 
 07:00-08:00 
 JSON is a format for structuring data as text in a way that's both easy for humans to read 
 and write and machines to parse and generate. Looking at the right-hand side, you can get 
 an idea of what JSON looks like. With JSON format, objects are collected in key value pairs 
 and closed by curly braces. If we look at the bottom, we see an example of the curly braces. 
 You'll see pfSense ﬁrewall or pfSense_FW:, and then a brace and then there are key value 
 pairs there. Data_length, and the value is 76. We have a key of ﬂags and the value of none, 
 key ID, which is a value of 11800. A key is IP version and a value is four. Arrays are ordered 
 lists of values enclosed by square brackets. 
 08:00-09:00 
 Most of my arrays you'll see are just values of one entry. I have detected_ﬁelds, which has 
 an array of source IP_host. Keys are always strings written in double quotes, and values can 
 be strings, numbers, true/ false, null, an object or an array also written in double quotes. 
 You'll be seeing a lot of JSON-formatted objects within the Stellar Cyber platform. One of 
 the most important concepts we'll be talking about within this set of lessons is the Interﬂow 
 record. In Stellar Cyber, an Interﬂow record refers to telemetry and metadata collected by 
 Stellar Cyber that is Enriched and Normalized into JSON format by Stellar Cyber to facilitate 
 analysis, correlation, and storage of telemetry and metadata from various sources. 
 09:00-10:00 
 By standardizing the format of all records, Interﬂow enables more efficient and effective 
 security and analytics, threat detection, and response activities as data from diverse 
 sources can be easily aggregated, correlated, and analyzed to identify and mitigate 
 security risks. If you take a look at the right, the data that comes into the Stellar Cyber 
 platform after being Normalized into JSON format has the key and value pairs, for example, 
 action is the key. The value is block. In other words, this was a ﬁrewall rule from a ﬁrewall 
 that took a look at the set of rules and blocked it based on a policy. Here we can see the 
 source IP host, which is 192 with state 1.102 as an array. 
 10:00-11:00 
 If you look at the bottom you'll see that it was Enriched as well. The desktop_geo are the 
 Enriched portion of the Interﬂow record that the log source would be gathered. The 
 information that you see in the JSON Interﬂow record doesn't come with a destination IP 
 geolocation for example, but the record gets Enriched by Stellar Cyber, where we add the 
 geolocation. We add many other ﬁelds as well. Interﬂow records in the UI are also called 
 documents. If you look at the right-hand side in the Stellar Cyber platform user interface, 
 ADM-03-01-224  11 


---

<!-- Página 12 -->

 you will see the word Documents. When you see that, realize this really is a list of Interﬂow 
 records. The Interﬂow records may be events or Alerts. 
 11:00-12:00 
 Another hugely important concept is a Case. We have lots of different modules talking 
 about Cases, but here, just so that we're on the same page, a Case is a set of multiple 
 correlated Alerts and entities, constituting a potential uniﬁed security attack, ranked by 
 dynamically updating score, indicating the severity of the attack. In other words, as more 
 Alerts are correlated into the Case, the risk score raises, therefore the Case score raises. 
 Stellar Cyber uses its machine-learning capabilities to generate Cases automatically, 
 grouping related Alerts into a uniﬁed Case for improved attack resolution. You can also 
 manually create Cases from a set of Alerts as well. Another term we just used in the 
 explanation of the Case is an entity. 
 12:00-13:00 
 An entity refers to an asset or user within an organization that is being monitored for 
 security purposes. Entities can include servers, routers, host systems, and individuals. Entities 
 are automatically registered in Stellar Cyber by sensors and can be de-authorized or 
 ignored if needed. Artifact, we don't use this that much within our lessons or within the 
 platform, but it's an important word to know. An artifact generally refers to any piece of 
 digital data or evidence that is created during the occurrence of a security event or incident. 
 Artifacts could be generated by both malicious activities, such as malware infections and 
 hacking attempts, and legitimate operations such as system updates and user activities. 
 This lesson is complete. Thank you for watching. 
 L03 - COLLECTING NETWORK TRAFFIC 
 L03A-PRES: Collecting Network Traffic (08m:48s) 
 00:00-01:00 
 The next lesson is  Collecting Network Traffic  . This  lesson,  Collecting Network Traffic  , 
 explains the ﬂows of network traffic and how Modular Sensors obtain network traffic from 
 switch SPAN ports and TAP devices. 
 In this lesson, I will go through how Modular Sensors collect network traffic and discuss 
 network traffic ﬂows. Modular Sensors collect network traffic traversing a network via SPAN 
 ports on switches or by connecting to TAP devices. On the upper right-hand side I have a 
 compass that basically shows that the internet is towards the North. I have servers towards 
 the East. I have clients towards the West and clients are essentially South as well. 
 ADM-03-01-224  12 


---

<!-- Página 13 -->

 01:00-02:00 
 The way we describe network traffic communication is we have North/ South 
 communication, which is also called vertical communication. North/ South communication is 
 to and from clients and servers that are accessing the internet as that dotted line shows. 
 East/West, or lateral communication, is traffic among clients and servers or even 
 client-to-client or server-to-server. Essentially it's when traffic is not traversing the network 
 to reach the internet. Switch port analyzer or SPAN ports on switches are conﬁgured to 
 replicate and mirror traffic from speciﬁc switch ports or VLANs to devices connected to the 
 SPAN port. 
 02:00-03:00 
 Stellar Cyber Modular Sensors receive network traffic from switch SPAN ports for analysis. 
 They perform deep packet inspection, which is called DPI, to identify applications and run 
 IDS signatures to detect threats and look for malware. They also forward network telemetry 
 metadata as Interﬂow to the Stellar Cyber platform. Looking at this picture, I have the 
 Modular Sensor connected to the switch's SPAN port. The Ethernet zero interface is the 
 interface that is for management. It has an IP address. I can access it via SSH, and that's the 
 interface that also communicates with the Stellar Cyber platform. When communication 
 happens, for example, North/ South communication or vertical communication. 
 03:00-04:00 
 The SPAN port replicates that data and sends it to the Stellar Cyber Modular Sensor. 
 Likewise, for East/West communication or lateral communication, the Stellar Cyber Modular 
 Sensor also receives that traffic from the SPAN port as well. Here I'll go through how SPAN 
 or mirror ports are conﬁgured on switches or give you an idea of how they're conﬁgured on 
 switches. Looking at the switch on top, I have port 1/1, which means module one on the 
 switch port one on the switch. That's connected to the Stellar Cyber Modular Sensor on 
 Ethernet zero, which is the management interface. 
 04:00-05:00 
 The management interface has an IP. That's what is used to communicate with this Stellar 
 Cyber platform.I can also access the management IP locally on the network via SSH. 
 Ethernet one on the Modular Sensor is connected to the switch port 1/2. That will be 
 conﬁgured as a SPAN port. I'll talk more about that. Looking at the bottom-left switch, that's 
 connected to port 2/12 of the switch on top, that's module two port twelve. On the right, on 
 the switch on the right is connected to module two, port twenty ﬁve, so 2/25. Now looking at 
 the conﬁguration on the right, I can essentially say, look for any traffic coming in on port 
 2/12 or 2/25, and look at the traffic bidirectionally. 
 ADM-03-01-224  13 


---

<!-- Página 14 -->

 05:00-06:00 
 In other words, it could be coming into the port from the bottom or coming out of the port 
 from the top. In this case I'm saying the destination SPAN port is 1/2. If I see any traffic going 
 in or out of port 2/12, send it to the SPAN port, which will then make it to the Modular Sensor. 
 Or if I see traffic coming in or out of port 2/25, send it to the SPAN port, which will then send 
 it to the Modular Sensor. Here's an example: I have a client on the bottom left 
 communicating with the internet, that's going into port 2/12. That gets mirrored essentially, 
 to the SPAN port, which then makes it to the Stellar Cyber Modular Sensor. 
 06:00-07:00 
 Likewise, I have traffic coming in 2/12 from the client on the left going to a server on the 
 right. In both cases I have traffic coming in 2/12 but I also have it going out of 2/25. And 
 then the reply traffic comes in 2/25. It's essentially bidirectional. In either case, the mirror 
 port will send it to the Stellar Cyber Modular Sensor, but the Modular Sensor knows to only 
 keep track of essentially one ﬂow. A network TAP device is a device that goes in between 
 switches. Essentially it's a break in the cable. This way I don't have to conﬁgure traffic on a 
 switch itself. These devices are usually made so that they will fail open. In other words if that 
 device were to die for any reason it will still maintain connectivity. But like a SPAN port, it will 
 mirror the traffic. 
 07:00-07:50 
 Traffic coming in from the North/ South communication or in this case really it's South/ 
 North communication, it'll get mirrored and sent to the Stellar Cyber Modular Sensor. 
 Likewise traffic going East/West or lateral will also get mirrored or copied to the Stellar 
 Cyber Modular Sensor. TAPs can connect to switch access ports or trunk ports. TAPs may be 
 conﬁgured to forward network traffic to Modular Sensors. 
 This lesson is complete. Thank you for watching. 
 L04 - FUNCTIONALITY OVERVIEW 
 L04A-PRES: Functionality Overview (06m:15s) 
 00:00-01:00 
 The next lesson is  Functionality Overview  . This lesson,  Functionality Overview,  provides an 
 overview of each of the core features that will be explained in detail throughout the  Modular 
 Sensors Concepts and Conﬁguration  training module.  This will help you see the big picture 
 of how the features work as a whole before diving into each individual feature. 
 ADM-03-01-224  14 


---

<!-- Página 15 -->

 Hi. In this lesson I will cover Stellar Cyber Modular Sensor functions. We've covered the 
 Stellar Cyber Modular Sensor functions in the big picture as an overview, but we're going to 
 be diving deep into each of these functions and how to conﬁgure them. I want to make sure 
 we do a quick recap so it's fresh in your mind. On the left-hand side is the Stellar Cyber 
 Modular Sensor. That talks to the Stellar Cyber Open XDR platform. 
 01:00-02:00 
 The Stellar Cyber Modular Sensors are deployed within organizations off of network 
 switches or they can be deployed in the cloud, such as in AWS, Microsoft Azure, GCP or 
 Google Cloud Platform, OCI for Oracle Cloud infrastructure, and so forth. The very ﬁrst 
 function we'll talk about is the log forwarder. Modular Sensors collect parts and Normalize 
 logs sent from security and infrastructure tools and systems into Interﬂow records in JSON 
 format and forward to the Stellar Cyber platform. Modular Sensors have hundreds of 
 built-in parsers, which we'll talk about, that interpret and Normalize logs into Interﬂow 
 records. Logs that are not relevant for threat investigation can be ﬁltered at the Modular 
 Sensor to optimize the amount of data that is ingested on the Stellar Cyber platform. That is 
 very important. We'll go through some examples of how to conﬁgure all of this. 
 02:00-03:00 
 Next, I'll talk about network traffic analysis. The Modular Sensors are deployed within an 
 organization off of switches and usually off a SPAN port or TAP device. Being off a SPAN or 
 TAP device, the Modular Sensors will receive network traffic. Modular Sensors capture 
 network traffic and create metadata summaries that are Normalized into interval records in 
 JSON format, and are forwarded to the Stellar Cyber platform. Modular Sensors identify 
 network traffic ﬂows and applications in network traffic using deep packet inspection. That 
 is Normalized into Interﬂow records in JSON format and forwarded to the Stellar Cyber 
 platform. The Stellar Cyber Modular Sensor also has an IDS engine. Modular Sensors apply 
 IDS rules to network packets to identify threats and create metadata summaries that are 
 Normalized into Interﬂow records in JSON format and are forwarded to the Stellar Cyber 
 platform. 
 03:00-04:00 
 Stellar Cyber Modular Sensors also have a malware sandbox that can be conﬁgured to 
 identify malware and unencrypted ﬁles and create metadata summaries that are 
 Normalized into Interﬂow records in JSON format and forward to the Stellar Cyber platform. 
 I hope that's becoming a very familiar case for you. Notice that all of it on the sensors gets 
 Normalized into Interﬂow records in JSON format and forwarded to the Stellar Cyber 
 platform as one of the key functions of the Modular Sensor. The Modular Sensor can also be 
 an Aggregator. Modular Sensors can be conﬁgured as an Aggregator for the traffic from 
 ADM-03-01-224  15 


---

<!-- Página 16 -->

 other Modular Sensors, Windows Server sensors, and Linux Server sensors within an 
 organization. 
 04:00-05:00 
 When sensors are conﬁgured to use a Modular Sensor conﬁgured as an Aggregator, 
 communication from sensors with the Stellar Cyber platform is from the Aggregator instead 
 of each individual sensor. Stellar Cyber Modular Sensors can also run a Tenable Nessus 
 scanner. With a license from Tenable.io, a security scan can be initiated to run on a Modular 
 Sensor to scan the network for vulnerabilities. We'll go into lots of detail on that as well. 
 Along with performing vulnerability scans, a Tenable.io Connector can be conﬁgured to 
 collect telemetry from Tenable that is Normalized into Interﬂow records. This is really cool 
 and I will show all of that later on in these lessons. Next are Connectors. 
 05:00-06:15 
 The Modular Sensor can obtain telemetry data from infrastructure identity and security 
 systems and tools via Connectors using APIs that Normalize it into Interﬂow records in JSON 
 format and then forward them to the Stellar Cyber platform. Using Connectors on Modular 
 Sensors enables the ability to trigger response actions as well to infrastructure identity and 
 security tools from the Stellar Cyber platform. This can be done via automated rules or 
 manual action Another cool thing about the Stellar Cyber Modular Sensors is the fact that it 
 can buffer Interﬂow records. If there is a connection issue to the Stellar Cyber platform 
 preventing the Modular Sensor from forwarding Interﬂow records, Modular Sensors can 
 temporarily hold the buffered Interﬂow records until the connection is resumed to prevent 
 loss of data. It will then trickle the data back so that it doesn't overwhelm the connection 
 once the connection is re-established. That's the end of the functionality overview. Thank 
 you. 
 This lesson is complete. Thank you for watching. 
 L05 - DATA PROCESSING 
 L05A-PRES: Data Processing (04m:49s) 
 00:00-01:00 
 The next lesson is  Stellar Cyber Platform Data Processing Overview.  This lesson,  Stellar 
 Cyber Platform Data Processing Overview,  gives an  overview from the perspective of the 
 Stellar Cyber Open XDR platform on how it processes the data received from the Modular 
 Sensors. 
 ADM-03-01-224  16 


---

<!-- Página 17 -->

 In this lesson, I'll give a brief overview of how the Stellar Cyber Open XDR platform receives 
 Interﬂow records from Modular Sensors, then processes and categorizes Interﬂow records 
 into indices. That's so the data can be quickly searched based on its category, for example, 
 traffic goes into the traffic indices. Syslogs go into Syslog indices. All Alerts that are 
 generated by the platform go into the Alerts indices. 
 01:00-02:00 
 Scans by a Tenable Nessus scanner go into the scan indices. Again, by having the indices, I 
 can quickly search through the different categories of data that's been collected by the 
 Stellar Cyber platform. The Stellar Cyber platform then Enriches Interﬂow records with ﬁelds 
 such as threat intel that has the IP reputation. Is it good? Is it malicious? Is it a brute forcer? 
 Is it a scanner? This is good information to have included in the Interﬂow records that were 
 received by the Stellar Cyber Modular Sensors. The Modular Sensors don't add that 
 information, but once received by the Stellar Cyber platform, this information gets Enriched 
 into the Interﬂow records. The other information that's important is the geolocation. Where 
 was that source? Where is the destination IP? 
 02:00-03:00 
 The Interﬂow records can be also Enriched with the DNS host names. The data source So 
 where did the Interﬂow record come from? What was the source of the data? Was it a 
 ﬁrewall? Was it a Windows Server or Linux Server or was it from the network traffic? Also, 
 the user identity could be added to Interﬂow records as well. What was the username? That 
 information can be learned from Active Directory as an example. You will see this later on as 
 we go through more examples showing you real records and the Enrichment that occurs. 
 The Stellar Cyber platform then stores categorized and Enriched Interﬂow records into the 
 Data Lake. Something that we will repeat over and over again: 
 03:00-04:00 
 The Stellar Cyber platform uses machine learning or ML statistical analysis rules, heuristic 
 rules, and custom ATH playbooks to identify threats and create Alerts. This Stellar Cyber 
 platform correlates Alerts from all data sources using graph machine learning to create 
 Cases. The Stellar Cyber platform provides a streamlined UI and API to enable effective 
 searches and analysis of all data. It also enables containment of threats using automated 
 and analyst-driven response actions using Connectors that integrate with hundreds of 
 security identity and infrastructure tools using APIs. On the Stellar Cyber platform, Interﬂow 
 records sent from the Modular Sensor are viewable and searchable for threat investigation. 
 04:00-04:50 
 Interﬂow are also used by the Stellar Cyber platform with machine learning and rules 
 engines to identify threats and anomalies to create Alerts. On the Stellar Cyber platform, 
 ADM-03-01-224  17 


---

<!-- Página 18 -->

 Interﬂow records collected from Modular Sensors are among the Alerts used by Graph ML 
 to correlate and create Cases. There are many more features of the Stellar Cyber platform, 
 but I wanted to give a brief overview of some of the features before diving in deep into 
 each of the Modular Sensor functions. Thank you for watching. 
 This lesson is complete. Thank you for watching. 
 L06 - MODULAR SENSOR PROFILES 
 L06A-PRES: Modular Sensor Proﬁles (12m:49s) 
 00:00-01:00 
 The next lesson is  Modular Sensor Conﬁguration with  Modular Sensor Proﬁles  . This lesson, 
 Modular Sensor Conﬁguration with Modular Sensor Proﬁles  ,  explains the concepts and tasks 
 needed to conﬁgure Modular Sensor proﬁles used to conﬁgure Modular Sensors. 
 Now we'll get right into it. In this lesson, I will cover how to conﬁgure Modular Sensors using 
 Modular Sensor proﬁles. As I just mentioned, Modular Sensors are conﬁgured by modifying 
 the settings of sensor proﬁles and assigning them to Modular Sensors. Modular Sensor 
 proﬁles are conﬁgured by going to  System  on the  top right, then selecting  Sensor Proﬁles  . 
 01:00-02:00 
 Once you get into  Sensor Proﬁles  , you can see a list.  By default, there are two sensor 
 proﬁles. The  Default  proﬁle is assigned by default  to Windows Server sensors, Linux Server 
 sensors, and some of the older sensors such as network sensors and security sensors. 
 Network sensors and security sensors are no longer available because all that functionality 
 rolls into a Modular Sensor so you can conﬁgure which modules you actually need. To start, 
 I will show you how to clone the default Modular Sensor proﬁle so you can change the 
 settings without modifying the existing default Modular Sensor proﬁle. After, you'll be shown 
 how to create a new Modular Sensor proﬁle as well. Check the box next to 
 Default_modular  . 
 02:00-03:00 
 Then on the right-hand side, select  Clone  . Note I'm using the word “select.” Sometimes 
 people use iPads so I was used to saying click. But now the new terminology we will say 
 “select” instead just in case someone does have a touch-screen device. Once you click 
 Clone  , or excuse me, once you select  Clone  , you can  type in a new clone name. I will call this 
 SC Modular Sensor, of course that stands for Stellar Cyber. I'll ﬁnish it off by selecting  Clone  . 
 Okay. The new Modular Sensor proﬁle appears in the list. If you select the pencil icon, next 
 ADM-03-01-224  18 


---

<!-- Página 19 -->

 to the Modular Sensor proﬁle name, on the right-hand side, you can edit the Modular Sensor 
 proﬁle. 
 03:00-04:00 
 By the way, if you want to delete and start over, you can click, excuse me, you can select 
 the trash can icon. If you want to create a new Modular Sensor proﬁle, you can select 
 Create  from the top right, then select  Add a Modular  Sensor Proﬁle  . Either way is ﬁne. 
 Modular Sensor features are enabled or disabled by conﬁguring and applying Modular 
 Sensor proﬁles to Modular Sensors. Modular Sensor proﬁle features are enabled or disabled 
 by sliding the lever to the right, which is on and it'll have a little green outline, or keeping the 
 lever off, which will be grayed out. You can select a feature heading to expand and see 
 additional options. 
 04:00-05:00 
 For example, when I selected  IDS  , now I can see that  there's networks, signature, and 
 buffering as IDS options. If I select  Sandbox  , for  example, it will close that one and open up 
 the  Sandbox  options. Note that the  Log Forwarder  feature  is always on to ingest logs and 
 cannot be turned off. Therefore, there is no lever to slide it on or off. But there are options if 
 I select the  Log Forwarder  to expand the options.  To start, I can enter a Proﬁle Name. It is 
 helpful to make the name of the proﬁle something that explains the intended use of the 
 Modular Sensor proﬁle. For example, maybe if I'm doing IDS, I can say this is the Stellar 
 Cyber Modular Sensor IDS proﬁle. 
 05:00-06:00 
 Or if you have all functions or all features enabled, maybe Stellar Cyber Modular Sensor All, 
 or something that just makes it so that you know what it means. It could also be based on a 
 location, maybe a different location or different customers or different tenants I have. I 
 might have different names to specify those as well. Next, under  Receivers  , you can select 
 in the  Receivers  ﬁeld to specify the destination  for receiving Interﬂow records. The default 
 Receiver is the Stellar Cyber platform. There are some cases where there's cluster 
 environments or for on-premises or cloud deployments where you might have multiple 
 receivers. If you want to close the selection box, select a point away from the selection box 
 to close it. After completing your conﬁguration settings in the sensor proﬁle 
 06:00-07:00 
 the  Submit  button must be selected to apply the conﬁguration  settings to the Modular 
 Sensor. On the bottom right of the Modular Sensor proﬁle, you select  Submit  . You will then 
 see a Stellar Cyber proﬁle was edited successfully message that appears in green every 
 time you select the Stellar Cyber. You will see a sensor proﬁle was edited successfully 
 message appear after you select  Submit  . As mentioned  previously, Modular Sensors are 
 ADM-03-01-224  19 


---

<!-- Página 20 -->

 assigned to the Default-modular proﬁle by default. To assign a new Modular Sensor proﬁle 
 to Modular Sensors, on the top, select  System  then  Sensors  . 
 07:00-08:00 
 Set number two, select  Manage  and  Assign Proﬁle  on  the right-hand side. Step number 
 three in the  ASSIGN PROFILE TO SENSORS  dialog box,  under  Sensor Proﬁles  , select the 
 radio button next to the new Modular Sensor proﬁle that you created, or if you want to 
 leave it by default you can leave it as default. On the right-hand side in step number four, 
 select the Modular Sensor or multiple Modular Sensors. You also have an option to  Select 
 All  . In step number ﬁve, select  Submit  . After selecting  Submit  on a Modular Sensor proﬁle or 
 assigning a Modular Sensor to a new Modular Sensor proﬁle, the Modular Sensors using the 
 proﬁle will restart their services using the new conﬁguration. 
 08:00-09:00 
 Step number one you'll see there that the Stellar Cyber Modular Sensor status will go red, 
 and a message will display that the conﬁguration is out of sync that is normal and is 
 supposed to happen. After a minute you will have to refresh your browser, and then you'll 
 see the  Sensor Status  go green, and the message will  be clear. Now I'll show you what 
 happens behind the scenes when you conﬁgure a Stellar Cyber Modular Sensor proﬁle, or 
 for the very ﬁrst time when the Modular Sensor proﬁle gets assigned to the Modular Sensor. 
 This is an example of the communication ﬂow for when the Stellar Cyber Open XDR 
 platform is installed on premises or in a private cloud. One of the very ﬁrst things that the 
 administrator needs to do on the Modular Sensor is set a CM command to the IP address of 
 the Stellar Cyber platform Data Lake. 
 09:00-10:00 
 Once that's done, on step number two there's a conﬁguration management connection 
 made to the Data Lake from the Modular Sensor using TCP ports 6640 to 6648, all using TLS 
 1 .2. The communication from the Modular Sensor to the Data Lake is encrypted. For step 
 number three, either the very ﬁrst time the Modular Sensor is assigned to the Modular 
 Sensor proﬁle, which, by default, is the default Modular Sensor proﬁle. Or if you're within the 
 proﬁle and you make a conﬁguration change and click  Submit  , or I should say select 
 Submit  . The Message appears on the user screen that  says the Sensor proﬁle was edited 
 successfully, and the Modular Sensor proﬁle is sent to the Modular Sensor. 
 10:00-11:00 
 The Modular Sensor proﬁle has the Interﬂow (JSON) receiver name, which is the Stellar 
 Cyber Data Analyzer IP address. When the Modular Sensor receives the Modular Sensor 
 proﬁle, its conﬁguration is updated and it restarts its services with that new conﬁguration. 
 The sensor then starts receiving logs or packets and creates Interﬂow records to send. On 
 ADM-03-01-224  20 


---

<!-- Página 21 -->

 step number six, Interﬂow records to the Interﬂow Receiver on the data analyzer are sent 
 using HTTPS on TCP port 8889 using TLS 1.2. This information is also encrypted. 
 11:00-12:00 
 The process is different for SaaS deployments. In a SaaS deployment, the administrator on 
 the Stellar Cyber Open XDR platform creates an auth token that contains information on 
 how to reach the Stellar Cyber platform that can be downloaded by the administrator. This 
 is also used to authenticate the sensor. On step two, the administrator goes to the Modular 
 Sensor and copies the auth token from step number one. Next, the Modular Sensor on step 
 three creates the conﬁguration management connection to the Stellar Cyber Open XDR 
 platform using HTTPS port 443 on TLS 1 .2. This contains the auth token information. 
 12:00-12:50 
 The auth token on step four is then validated and authorized. In step ﬁve, the Modular 
 Sensor proﬁle is sent to the Modular Sensor, and it has the JSON Interﬂow receiver name. In 
 step six, the conﬁguration is updated. In step seven, logs and packets are received and 
 Normalized into Interﬂow records. Then they are sent on step eight to the adjacent Interﬂow 
 receiver, which is the Stellar Cyber platform on HTTPS port 8889 using TLS 1.2. That is what 
 happens behind the scenes and it's good to know. 
 This lesson is complete. Thank you for watching. 
 L07 - MODULAR SENSOR CONFIGURATION 
 L07A-PRES: Modular Sensor Conﬁguration (03m:31s) 
 00:00-01:00 
 The next lesson is  Modular Sensor Speciﬁc Conﬁguration.  This lesson,  Modular Sensor 
 Speciﬁc Conﬁguration,  goes through the parameters  that are conﬁgured on individual 
 Modular Sensors. 
 Hi everyone. There are speciﬁc parameters that must be conﬁgured directly for a Modular 
 Sensor that are accessed by selecting  System  , then  Sensors  . Then select the pencil icon to 
 edit the Modular Sensor parameters next to the Modular Sensors you want to edit. In the 
 Modular Sensor speciﬁc conﬁguration you can assign the tenant name. For example, if I 
 have other customers and I want to assign the Modular Sensor to a speciﬁc customer, I can 
 do that right from here. For this example I'm using the root tenant. 
 01:00-02:00 
 ADM-03-01-224  21 


---

<!-- Página 22 -->

 You can change the Hostname and DNS Name that was conﬁgured during the installation 
 of the Modular Sensor here. That can be handy, especially if you have lots of Modular 
 Sensors and you want to rename them. For step number three, you can validate if the 
 Modular Sensor proﬁle is correct or assign a different Modular Sensor proﬁle. The next thing 
 that's incredibly important is make sure the Timezone is set to the location of where the 
 Modular Sensor is deployed. This is important for the logs to display the proper time. For 
 step number ﬁve, if you are sending Syslogs to a Modular Sensor over an unsecured 
 network, it is recommended that you enable Syslog over TLS. This will require that you 
 conﬁgure a certiﬁcate on the log source and in this Modular Sensor conﬁguration. 
 02:00-03:00 
 Then select  Submit  . After you submit the settings, you can validate the Modular Sensor 
 status for the conﬁgured components. If you go to  System | Sensors  , where actually you 
 should be at this moment, you can select the name of a sensor in the  Sensor Name  column. 
 Then if you look inside, you can see the Service and the Status for each of the services. If 
 they are green, they are running successfully. 
 03:00-03:30 
 You can also validate that the sensor proﬁle conﬁgured is the correct proﬁle. The cool thing 
 about that is that you can also go right to the Modular Sensor proﬁle right from this page. If 
 you select the module proﬁle link, you can actually see the name, and then conﬁgure 
 settings as needed. You can then validate the settings are enabled as expected. If you do 
 make some changes, make sure you submit the Modular Sensor proﬁle. Otherwise, if no 
 changes are needed, or you can select the  X  on the  upper-right side of the Modular Sensor 
 proﬁle to leave the proﬁle without saving any changes. That's it. I hope you enjoyed this 
 lesson. 
 This lesson is complete. Thank you for watching. 
 L07B-DEMO: Modular Sensor Conﬁguration (16m:18s) 
 00:00-01:00 
 This lesson continues with demonstrations for  Modular  Sensor Conﬁguration with Modular Sensor 
 Proﬁles and Modular Sensor Speciﬁc Conﬁguration  .  This lesson is a demonstration of  Modular Sensor 
 Conﬁguration with Modular Sensor Proﬁles and Conﬁguring Modular Sensor Speciﬁc  Settings. 
 Hi. For this demonstration, I will show you how Modular Sensors are conﬁgured using Modular Sensor 
 proﬁles. I will log in to the Stellar Cyber Open XDR platform with my administrator account, called 
 admin. Okay. 
 01:00-02:00 
 ADM-03-01-224  22 


---

<!-- Página 23 -->

 When you ﬁrst log in to the Stellar Cyber platform, you start off on the  Visualize | XDR. Kill Chain 
 page. It's actually located right here:  Visualize  | XDR Kill Chain  . The very ﬁrst thing I'm going to  do is 
 go to the Modular Sensor proﬁles, which are located under  System  then  Sensor Proﬁles  . In this list, 
 by default, there's the Default proﬁle. You look at the proﬁle type over here, that's a standard proﬁle. 
 If you look at the next one in the list it's the Default_modular. That is the Modular Sensor proﬁle. The 
 default proﬁles go on to Linux Server sensors and Windows Server sensors, and the default Modular 
 Sensor proﬁle goes on to Modular Sensors. 
 02:00-03:00 
 There used to be two other sensor types. One was called a network sensor and one was called a 
 security sensor. But now Modular Sensors are all-encompassing, and everything can be conﬁgured in 
 a Modular Sensor proﬁle. I'll take a look ﬁrst at what's inside the default Modular Sensor proﬁle. When 
 I go inside, the Proﬁle Name is Default_modular. The Receiver is the Default_receiver, which is the IP 
 address of my Stellar Cyber Open XDR platform. The Log Forwarder is enabled by default. If I select 
 it, you can see the other options that are available. 
 03:00-04:00 
 By going further, I can see that I have the Network Traffic and I can expand or collapse that as well. I 
 will stop here just to make sure that everything is working. I can click  Submit  or if I just want to  leave 
 without saving any settings, you can click the  X  on  the top right. I'll go down and select  Submit  . Here 
 you see the sensor proﬁle was edited successfully. But is this sensor proﬁle in use? Well, what I can do 
 is I can go to  System  and  Sensors  . In my network,  let me take one of these columns and I will say 
 autosize all columns. Okay. Now that I've autosized my columns, I can see all the different sensor 
 names. 
 04:00-05:00 
 The sensor or the Modular Sensor that I'm using for this demonstration is the SC-modular-sensor, 
 which is right here. I can select SC-modular-sensor to get more details. Looking inside, I see that the 
 Default_modular sensor is the sensor proﬁle, and I can actually go right to the Default_modular 
 sensor proﬁle from here as well. Taking a look, the name is the Default_modular. The receiver is 
 Default_receiver, which is the IP address of the Stellar Cyber platform. Log Forwarder is enabled. If I 
 expand it, I can see the options available. Network traffic is enabled. If I scroll down here or expand it, 
 I can also see there are many other network traffic options. We'll be talking about some of these as 
 well. 
 05:00-06:00 
 But what matters now is that this is the proﬁle that is installed. If I were to click  Submit  right now, 
 Submit  will save the conﬁguration and apply it to  the Modular Sensor. If I want to leave a sensor 
 proﬁle without making any changes, you can select the  X  . Now I will then go back to  System  and 
 Sensors  . Again, I can autosize all columns. The other  option I have here is to edit with the pencil icon. 
 As I was mentioning in the slideware that you can edit sensor parameters directly for some of them. 
 These are crucial parameters. 
 06:00-07:00 
 ADM-03-01-224  23 


---

<!-- Página 24 -->

 For example, I can set or change the hostname of this Modular Sensor. I can assign a Modular Sensor 
 proﬁle, which again right now, mine is set to the Default_modular. Once I have an Aggregator 
 conﬁgured, I can select an Aggregator. One of the most important things that you need to set is the 
 timezone. I'm in California, and my sensor is in California, that's what matters the most. Therefore, I 
 have chosen the  America/ Los Angeles  timezone, but  all the timezones are available. For example, if 
 I take a look at the list, there are lots of different options to choose from. I'm going to select  America  . 
 I'm going to select  Los Angeles  . 
 07:00-08:00 
 I can also add a note, which I really like. I can say, “Modular Sensor for Training.” Then I will select 
 Submit  . Again, once you modify the conﬁguration of  a Modular Sensor, you will see the status say 
 disconnected and the conﬁguration will be out of sync. After less than a minute, it will come back and 
 sure enough within, it was actually 10 to 15 seconds, my sensor is now green. Now let's take a look at 
 the Default_modular sensor proﬁle. 
 08:00-09:00 
 If I go here, if I take a look at the Default_modular, if I'm looking at this I might want to ensure that it 
 has a default proﬁle that hasn't been touched, that hasn't been modiﬁed. One way I can do that is I 
 can select the Default_modular proﬁle and click the option to  Clone  . When I clone, to begin with it will 
 always add a date. I can say, I'll use SC (for Stellar Cyber) Modular Sensor and I'll say training for this 
 one, and  Clone  . Now, if I modify this Modular Sensor,  again I can deselect that one, but if I modify this 
 Modular Sensor proﬁle, again it defaults to the default receiver. 
 09:00-10:00 
 The network traffic is there and Log Forwarder is conﬁgured because it's always on. To begin with, 
 we'll take a look at these options, the network traffic. There's the Application Identiﬁcation, which is 
 the deep packet inspection I was talking about earlier. There's the Application Session that tracks the 
 state of the applications from the network ﬂows. That's really cool. When I type in  show session  on 
 a Modular Sensor, I can see all the traffic going through. Then there's the Application Metadata. This 
 is how the Modular Sensor is collecting the metadata that it will Normalize into Interﬂow and send to 
 the platform. 
 10:00-11:00 
 One of the options we'll be talking about later is excluding certain applications. We also have some 
 other options, which are there by default. You don't need to touch them. You can leave them on, and 
 we'll also talk about buffering a little bit later as well. But right now I'll  Submit  . The sensor proﬁle  was 
 edited successfully. Do you remember how to assign this proﬁle to the Modular Sensor? Let's go take 
 a look. If I go to  System  then  Sensors  , the next option for the sensors is to select  Manage  , and then 
 Assign Proﬁle  . Now I have an extra sensor proﬁle. 
 11:00-12:00 
 I will select  SC Modular Sensor  . I will assign that  to the SC-modular-sensor I have here. If I had a 
 whole bunch of sensors I was assigning this to, I could say  Select All  . I won't do that though. I will 
 select  Submit  . Notice once I select  Submit  , the status  has now gone red. That is because the system 
 ADM-03-01-224  24 


---

<!-- Página 25 -->

 is out of sync now. The conﬁguration is out of sync. Now, if I wait a few let's see how long this takes. 
 That was again like 10 seconds or less. Now my Modular Sensor is assigned. Let me just make sure 
 it's the right one in the list. I can select it. 
 12:00-13:00 
 If I hover over the  Sensor Proﬁle  I see that it's  SC Modular Sensor training. If I select it, there's my 
 conﬁguration that I made. Now I can close this out. If you close it out that way, it doesn't cause the 
 sensor to reload its conﬁguration. That's all there is to assigning a sensor proﬁle to a Modular Sensor. 
 Okay. In the last demonstration I showed you how to clone the default Modular Sensor proﬁle to 
 create a new Modular Sensor proﬁle and assign it to a Modular Sensor. Now I'll show you how to 
 create a Modular Sensor proﬁle from scratch. Okay. 
 13:00-14:00 
 To do that, I will go to  System  , then  Sensor Proﬁles  .  Then I will select  Create  and  Add Modular 
 Sensor Proﬁle  . Note that the standard sensor proﬁle  is for Linux Server sensors and Windows Server 
 sensors. They were also for network sensors as well and security sensors. Network sensors and 
 security sensors are no longer available. For new installations, Modular Sensors can do everything 
 that the network sensors and security sensors did, plus as a lot more functionality. You can select the 
 modules that you want to have enabled or disabled. We'll add a new Modular Sensor proﬁle. I will 
 give it the name SC Modular Sensor New 
 14:00-15:00 
 just so we know it's the brand new Modular Sensor proﬁle. For the Receivers you select in the 
 selection box, select the default_receiver, then you select out of the selection box. By default, the Log 
 Forwarder is always enabled. That's what we'll use to begin with for this example. I'll select  Submit  . 
 Now my new Modular Sensor proﬁle has been created. To assign it, again I go to  System |  Sensors  . 
 You don't need to select any other sensor here. Just go to  Manage  , then  Assign Proﬁle  . I can select 
 the new Modular Sensor proﬁle, SC Modular Sensor New, and assign it to the SC Modular Sensor. 
 15:00-16:20 
 All you need to do is select  Submit  . As always, if  we take a look at this line, the Modular Sensor then 
 loads its services again using the new conﬁguration. We'll go red for the status saying it's 
 disconnected. The message will be: Conﬁguration is out of sync. If I refresh it may take about 30 
 seconds to a minute when assigning a brand new Modular Sensor proﬁle. There you have it. I would 
 say about 40 seconds after assigning a brand new Modular Sensor proﬁle, the status became green 
 again. Just to validate, if I go to SC Modular Sensor and select it, and take a look, it's now SC Modular 
 Sensor New. Alright. This is the end of this lesson. I look forward to seeing you in the next lesson. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  25 


---

<!-- Página 26 -->

 L08 - PARSERS, NORMALIZATION, AND INTERFLOW 
 L08A-PRES: Parsers, Normalization, and Interﬂow (15m:06s) 
 00:00-01:00 
 The next lesson is  Parsers for Normalization into  Interﬂow.  This lesson,  Parsers for 
 Normalization into Interﬂow,  provides details for  how parsers are used on Modular Sensors 
 to Normalize metadata and telemetry into Interﬂow records in JSON format. 
 In this lesson, I will discuss more about parsers and how they are used for normalization into 
 Interﬂow records. Parsers are used to analyze, interpret, and extract relevant information 
 from log ﬁles generated by various devices, systems, and applications. Parsers can identify 
 speciﬁc ﬁelds within the log data, such as timestamps, source and destination IP addresses, 
 event descriptions, and much more. 
 01:00-02:00 
 Using parsed logs, security analysts can gain insights into potential security threats, detect 
 anomalies, and investigate incidents. Parsers play a crucial role in log analysis and are 
 essential for effective threat detection and response by analysts and the Stellar Cyber Open 
 XDR platform. Note that Stellar Cyber has hundreds of built-in parsers that can interpret 
 logs from generic or vendor-speciﬁc sources and more are included in every release. 
 Looking at the right is an excerpt of the Stellar Cyber parser documentation. Here you can 
 see the list of names on the left-hand side for the different parsers. I will cover this next. 
 02:00-03:00 
 To access the Stellar Cyber documentation for log parts reports, you can go to 
 https://docs.stellarcyber.ai. When the search bar appears, you can search for log parser 
 ports. The entry gets returned called log parser ports that you can select. Also note that 
 there's a help version. By default, if you're on the Stellar Cyber platform, the correct help 
 version will be displayed for the platform you are using. If you go to docs.StellarCyber.ai, you 
 have to select the help version you want to use. If you are not sure, always select the latest 
 help version. When you select log parser ports in the documentation, you can scroll down to 
 see the table containing all the log parsers. 
 03:00-04:00 
 Looking at the Stellar Cyber parser documentation excerpt on the right-hand side, you'll see 
 that there are several different columns. Each of them is very important The  Device  column 
 speciﬁes the device system or application that is forwarding logs to the Stellar Cyber 
 Modular Sensors for analysis by the Stellar Cyber Open XDR platform The  Port  column 
 speciﬁes the TCP or UDP port to conﬁgure on the log source that sends logs to the Modular 
 ADM-03-01-224  26 


---

<!-- Página 27 -->

 Sensor. The port is used by the Modular Sensor to identify the appropriate parser to use to 
 Normalize the logs into Interﬂow records. The  msg_origin.source  column speciﬁes the 
 vendor's product. You use this ﬁeld and the Interﬂow records to ﬁnd the logs when threat 
 hunting using the index speciﬁed in the index column. 
 04:00-05:00 
 The  msg_origin.category  column speciﬁes the overall  category of where the product ﬁts 
 into a solution such as ﬁrewall, or pass, which is password as a service, DB logs which is 
 database logs, endpoint, XDR, and many more. The  Index  column indicates the ﬁelds that 
 must be present and are not null for the logged data to be entered into the respective index. 
 In some instances, no speciﬁc ﬁeld is required. Just the index name is listed. For many 
 parsers, the remaining data that is not mapped to a speciﬁc index is otherwise mapped to 
 the Syslog index. 
 05:00-06:00 
 For example, for Fortinet data analyzer logs received on port 5542 by the Modular Sensor 
 that are forwarded to the Stellar Cyber platform. Data is added to the ML IDS/Malware 
 index. If the incoming vendor.attack underscore name ﬁeld is not null. Data is added to the 
 traffic index if the desktop IP is not null. The remaining data is added to the Syslog index. 
 Use the  dev_type  ﬁeld in the Interﬂow records to  ﬁnd the logs when thread hunting in the 
 speciﬁed index. With help from the documentation you can ﬁnd the indices used for the 
 speciﬁc device type. Here if I look at the pfSense ﬁrewall, the index is traffic if the source IP, 
 source port, destination IP, dstport, and protocol ﬁelds are within the logs. 
 06:00-07:00 
 Otherwise, traffic is sent to the Syslog. Find the name of the device under 
 msg_origin.source  . In this case, it is pfSense_fw  for pfSense ﬁrewall. For indices, select the 
 box to select all. This is only a test to ﬁnd out which indices are actually in use by that 
 message origin dot source. In the search box type, dev_type: pfSense_fw. After typing in the 
 search, all the records and charts displayed are reﬂected by what was typed in the search 
 along with all the indices speciﬁed. Here, the legend shows that the indices are Syslog, 
 traffic, and Alerts. 
 07:00-08:00 
 The documentation just mentioned traffic and Syslog because that's how it gets into the 
 platform. But Stellar Cyber creates the Alerts indices well when it analyzes all the logs that 
 are coming in. Stellar Cyber creates the Alerts from looking at the logs that are in the Syslog 
 and traffic indices. The Alerts are generated by the Stellar Cyber platform. Log event 
 messages received from different sources arrive with different vendor speciﬁc formats. On 
 number one on the right-hand side is a Check Point log from a Check Point ﬁrewall. Here we 
 ADM-03-01-224  27 


---

<!-- Página 28 -->

 have a time stamp, then the Check Point ﬁrewall name, and then there's a FW ﬁeld, which is 
 the IP address of the ﬁrewall itself. 
 08:00-09:00 
 There's a source, which is the IP address of the traffic coming into the ﬁrewall, and a DST is 
 the IP address of where the traffic was going from 192.168.1.10 in this example. There's also a 
 source port and a destination port, and the action of the rule. All these are within the log 
 message sent by the Check Point ﬁrewall. Looking at the bottom is an example of a 
 SonicWall ﬁrewall. The SonicWall has again a timestamp as the name of the SonicWall itself. 
 There is an IP address for the SonicWall, but this one does not have the FW equals. It’s just 
 the IP address itself. Note there's an ID. There's a serial number. There's a whole bunch of 
 different ﬁelds that are on two examples. 
 09:00-10:00 
 Looking at the Check Point ﬁrewall, with this SRC equals 192.168.1.10 and SRC_port equals 
 56034. On the SonicWall, the source is 192.168.1.99: the source port 34098. The format is 
 completely different. If I am trying to analyze and compare log messages from different 
 vendors, it gets very difficult at this point because now I have to understand all the different 
 formats of all the different logs that come in. Well, that's where Stellar Cyber comes in 
 handy. Now here’s an example of what happens when the logs are Normalized into 
 Interﬂow records. 
 10:00-11:00 
 Modular Sensors use the built-in parsers to Normalize log messages from independently 
 formatted third-party logs collected as Syslog in CEF format, LEEF format. It could be JSON 
 logs, etcetera. They get Normalized into consistent Stellar Cyber Interﬂow JSON formatted 
 records for all ﬁeld names and values. Note, the ﬁeld names are now the same for Check 
 Point and SonicWall Interﬂow records. Looking at the top right, number one, the Stellar 
 Cyber Normalized Check Point log excerpt shows a key of source IP and a value of 
 192.168.1.10. I like calling the key the ﬁeld name, and then the right-hand side is the value. The 
 source port is srcport: 56034. The key is source port. The value is 56034. 
 11:00-12:00 
 Looking at the Normalized SonicWall log, it is now the same ﬁeld name, SRCIP and value of 
 course will be what was received by the log itself. That will be different and that's okay. The 
 srcport is the same, again ﬁeld name, then the value is the source port received. Looking at 
 all the ﬁeld names and values, they are Normalized into a consistent format. This now 
 allows SOC analysts to use a consistent format when searching for values among all 
 different types of devices and services. It also allows the Stellar Cyber machine learning, 
 ADM-03-01-224  28 


---

<!-- Página 29 -->

 statistical analysis, and heuristic rules to be able to compare and correlate all the data to 
 ﬁnd threats. 
 12:00-13:00 
 Additional examples of Normalization from third-party integrations to Stellar Cyber are like 
 the CrowdStrike EDR has a ﬁeld for the local IP or host name of the device. It's called 
 CrowdStrike.event.local IP. With Stellar Cyber normalization, the CrowdStrike local IP ﬁeld 
 and similar ﬁelds from other third-party integrations are Normalized to host.IP. CrowdStrike 
 EDR has a ﬁeld for classiﬁcation of threats. It's called threat info.classiﬁcation. Again, with 
 Stellar Cyber normalization, the CrowdStrike threat info_classiﬁcation ﬁeld and similar ﬁelds 
 from other third-party integrations are just Normalized to a ﬁeld called, “threat.” Again, this 
 makes it much easier. Now I don't have to memorize the speciﬁc name for the values from 
 all the different integrations that we have. Interﬂow records in JSON format based on a 
 summary of the sessions including metadata about the session, 
 13:00-14:00 
 and sends them to the Stellar Cyber platform. Interﬂow records are created using data that 
 is Normalized from logs, network traffic, and Connectors. Looking at the picture on the right, 
 there's a Modular Sensor and an example of a JSON Interﬂow record excerpt. The JSON 
 Interﬂow record contains application and network metadata and telemetry. On the right is 
 an example of the key value of source IP colon, the IP address, which is the value. Notice 
 that this is Normalized because every source IP within Stellar Cyber will be listed as srcip. 
 The destination port as an example is a ﬁeld name, DST port, and the value is 443. 
 14:00-15:06 
 The total bytes is metadata as an example of how many bytes have been included in this 
 session so far. The app ID family again is extra metadata. The app path is something called, 
 “ssl.https” to let you know it's encrypted. There's the destination IP and the appid_name. The 
 appid_name actually comes from deep packet inspection. We'll cover more about that later. 
 Modular Sensors send the JSON Interﬂow records to the Stellar Cyber platform over an 
 HTTPS connection. The Stellar Cyber platform is then able to perform data processing on 
 the received Interﬂow record. It actually gets stored in the platform where all the machine 
 learning and statistical analysis rules and heuristic rules are applied to look for threats. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  29 


---

<!-- Página 30 -->

 L09 - LOG FORWARDER AND LOG FILTER CONFIGURATION 
 L09A-PRES: Log Forwarder and Log Filter Conﬁguration (12m:09s) 
 00:00-01:00 
 The next lesson is  Log Forwarder and Log Filter Conﬁguration.  This lesson,  Log Forwarder 
 and Log Filter Conﬁguration  , explains the process  and conﬁguration steps to ingest logs 
 from third-party security, identity, and infrastructure systems and tools as well as how to 
 optimize ingestion by ﬁltering logs that are not essential for security operations. 
 Now I will discuss one of my favorite topics, which is the Log Forwarder and Log Filter, which 
 is part of the Modular Sensor. This is a key function of the Modular Sensor. Logs are sent to 
 the Modular Sensors from security and network infrastructure systems and tools. Once they 
 are forwarded to the Modular Sensor, Modular Sensors Normalize the logs into Interﬂow 
 records in JSON format, which are then forwarded to the Stellar Cyber platform. 
 01:00-02:00 
 The Stellar Cyber platform then uses machine learning, statistical analysis rules, heuristic 
 rules, custom ATH playbooks, and graph machine learning to identify threats, generate 
 Alerts, and correlate Alerts into Cases. Log ﬁlters can be conﬁgured on Modular Sensors to 
 optimize the data ingested by the Stellar Cyber platform by excluding speciﬁc log types that 
 are not required for threat investigation or detection. Examples of security and 
 infrastructure systems include ﬁrewalls, EDR, which are endpoint detection and response, 
 NDR, which is network detection and response, vulnerability management systems, email, 
 and many more conﬁgured to send logs in the form of Syslog and CEF or LEEF format. 
 JSON and Netﬂow/IPFix. 
 02:00-03:00 
 Netﬂow is Cisco speciﬁc. IPFix is more a generic way of forwarding logs. All can be sent to 
 the Stellar Cyber Modular Sensors. Modular Sensors that Normalize the logs from all the 
 different sources into Interﬂow records in JSON format and forward to the Stellar Cyber 
 platform. Hopefully that is being locked in. I've said this over and over again, and I will keep 
 on repeating this so that It ﬂows nicely off your tongues as well. Modular Sensors Normalize 
 the logs from all the different sources into Interﬂow records in JSON format, and forward to 
 the Stellar Cyber platform. I know this might sound kind of repetitive, but it is incredibly 
 important to understand the importance of how the logs are parsed, Normalized, and 
 forwarded to the Stellar Cyber platform. 
 03:00-04:00 
 ADM-03-01-224  30 


---

<!-- Página 31 -->

 Note that each log source that can be parsed and Normalized by the Modular Sensors is 
 found in the Stellar Cyber documentation and has a dedicated TCP/UDP port for 
 identiﬁcation of the log in the Modular Sensor. Now here's an example on the Stellar Cyber 
 platform of how a log forwarder is enabled and conﬁgured. Log Forwarder is enabled by 
 default and conﬁgured in sensor proﬁles. To get to Modular Sensor proﬁles, you select 
 System  from the top menu and then  Sensor Proﬁles  on the left-hand side. You ﬁnd a 
 sensor proﬁle that you want to modify and click the pencil or I should say again, select the 
 pencil icon to edit a Modular Sensor proﬁle. 
 04:00-05:00 
 The Log Forwarder module in the Modular Sensor proﬁle has additional settings that can be 
 conﬁgured by selecting the  Log Forwarder  option.  One of the options you'll see is the 
 Worker's Batch Size  . You should not have to modify  this unless directed by our Stellar 
 Cyber Customer Success or Support teams. But you can set the maximum number of 
 records that can accumulate before they are sent to the Data Sink for storage. The default 
 is 100 records, and the range is between one and 10,000. This allows for batching of logs to 
 improve transmission efficiency. One hundred should suffice for most deployments. Data 
 ﬁltering or log ﬁlters. One of the other options is to add log ﬁlters to ﬁlter out logs that are 
 not needed before sending the logs to the Stellar Cyber platform. This is helpful to optimize 
 the amount of data that needs to be sent and ingested by the Stellar Cyber platform. We'll 
 cover more on this later. 
 05:00-06:00 
 There are no log ﬁlters by default. If you do not have log ﬁlters, you can leave the sensor 
 proﬁle conﬁguration by selecting  Submit  . Then create  log ﬁlters as described in the next set 
 of slides. After, come back to the Modular Sensor proﬁle to conﬁgure the log ﬁlters and 
 assign them to this Modular Sensor proﬁle. As you can see in step number three, to create 
 log ﬁlters go to  System | Log Filters  . On the  Log  Filters  page, select  Create  as you see in 
 step number four. Specify the following log ﬁlter parameters. Enter the log ﬁlter name. Enter 
 a value that describes which data logs are being ﬁltered. 
 06:00-07:00 
 In this environment, there are some QA test devices that use speed tests and some other 
 tests that I do not want to log on the Stellar Cyber Modular Sensor or on the Stellar Cyber 
 platform. Therefore, I will ensure that the log ﬁlter name is describing the logs that I am 
 trying to ﬁlter, such as exclude QA test services. For the tenant, select  All Tenants  , or if you 
 are only enabling this log ﬁlter for a speciﬁc tenant, then you select that. Next, for the Log 
 Source, this is optional. You can select a speciﬁc product or technology from the drop-down 
 list. In this case, if you are not excluding speciﬁc products or technologies, but are instead 
 ADM-03-01-224  31 


---

<!-- Página 32 -->

 excluding speciﬁc servers with speciﬁc ﬁeld names within logs, the Log Source does not 
 need to be speciﬁed. 
 07:00-08:00 
 Next, as you see in step number four, select  +Condition  .  In step number ﬁve, select a ﬁeld 
 name from the list, such as computer_name. For step number six, for the operator, select an 
 operator, such as “is,” “is not,” or “contains,” or “does not contain,” or the ﬁeld just actually 
 exists. For step number seven, enter the values. Type in values, such as the preﬁx of a host 
 name for servers, then press  Enter  . Every time you  type in a new value, you can press  Enter 
 again and that will actually add the value to the Values ﬁeld. 
 08:00-09:00 
 For step number eight, optionally add additional conditions that are logically ANDed with 
 the other conditions by selecting  +Condition  again.  In this case, I have added another value 
 called dstip, and the operator is “matches.” The IP is 10.20.1.99. With this additional 
 parameter, The log ﬁlter will exclude logs that have a computer_name ﬁeld with a value 
 containing QA1-test or a value containing QA-test and have a destination IP value of 
 10.20.1.99, which is a test server. 
 09:00-10:00 
 In other words, if the log received has a ﬁeld name called computer_name with a value of 
 QA-Test contained in the name of the value, and the destination IP ﬁeld in the log is 
 10.20.1.99, do not ingest that log. Likewise, if the log has a computer name ﬁeld that contains 
 QA-Test and has a dstip value set to 10.20.1.99, then that will also be excluded. When you are 
 done, select  Submit  . Then back on the  Log Filters  page you can see your new log ﬁlter was 
 added. If you would like to create additional log ﬁlters, go ahead and select  Create  . Now it's 
 very important to know here that having the log ﬁlter does not mean logs are being ﬁltered. 
 10:00-11:00 
 You actually have to assign the log ﬁlter to a Modular Sensor proﬁle under  Log Forwarders 
 for the log ﬁlter to take effect. Also note, if you select the stacked line icon, for a column, 
 you can autosize the column to view the entire column name. As I just mentioned, to apply 
 log ﬁlters to a Modular Sensor proﬁle, go to  System  | Sensor Proﬁles  .  Edit the Modular 
 Sensor proﬁle. For step number three, select the space for  Exclude by Filters  . When you do 
 that, you'll have a selection box. In the selection box select your log ﬁlters, then select 
 outside of the selection box to close it. 
 11:00-12:10 
 Then select  Submit  to save your settings. The Modular  Sensor will then load the new proﬁle 
 with the new ﬁlter settings and will no longer ingest those types of logs. Now for some 
 ADM-03-01-224  32 


---

<!-- Página 33 -->

 troubleshooting tips. If you are on the  Log Filter  page and you notice that there is no trash 
 can icon next to a log ﬁlter and you're trying to remove the log ﬁlter, the cause for this is 
 that the log ﬁlter is in use. You will have to go to your Modular Sensor proﬁle and deselect 
 the log ﬁlters from the  Log Forwarding  section. Then  after you do that and save the 
 Modular Sensor proﬁle, you will then go back to the  Log Filters  page and the trash icon for 
 deleting an entry will exist. 
 This lesson is complete. Thank you for watching. 
 L10 - LOG FORWARDER EXAMPLE 
 L10A-PRES: Log Forwarder Example (05m:35s) 
 00:00-01:00 
 The next lesson is  Log Forwarder Example  . This lesson,  Log Forwarder Example,  uses a pfSense 
 ﬁrewall as an example to describe the entire end-to-end process of conﬁguring log forwarding for 
 the Modular Sensor to ingest pfSense logs in order to parse and normalize into Interﬂow records and 
 send to the Stellar Cyber Open XDR platform. 
 Here I'll provide a real example of conﬁguring a Modular Sensor to be a log forwarder for a pfSense 
 ﬁrewall. In this example, the goal is for the Stellar Cyber platform to obtain metadata from the 
 pfSense ﬁrewall as a data source for use in analysis and threat detection. 
 01:00-02:00 
 The pfSense ﬁrewall can be conﬁgured to send its log messages to the IP or hostname of the 
 Modular Sensor along with the speciﬁed TCP/UDP destination port that we'll ﬁnd in the 
 documentation. The Modular Sensor uses the port speciﬁed to identify the logs from pfSense to 
 parse and normalize them into Interﬂow records. The speciﬁc TCP or UDP port to conﬁgure on the 
 pfSense ﬁrewall to send logs to the Modular Sensor is available in the Stellar Cyber documentation at 
 https://docs.stellarcyber.ai. When the  Documentation  page appears, in the search box, you can 
 search for log parser ports. As an example here, I search for log parser ports. 
 02:00-03:00 
 Then the entry appears called log parser ports, which you can then select. In the documentation use 
 your browser search or command f or control f to ﬁnd pfSense. When you ﬁnd pfSense in the table, 
 the ﬁrst column is the name of the log source, which is pfSense ﬁrewall, the second column is the 
 TCP/UDP destination port number, which is 5543. With this information, you can conﬁgure the 
 pfSense ﬁrewall that will forward the logs to the Modular Sensor IP, which is in this case 10.20.1.15 on 
 port 5543. In the pfSense user interface, from the top menu bar as an example, you can select  Status 
 | System Logs  . 
 03:00-04:00 
 ADM-03-01-224  33 


---

<!-- Página 34 -->

 Then you select  Settings  . For the log message format one of the options is Syslog (RFC 5424, RFC 
 3339, microsecond-precision timestamps). You can use that log message format, which is selected by 
 default. You scroll down a little bit further you'll see Remote log servers. If you have an IP colon port 
 ﬁeld available, looking at this example, here's one that's empty. It says IP colon port. If you do not 
 specify a port, port 514 is used by default. Here I did have a free entry, so I typed in 10.20.1.15:5543 
 04:00-05:00 
 which is the IP address of the Modular Sensor: the port Sensor found in the Stellar Cyber 
 documentation for the pfSense ﬁrewall. Modular Sensors identify logs that come in on TCP or UDP 
 port 5543 as pfSense ﬁrewall logs so that they can parse them. For remote syslog content, select the 
 logs you want to forward to the Stellar Cyber platform or select  Everything  to send all logs. As this is 
 an example, I am sending everything. In real life if you do not need to have all the logs sent to the 
 Stellar Cyber Modular Sensor, then you can select individual logs. Next, save the conﬁguration. The 
 pfSense ﬁrewall is now conﬁgured to forward logs to the Modular Sensor IP on 10.20.1.15 with port 
 5543 as shown in this example. 
 05:00-05:35 
 The Modular Sensor uses the port to identify the logs as pfSense to parse and normalize into 
 Interﬂow records. The Modular Sensor forwards the Interﬂow record in JSON format to the Stellar 
 Cyber platform. That's how it's done. This can be done in similar ways for any product. 
 This lesson is complete. Thank you for watching. 
 L10B-DEMO: Log Forwarder Example (28m:16s) 
 00:00-01:00 
 This lesson continues with demonstrations for log forwarder example. This lesson is a demonstration 
 of log forwarder conﬁguration and validation using a pfSense ﬁrewall as an example. 
 Hi everyone. In this lesson, I will show you how to conﬁgure the Stellar Cyber Modular Sensor as a log 
 forwarder and give an example of using a pfSense ﬁrewall that will send logs to the Modular Sensor, 
 which will then be sent to the Stellar Cyber platform. We'll then verify that the logs are making it 
 correctly. Alright. Let's do it. 
 01:00-02:00 
 First thing I'm going to do is look at the Modular Sensor proﬁle. I'll go to  System | Sensor Proﬁles  , 
 and remember yesterday or for me it was yesterday, I created a new Modular Sensor proﬁle called 
 SC Modular Sensor new, go take a look at this one. What we see here is I do have the log forwarder 
 enabled. If I take a look, if I expand it, I have Workers, which I don't need to modify, and I have Data 
 Filtering, which we will not touch this until later in this lesson. What data ﬁltering will do again, is make 
 sure that I can ﬁlter out applications or, for example, the communications between the sensor and 
 the Stellar Cyber platform that I don't actually need to ingest into the platform. 
 02:00-03:00 
 ADM-03-01-224  34 


---

<!-- Página 35 -->

 Alright. But for now, look–I actually don't have to do anything because by default, the Log Forwarder 
 is enabled. Then if I take a look at the Modular Sensor itself from  System | Sensors  and I take a look 
 at my Modular Sensor. I'll just expand this window a little bit and click the name of the Modular 
 Sensor. Here, it is deﬁnitely the right proﬁle. It is SC Modular Sensor New. Again clicking into that I see 
 that the log forwarder is there. Okay. The next step is really what I do on the pfSense, but I do need to 
 ﬁgure out what port for Syslog, I need to send to the Modular Sensor. 
 03:00-04:00 
 One of the ways I can do that is open up the Stellar Cyber documentation. That's under the question 
 mark right from the platform. If you're inside the platform, I can go right to Knowledge Base home or 
 you can go to docs.stellarcyber.ai. What I want to look for now is log parser ports. It doesn't matter 
 the case I type. I can use uppercase or lowercase. It doesn't matter. I can look for log parser ports. If 
 you don't want to see the highlighting, I can select the highlighter right here and that'll remove the 
 highlight from the search. 
 04:00-05:00 
 I then can scroll down in this help document, which is really, really useful. I can look for the device, 
 which is my pfSense ﬁrewall. There are hundreds of devices here, and I can scroll down or I can just 
 search for it but I think it's funner. I know funner's actually not a word, but that's okay. It is more fun to 
 scroll down and look at all the different device sources that are available. If I scroll down further and 
 go right to here, there's some Palo Alto. What I am looking for is pfSense and there it is. So the name 
 is pfSense, the port is 5543. The message origin source is pfSense_FW. We'll need that for later. 
 05:00-06:00 
 The device category is ﬁrewall. The indexes or indices, you can use either index or indices or indexes 
 it's ﬁne. Traffic, if the logs have a source IP, a source port, a destination IP a destination port and a 
 protocol. The log will be sent to the traffic index. Otherwise, all the rest of the pfSense logs will be sent 
 to the Syslog index. On top of that, the Stellar Cyber platform will look for threats and create Alerts 
 from these logs. So you might also see traffic in the Alerts index. Alright. Now that I have 5543 do you 
 think you can remember that? 5543. Okay. I will go to my pfSense ﬁrewall. 
 06:00-07:00 
 Again, the reason why I'm showing you pfSense is because it's free, and you can download pfSense 
 and test pfSense. It's a great ﬁrewall to use for testing. If I go to  Status  and  System Logs  you'll  see 
 that there are many types of system logs available. There's ﬁrewall logs as well and DHCP logs and 
 Authentication logs, all depending on the services I have enabled on the pfSense. But there we go. 
 What I want to go to right now are the  Settings  . In  the  Settings  , add the log message format, I'm 
 going to use the syslog message format. If I scroll down there are many different options. 
 07:00-08:00 
 What I'm looking for in the conﬁguration is where I can send logs remotely. Right now I have logs 
 already being sent to another sensor, which is on the 10.20.1.19, but I also have a sensor with a 
 different IP address. Let's take a look. I have a sensor on my network and I'm going to use the 
 command line of my Mac to access my sensor, which is at 10.20.1.15. And I can log in and type in  show 
 ADM-03-01-224  35 


---

<!-- Página 36 -->

 interface  . Here I see yes that it's 10.20.1.15. But again, I can also go ahead and go to my platform 
 and see it here as well. 
 08:00-09:00 
 Just by going to my platform, go to  Sensors  . If I  select my sensor here you see in the pop up here, it's 
 10.20.1.15. I have all the information I need. Do you remember the port number? I do. It's 5543, but you 
 know what? It's better to double check. Yes. 5543 in the documentation. Excellent. I'm ready to go. I'm 
 going to send it to 10.20.1.15:5543. Usually you have multiple servers or multiple log servers you can 
 send to, just make sure you have an option available. You can keep your other remote log servers as 
 well and add Stellar Cyber as an additional log source. 
 09:00-10:00 
 In this case I'm going to log everything. Now in real life, I would only log what I need to log. But for 
 now, to get more data, I will just log everything. That's it. I will now select  Save  . There's nothing  else to 
 do except verify that it's working. Alright. I will go back to actually I'll go to my sensor ﬁrst, and I can 
 type in  show log forwarder  .  Alright. I do see that  pfSense is here. Now I had pfSense running 
 already. I do have some data here. 
 10:00-11:00 
 But if it's a new installation, you will deﬁnitely see this start to increase from zero all the way up. Now I 
 will go to my platform. Do that. I'll go and scroll down here. I can look at  Log Forwarder Stats  ,  Log 
 Forwarder Summary  . Again, I can see that I do have  log forwarder data coming in. Now the other 
 thing I can do is look at the documentation again. Then the documentation for pfSense, again this is 
 called the message origin source. If I scroll up in the documentation all the way to the top of this 
 table. Here we go. 
 11:00-12:00 
 Msg_origin.source. This can be used for a search. If I go into the Stellar Cyber platform if you are 
 searching for data in the platform, the best place to go is I  nvestigate | Threat Hunting  . Now here this 
 page defaults to showing you the  Alerts  indices. Again  the Stellar Cyber platform takes all the log 
 messages and depending on the type of message categorizes them into one of the indices you see 
 here. This makes it much easier to search for data more efficiently. I know right now if they're by 
 machine learning or by heuristic rules or statistical analysis rules 
 12:00-13:00 
 that Alerts may be created by the platform, but also, I could have some Syslog, and I may have 
 some traffic as well. Again, I didn't have to memorize that If I look for pfSense. Let's do a search. 
 Doing the search in my browser with the command f or control f, I can then ﬁnd the line. Here I see 
 the traffic index and syslog index. Again, I don't have to memorize any of this stuff. It's helpful if you 
 memorize it. But again the documentation is always there for you. Alright. Select off this pop up to 
 close the pop up. Now this is the search box. I can type msg_origin.source, or is it the other way 
 around? Did I do it right? Let's take a look. 
 13:00-14:00 
 ADM-03-01-224  36 


---

<!-- Página 37 -->

 I will search for message or how about origin? Yeah. msg_origin.Source. Again, I don't have to 
 memorize this stuff. It's easier if you do though. Use colon and then pfSense_ﬁrewall. I'm looking for 
 all messages that have a source of pfSense_FW. Right now again I've had this connected for a while. 
 I disconnected it for this demonstration and I brought it back in. But right now the time is 9:35 in my 
 lab. Right now I have logs from 9:05. Let me see if that's the latest. There we go. Now I just ﬁltered on 
 the time. 
 14:00-15:00 
 Today is April 5th and now I see 9:35. I am receiving the logs again. Alright. Now they are coming in. If 
 I take a look at one of these logs I see ICMP, which is ping essentially. There's DNS requests. There's 
 tcp3389. tcp3389 is I think that is remote desktop, right? If we go to 3389 port, yes Windows remote 
 desktop. Again, you don't have to remember everything. If I look at these messages here and I scroll 
 through 
 15:00-16:00 
 I can see all the Interﬂow records that are coming in. The JSON Interﬂow. Here's the cool thing. 
 Again, the logs have now been normalized. If I take a look, SRCIP is the Stellar Cyber normalized ﬁeld 
 name for the source IP address. Take a look here. Stellar Cyber has added the dstip geolocation. 
 We've added the source IP geolocation. Again, this does not come from the sensor itself. It's when the 
 data arrives or the Interﬂow record arrives at the Stellar Cyber platform. We will, or the platform will, 
 not we, but the platform will add the geolocation. That's really cool. There's some other really cool 
 things that are added as well. 
 16:00-17:00 
 Let's scroll down through this JSON Interﬂow record. We also see some other geo information. If you 
 scroll down here, I can see the log information. Scroll down further. Again, yeah the message origin 
 source, which we looked for earlier. We have the message_origin.source. This is, if you take a look, 
 this is the top of it. So you'll message origin. And then underneath it you always do the dot source or 
 message origin dot category or message origin dot processor so I can search for any of these. If I 
 scroll down further, what else do we have? We also have some of the reasons why this log is here. 
 This was a matching ﬁrewall rule. 
 17:00-18:00 
 I matched the rule. If I go down any further, yeah there's is there a there a type? Let me take a look 
 here. Let's say type. Yeah. Source IP type That's something else that Stellar Cyber adds during the 
 enrichment process. We enrich with the geolocation. We enrich with the source IP type. Before I 
 mentioned that there is RFC 1918 addresses. RFC 1918 addresses are, for example, anything in the ten 
 dot zero dot zero dot zero slash eight or the one seventy two sixteen dot zero to zero slash twelve or 
 the one ninety two one sixty eight zero to zero slash sixteen. 
 18:00-19:00 
 But if it's not that or not what's called the multicast IP address, then it's public. In other words, 
 everything on the internet almost is public. We add that. We also take the IP address for the IP and 
 the destination IP, and we look for the geo, excuse me, the threat intel. Are the IP addresses good IP 
 ADM-03-01-224  37 


---

<!-- Página 38 -->

 addresses? This could be good. It could say Tor node. The reputation is incredibly important. This 
 record gets enriched with that data. Again, the log itself did not have any of this information but 
 Stellar Cyber enriches all the data that comes in. When it creates the Interﬂow, it adds on all this 
 essential information that is really useful for looking for threats. 
 19:00-20:00 
 Then Stellar Cyber statistical analysis rules and heuristic rules and machine learning can use all this 
 information as well to look for a threat. Look at what else we added. This deﬁnitely was not in the log, 
 but we actually have the username. Who was doing the remote desktop. This is Jerry G. It's actually 
 Jerry Guthmiller. He's my head of enablement. He's performing remote desktop, and his name is in 
 this log. Again, this is all enriched data which is really cool. Alright. I'll close this out, and we know the 
 logs are showing up. That's great. Okay. Now that I've shown you how to use the 
 message_origin.source to look for the pfSense ﬁrewall. 
 20:00-21:00 
 I’ll remove this message origin source so you can see what happens if I don't have that selected. Now 
 that I've removed the ﬁlter, I can see all the sources coming in. Now in these charts, I have top log 
 sources, I have top sensors. I have documents over time which are Interﬂow records over time 
 essentially. This shows you the indices, which are Syslog traffic and Alerts. If I scroll in I can actually 
 see that I do have a little bit of light purple there, which is the Alerts. I have the traffic and Syslog. 
 That's the breakdown of each. Right now I'm actually looking for relative time in the last ﬁve hours. 
 Okay. Next, if you look at the  Top Log Sources  , one  of them is the pfSense ﬁrewall. 
 21:00-22:00 
 If I zoom in a little bit here for you, I can select the plus or the minus. Plus says ﬁlter for the pfSense 
 ﬁrewall, which is the message origin source. And minus says ﬁlter out the pfSense ﬁrewall. In other 
 words, on the display I will not see this information. Well, I want to look for just pfSense ﬁrewall. I can 
 select it here. If I can scroll back now, all these messages are from what I see from the pfSense 
 ﬁrewall in the last ﬁve hours. Okay? I will then go to  Filters  and I see the log source was added.  By 
 clicking that plus next to pfSense ﬁrewall, it added the log source pfSense _FW. I can actually copy 
 this as a query to see what the query looks like. 
 22:00-23:00 
 I will remove this from the ﬁlter right now and close the ﬁlters. Now if I paste what I had in the ﬁlter 
 and hit Return, I can then see, and I'll zoom in for you as well here, that the message_origin.source is 
 pfsense_fw, or message underscore origin dot source dot keyword is quotes, pfsense_fw. Now the 
 quotes aren't actually needed in this case. There are reasons to use quotes, but pfSense_ﬁrewall is 
 one term. Since it's one term, I don't need quotes. Quotes are used to basically specify you have a 
 phrase and we don't really have a phrase. You can use it with or without quotes. You get the same 
 exact results. 
 23:00-24:00 
 Here, the dot keyword means it must be the exact case. Let me give you an example of that. I'm 
 going to remove this portion and you'll get the same one hundred and thirty thousand, two hundred 
 ADM-03-01-224  38 


---

<!-- Página 39 -->

 and ﬁfty one. But since its message, now underscore origin dot source dot keyword, if I were to say 
 with a capital P, I get nothing because it must be an exact match. That's what dot keyword means. If I 
 get rid of dot keyword and put the colon in here, watch what happens. If I say capital P, there's no 
 change. I could even make this capital FW. No change. When I don't use the dot keyword, the 
 searches are case insensitive. 
 24:00-25:00 
 The ﬁeld name is case sensitive, but the value is not case sensitive. That's a good thing to know. We'll 
 cover this over and over again in these examples. Again the other thing is what happens if I don't 
 select the index? So let me leave this page. I will go to the XDR Kill Chain. I'll go back to the XDR Kill 
 Chain. The reason why I'm showing this is as you're analyzing threats or doing some investigation, 
 you may switch between the different pages on the system. Notice though that my ﬁlter is preserved. 
 Message origin source is still there. But if I go back to  Investigate | Threat Hunting,  again I see  my 
 ﬁlters preserved. I'll expand it so you can see more. 
 25:00-26:00 
 But now I only have 13 Interﬂow records showing. When I was looking at it before, I had over a 
 hundred thousand Interﬂow records. I'm looking here and I go oh maybe it's the time frame but no I 
 was using ﬁve hours before. What's the difference? And then if? you take a look and I'll scroll down 
 here you can see the uh in this case there's now 13 records. Because it is a live system. As I move 
 around more will increase. As I'm going through now and I go wait a minute, I am seeing only Alerts. 
 That's because when I go back to the  Investigate |  Threat Hunting  page, the indices section defaults 
 to  Alerts  . I can go back down and select  Syslog  and  Traffic  . 
 26:00-27:00 
 Now I'm back over a hundred thousand again. I thought I did something wrong actually. Yeah. I really 
 didn't. But you know it's really important to understand what happens. Just so it's clear now, let me 
 go back to Visualize. I'll go to another page, maybe  Analyst View  . I'll go back to  Investigate | Threat 
 Hunting  . Again every time you come to this page, it  defaults to Alerts. You got that. I hope so. Alright. 
 This is actually another important thing to understand about this page as well. Let's say for instance, I 
 have Alerts but I'm looking for the past week. That could be a lot of data in a production system. But 
 look what happens if I select multiple indices:  Syslog  and  Traffic  . 
 27:00-28:16 
 Now the time interval is the last 24 hours. The last 24 hours is the maximum time you can search 
 when multiple indices are selected. If I were to bring this back to just for example, Traffic. Now I can 
 go back and set this for a longer period of time. Note that as well. On a single indice you can search 
 pretty far back. Let's go over here. I can search for the last week, for the last month. Whereas once I 
 put multiple indices in, now I have Syslog and Traffic, the max I can go to is 24 hours. Okay. You got 
 that? Awesome. Okay. I will clear this ﬁlter out now and I hope you enjoyed this lesson. Thank you 
 very much. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  39 


---

<!-- Página 40 -->

 L11 - LOG SOURCE CONFIGURATION FOR SINGLE TCP OR UDP 
 PORT 
 L11A-PRES: Log Source Conﬁguration for Single TCP or UDP Port 
 (05m:55s) 
 00:00-01:00 
 The next lesson is  Log Source Conﬁguration for Single  TCP or UDP Port.  This lesson,  Log Source 
 Conﬁguration for Single TCP or UDP Port,  shows how  to conﬁgure the Stellar Cyber platform to 
 enable the Modular Sensor to receive logs from systems using a single port, such as the default 
 Syslog port 514. 
 In this lesson I will cover what happens if you do not have the option to conﬁgure a log port on a log 
 source, and you have to conﬁgure the default Syslog port, TCP or UDP 514. 
 01:00-02:00 
 As we demonstrated previously for the log parsing to function, the Modular Sensor needs to identify 
 the log and the product that it belongs to so it can assign a parser. If you send logs to the Modular 
 Sensor on port 514, which is the default, the Modular Sensor then needs to identify the log from a 
 speciﬁc vendor. Stellar Cyber has a way of accomplishing this. Stellar Cyber has a log source 
 conﬁguration that provides you the ability to map log sources to parsers, which gets conﬁgured on 
 Modular Sensors. To conﬁgure log sources, go to  System  on step number one,  Log Sources  on the 
 left-hand side. Now I will conﬁgure the log source by selecting  Create  . This will open the  Add Log 
 Source Conﬁguration  dialog. 
 02:00-03:00 
 The ﬁrst option I will conﬁgure is the name. In this case, I am using only port 514 on the Check Point 
 ﬁrewall to send logs to the Stellar Cyber Modular Sensor. This will be a perfect device to do that with. 
 The name will be “Check Point Firewall.” Next, I will specify a tenant name. If I have multiple tenants, 
 this will be the tenant that has the Check Point ﬁrewall inside. In my case, it's the root tenant. Next, I'll 
 specify a log source address. Here I type in the IP address for each log source device and enter 
 Return  . In this case, the log source devices must be Check Point ﬁrewalls. You can enter multiple after 
 every IP address, you hit  Return  or  Enter  . Type in  another IP address. 
 03:00-04:00 
 Hit  Return  or  Enter  and it creates a bubble box for  each IP address you enter. Note that the 
 addresses from the log source to the Stellar Cyber Modular Sensor cannot be NATed or Proxied. 
 Otherwise, the IP addresses will not work. Next, I will specify the ingestion port. This is the port for 
 incoming log messages from log source devices. The default Syslog port for UDP and TCP is 514. If 
 you are using Syslog with TLS, you can set it to 6514. The other reason to set the ingestion port is if 
 your Check Point ﬁrewall or any other type of device is using a different ingestion port, you can enter 
 that here as well. When you're done, select  Submit  . 
 ADM-03-01-224  40 


---

<!-- Página 41 -->

 04:00-05:00 
 The settings are automatically applied to Modular Sensors and the root tenant in this example. 
 Modular Sensors will now be able to parse and normalize Syslogs from Check Point ﬁrewalls coming 
 in on port 514, as long as they match the IP addresses speciﬁed. From the Modular Sensor 
 command-line interface, you can view the log sources with the following command:  show 
 logforwarder port-ingestion  . Here I see the rule that's  added to the Modular Sensor. For 
 example, on lines seven, eight, nine, and ten, I have the different IP addresses 10.20.1.241 and 
 10.20.1.240. On TCP and UDP port 514 will get mapped to the parser port 5519 
 05:00-05:55 
 which is the port the Stellar Cyber Modular Sensor can use to identify the Check Point ﬁrewall parser. 
 Now as an example, here's the Check Point ﬁrewall in the diagram. That is 10.20.1.241. The Check Point 
 ﬁrewall is conﬁgured to forward logs to the Modular Sensor IP 10.20.1.15 with port 514, which is the 
 default Syslog port. The Modular Sensor uses the port ingestion table to identify the logs from Check 
 Point to parse and normalize it into Interﬂow records. Then the normalized logs as Interﬂow records 
 in JSON format are sent to the Stellar Cyber platform. 
 This lesson is complete. Thank you for watching. 
 L11B-DEMO: Log Source Conﬁguration for Single TCP or UDP Port 
 (05m:28s) 
 00:00-01:00 
 This lesson continues with demonstrations for log source conﬁguration for single TCP or 
 UDP port. This lesson gives a demonstration of how to conﬁgure the Stellar Cyber platform 
 to enable the Modular Sensor to receive logs from systems using a single port, such as the 
 default Syslog port 514. 
 Okay. In the slide presentation I explained about the log forwarder, but what happens when 
 the port cannot be set? 
 01:00-02:00 
 In other words, I learned the port of the pfSense ﬁrewall, but maybe I have some devices 
 that I can't change the port or I'm working with a a company that I am managing as a 
 managed service provider and they don't have the ability to change the port that's being 
 that's being used to forward traffic to a Modular Sensor to identify the parser for log 
 ingestion. Well, Stellar Cyber also has a method to solve this, which is our log sources 
 capability. If I go now to  System  and go to  Log Sources  ,  from the log source conﬁguration, I 
 can now make it so if a log comes to a Modular Sensor on the default TCP UDP port of 514, 
 or maybe a different port that's being used by the organization, I can map that to the 
 correct parser. 
 ADM-03-01-224  41 


---

<!-- Página 42 -->

 02:00-03:00 
 Let's give an example here. I'll go to  Create  and  there's a list of parsers here already, which 
 are essentially log sources that Stellar Cyber has parsers available for. As an example here, 
 I'll just choose the Check Point ﬁrewall like I used in the slides. Now I can say alright. For the 
 root tenant or maybe a speciﬁc tenant, depending on your organization, or if I'm managing 
 an organization and that one organization cannot change their port number I can do it just 
 for the one tenant. Now I'm going to specify a speciﬁc IP address for the log source in the 
 root tenant: 10.20.1.240. 
 03:00-04:00 
 Maybe I have another Check Point at 10.20.1.241. Now, and I click away from the selection 
 box to clear it, now I say okay. If in the root tenant in this case, I have a log source of 
 10.20.1.240 or 10.20.1.241, sending logs on the default port of 514 using UDP or TCP, that is 
 Check Point ﬁrewall log traffic. Alright. Then this Modular Sensor can apply the parser for 
 the Check Point ﬁrewall. Now I can select  Submit  .  That's all I need to do. I don't need to do 
 anything else. Modular Sensors will automatically be updated. 
 04:00-05:00 
 If I go to  System  , I go to  Sensors  . There's nothing  red here. I don't need to modify anything. 
 But if I now go to my sensor and I type in  show logforwarder  and I can do a question 
 mark here and go oh what was the command?  show logforwarder  port-ingestion  . 
 It's not here yet. There we go. It looks like it takes a moment or two. There it is. I now see 
 that these rules got added. One for each UDP and TCP from 240 to 241. That's cool. 
 05:00-05:30 
 Now I can parse traffic and I don't have to make the speciﬁc port for a parser. I think it's 
 easier just to use the parser port and I think it's a recommendation from Stellar Cyber to 
 use the parser port. But in cases where you can't, Stellar Cyber has you covered. Okay. 
 This lesson is complete. Thank you for watching. 
 L12 - VALIDATE LOG FORWARDER 
 L12A-PRES: Validate Log Forwarder (07m:46s) 
 00:00-01:00 
 The next lesson is  Validate Log Forwarder  . This lesson,  Validate Log Forwarder,  provides the 
 steps to validate the parsed and normalized logs are being ingested by the Modular Sensor 
 as Interﬂow records in the Stellar Cyber Open XDR platform. 
 ADM-03-01-224  42 


---

<!-- Página 43 -->

 You might be asking yourself, “How to validate that the log forwarder is working?” Or you 
 might be asking me, “Hey Paul. How do I know that the log forwarder is working?” Well, 
 there are several ways to validate the log forwarder’s working and that the Stellar Cyber 
 platform is ingesting log data. From the Stellar Cyber platform, if you select  System | 
 Sensors  and select the name of your Modular Sensor  in the list, you will see a page with a 
 bunch of details. 
 01:00-02:00 
 You can then scroll down and select  Log Forwarder  Summary  . You also want to make sure 
 that the time frame is relevant. In this case, I will say the time type is  Relative  and the time 
 interval is in the  last 24 hours  . Looking at the bottom  now under the log forwarder 
 summary, I see that I have plenty of logs coming in. Another option to validate log 
 forwarder data is being ingested by the Stellar Cyber platform is from the  Operational 
 View  . If you go to  Visualize | Operational View  , then  in  Event Origins  look for pfSense. 
 Here's the  Event Origins  chart. 
 02:00-03:00 
 There I see Linux agent Modular Sensor, and pfSense_ﬁrewall. Perfect. For the pfSense 
 ﬁrewall, I can select the plus right next to it, which will ﬁlter for all the events that are related 
 to the pfSense ﬁrewall. On the top left, on the  Filters  ,  you'll see a little bubble pop up. That 
 lets you know a ﬁlter has been applied. Next, if you select  Filters  , the ﬁlters bar will appear. 
 On step ﬁve you'll see the pfSense ﬁlter was added, but you yourself may not know what 
 that actually means. What does it mean that the pfSense ﬁrewall is added as a log source? 
 03:00-04:00 
 You can actually ﬁgure out what query that actually is. One of the options is to as step 
 number ﬁve,  Copy as Query  . On step number six, after  selecting  Copy as Query  , select the 
 x  to remove the pfSense ﬁrewall query. This will  make sure it doesn't interfere with some of 
 the tasks we're doing in a few minutes. Next, on step seven, I can paste the query. There you 
 see again the key value pairs. We have message_origin.source of pfsense_ﬁrewall, or 
 message_origin.source.keyword pfSense_ﬁrewall. Now keyword, we'll talk about much, 
 much later. Keyword is just saying that it must be an exact match. That's all the dot keyword 
 means in this case. 
 04:00-05:00 
 Next, if you scroll down after entering the search, on the  Operational  View  page, you'll see 
 all the Alerts associated with the log source speciﬁed in the search. Note that Alerts have an 
 Alert Type  and  Alert Score  ﬁelds, which can also  be column headers. This can help you 
 determine how critical the Alert is. You can also view the Interﬂow events and Alerts from 
 the log source by going to  Investigate | Threat Hunting  .  Once you're in  Investigate | 
 ADM-03-01-224  43 


---

<!-- Página 44 -->

 Threat Hunting  , next to  Indices  , you can select the  Alerts  button. It looks like an  Alerts 
 button by default because that's the default indice that's speciﬁed. 
 05:00-06:00 
 But if you select  Alerts  , you'll get a drop-down list  with many other indices. In this case, we 
 know that the pfSense ﬁrewall from our documentation will have logs that are categorized 
 as Syslog or Traffic and also Alerts that are generated by the Stellar Cyber platform. In this 
 case, I've selected all three Alerts, Syslog, and Traffic. To close the pop-up box, select outside 
 the pop up box to close it. Next, on the top search bar to the right of  Filters  , select the  L  , 
 which is for the Lucene query. This will expand the search box. Here you can see that the 
 same query that we copied previously is still applied. 
 06:00-07:00 
 If you select  L  also it will bring up a little pop  up letting you know what Lucene actually is. 
 Here, you see the legend shows data is received for Syslog, Traffic, and Alerts. If you zoom 
 in, you can see that all three colors are there. If you look at the middle of the chart you will 
 see that there are some Alerts there that have the lighter purple color. You can also select a 
 single indice from the indices selection box to view events for speciﬁc indices. For example, I 
 can look for just Alerts, or just Syslog, or just Traffic from the pfSense ﬁrewall. You can also 
 validate log forwarder by viewing details on the Modular Sensor by going to  System | 
 Sensors  . 
 07:00-07:45 
 If you select and A  dd a Checkbox  next to the Modular  Sensor of your choice, you can then 
 select  CLI access  from the CLI pop-up window, or from  an SSH to your Modular Sensor, you 
 can type  show logforwarder  . Logforwarder is one word.  You wait about 10 to 20 seconds, 
 and you'll get the result back. Here, I can see a number of logs associated with the 
 pfSense_ﬁrewall. I know that it is working. 
 This lesson is complete. Thank you for watching. 
 L13 - LOG FORWARDER PRESERVING RAW LOGS 
 L13A-PRES: Log Forwarder Preserving Raw Logs (05m:17s) 
 00:00-01:00 
 The next lesson is  Log Forwarder Preserving Raw Logs.  This lesson,  Log Forwarder 
 Preserving Raw Logs  , shows how to conﬁgure Modular  Sensors to include the original raw 
 log message in the Interﬂow record that is sent to the Stellar Cyber Open XDR platform. 
 ADM-03-01-224  44 


---

<!-- Página 45 -->

 You might be asking yourself, can the Stellar Cyber Modular Sensor log forwarder function 
 preserve the raw log that it received from various security and infrastructure tools? The 
 answer is yes. Raw logs can be preserved by the log forwarder by conﬁguring the log 
 forwarder settings in the Modular Sensor proﬁle. 
 01:00-02:00 
 If you go on the top right on step number one to  System  ,  then select  Sensor Proﬁles  . You 
 can then select the pencil icon to edit a Modular Sensor proﬁle. As described in the log 
 forwarder lessons, Stellar Cyber normalizes all log messages into Interﬂow records in JSON 
 format. However, the original raw log is not preserved by default because metadata from 
 raw log was already collected and normalized into Interﬂow records, there may not be a 
 need to preserve the raw logs, and saving raw logs might actually cause a higher level of 
 ingestion on the Stellar Cyber platform. However, sometimes organizations have a need to 
 preserve the original raw log, and we can conﬁgure that. If there's a need to preserve the 
 original raw log within the Interﬂow record, you can enable  Raw Log Capture  in the log 
 forwarder conﬁguration. 
 02:00-03:00 
 Under  Data Filtering  , you then go down to  Raw Log  Capture  and slide the lever to the right 
 to enable raw log capture. After completing your conﬁguration settings in the sensor proﬁle, 
 you must select the  Submit  button to apply the settings  to the Modular Sensor. If all was 
 successful, you'll see, “Sensor proﬁle was edited successfully.” After this, it will take a minute 
 for the conﬁguration to be reloaded on the Modular Sensor. Next, in the Stellar Cyber 
 platform, to view the raw log within an Interﬂow record, go to  Investigate | Threat Hunting  . 
 03:00-04:00 
 Next to  Indices  , in this example I will select  Syslog  ,  Traffic  , and  Alerts  . You can select  All 
 until you know which indices contain the data you need. Next, in the search toolbar type 
 parser_raw_message  as the ﬁeld name  :*  , which is  a wildcard. I'm saying look for all the 
 Interﬂow records that contain the ﬁeld name parser raw message. Next, if I scroll down to 
 the event list called documents here and select  i  in the  Action  column for an event, I can 
 view the Interﬂow record. In the Interﬂow record, select  Details  . Now I can scroll down to 
 ﬁnd parser_raw_message. 
 04:00-05:16 
 There I'll see the raw log message in its entirety as it would appear without normalization 
 and enrichment. Note that the name of the IP ﬁelds in the raw log for example is source IP 
 has SRC_IP. Destination IP has DST_IP. Here I can validate that normalization happens. Here 
 the source IP now in the Stellar Cyber normalized portion is SRC IP as a ﬁeld name colon, 
 the IP address. The destination IP is DSTIP colon, the destination IP address. This is a perfect 
 ADM-03-01-224  45 


---

<!-- Página 46 -->

 screenshot for showing normalization. If we did not have normalization, you would get what 
 you see in the raw logs from every single device that you have integrated into the platform. 
 Normalization is essential for being able to ﬁnd information quickly and for machine 
 learning, statistical analysis rules, and heuristic rules to be applied. 
 This lesson is complete. Thank you for watching. 
 L13B-DEMO: Log Forwarder Preserving Raw Logs (19m:26s) 
 00:00-01:00 
 This lesson continues with demonstrations for log forwarder preserving raw logs. This lesson 
 is a demonstration to show how to conﬁgure Modular Sensors to include the original raw log 
 message in the Interﬂow record that is sent to the Stellar Cyber Open XDR platform. 
 Hi everyone. For this lesson, I want to show you how to preserve the original raw message 
 or the original raw log that gets sent to the Modular Sensor from a log source. Now this 
 might be needed by some organizations for some compliance reasons. 
 01:00-02:00 
 It might be needed because SOC analysts within an organization are used to the original 
 message, and they know they understand the ﬁelds of the original message. Whatever the 
 reason why you want to preserve the original raw message before it gets normalized and 
 before it gets enriched, I can show you how to do that. Now what we'll do here is go to 
 System | Sensor Proﬁles  . Again I'll modify SC Modular  Sensor New. We'll go to  Log 
 Forwarder  . Here I can slide the option to enable  Raw  Log Capture  . I'll go ahead and submit 
 that. If I go back to my sensors list, I will now see that– 
 02:00-03:00 
 –as we always see now, this sensor will be restarted using the new conﬁguration. While 
 that's happening though, I'll go to  Investigate |  Threat Hunting  Okay. So now I want to 
 search for the parser_raw_message:*, and I see that I don't have any messages yet coming 
 in with the parser raw message ﬁeld. Actually, maybe I do. Does anyone see what could be 
 happening here? Every time I go to the  Investigate | Threat Hunting  page on the Stellar 
 Cyber platform, we default to the  Alerts  indice. What  we want to be looking at right now is 
 either the  Traffic  or the  Syslog  indices. Keep that  in mind. 
 03:00-04:00 
 Now if I were to specify  Traffic  for the indice, take  a look now. I see messages that contain 
 the parser raw_message ﬁeld. If I take a look at one of these now, I'll take a look at this one. 
 One of the best ways to see this is from the  Details  .  I can look for the parser raw message 
 ﬁeld. Let me scroll down and there it is. I see the log type, this is the ﬁrewall, I see the ﬁrewall 
 ADM-03-01-224  46 


---

<!-- Página 47 -->

 rule. I see exactly how it comes to the Modular Sensor. You'll notice for example the desk IP 
 is dst_IP. We see the dst port as DST_port. 
 04:00-05:00 
 Let's see if we can ﬁnd the source as well. There must be a source port in here. My vision 
 isn't as good as it used to be. The source IP is 192.168.1.103. Okay. This is not normalized. 
 Right? Don't forget if it's normalized, what's it going to be? If you take a look at the source IP 
 here, and look at the source IP here, the source IP ﬁeld after normalization is SRC IP. Before 
 normalization for every product it could be totally different. That's why normalization is 
 incredibly important. Notice there's no geolocation. There's nothing letting us know that the 
 destination IP reputation is good or bad. Well, in this case, the destination IP is a broadcast. 
 It's a local network message. Let me ﬁnd a better one to use. 
 05:00-06:00 
 Let's try DNS or let's try this one right here. That's another broadcast. If I want to ﬁnd some 
 other messages here, let's take a look. I want something that's not a broadcast. 3389. Do 
 you guys know what 3389 is? 3389 is a remote desktop. If I take a look here, wow! Here I see 
 the reputation of the source is malicious. I see that the source country is Panama. If I go to 
 Details  now, and see if we can ﬁnd the parser raw  message. In the parser raw message, I 
 just have that it's the following. Right? 
 06:00-07:00 
 It's TCP. It has an IP address in it. It's actually really, really hard to read or understand. But 
 the fact that we normalized the message and to then readable ﬁelds in JSON format, now I 
 can get a better idea. I can look at the destination IP, the region, which is my device. It's in 
 my lab. It's a private address. Then if I look at the source itself, the country is Panama, the 
 reputation is malicious. It learned that through ETPro in DHS. Right? These are some threat 
 intel's we are using. At this point I should take a look and start to block some IPs in my 
 ﬁrewall. 
 07:00-08:00 
 I can also look right here as well. If I go to  Key Fields  –  Key Fields  is, when we are not 
 analyzing the threats, we can make it so that you can look up some of these IPs. For 
 example, I go to VirusTotal and it takes me to a different site. The VirusTotal is saying, “Hey, 
 by the way, this IP address is malicious.” That's pretty cool. Right? I can do that right from 
 the platform itself. What port is being used? It is 3389. I want to make sure that I block this IP 
 or make sure that no one has access to my devices internally using port 3389. 
 08:00-09:00 
 ADM-03-01-224  47 


---

<!-- Página 48 -->

 At this point I would check my pfSense ﬁrewall. Let me go back in here again. Okay. I can go 
 even further. If I had a Connector to my ﬁrewall, I could actually block the IP address right 
 here. I could run a script, I can actually add a log ﬁlter. If it wasn't important, I could actually 
 just create a log ﬁlter and ﬁlter out that type of message from even appearing. I can trigger 
 an email if I ever see something like this again. A lot of things you can do at this point 
 though I know that I will need to block some IP addresses or actually only permit some IP 
 addresses to access my network on Port 3389. 
 09:00-10:00 
 Again, this is a test lab environment, so that's okay. But you always want to make sure you 
 are safe and using the Stellar Cyber platform you can see that. But again, the raw message 
 itself, it's great to see that you can do it. But you notice there was not much in the raw 
 message. It's the Stellar Cyber platform on top of the raw message that's doing the 
 normalization and enrichment that gives you the value. Now I think it's a good time to do a 
 little bit of digging into the threats I just noticed when looking at the parser raw messages. 
 Again, getting the extra value out of the platform. One of the things I'll do is I don't really 
 care much for the parser raw message anymore. I'll clear that search out. Again, I see all my 
 messages coming into the traffic log in the last 24 hours. 
 10:00-11:00 
 What I was looking at before was the remote desktop, which is port 3389. If I do a search 
 now for 3389, again I don't need to actually specify a ﬁeld name, we do 3389, and I see here, 
 here's one right here. If I go into the more info, I see that there is a source reputation of the 
 scanner from this one, which is from the Netherlands. So this source host if I go to VirusTotal 
 for this one, let's see if this is a bad host. Well, this one actually shows as clean, which is 
 interesting but who knows? Maybe it's not clean now. Alright. 
 11:00-12:00 
 But they're actually doing some scanning on my port 3389. Okay. What I want to do though 
 is see if I could ﬁnd any other source reputations that are bad. I'll go to the JSON, or, 
 actually I'll use JSON. I can look for the reputation right here. There's a destination IP 
 reputation, but I want the source reputation, let's ﬁnd that. There it is right here. Search down 
 further. Here we are. Source reputation of scanner. Okay? I go, “Wow! I wish I knew what 
 other reputations there were.” I can use this as a copy right now source reputation scanner. 
 12:00-13:00 
 If I were to copy this, and do a source reputation of scanner, I can now see that I have 927 
 with a source reputation of scanner. What I can do as well is actually select the  Column  . I 
 can go here and say, reputation. I can make that a column that I have now. There we go, 
 scanner. If I were to clear this out, I have good, and then you had scanner before. But what if 
 ADM-03-01-224  48 


---

<!-- Página 49 -->

 I want to see more? What are the other ﬁelds that I've collected? Do I have to search 
 through everything to ﬁnd the other types of reputations? The answer is no. We have 
 something built in called the Interﬂow dictionary. I can open the Interﬂow dictionary and do 
 a command f and search for a reputation. 
 13:00-14:00 
 There it is right there. I want the source reputation though, so I'll scroll down further. It's also 
 going to hit Reply, but source reputation. If I select this, I see that I have good, or scanner, or 
 malicious. I have a lot more good than everything else. That's what the chart is showing. But 
 if I want to see all the malicious, I can actually use this Interﬂow dictionary, select the plus 
 here, and then I can close the Interﬂow dictionary, and every single record I see here is 
 malicious. One of the other options you can do as well, if I ﬁnd that inside the log here, let's 
 look for the reputation again. 
 14:00-15:00 
 I'll scroll down here. That's DST IP reputation, Source reputation. There we go. From here you 
 can create a query. If I go up here to the search, and command V, we now will have a query 
 for you to use. The keyword is saying that this malicious has to be the exact case. I don't 
 care about the case, so I'm going to get rid of this OR. But I can say, for example, AND 
 dstport and 3389. All of these are malicious for this destination port. There are a lot of cool 
 things I can do here. But should I be concerned? 
 15:00-16:00 
 I am seeing a lot of activity for remote desktop that's a source of malicious. Well, let's take a 
 look even further. If I go to the  Details  , this is  from my ﬁrewall that's reporting it. But one of 
 the most important things here is that there was an action of block. Right? At least I know 
 that the traffic didn't make it. I'm actually logging blocked attempts. Many times you don't 
 log blocked attempts, but I like to do it because I want to know what's happening. But I can 
 go a little bit further on this as well. I know this ﬁeld name is  action  and  block  . So if I were to 
 say AND–excuse me. Let's try it over here. I should have the same exact results: 411. But 
 again, let me close this out because what I want to know next–I'll get rid of the AND action 
 block– 
 16:00-17:00 
 –is what other actions there are for that ﬁrewall. Again, I can go to the open Interﬂow 
 dictionary, look at the  action  , which is the ﬁrst  one. I see that I only have an action of  block  . 
 Maybe because I have a ﬁlter. Let me go here. That's malicious. Let me get rid of malicious. 
 I'll clear all here. Here we go. Clearing all ﬁlters. I see that I have some records with pass, 
 some with block, and some with deny. If I were to say pass and just ﬁlter on these, alright 
 ADM-03-01-224  49 


---

<!-- Página 50 -->

 now I can say, okay–let me close all the ﬁlters, and I'll close the Interﬂow dictionary. Again, 
 my ﬁlter stays there, it's pass, or I can copy this as a query. 
 17:00-18:00 
 Close it out, go to  Filters  , paste that in here and  it does the same thing. Again, we always 
 give you the action keyword, which is the exact case. I don't care about the exact case. Now 
 I can start combining these things. Okay. What's been good is 53 DNS. Well, DNS has been 
 permitted. Okay. But do I have any action pass for the dst port 3389? I don't. Right? That's 
 good news. We just make sure that dst port is actually correct by itself. Yes. The dst port 
 3389. But in all these cases, the 6,524 records, if I say action AND action block. 
 18:00-19:00 
 Yes most of them right there OR action and we'll say a deny. I'll put this in a grouping that 
 says the destination port AND one of these two–either action block OR action deny. Okay. 
 That's the case here. All these records will have action block or action deny. But if I were to 
 say AND action pass, nothing. Okay. That's good news that no one was able to get in or was 
 permitted into, viewing those records. 
 19:00-19:25 
 Again, I will make sure one more time for the  action  ﬁeld. Yes. Pass, block, or deny. Okay. 
 That is good to know. Thank you for watching. I hope that you found this lesson valuable. 
 This lesson is complete. Thank you for watching. 
 L14 - NETWORK TRAFFIC ANALYSIS 
 L14A-PRES: Network Traffic Analysis (10m:22s) 
 00:00-01:00 
 The next lesson is  Network Traffic Analysis Details  and Conﬁguration.  This lesson,  Network 
 Traffic Analysis Details and Conﬁguration,  explains  how to conﬁgure to collect network 
 traffic off SPAN ports or TAP devices and provides details of how the Modular Sensor 
 analyzes network traffic to create sessions in metadata and forward it as Interﬂow records 
 to the Stellar Cyber Open XDR platform. 
 Here I will describe network traffic analysis. Network traffic analysis is essential for network 
 detection and response, which is done by the Stellar Cyber Open XDR platform. Network 
 traffic from switches is sent to the Stellar Cyber Modular Sensor via SPAN ports or TAP 
 devices. 
 ADM-03-01-224  50 


---

<!-- Página 51 -->

 01:00-02:00 
 Modular Sensors use deep packet inspection, DPI, to identify applications, create a session 
 state, correlate app processes, and add metadata such as the number of bytes used by the 
 application during a session. A summary of the traffic and metadata is normalized into 
 Interﬂow records and forwarded to the Stellar Cyber platform. Now I will describe how 
 network traffic analysis works on the Modular Sensors. To begin though, I'll describe this 
 network diagram. On the bottom left is Laptop A. It has an IP address of 192.168.1.190. Does 
 anyone remember what type of IP address that is? 
 02:00-03:00 
 You guessed it. It is an RFC 1918 address, and it is a private IP address. Laptop A connects 
 wirelessly to the WiFi access point, which is then connected to the bottom switch on the left. 
 That is an access layer switch. That access switch connects to a distribution switch on port 
 2/12. The Modular Sensor’s management interface is connected to 1/12 of the switch. The 
 management interface is what's used to connect to the Stellar Cyber platform. Port 1/14 on 
 the switch is connected to Ethernet 1 on the sensor. If we look at the conﬁguration, we've 
 basically said any traffic coming in on port 2/12 of the distribution layer switch, either from 
 or to that port, mirror that traffic to the Modular Sensor on port 1/14. 
 03:00-04:00 
 Or basically all the switch knows is it's mirroring the traffic to port 1/14. The fact that we 
 have a Modular Sensor on it means that the Modular Sensor can collect that traffic. Next, 
 the distribution layer switch is connected to a ﬁrewall. The ﬁrewall is connected to a router, 
 which then takes you to the internet. On the internet is where the AWS management console 
 exists. AWS again is a cloud infrastructure company–Amazon Web Services. The IP address 
 of the console used to manage AWS, or my AWS environment. This example was actually 
 the IP 3.3.10.1. 
 04:00-05:00 
 This is a public IP address. In this example now Laptop A, again with IP address 192.168.1.190 
 connects to the AWS management console with an IP of 3.3.10.1 using HTTPS, which is TCP 
 port 443. That's a mouthful. Now when that connection is made, the traffic is mirrored. The 
 SPAN port mirrors the traffic to and from the switch on port 2/12 and sends to the Modular 
 Sensor on port 1/14. Traffic from Laptop A, in this case to AWS is captured by the Modular 
 Sensor. Now my laptop will have a screen showing the AWS console. 
 05:00-06:00 
 Looking at the Modular Sensor now, the Stellar Cyber Modular Sensor performs deep 
 packet inspection, or DPI, on traffic to identify applications. There are over thirty eight 
 hundred applications detected by Stellar Cyber's deep packet inspection engine. On the 
 ADM-03-01-224  51 


---

<!-- Página 52 -->

 sensor, if I were to have CLI access, I can type  show dpi  .  Looking at  show dpi  , I can scroll 
 down to look for AWS console. There I see AWS_console has an app ID of 3574, and it is a 
 web category. Modular Sensors create a session table based on IP ﬂows learned from 
 network packets using stateful ﬁrewall technology, which includes the following metadata. 
 06:00-07:00 
 It has the 5-tuple. You'll hear this a lot and see this a lot when talking about ﬁrewall routers 
 and switches. The 5-tuple is the source IP address within a packet, the destination IP address 
 in a packet, the protocol, which is either TCP/UDP/ICMP, the source port within a packet, and 
 the destination port within the packet. Together, there's ﬁve entries and that's called the 
 5-tuple. Next, the application is determined from deep packet inspection. Do you remember 
 what that number was? Well, let's take a look. What you're seeing here on the Modular 
 Sensor is the output of the command  show session  .  If I look at the  show session  , I will 
 actually see the entry. You'll see the IP address 192.168.1.190, the source port. 
 07:00-08:00 
 You'll then see the destination IP, which was 3.3.10.1/443, which is the destination port, which is 
 HTTPS, and 6 is the protocol. There's the 5-tuple. The protocol 6, by the way, is TCP 17 UDP 
 ICMP, which is Ping, if you've ever heard of that, is one. Next, you'll see some of the 
 metadata associated with it as well. You'll see the number of forwarded packets and the 
 number of forwarded bytes. You'll also see the backward packets, BWD packet, and the 
 backward BWD bytes, which essentially is the return traffic for the session. But remember 
 we talked about it earlier, there was an app ID and the app ID is 3574. If we go back and 
 look at that table, 3574 was the AWS console. 
 08:00-09:00 
 Pretty cool. By doing this, the Stellar Cyber Modular Sensor doesn't need to send every 
 single packet to the Stellar Cyber platform. It can determine all the packets are related to 
 this session and start recording the number of bytes and packets that are sent and 
 received, and then that information as metadata can be put into the Interﬂow to send to the 
 Stellar Cyber platform. When Modular Sensors collect metadata for each network session 
 ﬂow and normalize it into Interﬂow records in JSON format, it looks something like this. 
 Looking at the JSON Interﬂow record excerpt, you can see that there's a source IP, which is 
 normalized SRC IP. There's a destination port 443. There's the number of bytes, which is 
 metadata. There's the App Family, which is metadata. 
 09:00-10:00 
 There's the app ID family, which is metadata, which is web. There's the app path, which is 
 letting you know that it's SSL or HTTPS communication. There's the destination IP and the 
 app ID name. There's a lot more information that goes along with this as well, but this is 
 ADM-03-01-224  52 


---

<!-- Página 53 -->

 what gets sent to the Stellar Cyber platform. To conﬁgure network traffic analysis, in the 
 Modular Sensor proﬁle assigned to the Modular Sensor, turning on network traffic enables 
 the Modular Sensor to form network traffic analysis, which again is essential for network 
 detection and response. After completing your conﬁguration settings in the sensor proﬁle, 
 the  Submit  button must be selected to apply the conﬁguration  settings to the Modular 
 Sensor. Note there are a lot of options available under  Network Traffic  . 
 10:00-10:25 
 These are usually left as default. Go ahead and click  Submit  , and then you should see, 
 “Sensor proﬁle was edited successfully.” 
 This lesson is complete. Thank you for watching. 
 L14B-DEMO: Modular Sensor Network Traffic Analysis (19m:01s) 
 00:00-01:00 
 This lesson continues with demonstrations for Network Traffic Analysis Details and 
 Conﬁguration. This lesson is a demonstration that shows how to conﬁgure Modular Sensors 
 to collect network traffic off SPAN ports or TAP devices and provides details of how the 
 Modular Sensor analyzes network traffic to create sessions and metadata and forward it as 
 Interﬂow records to the Stellar Cyber Open XDR platform. 
 Now I will show you some in-depth analysis that's being performed by the Stellar Cyber 
 Modular Sensors. As an administrator of the Stellar Cyber Open XDR platform, I have SSH 
 and console access to the Modular Sensor. 
 01:00-02:00 
 SOC analysts never need to go to the Modular Sensor itself to look at the data because it's 
 all in the Stellar Cyber platform that you see here. But I think for learning right now and 
 getting a better idea of how the sensor works, I will SSH to the Modular Sensor to get a 
 command-line interface so you can see exactly what's happening on the Modular Sensor 
 itself. I have a terminal window on my MacBook. I will type in  ifconfig  ,  which is interface 
 conﬁg, and look for en0. In the terminal window now I can see that my IP address of my 
 MacBook is 10.20.1.112. Again, going back to my Modular Sensor that's 10.20.1.15. 
 02:00-03:00 
 We're on the same subnet. I will now SSH to my Modular Sensor. To do that, you have to 
 have the username, which is Aella in this case. That is the default username, and I go to 
 10.20.1.15. I'll enter my secret password and I am in. I can type in  show interface  as an 
 example. Here I can see that the IP address of my Modular Sensor’s management interface 
 is 10.20.1.15. Ethernet0 connects to my switch for management purposes. Ethernet1 on the 
 ADM-03-01-224  53 


---

<!-- Página 54 -->

 Modular Sensor connects to the switch SPAN port. Alright. Now I will type in  show question 
 mark  as an example. 
 03:00-04:00 
 This gives you an idea of the commands that you can type in. We have some other 
 commands we'll be using:  show session  . We'll also  be using  show dpi  , which is the deep 
 packet inspection information. This shows you all the applications. Later on we'll do some or 
 I think but previously we showed  show logforwarder  .  That was a very useful command. 
 So  show dpi  gives you an idea of the applications  that the Stellar Cyber and Modular 
 Sensor can identify. Stellar Cyber can identify thousands of applications; I think over 3,800 
 or 4,000 applications that we can identify on the Modular Sensor. Some examples I can 
 show you. Here's one like on my phone if I was running Apple News, I could see that. 
 04:00-05:00 
 I can look for oops, let me try that again. Command f. Look for Zoom. If I was running a 
 Zoom call, I could see 2928 is the application ID for Zoom. Another thing that we can look at 
 is I'll be using AWS console. AWS console has an application ID of 3574. Once we identify the 
 application, we'll correlate it with an application ID. That'll be used so that we can track 
 what's going on. But if I scroll to the top of this list here Let me put it this way. We have this. 
 Let me go all the way down to the top of this list here. You'll see that there are lots and lots 
 and lots of applications. 
 05:00-06:00 
 Okay. Now we see the application ID, the app name, and the app category. For example, 
 you can see Bittorrent would be 15. There is VMware itself. I just saw that appear. VMware is 
 220. Alright. There's Yahoo. There's Google, Google Maps, everything. Most of the common 
 applications in the world you will see here. Again, AWS console is 3574. What does that mean 
 and why do I care? Well, let's take a look. I'll go to AWS console. 
 06:00-07:00 
 I'll look around. Now these are all TCP sessions for a web app, so they're not persistent. You 
 will have to be quick to view them in the Stellar Cyber Modular Sensor. I have another 
 terminal window open. I'm doing this so that I can show you the sessions on one tab and 
 then show you the DPI on the other tab. Let's take a look here. I will also open up a 
 connection. There we go. To the same Modular Sensor. Alright. On this one I will type in  show 
 session  . Okay. But what I'll do now, as I told you  these sessions are short lived. Here we go. 
 Let me go back in. The sessions are short lived, so I need to make sure I capture it right 
 away. 
 07:00-08:00 
 ADM-03-01-224  54 


---

<!-- Página 55 -->

 Then if I do a  show session  let's see if we can ﬁnd it. There it is. There's the 5-tuple and 
 lots of other information as well. Here I see application ID 3574 from my Mac 10.20.1.112. My 
 source port going to 13.248.199.77, which is the AWS console on 443. This is just HTTPS with 
 TCP, right? But we're able to identify that it’s not just HTTPS. It is HTTPS that is AWS console 
 3574 and that could mean different things when correlating and looking for Alerts or 
 identifying Alerts. We also see the number of packets being sent, the number of bytes being 
 sent 
 08:00-09:00 
 the number of packets received, and the number of bytes received. Alright. Again, we can 
 identify lots of things in applications. I had multiple connections to AWS console, but also 
 AWS does some round robining and it takes me to other IP addresses as well. You'll see that 
 there are multiple connections out from my Mac to AWS. Next, another thing I could look at 
 is Zoom. Let me end. There's been no communication on this, so let me see if I can start a 
 new Zoom session. Here we go. I'm starting a meeting right now. Let's do a  show session  . 
 09:00-10:00 
 Okay. I see 2928. I'm not sure if that's it. We'll ﬁnd out. If I do it 2928. There it is, right there. 
 Zoom: 2928. I see that yes, I had a connection going out from my Mac source port 52467. 
 Again, source ports are what are called ephemeral. They are made up. They're above 1024 
 and less than 65535. Then this is going to Zoom 170.114.52.6. Again, on 443. AWS was on 443. 
 This is on port 443. Again, because it's all HTTPS communication, and being able to identify 
 the application is key. 
 10:00-11:00 
 Then again I see the packets out. The packet or the bytes set, the packets received, and the 
 bytes received so far. Some pretty cool stuff happening on the Modular Sensors. Let's go 
 ahead and take a look here. We see this connection is 170.114.52.6. On the command line of 
 the sensor itself, you can do a shell command. In other words, I can run some commands 
 that would ordinarily be in Linux. For example, there's a command called Dig. Dig let’s me 
 ﬁnd that it does a host name to IP address lookup, a DNS lookup essentially. So dig:  shell 
 dig  , and I'll say  zoom.com  . 
 11:00-12:00 
 Here we see zoom is 170.114.0.12. But again, they round robin as well. If I take a look here 
 you'll see it's a different IP address, but it starts off the same. It looks like they have this 
 subnet here 170.114 or at least some of that subnet. Alright. It gives you an idea of what's 
 going on but the shell dig command can be very useful. Okay. Now let's go back on to the 
 Modular Sensor, but see it from the perspective of network traffic analysis. I can go to 
 ADM-03-01-224  55 


---

<!-- Página 56 -->

 Investigate | Threat Hunting  . I'm not going to look for an Alert right now. Let's look just for 
 the traffic itself. For the traffic, let's see what we can ﬁnd. There we go. 
 12:00-13:00 
 Already, right off the bat there's some of my AWS console. 10.20.1.112 to 3.136.230.111. Right? If 
 I were to look through that list one of the IP addresses would be 10 or 3.136. I go do I have 
 any other AWS console? I can type an AWS console from the top search bar. Sure enough, 
 here's the AWS console. You notice that it goes to a lot of different destinations from my 
 source IP to many destination IPs because it turns out Amazon is quite big. They have a lot 
 of IP addresses. A lot of the world runs on AWS. Alright. Some of the other things–remember 
 I had Zoom before so let's look at Zoom. 
 13:00-14:00 
 See all the Zoom sessions that I had. Here I can see that my source IP 10.20.1.112 went to this 
 destination IP and port 443, which is the app Zoom. But there's been other connections as 
 well because the Zoom app is doing other other things as well. Okay. There's the AI and a 
 whole bunch of other modules within Zoom. Remember that on the Modular Sensor itself. 
 Again, Zoom is 2928. Then if I look at the session table for 2928 as an example, we see the 
 source IP, the source port, and the destination IP, and the destination port in this example. 
 The number of bytes transmitted. 
 14:00-15:00 
 Again, the fact that we are recording the number of bytes I don't need to send every single 
 packet to the Stellar Cyber platform. I only send a summary of the metadata, which 
 contains the 5-tuple and the application ID, but the packet sent, and the out bytes sent, and 
 the packets received and so forth. Alright? That's really cool. But again that's not a lot of 
 information. Let’s take a look now at one of these on the platform and open up an Interﬂow 
 record. Now looking at the Interﬂow record, and I click on  Details  or click  JSON  –don't forget 
 everything's in JSON formatted Interﬂow records–you'll see there's a lot more information in 
 here. For example, the dstip_geo. This is called enrichment. 
 15:00-16:00 
 We are enriching the Interﬂow record that came from the Modular Sensor to the  Traffic 
 index. Now we can see the dst geo. This one doesn't actually show the city, but I know it's in 
 the United States. Right? It also gives a latitude line and a longitude line so I can pinpoint 
 where it is on the map. The other thing I have is the source geo (srcip_geo). Sunnyvale. This 
 is where the lab exists where my Modular Sensor exists and where the communication is 
 starting from. Alright. Again, we have the app ID name Zoom. The ﬁeld name is app ID 
 underscore name, and the application is Zoom. I see the number of out bytes that were 
 ADM-03-01-224  56 


---

<!-- Página 57 -->

 sent. Another really cool thing is dst IP reputation. We're using what's called threat intel and 
 we are identifying whether or not the destination IP is from a good source. 
 16:00-17:00 
 Is it Bittorrent? Is it a brute forcer? Do they have a good reputation? In this case yes, it turns 
 out that Zoom does have a good reputation. Okay. That's all called enrichment. We see a lot 
 of data coming in. I actually see the origin, so we actually add that as well. When you're 
 looking around you could see where that came from. We are adding the host as well for the 
 communication. There's a lot of really detailed information that could be used especially for 
 the correlation with other records within the system. I could do the same thing for the AWS 
 console. Right? Now I know that by the way, I could type in  appid_name:AWS_console  , 
 right? 
 17:00-18:00 
 Because I found the ﬁeld name when looking at the Interﬂow record. Searches are ﬁeld 
 name and ﬁeld value. Take a look right here. Again, these are the AWS consoles from my 
 source IP. If I take a look here at a record, I'll go to the JSON and there again I see the 
 source IP, which is my MacBook. The destination IP geo is the geolocation of that IP address 
 for the destination. If I scroll down further, I see that it is Interﬂow traffic, the destination IP 
 geo, the destination IP reputation is good. That's deﬁnitely what you want to see. If I scroll 
 further down, we have a lot of information that gets added 
 18:00-19:01 
 to make it easier to identify and correlate this information with other as well. The source IP 
 geo, which is my lab environment, it's also good so that's also a good sign. Again, what 
 comes from the Modular Sensor is the 5-tuple. Source IP, destination IP, source port, 
 destination port, and protocol. Then Stellar Cyber is able to use threat intel, DNS lookups, 
 geolocation, and a lot of other information that you'll see here within the record to ﬁll it in to 
 give it more context. When you're using it in identifying threats, you have a lot more context 
 to use. Pretty cool stuff. Alright. I will stop there. 
 This lesson is complete. Thank you for watching. 
 L15 - NETWORK DETECTION AND RESPONSE (NDR) 
 L15A-PRES: Network Detection and Response (NDR) in the Stellar 
 Cyber Platform (06m:45s) 
 00:00-01:00 
 ADM-03-01-224  57 


---

<!-- Página 58 -->

 The next lesson is  Network Detection and Response (NDR) in the Stellar Cyber Platform  . 
 This lesson,  Network Detection and Response (NDR) in the Stellar Cyber Platform,  explains 
 some key concepts of how data collected from Modular Sensors in the Stellar Cyber 
 platform is analyzed and utilized. 
 Hi everyone. In this lesson, I will cover some of the capabilities of network detection and 
 response, also known as NDR, in the Stellar Cyber platform. On the Stellar Cyber platform 
 traffic metadata from Modular Sensors arrives as Interﬂow records and is stored in the 
 Traffic  index within the Stellar Cyber Data Lake. 
 01:00-02:00 
 Remember from previous lessons, that Modular Sensors can perform deep packet 
 inspection to determine the application, create network session ﬂows, and report that as 
 Interﬂow to the Stellar Cyber platform. The traffic Interﬂow records are visible on the Stellar 
 Cyber platform by selecting  Investigate  then  Threat  Hunting  . You then select the  Traffic 
 indices where it says indices as step number two. For step number three, you can ﬁlter on, 
 for example, aws_console. That was the application found with the deep packet inspection. 
 You can then scroll down on the page to view the Interﬂow records, called documents, by 
 expanding an individual entry in the list. 
 02:00-03:00 
 To view the details of the Interﬂow record, for the traffic to the AWS console, select an 
 Interﬂow record entry, also again known as a document, from the list. Under the  Actions 
 column on the right-hand side, select the little  i  for more info. More info gives the ability to 
 view key ﬁelds, details, Interﬂow in JSON format, and perform actions. As shown in step 
 number three, select  Details  to view Interﬂow record  ﬁeld names and values, including the 
 enrichment performed by the Stellar Cyber platforms such as the geolocation, host names, 
 threat intel, reputation, desktop IP, type, duration, and much more. Again, this enrichment is 
 really helpful for identifying threats. 
 03:00-04:00 
 For step number four, the Interﬂow record can be viewed in JSON format by selecting 
 JSON, or J-S-O-N. JSON, or JavaScript object notation, is a lightweight data interchange 
 format that is easy for humans to read and write and easy for machines to parse and 
 generate. It's a perfect format for analyzing data and using data with the machine learning 
 and rule-based algorithms on the Stellar Cyber platform. In step number ﬁve,  Key Fields 
 provide essential details that are crucial for understanding and analyzing the data that are 
 all visible by selecting  Key Fields  . 
 04:00-05:00 
 ADM-03-01-224  58 


---

<!-- Página 59 -->

 Number six,  Actions  provide the ability for a SOC analyst to mitigate threats by initiating 
 response actions with integrations to security infrastructure and identity tools by selecting 
 Actions  . The list of actions available, as you see  in number seven, is based on services and 
 Connectors conﬁgured within the Stellar Cyber platform, such as block an IP on a ﬁrewall or 
 a security switch, disable a user in Active Directory, or contain a host with an EDR, which is 
 an endpoint detection response platform, and there's so much more. You can run scripts, 
 send Slack messages, and trigger an email. Again, the response actions are incredibly 
 valuable, especially when trying to mitigate threats and inform people of threats as well. 
 05:00-06:00 
 Another key component for network detection and response on the Stellar Cyber platform 
 is the automation. On step number one, if you go to the  Respond  menu on the top menu 
 bar, then select  Automation  , you can create an automated  threat hunting, or ATH, playbook 
 that can be conﬁgured to automate response actions based on conditions learned from 
 network traffic analysis. The response actions, or ATH playbooks, can also be run manually 
 by SOC analysts. When a condition is met, for example, an NDR threat is detected, you can 
 trigger an email, send a Slack, create a webhook responder. You can block an IP on a 
 ﬁrewall or security switch, you can create an Alert. 
 06:00-06:45 
 You can disable a user, such as with an IDP, as Active Directory or Azure. You can run a 
 script of your choice. Again, these are all things that can be scheduled automatically when a 
 triggered condition is met or you can have a SOC analyst run one of these ATH playbooks if 
 they see, for example, the Alert get created. Thank you for watching. 
 This lesson is complete. Thank you for watching. 
 L16 - OPTIMIZING NETWORK TRAFFIC INGESTION 
 L16A-PRES: Optimizing Network Traffic Ingestion (04m:30s) 
 00:00-01:00 
 The next lesson is  Optimizing Network Traffic Ingestion  .  This lesson,  Optimizing Network 
 Traffic Ingestion,  provides explanations and conﬁguration  examples to optimize ingestion of 
 network traffic by excluding network applications and services that are not essential to 
 ingest on the Stellar Cyber platform. 
 In this lesson, I will cover optimizing network traffic ingestion. Why is optimizing network 
 traffic ingestion important? The following requests from Stellar Cyber partners and 
 customers give good examples of why optimizing network traffic congestion is important. 
 ADM-03-01-224  59 


---

<!-- Página 60 -->

 One customer wrote, “I need to bring down the ingestion to be in compliance with the 
 license limit of Stellar Cyber.” 
 01:00-02:00 
 Others wrote, “We want to reduce data ingestion to have room for a longer period of log 
 retention.” This could be for compliance reasons. “We are only interested in a small portion 
 of the tenant's network traffic. The rest can be discarded.” “A certain forwarded log event is 
 not relevant to our security posture, but is a high portion of our overall log volume. For 
 example, ﬁrewall deny actions. If the ﬁrewall is actually doing the job of protecting the 
 network, why do I need to send that to the Stellar Cyber platform for analysis?” in their case. 
 There are some organizations that might want to see the ﬁrewall deny actions, but you 
 have a choice on what you can ingest. 
 02:00-03:00 
 In the Modular Sensor proﬁle, network traffic application metadata settings have been set 
 by default to optimize the amount of network traffic ingested. You can optimize data 
 ingestion further by setting the  Collection Scope  to exclude certain applications or only 
 collect certain applications. For example, select  Exclude certain applications  and an option 
 to exclude the following applications or application groups appears. Select inside the box to 
 get a search box with a list of applications and application groups. In the search box, by 
 typing the name of an application or application group, the list narrows. In this case, I've 
 typed in YouTube. 
 03:00-04:00 
 Here we see some of the applications: YouTube, YouTube_HD, YouTube Kids, and YouTube 
 music. You can select applications and application groups by selecting the check box next to 
 the application or application group name. Select outside the pop-up box to close it. By 
 excluding applications or application groups, these selections are added as traffic ﬁlters to 
 the Modular Sensor. In this case, I am excluding YouTube traffic and speed test traffic. 
 Packets that match the applications or application groups within the traffic ﬁlter are 
 discarded. In this case, the Modular Sensor will discard all YouTube traffic and all speed test 
 traffic. Modular Sensors will not create or report Interﬂow records for the excluded 
 applications to the Stellar Cyber platform. 
 04:00-04:30 
 Once you have selected the applications or application groups, select  Submit  at the bottom 
 of the Stellar Cyber Modular Sensor proﬁle to save and apply the settings to the Modular 
 Sensors assigned to this Modular Sensor proﬁle. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  60 


---

<!-- Página 61 -->

 L17 - EXAMPLE OF OPTIMIZING NETWORK TRAFFIC 
 INGESTION 
 L17A-PRES: Example of Optimizing Network Traffic Ingestion 
 (09m:08s) 
 00:00-01:00 
 The next lesson is  Example for Optimizing Network  Traffic Congestion  . This lesson,  Example 
 for Optimizing Network Traffic Ingestion,  gives an  end-to-end example of conﬁguring traffic 
 ﬁlters to exclude Modular Sensor conﬁguration management and ingestion communication 
 to the Stellar Cyber Open XDR platform from being ingested by the platform. 
 In this lesson, I will give an example of optimizing network traffic ingestion. One, we can ﬁlter 
 sensor communication to the Stellar Cyber platform. In most cases, this data is irrelevant 
 and should be ﬁltered. 
 01:00-02:00 
 This not only applies to Modular Sensors, but it also applies to Windows Server sensors and 
 Linux Server sensors as well. For example, you can ﬁlter the Modular Sensor IP that opens a 
 conﬁguration and management connection to the Stellar Cyber platform Data Lake. This 
 connection uses TCP port 6640-6648. It also opens up a connection to the Stellar Cyber 
 platform Data Lake on port 8443 for downloading software updates. The Modular Sensor IP 
 also communicates to the Stellar Cyber platform for data ingestion on port 8889 to the 
 Stellar Cyber platform Data Analyzer. You can also ﬁlter log sources to the sensor, which is 
 the traffic mirrored to the Modular Sensor. 
 02:00-03:00 
 For example, Fortinet sends logs to the sensor port 5517. The sensor log forwarder 
 processes the logs and the packets to 5517 are also mirrored to the sensor. The mirror traffic 
 in this case can be ﬁltered. Here's an example: When conﬁguring the traffic ﬁltering, it is 
 helpful to have a network diagram. In this case, I have Stellar Cyber sensors on the 10.20.10 
 subnet. I have Modular Sensors on that subnet, Windows Server sensors on that subnet and 
 Linux Server sensors. Each of these opens up a conﬁguration management connection to 
 the Stellar Cyber Open XDR platform using TCP ports 6640 to 6648 over TLS to the Data 
 Lake. 
 03:00-04:00 
 ADM-03-01-224  61 


---

<!-- Página 62 -->

 Again, this is for on-premises or cloud deployments. For SaaS, this would only be port 443. 
 Stellar Cyber sensors also open a connection for Interﬂow ingestion using TCP port 8889 
 over TLS to the Data Analyzer IP on the Stellar Cyber Open XDR platform. To optimize the 
 traffic, for on-premises or cloud Stellar Cyber platform deployments, you can create a 
 custom application for Stellar Cyber platform communication from sensors to the Data 
 Lake for conﬁguration management, and also create a custom application for Stellar Cyber 
 platform communication from sensors to the Data Analyzer for Interﬂow ingestion. 
 04:00-05:00 
 Using the last diagram as a reference, for this example, I will create a custom application in 
 traffic ﬁlters for the Modular Sensor communication to the Stellar Cyber platform Data 
 Analyzer for data ingestion. For example, the Data Analyzer I am using has an IP address of 
 192.168.1.150/32. What is slash 32? That is the netmask. Slash 32 says that I care about every 
 single bit in this IP address. In other words, the complete IP address. Sometimes you'll see 
 /24. What that means is the 192.168.1.0. We want to make sure that this is /32 to ensure that 
 we are identically matching this IP address. The ports that are used are TCP 6640 to TCP 
 6648. 
 05:00-06:00 
 Here on step number one I will go to  System | Traffic  Filters  .  At the top there are two tabs, 
 Custom Applications  and  Application Groups  . In this  example, separate traffic ﬁlters will be 
 created for each IP address and port combination to be ﬁltered. For step number one, I'll 
 select  Custom Applications  . For step number two, I'll  put an application name in. Now I like 
 to make sure that this is easy to understand and easy to recognize because if you make a 
 mistake or type in a different name, it might be harder to realize what you are ﬁltering in the 
 traffic. In this case, I'll use the tenant name. I'll use the word “sensor” to say this is sensor 
 communication. 
 06:00-07:00 
 DA is saying that traffic is going to the Data Analyzer, and the port number is the port that 
 I'm actually ﬁltering. In this case, I'm using Customer_one, which is the tenant name dash 
 sensor dash DA, dash 6640. Next, since I have a customer called Customer_One, for the 
 tenant, I will select Customer_One because that's where these sensors are deployed. Now if 
 the sensors are for my own network, I would just say the root tenant unless I have a tenant 
 speciﬁed. Next, I will say Matched on Protocol. I will select TCP. For number ﬁve, I'll enable 
 Match on Source, and I'll enter the IP address or subnet that contains the sensors. 
 07:00-08:00 
 In this example I could use a single IP of 10.20.1.15/32, which is my Modular Sensor. But I have 
 other sensors as well on my Linux Servers and on my Windows Servers that are on the 
 ADM-03-01-224  62 


---

<!-- Página 63 -->

 same subnet. I can say 10.20.1.0/24, which covers the entire subnet. Next, I will enable 
 Matched on Destination  . For on-premises and cloud  deployments, I could enter the IP 
 address of the Stellar Cyber platform Data Analyzer. As an example, in my lab I have 
 192.168.1.150, and I'm entering /32 to say that speciﬁc IP address. If I used /24, it would say 
 the entire 192.160.1.0 subnet, which I don't want in this case. 
 08:00-09:07 
 Here I'll enter the TCP port example 6640. Now I can select  Submit  . I will do this for each of 
 the ports and combinations of subnets. I select  Create  to create additional traffic ﬁlters. 
 Note traffic ﬁlters are not applied until they are assigned to the sensor proﬁle in the 
 application metadata section. When done, as an example, I have created these 12 traffic 
 ﬁlters. If we take a look, I have Customer_One-Sensor-DA-6640, same as 6641, all the way to 
 6648. Then also ﬁltering out 8443, which is the software downloaded to the Data Lake, and 
 8889 as well for the conﬁguration and management connection. 
 This lesson is complete. Thank you for watching. 
 L17B-DEMO: Example of Optimizing Network Traffic Ingestion 
 (27m:07s) 
 00:00-01:00 
 This lesson continues with demonstrations for optimizing network traffic congestion. This 
 lesson is a demonstration that provides explanations and conﬁguration examples to 
 optimize ingestion of network traffic by excluding network applications and services that 
 are not essential to ingest on the Stellar Cyber platform. 
 Hi everyone. In this example, I'm going to provide a demonstration of how to create traffic 
 ﬁlters so that I can optimize the ingestion of traffic into the Stellar Cyber Modular Sensors, 
 which then would get forwarded to the Stellar Cyber platform. 
 01:00-02:00 
 If it's traffic that I don't need to analyze on the Stellar Cyber platform, then I can ﬁlter it out 
 so that I don't cause unwanted ingestion. To begin, I will take a look at the sensor proﬁle I 
 am actually using to see what I have conﬁgured. I can go to  System | Sensor Proﬁles  . The 
 Modular Sensor proﬁle I'm using is the SC Modular Sensor IDS. I can click the pencil to edit. If 
 I scroll down to create a traffic ﬁlter I have the ability to select the ﬁeld here. I can select 
 Network Traffic  and scroll down to  Application Metadata  .  If I expand  Application 
 Metadata  , I see that I have a  Collection Scope  of  All applications  . 
 02:00-03:00 
 ADM-03-01-224  63 


---

<!-- Página 64 -->

 If I want to exclude certain applications, I click the radio button there. Then from here I can 
 choose an application. Now, by default, Stellar Cyber has a lot of applications and 
 application groups built in. For example, there's YouTube. If I type in YouTube, I can see that 
 YouTube is here. If I don't want the Modular Sensors to look at YouTube traffic or capture 
 YouTube traffic, and send that information as Interﬂow records to this Stellar Cyber 
 platform, I can create a ﬁlter, as I did right here, for YouTube. Now the way this selection box 
 works I click into the box. I get a selection window, and then I click out of the box, and then 
 whatever I have selected goes here. 
 03:00-04:00 
 I don't have any custom applications right now. I'm going to leave this Modular Sensor 
 proﬁle and create a traffic ﬁlter of my own. From  System  , I go to  Traffic Filters  . I have no 
 traffic ﬁlters to ﬁnd. But if I look at  Application  Groups  , there are lots of applications 
 available. What I'm seeing here are the application group categories. If I wanted to ﬁnd 
 YouTube, for example, I can go to mm–I think it's mm_streaming, yes multimedia streaming. 
 If I select the hamburger icon here I can say auto-size all columns, and in this list of 
 multimedia streaming apps is YouTube, as an example. 
 04:00-05:00 
 If I block the whole category from being ingested, or if I ﬁlter based on this category not 
 blocked again, we're not blocking any traffic. I'm just ﬁltering traffic that I'm going to ingest 
 and send to the Stellar Cyber platform. But in this case, I'm going to remove the ﬁlter, go 
 back to  Custom Applications  , and create a traffic  ﬁlter or a set of traffic ﬁlters to ﬁlter the 
 ingestion of the Stellar Cyber communication for the Modular Sensors to the Stellar Cyber 
 platform. Again, this is information that does not need to be analyzed by the Stellar Cyber 
 platform. To begin, I can create an application. The application name–again what I want to 
 do is make sure that I can recognize the application. 
 05:00-06:00 
 I'm going to apply this application to all my tenants. I will actually call it All_Tenants. This is 
 communication from my sensor to the Stellar Cyber platform Data Lake. For the 
 conﬁguration management connection, this is TCP port 6640. I'm going to match based on 
 TCP. Now here's where I could decide to be more speciﬁc or less speciﬁc. If I say  Matched 
 on Source  , which I'll do in this example, I will match  on the subnet that contains my Modular 
 Sensor, my Windows Server sensor, and my Linux Server sensors. 
 06:00-07:00 
 I'll type in 10.20.1.0/24. I am saying any communication from the 10.20.1.0/24 subnet matches 
 this rule. But then it also has to match the destination. As I mentioned before, this is the 
 communication from the sensors to the Stellar Cyber platform Data Lake because this is an 
 ADM-03-01-224  64 


---

<!-- Página 65 -->

 on-premises deployment. If this is a SaaS deployment, then I would just use the IP address 
 of the Stellar Cyber platform. I will use 192.168.1.175, which is the IP address of my Data Lake. 
 Now here's where people can make mistakes. This is /32. 
 07:00-08:00 
 Each of these–these are called octets that are separated by the dotted notation–is eight 
 bits. This is eight bits. This is eight bits, so that's sixteen. This is eight bits, so that's 24. If I say 
 another eight bits, that's 32. If I were to put /24, then I would essentially be saying–and I'll 
 scroll this up a little bit so you can see it better–essentially I'd be saying I will apply this rule 
 from anything in this subnet 10.20.1.0 to anything in the 192.168.1., essentially 1.0/24. I want to 
 actually ensure that it's only to my Data Lake. I need to use /32. 
 08:00-09:00 
 Next, I'll put in the port, which is 6640. Click off anywhere other than the selection box, and 
 now the  Submit  button appears. I can now auto-size  all the columns. Now I see a clearly 
 deﬁned rule. It's for all tenants. It's for the sensor talking to the DL, on port 6640 from a 
 source subnet of 10.20.1.0 to a destination IP of 192.168.1.175 on port 6640 with TCP and all 
 tenants. Alright. I need to do this a few more times. To do it again, I will add another [selects 
 the  Create  button] and do essentially the same thing. 
 09:00-10:00 
 The application name is going to be All_ Tenants_sensor to Data Lake on port 6641. Now, I 
 will then do the same thing 4642, 43, 44, 45, 46, 47, 48. I'll apply this to all tenants. If at a 
 speciﬁc customer environment and they're in their own tenant, I could create a ﬁlter just for 
 their speciﬁc tenant. For example, here I have Customer_One and Customer_Two. I'm going 
 to Matched on Protocol TCP. I will match on source 10.20.1.0/24. I'll Matched on Destination 
 192.168.1.175 again /32. 
 10:00-11:00 
 The port will be 6641. Now, if I were to turn off  Matched on Source  , I could make my life a 
 little easier. I can essentially say any communication to the Stellar Cyber Data Lake that's 
 using 6640, 6641, 6642 will match this rule. In reality, that's probably what I'd do in most 
 situations. But what I want to show is that it is being more exact. For this, I will use the 
 10.20.1.0/24 because that's where all my sensors are anyway. Alright. I'll submit that. 
 11:00-12:00 
 I will continue on. I'll do just one more, so it's really locked in. I'll go back to  Application 
 Name  . Again, this is All_Tenants-Sensor-Data Lake-6642  and make that TCP, and Matched 
 on Source 10.20.1.0/24. The Data Lake IP is 192.168.1.175. The port, in this case is 6642. So six 
 six four zero, six six four one, and six six four two. 
 ADM-03-01-224  65 


---

<!-- Página 66 -->

 12:00-13:00 
 I will stop for a minute and put the rest in, but I will make it so that you don't have to watch 
 me doing that. I'll be right back. Voila, I am ﬁnished creating the traffic ﬁlters, or am I? If you 
 look at the custom applications I have now, there's one of these entries that doesn't look like 
 the others. Which one is it? Maybe you saw me make the mistake on the last conﬁguration 
 of a traffic ﬁlter I did before taking a break. Now if we take a look at the destination IP, one 
 of them doesn't have a /32. That's why it's really good also to ﬁlter here or take a look here 
 and see the traffic ﬁlters and see if they're all aligned with each other. 
 13:00-14:00 
 What's really great now is I can just go back and modify this one. Scroll down to the bottom 
 and use /32. Click  Submit  . Now they're all in line  with each other. Next, I will apply these 
 traffic ﬁlters to my Modular Sensor proﬁle. I can go to  System | Sensor Proﬁles  . I'm using 
 the SC Modular Sensor IDS. I will edit this row. Go to  Network Traffic  . Select  Application 
 Metadata  . Now for  Collection Scope  I will exclude  certain applications. 
 14:00-15:00 
 Here now, if I were to start typing in the name, I had all tenants. I have all my tenants DL 
 6640. Again then type in all again, do the next one. Type in all again and do the next one. I'll 
 do that until they're all selected. If it wasn't a custom application, I could actually do this in 
 one swoop here. I'll scroll down. Type in all again until I have them all selected. That's it. Click 
 off. 
 15:00-16:00 
 Now I can see that they're all there and I'll go ahead and click  Submit  . Actually, select 
 Submit  . Alright. Now if I go to my Modular Sensors,  we'll go to  System | Sensors  and we'll 
 see here that the, what does it say? If I go to here, and auto-size all columns, the 
 conﬁguration is out of sync. It's out of sync because I just modiﬁed the proﬁle and actually 
 modiﬁed my Linux Server sensor proﬁle as well. This will take a minute for it to come back. 
 I'll refresh my screen and there it is. It's back. I will also readjust the columns. Now my traffic 
 ﬁlter is applied. 
 16:00-17:00 
 I will no longer see the traffic from my sensors to the Stellar Cyber platform. Okay. Now that 
 my Modular Sensor proﬁle has been updated and assigned to the Stellar Cyber sensor well, 
 ﬁrst of all let me just make sure. I modiﬁed the SC Modular Sensor IDS proﬁle. Let me go to 
 my Modular Sensor just to make sure that that is the proﬁle in use. I am pretty sure it is 
 because it was red a minute ago. Alright. If I were to look at my SC Modular Sensor proﬁle. I 
 look right here, yes the SC Modular Sensor IDS is assigned to my Modular Sensor. 
 ADM-03-01-224  66 


---

<!-- Página 67 -->

 17:00-18:00 
 If I select into it, go to  Network Traffic  , go to  Application Metadata  , I see these applied. 
 Now, I'll close that out. Next, if I go to  Investigate  | Threat Hunting  I can actually see where, 
 or how much traffic is coming from the 6640 to 6648 ports. To begin with, I will select all 
 indices because I don't know which indices contain the communication from the Stellar 
 Cyber Modular Sensors to the Stellar Cyber platform. Now that I've selected all indices, I will 
 search for a destination port. In Lucene queries syntax is dstport:, and I'm going to use a 
 range. 
 18:00-19:00 
 For a range I use a square bracket. I have a space or no space. It's your choice. I'll put a 
 square bracket and I will say 6640. Capital T-O is a range to 6648. Close the square bracket, 
 hit  Return  . Now I see that I have a legend called  interﬂow_traffic  . Well who would have 
 thought? If I look at Interﬂow traffic here and I ﬁlter for that, and look down here, I can see 
 that, yes, I had my Linux Server sensors and scroll up here and my Modular Sensor all using 
 those ports. The application that it did see. 
 19:00-20:00 
 Let me click on this, and go to  Details  . Here I can  look through and ﬁnd, ﬁrst of all DST port. 
 DST port is 6640. The destination IP host is 192.168.1.175, which is my Data Lake IP address. 
 The source IP, if I scroll down these are in alphabetical order, is 10.20.1.15. If I look at the time 
 this came in, which is at the top here, this came in on April 3rd at 4:17 PM, which is 16:17. I 
 should not receive any more of these messages. Look over here and see the same thing: 
 16:17. 
 20:00-21:00 
 The rest are my Linux Server. The Linux Server is using a different policy. Therefore, the 
 messages are still coming in, at 16:57 is the last one. Okay. Now that we have all the 
 conﬁguration management connections being ﬁltered, the next thing I will do is create two 
 more traffic ﬁlters. I will create the traffic ﬁlter for the ingestion on the Stellar Cyber platform 
 Data Analyzer, or if it's SaaS, the Stellar Cyber platform itself. I'll create a new custom 
 application. Again, I'll give a descriptive name of All_Tenants. 
 21:00-22:00 
 This is for sensors talking to the DA (the Data Analyzer) using port 8889. This will be TCP. I 
 will Matched on Source. The source is 10.20.1.0/24. I will match on the destination, which is 
 the IP address of the on-premises platform Data Analyzer. The 192.168.1.150/32 to match the 
 IP address, and the port is 8889. I can go ahead and submit that. I will create one more to 
 the Data Lake. 
 ADM-03-01-224  67 


---

<!-- Página 68 -->

 22:00-23:00 
 This one will be the All_Tenants again. From the sensor to the Data Lake on port 8443. This 
 is for software that the Modular Sensor downloads or even sensors download to get 
 updates. This will be TCP  Matched on Source  10.20.1.0/24.  See? I wasn't paying attention. 
 This has to 10.20.1.0/24. The port number is 8443. 
 23:00-24:00 
 Again, it's okay to make mistakes. Just make sure you correct them. Of course I did that on 
 purpose. Now I'll go back to my Sensor Proﬁles. Go to  Network Traffic | Application 
 Metadata  . Click in the selection box here or select  in the selection box. I'll type in “all” again 
 to see if I have anything new. I do. I have my DL 8443. Try that again. All and I had all 
 tenants to the DA. Again, I will apply. 
 24:00-25:00 
 As soon as I apply, if I go to my sensors now,  System  | Sensors  .  Yeah. I see that this time, it's 
 only the Modular Sensor. Now, last time I had multiple administrators on the platform. They 
 were both red. That was because actually somebody else was modifying the Linux Server 
 sensor. Always be aware of what you're doing. Right now the conﬁguration is out of sync, 
 but it will come back shortly. There we go. After a quick refresh, it is now all working 
 correctly. If I go to  Investigate | Threat Hunting  ,  let's just take a look. If I select  all  here and 
 look for just let's say, dst port 8443. 
 25:00-26:00 
 Of course this is in the last 24 hours. Nothing was there. If I were to choose a dst port of 
 8889, let's take a look. There's a lot more records there that will be ﬁltered out. What do 
 these look like? This is your TCP 8889. These are from the Modular Sensor to the Data 
 Analyzer, just as we had conﬁgured. This is exactly what we want to ﬁlter out. Now if I scroll 
 down, it's all the traffic ﬂows and the message class is Interﬂow traffic. Seeing this message 
 class Interﬂow traffic, I can actually do this as well. I can go over here. Okay. Now let's see if 
 I see the message_class Interﬂow traffic. 
 26:00-27:10 
 I'll go to MSG_class: Interﬂow traffic. Here I see 1,285,000 records. If I look over here, I have 
 this in  Alerts  and in the  Traffic  index. If I go to  the  Traffic  index, and only select that here. 
 Again, I see one 1,285,000 records. Now let's see what it's been like for the last week. Seven 
 million, eight-hundred thousand and seventy nine records. Okay? Filtering out this traffic 
 isn't a bad thing to do. It’s actually quite good for optimization. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  68 


---

<!-- Página 69 -->

 L18 - INTRUSION DETECTION SYSTEM (IDS) CONFIGURATION 
 L18A-PRES: Intrusion Detection System (IDS) Conﬁguration (07m:53s) 
 00:00-01:00 
 The next lesson is  Intrusion Detection System (IDS)  Details and Conﬁguration.  This lesson, 
 Intrusion Detection System (IDS) Details and Conﬁguration,  provides the explanation and 
 conﬁguration of the IDS module on the Stellar Cyber Modular Sensor. 
 In this lesson, I will cover the Modular Sensor Intrusion Detection System, also known as IDS. 
 Looking at the picture on the left, IDS is built into the Stellar Cyber Modular Sensor. It works 
 in conjunction with the network traffic analysis that we enabled earlier. 
 01:00-02:00 
 After receiving network traffic from SPAN ports or TAP devices, Modular Sensors use a 
 Suricata engine with over 60,000 commercial IDS rules to detect threats within network 
 traffic, which also includes traffic from OT devices, which is operational technology. The 
 Modular Sensors create metadata summaries from IDS data that are normalized into 
 Interﬂow records in JSON format. The Modular Sensor forwards IDS metadata as Interﬂow 
 records to the Stellar Cyber platform. After receiving the IDS metadata or Interﬂow records, 
 the Stellar Cyber platform uses machine learning to reduce the number of events generated 
 by the IDS engine and performs complex analysis and correlation with other data sources to 
 generate Alerts. 
 02:00-03:00 
 To authorize the IDS engine and optionally the APT, which is the Malware Sandbox licenses 
 for the Modular Sensor, you go to  System | Sensors  ,  then step two go to  Manage  and then 
 Authorization  . To authorize the IDS, you ensure that  the modules are selected from the 
 left-hand side. In step number one, there's the  Authorize  menu. If you look to the right of 
 that is the  Unauthorize  . In this case, we want to  authorize. It looks like during the installation 
 process of the Modular Sensor, the authorization of the Modular Sensor was done with the 
 IDS. Well, that's why it's in the right-hand table, but by default, it may not be checked. 
 03:00-04:00 
 As you see here for SC Modular Sensor under  IDS License  ,  I now have it checked. APT 
 license is also checked, which is the Malware Sandbox. Log Forwarder is always checked 
 because it is always enabled by default. Step number three we click  Submit  . After 
 submitting authorization, the sensor status will display the message disconnected and 
 conﬁguration is out of sync. The status will be red. After a few moments, if you refresh the 
 browser, the message will clear and the sensor status will be green. The Modular Sensor 
 ADM-03-01-224  69 


---

<!-- Página 70 -->

 Intrusion Detection System is enabled by editing the Modular Sensor proﬁle and system 
 sensor proﬁles. In the Modular Sensor proﬁle, enable  Network Traffic  in step number one 
 04:00-05:00 
 which is required for capturing network traffic used to apply IDS rules. Step number two, 
 enable IDS. Inside that, it is used for conﬁguring the home and external networks to apply 
 IDS rules and for determining the signatures to apply. Conﬁgure Networks as a policy to 
 determine when IDS rules will be applied. On the right is a picture with an example with IDS 
 networks with a home of private and an external network of public. In step number three, 
 you can select  Private  ,  Public  ,  Any  , or  Speciﬁc  for  the home network. In this case, I will 
 select  Private  . For the external network, you can  also select  Private  ,  Public  ,  Any  , or 
 Speciﬁc  . In this case I will use  Public  . 
 05:00-06:00 
 In other words, the home network is my private network within my organization. The 
 external network is public, which is the internet. Home and external networks can be set to 
 Private  , which is RFC 1918 IP addresses, which are  10.0.0.0/8. In other words 10 dot anything 
 or 172.16.0.0/12, which is actually 172.16.0.0 to 172.31.255.255 and 192.168.0.0/16, which is 
 192.168, anything. Public is all but private RFC 1918 addressing and not multicast IP 
 addresses, which are in the range of 224.0.0.0 to 239.255.255.255.  Any  of course, is all 
 networks. 
 06:00-07:00 
 Speciﬁc  is used to deﬁne custom IP ranges, if there  are speciﬁc networks inside a format, 
 for which to apply IDS rules within your organization. For example, there are some 
 universities that have public IP addresses. But they are really considered internal network 
 addresses for their organization. You could deﬁne speciﬁc IP address subnets to use for 
 your own private networks. An example here, I have IDS networks with a home of  Private 
 with an external network of  Speciﬁc  . The  Speciﬁc  IP in this case is 3.3.0.0/16 and 2.2.1.0/24. 
 You can have multiple entries. 
 07:00-07:55 
 For the IDS conﬁguration you also have the signature. The  Signature  section lets you 
 conﬁgure a list of IDS rule sets. These rules are integrated by Stellar Cyber from third-party 
 threat intelligence. You can choose which rules to use, but you cannot add your own rule set. 
 Again, you select into the box, and you'll get a set of rules to choose from. By default, the 
 rules are there. But if there are additional rules that get added in a new release for an 
 example, you will see them appear in this list. After completing your conﬁguration settings in 
 the sensor proﬁle, the  Submit  button must be selected  to apply the conﬁguration settings to 
 the Modular Sensor. 
 ADM-03-01-224  70 


---

<!-- Página 71 -->

 This lesson is complete. Thank you for watching. 
 L19 - IDS IN THE STELLAR CYBER PLATFORM 
 L19A-PRES: IDS in the Stellar Cyber Platform (07m:05s) 
 00:00-01:00 
 The next lesson is  Intrusion Detection System (IDS)  Stellar Cyber Platform Operations  . This lesson, 
 Intrusion Detection System (IDS) Stellar Cyber Platform Operations  , explains how to view the IDS 
 event data received from Modular Sensors and how the Stellar Cyber Open XDR platform uses 
 machine learning to create actionable Alerts from the IDS events. 
 In this lesson, I will cover the Intrusion Detection System as performed with operations in the Stellar 
 Cyber platform. 
 01:00-02:00 
 Now that the Modular Sensor proﬁle has been applied to the Modular Sensor with the IDS 
 functionality enabled, the Modular Sensor will now apply IDS rules to all the traffic it receives based 
 on the home network and destination network speciﬁed to generate IDS events. To view IDS events 
 that have been received by the Stellar Cyber platform, go to  Visualize  |  ML IDS  , which is a little bit 
 further than midway down the list. Ensure you do not have any ﬁlters set that are not intended. You 
 can expand the  Filters  sidebar and just make sure  you don't have any ﬁlters. Otherwise, you may not 
 get the results you're expecting to see. Set the  Time  Interval  such as the last twenty four hours. You 
 could make it longer if desired. View events and make sure that you scroll down to see them all. 
 02:00-03:00 
 Here we do see that there are ML IDS events. Stellar Cyber Machine Learning is applied to the ideas 
 events from the Modular Sensors to identify threats and create Alerts. In other words, the Modular 
 Sensors themselves use the Suricata engine to identify threats from the Suricata rules. Those get sent 
 to the Stellar Cyber platform. The Stellar Cyber platform then applies machine learning, statistical 
 analysis rules, and heuristic rules to identify threats along with using graph machine learning to 
 correlate Alerts into what are called Cases. In this view we can see that some Alerts have actually 
 been created. 
 03:00-04:00 
 Here we're looking for private-to-private exploit attempt anomalies, private-to-public exploit attempt 
 anomalies, public-to-private exploit attempt anomalies, and public-to-public exploit attempt 
 anomalies. In this situation, I have nine private-to-private exploit attempt anomalies, one 
 private-to-public exploit attempt anomaly, and one public-to-private exploit attempt anomaly. Each 
 of these can be investigated. Under the Alert that I want to investigate or under the Alert type, I'll 
 select  Investigate  . This will take you to the  Alerts  page on the Stellar Cyber platform. In the  Alerts 
 ADM-03-01-224  71 


---

<!-- Página 72 -->

 page, all the charts and Alert records are displayed from the Alert that we are investigating right now, 
 which is the private-to-private exploit attempt anomalies. 
 04:00-05:00 
 If you scroll down, you'll see the actual Interﬂow records that are related to the Alert. The  ML-IDS 
 Events  and related Alerts can also be viewed by going  to  Investigate | Threat Hunting  .  Next to 
 Indices  , select  Alerts  , which is the indices or index  displayed by default. Clear the checkbox next to 
 Alerts  . Select the checkbox for  ML-IDS/Malware Sandbox  Events  . Step number ﬁve, with the 
 ML-IDS/Malware Sandbox Events  indices selected, all  ML-IDS-related charts and events are 
 displayed. Here are a few troubleshooting tips for the Intrusion Detection System on the Modular 
 Sensors. 
 05:00-06:00 
 Let's say you're on the Stellar Cyber platform and there's no IDS data being received. The potential 
 solutions for that are number one, ensure the Modular Sensor is authorized and has the IDS license 
 set to  Authorized  . That's the little check box for  the IDS license. Number two, validate the sensor 
 proﬁle used by the Modular Sensor has IDS enabled. Don't forget that the Modular Sensor could be 
 assigned to a different Modular Sensor proﬁle. Number three, validate the IDS conﬁguration in the 
 Modular Sensor proﬁle has the proper network selected and signature selected. The other thing is 
 validate the maps are appropriate for the networks that you have if you created your own speciﬁc 
 networks. Number four, ensure that the Modular Sensor is receiving traffic from SPAN ports or TAP 
 devices. 
 06:00-07:05 
 This is important because the Modular Sensor needs to receive the network traffic to perform the IDS 
 functionality. Next, on the left-hand side, again another symptom, limited IDS data is being displayed 
 in the Stellar Cyber platform. I'm going to say this one over and over again. Ensure the correct ﬁlters 
 and time ranges are set on the page you are on. If you're on the  Alerts  or  Visualize |  ML IDS  pages, 
 ensure that the time range is set in the upper right. On the left-hand ﬁlter bar, make sure that you are 
 using the ﬁlters you are expecting to see. If you have not set a ﬁlter, make sure you just clear the 
 ﬁlters out. There's a little option to do that. For step number two, from  Investigate | Threat Hunting  , 
 ensure the  ML-IDS  index is set. Okay. That's it for  now. Thank you for watching this lesson. 
 This lesson is complete. Thank you for watching. 
 L19B-DEMO: IDS in the Stellar Cyber Platform (33m:35s) 
 00:00-01:00 
 This lesson continues with demonstrations for  Intrusion  Detection System (IDS) Stellar Cyber Platform 
 Operations  . This demonstration explains the concepts  and conﬁguration of the IDS module on Stellar 
 Cyber Modular Sensors and provides details on investigating IDS events and Alerts in the Stellar 
 Cyber Open XDR platform. 
 ADM-03-01-224  72 


---

<!-- Página 73 -->

 Hi everyone. In this lesson, I will show you how to enable IDS in Modular Sensors. The ﬁrst thing you 
 need to do is go to  System | Sensors  . 
 01:00-02:00 
 The IDS module is a licensed feature and that's available by going to the  Manage | Authorization  . 
 Here in the  Authorize Sensors  page, I can go and take  a look at my Modular Sensor, and I see that I 
 have an IDS license. All I have to do is check the box for  IDS License  to enable it, then go ahead and 
 select  Submit  . Though I've authorized the Modular  Sensor to use the IDS module, it's still not 
 conﬁgured yet. How do I conﬁgure a Modular Sensor to use the IDS module? You guessed it. I have to 
 go and conﬁgure the Modular Sensor proﬁle. To do that I go to  System | Sensor Proﬁles  . The 
 Modular Sensor proﬁle I am using for these examples is SC Modular Sensor New. 
 02:00-03:00 
 I will go ahead and select that now and select the pencil to edit. To use IDS, one of the ﬁrst things you 
 need to do is ensure that you have network traffic being collected as well. The IDS module is 
 applying signatures and rules to look for threats in network traffic. If you are not forwarding network 
 traffic to the Modular Sensor, the IDS module isn't going to do you much good. Here, I do have 
 Network Traffic  enabled. I do have my Modular Sensor  conﬁgured off a SPAN port on my switch. 
 The next thing I need to do is enable  IDS  . Now,  IDS  is enabled, but for what traffic? 
 03:00-04:00 
 Let's take a look. To conﬁgure the traffic, we can look at the networks. The IDS module uses a home 
 network and an external network. What does this mean? Well, in every rule that's used for IDS, there's 
 something that will go from either home to home, or home to external, or external to home. It needs 
 to know which networks you consider home, and which networks are considered external. Now, 
 typically a home network is a private network. It is RFC 1918, which is my 10.0.0.0/8 CIDR block, which 
 is 10.0.0.0 to 10.255.255.255. 
 04:00-05:00 
 It's also 172.16.0.0/12 to 172.31.255.255. There's also the 192.168.0.0/16, which is the 192.168.0.0 to 
 192.168.255.255. Next, what is the external network? The external network is using a public IP address. 
 Public addresses are, number one, not private. Everything that's not RFC 1918 and not multicast. 
 Multicast is the 224.0.0.0 to 239.255.255. With that in mind now, the rules will say, look for a threat in 
 the home network to the external network. 
 05:00-06:00 
 Or look for a threat in home to home or look for a threat in external to home. Now private to public 
 does not apply to everyone. In some organizations or even universities the private network actually 
 might be a public IP address. They're assigned a certain range of public IP addresses. They're trusted 
 home network contains public IPs. If that's the case, you can actually change what a home network 
 applies to. You could say the home network applies to  Any  but then you'd be looking at all traffic.  You 
 can specify  Speciﬁc  . Now for  Speciﬁc  , you can enter  IP range in the form of CIDR notation. I can 
 select  plus  . Now let's say my organization uses the  2.2.0.0/16 network. 
 ADM-03-01-224  73 


---

<!-- Página 74 -->

 06:00-07:00 
 Now I could say anything that is from 2.2.0.0 to  2.2.255.255  is essentially my home-to-home network. 
 Or I can say my home to public is the 2.2.0.0/16 to public, which is everything else. We give you the 
 ability to specify what your home network is. Okay. I also have the ability to specify additional IP 
 ranges. Again, in the form of CIDR notation. I might have a 2.3.0.0/16. I might have a 2.4.1.0/24. 
 07:00-08:00 
 I might even have a 3.1.1.0/24. Alright. You can have multiple IP CIDR blocks that are used to identify 
 your home network. But in most cases, I'll clear all these. It's usually going to be  Public  . So excuse  me. 
 In most cases, it's going to be a  Private  as my home  network to an external of  Public  . Now, if you 
 really want to see how this works, I think one of the best ways is to actually look at a Suricata engine 
 rule. I have one here. One of the best ways to understand this concept is to actually take a look at a 
 Suricata engine rule. 
 08:00-09:00 
 I have a few lined up here. In my trusty text editor, I have copied a few Suricata rules for us to take a 
 look at. if we take a look at the ﬁrst one, you'll see that the rule has a variable saying look for home 
 network to external network. In this case, it would be a private IP address to a public IP address. This 
 one I can say if a packet has an external IP address, which is a public IP address to the internal IP 
 address, which is my private network, then this is an external to home. If I look over here again, I have 
 a rule that shows a home network to home network. That's a private to private. This will make more 
 sense even when I take a look at the ML-IDS in the Stellar Cyber user interface. 
 09:00-10:00 
 In the conﬁguration of the IDS, you can also take a look at the signatures that are being used. These 
 are the Suricata rules. Go to  Signature  . I can look  at the selected rules. By default, we have selected 
 most of the rules that apply to most organizations. If I scroll through here I can see the rules. If you 
 want to check and see if there are other rules available, you can select outside of these bubbles here. 
 If you do that, you'll get a selection box and you can scroll through this list as well. One of the 
 questions that pops up a bunch is, “Hey I have operational technology in my organization. Do you 
 have any rules that cover that?” The answer for that is absolutely we do. 
 10:00-11:00 
 If we scroll over here you'll see that we have scada rules and that is selected. By default, the IDS in 
 Stellar Cyber does take into account operational technology as well to look for threats. Again, to 
 close the selection box you can click outside the selection box. Now what's important is that these 
 aren't individual rules. These are groupings of rules. The scada rules, there's lots of scada rules, 
 there's lots of netbios rules by default, Stellar Cyber is looking for approximately 60,000 different 
 rules to detect threats in network traffic. Also, if we look here there's some buffering involved. If the 
 Modular Sensor loses connectivity to the Stellar Cyber platform, maybe there's an internet outage at 
 the remote site, we can buffer the Interﬂow records. 
 11:00-12:00 
 ADM-03-01-224  74 


---

<!-- Página 75 -->

 Alright. I will go ahead and select  Submit  , and this will enable the IDS module. To view the status, I can 
 go to  System | Sensors  . You'll see the conﬁguration is out of sync. That is because it is now loading 
 the new conﬁguration. Okay. After about ten to twenty seconds, the Modular Sensor status became 
 green, which is success. That means that it has loaded the new conﬁguration. It may take a couple 
 extra seconds for the modules themselves to load. If I select the Modular Sensor name from this 
 page, I can get the sensor details. Looking at the sensor details on the right, I do see that the modules 
 have loaded. I have the IDS Analyzer, I have the IDS Rules and the Traffic Monitoring. Everything is 
 green, so that looks good. 
 12:00-13:00 
 If I scroll down, I could also get additional statistics as well. One of the tabs here is the  ML-IDS 
 Malware Sandbox  stats. I can see right now I have  76,000 ML IDS Interﬂow records that have been 
 collected. If I look over here as well I see that this is from March 24. Right? So it is important to also 
 know that everything in this  Sensor Details  page is  related to the time I have speciﬁed up here as 
 well. Turns out that I was using the IDS module previously. But now what I'll do is go ahead and select 
 a more reasonable time frame since we just enabled the IDS module. Now the stats below will be 
 more current. 
 13:00-14:00 
 Within the last hour, I have received some ML-IDS Interﬂow records. If I scroll down I can actually see 
 that yes I am receiving traffic. Okay. Everything is now looking good, and I will close out of this page. 
 Now that the IDS module is enabled, there are some places you can go to view ML-IDS-speciﬁc 
 information. ML, again it's machine learning, IDS. Even though we've enabled IDS on the Modular 
 Sensor, the IDS engine is looking for threats in network traffic using the Suricata rules. When it 
 identiﬁes threats, it creates Interﬂow records and sends those back to the Stellar Cyber platform. 
 14:00-15:00 
 The Stellar Cyber platform then uses machine learning and statistical analysis rules and heuristic 
 rules to look for threats. If it identiﬁes a threat, that will get created as an Alert. Alerts themselves can 
 be correlated into Cases using graph machine learning. For now, let's take a look at some of the 
 IDS-based Alerts. We go to  Visualize | ML-IDS  .  Here  are the main Alert types associated with IDS. 
 There are private-to-private exploit attempt anomalies. There are private-to-public exploit attempt 
 anomalies. There are public-to-private exploit attempt anomalies. And public-to-public exploit 
 attempt anomalies. 
 15:00-16:00 
 In the last hour there have been no threats on my internal lab network. Let me extend the range. 
 Again, I have been using the IDS engine previously. I had turned it off just so I could turn it on again. 
 The ﬁrst thing I'm going to do is take a look at, let's say, last week. Okay. Now looking at this chart, I 
 can actually take a look at the signatures that have the most activity. If I take a look at this one right 
 now, the ID 2027267, the signature is for an attack response possible lateral movement. Again that's 
 the East/West Movement. There's a ﬁle creation request and remote system 32 directory. The 
 category is attempted user privilege, gain, and severity is critical. 
 ADM-03-01-224  75 


---

<!-- Página 76 -->

 16:00-17:00 
 There's been 22,000 entries that have matched this threat. Looking over here as well for this 
 signature, I have the 2027757 is a DNS query for a top level domain as TOs that's the country of 
 Tonga. Or I guess the Republic of Tonga. That's potentially bad traffic there. The severity is high. Once 
 the IDS module on the Modular Sensor detects a threat, it creates the Interﬂow record and sends that 
 to the Stellar Cyber platform. That is the raw event. But what's cool about that is the other 22,000 
 entries here and there's 10,000 entries here and there's 1.6k here and 251 entries here. That's a lot of 
 records to sort through. 
 17:00-18:00 
 Well, the good thing is the Stellar Cyber platform is applying machine learning on top of this and 
 heuristic rules and statistical analysis rules. Based on that, the Stellar Cyber platform has detected six 
 Alerts. Six is a much more reasonable number to deal with. Here to investigate these six, I will select 
 Investigate  . Now you can see I've been taken to the  Alerts  page. The main difference between going 
 here directly is that by using the  Investigate  for  those speciﬁc Alerts, the correct ﬁlter has already 
 been applied. From here I can see the private-to-private exploit attempt anomalies. I can see the Kill 
 Chain stage for MITRE as Propagation. The tactic is lateral movement. The technique is exploration of 
 remote services. There's even an explanation right below. 
 18:00-19:00 
 For example, a private IP address initiated a large number of exploit attempts identiﬁed by a given 
 signature or a rarely seen exploit attempt to another private IP address, investigate that signature. 
 Okay. If I look over here now, I can scroll down and look at those actual threats. If I take a look here, I 
 have an Alert score of 82. That means if you see an Alert score, the Alert score is what Stellar Cyber 
 has identiﬁed as a higher Alert. There's also something called Score, which you might see in a IDS raw 
 event message, and that score actually comes from the IDS engine itself. But the Alert score is 
 generated by the Stellar Cyber machine learning. 
 19:00-20:00 
 I'll click on the Interﬂow record for an Alert, which is called More info. In the more info, I see again at 
 the top that this is a private-to-private exploit anomaly. I see the stage is Propagation. The tactic is 
 lateral movement. If I want to know what this actually means, I can select lateral movement here and 
 that takes me to the MITRE ATT&CK framework page. If I scroll down in here, I can get lots of details 
 on what this means. I'll go back to my Alert. I can also select the technique here that also links to the 
 MITRE ATT&CK framework page. Over here now I can see what exploitation of remote services 
 means. Again, you don't have to remember everything. There is a lot of information out there. What's 
 important, more than anything else, is to know how to get that information when you need to get to 
 it. 
 20:00-21:00 
 Luckily, Stellar Cyber links this information right from the platform itself. Now if I scroll down I can 
 look at the  Key Fields  . Looking at the  Key Fields  here, I see the  Tenant  , which is the root tenant.  I see 
 the  Exploit Signature  , which is the attack response,  possible lateral movement. There's the  Exploit 
 Severity  , which is critical in this case. There's  the  Actual  .  Actual  is a weighted number. If I wanted  to 
 ADM-03-01-224  76 


---

<!-- Página 77 -->

 determine what that weighted number means, I can use a little  i  . Here, it's the actual number of times 
 this signature was found in the period. With critical ideas signatures counted as two, high counted as 
 one, low counted as point ﬁve, and others counted as one. Again, this is a weighted number. 
 21:00-22:00 
 I can see the source host and the destination host. The source host is 10.20.1.15. Does anyone 
 remember what that IP address is? It is the IP address of my Modular Sensor, and the destination 
 host is winad-San Jose, Training DC two, so that is my Windows server. The cool thing about looking 
 at this is that I now know where this came from. My Modular Sensor is also running a vulnerability 
 scanner. I will explain more about that later, but the cool thing about that now is it did a vulnerability 
 scan, which looks for threats. The vulnerability scanner actually made a threat that was identiﬁed by 
 the Modular Sensor as well in the IDS engine, and therefore, it was reported. 
 22:00-23:00 
 I can ﬁlter out this communication, and most likely I would. I would say, “Look I don't want to look for 
 threats from my Modular Sensor.” But for this lab environment it's a great way to see a whole bunch 
 of Alerts. Now I can also see if this Alert is related to a Case. A Case is created by graph machine 
 learning on the Stellar Cyber platform. It correlates related Alerts. Here I can see that the correlated 
 Alerts have a score of 99.6. In other words, the Case score. The platform links you to the Case as well. 
 Looking over here, I can see the Case is a private-to-private exploit anomaly and 30 others. 
 23:00-24:00 
 In other words, there have been 30 Alerts that have been correlated together. I can see if I scroll 
 down, all the Alerts that are related. Now the cool thing about a Case is that I can analyze it. I can see 
 the external hosts that were involved. I can see the internal hosts that were involved. I can see the 
 URLs that were attempting to be accessed. Over here as well I can look at a timeline and see what 
 happens. I can move this out of the way. Here I see the IP addresses involved. The ten dot twenty dot 
 one to ﬁfteen is my Modular Sensor. These are the URLs that were being accessed on the 10.20.1.12 
 Windows server. I also see some remote hosts as well. 
 24:00-25:00 
 If I select the number here, it ﬁlters the Alerts in the timeline on the left-hand side. If I want to see 
 what this one is about, it's an external ﬁrewall denial anomaly. What does this one say? It is a host 
 with 80.66.88.215 has actions blocked by the ﬁrewall too many times trying to access the 10.20.1.12 
 server. I could investigate more. We cover how to process Cases in the SOC analyst modules, but just 
 so that you can get an idea of what you can do, if I do detect a threat I can disable the user in an 
 identity platform such as Active Directory. I can run a script. Depending on the Connectors that I have 
 connected to the Stellar Cyber platform or to the Modular Sensor, I can have a lot more different 
 actions. 
 25:00-26:00 
 I will go back to the Alert. If I go further down, I can get the details of the Alert. The Details are all the 
 ﬁeld names and ﬁeld values collected There's also the JSON format version of this as well that you 
 can also export here or copy to a clipboard. What's also really cool is that I can take an action. 
 ADM-03-01-224  77 


---

<!-- Página 78 -->

 Depending on the Connectors I have conﬁgured either on the Modular Sensor or on the Stellar Cyber 
 platform, I have a set of external actions that are available. With an Active Directory Connector I can 
 disable the user, I can run a script that goes on a server. 
 26:00-27:00 
 If I have a Connector to an EDR platform, I could contain the endpoint, and there's many more 
 actions depending on the Connectors I have. Here I would be able to disable the user. In this 
 environment, I have Connectors to Active Directory. I could locate the user associated with this Alert 
 and disable the user. I will demonstrate that in the Connector lessons. Another very important 
 concept to understand is that the IDS module on the Modular Sensor is looking at these 60,000 
 Suricata rules to identify threats. When network traffic matches one of the rules, the IDS module 
 creates the Interﬂow record and sends that to the Stellar Cyber platform as a raw event. 
 27:00-28:00 
 It is a raw event as an Interﬂow record, but it's still a raw event. Now if I had to look through 32,300 
 events by myself, that can take a long time. That's where machine learning comes in and the 
 statistical analysis rules and the heuristic rules. Letting the Stellar Cyber platform do the work gets rid 
 of the noise, so you can focus on the real threats. Now if I scroll down and look at the threats that 
 Stellar Cyber has determined out of all those 32,000 events, these are the six that are determined to 
 be real threats, and they have been given a score. The ﬁrst one I see here is a score of 82. I can then 
 go ahead and analyze that as well. By the way, the score with an 82 had 23,580 raw events 
 associated with it. 
 28:00-29:00 
 Now another important place to go to investigate IDS-related Alerts and events is the  Investigate | 
 Threat Hunting  page. From the  Investigate | Threat  Hunting  page, the default indices is  Alerts  . 
 Again, Alerts are the statistical analysis rules, the heuristic rules, and the machine learning Alerts that 
 are created from the raw events that are received. If I go over here, I'm looking at Alerts for the past 
 week. What if I just want to see Alerts related to IDS? 
 29:00-30:00 
 Well, you can do that quite simply from this interface. If I scroll down to here where it says  Top Log 
 Source Classes  , if I look at the legend, one of the  legend entries is  ids_event  . Let me zoom in so you 
 can see it better. Over here I will create a ﬁlter that includes ids_event. Now this whole page is for 
 everything that is related to an IDS event. You'll also see here that there's a ﬁlter created. Scrolling 
 down I see ids_event is a message class. What if I want to know what that actually means and what 
 it looks like? The cool thing is you can copy as query. I'll also remove this ﬁlter now because I'll do the 
 same query up top. 
 30:00-31:00 
 I'll close these ﬁlters. If I expand this content search here, I'll paste in that query. I have 
 message_class is the ﬁeld name. The value is ids_event. This query also has or message 
 class.keyword colon quote IDS event end quote. Now keyword just says that the IDS event must be in 
 this exact case. I really don't care right now. All I really care about is that the message class is an IDS 
 ADM-03-01-224  78 


---

<!-- Página 79 -->

 event. If I select  Return  again. Let me minimize this. If I select  Return  , I go from 283 back to eight But 
 if I want to ﬁlter more now, I can take a look at one of these events. 
 31:00-32:00 
 Let me take a look at ones by sorting on the  Alert  Score  . This Alert with an 82 is the Alert we were 
 looking at in the  Visualize | ML-IDS  page. But what  if I want to get more information? If I expand this 
 Alert and maybe I just want to search for similar to the same destination IP. I'll look over here. Let me 
 expand this more. So the destination IP 10.20.1.12, I can also copy as query. I'll minimize that. You'll 
 have a green notiﬁcation box that the query was copied. I'll go back over here. I'll zoom in one more 
 time and I will type in AND. AND has to be uppercase. 
 32:00-33:00 
 These operators OR and AND must be in uppercase, and I can paste. This query is saying show me 
 all IDS events that have a destination IP of 10.20.1.12 in the  Alerts  indices. In other words, it has to  be 
 an Alert. Now minimize this again, zoom out, and I'll press  Return  . Now I have three events that are 
 going to the same IP. To validate that, if I expand one of these, I can look for the destination IP is 
 10.20.1.12. If I were to scroll down further, I can look for the message class. There it is right there: 
 Message class is IDS event. 
 33:00-33:35 
 It's really cool to be able to do the copy as query and to focus and ﬁlter on what you really want to 
 ﬁnd, to ﬁnd related events. I can go ahead and say  Clear all  if I have anything here just to make sure. 
 You do want to make sure that if you are done ﬁltering or searching for an item, that you do clear 
 your ﬁlters. 
 This lesson is complete. Thank you for watching. 
 L20 - MALWARE SANDBOX 
 L20A-PRES: Malware Sandbox Details and Conﬁguration (06m:32s) 
 00:00-01:00 
 The next lesson is  Malware Sandbox Details and Conﬁguration  .  This lesson,  Malware Sandbox Details 
 and Conﬁguration,  provides the concepts and details  on how to conﬁgure the Malware Sandbox 
 functionality on a Modular Sensor. 
 Hi everyone. Here I will describe the malware sandbox built into the Modular Sensor. A Malware 
 Sandbox is a security mechanism that allows for the analysis and execution of potentially malicious 
 ﬁles in a controlled environment. It is used to detect and analyze the behavior of malware without 
 risking the security of the host system. 
 01:00-02:00 
 The sandbox isolates the malware from the rest of the system, allowing security analysts to observe 
 its actions and gather information about its behavior, such as ﬁle modiﬁcations, network connections, 
 ADM-03-01-224  79 


---

<!-- Página 80 -->

 and system changes. By running the malware in a sandbox, security professionals can gain insights 
 into its capabilities and develop appropriate countermeasures. Within the Modular Sensor, on 
 Modular Sensor feature number four, I will describe the Malware Sandbox. The Malware Sandbox is 
 enabled in the license called APT for advanced persistent threat. After receiving and identifying ﬁles 
 in the network traffic from SPAN ports or TAP devices, Modular Sensors identify, extract, and 
 reconstruct malware traveling through the network within unencrypted protocols 
 02:00-03:00 
 such as HTTP, FTP, which is the ﬁle transfer protocol, SMB, which is Windows ﬁle sharing, and SMTP, 
 which is simple mail transfer protocol. Modular Sensors forward ﬁles identiﬁed as malicious to an 
 external HTTPS server for storage. Modular Sensors normalize malware metadata into Interﬂow 
 records and forward to the Stellar Cyber platform. From the Stellar Cyber platform, you can view and 
 analyze observations of malware traveling through the network and arriving at speciﬁc hosts as well 
 as view summaries of the events related to malware. Enabling the Malware Sandbox requires 
 authorization of the APT Malware Sandbox license for Modular Sensors. 
 03:00-04:00 
 To authorize, you can go to  System | Sensors  . Then  on the  Sensors  page, select  Manage  , then 
 Authorization  . If you look at the radio buttons on  top, there is an  Authorize  and  Unauthorize  radio 
 button. You're going to ensure the  Authorize  radio  button is selected. If The Modular Sensor itself was 
 not authorized. it would be on the left-hand side. As it has been authorized by the administrator 
 already, I see the SC Modular Sensor on the right as a selected sensor. Underneath, I have an IDS 
 license and an APT license. I have checked both of them. 
 04:00-05:00 
 You just need to make sure if it's not checked, to check the APT license. After you're done, you can 
 select  Submit  . As a side note, APT stands for advanced  persistent threat. It refers to a prolonged and 
 targeted cyber attack in which an intruder gains access to a network and remains undetected for an 
 extended period. APT attacks are initiated to steal data rather than cause damage to the target 
 organization's network. After submitting authorization, the  Sensor Status  will display as red and the 
 message will show that it is disconnected and the conﬁguration is out of sync. But you will see the 
 authorization as authorized for the sensor. 
 05:00-06:00 
 After a minute if you refresh the browser, you will then see the message go away, and the status will 
 be green, and the sensor of course is authorized. The Modular Sensor sandbox is enabled by editing 
 the Modular Sensor proﬁle in  System | Sensor Proﬁles  .  In the Modular Sensor proﬁle you must 
 enable  Network Traffic  because to ﬁnd malware, you  actually have to capture network packets. You 
 then ensure you enable  Sandbox  . One of the options  under  Sandbox  is that you can set the max ﬁle 
 size in megabytes, exclude MIME types, and a region close to the sensor to minimize latency in 
 sending ﬁles. 
 06:00-06:31 
 ADM-03-01-224  80 


---

<!-- Página 81 -->

 You can leave the region as  Automatic  and it will pick up the region from the sensor, or you can 
 select a speciﬁc region. After completing your conﬁguration settings in the sensor proﬁle, the  Submit 
 button must be selected to apply the conﬁguration settings to the Modular Sensor. Hopefully by now 
 this is a very simple task for you. 
 This lesson is complete. Thank you for watching. 
 L21 - MALWARE VISIBILITY IN THE STELLAR CYBER 
 PLATFORM 
 L21A-PRES: Malware Visibility in the Stellar Cyber Platform (06m:33s) 
 00:00-01:00 
 The next lesson is  Malware Visibility in the Stellar  Cyber Platform  . This lesson,  Malware Visibility in  the 
 Stellar Cyber Platform,  explains how to view details  about ﬁles collected and analyzed by the 
 Malware Sandbox module in the Stellar Cyber Open XDR platform. 
 Hi! In this lesson, I will show you how to validate that the malware module is enabled in the Stellar 
 Cyber Modular Sensor. I'll also show you how to view the occurrences of malware within the network 
 traffic received. I'll also show you how to mitigate threats by blocking an IP using a Connector to a 
 ﬁrewall. 
 01:00-02:00 
 To begin, for step number one, let's go ahead and select  System  and  Sensors  . That takes you to this 
 Sensor  page. On the  Sensor  page, you will select the  name of the Modular Sensor that has the 
 Malware Sandbox enabled. For step number three, if you look on the right-hand side, you have a 
 Service  and  Status  for Malware Sandbox. Right now  we see that the Malware Sandbox is green for 
 Status  . That's a very good sign. You can also view  the ML IDS Malware Sandbox output chart and see 
 the number of events. Here we do see that the events are increasing. 
 02:00-03:00 
 Therefore, we know it’s working. Also the chart below gives you details on this bits per second for 
 example, for the malware and IDS. To view the Alerts related to malware and take an action to 
 mitigate threats, you can go to  Alerts  on the top  menu bar, then search in the search bar: type 
 malware. By doing that and making sure you hit  Enter  or  Return  after typing “malware,” you will see, 
 for example, uncommon process anomaly or external other malware. Let's take a look at the 
 external other malware. On the right-hand side for step number three, you can select  View  . When 
 you see the chart appear, you can scroll down to view the malware or other malware documents. 
 03:00-04:00 
 You can locate an Alert record and select the  i  for  more information. This will bring up the Interﬂow 
 record. In the Interﬂow record, you can select the  Key Fields  and  Details  to look at the IP addresses 
 and usernames and other important information associated with this malware event. If you want to 
 ADM-03-01-224  81 


---

<!-- Página 82 -->

 mitigate, for example, there's a host out there that has been infected, and you want to block the IP 
 address or prevent that host from sending any other information. You can go to  Actions  . 
 04:00-05:00 
 One of the options available, depending on your Connectors, if I have a Connector to a ﬁrewall, I 
 have Block IP. If I have a Connector to an EDR platform such as CrowdStrike or BlackBerry Cylance, 
 or any of the EDRs that exist, you can have a Contain Endpoint option as well, which is actually 
 probably one of the better solutions to do, but Block IP will be a good example for this demonstration. 
 In the action conﬁguration after selecting block IP, for step number nine, I can select the  Connector  .  I 
 have a Connector to a FortiGate ﬁrewall. I can select the IP source host, which actually comes from 
 the Interﬂow record. I can specify a  Direction  for  the network traffic for the ﬁrewall policy. 
 05:00-06:00 
 In this case, I will select  Any  . Then you can specify  a duration. Maybe I just want to block an IP for ﬁve 
 hours while I'm doing some research investigation or just even a few minutes. I can say 30, then put 
 minutes for the duration. It's your choice. You can even put “forever,” but I think that will be drastic. I 
 don't think we need to do it forever. At that point, when you're done, click  Submit  . After submitting,  if 
 you go to the top menu bar and select  Investigate  | Actions  , you can see the list of actions that have 
 been performed. In this case, I see that the ﬁrewall action did succeed. 
 06:00-06:35 
 If, for example, the username was wrong for my API or something of the sort, you might get it failed. I 
 do have some tests below that do show failed, as an example. But once it succeeded, that IP now will 
 not be allowed to go through the ﬁrewall. There are many other actions that can be performed. This 
 just gives you an example of where to check your actions are working. 
 This lesson is complete. Thank you for watching. 
 L21B-DEMO: Malware Visibility in the Stellar Cyber Platform (24m:12s) 
 00:00-01:00 
 This lesson continues with demonstrations for malware visibility in the Stellar Cyber platform. This 
 demonstration explains how to conﬁgure the Malware Sandbox on Modular Sensors and shows how 
 to view details about ﬁles collected and analyzed by the Malware Sandbox module in the Stellar 
 Cyber Open XDR platform. 
 Next, I will show you how to enable the Malware Sandbox. Malware Sandbox is used in conjunction 
 with IDS. To do that you go to  System | Sensors  . On  the  System Sensors  page, the Malware Sandbox 
 is another authorization. 
 01:00-02:00 
 If I go to  Manage | Authorization  you'll see here  that there's something called APT license. That's 
 advanced persistent threat, which is the Malware Sandbox. I'll select that to enable that option and 
 then submit. Once the authorization is made, the sensor will reload the conﬁguration so that the 
 ADM-03-01-224  82 


---

<!-- Página 83 -->

 module will function. It only takes a second. Now I will go and conﬁgure the  System | Sensor Proﬁles  . 
 Again, the Modular Sensor proﬁle that I am using for this demonstration is the SC Modular Sensor 
 New. I will select the pencil to edit this proﬁle. 
 02:00-03:00 
 To enable the Malware Sandbox feature, there are three options that need to be enabled. The ﬁrst is 
 Network Traffic  . The Malware Sandbox analyzes network  traffic to ﬁnd ﬁles. Therefore,  Network 
 Traffic  must be enabled. Second, you must have  Malware  Sandbox  enabled. That one is pretty 
 obvious I hope. The maximum ﬁle size for a ﬁle that will be analyzed is ten megabytes. This is the 
 default and the maximum size possible. Next, you can exclude MIME types. By default we've excluded 
 types that are not really considered a threat. However, if we go in here, and select next to one of 
 these bubbles, there are many other options as well that you could exclude if you ﬁnd they're not 
 important to exclude in your environment. 
 03:00-04:00 
 Select outside of the box to close the selection. Next, the region. There are regions all around the 
 world where the Malware Sandbox can store ﬁles that are uploaded from the Stellar Cyber Modular 
 Sensor. When malware is found, the malware will be stored in a location of your choice, and it should 
 be the closest region to where your Modular Sensor is deployed. The Malware Sandbox requires the 
 IDS module as well for a couple of purposes. One is for the reconstruction or reassembly of ﬁles from 
 packets that are being forwarded to the Modular Sensor. Two, it's for the deﬁnition of what ﬁles 
 should be checked. 
 04:00-05:00 
 This is based on the IDS networks that were speciﬁed. From the home network to external network or 
 external network to home network and home network to home network, as an example. With these 
 three things: Network Traffic, the sandbox feature, and IDS, I do not need to conﬁgure anything else. 
 The sandbox will work appropriately. I'll submit. To check on the status, I go to  System | Sensors  .  I see 
 that my Modular Sensor is already a status of success. I will expand that out so we can see it. There 
 we go. I'll select my Modular Sensor. If I go over here, I see that Malware Sandbox is running 
 successfully. 
 05:00-06:00 
 If I go over here as well and look at the ML-IDS stats, I do see that I do have traffic coming in and 
 being processed for ML-IDS, which is also being processed for ﬁles. Next, I will go to  Visualize  and 
 Malware Sandbox Overview  . In this Malware Sandbox  view, I will start with the  Overview  . In the 
 Overview  , I can see that there are lots of good ﬁles  found, but there was also a malicious ﬁle. It's 
 called eicar_com.zip. I can select the  (i)  to get  more info. Looking at this, I see the ﬁle name here. One 
 of the most important things to understand about analyzing ﬁles is that the ﬁle name could be 
 anything. 
 06:00-07:00 
 It might even be the name of a ﬁle that you use on a regular basis. You cannot rely on ﬁle names 
 whatsoever. No one's going to create a malware ﬁle and call it, “malware ﬁle” because then you won't 
 ADM-03-01-224  83 


---

<!-- Página 84 -->

 click it and open it and get exposed. One of the most important things to understand is that every ﬁle 
 has a hash. A hash algorithm looks at the entire ﬁle and creates a 128-bit output representing that ﬁle 
 only. If I change a ﬁle in any way, then this MD5 hash will also change. There's also SHA-1, which is a 
 hash algorithm as well that uses 160-bits and there are other different versions as well. But the most 
 important thing is the name of the ﬁle can be changed, but the contents of the ﬁle will always 
 produce the same hash. 
 07:00-08:00 
 Now let me give you an example. Here, I will look at a ﬁle that I have on my Mac. This ﬁle is called 
 “testﬁle1.text.” I know, it's a very complex ﬁle name. I can say  vi  , which is an editor, and I can  look at 
 this ﬁle. This ﬁle only has, “Stellar Cyber training, example of hash function.” Now Macs come built in 
 with an MD5 hash function, and I can hash. I can run the hash on this ﬁle. Here I see the 128-bit output 
 starting with “b,” and ending in “6.” Now let me rename the ﬁle. I'll say, “CP testﬁle1.text to 
 testﬁle2.text.” 
 08:00-09:00 
 If I do the MD5 hash again, on testﬁle2.text, you'll see it's the exact same hash. If I had malware in one 
 of these ﬁles and I copied the name to something that looks right, it's still malware, and it will be 
 detected. It does not matter what the ﬁle name is. But if I were to modify testﬁle2.text in any way, I'll 
 just add a one inside the ﬁle name. I run the MD5 hash again, you'll see that the hash has changed. 
 That's the concept of looking for malware. It's looking for essentially a signature or a hash of the ﬁle 
 to see if known bad malware is found. Alright. I hope that was helpful. Okay. Now I will take a look at 
 this MD5. 
 09:00-10:00 
 One of the options you can do is do a VirusTotal lookup on that hash. Sure enough, I see that 
 VirusTotal has found that this is a bad ﬁle. The other thing I can do is copy this to clipboard. Over here 
 I can see if there's any other ﬁle with this hash. I can do a search. I can zoom in a little bit for you. 
 [Types] md5: the hash. Again, it only ﬁnds the one ﬁle. That's what we're actually expecting because I 
 only had one occurrence of it. Okay. Now I will close out this ﬁlter. I'll select  Clear all  , minimize  the 
 ﬁlter box, and we'll go back to the main screen. 
 10:00-11:00 
 Now I will go through the tabs. Looking at the tabs on the  Visualize  |  Malware Sandbox  , if I had 
 ransomware I would see accounts here or trojans, spyware, PUS or potentially unwanted 
 applications, or other malware, but I also have good ﬁles. Looking at the good ﬁles, hopefully that 
 you have a higher number of good ﬁles than the rest. If I scroll down and take a look, I can see that I 
 have a lot of events related to good ﬁles and hopefully that is the case. I can also take a look at 
 these good ﬁles. Just like I did for the malware, if I'm investigating a threat or I want to see if 
 someone else had received the same ﬁle as somebody else, I could take a look at the MD5 hash of 
 the ﬁle. 
 11:00-12:02 
 ADM-03-01-224  84 


---

<!-- Página 85 -->

 I can copy that to clipboard or add as an including ﬁlter. If I go over here, from the top. Again, I can 
 zoom in here, do a paste, and search for MD5:, and I'll zoom back out. Here I see there are three 
 events related. This destination host here, this host here, and this host here all have the same ﬁle. 
 Maybe this ﬁle was part of an upgrade that was done by each of these three servers. They are all 
 Windows servers. That is potentially what happened. But either case it's good to be able to have 
 access to the ﬁle hashes so that you can use that in your threat investigations. 
 This lesson is complete. Thank you for watching. 
 L22 - MODULAR SENSOR Aggregator 
 L22A-PRES: Modular Sensor Aggregator (09m:32s) 
 00:00-01:00 
 The next lesson is  Aggregator Details and Conﬁguration.  This lesson,  Aggregator Details and 
 Conﬁguration,  explains the concepts and conﬁguration  of Modular Sensors to be an Aggregator as 
 well as how to conﬁgure other Stellar Cyber sensors to use the Modular Sensor as an Aggregator. 
 In this lesson I will cover the Modular Sensor Aggregator, and its uses and how to conﬁgure it. 
 Looking at the picture on the left-hand side, the Aggregator is listed as one of the core features of 
 the Modular Sensor. 
 01:00-02:00 
 When conﬁgured as an Aggregator, the Modular Sensor acts as a proxy to forward traffic from other 
 Modular Sensors, Windows Server sensors, and Linux Server sensors to the Stellar Cyber platform. 
 Sensors send Interﬂow records to the Modular Sensor Aggregator using TCP port 8080. It's therefore 
 important that you don't have any type of ﬁrewall or any type of access control blocking TCP port 
 8080 between the sensors and the Modular Sensor Aggregator. When the Interﬂow records get sent 
 by these sensors to the Aggregator, it will then forward them all from a single IP of the Modular 
 Sensor to the Stellar Cyber platform. The Aggregator feature reduces the number of connections 
 that are made from the Modular Sensors and server sensors within an organization to the Stellar 
 Cyber platform over the internet. 
 02:00-03:00 
 For some organizations that's important. For a lot of other organizations, it doesn't matter that each 
 Windows Server sensor or Linux Server sends directly to this Stellar Cyber platform. This is a 
 preference based on your organizational needs or your customer's organizational needs. You can 
 conﬁgure multiple Aggregators because the sensors can have a primary and backup as well. When 
 the Aggregator feature is not in use, all sensors for an Interﬂow records directly to the Stellar Cyber 
 platform. Just so it's clear, when the Aggregator feature is not in use, all sensors–Linux Server 
 sensors, Windows Server sensors, Modular Sensors, forward Interﬂow records directly to the Stellar 
 Cyber platform. 
 03:00-04:00 
 ADM-03-01-224  85 


---

<!-- Página 86 -->

 With the Aggregator feature enabled, sensors can be conﬁgured to forward Interﬂow records to the 
 Stellar Cyber platform through the Aggregator. To conﬁgure the Modular Sensor to be an 
 Aggregator, modify the Modular Sensor proﬁle in  System | Sensor Proﬁles  . In the Modular Sensor 
 proﬁle, enable Aggregator as in step number one. For step number two, select  Submit  . That's pretty 
 simple. That's all there is on the Modular Sensor. The rest of the work is to tell the other sensors within 
 the organization to use this Modular Sensor Aggregator. You can conﬁgure other Modular Sensors as 
 Aggregators for scale. You can also conﬁgure other Aggregators for redundancy as well. 
 04:00-05:00 
 When you conﬁgure a sensor, you have the ability to conﬁgure a primary Aggregator and secondary 
 Aggregator. Okay. Next, conﬁgure Modular Sensors, Windows sensors, and Linux Server sensors, 
 within a network to use the Modular Sensor as their primary Aggregator. As a reminder, TCP 8080 
 must be permitted between sensors and the Modular Sensor Aggregator within the network. Now to 
 conﬁgure Modular Sensors, Windows Server sensors, and Linux Server sensors to use the Modular 
 Sensor as their Aggregator, on step number one, select  System  , then go to  Sensors  . This will bring up 
 a list of sensors you have deployed. 
 05:00-06:00 
 For each sensor on step number two, that will use a conﬁgured Modular Sensor as its Aggregator 
 sensor, select the pencil icon to edit the sensor parameters. This will bring up the list of parameters 
 for a sensor. For step number three, select the primary Aggregator, which is the host name of the 
 Modular Sensor conﬁgured as an Aggregator. Once you select a primary Aggregator, a secondary 
 Aggregator is available to be selected. If you do not have a secondary Aggregator, that is okay. This 
 is optional. Next, select  Submit  . After selecting  Submit  , the sensor status will display the following: 
 The messages column will show as disconnected conﬁguration out of sync, the Sensor Status will be 
 red, and the authorization will be authorized. 
 06:00-07:00 
 After a minute if you refresh the browser the messages will show empty. The Sensor Status will show 
 green and the Modular Sensor will still be authorized. After the Modular Sensor status is green, you 
 can check the status of the Modular Sensor Aggregator. Now that the Modular Sensor has been 
 conﬁgured as an Aggregator, and another sensor has been conﬁgured to use the Aggregator, you 
 can check the status of both using CLI commands. Select the checkbox next to the Stellar Cyber 
 Modular Sensor that is the Aggregator, and then you'll see an option for CLI access. Select  CLI 
 Access  . In the  CLI Access  window you can type  show  Aggregator  . 
 07:00-08:00 
 After typing  show Aggregator  in about twenty seconds  or so, you will see a message that shows 
 DS, which is data sensor, is not routed through an Aggregator. That is true because it is in itself the 
 Aggregator. This device acts as an Aggregator, and it will show you that it has received traffic from 
 sensors, and has sent traffic to sensors, and it is connected to a sensor. In this case, it's ten dot twenty 
 dot one dot twenty three and the connection is established. That's a very good sign that everything is 
 working. Next, similar to what you just did with the Modular Sensor Aggregator, you can also check 
 the status of the sensor that is using the Modular Sensor as its Aggregator. 
 ADM-03-01-224  86 


---

<!-- Página 87 -->

 08:00-09:00 
 For step number one, from the  System | Sensors  list, check the box next to the name of the sensor 
 that is using the Modular Sensor as its Aggregator. For step number two, select  CLI Access  from the 
 Sensor CLI Access  window. For step number one, type  show Aggregator  . For step number two, 
 you'll see after about twenty seconds, that the DS, or data sensor, is routed through the Aggregator, 
 which shows the correct IP address of the Modular Sensor, which is 10.20.1.15. You can also see that 
 the connection is established to the conﬁguration and management connection of the Stellar Cyber 
 platform. 
 09:00-09:31 
 At this point everything looks great. The connection is working and data is being sent from this 
 sensor to the Modular Sensor, which is then forwarded to the Stellar Cyber platform. All done there. 
 That's all we need to do for this. 
 This lesson is complete. Thank you for watching. 
 L22B-DEMO: Modular Sensor Aggregator (07m:51s) 
 00:00-01:00 
 This lesson continues with demonstrations for Aggregator details and conﬁguration. This 
 demonstration explains the concepts and conﬁguration of Modular Sensors to be an Aggregator, as 
 well as how to conﬁgure other Stellar Cyber sensors to use the Modular Sensor as an Aggregator. 
 Hi everyone. In this lesson, I will show you how to conﬁgure a Modular Sensor as an Aggregator. From 
 the  System | Sensors  page, I can see that I have three  sensors. The ﬁrst one here is a Modular 
 Sensor, the second one is a Linux Server sensor, and this one is a Windows Server sensor. 
 01:00-02:00 
 By default, every sensor communicates directly with the Stellar Cyber Open XDR platform. When the 
 Windows Server sensor creates an Interﬂow record from events, it will then forward that to the Stellar 
 Cyber platform. When the Linux server sensor generates Interﬂow records from events, it will then 
 forward that directly to the Stellar Cyber Open XDR platform. Of course, the Modular Sensor does the 
 same. In some organizations, you may want to limit the connectivity of servers talking directly out to 
 the internet or to the Stellar Cyber Open XDR platform. If you want to consolidate the 
 communication, you can conﬁgure the Stellar Cyber Modular Sensor as an Aggregator. 
 02:00-03:00 
 To do that, I go to  System | Sensor Proﬁles.  The  proﬁle that I'm conﬁguring right now for my 
 Modular Sensor is the SC Modular Sensor New. Here, I can enable the Modular Sensor as an 
 Aggregator. It's pretty simple. That's all I have to do now. You'll see here, by the way, it says 
 Aggregator: Act as a proxy to forward traffic from sensors to DP. When you see the letters DP in 
 capital letters, that is the Stellar Cyber Data Processor. The Data Processor is another for the Stellar 
 ADM-03-01-224  87 


---

<!-- Página 88 -->

 Cyber platform. I will now select  Submit  . The interesting thing about this is that this doesn't change 
 anything yet. 
 03:00-04:00 
 Even though the Stellar Cyber Modular Sensor has the aggregated capabilities, other sensors now 
 need to point to that Modular Sensor. I can select the pencil of the sensor that I want to edit. Here, 
 there's an option for  Primary Aggregator  . I can go  ahead and select SC Modular Sensor. Note that if 
 I had multiple Modular Sensors in the organization, which might be either for redundancy or for scale. 
 In other words, I'm sending everything to one Modular Sensor, I might want to have multiple. In this 
 case I only have one Modular Sensor so I don't have a secondary and that's okay. I will go ahead now 
 and select  Submit  . And that's all I need to do. 
 04:00-05:00 
 The Linux Server sensor I see here will now reload its services to use the new conﬁguration, using the 
 Modular Sensor as its Aggregator. If I take a look now, I hit refresh. I see that now that it's active. To 
 validate the status of the Aggregator what I can do is go to the CLI shell. One way is from this screen 
 right here where I can select the Modular Sensor and select  CLI Access  . From the CLI window, I could 
 type in  show aggregator  . This will take about 10 to  20 seconds. 
 05:00-06:00 
 Here I can see that this device is an Aggregator that it has received from the sensor and sent to the 
 sensors. In other words, it has received from sensors and it is sending traffic to sensors back. There's 
 another sensor that's connected, which is the 10.20.1.23. To see this a little clearer I'll use my SSH. An 
 SSH to aella@10.20.1.15. I type in my secret password. Here I could type in  show aggregator  . As you 
 saw on the previous screen, I can see the communication is to the Stellar Cyber Open XDR platform 
 Data Lake, which is 192.168.1.175. I see the port, which is 6644. 
 06:00-07:00 
 I see that this device is an Aggregator. It is receiving traffic from sensors and it is sending traffic back 
 to sensors. It is connected to the sensor 10.20.1.23. If you look over here 10.20.1.23 is the Linux Server 
 sensor. I can do the same thing again for the Windows Server sensor as well. That's all there is to 
 conﬁguring an Aggregator. I could conﬁgure an Aggregator per tenant for example, or for each site 
 that my sensors are in so I can have one set of communication from that site back to the Stellar 
 Cyber Open XDR platform. Those are some of the main reasons why I might do this. It's really just to 
 aggregate all the communication from each site. 
 07:00-07:51 
 This is an optional feature. Now you also want to be careful here as well though. If I do have a 
 Modular Sensor that's receiving all the Interﬂow records from all the other sensors, you have to make 
 sure that there's enough bandwidth, interface speed, and processing power on the Modular Sensor 
 that is an Aggregator. In this case, if you are ﬁnding that you have too many connections being made 
 to the Modular Sensor, you can conﬁgure multiple Modular Sensors as Aggregators. Then you have a 
 choice of which servers point to each Modular Sensor. Okay. Well that's it for this lesson. Thank you 
 very much. 
 ADM-03-01-224  88 


---

<!-- Página 89 -->

 This lesson is complete. Thank you for watching. 
 L23 - MODULAR SENSOR TENABLE NESSUS SCANNER 
 L23A-PRES: Modular Sensor Tenable Nessus Scanner (15m:27s) 
 00:00-01:00 
 The next lesson is  Tenable Nessus Scanner Details  and Conﬁguration.  This lesson,  Tenable Nessus 
 Scanner Details and Conﬁguration,  provides the concepts  and conﬁguration of how to enable the 
 ability to initiate scans from the Tenable cloud website to run on the Nessus vulnerability scanner 
 module that can be enabled on Modular Sensors. 
 Another cool feature of the Stellar Cyber Modular Sensor is that it contains a Tenable Nessus scanner. 
 A Tenable Nessus vulnerability scanner is used to scan servers either by IP address or by network or 
 by IP ranges 
 01:00-02:00 
 to look for vulnerabilities within the operating system or those devices themselves. You can even 
 conﬁgure the Nessus scans to log into servers–Linux Servers and Windows Servers–for example, to, 
 again look for threats and then report those back. A lot of organizations use Tenable Nessus 
 vulnerability scanning capabilities, but they usually have to install a separate server within a network 
 and run the Tenable Nessus scanner from that. Stellar Cyber Modular Sensors actually have a 
 Tenable Nessus vulnerability scanner built in. You still need to have an account on Tenable.io. Once 
 you get an account on Tenable.io, then you can then use that license to link the vulnerability scanner 
 that's built into Modular Sensor to run a security scan. 
 02:00-03:00 
 From the Tenable website, which is cloud.tenable.com as an example, I can actually go to an option 
 called  Scans  and run a scan that will then be triggered  from the Modular Sensor, and then reported 
 back to the Tenable cloud site. Once the Nessus scan is complete, the Tenable site creates and makes 
 a report available with the results. Here's an example of the results you will see when running a 
 vulnerability scan. An important note, for conﬁguration of Tenable Nessus's vulnerability scanner on 
 the Modular Sensor virtual appliances 
 03:00-04:00 
 you will want to add an additional 1.5 gigabytes of RAM and add an additional vCPU. Alright? You 
 can do this after the fact. Again once you determine you want to run the Tenable Nessus vulnerability 
 scanner, you can go back to your virtual environment and increase the memory and vCPU and then 
 essentially restart the sensor. It will then have the correct amount of resources to run properly. 
 Nessus's scan functionality does require purchasing a vulnerability management service from 
 Tenable.io. Once you have that purchased from the Tenable cloud website, you go to  Sensors  , then 
 Nessus Scanners  . 
 ADM-03-01-224  89 


---

<!-- Página 90 -->

 04:00-05:00 
 The next step is you add a Nessus scanner, which is on the right-hand side, and you'll be provided a 
 linking key. You can copy the linking key and that will be used in the conﬁguration on the Stellar 
 Cyber Modular Sensor. Back in the Stellar Cyber platform, Tenable Nessus is enabled by editing the 
 Modular Sensor proﬁle in  System | Sensor  Proﬁles.  In this Modular Sensor proﬁle, you enable Tenable 
 Nessus. For step number two, you paste the linking key from Tenable.io copied from the  Add 
 Necessary Scanner  section. Note that the linking key  I have here is not valid. For you I've used it in 
 my test lab, but then disabled it. 
 05:00-06:00 
 For step number three, you enter the host, which in our case is cloud.tenable.com. Step number four, 
 enter port 443. That's not there by default so please make sure you do enter it. After completing your 
 conﬁguration settings in the sensor proﬁle, The  Submit  button must be selected to apply the 
 conﬁguration settings to the Modular Sensor. After you select  Submit  on the Modular Sensor proﬁle, 
 the Modular Sensors using the proﬁle will restart their services using the new conﬁguration. Again, 
 we've gone through this several times but again it's good to see. With repetition we remember. Alright. 
 Step number one the  Sensor Status  will go red, and  the message will display the conﬁguration is out 
 of sync. 
 06:00-07:00 
 After a minute, you will have to refresh your browser, and you will see the  Sensor Status  go green, 
 and the message will be clear. To validate the status of the Tenable Nessus module, go to  System | 
 Sensors  . Then select the name of the Modular Sensor  with the Tenable Nessus scanner enabled. You 
 then verify the  SERVICE STATUS  for Tenable Nessus  is green. Here the one I have is green so we are 
 good to go. You can get more details of the status of the Tenable Nessus client from the Modular 
 Sensor CLI. 
 07:00-08:00 
 Again from  System | Sensors  , select the checkbox next  to the Modular Sensor that has the 
 vulnerability scanner enabled. For step number two, select  CLI Access  . You will then have a  CLI 
 Access  window that appears. From that window you can  type  show tenable  . By the way, if you are 
 on the network, and you are the IT administrator, for example, you can SSH to the Modular Sensor 
 and run the same set of commands. Step number two, about twenty seconds after typing in  show 
 tenable  from the  CLI Access  window you will see a  working result hopefully that says, “Linked.” It'll 
 show you linked to the cloud.tenable.com:443, which is the port number. 
 08:00-09:00 
 Back on Tenable, the name of the Modular Sensor will show up in  Settings | Sensors | Nessus 
 Scanners  . Then select  Linked Scanners  . If you have  a lot of scanners available, you can type the 
 start of the host name and the list of linked scanners will be ﬁltered. Under  Linked Scanner  , the 
 Modular Sensor will be listed. Then select the name of the Modular Sensor. From the  Overview  tab, 
 you can see the status of the Nessus scanner within the Modular Sensor. Here we see that the status 
 is “Online.” Next, you can create a vulnerability scan on Tenable. 
 ADM-03-01-224  90 


---

<!-- Página 91 -->

 09:00-10:00 
 If you select the stacked line, often known as the hamburger icon, you can go to  Scans  . Then on the 
 right-hand side for step number three,  Create Scan  .  Now there are many different types of scans. 
 The Advanced scan gives you a lot more ﬂexibility. For this case, I will just do a Basic Network scan, 
 which is an in-depth scan. It just means that it's less for you to do. Enter a name for the vulnerability 
 scan. Mine is called, “SC Labs Training Basic.” For the scanner type, choose  Internal Scanner  . You 
 then select the Stellar Cyber host name as the scanner from the scanner list. By default it's set to 
 auto. Please make sure you select the scanner to ensure that it is the scanner being used. 
 10:00-11:00 
 Again, I have a note to verify that you have selected the Stellar Cyber Modular Sensor as the scanner. 
 For step number eight, there are targets. Targets can be IP ranges. For example, 10.20.1.21-10.20.1.23. 
 That will do 21, 22, and 23. Comma, an individual host such as 10.20.1.11. You could even do a CIDR 
 notation and say 10.20.1.0/24 and that will target the entire subnet. But again, every scan is very 
 in-depth and does take time. For the very ﬁrst time, you might want to consider using a single IP 
 address, then after you know everything is working, then increase the range. 
 11:00-12:00 
 The next thing you can do is specify email recipients. I could put in, for example, one of our heads of 
 training in Australia. His name is David Shirley, and myself as well are the email recipients. I can then 
 also give the correct permissions. The permissions may only need to be  Can View  , but mine is  Can 
 Edit  just in case. Next, you could save and not launch,  but I will save and launch so that I can see the 
 test actually happen. Next, back on the Stellar Cyber platform, to validate the scan is started on the 
 Modular Sensor Tenable Nessus's client, SSH to the Modular Sensor 
 12:00-13:00 
 or use the CLI access in the Stellar Cyber platform by going to  System | Sensors  , and select the 
 checkbox next to the Modular Sensor. Then select  CLI  Access  . From the  Sensor CLI Access  window, 
 you can type  show tenable  . Then wait about 20 seconds.  When the results come back you will see 
 that the scanner is linked to cloud.tenable.com:443, which is the port number. In this case, I actually 
 have a scan started, so there's one job pending. Back on the Tenable cloud, the status of the scan will 
 be displayed as follows. First you will see initializing, then pending, then running, then publishing 
 results, then ﬁnally, the scan will be completed, and you can then view the results. 
 13:00-14:00 
 It may take a few minutes to over an hour for a scan to complete depending on the number of 
 targets and the type of scan you perform. To see the scan, select the scan name and select  See All 
 Details  in the upper right. The resulting report provides  details for vulnerabilities for target hosts 
 speciﬁed in the scan. The email recipients conﬁgured in the scan are also sent a copy of the 
 vulnerability report. In case you run into any problems on the Tenable Nessus scanner, if you see for 
 example, that it does not appear on Tenable.io, on the Modular Sensor you can type  show tenable  . 
 14:00-15:27 
 ADM-03-01-224  91 


---

<!-- Página 92 -->

 If you see that the scanner is not linked to a manager, you must ensure that the linking key that you 
 copied from the  Add Network Scanner  is copied and  pasted into the Tenable Nessus conﬁguration in 
 the Modular Sensor proﬁle assigned to the Modular Sensor. For example, if you added the linking key 
 to a different Modular Sensor proﬁle, you will see the message on the left–that it's not linked. Or if 
 you had a typo in the linking key, the same thing will happen. Also, when conﬁguring the Tenable 
 scan on cloud.tenable.com for example, you might get an error message that appears: The following 
 targets were not routable. In this case, please ensure the Modular Sensor is speciﬁed as the Modular 
 Sensor in the conﬁguration in the Nessus scan. Remember previously when I talked about something 
 you must double check? By default, the scan will be set to using a scanner of auto. You want to make 
 sure that the scanner is selected as the Modular Sensor. Okay. These are just some tips for solving 
 some problems I ran into. Hope you enjoyed the lesson. 
 This lesson is complete. Thank you for watching 
 L23B-DEMO: Modular Sensor Tenable Nessus Scanner (12m:47s) 
 00:00-01:00 
 This lesson continues with demonstrations for  Tenable  Nessus Scanner Details and Conﬁguration. 
 This demonstration provides step-by-step details for conﬁguring a Tenable Nessus vulnerability 
 scanner on a Modular Sensor, adding the Modular Sensor vulnerability scanner to Tenable.io, and 
 creating a scan on Tenable.io that runs on the Modular Sensor Tenable Nessus vulnerability scanner. 
 Hi everyone. In this lesson I will show you how to conﬁgure the Tenable Nessus scanner module on 
 the Modular Sensor. With this module from Tenable.io. or cloud.Tenable.com, you can actually launch 
 a vulnerability scan right on the Modular Sensor to scan the local network. 
 01:00-02:00 
 This is a really cool feature because if you don't use a Modular Sensor, oftentimes organizations have 
 to install a separate server to run a Tenable Nessus scanner. Having the ability to run the Tenable 
 Nessus scan right from the Modular Sensor deﬁnitely saves a lot of time and resources as well as 
 makes it really easy to run the scans. First, let me show you how to conﬁgure a Tenable Nessus 
 scanner. As we've done many times before, to conﬁgure a Modular Sensor, we have to modify the 
 Modular Sensor proﬁle. I can select the SC Modular Sensor New and edit by selecting the pencil. Here 
 we've enabled the Log Forwarder, the Network Traffic, Sandbox, and IDS. None of these are actually 
 needed for being a Tenable Nessus scanner. 
 02:00-03:00 
 Once you slide the lever to enable the Tenable Nessus vulnerability scanner, there are a few 
 parameters that you need to conﬁgure. One is the linking key, two is the host, and three is the port. 
 The port is 443, but the linking key I need to obtain from Tenable. Let me show you how that's done. 
 Let me close this out. I have an account on cloud.Tenable.com. I'll go there now. From 
 cloud.Tenable.com, I have the option to go to  Settings  .  In  Settings  , the option I'm looking for is 
 Sensors  . Under  Scanning  , there are  Sensors  . 
 ADM-03-01-224  92 


---

<!-- Página 93 -->

 03:00-04:00 
 Here I see that there are quite a few sensors within my organization. What I want to look for are 
 Linked Scanners. If I take a look at the scanner name that I have, it's called SC-Modular Sensor. You'll 
 see that I don't have it in this list. To enable the Tenable Nessus scanner, I can select the option to  Add 
 Nessus Scanner  .  I have a linking key. I will copy this linking key. Now that I had the linking key copied, 
 I will go back to the Stellar Cyber platform and I will go to SC Modular Sensor New and edit. Next, I'll 
 enable the Tenable Nessus's vulnerability scanner and I will copy the linking key. The port will be 443. 
 That's just HTTPS. Then I select  Submit  . Enabling  the Tenable Nessus's vulnerability scanner on the 
 Modular Sensor is a very simple task, but there's also something you should be aware of. It does take 
 a little bit more CPU and memory. The best way to see what you should do here is go to the 
 documentation. In the documentation of the Modular Sensor proﬁle towards the bottom is the 
 Tenable Nessus  section. In the  Tenable Nessus  section  you can see this note: “This feature is 
 supported on Modular Sensors running version 434 or later. Stellar Cyber recommends that you 
 provision the Modular Sensor with an additional 1.5 gigabytes of RAM and one vCPU when you 
 enable this option.” 
 04:00-05:00 
 You can go–usually before you enable the Tenable scanner to enable this option. That will deﬁnitely 
 give you better performance. Okay. Now I will go to  System | Sensors  . I will check my Modular 
 Sensor. I see that Tenable Nessus is enabled. Great. Now I will go back to cloud.Tenable.com. Okay. 
 Back in the  Linked Scanners  , I will look for my Modular  Sensor. There it is! It is now connected and 
 functioning. That is perfect. The next step that I need to do is conﬁgure a scan that uses this Modular 
 Sensor vulnerability scanner. 
 05:00-06:00 
 To do that, you select the three-line stacked icon. I go over here and go to  Scans  . Then from  Scans  ,  I 
 can go ahead and create a new scan. Here, there are many different scans. There's an Advanced 
 Network scan, which I could use and make it even simpler than a Basic Network scan. A lot of the 
 time I will use the Advanced Network scan just to do a really quick task. The Basic Network scan is a 
 full system scan and is suitable for any hosts. It does take a little bit more time though. I will actually 
 do that one; I'll do the Basic Network scan. I'll give it a name. I'll call it, Training SC Modular Sensor. 
 07:00-08:00 
 Okay. Since this is a Basic scan, I'll put that as well. Next, here's something that got me. This is an 
 internal scanner. But the scanner by default is auto select. I went here and I saved my scan and 
 started it. It couldn't ﬁnd my host. It said that my hosts that I was trying to scan weren't on the same 
 network. Then I found out because you do need to select the scanner. Now for the targets, you can 
 use a range of IP addresses with a dash or you can use CIDR notation or even host names. 
 08:00-09:00 
 I will start off with a simple IP address because I want this to be as quick as possible. I will use 
 10.20.1.12, which is one of my Windows servers. Next, there's the email recipients for notiﬁcations. I'll 
 use my email. Then, when the scan is done, I will get an email letting me know that it's done. If I want 
 to give other people access to use my scan, I can give them  View  access. Now there's also something 
 ADM-03-01-224  93 


---

<!-- Página 94 -->

 else that's really cool: I can create credentials. I'm going to allow my Tenable Nessus scanner to log in 
 to my Windows server to look for vulnerabilities. I'll go over here and type in  Windows  . 
 09:00-10:00 
 Here this is the host. I'll select  Windows  . I will type in my administrator. I'll put in the administrator's 
 password. I really should create a separate account, maybe as an administrator called Tenable, but 
 for now, for ease of use I'm just going to use my administrator account. The domain is SC labs.ai and 
 I will save this credential. I'll go back to the settings. It looks good. I have my target. I have my Email 
 recipient, and now I can save and launch. This will go from pending and then initializing and a whole 
 bunch of other stages. This will take up to an hour. 
 10:00-11:00 
 I will leave this for now and then come back later. After a few minutes on cloud.Tenable.com, I see 
 that my scan is running. It's running with one scan target. The other thing I could do either from the 
 Stellar Cyber Open XDR platform, or from a command shell and SSH, I can see that there is a job 
 pending on the Modular Sensor. In this example, I will just use a terminal window and I will open up a 
 connection to my Modular Sensor. There we go. I'll type in my password. Then all I need to do is type 
 in  show tenable  . 
 11:00-12:00 
 Here I can see, as I showed you before, that the scanner is linked to cloud.Tenable.com using 443. We 
 also see a scanner has one job pending and that's the scan that's running. Great! This is exactly what 
 we're looking for. I will continue to wait for the scan to complete. Okay. Checking back on the Tenable 
 website. I see that my scan is publishing now, so that's great to see. It looks like it'll be a little bit 
 longer. I will check back again. Okay. I did receive an email showing me that the vulnerability scan 
 was completed. I have my report from Tenable. This shows me that there are some critical severity 
 vulnerabilities that I need to ﬁx on my servers, and I will do that. 
 12:00-12:47 
 That's really cool. I was able to perform the vulnerability scan from my Modular Sensor to servers on 
 the network and then that information gets reported to Tenable. Then Tenable was able to send me a 
 report showing me the results of the vulnerability scan. Then, with a Connector, which is conﬁgured in 
 another module, you can actually get the info from the scans into the Stellar Cyber platform. Thank 
 you very much. I hope to see you in another lesson. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  94 


---

<!-- Página 95 -->

 L24 - MODULAR SENSOR PLATFORM Connector WITH 
 TENABLE 
 L24A-PRES: Modular Sensor Platform Connector with Tenable 
 (30m:26s) 
 00:00-01:00 
 The next lesson is  Stellar Cyber Platform Connectors  Example with Tenable.io (Cloud)  . This lesson, 
 Stellar Cyber Platform Connectors Example with Tenable.io,  explains Stellar Cyber platform 
 Connectors and provides an example of how to conﬁgure a Tenable.io. Connector on the Stellar 
 Cyber platform to collect vulnerability scan data and reports as well as collect assets learned by the 
 Tenable vulnerability scan. 
 Hi everyone. In this lesson, I will cover Connectors. I will also provide an example of using Stellar 
 Cyber Connectors that connect with the Tenable.io service, which is in the cloud. 
 01:00-02:00 
 Stellar Cyber, being an Open XDR platform, has hundreds of built-in Connectors for integrating with 
 security, identity, and infrastructure systems and tools. Looking at the picture on the right, you'll see I 
 have the Stellar Cyber platform, and at the bottom of the platform are Connectors. The Connectors 
 use APIs to connect with cloud security services and apps, infrastructure tools, identity tools. As an 
 example here, the APIs can connect to identity-management tools such as identity platforms Azure, 
 OKTA, Google. They can connect to email services such as Microsoft 365 or Google Mail. They can 
 connect to EDR platforms such as SentinelOne, CrowdStrike, BlackBerry Cylance. 
 02:00-03:00 
 They can connect to vulnerability-scanning services, which is what this example will be, such as with 
 Tenable.io or Qualys and even other tools such as cloud-based, next-generation ﬁrewalls or CASB or 
 WAFs. They could also provide response actions to these as well to block IP addresses and much, 
 much more. The Connectors can also be used to connect with, for instance, Salesforce as an app. 
 Let's go a little bit further now. Connectors are an essential component of the Stellar Cyber Open 
 XDR architecture that enable these third-party integrations with APIs as I just mentioned. Connectors 
 run on Modular Sensors or on the Stellar Cyber platform, depending on which has the best 
 reachability to the security, identity, and infrastructure systems and tools in place. 
 03:00-04:00 
 Connectors to cloud-based systems run on the Stellar Cyber platform, as this provides the most 
 direct reachability to the internet or these cloud systems. Connectors enable automated or manual 
 response actions using third-party integrations. For example, an automated threat hunting, or ATH, 
 playbook can be created to block an IP obtained from an Interﬂow record on a ﬁrewall if an Alert is 
 detected. Another example, when analyzing an Alert, an analyst can trigger a response action to 
 contain an endpoint using an EDR solution. That's pretty cool. They don't actually have to log in to 
 that third-party solution. They can use the APIs right from the Stellar Cyber platform. 
 ADM-03-01-224  95 


---

<!-- Página 96 -->

 04:00-05:00 
 Connectors to on-premises or private cloud systems typically run on Modular Sensors deployed 
 within the same network for direct reachability to these local systems. They can run queries, perform 
 response actions, all directly to the local services or systems. In this example, I have local services, 
 including Active Directory, a ﬁrewall, and a vulnerability scanning service as well, which can be 
 deployed internally within an organization. Stellar Cyber online documentation provides details on 
 whether the Connectors run on Modular Sensors or the Stellar Cyber platform. As an example, I will 
 show you how to connect with Tenable.io. We've already had examples on using the vulnerability 
 scanner on the Modular Sensor, which was from Tenable.io. 
 05:00-06:00 
 Now I'll show you how to build a Connector as well. Therefore, you can see the results of the security 
 scans. Right now if you want to understand what type of Connector and where it goes and how it's 
 installed, you can look at the documentation. You can search for Connector types and functions by 
 going to HTTPS docs dot stellarcyber dot ai. At the very top there's a drop-down box for the speciﬁc 
 version. As per the  Collect  column, if we take a look  at the columns, there's the  Connector  column on 
 the left, the  Collect  column next then the  Respond  column,  Alert Integration  ,  Indices  ,  Runs On  , 
 Interval  ,  External Actions  , and  HTTP Proxy supported  . 
 06:00-07:00 
 Looking at this diagram, I will use Tenable.io Connector to collect data from Tenable.io. If I go to the 
 right, this data will go into the  Scans  indices. It  will run on the DP. The DP is another name for the 
 Stellar Cyber platform and the interval for collection is conﬁgurable. The default is 60 minutes. If I do 
 happen to have an HTTP proxy in my network to get out to the internet, this is supported when 
 conﬁguring this Connector. The Stellar Cyber online help documentation also provides the steps 
 needed to conﬁgure the Tenable.io Connector. 
 07:00-08:00 
 In this example, a Connector will be created for the Stellar Cyber platform to access Tenable.io via 
 APIs that will collect scanning data that was performed by the Nessus client on the Modular Sensor. 
 Pretty cool. Okay. Again, in this example, the Tenable access is going to be cloud at Tenable.com 
 where I have a valid account that I have paid for. Next, after logging into the Tenable cloud platform, 
 select the proﬁle name in the upper right-hand corner of the page. This will enable you to generate 
 API keys that will enable the Stellar Cyber Tenable Connector to access Tenable using APIs. As an 
 example, from the proﬁle of my account, I can go down on the bottom left and select  API KEYS  . Then 
 I can select  Generate  to generate API keys. 
 08:00-09:00 
 Note that if I have other API keys in use, once I select  Generate  , those will no longer be available. 
 Please make sure if you do this that you will not hurt any other types of API integrations that you 
 have. If you have your API key stored somewhere else, then you can use those. But if you need to 
 generate new keys, for example, for a brand new account, then select  Generate  . Again the warning 
 will appear. This will replace any existing keys and unauthorize all applications currently using them. 
 ADM-03-01-224  96 


---

<!-- Página 97 -->

 Are you sure you want to continue? Again, just be very careful with this. If you know it's a new system 
 or your new account, because your account will affect your keys. Alright. I'll continue because this is 
 new for my deployment. 
 09:00-10:00 
 Once this is done, the API keys are generated. Note these keys will not work for you. They've already 
 been erased. You will need both the  Access Key  and  the  Secret Key  to paste into the conﬁguration of 
 the Tenable Connector when conﬁguring it on Stellar Cyber. Next, to create a Tenable Connector that 
 will be run on the Stellar Cyber platform, go to  System  | Connectors  . On the  Connector Overview 
 page, which is step number two, select  Create  . You  can specify the Connector parameters for 
 Tenable.io. First, Tenable.io is a vulnerability scanner. Next, specify the following Connector 
 parameters for Tenable.io. 
 10:00-11:00 
 For step number three, the category select  Vulnerability  Scanner  . Note that there are other 
 categories as well for the hundreds of Connectors available on Stellar Cyber. Please ensure you 
 select  Vulnerability Scanner  . For step number four,  you have the type. Select  Tenable.io  . Note that 
 you'll also see there's a Nessus Connector and there's also a Tenable.SC Connector. Even though this 
 is performing a Nessus scan, the Connector itself is going to cloud.Tenable, which is the Tenable.io 
 Connector. Please make sure you select that. For step number ﬁve, ensure  Collect  is selected. 
 Actually, you don't really have a choice; the Tenable.io Connector is collect only. 
 11:00-12:00 
 You are only provided a single option, which is defaulted to be checked, which is  Collect  . Next, for 
 step number six, specify the name. The name I'm using here is, “SCLABS-Tenable- Connector.” 
 Number seven, select the tenant. Again, if I have a customer that has their own tenant, I could have 
 the Connector only be available for that tenant, but since this is a deployment for my corporation, the 
 root tenant is all I need to specify. Next, as the Tenable Connector is connecting to a cloud service, 
 the  Run On  is for the Data Processor. The Data Processor  is another word that's used to say 
 essentially the Stellar Cyber platform. 
 12:00-13:00 
 When you see Data Processor, it is synonymous with this Stellar Cyber platform. For step number 
 nine, select  Next  . For step number 10, please note  that you have the API keys on Tenable. Again, as I 
 mentioned before on the Tenable.io site cloud.tenable.com, when I log in I have a proﬁle in the upper 
 right-hand corner. When I select my proﬁle, I can scroll down to API keys and select that. If I generate 
 new keys, those keys are displayed, and you must take those keys and put them in a safe place 
 because once you leave that  Keys  page or the  API Keys  page, for example you log out and log back 
 in again, those keys will not be visible again. 
 13:00-14:00 
 In that case, you would have to generate new keys if you did not have them saved. Please note 
 though when you generate new keys, those keys do make the other ones no longer function. 
 Therefore, be very careful when you create or generate new keys. Please make sure you store your 
 ADM-03-01-224  97 


---

<!-- Página 98 -->

 keys somewhere safe. In step number 10, we'll copy the access key and place that in the  Access Key 
 ﬁeld. It's also very important that you make sure you copy all the numbers. What happened to me 
 one of my copies is, for example, on the number six, on the access key at the start, I actually started 
 from number ﬁve. I pasted it and nothing was working, and you're getting frustrated saying why isn't 
 it working? Then you go back and check and you realize, “Oh, I didn't copy the full access key.” 
 14:00-15:00 
 It can deﬁnitely happen if you have a smaller screen you're working with as well. Alright. Make sure 
 you have the full key from the start to the end and paste it into  Access Key  . Next, for the  Secret Key  , 
 do the same thing. Copy the secret key from the ﬁrst number to the last and paste it into  Secret Key  . 
 I'll actually go back a step that's not shown here on the  Interval  , which is below, the  Interval  defaults 
 to 60 minutes. That's how often the Connector will query Tenable.io to ﬁnd if new scans or new assets 
 are created. That should be ﬁne by default. If you have a test environment and you want to see 
 results happen sooner, you can make that a smaller number like, for example, 10 minutes. 
 15:00-16:00 
 In my case though, I will leave this as the default of 60 minutes. Next, is the  Asset Synchronization  . 
 When targets are scanned inTenable, assets get created, which are essentially a representation of 
 the system being scanned. That information can be sent to Stellar Cyber. Stellar Cyber can send 
 Tenable information as well about assets. Select the checkbox for  Asset Synchronization  on step 13. 
 For step 14, if you select the ﬁeld next to  Content  Type  , you'll get a selection box. In that selection 
 box, choose  Scans and Vulnerabilities  . Then for step  number 15, select  Next  . Alright. 
 16:00-17:00 
 You are now done with your conﬁguration. For step number 16, select  Submit  . This is important for 
 on-premises or cloud deployments. This does not apply to SaaS deployments of Stellar Cyber. But 
 when prompted by the Stellar Cyber platform to add the Connector to the default Data Analyzer 
 proﬁle, please ensure you select  OK  . Step seventeen,  select  OK  . If the Connector is not assigned to a 
 Data Analyzer proﬁle, it will not run. Let me reiterate this again. If you select  Cancel  , the status of the 
 Tenable.io Connector will show a gray circle that will inform you that you need to add the Connector 
 in a Data Analyzer proﬁle. 
 17:00-18:00 
 You can ﬁnd the Data Analyzer proﬁle in  System |  Data Analyzer Proﬁles  . Data Analyzer proﬁles are 
 only used for on-premises or private cloud deployments of Stellar Cyber. For SaaS, Connectors are 
 automatically added to the Stellar Cyber platform, so you will not see this pop up. Just for the 
 on-premises or cloud deployments, optionally, you can review the Connectors assigned to a Data 
 Analyzer proﬁle by going to  System | Data Analyzer  Proﬁles  . Then edit the proﬁle. If you look here 
 under  Added  , you'll see the SCLABS Tenable Connector.  You'll also see right above that there's 
 something called  Available  . If you had other Connectors  that you didn't add, 
 18:00-19:00 
 you can select it from the drop down and to the right of the drop down select  Add  . Then when you're 
 done select  Submit  . But if you are now done reviewing  this page and no changes are needed, go to 
 ADM-03-01-224  98 


---

<!-- Página 99 -->

 the upper right-hand corner and click the little  x  to close it out. Now back in  System | Connectors  , 
 after you have created the Connector, on the row of the Tenable scanner Connector, select  Test  . This 
 will come back with a green box hopefully, showing that your test was successful. “Test Success.” Yay. 
 Alright. But, if you did have a problem with for example the keys that you pasted in you'll immediately 
 get an error letting you know that the authentication is invalid. For number 19, if no scans have been 
 performed in the past 24 hours, the status of the Connector will show red. 
 19:00-20:00 
 If you go to cloud.Tenable.com and start a new scan, you have to wait for it to complete to have new 
 data available. Once the data is available on cloud.Tenable.com, you are then waiting for the 
 Connector poll interval. The next time the Connector does a poll, which is every 60 minutes, it will then 
 be able to see this new scan data and pull it in. After the status is healthy or green on the row of the 
 Tenable Connector, select the name of the Modular Sensor to see the conﬁguration settings and 
 detailed status. Next, in  Connector Details  in the  General  section, for step 21, you can view the 
 conﬁguration settings. 
 20:00-21:00 
 For example, you see the name of the Connector that is able to collect data is enabled, the type of 
 Connector which is Tenable.io, whether it can respond, and we know that Tenable Connector does not 
 have response actions, so that's NA. You see the tenant involved, which is the root tenant in this case, 
 and that you could also see that it runs on the data processor, which is the Stellar Cyber platform, 
 and the category, which is vulnerability scanner. For step 22 the status, you can view the last activity 
 and last data received. This is good to know in case there's for some reason you're not receiving any 
 data, but you could also see that you are getting consistent reports. For step 23 you have  Connector 
 Ingestion Over Time  . This lets you view the ingestion  details for security scan data and security scan 
 reports just to make sure that you are receiving them over time. 
 21:00-22:00 
 For step 24 you have  Connector Documents  with our  Interﬂow records. For step 25 you can select 
 View Data  on the upper right to view the Interﬂow  records with the Connector name and the sensor 
 monitoring index selected. After selecting  View Data  from the Connector  Details  page, a ﬁlter will 
 automatically be applied to view Interﬂow records with statistics about the Connector in the sensor 
 monitoring index. Once you have selected  View Data  ,  you're taken to the  Investigate | Threat 
 Hunting  page. You'll see here that there is a search  on Step 26 that says, “Searching for Connector 
 name keyword, SCLABS Tenable Connector AND tenantid,” 
 22:00-23:00 
 which is the root tenant in this case. On step 27, you'll see that the indices is set to  Sensor Monitoring  . 
 In step 28, you will see the Interﬂow are records related to the search and the indices selected. This is 
 just letting you know that the connections are healthy because you are receiving Connector-related 
 sensor monitoring Interﬂow records. For step 29, you go back to  System | Connectors  . With the 
 Tenable Connector status, green or healthy, on the row of the Tenable Connector, select  View Events  , 
 which is step 30. For step 31, after selecting  View  Events  , a ﬁlter will be automatically applied. 
 ADM-03-01-224  99 


---

<!-- Página 100 -->

 23:00-24:00 
 You can then select  x  to clear that ﬁlter if you  want to, but if you want to use this automatically create 
 a ﬁlter, it will get you the data you are actually looking for. In step 32, the indices will be set to the 
 Scans  index. In step 33, you will see the Interﬂow  records from the Tenable Nessus scan that have 
 CVEs, or common vulnerabilities and exposures. This is the meat of it. When you are using the 
 Tenable Connector, this is the data you want to see. Also, by using the Tenable Connector, you can 
 view the assets from the bidirectional sharing with the Tenable Connector from the Tenable scans. 
 When the Tenable scans different devices, that information gets reported back to the Stellar Cyber 
 platform via the Connector. 
 24:00-25:00 
 Now you can view the assets in  Investigate  by selecting  Investigate  , then select  Asset Analytics  . On 
 step three you can select  MAC Identiﬁed Assets  , and  a MAC address is the layer two address for a 
 device. An IP address is layer three. You can select  Filters  to view the ﬁlter sidebar. Step number ﬁve, 
 you can type in  tenableio  as one word, and that will  just help you see the assets that have also 
 been identiﬁed by Tenable. For step number six, if you select the name of an asset, which is a host 
 name, 
 25:00-26:00 
 in the  FRIENDLY NAME  column you get many more details  about that asset. You'll see at step number 
 seven there's an  Asset Details  tab. Next to that is  the risk score. If it's a high risk asset, that number 
 will be higher. You can see the detected name of the host. You can see the reputation. For example, if 
 it's good or malicious or scanner the importance, the tenant that it's in, its location, if there are any 
 tags associated with it again tags are created on the Stellar Cyber platform to help you identify and 
 locate either Interﬂow records or assets themselves. You can see the vendor. In this case, the vendor 
 is VMware because it's actually a virtual machine running windows 
 26:00-27:00 
 and the last time that it reported some information so the last scene. Lots of really good information 
 about assets themselves. You also see the data source. The data sources in this case, where a 
 Tenable.io recognized this asset. The Modular Sensor itself, uh found this asset. We have a Sophos 
 ﬁrewall that found it and Active Directory as well. You can view the summary of Interﬂow records at 
 step number nine and see for example, the risk, the Alerts, the vulnerabilities associated with that 
 asset. In this case I will select the  Vulnerabilities  tab because I have seven of them and I can look at 
 the CVEs or any other detailed information in the Interﬂow records for those vulnerabilities. 
 27:00-28:00 
 The Interﬂow records displayed are related only to that selected asset. That's really cool. Next, you 
 can also view vulnerabilities in the threat hunting library by going to  Investigate | Threat Hunting  in 
 step number one. For step number two, you can select  Threat Hunting Library  . These are 
 pre-canned, essentially dashboards that give you lots of really cool information that are organized 
 based on for example the vulnerabilities themselves or vulnerability scan or if you look at the top 
 here there's AWS CloudTrail, or cloud email providers. It will give you charts related to those speciﬁc 
 services or tools. 
 ADM-03-01-224  100 


---

<!-- Página 101 -->

 28:00-29:00 
 So on step number three, if I go down to  Vulnerabilities  I'll see that I have 1.6k vulnerabilities from the 
 scanning itself. I have useful charts that show vulnerabilities over time, vulnerability scans over time, 
 vulnerabilities by plug in families, vulnerabilities by risk score, vulnerabilities by top assets, 
 vulnerabilities by top CVEs, vulnerabilities as Interﬂow records, lots of really cool information, just 
 available in the charts. Now there are a couple of things that I think are good troubleshooting tips. 
 One is if you look at the symptom, you get it during your test, you get a connection error 
 unauthorized. 
 29:00-29:13 
 Please check auth. Well, as I mentioned before, it is very important to copy the exact access and 
 security keys when creating the Connector. This error usually happens when you have the wrong key 
 or you could have copied from the wrong key on the Tenable.io platform as well or maybe someone 
 selected generate keys after you copied your key, which would then invalidate the keys that you 
 have. Next, if the Tenable Connector shows a red status, this means–or at least in this case–you want 
 to look at the message and what the message says right next to it. The message right next to this 
 one is saying that there's been no data received in the last 24 hours. 
 30:00-30:35 
 What you could do is do a vulnerability scan on cloud.tenable.com, wait for the Tenable scan to 
 complete, and then wait for the interval. It might be a 60-minute interval you have when you created 
 the Connector, before it does the next pull to check if there is data. That's usually the case here. I 
 hope you enjoyed the lesson. Thank you. 
 This lesson is complete. Thank you for watching. 
 L24B-DEMO: Stellar Cyber Platform Connectors Example with 
 Tenable.io (17m:45s) 
 00:00-01:00 
 This lesson continues with demonstrations for S  tellar  Cyber Platform Connectors Example with 
 Tenable.io (Cloud)  . This demonstration explains Stellar  Cyber platform Connectors and provides an 
 example of how to conﬁgure a Tenable.io Connector on the Stellar Cyber platform and on Tenable.io 
 to collect vulnerability scan data and reports as well as collect assets learned by the Tenable 
 vulnerability. 
 Hi. Great to have you back. Now on the previous module, I showed you how to make the Modular 
 Sensor a Tenable vulnerability scanner. Now this is only visible though from Tenable.io or 
 cloud.tenable.com. 
 01:00-02:00 
 ADM-03-01-224  101 


---

<!-- Página 102 -->

 If you want to view the scan, all the results are sent there. However, there's lots of good data that the 
 scans will provide. For example, all the assets that are discovered during the scans. One of the things 
 that we can do to grab that information is to conﬁgure a Connector. For this lesson, I will show you 
 how to create a Connector to cloud.tenable.com. As I've shown you before, the best way to get 
 started with the Connector is to go to the documentation. I can go here or go to docs.Stellar Cyber. I 
 will go to the Knowledge Base home and search for a Tenable Connector. The Connector that we are 
 going to be using is the Tenable.io Connector. 
 02:00-03:00 
 Again, when you go to a help page, one thing if you are searching for a word, it will highlight the 
 word. I like to remove the highlighting. Here I can see the capabilities. With the Tenable.io Connector I 
 can collect information. There is no response because there's nothing I need to do to the Tenable.io. 
 There are no native Alerts mapped to what we collect. We're really going to collect assets. It says 
 here it runs on the Data Processor. In other words, it runs on the Stellar Cyber platform. We 
 conﬁgured an Active Directory Connector previously that was run on the Modular Sensor. 
 03:00-04:00 
 But here, since Tenable.io is in the cloud, then the Data Processor or the Stellar Cyber platform has 
 better access to cloud.tenable.com. We will conﬁgure it on the platform itself. The interval is 
 conﬁgurable. The default interval for the Tenable Connector is 60 minutes. We might change that for 
 our testing. Make it smaller. The information will be in the scan's index. It's also showing me that the 
 message class is security scan. When I do a search I can search for MSG_class:security scan or 
 security scan reports. I can look for message_ origin.source of  tenableio  or  tenableio_reports  . 
 There's also message_origin.vendor. All this will be very handy to have. Okay? 
 04:00-05:00 
 Some other things that are required are the Access key and Security key. I will show you how to get 
 that information from my cloud.tenable.com account. Now I will make sure to change out those keys 
 after I use them so they won't be valid for anyone else. First, I will start from the  System  . To create  a 
 Connector to Tenable.io, I will go to  System  , then  Connectors  . Here I have an Active Directory 
 Connector. I will now create the Tenable Connector. Here the category I should have vulnerability 
 scan. Here it is:  Vulnerability Scanner  . 
 05:00-06:00 
 I will select the  Tenable.io  Connector. There's also  a Nessus scanner, but that's not what we're 
 conﬁguring here. We're conﬁguring the Connector to Tenable.io. Next, the  Collect  option is the only 
 option available to Tenable.io. Again, there is no response action for Tenable. We saw that in the 
 documentation as well. Next, I will give a name. I will call this the “SC (for Stellar Cyber) Training 
 Tenable.io Connector.” Okay. This will be in my root tenant and it will run on the Data Processor. Again, 
 the Data Processor is another name for the Stellar Cyber Open XDR platform. 
 06:00-07:00 
 Next, if there were some speciﬁc ﬁelds or any other types of logs I did not want to gather, I could 
 make a ﬁlter here. But for now I will leave it as default to have nothing ﬁltered. Go ahead and select 
 ADM-03-01-224  102 


---

<!-- Página 103 -->

 Next  . Then here is where I need an Access Key and Security Key. Let me go to Tenable. Here I can 
 see, by the way, that my last scan did complete. If I go to  Settings  . Here on Tenable I can go to my 
 account proﬁle. It's on the upper right-hand corner and view my proﬁle. 
 07:00-08:00 
 Then in here, one of the options is  API Keys  . Now  this is incredibly important right now. When you are 
 conﬁguring API keys, you select  Generate  down here.  But if I'm using API keys already, and then I say 
 Generate  now, notice what happens. There's a warning  message. This will replace any existing keys 
 and unauthorize all applications currently using them. Are you sure you want to continue? In this 
 environment, I have not used any API keys for anything else. So it's okay for me to continue. However, 
 in your environment, you do have to make sure that you will not hurt anyone else. Right? You have to 
 make sure that you don't disable someone else's service. 
 08:00-09:00 
 Again, my account is for me only so I'm not concerned. I do not have keys in use. I will go ahead and 
 select  Generate  .  Continue  and then I have my access  keys. I will make these available for my test. 
 Then of course I will change out these keys by selecting  Generate  again as soon as this lab is over so 
 that these keys will no longer function for anyone else. Sorry, but this is training material, and I do not 
 want anyone else to access my Tenable. Here we go. Next, I will select my access key and make sure 
 to grab the entire number. Okay. I’ve done this before where I haven't and that's also caused 
 problems. I'll go back over here and paste in my access key. 
 09:00-10:00 
 Next, I will go back to Tenable and grab my Secret key. In the Secret key–oops, here we go–I will 
 paste my Secret key here and set the interval to a smaller period of time. In my environment, this is a 
 test environment, I'm going to switch it from a 60-minute polling interval. I will change this from a 
 60-minute interval to a 10-minute interval. Next, for  Asset Synchronization  , I will synchronize the 
 assets collected from Stellar Cyber to Tenable.io and also from Tenable IO to Stellar Cyber. Next, 
 there's the content. I want to grab the scans and the vulnerabilities. Okay. Now I can select  Next  . 
 10:00-11:00 
 The contactor conﬁguration is complete. Let's see if this worked. Go ahead and  Submit  . Here's 
 something that you see only on on-premises or private cloud deployments. You'll see that The 
 Connector has been added successfully. Do you want to add it to the default data analyzer proﬁle? 
 The Data Analyzer is the Stellar Cyber platform. The answer to this question is yes. Yes, you do want 
 to add it. If you are on a SaaS deployment, then you will not be asked this question. It will 
 automatically be deployed to SaaS. Now that the conﬁguration is complete, I see the status is not 
 available. But I can select  Test  . Here I have, “Test  Success!” 
 11:00-12:00 
 Again, if my key was wrong, I would not have, “Test Success.” You will see here though that there's no 
 data received in the last 24 hours. I can take a look at  Events  . There are no events at this time. Now  I 
 will then go to Tenable and start a new scan. Now from Tenable.io, I'll go ahead and create a new 
 scan or actually just to keep it simple. I will modify the scan I already had and I will just change the 
 ADM-03-01-224  103 


---

<!-- Página 104 -->

 target host to a different host. Save and launch. Then I will get another scan. Again, this will take 
 another 30 minutes to an hour. 
 12:00-13:00 
 If I go back over here, I can see if any other previous scans have been collected. It looks like there 
 has. If I go back to the Tenable.io Connector, I see now the status is healthy. Now I can view the 
 events related to the Tenable.io Connector. By selecting  View Events  , what it's actually taking me to is 
 Investigate | Threat Hunting  , and it adds a search  automatically here. This is looking for the Tenable 
 Connector and every event here is displayed from the Tenable Connector. If I look at one of these 
 events here, I can see that they are just events. They are not Alerts. Alright? Notice there's no Alert 
 score. There's no MITRE information here as well. Alright? But I do know I am receiving this traffic. 
 13:00-14:00 
 One of the other options as well if I go to  investigate  and  Asset Analytics  and search for  MAC 
 Identiﬁed Assets  I can now look for any asset that  has been discovered from Tenable.io. If I go to 
 Filters  and look at the data source, I can type Tenable.  I think it's Tenable.io. There we go. All these 
 host names are discovered from Tenable.io. If I scroll down on this list for example, this Windows 
 server, I have discovered it already with my Active Directory Connector. 
 14:00-15:00 
 It's actually been discovered by my Sophos Connector. It's been discovered from the Modular Sensor 
 by viewing the traffic, but it's also been discovered by Tenable.io. Each data source can give 
 additional information about the asset. If I go down to here for example, I can take a look at 
 Vulnerabilities. This would be from the vulnerability scan. If I look over here on the  Vulnerabilities  tab, 
 here I see that I have some vulnerabilities. There's a CVE right here, which is Common Vulnerabilities 
 and Exploits. If I select the Interﬂow record by selecting  More Info  , I can see what was reported by 
 the Tenable.io Connector. If I go to  Details  and scroll  down, I can see that the vulnerability output was 
 that there's a medium-strength cipher. 
 15:00-16:00 
 This just gives you an idea of what each of the line items in the report has and it applies it to this 
 asset. I can use that in my threat investigations. Really, really cool integration here with Tenable.io. 
 The next thing I can do is go to  Investigate | Threat  Hunting  . I can also look for Alerts. Before we 
 looked for a message origin source, if you remember in the documentation there were some ﬁelds 
 here: message origin source Tenable.io and Tenable.io Reports. Let me see what happens if I go to 
 Investigate | Threat Hunting  . 
 16:00-17:00 
 I'll close the ﬁlter I'll type in:  msg_origin.source:tenable.io  .  Let's make sure that's correct. Yep, 
 that is correct. I can also do underscore reports. Here, oh my god I have nothing. Why? The reason is 
 because there is no Alert. However, if I go to  Scans  ,  now my message origin source shows me the 
 Tenable. There are 35 Interﬂow records based on the message origin source of Tenable.io_reports. 
 Now let's see what happens if I say just Tenable.io. 
 ADM-03-01-224  104 


---

<!-- Página 105 -->

 17:00-17:45 
 Now I have a lot more. Okay. If I look at these, again these will show me the CVEs. This is the output. I 
 can see you know the vulnerabilities that have been found. Okay. If I look at the  Details  or the JSON,  I 
 can see the information about the source and the scan that was performed and see the CVEs related. 
 Right? There's the CVE ID. I can also see it right from here as well. Okay. That's the integration with 
 Tenable.io. That's pretty cool. Thank you for watching. 
 This lesson is complete. Thank you for watching. 
 L25 - MODULAR SENSOR ACTIVE DIRECTORY (AD) Connector 
 L25A-PRES: Modular Sensor Active Directory (AD) Connector 
 (13m:22s) 
 00:00-01:00 
 The next lesson is  Active Directory Connector Details  and Conﬁguration.  This lesson,  Active Directory 
 Connector Details and Conﬁguration  , provides details  and explanations of how to conﬁgure an Active 
 Directory Connector on Modular Sensors to collect Windows event logs, user behavior and computer 
 asset information, as well as perform response actions from the Stellar Cyber platform to disable 
 users in Active Directory. 
 Hi everyone. Great to see you again. In this lesson, I will cover Modular Sensor, Active Directory 
 Connector details, and conﬁguration. 
 01:00-02:00 
 Stellar Cyber Active Directory Connectors run on Modular Sensors for Stellar Cyber to ingest data 
 from Active Directory and add as Interﬂow records to store in the Stellar Cyber platform. Because 
 Modular Sensors are deployed within an organization's network, the Modular Sensors have access 
 using LDAP to the Active Directory servers. They can perform LDAP search to obtain information 
 about users and computers within the organization. They can also use LDAP to set a parameter, for 
 example, to disable a user with an Active Directory. This could be done from inside the platform and 
 we'll discuss more about that later. 
 02:00-03:00 
 Stellar Cyber Active Directory Connectors provide key capabilities such as enriching event Interﬂow 
 records with user and computer information from Active Directory and supporting Windows Event 
 Collector. Now, I want to make sure that we discuss some prerequisites. Before getting started with 
 conﬁguring an Active Directory Connector that can collect data and perform response actions to 
 disable and enable users in Active Directory, it is recommended you conﬁgure a dedicated user or 
 group with speciﬁc permissions for the Connector. In this example, an account named 
 stellarconnector will be used that is a domain user and a domain admin. Now for a very important 
 note: To collect data using the Active Directory Connector, only domain user privileges are needed. 
 ADM-03-01-224  105 


---

<!-- Página 106 -->

 03:00-04:00 
 To provide response actions to disable the user, elevated permissions are needed, and that is why the 
 user in this example has been assigned to the administrator group. This level of privilege is not 
 required. But it is easy for lab environments. Please check with your Active Directory administrator to 
 use the correct permissions needed for disabling and enabling user accounts in your Active Directory 
 environment. If we take a look at a user in Active Directory, I have an account named 
 stellarconnector at sclabs.ai. If I look at that picture right below that, that's the member of. Here you 
 can see the user is a member of administrators and a member of domain users. 
 04:00-05:00 
 What I could have done instead of assigning the user to the administrators group is to delegate the 
 permissions. One of the options in Active Directory is to select an organizational unit such in my case 
 as sclabs.ai or the user's container. I can say delegate the user account control permissions. There's 
 read user account control, and there's write user account control permissions. I can use those instead. 
 Our documentation explains how to do that in the Active Directory Connectors documentation. To 
 create an Active Directory Connector that will run on a Modular Sensor, in the Stellar Cyber platform, 
 perform the following steps. Go to the  System  menu  on the top and select  Connectors  . 
 05:00-06:00 
 On the  Connector  Overview  page, select  Create  . Specify  the following Connector parameters. For 
 step number three, select  IdP  for identity provider.  That will narrow the types you see on the next line. 
 For the  Type  , select  Active Directory  . For the  Function  in this example, I will use  Collect  and 
 Respond  . Because there are different permissions that  are required for  Collect  than there are for 
 Respond  , some organizations create a separate Connector  for collect and a separate Connector for 
 respond. This way, the elevated permissions are only used on the respond Connector that's used to 
 disable users. 
 06:00-07:00 
 In this example, I will select both. Next, specify a name for the AD Connector. I like to use the host's 
 name within the name of the Connector, mainly because some organizations have hundreds of 
 Connectors because they have hundreds of different Active Directory servers at different sites. By 
 putting the host name in the name I can clearly identify which Connector this is. Also, in this example, I 
 have the  Tenant Name  for Root. I don't have any other  customers and I don't have any other 
 tenants, so everything will go into the root tenant. But if I did have other tenants, I could specify a 
 Connector within a tenant. 
 07:00-08:00 
 Next, I'm going to run the AD Connector on a Modular Sensor. This is also where the naming of the 
 Modular Sensor makes a big difference. If you have lots of different sites, please make sure that the 
 name of your Modular Sensor represents the site or even the tenant that the Modular Sensor belongs 
 in. Otherwise, you could possibly choose the wrong Modular Sensor. In my case, I have one so it's 
 pretty easy. Select  Next  . Next, for step number 10,  enter the  Active Directory Domain  . The domain 
 ADM-03-01-224  106 


---

<!-- Página 107 -->

 name is not case sensitive. Then enter the  Server Hostname  , which is the Active Directory server 
 fully qualiﬁed domain name, or FQDN. You can also use an IP address. 
 08:00-09:00 
 This  Server Hostname  is also not case sensitive. In  this example I've used both upper case and lower 
 case to show you that it doesn't make a difference. Also in Windows, often you will see the domain 
 names in uppercase. Next, for step number 12, the  Interval  by default is ﬁve minutes. I will leave  it at 
 that. This is how often the Active Directory Connector on the Modular Sensor obtains event logs and 
 user information and computer information from the Active Directory server. For step number 13, 
 enter the  User Name  . If performing response actions to disable a user, this user must have 
 permissions for read and write user access control. 
 09:00-10:00 
 Those permissions can be delegated from within Active Directory. For ease of testing in a test 
 environment, you can use a domain admin group. That's what I've used for the stellarconnector here. 
 For step 14, enter the  Password  that is assigned to  the user name that was entered in the step before. 
 For step 15, enter the  Content Type  . By default, the  Active Directory Connector collects user behavior 
 information, and it will always do that. This option for  Content Type  here is to collect computer 
 information as well that will be viewable in  Assets  in the Stellar Cyber platform. The Active Directory 
 Connector conﬁguration is complete. 
 10:00-11:00 
 For step number 16, select  Submit  . For step 17, on  the row of the Active Directory Connector, select 
 Test.  Within a minute you should receive a green box  with, “Test Success!” Then the status should turn 
 green within ﬁve minutes as that is my polling interval. For step 20, after the status turns green, select 
 the name of the Connector to get details and status information. From the  Connector Details  , you 
 can verify the Connector is functioning and ingesting data. 
 11:00-12:00 
 Step 21, you can view the conﬁguration settings. Here, I see the name and type and tenant category 
 and that it is able to collect data from Active Directory and respond within Active Directory. It's run on 
 the name of the sc-modular-sensor. That is good general conﬁguration settings there. For step 22, 
 there's the status. You can view the last activity and last data received. Here you know that the 
 Connector is functioning, especially if the time is recent. For step 23,  Conﬁguration  , you can view  the 
 conﬁguration details. Here I see the Active Directory domain. 
 12:00-13:21 
 I see the  Server Hostname  , the  Interval  I conﬁgured,  the  User Name  that was assigned to this 
 Connector. I can see the  Protocol  Type  that I assigned.  In this case, it was LDAP. Also I have the 
 Content Type  , which is obtaining information from  computers. But it also is grabbing user 
 information that is happening by default.  Content  Type  really should be users and computers, but 
 users is by default, so it doesn't show up here. For step 24, there's  Ingestion  . You can see if you are 
 getting ingestion data. That means the Connector is deﬁnitely working and healthy. You also have 
 Connector Documents  . This shows that data is being  collected from Active Directory for computers 
 ADM-03-01-224  107 


---

<!-- Página 108 -->

 and users. This is really just the Connector communication logs and it's not related to actual events 
 or Alerts. With all the data we see here, we know the Connector is successfully collecting data. 
 This lesson is complete. Thank you for watching. 
 L26 - AD Connector COLLECTION OF ASSET & USER DETAILS 
 L26A-PRES: AD Connector Collection of Asset & User Details 
 (09m:19s) 
 00:00-01:00 
 The next lesson is  Active Directory Connector Collection  of Asset and User Details.  This lesson,  Active 
 Directory Connector Collection of Asset and User Details,  explains how to view the asset and user 
 behavior information collected by the Active Directory Connector in the Stellar Cyber Open XDR 
 platform. 
 Hi everyone. In this lesson, I will show you the assets and computers that are collected by the Active 
 Directory Connector from Active Directory. Now that we've actually conﬁgured the Active Directory 
 Connector appropriately, now we can check by going to  Investigate  then go to  Asset Analytics  . 
 01:00-02:00 
 From here, you can search for the assets collected from Active Directory. To do that for step number 
 three, select  Filters  . That will expand the  Filters  bar. Then select  Data Source  ,  at which point you  can 
 enter active_directory. Here, the asset list is ﬁltered to show only assets learned from Active 
 Directory. Looking at the list I have here, under  Friendly Name  , those are my Active Directory servers 
 that were learned from the Active Directory Connector. For step number ﬁve, you can select the 
 hostname of an asset from the  Friendly Name  column  to view the  Asset Details  . 
 02:00-03:00 
 For step number six, you can see the  Asset Details  ,  which contains the risk score. In this case it’s 16.7, 
 so this server is not a high risk. You can see the name, which is the hostname of the Active Directory 
 server. I can see the  Tenant  . If I had multiple tenants,  this would be very helpful because now I know 
 which tenant it belongs to. I can see its  Location  and even the location on the map along with any 
 Tags  that might be assigned to it so I can ﬁnd it  quicker in searches. I can see the  Vendor  and lots  of 
 other good information including the operating system. Going a little bit further down I can view the 
 Data Sources  . Here I see that Active Directory is  one of the data sources. 
 03:00-04:00 
 You could have multiple data sources reporting information for each asset. Here I actually have 
 Tenable.io reporting information, the Modular Sensor itself from network traffic, and Sophos, which is 
 a ﬁrewall. That's pretty cool. For step number eight, you can view a summary of the Interﬂow records 
 for risk Alerts and vulnerabilities. As an example, I can see the latest risk score. See the Alerts over the 
 past month, the Alerts, the vulnerabilities, commands that have been detected, logins that have been 
 ADM-03-01-224  108 


---

<!-- Página 109 -->

 detected, login failures, and ﬁles. On step number nine, I can scroll through the tabs from left to right 
 to view the related Interﬂow records. For example, I have the  Alerts  tab selected. 
 04:00-05:00 
 Here, in the column, I see all the CVEs, which are the Common Vulnerabilities and Exposures. Each of 
 those can be looked up on the internet to determine what they are or you go into  More Info  and the 
 Actions  column to view the detailed information. For  step number 10, the Interﬂow records displayed 
 are related to the selected asset only, so that's really cool. If I just want to see if this server has been 
 having any threats involved, you can go here to view those threats. Similar to how the Active 
 Directory Connector uses LDAP to collect information about assets, it also uses LDAP to search and 
 obtain user information from Active Directory. To view the user information, you can go to 
 Investigate | User Behavior Analytics  . 
 05:00-06:00 
 For step number two, select the  Users  tab. For step  number three, when a user and associated data 
 is collected from the Active Directory Connector, the  Data Sources  column shows Active Directory. 
 Note just like with assets, there might be multiple data sources reporting information about users. If 
 you look at the last one, which is the administrator, both the Windows Server sensor, which is called 
 Windows agent here and the Active Directory Connector are reporting information about 
 administrator. For step number four, select the name of a user to get details collected by the Active 
 Directory Connector from Active Directory that will be stored in the platform. 
 06:00-07:00 
 For step number ﬁve,  User Details  contains the name,  job title, principal name, privilege level, last 
 login, last password set, and much more. This information is very useful when you are running 
 through the events and Alerts on the Stellar Cyber platform. Having access to the user information 
 makes it much easier to identify who is involved and what is involved in identifying threats. For step 
 number six, the  Data Source  is Active Directory. For  step number seven, you can select  Show More 
 at the very bottom to get much more data about the user. 
 07:00-08:00 
 After selecting  Show More  on the previous step, you  can see much more detailed information 
 including the  Proﬁle  ,  Bad Password Count  ,  CN  , the  Member Of  groups. All of this can help determine 
 the level of risk especially when able to view permissions assigned to the user when identifying risks 
 and threats. For step number nine, you can view a summary of the Interﬂow records for risks, Alerts, 
 vulnerabilities, and more. Looking at the charts, I see the latest risk score. I see the Alerts associated 
 with this user, commands that the user might have typed, the authentications, the login failures and 
 ﬁles. If I go to step number 10, there's a set of tabs there as well. 
 08:00-09:19 
 I can scroll through them to view the Alerts, related assets, commands, authentications, login failures, 
 and ﬁles. Step number 11 one of the ones I ﬁnd really cool is the  Related Assets  tab. You can view the 
 other servers that this user has been associated with and has logged into. If I go to step 12, if I select 
 the three stacked dots next to an asset, I can get even a lot more information about the assets that 
 ADM-03-01-224  109 


---

<!-- Página 110 -->

 the user has logged into. For example, I can get the  Asset Details  view for that asset, I can do a 
 VirusTotal lookup to see if there's anything bad about that asset that has been detected by other 
 sources. I could even copy as a query so that I don't have to write down that host name, and I can 
 use that copy as query to paste into the search bar, maybe to look for that and other items as well to 
 help me investigate a threat. 
 This lesson is complete. Thank you for watching. 
 L27 - AD Connector RESPONSE ACTIONS TO DISABLE A USER 
 L27A-PRES: AD Connector Response Actions to Disable a User 
 (17m:42s) 
 00:00-01:00 
 The next lesson is  Modular Sensor Active Directory  Connector Response Actions to Disable a User. 
 The next lesson is  Modular Sensor Active Directory  Connector Response Actions to Disable a User  . 
 Hi everyone. In this lesson, I will provide an example of how to conﬁgure and use an Active Directory 
 Connector with response actions. With the Stellar Cyber Active Directory Connector on the Modular 
 Sensor, a response action can be performed automatically using automated threat hunting 
 playbooks, or ATH playbooks, or manually by an analyst on the Stellar Cyber platform viewing an 
 Interﬂow record. 
 01:00-02:00 
 When an analyst is alerted to a threat, an action can be taken from the Interﬂow record to disable a 
 user in Active Directory. Viewing the Interﬂow record on the platform there will be an option to take 
 actions. From there, you specify the Connector, which is on the Modular Sensor. Then you can select 
 Submit  to send an LDAP-modiﬁed query to change the  user to disabled in Active Directory. That's 
 pretty cool. I didn't actually have to call an administrator of Active Directory to do that task. But you 
 can also specify duration. You don't have to disable the user permanently. You can say, “Hey look 
 while I'm investigating, I think there's a signiﬁcant possibility the user has a problem. 
 02:00-03:00 
 Therefore, I will disable that user for a certain amount of time.” I could say ten minutes or an hour, 
 just to make sure that the user will not be compromised any further or compromise any other 
 machines any further. Alright. In this example, I'm showing a duration of ﬁve minutes, but that's just 
 for a test. Response actions to disable a user with the Active Directory Connector could be taken 
 from several different places in the Stellar Cyber Open XDR platform. I will give you a quick overview 
 of each of the locations. For number one, you can go to  Investigate | User Behavior Analytics  , and 
 select the  Users  tab. From the  Users  tab, there's  an option in the  Actions  column to disable a user. 
 03:00-04:00 
 ADM-03-01-224  110 


---

<!-- Página 111 -->

 For step number two, for analysts that are investigating Interﬂow records, you can select  More Info 
 for Interﬂow records to get to select an  Actions  tab. On the  Actions  tab there's an option to disable  a 
 user there if the Interﬂow record has users within the record. For step number three, another location 
 is from the  Respond | Actions | User Actions  menu.  Here you can disable a user right from this 
 screen. On step number four, if you are using Case management to analyze a Case, which is a 
 collection of Alerts, there is a response section there where you can again disable a user if there are 
 users involved in the Case. 
 04:00-05:00 
 For step number ﬁve, there's also the  Respond | Automation  ,  which is the ATH Playbooks inside an 
 ATH playbook based on the condition, you can have it automatically trigger an action to disable a 
 user. Or you create the ATH playbook, and then that playbook can manually be selected at any time 
 as well. To perform a simple test to disable a user from the Stellar Cyber platform, using the Active 
 Directory Connector on a Modular Sensor, go to  Investigate  | User Behavior Analytics  , then select 
 the  Users  tab. This is really important. Next to a  user,  do not  disable the Active Directory Connector 
 user. 
 05:00-06:00 
 In this case, mine is called stellarconnector. You deﬁnitely don't want to disable the stellarconnector 
 because that is the user that is actually performing the response actions. Also, what's very important 
 is you probably don't want to disable the administrator account unless of course that administrator is 
 compromised, but especially if you're running a test, please just make sure to disable a test user. For 
 step number four, you can select the Active Directory Connector. For step number ﬁve, for the 
 Duration  you can select  Forever  , but especially if  it's a test environment, you can select  Limited  .  At 
 that point you can specify either the days, hours, or minutes. 
 06:00-07:00 
 After the duration is complete, the user will be re-enabled by the Stellar Cyber Connector. For step 
 number seven, verify that the name is correct. That was the name that you clicked on to disable the 
 user in Active Directory. It should be correct because that's what you selected. But just to make sure. 
 Then for step number eight, select  Submit  . You should  get a message that says the disabled user was 
 created successfully. It just means that the disabled user action was created successfully. It does not 
 mean that the user was disabled yet. To verify that, you go to the  Respond | Actions  menu. 
 07:00-08:00 
 From the top menu bar, select  Respond  , then  Actions  .  For step number 10, you can select the  User 
 Actions  tab. It defaults to the 100 most-recent actions,  but you can go to the  User Actions  tab. From 
 the  User Actions  tab, you will see that a user has  been disabled or is being disabled. But you might 
 look at it and go wait a minute. Like in my example, this time it's S-1-5-21- all the way ending in -1117. 
 Well, depending on how the user was found, especially from Active Directory, you might just see the 
 SID value when you are in the user behavior analytics, if you do select a user, one of the options is a 
 Real ID  tab. In the  Real ID  tab, you can see the SID. 
 08:00-09:00 
 ADM-03-01-224  111 


---

<!-- Página 112 -->

 In this case you'll notice that 117 was the user that was successfully disabled. All good here. If you 
 need to undo the disable action, by the way, you do have a safety net. You can select  Revert  . If you 
 disable the Active Directory Connector username, then you will not be able to revert. Next, when 
 viewing Alerts that contain usernames from Active Directory, the Active Directory Connector on a 
 Modular Sensor could be used to disable users from the Interﬂow record without having to log in to 
 Active Directory. That's pretty cool. If you go to  Investigate  on step number one,  Threat Hunting  , 
 you can verify the indices here. I have  Alerts  selected.  You could also select  Windows Events  , 
 09:00-10:00 
 especially if you don't see any Alerts yet. When viewing Cases and Alerts, SOC analysts, based on the 
 type of Alert, can disable users while they are investigating a threat. As the goal for this lesson to 
 understand how to disable a user, search for Alerts with users to test the ability to disable users. In 
 other words, if you just start going through the platform and selecting Alerts at random, you may not 
 ﬁnd an Alert that you can disable a user from. As step number three shows in the search, type the 
 following:  smb_username:*  . That says look for any  Alert with the SMB_ﬁeld. 
 10:00-11:00 
 An SMB is a Windows username. There are other ﬁelds as well. Optionally, as step number four 
 shows, there's the Interﬂow dictionary. If you are not sure what other usernames are involved in the 
 Interﬂow records that you have collected, you can use the Interﬂow dictionary and use command f, 
 which is a browser search or control f on Windows, command f on on Mac, to ﬁnd all ﬁelds related to 
 a certain word like username. You can type in  command  f username  , and then you can scroll 
 through looking for every single ﬁeld name that has a username value in it. You can select that to see 
 if you have any usernames collected and you can see the values of the usernames and then ﬁlter the 
 records right from there. 
 11:00-12:00 
 The  Interﬂow Dictionary  is cool. I will provide a  demonstration of that capability, but for now, SMB 
 username works in my environment. For step number four, now that I've searched for SMB 
 username:*, I will select one of the Interﬂow records that shows up in the list of documents that you'll 
 see if you scroll down essentially on the  Investigate  | Threat Hunting  page. For step number ﬁve, 
 within the Interﬂow record, you can go to  Details  .  You can now look for the SMB username to scroll 
 down to ﬁnd it. They are in alphabetical order. If you are using another name or you're not sure, 
 select a record. 
 12:00-13:00 
 You can scroll down and look for anything that looks like a user and then see if you can use that ﬁeld 
 name instead. You need to know the ﬁeld name for disabling a user. In this case SMB username will 
 work ﬁne. But you might also have something like desktop username, source IP username, target 
 username so there there's other username ﬁelds that may appear in Interﬂow records related to 
 Active Directory. For step number seven, select  Actions  .  In the actions for the Alert, one of the 
 options, again since the username is in the Alert and I have an Active Directory Connector, I do have 
 the ability to disable the user associated with this Alert. I have other options as well, such as adding a 
 ﬁlter or a tag or running a script. 
 ADM-03-01-224  112 


---

<!-- Página 113 -->

 13:00-14:00 
 I could even contain an endpoint depending on if I have an EDR associated with it. But for now, 
 Disable User  is what we are trying to show. Note,  if you do not have  Disable User  as an option that 
 means there are no username ﬁelds in the Alert Interﬂow record. You'll have to ﬁnd another Alert with 
 a username. In the  Disable User  conﬁguration box,  one is you can select the Connector. Now again if 
 you have lots of Connectors, this is why it's important to make sure that you name your Connectors 
 speciﬁcally related to the host they're going to connect to. In my case, I know exactly that this is my 
 SCLABS-WINAD-San Jose training DC1. 
 14:00-15:00 
 It's a domain controller and it's the ﬁrst one. The duration I'll set a time for will be ﬁve hours. Maybe 
 I'm going to be investigating this Alert. I've already called the user to let them know that I'm disabling 
 their account. It depends on what type of Alert it is. Now for the disable user, if you select the box 
 next to  Disable User  , you can start typing in a username  ﬁeld. I know my username ﬁeld is called 
 SMB_username. I start to type  sm  . As soon as I do  that I start seeing the list of entries that match. I 
 can select SMB username in this case, and then select off the box. That will then show you that you 
 have that SMB username selected. 
 15:00-16:00 
 Next, I can select  Submit  . After you select  Submit  ,  the green success box is displayed with a note to 
 check the status in the  Respond | Actions  table. Again,  the user is not disabled yet at this time. By 
 viewing this table we can see the status. From the  Respond | Actions  menu, I see the table here. I can 
 go to the  User Actions  tab. I see the username. It's  the target user, which is the SMB username. I see 
 that the disable user action succeeded. You can see the time and you can see where the Connector 
 was run, which in this case, is the SC-Modular Sensor. 
 16:00-17:00 
 Alright. If you get here a little early, it might take about a minute for it to complete. You will see the 
 progress in the  Status  column as you're waiting for  it to succeed. In this case, the respond action for 
 disabled user was successful, so I'm pretty happy about that. If I wasn't happy though, for example, I 
 go, “Shoot, I should not have disabled that user.” That's my boss and my boss was doing something 
 very important. You can revert. Right? You do have a safety net that you can use. If you are an AD 
 administrator, you can go to Active Directory and take a look at the user itself. 
 17:00-17:42 
 In my environment, I went to  Users  , and in Active  Directory you'll see that Paul Levasseur has a little 
 down arrow next to the name in the user's icon. That lets you know that that user is disabled. If you 
 want to enable the user from Active Directory, I can right-click on the username and re-enable that 
 user. Yes, this user was disabled successfully. 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  113 


---

<!-- Página 114 -->

 L27B-DEMO: AD Connector Response Actions to Disable a User 
 (20m:05s) 
 00:00-01:00 
 This lesson continues with demonstrations for  Modular Sensor Active Directory Connector 
 Conﬁguration and Use  . This demonstration provides step-by-step details for conﬁguring an Active 
 Directory Connector on a Modular Sensor, setting the proper permissions in Active Directory for data 
 collection and response actions using the Active Directory Connector and provides examples of 
 viewing computer and user data, as well as disabling a user from an Interﬂow record in the Stellar 
 Cyber Open XDR platform. 
 Hi everyone. In this lesson, I will show you how to conﬁgure an Active Directory Connector that will 
 run on a Modular Sensor. With the Active Directory Connector, you will be able to collect assets which 
 are computer information, 
 01:00-02:00 
 and you'll be able to gather user behavior analytics information, which are from the user accounts in 
 Active Directory. Before getting started creating a Connector, what I like to do ﬁrst is go to the 
 documentation. I can search for Connector types, and functions. The ﬁrst entry that appears is 
 Connector Types and Functions  . From the  Connector  Types and Functions  documentation, I can see 
 what the Connectors are capable of doing. If I scroll down to all Connectors, I can look at the ﬁrst 
 column is  Connector  that gives the Connector name. 
 02:00-03:00 
 The  Collect  column speciﬁes that the Connector is  able to obtain information from the system it 
 works with. The  Respond  column means that the Connector  can actually perform some type of 
 response, such as disabling a user or containing an endpoint.  Alert Integration  lets me know if 
 there's special machine learning integration or some rules that are in the Stellar Cyber platform that 
 apply to this Connector. The  Indices  column speciﬁes  the indices the data collected goes into.  Runs 
 On  means that the Connector can run on a Data Processor,  which is another name for the Stellar 
 Cyber platform, or a sensor, such as the Modular Sensor. The  Interval  is how often Connector pulls 
 the system it is working with. These are the main settings that we are going to delve into right now. 
 03:00-04:00 
 If I scroll down a little bit, I'll ﬁnd the  IdP  section.  I see Active Directory. Again, IdP is identity provider. 
 This category name will also be used in the conﬁguration of the Connector. This shows the  Collect 
 column that the Active Directory can collect data from Active Directory. The  Respond  column shows 
 that the Active Directory Connector can perform response actions, in this case to disable a user. 
 Windows is the index or indices where the data collected by the Connector will go. The Active 
 Directory Connector will run on a DP or sensor. The  Time Interval  is conﬁgurable, and the response 
 or external action is the ability to disable a user. 
 04:00-05:00 
 ADM-03-01-224  114 


---

<!-- Página 115 -->

 Now from the  System | Connectors  page, I will create an Active Directory Connector by selecting 
 Create  . The category is IdP. That's what we read in  the documentation. For the  Type  , we're going to 
 choose Active Directory. Note you can create Connectors for other identity platforms as well. The 
 Function  will be for collecting and responding, so  collect and respond.  Collect  means I'm obtaining 
 user and computer and event logs.  Respond  as I am  disabling a user. For the  Name  I like to use the 
 hostname of my Windows AD server in the name of the Connector. Because I could have hundreds of 
 Connectors in my organization. I might have hundreds of servers in my organization. 
 05:00-06:00 
 What I want to do is go to my Active Directory and make sure I'm using the right hostname. One of 
 the easiest ways is just from a command prompt and Active Directory. I will obtain the hostname 
 here and I'll go back. I will call this, “SC,” for Stellar Cyber and I will paste the hostname, and then use 
 the word, “Connector.” I will install this in my root tenant. If I had other tenants with the Active 
 Directory server, I would create it speciﬁcally for those tenants. I'm going to run it on this Modular 
 Sensor. Even though I have log ﬁlters conﬁgured, I do not need any log ﬁlters for this Connector right 
 now. Eventually if I ﬁnd that there are Windows Events I do not want to import, 
 06:00-07:00 
 I can go ahead and add log ﬁlters here. Then select  Next  . Next, on the  Conﬁguration  step, the Active 
 Directory domain in my lab is sclabs.ai. The  Server  Hostname  is the fully qualiﬁed domain name of 
 the server or the IP address. You cannot just put the hostname itself. Now I copied the hostname. This 
 can be uppercase or lowercase–it doesn't matter–SClabs.ai. Now this is the fully qualiﬁed domain 
 name for the Active Directory server. The  Interval  is how often the Active Directory Connector 
 obtains user information, computer information, and event logs from Active Directory. 
 07:00-08:00 
 The  User Name  is a user that I dedicate directly for  this purpose, the purpose of having a Connector 
 to obtain information. Now one of the best ways to do this is to go to Active Directory and create 
 yourself an account. Here I go to  Tools  on my Active  Directory server,  Active Directory Users and 
 Computers  . I have created a user called Stellar Connector.  This is just a domain user. Now in order to 
 collect information from Active Directory, this user only needs to be a domain user. I can see this by 
 going to  Member Of  . 
 08:00-09:00 
 If I go to  Member Of  , I will see that this user is  only a domain user. To create a response action from 
 the Connector to Active Directory, the user needs to have elevated permissions. The user needs to 
 have permissions for read and write account control. I can do that by going to sclabs.ai, which is my 
 organization. I can right-click that and specify  Delegate  Control  . From here it brings up a wizard 
 where I can specify the permissions that the user can have. I'll go ahead and select  Users  and 
 Groups  . I will add and select my Stellar Connector  user. I just hit  Return  and when you hit return it'll 
 ﬁnd it. Then I go ahead and select  Next  . 
 09:00-10:00 
 ADM-03-01-224  115 


---

<!-- Página 116 -->

 At this point I will create a custom task to delegate. I then will only delegate for the following objects 
 in the folder. That will be all the way at the bottom. It'll be the user objects. Then I select  Next  . For  the 
 permissions I can remove the general and I will select a property-speciﬁc permission and I'm looking 
 for user account control. This will be alphabetical from the second column. I'm going to scroll down 
 nice and neat and ﬁnd l m n o p q r s t u and ﬁnd let's ﬁnd user. There it is right there: 
 10:00-11:00 
 Read userAccountControl and Write userAccountControl. I'll select  Next  , and that's it. If I scroll down 
 here it says for that domain sclabs.ai. The Stellar Connector user will have the following permissions: 
 Read userAccountControl and Write userAccountControl. For the following object types: User. Perfect. 
 That's all I need. Now back on the platform, I will specify my username, which is stellarconnector. I will 
 enter my secret password. This should be a really good and complex password. The protocol type is 
 LDAP that I will use. 
 11:00-12:00 
 You could use LDAPS, which is a secure or more secure version of LDAP and kerberos. In my 
 environment I will use LDAP as my Modular Sensor is on the same network as my Active Directory 
 server. Now by default, the Active Directory Connector collects user behavior information and event 
 information. But if I want to also collect computer information that will be in the  Investigate  Assets  , 
 then go ahead and select the content type of computers as well. This is really computers  and  user 
 information. Select  Next  . I will select  Submit  . My  Active Directory Connector has been conﬁgured, but 
 it's not functioning yet. Notice the status right now. 
 12:00-13:00 
 It's not available, but what I can do is try to test. This takes about 30 seconds to a minute. I'll wait right 
 here. Here I see, “Test Success!” I see an error. That is okay. That's really just saying there's been no 
 data received in the past 24 hours. Within the ﬁrst ﬁve minutes though this Connector will turn green. 
 Okay. It's been a couple of minutes, and now my status is healthy. If I take a look now at the 
 Connector, I will see that the name of the Connector is here. I see that it's run on the Modular Sensor. 
 It has both collect and respond capabilities. 
 13:00-14:00 
 It shows me the last activity, which is a minute ago. It also gives me the conﬁguration settings such as 
 the  Active Directory Domain  , and the  Server Hostname  and the time  Interval  for how often it 
 collects and the  User Name  associated with this Connector.  The fact that I'm using LDAP and the 
 content type is also pulling users and computers. If I look over here, I can see that here in the legend 
 as well. It's collecting computer information and Active Directory user proﬁles information. When you 
 look down here, this is letting you know that the Connector is communicating with the Active 
 Directory server and it's obtaining AD computer information and AD user information. These aren't 
 event records. These are really Connector records. Okay. Now I'll go back to  Investigate  | Threat 
 Hunting  . What I'll see here is this. 
 14:00-15:00 
 ADM-03-01-224  116 


---

<!-- Página 117 -->

 I have the  Time Interval  set for the last 30 minutes. If I deselect  Alerts  , remember that when we 
 looked at the documentation, the Connector traffic is going to the Windows Events. I see here in the 
 last 30 minutes I now have 15,000 Windows Events I have collected. If I look at one of these events 
 again these aren't Alerts, these are the events themselves. Looking at the details, I can see the event 
 that was collected from the Active Directory server. Over time if I get Alerts, the Alerts also might be 
 associated with the Connector. But if I look over here I also have the username. I've collected some 
 username details. If I go to  Investigate | User Behavior Analytics  I can look at the list of users in the 
 last 30 minutes. 
 15:00-16:00 
 In this case, it did pull administrator and a system account. If I go back in time a little bit further now 
 because I've actually been using this Active Directory Connector before I installed it, I had it installed 
 previously. It was able to collect more information for users as well. My Connector will do the same 
 thing in a couple of minutes. But if I take a look at my username, I can see that it was able to grab my 
 Principal Name  , my  Job Title  , my  Company  . I grabbed  all the information from my user account, 
 and you'll see the data source is Active Directory. If I go down a little bit further, I'll also see the 
 number of times that it's located  Authentications  and  Alerts  . Records associated with 
 authentications and an Alert over here as well. 
 16:00-17:00 
 If I look at the Alert, I see that there was an external ﬁrewall deny action. Here I can see the Alert. If I 
 go to  Details  , I can get information as to what was  involved, and my Macbook was involved, and the 
 pfSense ﬁrewall actually collected this information. What's really cool about that is pfSense's ﬁrewall 
 has no concept of users, but the Connector to Active Directory was able to obtain my user 
 information and correlate that with this Alert. Along with the enrichment that we have, the 
 geolocation, we have the IP type–private or public–and a whole bunch of other information, this 
 makes it much easier to identify threats or even if I need to disable a user. 
 17:00-18:00 
 Because this user and this Connector exist, and I have a problem identiﬁed such as this right here. If I 
 found that this Alert was serious, I could select the Connector. I can specify  Duration  . Maybe I'm 
 investigating so I only want to disable it for one hour. You have to use the name of the ﬁeld that had 
 the username. Again, let me go back one more time so this is clear. I'm going to cancel out of this 
 right now. Let's go back to  Details  . Let's look where  my username was detected. My username was 
 assigned to source IP username (srcip_username) right here. This is the ﬁeld. If I go to  Actions  , 
 Disable User  , 
 18:00-19:00 
 go to the  Connector, Duration  one hour,  Disable User  will be the source IP username. I started 
 typing that in and it found it. Then I'm going to go ahead and  Submit  . If you look up here it says, 
 “Request to disable user is in progress. Monitor progress in the  Respond | Actions  table.” If I go to 
 User Actions  I'll see the username right here and  I'll see that it's in progress. I've done this in the past 
 before. But here I'll wait till it's not in progress anymore. I'll just refresh the screen a couple of times. 
 Still in progress. This is actually using LDAP to disable the user. 
 ADM-03-01-224  117 


---

<!-- Página 118 -->

 19:00-20:05 
 It's doing an LDAP modify from the Modular Sensor to the Connector. I see the user was disabled. 
 Now if I go to Active Directory, I can see that my user has a down arrow, which lets me know this 
 account is disabled. Have no fear, if I want to re-enable this account, I can go to  All Tasks  as an 
 administrator and specify  Enable Account  . Also though,  from the platform itself, I can also revert my 
 action here as well. Now the user was reverted successfully, then this account will be re-enabled 
 again. Now going back to my Active Directory server, If I take a look at my user account, Paul 
 Levasseur, there's no longer a down arrow. Therefore, the revert was processed successfully. That's it! 
 I hope you enjoyed the lesson. Thank you. 
 This lesson is complete. Thank you for watching. 
 L28 - MODULAR SENSOR BUFFERING 
 L28A-PRES: Modular Sensor Buffering (04m:22s) 
 00:00-01:00 
 The next lesson is  Buffering  . This lesson,  Buffering  ,  provides a summary of the buffering capabilities 
 of the Modular Sensor that are used in an event where connectivity is temporarily lost between a 
 Modular Sensor and the Stellar Cyber Open XDR platform and how data is trickled back once the 
 connection is restored. 
 Hi all! In this lesson, I will just do a recap of the buffering that's done by Modular Sensors. In each of 
 the individual lessons for each part, I discussed the buffering option, but now I just want to put them 
 together in one place as more of a review than anything else. 
 01:00-02:00 
 Looking at the Modular Sensor with the Log Forwarder, network traffic metadata, and IDS features 
 on the Modular Sensors, buffering is enabled by default to temporarily store Interﬂow records locally. 
 If there is a connection issue to the Stellar Cyber platform, Modular Sensors temporarily hold the 
 buffered Interﬂow records. When connections are restored to the Stellar Cyber platform, buffered 
 Interﬂow records resume being forwarded at a trickle to prevent overwhelming the network 
 connection. Again, just to be clear, the Modular Sensor, when the connection comes back up, will still 
 be doing its ordinary duties. It will be normalizing the logs and network traffic that it's receiving into 
 Interﬂow records to send to the Stellar Cyber platform. But it also has previous Interﬂow records 
 buffered. 
 02:00-03:00 
 Instead of blasting all those at once to the Stellar Cyber platform, it will start trickling in the Interﬂow 
 records to the Stellar Cyber platform until the buffer has been depleted. The amount of time logs are 
 buffered depends on the conﬁgured buffer size. Buffering options are available in the Modular 
 Sensor Proﬁle in the following modules. Number one is the Log Forwarder. In the Modular Sensor 
 Proﬁle for the Log Forwarder, there's an option for buffering. This will save data locally where there's 
 ADM-03-01-224  118 


---

<!-- Página 119 -->

 a connection issue with the DP and send the data later. Again, the DP is called the Data Processor. 
 That's just the term for the Stellar Cyber platform. 
 03:00-04:00 
 The next option is for Network Traffic. In the Network Traffic section in the Modular Sensor proﬁle. 
 There's an option to save data locally when there is a connection issue with the DP, it sends the data 
 later. Again you see the buffer size. For IDS, again, there's an option for buffering. It saves data locally 
 when there is a connection issue with the DP, and sends the data later. Again, here there is a buffer 
 size. The buffer sizes are related to the amount of traffic that usually comes in Network traffic is 
 typically a lot more. Log traffic is usually less, and then IDS is even less than that. The buffer sizes are 
 related to the type of traffic being received. Just to make it really clear, 
 04:00-04:22 
 if connectivity is lost to the Stellar Cyber platform, the data will be buffered based on the size 
 speciﬁed in the conﬁguration until the connection is restored, and the data from the buffers is trickled 
 back to the Stellar Cyber platform. 
 This lesson is complete. Thank you for watching. 
 L29 - MODULAR SENSOR LESSONS SUMMARY 
 L29A-PRES: Modular Sensor Lessons Summary (02m:48s) 
 00:00-01:00 
 The next lesson is  Modular Sensor Summary  . This lesson,  Modular Sensor Summary,  provides a brief 
 summary of Modular Sensors within the Stellar Cyber Open XDR Architecture and ends the  Stellar 
 Cyber Modular Sensor Concepts and Conﬁguration  module. 
 Hi everyone. We have now completed the training module for  Modular Sensor Concepts and 
 Conﬁguration.  Looking at the slide once again, the  Stellar Cyber Open XDR Architecture Overview, 
 the “Big Picture,” we have now covered everything on the left-hand side related to Modular Sensors. 
 We talked about the Log Forwarder, log ﬁltering, how network traffic is captured from SPAN ports or 
 TAP devices. 
 01:00-02:00 
 We talked about app identiﬁcation with deep packet inspection, how it creates session state and 
 correlates processes and how it collects metadata and how to optimize the ingestion with data 
 ﬁltering. We've covered the IDS module on the Modular Sensors along with the Malware Sandbox. I've 
 provided examples of how to conﬁgure the Modular Sensors as an Aggregator. I've covered the 
 Tenable Nessus scanner that's built into the Modular Sensor and how to initiate scans from Tenable.io 
 into the local environment using Modular Sensors, as well as I've demonstrated how to use 
 Connectors to Tenable to obtain a scan details and asset information. I've also explained and 
 demonstrated how to create Active Directory Connectors from the Modular Sensor 
 ADM-03-01-224  119 


---

<!-- Página 120 -->

 02:00-02:47 
 that can obtain event logs from Windows as well as computer assets and user information. I've 
 shown you where to conﬁgure buffering so that if the connectivity to the Open XDR platform is lost 
 due to maybe an internet outage that the Stellar Cyber Modular Sensor can buffer that data locally, 
 and then when the connection comes back up can start trickling those Interﬂow records back to the 
 Stellar Cyber Open XDR platform. Thank you for participating in the lessons in this module. I hope to 
 see you in other modules as well. Happy learning! 
 This lesson is complete. Thank you for watching. 
 ADM-03-01-224  120 


---