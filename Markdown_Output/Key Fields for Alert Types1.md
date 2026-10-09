✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Key Fields for Alert Types
There are Key Fields for the following:
Third Party Native Alert Types
ML and Rule-Based Alert Types
For information on Key Fields in the user interface, see Key Fields in User Interface.
Key Fields for Third Party Native Alert Types
Stellar Cyber supports third party native alert integration. The Key Fields for third party native alert
types are as follows:
Third Party Display Name Key Field Name Display Name Description
Abnormal Security email.message_id Message ID Unique identifier of the email
(abnormal_security) srcip Source IP Source IP address
email.recipient.addresses Recipient Address(es) All recipients of the email,
including those in the 'To', 'CC'
(carbon copy), and 'BCC' (blind
carbon copy) fields.
email.to.addresses To Address(es) Primary intended recipients of
the email. These are the email
addresses explicitly listed in the
'To' field of the email.
email.from.address From Address Email address that appears in
the 'From' field of the email. It is
the address that the recipient
sees as the sender of the email.
email.subject Email Subject Subject line of the email
abnormal_security.sentTime Sent Time Time the email was sent
abnormal_security.receivedTime Received Time Time the email was received
abnormal_security.attackStrateg Attack Strategy Strategy used in the attack
y
abnormal_security.attackType Attack Type Type of attack

Third Party Display Name Key Field Name Display Name Description
abnormal_security.attackVector Attack Vector Vector used in the attack
abnormal_security.remediationSt Remediation Status Status of the remediation
atus
abnormal_security.autoRemediat Auto-Remediated Whether the email was auto-
|     | ed  |     | remediated or not |
| --- | --- | --- | ----------------- |
abnormal_security.summaryInsig Summary Insights Summary insights about the
|     | hts |     | email |
| --- | --- | --- | ----- |
abnormal_security.urlCount URL Count Number of URLs in the email
abnormal_security.attachmentCo Attachment Count Number of attachments in the
|     | unt |     | email |
| --- | --- | --- | ----- |
abnormal_security.abxPortalUrl ABX Portal URL URL to the ABX portal for more
details
|     | url_list | URL List | List of URLs in the email |
| --- | -------- | -------- | ------------------------- |
Acronis (Antimalware protection) event.threat.name Alert Type Alert type
acronis_cyber_protect.details.thr Acronis Threat Name Acronis threat name
(acronis_cyber_protect)
eatName
|     | event.category | Alert Category | Alert category |
| --- | -------------- | -------------- | -------------- |
|     | host.name      | Host Name      | Host name      |
event.severity_str Acronis Severity Level Acronis severity level
|               | file.name         | File Name   | File name   |
| ------------- | ----------------- | ----------- | ----------- |
|               | file.path         | File Path   | File path   |
|               | file.hash.sha1    | File SHA1   | File SHA1   |
|               | file.hash.md5     | File MD5    | File MD5    |
|               | file.hash.sha256  | File SHA256 | File SHA256 |
| Acronis (EDR) | event.threat.name | Alert Type  | Alert type  |
(acronis_cyber_protect) event.category Alert Category Alert category
|     | host.name | Host Name | Host name |
| --- | --------- | --------- | --------- |
event.severity_str Acronis Severity Level Acronis severity level
acronis_cyber_protect.details.re Acronis Alert Redirect Link Acronis alert redirect link
directLink
acronis_cyber_protect.details.verAcronis Alert Verdict Acronis alert verdict
dict
Acronis (Email security) event.threat.name Alert Type Alert type
(acronis_cyber_protect) event.category Alert Category Alert category
event.severity_str Acronis Severity Level Acronis severity level
|     | email.from.address | Email From Address | Email from address |
| --- | ------------------ | ------------------ | ------------------ |
|     | email.subject      | Email Subject      | Email Subject      |
Acronis (URL filtering) event.threat.name Alert Type Alert type
(acronis_cyber_protect) acronis_cyber_protect.details.thr Acronis Threat Name Acronis threat name
eatName
|     | event.category | Alert Category | Alert category |
| --- | -------------- | -------------- | -------------- |

Third Party Display Name Key Field Name Display Name Description
|     | host.name | Host Name | Host name |
| --- | --------- | --------- | --------- |
event.severity_str Acronis Severity Level Acronis severity level
|       | url                | URL            | URL                          |
| ----- | ------------------ | -------------- | ---------------------------- |
|       | process.pid        | Process ID     | Process ID                   |
|       | process.executable | Process Path   | Process path                 |
| Armis | armis.alertId      | Alert ID       | Alert ID assigned by Armis   |
|       | armis.severity     | Armis Severity | Original severity from Armis |
(armis)
|     | armis.title | Alert Title | Title of the alert |
| --- | ----------- | ----------- | ------------------ |
armis.policyTitle Policy Title Title of the policy that triggered
the alert
armis.affectedDevicesCount Affected Devices Count Number of devices affected by
the alert
armis.deviceIds Affected Device IDs IDs of the affected devices
|     | host_list | Affected Devices | List of affected devices |
| --- | --------- | ---------------- | ------------------------ |
|     | ip        | Host IP          | Host IP address          |
|     | mac       | Host MAC         | Host MAC address         |
armis.status Armis Alert Status Current status of the alert from
Armis
Avanan (Delivered) email.from.address From Address Who the email is from
email.to.addresses To Address(es) Primary intended recipient of the
(avanan_delivered)
email
email.sender.address Sender Address Who actually sent the email on
behalf of the primary sender
email.recipient.addresses Recipient Address(es) Who received the email
(including CC and BCC)
|     | email.subject | Email Subject         | Email subject                   |
| --- | ------------- | --------------------- | ------------------------------- |
|     | url_list      | URL List              | URL(s) in the email             |
|     | domain_list   | Email Links Domain(s) | Email links domain(s)           |
|     | file_list     | File List             | File name of the malicious file |
|     | name          | File Name             | File name                       |
|     | hash.md5      | Host Hash             | File hash                       |
threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
Avanan (Quarantined) email.from.address From Address Who the email is from
(avanan_quarantined) email.to.addresses To Address(es) Primary intended recipient of the
email
email.sender.address Sender Address Who actually sent the email on
behalf of the primary sender
email.recipient.addresses Recipient Address(es) Who received the email
(including CC and BCC)
|     | email.subject | Email Subject | Email subject |
| --- | ------------- | ------------- | ------------- |

Third Party Display Name Key Field Name Display Name Description
|     | url_list    | URL List              | URL(s) in the email             |
| --- | ----------- | --------------------- | ------------------------------- |
|     | domain_list | Email Links Domain(s) | Email links domain(s)           |
|     | file_list   | File List             | File name of the malicious file |
|     | name        | File Name             | File name                       |
|     | hash.md5    | Host Hash             | File hash                       |
threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
AWS GuardDuty aws_guardduty.Title Alert Title AWS GuardDuty alert title
(aws_guardduty) host_list Host IP Address(es) Private IP addresses of the
network interfaces of the
resource instance
|     | user.name | User Name | User name associated with the |
| --- | --------- | --------- | ----------------------------- |
access key details of the
resource
|     | event.threat.name | Threat Name | Threat name |
| --- | ----------------- | ----------- | ----------- |
event.severity AWS GuardDuty Severity Score AWS GuardDuty severity score
|                    | cloud.resource.type | Cloud Resource Type | Cloud resource type |
| ------------------ | ------------------- | ------------------- | ------------------- |
|                    | cloud.resource.id   | Cloud Resource ID   | Cloud resource ID   |
|                    | cloud.resource.name | Cloud Resource Name | Cloud resource name |
| Bitdefender IP     | host.name           | Host Name           | Host name           |
| (bitdefender_ip)   | host.ip             | Host IP Address     | Host IP address     |
|                    | srcip               | Source IP           | Source IP address   |
| Bitdefender Threat | event.type          | Event Type          | Event type          |
|                    | host.name           | Host Name           | Host name           |
(bitdefender_threat)
|                   | host.ip           | Host IP Address | Host IP address |
| ----------------- | ----------------- | --------------- | --------------- |
|                   | event.threat.name | Threat Type     | Threat type     |
| Bitdefender URL   | event.type        | Event Type      | Event type      |
| (bitdefender_url) | host.name         | Host Name       | Host name       |
|                   | host.ip           | Host IP Address | Host IP address |
|                   | url               | URL             | URL             |
|                   | host.name         | Host Name       | Computer name   |
Blackberry CylancePROTECT
| (cylance_protect) | host.ip      | Host IP Address | Host IP address |
| ----------------- | ------------ | --------------- | --------------- |
|                   | file_name    | File Name       | File name       |
|                   | file_path    | File Path       | File path       |
|                   | process_name | Process Name    | Process name    |
Broadcom SES event.severity Broadcom SES Severity Original severity from Broadcom
SES
(broadcom_ses)
broadcom.incident_uid Broadcom SES Incident ID Unique identifier for the
Broadcom SES incident

Third Party Display Name Key Field Name Display Name Description
| broadcom.events | Event List | User activities and process |
| --------------- | ---------- | --------------------------- |
executions detected in this
incident
| device_name       | Device Name  | Device name       |
| ----------------- | ------------ | ----------------- |
| device_ip         | Device IP    | Device IP address |
| user.name         | User Name    | User name         |
| process.pid       | Process ID   | Process ID        |
| process.file.path | Process Path | Process path      |
| process.file.name | Process Name | Process name      |
process.file.sha1 File SHA1 Hash SHA1 hash of the malicious file
process.file.md5 File MD5 Hash MD5 hash of the malicious file
process.file.sha2 File SHA256 Hash SHA256 hash of the malicious
file
| parent.pid       | Parent Process ID   | Parent process ID   |
| ---------------- | ------------------- | ------------------- |
| parent.file.path | Parent Process Path | Parent process path |
parent.file.sha1 Parent File SHA1 Hash SHA1 hash of the parent file
parent.file.sha2 Parent File SHA256 Hash SHA256 hash of the parent file
parent.file.md5 Parent File MD5 Hash MD5 hash of the parent file
| file.name | File Name | File name |
| --------- | --------- | --------- |
process_list Process Threat Intelligence Threat intelligence information
for processes
threat_indicator.labels Threat Labels Threat intelligence labels for this
process hash
threat_indicator.sources Threat Sources Threat intelligence sources that
identified this process hash
parent.threat_indicator.labels Parent Threat Labels Threat intelligence labels for the
parent process hash
parent.threat_indicator.sourc Parent Threat Sources Threat intelligence sources that
| es  |     | identified the parent process |
| --- | --- | ----------------------------- |
hash
Cato Networks cato_networks.event_sub_type Event Subtype Event subtype
| user_agent.original | User Agent | User agent |
| ------------------- | ---------- | ---------- |
(cato_networks)
| cato_networks.threat_verdict | Threat Verdict | Threat verdict              |
| ---------------------------- | -------------- | --------------------------- |
| file.name                    | File Name      | File name                   |
| file.file_hash               | File Hash      | File hash (IOC enrichment / |
VirusTotal look-ups)
| file.size | File Size | File size |
| --------- | --------- | --------- |
file.threat_indicator.labels File Hash Reputation Labels File hash reputation labels
file.threat_indicator.sources File Hash Reputation Sources File hash reputation sources
| cato_networks.domain_name | Domain Name | Domain name |
| ------------------------- | ----------- | ----------- |
| url                       | URL         | URL         |

Third Party Display Name Key Field Name Display Name Description
| host.ip                    | Host IP     | Host IP address         |
| -------------------------- | ----------- | ----------------------- |
| srcport                    | Source Port | Source port             |
| user.name                  | User Name   | User name               |
| cato_networks.rule_id      | Rule ID     | Rule ID                 |
| checkpoint_harmony.eventId | Event ID    | Unique event identifier |
Check Point Harmony Email
checkpoint_harmony.type Alert Type Alert category (phishing, spam,
(checkpoint_harmony)
graymail, shadow_it, anomaly)
checkpoint_harmony.severity Check Point Harmony Severity Check Point Harmony severity
level
checkpoint_harmony.confidenceI Confidence Indicator Threat confidence level
| ndicator |     | (malicious, graymail, detected) |
| -------- | --- | ------------------------------- |
email.sender.address Email Sender Address Normalized sender's email
address
email.recipient.addresses Email Recipient Addresses Normalized recipient email
addresses
| checkpoint_harmony.saas | SaaS Service | Source SaaS service |
| ----------------------- | ------------ | ------------------- |
checkpoint_harmony.entityLink Entity Link Portal link for threat details
CrowdStrike crowdstrike.metadata.eventType Event Type Event type
| crowdstrike.event.Name | Threat Name | Threat name |
| ---------------------- | ----------- | ----------- |
(crowdstrike_v2)
| crowdstrike.event.DomainNamesDomain Names |     | Domain names |
| ----------------------------------------- | --- | ------------ |
crowdstrike.event.SeverityName Crowdstrike Severity CrowdStrike severity
crowdstrike.event.Severity Crowdstrike Severity Score CrowdStrike severity score
| host.name        | Computer Name   | Computer name    |
| ---------------- | --------------- | ---------------- |
| hostip           | Host IP Address | Host IP address  |
| host.ip          | Host IP         | Local IP address |
| user.name        | User Name       | User name        |
| file.name        | File Name       | File name        |
| file.path        | File Path       | File path        |
| file.hash.md5    | MD5             | MD5 hash         |
| file.hash.sha256 | SHA256          | SHA256 hash      |
file.threat_indicator.labels File Hash Reputation Labels File hash reputation labels
file.threat_indicator.sources File Hash Reputation Sources File hash reputation sources
| process.command_line | Command Line        | Command line        |
| -------------------- | ------------------- | ------------------- |
| process.parent.name  | Parent Process Name | Parent process name |
| process.parent.pid   | Parent Process ID   | Parent process ID   |
process.parent.command_line Parent Command Line Parent command line
| crowdstrike.event.CompositeId   | Composite ID | Composite ID     |
| ------------------------------- | ------------ | ---------------- |
| crowdstrike.event.FalconHostLin | Falcon Link  | Falcon host link |
k
| cyberark_epm.eventType | Event Type | CyberArk event type |
| ---------------------- | ---------- | ------------------- |
CyberArk EPM

Third Party Display Name Key Field Name Display Name Description
cyberark_epm.policyName Policy Name Policy that triggered the event
(cyberark_epm)
cyberark_epm.displayName Display Name CyberArk EPM event display
name
cyberark_epm.fileName File Name Name of the file that triggered
the event
cyberark_epm.filePath File Path File path of the file that triggered
the event
|     | file.hash.sha1 | File SHA1 Hash | File SHA1 hash |
| --- | -------------- | -------------- | -------------- |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | cyberark_epm.userName | User Name | User who triggered the event |
| --- | --------------------- | --------- | ---------------------------- |
cyberark_epm.threatProtectionAct CyberArk EPM Action Action that was performed by
|     | ion |     | CyberArk EPM when the event |
| --- | --- | --- | --------------------------- |
occurred: Block or Detect
cyberark_epm.processCommand Process Command Line Process creation command line
Line
cyberark_epm.sourceProcessCo Parent Process Command Line Initiating process creation
|     | mmandLine |     | command line from which the |
| --- | --------- | --- | --------------------------- |
event was triggered
cyberark_epm.sourceProcessUse Parent Process Username Username of the initiating
|     | rname |     | process from which the event |
| --- | ----- | --- | ---------------------------- |
was triggered
cyberark_epm.evidences Evidences Evidence related to a threat
protection event
|     | accessedObject.name | Accessed Object Name | Accessed object name |
| --- | ------------------- | -------------------- | -------------------- |
|     | comment             | Comment              | Comment              |
cyberark_epm.exposedUsers Exposed Users Users who were exposed in the
threat protection event
|              | username          | User Name           | User name           |
| ------------ | ----------------- | ------------------- | ------------------- |
|              | domain            | Domain              | Domain              |
|              | accountName       | Account Name        | Account name        |
| Cybereason   | user_list         | User Names          | User names          |
| (cybereason) | file.name         | File Name           | File name           |
|              | process.name      | Process Name        | Process name        |
|              | host_list         | Host IP Address(es) | Host IP address(es) |
| Cyble        | event.threat.name | Alert Type          | Alert type          |
event.severity_str Cyble Alert Severity Level Cyble alert severity level
(cyble)
|     | cyble.status | Cyble Alert Status  | Cyble alert status           |
| --- | ------------ | ------------------- | ---------------------------- |
|     | cyble.host   | Alert Related Host  | Alert related host           |
|     | cyble.port   | Alert Related Port  | Alert related port           |
|     | cyble.ip     | Alert Related IP(s) | Alert related IP address(es) |

