Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

OT Deployment

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lessons.

P02 Operational Technology (OT) Security in Stellar Cyber (60m:00s)  

PART 1: Operational Technology Security in Stellar Cyber - Introduction (05m:15s)

Learn how Stellar Cyber protects operational technology (OT) environments from cyber
threats. Understand key differences between IT and OT systems, such as OT's focus on
availability and safety, and explore examples from industries like manufacturing, energy,
and healthcare. See how the Stellar Cyber Platform integrates IT and OT security to
detect threats across the operational landscape.

PART 2: OT Fundamentals (04m:15s)

Understand the components of OT systems, including SCADA systems, PLCs, and
HMIs, and learn how they control industrial processes. Explore why OT security is
crucial due to legacy systems, physical consequences, and targeted attacks. See how
Stellar Cyber addresses risks with monitoring, anomaly detection, and compliance with
standards like NIST and NERC CIP.

PART 3: OT Security (06m:45s)

Discover common OT security concerns, such as unpatched legacy systems, IT/OT
network convergence, and targeted attacks. Learn how Stellar Cyber mitigates these
risks by identifying unauthorized devices, monitoring critical infrastructure, and
preventing lateral movement. Explore OT use cases in manufacturing, energy,
healthcare, and building management.

PART 4: Securing OT with Stellar Cyber (12m:45s)

Gain insights into the Stellar Cyber approach to OT security using deep packet
inspection, machine learning, and SCADA-specific protocol analysis. Learn how the
platform detects anomalies, unauthorized communications, and malware across

industrial control systems. See how defense-in-depth strategies like DMZs and secure
communication layers protect OT environments.

PART 5: OT Demonstration (10m:30s)

Watch a real-world example of Stellar Cyber in action, identifying suspicious activity
from OT user to PLC. Follow how the platform tracks Oracle SQL scans, VNC
connection attempts, and PostgreSQL port scans. Learn how to isolate compromised
assets, detect buffer overflow vulnerabilities, and prevent lateral movement in OT
networks.

PART 6: IT/OT Attack Demonstration (14m:35s)

Watch a simulated attack that originates in the IT network and crosses the IT/OT
boundary into critical OT systems. Follow how the Stellar Cyber Platform detects,
correlates, and responds to the attack as it propagates through the OT network. See
how the platform surfaces indicators of compromise, traces lateral movement between
IT and OT assets, and enables analysts to contain the threat before operational systems
are impacted.

The first time you access a link on the portal during a session, you must log in to access
content.

Stellar Cyber has a flexible deployment model and a unified platform that natively supports
Operational Technology (OT) security use cases. This allows immediate deployment and future
proofing to new security demands. Defending both IT and OT from a single platform results in a
more efficient and cost effective approach to Security Operations.

Introduction
Stellar Cyber’s integrations, Connectors and Parsers, Sensors, approach to Detections, and
Partner Ecosystem address the main challenges of getting complete visibility across both IT and
OT environments. Those challenges are typically:

Ability to integrate any IT and OT source in a single SOC Platform—Addressed by
Connectors and Parsers

Inability to get agent-based solutions in OT environment, thus a need for agentless
security solutions—Addressed by Security Sensors

Need for broad, out-of-the-box, detection coverage across IT, OT, and IT or OT lateral
movement use cases—Addressed by approach to Detections

Network architecture requirements restricting unidirectional data flow or inability to
deploy any sensors in an OT environment—Addressed by Partner Ecosystem

Use this guide to understand the in-depth capabilities of Stellar Cyber in OT environments, the
detection use cases covered, and the deployment scenarios for network architectures and risk
levels.

Technical Capabilities

Multiple Stellar Cyber components play different roles in getting coverage into OT environments
and providing detection coverage. If not already familiar, it is recommended to be acquainted
with Stellar Cyber’s architecture prior to continuing this guide.

The following table lists the core technologies leveraged by Stellar Cyber and the associated
component in OT environments.

