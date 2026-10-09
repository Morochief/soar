✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Connectors and Integrations Summary
The table below summarizes Stellar Cyber connectors and third party alert integrations and correlates them to assets.
Definitions
The definitions in the table are as follows:
Connector— A method of collecting information and compiling it into Interflow records that are indexed and
stored in the Data Lake. Stellar Cyber develops connectors based on the access methods provided for each
external data source, typically an API. These processes run on the Data Processor (DP) to fetch information
actively on a scheduled basis. Connectors collect data from external sources and can also respond to
actions such as blocking on a firewall or disabling users. The connection to a data source can be configured
in Stellar Cyber. For all connectors, see Connector Types & Functions.
Collect—A function of a connector that collects data from external data sources and adds it to the Data
Lake.
Respond—A function of a connector that takes actions on external data sources in response to detected
security events.
Third party alert integration—The process of ingesting, normalizing, and enriching alerts that are natively
created by third party services. These alerts are then mapped to the Stellar Cyber XDR Kill Chain and added
to the Alert index. The integration allows for the correlation of third-party native alerts with Stellar Cyber's
alerts, leveraging Machine Learning (ML) and Security Analytics (SA) to enhance the alert data. This
process includes deduplication to reduce noise. For all third party alert integrations, see Integration of Third
Party Native Alerts.
Detections—The identification of potential threats or risky behavior using various techniques such as
Machine Learning (ML) and Security Analytics (SA), as well as rules, and third party alert integration.
Detections can be based on known bad behaviors, anomalies, or suspicious activities identified through
different methods. These detections generate alerts which are then correlated into cases for further
investigation.
Asset Discovery—The process of identifying assets and tracking assets within a network from observed data
using a passive discovery service. This service can discover assets via data collected from various sources
such as endpoint data sources (for example, EDR or Directory Services), cloud audit logs, traffic-related
sources (for example, firewalls), Stellar Cyber server sensors (Linux and Windows), Stellar Cyber modular
sensors, and other log sources or connectors. The discovered assets can include both IP and MAC
addresses, which are associated with hosts. This process happens in real time as new data comes into the
system, and the unique assets are counted daily. The discovered data is then used to analyze the behavior
of these assets to detect security events.
Legend
The columns in the table are as follows:
Connector Name—The name of the connector in alphabetic order, and a link to the document
Connector Category—The category to which the connector belongs
Integration Function—The function of the integration:
Collect—only collect
Respond—only respond
Collect, Respond—both collect and respond
Third party—third party alert integration
Third Party Alert Integration Name—The name of the third party alert integration and a link to the document
Third Party Based On—What the third party alert integration is based on:
connector, and if there is a specific content type that needs to be configured, as well as the
msg_class
parser, and if there is a specific format, such as CEF