Third Party Display Name Key Field Name Display Name Description
|     | cyble.username         | User Name         | User name         |
| --- | ---------------------- | ----------------- | ----------------- |
|     | cyble.url              | Alert Related URL | Alert related URL |
|     | cyble.breach_source    | Breach Source     | Breach source     |
|     | cyble.breach_date      | Breach Date       | Breach date       |
|     | cyble.compromised_date | Compromised Date  | Compromised date  |
|     | cyble.expiry_date      | Expiry Date       | Expiry date       |
|     | cyble.repository_name  | Repository Name   | Repository name   |
|     | cyble.filename         | File Name         | File name         |
cyble.llm_explanation Cyble LLM Explanation Cyble Large Language Model
(LLM) explanation
cyble.true_positive Cyble Alert True Positive Flag Cyble alert true positive flag
|     | host.ip | Host IP Address | Host IP address |
| --- | ------- | --------------- | --------------- |
Cynet
| (cynet)   | event.threat.name | Threat Name    | Event threat name           |
| --------- | ----------------- | -------------- | --------------------------- |
|           | file.name         | File Name      | File name                   |
| Darktrace | event.threat.name | Alert Name     | Alert name                  |
|           | event.severity    | Severity Level | CEF numeric severity (1-10) |
(darktrace)
|     | cef.device_event_class_id | Event ID        | Event ID            |
| --- | ------------------------- | --------------- | ------------------- |
|     | host.ip                   | Host IP Address | Host IP address     |
|     | host.name                 | Host Name       | Host name           |
|     | url                       | Alert URL       | Darktrace alert URL |
|     | user.name                 | User Name       | User name           |
|     | user.id                   | User ID         | User ID/SID         |
|     | deep_instinct.msp_name    | MSP             | MSP name            |
Deep Instinct
deep_instinct.MSPName Deep Instinct MSP Name Deep Instinct MSP name
(deepinstinct)
|     | event.id           | Event ID        | Event ID                 |
| --- | ------------------ | --------------- | ------------------------ |
|     | deep_instinct.type | Type            | Deep Instinct event type |
|     | host.name          | Host Name       | Host name                |
|     | host.ip            | Host IP Address | Host IP address          |
|     | file.path          | File Path       | File path                |
|     | file.file_hash     | File Hash       | File hash                |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | deep_instinct.action | Event Action | Deep Instinct event action |
| --- | -------------------- | ------------ | -------------------------- |
deep_instinct.threat_type Deep Instinct Threat Type Deep Instinct threat type
event.severity_str Deep Instinct Severity Original Deep Instinct severity
Duo Trust Monitor duosecurity.type Duo Event Type Duo event type
| (duosecurity_trust_monitor) | user.name | User Name | User name                |
| --------------------------- | --------- | --------- | ------------------------ |
|                             | srcip     | Source IP | Access device IP address |

Third Party Display Name Key Field Name Display Name Description
duosecurity.surfaced_auth.access Access Device Location City Access device location city
_device.location.city
duosecurity.surfaced_auth.access Access Device Location State Access device location state
_device.location.state
duosecurity.surfaced_auth.access Access Device Location Country Access device location country
_device.location.country
duosecurity.surfaced_auth.access Access Device OS Access device OS
_device.os
duosecurity.surfaced_auth.access Access Device OS Version Access device OS version
_device.os_version
duosecurity.surfaced_auth.factor Authentication Factor Authentication factor
duosecurity.surfaced_auth.result Authentication Result Authentication result
duosecurity.surfaced_auth.reason Authentication Reason Authentication reason
duosecurity.surfaced_auth.auth_d Auth Device IP Authentication device IP
| evice.ip                          |                  | address          |
| --------------------------------- | ---------------- | ---------------- |
| duosecurity.surfaced_auth.applica | Application Name | Application name |
tion.name
duosecurity.surfaced_auth.applica App Integration Key Application integration key
tion.key
| duosecurity.sekey | Event ID | Duo Security event ID |
| ----------------- | -------- | --------------------- |
duosecurity.triage_event_uri Triage Event URI Duo triage event URI
| duosecurity.priority_event   | Priority Event        | Priority event        |
| ---------------------------- | --------------------- | --------------------- |
| duosecurity.priority_reasons | Priority Reasons      | Priority reasons      |
| type                         | Priority Reason Type  | Priority reason type  |
| label                        | Priority Reason Label | Priority reason label |
| duosecurity.explanations     | Explanations          | Explanations          |
| type                         | Explanations Type     | Explanations type     |
| summary                      | Explanations Summary  | Explanations summary  |
duosecurity.from_common_netblo From Common Netblock Boolean describing if this event
| ck  |     | was created from a common IP |
| --- | --- | ---------------------------- |
netblock
duosecurity.low_risk_ip Low Risk IP Boolean describing if this event
was created from an IP address
identified as a low risk IP
address
duosecurity.from_new_user From New User Boolean describing if this event
was created for a new user
duosecurity.triaged_as_interesting Triaged as Interesting Triaged as interesting
| duosecurity.state | Event State | Event state |
| ----------------- | ----------- | ----------- |
duosecurity.bypass_status_enabl Bypass Status Enabled Bypass status enabled
| ed                     |            | timestamp  |
| ---------------------- | ---------- | ---------- |
| duosecurity.enabled_by | Enabled By | Enabled by |

Third Party Display Name Key Field Name Display Name Description
|     | duosecurity.enabled_for | Enabled For | Enabled for                |
| --- | ----------------------- | ----------- | -------------------------- |
|     | eset.Tenant             | ESET Tenant | ESET Cloud Office Security |
ESET Cloud Office Security
tenant name
(eset_cloud_office_security)
eset.OperationId ESET Operation ID ESET Cloud Office Security
operation ID
|     | eset.ScanResult | ESET Threat Type | ESET Cloud Office Security |
| --- | --------------- | ---------------- | -------------------------- |
threat type
|     | eset.Action | ESET Event Action | ESET Cloud Office Security |
| --- | ----------- | ----------------- | -------------------------- |
event action
|     | file.name | File Name | File name |
| --- | --------- | --------- | --------- |
file.hash.sha1 File SHA1 Hash SHA1 hash of the malicious file
|     | srcip              | Source IP      | Email sender source IP address |
| --- | ------------------ | -------------- | ------------------------------ |
|     | email.from.address | Sender Address | Sender address                 |
email.to.addresses Recipient Address(es) Recipient address(es)
|     | email.subject | Email Subject | Email subject |
| --- | ------------- | ------------- | ------------- |
ESET Protect (Filtered Websites srcip Source IP Source IP address
| Event) | dstip        | Destination IP       | Destination IP address |
| ------ | ------------ | -------------------- | ---------------------- |
|        | eset.rule_id | ESET Protect Rule ID | ESET Protect rule ID   |
(eset_protect_filtered_websites_
event) eset.event_type ESET Protect Event Type ESET Protect event type
event.severity_str ESET Protect Event Severity ESET Protect event severity
event.threat.name ESET Protect Threat Name ESET Protect threat name
|     | process.executable | Process Path   | Process path   |
| --- | ------------------ | -------------- | -------------- |
|     | user.name          | User Name      | User name      |
|     | host.name          | Host Name      | Host name      |
|     | file.hash.sha1     | File SHA1 Hash | File SHA1 hash |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | srcip | Source IP | Source IP address |
| --- | ----- | --------- | ----------------- |
ESET Protect (Firewall
Aggregated Event) dstip Destination IP Destination IP address
eset.event_type ESET Protect Event Type ESET Protect event type
(eset_protect_firewall_aggregate
d_event) event.severity_str ESET Protect Event Severity ESET Protect event severity
event.threat.name ESET Protect Threat Name ESET Protect threat name
|                            | process.executable | Process Path | Process path    |
| -------------------------- | ------------------ | ------------ | --------------- |
|                            | user.name          | User Name    | User name       |
| ESET Protect (ESET Inspect | host.ip            | Host IP      | Host IP address |
| Alert)                     | host.name          | Host Name    | Host name       |
eset.event_type ESET Protect Event Type ESET Protect event type
(eset_protect_inspect_alert)
|     | eset.rulename      | ESET Protect Rule Name | ESET Protect rule name |
| --- | ------------------ | ---------------------- | ---------------------- |
|     | process.executable | Process Path           | Process path           |
|     | user.name          | User Name              | User name              |

Third Party Display Name Key Field Name Display Name Description
event.severity_str ESET Protect Event Severity ESET Protect event severity
eset.eiconsolelink ESET Protect Console Link ESET Protect console link
eset.source_uuid ESET Protect Source UUID ESET Protect source UUID
| file.hash.sha1 | File SHA1 Hash | File SHA1 hash |
| -------------- | -------------- | -------------- |
file.threat_indicator.labels File Hash Reputation Label(s) File Hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File Hash reputation source(s)
| host.ip | Host IP | Host IP address |
| ------- | ------- | --------------- |
ESET Protect (Threat Event)
| host.name | Host Name | Host name |
| --------- | --------- | --------- |
(eset_protect_threat_event)
eset.event_type ESET Protect Event Type ESET Protect event type
| process.executable | Process Path | Process path |
| ------------------ | ------------ | ------------ |
| user.name          | User Name    | User name    |
event.severity_str ESET Protect Event Severity ESET Protect event severity
eset.source_uuid ESET Protect Source UUID ESET Protect source UUID
| file.hash.sha1 | File SHA1 Hash | File SHA1 hash |
| -------------- | -------------- | -------------- |
file.threat_indicator.labels File Hash Reputation Label(s) File Hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File Hash reputation source(s)
ExtraHop Reveal(x) 360 extrahop.id Detection ID ExtraHop detection ID
| extrahop.title | Detection Title | Detection title |
| -------------- | --------------- | --------------- |
(extrahop_reveal_x_360)
| extrahop.type        | Detection Type | Detection type        |
| -------------------- | -------------- | --------------------- |
| extrahop.risk_score  | Risk Score     | Risk score (0-99)     |
| extrahop.categories  | Categories     | Detection categories  |
| extrahop.description | Description    | Detection description |
| srcip                | Source IP      | Source IP address     |
(offender/initiator)
| srcip_host | Source Host | Source hostname |
| ---------- | ----------- | --------------- |
(offender/initiator)
| dstip | Destination IP | Destination IP address |
| ----- | -------------- | ---------------------- |
(victim/target)
| dstip_host | Destination Host | Destination hostname |
| ---------- | ---------------- | -------------------- |
(victim/target)
extrahop.participants Participants Participants (offenders and
victims)
| role                  | Role         | Participant role      |
| --------------------- | ------------ | --------------------- |
| endpoint              | Endpoint     | Endpoint type         |
| hostname              | Hostname     | Hostname              |
| object_value          | IP/Value     | IP address or value   |
| external              | External     | External entity       |
| extrahop.appliance_id | Appliance ID | ExtraHop appliance ID |
| extrahop.status       | Status       | Detection status      |
| extrahop.resolution   | Resolution   | Detection resolution  |

Third Party Display Name Key Field Name Display Name Description
extrahop.recommended Recommended Recommended for investigation
| extrahop.url       | ExtraHop Link | ExtraHop detection link |
| ------------------ | ------------- | ----------------------- |
| fortinet_edr.rules | Rules         | Rules                   |
Fortinet EDR
| process.name | Process Name | Process name |
| ------------ | ------------ | ------------ |
(fortinet_edr)
| process.executable | Process Path | Process path |
| ------------------ | ------------ | ------------ |
| user.name          | Logged User  | Logged user  |
fortinet_lacework.START_TIME Start Time Time and date when the hourly
Fortinet Lacework
aggregation time period starts
(laceworkt) fortinet_lacework.END_TIME End Time Time and date when the hourly
aggregation time period ends
| event.threat.name | Alert Type | Type of the alert |
| ----------------- | ---------- | ----------------- |
fortinet_lacework.EVENT_ID Event ID Unique identifier generated for
this event by Lacework
FortiCNAPP
fortinet_lacework.EVENT_MODE Event Model Data model used for generating
| L   |     | the alert |
| --- | --- | --------- |
fortinet_lacework.EVENT_ACTOR Event Actor Event actor that categorizes the
type of an alert such as
application, process, files, etc
| fortinet_lacework.ENTITY_MAP.U | User(s) | User(s) |
| ------------------------------ | ------- | ------- |
ser
| KEY.username                   | User Name          | User's name        |
| ------------------------------ | ------------------ | ------------------ |
| PROPS.hostname                 | Host Name          | User's host name   |
| fortinet_lacework.ENTITY_MAP.C | CloudTrail User(s) | CloudTrail user(s) |
T_User
| KEY.username  | User Name    | User's name    |
| ------------- | ------------ | -------------- |
| PROPS.account | User Account | User's account |
fortinet_lacework.ENTITY_MAP.S Source IP Address(es) Source IP address(es)
ourceIpAddress
| KEY.ip_addr                     | IP Address   | IP address   |
| ------------------------------- | ------------ | ------------ |
| fortinet_lacework.ENTITY_MAP.Fi | File Path(s) | File path(s) |
leExePath
| KEY.exe_path | File Path  | File path            |
| ------------ | ---------- | -------------------- |
| KEY.mid      | Machine ID | Lacework FortiCNAPP- |
generated machine identifier
where the file was found
| fortinet_lacework.ENTITY_MAP.P | Process(es) | Process(es) |
| ------------------------------ | ----------- | ----------- |
rocess
| PROPS.hostname | Host Name    | Host name                        |
| -------------- | ------------ | -------------------------------- |
| PROPS.cmdline  | Command Line | Command line                     |
| PROPS.pid      | PID          | Unique identifier of the process |

Third Party Display Name Key Field Name Display Name Description
|     | fortinet_lacework.ENTITY_MAP.M | Machine(s) | Machine(s) |
| --- | ------------------------------ | ---------- | ---------- |
achine
|                        | PROPS.hostname         | Host Name    | Host name    |
| ---------------------- | ---------------------- | ------------ | ------------ |
|                        | PROPS.internal_ip_addr | IP Address   | IP address   |
|                        | source                 | Alert Source |              |
| Google Workspace Alert |                        |              | Alert source |
(google_workspace_alert)
|     | type      | Alert Type       | Alert type                     |
| --- | --------- | ---------------- | ------------------------------ |
|     | rule.name | Rule Name        | Alert rule name                |
|     | host.ip   | Login IP Address | IP address associated with the |
warning event
|     | data.email | Data Email | Email of the user to which this |
| --- | ---------- | ---------- | ------------------------------- |
event belongs
securityInvestigationToolLink Investigation Tool Link Google Workspace security
investigation tool link
|     | user.id            | User ID            | User ID            |
| --- | ------------------ | ------------------ | ------------------ |
|     | user.name          | User Name          | User name          |
|     | email.from.address | Email From Address | Email from address |
email.recipient.addresses Email Recipient Addresses Email recipient addresses
|     | group_ib.event_type_title | Threat Category | Threat category |
| --- | ------------------------- | --------------- | --------------- |
Group IB
|     | group_ib.severity | Severity Level | Severity level (1-5) |
| --- | ----------------- | -------------- | -------------------- |
(group_ib)
|     | group_ib.message | Alert Message | Alert message |
| --- | ---------------- | ------------- | ------------- |
group_ib.integration_system Detection Source Detection source system
|     | group_ib.matchers            | Detection Rule IDs | Detection rule IDs  |
| --- | ---------------------------- | ------------------ | ------------------- |
|     | group_ib.target.ip_addresses | Target IP          | Target IP addresses |
group_ib.target.mac_addresses Target MAC Target MAC addresses
|     | group_ib.target.asset_ids | Target Asset IDs | Target asset IDs       |
| --- | ------------------------- | ---------------- | ---------------------- |
|     | group_ib.host             | Host             | Primary host           |
|     | group_ib.action           | Action           | Detection action taken |
|     | group_ib.status           | Status           | Alert status           |
|     | group_ib.resolved         | Resolved         | Resolution state       |
group_ib.false_positive False Positive False positive indication
|         | group_ib.attribution.cve     | CVE                 | CVE identification   |
| ------- | ---------------------------- | ------------------- | -------------------- |
|         | group_ib.attribution.malware | Malware Attribution | Attributed malware   |
|         | group_ib.related_info.ips    | Related IPs         | Related IP addresses |
|         | group_ib.ioc.event.domains   | IOC Domains         | IOC domains          |
| Halcyon | event.threat.name            | Threat Name         | Threat name          |
|         | halcyon.alertType            | Vendor Alert Type   | Vendor alert type    |
(halcyon)
|     | halcyon.action                    | Action           | Response action taken |
| --- | --------------------------------- | ---------------- | --------------------- |
|     | halcyon.summary.artifact.filePath | Artifact Path    | Artifact path         |
|     | file.hash.sha256                  | File SHA256 Hash | File SHA256 hash      |

Third Party Display Name Key Field Name Display Name Description
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | process.pid          | Process ID          | Process ID           |
| --- | -------------------- | ------------------- | -------------------- |
|     | process.command_line | Command Line        | Process command line |
|     | process.executable   | Process Executable  | Process executable   |
|     | process.parent.pid   | Parent Process ID   | Parent process ID    |
|     | process.hash.sha256  | Process SHA256 Hash | Process SHA256 hash  |
process.threat_indicator.labels Process Hash Reputation Process hash reputation label(s)
Label(s)
process.threat_indicator.sources Process Hash Reputation Process hash reputation
|     |              | Source(s)    | source(s)            |
| --- | ------------ | ------------ | -------------------- |
|     | process_list | Process List | Process list         |
|     | executable   | Executable   | Process executable   |
|     | command_line | Command Line | Process command line |
|     | pid          | PID          | Process ID           |
|     | parent.pid   | Parent PID   | Parent process ID    |
|     | hash.sha256  | SHA256       | Process SHA256 hash  |
threat_indicator.labels Reputation Label(s) Process hash reputation label(s)
threat_indicator.sources Reputation Source(s) Process hash reputation
source(s)
| HoxHunt | hoxhunt.severity | Alert Severity | Alert severity |
| ------- | ---------------- | -------------- | -------------- |
hoxhunt.classification Automated Threat Classification Automated threat classification
(hoxhunt)
hoxhunt.prediction.mlopsIocEmail HoxHunt Maliciousness Maliciousness prediction score
|     | MaliciousnessProbability | Prediction | according to HoxHunt IoC |
| --- | ------------------------ | ---------- | ------------------------ |
model
|     | email.subject      | Email Subject          | Email subject          |
| --- | ------------------ | ---------------------- | ---------------------- |
|     | email.from.address | From Address           | From address           |
|     | email.to.addresses | To Address(es)         | To address(es)         |
|     | hoxhunt.email.date | Email Sent Time        | Email sent time        |
|     | file_list          | Email Attachments List | Email attachments list |
|     | name               | File Name              | File name              |
|     | hash.sha256        | File Hash              | File hash              |
threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | url_list | URL List | URL(s) in the email |
| --- | -------- | -------- | ------------------- |
Huntress Incident huntress.organization_name Organization Name Huntress organization name
(huntress_incident) huntress.security_products Originating Security Products Originating security products
huntress.incident_report_url Incident Report URL Huntress incident report URL
|     | huntress.user_url | User URL | Huntress user URL |
| --- | ----------------- | -------- | ----------------- |
|     | huntress.host_url | Host URL | Huntress host URL |

