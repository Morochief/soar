✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Integration of Third Party Native Alerts
Stellar Cyber's alerts are created from data pathways that leverage raw data collected from all forms of data sources,
including third party services and Stellar Cyber’s sensors. You can choose to allow Stellar Cyber's Machine Learning
(ML) and Statistical Analysis (SA) to generate alerts based on raw data ingested from third party services. For certain
services, you can additionally choose to ingest and integrate alerts that are natively created in those services.
This topic summarizes which third party services and products Stellar Cyber supports for native alert integration and
how those alerts are mapped in Stellar Cyber.
Third Party Native Alert Mapping
Stellar Cyber handles each service and product in a custom manner, according to the nature of the incoming data,
including third party native alerts and other security events. To view alerts and events from multiple sources in our
unified, common platform, Stellar Cyber normalizes and enriches the third party native alerts and security events
during the data ingestion process. With ingested, normalized, and enriched third party native alerts and security
events, Stellar Cyber further applies ML/SA engines, a direct mapping, or a combination of the two, to create Stellar
Cyber alerts mapped to the XDR Kill Chain with additional deduplication to reduce noise and alert fatigue.
Review the following to better understand the native third party alert mapping Stellar Cyber is doing to help you get to
the decision points more efficiently:
Deduplication: In mapping third-party native alerts and security events to the XDR Kill Chain, Stellar Cyber
uses a variety of methods to identify and eliminate potential duplicates for each applicable alert or event
type. In particular, Stellar Cyber identifies a combination of fields and values to be key characteristics and
uses those to identify duplicates. An example method is to compare the values in that combination for each
new third party native alert; if the same value set occurs within a time threshold, that record is considered a
duplicate and only the original record is mapped. This process is a critical mechanism to eliminate noise and
reduce alert fatigue.
Normalization: A key benefit of Stellar Cyber is standardization of all incoming data sources to a common
data model (Interflow record), that includes some fields based on the Elastic Common Schema (ECS).
Values from the incoming raw data are mapped into standardized fields in Stellar Cyber. In some cases, the
original data field is still saved with the Interflow record. This normalization allows Stellar Cyber Analytics
and Machine Learning to perform complex analysis and identify related events from disparate ingestion
sources. Here are examples of normalization:
crowdstrike.event.LocalIP is mapped to Stellar Cyber's host.ip field
threatInfo.classification is mapped to Stellar Cyber threat field
Enrichment: Stellar Cyber's data framework requires certain fields to help identify the data source, the
category of data, the type of event, to support scoring calculations and certain other activities. In some
cases, the ingested data can be directly mapped into these fields. In other cases, Stellar Cyber generates
that data. Examples of data enrichment are:
(No incoming source field) msg_origin.source is created and populated with the vendor name,
such as crowdstrike
(No incoming source field) msg_origin.category is created and populated with the applicable
category for the data type, such as endpoint
Incoming data source field crowdstrike.metadata.eventType field exists and its value (such as
crowdstrike_detection_summary) is mapped to Stellar Cyber field msg_class
Incoming data source field event.technique.name field exists and its value is either mapped
directly or algorithmically standardized to populate to Stellar Cyber field xdr.event_name.

Populating the xdr_event structure is a key part of enrichment, with Stellar Cyber ensuring that a
Tactic, Technique, and Procedure name, and important scores, are present in every Alert record.
Supported Native Third Party Alerts
The table below lists all the services and products for which Stellar Cyber has developed direct integration of third
party native alerts, which includes mapping to the Stellar Cyber XDR Kill Chain and adding those alerts to the Alert
index. Data not directly mapped is still run through the Stellar Cyber ML/SA pipeline, where applicable. The third party
native alerts that are not mapped are ingested and available for creating ATH rules for automatic actions and entry of
the result into the Alert index.
Use the table below to identify the data applicable for direct alert mapping, the method of ingestion, and the nature of
the mapping.

In cases where a value is indicated as Derived, Stellar Cyber assigns a value based on other
attributes in the ingested data.
Where possible, links to the third party data type format are provided for reference.
For the Key Fields for Third Party Alerts, see Key Fields for Third Party Native Alert Types.
Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Abnormal Abnormal Security Abnorm Stellar Cyber maps msg_origin.source: abnormal_security_email_security
msg_class: abnormal_security_email_security_threat
Security Email Security al Abnormal Security Event (Alert) Name: Abnormal Security Threat: with the assigned Technique, for example Abnormal
Email Alerts Securit Email Security Security Threat: Unknown Sender:
Severity: 45
Security y Email alerts. The alerts
Fidelity: Is Severity by default
Securit are read from the
Kill Chain & MITRE | ATT&CK values are derived
y Syslog index,
Connec enriched with
tor Stellar Cyber
This fields, and mapped
connect (with deduplication)
or to the Alerts index.
ingests Deduplication is by
logs tenantid,
from email.message_i
Abnorm d, and
al event.threat.na
Securit me.
y Email
Securit
y to get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Threats
content
type.
Acronis Acronis Cyber Acronis Stellar Cyber maps msg_origin.source: acronis_cyber_protect
msg_class: acronis_cyber_protect_alert
Cyber Protect Cloud Cyber Acronis Cyber Event (Alert) Name:
Protect Alerts Protect Protect Cloud Acronis Cyber Protect: with the assigned Technique, for example Acronis Cyber Protect Cloud:
Phishing
Cloud Cloud alerts. The alerts
Acronis Cyber Protect: with the assigned Technique, for example Acronis Cyber Protect Cloud:
Connec are read from the XDR Anomaly
tor Syslog index, Acronis Cyber Protect: with the assigned Technique, for example Acronis Cyber Protect Cloud:
Hide Artifacts
enriched with

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
This Stellar Cyber Acronis Cyber Protect: with the assigned Technique, for example Acronis Cyber Protect Cloud:
Drive-by Compromise
connect fields, and mapped Severity: Derived from event.severity_str
or (with deduplication) Fidelity: Is Severity by default
ingests to the Alerts index. Kill Chain & MITRE | ATT&CK values are derived
logs The following four
from alert types are
Acronis supported: Email
Cyber security, EDR,
Protect Antimalware
Cloud protection, and
to get URL filtering.
the raw
Tactic and
alerts
Technique are
that are
based on alert
stored
type.
in the
Deduplication is by
Syslog
tenantid,
index.
event.threat.na
Select
me, host.name,
the
user.name, url,
Alerts
process.pid,
content
file.hash.sha1,
type.
email.from.addr
ess, and
acronis_cyber_p
rotect.details.
edrAlertId.
Armis Armis Alerts Armis Stellar Cyber maps msg_origin.source: armis
msg_class: armis_alerts
Connec Armis alerts. The Event (Alert) Name: Armis: with their multiple TTPs, for example Armis: [MITRE ATT&CK | ICS] T0886 |
 Armis alert tor alerts are read Initial Access, Lateral Movement | Remote Services...