Technology

Stellar Cyber Product Component Details

DPI

IDS

Security & Linux Sensors

3700 total protocols, 57 SCADA (includes iccp
and dnp3), 18 IoT; entire support list detailed
below. See DPI SCADA Reference.

Security & Linux Sensors

Real time updates from paid signature feeds.

Malware AV

Security Sensors

NTA / NDR

Data Processor

Asset Discovery

Data Processor

Vulnerability
Management

Security Sensor

DMZ Log Collection

Connectors, Logs via Security
Sensors, Linux & Windows Sensors

Level 3 Device Log
Collection

Logs via Security Sensors, Linux &
Windows Sensors

OT Product Log
Collection

Logs via Security Sensors

Case Correlation

Data Processor

DPI SCADA Reference

Click here to expand: DPI SCADA Reference

Over the wire file reconstruction and
classification.

Supervised and unsupervised Machine
Learning.

Asset discovery and resolution from all data
sources.

Third party vulnerability management sensors
can be installed on a Security Sensor (for
example, Tenable).

Ability to collect logs from all sources within
DMZ (for example, Windows jump host, Zero
Trust Solution).

Ability to collect logs from all sources within
Level 3 (for example, Engineering Workstation,
Remote Access Server).

Ability to collect logs from OT security products
(for example, Nozomi) and OT devices (for
example, Honeywell).

Analyze and investigate all alerts, across IT and
OT, together automatically.

The following protocols are natively understood by Stellar Cyber’s network based Security
Sensors. Stellar Cyber’s DPI understands many other protocols beyond the following SCADA
reference.

Protocol

AAON PRISM 2

B&R Automation

BACnet Application Layer

BACnet Network Layer

Description

AAON Prism 2 is a software for control of AAON HVAC, Wattmaster
Commlink 5 module over IP.

B&R Industrial Automation is a manufacturer for the industry. This plugin
classifies a plastic molding machinery.

BACnet is a communication protocol for Building Automation and Control
(BAC) networks defined by the standard ISO 16484-5. The BACnet stack
defines different layers, the BACnet Application Layer (bacnet_app)
manages access to objects exposed by BACnet devices and operations
done on them.

BACnet is a communication protocol for Building Automation and Control
(BAC) networks defined by the standard ISO 16484-5. The BACnet stack
defines different layers, the BACnet Network Layer (bacnet_net) contains
the network addresses required for routing BACnet messages to BACnet
devices.

Protocol

Description

BACnet Virtual Link Control

Bosch Security Conettix

Codesys Protocol (IDE-PLC)

BACnet is a communication protocol for Building Automation and Control
(BAC) networks defined by the standard ISO 16484-5. The BACnet stack
defines different layers, the BACnet Virtual Link Control layer
(bacnet_vlc) is used by BACnet devices over IP networks. It formalizes
all the services that a BACnet device might require from the link layer but
are not readily available from the underlying IP layer.

Bosch Conettix is a security alarm product line. This plugin classifies the
D6600 when no encryption is configured.

Codesys is an embedded system and its IDE for industrial Programmable
Logic Controller (PLC). This plugin classifies the protocol between the
IDE and the PLC.

Common Industrial Protocol

The Common Industrial Protocol (CIP) is an industrial protocol for
industrial automation applications.

CSP AB/Ethernet

DeltaV

Distributed Network Protocol

DLMS/COSEM over IP

DLMS/COSEM over IP wrapper

Dr Schenk Inspection System

EquipCommand

ESK M3

Ethernet/IP

Experion product

fanuc gen

General Electric Proficy

Generic Object Oriented Substation
Events

High-Availability Seamless
Redundancy

High-Level Data Link Control

Honeywell Process History
Database

HSR/PRP supervision frame

IEC 60870-5-104

Proprietary protocol developed by Allen-Bradley, used on programmable
logical controllers (PLC).

