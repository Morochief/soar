Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Types of Stellar Cyber Sensors

 Learn more at Stellar Cyber Academy.

The following link takes you to a course on the Stellar Cyber Academy technical training
portal where you can learn more about this topic by watching the suggested lesson.

J01 Open XDR: Explained (01h:05m)  

Modular Sensor Functions (12m:00s)

Learn about the role of modular sensors in gathering and analyzing data from diverse
network sources. Discover how log forwarding, network traffic analysis, and intrusion
detection contribute to real-time threat monitoring.

The first time you access a link on the portal during a session, you must log in to access
content.

This topic describes the family of sensors available from Stellar Cyber, from lightweight server
sensors that install as agents on target Linux and Windows servers to purpose-built physical
sensors capable of monitoring at 10G network speeds. Sensors provide the data gathering
foundation for Stellar Cyber's OpenXDR platform, gathering the right data with context.

Sensors are used to create visibility where it does not yet exist, or to simplify and consolidate
telemetry collection with Stellar Cyber. You can capture data from the network and assets, all
under the same license, and administered from the same platform.

 Starting with the 4.3.7 release, new physical sensors are shipped as modular sensors on

Ubuntu 22.04.

Family of Stellar Cyber Sensors
The Stellar Cyberfamily of sensors consists of the following members:

Server Sensors – Server Sensors install as software on target hosts to be monitored.
They are also referred to as agents. Server Sensors are available for both Linux and
Windows, as described below.

Device Sensors – Device Sensor is an umbrella term that refers to any purpose-built
Stellar Cyber sensor that includes both the host and the Stellar Cyber monitoring
software. Device Sensors are provided as both physical devices (Photon sensors) and
virtual machine images for different target environments.

 Previous releases provided a variety of different types of device sensors, including
Network, Security, and Modular. Starting with 4.3.7, the only type of device sensor
is Modular. You can use the Modular Sensor Profile to enable whatever sensor
features you like, creating the same functionality provided by the different sensor
types in previous releases. For your convenience, both Modular sensors and the
legacy Network and Security sensors are described below.

Linux Server Sensor

A Linux server sensor is a managed background daemon that works as a modular sensor without
log forwarding that also monitors:

Process info
Command execution
Files
File events

The server sensor converts that information to metadata and forwards it to the DP as Interflow.
The DP can then correlate traffic, processes, users, and commands for security, DDoS, and
breach attempt detections.

The server sensor launches the following processes:

aella_audit – collects audit logs and provides file integrity monitoring
aella_conf – handles the configuration
aella_ctrl – monitors other services, and can stop or start them based on the
configuration
aella_flow – collects metadata in traffic
aella_mon – collects system resource usage, including CPU, RAM, and disk

Data collected by the Linux server sensor can feed the following Stellar Cyber indices:

Traffic (aella-adr-*)

Linux Events (aella-audit-*)

Sensor Monitoring (aella-ade-*)

Windows Server Sensor

The Windows Server Sensor (agent) runs as a Windows service in a compatible Windows Server
system. The Server Sensor observes events within the Windows Server system and sends

Interflow data records to the data processor.

The captured events are:

Hardware
Security
System
Windows Firewall
Windows Defender
PowerShell

The Windows Server Sensor launches the following processes:

Name in Task

Name in Services

Manager

App

Description

aella_conf_win_sr

Windows Agent

Handles Windows Server Sensor configuration

v.exe

Sensor Conf

aella_ctrl_win_srv.

Windows Agent

Monitors other services, and can stop or start them based on the configuration

exe

Sensor Ctrl

aella_winlog.exe Windows Agent

Sends Windows events to DP

Sensor Logbeat

aella_filebeat.exe Windows Agent

Sends log files from Windows DHCP server (if installed and running) to DP or acts as

Sensor Filebeat

syslog forwarder if Filebeat is enabled in the Sensor Profile

aella_fim.exe

Windows Agent

Provides file integrity monitoring services, as configured in the Sensor Profile

Sensor FIM

aella_diagnostics_

Windows Agent

Sends Windows Server Sensor logs to DP

win_srv.exe

Sensor Phonehome

Modular Sensor

 See the top of this page for recommended lessons about this section at Stellar

Cyber Academy.

A modular sensor lets you easily add the features you like to your sensor. This helps simplify
your deployment and lets you manage the VM requirements for the sensors based on the
modular features they use.

Modular Sensors always include log ingestion. From there, you can enable different features as
part of your modular sensor profile:

Enable the Network Traffic feature to monitor the virtual environment, the physical
environment if connected to the span port of a physical switch, or the LAN segment via
a mirror port on a switch. The sensor monitors network and server response times and
can identify applications.

The sensor converts that information to metadata and forwards it to the DP as Interflow.
The DP can then provide security, DDoS, and breach attempt detections.

Enable the Sandbox and IDS features to improve your security posture:

Sandbox lets you detect malware in files and network traffic through Stellar
Cyber's integrated cloud service and also provides anti-virus services.
IDS lets you detect intrusion attempts using both files and network traffic.

 Keep in mind that VM resource requirements increase as you add more features to the

Modular Sensor Profile. Refer to Virtual Modular Sensor Provisioning and Performance
for details on the resources required to run different combinations of features in a Modular
Sensor Profile, as well as how to use the show module and show module request
CLI commands to compare provisioned resources against those required to run specific
feature combinations. Stellar Cyber only enables a Modular Sensor Profile on a sensor if the
host VM's resources can support it.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