Severity: Derived from event.severity_str
integration This from the Syslog
Fidelity: Is Severity by default
supports connect index, enriched Kill Chain & MITRE | ATT&CK values are derived
Mobile and or with Stellar Cyber
Industrial ingests fields, and mapped
Control logs (with deduplication)
Systems from to the Alerts index.
(ICS) tactics, Armis Deduplication is by
in addition to to get tenantid,
Enterprise. the raw armis.alertId,
alerts and host.ip.
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
Avanan Avanan Alerts Configu Avanan sends msg_origin.source: avanan
msg_class: avanan
re email data to the Event (Alert) Name:
The alert types are:
ingestio Stellar Cyber Avanan (Delivered): with the assigned Technique, for example Avanan (Delivered): Phishing
spam n of Syslog index, Avanan (Quarantined): with the assigned Technique, for example Avanan (Quarantined): Spam
phishing Severity: Derived from Avanan severity
HTTP J which maps
suspicious_ Fidelity: Is Severity by default
phishing SON Avanan alerts to
Kill Chain & MITRE | ATT&CK values are derived
malware format the Alerts index.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
shadow_it logs to Deduplication is by
dlp
a tenantid,
alert
Stellar email.sender.ad
anomaly
Cyber dress, and
malicious_u
rl sensor. email.from.addr
ess.
If neither
email.sender.ad
dress or
email.from.addr
ess exists,
file.name is used
for deduplication.
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the queries:
msg_class
: avanan
AND
event.act
ion:
Delivered
msg_class
: avanan
AND
event.act
ion:
Quarantin
ed
AWS Guard AWS GuardDuty AWS Stellar Cyber maps msg_origin.source: aws_guardduty
msg_class: aws_guardduty_finding
Duty Alerts GuardD AWS GuardDuty Event (Alert) Name: AWS GuardDuty: with the assigned Technique, for example AWS GuardDuty: Valid
uty Con alerts. The alerts Accounts
Refer to Amazon Severity: Derived from event.severity_str
nector are read from the
GuardDuty. Fidelity: Is Severity by default
This Syslog index,
Kill Chain & MITRE | ATT&CK values are derived
connect enriched with
or Stellar Cyber
ingests fields, and mapped
logs (with deduplication)
from to the Alerts index.
AWS G Deduplication is by
uardDut tenantid and
y to get aws_guardduty_i
the raw d.
alerts
that are
stored
in the
Syslog
index.
Bitdefender URL--based Configu Of the different msg_origin.source: bitdefender
re record types you msg_class: Several. See the Bitdefender connector information card for a full list.
Antiphishing
ingestio can configure to Event (Alert) Name: Bitdefender: with the assigned Technique, for example Bitdefender: Data Encrypted
for Impact
Data Protection n of push to Stellar Severity: Derived from event.type
User Control / Bitdefe Cyber's httpjson Fidelity: Is Severity by default
Content Control nder's parser, the 11 at MITRE | ATT&CK Technique and Tactic values are assigned as follows:
Push left are normalized
Advanced Threat Control (ATC) XDR Malware; XDR Misc Malware
IP-based
event and enriched as
Antiexploit Event
Firewall for they are added to

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Ransomware JSON the Syslog index. Antimalware
activity RPC The records are Hyper Detect event
detection messag evaluated against Sandbox Analyzer Detection
es toexisting records in
Threat-based
User Control/Content Control Execution; Exploitation for Client Execution
send the Alert index--
Advanced Threat
data to those that do not
Data Protection Impact; Data Manipulation
Control (ATC)
a already exist are
Storage Antimalware Event
Antiexploit Stellar directly mapped to
Event Cyber the Alert index and Ransomware activity detection Impact; Data Encrypted for Impact
sensor XDR Kill chain.
Antimalware Antiphishing Initial Access; Phishing
configur The other records
Hyper Detect ed to are run through the Firewall XDR NBA; XDR Firewall Anomaly
event
ingest ML/SA pipeline,
Sandbox Analyzer httpjson which may
Detection (port generate alerts
5200) based on those
Storage
over algorithms. The
Antimalware
TLS. labels assigned to
the alert groups at
left refer simply to
the nature of the
key data points for
those alerts.
Specifically, these
data are supplied
with the relevant
alert
description (Bitdefe
nder field in
parenthesis):
URL-based
alerts:
event.type
(module
acronym),
host.name
(computer_
fqdn),
host.ip
(computer_i
p), url
IP-based
alerts:
event.type
(module
acronym),
host.name
(computer_
fqdn),
host.ip
(computer_i
p), srcip
(attack
source or
source-ip)
Threat-
based
alerts:
event.type
(module
acronym),
host.name
(computer_
fqdn),
host.ip
(computer_i
p),
threatName
, where
threatName
varies
depending
on the
record type
(malware_n
ame,
threatType,
detection_t
hreatName,
attack_type
s,
aph_type,

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
| Party |     | Notable Interflow Fields |     |     |
| ----- | --- | ------------------------ | --- | --- |
Type Metho Stellar Cyber
Service
d Alerts
exploit_typ
e, or
target_type
)
See the
Bitdefender
connector
information card for
more details on
normalization of
these and other
Bitdefender
records.
Deduplication is by
the following fields:
IP—
tenantid,
event.typ
e,
host.name,
host.ip,
and srcip.
Threat—
tenantid,
event.typ
e,
host.name,
host.ip,
and
event.thr
eat.name.
URL—
tenantid,
event.typ
e,
host.name,
host.ip,
and url.
F o r
| Blackberry CylancePROTECT: | Forwar | C y lancePR CylancePROTECT |                                    |     |
| -------------------------- | ------ | -------------------------- | ---------------------------------- | --- |
| CylancePR                  |        | O T E C T ,                |                                    |     |
| Exploit Attempts          | d log  | th re e  t yp es           | msg_origin.source: cylance_protect |     |
of Cylance
| OTECT and | files to |     | msg_class:  cylance_protect_alert |     |
| --------- | -------- | --- | --------------------------------- | --- |
events are E v e n t  (A l e rt )  N a m e :  C y l a ncePROTECT: with the assigned Technique, for example CylancePROTECT:
| CylanceOP Script Control |      | mapped to |                    |                      |
| ------------------------- | ---- | --------- | ------------------ | -------------------- |
|                           | port | the XDR   | OS   C r e d e n t | i a l  D u m p i n g |
TICS
| Threats | 5177 | Kill Chain | Severity: Not present in incoming data; Derived |     |
| -------- | ---- | ---------- | ----------------------------------------------- | --- |
and Stellar
(specifi Cyber's Fidelity: cylance_score unless blank, then is populated with the same value as Severity
CylanceOPTICS:
|             |         | Alert index:   | Kill Chain & MITRE | ATT&CK values are derived from event_type and |     |
| ----------- | ------- | -------------- | ------------------------------------------------------------------ | --- |
|             | c for   | Exploit        |                                                                    |     |
|             |         | A t t e m pts, | violation_type/threat_classification                               |     |
| Detections | handlin |                |                                                                    |     |
S c r ip t CylanceOPTICS
Control,
|     | g   | and |     |     |
| --- | --- | --- | --- | --- |
msg_origin.source: cylance_optics
|     | Cylanc | Threats.  |                                  |     |
| --- | ------ | --------- | -------------------------------- | --- |
|     |        | The other | msg_class:  cylance_optics_event |     |
data (Audit
e logs) Event (Alert) Name: CylanceOPTICS: with the assigned Technique, for example CylanceOPTICS: XDR
|     |     | Log, | Anomaly |     |
| --- | --- | ---- | ------- | --- |
Device,
|     | The     | Device     | Severity: severity               |     |
| --- | ------- | ---------- | -------------------------------- | --- |
|     |         | Control,   | Fidelity: Is Severity by default |     |
|     | Blackbe | and Threat |                                  |     |
C la s s i ficati
rry K i ll  C h a in  &   M ITRE | ATT&CK values are assigned a value during processing of CylanceOPTICS in the
|     |     | on )  a r e | M L / S A  p ip el | i ne |
| --- | --- | ----------- | ------------------ | ---- |
ingested
|     | Cylanc | and |     |     |
| --- | ------ | --- | --- | --- |
mapped to
e
the Syslog
|     | Connec | index (not |     |     |
| --- | ------ | ---------- | --- | --- |
Alerts
|     | tor is | index), and |     |     |
| --- | ------ | ----------- | --- | --- |
are not run
|     | applica | through the |     |     |
| --- | ------- | ----------- | --- | --- |
ML/SA
|     | ble only | pipeline. |     |     |
| --- | -------- | --------- | --- | --- |
|     | for      | For       |     |     |
CylanceOP
TICS,
respons
Detection
|     | e   | events are |     |     |
| --- | --- | ---------- | --- | --- |
evaluated
|     | actions. | with Stellar |     |     |
| --- | -------- | ------------ | --- | --- |
Cyber time
series
analysis
models to
determine
abnormality
of the event
before
mapping.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Deduplication is by
org_id, tenantid,
event.type,
host.name,
host.ip,
file_name,
file_path, and
process_name.
Broadcom Broadcom Broadc Stellar Cyber maps msg_origin.source: broadcom_ses
msg_class: broadcom_ses_incidents
SES Incidents om Broadcom SES Event (Alert) Name: Broadcom SES Incident: with the assigned Technique, for example Broadcom
SES Incident: Data Encrypted for Impact
SES incidents. The
Severity: Derived from event.severity:
Connec incidents are read
Unknown: 1
tor from the Syslog
Informational: 15
This index, enriched Warning: 30
connect with Stellar Cyber Minor: 45
or fields, and mapped Major: 60
ingests (with deduplication) Critical: 75
logs to the Alerts index. Fatal: 90
Fidelity: Is Severity by default
from Deduplication is by
Kill Chain & MITRE | ATT&CK values are derived
Broadc tenantid and
om broadcom.incide
Symant nt_uid.
ec
Endpoi
nt
Securit
y
(SES) t
o get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Incident
s
content
type.
Cato Cato Networks Cato Stellar Cyber maps msg_origin.source: cato_networks
msg_class: cato_security
Networks events Networ Cato Networks Event (Alert) Name: Cato Networks: with the event subtype, for example Cato Networks: NG Anti
Malware
ks events. The events
Severity: Derived from event.severity:
Connec are read from the
Fidelity: Is Severity by default
tor Syslog index,
Kill Chain & MITRE | ATT&CK values are derived
This enriched with
connect Stellar Cyber
or fields, and mapped
ingests (with deduplication)
logs to the Alerts index.
from Deduplication is by
Cato event_id.
Networ
ks to
get the

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Securit
y
content
type.
Check PointCheck Point Check Stellar Cyber maps msg_origin.source: checkpoint_harmony
msg_class: checkpoint_harmony_security_event
Harmony Harmony Email Point Check Point Event (Alert) Name: Check Point Harmony Email: with the checkpoint_harmony.type, for example Check
Point Harmony Email: Phishing
Email events Harmon Harmony Email
Severity: Derived from event.severity:
y Email events. The events
The alert types are: 4=Very High: 80
Connec are read from the
5=Critical: 99
spam
tor Syslog index,
Fidelity: Is Severity by default
phishing.
This enriched with Kill Chain & MITRE | ATT&CK values are derived
anomaly
shadow_it connect Stellar Cyber
graymail or fields, and mapped
ingests (with deduplication)
logs to the Alerts index.
from Deduplication is by
Check tenantid and
Point checkpoint_harm
Harmon ony.eventId.
y Email
to get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Securit
y Event
content
type.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
CrowdStrik CrowdStrike CrowdS Stellar Cyber maps msg_origin.source: crowdstrike
msg_class: crowdstrike.metadata.eventType:EppDetectionSummaryEvent or
e events trike CrowdStrike crowdstrike_XdrDetectionSummaryEvent
Event (Alert) Name: CrowdStrike: with the assigned Technique, for example CrowdStrike: XDR Endpoint
Connec events. The events
Indicator of Threat
tor are read from the Severity: Derived from event.severity_str
This Syslog index, Fidelity: Is Severity by default
connect enriched with Kill Chain & MITRE | ATT&CK values are derived
or Stellar Cyber
ingests fields, and mapped
logs (with deduplication)
from to the Alerts index.
CrowdS Deduplication is by
trike to tenantid and
get the crowdstrike.eve
raw nt.CompositeId.
alerts
that are
stored
in the
Syslog
index.
Select
the
EppDet
ectionS
ummary
Event
content
type or
the
crowds
trike_
{metad
ata.ev
entTyp
e}
(exampl
e:
crowdst
rike_Xd
rDetecti
onSum
maryEv
ent)
default
content
type.
CyberArk CyberArk EPM CyberA Stellar Cyber maps msg_origin.source: cyberark_epm
msg_class: cyberark_epm_event
EPM events rk EPM CyberArk EPM Event (Alert) Name: CyberArk EPM : with the threat detection rule, for example CyberArk EPM: Credential
Theft From Windows Credential Manager
Connec events. The events
The following Severity: 45, by default
tor are read from the
threat detection Fidelity: Is Severity by default
This Syslog index,
categories are Kill Chain & MITRE | ATT&CK values are derived
connect enriched with
supported:
or Stellar Cyber
AttackAtte
mpt ingests fields, and mapped
AttackBlock logs (with deduplication)
Suspicious from to the Alerts index.
ActivityAtte
mpt CyberA

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Suspicious rk EPM Deduplication is by
ActivityBloc
k to get tenantid,
the raw cyberark_epm.ev
alerts entType,
that are cyberark_epm.po
stored licyName,
in the cyberark_epm.fi
Syslog lePath, and
index. cyberark_epm.us
Select erName.
the
Events
content
type.
CybereasonMalOp Cybere Stellar Cyber can msg_origin.source: cybereason_malops_all_types
msg_class: cybereason_malops_all_types
ason generate alerts Event (Alert) Name: Cybereason: with the assigned Technique, for example Cybereason: Phishing
Connec based on the Severity: Derived from threat and event.severity_str
tor Cybereason Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived from malopDetectionType
Select sensor and MalOp
the data, however the
MalOp MalOp records are
content most applicable for
type. direct mapping.
The value in
malopDetectionT
ype is reformatted
and used for the
alert name. Stellar
Cyber has
evaluated each
possible alert and
assigned a
corresponding
MITRE | ATT&CK
Stage, Tactic and
Technique.
Deduplication is by
tenantid,
user_list,
threat,
host_list,
file.name, and
process.name.
Cyble Cyble alerts Cyble Stellar Cyber maps msg_origin.source: cyble
msg_class: cyble_alerts
Connec Cyble alerts. The Event (Alert) Name: Cyble: with the event.threat.name, for example Cyble: leaked_credentials
The following alert
tor alerts are read Severity: Derived from event.severity_str:
types are
This from the Syslog HIGH: 60
supported:
connect index, enriched MEDIUM: 45
l d e e a n k t e ia d l _ s cre or with Stellar Cyber LOW: 30
Fidelity: Is Severity by default
stealer_log ingests fields, and mapped
s Kill Chain & MITRE | ATT&CK values are derived
logs (with deduplication)
darkweb_d
ata_breach from to the Alerts index.
es
Cyble Deduplication is by
darkweb_m
arketplaces to get cyble.id.
suspicious_
the raw
domains
vulnerability alerts

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
new_vulner that are
ability
ip_risk_sco stored
re
in the
ssl_expiry
Syslog
index.
Select
the
Alerts
content
type.
Cynet ADT Alerts Configu The collection of msg_origin.source: cynet
msg_class: cynet_alert
NextGen Antivirus re Cynet alerts listed Event (Alert) Name: Cynet: with the assigned Technique, for example Cynet: Data Encrypted for Impact
Alerts ingestio here are read from Severity: Derived from event.threat.name and event.severity_str
n of the Syslog index, Fidelity: Is Severity by default
Threat Intelligence CEF enriched and Kill Chain & MITRE | ATT&CK values are assigned based on the value in Cynet's alert type which is mapped
to event.threat.name
Alerts
format mapped (with
Memory Protection logs to deduplication) to
Alerts a the Alert index and
Stellar Stellar Cyber Kill
Network Activity
Cyber Chain. The Cynet
Alerts
sensor. alert type is
AMSI Alerts mapped to Stellar
Feature Alerts Cyber's
event.threat.na
me, which is shown
in the key fields.
Deduplication is by
tenantid,
host.ip,
event.threat.na
me, and
file.name.
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the query:
msg_class
:
cynet_ale
rt AND
_exists_:
event.thr
eat.name
AND NOT
event.thr
eat.name:
Audit
Darktrace Darktrace events Configu Darktrace sends msg_origin.source: darktrace
msg_class: darktrace
re Syslog CEF events Event (Alert) Name: Darktrace: with the event.threat.name, for example Darktrace: Anomalous
Connection/Download and Upload
ingestio to Stellar Cyber,
Severity: Derived from event.severity: CEF numeric severity (1-10)
n of which maps
Fidelity: Is Severity by default
CEF Darktrace events
Kill Chain & MITRE | ATT&CK values are derived
format to the Alerts index.
logs to Deduplication is by
a tenantid and
Stellar darktrace.exter
Cyber nalid.
sensor.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the query:
msg_class
:darktrac
e AND
_exists_:
event.thr
eat.name
Deep Events Deep The Events record msg_origin.source: deep_instinct
msg_class: deep_instinct_maliciousevent
Instinct Instinct includes a MITRE | Event (Alert) Name: DeepInstinct: with the assigned Technique, for example DeepInstinct: User
Execution
Connec ATT&CK structure
Severity: Derived from event.threat.name and event.severity_str
tor with values that
Fidelity: Is Severity by default
The support direct Kill Chain & MITRE | ATT&CK values:
connect mapping to Stellar Stage: Derived from MitreClassifications.mitre_id
or can Cyber's XDR Kill Tactic: MitreClassifications.tactic_name
be used Chain. If the Technique: MitreClassifications.technique_name
for incoming tactic or See also:
event.reason contains trigger
three technique are
action contains act
data blank, the following
types values are
but only assigned in Stellar
Events Cyber:
are tactic_name =
applica XDR Malware
ble for technique_name =
alert XDR
mappin Miscellaneous
g. Malware
Select Deduplication is by
the tenantid,
Events event.type,
content host.name,
type. host.ip,
file.path,
file.file_hash,
and
deep_instinct.a
ction.
Duo Trust Duo Trust Monitor Duo Stellar Cyber maps msg_origin.source: duosecurity
msg_class: duosecurity_trust_monitor
Monitor events Securit Duo Trust Monitor Event (Alert) Name: Duo Trust Monitor: with the event.threat.name, for example Duo Trust Monitor:
Bypass Status Enabled
y events. The events
Severity: Derived from event.severity_str:
Connec are read from the
duosecurity.priority_event:false: 45
tor Syslog index,
duosecurity.priority_event:true: 60
This enriched with Fidelity: Is Severity by default
connect Stellar Cyber Kill Chain & MITRE | ATT&CK values are derived
or fields, and mapped
ingests (with deduplication)
logs to the Alerts index.
from Deduplication is by
Duo duosecurity.sek
Securit ey.
y to get
the raw
alerts

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
that are
stored
in the
Syslog
index.
Select
the
Trust
Monitor
content
type.
ESET ESET Cloud Office Configu ECOS quarantines msg_origin.source: eset_cos
msg_class: eset_cos_googledrive, eset_cos_gmail, eset_cos_team, eset_cos_exchange,
Cloud Security re malicious emails eset_cos_sharepoint, or eset_cos_onedrive
Office ingestio and files when Event (Alert) Name: ESET Cloud Office Security: with the assigned Technique, for example ESET Cloud
Types of alerts: Office Security: XDR Endpoint Indicator of Threat
Security n of anything from Severity: Derived from severity
malware
(ECOS) Syslog Exchange, Fidelity: Is Severity by default
spam
format OneDrive, Teams, Kill Chain & MITRE | ATT&CK values are derived
phishing
logs to SharePoint, Gmail,
For the following
a and GoogleDrive
apps:
Stellar are identified as
Microsoft
Cyber malicious or
365
(Exchange, sensor. suspicious. When
OneDrive,
SharePoint, such an event
and Teams)
happens, a
Google
Workspace security event
(Gmail and
Google (malware, spam, or
Drive)
phishing) is
generated and
ingested by Stellar
Cyber's Syslog-
based parser.
ECOS Detections
and Quarantine
events are mapped
from Syslog to the
Alerts index.
Deduplication is by
tenantid,
eset.ScanResult,
eset.OperationI
d, eset.Service,
and eset.Tenant.
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the query:
msg_origi
n.source:
eset_cos
AND
eset.Scan
Result:
(Malware*
OR Spam
OR
Phishing)

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
ESET ESET Protect Configu Stellar Cyber maps msg_origin.source: eset_protect
msg_class: eset_protect_filtered_websites, eset_protect_firewall_aggregated,
Protect Alerts and Events re ESET Protect eset_protect_enterprise_inspector, and eset_protect_threatevent
Event (Alert) Name:
The following types ingestio alerts and events.
ESET Protect (Filtered Websites Event): with the assigned Technique, for example ESET Protect
of alerts and n of The alerts and (Filtered Websites Event): Blocked by Internal IP blacklist
events are JSON events are read ESET Protect (Firewall Aggregated Event): with the assigned Technique, for example ESET Protect
(Firewall Aggregated Event): Security vulnerability exploitation attempt
supported: format from the Syslog ESET Protect (ESET Inspect Alert): with the assigned Technique, for example ESET Protect (ESET
logs to index, enriched Inspect Alert): Suspicious PowerShell script - Obfuscation
Filtered ESET Protect (Threat Event): with the assigned Technique, for example ESET Protect (Threat
Websites a with Stellar Cyber Event): XDR Endpoint Indicator of Threat
Event
Stellar fields, and mapped Severity: Derived from event.severity_str for ESET Protect event:
Firewall
Aggregated Cyber (with deduplication) HIGH: 75
Event
sensor. to the Alerts index. FATAL: 75
ESET
Inspect Error: 75
Alert Deduplication is by MED: 55
Threat the following fields: Warning: 25
Event
ESET LOW: 25
Refer to Events Protect Information: 10
(Filtered
exported to JSON Websites DIAGNOSTIC: 10
format. E te v n e a n n t) t — id, Fidelity: Is Severity by default
eset.rule Kill Chain & MITRE | ATT&CK values are derived
_id,
host.name,
file.hash
.sha1,
srcip, and
dstip.
ESET
Protect
(Firewall
Aggregated
Event)—
tenantid,
event.thr
eat.name,
eset.sour
ce_uuid,
srcip,
dstip, and
user.name.
ESET
Protect
(ESET
Inspect
Alert)—
tenantid,
eset.eial
armid, and
eset.rule
name.
ESET
Protect
(Threat
Event)—
tenantid,
process.e
xecutable,
host.ip,
and
file.hash
.sha1.
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the queries:
ESET
Protect
(Filtered
Websites
Event)—
msg_origi
n.source:
eset_prot
ect AND
eset.even
t_type:
\"Filtere
dWebsites
_Event\"
ESET
Protect
(Firewall
Aggregated
Event)—
msg_origi

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
n.source:
eset_prot
ect AND
eset.even
t_type:
\"Firewal
lAggregat
ed_Event\
"
ESET
Protect
(ESET
Inspect
Alert)—
msg_origi
n.source:
eset_prot
ect AND
eset.even
t_type:
\"ESET
Inspect
Alert\"
ESET
Protect
(Threat
Event)—
msg_origi
n.source:
eset_prot
ect AND
eset.even
t_type:
Threat_Ev
ent
ExtraHop ExtraHop ExtraH Stellar Cyber maps msg_origin.source: extrahop_reveal_x_360
msg_class: extrahop_reveal_x_360_detections
Reveal(x) Reveal(x) 360 op ExtraHop Event (Alert) Name: ExtraHop Reveal(x) 360: with the extrahop.title, for example ExtraHop Reveal(x) 360:
Unusual Archive File Upload
360 detection events Reveal( Reveal(x) 360
Severity: Derived from event.severity using risk score directly as severity score (0-99)
x) 360 detection events.
Fidelity: Is Severity by default
Connec The events are
Kill Chain & MITRE | ATT&CK values are derived
tor read from the
This Syslog index,
connect enriched with
or Stellar Cyber
ingests fields, and mapped
logs (with deduplication)
from to the Alerts index.
ExtraH Deduplication is by
op tenantid and
Reveal( extrahop.id.
x) 360
to get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Detecti
ons
content
type.
FortiEDR FortiEDR events FortiED Stellar Cyber maps msg_origin.source: fortinet_edr
msg_class: fortiedr_events
R FortiEDR events. Event (Alert) Name: FortiEDR: with the event.threat.name, for example FortiEDR: Unconfirmed
Executable
Connec The events are
Severity: Derived from fortinet_edr.severity:
tor read from the
Malicious: 65
This Syslog index, Suspicious: 55
connect enriched with Potentially Unwanted Program (PUP): 45
or Stellar Cyber Inconclusive: 35
Likely Safe: 25

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
ingests fields, and mapped Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived
logs (with deduplication)
from to the Alerts index.
FortiED Deduplication is by
R to get tenantid and
the raw fortinet_edr.ev
alerts entId.
that are
stored
in the
Syslog
index.
Select
the
Events
content
type.
Fortinet Fortinet Lacework Generic Stellar Cyber maps msg_origin.source: s3
msg_class: generic_s3_fortinet_lacework_alert_details
Lacework Alerts, which are S3 Fortinet Lacework Event (Alert) Name: Lacework: with the assigned Technique, for example Lacework: ApiFailedWithError
ingested using the Connec alerts. The alerts Severity: 45, by default
Generic S3 tor are read from the Fidelity: Is Severity by default
connector This Syslog index, Kill Chain & MITRE | ATT&CK values are derived
connect enriched with
or pulls Stellar Cyber
data fields, and mapped
sent to (with deduplication)
S3 for to the Alerts index.
Fortinet Deduplication is by
Lacewo tenantid and
rk to fortinet_lacewo
get the rk.EVENT_ID.
raw
alerts
that are
stored
in the
Syslog
index.
Google Google Workspace Google Stellar Cyber maps msg_origin.source: gsuite
msg_class: gsuite_alert
Workspace Alerts Worksp Google Workspace Alert Subtype: gsuite.type or type
The following are ace alerts. The alerts Event (Alert) Name: Google Workspace Alert: with the assigned Technique, for example Google Workspace
Alert: Phishing
Connec are read from the
supported: Severity: metadata.severity
tor Linux Events
Gmail Fidelity: Is Severity by default
phishing index, enriched
This Kill Chain & MITRE | ATT&CK values are assigned
Google with Stellar Cyber
identity connect
fields, and mapped
User or
Changes (with deduplication)
ingests
Access to the Alerts index.
Approvals alerts
Domain from Deduplication is by
wide
takeout Google org_id, tenantid,
State Worksp metadata.custom
Sponsored
Attack ace to erId, source,
Mobile get the type, and
device
manageme raw metadata.alertI
nt
alerts d.
Security
Center that are
rules
stored