Traffic related to DeltaV, a distributed control system used in industrial
process control (Emerson Process Management).

DNP3 (Distributed Network Protocol) is a set of protocols used between
components in process automation systems (SCADA).

DLMS/COSEM is a standardized protocol for energy and water smart
meters. This plugin classifies DLMS above the UDP or wrapper_dlms
(WPDU).

TCP/UDP wrapper protocol (WPDU) for transporting over IP the
DLMS/COSEM (IEC-62056) protocol for energy and water smart meters.

Dr Schenk Inspection System is a product that inspects and analyzes raw
material from a factory production chain. It gathers sensors, actuators,
and visualization components all interacting with the Inspection System.

This layer classifies EquipCommand protocol from TotalTrax equipment
(SX/VX series). It solely handles the non-ciphered part of this protocol.

This plugin classifies the control protocol between ESK M3 Access
Control module for forklifts and the P106 software that manages them.

ENIP (EtherNet/IP) is an industrial network protocol that adapts the
Common Industrial Protocol to standard Ethernet.

This plugin classifies Experion Control Builder for Server LX.

This layer gathers signatures of protocols used by Fanuc equipment. This
layer does not cover ALL protocols generated by Fanuc equipment.

Proficy is a General Electric product for industrial environments allowing
monitoring and data management from the SCADA network. This plugin
classifies traffic related to Proficy Gateway service (PR Gateway) and
Proficy Licensing server (PR Licensing).

GOOSE (Generic Object Oriented Substation Events) is a controlled
model mechanism in which any format of data (status, value) is grouped
into a data set and transmitted within a time period of 4 milliseconds.

High-Availability Seamless Redundancy provides redundancy for
industrial Ethernet networks. This header is used for packet duplication
removal. The ixEngine does not run the duplication removal algorithm.

High-Level Data Link Control (HDLC) is a data link layer protocol
standardized by ISO/IEC 13239:2002. This plugin classifies Frame
Type 3 when transported over TCP/IP.

Traffic related to Honeywell Process History Database (PHD).

High-Availability Seamless Redundancy (HSR) and Parallel Redundancy
Protocol (PRP) provide redundancy for industrial Ethernet networks. This
plugin classifies supervision frames.

IEC 60870-5-104 protocol (aka IEC 104) is a part of IEC Telecontrol
Equipment and Systems Standard IEC 60870-5 that provides a

Protocol

Description

IEC 61850 Sampled Values

IEEE C37.118 Synchrophasor

Inter-Control Center
Communications Protocol

Intermec SmartSystem Foundation

Invar Systems AS/RS Control

iWarehouse

KEYENCE Barcode Reader

Lenel OnGuard client

Manufacturing Message
Specification (ISO 9506)

Mercury Security

communication profile for sending basic telecontrol messages between
two systems in electrical engineering and power system automation.

IEC 61850 Sampled Measured Values (SMV or SV) is protocol used in
Electrical substations to share data between Intelligent Electronic Device
(IED) under hard real time constraints (IEC 61850-9-2).

IEEE C37.118 Synchrophasor Protocol conveys electrical current
measurements in power grid substations.

IEC 60870-6/TASE.2. Inter-Control Center Communications Protocol
(ICCP) provides data exchange over Wide Area Networks (WANs)
between utility control centers, utilities, power pools, regional control
centers, and Non-Utility Generators.

Intermec (Honeywell subsidiary) SmartSystem is a barcode scanner fleet
management software.

Invar Systems AS/RS (Automated Storage and Retrieval System) control
protocol is part of Invar's integrated warehouse software system (IWS).

iWarehouse is the fleet and warehouse management system of Raymond
Corporation (a subsidiary of Toyota Industries that manufactures and
distributes electric lift trucks). This plugin classifies the protocol of the on-
board device, named Monitor.

This plugin classifies the control protocol of KEYENCE Barcode Reader
products, also used by their setup software (AutoID Network Navigator).