Third Party Display Name Key Field Name Display Name Description
|                      | host.name                  | Host Name                   | Host name                      |
| -------------------- | -------------------------- | --------------------------- | ------------------------------ |
|                      | host.ip                    | Host IP                     | Host IP address                |
|                      | user_name                  | User Name                   | User name                      |
|                      | event.threat_list          | Threat List                 | Huntress event threat list     |
|                      | name                       | Threat Name                 | Huntress event threat name     |
|                      | severity_str               | Threat Severity             | Huntress event threat severity |
| HYAS Protect (Block) | srcip                      | Client IP                   | Client IP address              |
| (hyas_protect_block) | dns.question.name          | Domain                      | Domain                         |
|                      | hyas_protect.registrar     | Domain Registrar            | Domain registrar               |
|                      | domain_creation            | Domain Creation Date        | Domain creation date           |
|                      | hyas_protect.verdictStatus | HYAS Protect Verdict Status |                                |
HYAS Protect verdict status:
Allow: allow
Block: block
Highly Suspicious: bad
Watch Engine: suspicious
hyas_protect.reason.type HYAS Protect Reason Type HYAS Protect reason type
hyas_protect.reason.lists HYAS Protect Reason Lists HYAS Protect reason lists
|     | id              | ID             | Reason ID                 |
| --- | --------------- | -------------- | ------------------------- |
|     | name            | Name           | Reason name               |
|     | datatype        | Datatype       | Reason data type          |
|     | dns.resolved_ip | Resolved IP(s) | Resolved IP address(es)   |
|     | dns.answers     | DNS Answer(s)  | DNS answer(s)             |
|     | name            | Domain name    | Domain name to which this |
resource record pertains. If a
chain of CNAME is being
resolved, each answer’s name
should be the one that
corresponds with the answer’s
data.
|     | type | Data Type | Type of data contained in this |
| --- | ---- | --------- | ------------------------------ |
resource record
|     | data | Data | Data in this resource record |
| --- | ---- | ---- | ---------------------------- |
HYAS Protect (Watch Engine) srcip Client IP Client IP address
| (hyas_protect_suspicious) | dns.question.name          | Domain                      | Domain               |
| ------------------------- | -------------------------- | --------------------------- | -------------------- |
|                           | hyas_protect.registrar     | Domain Registrar            | Domain registrar     |
|                           | domain_creation            | Domain Creation Date        | Domain creation date |
|                           | hyas_protect.verdictStatus | HYAS Protect Verdict Status |                      |
HYAS Protect verdict status:
Allow: allow
Block: block
Highly Suspicious: bad
Watch Engine: suspicious

Third Party Display Name Key Field Name Display Name Description
hyas_protect.reason.type HYAS Protect Reason Type HYAS Protect reason type
hyas_protect.reason.lists HYAS Protect Reason Lists HYAS Protect reason lists
|     | id              | ID             | Reason ID                 |
| --- | --------------- | -------------- | ------------------------- |
|     | name            | Name           | Reason name               |
|     | datatype        | Datatype       | Reason data type          |
|     | dns.resolved_ip | Resolved IP(s) | Resolved IP address(es)   |
|     | dns.answers     | DNS Answer(s)  | DNS answer(s)             |
|     | name            | Domain name    | Domain name to which this |
resource record pertains. If a
chain of CNAME is being
resolved, each answer’s name
should be the one that
corresponds with the answer’s
data.
|     | type | Data Type | Type of data contained in this |
| --- | ---- | --------- | ------------------------------ |
resource record
|                      | data              | Data      | Data in this resource record |
| -------------------- | ----------------- | --------- | ---------------------------- |
| HYAS Protect (Highly | srcip             | Client IP | Client IP address            |
| Suspicious)          | dns.question.name | Domain    | Domain                       |
(hyas_protect_suspicious) hyas_protect.registrar Domain Registrar Domain registrar
|     | domain_creation            | Domain Creation Date | Domain creation date |
| --- | -------------------------- | -------------------- | -------------------- |
|     | hyas_protect.verdictStatus | HYAS Verdict Status  |                      |
HYAS Protect verdict status:
Allow: allow
Block: block
Highly Suspicious: bad
Watch Engine: suspicious
hyas_protect.reason.type HYAS Reason Type HYAS Protect reason type
hyas_protect.reason.lists HYAS Protect Reason Lists HYAS Protect reason lists
|     | id              | ID             | Reason ID                 |
| --- | --------------- | -------------- | ------------------------- |
|     | name            | Name           | Reason name               |
|     | datatype        | Datatype       | Reason data type          |
|     | dns.resolved_ip | Resolved IP(s) | Resolved IP address(es)   |
|     | dns.answers     | DNS Answer(s)  | DNS answer(s)             |
|     | name            | Domain name    | Domain name to which this |
resource record pertains. If a
chain of CNAME is being
resolved, each answer’s name
should be the one that
corresponds with the answer’s
data.
|     | type | Data Type | Type of data contained in this |
| --- | ---- | --------- | ------------------------------ |
resource record

Third Party Display Name Key Field Name Display Name Description
| data       | Data        | Data in this resource record |
| ---------- | ----------- | ---------------------------- |
| srcip_host | Source Host | Name of the workstation      |
LimaCharlie
| srcip | Source IP | IP address of the source |
| ----- | --------- | ------------------------ |
(limacharlie_alert)
| srcport                         | Source IP Port | Port of the source IP |
| ------------------------------- | -------------- | --------------------- |
| host.name                       | Host Name      | Host name             |
| host.ip                         | Host IP        | Host IP address       |
| limacharlie.detect.event.ACTION | Action         | Event action          |
| limacharlie.detect.event.REGIST | Registry Key   | Registry key          |
RY_KEY
| limacharlie.detect.event.REGIST | Registry Value | Registry value |
| ------------------------------- | -------------- | -------------- |
RY_VALUE
| process.name | Process File Path | File path of the process |
| ------------ | ----------------- | ------------------------ |
process.hash.sha256 Process File Hash File hash of the process
process.threat_indicator.labels Process File Hash Reputation Process file hash reputation
|     | Label(s) | label(s) |
| --- | -------- | -------- |
process.threat_indicator.sources Process File Hash Reputation Process file hash reputation
|     | Source(s) | source(s) |
| --- | --------- | --------- |
event.severity_str LimaCharlie Severity Original severity of the
LimaCharlie alert
| limacharlie.detect.event.EVENT. | SID | SID of the target user |
| ------------------------------- | --- | ---------------------- |
EventData.TargetUserSid
| file.path        | File Path | Path of the file        |
| ---------------- | --------- | ----------------------- |
| file.hash.sha256 | File Hash | SHA256 hash of the file |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
process.command_line Process Command Line Command line of the process
| process.pid                     | Process ID | Process ID |
| ------------------------------- | ---------- | ---------- |
| user.name                       | User Name  | User name  |
| limacharlie.detect.event.EVENT. | Event ID   | Event ID   |
System.EventID
| limacharlie.detect.event.EVENT. | Logon Type | Logon type |
| ------------------------------- | ---------- | ---------- |
EventData.LogonType
| limacharlie.detect.event.EVENT. | Process Name | Process name |
| ------------------------------- | ------------ | ------------ |
EventData.ProcessName
limacharlie.detect.event.PAREN Parent Process File Path File path of the parent process
T.FILE_PATH
limacharlie.detect.event.PAREN Parent Process File Hash File hash of the parent process
T.HASH
process.parent.threat_indicator.l Parent Process File Hash Reputation label(s) of the parent
| abels | Reputation Label(s) | process file hash |
| ----- | ------------------- | ----------------- |
process.parent.threat_indicator.s Parent Process File Hash Reputation source(s) of the
| ources | Reputation Source(s) | parent process file hash |
| ------ | -------------------- | ------------------------ |

Third Party Display Name Key Field Name Display Name Description
process.parent.command_line Parent Process Command Line Command line of the parent
process
| process.parent.pid | Parent Process ID | Parent process ID |
| ------------------ | ----------------- | ----------------- |
limacharlie.detect.event.PAREN Parent User Name User name of the parent process
T.USER_NAME
limacharlie.link LimaCharlie Alert Link LimaCharlie alert link
limacharlie.source_rule Source Rule Source rule that LimaCharlie
used to generate the alert
limacharlie.detect_mtd.reference Rule References References of the rule
s
| event.severity_str | Severity | Alert severity |
| ------------------ | -------- | -------------- |
Microsoft App Governance
(Graph Security API) event.threat.name Threat Name Threat name
(microsoft_app_governance_gra microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
gory
ph_security_api)
microsoft_graph_security_api.inve Investigation State Investigation state
stigationState
| microsoft_graph_security_api.dete | Determination | Determination |
| --------------------------------- | ------------- | ------------- |
rmination
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type      | Evidence type       |
| --------------------------- | --------- | ------------------- |
| verdict                     | Verdict   | Verdict             |
| displayName                 | App Name  | App display name    |
| appId                       | App ID    | Application ID      |
| publisher                   | Publisher | Publisher           |
| userAccount.userPrincipalNa | User      | User principal name |
me
| roles | Roles | Roles |
| ----- | ----- | ----- |
microsoft_graph_security_api.addi Consent Scopes OAuth consent scopes
tionalData.appConsentScopes
| microsoft_graph_security_api.addi | Reply URL | Reply URL |
| --------------------------------- | --------- | --------- |
tionalData.replyUrl
| user.name          | User Name | User name      |
| ------------------ | --------- | -------------- |
| event.severity_str | Severity  | Alert severity |
Microsoft Data Loss Prevention
(Graph Security API) event.threat.name Threat Name Threat name
(microsoft_data_loss_prevention microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
_graph_security_api) gory

Third Party Display Name Key Field Name Display Name Description
| microsoft_graph_security_api.addi | DLP Policy | DLP policy name |
| --------------------------------- | ---------- | --------------- |
tionalData.AlertPolicyTitle
| microsoft_graph_security_api.addi | DLP Alert Type | DLP alert type |
| --------------------------------- | -------------- | -------------- |
tionalData.DlpAlertType
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type    | Evidence type       |
| --------------------------- | ------- | ------------------- |
| verdict                     | Verdict | Verdict             |
| userAccount.userPrincipalNa | User    | User principal name |
me
| userAccount.displayName | Display Name      | User display name      |
| ----------------------- | ----------------- | ---------------------- |
| fileDetails.fileName    | File Name         | File name              |
| fileDetails.filePath    | File Path         | File path              |
| displayName             | Application       | Cloud application name |
| user.name               | User Name         | User name              |
| file.name               | File Name         | File name              |
| file.path               | File Path         | File path              |
| cloud.resource.name     | Cloud Application | Cloud application name |
| host.name               | Host Name         | Host name              |
Microsoft Defender ATP
| host.ip | Host IP Address | Host IP address |
| ------- | --------------- | --------------- |
(ms_defender_atp)
| user.name                         | User Name    | User name      |
| --------------------------------- | ------------ | -------------- |
| user.domain                       | User Domain  | User domain    |
| threat                            | Threat Name  | Threat name    |
| file_list                         | File List    | File list      |
| process_list                      | Process List | Process list   |
| event.severity_str                | Severity     | Alert severity |
| event.threat.name                 | Threat Name  | Threat name    |
| microsoft_graph_security_api.cate | Category     | Alert category |
gory
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.dete | Detection Source | Detection source |
| --------------------------------- | ---------------- | ---------------- |
ctionSource
microsoft_graph_security_api.thre Threat Display Name" }, Threat display name
atDisplayName
microsoft_graph_security_api.thre Threat Family Threat family name
atFamilyName

Third Party Display Name Key Field Name Display Name Description
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type        | Evidence type       |
| --------------------------- | ----------- | ------------------- |
| verdict                     | Verdict     | Verdict             |
| deviceDnsName               | Device Name | Device DNS name     |
| hostName                    | Host Name   | Host name           |
| osPlatform                  | OS Platform | OS platform         |
| lastIpAddress               | IP Address  | Last IP address     |
| fileDetails.fileName        | File Name   | File name           |
| fileDetails.filePath        | File Path   | File path           |
| fileDetails.sha256          | SHA256      | SHA256 hash         |
| fileDetails.md5             | MD5         | MD5 hash            |
| fileDetails.sha1            | SHA1        | SHA1 hash           |
| userAccount.userPrincipalNa | User Name   | User principal name |
me
| userAccount.azureAdUserId | User ID      | Microsoft Entra ID user ID |
| ------------------------- | ------------ | -------------------------- |
| url                       | URL          | URL                        |
| ipAddress                 | IP Address   | IP address                 |
| processCommandLine        | Command Line | Process command line       |
| processId                 | Process ID   | Process ID                 |
| parentProcessId           | Parent PID   | Parent process ID          |
| event.severity_str        | Severity     | Alert severity             |
Microsoft Entra ID Protection
(Graph Security API) event.threat.name Threat Name Threat name
(azure_ad_identity_protection_g microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
gory
raph_security_api)
| microsoft_graph_security_api.addi | Risk Type | Risk event type |
| --------------------------------- | --------- | --------------- |
tionalData.riskEventType
| microsoft_graph_security_api.addi | Risk Level | Risk level |
| --------------------------------- | ---------- | ---------- |
tionalData.riskLevel
| microsoft_graph_security_api.addi | Risk State | Risk state |
| --------------------------------- | ---------- | ---------- |
tionalData.riskState
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type | Type | Evidence type |
| ----------- | ---- | ------------- |

Third Party Display Name Key Field Name Display Name Description
| verdict                     | Verdict | Verdict             |
| --------------------------- | ------- | ------------------- |
| userAccount.userPrincipalNa | User    | User principal name |
me
| userAccount.accountName  | Account    | Account Name      |
| ------------------------ | ---------- | ----------------- |
| ipAddress                | IP Address | IP address        |
| location.city            | City       | City              |
| location.countryOrRegion | Country    | Country           |
| user.name                | User Name  | User name         |
| srcip                    | Source IP  | Source IP address |
| userDisplayName          | User Name  | User name         |
Microsoft Entra RiskDetection
(formerly Azure Active Directory) ipAddress Host IP Address Host IP address
(azure_ad_risk_detection) riskEventType Microsoft Entra Risk Event Type Microsoft Entra risk event type
riskLevel Microsoft Entra Risk Level Microsoft Entra risk level
microsoft_defender_cloud.AlertUri Microsoft Defender for Cloud Microsoft Defender for Cloud
Microsoft Defender for Cloud
|     | Alert URI | alert URI |
| --- | --------- | --------- |
(microsoft_defender_cloud)
event.severity_str Microsoft Defender for Cloud Original severity from Microsoft
|                   | Severity    | Defender for Cloud |
| ----------------- | ----------- | ------------------ |
| event.threat.name | Threat Name | Threat name        |
microsoft_defender_cloud.AlertDis Microsoft Defender for Cloud Microsoft Defender for Cloud
| playName            | Alert Name          | alert name          |
| ------------------- | ------------------- | ------------------- |
| cloud.resource.name | Cloud Resource Name | Cloud resource name |
| cloud.resource.type | Cloud Resource Type | Cloud resource type |
| cloud.resource.id   | Cloud Resource ID   | Cloud resource ID   |
| srcip_list          | Source IP List      | Source IP list      |
| srcip               | Source IP           | Source IP address   |
| user.name           | User Name           | User name           |
| host.name           | Host Name           | Host name           |
| host.ip             | Host IP Address     | Host IP address     |
| file.name           | File Name           | File name           |
| file.path           | File Path           | File path           |
| file.hash.md5       | File MD5 Hash       | File MD5 hash       |
| file.hash.sha1      | File SHA1 Hash      | File SHA1 hash      |
| file.hash.sha256    | File SHA256 Hash    | File SHA256 hash    |
| process.executable  | Process Executable  | Process executable  |
| process.id          | Process ID          | Process ID          |
process.command_line Process Command Line Process command line
| process.parent.name | Parent Process Name | Parent process name |
| ------------------- | ------------------- | ------------------- |
process.parent.executable Parent Process Executable Parent process executable
| process.parent.id | Parent Process ID | Parent process ID |
| ----------------- | ----------------- | ----------------- |
process.parent.command_line Parent Process Command Line Parent process command line