|     | Ingesti | Mapping of |     |
| --- | ------- | ---------- | --- |
Third
| Third Party Data | on         | Native Alerts to         |     |
| ---------------- | ---------- | ------------------------ | --- |
| Party            |            | Notable Interflow Fields |     |
|                  | Type Metho | Stellar Cyber            |     |
Service
d Alerts
Data Loss
Prevention in the
Linux
Apps
outage
Events
Sensitive
Admin index.
Action
Select
Customer
abuse
the
Reporting
Alert
Rule
Chrome content
Google type.
Mandatory
Service
Announce
ment
Google
Operations
Google
Voice
AppMaker
Editor
App
Settings
Changed
msg_origin.source: group_ib
| Group IB Group IB alerts | Group- | Stellar Cyber maps |     |
| ------------------------ | ------ | ------------------ | --- |
msg_class: group_ib_alerts
|     | IB  | Group-IB alerts. |     |
| --- | --- | ---------------- | --- |
The alert types are: Event (Alert) Name: Group IB: with the event.threat.name, for example Group IB: Generic Trojan
|     | Connec | The alerts are read |     |
| --- | ------ | ------------------- | --- |
Severity: Derived from event.severity:
Generic
|     | Trojan tor | from the Syslog | 5: 99 |
| --- | ---------- | --------------- | ----- |
|     |            | index, enriched | 4: 80 |
Covert This
|     | Channel. |                    | 3: 60 |
| --- | -------- | ------------------ | ----- |
|     | connect  | with Stellar Cyber |       |
Exploit Kits
|     |     | fields, and mapped | Fidelity: Is Severity by default |
| --- | --- | ------------------ | -------------------------------- |
Malicious or
Kill Chain & MITRE | ATT&CK values are derived
|     | File ingests     | (with deduplication) |     |
| --- | ---------------- | -------------------- | --- |
|     | S u s p i c ious | to the Alerts index. |     |
A ct iv i t y logs
|     | from   | Deduplication is by |     |
| --- | ------ | ------------------- | --- |
|     | Group- | group_ib.ID.        |     |
IB to
get the
raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
| Halcyon | Halcyo | Stellar Cyber maps | msg_origin.source: halcyon |
| ------- | ------ | ------------------ | -------------------------- |
Halcyon alerts
msg_class: halcyon_alerts
n Halcyon alerts. The Event (Alert) Name: Halcyon: with the event.threat.name, for example Halcyon: VulnerableDriver
|     | Connec | alerts are read |     |
| --- | ------ | --------------- | --- |
Severity: Derived from halcyon.action:
|     | tor | from the Syslog | Report: Informational/Low: 30 |
| --- | --- | --------------- | ----------------------------- |
|     |     | index, enriched | Block: Medium: 45             |
This
Fidelity: Is Severity by default
|     | connect | with Stellar Cyber |     |
| --- | ------- | ------------------ | --- |
Kill Chain & MITRE | ATT&CK values are derived
fields, and mapped
or
|     | ingests | (with deduplication) |     |
| --- | ------- | -------------------- | --- |
to the Alerts index.
logs
|     | from   | Deduplication is by |     |
| --- | ------ | ------------------- | --- |
|     | Halcyo | halcyon.id.         |     |
n to get
the raw
alerts

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
HoxHunt HoxHunt events Hoxhun Stellar Cyber maps msg_origin.source: hoxhunt
msg_class: hoxhunt_threats
t HoxHunt events. Event (Alert) Name: HoxHunt: with the event.threat.name, for example HoxHunt: User Reported
Malicious Email
Connec The events are
Severity: Derived from event.severity_str:
tor read from the
COMPROMISED_EMAIL: 90
This Syslog index, SPEAR: 80
connect enriched with PHISH: 75
or Stellar Cyber SPAM: 60
ingests fields, and mapped INCONCLUSIVE: 45
logs (with deduplication) FALSE_POSITIVE: 3
from to the Alerts index. Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived
HoxHu Deduplication is by
nt to email.from.addr
get the ess,
raw email.to.addres
alerts ses, and
that are email.subject.
stored
in the
Syslog
index.
Select
the
Threats
content
type.
Huntress Huntress Incidents Huntres Stellar Cyber maps msg_origin.source: huntress
msg_class: huntress_incident_report
s Huntress incidents.
Alert Subtype: huntress.subject
Connec The incidents are
Event (Alert) Name: Huntress Incident: with the assigned Technique, for example Huntress Incident:
tor read from the Event Triggered Execution
Severity: Derived from event.severity_str
This Syslog index,
Fidelity: Is Severity by default
connect enriched with
Kill Chain & MITRE | ATT&CK values are derived
or Stellar Cyber
ingests fields, and mapped
logs (with deduplication)
from to the Alerts index.
Huntres Deduplication is by
s to get tenantid,
the raw huntress_id,
alerts huntress.organi
that are zation_id, and
stored huntress.accoun
in the t_id.
Syslog
Huntress has six
index.
indicator types for
Select
Tactic and
the
Technique
Incident

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Reports mapping:
content monitored_files,
type. process_detections
,
ransomware_canar
ies, footholds,
managed_identity,
and
antivirus_detection
s. One incident
could have as
many as six
indicators showing
at the same time.
HYAS Prote HYAS Protect HYAS Stellar Cyber maps msg_origin.source: hyas_protect
msg_class: hyas_protect_dns_log_report
ct passthrough alerts Protect HYAS Protect Event (Alert) Name: HYAS Protect (passthrough alert): with the assigned Technique, for example:
The following are Connec passthrough alerts. Domain tagged with Suspicious Registrar, for example: HYAS Protect (Watch Engine): Valid
Accounts
supported: tor The alerts are read
Tactic: Initial Access
Domain This from the Syslog
tagged with Technique: Valid Accounts
Suspicious connect index, enriched Sub-technique: Domain Accounts
Registrar
or with Stellar Cyber Domain tagged as blocked by HYAS Engine, for example> HYAS Protect (Block): Application
Domain Layer Protocol
tagged as ingests fields, and mapped
blocked by Tactic: Command and Control
HYAS Engi logs (with deduplication)
ne from to the Alerts index. Technique: Application Layer Protocol: DNS
Domain Domain tagged as Highly Suspicious, for example: HYAS Protect (Highly Suspicious): Dynamic
tagged as HYAS PDeduplication is by Resolution
Highly Tactic: Command and Control
Suspicious rotect tenantid,
Technique: Dynamic Resolution
to get dns.question.na
Severity: Derived from event.severity_str for HYAS threat level:
the raw me. and srcip. critical: 75
alerts high: 55
that are medium: 35
stored low: 15
in the Fidelity: Is Severity by default
Syslog Kill Chain & MITRE | ATT&CK values are derived
index.
Select
the
DNS Lo
g
Reports
content
type.
LimaCharlie LimaCharlie Alerts LimaCh Stellar Cyber maps msg_origin.source: limacharlie
msg_class: limacharlie_alert
The following types arlie LimaCharlie alerts. Event (Alert) Name: LimaCharlie: with the assigned Technique, for example LimaCharlie: Data
Manipulation
of events for alerts Connec The alerts are read
Severity: Derived from event.severity_str
collected by tor from the Syslog
Fidelity: Is Severity by default
LimaCharlie's EDR This index, enriched
Kill Chain & MITRE | ATT&CK values are derived
sensors are connect with Stellar Cyber
supported: or fields, and mapped
Process ingests (with deduplication)
Events logs to the Alerts index.
Logon
Events from Deduplication is by
FIM Events LimaCh tenantid and
Refer to Events. arlie to limacharlie.rou
get the ting.event_id.
raw
Tactic and
alerts
Technique are
that are

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
stored provided by the
in the LimaCharlie raw
Syslog alerts field
index. limacharlie.det
Select ect_mtd.tags.
the
Alerts
content
type.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: microsoft_app_governance_alerts
App alerts ft Microsoft App Event (Alert) Name: Microsoft App Governance: with the event.threat.name, for example Microsoft App
Governance: OAuth App with suspicious Reply URL
Governanc Graph Governance alerts.
Severity: Derived from event.severity_str:
e (Graph Securit The alerts are read
High: 75
Security y API from the Windows
Medium: 55
API) Connec Events index, Low: 35
tor enriched with Informational: 15
Stellar Cyber Unknown: 15
This
fields, and mapped Unknown future value: 15
connect
Fidelity: Is Severity by default
to the Alerts index.
or
Kill Chain & MITRE | ATT&CK values are derived
ingests Deduplication is by
logs tenantid and
from microsoft_graph
Graph _security_api.i
Securit d.
y API to
get the
raw
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: microsoft_data_loss_prevention_alerts
Data Loss alerts ft Microsoft Data Event (Alert) Name: Microsoft Data Loss Prevention: with the event.threat.name, for example Microsoft
Data Loss Prevention: Exfiltration
Prevention Graph Loss Prevention
Severity: Derived from event.severity_str:
(Graph Securit (DLP) alerts. The
High: 75
Security y API alerts are read Medium: 55
API) Connec from the Windows Low: 35
tor Events index, Informational: 15
enriched with Unknown: 15
This
Stellar Cyber Unknown future value: 15
connect
Fidelity: Is Severity by default
fields, and mapped
or Kill Chain & MITRE | ATT&CK values are derived
to the Alerts index.
ingests
logs Deduplication is by
from tenantid and
Graph microsoft_graph
Securit _security_api.i
y API to d.
get the
raw
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
Microsoft Syslog Microso Stellar Cyber maps msg_origin.source: microsoft_defender
msg_class: microsoft_defender_alerts
Defender ft Microsoft Defender
Alert Subtype: microsoft_defender.title
for Endpoint Defend ATP alerts.
Event (Alert) Name: Microsoft Defender ATP: with the assigned Technique, for example Microsoft
er for Deduplication is by Defender ATP: OS Credential Dumping
Severity: Derived from threat and event.severity_str
Endpoi tenantid,
Fidelity: Is Severity by default
nt host.ip,
Tactic: XDR Malware
Connec host.name, and Mitre TTP mappings are provided by the Microsoft ATP field microsoft_defender.mitreTechniques. When
tor microsoft_defen the field is empty, Stellar Cyber's own TTP mapping is used.
This der.id.
connect
 The