OnGuard is a product from Lenel for managing physical security of
buildings. This plugin classifies the connection from the client software to
the server.

ISO 9506 Manufacturing Message Specification (MMS).

This plugin classifies Mercury Security controllers communication
protocol with TLS disabled. Mercury security controllers manage physical
access control (doors and card readers) to buildings.

Mettler Toledo Standard Interface
Command Set

Standard Interface Command Set (SICS) is a protocol to control Mettler
Toledo industrial scales.

Modbus

Modbus Remote Terminal Unit

Modbus is a standard communication protocol in industry for connecting
industrial electronic devices (SCADA). Here, we consider modbus as the
combination of Modbus/TCP (Transport layer for TCP/IP networks) and
Modbus (serial communication protocol).

Traffic related to Modbus Remote Terminal Unit (RTU), a distributed
control system used in industrial process control. The Modbus RTU
communications can be sent to the network using a basic RS485 to TCP
adapter.

Moxa Async Server Proprietary
Protocol (ASPP)

This plugin classifies ASPP (Async Server Proprietary Protocol) from
Moxa (NPort devices) without activation of encryption.

Omron FINS protocol

Omron FINS Protocol is SCADA protocol to communicate with PLC.

OPC Unified Architecture

Parallel Redundancy Protocol

PC-cubed

OPC is the interoperability standard for the secure and reliable exchange
of data in the industrial automation space and in other industries. This
plug-in classifies the OPC Unified Architecture (UA) binary protocol over
TCP.

Parallel Redundancy Protocol provides redundancy for industrial Ethernet
networks. This plugin detects the Redundancy Control Trailer (RCT) to
Ethernet frames. The ixEngine does not run the duplication removal
algorithm.

PCCC is Programmable Controller Communication Commands, which is
used to control software running in Programmable Logic Controller
(PLC). PCCC traffic can be hardware-specific. This plugin addresses
traffic generated by Rockwell/Allen-Bradley to talk to SLC5, PLC5E, and
MicroLogix PLC for service.

Protocol

PI AF

PI Data Archive

Process Field Net

Rockwell RNA protocol

s7 Communication

S7 Communication Plus

Schneider Integrated Object
Network

SeamLess Message Protocol

Siemens Apogee

Socomec

Toyo PLC protocol

Vnet/IP

Yokogowa protocol

Description

OSI PI Analysis Framework SCADA protocol (AF Server, MDB Sync,
etc.).

OSI PI DataArchive and Server SCADA protocol (ProcessBook, Datalink,
etc.).

PROFINET (an acronym for Process Field Net) is an industry technical
standard for data communication over Industrial Ethernet, designed for
controlling and collecting data from equipment in industrial systems, with
a particular strength in delivering data under tight time constraints (1ms
or less). The standard is maintained and supported by Profibus & Profinet
International, an umbrella organization headquartered in Karlsruhe,
Germany.

Rockwell Network Applications (RNA) is a Rockwell implementation of
Windows DNA-M and is used for communication between Rockwell
FactoryTalk products.

S7comm (S7 Communication) is a Siemens proprietary protocol that runs
between programmable logic controllers (PLCs) of the Siemens S7-
300/400 family. It is used for PLC programming, exchanging data
between PLCs, accessing PLC data from SCADA (supervisory control
and data acquisition) systems, and diagnostic purposes.

S7communication Plus is a Siemens proprietary protocol for Siemens'
Programmable Logic Controllers (PLC).

Integrated Object Network (ION) is a proprietary SCADA protocol for
Schneider Electrics smart meters.

SeamLess Message Protocol (SLMP) is for the control of Mitsubishi PLC
devices.

This plugin classifies the main data protocol used by Siemens Apogee
HVAC product line. This device also uses BACnet and other control
protocols that are not covered here.