Third Party Display Name Key Field Name Display Name Description
microsoft_defender_cloud.Extend Extended Properties Extended properties
edProperties
azure_security_center.ExtendedPr Extended Properties Extended properties
operties
microsoft_defender_cloud.Remedi Remediation Steps Remediation steps
ationSteps
azure_security_center.Remediatio Remediation Steps Remediation steps
nSteps
| microsoft_graph_security_api.cate | Category | Alert category |
| --------------------------------- | -------- | -------------- |
gory
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.dete | Detection Source | Detection source |
| --------------------------------- | ---------------- | ---------------- |
ctionSource
microsoft_graph_security_api.thre Threat Display Name Threat display name
atDisplayName
microsoft_graph_security_api.thre Threat Family Threat family name
atFamilyName
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type          | Type          | Evidence type     |
| -------------------- | ------------- | ----------------- |
| verdict              | Verdict       | Verdict           |
| azureResourceId      | Resource ID   | Azure resource ID |
| resourceName         | Resource Name | Resource name     |
| resourceType         | Resource Type | Resource type     |
| ipAddress            | IP Address    | IP address        |
| location.countryName | Country       | Country name      |
| location.city        | City          | City              |
| event.severity_str   | Severity      | Alert severity    |
Microsoft Defender for Cloud
(Graph Security API) event.threat.name Threat Name Threat name
(microsoft_defender_for_cloud_ microsoft_graph_security_api.cate Category Alert category
gory
graph_security_api)
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.dete | Detection Source | Detection source |
| --------------------------------- | ---------------- | ---------------- |
ctionSource
microsoft_graph_security_api.thre Threat Display Name Threat display name
atDisplayName

Third Party Display Name Key Field Name Display Name Description
microsoft_graph_security_api.thre Threat Family Threat family name
atFamilyName
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type          | Type          | Evidence type     |
| -------------------- | ------------- | ----------------- |
| verdict              | Verdict       | Verdict           |
| azureResourceId      | Resource ID   | Azure resource ID |
| resourceName         | Resource Name | Resource name     |
| resourceType         | Resource Type | Resource type     |
| ipAddress            | IP Address    | IP address        |
| location.countryName | Country       | Country name      |
| location.city        | City          | City              |
microsoft_defender_cloud.AlertUri Microsoft Defender for Cloud Microsoft Defender for Cloud
|     | Alert URI | alert URI |
| --- | --------- | --------- |
microsoft_defender_cloud.AlertDis Microsoft Defender for Cloud Microsoft Defender for Cloud
| playName            | Alert Name          | alert name             |
| ------------------- | ------------------- | ---------------------- |
| cloud.resource.name | Cloud Resource Name | Cloud resource name    |
| cloud.resource.type | Cloud Resource Type | Cloud resource type    |
| cloud.resource.id   | Cloud Resource ID   | Cloud resource ID      |
| srcip_list          | Source IP List      | Source IP address list |
| srcip               | Source IP           | Source IP address      |
| user.name           | User Name           | User name              |
| host.name           | Host Name           | Host name              |
| host.ip             | Host IP Address     | Host IP address        |
| file.name           | File Name           | File name              |
| file.path           | File Path           | File path              |
| file.hash.md5       | File MD5 Hash       | File MD5 hash          |
| file.hash.sha1      | File SHA1 Hash      | File SHA1 hash         |
| file.hash.sha256    | File SHA256 Hash    | File SHA256 hash       |
| process.executable  | Process Executable  | Process executable     |
| process.id          | Process ID          | Process ID             |
process.command_line Process Command Line Process command line
| process.parent.name | Parent Process Name | Parent process name |
| ------------------- | ------------------- | ------------------- |
process.parent.executable Parent Process Executable Parent process executable
| process.parent.id | Parent Process ID | Parent process ID |
| ----------------- | ----------------- | ----------------- |
process.parent.command_line Parent Process Command Line Parent process command line

Third Party Display Name Key Field Name Display Name Description
microsoft_defender_cloud.Extend Extended Properties Extended properties
edProperties
azure_security_center.ExtendedPr Extended Properties Extended properties
operties
microsoft_defender_cloud.Remedi Remediation Steps Remediation steps
ationSteps
azure_security_center.Remediatio Remediation Steps Remediation steps
nSteps
microsoft_defender_for_cloud_ap Microsoft Defender for Cloud Microsoft Defender for Cloud
Microsoft Defender for Cloud
| Apps | ps.URL            | Apps URL    | Apps URL    |
| ---- | ----------------- | ----------- | ----------- |
|      | event.threat.name | Threat Name | Threat name |
(ms_defender_for_cloud_apps)
|     | event.threat_list | Risk category | Threat list                  |
| --- | ----------------- | ------------- | ---------------------------- |
|     | name              | Risk category | Microsoft Defender for Cloud |
Apps risk category
event.severity_str Microsoft Defender for Cloud Original severity value from
|     |     | Apps Severity | Microsoft Defender for Cloud |
| --- | --- | ------------- | ---------------------------- |
Apps
microsoft_defender_for_cloud_ap Preview Alerts that have been recently
|     | ps.isPreview |         | released as GA             |
| --- | ------------ | ------- | -------------------------- |
|     | user.id      | User ID | User ID of entity that was |
involved in this alert
|     | user.name | Username | Username of entity that was |
| --- | --------- | -------- | --------------------------- |
involved in this alert
|     | srcip | Source IP Address | Source IP address of attack that |
| --- | ----- | ----------------- | -------------------------------- |
was involved in this alert
|     | srcip_host | Source Host | Name of the source workstation |
| --- | ---------- | ----------- | ------------------------------ |
involved in this alert
|     | dstip_host | Destination Host | Name of the destination |
| --- | ---------- | ---------------- | ----------------------- |
workstation involved in this alert
|     | observables | Entities | List of observables related to |
| --- | ----------- | -------- | ------------------------------ |
the alert
|     | name                              | Entity Name | Entity name    |
| --- | --------------------------------- | ----------- | -------------- |
|     | type                              | Entity Yype | Entity type    |
|     | id                                | Entity ID   | Entity ID      |
|     | microsoft_graph_security_api.cate | Category    | Alert category |
gory
|     | microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --- | --------------------------------- | ----------- | ----------- |
ctorId
|     | microsoft_graph_security_api.alert | Policy ID | Alert policy ID |
| --- | ---------------------------------- | --------- | --------------- |
PolicyId
|     | microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| --- | ---------------------------------- | --------- | ------------- |
WebUrl

Third Party Display Name Key Field Name Display Name Description
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type          | Evidence type       |
| --------------------------- | ------------- | ------------------- |
| displayName                 | Display Name  | Display name        |
| instanceName                | Instance Name | Instance name       |
| saasAppId                   | App ID        | SaaS app ID         |
| verdict                     | Verdict       | Verdict             |
| userAccount.userPrincipalNa | User Name     | User principal name |
me
| userAccount.azureAdUserId | User ID             | Microsoft Entra ID user ID |
| ------------------------- | ------------------- | -------------------------- |
| ipAddress                 | IP Address          | IP address                 |
| remediationStatus         | Remediation Status  | Remediation status         |
| remediationStatusDetails  | Remediation Details | Remediation details        |
| detailedRoles             | Detailed Roles      | Detailed roles             |
| event.severity_str        | Severity            | Alert severity             |
Microsoft Defender for Cloud
Apps (Graph Security API) event.threat.name Threat Name Threat name
(microsoft_defender_for_cloud_ microsoft_graph_security_api.cate Category Alert category
gory
apps_graph_security_api)
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.alert | Policy ID | Alert policy ID |
| ---------------------------------- | --------- | --------------- |
PolicyId
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type          | Evidence type       |
| --------------------------- | ------------- | ------------------- |
| displayName                 | Display Name  | Display name        |
| instanceName                | Instance Name | Instance name       |
| saasAppId                   | App ID        | SaaS app ID         |
| verdict                     | Verdict       | Verdict             |
| userAccount.userPrincipalNa | User Name     | User principal name |
me
| userAccount.azureAdUserId | User ID             | Microsoft Entra ID user ID |
| ------------------------- | ------------------- | -------------------------- |
| ipAddress                 | IP Address          | IP address                 |
| remediationStatus         | Remediation Status  | Remediation status         |
| remediationStatusDetails  | Remediation Details | Remediation details        |

Third Party Display Name Key Field Name Display Name Description
| detailedRoles | Detailed Roles | Detailed roles |
| ------------- | -------------- | -------------- |
microsoft_defender_for_cloud_ap Microsoft Defender for Cloud Microsoft Defender for Cloud
| ps.URL            | Apps URL      | Apps URL                     |
| ----------------- | ------------- | ---------------------------- |
| event.threat_list | Risk Category | Threat List                  |
| name              | Risk Category | Microsoft Defender for Cloud |
Apps Risk category
microsoft_defender_for_cloud_ap Preview Alerts that have been recently
| ps.isPreview |         | released as GA             |
| ------------ | ------- | -------------------------- |
| user.id      | User ID | User ID of entity that was |
involved in this alert
| user.name | Username | Username of entity that was |
| --------- | -------- | --------------------------- |
involved in this alert
| srcip | Source IP Address | Source IP address of attack that |
| ----- | ----------------- | -------------------------------- |
was involved in this alert
| srcip_host | Source Host | Name of the source workstation |
| ---------- | ----------- | ------------------------------ |
involved in this alert
| dstip_host | Destination Host | Name of the destination |
| ---------- | ---------------- | ----------------------- |
workstation involved in this alert
| observables | Entities | List of observables related to |
| ----------- | -------- | ------------------------------ |
the alert
| name               | Entity Name | Entity name    |
| ------------------ | ----------- | -------------- |
| type               | Entity Type | Entity type    |
| id                 | Entity ID   | Entity ID      |
| event.severity_str | Severity    | Alert severity |
Microsoft Defender for Endpoint
(Graph Security API) event.threat.name Threat Name Threat name
| microsoft_graph_security_api.cate | Category | Alert category |
| --------------------------------- | -------- | -------------- |
(microsoft_defender_for_endpoi
nt_graph_security_api) gory
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.dete | Detection Source | Detection source |
| --------------------------------- | ---------------- | ---------------- |
ctionSource
microsoft_graph_security_api.thre Threat Display Name Threat display name
atDisplayName
microsoft_graph_security_api.thre Threat Family Threat family name
atFamilyName
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type | Type | Evidence type |
| ----------- | ---- | ------------- |

Third Party Display Name Key Field Name Display Name Description
| verdict                     | Verdict     | Verdict             |
| --------------------------- | ----------- | ------------------- |
| deviceDnsName               | Device Name | Device DNS name     |
| hostName                    | Host Name   | Host name           |
| osPlatform                  | OS Platform | OS platform         |
| lastIpAddress               | IP Address  | Last IP address     |
| fileDetails.fileName        | File Name   | File name           |
| fileDetails.filePath        | File Path   | File path           |
| fileDetails.sha256          | SHA256      | SHA256 hash         |
| fileDetails.md5             | MD5         | MD5 hash            |
| fileDetails.sha1            | SHA1        | SHA1 hash           |
| userAccount.userPrincipalNa | User Name   | User principal name |
me
| userAccount.azureAdUserId | User ID         | Microsoft Entra ID user ID |
| ------------------------- | --------------- | -------------------------- |
| url                       | URL             | URL                        |
| ipAddress                 | IP Address      | IP address                 |
| processCommandLine        | Command Line    | Process command line       |
| processId                 | Process ID      | Process ID                 |
| parentProcessId           | Parent PID      | Parent process ID          |
| host.name                 | Host Name       | Host name                  |
| host.ip                   | Host IP Address | Host IP address            |
| user.name                 | User Name       | User name                  |
| user.domain               | User Domain     | User domain                |
| threat                    | Threat Name     | Threat name                |
| file_list                 | File List       | File list                  |
| process_list              | Process List    | Process list               |
| event.severity_str        | Severity        | Alert severity             |
Microsoft Defender for Identity
(Graph Security API) event.threat.name Threat Name Threat name
microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
(microsoft_defender_for_identity
_graph_security_api) gory
| microsoft_graph_security_api.dete | Detector ID | Detector ID |
| --------------------------------- | ----------- | ----------- |
ctorId
| microsoft_graph_security_api.dete | Detection Source | Detection source |
| --------------------------------- | ---------------- | ---------------- |
ctionSource
microsoft_graph_security_api.reco Recommended Actions Recommended actions
mmendedActions
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence

Third Party Display Name Key Field Name Display Name Description
| @odata.type                 | Type    | Evidence type       |
| --------------------------- | ------- | ------------------- |
| verdict                     | Verdict | Verdict             |
| userAccount.userPrincipalNa | User    | User principal name |
me
| userAccount.accountName | Account     | Account name      |
| ----------------------- | ----------- | ----------------- |
| userAccount.domainName  | Domain      | Domain name       |
| ipAddress               | IP Address  | IP address        |
| hostName                | Host Name   | Host name         |
| roles                   | Roles       | Roles             |
| user.name               | User Name   | User name         |
| user.domain             | User Domain | User domain       |
| srcip                   | Source IP   | Source IP address |
| host.name               | Host Name   | Host name         |
| host.ip                 | Host IP     | Host IP address   |
Microsoft Defender for Office event.severity_str Severity Alert severity
| event.threat.name | Threat Name | Threat name |
| ----------------- | ----------- | ----------- |
365 (Graph Security API)
microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
(microsoft_defender_for_office3
gory
65_graph_security_api)
microsoft_graph_security_api.inve Investigation State Investigation state
stigationState
| microsoft_graph_security_api.dete | Determination | Determination |
| --------------------------------- | ------------- | ------------- |
rmination
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type                 | Type              | Evidence type           |
| --------------------------- | ----------------- | ----------------------- |
| verdict                     | Verdict           | Verdict                 |
| primaryAddress              | Email             | Primary email address   |
| subject                     | Subject           | Email subject           |
| senderIp                    | Sender IP         | Sender IP address       |
| recipientEmailAddress       | Recipient         | Recipient email address |
| deliveryAction              | Delivery Action   | Delivery action         |
| deliveryLocation            | Delivery Location | Delivery location       |
| userAccount.userPrincipalNa | User              | User principal name     |
me
| ipAddress  | IP Address  | IP address             |
| ---------- | ----------- | ---------------------- |
| clusterBy  | Cluster By  | Mail cluster criteria  |
| emailCount | Email Count | Email count in cluster |

Third Party Display Name Key Field Name Display Name Description
| user.name            | User Name    | User name            |
| -------------------- | ------------ | -------------------- |
| email.sender.address | Sender Email | Sender email address |
email.recipient.addresses Recipient Emails Recipient email addresses
| email.subject      | Email Subject | Email subject     |
| ------------------ | ------------- | ----------------- |
| srcip              | Source IP     | Source IP address |
| event.severity_str | Severity      | Alert severity    |
Microsoft Defender XDR
| event.threat.name | Threat Name | Threat name |
| ----------------- | ----------- | ----------- |
(microsoft_defender_xdr)
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| type                        | Type      | Evidence type |
| --------------------------- | --------- | ------------- |
| userAccount.userPrincipalNa | User Name | User's name   |
me
| userAccount.azureAdUserId | User ID       | User's ID                   |
| ------------------------- | ------------- | --------------------------- |
| fileDetails.fileName      | File Name     | File name                   |
| fileDetails.filePath      | File Path     | File path                   |
| fileDetails.sha256        | SHA256        | SHA256 hash                 |
| fileDetails.md5           | MD5           | MD5 hash                    |
| fileDetails.sha1          | SHA1          | SHA1 hash                   |
| hostName                  | Host Name     | Host name                   |
| ipInterfaces              | IP Interfaces | IP interfaces of the device |
during the time of the alert
| ipAddress         | IP Address  | IP address  |
| ----------------- | ----------- | ----------- |
| event.threat.name | Threat Name | Threat name |
Microsoft 365
event.severity_str Microsoft 365 Severity Level Microsoft 365 severity level
(microsoft_365)
| event.category | Category   | Microsoft 365 alert category |
| -------------- | ---------- | ---------------------------- |
| Source         | Source     | Microsoft 365 alert source   |
| AlertType      | Alert Type |                              |
Microsoft 365 alert type
event_summary.alert_entity_list Alert Entity List Microsoft 365 Alert entity list
| username | User Name | User name |
| -------- | --------- | --------- |
microsoft_sentinel.Title Incident Title Microsoft Sentinel incident title
Microsoft Sentinel
microsoft_sentinel.ModifiedBy Modified By Microsoft Sentinel modified by
(ms_sentinel_incident)
microsoft_sentinel.AdditionalDat Alerts Count Microsoft Sentinel additional
| a.alertsCount |     | data alerts count |
| ------------- | --- | ----------------- |
microsoft_sentinel.IncidentUrl Incident Link Microsoft Sentinel incident link
microsoft_sentinel.SourceSyste Source System Microsoft Sentinel source system
m
microsoft_sentinel.AlertIds Alert IDs Microsoft Sentinel alert IDs
Microsoft Threat Intelligence event.severity_str Severity Alert severity
(Graph Security API) event.threat.name Threat Name Threat name

