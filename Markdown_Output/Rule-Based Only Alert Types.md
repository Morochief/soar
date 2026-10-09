Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rule-Based Only Alert Types

This article contains only the rule-based alert types. They are listed alphabetically by their display
name.

For the Machine Learning only alert types, see Machine Learning Only Alert Types.

For all the alert types, see All Alert Types Details.

Abnormal Parent / Child Process

A process that typically launches a small, consistent number of child processes has launched a
new child process. Investigate the new child process or the parent process to see if it is benign.

This alert type has the following subtype categories:

Machine Learning Anomaly Detection
Rule Based Detection

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: XDR EBA (XTA0001)

Technique: XDR Process Relationship Anomaly (XT1002)

Tags: [Process Anomaly]

Event Name

The xdr_event.name for this alert type in the Interflow data is parent_child.

Severity

25

Alert Subtype: Machine Learning Anomaly Detection

The xdr_event.subtype.name for this alert subtype in the Interflow data is
machine_learning_anomaly_detection.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

parent_proc_name

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

process_name — name of the process
parent_proc_name — name of the parent process
hostip — host IP address
hostip_host — host name
stability — score measuring the time since the parent process launched the last
child process
days_stable — time since the parent process launched the last child process
diversity — score measuring the number of child processes that the parent process
spawned
child_count — number of child processes that the parent process spawned

Use Case with Data Points

Each pair of parent/child processes (parent_proc_name and process_name) is examined
periodically. If a parent process (parent_proc_name) with a small number of child processes
(diversity, child_count) has not launched a new child process (process_name) for a long
time (stability, days_stable) launches a new child process from a host (srcip_host), an
alert is triggered.

Alert Subtype: Rule Based Detection

The Parent/Child Suspicious Process Creation rules are used to identify suspicious activity with
parent/child relationships associated with process creation. Any one or more of these will trigger
the Parent/Child Suspicious Process Creation alert types.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

hostip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Parent/Child Suspicious Process Creation Alert Type

Account MFA Login Failure Anomaly

An anomalously large number of Multi-Factor Authentication (MFA) user login failures was
observed for an account. Check with the user.

This alert type has the following subtypes:

Machine Learning Anomaly
Rule Based

Alert Subtype: Machine Learning Anomaly

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: [External] Credential Access (TA0006  )

Technique: Brute Force (T1110  )