Socomec is a manufacturer for industrial power networks. This plugin
classifies the monitoring socket of the Silverlight user interface for the
PassIP+ gateway to the proprietary ISOM bus. It is used for insulation
fault detection.

This layer classifies only a limited number of protocols known to be used
by Toyo hardware (PLC).

Yokogawa's control communication network approved by international
standards (IEC 61784-2 Ed.2.0).

This layer classifies only a limited number of protocols known to be used
by Yokogowa hardware.

IDS Signature Reference

Stellar Cyber’s Security Sensors are continuously updated with signatures from Proofpoint ET
Pro  out-of-the-box. The ruleset contains coverage against OT attacks, for example, SCADA
and IoT. With an upcoming release of Stellar Cyber’s Threat Intelligence feature, all signatures
will become searchable in the platform itself.

Detection Use Cases
From the technologies described above, visibility and detections are created that can be used to
cover key use cases related to defending OT.

Use Case

Methodology

Non-Standard SCADA
Protocol Detection

DPI engine detects all protocols occurring within SCADA network

Use Case

Methodology

SCADA Network
Segmentation Violation

Network Attack Detection

Malicious or Suspicious
File

Anomalous
Communication /
Process / Port / Data
Transfer

IT to OT Lateral
Movement

Custom Detection: Alert if anything outside standard protocols (for example,
iccp & dnp3) occurs in the SCADA network (defined by subnet, host list, etc.)

All traffic flows (east-west, north-south) is monitored via Sensors, Logs (for
example, firewalls), and Connectors (for example, endpoint products)

Alert if SCADA hosts communicate with anything outside of other SCADA
hosts or DMZ (defined by subnet, host list, etc.)

IDS, with commercial signature feeds, will pick up thousands of network-based
attacks

Malware AV will reconstruct files over the wire and detect if they are malicious
or suspicious

Can optionally submit to cloud-based Malware Sandbox if there is Internet
access

“Normal” is learned for all environments, including SCADA

If a SCADA asset has an anomalous communication with another asset,
process launch, port usage, data transfer, NDR alerts

All data across IT, DMZ, and OT are collected and analyzed

Alerts are correlated together to detect events that start / end in IT, and
laterally move to OT

Deployment Scenarios
Getting visibility into OT environments depends on a number of factors of how those networks
are managed to include connectivity and managed infrastructure. The following deployment
scenarios will reference the Purdue Model, which is a network and device segmentation
guideline for Industrial Control Systems (ICS). For an overview of the Purdue Model, reference
this overview  from ZScaler.

Stellar Cyber can be flexibly deployed depending on the OT network architecture and risk levels.
Use the following table for understanding which deployment scenario is best suited for your
enterprise. For the most comprehensive solution, Stellar Cyber recommends deployment
scenario (1). For the easiest to deploy, easiest to maintain, and lowest risk solution,
Stellar Cyber recommends deployment scenario (2).

Deployment Scenario

Description

Technologies Required

Security Sensors

(Optional) Data Diode

(Optional) Breakout Network TAP

Security Sensors

Aggregator Network TAP

Packet Broker

(Optional) Data Diode TAP

Security Sensors

(Optional) Data Diode TAP

(1) Sensors Deployed to
Level 3 & 2 Switches

(2) Sensors Deployed in
Level 4 With Traffic
Visibility

(3) Sensors Deployed in
Level 4 With No Traffic
Visibility

(4) Airgap

(5) Combination of
Scenarios

Security Sensors are deployed, as
hardware or VMs, in Level 3 and 2,
and mirror relevant switch traffic.

When you would do this
It is acceptable to put sensors in
Level 3 and below, and you want full
visibility and capability.

Security Sensors are deployed, as
hardware or VMs, in Level 4 and
receive mirrored traffic from Level 3
switches and below.

When you would do this
It is too risky to put products in
Level 3 and you want easy updates
on the sensors.

Security Sensors are deployed, as
hardware or VMs, in Level 4 and
receive any available syslog
sources from Level 3 and below.