Third Party Display Name Key Field Name Display Name Description
(microsoft_threat_intelligence_gr microsoft_graph_security_api.cate Category Alert category (MITRE Tactic)
gory
aph_security_api)
| microsoft_graph_security_api.thre | Threat | Threat display name |
| --------------------------------- | ------ | ------------------- |
atDisplayName
| microsoft_graph_security_api.thre | Threat Family | Threat family |
| --------------------------------- | ------------- | ------------- |
atFamilyName
microsoft_graph_security_api.addi Threat Actor Threat actor name
tionalData.threatActorName
| microsoft_graph_security_api.alert | Alert URL | Alert web URL |
| ---------------------------------- | --------- | ------------- |
WebUrl
| microsoft_graph_security_api.inci | Incident URL | Incident web URL |
| --------------------------------- | ------------ | ---------------- |
dentWebUrl
| microsoft_graph_security_api.evid | Evidence | Evidence |
| --------------------------------- | -------- | -------- |
ence
| @odata.type   | Type              | Evidence type                     |
| ------------- | ----------------- | --------------------------------- |
| verdict       | Verdict           | Verdict                           |
| ipAddress     | IP Address        | IP address                        |
| url           | URL               | URL                               |
| deviceDnsName | Device            | Device DNS name                   |
| roles         | Roles             | Roles                             |
| tags          | Tags              | Tags                              |
| srcip         | Source IP         | Source IP address                 |
| url.full      | URL               | URL                               |
| host.name     | Host Name         | Host name                         |
| srcip         | Source IP Address | Source IP address of the original |
Mimecast Attachment Protect
message that contained the
(mimecast_attachment_protect)
malicious file
Mimecast API 1.0
| file.name | File Name | File name of the malicious file |
| --------- | --------- | ------------------------------- |
mimecast.fileExt File Extension File extension of the malicious
file
| mimecast.Size | File Size | Size (in bytes) of the malicious |
| ------------- | --------- | -------------------------------- |
file
mimecast.sizeAttachment File Size Size (in bytes) of the malicious
file
| file.hash.md5 | File MD5 Hash | MD5 hash of the malicious file |
| ------------- | ------------- | ------------------------------ |
file.hash.sha1 File SHA1 Hash SHA1 hash of the malicious file
file.hash.sha256 File SHA256 Hash SHA256 hash of the malicious
file
| mimecast.fileMime | File MIME Type | Detected MIME type of the |
| ----------------- | -------------- | ------------------------- |
malicious file
| email.sender.address | Sender Address | Sender address |
| -------------------- | -------------- | -------------- |
email.recipient.addresses Recipient Address(es) Recipient address(es)

Third Party Display Name Key Field Name Display Name Description
| email.subject         | Email Subject            | Email subject                     |
| --------------------- | ------------------------ | --------------------------------- |
| mimecast.senderDomain | Sender Domain            | Sender domain                     |
| mimecast.Route        | The Route of the Message | Route of the message              |
| mimecast.route        | The Route of the Message | Route of the message              |
| srcip                 | Source IP Address        | Source IP address of the original |
Mimecast AV
message
(mimecast_av)
| file.name | File Name | File name |
| --------- | --------- | --------- |
Mimecast API 1.0
| mimecast.fileExt       | File Extension   | File extension          |
| ---------------------- | ---------------- | ----------------------- |
| mimecast.fileExtension | File Extension   | File extension          |
| mimecast.Size          | Email Size       | Total size of the email |
| mimecast.emailSize     | Email Size       | Total size of the email |
| file.hash.md5          | File MD5 Hash    | File MD5 hash           |
| file.hash.sha1         | File SHA1 Hash   | File SHA1 hash          |
| file.hash.sha256       | File SHA256 Hash | File SHA256 hash        |
| mimecast.fileMime      | File MIME Type   | File MIME type          |
| email.sender.address   | Sender Address   | Sender address          |
| mimecast.senderDomain  | Sender Domain    | Sender domain           |
email.recipient.addresses Recipient Address(es) Recipient address(es)
| email.subject       | Email Subject            | Email subject               |
| ------------------- | ------------------------ | --------------------------- |
| mimecast.Route      | The Route of the Message | Route of the message        |
| mimecast.route      | The Route of the Message | Route of the message        |
| mimecast.Virus      | Virus Signature          | Virus signature             |
| mimecast.virusFound | Virus Signature          | Virus signature             |
| mimecast.aCode      | Mimecast aCode           | Unique ID used to track the |
Mimecast Impersonation Protect
email through the different log
(mimecast_email_impersonation
types from Mimecast
_protect)
mimecast.processingId Mimecast Processing ID Processing ID used to track the
Mimecast API 1.0
email through Mimecast
(mimecast2_email_impersonatio srcip Source IP Address Source IP address of the original
n_protect)
message
| email.sender.address | Sender Address | Sender address |
| -------------------- | -------------- | -------------- |
Mimecast API 2.0
email.recipient.addresses Recipient Address(es) Recipient address(es)
| email.subject     | Email Subject    | Email subject    |
| ----------------- | ---------------- | ---------------- |
| event.threat.name | Alert Definition | Alert definition |
mimecast.Hits Number of Items Flagged Number of items flagged for the
message
mimecast.itemsDetected Number of Items Detected Number of items detected for the
message
| mimecast.Route | The Route of the Message | Route of the message |
| -------------- | ------------------------ | -------------------- |
| mimecast.route | The Route of the Message | Route of the message |

Third Party Display Name Key Field Name Display Name Description
|     | Mimecast aCode | Unique ID used to track the |
| --- | -------------- | --------------------------- |
Mimecast Internal Email Protect
mimecast.aCode
email through the different log
(mimecast_internal_email_prote
types from Mimecast
ct)
|     | Mimecast Processing ID | Processing ID used to track the |
| --- | ---------------------- | ------------------------------- |
mimecast.processingId
Mimecast API 1.0
email through Mimecast
(mimecast2_internal_email_prot
| srcip | Source IP Address | Source IP address of the |
| ----- | ----------------- | ------------------------ |
ect)
sending mail server
| url | Clicked URL | URL that the user clicked |
| --- | ----------- | ------------------------- |
Mimecast API 2.0
| event.threat.name    | URL Category   | URL category   |
| -------------------- | -------------- | -------------- |
| email.sender.address | Sender Address | Sender address |
email.recipient.addresses Recipient Address(es) Recipient address(es)
| email.subject  | Email Subject            | Email subject        |
| -------------- | ------------------------ | -------------------- |
| mimecast.Route | The Route of the Message | Route of the message |
| mimecast.route | The Route of the Message | Route of the message |
Mimecast Malicious Receipt Log Mimecast aCode Unique ID used to track the
mimecast.aCode
email through the different log
(mimecast_receipt_with_virus)
types from Mimecast
Mimecast API 1.0
|     | Mimecast Processing ID | Processing ID used to track the |
| --- | ---------------------- | ------------------------------- |
mimecast.processingId
(mimecast2_receipt_with_virus) email through Mimecast
| srcip | Source IP Address | Source IP address of the |
| ----- | ----------------- | ------------------------ |
Mimecast API 2.0
sending mail server
| email.sender.address | Sender Address | Sender address |
| -------------------- | -------------- | -------------- |
email.recipient.addresses Recipient Address(es) Recipient address(es)
| email.subject | Email Subject   | Email subject                     |
| ------------- | --------------- | --------------------------------- |
|               | Errors Occurred | Information about any errors that |
mimecast.Error
occurred during receipt
|     | Errors Occurred | Information about any errors that |
| --- | --------------- | --------------------------------- |
mimecast.receiptErrors
occurred during receipt
|     | Email Direction | Direction of the email based on |
| --- | --------------- | ------------------------------- |
mimecast.Dir
the sending and receiving
domains
|     | Email Direction | Direction of the email based on |
| --- | --------------- | ------------------------------- |
mimecast.direction
the sending and receiving
domains
|     | Virus Signature | Virus signature |
| --- | --------------- | --------------- |
event.threat.name
|     | Action | Action taken at the receipt stage |
| --- | ------ | --------------------------------- |
mimecast.Act
|     | Action | Action taken at the receipt stage |
| --- | ------ | --------------------------------- |
mimecast.action
|     | Rejection Information | Rejection information if the email |
| --- | --------------------- | ---------------------------------- |
mimecast.RejInfo
was rejected at the receipt stage

Third Party Display Name Key Field Name Display Name Description
|     | Rejection Information | Rejection information if the email |
| --- | --------------------- | ---------------------------------- |
mimecast.rejectionInfo
was rejected at the receipt stage
|     | Rejection Type | Rejection type if the email was |
| --- | -------------- | ------------------------------- |
mimecast.RejType
rejected at the receipt stage
|     | Rejection Type | Rejection type if the email was |
| --- | -------------- | ------------------------------- |
mimecast.rejectionType
rejected at the receipt stage
|     | TLS Version | TLS version used if the email |
| --- | ----------- | ----------------------------- |
mimecast.TlsVer
was received using TLS
|     | TLS Version | TLS version used if the email |
| --- | ----------- | ----------------------------- |
mimecast.tlsVersion
was received using TLS
|     | TLS Cipher | TLS cipher used if the email was |
| --- | ---------- | -------------------------------- |
mimecast.Cphr
received using TLS
|     | TLS Cipher | TLS cipher used if the email was |
| --- | ---------- | -------------------------------- |
mimecast.tlsCipher
received using TLS
| srcip | Source IP Address | Source IP address of the |
| ----- | ----------------- | ------------------------ |
Mimecast URL Protect
sending mail server
(mimecast_url_protect)
| url | Clicked URL | URL |
| --- | ----------- | --- |
Mimecast API 1.0
| event.threat.name    | URL Category   | URL category   |
| -------------------- | -------------- | -------------- |
| event.reason         | Reason         | Reason         |
| email.sender.address | Sender Address | Sender address |
email.recipient.addresses Recipient Address(es) Recipient address(es)
| email.subject         | Email Subject            | Email subject        |
| --------------------- | ------------------------ | -------------------- |
| mimecast.action       | Mimecast Action          | Mimecast action      |
| mimecast.senderDomain | Sender Domain            | Sender domain        |
| mimecast.route        | The Route of the Message | Route of the message |
| netskopewsg.type      | Netskope Alert Type      | Netskope alert type  |
Netskope Alert (Breach)
| netskopewsg.breach_id | Netskope Breach ID | Netskope breach ID |
| --------------------- | ------------------ | ------------------ |
(netskope_protect_breach)
| netskopewsg.alert_name | Alert Name          | Alert name                 |
| ---------------------- | ------------------- | -------------------------- |
| srcip                  | Source IP           | Source IP address          |
| dstip                  | Destination IP      | Destination IP address     |
| host.ip                | Host IP (User's IP) | Host IP address (user's IP |
address)
| user.name | User Name | User name associated with |
| --------- | --------- | ------------------------- |
Netskope account
netskopewsg.matched_usernam Matched User Name Email address associated with
| e   |     | the breached access method |
| --- | --- | -------------------------- |
| url | URL | URL                        |
event.severity_str Netskope Alert Severity Netskope alert severity
netskopewsg.breach_score Netskope Breach Score Netskope breach score
| file.hash.sha256 | File SHA256 Hash | SHA256 hash of the file |
| ---------------- | ---------------- | ----------------------- |
| file.hash.md5    | File MD5 Hash    | MD5 hash of the file    |

Third Party Display Name Key Field Name Display Name Description
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
| netskopewsg.type | Netskope Alert Type | Netskope alert type |
| ---------------- | ------------------- | ------------------- |
Netskope Alert (Connection)
netskopewsg.connection_id Netskope Connection ID Netskope connection ID
(netskope_protect_connection)
| srcip   | Source IP           | Source IP address          |
| ------- | ------------------- | -------------------------- |
| dstip   | Destination IP      | Destination IP address     |
| host.ip | Host IP (User's IP) | Host IP address (user's IP |
address)
| user.name | User Name | User name |
| --------- | --------- | --------- |
| url       | URL       | URL       |
event.severity_str Netskope Alert Severity Netskope alert severity
| file.hash.sha256 | File SHA256 Hash | SHA256 hash of the file |
| ---------------- | ---------------- | ----------------------- |
| file.hash.md5    | File MD5 Hash    | MD5 hash of the file    |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
| netskopewsg.type | Netskope Alert Type | Netskope alert type |
| ---------------- | ------------------- | ------------------- |
Netskope Alert
| netskopewsg.breach_id | Netskope Breach ID | Netskope breach ID |
| --------------------- | ------------------ | ------------------ |
(netskope_protect_general)
| netskopewsg.alert_name | Alert Name          | Alert name                 |
| ---------------------- | ------------------- | -------------------------- |
| srcip                  | Source IP           | Source IP address          |
| dstip                  | Destination IP      | Destination IP address     |
| host.ip                | Host IP (User's IP) | Host IP address (user's IP |
address)
| host.name | Host Name | Host name                 |
| --------- | --------- | ------------------------- |
| user.name | User Name | User name associated with |
Netskope account
netskopewsg.matched_usernam Matched User Name Email address associated with
| e                    |                 | the breached access method |
| -------------------- | --------------- | -------------------------- |
| netskopewsg.activity | Activity        | Activity                   |
| netskopewsg.action   | Action          | Action                     |
| netskopewsg.policy   | Policy Name     | Policy name                |
| netskopewsg.app      | Application     | Application                |
| url                  | Application URL | Application URL            |
event.severity_str Netskope Alert Severity Netskope alert severity
netskopewsg.breach_score Netskope Breach Score Netskope breach score
| file.hash.sha256 | File SHA256 Hash | SHA256 hash of the file |
| ---------------- | ---------------- | ----------------------- |
| file.hash.md5    | File MD5 Hash    | MD5 hash of the file    |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)

Third Party Display Name Key Field Name Display Name Description
|     | netskopewsg.type | Netskope Alert Type | Netskope alert type |
| --- | ---------------- | ------------------- | ------------------- |
Netskope Alert (Malsite)
|     | event.threat.name | Malsite Category | Malsite category |
| --- | ----------------- | ---------------- | ---------------- |
(netskope_protect_malsite)
|     | netskopewsg.malsite_id | Malsite ID          | Malsite ID                 |
| --- | ---------------------- | ------------------- | -------------------------- |
|     | srcip                  | Source IP           | Source IP address          |
|     | dstip                  | Destination IP      | Destination IP address     |
|     | host.ip                | Host IP (User's IP) | Host IP address (user's IP |
address)
|     | user.name | User Name   | User name   |
| --- | --------- | ----------- | ----------- |
|     | url       | Malsite URL | Malsite URL |
event.severity_str Netskope Alert Severity Netskope alert severity
|     | file.hash.sha256 | File SHA256 Hash | SHA256 hash of the file |
| --- | ---------------- | ---------------- | ----------------------- |
|     | file.hash.md5    | File MD5 Hash    | MD5 hash of the file    |
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)
|     | event.type | Problem Type | Problem type |
| --- | ---------- | ------------ | ------------ |
Oracle Cloud Infrastructure
| (OCI) CloudGuard | event.threat.name | Threat Name | Threat name |
| ---------------- | ----------------- | ----------- | ----------- |
(oci_cloudguard) event.severity_str OCI Severity Level OCI CloudGuard severity level
|     | cloud.resource.type | Cloud Resource Type | Cloud resource type |
| --- | ------------------- | ------------------- | ------------------- |
|     | cloud.resource.id   | Cloud Resource ID   | Cloud resource ID   |
|     | cloud.resource.name | Cloud Resource Name | Cloud resource name |
oracle.data.additionalDetails.pro Problem Recommendation Problem recommendation from
|     | blemRecommendation |     | OCI |
| --- | ------------------ | --- | --- |
Palo Alto Networks Cortex palo_alto_networks.name Alert Name Alert name
| XDR(PAN NGFW) | palo_alto_networks.source | Source | Alert source |
| ------------- | ------------------------- | ------ | ------------ |
(palo_alto_cortex_xdr_ngfw) palo_alto_networks.category Category Alert category
event.severity_str Palo Alto Networks Cortex XDR Palo Alto Networks Cortex XDR
|     |                                   | Alert Severity | alert severity    |
| --- | --------------------------------- | -------------- | ----------------- |
|     | host.name                         | Host Name      | Host name         |
|     | host.ip                           | Host IP        | Host IP address   |
|     | palo_alto_networks.alert_id       | Alert ID       | Alert ID          |
|     | palo_alto_networks.action_pretty  | Action         | Action taken      |
|     | palo_alto_networks.agent_version  | Agent Version  | Agent version     |
|     | palo_alto_networks.resolution_sta | Status         | Resolution status |
tus
|     | palo_alto_networks.events | Network Events | Network events     |
| --- | ------------------------- | -------------- | ------------------ |
|     | event_type                | Event Type     | Event type         |
|     | fw_rule                   | Rule Name      | Firewall rule name |
|     | fw_rule_id                | Rule ID        | Firewall rule ID   |
|     | action_local_ip           | Local IP       | Local IP address   |
|     | action_local_port         | Local Port     | Local port         |

Third Party Display Name Key Field Name Display Name Description
|     | action_remote_ip   | Remote IP       | Remote IP address   |
| --- | ------------------ | --------------- | ------------------- |
|     | action_remote_port | Remote Port     | Remote port         |
|     | action_country     | Remote Country  | Remote country      |
|     | dst_action_country | Dest Country    | Destination country |
|     | fw_device_name     | Device Name     | Firewall device     |
|     | fw_serial_number   | Serial Number   | Firewall serial     |
|     | fw_interface_from  | From Interface  | From interface      |
|     | fw_interface_to    | To Interface    | To interface        |
|     | fw_app_id          | App ID          | Application ID      |
|     | fw_app_category    | App Category    | App category        |
|     | fw_app_subcategory | App Subcategory | App subcategory     |
|     | fw_app_technology  | App Technology  | App technology      |
Palo Alto Networks Cortex palo_alto_networks.name Alert Name Alert name
| XDR(XDR Agent) | palo_alto_networks.source | Source | Alert source |
| -------------- | ------------------------- | ------ | ------------ |
(palo_alto_cortex_xdr_agent) palo_alto_networks.category Category Alert category
event.severity_str Palo Alto Networks Cortex XDR Palo Alto Networks Cortex XDR
|     |                                   | Alert Severity | alert severity    |
| --- | --------------------------------- | -------------- | ----------------- |
|     | host.name                         | Host Name      | Host name         |
|     | host.ip                           | Host IP        | Host IP address   |
|     | palo_alto_networks.alert_id       | Alert ID       | Alert ID          |
|     | palo_alto_networks.action_pretty  | Action         | Action taken      |
|     | palo_alto_networks.agent_version  | Agent Version  | Agent version     |
|     | palo_alto_networks.resolution_sta | Status         | Resolution status |
tus
|     | palo_alto_networks.events | Events         | Related events |
| --- | ------------------------- | -------------- | -------------- |
|     | event_type                | Event Type     | Event type     |
|     | user_name                 | User Name      | User name      |
|     | action_process_image_nam  | Action Process | Action process |
e
|     | actor_process_image_name  | Actor Process  | Actor process  |
| --- | ------------------------- | -------------- | -------------- |
|     | action_process_image_sha2 | Process SHA256 | Process SHA256 |
56
|     | actor_process_image_sha25 | Actor SHA256 | Actor process SHA256 |
| --- | ------------------------- | ------------ | -------------------- |
6
|     | action_process_image_com | Command Line | Process command line |
| --- | ------------------------ | ------------ | -------------------- |
mand_line
|     | actor_process_command_lin | Actor Command Line | Actor command line |
| --- | ------------------------- | ------------------ | ------------------ |
e
|     | actor_process_image_path | Actor Process Path | Actor process path |
| --- | ------------------------ | ------------------ | ------------------ |
|     | actor_process_image_md5  | Actor MD5 Hash     | Actor process MD5  |

