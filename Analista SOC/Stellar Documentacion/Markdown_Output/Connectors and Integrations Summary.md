✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Connectors and Integrations Summary
The table below summarizes Stellar Cyber connectors and third party alert integrations and
correlates them to assets.
Definitions
The definitions in the table are as follows:
Connector— A method of collecting information and compiling it into Interflow records
that are indexed and stored in the Data Lake. Stellar Cyber develops connectors based
on the access methods provided for each external data source, typically an API. These
processes run on the Data Processor (DP) to fetch information actively on a scheduled
basis. Connectors collect data from external sources and can also respond to actions
such as blocking on a firewall or disabling users. The connection to a data source can
be configured in Stellar Cyber. For all connectors, see Connector Types & Functions.
Collect—A function of a connector that collects data from external data sources and
adds it to the Data Lake.
Respond—A function of a connector that takes actions on external data sources in
response to detected security events.
Third party alert integration—The process of ingesting, normalizing, and enriching alerts
that are natively created by third party services. These alerts are then mapped to the
Stellar Cyber XDR Kill Chain and added to the Alert index. The integration allows for the
correlation of third-party native alerts with Stellar Cyber's alerts, leveraging Machine
Learning (ML) and Security Analytics (SA) to enhance the alert data. This process
includes deduplication to reduce noise. For all third party alert integrations, see
Integration of Third Party Native Alerts.
Detections—The identification of potential threats or risky behavior using various
techniques such as Machine Learning (ML) and Security Analytics (SA), as well as
rules, and third party alert integration. Detections can be based on known bad
behaviors, anomalies, or suspicious activities identified through different methods.
These detections generate alerts which are then correlated into cases for further
investigation.