or
lastUpdateTi
ingests
me
logs
timestamp is
from
used with the
Microso
API to pull
ft
alerts/events.
Defend
The
er for
alertCreation
Endpoi
Time
nt
timestamp is
(connec
not used.
tor).
This may
Select
result in the
the
old event
Alerts
being pulled

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
content again when
type. an update
happens on
This
the event.
alert
integrati
on
support
s the
followin
g
detectio
n
sources
: Windo
wsDefe
nderAv
and
Window
sDefen
derAtp.
If you
have
integrat
ed both
Microso
ft
Defend
er for
Endpoi
nt
(connec
tor) and
Window
s
Defend
er
Antiviru
s (free
version)
, there
may be
two
data
sources
for third
party
native
alerts.
The
integrati
on of
Microso
ft
Defend
er for
Endpoi
nt
(connec

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
tor)
may
stop the
alert
mappin
g for
Window
s
Defend
er
Antiviru
s (free
version)
.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_apif
msg_class: microsoft_defender_for_endpoint_alerts
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender ATP: with the assigned Technique, for example Microsoft
Defender ATP: OS Credential Dumping
for Endpoint Graph for Endpoint alerts.
Severity: Derived from event.severity_str:
(Graph Securit The alerts are read
High: 75
Security y API from the Windows
Medium: 55
API) Connec Events index, Low: 35
tor enriched with Informational: 15
Stellar Cyber Unknown: 15
This
fields, and mapped Unknown future value: 15
connect
Fidelity: Is Severity by default
to the Alerts index.
or
Kill Chain & MITRE | ATT&CK values are derived
ingests There is no
logs deduplication of
from alerts between
Graph Microsoft Defender
Securit ATP and Microsoft
y API to Defender for
get the Endpoint (Graph
raw Security API).
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
Microsoft Microsoft Defender Azure Stellar Cyber maps msg_origin.source: azure_eventhub
msg_class: microsoft_defender_cloud
Defender for Cloud alerts Event Microsoft Defender Event (Alert) Name: Microsoft Defender for Cloud: with the assigned Technique, for example Microsoft
Defender for Cloud: Traffic detected from IP addresses recommended for blocking
for Cloud Hub for Cloud alerts.
Refer to Alerts. Severity: Derived from original severity from Microsoft Defender for Cloud
Connec The alerts are read
Fidelity: Is Severity by default
tor from the Windows Kill Chain & MITRE | ATT&CK values are derived from microsoft_defender_cloud.Intent:
This Events index, Probing, Reconnaissance
connect enriched with PreAttack , Reconnaissance
or Stellar Cyber
ingests fields, and mapped
logs (with deduplication)
from to the Alerts index.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
the Deduplication is by
content tenantid and
type, microsoft_defen
Microso der_cloud.Syste
ft mAlertId.
Defend
er for
Cloud,
to get
the raw
alerts
that are
stored
in the
Window
s
Events
index.
| Microsoft          | msg_origin.source: microsoft_graph_security_api |     |
| ------------------ | ----------------------------------------------- | --- |
| Graph Security API | Microso Stellar Cyber maps                      |     |
msg_class: microsoft_defender_for_cloud_alerts
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender for Cloud: with the assigned Technique, for example Microsoft
for Cloud Defender for Cloud: Traffic detected from IP addresses recommended for blocking
Graph for Cloud alerts.
Severity: Derived from event.severity_str:
| (Graph | Securit The alerts are read |     |
| ------ | --------------------------- | --- |
High: 75
Security
|      | y API from the Windows | Medium: 55        |
| ---- | ---------------------- | ----------------- |
| API) | Connec Events index,   | Low: 35           |
|      | tor enriched with      | Informational: 15 |
|      | Stellar Cyber          | Unknown: 15       |
This
Unknown future value: 15
connect fields, and mapped
Fidelity: Is Severity by default
to the Alerts index.
|     | or Kill Chain & MITRE | ATT&CK values are derived |     |
| --- | ------------------------------------------------- | --- |
ingests There is no
logs deduplication of
from alerts between
Graph Microsoft Defender
Securit for Cloud and
y API to Microsoft Defender
get the for Cloud (Graph
raw Security API).
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
msg_origin.source: ms_defender_for_cloud_apps
| Microsoft Microsoft Defender | Microso Stellar Cyber maps |     |
| ---------------------------- | -------------------------- | --- |
msg_class: microsoft_defender_for_cloud_apps_alerts
| Defender | ft  |     |
| -------- | --- | --- |
for Cloud Apps Microsoft Defender Event (Alert) Name: Microsoft Defender for Cloud Apps: {microsoft_defender_for_cloud_apps.title}, for
example Microsoft Defender for Cloud Apps: Activity from a Tor IP address
| for Cloud alerts | Defend for Cloud Apps |     |
| ---------------- | --------------------- | --- |
Apps er for Severity: Derived from original severity from Microsoft Defender for Cloud Apps:
alerts. The alerts
| The risk categories |     | 0: LOW |
| ------------------- | --- | ------ |
Cloud are read from the
| are: |     | 1: MEDIUM |
| ---- | --- | --------- |
Apps
|               | Windows Events                                      | 2: HIGH          |
| ------------- | --------------------------------------------------- | ---------------- |
| 0:            | Connec index, enriched                              | 3: INFORMATIONAL |
| THREAT_DETECT | tor                                                 |                  |
|               | with Stellar Cyber Fidelity: Is Severity by default |                  |

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Kill Chain & MITRE | ATT&CK values are derived from microsoft_defender_cloud.Intent:
| ION | This fields, and mapped |     |
| --- | ----------------------- | --- |
UNKNOWN, Reconnaissance
connect (with deduplication)
| 1:            |                         | PREATTACK , Reconnaissance |
| ------------- | ----------------------- | -------------------------- |
| PRIVILEGED_AC | or to the Alerts index. |                            |
ingests
| COUNT_MONITO | Deduplication is by |     |
| ------------ | ------------------- | --- |
logs
| RING | tenantid and |     |
| ---- | ------------ | --- |
from
microsoft_defen
| 2: COMPLIANCE | Microso |     |
| ------------- | ------- | --- |
der_for_cloud_a
| 3: DLP | ft  |     |
| ------ | --- | --- |
pps._id.
Defend
4: DISCOVERY
er for
| 5:  | Cloud |     |
| --- | ----- | --- |
SHARING_CONTRApps to
| OL  | get the |     |
| --- | ------- | --- |
| 7:  | raw     |     |
alerts
ACCESS_CONTR
| OL  | that are |     |
| --- | -------- | --- |
stored
8:
in the
CONFIGURATION
Window
_MONITORING
s
Events
index.
Select
the
Alerts
content
type.
msg_origin.source: microsoft_graph_security_api
| Microsoft Graph Security API | Microso Stellar Cyber maps |     |
| ---------------------------- | -------------------------- | --- |
msg_class: microsoft_defender_for_cloud_apps_alerts
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender for Cloud Apps: {microsoft_defender_for_cloud_apps.title}, for
example Microsoft Defender for Cloud Apps: Activity from a Tor IP address
| for Cloud | Graph for Cloud Apps                       |     |
| --------- | ------------------------------------------ | --- |
| Apps      | Severity: Derived from event.severity_str: |     |
Securit alerts. The alerts
High: 75
| (Graph | y API are read from the |     |
| ------ | ----------------------- | --- |
Medium: 55
Security
|      | Connec Windows Events | Low: 35           |
| ---- | --------------------- | ----------------- |
| API) | tor index, enriched   | Informational: 15 |
|      | with Stellar Cyber    | Unknown: 15       |
This
|     | fields, and mapped | Unknown future value: 15 |
| --- | ------------------ | ------------------------ |
connect
Fidelity: Is Severity by default
to the Alerts index.
|     | or Kill Chain & MITRE | ATT&CK values are derived |     |
| --- | ------------------------------------------------- | --- |
ingests There is no
logs deduplication of
from alerts between
Graph Microsoft Defender
Securit for Cloud Apps and
y API to Microsoft Defender
get the for Cloud Apps
raw (Graph Security
alerts API).
that are
stored
in the
Window
s
Events
index.
Select
the
Alert

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
content
type.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: microsoft_defender_for_identity_alerts
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender for Identity: with the event.threat.name, for example Microsoft
Defender for Identity: Potential Credential Abuse in Entra ID Authentication
for Identity Graph for Identity alerts.
Severity: Derived from event.severity_str:
(Graph Securit The alerts are read
High: 75
Security y API from the Windows Medium: 55
API) Connec Events index, Low: 35
tor enriched with Informational: 15
Stellar Cyber Unknown: 15
This
fields, and mapped Unknown future value: 15
connect
Fidelity: Is Severity by default
to the Alerts index.
or Kill Chain & MITRE | ATT&CK values are derived
ingests Deduplication is by
logs tenantid and
from microsoft_graph
Graph _security_api.i
Securit d.
y API to
get the
raw
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: microsoft_defender_for_office365_alerts
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender for Office 365: with the event.threat.name, for example Microsoft
for Office Graph for Office 365 Defender for Office 365: Email messages removed after delivery
Severity: Derived from event.severity_str:
365 (Graph Securit alerts. The alerts
High: 75
Security y API are read from the
Medium: 55
API) Connec Windows Events Low: 35
tor index, enriched Informational: 15
with Stellar Cyber Unknown: 15
This
fields, and mapped Unknown future value: 15
connect
Fidelity: Is Severity by default
to the Alerts index.
or
Kill Chain & MITRE | ATT&CK values are derived
ingests Deduplication is by
logs tenantid and
from microsoft_graph
Graph _security_api.i
Securit d.
y API to
get the
raw
alerts
that are
stored
in the
Window

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
s
Events
index.
Select
the
Alert
content
type.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: microsoft_graph_defender_xdr_alert
Defender alerts ft Microsoft Defender Event (Alert) Name: Microsoft Defender XDR: with the microsoft_graph_security_api.title, for example
Microsoft Defender XDR: Activity Outside of U.S.
XDR Graph XDR alerts. The
Severity: Derived from event.severity_str:
Securit alerts are read
High: 75
y API from the Syslog
Medium: 55
Connec index, enriched
Low: 35
tor with Stellar Cyber Informational: 15
This fields, and mapped Unknown: 15
connect (with deduplication) Unknown future value: 15
or to the Alerts index. Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived
ingests Deduplication uses
logs the
from microsoft_graph
Graph _security_api.i
Securit d field.
y API to
get the
raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Alert
content
type.
Microsoft riskDetections>risk Microso The value in the msg_origin.source: azure_ad
msg_class: azure_ad_risk_detection
Entra Events ft Entra fields for the data Event (Alert) Name: Microsoft Entra RiskDetection: with the assigned Technique, for example Microsoft
Entra RiskDetection: Valid Accounts
ID (formerly ID (formtype noted at left
Azure AD)  The erly are mapped to Severity: Derived from riskLevel
Fidelity: Is Severity by default
integration Azure Stellar Cyber's
Kill Chain & MITRE | ATT&CK values are derived
does not AD) XDR Alert index.
include alerts Connec These alerts are
of tor suitable for MITRE
"riskEventTy This | ATT&CK
pe": connect classification, but
"generic". or do not contain
ingests tactic and
several technique values.
log Stellar Cyber has
types evaluated each
from possible alert and
Microso assigned a
ft Entra corresponding
ID to MITRE | ATT&CK

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
get the Stage, Tactic and
raw Technique.
alerts Deduplication is by
that are tenantid,
stored riskEventType,
in the riskLevel,
Window userDisplayName,
s and ipAddress.
Events
index.
Only
Risk
Detecti
on logs
are
relevant
to alert
mappin
g.
Select
the
Risk
Detecti
on
Collecti
on
content
type.
 W
h
e
n
b
ot
h
th
e
M
ic
ro
s
of
t
E
nt
ra
I
D
(f
or
m
er
ly
A
z
ur
e
A

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
D
)
c
o
n
n
e
ct
or
a
n
d
th
e
M
ic
ro
s
of
t
G
ra
p
h
S
e
c
ur
it
y
A
PI
c
o
n
n
e
ct
or
ar
e
e
n
a
bl
e
d
fo
r
th
e
s
a
m
e
te
n
a
nt

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
,
th
e
s
a
m
e
u
n
d
er
lyi
n
g
ri
s
k
e
v
e
nt
wi
ll
g
e
n
er
at
e
t
w
o
al
er
ts
,
o
n
e
fo
r
e
a
c
h
c
o
n
n
e
ct
or
.
It
is
re
c
o
m

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
m
e
n
d
e
d
th
at
w
h
e
n
y
o
u
e
n
a
bl
e
th
e
M
ic
ro
s
of
t
G
ra
p
h
S
e
c
ur
it
y
A
PI
c
o
n
n
e
ct
or
,
y
o
u
di
s
a
bl
e
th
e
M

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
ic
ro
s
of
t
E
nt
ra
I
D
(f
or
m
er
ly
A
z
ur
e
A
D
)
c
o
n
n
e
ct
or
to
a
v
oi
d
al
er
t
d
u
pl
ic
at
io
n.
Microsoft Graph Security API Microso Stellar Cyber maps msg_origin.source: microsoft_graph_security_api
msg_class: azure_ad_identity_protection_alerts
Entra ID alerts ft Microsoft Entra ID Event (Alert) Name: Microsoft Entra ID Protection: with the event.threat.name, for example Microsoft Entra
ID Protection: Sign-in from malicious IP address
Protection Graph Protection alerts.
Severity: Derived from event.severity_str:
(Graph Securit The alerts are read
High: 75
Security y API from the Windows Medium: 55
API) Connec Events index, Low: 35
tor enriched with Informational: 15
Stellar Cyber Unknown: 15
This
fields, and mapped Unknown future value: 15
connect
Fidelity: Is Severity by default
to the Alerts index.
or Kill Chain & MITRE | ATT&CK values are derived
ingests Deduplication is by
logs tenantid and
from microsoft_graph

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Graph _security_api.i
Securit d.
y API to
get the
raw
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
 W