Third Party Display Name Key Field Name Display Name Description
actor_process_signature_ve Actor Signature Vendor Actor process signature vendor
ndor
actor_process_signature_sta Actor Signature Status Actor process signature status
tus
| actor_process_os_pid   | Actor Process PID |     | Actor process PID |
| ---------------------- | ----------------- | --- | ----------------- |
| actor_thread_thread_id | Actor Thread ID   |     | Actor thread ID   |
causality_actor_process_ima Causality Actor Process Name Causality actor process name
ge_name
causality_actor_process_ima Causality Actor Process Path Causality actor process path
ge_path
causality_actor_process_co Causality Actor Command Line Causality actor process
| mmand_line |     |     | command line |
| ---------- | --- | --- | ------------ |
causality_actor_process_ima Causality Actor SHA256 Causality actor process SHA256
ge_sha256
causality_actor_process_sig Causality Actor Signature Causality actor process
| nature_vendor | Vendor |     | signature vendor |
| ------------- | ------ | --- | ---------------- |
causality_actor_process_sig Causality Actor Signature Status Causality actor process
| nature_status |     |     | signature status |
| ------------- | --- | --- | ---------------- |
causality_actor_process_exe Causality Actor Execution Time Causality actor process
| cution_time               |                     |     | execution time      |
| ------------------------- | ------------------- | --- | ------------------- |
| action_process_image_path | Action Process Path |     | Action process path |
action_process_signature_v Action Process Signature Action process signature vendor
| endor | Vendor |     |     |
| ----- | ------ | --- | --- |
action_process_signature_st Action Process Signature Status Action process signature status
atus
| action_file_name   | Action File Name   |     | Action file name   |
| ------------------ | ------------------ | --- | ------------------ |
| action_file_path   | Action File Path   |     | Action file path   |
| action_file_sha256 | Action File SHA256 |     | Action file SHA256 |
| action_file_md5    | Action File MD5    |     | Action file MD5    |
Palo Alto Networks Cortex palo_alto_networks.na Alert Name Alert name
me
XDR(XDR Analytics BIOC)
(palo_alto_cortex_xdr_analytics palo_alto_networks.cat Category Alert category
egory
_bioc)
| palo_alto_networks.ale | Alert Type | Alert type |     |
| ---------------------- | ---------- | ---------- | --- |
rt_type
event.severity_str Palo Alto Networks Palo Alto Networks Cortex XDR alert severity
Cortex XDR Alert
Severity
| host.name              | Host Name | Host name       |     |
| ---------------------- | --------- | --------------- | --- |
| host.ip                | Host IP   | Host IP address |     |
| palo_alto_networks.ale | Alert ID  | Alert ID        |     |
rt_id

Third Party Display Name Key Field Name Display Name Description
| palo_alto_networks.ma | Rule ID | Matching rule ID |
| --------------------- | ------- | ---------------- |
tching_service_rule_id
| palo_alto_networks.ma | Match Status | Matching status |
| --------------------- | ------------ | --------------- |
tching_status
| palo_alto_networks.act | Action | Action taken |
| ---------------------- | ------ | ------------ |
ion_pretty
| palo_alto_networks.so | Source | Alert source |
| --------------------- | ------ | ------------ |
urce
| palo_alto_networks.ag | Agent Version | Agent version |
| --------------------- | ------------- | ------------- |
ent_version
| palo_alto_networks.ag | OS Type | Operating System type |
| --------------------- | ------- | --------------------- |
ent_os_type
| palo_alto_networks.ag | OS Version | OS version |
| --------------------- | ---------- | ---------- |
ent_os_sub_type
| palo_alto_networks.res | Status | Resolution status |
| ---------------------- | ------ | ----------------- |
olution_status
| palo_alto_networks.mit | MITRE Tactics | MITRE tactics |
| ---------------------- | ------------- | ------------- |
re_tactic_id_and_nam
e
| palo_alto_networks.mit | MITRE Techniques | MITRE techniques |
| ---------------------- | ---------------- | ---------------- |
re_technique_id_and_
name
| palo_alto_networks.ev | Events | Related events |
| --------------------- | ------ | -------------- |
ents
| event_type       | Event Type     | Event type     |
| ---------------- | -------------- | -------------- |
| user_name        | User Name      | User name      |
| action_process_i | Action Process | Action process |
mage_name
| action_process_i | Command Line | Process command line |
| ---------------- | ------------ | -------------------- |
mage_command_line
| actor_process_im | Actor Process Path | Actor process path |
| ---------------- | ------------------ | ------------------ |
age_path
| action_process_i | Process SHA256 | Process SHA256 |
| ---------------- | -------------- | -------------- |
mage_sha256
| action_process_si | Action Process   | Action process signature vendor |
| ----------------- | ---------------- | ------------------------------- |
| gnature_vendor    | Signature Vendor |                                 |
| action_process_si | Action Process   | Action process signature status |
| gnature_status    | Signature Status |                                 |
| action_process_c  | Action Process   | Action process causality ID     |
| ausality_id       | Causality ID     |                                 |
| actor_process_im  | Actor Process    | Actor process                   |
age_name

Third Party Display Name Key Field Name Display Name Description
| actor_process_co | Actor Command      | Actor command line |
| ---------------- | ------------------ | ------------------ |
| mmand_line       | Line               |                    |
| actor_process_im | Actor Process Path | Actor process path |
age_path
| actor_process_im | Actor SHA256 | Actor process SHA256 |
| ---------------- | ------------ | -------------------- |
age_sha256
| actor_process_im | Actor MD5 Hash | Actor process MD5 |
| ---------------- | -------------- | ----------------- |
age_md5
| actor_process_sig | Actor Signature   | Actor process signature vendor |
| ----------------- | ----------------- | ------------------------------ |
| nature_vendor     | Vendor            |                                |
| actor_process_sig | Actor Signature   | Actor process signature status |
| nature_status     | Status            |                                |
| actor_process_os  | Actor Process PID | Actor process PID              |
_pid
| actor_process_ins  | Actor Process       | Actor process instance ID            |
| ------------------ | ------------------- | ------------------------------------ |
| tance_id           | Instance ID         |                                      |
| actor_process_ca   | Actor Process       | Actor process causality ID           |
| usality_id         | Causality ID        |                                      |
| causality_actor_pr | Causality Actor     | Causality actor process name         |
| ocess_image_name   | Process Name        |                                      |
| causality_actor_pr | Causality Actor     | Causality actor process path         |
| ocess_image_path   | Process Path        |                                      |
| causality_actor_pr | Causality Actor     | Causality actor process command line |
| ocess_command_line | Command Line        |                                      |
| causality_actor_pr | Causality Actor     | Causality actor process SHA256       |
| ocess_image_sha256 | SHA256              |                                      |
| causality_actor_pr | Causality Actor MD5 | Causality actor process MD5          |
ocess_image_md5
| causality_actor_pr   | Causality Actor  | Causality actor process signature vendor |
| -------------------- | ---------------- | ---------------------------------------- |
| ocess_signature_vend | Signature Vendor |                                          |
or
| causality_actor_pr    | Causality Actor  | Causality actor process signature status |
| --------------------- | ---------------- | ---------------------------------------- |
| ocess_signature_statu | Signature Status |                                          |
s
| causality_actor_pr   | Causality Actor  | Causality actor process execution time |
| -------------------- | ---------------- | -------------------------------------- |
| ocess_execution_time | Execution Time   |                                        |
| causality_actor_c    | Causality Actor  | Causality actor causality ID           |
| ausality_id          | Causality ID     |                                        |
| os_actor_process     | OS Actor Process | OS actor process name                  |
| _image_name          | Name             |                                        |
| os_actor_process     | OS Actor Process | OS actor process path                  |
| _image_path          | Path             |                                        |
| os_actor_process     | OS Actor Command | OS actor process command line          |
| _command_line        | Line             |                                        |

Third Party Display Name Key Field Name Display Name Description
| os_actor_process | OS Actor SHA256 | OS actor process SHA256 |     |
| ---------------- | --------------- | ----------------------- | --- |
_image_sha256
| os_actor_process  | OS Actor Signature | OS actor process signature vendor |     |
| ----------------- | ------------------ | --------------------------------- | --- |
| _signature_vendor | Vendor             |                                   |     |
| os_actor_process  | OS Actor Signature | OS actor process signature status |     |
| _signature_status | Status             |                                   |     |
| os_actor_process  | OS Actor Process   | OS actor process PID              |     |
| _os_pid           | PID                |                                   |     |
| os_actor_process  | OS Actor Process   | OS actor process instance ID      |     |
| _instance_id      | Instance ID        |                                   |     |
| os_actor_process  | OS Actor Process   | OS actor process causality ID     |     |
| _causality_id     | Causality ID       |                                   |     |
| os_actor_thread_t | OS Actor Thread ID | OS actor thread ID                |     |
hread_id
| event_timestamp    | Event Timestamp    | Event timestamp              |     |
| ------------------ | ------------------ | ---------------------------- | --- |
| association_stren  | Association        | Association strength         |     |
| gth                | Strength           |                              |     |
| event_sub_type     | Event Sub Type     | Event sub type               |     |
| agent_install_type | Agent Install Type | Agent install type           |     |
| agent_host_boot_   | Agent Host Boot    | Agent host boot time         |     |
| time               | Time               |                              |     |
| contains_featured  | Contains Featured  | Contains featured host       |     |
| _host              | Host               |                              |     |
| contains_featured  | Contains Featured  | Contains featured IP address |     |
| _ip                | IP                 |                              |     |
| contains_featured  | Contains Featured  | Contains featured user       |     |
| _user              | User               |                              |     |
| action_country     | Action Country     | Action country               |     |
Palo Alto Networks Cortex palo_alto_networks.name Alert Name Alert name
XDR(XDR BIOC)
| palo_alto_networks.category | Category |     | Alert category |
| --------------------------- | -------- | --- | -------------- |
(palo_alto_cortex_xdr_bioc) palo_alto_networks.bioc_category BIOC Category BIOC category
_enum_key
| palo_alto_networks.alert_type | Alert Type |     | Alert type |
| ----------------------------- | ---------- | --- | ---------- |
event.severity_str Palo Alto Networks Cortex XDR Palo Alto Networks Cortex XDR
|                                 | Alert Severity |     | alert severity   |
| ------------------------------- | -------------- | --- | ---------------- |
| host.name                       | Host Name      |     | Host name        |
| host.ip                         | Host IP        |     | Host IP address  |
| palo_alto_networks.alert_id     | Alert ID       |     | Alert ID         |
| palo_alto_networks.case_id      | Case ID        |     | Case ID          |
| palo_alto_networks.matching_ser | Rule ID        |     | Matching rule ID |
vice_rule_id

Third Party Display Name Key Field Name Display Name Description
| palo_alto_networks.matching_stat | Match Status | Matching status |
| -------------------------------- | ------------ | --------------- |
us
| palo_alto_networks.action_pretty | Action        | Action taken  |
| -------------------------------- | ------------- | ------------- |
| palo_alto_networks.source        | Source        | Alert source  |
| palo_alto_networks.agent_version | Agent Version | Agent version |
palo_alto_networks.agent_os_typ OS Type Operating System type
e
| palo_alto_networks.agent_os_sub | OS Version | OS version |
| ------------------------------- | ---------- | ---------- |
_type
| palo_alto_networks.resolution_sta | Status | Resolution status |
| --------------------------------- | ------ | ----------------- |
tus
palo_alto_networks.bioc_indicator BIOC Indicator BIOC indicator details
| palo_alto_networks.mitre_tactic_i | MITRE Tactics | MITRE tactics |
| --------------------------------- | ------------- | ------------- |
d_and_name
palo_alto_networks.mitre_techniq MITRE Techniques MITRE techniques
ue_id_and_name
| palo_alto_networks.events | Events         | Related events |
| ------------------------- | -------------- | -------------- |
| event_type                | Event Type     | Event type     |
| user_name                 | User Name      | User name      |
| action_process_image_nam  | Action Process | Action process |
e
| action_process_image_com | Command Line | Process command line |
| ------------------------ | ------------ | -------------------- |
mand_line
| action_process_image_path | Action Process Path | Action process path |
| ------------------------- | ------------------- | ------------------- |
| action_process_image_sha2 | Process SHA256      | Process SHA256      |
56
action_process_signature_v Action Process Signature Action process signature vendor
| endor | Vendor |     |
| ----- | ------ | --- |
action_process_signature_st Action Process Signature Status Action process signature status
atus
action_process_causality_id Action Process Causality ID Action process causality ID
action_process_instance_id Action Process Instance ID Action process instance ID
| actor_process_image_name  | Actor Process      | Actor process      |
| ------------------------- | ------------------ | ------------------ |
| actor_process_command_lin | Actor Command Line | Actor command line |
e
| actor_process_image_path  | Actor Process Path | Actor process path   |
| ------------------------- | ------------------ | -------------------- |
| actor_process_image_sha25 | Actor SHA256       | Actor process SHA256 |
6
| actor_process_image_md5 | Actor MD5 Hash | Actor process MD5 |
| ----------------------- | -------------- | ----------------- |
actor_process_signature_ve Actor Signature Vendor Actor process signature vendor
ndor

Third Party Display Name Key Field Name Display Name Description
actor_process_signature_sta Actor Signature Status Actor process signature status
tus
| actor_process_os_pid | Actor Process PID | Actor process PID |
| -------------------- | ----------------- | ----------------- |
actor_process_instance_id Actor Process Instance ID Actor process instance ID
actor_process_causality_id Actor Process Causality ID Actor process causality ID
| actor_thread_thread_id | Actor Thread ID | Actor thread ID |
| ---------------------- | --------------- | --------------- |
causality_actor_process_ima Causality Actor Process Name Causality actor process name
ge_name
causality_actor_process_ima Causality Actor Process Path Causality actor process path
ge_path
causality_actor_process_co Causality Actor Command Line Causality actor process
| mmand_line |     | command line |
| ---------- | --- | ------------ |
causality_actor_process_ima Causality Actor SHA256 Causality actor process SHA256
ge_sha256
causality_actor_process_ima Causality Actor MD5 Causality actor process MD5
ge_md5
causality_actor_process_sig Causality Actor Signature Causality actor process
| nature_vendor | Vendor | signature vendor |
| ------------- | ------ | ---------------- |
causality_actor_process_sig Causality Actor Signature Status Causality actor process
| nature_status |     | signature status |
| ------------- | --- | ---------------- |
causality_actor_process_exe Causality Actor Execution Time Causality actor process
| cution_time |     | execution time |
| ----------- | --- | -------------- |
causality_actor_causality_id Causality Actor Causality ID Causality actor causality ID
os_actor_process_image_na OS Actor Process Name OS actor process name
me
| os_actor_process_image_pa | OS Actor Process Path | OS actor process path |
| ------------------------- | --------------------- | --------------------- |
th
os_actor_process_command OS Actor Command Line OS actor process command line
_line
os_actor_process_image_sh OS Actor SHA256 OS actor process SHA256
a256
os_actor_process_signature OS Actor Signature Vendor OS actor process signature
| _vendor |     | vendor |
| ------- | --- | ------ |
os_actor_process_signature OS Actor Signature Status OS actor process signature
| _status                 |                      | status               |
| ----------------------- | -------------------- | -------------------- |
| os_actor_process_os_pid | OS Actor Process PID | OS actor process PID |
os_actor_process_instance_i OS Actor Process Instance ID OS actor process instance ID
d
os_actor_process_causality_ OS Actor Process Causality ID OS actor process causality ID
id
| os_actor_thread_thread_id | OS Actor Thread ID   | OS actor thread ID   |
| ------------------------- | -------------------- | -------------------- |
| event_timestamp           | Event Timestamp      | Event timestamp      |
| association_strength      | Association Strength | Association strength |