Asset Discovery—The process of identifying assets and tracking assets within a
network from observed data using a passive discovery service. This service can
discover assets via data collected from various sources such as endpoint data sources
(for example, EDR or Directory Services), cloud audit logs, traffic-related sources (for
example, firewalls), Stellar Cyber server sensors (Linux and Windows), Stellar Cyber
modular sensors, and other log sources or connectors. The discovered assets can
include both IP and MAC addresses, which are associated with hosts. This process
happens in real time as new data comes into the system, and the unique assets are
counted daily. The discovered data is then used to analyze the behavior of these assets
to detect security events.
Legend
The columns in the table are as follows:
Connector Name—The name of the connector in alphabetic order, and a link to the
document
Connector Category—The category to which the connector belongs
Integration Function—The function of the integration:
Collect—only collect
Respond—only respond
Collect, Respond—both collect and respond
Third party—third party alert integration
Third Party Alert Integration Name—The name of the third party alert integration and a
link to the document
Third Party Based On—What the third party alert integration is based on:
connector, and if there is a specific content type that needs to be configured,
as well as the msg_class
parser, and if there is a specific format, such as CEF
Windows agent
Detections—What to enter in the Stellar Cyber Detections & Response page
(https://detections.stellarcyber.ai/v/6.6.0 ) in the Select Applications field to produce
a list of detections and third party alert integrations supported for a data source
Asset Discovery—Whether the data source sends assets to the Assets index
Connectors and Integrations Table
Integratio Detections
Connector Third Party Alert Third Party
Connector Name n (Select Asset Discovery
Category Integration Name Based On
Function Applications)
1Password Password Collect
1Password
Management

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
Abnormal Security Email Collect, Abnormal Security Connector,
|                |     |             |                      |                | Abnormal |     |
| -------------- | --- | ----------- | -------------------- | -------------- | -------- | --- |
| Email Security |     | Third party |                      |                |          |     |
|                |     |             | Email Security:      | Content        | Security |     |
|                |     |             | Integration of Third | Type: Threats, |          |     |
|                |     |             | Party Native Alerts  | msg_class:     |          |     |
abnormal_secur
ity_email_secu
rity_threat
| Acronis Cyber | Endpoint Security | Collect,    |                      |               |               |              |
| ------------- | ----------------- | ----------- | -------------------- | ------------- | ------------- | ------------ |
|               |                   |             | Acronis: Integration | Connector,    | Acronis Cyber | Yes, Content |
| Protect Cloud |                   | Respond,    |                      |               |               |              |
|               |                   |             | of Third Party       | Content       | Protect       | Type: Agents |
|               |                   | Third party | Native Alerts        | Type: Alerts, |               |              |
msg_class:
acronis_cyber_
protect_alert
| Active Directory | IdP | Collect, |     |     |        |              |
| ---------------- | --- | -------- | --- | --- | ------ | ------------ |
|                  |     |          |     |     | Active | Yes, Content |
Respond
|        |                   |         |     |     | Directory | Type: Computers |
| ------ | ----------------- | ------- | --- | --- | --------- | --------------- |
| Akamai | Endpoint Security | Collect |     |     |           | Yes, Content    |
Type: Connectors
| Amazon Security | Web Security | Collect |     |     |        |     |
| --------------- | ------------ | ------- | --- | --- | ------ | --- |
|                 |              |         |     |     | Amazon |     |
Lake
Security Lake
Armis Endpoint Security Collect, Armis: Integration Connector, Yes, Content
Armis
Third party
|     |     |     | of Third Party | Content       |     | Type: Devices |
| --- | --- | --- | -------------- | ------------- | --- | ------------- |
|     |     |     | Native Alerts  | Type: Alerts, |     |               |
msg_class:
armis_alerts
| Aruba Central | Network Managem | Collect |     |     |     |     |
| ------------- | --------------- | ------- | --- | --- | --- | --- |
|               |                 |         |     |     |     |     |
ent
| Automox | IT Management | Collect |     |     |     | Yes, Content |
| ------- | ------------- | ------- | --- | --- | --- | ------------ |

Type: Devices
Avanan   Third party Avanan: Integration Parser (HTTP Avanan
|     |     |     | of Third Party | JSON format), |     |     |
| --- | --- | --- | -------------- | ------------- | --- | --- |
|     |     |     | Native Alerts  | Content Type: |     |     |
N/A, msg_class:
avanan
|     | PaaS | Collect |     |     | AWS Cloudtrail |     |
| --- | ---- | ------- | --- | --- | -------------- | --- |
AWS CloudTrail
| AWS CloudWatch | PaaS | Collect |     |     | AWS Cloudwat |     |
| -------------- | ---- | ------- | --- | --- | ------------ | --- |
ch

|                |           | Integratio  |                      |                 | Detections    |                 |
| -------------- | --------- | ----------- | -------------------- | --------------- | ------------- | --------------- |
|                | Connector |             | Third Party Alert    | Third Party     |               |                 |
| Connector Name |           | n           |                      |                 | (Select       | Asset Discovery |
|                | Category  |             | Integration Name     | Based On        |               |                 |
|                |           | Function    |                      |                 | Applications) |                 |
| AWS Firewall   | Firewall  | Respond     |                      |                 |               |                 |
| AWS GuardDuty  | PaaS      | Collect,    | AWS GuardDuty:       | Connector,      | AWS           |                 |
|                |           | Third party | Integration of Third | Content Type:   | GuardDuty     |                 |
|                |           |             | Party Native Alerts  | N/A, msg_class: |               |                 |
aws_guardduty_
finding
| AWS Inspector | Vulnerability | Collect |     |     |     |     |
| ------------- | ------------- | ------- | --- | --- | --- | --- |
Scanner
Azure Event Hub PaaS Collect, Microsoft Defender Connector, Azure Event
|     |     | Third party | for Cloud:           | Content Type: | Hub, Microsoft |     |
| --- | --- | ----------- | -------------------- | ------------- | -------------- | --- |
|     |     |             | Integration of Third | Microsoft     | Defender for   |     |
|     |     |             | Party Native Alerts  | Defender for  | Cloud,         |     |
|     |     |             |                      | Cloud,        | Microsoft      |     |
and Microsoft
|     |     |     |     | msg_class: | Sentinel |     |
| --- | --- | --- | --- | ---------- | -------- | --- |
Sentinel:
|     |     |     | Integration of Third | microsoft_defe |     |     |
| --- | --- | --- | -------------------- | -------------- | --- | --- |
nder_cloud
Party Native Alerts
and Content
Type: Microsoft
Sentinel,
msg_class:
microsoft_sent
inel
| Azure NSG       | Firewall | Respond |     |     |           |     |
| --------------- | -------- | ------- | --- | --- | --------- | --- |
| Barracuda Email | Email    | Respond |     |     | Barracuda |     |
Email
| Barracuda Firewall | Firewall | Respond |     |     | Barracuda |     |
| ------------------ | -------- | ------- | --- | --- | --------- | --- |
Firewall Logs
| Barracuda WAF | Web Security | Collect |     |     |     |     |
| ------------- | ------------ | ------- | --- | --- | --- | --- |
Barracuda
WAF
| BeyondTrust | Privileged Access | Collect |     |     |     |     |
| ----------- | ----------------- | ------- | --- | --- | --- | --- |
Management
Endpoint Security
Bitdefender Respond, Bitdefender: Integr Parser (Syslog BitDefender
|     |     | Third party | ation of Third Party | JSON format), |     |     |
| --- | --- | ----------- | -------------------- | ------------- | --- | --- |
|     |     |             | Native Alerts        | Content Type: |     |     |
N/A, msg_class:
several

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
Blackberry Cylance Endpoint Security Respond Blackberry Cylance logs, Cylance
|     |     | (templates | CylancePROTECT | Content Type:   | Optics, |     |
| --- | --- | ---------- | -------------- | --------------- | ------- | --- |
|     |     | in         | and            | N/A, msg_class: | Cylance |     |
|     |     | Universal  | CylanceOPTICS: |                 | Protect |     |
cylance_protec
|     |     | Webhook   | Integration of Third | t_alert |     |     |
| --- | --- | --------- | -------------------- | ------- | --- | --- |
|     |     | Responder | Party Native Alerts  |         |     |     |
),
Third party
| Box | SaaS | Collect |     |     |     |     |
| --- | ---- | ------- | --- | --- | --- | --- |
Broadcom Endpoint Security Collect, Broadcom SES: Connector. Broadcom SES Yes, Content
Symantec Endpoint Third party Integration of Third Content Type: Type: Devices
| Security (SES) |     |     | Party Native Alerts | Incidents, |     |     |
| -------------- | --- | --- | ------------------- | ---------- | --- | --- |
msg_class.
broadcom_ses_i
ncidents
| Broadcom | Cloud Security | Collect |     |     |     |     |
| -------- | -------------- | ------- | --- | --- | --- | --- |
(Symantec) Cloud
Workload Protection
| Broadcom | Email | Collect |     |     |     |     |
| -------- | ----- | ------- | --- | --- | --- | --- |
(Symantec) Email
Security.cloud
| Broadcom (Blue   | Web Security | Collect |     |     | Symantec Web |     |
| ---------------- | ------------ | ------- | --- | --- | ------------ | --- |
| Coat / Symantec) |              |         |     |     | Security     |     |
WSS
Cato Networks SASE Collect, Cato Networks: Connector. Cato Networks
|     |     | Third party | Integration of Third | Content Type: |     |     |
| --- | --- | ----------- | -------------------- | ------------- | --- | --- |
|     |     |             | Party Native Alerts  | Security,     |     |     |
msg_class.
cato_security
| Check Point | Firewall | Respond |     |     | Checkpoint |     |
| ----------- | -------- | ------- | --- | --- | ---------- | --- |
Firewall
| Check Point Smart- | Firewall | Respond |     |     |     |     |
| ------------------ | -------- | ------- | --- | --- | --- | --- |
1 Cloud
Check Point Email Collect, Check Point Connector. Checkpoint
| Harmony Email |     | Third party | Harmony Email:       | Content Type:   | EDR       |     |
| ------------- | --- | ----------- | -------------------- | --------------- | --------- | --- |
|               |     |             | Integration of Third | Security Event, | (Harmony) |     |
|               |     |             | Party Native Alerts  | msg_class.      |           |     |
checkpoint_har

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
mony_security_
event
Endpoint Security
| Cisco AMP |     | Collect |     |     |     | Yes, Content |
| --------- | --- | ------- | --- | --- | --- | ------------ |
Type: Computers
|     | Firewall | Respond |     |     | Cisco |     |
| --- | -------- | ------- | --- | --- | ----- | --- |
Cisco FMC
Firepower(FW
class)
|     | Firewall | Respond |     |     | Meraki |     |
| --- | -------- | ------- | --- | --- | ------ | --- |
Cisco Meraki
Firewall
| Cisco Secure | Cloud Security | Collect |     |     |     |     |
| ------------ | -------------- | ------- | --- | --- | --- | --- |
Access
| Cisco Umbrella | DNS Security  | Collect |     |     | Cisco Umbrella |              |
| -------------- | ------------- | ------- | --- | --- | -------------- | ------------ |
| Cloudflare     | Web Security  | Collect |     |     |                |              |
| CODA Footprint | Vulnerability | Collect |     |     |                | Yes, Content |

|                  | Scanner           |         |     |     |     | Type: Device |
| ---------------- | ----------------- | ------- | --- | --- | --- | ------------ |
| ConnectSecure V4 | Vulnerability     | Collect |     |     |     | Yes, Content |
|                  | Scanner           |         |     |     |     | Type: Asset  |
|                  | Endpoint Security |         |     |     |     |              |
| Coro             |                   | Collect |     |     |     |              |
| CrowdStrike FDR  | Endpoint Security | Collect |     |     |     |              |
CrowdStrike Endpoint Security Collect, CrowdStrike: Connector. Crowdstrike Yes, Content
|     |     | Respond,    | Integration of Third | Content          | (Endpoint) | Type: Host |
| --- | --- | ----------- | -------------------- | ---------------- | ---------- | ---------- |
|     |     | Third party | Party Native Alerts  | Type: EppDetecti |            |            |
onSummaryEven
t or
XdrDetectionSu
mmaryEvent,
msg_class:
crowdstrike.me
tadata.eventTy
pe:EppDetectio
nSummaryEvent
or
crowdstrike_Xd
rDetectionSumm
aryEvent

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
CyberArk EPM Endpoint Security Collect, CyberArk EPM: Connector. CyberArk EPM
|     |     | Third party | Integration of Third | Content Type: |     |     |
| --- | --- | ----------- | -------------------- | ------------- | --- | --- |
|     |     |             | Party Native Alerts  | Events,       |     |     |
msg_class.
cyberark_epm_e
vent
| CyberCNS | Vulnerability | Collect |     |     | CyberCNS |     |
| -------- | ------------- | ------- | --- | --- | -------- | --- |
Scanner
Endpoint Security
Cybereason Collect, Cybereason: Connector: Cont Cybereason Yes, Content
|     |     | Respond,    | Integration of Third | ent Type: MalOp, | (EDR) | Type: Sensor |
| --- | --- | ----------- | -------------------- | ---------------- | ----- | ------------ |
|     |     | Third party | Party Native Alerts  | msg_class:       |       |              |
cybereason_mal
ops_all_types
Cyble Threat Intel Vendor Collect, Cyble: Integration Connector: Cont
|     |     | Third party | of Third Party | ent Type: Alerts, |     |     |
| --- | --- | ----------- | -------------- | ----------------- | --- | --- |
|     |     |             | Native Alerts  | msg_class:        |     |     |
cyble_alerts
Endpoint Security
Cynet Collect, Cynet: Integration Parser (CEF Cynet Yes, Content
|     |     | Respond,    | of Third Party | format),  Content |     | Type: Hosts |
| --- | --- | ----------- | -------------- | ----------------- | --- | ----------- |
|     |     | Third party | Native Alerts  | Type: N/A,        |     |             |
msg_class:
cynet_alert
|     | Vulnerability | Collect |     |     |     | Yes, Content |
| --- | ------------- | ------- | --- | --- | --- | ------------ |
CYRISMA
|           | Scanner |             |                      |                  |     | Type: Host |
| --------- | ------- | ----------- | -------------------- | ---------------- | --- | ---------- |
| Darktrace |         | Third party | Darktrace:           | Parser (CEF      |     |            |
|           |         |             | Integration of Third | format), Content |     |            |
|           |         |             | Party Native Alerts  | Type: N/A,       |     |            |
msg_class:
 darktrace
Endpoint Security
Deep Instinct Collect, Deep Instinct: Connector, Deep Instinct Yes, Content
|     |     | Respond,    | Integration of Third | Content Type: |     | Type: Devices |
| --- | --- | ----------- | -------------------- | ------------- | --- | ------------- |
|     |     | Third party | Party Native Alerts  | Events,       |     |               |
msg_class:
deep_instinct_
maliciousevent
| Duo Security | IdP | Collect,    |     | Connector: Cont |     |     |
| ------------ | --- | ----------- | --- | --------------- | --- | --- |
|              |     | Third party |     | ent Type: Trust |     |     |
Monitor,

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
msg_class:
duosecurity_tr
ust_monitor
| ESET | Webhook | Respond | ESET Protect: | Parser (Syslog |     |     |
| ---- | ------- | ------- | ------------- | -------------- | --- | --- |
ESET PROTE
|     |     | (templates | Integration of Third | JSON format), | CT  |     |
| --- | --- | ---------- | -------------------- | ------------- | --- | --- |
|     |     | in         | Party Native Alerts  | Content       |     |     |
|     |     | Universal  |                      | Type: N/A,    |     |     |
|     |     | Webhook    |                      | msg_class:    |     |     |
|     |     | Responder  |                      | eset_protect  |     |     |
),
Third party
ESET Cloud Office   Third party ESET Cloud Office Parser (Syslog

| Security (ECOS) |     |     | Security:            | format), Content |     |     |
| --------------- | --- | --- | -------------------- | ---------------- | --- | --- |
|                 |     |     | Integration of Third | Type: N/A,       |     |     |
|                 |     |     | Party Native Alerts  | msg_class:       |     |     |
 eset_cos_goog
ledrive,
eset_cos_gmail
,
eset_cos_team,
eset_cos_excha
nge,
eset_cos_share
point, or
eset_cos_onedr
ive
ExtraHop Reveal(x) NDR Collect, ExtraHop Reveal(x) Connector, ExtraHop Yes, Content
360 Third party 360: Integration of Content Reveal(x) 360 Type: Devices
|     |     |     | Third Party Native | Type: Detections, |     |     |
| --- | --- | --- | ------------------ | ----------------- | --- | --- |
|     |     |     | Alerts             | msg_class:        |     |     |
extrahop_revea
l_x_360_detect
ions
| F5 BIG-IP ASM      | Firewall | Respond |     |     |               |              |
| ------------------ | -------- | ------- | --- | --- | ------------- | ------------ |
| F5 BIG-IP Firewall | Firewall | Respond |     |     | F5 Big IP     |              |
| F5 Silverline      | Firewall | Respond |     |     | F5 Silverline |              |
| Firewalla Managed  | Firewall | Collect |     |     |               | Yes, Content |

| Security Portal |     |     |     |     |     | Type: Device |
| --------------- | --- | --- | --- | --- | --- | ------------ |

|                |                   | Integratio |                   |             | Detections    |                 |
| -------------- | ----------------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector         |            | Third Party Alert | Third Party |               |                 |
| Connector Name |                   | n          |                   |             | (Select       | Asset Discovery |
|                | Category          |            | Integration Name  | Based On    |               |                 |
|                |                   | Function   |                   |             | Applications) |                 |
| Forescout      | Endpoint Security | Respond    |                   |             | ForeScout     |                 |
FortiEDR Endpoint Security Collect, FortiEDR: Connector, Fortinet
|     |     | Third party | Integration of Third | Content       | FortiEDR |     |
| --- | --- | ----------- | -------------------- | ------------- | -------- | --- |
|     |     |             | Party Native Alerts  | Type: Events, |          |     |
msg_class:
fortiedr_event
s
| Fortigate | Firewall | Respond |     |     | Fortinet |     |
| --------- | -------- | ------- | --- | --- | -------- | --- |
FortiGate(FW
class)
| FortiManager | Firewall | Respond |     |     |     |     |
| ------------ | -------- | ------- | --- | --- | --- | --- |

Fortinet Lacework cloudsec Third party Fortinet Lacework: Generic S3 Generic S3
|     |     |     | Integration of Third | Connector, |     |     |
| --- | --- | --- | -------------------- | ---------- | --- | --- |
via Generic S3
|     |     |     | Party Native Alerts | Content |     |     |
| --- | --- | --- | ------------------- | ------- | --- | --- |
Type: Alert,
msg_class:
generic_s3_for
tinet_lacework
_alert_details
| Fortra Frontline | Vulnerability | Collect |     |     |     |     |
| ---------------- | ------------- | ------- | --- | --- | --- | --- |

Scanner
| Generic S3         | PaaS | Collect |     |     | Generic S3    |     |
| ------------------ | ---- | ------- | --- | --- | ------------- | --- |
|                    | PaaS | Collect |     |     |               |     |
| Google Cloud Audit |      |         |     |     | Google Cloud  |     |
| Logging            |      |         |     |     | Audit Logging |     |

| Google Cloud | SaaS | Collect |     |     |     |     |
| ------------ | ---- | ------- | --- | --- | --- | --- |
Security Command
Center
| Google Workspace | SaaS | Collect,    | Google               | Connector,   | G-Suite |     |
| ---------------- | ---- | ----------- | -------------------- | ------------ | ------- | --- |
|                  |      | Third party | Workspace:           | Content      |         |     |
|                  |      |             | Integration of Third | Type: Alert, |         |     |
|                  |      |             | Party Native Alerts  | msg_class:   |         |     |
gsuite_alert
Endpoint Security
| Group-IB |     | Collect,    | Group IB:            | Connector,    |     | Yes, Content |
| -------- | --- | ----------- | -------------------- | ------------- | --- | ------------ |
|          |     | Third party | Integration of Third | Content       |     | Type: Assets |
|          |     |             | Party Native Alerts  | Type: Alerts, |     |              |
msg_class:

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
group_ib_alert
s
Endpoint Security
| Halcyon |     | Collect, | Halcyon: | Connector, |     |     |
| ------- | --- | -------- | -------- | ---------- | --- | --- |

|     |     | Third party | Integration of Third | Content       |     |     |
| --- | --- | ----------- | -------------------- | ------------- | --- | --- |
|     |     |             | Party Native Alerts  | Type: Alerts, |     |     |
msg_class:
halcyon_alerts
| HanDreamNet | Security Switch | Respond |     |     |     |     |
| ----------- | --------------- | ------- | --- | --- | --- | --- |
(HDN)
| HIBUN | Endpoint Security | Collect |     |     | Hibun |     |
| ----- | ----------------- | ------- | --- | --- | ----- | --- |

| Hillstone | Firewall | Respond |     |     | Hillstone(FW |     |
| --------- | -------- | ------- | --- | --- | ------------ | --- |
class)
| Hoxhunt |       | Collect,    | HoxHunt:             | Connector: Cont |     |     |
| ------- | ----- | ----------- | -------------------- | --------------- | --- | --- |
|         | Email |             |                      |                 |     |     |
|         |       | Third party | Integration of Third | ent             |     |     |
|         |       |             | Party Native Alerts  | Type: Threats,  |     |     |
msg_class:
hoxhunt_threat
s
Endpoint Security
| Huntress |     | Collect,    | Huntress:            | Connector,     | Huntress | Yes, Content |
| -------- | --- | ----------- | -------------------- | -------------- | -------- | ------------ |
|          |     | Third party | Integration of Third | Content        |          | Type: Agents |
|          |     |             | Party Native Alerts  | Type: Incident |          |              |
Reports,
msg_class:
huntress_incid
ent_report
HYAS Protect DNS Security Collect, HYAS Protect: Connector, HYAS Protect Yes, Content
|     |     | Third party | Integration of Third | Content       |     | Type: Agents |
| --- | --- | ----------- | -------------------- | ------------- | --- | ------------ |
|     |     |             | Party Native Alerts  | Type: DNS Log |     |              |
Reports,
msg_class:
hyas_protect_d
ns_log_report
| iManage Threat | Data Loss  | Collect |     |     |     |     |
| -------------- | ---------- | ------- | --- | --- | --- | --- |
| Manager        | Prevention |         |     |     |     |     |
Imperva Incapsula Web Security Collect     Imperva Yes, Content
|     |     |     |     |     | Incapsula | Type: Logs |
| --- | --- | --- | --- | --- | --------- | ---------- |

|                |              | Integratio |                   |             | Detections    |                 |
| -------------- | ------------ | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector    |            | Third Party Alert | Third Party |               |                 |
| Connector Name |              | n          |                   |             | (Select       | Asset Discovery |
|                | Category     |            | Integration Name  | Based On    |               |                 |
|                |              | Function   |                   |             | Applications) |                 |
| Indusface      | Web Security | Collect    |                   |             | Indusface     |                 |
| Ironscales     | Email        | Collect    |                   |             | IronScales    |                 |
SIEM
| Jamf Pro | Asset Management | Collect |     |     |     |     |
| -------- | ---------------- | ------- | --- | --- | --- | --- |

Endpoint Security
| Jamf Protect |     | Collect |     |     | Jamf Protect | Yes, Content |
| ------------ | --- | ------- | --- | --- | ------------ | ------------ |
Types: Alerts and
Computers
| JumpCloud    | IdP      | Collect |     |     |          |     |
| ------------ | -------- | ------- | --- | --- | -------- | --- |
|              | NDR      |         |     |     |          |     |
| Juniper Mist |          | Collect |     |     |          |     |
| LastPass     | Password | Collect |     |     | LastPass |     |
Management
LimaCharlie Endpoint Security Collect, LimaCharlie: Connector, LimaCharlie Yes, Content
|     |     | Third party | Integration of Third | Content       |     | Type: Sensors |
| --- | --- | ----------- | -------------------- | ------------- | --- | ------------- |
|     |     |             | Party Native Alerts  | Type: Alerts, |     |               |
msg_class:
limacharlie_al
ert
| Liongard | Asset Management | Collect |     |     |     |     |
| -------- | ---------------- | ------- | --- | --- | --- | --- |

| Mailprotector | Email         | Collect |     |     |     |     |
| ------------- | ------------- | ------- | --- | --- | --- | --- |
| Manage Engine | IT Management | Collect |     |     |     |     |
|               |               |         |     |     |     |     |
Endpoint Central
| Memcyco | Web Security | Collect |     |     |     | Yes, Content |
| ------- | ------------ | ------- | --- | --- | --- | ------------ |
Type: Devices
Microsoft Defender SaaS Collect, Microsoft Defender Microsoft
Connector,
| for Cloud Apps |     | Third party | for Cloud Apps: |     | Defender for |     |
| -------------- | --- | ----------- | --------------- | --- | ------------ | --- |
Content
|     |     |     | Integration of Third | Type: Alerts, | Cloud Apps |     |
| --- | --- | --- | -------------------- | ------------- | ---------- | --- |
Party Native Alerts
msg_class:
microsoft_defe
nder_for_cloud
_apps_alerts

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
Microsoft Defender Endpoint Security Collect, Microsoft Defender Microsoft Yes, Content
Connector,
for Endpoint Respond, for Endpoint: Content Defender Type: Host
|     |     | Third party | Integration of Third |     |     |     |
| --- | --- | ----------- | -------------------- | --- | --- | --- |
Type: Alerts,
Party Native Alerts
msg_class: micr
osoft_defender
_alerts
Microsoft Entra ID SaaS Collect, Microsoft Entra ID: Connector, Azure AD
|     |     | Respond,    | Integration of Third | Content    |     |     |
| --- | --- | ----------- | -------------------- | ---------- | --- | --- |
|     |     | Third party | Party Native Alerts  | Type: Risk |     |     |
Detection
Collection,
msg_class:
azure_ad_risk_
detection
| Microsoft Graph | Endpoint Security | Collect |     |     |     |     |
| --------------- | ----------------- | ------- | --- | --- | --- | --- |
Intune
|                 | Email |         |     |     |     |     |
| --------------- | ----- | ------- | --- | --- | --- | --- |
| Microsoft Graph |       | Collect |     |     |     |     |
Message Trace
| Microsoft Graph | Extended | Collect, | Microsoft Defender |            |     |     |
| --------------- | -------- | -------- | ------------------ | ---------- | --- | --- |
|                 |          |          |                    | Connector, |     |     |
Security API Detection Third party XDR: Integration of Content Type:
|     | & Response |     | Third Party Native |     |     |     |
| --- | ---------- | --- | ------------------ | --- | --- | --- |
Alert ,
Alerts
msg_class:
|     |     |     | and Microsoft  | microsoft_grap |     |     |
| --- | --- | --- | -------------- | -------------- | --- | --- |
|     |     |     | Defender for   | h_defender_xdr |     |     |
|     |     |     | Endpoint(Graph | _alert         |     |     |
Security API):
and Content
Integration of Third
Type: Alerts,
Party Native Alerts
msg_class: micr
and Microsoft
osoft_defender
|     |     |     | Defender for Cloud | _for_endpoint_ |     |     |
| --- | --- | --- | ------------------ | -------------- | --- | --- |
Apps (Graph
alerts
Security API):
and Content
Integration of Third
Type: Alerts,
Party Native Alerts
msg_class:
and Microsoft
microsoft_defe
Defender for Cloud
nder_for_cloud
(Graph Security
_apps_alerts
API): Integration of
and Content
Type: Microsoft

|                |           | Integratio |                    |              | Detections    |                 |
| -------------- | --------- | ---------- | ------------------ | ------------ | ------------- | --------------- |
|                | Connector |            | Third Party Alert  | Third Party  |               |                 |
| Connector Name |           | n          |                    |              | (Select       | Asset Discovery |
|                | Category  |            | Integration Name   | Based On     |               |                 |
|                |           | Function   |                    |              | Applications) |                 |
|                |           |            | Third Party Native | Defender for |               |                 |
|                |           |            | Alerts             | Cloud,       |               |                 |
msg_class:
microsoft_defe
nder_for_cloud
_alerts
| Microsoft  | Database | Collect |     |     |     | Yes, Content |
| ---------- | -------- | ------- | --- | --- | --- | ------------ |
| SQL Server |          |         |     |     |     | Type: Client |
agent status Logs
(Klassify)
Mimecast API 1.0 Email Collect, Mimecast: Integrati Connector, Mimecast

|     |     | Third party | on of Third Party | Content        |     |     |
| --- | --- | ----------- | ----------------- | -------------- | --- | --- |
|     |     |             | Native Alerts     | Type: MTA Log, |     |     |
msg-
class: several
| Mime cast API 2.0 | Email | Collect, |                     |            | Mimecast |     |
| ----------------- | ----- | -------- | ------------------- | ---------- | -------- | --- |
|                   |       |          | Mimecast: Integrati | Connector, |          |     |
Third party
|     |     |     | on of Third Party | Content        |     |     |
| --- | --- | --- | ----------------- | -------------- | --- | --- |
|     |     |     | Native Alerts     | Type: MTA Log, |     |     |
msg-
class: several
| MySQL      | Database      | Collect |     |     |     |     |
| ---------- | ------------- | ------- | --- | --- | --- | --- |
|            | SASE          |         |     |     |     |     |
| NetFoundry |               | Collect |     |     |     |     |
| Nessus     | Vulnerability | Collect |     |     |     | Yes |
Scanner
Netskope Web Security Collect, Netskope: Connector, Netskope WSG
|     |     | Respond    | Integration of Third | Content        |     |     |
| --- | --- | ---------- | -------------------- | -------------- | --- | --- |
|     |     | (templates | Party Native Alerts  | Type: Alert,   |     |     |
|     |     | in         |                      | msg_class:     |     |     |
|     |     | Universal  |                      | netskopewsg_al |     |     |
Webhook
ert
Responder
),
Third party
| Nodeware | Vulnerability | Collect |     |     |     |     |
| -------- | ------------- | ------- | --- | --- | --- | --- |
Scanner
| NodeZero | Penetration Testing | Collect |     |     |     |              |
| -------- | ------------------- | ------- | --- | --- | --- | ------------ |
|          |                     |         |     |     |     | Yes, Content |
Type: Hosts

|                |                     | Integratio |                   |             | Detections    |                 |
| -------------- | ------------------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector           |            | Third Party Alert | Third Party |               |                 |
| Connector Name |                     | n          |                   |             | (Select       | Asset Discovery |
|                | Category            |            | Integration Name  | Based On    |               |                 |
|                |                     | Function   |                   |             | Applications) |                 |
| NordStellar    | Threat Intel Vendor | Collect    |                   |             |               |                 |

| Office 365 | SaaS | Collect,    | Office 365:          | Connector,  | Office365 |     |
| ---------- | ---- | ----------- | -------------------- | ----------- | --------- | --- |
|            |      | Third party | Integration of Third | Content     |           |     |
|            |      |             | Party Native Alerts  | Type: Audit |           |     |
General,
msg_class:
office365_audi
t_general
| Office 365 Reporting | SaaS | Collect |     |     |     |     |
| -------------------- | ---- | ------- | --- | --- | --- | --- |
Web Service
| Okta     | IdP | Collect |     |     | Okta     |     |
| -------- | --- | ------- | --- | --- | -------- | --- |
| OneLogin | IdP | Collect |     |     | OneLogin |     |
Oracle Cloud PaaS Collect, Oracle Cloud Connector, OCI Logs
Infrastructure (OCI) Third party Infrastructure (OCI) Content Type:
| Streaming |     |     | CloudGuard:          | N/A, msg_class: |     |     |
| --------- | --- | --- | -------------------- | --------------- | --- | --- |
|           |     |     | Integration of Third | oracle_cloud_g  |     |     |
|           |     |     | Party Native Alerts  | uard            |     |     |
Endpoint Security
Palo Alto Networks Collect, Palo Alto Networks Connector, Palo Alto Yes, Content
CORTEX XDR Respond, CORTEX XDR: Content Type: Networks Type: Endpoints
|     |     | Third party | Integration of Third | Alerts,    | CORTEX |     |
| --- | --- | ----------- | -------------------- | ---------- | ------ | --- |
|     |     |             | Party Native Alerts  | msg_class: |        |     |
palo_alto_netw
orks_cortex_xd
r_alerts
| Palo Alto Networks | Firewall | Respond |     |     | Palo Alto |     |
| ------------------ | -------- | ------- | --- | --- | --------- | --- |
Firewall
Networks
Firewall
| Palo Alto Networks | Firewall | Respond |     |     | Palo Alto   |     |
| ------------------ | -------- | ------- | --- | --- | ----------- | --- |
| Panorama           |          |         |     |     | Panorama(FW |     |
class)
| People Risk | Email | Collect |     |     |     |     |
| ----------- | ----- | ------- | --- | --- | --- | --- |
Explorer
| Perception Point X- |       | Collect |     |     |     |     |
| ------------------- | ----- | ------- | --- | --- | --- | --- |
|                     | Email |         |     |     |     |     |
Ray
Prisma Cloud Cloud Security Collect, Prisma Cloud: Connector, Palo Alto
|     |     | Third party | Integration of Third | Content Type: | Networks |     |
| --- | --- | ----------- | -------------------- | ------------- | -------- | --- |

|                |           | Integratio |                     |                   | Detections    |                 |
| -------------- | --------- | ---------- | ------------------- | ----------------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert   | Third Party       |               |                 |
| Connector Name |           | n          |                     |                   | (Select       | Asset Discovery |
|                | Category  |            | Integration Name    | Based On          |               |                 |
|                |           | Function   |                     |                   | Applications) |                 |
|                |           |            | Party Native Alerts | Alert, msg_class: | Prisma Cloud  |                 |
|                |           |            |                     | palo_alto_netw    | (Compute      |                 |
|                |           |            |                     | orks_prisma_cl    | Edition)      |                 |
oud
| Proofpoint on | Email | Collect, |     |     | Proofpoint |     |
| ------------- | ----- | -------- | --- | --- | ---------- | --- |
| Demand        |       | Respond  |     |     |            |     |
(templates
in
Universal
Webhook
Responder
)
Proofpoint TAP Email Collect, Proofpoint Targeted Connector, Proofpoint
|     |     | Third party | Attack Protection  | Content        | Targeted Attack |     |
| --- | --- | ----------- | ------------------ | -------------- | --------------- | --- |
|     |     |             | (TAP): Integration | Type: Events,  | Protection      |     |
|     |     |             | of Third Party     | msg_class:     |                 |     |
|     |     |             | Native Alerts      | proofpoint_tap |                 |     |
_event
| Qualys     | Vulnerability | Collect |     |     |        | Yes, Content |
| ---------- | ------------- | ------- | --- | --- | ------ | ------------ |
|            | Scanner       |         |     |     |        | Type: Hosts  |
| Qualys FIM | Vulnerability | Collect |     |     |        | Yes, Content |
|            | Scanner       |         |     |     |        | Type: Asset  |
| Rapid7     | Vulnerability | Collect |     |     | Rapid7 | Yes          |
Scanner
Recorded Future Cloud Security Collect, Recorded Future: Connector, Recorded
|     |     | Third party | Integration of Third | Content Type: |     |     |
| --- | --- | ----------- | -------------------- | ------------- | --- | --- |
Future
|     |     |     | Party Native Alerts | Alert and |     |     |
| --- | --- | --- | ------------------- | --------- | --- | --- |
Playbook Alert,
msg_class:
recorded_futur
e_alert and
recorded_futur
e_playbook_ale
rt
| Remote SSH Host | Remote Host | Respond |     |     |            |     |
| --------------- | ----------- | ------- | --- | --- | ---------- | --- |
| Salesforce      | SaaS        | Collect |     |     | Salesforce |     |
SentinelOne Endpoint Security Collect, SentinelOne Cloud: Connector, SentinelOne Yes, Content
|     |     | Respond, | Integration of Third | Content |     | Type: Host |
| --- | --- | -------- | -------------------- | ------- | --- | ---------- |

|                |           | Integratio  |                     |               | Detections    |                 |
| -------------- | --------- | ----------- | ------------------- | ------------- | ------------- | --------------- |
|                | Connector |             | Third Party Alert   | Third Party   |               |                 |
| Connector Name |           | n           |                     |               | (Select       | Asset Discovery |
|                | Category  |             | Integration Name    | Based On      |               |                 |
|                |           | Function    |                     |               | Applications) |                 |
|                |           | Third party | Party Native Alerts | Type: Threat, |               |                 |
|                |           |             | and SentinelOne     | msg_class:    |               |                 |
sentinelone_th
Singularity Identity:
|     |     |     | Integration of Third | reat_detection |     |     |
| --- | --- | --- | -------------------- | -------------- | --- | --- |
|     |     |     | Party Native Alerts  | and Content    |     |     |
Type: Unified
Alerts,
msg_class:
sentinelone_un
ified_alerts
SOCRadar Endpoint Security Collect, Socradar: Connector: Cont
|     |     | Third party | Integration of Third | ent              |     |     |
| --- | --- | ----------- | -------------------- | ---------------- | --- | --- |
|     |     |             | Party Native Alerts  | Type: Incidents, |     |     |
msg_class:
socradar_incid
ents
SonicWall Capture Endpoint Security Collect,       Yes, Content
| Client |     | Respond |     |     |     | Type: Host |
| ------ | --- | ------- | --- | --- | --- | ---------- |
SonicWall Endpoint Endpoint Security Collect, SonicWall Endpoint Connector,
|          |     |             |                      |               |     |     |
| -------- | --- | ----------- | -------------------- | ------------- | --- | --- |
| Security |     | Third party | Security:            | Content Type: |     |     |
|          |     |             | Integration of Third | Alerts,       |     |     |
|          |     |             | Party Native Alerts  | msg_class:    |     |     |
sonicwall_ther
on_alerts
| SonicWall Firewall | Firewall | Respond |     |     | SonicWall(FW |     |
| ------------------ | -------- | ------- | --- | --- | ------------ | --- |
class)
Sophos Central Endpoint Security Collect, Sophos Central: Connector, Sophos Yes, Content
Respond, Integration of Third Content Endpoint Types: Alerts and
|     |     | Third party | Party Native Alerts | Type: Alerts and |     | Events |
| --- | --- | ----------- | ------------------- | ---------------- | --- | ------ |
Events,
msg_class:
 sophos_alerts
and
sophos_events
| Sophos XG | Firewall | Respond |     |     | Sophos |     |
| --------- | -------- | ------- | --- | --- | ------ | --- |
XG Firewall
| Stellar Cyber | Extended | Collect |     |     |     |     |
| ------------- | -------- | ------- | --- | --- | --- | --- |
Detection
& Response

|                  |           | Integratio |                   |             | Detections    |                 |
| ---------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                  | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name   |           | n          |                   |             | (Select       | Asset Discovery |
|                  | Category  |            | Integration Name  | Based On    |               |                 |
|                  |           | Function   |                   |             | Applications) |                 |
| Stormshield      | Firewall  | Respond    |                   |             | Stormshield   |                 |
| Network Security |           |            |                   |             | Net Security  |                 |
| (SNS) Firewall   |           |            |                   |             | Firewall (FW  |                 |
class)
| Sucuri Security | Web Security   | Collect |     |     |     |     |
| --------------- | -------------- | ------- | --- | --- | --- | --- |
| Tenable Cloud   | Cloud Security | Collect |     |     |     |     |
Security
| Tenable.io | Vulnerability | Collect |     |     |     | Yes, Content        |
| ---------- | ------------- | ------- | --- | --- | --- | ------------------- |
|            | Scanner       |         |     |     |     | Type: Vulnerabiliti |
es
| Tenable.sc | Vulnerability | Collect |     |     |     | Yes, Content        |
| ---------- | ------------- | ------- | --- | --- | --- | ------------------- |
|            | Scanner       |         |     |     |     | Type: Vulnerabiliti |
es
Thinkst Canary Honeypot Collect     Thinkst Canary Yes, Content
Type: Devices
Endpoint Security
| ThreatDown        |     | Collect |     |     |     | Yes, Content    |
| ----------------- | --- | ------- | --- | --- | --- | --------------- |
| OneView (formerly |     |         |     |     |     | Type: Endpoints |
Malwarebytes
OneView)
Endpoint Security
| Threatlocker |     | Collect |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- |
Trellix Endpoint Security Collect, Trellix (FireEye) Connector, FireEye HX Yes, Content
| (FireEye) Endpoint |     | Third party | Endpoint             | Content        |     | Type: Hosts |
| ------------------ | --- | ----------- | -------------------- | -------------- | --- | ----------- |
| Security HX        |     |             | Security:Integration | Type: Alerts,  |     |             |
|                    |     |             | of Third Party       | msg_class:     |     |             |
|                    |     |             | Native Alerts        | fireeye_alerts |     |             |
Trellix MVISION Endpoint Security Collect, Trellix MVISION: Connector, Trellix Yes, Content
Third Party Integration of Third Content Type: MVISION Type: Devices
|     |     |     | Party Native Alerts | Alerts, |     |     |
| --- | --- | --- | ------------------- | ------- | --- | --- |
msg_class:
trellix_mvisio
n_edr_alerts
Trend Micro Apex Endpoint Security Collect     Trend Micro - Yes, Content
| Central |     |     |     |     | Apex Central | Types: Agents |
| ------- | --- | --- | --- | --- | ------------ | ------------- |
and Servers
Trend Micro Cloud Cloud Security Collect, Trend Micro Cloud Connector,
| App Security |     | Third party | App Security: | Content |     |     |
| ------------ | --- | ----------- | ------------- | ------- | --- | --- |
Types: Exchange

|                |           | Integratio |                      |                 | Detections    |                 |
| -------------- | --------- | ---------- | -------------------- | --------------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert    | Third Party     |               |                 |
| Connector Name |           | n          |                      |                 | (Select       | Asset Discovery |
|                | Category  |            | Integration Name     | Based On        |               |                 |
|                |           | Function   |                      |                 | Applications) |                 |
|                |           |            | Integration of Third | , OneDrive,     |               |                 |
|                |           |            | Party Native Alerts  | Sharepoint Log, |               |                 |
and Teams,
msg_class:
 trendmicro_ca
s_logs_exchang
e,
trendmicro_cas
_logs_onedrive
,
trendmicro_cas
_logs_sharepoi
nt, and
trendmicro_cas
_logs_teams
Trend Micro Cloud Endpoint Security Collect       Yes, Content
| One Workload |     |     |     |     |     | Type: Computers |
| ------------ | --- | --- | --- | --- | --- | --------------- |
Security
| Trend Micro Email | Email | Collect |     |     |     |     |
| ----------------- | ----- | ------- | --- | --- | --- | --- |
|                   |       |         |     |     |     |     |
Security
Trend Micro Vision Endpoint Security Collect, Trend Micro Vision Connector, Trend Micro
| One |     | Respond    | One: Integration of | Content        | Vision One |     |
| --- | --- | ---------- | ------------------- | -------------- | ---------- | --- |
|     |     | (templates | Third Party Native  | Type: Alerts,  |            |     |
|     |     | in         | Alerts              | msg_class:     |            |     |
|     |     | Universal  |                     | trendmicro_vis |            |     |
|     |     | Webhook    |                     | ionone_alerts  |            |     |
Responder
),
Third party
| Universal Webhook | Webhook | Respond |     |     |     |     |
| ----------------- | ------- | ------- | --- | --- | --- | --- |
(Custom)
| VadeSecure   |       | Collect     |                      |                  |              |     |
| ------------ | ----- | ----------- | -------------------- | ---------------- | ------------ | --- |
|              | Email |             |                      |                  |              |     |
| Varonis      |       | Third party | Varonis              | Parser (CEF      | Varonis-     |     |
| DatAdvantage |       |             | DatAdvantage:        | format), Content | Datadvantage |     |
|              |       |             | Integration of Third | Type: N/A,       |              |     |
|              |       |             | Party Native Alerts  | msg_class:       |              |     |
 varonis_datad
vantage_file_s
ystem_operatio
n or

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
varonis_datadv
antage_directo
ry_services_op
eration
| Verkada | Internet of Things | Collect |     |     |     |     |
| ------- | ------------------ | ------- | --- | --- | --- | --- |
Security
| Versa Networks | SASE | Collect |     |     | Versa |     |
| -------------- | ---- | ------- | --- | --- | ----- | --- |
Networks
Concerto
SASE
|                | Firewall |         |     |     | Versa |     |
| -------------- | -------- | ------- | --- | --- | ----- | --- |
| Versa Networks |          | Respond |     |     |       |     |
Networks
Firewall
Firewall
| Vicarius | Vulnerability | Collect |     |     |     | Yes, Content |
| -------- | ------------- | ------- | --- | --- | --- | ------------ |
|          | Scanner       |         |     |     |     | Type: Assets |
VMware Carbon Endpoint Security Collect, VMware Carbon Connector, Carbon Black Yes, Content
| Black Cloud |     | Respond,    | Black Cloud:         | Content         |     | Type: Alert |
| ----------- | --- | ----------- | -------------------- | --------------- | --- | ----------- |
|             |     | Third party | Integration of Third | Type: Alert,    |     |             |
|             |     |             | Party Native Alerts  | msg_class: carb |     |             |
onblack_alert
VMware Workspace
|     | Endpoint Security | Collect |     |     | VMware    |     |
| --- | ----------------- | ------- | --- | --- | --------- | --- |
| ONE |                   |         |     |     | Workspace |     |
One
| WatchGuard Firebox | Webhook | Respond |     |     |     |     |
| ------------------ | ------- | ------- | --- | --- | --- | --- |
(templates
in
Universal
Webhook
Responder
)
| Webroot | Endpoint Security | Collect |     |     | Webroot | Yes, Content |
| ------- | ----------------- | ------- | --- | --- | ------- | ------------ |
Type: Endpoints
Windows Defender   Third party Windows Defender Windows agent, Windows Agent
| Antivirus |     |     | Antivirus:           | Content    |     |     |
| --------- | --- | --- | -------------------- | ---------- | --- | --- |
|           |     |     | Integration of Third | Type: N/A, |     |     |
|           |     |     | Party Native Alerts  | msg_class: |     |     |
Microsoft-
Windows-

|                |           | Integratio |                   |             | Detections    |                 |
| -------------- | --------- | ---------- | ----------------- | ----------- | ------------- | --------------- |
|                | Connector |            | Third Party Alert | Third Party |               |                 |
| Connector Name |           | n          |                   |             | (Select       | Asset Discovery |
|                | Category  |            | Integration Name  | Based On    |               |                 |
|                |           | Function   |                   |             | Applications) |                 |
Windows
Defender
WithSecure Endpoint Security, Collect, WithSecure Connector: Cont Yes, Content

| Elements | Webhook | Respond    | Elements:            | ent               |     | Type: Devices |
| -------- | ------- | ---------- | -------------------- | ----------------- | --- | ------------- |
|          |         | (templates | Integration of Third | Type: Detections, |     |               |
|          |         | in         | Party Native Alerts  | msg_class:        |     |               |
|          |         | Universal  |                      | withsecure_elem   |     |               |
|          |         | Webhook    |                      | ents_detection    |     |               |
Responder
),
Third party
Wiz Cloud Security Collect, Wiz: Integration of Connector: Cont
|     |     | Third party | Third Party Native | ent Type: Issues, |     |     |
| --- | --- | ----------- | ------------------ | ----------------- | --- | --- |
|     |     |             | Alerts             | msg_class:        |     |     |
wiz_issues
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
|     |     |     |     |     | Support   |  Contact Us |   |            |
| --- | --- | --- | --- | --- | ----------------------- | ---------------- |