Windows agent
Detections—What to enter in the Stellar Cyber Detections & Response page
(https://detections.stellarcyber.ai/v/6.6.0) in the Select Applications field to produce a list of detections
and third party alert integrations supported for a data source
Asset Discovery—Whether the data source sends assets to the Assets index
Connectors and Integrations Table
Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
| 1Password               | Password ManagementCollect |                                  |                    |                   |     |
| ----------------------- | -------------------------- | -------------------------------- | ------------------ | ----------------- | --- |
|                         |                            |                                  |                    | 1Password         |     |
| Abnormal Security Email | Email                      | Collect, Third Abnormal Security | Connector, Content |                   |     |
|                         |                            |                                  |                    | Abnormal Security |     |
| Security                |                            | party                            |                    |                   |     |
|                         |                            | Email Security:                  | Type: Threats,     |                   |     |
|                         |                            | Integration of Third             | msg_class:         |                   |     |
|                         |                            | Party Native Alerts              | abnormal_security  |                   |     |
_email_security_t
hreat
Acronis Cyber Protect Endpoint Security Collect, Acronis: Integration of Connector, Content Acronis Cyber Yes, Content Type:
Cloud Respond, Third Party Native Type: Alerts, Protect Agents
Third party
|     |     | Alerts | msg_class: |     |     |
| --- | --- | ------ | ---------- | --- | --- |
acronis_cyber_pro
tect_alert
Active Directory IdP Collect,     Active Directory Yes, Content Type:
Respond
Computers
| Akamai | Endpoint Security | Collect   |     |     | Yes, Content Type: |
| ------ | ----------------- | --------- | --- | --- | ------------------ |
Connectors
| Amazon Security Lake | Web Security | Collect |     |                 |     |
| -------------------- | ------------ | ------- | --- | --------------- | --- |
|                      |              |         |     | Amazon Security |     |
Lake
Armis Endpoint Security Collect, Armis: Integration of Connector, Content Yes, Content
Armis
Third party
|     |     | Third Party Native | Type: Alerts, |     | Type: Devices |
| --- | --- | ------------------ | ------------- | --- | ------------- |
|     |     | Alerts             | msg_class:    |     |               |
armis_alerts
| Aruba Central | Network Management | Collect |     |     |              |
| ------------- | ------------------ | ------- | --- | --- | ------------ |
|               |                    |         |     |     |              |
| Automox       | IT Management      | Collect |     |     |              |
|               |                    |         |     |     | Yes, Content |
Type: Devices
Avanan   Third party Avanan: Integration of Parser (HTTP Avanan
|     |     | Third Party Native | JSON format),      |     |     |
| --- | --- | ------------------ | ------------------ | --- | --- |
|     |     | Alerts             | Content Type: N/A, |     |     |
msg_class: avanan
| AWS CloudTrail | PaaS     | Collect   |     | AWS Cloudtrail |     |
| -------------- | -------- | --------- | --- | -------------- | --- |
| AWS CloudWatch | PaaS     | Collect   |     | AWS Cloudwatch |     |
| AWS Firewall   | Firewall | Respond   |     |                |     |
AWS GuardDuty PaaS Collect, AWS GuardDuty: Connector, Content AWS GuardDuty
|     |     | Third party Integration of Third | Type: N/A, |     |     |
| --- | --- | -------------------------------- | ---------- | --- | --- |
|     |     | Party Native Alerts              | msg_class: |     |     |
aws_guardduty_fin
ding
| AWS Inspector | Vulnerability Scanner | Collect   |     |     |     |
| ------------- | --------------------- | --------- | --- | --- | --- |
Azure Event Hub PaaS Collect, Microsoft Defender for Connector, Content Azure Event Hub,
|     |     | Third party Cloud: Integration of | Type: Microsoft     | Microsoft Defender |     |
| --- | --- | --------------------------------- | ------------------- | ------------------ | --- |
|     |     | Third Party Native                | Defender for Cloud, | for Cloud,         |     |
|     |     | Alerts                            | msg_class:          | Microsoft Sentinel |     |
|     |     | and Microsoft Sentinel:           | microsoft_defende   |                    |     |
|     |     | Integration of Third              | r_cloud             |                    |     |
|     |     | Party Native Alerts               | and Content Type:   |                    |     |
Microsoft Sentinel,
msg_class:

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
microsoft_sentine
l
| Azure NSG          | Firewall | Respond   |     |                    |     |
| ------------------ | -------- | --------- | --- | ------------------ | --- |
| Barracuda Email    | Email    | Respond   |     | Barracuda Email    |     |
| Barracuda Firewall | Firewall | Respond   |     | Barracuda Firewall |     |
Logs
| Barracuda WAF | Web Security | Collect   |     |     |     |
| ------------- | ------------ | --------- | --- | --- | --- |
Barracuda WAF
| BeyondTrust | Privileged Access | Collect   |     |     |     |
| ----------- | ----------------- | --------- | --- | --- | --- |
Management
Bitdefender Endpoint Security Respond, Bitdefender: Integration Parser (Syslog BitDefender
|     |     | Third party of Third Party Native | JSON format),      |     |     |
| --- | --- | --------------------------------- | ------------------ | --- | --- |
|     |     | Alerts                            | Content Type: N/A, |     |     |
msg_class: several
Endpoint Security
Blackberry Cylance Respond Blackberry Cylance logs, Cylance Optics,
|     |     | (templates in CylancePROTECT and | Content Type: N/A, | Cylance Protect |     |
| --- | --- | -------------------------------- | ------------------ | --------------- | --- |
|     |     | Universal CylanceOPTICS:         | msg_class:         |                 |     |
|     |     | Webhook Integration of Third     | cylance_protect_a  |                 |     |
|     |     | Responder), Party Native Alerts  | lert               |                 |     |
Third party
| Box | SaaS | Collect   |     |     |     |
| --- | ---- | --------- | --- | --- | --- |
Endpoint Security
Broadcom Symantec Collect, Broadcom SES: Connector. Content Broadcom SES Yes, Content Type:
Endpoint Security (SES) Third party Integration of Third Type: Incidents, Devices
|     |     | Party Native Alerts | msg_class. |     |     |
| --- | --- | ------------------- | ---------- | --- | --- |
broadcom_ses_inci
dents
| Broadcom (Symantec) | Cloud Security | Collect   |     |     |     |
| ------------------- | -------------- | --------- | --- | --- | --- |
Cloud Workload
Protection
| Broadcom (Symantec) | Email | Collect   |     |     |     |
| ------------------- | ----- | --------- | --- | --- | --- |
Email Security.cloud
Broadcom (Blue Coat / Web Security Collect     Symantec Web
| Symantec) WSS |     |     |     | Security |     |
| ------------- | --- | --- | --- | -------- | --- |
Cato Networks SASE Collect, Cato Networks: Connector. Content Cato Networks
|     |     | Third party Integration of Third | Type: Security, |     |     |
| --- | --- | -------------------------------- | --------------- | --- | --- |
|     |     | Party Native Alerts              | msg_class.      |     |     |
cato_security
| Check Point | Firewall | Respond   |     | Checkpoint |     |
| ----------- | -------- | --------- | --- | ---------- | --- |
Firewall
| Check Point Smart-1 | Firewall | Respond   |     |     |     |
| ------------------- | -------- | --------- | --- | --- | --- |
Cloud
Check Point Harmony Email Collect, Check Point Harmony Connector. Content Checkpoint EDR
Email Third party Email: Integration of Type: Security Event,(Harmony)
|     |     | Third Party Native | msg_class.        |     |     |
| --- | --- | ------------------ | ----------------- | --- | --- |
|     |     | Alerts             | checkpoint_harmon |     |     |
y_security_event
| Cisco AMP | Endpoint Security | Collect |     |     | Yes, Content |
| --------- | ----------------- | ------- | --- | --- | ------------ |
Type: Computers
| Cisco FMC | Firewall | Respond   |     | Cisco |     |
| --------- | -------- | --------- | --- | ----- | --- |
Firepower(FW
class)
| Cisco Meraki Firewall | Firewall       | Respond   |     | Meraki         |     |
| --------------------- | -------------- | --------- | --- | -------------- | --- |
| Cisco Secure Access   | Cloud Security | Collect   |     |                |     |
| Cisco Umbrella        | DNS Security   | Collect   |     | Cisco Umbrella |     |

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
| Cloudflare | Web Security | Collect   |     |     |     |
| ---------- | ------------ | --------- | --- | --- | --- |
CODA Footprint Vulnerability Scanner Collect     Yes, Content

Type: Device
ConnectSecure V4 Vulnerability Scanner Collect       Yes, Content
Type: Asset
|                 | Endpoint Security |           |     |     |     |
| --------------- | ----------------- | --------- | --- | --- | --- |
| Coro            |                   | Collect   |     |     |     |
| CrowdStrike FDR | Endpoint Security | Collect   |     |     |     |
Endpoint Security
CrowdStrike Collect, CrowdStrike: Connector. Content Crowdstrike Yes, Content
|     |     | Respond, Integration of Third   | Type: EppDetectionS | (Endpoint) | Type: Host |
| --- | --- | ------------------------------- | ------------------- | ---------- | ---------- |
|     |     | Third party Party Native Alerts | ummaryEvent or      |            |            |
XdrDetectionSumma
ryEvent, msg_class:
crowdstrike.metad
ata.eventType:Epp
DetectionSummaryE
vent or
crowdstrike_XdrDe
tectionSummaryEve
nt
CyberArk EPM Endpoint Security Collect, CyberArk EPM: Connector. Content CyberArk EPM
|     |     | Third party Integration of Third | Type: Events, |     |     |
| --- | --- | -------------------------------- | ------------- | --- | --- |
|     |     | Party Native Alerts              | msg_class.    |     |     |
cyberark_epm_even
t
| CyberCNS | Vulnerability Scanner | Collect   |     | CyberCNS |     |
| -------- | --------------------- | --------- | --- | -------- | --- |
Cybereason Endpoint Security Collect, Cybereason: IntegrationConnector: Content Cybereason (EDR)Yes, Content
|     |     | Respond, of Third Party Native | Type: MalOp, |     | Type: Sensor |
| --- | --- | ------------------------------ | ------------ | --- | ------------ |
|     |     | Third party Alerts             | msg_class:   |     |              |
cybereason_malops
_all_types
Cyble Threat Intel Vendor Collect, Cyble: Integration of Connector: Content
|     |     | Third party Third Party Native | Type: Alerts, |     |     |
| --- | --- | ------------------------------ | ------------- | --- | --- |
|     |     | Alerts                         | msg_class:    |     |     |
cyble_alerts
Cynet Endpoint Security Collect, Cynet: Integration of Parser (CEF format), Cynet Yes, Content
|     |     | Respond, Third Party Native |  Content Type: N/A, |     | Type: Hosts |
| --- | --- | --------------------------- | ------------------- | --- | ----------- |
|     |     | Third party Alerts          | msg_class:          |     |             |
cynet_alert
|     | Vulnerability Scanner | Collect   |     |     | Yes, Content |
| --- | --------------------- | --------- | --- | --- | ------------ |
CYRISMA
Type: Host
Darktrace   Third party Darktrace: Integration Parser (CEF format),
|     |     | of Third Party Native | Content Type: N/A, |     |     |
| --- | --- | --------------------- | ------------------ | --- | --- |
|     |     | Alerts                | msg_class:         |     |     |
 darktrace
Deep Instinct Endpoint Security Collect, Deep Instinct: Connector, Content Deep Instinct Yes, Content Type:
|     |     | Respond, Integration of Third   | Type: Events, |     | Devices |
| --- | --- | ------------------------------- | ------------- | --- | ------- |
|     |     | Third party Party Native Alerts | msg_class:    |     |         |
deep_instinct_mal
iciousevent
| Duo Security | IdP | Collect,    | Connector: Content   |     |     |
| ------------ | --- | ----------- | -------------------- | --- | --- |
|              |     | Third party | Type: Trust Monitor, |     |     |
msg_class:
duosecurity_trust
_monitor
ESET Webhook Respond ESET Protect: Parser (Syslog ESET PROTECT
|     |     | (templates in Integration of Third | JSON format),      |     |     |
| --- | --- | ---------------------------------- | ------------------ | --- | --- |
|     |     | Universal Party Native Alerts      | Content Type: N/A, |     |     |
Webhook

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
|     |     | Responder), | msg_class: |     |     |
| --- | --- | ----------- | ---------- | --- | --- |
Third party
eset_protect
ESET Cloud Office   Third party ESET Cloud Office Parser (Syslog
| Security (ECOS) |     | Security: Integration of | format), Content |     |     |
| --------------- | --- | ------------------------ | ---------------- | --- | --- |
|                 |     | Third Party Native       | Type: N/A,       |     |     |
|                 |     | Alerts                   | msg_class:       |     |     |
 eset_cos_googled
rive,
eset_cos_gmail,
eset_cos_team,
eset_cos_exchange
,
eset_cos_sharepoi
nt, or
eset_cos_onedrive
ExtraHop Reveal(x) 360 NDR Collect, ExtraHop Reveal(x) Connector, Content ExtraHop Yes, Content Type:
|     |     | Third party 360: Integration of ThirdType: Detections, |            | Reveal(x) 360 | Devices |
| --- | --- | ------------------------------------------------------ | ---------- | ------------- | ------- |
|     |     | Party Native Alerts                                    | msg_class: |               |         |
extrahop_reveal_x
_360_detections
| F5 BIG-IP ASM      | Firewall | Respond   |     |               |                    |
| ------------------ | -------- | --------- | --- | ------------- | ------------------ |
| F5 BIG-IP Firewall | Firewall | Respond   |     | F5 Big IP     |                    |
| F5 Silverline      | Firewall | Respond   |     | F5 Silverline |                    |
| Firewalla Managed  | Firewall | Collect   |     |               | Yes, Content Type: |
| Security Portal    |          |           |     |               | Device             |
Endpoint Security
| Forescout |     | Respond   |     | ForeScout |     |
| --------- | --- | --------- | --- | --------- | --- |
FortiEDR Endpoint Security Collect, FortiEDR: Integration of Connector, Content Fortinet FortiEDR
|     |     | Third party Third Party Native | Type: Events, |     |     |
| --- | --- | ------------------------------ | ------------- | --- | --- |
|     |     | Alerts                         | msg_class:    |     |     |
fortiedr_events
| Fortigate | Firewall | Respond   |     | Fortinet |     |
| --------- | -------- | --------- | --- | -------- | --- |
FortiGate(FW
class)
| FortiManager | Firewall | Respond   |     |     |     |
| ------------ | -------- | --------- | --- | --- | --- |

Fortinet Lacework Third party Fortinet Lacework: Generic S3 Generic S3
cloudsec
| via Generic S3 |     | Integration of Third | Connector, Content |     |     |
| -------------- | --- | -------------------- | ------------------ | --- | --- |
|                |     | Party Native Alerts  | Type: Alert,       |     |     |
msg_class:
generic_s3_fortin
et_lacework_alert
_details
| Fortra Frontline | Vulnerability Scanner | Collect   |     |     |     |
| ---------------- | --------------------- | --------- | --- | --- | --- |

| Generic S3         | PaaS | Collect   |     | Generic S3    |     |
| ------------------ | ---- | --------- | --- | ------------- | --- |
| Google Cloud Audit | PaaS | Collect   |     | Google Cloud  |     |
| Logging            |      |           |     | Audit Logging |     |
|                    | SaaS | Collect   |     |               |     |
Google Cloud Security
Command Center
Google Workspace SaaS Collect, Google Workspace: Connector, Content G-Suite
|     |     | Third party Integration of Third | Type: Alert, |     |     |
| --- | --- | -------------------------------- | ------------ | --- | --- |
|     |     | Party Native Alerts              | msg_class:   |     |     |
gsuite_alert
Group-IB Endpoint Security Collect, Group IB: Integration of Connector, Content   Yes, Content Type:
|     |     | Third party Third Party Native | Type: Alerts, |     | Assets |
| --- | --- | ------------------------------ | ------------- | --- | ------ |
|     |     | Alerts                         | msg_class:    |     |        |
group_ib_alerts

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
Endpoint Security
Halcyon Collect, Halcyon: Integration of Connector, Content
|     |     | Third party Third Party Native | Type: Alerts, |     |     |
| --- | --- | ------------------------------ | ------------- | --- | --- |
|     |     | Alerts                         | msg_class:    |     |     |
halcyon_alerts
| HanDreamNet (HDN) | Security Switch   | Respond   |     |       |     |
| ----------------- | ----------------- | --------- | --- | ----- | --- |
| HIBUN             | Endpoint Security | Collect   |     | Hibun |     |

| Hillstone | Firewall | Respond   |     | Hillstone(FW |     |
| --------- | -------- | --------- | --- | ------------ | --- |
class)
Hoxhunt Email Collect, HoxHunt: Integration of Connector: Content
|     |     | Third party Third Party Native | Type: Threats, |     |     |
| --- | --- | ------------------------------ | -------------- | --- | --- |
|     |     | Alerts                         | msg_class:     |     |     |
hoxhunt_threats
Huntress Endpoint Security Collect, Huntress: Integration of Connector, Content Huntress Yes, Content
|     |     | Third party Third Party Native | Type: Incident      |     | Type: Agents |
| --- | --- | ------------------------------ | ------------------- | --- | ------------ |
|     |     |   Alerts                       | Reports, msg_class: |     |              |
huntress_incident
_report
HYAS Protect DNS Security Collect, HYAS Protect: Connector, Content HYAS Protect Yes, Content
|     |     | Third party Integration of Third | Type: DNS Log       |     | Type: Agents |
| --- | --- | -------------------------------- | ------------------- | --- | ------------ |
|     |     | Party Native Alerts              | Reports, msg_class: |     |              |
hyas_protect_dns_
log_report
| iManage Threat ManagerData Loss Prevention |     | Collect   |     |     |     |
| ------------------------------------------ | --- | --------- | --- | --- | --- |
Imperva Incapsula Web Security Collect     Imperva Incapsula Yes, Content
Type: Logs
| Indusface  | Web Security | Collect   |     | Indusface |     |
| ---------- | ------------ | --------- | --- | --------- | --- |
| Ironscales | Email        | Collect   |     |           |     |
IronScales SIEM
| Jamf Pro | Asset Management | Collect   |     |     |     |
| -------- | ---------------- | --------- | --- | --- | --- |
Endpoint Security
| Jamf Protect |     | Collect   |     | Jamf Protect | Yes, Content |
| ------------ | --- | --------- | --- | ------------ | ------------ |
Types: Alerts and
Computers
| JumpCloud    | IdP                        | Collect   |     |          |     |
| ------------ | -------------------------- | --------- | --- | -------- | --- |
| Juniper Mist | NDR                        | Collect   |     |          |     |
| LastPass     | Password ManagementCollect |           |     | LastPass |     |
LimaCharlie Endpoint Security Collect, LimaCharlie: IntegrationConnector, Content LimaCharlie Yes, Content
|     |     | Third party of Third Party Native | Type: Alerts, |     | Type: Sensors |
| --- | --- | --------------------------------- | ------------- | --- | ------------- |
|     |     | Alerts                            | msg_class:    |     |               |
limacharlie_alert
| Liongard | Asset Management | Collect   |     |     |     |
| -------- | ---------------- | --------- | --- | --- | --- |

| Mailprotector                       |       | Collect   |     |     |     |
| ----------------------------------- | ----- | --------- | --- | --- | --- |
|                                     | Email |           |     |     |     |
| Manage Engine EndpointIT Management |       | Collect   |     |     |     |
Central
| Memcyco |              | Collect |     |     | Yes, Content |
| ------- | ------------ | ------- | --- | --- | ------------ |
|         | Web Security |         |     |     |              |
Type: Devices
Microsoft Defender for SaaS Collect, Microsoft Defender for Connector, Content Microsoft Defender
Cloud Apps Third party Cloud Apps: Integration for Cloud Apps
Type: Alerts,
|     |     | of Third Party Native | msg_class:        |     |     |
| --- | --- | --------------------- | ----------------- | --- | --- |
|     |     | Alerts                | microsoft_defende |     |     |
r_for_cloud_apps_
alerts

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
Endpoint Security
Microsoft Defender for Collect, Microsoft Defender for Connector, Content Microsoft DefenderYes, Content
Endpoint Respond, Endpoint: Integration of Type: Alerts, Type: Host
Third party Third Party Native
msg_class: microso
|     |     | Alerts | ft_defender_alert |     |     |
| --- | --- | ------ | ----------------- | --- | --- |
s
Microsoft Entra ID SaaS Collect, Microsoft Entra ID: Connector, Content Azure AD
|     |     | Respond, Integration of Third   | Type: Risk Detection |     |     |
| --- | --- | ------------------------------- | -------------------- | --- | --- |
|     |     | Third party Party Native Alerts | Collection,          |     |     |
msg_class:
azure_ad_risk_det
ection
|                        | Endpoint Security |           |     |     |     |
| ---------------------- | ----------------- | --------- | --- | --- | --- |
| Microsoft Graph Intune |                   | Collect   |     |     |     |
| Microsoft Graph        | Email             | Collect   |     |     |     |
Message Trace
Microsoft Graph Security Extended Detection Collect, Microsoft Defender Connector, Content
| API | & Response | Third party XDR: Integration of | Type: Alert , |     |     |
| --- | ---------- | ------------------------------- | ------------- | --- | --- |
Third Party Native
msg_class:
|     |     | Alerts                 | microsoft_graph_d |     |     |
| --- | --- | ---------------------- | ----------------- | --- | --- |
|     |     | and Microsoft Defender | efender_xdr_alert |     |     |
for Endpoint(Graph
and Content
|     |     | Security API): | Type: Alerts, |     |     |
| --- | --- | -------------- | ------------- | --- | --- |
Integration of Third
msg_class: microso
Party Native Alerts
ft_defender_for_e
|     |     | and Microsoft Defender | ndpoint_alerts |     |     |
| --- | --- | ---------------------- | -------------- | --- | --- |
for Cloud Apps (Graph
and Content Type:
Security API):
Alerts, msg_class:
Integration of Third
microsoft_defende
Party Native Alerts
r_for_cloud_apps_
and Microsoft Defender
alerts
for Cloud (Graph
and Content Type:
Security API):
Microsoft Defender
Integration of Third
|     |     | Party Native Alerts | for Cloud, |     |     |
| --- | --- | ------------------- | ---------- | --- | --- |
msg_class:
microsoft_defende
r_for_cloud_alert
s
| Microsoft SQL Server | Database | Collect   |     |     | Yes, Content |
| -------------------- | -------- | --------- | --- | --- | ------------ |
Type: Client agent
status Logs (Klassify)
Mimecast API 1.0 Email Collect, Mimecast: Integration ofConnector, Content Mimecast

|                   |                       | Third party Third Party Native             | Type: MTA Log, msg- |          |     |
| ----------------- | --------------------- | ------------------------------------------ | ------------------- | -------- | --- |
|                   |                       | Alerts                                     | class: several      |          |     |
| Mime cast API 2.0 | Email                 | Collect,                                   |                     | Mimecast |     |
|                   |                       | Mimecast: Integration ofConnector, Content |                     |          |     |
|                   |                       | Third party Third Party Native             | Type: MTA Log, msg- |          |     |
|                   |                       | Alerts                                     | class: several      |          |     |
| MySQL             | Database              | Collect                                    |                     |          |     |
| NetFoundry        | SASE                  | Collect                                    |                     |          |     |
| Nessus            | Vulnerability Scanner | Collect                                    |                     |          | Yes |
Netskope Web Security Collect, Netskope: Integration ofConnector, Content Netskope WSG
|     |     | Respond Third Party Native | Type: Alert,      |     |     |
| --- | --- | -------------------------- | ----------------- | --- | --- |
|     |     | (templates in Alerts       | msg_class:        |     |     |
|     |     | Universal                  | netskopewsg_alert |     |     |
Webhook
Responder),
Third party
| Nodeware | Vulnerability Scanner | Collect   |     |     |     |
| -------- | --------------------- | --------- | --- | --- | --- |

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
| NodeZero | Penetration Testing | Collect   |     |     | Yes, Content |
| -------- | ------------------- | --------- | --- | --- | ------------ |
Type: Hosts
| NordStellar | Threat Intel Vendor | Collect   |     |     |     |
| ----------- | ------------------- | --------- | --- | --- | --- |

Office 365 SaaS Collect, Office 365: Integration Connector, Content Office365
|     |     | Third party of Third Party Native | Type: Audit General, |     |     |
| --- | --- | --------------------------------- | -------------------- | --- | --- |
|     |     | Alerts                            | msg_class:           |     |     |
office365_audit_g
eneral
| Office 365 Reporting | SaaS | Collect   |     |     |     |
| -------------------- | ---- | --------- | --- | --- | --- |
Web Service
| Okta     | IdP | Collect   |     | Okta     |     |
| -------- | --- | --------- | --- | -------- | --- |
| OneLogin | IdP | Collect   |     | OneLogin |     |
Oracle Cloud PaaS Collect, Oracle Cloud Connector, Content OCI Logs
| Infrastructure (OCI) |     | Third party Infrastructure (OCI)  | Type: N/A,        |     |     |
| -------------------- | --- | --------------------------------- | ----------------- | --- | --- |
| Streaming            |     | CloudGuard: Integrationmsg_class: |                   |     |     |
|                      |     | of Third Party Native             | oracle_cloud_guar |     |     |
Alerts
d
Palo Alto Networks Endpoint Security Collect, Palo Alto Networks Connector, Content Palo Alto NetworksYes, Content
CORTEX XDR Respond, CORTEX XDR: Type: Alerts, CORTEX Type: Endpoints
|     |     | Third party Integration of Third | msg_class:        |     |     |
| --- | --- | -------------------------------- | ----------------- | --- | --- |
|     |     | Party Native Alerts              | palo_alto_network |     |     |
s_cortex_xdr_aler
ts
| Palo Alto Networks | Firewall | Respond   |     | Palo Alto Networks  |     |
| ------------------ | -------- | --------- | --- | ------------------- | --- |
| Firewall           |          |           |     | Firewall            |     |
| Palo Alto Networks | Firewall | Respond   |     | Palo Alto           |     |
| Panorama           |          |           |     | Panorama(FW         |     |
class)
| People Risk Explorer   | Email | Collect   |     |     |     |
| ---------------------- | ----- | --------- | --- | --- | --- |
| Perception Point X-Ray |       | Collect   |     |     |     |
|                        | Email |           |     |     |     |
Prisma Cloud Cloud Security Collect, Prisma Cloud: Connector, Content Palo Alto Networks
|     |     | Third party Integration of Third | Type: Alert, | Prisma Cloud      |     |
| --- | --- | -------------------------------- | ------------ | ----------------- | --- |
|     |     | Party Native Alerts              | msg_class:   | (Compute Edition) |     |
palo_alto_network
s_prisma_cloud
| Proofpoint on Demand | Email | Collect,   |     | Proofpoint |     |
| -------------------- | ----- | ---------- | --- | ---------- | --- |
Respond
(templates in
Universal
Webhook
Responder)
Proofpoint TAP Email Collect, Proofpoint Targeted Connector, Content Proofpoint
|     |     | Third party Attack Protection (TAP):Type: Events, |            | Targeted Attack |     |
| --- | --- | ------------------------------------------------- | ---------- | --------------- | --- |
|     |     | Integration of Third                              | msg_class: | Protection      |     |
Party Native Alerts
proofpoint_tap_ev
ent
| Qualys | Vulnerability Scanner | Collect   |     |     | Yes, Content |
| ------ | --------------------- | --------- | --- | --- | ------------ |
Type: Hosts
| Qualys FIM | Vulnerability Scanner | Collect   |     |     | Yes, Content |
| ---------- | --------------------- | --------- | --- | --- | ------------ |
Type: Asset
| Rapid7 | Vulnerability Scanner | Collect   |     | Rapid7 | Yes |
| ------ | --------------------- | --------- | --- | ------ | --- |
Recorded Future Cloud Security Collect, Recorded Future: Connector, Content Recorded Future
|     |     | Third party Integration of Third | Type: Alert and |     |     |
| --- | --- | -------------------------------- | --------------- | --- | --- |
|     |     | Party Native Alerts              | Playbook Alert, |     |     |
msg_class:

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
recorded_future_a
lert and
recorded_future_p
laybook_alert
| Remote SSH Host | Remote Host | Respond   |     |            |     |
| --------------- | ----------- | --------- | --- | ---------- | --- |
| Salesforce      | SaaS        | Collect   |     | Salesforce |     |
SentinelOne Endpoint Security Collect, SentinelOne Cloud: Connector, Content SentinelOne Yes, Content
|     |     | Respond, Integration of Third   | Type: Threat,     |     | Type: Host |
| --- | --- | ------------------------------- | ----------------- | --- | ---------- |
|     |     | Third party Party Native Alerts | msg_class:        |     |            |
|     |     | and SentinelOne                 | sentinelone_threa |     |            |
t_detection
Singularity Identity:
|     |     | Integration of Third | and Content Type: |     |     |
| --- | --- | -------------------- | ----------------- | --- | --- |
|     |     | Party Native Alerts  | Unified Alerts,   |     |     |
msg_class:
sentinelone_unifi
ed_alerts
| SOCRadar | Endpoint Security | Collect, Socradar: Integration of | Connector: Content |     |     |
| -------- | ----------------- | --------------------------------- | ------------------ | --- | --- |
|          |                   |                                   |                    |     |     |
|          |                   | Third party Third Party Native    | Type: Incidents,   |     |     |
|          |                   | Alerts                            | msg_class:         |     |     |
socradar_incident
s
SonicWall Capture Client Endpoint Security Collect,       Yes, Content
|                    |                   | Respond                              |                    |     | Type: Host |
| ------------------ | ----------------- | ------------------------------------ | ------------------ | --- | ---------- |
| SonicWall Endpoint | Endpoint Security | Collect, SonicWall Endpoint          | Connector, Content |     |            |
|                    |                   |                                      |                    |     |            |
| Security           |                   | Third party Security: Integration of | Type: Alerts,      |     |            |
|                    |                   | Third Party Native                   | msg_class:         |     |            |
|                    |                   | Alerts                               | sonicwall_theron_  |     |            |
alerts
| SonicWall Firewall | Firewall | Respond   |     | SonicWall(FW |     |
| ------------------ | -------- | --------- | --- | ------------ | --- |
class)
Sophos Central Endpoint Security Collect, Sophos Central: Connector, Content Sophos Endpoint Yes, Content
|     |     | Respond, Integration of Third   | Type: Alerts and   |     | Types: Alerts and |
| --- | --- | ------------------------------- | ------------------ | --- | ----------------- |
|     |     | Third party Party Native Alerts | Events, msg_class: |     | Events            |
 sophos_alerts and
sophos_events
| Sophos XG | Firewall | Respond   |     | Sophos |     |
| --------- | -------- | --------- | --- | ------ | --- |
XG Firewall
| Stellar Cyber | Extended Detection | Collect   |     |     |     |
| ------------- | ------------------ | --------- | --- | --- | --- |
& Response
| Stormshield Network     | Firewall | Respond   |     | Stormshield Net   |     |
| ----------------------- | -------- | --------- | --- | ----------------- | --- |
| Security (SNS) Firewall |          |           |     | Security Firewall |     |
(FW class)
| Sucuri Security        | Web Security          | Collect   |     |     |              |
| ---------------------- | --------------------- | --------- | --- | --- | ------------ |
| Tenable Cloud Security | Cloud Security        | Collect   |     |     |              |
| Tenable.io             | Vulnerability Scanner | Collect   |     |     | Yes, Content |
Type: Vulnerabilities
| Tenable.sc | Vulnerability Scanner | Collect   |     |     | Yes, Content |
| ---------- | --------------------- | --------- | --- | --- | ------------ |
Type: Vulnerabilities
Thinkst Canary Honeypot Collect     Thinkst Canary Yes, Content
Type: Devices
Endpoint Security
| ThreatDown OneView     |     | Collect   |     |     | Yes, Content    |
| ---------------------- | --- | --------- | --- | --- | --------------- |
| (formerly Malwarebytes |     |           |     |     | Type: Endpoints |
OneView)
Endpoint Security
| Threatlocker |     | Collect   |     |     |     |
| ------------ | --- | --------- | --- | --- | --- |

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
Trellix (FireEye) EndpointEndpoint Security Collect, Trellix (FireEye) Connector, Content FireEye HX Yes, Content Type:
| Security HX |     | Third party Endpoint    | Type: Alerts,  |     | Hosts |
| ----------- | --- | ----------------------- | -------------- | --- | ----- |
|             |     | Security:Integration of | msg_class:     |     |       |
|             |     | Third Party Native      | fireeye_alerts |     |       |
Alerts
Trellix MVISION Endpoint Security Collect, Trellix MVISION: Connector, Content Trellix MVISION Yes, Content
|     |     | Third Party Integration of Third | Type: Alerts, |     | Type: Devices |
| --- | --- | -------------------------------- | ------------- | --- | ------------- |
|     |     | Party Native Alerts              | msg_class:    |     |               |
trellix_mvision_e
dr_alerts
Trend Micro Apex Endpoint Security Collect     Trend Micro - ApexYes, Content Types:
| Central |     |     |     | Central | Agents and Servers |
| ------- | --- | --- | --- | ------- | ------------------ |
Trend Micro Cloud App Cloud Security Collect, Trend Micro Cloud App Connector, Content
| Security |     | Third party Security: Integration of | Types: Exchange,    |     |     |
| -------- | --- | ------------------------------------ | ------------------- | --- | --- |
|          |     | Third Party Native                   | OneDrive,           |     |     |
|          |     | Alerts                               | Sharepoint Log, and |     |     |
Teams, msg_class:
 trendmicro_cas_l
ogs_exchange,
trendmicro_cas_lo
gs_onedrive,
trendmicro_cas_lo
gs_sharepoint, and
trendmicro_cas_lo
gs_teams
Trend Micro Cloud One Endpoint Security Collect       Yes, Content
| Workload Security |       |           |     |     | Type: Computers |
| ----------------- | ----- | --------- | --- | --- | --------------- |
| Trend Micro Email | Email | Collect   |     |     |                 |
|                   |       |           |     |     |                 |
Security
Trend Micro Vision One Endpoint Security Collect, Trend Micro Vision Connector, Content Trend Micro Vision
|     |     | Respond One: Integration of      | Type: Alerts,     | One |     |
| --- | --- | -------------------------------- | ----------------- | --- | --- |
|     |     | (templates in Third Party Native | msg_class:        |     |     |
|     |     | Universal Alerts                 | trendmicro_vision |     |     |
|     |     | Webhook                          | one_alerts        |     |     |
Responder),
Third party
| Universal Webhook | Webhook | Respond   |     |     |     |
| ----------------- | ------- | --------- | --- | --- | --- |
(Custom)
| VadeSecure | Email | Collect   |     |     |     |
| ---------- | ----- | --------- | --- | --- | --- |
Varonis DatAdvantage   Third party Varonis DatAdvantage: Parser (CEF format), Varonis-
|     |     | Integration of Third | Content Type: N/A, | Datadvantage |     |
| --- | --- | -------------------- | ------------------ | ------------ | --- |
|     |     | Party Native Alerts  | msg_class:         |              |     |
 varonis_datadvan
tage_file_system_
operation or
varonis_datadvant
age_directory_ser
vices_operation
| Verkada |                    | Collect   |     |     |     |
| ------- | ------------------ | --------- | --- | --- | --- |
|         | Internet of Things |           |     |     |     |
Security
|                         | SASE     |           |     | Versa Networks |     |
| ----------------------- | -------- | --------- | --- | -------------- | --- |
| Versa Networks          |          | Collect   |     |                |     |
| Concerto                |          |           |     | SASE           |     |
|                         | Firewall |           |     | Versa Networks |     |
| Versa Networks Firewall |          | Respond   |     |                |     |
Firewall
Vicarius Vulnerability Scanner Collect       Yes, Content Type:
Assets
VMware Carbon Black Endpoint Security Collect, VMware Carbon Black Connector, Content Carbon Black Yes, Content Type:
| Cloud |     | Respond, Cloud: Integration of | Type: Alert, |     | Alert |
| ----- | --- | ------------------------------ | ------------ | --- | ----- |

Detections
|                |                    | Integration Third Party Alert | Third Party Based |         |                 |
| -------------- | ------------------ | ----------------------------- | ----------------- | ------- | --------------- |
| Connector Name | Connector Category |                               |                   | (Select | Asset Discovery |
|                |                    | Function Integration Name     | On                |         |                 |
Applications)
|     |     | Third party Third Party Native | msg_class: carbonb |     |     |
| --- | --- | ------------------------------ | ------------------ | --- | --- |
Alerts
lack_alert
| VMware Workspace   | Endpoint Security | Collect   |     | VMware        |     |
| ------------------ | ----------------- | --------- | --- | ------------- | --- |
| ONE                |                   |           |     | Workspace One |     |
| WatchGuard Firebox | Webhook           | Respond   |     |               |     |
(templates in
Universal
Webhook
Responder)
Webroot Endpoint Security Collect     Webroot Yes, Content Type:
Endpoints
Windows Defender   Third party Windows Defender Windows agent, Windows Agent
| Antivirus |     | Antivirus: Integration of | Content Type: N/A, |     |     |
| --------- | --- | ------------------------- | ------------------ | --- | --- |
|           |     | Third Party Native        | msg_class:         |     |     |
|           |     | Alerts                    | Microsoft-         |     |     |
Windows-Windows
Defender
WithSecure Elements Endpoint Security, Collect, WithSecure Elements: Connector: Content Yes, Content Type:

|     | Webhook | Respond Integration of Third      | Type: Detections,   |     | Devices |
| --- | ------- | --------------------------------- | ------------------- | --- | ------- |
|     |         | (templates in Party Native Alerts | msg_class:          |     |         |
|     |         | Universal                         | withsecure_elements |     |         |
|     |         | Webhook                           | _detection          |     |         |
Responder),
Third party
Wiz Cloud Security Collect, Wiz: Integration of ThirdConnector: Content
|     |     | Third party Party Native Alerts | Type: Issues, |     |     |
| --- | --- | ------------------------------- | ------------- | --- | --- |
msg_class:
wiz_issues
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber. All rights reserved.
Support  |  Contact Us  |       