Third Party Display Name Key Field Name Display Name Description
dst_association_strength Dst Association Strength Destination association strength
| event_sub_type         | Event Sub Type         | Event sub type         |
| ---------------------- | ---------------------- | ---------------------- |
| agent_install_type     | Agent Install Type     | Agent install type     |
| agent_host_boot_time   | Agent Host Boot Time   | Agent host boot time   |
| contains_featured_host | Contains Featured Host | Contains featured host |
contains_featured_ip Contains Featured IP Contains featured IP address
| contains_featured_user | Contains Featured User | Contains featured user |
| ---------------------- | ---------------------- | ---------------------- |
| action_country         | Action Country         | Action country         |
Palo Alto Networks Cortex palo_alto_networks.name Alert Name Alert name
XDR(XDR IOC)
| palo_alto_networks.category | IOC Category | IOC category |
| --------------------------- | ------------ | ------------ |
(palo_alto_cortex_xdr_ioc_alerts palo_alto_networks.bioc_category IOC Type IOC type
_enum_key
)
event.severity_str Palo Alto Networks Cortex XDR Palo Alto Networks Cortex XDR
|                                 | Alert Severity | alert severity   |
| ------------------------------- | -------------- | ---------------- |
| host.name                       | Host Name      | Host name        |
| host.ip                         | Host IP        | Host IP address  |
| palo_alto_networks.alert_id     | Alert ID       | Alert ID         |
| palo_alto_networks.matching_ser | Rule ID        | Matching rule ID |
vice_rule_id
| palo_alto_networks.matching_stat | Match Status | Matching status |
| -------------------------------- | ------------ | --------------- |
us
| palo_alto_networks.action_pretty | Action        | Action taken  |
| -------------------------------- | ------------- | ------------- |
| palo_alto_networks.source        | Source        | Alert source  |
| palo_alto_networks.agent_version | Agent Version | Agent version |
palo_alto_networks.agent_os_typ OS Type Operating System type
e
| palo_alto_networks.agent_os_sub | OS Version | OS version |
| ------------------------------- | ---------- | ---------- |
_type
| palo_alto_networks.resolution_sta | Status | Resolution status |
| --------------------------------- | ------ | ----------------- |
tus
| palo_alto_networks.events | Events         | Related events |
| ------------------------- | -------------- | -------------- |
| event_type                | Event Type     | Event type     |
| user_name                 | User Name      | User name      |
| action_process_image_nam  | Action Process | Action process |
e
| actor_process_image_name  | Actor Process  | Actor process  |
| ------------------------- | -------------- | -------------- |
| action_process_image_sha2 | Process SHA256 | Process SHA256 |
56
| actor_process_image_sha25 | Actor SHA256 | Actor process SHA256 |
| ------------------------- | ------------ | -------------------- |
6
| action_process_image_com | Command Line | Process command line |
| ------------------------ | ------------ | -------------------- |
mand_line

Third Party Display Name Key Field Name Display Name Description
|     | actor_process_command_lin | Actor Command Line | Actor command line |
| --- | ------------------------- | ------------------ | ------------------ |
e
|     | actor_process_image_path | Actor Process Path | Actor process path |
| --- | ------------------------ | ------------------ | ------------------ |
|     | actor_process_image_md5  | Actor MD5 Hash     | Actor process MD5  |
actor_process_signature_ve Actor Signature Vendor Actor process signature vendor
ndor
actor_process_signature_sta Actor Signature Status Actor process signature status
tus
|     | actor_process_os_pid   | Actor Process PID | Actor process PID |
| --- | ---------------------- | ----------------- | ----------------- |
|     | actor_thread_thread_id | Actor Thread ID   | Actor thread ID   |
causality_actor_process_ima Causality Actor Process Name Causality actor process name
ge_name
causality_actor_process_ima Causality Actor Process Path Causality actor process path
ge_path
causality_actor_process_co Causality Actor Command Line Causality actor process
|     | mmand_line |     | command line |
| --- | ---------- | --- | ------------ |
causality_actor_process_ima Causality Actor SHA256 Causality actor process SHA256
ge_sha256
causality_actor_process_sig Causality Actor Signature Causality actor process
|     | nature_vendor | Vendor | signature vendor |
| --- | ------------- | ------ | ---------------- |
causality_actor_process_sig Causality Actor Signature Status Causality actor process
|     | nature_status |     | signature status |
| --- | ------------- | --- | ---------------- |
causality_actor_process_exe Causality Actor Execution Time Causality actor process
|     | cution_time               |                     | execution time      |
| --- | ------------------------- | ------------------- | ------------------- |
|     | action_process_image_path | Action Process Path | Action process path |
action_process_signature_v Action Process Signature Action process signature vendor
|     | endor | Vendor |     |
| --- | ----- | ------ | --- |
action_process_signature_st Action Process Signature Status Action process signature status
atus
|     | action_file_name   | Action File Name   | Action file name   |
| --- | ------------------ | ------------------ | ------------------ |
|     | action_file_path   | Action File Path   | Action file path   |
|     | action_file_sha256 | Action File SHA256 | Action file SHA256 |
|     | action_file_md5    | Action File MD5    | Action file MD5    |
Palo Alto Networks Prisma palo_alto_networks_prisma_clou Alert Type Type of Prisma Cloud alert or
| Cloud | d.type |     | audit event (for example, |
| ----- | ------ | --- | ------------------------- |
admission_audit,
(palo_alto_networks_prisma_clo
container_runtime_audit,
ud)
container_scan)
palo_alto_networks_prisma_clou Log Type Category of the log entry (for
|     | d.log_type |     | example, compliance, |
| --- | ---------- | --- | -------------------- |
vulnerability, filesystem, network)
palo_alto_networks_prisma_clou Attack Type Specific attack pattern detected
|     | d.attack_type |     | (for example, explicitly denied |
| --- | ------------- | --- | ------------------------------- |

Third Party Display Name Key Field Name Display Name Description
file, explicitly denied IP)
palo_alto_networks_prisma_clou Rule Name Prisma Cloud policy or detection
|     | d.rule |     | rule that was triggered |
| --- | ------ | --- | ----------------------- |
palo_alto_networks_prisma_clou Severity Severity level of the alert (critical,
|     | d.severity |     | high, medium, low, info) |
| --- | ---------- | --- | ------------------------ |
palo_alto_networks_prisma_clou Namespace Kubernetes namespace where
|     | d.namespace |     | the event occurred |
| --- | ----------- | --- | ------------------ |
palo_alto_networks_prisma_clou Cluster Kubernetes cluster name
d.cluster
palo_alto_networks_prisma_clou Image Name Container image name
d.image_name
|     | file.path | File Path | File path involved in the alert (for |
| --- | --------- | --------- | ------------------------------------ |
filesystem-related events)
|     | user.name | User Name | Username associated with the |
| --- | --------- | --------- | ---------------------------- |
alert
|     | host.name | Host Name | Host name where the event |
| --- | --------- | --------- | ------------------------- |
occurred
| Proofpoint TAP | srcip | Source IP Address | Source IP address |
| -------------- | ----- | ----------------- | ----------------- |
(proofpoint_tap) url Malicious URL Malicious URL that was clicked
|     | email.subject | Email Subject | Email subject |
| --- | ------------- | ------------- | ------------- |
email.sender.address Sender Address Who actually sent the email on
behalf of the primary sender
|     | email.from.address | From Address | Who the email is from |
| --- | ------------------ | ------------ | --------------------- |
email.recipient.addresses Recipient Address(es) Who received the email
(including CC and BCC)
email.to.addresses To Address(es) Primary intended recipient of the
email
|     | email.x_mailer | X-Mailer | X-Mailer content |
| --- | -------------- | -------- | ---------------- |
event.threat_list Proofpoint Event Threat List Threat category: Threat artifact
|     | name       | Threat Name       | Proofpoint threat name       |
| --- | ---------- | ----------------- | ---------------------------- |
|     | category   | Threat Category   | Proofpoint threat category   |
|     | attachment | Threat Attachment | Proofpoint threat attachment |
severity Proofpoint Threat Severity Proofpoint threat severity
|     | url                       | Proofpoint Threat URL | Proofpoint threat URL |
| --- | ------------------------- | --------------------- | --------------------- |
|     | recorded_future.rule.name | Rule Name             | Rule name             |
Recorded Future Alert
recorded_future.owner_organisati Organizations as defined by Organizations as defined by
(recorded_future_normal_alert)
|     | on_details.organisations      | Recorded Future   | Recorded Future   |
| --- | ----------------------------- | ----------------- | ----------------- |
|     | organisation_name             | Organization Name | Organization name |
|     | recorded_future.log.triggered | Alert Time        | Alert time        |
recorded_future.url.portal Recorded Future Alert URL Recorded Future alert URL
recorded_future.rule.url.portal Recorded Future Alert Rule URL Recorded Future alert rule URL

Third Party Display Name Key Field Name Display Name Description
| recorded_future.playbook_alert_id | Playbook Alert ID | Playbook alert ID |
| --------------------------------- | ----------------- | ----------------- |
Recorded Future Playbook Alert
| recorded_future.priority | Alert Priority | Alert priority |
| ------------------------ | -------------- | -------------- |
(recorded_future_playbook_alert
recorded_future.panel_status.cas Playbook Alert Rule Name Playbook alert rule name
)
e_rule_label
| recorded_future.title              | Alert Title | Alert title |
| ---------------------------------- | ----------- | ----------- |
| recorded_future.panel_status.entit | Entity Name | Entity name |
y_name
| recorded_future.panel_status.entit | Entity ID | Entity ID |
| ---------------------------------- | --------- | --------- |
y_id
recorded_future.owner_organisati Organizations as defined by Organizations as defined by
| on_details.organisations          | Recorded Future   | Recorded Future   |
| --------------------------------- | ----------------- | ----------------- |
| organisation_name                 | Organization Name | Organization name |
| recorded_future.panel_status.targ | Alert Targets     | Alert targets     |
ets
| recorded_future.panel_status.targ | Alert Targets | Alert targets |
| --------------------------------- | ------------- | ------------- |
ets_obj
| name                              | Alert Target     | Alert target     |
| --------------------------------- | ---------------- | ---------------- |
| recorded_future.actions_taken     | Actions Taken    | Actions taken    |
| recorded_future.panel_status.subj | Affected Subject | Affected subject |
ect
recorded_future.panel_status.aut Authorization URL Authorization URL
horization_url
| recorded_future.panel_evidence_ | Malware Family | Malware family |
| ------------------------------- | -------------- | -------------- |
summary.malware_family.name
| recorded_future.panel_evidence_ | Malware File | Malware file |
| ------------------------------- | ------------ | ------------ |
summary.compromised_host.mal
ware_file
| recorded_future.panel_evidence_ | Exfiltration Date | Exfiltration date |
| ------------------------------- | ----------------- | ----------------- |
summary.compromised_host.exfilt
ration_date
recorded_future.panel_evidence_ Compromised Host OS Compromised host OS
| summary.compromised_host.os_uUsername |     | username |
| ------------------------------------- | --- | -------- |
sername
recorded_future.panel_evidence_ Compromised Host Computer Compromised host computer
| summary.compromised_host.com | Name | name |
| ---------------------------- | ---- | ---- |
puter_name
recorded_future.panel_evidence_ Infrastructure IP Address Infrastructure IP address
summary.infrastructure.ip
| recorded_future.panel_evidence_ | Repository Name | Repository name |
| ------------------------------- | --------------- | --------------- |
summary.repository.name
| recorded_future.panel_evidence_ | Repository Owner | Repository owner |
| ------------------------------- | ---------------- | ---------------- |
summary.repository.owner.name

Third Party Display Name Key Field Name Display Name Description
recorded_future.panel_status.entit Critical Level for Entity Critical level for entity
y_criticality
| recorded_future.panel_status.lifec | Lifecycle Stage | Lifecycle stage |
| ---------------------------------- | --------------- | --------------- |
ycle_stage
| recorded_future.panel_overview.e | Alert Event Type | Alert event type |
| -------------------------------- | ---------------- | ---------------- |
vent_type
| recorded_future.panel_overview.l | Alert Location | Alert location |
| -------------------------------- | -------------- | -------------- |
ocation
| recorded_future.panel_overview.f | Facility Name | Facility name |
| -------------------------------- | ------------- | ------------- |
acility_name
| host.name | Host Name | Computer name |
| --------- | --------- | ------------- |
SentinelOne
| host.ip | Host IP Address | Host IP address |
| ------- | --------------- | --------------- |
(sentinelone)
| file.name | File Name | File name |
| --------- | --------- | --------- |
| file.path | File Path | File path |
process.parent.name Parent Process Name Originator process name
SentinelOne Singularity Identity event.threat.name Threat Name Threat name
(sentinelone_identity) event.severity_str Alert Severity Level Alert severity level
| sentinelone.confidenceLevel     | Confidence Level     | Confidence level     |
| ------------------------------- | -------------------- | -------------------- |
| sentinelone.classification      | Alert Classification | Alert classification |
| host.name                       | Host Name            | Host name            |
| host.ip                         | Host IP Address      | Host IP address      |
| sentinelone.asset.id            | Asset ID             | Asset ID             |
| sentinelone.asset.osType        | Asset OS Type        | Asset OS type        |
| sentinelone.detectionTime.scope | Account Name         | Account name         |
.accountName
| sentinelone.detectionTime.scope | Group Name | Group name |
| ------------------------------- | ---------- | ---------- |
.groupName
| sentinelone.detectionTime.scope | Site Name | Site name |
| ------------------------------- | --------- | --------- |
.siteName
| sentinelone.analytics.category | Analytics Category | Analytics category |
| ------------------------------ | ------------------ | ------------------ |
| sentinelone.analytics.uid      | Analytics UID      | Analytics UID      |
sentinelone.detectionSource.pro Detection Source Product Detection source product
duct
| sentinelone.status         | Alert Status    | Alert status    |
| -------------------------- | --------------- | --------------- |
| sentinelone.attackSurfaces | Attack Surfaces | Attack surfaces |
SOCRadar socradar.consolidated_alarm_id Alert ID Alert ID (consolidated)
| socradar.alarm_risk_level | Risk Level | Risk level |
| ------------------------- | ---------- | ---------- |
(socradar)
| socradar.alarm_type_details.alar | Alert Main Type | Alert main type |
| -------------------------------- | --------------- | --------------- |
m_main_type
| socradar.alarm_type_details.alar | Alert Sub Type | Alert sub type |
| -------------------------------- | -------------- | -------------- |
m_sub_type

Third Party Display Name Key Field Name Display Name Description
| socradar.alarm_type_details.alar | Generic Title | Generic title |
| -------------------------------- | ------------- | ------------- |
m_generic_title
| socradar.alarm_notification_texts. | Alert Title | Alert title |
| ---------------------------------- | ----------- | ----------- |
alarm_title
socradar.alarm_notification_texts. Narrative Summary Narrative summary
alarm_text
socradar.alarm_notification_texts. Suggested Mitigation Suggested mitigation
alarm_mitigation_plan
socradar.alarm_detection_and_an Detection & Analysis Notes Detection & analysis notes
alysis
| socradar.alarm_response | Response Playbook | Response playbook |
| ----------------------- | ----------------- | ----------------- |
socradar.alarm_post_incident_an Post-Incident Analysis Post-incident analysis
alysis
| socradar.alarm_assets | Primary Assets | Primary assets in scope |
| --------------------- | -------------- | ----------------------- |
socradar.alarm_related_assets Related Assets Related asset values
| key   | Asset Type   | Related asset type   |
| ----- | ------------ | -------------------- |
| value | Asset Values | Related asset values |
socradar.alarm_related_entities Related Entities Related entity values
| key   | Entity Type   | Related entity type   |
| ----- | ------------- | --------------------- |
| value | Entity Values | Related entity values |
socradar.is_false_positive False Positive Marked false positive
| socradar.tags            | Tags             | Tags / keywords  |
| ------------------------ | ---------------- | ---------------- |
| socradar.notes           | Analyst Notes    | Analyst notes    |
| socradar.source_file     | Source File      | Source file      |
| socradar.alarms          | Alarms Details   | Alarms details   |
| alarmId                  | Alarm ID         | Alarm ID         |
| date                     | Alarm Time       | Alarm time       |
| status                   | Alarm Status     | Alarm status     |
| approvedBy               | Approved By      | Approved by      |
| tags                     | Alarm Tags       | Alarm tags       |
| content.company          | Affected Company | Affected company |
| content.published        | Published Time   | Published time   |
| content.ransomware_group | Threat Group     | Threat group     |
| content.country          | Country/Region   | Country/region   |
| content.content          | Headline         | Headline/blurb   |
| content.content_link.url | Content Link     | Content link     |
| content.Asset            | Asset            | Asset            |
| content.Port             | Port             | Port             |
| content.Protocol         | Protocol         | Protocol         |
| content.Vendor           | Vendor           | Vendor           |
| content.Product          | Product          | Product          |

Third Party Display Name Key Field Name Display Name Description
| content.Version           | Version          | Version            |
| ------------------------- | ---------------- | ------------------ |
| content.CPE               | CPE              | CPE (fingerprint)  |
| content.scan_result.Asset | Vulnerable Asset | Vulnerable asset   |
| content.scan_result.Ports | Vulnerable Ports | Vulnerable port(s) |
| content.scan_result.CVE   | CVE              | CVE (primary)      |
| content.scan_result.CVSS  | CVSS Score       | CVSS score         |
Score
| content.scan_result.CVSS | CVSS Vector | CVSS vector |
| ------------------------ | ----------- | ----------- |
Vector
| content.scan_result.CWE | CWE Details | CWE details |
| ----------------------- | ----------- | ----------- |
Details
| content.scan_result.Affected | Affected Software | Affected software |
| ---------------------------- | ----------------- | ----------------- |
Software
| content.phishing_domain     | Phishing Domain      | Phishing domain      |
| --------------------------- | -------------------- | -------------------- |
| content.phishing_domain_url | Phishing Domain Link | Phishing domain link |
| content.phishing_keyword    | Phishing Keyword     | Phishing keyword     |
| content.ip_address          | IP Address           | IP address           |
| content.ip_addresses        | IP Addresses         | IP addresses         |
| content.email               | Email                | Email                |
| content.password            | Password             | Password             |
| content.full_name           | Account Display Name | Account display name |
| content.username            | Username             | Username/handle      |
| content.profile_url         | Profile URL          | Profile URL          |
| content.source              | Source               | Source               |
| content.source_link         | Source Link          | Source link          |
SonicWall Endpoint Security sonicwall_theron.threat_name Threat Name Threat name
| event.severity | Event Severity Level | Event severity level |
| -------------- | -------------------- | -------------------- |
(sonicwall_theron)
sonicwall_theron.reason Threat Trigger Reason Threat trigger reason
| host.ip          | Host IP Address  | Host IP address  |
| ---------------- | ---------------- | ---------------- |
| host.name        | Host Name        | Host name        |
| user.name        | User Name        | User name        |
| file.path        | File Path        | File path        |
| file.hash.sha256 | File SHA256 Hash | File SHA256 hash |
file.threat_indicator.labels File Hash Reputation Labels File hash reputation labels
file.threat_indicator.sources File Hash Reputation Sources File hash reputation sources
| process.pid | Process ID | Process ID |
| ----------- | ---------- | ---------- |
process.command_line Process Command Line Process command line
| process.parent.pid | Parent Process ID  | Parent process ID  |
| ------------------ | ------------------ | ------------------ |
| process.executable | Process Executable | Process executable |
| process.hash.md5   | Process MD5 Hash   | Process MD5 hash   |

