Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Index Definitions & Details

Stellar Cyber organizes data into indices, which helps to speed up your searches.

The following table lists the name of each index in Stellar Cyber, the name of the index in the
Interflow data, the type of data collected in that index, and the source of the data.

 Stellar Cyber provides Coverage Analyzer  and Detections & Response  tools that let

you look up alert types by sensor, data source, application, alert name, alert type, or by XDR
attributes such as kill chain stage, tactic, or technique. You can also view alert types by
index in Machine Learning Alert Types by Index, which provides links to descriptions of the
alert types that can appear in each available index.

Index

Alerts

Interflow

Name

aella-ser-*

Data Source

Security events from Machine Learning, security analytics, and ATH playbooks

Assets

aella-

Asset data based on Stellar Cyber analytics

assets-*

Connectors:

Acronis Cyber Protect Cloud

Active Directory

Akamai

Armis

Automox

Broadcom SES

Cisco AMP

CODA Footprint

ConnectSecure V4

CrowdStrike

Cybereason

Cynet

CYRISMA

Index

Interflow

Name

Data Source

Deep Instinct

ExtraHop Reveal(x) 360

Firewalla Managed Security Portal

Fortra Frontline

Generic S3

Group-IB

Huntress

HYAS Protect

Imperva Incapsula

Jamf Pro

Jamf Protect

LimaCharlie

Liongard

Memcyco

Microsoft Defender for Endpoint

Microsoft SQL Server

Nessus

NodeZero

Palo Alto Networks CORTEX XDR

Qualys

Qualys FIM

SentinelOne

SonicWall Capture Client

SonicWall Endpoint Security

Sophos Central

Tenable.io

Tenable.sc

Thinkst Canary

ThreatDown OneView (formerly Malwarebytes OneView)

Trend Micro Apex Central

Trend Micro Cloud One Workload Security

Trellix (FireEye) Endpoint Security HX

Trellix MVISION

Verkada

Vicarius

VMware Carbon Black

Webroot

Index

Interflow

Name

Data Source

WithSecure Elements

AWS Events

aella-

CloudTrail non-traffic logs

cloudtrail-*

IDPS/Malware

aella-

Sandbox Events

maltrace-*

Machine Learning alerts types for this Index

Connectors:

Amazon Security Lake

AWS CloudTrail

Generic S3

Google Workspace

Firewall threats from sensors/log forwarders

Maltrace SDS/Sandbox

Machine Learning alert types for this index

Connectors:

Cato Networks

Linux Events

aella-audit-*

Audit data from Linux agents

Machine Learning alert types for this index

Connectors:

Cisco AMP

Google Workspace

Prisma Cloud (Palo Alto Networks)

SentinelOne

SonicWall Capture Client

Scans

aella-scan-*

Machine Learning alert types for this index

Connectors:

Armis

CODA Footprint

ConnectSecure V4

CyberCNS

CrowdStrike

CYRISMA

Fortra Frontline

Microsoft Defender for Endpoint

Nessus

Nodeware

Index

Interflow

Name

Data Source

NodeZero

Qualys

Rapid7

SentinelOne

SonicWall Capture Client

Tenable.io

Tenable.sc

Vicarius

Wiz

Sensor Monitoring aella-ade-*

Sensor statistics from DP Configuration Manager

Machine Learning alert types for this index

Signals

aella-

signals-*

Sensitive events that are not alerts but may provide useful context in threat hunting. The

following Windows events are stored in the Signals index:

104, 643, 1102, 4698, 4727, 4728, 4729, 4731, 4732, 4733, 4739, 4740, 4741, 4743, 4754,

4756, and 4757

Syslog

aella-

syslog-*

Application logs from sensor log forwarder parsers

Machine Learning alert types for this index

Connectors:

1Password

Abnormal Security Email Security

Acronis Cyber Protect Cloud

Akamai

Amazon Security Lake

Armis

Aruba Central

Automox

AWS Cloudwatch

AWS GuardDuty

AWS Inspector

Azure Event Hub

Barracuda Email Security

Barracuda WAF

BlackBerry Cylance

BeyondTrust

Broadcom SES

Broadcom (Bluecoat / Symantec) WSS

Index

Interflow

Name

Data Source

Broadcom (Symantec) Cloud Workload Protection

Broadcom (Symantec) Email Security.cloud

Box

Check Point Harmony Email

Cisco AMP

Cisco Secure Access

Cisco Umbrella

Cloudflare

CODA Footprint

ConnectSecure V4

Coro

CrowdStrike

CrowdStrike FDR

CyberArk EPM

Cybereason

Cyble

Cynet

Deep Instinct

Duo Security

ExtraHop Reveal(x) 360

Firewalla Managed Security Portal

Forescout

FortiEDR

Fortra Frontline

Generic S3

Google Cloud Audit Log

Google Cloud Security Command Center

Group-IB

Halcyon

HanDreamnet Security Switch

HIBUN

Hoxhunt

Huntress

HYAS Protect

iManage Threat Manager

Imperva Incapsula

Index

Interflow

Name

Data Source

Indusface

Ironscales

Jamf Pro

Jamf Protect

JumpCloud

Juniper Mist

LastPass

LimaCharlie

Liongard

Mailprotector

Manage Engine Endpoint Central

Memcyco

Microsoft Defender for Endpoint

Microsoft Graph Intune

Microsoft SQL Server

Mimecast API 1.0

Mimecast API 2.0

MySQL

NetFoundry

Netskope WSG

NodeZero

NordStellar

OCI Streaming

OneLogin

Okta

Palo Alto Networks CORTEX XDR

People Risk Explorer

Perception Point X-Ray

Prisma Cloud (Palo Alto Networks)

Proofpoint On Demand

Proofpoint Targeted Attack Protection (TAP)

Qualys

Qualys FIM

Recorded Future

Salesforce

SentinelOne

Index

Interflow

Name

Data Source

SOCRadar

SonicWall Capture Client

SonicWall Endpoint Security

Sophos Central

Stellar Cyber

Sucuri Security

Tenable Cloud Security

Thinkst Canary

Threatlocker

ThreatDown OneView (formerly Malwarebytes OneView)

Trellix (FireEye) Endpoint Security HX

Trellix MVISION

Trend Micro Apex Central

Trend Micro Cloud App Security

Trend Micro Cloud One Workload Security

Trend Micro Email Security

Trend Micro Vision One

VadeSecure

Verkada

Versa Networks Concerto

Vicarius

VMware Carbon Black

VMware Workspace One

Webroot

WithSecure Elements

Wiz

Traffic

aella-adr-*

Flow traffic from sensors

Machine Learning alert types for this index

CloudTrail traffic

Firewall traffic logs from sensor log forwarders

DHCP server logs from sensors

VPC Flow logs

ICMP/IGMP logs

Connectors:

Index

Interflow

Name

Data Source

Amazon Security Lake

AWS CloudTrail

AWS CloudWatch

Azure Event Hub

Cato Networks

OneLogin

Users

aella-users-

User data from analytics

*

Connectors:

Okta

Windows Events

aella-

Machine Learning alert types for this index

wineventlog

-*

Active Directory connector user data

Office 365 Active Directory user data

Windows logs from Windows agents

Windows System Security logs

Connectors:

Azure Event Hub

Microsoft Defender for Cloud Apps

Microsoft Entra ID (formerly Azure AD) Active Directory user data

Microsoft Graph Message Trace

Microsoft Graph Security API

Office 365

Office 365 Reporting Web Service

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