h
e
n
b
ot
h
th
e
M
ic
ro
s
of
t
G
ra
p
h
S
e
c
ur
it
y
A
PI
c
o
n
n
e
ct
or
a
n
d
th
e

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
M
ic
ro
s
of
t
E
nt
ra
I
D
(f
or
m
er
ly
A
z
ur
e
A
D
)
c
o
n
n
e
ct
or
ar
e
e
n
a
bl
e
d
fo
r
th
e
s
a
m
e
te
n
a
nt
,
th
e
s
a
m
e
u
n

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
d
er
lyi
n
g
ri
s
k
e
v
e
nt
wi
ll
g
e
n
er
at
e
t
w
o
al
er
ts
,
o
n
e
fo
r
e
a
c
h
c
o
n
n
e
ct
or
.
It
is
re
c
o
m
m
e
n
d
e
d
th
at
w

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
h
e
n
y
o
u
e
n
a
bl
e
th
e
M
ic
ro
s
of
t
G
ra
p
h
S
e
c
ur
it
y
A
PI
c
o
n
n
e
ct
or
,
y
o
u
di
s
a
bl
e
th
e
M
ic
ro
s
of
t
E
nt
ra
I

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
D
(f
or
m
er
ly
A
z
ur
e
A
D
)
c
o
n
n
e
ct
or
to
a
v
oi
d
al
er
t
d
u
pl
ic
at
io
n.
msg_origin.source:office365
Microsoft Windows Events Office Stellar Cyber maps msg_class: office365_audit_general
Office 365 365 Microsoft Office Alert Subtype: event.threat.name or office365.Name
Connec 365 alerts from the Event (Alert) Name: Microsoft 365: with the assigned Technique and the assigned (Tactic), for example
Microsoft 365: Valid Accounts (Privilege Escalation)
tors AlertTriggered
Fidelity: Is Severity by default
This operation. Severity: Derived from Office 365 alert policy Severity event.severity_str:
connect For the Audit High: 75
or Medium: 55
General content
ingests Low: 35
type, Office 365
logs Informational: 15
alerts contain
Kill Chain & MITRE | ATT&CK values are mapped to the Office 365 alert policies and the category to which
from events from the each policy is assigned. You can also refer to the Microsoft documentation.
Microso
AlertTriggered Click Here for Alert Details
ft Office Severi
operation, which Alerts Tactic Technique
365 to ty
are sent to the
get the High Severity Alerts:
Alerts index.
raw
The source records A potentially malicious URL Initial Access Phishing High
alerts click was detected
may also include
that are
related events in A user clicked through to a Initial Access Phishing High
stored potentially malicious URL
the
in the
Window AlertEntityGenera A as c s ti o v c it i y a t f e ro d m IP a a p d a d s r s e w ss ord-spray Credential Brute Force High
Access
ted operation.
s
Some information

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Events (AlertEntityId and Activity from a Tor IP address Command and Proxy High
index. EntityType) from Control
Select the
| Data exfiltration to an app that | Exfiltration | Exfiltration Over Web Service | High |
| -------------------------------- | ------------ | ----------------------------- | ---- |
the AlertEntityGenera is not sanctioned
ted operation is
Audit
| Data Leaks - Priority Users | Exfiltration | Exfiltration Over Web Service | High |
| --------------------------- | ------------ | ----------------------------- | ---- |
General merged with the
AlertTriggered
content DataLossPrevention Exfiltration Exfiltration Over Web Service High
type. operation for the
same Alert ID. The E l e v a t io n of administrative P r i v ile g e Valid Accounts High
Only pr i v il e g e
E s c a la t ion
information
the
(AlertEntityId and Form blocked due to potential Lateral Internal Spearphishing High
AlertTri
| phishing attempt | Movement |     |     |
| ---------------- | -------- | --- | --- |
EntityType) is
ggered
stored in the
operati Form flagged and confirmed Initial Access Phishing High
as phishing
event_summary
on is
field.
relevant High Alert Forwarding Redirect XDR UBA XDR Anomaly High
to alert Deduplication is by
| Malware detection | Execution | User Execution | High |
| ----------------- | --------- | -------------- | ---- |
mappin tenantid and
g. AlertId.
| Messages have been delayed      | XDR NBA        | XDR Rule Violation | High |
| ------------------------------- | -------------- | ------------------ | ---- |
| Potential nation-state activity | Initial Access | Valid Accounts     | High |
| Privilege Escalation - Office   | Privilege      | Valid Accounts     | High |
365
Escalation
Risky Action
|     | XDR UBA | XDR Anomaly | High |
| --- | ------- | ----------- | ---- |
Suspicious connector activity
|                             | Initial Access | Phishing         | High |
| --------------------------- | -------------- | ---------------- | ---- |
| Suspicious email forwarding | Collection     | Email Collection | High |
activity
| Suspicious impersonated | Defense Evasion | Masquerading | High |
| ----------------------- | --------------- | ------------ | ---- |
activity
| Suspicious inbox forwarding | Collection | Email Collection | High |
| --------------------------- | ---------- | ---------------- | ---- |
rule
Suspicious inbox manipulation
|     | Collection | Email Collection | High |
| --- | ---------- | ---------------- | ---- |
rule
| Suspicious OAuth app file | Persistence | Account Manipulation | High |
| ------------------------- | ----------- | -------------------- | ---- |
download activities
| Suspicious tenant sending | Privilege | Valid Accounts | High |
| ------------------------- | --------- | -------------- | ---- |
patterns observed
Escalation
| Tenant restricted from sending | Privilege | Valid Accounts | High |
| ------------------------------ | --------- | -------------- | ---- |
email
Escalation
| Tenant restricted from sending | Initial Access | Valid Accounts | High |
| ------------------------------ | -------------- | -------------- | ---- |
unprovisioned email
Unusual addition of credentials
|                            | Credential         | Steal Application Access Token      | High |
| -------------------------- | ------------------ | ----------------------------------- | ---- |
| to an OAuth app            | Access             |                                     |      |
| Unusual external user file | Impact/Exfiltratio | Data Destruction, Exfiltration Over | High |
activity
|                              | n              | Web Service    |      |
| ---------------------------- | -------------- | -------------- | ---- |
| User restricted from sending | Initial Access | Valid Accounts | High |
email
| User restricted from sharing | Lateral | Internal Spearphishing | High |
| ---------------------------- | ------- | ---------------------- | ---- |
forms and collecting
| responses                 | Movement       |                |       |
| ------------------------- | -------------- | -------------- | ----- |
| Medium Severity Alerts:   |                |                |       |
| Access granted to a users | Initial Access | Valid Accounts | Mediu |
mailbox
m
AccessGovernance
|     | Privilege  | Valid Accounts | Mediu |
| --- | ---------- | -------------- | ----- |
|     | Escalation |                | m     |

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
| Activities from suspicious user | Exfiltration | Exfiltration Over C2 Channel | Mediu |
| ------------------------------- | ------------ | ---------------------------- | ----- |
agents
m
| Activity from an anonymous | Command and | Proxy | Mediu |
| -------------------------- | ----------- | ----- | ----- |
proxy
|                                  | Control         |                          | m     |
| -------------------------------- | --------------- | ------------------------ | ----- |
| Activity from infrequent country | Defense Evasion | Unused/Unsupported Cloud | Mediu |
|                                  |                 | Regions                  | m     |
Add or remove delegated
|     | Collection | Email Collection | Mediu |
| --- | ---------- | ---------------- | ----- |
permission
m
| Admin triggered user     | XDR UBA    | XDR Suspicious User | Mediu |
| ------------------------ | ---------- | ------------------- | ----- |
| compromise investigation |            |                     | m     |
| Altum Capital            | Collection | Email Collection    | Mediu |
Forward/Redirect Rule
m
| Colleague Global Login | Initial Access | Valid Accounts | Mediu |
| ---------------------- | -------------- | -------------- | ----- |
m
| Data Leaks - General | Exfiltration | Exfiltration Over Web Service | Mediu |
| -------------------- | ------------ | ----------------------------- | ----- |
m
Delegate Permissions on
|     | Persistence | Account Manipulation | Mediu |
| --- | ----------- | -------------------- | ----- |
Mailbox
m
| Email sending limit exceeded | Initial Access | Valid Accounts | Mediu |
| ---------------------------- | -------------- | -------------- | ----- |
m
| External File Share Policy | Exfiltration | Exfiltration Over Web Service | Mediu |
| -------------------------- | ------------ | ----------------------------- | ----- |
m
| Forwarding | Collection | Email Collection | Mediu |
| ---------- | ---------- | ---------------- | ----- |
m
| Granted mailbox permission | Persistence | Account Manipulation | Mediu |
| -------------------------- | ----------- | -------------------- | ----- |
m
Granted mailbox permissions
|     | Persistence | Account Manipulation | Mediu |
| --- | ----------- | -------------------- | ----- |
m
| Impossible travel activity | XDR UBA | XDR Location Anomaly | Mediu |
| -------------------------- | ------- | -------------------- | ----- |
m
| Inbox Rule Modification | Collection | Email Collection | Mediu |
| ----------------------- | ---------- | ---------------- | ----- |
m
| InsiderRiskManagement | XDR UBA | XDR Anomaly | Mediu |
| --------------------- | ------- | ----------- | ----- |
m
| ISP for an OAuth App | Credential | Steal Application Access Token | Mediu |
| -------------------- | ---------- | ------------------------------ | ----- |
|                      | Access     |                                | m     |
Mailbox Permission Change
|          | Collection | Email Collection | Mediu |
| -------- | ---------- | ---------------- | ----- |
| Alert    |            |                  | m     |
| MailFlow | XDR UBA    | XDR Anomaly      | Mediu |
m
| Mass delete | Impact | Data Destruction | Mediu |
| ----------- | ------ | ---------------- | ----- |
m
| Mass download | Exfiltration | Data Transfer Size Limits | Mediu |
| ------------- | ------------ | ------------------------- | ----- |
m
| Mass download by a single | Exfiltration | Data Transfer Size Limits | Mediu |
| ------------------------- | ------------ | ------------------------- | ----- |
user
m
Messages containing
|                              | Initial Access | Phishing | Mediu |
| ---------------------------- | -------------- | -------- | ----- |
| malicious entity not removed |                |          | m     |
after delivery
Multiple failed login attempts
|     | Credential | Brute Force | Mediu |
| --- | ---------- | ----------- | ----- |
|     | Access     |             | m     |

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
| Multiple failed user log on | Credential | Brute Force | Mediu |
| --------------------------- | ---------- | ----------- | ----- |
attempts to an app
|                            | Access     |             | m     |
| -------------------------- | ---------- | ----------- | ----- |
| Multiple failed user logon | Credential | Brute Force | Mediu |
attempts to a service
|                            | Access |                  | m     |
| -------------------------- | ------ | ---------------- | ----- |
| Suspicious Amount of files | Impact | Data Destruction | Mediu |
being moved
m
Suspicious email deletion
|     | Impact | Data Destruction | Mediu |
| --- | ------ | ---------------- | ----- |
activity
m
| Suspicious email sending | Initial Access | Valid Accounts | Mediu |
| ------------------------ | -------------- | -------------- | ----- |
| patterns detected        |                |                | m     |
Suspicious Power BI report
|     | Persistence | Account Manipulation | Mediu |
| --- | ----------- | -------------------- | ----- |
sharing
m
| ThreatManagement | XDR UBA | XDR Anomaly | Mediu |
| ---------------- | ------- | ----------- | ----- |
m
| Transom Forwarding/Redirect | Collection | Email Collection | Mediu |
| --------------------------- | ---------- | ---------------- | ----- |
Rule
m
Unusual volume of external file
|     | Exfiltration | Exfiltration Over Web Service | Mediu |
| --- | ------------ | ----------------------------- | ----- |
sharing
m
| Unusual volume of file deletion | Impact | Data Destruction | Mediu |
| ------------------------------- | ------ | ---------------- | ----- |
m
| Users targeted by phish | Initial Access | Phishing | Mediu |
| ----------------------- | -------------- | -------- | ----- |
campaigns
m
| Low Severity Alerts:      |              |                               |     |
| ------------------------- | ------------ | ----------------------------- | --- |
| Alert when file is shared | Exfiltration | Exfiltration Over Web Service | Low |
externally
| Block cut/copy and paste | Persistence | Account Manipulation | Low |
| ------------------------ | ----------- | -------------------- | --- |
based on real-time content
inspection
| Block download on personal | Initial Access | Drive-by Compromise | Low |
| -------------------------- | -------------- | ------------------- | --- |
devices
CC_User-reported messages
|     | Initial Access | Phishing | Low |
| --- | -------------- | -------- | --- |
Compliance Manager Default
|     | Initial Access | Phishing | Low |
| --- | -------------- | -------- | --- |
Alert Policy
| DataGovernance              | Exfiltration | Exfiltration Over Web Service | Low |
| --------------------------- | ------------ | ----------------------------- | --- |
| Elevation of Exchange admin | Privilege    | Valid Accounts                | Low |
privilege
Escalation
| Email Quarantined              | Initial Access | Phishing | Low |
| ------------------------------ | -------------- | -------- | --- |
| Email reported by user as junk | Initial Access | Phishing | Low |
| Email reported by user as      | Initial Access | Phishing | Low |
malware or phish
Email reported by user as not
|     | Initial Access | Phishing | Low |
| --- | -------------- | -------- | --- |
junk
| Flextrade Billing account | XDR UBA | XDR Anomaly | Low |
| ------------------------- | ------- | ----------- | --- |
notification
| Mailbox access test Cloud App | Initial Access | Valid Accounts | Low |
| ----------------------------- | -------------- | -------------- | --- |
| Other                         | XDR UBA        | XDR Anomaly    | Low |
| Repeat users contributing to  | Persistence    | Valid Accounts | Low |
incidents
Sharepoint File Deletion
|                       | Impact | Data Destruction | Low |
| --------------------- | ------ | ---------------- | --- |
| Info Severity Alerts: |        |                  |     |

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
| Party | Notable Interflow Fields |     |     |     |     |
| ----- | ------------------------ | --- | --- | --- | --- |
Type Metho Stellar Cyber
Service
d Alerts
|     |     | Access Agreement Template | Privilege | Valid Accounts | Info |
| --- | --- | ------------------------- | --------- | -------------- | ---- |
Accessed
Escalation
|     |     | Admin submission result | XDR UBA | XDR Anomaly | Info |
| --- | --- | ----------------------- | ------- | ----------- | ---- |
completed
|     |     | Admin triggered manual | XDR UBA | XDR Anomaly | Info |
| --- | --- | ---------------------- | ------- | ----------- | ---- |
investigation of email
Administrative action
|     |     |     | XDR UBA | XDR Anomaly | Info |
| --- | --- | --- | ------- | ----------- | ---- |
submitted by an Administrator
|     |     | Creation of forwarding/redirect | Collection | Email Collection | Info |
| --- | --- | ------------------------------- | ---------- | ---------------- | ---- |
rule
|     |     | eDiscovery search started or | Discovery | Account Discovery | Info |
| --- | --- | ---------------------------- | --------- | ----------------- | ---- |
exported
|     |     | Email messages containing | Initial Access | Phishing | Info |
| --- | --- | ------------------------- | -------------- | -------- | ---- |
malicious file removed after
delivery
|     |     | Email messages containing | Initial Access | Phishing | Info |
| --- | --- | ------------------------- | -------------- | -------- | ---- |
malicious URL removed after
delivery
|     |     | Email messages containing | Initial Access | Phishing | Info |
| --- | --- | ------------------------- | -------------- | -------- | ---- |
malware removed after
delivery
|     |     | Email messages containing | Initial Access | Phishing | Info |
| --- | --- | ------------------------- | -------------- | -------- | ---- |
phish URLs removed after
delivery
|     |     | Email messages from a | Initial Access | Phishing | Info |
| --- | --- | --------------------- | -------------- | -------- | ---- |
campaign removed after
delivery
|     |     | Email messages removed | Initial Access | Phishing | Info |
| --- | --- | ---------------------- | -------------- | -------- | ---- |
after delivery
|     |     | Malware not zapped because | Initial Access | Phishing | Info |
| --- | --- | -------------------------- | -------------- | -------- | ---- |
ZAP is disabled
Phish delivered because a
|     |     |     | Initial Access | Phishing | Info |
| --- | --- | --- | -------------- | -------- | ---- |
user's Junk Mail folder is
disabled
Phish delivered due to an ETR
|     |     |     | Initial Access | Phishing | Info |
| --- | --- | --- | -------------- | -------- | ---- |
override
|     |     | Phish delivered due to an IP | Initial Access | Phishing | Info |
| --- | --- | ---------------------------- | -------------- | -------- | ---- |
allow policy
|     |     | Phish not zapped because | Initial Access | Phishing | Info |
| --- | --- | ------------------------ | -------------- | -------- | ---- |
ZAP is disabled
|     |     | Remediation action taken by | Initial Access | Phishing | Info |
| --- | --- | --------------------------- | -------------- | -------- | ---- |
admin on emails or URL or
sender
|     |     | Removed an entry in Tenant | Defense Evasion | Impair Defenses | Info |
| --- | --- | -------------------------- | --------------- | --------------- | ---- |
Allow/Block List
Tenant Allow/Block List entry is
|     |     |     | XDR UBA | XDR Policy Anomaly | Info |
| --- | --- | --- | ------- | ------------------ | ---- |
about to expire
|     |     | User requested to release a | Initial Access | Valid Accounts | Info |
| --- | --- | --------------------------- | -------------- | -------------- | ---- |
quarantined message
| Microsoft          | Azure              | msg_origin.source: azure_eventhub |     |     |     |
| ------------------ | ------------------ | --------------------------------- | --- | --- | --- |
| Microsoft Sentinel | Stellar Cyber maps |                                   |     |     |     |
msg_class: microsoft_sentinel
Sentinel incidents Event Microsoft Sentinel Event (Alert) Name: Microsoft Sentinel Incident: with the assigned Technique, for example Microsoft
|     | Hub | Sentinel Incident: Unfamiliar sign-in properties |     |     |     |
| --- | --- | ------------------------------------------------ | --- | --- | --- |
incidents. The
Refer to Severity: Derived from original severity from Microsoft Sentinel
Connec alerts are read
| Incidents. |     | Fidelity: Is Severity by default |     |     |     |
| ----------- | --- | -------------------------------- | --- | --- | --- |
tor
|     | from the Syslog | Kill Chain & MITRE | ATT&CK values are derived |     |     |     |
| --- | --------------- | ---------------------------------------------- | --- | --- | --- |
 This index, enriched