Third Party Display Name Key Field Name Display Name Description
| process.hash.sha1   | Process SHA1 Hash   | Process SHA1 hash   |
| ------------------- | ------------------- | ------------------- |
| process.hash.sha256 | Process SHA256 Hash | Process SHA256 hash |
process.threat_indicator.labels Process Hash Reputation Process hash reputation labels
Labels
process.threat_indicator.sources Process Hash Reputation Process hash reputation
|                           | Sources     | sources     |
| ------------------------- | ----------- | ----------- |
| sonicwall_theron.ep_id    | Endpoint ID | Endpoint ID |
| sonicwall_theron.event_id | Event ID    | Event ID    |
| sonicwall_theron.alert_id | Alert ID    | Alert ID    |
sonicwall_theron.agent_version Detection Agent Version Detection agent version
| sonicwall_theron.scope          | Vendor Event Scope | Vendor event scope |
| ------------------------------- | ------------------ | ------------------ |
| sonicwall_theron.process_killed | Process Killed     | Process killed     |
sonicwall_theron.os_version Operating System Version Operating system version
| sonicwall_theron.file_quarantined | File Quarantined     | File quarantined     |
| --------------------------------- | -------------------- | -------------------- |
| process_list                      | Process List Details | Process list details |
| pid                               | Process ID           | Process ID           |
| parent.pid                        | Parent Process ID    | Parent process ID    |
| name                              | Process Name         | Process name         |
| command_line                      | Command Line         | Command line         |
| hash.md5                          | Process MD5 Hash     | Process MD5 hash     |
| hash.sha1                         | Process SHA1 Hash    | Process SHA1 hash    |
| hash.sha256                       | Process SHA256 Hash  | Process SHA256 hash  |
threat_indicator.labels Process Hash Reputation Process hash reputation labels
Labels
threat_indicator.sources Process Hash Reputation Process hash reputation
|         | Sources | sources         |
| ------- | ------- | --------------- |
| host.ip | Host IP | Host IP address |
Sophos Alert
| user.name | User Name | User name |
| --------- | --------- | --------- |
(sophos_alerts)
event.severity_str Sophos Severity Original severity level from
Sophos
| sophos.type                   | Sophos Event Type | Sophos event type |
| ----------------------------- | ----------------- | ----------------- |
| sophos.data.endpoint_platform | Endpoint Platform | Endpoint platform |
| file.path                     | File Path         | File path         |
| file.hash.sha256              | File SHA256       | File SHA256       |
| host.ip                       | Host IP           | Host IP address   |
Sophos Event
| user.name | User Name | User name |
| --------- | --------- | --------- |
(sophos_events)
| sophos.user_id | User ID | User ID |
| -------------- | ------- | ------- |
event.severity_str Sophos Severity Original severity level from
Sophos
| sophos.type          | Sophos Event Type | Sophos event type |
| -------------------- | ----------------- | ----------------- |
| sophos.endpoint_type | Endpoint Platform | Endpoint platform |

Third Party Display Name Key Field Name Display Name Description
|     | file.path        | File Path   | File path                 |
| --- | ---------------- | ----------- | ------------------------- |
|     | file.hash.sha256 | File SHA256 | File SHA256               |
|     | fireeye.source   | Alert Type  | FireEye alert source type |
Trellix (FireEye HX) Endpoint
Security (AMSI) event.threat.name Threat Name FireEye alert name
| (fireeye_amsi) | event.severity_str | Severity | Severity level |
| -------------- | ------------------ | -------- | -------------- |

|     | host.ip      | Host IP Address | Host IP address   |
| --- | ------------ | --------------- | ----------------- |
|     | host.name    | Host Name       | Host name         |
|     | file_list    | File List       | File list         |
|     | process_list | Process List    | Process list      |
|     | pid          | PID             | Process ID        |
|     | command_line | Command Line    | Command line      |
|     | event.url    | Event URL       | FireEye event URL |
Trellix (FireEye HX) Endpoint fireeye.source Alert Type FireEye alert source type
| Security (IOC) | host.ip   | Host IP Address | Host IP address |
| -------------- | --------- | --------------- | --------------- |
|                | host.name | Host Name       | Host name       |
(fireeye_ioc)
|     | user.name          | User Name          | User name                 |
| --- | ------------------ | ------------------ | ------------------------- |
|     | event.name         | Event Name         | Event name                |
|     | file.name          | File Name          | File name                 |
|     | process.name       | Process Name       | Process name              |
|     | process.executable | Process Executable | Process executable        |
|     | event.url          | Event URL          | FireEye event URL         |
|     | fireeye.source     | Alert Type         | FireEye alert source type |
Trellix (FireEye HX) Endpoint
Security (MAL) event.threat.name Threat Name FireEye alert name
(fireeye_mal) fireeye.infection_type Infection Type FireEye Infection Type
event.severity_str FireEye Severity Level FireEye severity level
|     | host.ip          | Host IP Address  | Host IP address  |
| --- | ---------------- | ---------------- | ---------------- |
|     | host.name        | Host IP Address  | Host name        |
|     | file.path        | File Path        | File path        |
|     | file.hash.md5    | File MD5 Hash    | File MD5 hash    |
|     | file.hash.sha1   | File SHA1 Hash   | File SHA1 hash   |
|     | file.hash.sha256 | File SHA256 Hash | File SHA256 hash |
process.executable Event Actor Process Path FireEye event actor process path
process.pid Event Actor Process Pid FireEye event actor process Pid
|     | event.url | Event URL | FireEye event URL |
| --- | --------- | --------- | ----------------- |
Trellix (FireEye HX) Endpoint fireeye.source Alert Type FireEye alert source type
Security (PROCGUARD)
|     | event.threat.name | Threat Name | FireEye alert name |
| --- | ----------------- | ----------- | ------------------ |
(fireeye_procguard)
|     | host.ip   | Host IP Address | Host IP address |
| --- | --------- | --------------- | --------------- |
|     | host.name | Host Name       | Host name       |
|     | file_list | File List       | File list       |

Third Party Display Name Key Field Name Display Name Description
| process_list | Process List | Process list: Pid (process |
| ------------ | ------------ | -------------------------- |
command line)
| event.url            | Event URL    | FireEye event URL          |
| -------------------- | ------------ | -------------------------- |
| process.command_line | Command Line | Full command line that was |
Trellix MVISION
executed by the process
(trellix_mvision)
| process.pid | Process ID | Unique identifier of the process |
| ----------- | ---------- | -------------------------------- |
process.executable Executable Executable file associated with
the process
| host.name | Host Name | Name of the host where the |
| --------- | --------- | -------------------------- |
event occurred
| user.name | User Name | Name of the user associated |
| --------- | --------- | --------------------------- |
with the event
event.severity_str Trellix MVISION Severity Original severity from Trellix
MVISION
| event.threat.name | Threat Name | Name of the detected threat or |
| ----------------- | ----------- | ------------------------------ |
activity
Trend Micro Cloud App Security event.threat.name Alert Type Alert type
event.severity_str Trend Micro Alert Severity Level Trend Micro alert severity level
(trendmicro_cloud_app_security)
| trendmicro_cloud_app_security.s | Cloud Service | Cloud service |
| ------------------------------- | ------------- | ------------- |
ervice
| trendmicro_cloud_app_security. | Affected User | Affected user |
| ------------------------------ | ------------- | ------------- |
message.affected_user
| trendmicro_cloud_app_security. | File Name | File name |
| ------------------------------ | --------- | --------- |
message.file_name
| trendmicro_cloud_app_security. | File Location | File location |
| ------------------------------ | ------------- | ------------- |
message.location
| trendmicro_cloud_app_security. | Risk Level | Risk level |
| ------------------------------ | ---------- | ---------- |
message.risk_level
trendmicro_cloud_app_security. Triggered Policy Name Triggered policy name
message.triggered_policy_name
trendmicro_cloud_app_security. Triggered Security Filter Triggered security filter
message.triggered_security_filte
r
| file.hash.sha256               | File SHA256 Hash   | SHA256 hash of the file |
| ------------------------------ | ------------------ | ----------------------- |
| file.hash.sha1                 | File SHA1          | File SHA1               |
| trendmicro_cloud_app_security. | Security Risk Name | Security risk name      |
message.security_risk_name
| trendmicro_cloud_app_security. | Threat Type | Threat type |
| ------------------------------ | ----------- | ----------- |
message.threat_type
file.threat_indicator.labels File Hash Reputation Label(s) File hash reputation label(s)
file.threat_indicator.sources File Hash Reputation Source(s) File hash reputation source(s)

Third Party Display Name Key Field Name Display Name Description
trendmicro_cloud_app_security. Virus/Malware Name Virus/Malware name
message.virus_name
| trendmicro_cloud_app_security. | Detection Method | Detection method |
| ------------------------------ | ---------------- | ---------------- |
message.detected_by
| trendmicro_cloud_app_security. | Action Taken | Action taken |
| ------------------------------ | ------------ | ------------ |
message.action
| trendmicro_cloud_app_security. | Email Sender | Email sender |
| ------------------------------ | ------------ | ------------ |
message.mail_message_sender
| trendmicro_cloud_app_security. | Email Recipients | Email recipients |
| ------------------------------ | ---------------- | ---------------- |
message.mail_message_recipie
nt
| trendmicro_cloud_app_security. | Email Subject | Email subject |
| ------------------------------ | ------------- | ------------- |
message.mail_message_subject
| trendmicro_cloud_app_security.u | Suspicious URL | Suspicious URL |
| ------------------------------- | -------------- | -------------- |
rl
| trendmicro_cloud_app_security.i | IP Address | IP address |
| ------------------------------- | ---------- | ---------- |
p
| trendmicro_cloud_app_security.d | Domain Name | Domain name |
| ------------------------------- | ----------- | ----------- |
omain
| trendmicro_cloud_app_security. | Attachment Name | Attachment name |
| ------------------------------ | --------------- | --------------- |
message.attachment_name
| trendmicro_cloud_app_security. | File Size | File size |
| ------------------------------ | --------- | --------- |
message.file_size
| trendmicro_cloud_app_security.l | Unique Alert ID | Unique alert ID |
| ------------------------------- | --------------- | --------------- |
og_item_id
trendmicro_cloud_app_security. Detection Timestamp Detection timestamp
message.detection_time
Trend Micro Vision One event.threat.name Threat Name Threat name
(trendmicro_visionone) event.severity_str Trend Micro Vision One Severity Original Trend Micro Vision One
severity level
trendmicro_visionone.workbenchL Trend Micro Vision One Trend Micro Vision One
| ink          | Workbench Link   | workbench link      |
| ------------ | ---------------- | ------------------- |
| host_list    | Host(s)          | Related host(s)     |
| name         | Host Name        | Host name           |
| ips          | Host IP(s)       | Host IP addresses   |
| process_list | Process(es)      | Related process(es) |
| file_list    | File(s)          | Related file(s)     |
| name         | File Name        | File name           |
| path         | File Path        | File path           |
| hash.md5     | File MD5 Hash    | File MD5 hash       |
| hash.sha1    | File SHA1 Hash   | File SHA1 hash      |
| hash.sha256  | File SHA256 Hash | File SHA256 hash    |

Third Party Display Name Key Field Name Display Name Description
trendmicro_visionone.alertProvide Alert Provider Trend Micro Vision One alert
|     | r          |            | provider        |
| --- | ---------- | ---------- | --------------- |
|     | user_list  | User(s)    | Related user(s) |
|     | event.type | Event Type | Event type      |
Varonis DatAdvantage
(varonis_datadvantage) event.threat.name Threat Name Threat name
event.severity CEF Severity Level Original CEF severity level
|     | user.name | User Name | User name     |
| --- | --------- | --------- | ------------- |
|     | file.name | File Name | File name     |
|     | file.path | File Path | File path     |
|     | host.name | Host Name | Computer name |
VMware Carbon Black Cloud
|     | host.external_ip | Host External IP | Host external IP address |
| --- | ---------------- | ---------------- | ------------------------ |
(carbonblack)
|     | host.ip           | Host Internal IP Address | Host internal IP address |
| --- | ----------------- | ------------------------ | ------------------------ |
|     | process.name      | Process Name             | Process name             |
|     | event.description | Event Reason             | Event reason             |
event.ms_incident_id Incident ID Windows Defender incident ID
Windows Defender Antivirus
| (windows_defender_antivirus) | threat       | Threat Name     | Threat name     |
| ---------------------------- | ------------ | --------------- | --------------- |
|                              | host.name    | Host Name       | Computer name   |
|                              | hostip       | Host IP Address | Host IP address |
|                              | file.path    | File Path       | File path       |
|                              | process.name | Process Name    | Process name    |
WithSecure Elements event.severity_str WithSecure Severity Level WithSecure severity level
|     | event.threat.name | Detection Name | Detection name |
| --- | ----------------- | -------------- | -------------- |
(withsecure)
|     | process.name      | Process File Name | Process file name |
| --- | ----------------- | ----------------- | ----------------- |
|     | process.hash.sha1 | Process SHA1 Hash | Process SHA1 hash |
process.command_line Process Command Line Process command line
|     | user.name                      | User Name       | User name       |
| --- | ------------------------------ | --------------- | --------------- |
|     | withsecure_elements.detectionC | Detection Class | Detection class |
lass
|     | withsecure_elements.deviceId | Device ID | Device ID |
| --- | ---------------------------- | --------- | --------- |
withsecure_elements.exePath Process Executable Path Process executable path
process.threat_indicator.labels Process File Hash Reputation Process file hash reputation
|     |     | Label(s) | label(s) |
| --- | --- | -------- | -------- |
process.threat_indicator.sources Process File Hash Reputation Process file hash reputation
|     |     | Source(s) | source(s) |
| --- | --- | --------- | --------- |
withsecure_elements.description WithSecure Detection WithSecure detection description
Description
|     | wiz.id | Issue ID | Wiz issue ID |
| --- | ------ | -------- | ------------ |
Wiz Cloud Security
|     | wiz.type | Issue Type | Wiz issue type |
| --- | -------- | ---------- | -------------- |
(wiz_issues)
|     | wiz.status   | Status   | Wiz issue status   |
| --- | ------------ | -------- | ------------------ |
|     | wiz.severity | Severity | Wiz issue severity |

Third Party Display Name Key Field Name Display Name Description
| wiz.sourceRule.id   | Rule ID   | Wiz source rule ID   |
| ------------------- | --------- | -------------------- |
| wiz.sourceRule.name | Rule Name | Wiz source rule name |
wiz.sourceRule.description Rule Description Wiz source rule description
wiz.sourceRule.resolutionRecom Resolution Recommendation Resolution recommendation
mendation
| wiz.entity.id                   | Entity ID      | Entity ID      |
| ------------------------------- | -------------- | -------------- |
| wiz.entity.name                 | Entity Name    | Entity name    |
| wiz.entity.type                 | Entity Type    | Entity type    |
| wiz.entitySnapshot.cloudPlatfor | Cloud Platform | Cloud platform |
m
| wiz.entitySnapshot.region       | Region            | Cloud region      |
| ------------------------------- | ----------------- | ----------------- |
| wiz.entitySnapshot.subscription | Subscription Name | Subscription name |
Name
| wiz.entitySnapshot.subscriptionI | Subscription ID | Subscription ID |
| -------------------------------- | --------------- | --------------- |
d
| wiz.createdAt | Created At | Created at |
| ------------- | ---------- | ---------- |
| wiz.updatedAt | Updated At | Updated at |
Key Fields for ML and Rule-Based Alert Types
The Key Fields for Machine Learning (ML) alert types and rule-based alert types are documented
individually. See the Key Fields and Relevant Data Points for any alert type by their display name in
Machine Learning Alert Type Details or by their XDR event name in Alert Types by XDR Event Name.
Key Fields in User Interface
To view the Key Fields in the user interface, click the Key Fields tab.
If the alert description is long, click the More button to display the full alert description. After the alert
description is expanded, the button toggles to Less.
Some Key Fields, such as File Path, have an icon. Click the icon to copy the field value to the
clipboard.

If the value of a Key Field is long, only three lines of text are displayed. Click the More button to
expand the value. After the value is expanded, the button toggles to Less.
If there are multiple values in a Key Field such as for a list, the sub-fields will appear below the Key
Field in a smaller and lighter font.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  