When you would do this
When the network is not willing to
accept anything new in Level 3 and
below but there is some logging
infrastructure in place.

If an OT environment is truly air
gapped, there is no network path to
receive any telemetry back to Stellar
Cyber. Stellar Cyber can be
deployed in an air gapped network,
however it would be unproductive to
have a single instance of Stellar
Cyber for a single air gapped IT
environment.

If certain OT environments have
different risk levels or networking
infrastructure, some combination of
scenarios (1), (2), and (3) can be
deployed.

N/A

In the subsequent scenario subsections, diagrams detail specific capabilities deployed in certain
locations, along with what telemetry is collected from where (both color coded for reference).

(1) Sensors Deployed to Level 3 & 2 Switches

Pros: This scenario is the maximal security coverage because it allows for capabilities like
Vulnerability Management to be deployed and device level syslog to be easily collected.

Cons: It involves installing agentless software or new hardware in Level 3 or below, which
comes with risk and bureaucratic process.

The following diagram shows several integrations and components deployed. Not everything
here is strictly necessary (such as, DMZ server logs, Firewall Syslog, OT Device Syslog),
however recommended for maximal coverage.

Components and integrations deployed:

Device Syslog (Red)—Any OT device capable of forwarding syslog events sends
events to a Security Sensor to then forward to the Data Processor

Security Sensors (Orange)—Security Sensors are deployed off of core OT switches,
mirroring traffic to perform capabilities including Network Traffic Analysis (NTA), Deep

Packet Inspection (DPI), Intrusion Detection System (IDS), Malware Sandbox, and
Vulnerability Management (VM)

Server Sensors (Purple)—Small agents used for log collection can be deployed on
DMZ servers

Firewall Syslog (Blue)—DMZ and above Firewalls can forward syslog to the Data
Processor or Security Sensors

Data Processor (Grey)—The Data Processor can be deployed on-premise or as a
SaaS solution

Data Diode TAP Usage

Click here to expand: Data Diode TAP Usage

Why Use A Data Diode TAP—A Data Diode TAP is used in circumstances when it is required
to restrict data to only be able to flow from Level 3 to Level 4, and not vice versa. This is often
recommended and provides significant security benefits. However, there is still a need to
monitor Level 3 and below because there are attacks that can bypass such network
segmentation.

Deployment Implications—Without direct access to the Data Process, Security Sensors will
have to be manually updated.

Data Flow Implications—For telemetry collection, none, because data can still be sent out of
the OT network. However, Security Sensors will not get up-to-date signatures because they
will not have Internet Access.

A Data Diode can also be deployed along with a Breakout Network TAP discussed below.

Breakout Network TAP Usage

Click here to expand: Breakout Network TAP Usage

Why Use A Breakout Network TAP—A Breakout Network TAP allows traffic mirroring from
legacy switches that do not natively support this functionality or unmanaged switches that
cannot be configured.

Deployment Implications—Everything else should be deployed the same, however you will
want to ensure the Security Sensor is getting both traffic mirroring from the Breakout Network
TAP and can still receive syslog from any OT devices.

Data Flow Implications—None.

(2) Sensors Deployed in Level 4 With Traffic Visibility

Pros: This scenario is the easiest to deploy and less risky from a perspective of introducing new
products within the OT environment, while maintaining much of the visibility from deployment
scenario (1). Security Sensors can auto update since they have access to download software
from the Data Processor.

Cons: It does involve acquiring additional networking technologies, specifically Aggregator
Network TAPs and a Packet Broker. Some log collection may be more challenging if syslog
cannot be easily streamed out of the environment, and certain capabilities like Vulnerability
Management will not be deployable to Level 3 and below.

The following diagram shows several integrations and components deployed. Not everything
here is strictly necessary, however recommended for maximal coverage.

Components and integrations deployed:

Device Syslog (Red)—Any OT device capable of forwarding syslog events sends
events through the Data Diode TAP to a Security Sensor to then forward to the Data
Processor

Security Sensor (Orange)—A Security Sensor is deployed in Level 4 receiving
mirrored traffic from the Packet Broker in Level 3, which allows it to perform capabilities
including Network Traffic Analysis (NTA), Deep Packet Inspection (DPI), Intrusion
Detection System (IDS), and Malware Sandbox

Firewall Syslog (Blue)—Level 4 Firewalls can forward syslog to the Data Processor or
Security Sensors

Data Processor (Grey)—The Data Processor can be deployed on-premise or as a
SaaS solution

Aggregator TAP (Green)—Mirrors network traffic from one or many switches with the
purpose of forwarding to a Packet Broker

Packet Broker (Green)—Receives and forwards traffic from one or many Aggregator
TAPs or Network Breakout TAPs to then forward as a single stream to a Security
Sensor

Data Diode TAP (Green)—Physically enforces unidirectional communication between
Level 4 and Level 3

Data Diode TAP Usage

Click here to expand: Data Diode TAP Usage

Why Use A Data Diode TAP—A Data Diode TAP is used in circumstances when it is required
to restrict data to only be able to flow from Level 3 to Level 4, and not vice versa. This is often
recommended and provides significant security benefits. However, there is still a need to
monitor Level 3 and below because there are attacks that can bypass such network
segmentation. In this deployment scenario, there would likely be a Data Diode TAP required,
given the decision to not place Security Sensors in Level 3 and below, although it is not
technically necessary.

Deployment Implications—This deployment scenario already places Security Sensors at
Level 4, so there are no implications other than setting up the Data Diode TAP.

Data Flow Implications—This deployment scenario already places Security Sensors at
Level 4, so there are no implications.

(3) Sensors Deployed in Level 4 With No Traffic Visibility

Pros: This scenario does not place any new products in the OT environment. Security Sensors
can auto update since they have access to download software from the Data Processor.

Cons: Losing traffic level visibility in the OT environment significantly limits detection use cases.

The following diagram shows several integrations and components deployed. Not everything
here is strictly necessary (such as, DMZ server logs, Firewall Syslog, OT Device Syslog),
however recommended for maximal coverage.

Components and integrations deployed:

Device Syslog (Red)—Any OT device capable of forwarding syslog events sends to a
Security Sensor to then forward to the Data Processor

Security Sensor (Orange)—A Security Sensor is deployed in the DMZ and is only
acting as a Log Forwarder since it has no access to OT network traffic

Server Sensors (Purple)—Small agents used for log collection can be deployed on
DMZ servers

Firewall Syslog (Blue)—All DMZ and above Firewalls can forward syslog to the Data
Processor or Security Sensors

Data Processor (Grey)—The Data Processor can be deployed on-premise or as a
SaaS solution

(4) Airgap

Pros: Strict network segmentation between OT and IT environments.

Cons: Not any security gains in practice compared to a Data Diode preventing data transmission
one way at the physical layer. Additionally, a true airgap is operationally painful, and inherently
obscures security visibility.

(5) Combination of Scenarios

The deployment scenarios above can easily be combined for enterprises that have multiple OT
environments that need various approaches to security. For example, a water treatment
enterprise may have many small sites and a single large water processing site. For the small
sites, each one implements Deployment Scenario (2). However for the large site, Deployment
Scenario (1) is implemented. All data ends up at a single Data Processor to defend all OT
environments in addition to any IT environments.

Technology Options For OT Networking
Stellar Cyber is, from a technical perspective, agnostic to different networking solution providers
for Data Diodes, Network Breakout TAPs, Aggregator TAPs, and Packet Brokers. However,
Garland Technology  is Stellar Cyber’s preferred and recommended vendor to work with as
they have an extensive portfolio of products completely focused on the different networking and
visibility challenges faced by OT environments.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