The
integration connect with Stellar Cyber
or fields, and mapped
focuses
exclusively ingests (with deduplication)
on Microsoft logs to the Alerts index.
from
Sentinel Deduplication is by
Incident data the
tenantid and
content
and only microsoft_senti
type,

| Ingesti | Mapping of |     |
| ------- | ---------- | --- |
Third
| Third Party Data on | Native Alerts to |     |
| ------------------- | ---------------- | --- |
Party Notable Interflow Fields
| Type Metho | Stellar Cyber |     |
| ---------- | ------------- | --- |
Service
d Alerts
| supports Microso | nel.IncidentNam |     |
| ---------------- | --------------- | --- |
| data ft          | e.              |     |
transferred Sentine
through l, to get
Azure Event the raw
Hub. alerts
that are
stored
in the
Syslog
index.
Microsoft msg_origin.source: microsoft_graph_security_api
Graph Security API Microso Stellar Cyber maps msg_class: microsoft_threat_intelligence_alerts
Threat alerts ft Microsoft Threat Event (Alert) Name: Microsoft Threat Intelligence: with the event.threat.name, for example Microsoft
Threat Intelligence: Connection to known threat actor infrastructure
| Intelligence Graph | Intelligence alerts. |     |
| ------------------ | -------------------- | --- |
(Graph Severity: Derived from event.severity_str:
| Securit | The alerts are read |     |
| ------- | ------------------- | --- |
High: 75
| Security y API | from the Windows |     |
| -------------- | ---------------- | --- |
Medium: 55
API)
| Connec | Events index, | Low: 35           |
| ------ | ------------- | ----------------- |
| tor    | enriched with | Informational: 15 |
|        | Stellar Cyber | Unknown: 15       |
This
|     | fields, and mapped | Unknown future value: 15 |
| --- | ------------------ | ------------------------ |
connect
Fidelity: Is Severity by default
to the Alerts index.
| or      | Kill Chain & MITRE | ATT&CK values are derived |     |
| ------- | ---------------------------------------------- | --- |
| ingests | Deduplication is by                            |     |
| logs    | tenantid and                                   |     |
| from    | microsoft_graph                                |     |
| Graph   | _security_api.i                                |     |
| Securit | d.                                             |     |
y API to
get the
raw
alerts
that are
stored
in the
Window
s
Events
index.
Select
the
Alert
content
type.
msg_origin.source: mimecast_email (for Mimecast API 1.0) and mimecast2_email (for Mimecast API 2.0)
| Mimecast Mimecast alerts Mimeca | Stellar Cyber maps |     |
| ------------------------------- | ------------------ | --- |
msg_class by event log type:
| st API | Mimecast alerts. |     |
| ------ | ---------------- | --- |
There are the mimecast_email_attachment_protect_log for Mimecast Attachment Protect logs
mimecast_email_av_log for Mimecast AV logs
| 1.0 | The alerts are read |     |
| --- | ------------------- | --- |
following types of mimecast_email_impersonation_protect_log for Mimecast Impersonation Protect logs
| Connec | from the Syslog |     |
| ------ | --------------- | --- |
alerts: mimecast_email_internal_email_protect_log for Mimecast Internal Email Protect logs
| tor | index, enriched | mimecast_email for Mimecast Malicious Receipt logs |
| --- | --------------- | -------------------------------------------------- |
M i m e c as t mimecast_email_url_protect_log for Mimecast URL Protect logs
| At t ac h m e nt Mimeca | with Stellar Cyber |                                        |
| ----------------------- | ------------------ | -------------------------------------- |
|  Protect                | fields, and mapped | mimecast2_email_mta_log for other logs |
safeguards st API
a g a in st Event (Alert) Name: Mimecast <event log type>: with the assigned Technique, for example Mimecast
| 2.0 | (with deduplication) Attachment Protect: Phishing |     |
| --- | ------------------------------------------------- | --- |
sp e a r
phishing to the Alerts index. Severity: 45, except for Mimecast URL Protect, which has Severity: 75
and other Connec
| t a r g e te d tor | Fidelity: Is Severity by default               |     |
| ------------------ | ---------------------------------------------- | --- |
| a t ta c k s       | Deduplication for                              |     |
| using email        | Kill Chain & MITRE | ATT&CK values are derived |     |
| This               | Mimecast API 1.0                               |     |
attachment
s
| connect | is by the following |     |
| ------- | ------------------- | --- |
Mimecast
| or  | fields: |     |
| --- | ------- | --- |
AV/AntiViru
s protects
| users by ingests | Attachment |     |
| ---------------- | ---------- | --- |
Protect and
checking

g
| Ingesti | Mapping of |     |
| ------- | ---------- | --- |
Third
| Third Party Data on | Native Alerts to |     |
| ------------------- | ---------------- | --- |
Party Notable Interflow Fields
| Type Metho | Stellar Cyber |     |
| ---------- | ------------- | --- |
Service
d Alerts
| the content    | AV/AntiViru |     |
| -------------- | ----------- | --- |
| again for logs | s—          |     |
| new from       | tenantid,   |     |
| malware        | srcip,      |     |
| released       | file.hash   |     |
Mimeca
.md5,
| Mimecast st to get | email.sen |     |
| ------------------ | --------- | --- |
| Impersonati        | der.addre |     |
on Protect the raw
| defends | ss, and |     |
| ------- | ------- | --- |
email.rec
| against alerts | ipient.ad |     |
| -------------- | --------- | --- |
emails that
| impersonat that are | dresses.    |     |
| ------------------- | ----------- | --- |
| e people            | Impersonati |     |
| and brands stored   | on Protect, |     |
Internal
Mimecast in the
Email , and
| Internal     | Malicious |     |
| ------------ | --------- | --- |
| Email Syslog | Receipt—  |     |
P ro te c t
| index.     | t e n antid |     |
| ---------- | ----------- | --- |
| de te c ts | a n d       |     |
| email-     | mimecast.   |     |
related Select
aCode.
security
| threats that the | URL      |     |
| ---------------- | -------- | --- |
| originate        | Protect— |     |
MTA Lo
| from within      | tenantid,       |     |
| ---------------- | --------------- | --- |
| an email         | srcip, url,     |     |
| system g         | email.sen       |     |
| Mimecast content | d e r . a d dre |     |
s s ,  a n d
| M a li ci o u s | e m a i l . r e c |     |
| --------------- | ----------------- | --- |
Re c e i p t type.
| Log is Mail | i p i e n t . a d |     |
| ----------- | ----------------- | --- |
dresses.
Transfer
Agent
| (MTA) data | Deduplication for |     |
| ---------- | ----------------- | --- |
| that       | Mimecast API 2.0  |     |
contains a
| virus found | is by the following |     |
| ----------- | ------------------- | --- |
by
| Mimecast | fields: |     |
| -------- | ------- | --- |
Mimecast
| URL Protec | Impersonati |     |
| ---------- | ----------- | --- |
on Protect,
| t blocks | Internal |     |
| -------- | -------- | --- |
malicious
| URLs | Email, and |     |
| ---- | ---------- | --- |
Malicious
Receipt
Refer to "Log Field
Log—
tenantid
| Descriptions" in | and       |     |
| ---------------- | --------- | --- |
| Understanding    | mimecast. |     |
processin
| SIEM Logs: | gId |     |
| ----------- | --- | --- |
Targeted Threat
Protection -
Attachment Protect
logs, AV logs,
Targeted Threat
Protection -
Impersonation
Protect logs, Target
Threat Protection -
Internal Email
Protect logs,
Receipt logs,
Targeted Threat
Protection - URL
Protect logs
msg_origin.source: netskopewsg
| Netskope Netskope Alerts Netsko | Stellar Cyber maps |     |
| ------------------------------- | ------------------ | --- |
msg_class: netskopewsg_alert
| pe  | Netskope alerts. |     |
| --- | ---------------- | --- |
Event (Alert) Name:
The following types
Connec The alerts are read Netskope Alert: with the assigned Technique, for example Netskope Alert: DLP or Netskope
are supported:
| tor | from the Syslog |     |
| --- | --------------- | --- |
Alert: uba or Netskope Alert: policy or Netskope Alert: ips
Netskope
Alert This index, enriched Netskope Alert (Breach): with the assigned Technique, for example Netskope Alert (Breach):
|     | with Stellar Cyber | Drive-by Compromise |
| --- | ------------------ | ------------------- |
connect
Netskope Alert (Connection): with the assigned Technique, for example Netskope Alert
| Netskope or | fields, and mapped | (Connection): Web Service |
| ----------- | ------------------ | ------------------------- |
A le rt (with deduplication) Netskope Alert ( Malsite): with the assigned Technique, for example Netskope Alert (Malsite):
(B re ach) ingests
Cryptocurrency Mining
| Netskope logs | to the Alerts index. |     |
| ------------- | -------------------- | --- |
Severity: Derived from event.severity_str
Alert
| (Connectio from | Deduplication is by | Fidelity: Is Severity by default |
| --------------- | ------------------- | -------------------------------- |
n)
| Netsko | the following fields: | Kill Chain & MITRE | ATT&CK values are derived |
| ------ | --------------------- | ---------------------------------------------- |
Netskope
pe to
| Alert | All types— |     |
| ----- | ---------- | --- |
(Malsite)
| get the | tenantid, |     |
| ------- | --------- | --- |
user.name,
host.name,