Tags: [External; Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
cloud_account_login_failure_okta.

Severity

45

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip_usersid

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_usersid — cloud account user ID
srcip_username — cloud account user name
event_summary.total_failed — number of failed logins in the period
event_summary.total_successful — number of successful logins in the period
event_summary.total_fail_ratio — percent of failed logins in the period, which is:
event_summary.total_failed / (event_summary.total_failed +
event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
srcip_host — host name of corresponding source IP address
login_type — type of login
srcip_reputation — source reputation
userIdentity.userName — user name of the account involved in the event
eventSource — source of the event
eventName — name of the event
eventType — type of the event

Use Case with Data Points

Multi-Factor Authentication login failures and successes are calculated periodically for every
account (srcip_usersid). If the number of failures is significantly larger than the number of
successes, an alert is triggered. A sample Interflow includes the login type (login_type), source
host (srcip_host), and source reputation (srcip_reputation).

Alert Subtype: Rule Based

The Suspicious AWS Login Failure rules are used to identify suspicious AWS account login
failures. Any one or more of these will trigger the AWS Cloud Account Login Failure alert type.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS Login Failure

AWS Default VPC Configuration

The AWS Default VPC Configuration rules are used to detect the use of AWS default VPC
settings. Any one or more of these will trigger the AWS Default VPC Configuration alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Exploit Public-Facing Application (T1190  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_config_default_vpc.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

aws.configurationItem.resourceType — resource type of the configuration item
aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS Default VPC Configuration Alert Type

AWS EC2 Security Group Deleted

The AWS EC2 Security Group Deleted rules are used to detect the deletion of an AWS EC2
security group. Any one or more of these will trigger the AWS EC2 Security Group Deleted alert
type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Cloud Firewall (T1562.007  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_ec2_security_group_deleted.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

aws.configurationItem.resourceType — resource type of the configuration item

aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS EC2 Security Group Deleted Alert Type

AWS High-Risk Ports Exposed to Internet

The AWS High-Risk Ports Exposed to Internet rules are used to detect AWS security group rules
that expose high-risk ports to the Internet. Any one or more of these will trigger the AWS High-
Risk Ports Exposed to Internet alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Cloud Firewall (T1562.007  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_high_risk_ports_exposed.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

aws.configurationItem.configuration.ipPermissions.fromPort

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

stellar.config_risky_port — port exposed to the Internet
aws.configurationItem.resourceType — resource type of the configuration item
aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS High-Risk Ports Exposed to Internet Alert Type

AWS IAM Policy with Wildcard Privileges

The AWS IAM Policy with Wildcard Privileges rules are used to detect IAM policies granting
excessive permissions via wildcards. Any one or more of these will trigger the AWS IAM Policy
with Wildcard Privileges alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_config_iam_wildcard_privileges.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

aws.configurationItem.resourceType — resource type of the configuration item
aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS IAM Policy with Wildcard Privileges Alert Type

AWS S3 Bucket Missing Server-Side Encryption

The AWS S3 Bucket Missing Server-Side Encryption rules are used to detect S3 buckets without
server-side encryption. Any one or more of these will trigger the AWS S3 Bucket Missing Server-
Side Encryption alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Collection (TA0009  )

Technique: Data from Cloud Storage Object (T1530  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_s3_missing_server_side_encryption.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

aws.configurationItem.resourceType — resource type of the configuration item
aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS S3 Bucket Missing Server-Side Encryption Alert Type

AWS S3 Bucket Policy with Public Access

The AWS S3 Bucket Policy with Public Access rules are used to detect S3 bucket policies that
allow unauthorized public access. Any one or more of these will trigger the AWS S3 Bucket
Policy with Public Access alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Collection (TA0009  )

Technique: Data from Cloud Storage Object (T1530  )

Tags: [AWS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_config_s3_policy_public_access.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aws.configurationItem.ARN

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

aws.configurationItem.resourceType — resource type of the configuration item
aws.configurationItem.resourceName — resource name of the configuration item
aws.configurationItem.ARN — resource ARN, which is the Amazon Resource Name
of the configuration item
aws.configurationItem.configurationItemStatus — status of the configuration
item
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to AWS S3 Bucket Policy with Public Access Alert Type

Azure Application Gateway Changed

The Azure Application Gateway Changed rules are used to identify events when an Azure
application's gateway is changed. Any one or more of these will trigger the Azure Application
Gateway Changed alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: External Remote Services (T1133  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_application_gateway_changed.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity

resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Azure Application Gateway Changed Alert Type

Azure DNS Zone Changed

The Azure DNS Zone Changed rules are used to identify events when an Azure DNS zone is
changed. Any one or more of these will trigger the Azure DNS Zone Changed alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Command and Control (TA0011  )

Technique: Application Layer Protocol (T1071  )

Sub-technique: DNS (T1071.004  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is azure_dns_zone_change.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved

identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Azure DNS Zone Changed Alert Type

Azure New CloudShell Created

The Azure New CloudShell Created rules are used to identify events when an Azure new Cloud
Shell is changed. Any one or more of these will trigger the Azure New CloudShell Created alert
type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Execution (TA0002  )

Technique: Command and Scripting Interpreter (T1059  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_new_cloudshell_created.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Azure New CloudShell Created Alert Type

Azure Security Configuration Changed

The Azure Security Configuration Changed rules are used to identify events when an Azure
security configuration is changed. Any one or more of these will trigger the Azure Security
Configuration Changed alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_security_config_changed.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Azure Security Configuration Changed Alert Type

BloodHound Enumeration Activity

The BloodHound Enumeration Activity rules are used to identify potential domain enumeration
activity from BloodHound or other Active Directory data collection tools. Any one or more of these
will trigger the BloodHound Enumeration Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Permission Groups Discovery (T1069  )

Sub-technique: Domain Groups (T1069.002  )

Tags: [LDAP; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_bloodhound_enumeration_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
metadata.request.base_object — baseObject field of the LDAP search request
metadata.request.scope — scope field of the LDAP search request
metadata.request.filter — filter field of the LDAP search request
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to BloodHound Enumeration Activity Alert Type

certutil.exe Certificate Extraction

The certutil.exe Certificate Extraction rules are used to identify certutil.exe certificate extraction
activity. Any one or more of these will trigger the certutil.exe Certificate Extraction alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Steal or Forge Authentication Certificates (T1649  )

Tags: [Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
certutil_exe_certificate_extraction.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

process_name

event_data.CommandLine

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
computer_name — host name
event_data.CommandLine — command line
process_name — process name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to certutil.exe Certificate Extraction Alert Type

DCERPC SMB Spoolss Named Pipe

The DCERPC SMB Spoolss Named Pipe rules detect suspicious SMB traffic accessing Spoolss
named pipes. Any one or more of these will trigger the DCERPC SMB Spoolss Named Pipe alert
type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_dce_rpc_smb_spoolss_named_pipe.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to DCERPC SMB Spoolss Named Pipe Alert Type

DNS Query to Anonymous File Upload Domains

The DNS Query to Anonymous File Upload Domains rules are used to identify DNS queries to
anonymous file upload platform domains often used for malicious purposes. Any one or more of
these will trigger the DNS Query to Anonymous File Upload Domains alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Exfiltration (TA0010  )

Technique: Exfiltration Over Web Service (T1567  )

Sub-technique: Exfiltration to Cloud Storage (T1567.002 )

Tags: [DNS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
dns_anonymous_file_upload_domains.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

dns.question.name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — IP address sending DNS query to anonymous file upload platform domains
srcip_geo.countryName — country of the source IP address
dstip — IP address receiving the DNS query
dstip_geo.countryName — country of the destination IP address
dns.question.name — anonymous file upload platform domain being resolved

metadata.request.query — anonymous file upload platform domain being resolved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to DNS Query to Anonymous File Upload Domains Alert Type

DNS Query to External Service Interaction Domains

The DNS Query to External Service Interaction Domains rules are used to identify DNS queries
to external service interaction domains often used for out-of-band interactions after successful
RCE. Any one or more of these will trigger the DNS Query to External Service Interaction
Domains alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Exploit Public-Facing Application (T1190  )

Tags: [DNS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
dns_external_service_interaction_domains.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

dns.question.name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — IP address sending external service domain DNS query
srcip_geo.countryName — country of the source IP address
dstip — IP address receiving the DNS query
dstip_geo.countryName — country of the destination IP address
dns.question.name — external service domain being resolved
metadata.request.query — external service domain being resolved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to DNS Query to External Service Interaction Domains Alert Type

DNS Query to Monero Crypto Coin Mining Pool Domains

The DNS Query to Monero Crypto Coin Mining Pool Domains rules are used to identify DNS
queries to Monero crypto coin mining pool domains. Any one or more of these will trigger the
DNS Query to Monero Crypto Coin Mining Pool Domains alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Resource Hijacking (T1496  )

Tags: [DNS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
dns_pua_cryptocoin_mining_xmr.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

dns.question.name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — IP address sending DNS query to crypto coin mining pool domains
srcip_geo.countryName — country of the source IP address
dstip — IP address receiving the DNS query
dstip_geo.countryName — country of the destination IP address
dns.question.name — crypto coin mining pool domain being resolved
metadata.request.query — crypto coin mining pool domain being resolved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to DNS Query to Monero Crypto Coin Mining Pool Domains Alert Type

DNS Query to TOR Proxy Domain

The DNS Query to TOR Proxy Domain rules are used to identify DNS queries to onion domains
and proxy domains for TOR network. Any one or more of these will trigger the DNS Query to
TOR Proxy Domain alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Exfiltration (TA0010  )

Technique: Proxy (T1090  )

Sub-technique: Multi-hop Proxy (T1090.003 )

Tags: [DNS]

Event Name

The xdr_event.name for this alert type in the Interflow data is dns_tor_proxy_domain.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

dns.question.name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — IP address sending TOR network related DNS query
srcip_geo.countryName — country of the source IP address
dstip — IP address receiving the DNS query
dstip_geo.countryName — country of the destination IP address
dns.question.name — TOR network domain being resolved
metadata.request.query — TOR network domain being resolved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to DNS Query to TOR Proxy Domain Alert Type

Impacket PsExec Execution

The Impacket PsExec Execution rules detect suspicious SMB traffic related to Impacket PsExec
execution. Any one or more of these will trigger the Impacket PsExec Execution alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_impacket_psexec.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Impacket PsExec Execution Alert Type

Microsoft Entra Application Configuration Changes

The Microsoft Entra Application Configuration Changes rules are used to identify suspicious
Microsoft Entra application configuration changes. Any one or more of these will trigger the
Microsoft Entra Application Configuration Changes alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_application_configuration_changes.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity

initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Application Configuration Changes Alert Type

Microsoft Entra Application Deleted

The Microsoft Entra Application Deleted rules are used to identify events when a Microsoft Entra
application is deleted. Any one or more of these will trigger the Microsoft Entra Application
Deleted alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Service Stop (T1489  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is microsoft_entra_app_deleted.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Application Deleted Alert Type

Microsoft Entra Application Permission Changes

The Microsoft Entra Application Permission Changes rules are used to identify suspicious
Microsoft Entra application permission changes. Any one or more of these will trigger the
Microsoft Entra Application Permission Changes alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_application_permission_changes.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Application Permission Changes Alert Type

Microsoft Entra Bitlocker Key Retrieval

The Microsoft Entra Bitlocker Key Retrieval rules are used to identify suspicious Microsoft Entra
Bitlocker key retrieval activity. Any one or more of these will trigger the Microsoft Entra Bitlocker
Key Retrieval alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Credentials from Password Stores (T1555  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_bitlocker_key_retrieval.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra BitLocker Key Retrieval Alert Type

Microsoft Entra Changes to Conditional Access Policy

The Microsoft Entra Changes to Conditional Access Policy rules are used to identify suspicious
Microsoft Entra changes to conditional access policy. Any one or more of these will trigger the
Microsoft Entra Changes to Conditional Access Policy alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Modify Authentication Process (T1556  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_suspicious_changes_to_conditional_access_policy.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.user.id

initiatedBy.app.servicePrincipalId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Changes to Conditional Access Policy Alert Type

Microsoft Entra Changes to Device Registration Policy

The Microsoft Entra Changes to Device Registration Policy rules are used to identify suspicious
Microsoft Entra changes to device registration policy. Any one or more of these will trigger the
Microsoft Entra Changes to Device Registration Policy alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Domain Policy Modification (T1484  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_changes_to_device_registration_policy.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Changes to Device Registration Policy Alert Type

Microsoft Entra Changes to Privileged Account

The Microsoft Entra Changes to Privileged Account rules are used to identify suspicious
Microsoft Entra changes to privileged account. Any one or more of these will trigger the Microsoft
Entra Changes to Privileged Account alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_changes_to_privileged_account.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Changes to Privileged Account Alert Type

Microsoft Entra Changes to Privileged Role Assignment

The Microsoft Entra Changes to Privileged Role Assignment rules are used to identify suspicious
Microsoft Entra changes to privileged role assignment. Any one or more of these will trigger the
Microsoft Entra Changes to Privileged Role Assignment alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_changes_to_privileged_role_assignment.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Changes to Privileged Role Assignment Alert Type

Microsoft Entra Federation Modified

The Microsoft Entra Federation Modified rules are used to identify suspicious Microsoft Entra
federation modified activity. Any one or more of these will trigger the Microsoft Entra Federation
Modified alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Domain Policy Modification (T1484  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is azure_federation_modified.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.user.id

initiatedBy.app.servicePrincipalId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity

stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Federation Modified Alert Type

Microsoft Entra Guest User Invited by Non-Approved Inviters

The Microsoft Entra Guest User Invited by Non-Approved Inviters rules are used to identify
suspicious Microsoft Entra guest user invited by non-approved inviters. Any one or more of these
will trigger the Microsoft Entra Guest User Invited by Non-Approved Inviters alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_guest_user_invited_by_non_approved_inviters.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.user.id

initiatedBy.app.servicePrincipalId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Guest User Invited by Non-Approved Inviters Alert Type

Microsoft Entra Hybrid Health AD FS New Server

The Microsoft Entra Hybrid Health AD FS New Server rules are used to identify a new hybrid
health AD FS server. Any one or more of these will trigger the Microsoft Entra Hybrid Health AD
FS New Server alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Account Discovery (T1087  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
microsoft_entra_hybrid_health_adfs_new_server.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Hybrid Health AD FS New Server Alert Type

Microsoft Entra Hybrid Health AD FS Service Deleted

The Microsoft Entra Hybrid Health AD FS Service Deleted rules are used to identify events when
a hybrid health AD FS server is deleted. Any one or more of these will trigger the Microsoft Entra
Hybrid Health AD FS Service Deleted alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Modify Cloud Compute Infrastructure (T1578  )

Sub-technique: Delete Cloud Instance (T1578.003 )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
microsoft_entra_hybrid_health_adfs_service_deleted.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Hybrid Health AD FS Service Deleted Alert Type

Microsoft Entra ID Discovery Using AzureHound

The Microsoft Entra ID Discovery Using AzureHound rules are used to identify Microsoft Entra ID
discovery using Azurehound. Any one or more of these will trigger the Microsoft Entra ID
Discovery Using Azurehound alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Account Discovery (T1087  )

Sub-technique: Cloud Account (T1087.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_discovery_using_azurehound.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip_username

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_username — user name of the account involved in the event
srcip — IP address of the login client
srcip_host — host name of the login client
UserAgent — user agent string of the login client
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra ID Discovery Using Azurehound Alert Type

Microsoft Entra ID MFA Disabled

The Microsoft Entra ID MFA Disabled rules are used to identify events when a Microsoft Entra ID
multi-factor authentication is disabled. Any one or more of these will trigger the Microsoft Entra ID
MFA Disabled alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Modify Authentication Process (T1556  )

Sub-technique: Multi-Factor Authentication (T1556.006 )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is azure_mfa_disabled.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra ID MFA Disabled Alert Type

Microsoft Entra Owner Removed from Application

The Microsoft Entra Owner Removed from Application rules are used to identify events when a
Microsoft Entra owner is removed from an application. Any one or more of these will trigger the
Microsoft Entra Owner Removed from Application alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Indicator Removal (T1070  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
microsoft_entra_owner_removed_from_app.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity

user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Owner Removed from Application Alert Type

Microsoft Entra PIM Setting Changed

The Microsoft Entra PIM Setting Changed rules are used to identify suspicious Microsoft Entra
PIM setting changed. Any one or more of these will trigger the Microsoft Entra PIM Setting
Changed alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is azure_pim_setting_changed.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra PIM Setting Changed Alert Type

Microsoft Entra Privileged Account Assignment or Elevation

The Microsoft Entra Privileged Account Assignment or Elevation rules are used to identify
suspicious Microsoft Entra privileged account assignment or elevation. Any one or more of these
will trigger the Microsoft Entra Privileged Account Assignment or Elevation alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_privileged_account_assignment_or_elevation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Privileged Account Assignment or Elevation Alert Type

Microsoft Entra Sign-in Failure

The Microsoft Entra Sign-in Failure rules are used to identify suspicious Microsoft Entra sign-in
failures. Any one or more of these will trigger the Microsoft Entra Sign-in Failure alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Brute Force (T1110  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is azure_sign_in_failures.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip_username

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_username — user name of the account involved in the event
srcip — IP address of the login client
srcip_host — host name of the login client
login_result — login result of user login events
azure_ad.status.failureReason — reason for the login failure
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft Entra Sign-in Failure Alert Type

Microsoft Entra Suspicious Sign-in Activity

The Microsoft Entra Suspicious Sign-in Activity rules are used to identify suspicious Microsoft
Entra sign-in activity. Any one or more of these will trigger the Microsoft Entra Suspicious Sign-in
Activity alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
azure_suspicious_sign_in_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip_username

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_username — user name of the account involved in the event
srcip — IP address of the login client
srcip_host — host name of the login client
login_result — login result of user login events
azure_ad.status.failureReason — reason for the login failure
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Microsoft Entra Sign-In Activity Alert Type

OCI Discovery Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The OCI Discovery Activity rules are used to identify suspicious discovery activity in OCI. Any
one or more of these will trigger the OCI Discovery Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Cloud Infrastructure Discovery (T1580  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is oci_discovery_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.definedTags.Oracle-Tags.CreatedBy

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event

oracle.data.definedTags.Oracle-Tags.CreatedBy — name of the user or service
principal that created the resource
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to OCI Discovery Activity Alert Type

OCI Insecure Metadata Endpoint

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The OCI Insecure Metadata Endpoint rules are used to identify potentially insecure metadata
endpoints in OCI. Any one or more of these will trigger the OCI Insecure Metadata Endpoint alert
type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Permission Groups Discovery (T1069  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
oci_insecure_metadata_endpoint.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.request.headers.oci-original-url

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.request.headers.oci-original-url — endpoint URL requested
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to OCI Insecure Metadata Endpoint Alert Type

OCI Insecure NFS Export Configuration

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The OCI Insecure NFS Export Configuration rules are used to identify insecure NFS export
configuration in OCI. Any one or more of these will trigger the OCI Insecure NFS Export
Configuration alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Cloud Infrastructure Discovery (T1580  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
oci_insecure_nfs_export_configuration.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.stateChange.current.exportOptions.source — clients (either
single IPv4 address or single IPv4 CIDR block) to which these options should apply
oracle.data.stateChange.current.exportOptions.access — type of access to
grant clients using the file system through this export
oracle.data.stateChange.current.exportOptions.identitySquash — used
when clients accessing the file system through this export have their UID and GID
remapped to anonymousUid and anonymousGid
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to OCI Insecure NFS Export Configuration Alert Type

OCI Instance Metadata Access

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The OCI Instance Metadata Access rules are used to identify suspicious metadata access of OCI
instances. Any one or more of these will trigger the OCI Instance Metadata Access alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Permission Groups Discovery (T1069  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
oci_instance_metadata_access.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — source IP address of the connection
dstip — destination IP address of the connection
action — decision made by the security lists to accept or reject traffic
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to OCI Instance Metadata Access Alert Type

OCI Unexpected User Agent

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The OCI Unexpected User Agent rules are used to identify unexpected user agents in OCI. Any
one or more of these will trigger the OCI Unexpected User Agent alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Exploit Public-Facing Application (T1190  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is oci_unexpected_user_agent.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.identity.userAgent

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.identity.userAgent — original user agent string from a web request
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to OCI Unexpected User Agent Alert Type

Office365 Rare Operations

The Office365 Rare Operations rules are used to identify rare and suspicious Microsoft 365
mailbox operations. Any one or more of these will trigger the Microsoft 365 Rare Operations alert
type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: [Office 365; Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is office365_rare_operations.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

office365.Operation

user.name

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

office365.Operation — name of the mail operation
user.name — username of the Office 365 account
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Microsoft 365 Rare Operations Alert Type

Password Reset By User Account

The Password Reset By User Account rules are used to identify events when a password is reset
by a user account. Any one or more of these will trigger the Password Reset By User Account
alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
password_reset_by_user_account.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

user.name — user name of the account involved in the activity
azure_ad.activityDisplayName — name of the activity
azure_ad.category — category of the activity
azure_ad.result — result of the activity
azure_ad.resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Password Reset By User Account Alert Type

Persistence and Execution at Scale via GPO Scheduled Task

The Persistence and Execution at Scale via GPO Scheduled Task rules detect suspicious SMB
traffic related to GPO scheduled task creation/access. Any one or more of these will trigger the
Persistence and Execution at Scale via GPO Scheduled Task alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Scheduled Task/Job (T1053  )

Sub-technique: Scheduled Task (T1053.005  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_gpo_scheduledtasks.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Persistence and Execution at Scale via GPO Scheduled Task Alert Type

Phishing Domain with File Extension TLD

The Phishing Domain with File Extension TLD rules are used to identify DNS queries to Top-
Level Domains (TLDs) that resemble file extensions. Any one or more of these will trigger the
Phishing Domain with File Extension TLD alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Phishing (T1566  )

Tags: [DNS]

Event Name

The xdr_event.name for this alert type in the Interflow data is
dns_phishing_file_extension_tld.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

dns.question.name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — IP address sending possible phishing domain DNS query
srcip_geo.countryName — country of the source IP address
dstip — IP address receiving the DNS query
dstip_geo.countryName — country of the destination IP address
dns.question.name — possible phishing domain being resolved
metadata.request.query — possible phishing domain being resolved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Phishing Domain with File Extension TLD Alert Type

Possible Impacket SecretDump Remote Activity

The Possible Impacket SecretDump Remote Activity rules detect suspicious SMB traffic related
to credential dumping using Impacket. Any one or more of these will trigger the Possible
Impacket SecretDump Remote Activity alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: OS Credential Dumping (T1003  )

Tags: [Internal; SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_impacket_secretdump.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Possible Impacket SecretDump Remote Activity Alert Type

Possible PetitPotam Coerce Authentication Attempt

The Possible Impacket SecretDump Remote Activity rules detect suspicious SMB traffic related
to credential dumping using Impacket. Any one or more of these will trigger the Possible
Impacket SecretDump Remote Activity alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Forced Authentication (T1187  )

Tags: [Internal; SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_petitpotam_network_share.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Possible PetitPotam Coerce Authentication Attempt Alert Type

Potentially Malicious AWS Activity

The Potentially Malicious AWS Activity rules are used to identify suspicious activity within AWS
logs. Any one or more of these will trigger the Potentially Malicious AWS Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_malicious_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

errorCode

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Potentially Malicious AWS Activity Alert Type

Potentially Malicious Windows Event

The Potentially Malicious Windows Event rules are used to identify suspicious activity with
Windows events. This is a generic rule name. Any one or more of these will trigger the Potentially
Malicious Windows Event alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Indicator Blocking (T1562.006  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_malicious_event.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.TargetUserName

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Potentially Malicious Event Alert Type

Protected Storage Service Access

The Protected Storage Service Access rules detect suspicious SMB traffic accessing protected
storage services. Any one or more of these will trigger the Protected Storage Service Access
alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_protected_storage_service_access.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Protected Storage Service Access Alert Type

Remote Service Activity via SVCCTL Named Pipe

The Remote Service Activity via SVCCTL Named Pipe rules detect suspicious SMB traffic
accessing SVCCTL named pipes. Any one or more of these will trigger the Remote Service
Activity via SVCCTL Named Pipe alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_svcctl_remote_service.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Remote Service Activity via SVCCTL Named Pipe Alert Type

Remote Task Creation via ATSVC Named Pipe

The Remote Task Creation via ATSVC Named Pipe rules detect suspicious SMB traffic
accessing ATSVC named pipes. Any one or more of these will trigger the Remote Task Creation
via ATSVC Named Pipe alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Scheduled Task/Job (T1053  )

Sub-technique: At (Windows) (T1053.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_atsvc_task.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Remote Task Creation via ATSVC Named Pipe Alert Type

Sensitive Windows Active Directory Attribute Modification

The Sensitive Windows Active Directory Attribute Modification rules are used to identify
suspicious activity with sensitive Windows Active Directory attribute modification. Any one or
more of these will trigger the Sensitive Windows Active Directory Attribute Modification alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Domain Policy Modification (T1484  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_ad_sensitive_attribute_modification.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Sensitive Windows Active Directory Attribute Modification Alert Type

Sensitive Windows Network Share File or Folder Accessed

The Sensitive Windows Network Share File or Folder Accessed rules are used to identify
suspicious activity with Windows network share file or folder access. Any one or more of these
will trigger the Sensitive Windows Network Share File or Folder Accessed alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_sensitive_networkshare.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Sensitive Windows Network Share File or Folder Accessed Alert Type

Startup/Logon Script Added to Group Policy Object

The Startup/Logon Script Added to Group Policy Object rules detect suspicious SMB traffic
related to GPO script modifications. Any one or more of these will trigger the Startup/Logon
Script Added to Group Policy Object alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Boot or Logon Autostart Execution (T1547  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_group_policy_iniscript.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Startup/Logon Script Added to Group Policy Object Alert Type

Steal or Forge Kerberos Tickets

The Steal or Forge Kerberos Tickets rules are used to identify suspicious activity to steal or forge
Kerberos tickets. Any one or more of these will trigger the Steal or Forge Kerberos Tickets alert
type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Steal or Forge Kerberos Tickets (T1558  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_steal_or_forge_kerberos_tickets.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.IpAddress

event_data.ServiceName

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
wineventlog_user — Windows user who executed the script
event_data.ScriptBlockText — Powershell script block text
event_id — Windows event ID associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Steal or Forge Kerberos Tickets Alert Type

Suspicious Access Attempt to Windows Object

The Suspicious Access Attempt to Windows Object rules are used to identify suspicious activity
with access attempt to Windows objects. Any one or more of these will trigger the Suspicious
Access Attempt to Windows Object alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_object_access_suspicious_attempt.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.ObjectName

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Access Attempt to Windows Object Alert Type

Suspicious Activity Related to Security-Enabled Group

The Suspicious Activity Related to Security-Enabled Group rules are used to identify suspicious
activity related to security-enabled groups. Any one or more of these will trigger the Suspicious
Activity Related to Security-Enabled Group alert types.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_suspicious_activity_related_to_security_enabled_group.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.SubjectDomainName

event_data.SubjectUserSid

event_data.TargetDomainName

event_data.TargetUserSid

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
event_data.SubjectUserName — subject user name associated with the activity
event_data.SubjectUserSid — subject user SID associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Activity Related to Security-Enabled Group Alert Type

Suspicious AD Machine Account Creation

The Suspicious AD Machine Account Creation rules are used to identify suspicious machine
account creation activity in Active Directory. Any one or more of these will trigger the Suspicious
AD Machine Account Creation alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Create Account (T1136  )

Tags: [Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_ad_machine_account_creation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

event_data.SubjectUserName

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
event_data.SubjectUserName — name of the user who created the account
event_data.TargetUserName — name of the created machine account
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AD Machine Account Creation Alert Type

Suspicious AWS Bucket Enumeration

The Suspicious AWS Bucket Enumeration rules are used to identify suspicious activity related to
AWS Bucket enumeration. Any one or more of these will trigger the Suspicious AWS Bucket
Enumeration alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Cloud Infrastructure Discovery (T1580  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_bucket_enumeration.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS Bucket Enumeration Alert Type

Suspicious AWS EBS Activity

The Suspicious AWS EBS Activity rules are used to identify suspicious AWS Elastic Block Store
(EBS) activity. Any one or more of these will trigger the Suspicious AWS EBS Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Collection (TA0009  )

Technique: Data Staged (T1074  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_suspicious_ebs_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS EBS Activity Alert Type

Suspicious AWS EC2 Activity

The Suspicious AWS EC2 Activity rules are used to identify suspicious activity within AWS EC2
logs. Any one or more of these will trigger the Suspicious AWS EC2 Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_suspicious_ec2_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS EC2 Activity Alert Type

Suspicious AWS ELB Activity

The Suspicious AWS ELB Activity rules are used to identify suspicious activity with AWS ELB.
Any one or more of these will trigger the Suspicious AWS ELB Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_suspicious_elb_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS ELB Activity Alert Type

Suspicious AWS IAM Activity

The Suspicious AWS IAM Activity rules are used to identify suspicious activity within AWS IAM
logs. Any one or more of these will trigger the Suspicious AWS IAM Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_suspicious_iam_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

errorCode

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS IAM Activity Alert Type

Suspicious AWS RDS Event

The Suspicious AWS RDS Event rules are used to identify suspicious activity related to AWS
RDS events. Any one or more of these will trigger the Suspicious AWS RDS Event alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Create Account (T1136  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is aws_suspicious_rds_event.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS RDS Event Alert Type

Suspicious AWS Root Account Activity

The Suspicious AWS Root Account Activity rules are used to identify suspicious activity with AWS
Root Account. Any one or more of these will trigger the Suspicious AWS Root Account Activity
alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Valid Accounts (T1078  )

Sub-technique: Cloud Accounts (T1078.004  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_root_account_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS Root Account Activity Alert Type

Suspicious AWS Route 53 Activity

The Suspicious AWS Route 53 Activity rules are used to identify suspicious activity within AWS
Route 53 logs. Any one or more of these will trigger the Suspicious AWS Route 53 Activity alert

type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_route53_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS Route 53 Activity Alert Type

Suspicious AWS SSL Certificate Activity

The Suspicious AWS SSL Certificate Activity rules are used to identify suspicious activity with
AWS SSL certificates. Any one or more of these will trigger the Suspicious AWS SSL Certificate
alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Resource Development (TA0042  )

Technique: Obtain Capabilities (T1588  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_ssl_certificate_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

errorCode

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS SSL Certificate Activity Alert Type

Suspicious AWS VPC Flow Logs Modification

The Suspicious AWS VPC Flow Logs Modification rules are used to identify suspicious
modification of AWS VPC Flow logs. Any one or more of these will trigger the Suspicious AWS
VPC Flow Logs Modification alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_vpc_flow_logs_modification.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS VPC Flow Logs Modification Alert Type

Suspicious AWS VPC Mirror Session

The Suspicious AWS VPC Mirror Session rules are used to identify suspicious AWS VPC mirror
session activity. Any one or more of these will trigger the Suspicious AWS VPC Mirror Session
alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_vpc_mirror_session.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious AWS VPC Mirror Session Alert Type

Suspicious Azure Account Permission Elevation

The Suspicious Azure Account Permission Elevation rules are used to identify suspicious Azure
account permission elevation. Any one or more of these will trigger the Suspicious Azure Account
Permission Elevation alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Account Manipulation (T1098  )

Sub-technique: Additional Cloud Roles (T1098.003 )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_account_permission_elevation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation

identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Account Permission Elevation Alert Type

Suspicious Azure Deployment Activity

The Suspicious Azure Deployment Activity rules are used to identify suspicious Azure
deployment activity. Any one or more of these will trigger the Suspicious Azure Deployment
Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Resource Hijacking (T1496  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_deployment_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Deployment Activity Alert Type

Suspicious Azure Firewall Activity

The Suspicious Azure Firewall Activity rules are used to identify suspicious Azure firewall activity.
Any one or more of these will trigger the Suspicious Azure Firewall Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Cloud Firewall (T1562.007  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_firewall_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Firewall Activity Alert Type

Suspicious Azure Key Vault Activity

The Suspicious Azure Key Vault Activity rules are used to identify suspicious Azure Key Vault
activity. Any one or more of these will trigger the Suspicious Azure Key Vault Activity alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Credentials from Password Stores (T1555  )

Sub-technique: Cloud Secrets Management Stores (T1555.006 )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_key_vault_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

aoperationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Key Vault Activity Alert Type

Suspicious Azure Kubernetes Activity: Credential Access

The Suspicious Azure Kubernetes Activity: Credential Access rules are used to identify
suspicious Azure Kubernetes activity usually in the credential access stage. Any one or more of
these will trigger the Suspicious Azure Kubernetes Activity: Credential Access alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Unsecured Credentials (T1552  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_kubernetes_activity_credential_access.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Kubernetes Activity: Credential Access Alert Type

Suspicious Azure Kubernetes Activity: Defense Evasion

The Suspicious Azure Kubernetes Activity: Defense Evasion rules are used to identify suspicious
Azure Kubernetes activity usually in the defense evasion stage. Any one or more of these will
trigger the Suspicious Azure Kubernetes Activity: Defense Evasion alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Tools (T1562.001 )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_kubernetes_activity_defense_evasion.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Kubernetes Activity: Defense Evasion Alert Type

Detection Time

Suspicious Azure Kubernetes Activity: Impact

The Suspicious Azure Kubernetes Activity: Impact rules are used to identify suspicious Azure
Kubernetes activity usually in the impact stage. Any one or more of these will trigger the
Suspicious Azure Kubernetes Activity: Impact alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Data Destruction (T1485  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_kubernetes_activity_impact.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Kubernetes Activity: Impact Alert Type

Suspicious Azure Kubernetes Activity: Persistence

The Suspicious Azure Kubernetes Activity: Persistence rules are used to identify suspicious
Azure Kubernetes activity usually in the persistence stage. Any one or more of these will trigger
the Suspicious Azure Kubernetes Activity: Persistence alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Scheduled Task/Job (T1053  )

Sub-technique: Container Orchestration Job (T1053.007 )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_kubernetes_activity_persistence.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Kubernetes Activity: Persistence Alert Type

Suspicious Azure Kubernetes Activity: Privilege Escalation

The Suspicious Azure Kubernetes Activity: Privilege Escalation rules are used to identify
suspicious Azure Kubernetes activity usually in the privilege escalation stage. Any one or more of
these will trigger the Suspicious Azure Kubernetes Activity: Privilege Escalation alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Privilege Escalation (TA0004  )

Technique: Valid Accounts (T1078  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_kubernetes_activity_privilege_escalation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity
category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Kubernetes Activity: Privilege Escalation Alert Type

Suspicious Azure Network Activity

The Suspicious Azure Network Activity rules are used to identify suspicious Azure network
activity. Any one or more of these will trigger the Suspicious Azure Network Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Network Denial of Service (T1498  )

Tags: [Azure]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_network_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

operationName

resourceId

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

callerIpAddress — IP address of the user who performed the activity
resourceId — identifier of the resource involved
operationName — name of the activity

category — activity category
resultType — result of the operation
identity.authorization.evidence.principalType — type of the service principal
involved
identity.authorization.evidence.principalId — identifier of the service
principal involved
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Azure Network Activity Alert Type

Suspicious Configuration Change to OCI Network Security Group

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious Configuration Change to OCI Network Security Group rules are used to identify
suspicious configuration changes to Network Security Groups in OCI. Any one or more of these
will trigger the Suspicious OCI Configuration Change to Network Security Group alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_configuration_change_to_network_security_group.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Configuration Change to OCI Network Security Group Alert
Type

Suspicious Connection to Another Process

The Suspicious Connection to Another Process rules are used to identify suspicious connection
to another process. Any one or more of these will trigger the Suspicious Connection to Another
Process alert types.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Execution (TA0002  )

Technique: Command and Scripting Interpreter (T1059  )

Sub-technique: PowerShell (T1059.001  )

Tags: [PowerShell]

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_suspicious_connection_process.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Connection to Another Process Alert Type

Suspicious Handle Request to Sensitive Object

The Suspicious Handle Request to Sensitive Object rules are used to identify suspicious activity
with handle requests to sensitive Windows objects. Any one or more of these will trigger the
Suspicious Handle Request to Sensitive Object alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: OS Credential Dumping (T1003  )

Sub-technique: LSASS Memory (T1003.001  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_suspicious_handle_request.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.ObjectName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
event_data.ObjectType — object type of the handle request
event_data.ObjectName — object name of the handle request
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Handle Request to Sensitive Object Alert Type

Suspicious Kerberos Authentication from Golden Certificate

The Suspicious Kerberos Authentication from Golden Certificate rules are used to identify
suspicious Kerberos certificate-based authentication activity potentially resulting from Golden
Certificate in Active Directory. Any one or more of these will trigger the Suspicious Kerberos
Authentication from Golden Certificate alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: Steal or Forge Kerberos Tickets (T1558  )

Tags: [Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_kerberos_authentication_from_golden_certificate.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

event_data.CertIssuerName

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
event_data.CertIssuerName — name of the CA certificate issuer
event_data.TargetUserName — name of the user requesting the Kerberos
authentication ticket
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Kerberos Authentication from Golden Certificate Alert Type

Suspicious LSASS Process Access

The Suspicious LSASS Process Access rules are used to identify suspicious process access to
or from the Local Security Authority Subsystem Service (LSASS). Any one or more of these will
trigger the Suspicious LSASS Process Access alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: OS Credential Dumping (T1003  )

Sub-technique: LSASS Memory (T1003.001  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_process_access_lsass.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.ObjectName

event_data.SourceImage

event_data.TargetImage

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address

hostip_host — host name
event_data.SourceImage — source image path associated with the activity
event_data.TargetImage — target image path associated with the activity
event_data.ObjectType — object type of the handle request
event_data.ObjectName — object name of the handle request
wineventlog_user — user associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious LSASS Process Access Alert Type

Suspicious Microsoft Entra Device Activity

The Suspicious Microsoft Entra Device Activity rules are used to identify suspicious Microsoft
Entra device activity. Any one or more of these will trigger the Suspicious Microsoft Entra Device
Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Network Denial of Service (T1498  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_device_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Microsoft Entra Device Activity Alert Type

Suspicious Microsoft Entra Service Principal Activity

The Suspicious Microsoft Entra Service Principal Activity rules are used to identify suspicious
Microsoft Entra service principal activity. Any one or more of these will trigger the Suspicious
Microsoft Entra Service Principal Activity alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Modify Cloud Compute Infrastructure (T1578  )

Tags: [Microsoft Entra]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_azure_service_principal_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

initiatedBy.app.servicePrincipalId

initiatedBy.user.id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

initiatedBy.user.id — user ID who initiated the activity
initiatedBy.app.servicePrincipalId — application and Service Principal ID that
initiated the activity
user.name — user name
activityDisplayName — activity display name
category — activity category
result — result of the activity
resultReason — result reason of the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Microsoft Entra Service Principal Activity Alert Type

Suspicious Modification of AWS CloudTrail Logs

The Suspicious Modification of AWS CloudTrail Logs rules are used to identify suspicious activity
within AWS CloudTrail logs. Any one or more of these will trigger the Suspicious Modification of

AWS CloudTrail Logs alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_cloudtrail_logs_modification.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Modification of AWS CloudTrail Logs Alert Type

Suspicious Modification of AWS Route Table

The Suspicious Modification of AWS Route Table rules are used to identify suspicious activity
related to modification of AWS route table. Any one or more of these will trigger the Suspicious
Modification of AWS Route Table alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_modification_of_route_table.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event
eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Modification of AWS Route Table Alert Type

Suspicious Modification of OCI Route Table

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious Modification of OCI Route Table rules are used to identify suspicious
modification of route tables in OCI. Any one or more of these will trigger the Suspicious OCI
Modification of Route Table alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_modification_of_route_table.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Modification of OCI Route Table Alert Type

Suspicious Modification of S3 Bucket

The Suspicious Modification of S3 Bucket rules are used to identify suspicious activity within S3
Bucket logs. Any one or more of these will trigger the Suspicious Modification of S3 Bucket alert
type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable Cloud Logs (T1562 .008 )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
aws_suspicious_modification_of_s3_bucket.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

eventName

eventSource

service_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

eventSource — source of event

eventName — name of event
eventType — type of event
userIdentity.accountId — key ID for the account involved in the event
userIdentity.userName — user name of the account involved in the event
userIdentity.type — type of account involved in the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Modification of S3 Bucket Alert Type

Suspicious OCI Bucket Enumeration

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Bucket Enumeration rules are used to identify suspicious bucket
enumeration activity in OCI. Any one or more of these will trigger the Suspicious OCI Bucket
Enumeration alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Cloud Infrastructure Discovery (T1580  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_bucket_enumeration.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.identity.principalId — Oracle Cloud Identifier (OCID) of the
principal entity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Bucket Enumeration Alert Type

Suspicious OCI Bucket Public Access Type Configuration

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Bucket Public Access Type Configuration rules are used to identify
suspicious public access type configuration of OCI buckets. Any one or more of these will trigger
the Suspicious OCI Bucket Public Access Type Configuration alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Discovery (TA0007  )

Technique: Cloud Infrastructure Discovery (T1580  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_bucket_public_access_type_configuration.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.additionalDetails.publicAccessType — type of public access
enabled on the bucket
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Bucket Public Access Type Configuration Alert Type

Suspicious OCI Event Rule Deletion

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Event Rule Deletion rules are used to identify suspicious deletion activity of
event rules in OCI. Any one or more of these will trigger the Suspicious OCI Event Rule Deletion
alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Indicator Removal (T1070  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_event_rule_deletion.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Event Rule Deletion Alert Type

Suspicious OCI IAM Activity: Impact

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI IAM Activity: Impact rules are used to identify suspicious OCI IAM activity
usually in the impact stage. Any one or more of these will trigger the Suspicious OCI IAM Activity:
Impact alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Account Access Removal (T1531  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_iam_activity_impact.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI IAM Activity: Impact Alert Type

Suspicious OCI IAM Activity: Persistence

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI IAM Activity: Persistence rules are used to identify suspicious OCI IAM
activity usually in the persistence stage. Any one or more of these will trigger the Suspicious OCI
IAM Activity: Persistence alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Account Manipulation (T1098  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_iam_activity_persistence.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI IAM Activity: Persistence Alert Type

Suspicious OCI Inbound SSH Connection

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Inbound SSH Connection rules are used to identify suspicious inbound SSH
connection activity in OCI. Any one or more of these will trigger the Suspicious OCI Inbound SSH
Connection alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Initial Access (TA0001  )

Technique: Exploit Public-Facing Application (T1190  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_inbound_ssh_connection.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — source IP address of the connection
dstip — destination IP address of the connection
dstport — destination port of the connection
action — decision made by the security lists to accept or reject traffic
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Inbound SSH Connection Alert Type

Suspicious OCI Instance Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Instance Activity rules are used to identify suspicious instance activity in
OCI. Any one or more of these will trigger the Suspicious OCI Instance Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Resource Hijacking (T1496  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_instance_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
srcip — source IP address of the user or service making the API request
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Instance Activity Alert Type

Suspicious OCI Instance Image Export

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Instance Image Export rules are used to identify suspicious instance image
export activity in OCI. Any one or more of these will trigger the Suspicious OCI Instance Image
Export alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Exfiltration (TA0010  )

Technique: Transfer Data to Cloud Account (T1537  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_instance_image_export.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Instance Image Export Alert Type

Suspicious OCI Kubernetes Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Kubernetes Activity rules are used to identify suspicious Kubernetes activity
in OCI. Any one or more of these will trigger the Suspicious OCI Kubernetes Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Data Destruction (T1485  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_kubernetes_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Kubernetes Activity Alert Type

Suspicious OCI Logging Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Logging Activity rules are used to identify suspicious logging activity in OCI.
Any one or more of these will trigger the Suspicious OCI Logging Activity alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Data Destruction (T1485  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_logging_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Logging Activity Alert Type

Suspicious OCI Object Storage Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Object Storage Activity rules are used to identify suspicious object storage
activity in OCI. Any one or more of these will trigger the Suspicious OCI Object Storage Activity
alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Cloud Logs (T1562.008  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_object_storage_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
oracle.data.response.status — status of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Object Storage Activity Alert Type

Suspicious OCI Scanning Activity

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Scanning Activity rules are used to identify suspicious scanning activity in
OCI. Any one or more of these will trigger the Suspicious OCI Scanning Activity alert type.

XDR Kill Chain

Kill Chain Stage: Initial Attempts

Tactic: Reconnaissance (TA0043  )

Technique: Active Scanning (T1595  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_scanning_activity.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — source IP address of the connection
dstip — destination IP address of the connection
dstport — destination port of the connection
action — decision made by the security lists to accept or reject traffic
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Scanning Activity Alert Type

Suspicious OCI Security Service Impairment

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The Suspicious OCI Security Service Impairment rules are used to identify suspicious
impairment activity to security services in OCI. Any one or more of these will trigger the
Suspicious OCI Security Service Impairment alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Impair Defenses (T1562  )

Sub-technique: Disable or Modify Tools (T1562.001  )

Tags: [OCI]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_security_service_impairment.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

oracle.data.eventName

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

oracle.data.eventName — name of the event
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious OCI Security Service Impairment Alert Type

Suspicious Office365 Inbox Rule

The Suspicious Office365 Inbox Rule rules are used to identify suspicious Microsoft 365 inbox
rules. Any one or more of these will trigger the Suspicious Microsoft 365 Inbox Rule alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Hide Artifacts (T1564  )

Sub-technique: Email Hiding Rules (T1564.008  )

Tags: [Office 365; Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_office365_inbox_rule.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

office365.Operation

user.name

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

office365.Operation — name of the mail operation
office365.ObjectId — ID of the inbox rule
user.name — username of the Office 365 account
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Microsoft 365 Inbox Rule Alert Type

Suspicious Office365 Mail Transport Rule

The Suspicious Office365 Mail Transport Rule rules are used to identify suspicious Microsoft 365
mail transport rules. Any one or more of these will trigger the Suspicious Microsoft 365 Mail
Transport Rule alert type.

XDR Kill Chain

Kill Chain Stage: Exploration

Tactic: Collection (TA0009  )

Technique: Email Collection (T1114  )

Tags: [Office 365; Identity Detection]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_office365_mail_transport_rule.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

office365.Operation

user.name

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

office365.Operation — name of the mail operation
office365.ObjectId — ID of the transport rule
office365.Name — name of the transport rule
user.name — username of the Office 365 account
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Microsoft 365 Mail Transport Rule Alert Type

Suspicious Powershell Script

The Suspicious PowerShell Script rules are used to identify suspicious activity relating to
PowerShell scripts. Any one or more of these will trigger the Suspicious PowerShell Script alert
types.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Execution (TA0002  )

Technique: Command and Scripting Interpreter (T1059  )

Sub-technique: PowerShell (T1059.001  )

Tags: [PowerShell]

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_powershell_script.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
wineventlog_user — Windows user who executed the script
event_data.ScriptBlockText — Powershell script block text
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious PowerShell Script Alert Type

Suspicious Process Creation Commandline

The Suspicious Process Creation Commandline rules are used to identify suspicious activity
relating to command-line process creation. Any one or more of these will trigger the Suspicious
Process Creation Commandline alert types.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Execution (TA0002  )

Technique: Command and Scripting Interpreter (T1059  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is suspicious_commandline.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.CommandLine

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
event_data.CommandLine — process creation command line
hostip_host — host name
wineventlog_user — Windows user who executed the command
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Process Creation Commandline Alert Type

Suspicious PsExec Execution

The Suspicious PsExec Execution rules detect suspicious SMB traffic related to PsExec
Execution activities. Any one or more of these will trigger the Suspicious PsExec Execution alert
type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_susp_psexec.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious PsExec Execution Alert Type

Suspicious Windows Active Directory Operation

The Suspicious Windows Active Directory Operation rules are used to identify suspicious activity
with Windows Active Directory operation. Any one or more of these will trigger the Suspicious
Windows Active Directory Operation alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: [Internal] Credential Access (TA0006  )

Technique: OS Credential Dumping (T1003  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_ad_suspicious_operation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Active Directory Operation Alert Type

Suspicious Windows Logon Event

The Suspicious Windows Logon Event rules are used to identify suspicious activity with Windows
logons. Any one or more of these will trigger the Suspicious Windows Logon alert types.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Valid Accounts (T1078  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_suspicious_logon_event.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Logon Event Alert Type

Suspicious Windows Network Connection

The Suspicious Windows Network Connection rules are used to identify suspicious Windows
network connection activities. Any one or more of these will trigger the Suspicious Windows
Network Connection alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Signed Binary Proxy Execution (T1218  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_windows_network_connection.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.Image

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
event_data.Image — process associated with the activity
wineventlog_user — user associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Network Connection Alert Type

Suspicious Windows Process Creation

The Suspicious Windows Process Creation rules are used to identify suspicious activity
associated with process creation. Any one or more of these will trigger the Suspicious Process
Creation alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Defense Evasion (TA0005  )

Technique: Signed Binary Proxy Execution (T1218  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_suspicious_process_creation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

process_name

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
process_name — process associated with the activity
hostip_host — host name
wineventlog_user — Windows user associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Windows Suspicious Process Creation Alert Type

Suspicious Windows Registry Event: Impact

The Suspicious Windows Registry Event: Impact rules are used to identify suspicious Windows
registry events usually in the impact stage. Any one or more of these will trigger the Suspicious
Windows Registry Event: Impact alert type.

XDR Kill Chain

Kill Chain Stage: Exfiltration & Impact

Tactic: Impact (TA0040  )

Technique: Defacement (T1491  )

Sub-technique: Internal Defacement (T1491.001  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_windows_registry_event_impact.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.TargetObject

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
event_data.Image — process associated with the activity
event_data.TargetObject — target registry
event_data.Details — value set to the registry
wineventlog_user — user associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Registry Event: Impact Alert Type

Suspicious Windows Registry Event: Persistence

The Suspicious Windows Registry Event: Persistence rules are used to identify suspicious
Windows registry events usually in the persistence stage. Any one or more of these will trigger
the Suspicious Windows Registry Event: Persistence alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Office Application Startup (T1137  )

Sub-technique: Add-ins (T1137.006  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
suspicious_windows_registry_event_persistence.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_data.TargetObject

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

hostip — host IP address
hostip_host — host name
event_data.Image — process associated with the activity
event_data.TargetObject — target registry
event_data.Details — value set to the registry
wineventlog_user — user associated with the activity
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Registry Event: Persistence Alert Type

Suspicious Windows Service Installation

The Suspicious Windows Service Installation rules are used to identify suspicious activity with
service installation. Any one or more of these will trigger the Suspicious Windows Service
Installation alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Execution (TA0002  )

Technique: Command and Scripting Interpreter (T1059  )

Sub-technique: PowerShell (T1059.001  )

Tags: []

Event Name

The xdr_event.name for this alert type in the Interflow data is
windows_security_suspicious_service_installation.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

computer_name

event_id

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

event_id — Windows event ID associated with the activity
hostip — host IP address
hostip_host — host name
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Suspicious Windows Service Installation Alert Type

T1047 Wmiprvse Wbemcomn DLL Hijack

The T1047 Wmiprvse Wbemcomn DLL Hijack rules detect suspicious SMB traffic related to WMI
DLL Hijack activities. Any one or more of these will trigger the T1047 Wmiprvse Wbemcomn DLL
Hijack alert type.

XDR Kill Chain

Kill Chain Stage: Propagation

Tactic: Lateral Movement (TA0008  )

Technique: Remote Services (T1021  )

Sub-technique: SMB/Windows Admin Shares (T1021.002  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_win_security_wmiprvse_wbemcomn_dll_hijack.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to T1047 Wmiprvse Wbemcomn DLL Hijack Alert Type

Windows Network Access Suspicious desktop.ini Action

The Windows Network Access Suspicious desktop.ini Action rules detect suspicious SMB traffic
accessing desktop.ini files. Any one or more of these will trigger the Windows Network Access
Suspicious desktop.ini Action alert type.

XDR Kill Chain

Kill Chain Stage: Persistent Foothold

Tactic: Persistence (TA0003  )

Technique: Boot or Logon Autostart Execution (T1547  )

Sub-technique: Shortcut Modification (T1547.009  )

Tags: [SMB; Network Traffic Analysis]

Event Name

The xdr_event.name for this alert type in the Interflow data is
network_security_net_share_obj_susp_desktop_ini.

Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

appid_name

srcip

dstip

stellar.rule_id

Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — network traffic protocol that triggered this detection
srcip — source IP address
dstip — destination IP address
stellar.rule_id — Stellar Cyber rule ID

Link to Rule-Based Alert Types

Rules Contributing to Windows Network Access Suspicious desktop.ini Action Alert Type

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