|     | Ingesti | Mapping of |     |
| --- | ------- | ---------- | --- |
Third
| Third Party Data | on         | Native Alerts to         |     |
| ---------------- | ---------- | ------------------------ | --- |
| Party            |            | Notable Interflow Fields |     |
|                  | Type Metho | Stellar Cyber            |     |
Service
d Alerts
and
|     | raw    | netskopew |     |
| --- | ------ | --------- | --- |
|     | alerts | sg._event |     |
_id.
that are
stored
Breach—
|     | in the | tenantid, |     |
| --- | ------ | --------- | --- |
user.name,
|     | Syslog | and |     |
| --- | ------ | --- | --- |
netskopew
index.
sg.breach
_id.
Select
Connection
|     | the | —   |     |
| --- | --- | --- | --- |
tenantid,
|     | Alert | user.name, |     |
| --- | ----- | ---------- | --- |
and
|     | content | netskopew |     |
| --- | ------- | --------- | --- |
sg.connec
type.
tion_id.
Malsite—
tenantid,
user.name,
and
netskopew
sg.malsit
e_id.
Oracle OCI Stellar Cyber maps msg_origin.source: oracle_cloud_infrastructure
OCI CloudGuard
msg_class: oracle_cloud_guard
Cloud Alerts Streami OCI CloudGuard Event (Alert) Name: OCI CloudGuard: with the assigned Technique, for example OCI CloudGuard: Modify
| Infrastructur  | ng     | alerts. The alerts | Cloud Compute                                  |
| -------------- | ------ | ------------------ | ---------------------------------------------- |
| Refer to       |        |                    | Severity: Derived from event.severity_str      |
| e              | Connec | are read from the  |                                                |
| OCI CloudGuard |        |                    | Fidelity: Is Severity by default               |
| (OCI) Cloud    | tor    | Syslog index,      |                                                |
|                | .     |                    | Kill Chain & MITRE | ATT&CK values are derived |
| Guard          | This   | enriched with      |                                                |
Stellar Cyber
connect
|     | or  | fields, and mapped |     |
| --- | --- | ------------------ | --- |
(with deduplication)
ingests
|     | logs | to the Alerts index. |     |
| --- | ---- | -------------------- | --- |
from
Deduplication is by
|     | OCI to | tenantid, |     |
| --- | ------ | --------- | --- |
get the
oracle.data.add
|     | raw | itionalDetails. |     |
| --- | --- | --------------- | --- |
alerts
tenantId,
|     | that are | event.threat.na |     |
| --- | -------- | --------------- | --- |
stored
me, and
|     | in the | cloud.resource. |     |
| --- | ------ | --------------- | --- |
Syslog
id.
index.
Palo Alto Palo Stellar Cyber maps msg_origin.source: palo_alto_networks_cortex_xdr
Palo Alto Networks
msg_class: palo_alto_networks_cortex_xdr_alerts
| Networks CORTEX XDR | Alto | Palo Alto Networks | Event (Alert) Name: |
| ------------------- | ---- | ------------------ | ------------------- |
CORTEX X Networ CORTEX XDR Palo Alto Networks Cortex XDR (PAN NGFW): with the palo_alto_networks.name, for example Palo
Alerts
Alto Networks Cortex XDR (PAN NGFW): Generic Cryptominer Traffic Detection
DR ks alerts. The alerts Palo Alto Networks Cortex XDR (XDR Agent): with the palo_alto_networks.name, for example Palo
There are the
CORTE are read from the Alto Networks Cortex XDR (XDR Agent): Administrative Hash Exception
Palo Alto Networks Cortex XDR (XDR Analytics BIOC): with the palo_alto_networks.name, for
following
X XDR Syslog index, example Palo Alto Networks Cortex XDR (XDR Analytics BIOC): PowerShell runs
| categories of |        |               | suspicious base64-encoded commands |
| ------------- | ------ | ------------- | ---------------------------------- |
|               | Connec | enriched with |                                    |
Palo Alto Networks Cortex XDR (XDR BIOC): with the palo_alto_networks.name, for example Palo
alerts: Alto Networks Cortex XDR (XDR BIOC): Process runs from the recycle bin
|     | tor | Stellar Cyber |     |
| --- | --- | ------------- | --- |
PAN NGFW Palo Alto Networks Cortex XDR (XDR IOC): with the palo_alto_networks.name, for example Palo
|     |     | fields, and mapped | Alto Networks Cortex XDR (XDR IOC): IOC (WinSCP.exe) |
| --- | --- | ------------------ | ---------------------------------------------------- |
This
|     | XDR Agent |                      | Severity: Derived from event.severity_str |
| --- | --------- | -------------------- | ----------------------------------------- |
|     | connect   | (with deduplication) |                                           |
XDR
|     | Analytics | to the Alerts index. | Fidelity: Is Severity by default |
| --- | --------- | -------------------- | -------------------------------- |
or
|     | BIOC*   |                     | Kill Chain & MITRE | ATT&CK values are derived |
| --- | ------- | ------------------- | ---------------------------------------------- |
|     | ingests | Deduplication is by |                                                |
XDR BIOC*
|     | XDR IOC logs | tenantid and    |     |
| --- | ------------ | --------------- | --- |
|     | from         | palo_alto_netwo |     |
* Behavioral
| Indicator of | Palo | rks.alert_id. |     |
| ------------ | ---- | ------------- | --- |
Alto
Compromise
| (BIOC) | Networ |     |     |
| ------ | ------ | --- | --- |
ks
CORTE
X XDR
to get

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
Palo Alto Palo Alto Networks Prisma Stellar Cyber maps msg_origin.source: palo_alto_networks_prisma_cloud
msg_class: palo_alto_networks_prisma_cloud
Networks Prisma Cloud Cloud Palo Alto Networks Event (Alert) Name: Prisma Cloud: with the event.threat.name, for example Prisma Cloud: Explicitly
Denied File
Prisma alerts Connec Prisma Cloud
Severity: Derived from event.severity_str:
Cloud tor alerts. The alerts
critical: 60
This are read from the high: 50
connect Syslog index, medium: 30
or enriched with moderate: 30
ingests Stellar Cyber low: 10
logs fields, and mapped Fidelity: Is Severity by default
from (with deduplication) Kill Chain & MITRE | ATT&CK values are derived
Palo to the Alerts index.
Alto Deduplication is by
Networ tenantid,
ks .palo_alto_netwo
Prisma rks_prisma_clou
Cloud d.type,
to get palo_alto_netwo
the raw rks_prisma_clou
alerts d.audit_id,
that are palo_alto_netwo
stored rks_prisma_clou
in the d.incident_id.
Syslog
index.
Select
the
Alert
content
type.
Proofpoint Proofpoint TAP Proofpo Stellar Cyber maps msg_origin.source: proofpoint_tap
msg_class: proofpoint_tap_event
Targeted Alerts int TAP Proofpoint TAP Event (Alert) Name: Proofpoint TAP: with the event type and the assigned Technique, for example
Proofpoint TAP messageBlocked: Phishing
Attack Connec alerts. The alerts
There are the Severity: Derived from event.severity_str
Protection tor are read from the
following Fidelity: Is Severity by default
(TAP) This Syslog index,
categories of Kill Chain & MITRE | ATT&CK values are derived
connect enriched with
alerts:
or Stellar Cyber
Phish:
Phishing is ingests fields, and mapped
when
attackers logs (with deduplication)
s m e a n li d cious from to the Alerts index.
emails
designed to Proofpo Deduplication is by
t in ri t c o k f p a e lli o n p g le int TAP email.from.addr
f T o y r p a ic s a c ll a y, m. to get ess and
the intent is the raw email.sender.ad
to get users
to reveal alerts dress.
financial
information, that are

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
system stored There are the
credentials
or other in the following event
sensitive
data. Syslog types:
I s m ca p m os m te e r r : A index. Proofpoint
sets up an TAP
email Select messageBl
address the ocked
that looks Proofpoint
like it is Events TAP
from your messageD
company. content elivered
Then the
scammer type. Proofpoint
sends out TAP
messages clickBlocke
using that d
email
address. Proofpoint
This TAP
practice is clickDeliver
called ed
spoofing,
and the
scammer is
what we
call a
business
email
imposter.
Malware:
Malware is
a common
cyber
attack and
an umbrella
term for
various
malicious
programs
delivered
and
installed on
end-user
systems
and
servers.
These
attacks are
designed to
cause harm
to a
computer,
server, or
computer
network,
and are
used by
cyber
criminals to
obtain data
for financial
gain
Toad
(Telephone-
Oriented
Attack
Delivery):
Toad is a
type of
social
engineering
attack that
lures
potential
victims to
contact
fraudulent
call centers
managed
by threat
actors in
attempts to
steal
credentials
or install
malware
onto their
systems.
Spam:
Email
spam, also
known as
junk email,
refers to
unsolicited
email
messages,
usually sent
in bulk to a
large list of
recipients.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Recorded Recorded Future Record Stellar Cyber maps msg_origin.source: recorded_future
msg_class: recorded_future_alert and recorded_future_playbook_alert
Future Alerts and ed Recorded Future Event (Alert) Name:
Playbook Alerts Future alerts. The alerts Recorded Future Alert: with the rule name, for example Recorded Future Alert: Company Email
on Code Repository
Connec are read from the Recorded Future Playbook Alert: with the rule name, for example Recorded Future Playbook
For Playbook Alert, Alert: Domain Abuse
tor Syslog index,
there are the Severity: Derived from recorded_future.panel_status.risk_score
This enriched with
following Fidelity: Is Severity by default
categories of connect Stellar Cyber Kill Chain & MITRE | ATT&CK values are derived
or fields, and mapped
alerts:
ingests (with deduplication)
Domain
Abuse logs to the Alerts index.
Novel from Deduplication is by
Identity
Exposure Record the following fields:
Data ed Alert—
Leakage on tenantid
Code Future and
Repository recorded_
to get future.id.
Cyber
Vulnerabilit the raw Playbook
y Alert—
alerts tenantid
Third Party
and
Risk that are recorded_
future.pl
stored
aybook_al
ert_id.
in the
Syslog
index.
Select
the
Alert
and
Playbo
ok Alert
content
types.
SentinelOn Threats Sentine The threat dataset msg_origin.source: sentinelone_endpoint
msg_class: sentinelone_threat_detection
e Cloud lOne C includes a variety Event (Alert) Name: SentinelOne: with the assigned Technique, for example SentinelOne: User
Execution
onnecto of fields that
Severity: Derived from threat
r enable Stellar
Fidelity: Is Severity by default
This Cyber to map the Kill Chain & MITRE | ATT&CK values are mapped from the indicators field set.
connect native SentinelOne If more than one value is present in the Tactic and/or Technique fields, Stellar Cyber software determines
or can alerts to the Stellar which pair of values reflects the most severe position in the XDR Killchain and uses that pair for mapping.
If those source fields are empty, the Tactic is set to XDR Malware, Technique set to XDR Miscellaneous
ingest Cyber alert index. Malware, and Stage is set to Propagation.
Hosts, For example,
Threats threatInfo.clas
, and sification
Vulnera describes the
bilities. event (such as
Of Trojan). That and
these, other fields in the
only threatInfo record
Threat support direct
s are mapping of
relevant SentinelOne's
for alert MITRE | ATT&CK
mappin Tactic and
g. Technique fields to
Stellar Cyber's
Select
XDR Kill Chain.
the
Threats Deduplication is by
content org_id, tenantid,
type. host.name,

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
For host.ip,
related file.name,
Sentine file.path, and
lOne process.parent.
Deep name.
VisibilitySentinelOne alerts
events, are also
see deduplicated, for
Related example, if a
Events previously created
for Alert alert is updated.
Types. This type of
deduplication
avoids old alerts
being resent.
SentinelOn SentinelOne alerts Sentine Stellar Cyber maps msg_origin.source: sentinelone_endpoint
msg_class: sentinelone_unified_alerts
e lOne SentinelOne alerts. Event (Alert) Name: SentinelOne Singularity Identity: with the event.threat.name, for example SentinelOne
Singularity Identity: LDAP - Domain Information Discovery Detected
Singularity Connec The alerts are read
Severity: Derived from event.severity_str:
Identity tor from the Syslog
CRITICAL: 75
This index, enriched HIGH: 60
connect with Stellar Cyber MEDIUM: 45
or fields, and mapped LOW: 30
ingests (with deduplication) Fidelity: Is Severity by default
logs to the Alerts index. Kill Chain & MITRE | ATT&CK values are derived
from Deduplication is by
Sentine tenantid and
lOne to sentinelone.ext
get the ernal_id.
raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Unified
Alerts
content
type.
SOCRadar SOCRadar SOCRa Stellar Cyber maps msg_origin.source: socradar
msg_class: socradar_incidents
incidents dar SOCRadar Event (Alert) Name: Socradar: with the socradar.alarm_notification_texts.alarm_title, for example Socradar:
Supply Chain Activity Detected in Dark Web
Connec incidents. The
Severity: Derived from event.severity_str:
tor incidents are read
INFO 15
This from the Syslog
LOW: 30
connect index, enriched MEDIUM: 45
or with Stellar Cyber HIGH: 60
ingests fields, and mapped Fidelity: Is Severity by default
logs (with deduplication) Kill Chain & MITRE | ATT&CK values are derived
from to the Alerts index.
SOCRa Deduplication is by
dar to tenantid and
get the socradar.consol
raw idated_alarm_id.
alerts
that are

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
stored
in the
Syslog
index.
Select
the
Incident
s
content
type.
SonicWall SonicWall EndpointSonicW Stellar Cyber maps msg_origin.source: sonicwall_theron
msg_class: sonicwall_theron_alerts
Endpoint Security alerts all SonicWall Endpoint Event (Alert) Name: SonicWall Endpoint Security: with the sonicwall_theron.reason, for example SonicWall
Endpoint Security: OnDownload
Security Endpoi Security alerts. The
Severity: Derived from event.severity_str:
nt alerts are read
4: 60
Securit from the Syslog
3: 45
y index, enriched
2: 30
Connec with Stellar Cyber Fidelity: Is Severity by default
tor fields, and mapped Kill Chain & MITRE | ATT&CK values are derived
This (with deduplication)
connect to the Alerts index.
or Deduplication is by
ingests sonicwall_thero
logs n.alert_id.
from
SonicW
all
Endpoi
nt
Securit
y to get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
Sophos Sophos Alerts and Sophos Stellar Cyber maps msg_origin.source: sophos_events or sophos_alerts
msg_class: sophos_events or sophos_alerts
Central Sophos Events Central Sophos alerts and
Connec events. The alerts Event (Alert) Name: Sophos Alert: or Sophos Event: with the assigned Technique, for example Sophos
Alert: Data Encrypted for Impact or Sophos Event: User Execution
tor and events are
Alert Subtype: event.type and event.threat.name, for example,
This read from the Event::Endpoint::WebFilteringBlocked
connect Syslog index, Severity: Derived from event.severity_str
Fidelity: Is Severity by default
or enriched with
Kill Chain & MITRE | ATT&CK values are derived
ingests Stellar Cyber
logs fields, and mapped
from (with deduplication)
Sophos to the Alerts index.
Central Deduplication is by
to get tenantid and
the raw sophos.id.
alerts

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
that are The subtype uses
stored sophos.type. Only
in the Endpoint-related
Syslog alerts and events
index. are integrated.
Select
the
Alerts
and
Events
content
types.
Trellix Alerts Trellix Stellar Cyber msg_origin.source: fireeye_hx
msg_class: fireeye_alerts
(FireEye) (FireEy identifies the Alert Subtype:
Endpoint e) FireEye data IOC: event.name
Security Endpoi logged into the MAL: event.threat.name
nt Secu Syslog index. AMSI: event.threat.name
rity HX Records of the PROCGUARD: event.threat.name
Event (Alert) Name:
The type Alerts are then
Fireeye IOC: with the assigned Technique, for example: Fireeye IOC: XDR Indicator of
connect normalized, Compromise
or can enriched, and Fireeye MAL: with the assigned Technique, for example: Fireeye MAL: User Execution
be used mapped to the Fireeye AMSI: with the assigned Technique, for example: Fireeye AMSI: Windows Management
Instrumentation
for Alerts index. The
Fireeye PROCGUARD: with the assigned Technique, for example: Fireeye PROCGUARD: OS
three following fields are Credential Dumping
Severity: Derived from alert source and severity level event.severity_str
data included as part of
Fidelity: Is Severity by default
types the Stellar Cyber
Kill Chain & MITRE | ATT&CK values are assigned
but only alert description:
Alerts indicator.name
are and agent.url.
applica Each relevant
ble for Syslog record is
alert compared against
mappin existing records in
g. the Alert index and
Select not added to that
the index if the values
Alerts in the following
content fields match those
type. of an existing
record logged in
the previous 24
hours: org_id,
tenantid,
user.name,
host.ip,
event.name,
file.path,
process.path.
The following four
alert types are
supported: IOC,
MAL, AMSI, and
PROCGUARD.
Tactic and
Technique are
based on alert
type.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Deduplication is by
the following fields:
AMSI—
tenantid,
host.ip,
host.name,
event.url,
and
event.thr
eat.name.
IOC—
tenantid,
user.name,
host.ip,
host.name,
event.nam
e,
file.path,
and
process.e
xecutable.
MAL—
tenantid,
host.ip,
host.name,
event.url,
and
file.path.
PROCGUA
RD—
tenantid,
host.ip,
host.name,
event.url,
and
event.thr
eat.name.
Trellix Trellix MVISION Trellix Stellar Cyber maps msg_origin.source: trellix_mvision
msg_class: trellix_mvision_edr_alerts
MVISION Alerts MVISIO Trellix MVISION Event (Alert) Name: Trellix MVISION: with the assigned Technique, for example Trellix MVISION: Threat
Detected
N alerts. The alerts
Severity: Derived from event.severity_str and mapped to severity score:
Connec are read from the
s5: 85
tor Syslog index,
s4: 75
This enriched with s3: 60
connect Stellar Cyber s2: 45
or fields, and mapped s1: 30
ingests (with deduplication) s0: 15
logs to the Alerts index. Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived
from Deduplication is by
Trellix tenantid and
MVISIO trellix_mvision
N to get .id.
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Alerts
content
type.
Trend Micro Trend Micro Cloud Trend Stellar Cyber maps msg_origin.source: trendmicro_cloud_app_security
msg_class: trendmicro_cas_logs_exchange, trendmicro_cas_logs_onedrive,
Cloud App App Security Micro Trend Micro Cloud trendmicro_cas_logs_sharepoint, and trendmicro_cas_logs_teams
Security events Cloud App Security E Cl v o e u n d t (A A l p e p rt ) S N e a c m ur e i : t T y r : e n M d a M li ic c r i o o C u l s o u U d R A L p s p Security: with the event.threat.name, for example Trend Micro
App events. The events Severity: Derived from event.severity_str:
Securit are read from the Dangerous: 75
y Syslog index, Highly suspicious: 60
Connec enriched with Suspicious: 45
tor Stellar Cyber Untested: 15
High Risk: 60
fields, and mapped

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
This (with deduplication) Medium Risk: 45
Low RIsk: 30
connect to the Alerts index.
Fidelity: Is Severity by default
or Deduplication is by
Kill Chain & MITRE | ATT&CK values are derived
ingests trendmicro_clou
logs d_app_security.
from log_item_id.
Trend
Micro
Cloud
App
Securit
y to get
the raw
alerts
that are
stored
in the
Syslog
index.
Select
the
Exchan
ge,
OneDri
ve,
Sharep
oint
Log,
and
Teams
content
types.
Trend Micro Trend Micro Vision Trend Stellar Cyber maps msg_origin.source: trendmicro_visionone
msg_class: trendmicro_visionone_alerts
Vision One One Alerts Micro Trend Micro Vision Event (Alert) Name: Trend Micro Vision One: with the Trend Micro alert type (Model name), for example
Trend Micro Vision One: Suspicious File Creation in Uncommon Folder
Vision One alerts. The
Severity: Derived from event.severity_str and mapped to:
One alerts are read
Critical: 75
Connec from the Syslog
High: 55
tor index, enriched
Medium: 35
This with Stellar Cyber Low: 15
connect fields, and mapped Fidelity: Is Severity by default
or (with deduplication) Kill Chain & MITRE | ATT&CK values are derived
ingests to the Alerts index.
logs Deduplication is by
from tenantid and
Trend trendmicro_visi
Micro onone.workbench
Vision Id.
One to
Tactic and
get the
Technique are
raw
provided by the
alerts
Trend Micro Vision
that are
One raw alerts field
stored
trendmicro_visi
in the
onone.matchedRu
Syslog
les.
index.

|     | Ingesti | Mapping of |     |
| --- | ------- | ---------- | --- |
Third
| Third Party Data | on         | Native Alerts to         |     |
| ---------------- | ---------- | ------------------------ | --- |
| Party            |            | Notable Interflow Fields |     |
|                  | Type Metho | Stellar Cyber            |     |
Service
d Alerts
Select
the
Alerts
content
type.
Varonis Configu Varonis sends msg_origin.source: varonis_datadvantage
Varonis Alerts msg_class: varonis_datadvantage_file_system_operation or
DatAdvanta re Syslog CEF events varonis_datadvantage_directory_services_operation
File system
| ge  | operation ingestio | to Stellar Cyber, | Alert Subtype: varonis.rulename |
| --- | ------------------ | ----------------- | ------------------------------- |
Directory Event (Alert) Name: Varonis DatAdvantage: with the assigned Technique, for example Varonis
|     | services n of | which maps |     |
| --- | ------------- | ---------- | --- |
DatAdvantage: File and Directory Discovery
|     | operation CEF | Varonis |     |
| --- | ------------- | ------- | --- |
Severity: Derived from CEF severity
|     | format  | DatAdvantage         | Fidelity: Is Severity by default               |
| --- | ------- | -------------------- | ---------------------------------------------- |
|     | logs to | alerts to the Alerts | Kill Chain & MITRE | ATT&CK values are derived |
|     | a       | index.               |                                                |
|     | Stellar | Deduplication is by  |                                                |
Cyber
tenantid,
|     | sensor. | user.name, |     |
| --- | ------- | ---------- | --- |
file.name,
file.path, and
event.threat.na
me.
To search the
alerts in the Alerts
index or to search
the Original
Records in the
Syslog index, use
the query:
msg_class
:
(varonis_
datadvant
age_file_
system_op
eration
or
varonis_d
atadvanta
ge_direct
ory_servi
ces_opera
tion)
| VMware Alerts of type |       |               | msg_origin.source: carbonblack_cloud |
| ---------------------- | ----- | ------------- | ------------------------------------ |
|                        | VMwar | VMware Carbon | msg_class: carbonblack_alert         |
Carbon
CB Analytics, e Black alerts are Event (Alert) Name: Carbon Black: with the assigned Technique, for example Carbon Black: OS
Credential Dumping
| Black Cloud Device Control, | Carbon | assigned a |     |
| --------------------------- | ------ | ---------- | --- |
and Watchlist Severity: Assigned based on threat_cause_threat_category, values range from 20-55
|     | Black | MITRE technique / |     |
| --- | ----- | ----------------- | --- |
Fidelity: Is Severity by default, except Watchlist alerts and alerts with threat category of UNKNOWN which
|     | Cloud | tactic / | receive a computed value from the ML/SA pipeline |
| --- | ----- | -------- | ------------------------------------------------ |
Kill Chain & MITRE | ATT&CK values are derived from the ttps field of the threat_indicators record. If
|     | Connec | procedure |     |
| --- | ------ | ---------- | --- |
those fields are empty or the threat_type is UNKNOWN, the Tactic is set to XDR Malware, Technique is set
tor (TTP) which is to XDR Miscellaneous Malware, and Stage is set to Persistent Foothold.
reformatted but ORIGINAL FIELDS: In addition to the mapping of fields to Stellar Cyber Interflow fields, all of the original fields for
Select
|     |     | otherwise this alert type are included in the Interflow record. |     |
| --- | --- | --------------------------------------------------------------- | --- |
the
preserved during
Alert
mapping, except
content
as noted below.
type.
CB Analytics and
Device Control:
Alerts with
a
threat_caus
e_threat_ca
tegory of
NON_MAL
WARE,
NEW_MAL
WARE, and
KNOWN_M
ALWARE
are directly
mapped to
the Alerts

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
index. The
kill_chain_s
tatus
values
(RECONNA
ISSANCE,
WEAPONIZ
E,
DELIVER_
EXPLOIT,
INSTALL_R
UN,
COMMAND
_AND_CO
NTROL,
EXECUTE_
GOAL,
BREACH) a
re
preserved
and
mapped to
the Stellar
Cyber
XDR Kill
Chain.
Alerts with
a threat
category
value of
RISKY_PR
OGRAM
are
assigned a
Tactic of
XDR Malwa
re and
Techinque
of
XDR PUA.
Alerts with
threat
category
value of
UNKNOWN
are run
through
Stellar
Cyber's
ML/SA
pipeline, to
better
ascertain
the nature
of the alert
before
mapping it
to the Alert
index. This
type is
assigned
an Tactic of
XDR EBA a
nd
Technique
of
XDR Anom
aly
Watchlist: This
type of alert is
considered noisy
(generates a large
volume of hits), so
it is routed through
the ML/SA pipeline
using our Time
Series Analytic and
Rare models,
along with
deduplication,
before being
mapped to the
Alerts index. This
type of alert is
classified as Tactic:
XDR EBA with
Technique: XDR
Anomaly.

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
Deduplication is by
org_id, tenantid,
event.type,
host.external_i
p, host.ip,
process.name,
event.descripti
on_id, and
file.name.
VMware Carbon
Black alerts are
also deduplicated,
for example, if a
previously created
alert is updated.
This type of
deduplication
avoids old alerts
being resent.
Windows Events Window These events are msg_origin.source: windows_agent
msg_class: Microsoft-Windows-Windows Defender
Defender s Agent ingested to the Event (Alert) Name: WindowsDefenderAntivirus: with the assigned Technique, for
example WindowsDefenderAntivirus: XDR Trojan
Antivirus Detecti Stellar Cyber
Severity: Derived from threat name and severity level event.severity_str
(free on Logs Windows Events
Fidelity: Is Severity by default
version ingeste index. As of the
Kill Chain values are derived (not displayed if values are blank)
only) d from v4.3.2 release, See also:
a they are also now event.ms_incident_id contains Detection ID
Window processed into the threat contains Threat name
s Agent Alerts index. In
these logs, multiple
events correlate to
a single case, such
as event_id 1116
(malware
detected), one with
event_id 1117
(means malware is
quarantined).
Stellar Cyber
manages this,
tracking the events
to the related case
during the mapping
process.
Deduplication is by
tenantid,
event.ms_incide
nt_id, threat,
and file.path.
To search the
events in the Alerts
index or to search
the Original
Records in the
Windows Events
index, use the
query:

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
msg_class
:\"Micros
oft-
Windows-
Windows
Defender\
" AND
_exists_:
event.ms_
incident_
id.keywor
d"
WithSecure WithSecure WithSe Stellar Cyber maps msg_origin.source: withsecure_elements
msg_class: withsecure_elements_detection
Elements Elements cure WithSecure Event (Alert) Name: WithSecure: with the withsecure_elements.name, for example WithSecure:
Powershell Memorystream
detections Elemen Elements
Severity: Derived from event.severity_str:
ts detections. The
critical: 75
Connec detections are read
high: 60
tor from the Syslog
medium: 45
This index, enriched low: 30
connect with Stellar Cyber Fidelity: Is Severity by default
or fields, and mapped Kill Chain & MITRE | ATT&CK values are derived
ingests (with deduplication)
logs to the Alerts index.
from Deduplication is by
WithSe tenantid,
cure event.threat.na
Elemen me, user.name,
ts to get process.hash.sh
the raw a1,
alerts withsecure_elem
that are ents.detectionI
stored d, and
in the withsecure_elem
Syslog ents.descriptio
index. n.
Select
the
Detecti
ons
content
type.
Wiz Wiz events Wiz Stellar Cyber maps msg_origin.source: wiz
msg_class: wiz_issues
Connec Wiz events. The Event (Alert) Name: Wiz Cloud Security: with the assigned Technique, for example Wiz Cloud Security:
Exploitation for Defense Evasion
tor events are read
Severity: Derived from event.severity_str:
This from the Syslog
critical: 70
connect index, enriched high: 60
or with Stellar Cyber medium: 45
ingests fields, and mapped low: 30
logs (with deduplication) info: 15
from to the Alerts index. Fidelity: Is Severity by default
Kill Chain & MITRE | ATT&CK values are derived
Wiz to Deduplication is by
get the tenantid and
raw wiz.id.
alerts
that are
stored
in the
Syslog
index.
Select
the
Issues

Ingesti Mapping of
Third
Third Party Data on Native Alerts to
Party Notable Interflow Fields
Type Metho Stellar Cyber
Service
d Alerts
content
type.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber. All rights reserved.
Support | Contact Us |  