✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
All Alert Types by Name
This article contains all the alert types, both Machine Learning (ML) and rules-based. They are
listed alphabetically by their display name. For all the alert types listed alphabetically by their
XDR event name, see All Alert Types by XDR Event Name.
For the Machine Learning only alert types, see Machine Learning Only Alert Types.
For the rule-based only alert types, see Rule-Based Only Alert Types.
 To minimize excessive alerting, each alert type is triggered only once in a configurable
period (from 1 to 24 hours) for the set of attributes that triggered that specific alert. You can
configure the alert suppression interval in the Detection Management System.
 Where applicable, the Tactics and Techniques are linked to the relevant MITRE | ATT&CK
page.
 Stellar Cyber provides Coverage Analyzer  and Detections & Response  tools that let
you look up alert types by sensor, data source, application, alert name, alert type, or by XDR
attributes such as kill chain stage, tactic, or technique. You can also view alert types by
index in Machine Learning Alert Types by Index, which provides links to descriptions of the
alert types that can appear in each available index.
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
Account Created and Deleted in Short Timeframe
Detects when an account was created and deleted in a short period of time.
This alert type has the following subtype category:
Microsoft Entra Account Created and Deleted Within a Close Time Frame
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Valid Accounts (T1078 )
Tags: [Microsoft Entra; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
account_created_deleted_in_short_timeframe.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
correlation_info.0.targetResources.id, from the record in wineventlog representing a
deletion
azure_ad.activityDisplayName: Delete user
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
user.name — user name of the account involved in the activity
activityDisplayName — name of the activity
category — category of the activity
result — result of the activity

resultReason — result reason of the activity
Use Case with Data Points
This alert is triggered if an account (user.name) is created and then deleted within 24 hours. The
Interflow includes the user account (user.name), the account creation time
(correlation_info[1].timestamp), and the account deletion time
(correlation_info[0].timestamp).
Alert Subtype: Microsoft Entra Account Created and Deleted Within a Close Time
Frame
The Microsoft Entra Account Created and Deleted Within a Close Time Frame subtype is the
same as the Account Created and Deleted in Short Timeframe alert type above, with the
following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
azure_ad_account_created_deleted.
Account Creation Anomaly
An anomalously large number of accounts were created in a 5-minute interval or a user created
an account for the first time in at least 14 days. Check the originating account and the new
accounts for malicious behavior.
 The data sources for this alert type are AWS, Microsoft Entra ID (formerly Azure AD),
Google Workspace, and Windows.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [Internal] Persistence (TA0003 )
Technique: Create Account (T1136 )
Tags: [Internal; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is account_creation_anomaly.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.SubjectUserName
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_usersid — SID of account creating new accounts
or
event_data.SubjectUserName — User name of account creating new accounts (for
Windows only)
 The key field for this alert type can be srcip_usersid or
event_data.SubjectUserName, depending on the data source.
srcip_username — user name of account creating new accounts
responseElements.user.meta.createdBy — AWS user creating new accounts
event_id — Windows event ID corresponding to the account creations
actual — Actual number of account creation events in a 5-minute period
typical — Typical number of account creation events in a 5-minute period
event_summary.account_creation.new_users_count — Count of user names of
new accounts
event_summary.account_creation.new_users_summary — Summary of user names
of new accounts, which is a list of up to 100 unique user names associated with the new
account creations
Use Case with Data Points
If an unusually high number of accounts were created (actual) by (srcip_usersid) in a 5-
minute period, an alert is triggered. The Interflow record includes the data source, the account
responsible for creating other accounts, the timestamp, the number of accounts created
(event_summary.account_creation.new_users_count), and a list of the created accounts
(event_summary.account_creation.new_users_summary).
Validation / Remediation
Investigate the account that is creating other accounts for a breach and investigate any activity
from the newly created accounts.
Potential False Positives
False positives may occur when many accounts are created at the same time for business
purposes, for example, when onboarding new users or otherwise procedurally generating
accounts.
Account MFA Login Failure Anomaly
An anomalously large number of Multi-Factor Authentication (MFA) user login failures was
observed for an account. Check with the user.
This alert type has the following subtypes:
Machine Learning Anomaly
Rule Based
Alert Subtype: Machine Learning Anomaly
XDR Kill Chain
Kill Chain Stage: Initial Attempts

Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
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
Application Usage Anomaly
An internal application had an anomalously large number of connections to one or more external
hosts in a measured interval, exceeding 99.99% of all other intervals corresponding to different
applications in the past two weeks. Investigate the application and connections, and consider
blocking connections from the application.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR App Anomaly (XT2003)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is pripub_appid.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
appid
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
appid — application ID
appid_name — application name
actual — actual number of connections in the period
stellar.threshold — threshold number of connections per interval below which
99.99% of all other intervals, corresponding to different applications in the past two
weeks, fall
srcip_host — host name of a sample source IP address
srcip_geo.countryName — source country
dstip_host — host name of a sample destination IP address
Use Case with Data Points
Every application's (appid) number of connections is calculated periodically. If an application’s
connections (actual) are larger than the threshold (stellar.threshold) below which 99.99%
of all other intervals corresponding to different applications in the past two weeks fall, an alert is
triggered. The Interflow includes a sample source host (srcip_host), the source country
(srcip_geo.countryName), and a sample destination host (dstip_host). If there are multiple
source or destination hosts, view the list in the Original Records.
AWS AMI Made Public
An AWS AMI was made public. Check with the user to make sure this was intentional.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
Tags: [AWS AMI; Access Control]
XDR Event Name
The xdr_event.name for this alert type in the Interflow data is aws_ami_public.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
userIdentity.accountId
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
userIdentity.accountId — key ID for the account
userIdentity.userName — AWS account user name
userIdentity.type — AWS account type

eventName — AWS event name
eventSource — AWS event source
eventType — AWS event type
Use Case with Data Points
For each AWS account (userIdentity.accountId), activity to make an AMI public is
monitored. If an AMI is made public, an alert is triggered. The Interflow includes the account ID
(userIdentity.accountId), user name (userIdentity.userName), account type
(userIdentity.type), AWS event name (eventName), AWS event source (eventSource), and
AWS event type (eventType).
AWS Default VPC Configuration
The AWS Default VPC Configuration rules are used to detect the use of AWS default VPC
settings. Any one or more of these will trigger the AWS Default VPC Configuration alert type.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable or Modify Cloud Firewall (T1562.007 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )

Sub-technique: Disable or Modify Cloud Firewall (T1562.007 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
AWS Logging Stopped
AWS CloudTrail logging was stopped. Check with the user to make sure this was intentional.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable or Modify Cloud Logs (T1562.008 )
Tags: [AWS CloudTrail]
Event Name
The xdr_event.name for this alert type in the Interflow data is aws_stoplogging.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
userIdentity.accountId — key ID for the account
userIdentity.userName — AWS account user name
userIdentity.type — AWS account type

eventName — AWS event name
eventSource — AWS event source
eventType — AWS event type
Use Case with Data Points
For each AWS account (userIdentity.accountId), log disabling is monitored. Logging is
enabled by default, so if logging is disabled, an alert is triggered. The Interflow includes the
account ID (userIdentity.accountId), AWS account user name (userIdentity.userName),
AWS account type (userIdentity.type), AWS event name (eventName), AWS event source
(eventSource), and AWS event type (eventType).
AWS S3 Bucket Missing Server-Side Encryption
The AWS S3 Bucket Missing Server-Side Encryption rules are used to detect S3 buckets without
server-side encryption. Any one or more of these will trigger the AWS S3 Bucket Missing Server-
Side Encryption alert type.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: Collection (TA0009 )
Technique: Data from Cloud Storage Object (T1530 )
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
Tactic: Collection (TA0009 )
Technique: Data from Cloud Storage Object (T1530 )
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
AWS S3 Ransomware
Possible AWS S3 ransomware was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Data Encrypted for Impact (T1486 )
Tags: [Malware; Ransomware; AWS S3]

Event Name
The xdr_event.name for this alert type in the Interflow data is aws_s3_ransomware.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
userIdentity.accountId — key ID for the account
userIdentity.userName — AWS account user name
userIdentity.type — AWS account type
eventName — AWS event name
eventSource — AWS event source
eventType — AWS event type
Use Case with Data Points
For each AWS account user name (userIdentity.userName), suspicious S3 ransomware is
monitored. If ransomware is detected, an alert is triggered. The Interflow includes the account ID
(userIdentity.accountId), AWS account user name (userIdentity.userName), AWS
account type (userIdentity.type), AWS event name (eventName), AWS event source
(eventSource), and AWS event type (eventType).
Azure Application Gateway Changed
The Azure Application Gateway Changed rules are used to identify events when an Azure
application's gateway is changed. Any one or more of these will trigger the Azure Application
Gateway Changed alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: External Remote Services (T1133 )
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
Tactic: Command and Control (TA0011 )
Technique: Application Layer Protocol (T1071 )
Sub-technique: DNS (T1071.004 )
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
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Backup Catalogs Deleted by Ransomware
The wbadmin.exe utility was used to delete the backup catalog. Ransomware and other malware
do this to prevent system recovery. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Indicator Removal on Host (T1070 )
Sub-technique: File Deletion (T1070.004 )
Tags: [Malware; Ransomware]
Event Name
The xdr_event.name for this alert type in the Interflow data is
ransomware_delete_backup_catalogs.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host on which the ransomware action happened
hostip_host — host name
process_name — name of the executed process
event_data.CommandLine — command line that is executed to delete the backup
catalog
Use Case with Data Points
If wbadmin.exe is used to delete the backup catalog, an alert is triggered. The Interflow includes
the host IP address (hostip), process name (process_name), and command line
(event_data.CommandLine).
Bad Destination Reputation Anomaly
A destination IP address with a bad reputation has received an anomalously large number of
connections. Investigate the connections and consider blocking the destination IP address.

XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR Intel (XTA0005)
Technique: XDR Bad Reputation (XT2010)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is dstip_bad_reps.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — destination IP address
dstip_host — destination host name
dstip_reputation — destination reputation
actual — actual number of connections to the destination IP address in the period
typical — typical number of connections to the destination IP address
srcip_host — source host name
srcip_reputation — source reputation
appid_name — application name
Use Case with Data Points
The number of connections for every destination IP address (dstip) with a bad reputation
(dstip_reputation) is calculated periodically. If a destination IP address's number of
connections (actual) is much larger than the typical historical number (typical), an alert is
triggered. The Interflow includes the source IP address making the connection (srcip_host), the
application (appid_name) used, and the reputation of the source host (srcip_reputation).
Bad Reputation Login
A successful login was observed from an IP address with a history of malicious activity. Check
with the user.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Bad Reputation (XT2010)
Tags: [External]

Event Name
The xdr_event.name for this alert type in the Interflow data is bad_reputation_login.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
srcip_reputation — source reputation (if not empty)
source_geo.countryName — source country
dstip_host — destination host name
login_type — type of login
username — user name
Use Case with Data Points
The login records are checked for every source IP address (srcip). If a source IP address has
successful login records and its reputation (srcip_reputation) is bad (except brute-forcer and
scanner), an alert is triggered. A sample Interflow includes source IP address (srcip), source
host (srcip_host), source reputation (srcip_reputation), source country
(srcip_geo.countryName), login type (login_type), and user name (username).
Bad Source Reputation Anomaly
A source IP address with a bad reputation has made an anomalously large number of
connections. Investigate the connections and consider blocking the source IP address.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Bad Reputation (XT2010)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is srcip_bad_reps.
Severity
30

Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
actual — actual number of connections in the period
typical — typical number of connections from the source IP address
dstip_host — host name of corresponding destination IP address
dstip_reputation — destination reputation
appid_name — application name
Use Case with Data Points
The number of connections for every source IP address (srcip) with a bad reputation
(srcip_reputation) is calculated periodically. If a source IP address's number of connections
(actual) is much larger than the typical historical number (typical), an alert is triggered. The
Interflow includes the application (appid_name) used and the reputation of the destination host
(dstip_reputation).
BloodHound Enumeration Activity
The BloodHound Enumeration Activity rules are used to identify potential domain enumeration
activity from BloodHound or other Active Directory data collection tools. Any one or more of these
will trigger the BloodHound Enumeration Activity alert type.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: Discovery (TA0007 )
Technique: Permission Groups Discovery (T1069 )
Sub-technique: Domain Groups (T1069.002 )
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
Carbon Black: XDR Anomaly
The Carbon Black endpoint generates an anomalously high amount of log data or a rarely seen
type of log data on the host. Investigate the device and the user, to see if this is expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)
Technique: XDR Anomaly (XT1000)
Tags: [Carbon Black]
Event Name
The xdr_event.name for this alert type in the Interflow data is carbonblack_edr_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
process.command_id
host.ip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
host.ip — device internal IP address
host.external_ip — device external IP address
actual — actual volume of log records in the period

typical — typical difference in volume of log records between this period and the
previous period
Use Case with Data Points
The number of occurrences of Carbon Black endpoint (cloud) log, based on the “UNKNOWN“
threat category (event.type), is tabulated periodically. If this category occurs (actual) much
more often compared to its history (typical) or a rarely seen type of record is observed, an alert
is triggered. The Interflow includes information such as the file name (file.name), process
(process.name), and description (xdr_event.description).
certutil.exe Certificate Extraction
The certutil.exe Certificate Extraction rules are used to identify certutil.exe certificate extraction
activity. Any one or more of these will trigger the certutil.exe Certificate Extraction alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Steal or Forge Authentication Certificates (T1649 )
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
Cloud Drive Data Exfiltration Anomaly

An account downloaded an atypical number of files over a 24-hour period. Check the user and
the targeted files.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Exfiltration (TA0010 )
Technique: Exfiltration Over Web Service (T1567 )
Sub-technique: Exfiltration to Cloud Storage (T1567.002 )
Tags: [External; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
cloud_drive_data_exfiltration_anomaly.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_username
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_username — user downloading an anomalous number of files
actual — number of downloads in the last 24 hours
typical — typical number of downloads in the last 24 hours
event_summary.cloud_drive_data_exfiltration_anomaly.downloaded_files_s
ummary — names of the downloaded files from Google Workspace, OneDrive, and
SharePoint (on a per-user basis)
Use Case with Data Points
If an unusually high number of files were downloaded from a cloud service by (srcip_username)
in a 24-hour period, an alert will be triggered. A sample Interflow record includes the user
requesting downloads (srcip_username) and a summary of what files have been downloaded
(event_summary.cloud_drive_data_exfiltration_anomaly.downloaded_files_summary).
Command & Control Reputation Anomaly
An anomalously large number of connections were made to known command and control
servers. Investigate the connections and source hosts. If malicious, block the IP addresses of the
command and control servers.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold

Tactic: XDR Intel (XTA0005)
Technique: XDR Command and Control Reputation (XT5001)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is cnc_reputation.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — destination IP address
dstip_host — destination host name
dstip_reputation — destination reputation
actual — actual number of connections in the period
typical — typical number of connections to the destination IP address with a C&C
reputation
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
appid_name — application name
Use Case with Data Points
The number of connections for every destination IP (dstip) with a command and control
reputation (dstip_reputation) is calculated periodically. If a destination IP has a much higher
number of connections (actual) than its history (typical) in any period, an alert is triggered.
The Interflow includes the application used in the connection (appid_name), the source host
(srcip_host), and the source reputation (srcip_reputation).
Command Anomaly
A command has been executed an anomalously large number of times compared to its typical
executions or those of other commands. Investigate the command and the user to determine if
this is expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Tags: [Internal]

Event Name
The xdr_event.name for this alert type in the Interflow data is command_anomaly.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
command
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
command — command executed
actual — actual number of executions in the period
typical — typical number of executions in the period
cwd — current working directory from which the command executed
hostip — host from which the command was run
hostip_host — host name
username — user name who ran the command
Use Case with Data Points
The number of times a command (command) has been executed is calculated periodically. If the
volume (actual) is much larger than the typical volume (typical) of the command or other
commands in any period, an alert is triggered. The Interflow includes the directory from which the
command was executed (cwd), the host and source IP addresses (hostip and srcip) from
which the command was executed, and the name of the user who ran the command (username).
Cryptojacking
An unauthorized coin miner used a computer to mine cryptocurrency. Consider blocking the
source IP address.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Resource Hijacking (T1496 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is cryptojacking.
Severity
70
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
srcip — source IP address of the cryptojacking action
dstip — destination IP address of the cryptojacking action
srcip_reputation — source reputation
srcip_host — source host name
dstip_reputation — destination reputation
dstip_host — destination host name
Use Case with Data Points
If an unauthorized coin miner is detected by IDS, an alert is triggered. A sample Interflow
includes the IDS signature (ids.signature), source IP address (srcip), source reputation
(srcip_reputation), source host (srcip_host), destination IP address (dstip), destination
reputation (dstip_reputation), and destination host (dstip_host).
CylanceOPTICS: XDR Anomaly
The Cylance OPTICS endpoint generates an anomalously high amount of log data or a rarely
seen type of log data on the host. Investigate the device and the user to see if this is expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)
Technique: XDR Anomaly (XT1000)
Tags: [Cylance]
Event Name
The xdr_event.name for this alert type in the Interflow data is cylance_edr_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
tenantid
event.description
host.id

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
host.name — device name
event.description — description of the detection rule
actual — actual number of log records in the period
typical — typical number of log records generated on the device
Use Case with Data Points
The number of occurrences of CylanceOPTICS log records (event.provider) is calculated
periodically. If this category occurs (actual) much more often compared to its history (typical)
or a rarely seen type of event is generated, an alert is triggered. The Interflow includes
information such as the process name (process.name), parent process name
(process.parent.name), and description (event.description).
Data Ingestion Volume Anomaly
A sensor is sending an anomalously high or low volume of data, compared to its typical volume.
Check the sensor. A low volume could indicate a sensor failure or other problems. For a high
volume, determine the cause of the increase.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: XDR SBA (XTA0003)
Technique: XDR Bytes Anomaly (XT3001)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is ade_outbytes_anomaly.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
engid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
engid — sensor ID
engid_name — sensor name
actual — actual volume of data in the period
typical — typical difference in data volume between this period and the previous
period

Use Case with Data Points
The data ingestion volume of every data sensor with sensor id (engid) and sensor name
(engid_name) is calculated periodically. If one of the following conditions is met, the anomaly is
triggered:
A moving window is used to record data ingestion volume. If the time window can be
divided into two sub windows and the metric values of these two sub windows show
large deviation
The ingestion volume is anomalously high compared to its own history
The ingestion volume is anomalously low compared to its history and it keeps being low
for a relatively longer period
A sample Interflow includes the sensor ID (engid) and sensor name (engid_name).
DCERPC SMB Spoolss Named Pipe
The DCERPC SMB Spoolss Named Pipe rules detect suspicious SMB traffic accessing Spoolss
named pipes. Any one or more of these will trigger the DCERPC SMB Spoolss Named Pipe alert
type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
DGA
A host is using a potential Domain Generation Algorithm (DGA). If the target domain is a
malicious domain, the host might be compromised. Investigate the DGA domains and the host.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Command and Control (TA0011 )
Technique: Dynamic Resolution (T1568 )
Sub-technique: Domain Generation Algorithms (T1568.002 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is dga_resolvable.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
metadata.request.effective_tld
metadata.response.resolved_ips
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host that sends the DGA queries
srcip_host — source host name
metadata.request.effective_tld — effective top-level domain of the DNS query
is_dga — flag marking whether or not the DNS query is a DGA query
actual — number of DGA domains the host has queried
Use Case with Data Points
Whenever a host (srcip) sends a DNS query (appid_name: dns) and the DNS server returns a
non-existent domain (NXDOMAIN) response (metadata.response.reply_code), the NX
domain query counter for the host is increased. We reset the counter if no NX domain queries
are observed for a period of time. When the counter reaches a certain threshold, the host is
monitored. When monitored, we run the FQDNs of all DNS queries
(metadata.response.query) sent by this host through domain generation analytics to

determine whether the domain's entropy indicates a DGA anomaly. If so, we mark the DNS
record (is_dga). If the DNS query gets a response with valid resolved IP addresses
(metadata.response.resolved_ips), we call it a resolvable query, otherwise we call it a non-
resolvable query.
If a monitored host (srcip) sends a resolvable DGA query (is_dga: yes_resolvable), we
check the effective top-level domain (metadata.response.effective_tld). If the same host
(srcip) previously sent non-resolvable DGA queries (is_dga: yes) with the same effective top-
level domain (metadata.response.effective_tld), the host is considered to have a high risk
of being compromised and performing C&C with DGA. The Interflow includes the source host
(srcip), DNS query (metadata.response.query), query effective top-level domain
(metadata.response.effective_tld), and DGA flag (is_dga).
DHCP Server Anomaly
A new DHCP server appeared in the network. This could be a hacker attempting to steer traffic.
Investigate and consider telling employees to avoid this server.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Server Anomaly (XT2007)
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is dhcp_anomaly.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
metadata.response.server_ip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.response.server_ip — IP address of the anomalous DHCP server
dstip — IP address of the anomalous DHCP destination
engid — sensor that reported the DHCP traffic
srcip_host — host name that visited the suspicious DHCP server
srcip_geo.countryName — country name of the source that visited the suspicious
DHCP server
Use Case with Data Points

If a DHCP server that has never been seen before appears in the network, an alert is triggered.
The Interflow includes the destination IP address (dstip), destination host (dstip_host), source
host (srcip_host), and source country (srcip_geo.countryName).
DNS Query to Anonymous File Upload Domains
The DNS Query to Anonymous File Upload Domains rules are used to identify DNS queries to
anonymous file upload platform domains often used for malicious purposes. Any one or more of
these will trigger the DNS Query to Anonymous File Upload Domains alert type.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Exfiltration (TA0010 )
Technique: Exfiltration Over Web Service (T1567 )
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
Tactic: Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
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
Tactic: Impact (TA0040 )
Technique: Resource Hijacking (T1496 )
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
Tactic: Exfiltration (TA0010 )
Technique: Proxy (T1090 )
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
DNS Tunneling Anomaly
An anomalously large number of connections tunneling high-entropy traffic through DNS were
made. This can indicate data exfiltration. Investigate the tunnel and source host. If malicious,
block the source host.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Exfiltration (TA0010 )
Technique: Exfiltration Over Alternative Protocol (T1048 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is dns_tunnel.
Severity
98
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.effective_tld
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address

metadata.request.effective_tld — effective top-level domain, such as yahoo.com
metadata.request.query — DNS query
actual — actual number of bytes transmitted through the tunnel in the period
typical — typical number of bytes transmitted through a tunnel in the period
total_entropy — total entropy (information density) sent by the DNS tunnel
query_count — number of queries sent by the DNS tunnel
Use Case with Data Points
The DNS queries (metadata.requests.query) for each DNS tunnel (comprising the source
host (srcip_host), destination host (dstip), and top-level domain (effective_tld)) are
analyzed periodically. If a DNS tunnel has sent anomalously more entropy (total_entropy) and
bytes (actual) than is normal (typical) in any period, an alert is triggered. The number of
queries sent (query_count) is also considered.
Dormant Account Anomaly
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
A user account has not logged any interactive actions such as logins, password changes, or
resource accesses recently. Check the user account and consider disabling it.
 N ote the following:
The data sources for the interactive actions are Active Directory, Microsoft Entra ID
(formerly Azure AD), and Office365.
For a user account to be eligible for dormant account alerts, sufficient historical
interactive activity must be present to establish a baseline of prior activity.
Reminder alerts are sent only if the user has a long history. There can be up to 3
alerts per user (at 14, 21, and 28 days), after which there will be no further alerts
unless the user stops being dormant.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] Persistence (TA0003 )
Technique: Valid Accounts (T1078 )
Tags: [Identity Detection]
XDR Event Name
The xdr_event.name for this alert type in the Interflow data is dormant_account.
Severity
30
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_username
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_username — source user name
days_silent — number of days since last activity
last_seen_ts — timestamp when the user last logged interactive data
Use Case with Data Points
If an account is observed to be dormant, an alert is triggered. The Interflow will contain a user
name (srcip_username), the number of days since an interactive action was logged
(days_silent), and the last seen timestamp (last_seen_ts) for that user.
Validation / Remediation
Analysts can validate the alert by checking whether activity is expected from that user. They can
disable the account if it is not supposed to be dormant.
Potential False Positives
A false positive could be generated if some user activity is not counted as interactive.
Emerging Threat
An emerging threat has been observed. Investigate the IP address, domain name, URL, or file
hashes (MD5, SHA1, SHA256) and consider blocking.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR Intel (XTA0005)
Technique: XDR Emerging Threat (XT5003)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is emerging_threat.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
domain_list

url_list
file.threat_indicator.file.hash.md5
event_summary.process_list_hash.md5
event_summary.file_list_hash.md5
process.parent.threat_indicator.file.hash.md5
process.threat_indicator.file.hash.md5
file.threat_indicator.file.hash.sha1
event_summary.process_list_hash.sha1
event_summary.file_list_hash.sha1
process.parent.threat_indicator.file.hash.sha1
process.threat_indicator.file.hash.sha1
file.threat_indicator.file.hash.sha256
event_summary.process_list_hash.sha256
event_summary.file_list_hash.sha256
process.parent.threat_indicator.file.hash.sha256
process.threat_indicator.file.hash.sha256
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address marked as an emerging threat
srcip_host — host name of corresponding source IP address
dstip — destination IP address marked as an emerging threat
dstip_host — host name of corresponding destination IP address
url_list — URL marked as an emerging threat
domain_list — domain marked as an emerging threat
event_summary.detected_hashes.md5 — MD5 hash marked as emerging threat
event_summary.detected_hashes.sha1 — SHA1 hash marked as emerging threat
event_summary.detected_hashes.sha256 — SHA256 hash marked as emerging
threat
event_summary.detected_file_names — detected file names with matched hash
value
event_summary.detected_process_names — detected process names with matched
hash value
event_summary.ioc_source_repu_summary.url_reputation — URL reputation
event_summary.ioc_source_repu_summary.srcip_reputation — source
reputation
event_summary.ioc_source_repu_summary.dstip_reputation — destination
reputation
event_summary.ioc_source_repu_summary.domain_reputation — domain
reputation

event_summary.ioc_source_repu_summary.filehash_reputation — hash
reputation
Use Case with Data Points
Stellar Cyber monitors traffic for emerging threats. This alert type has file hash detection that
monitors traffic, Syslog, and Windows events.
An alert is triggered if emerging threats are observed in any of the following:
Source IP address (srcip)
Destination IP address (dstip)
URL (url_list)
Domain (domain_list)
MD5 file hash (event_summary.detected_hashes.md5)
SHA1 file hash (event_summary.detected_hashes.sha1)
SHA256 file hash (event_summary.detected_hashes.sha256)
Note that only one of these is needed to trigger the alert. So, although the Interflow includes the
source IP address (srcip), destination IP address (dstip), URL (url_list), domain
(domain_list), and file hashes (event_summary.detected_hashes.md5,
event_summary.detected_hashes.sha1, and event_summary.detected_hashes.256), not all
the values may be populated, depending on the nature of the observed threat.
Encoded PowerShell
A Windows host executed an encoded PowerShell script. Investigate the script contents to see if
it is malicious. If so, consider quarantining the host.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Tags: [PowerShell]
Event Name
The xdr_event.name for this alert type in the Interflow data is encoded_powershell.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the Windows host

hostip_host — host name
event_data.ContextInfo — PowerShell script context
event_data.Payload — PowerShell script payload
Use Case with Data Points
If a Windows host (srcip) executes a PowerShell script whose context
(event_data.ContextInfo) includes flags that indicate encoding or obfuscation of the script, an
alert is triggered. The Interflow includes the IP address of the Windows host (srcip), the script
context (event_data.ContextInfo), and script payload (event_data.Payload).
Rule Based Detection
The Encoded PowerShell rules are used to identify when a Windows host executed an encoded
PowerShell script. Any one or more of these will trigger the Encoded PowerShell alert type.
The rule-based detection is the same as the Encoded PowerShell alert type above, with the
following difference:
The detection_flag is a Stellar Cyber enriched field:
2100: Encoded PowerShell
2101: Encoded PowerShell with hidden flag
Link to Rule-Based Alert Types
Rules Contributing to Encoded PowerShell Alert Type
Encrypted C&C
A connection to or from known command and control servers was observed in encrypted traffic.
Consider blocking the source IP address.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Command and Control (TA0011 )
Technique: Encrypted Channel (T1573 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is ssl_certificate.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the connection
dstip — destination IP address of the connection
srcip_host — host name of corresponding source IP address
srcip_geo.countryName — source country of the connection
dstip_host — host name of corresponding destination IP address
dstip_geo.countryName — destination country of the connection
Use Case with Data Points
If known command and control servers are detected on either side of a connection with
encrypted traffic, an alert is triggered. The Interflow includes the source IP address (srcip),
source host (srcip_host), source country (srcip_geo.countryName), destination IP address
(dstip), destination host (dstip_host), and destination country (dstip_geo.countryName).
Exploited C&C Connection
An exploited host with vulnerabilities initiated a connection to the exploit attacker, which could
indicate the host being compromised and performing C&C activities. See if the exploit was
successful. Check the source host, and consider blocking.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Command and Control Connection Exploitation (XT2014)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is exploit_attempt_correlation.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
exploit_attempt record’s srcip, dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
tenant_id — tenant ID
exploit_id — ID of the original exploit event
seen_traffic_id — ID of the original Interflow traffic record
srcip (of exploit event) — IP address of the attacker (correlation_info.srcip)
dstip (of exploit event) — IP address of the target host (correlation_info.dstip)
srcip (of traffic record) — IP address of the target host (correlation_info.srcip)

dstip (of traffic record) — IP address of the attacker (correlation_info.dstip)
Use Case with Data Points
Two events are involved in this alert type. In the first event, an attacker (srcip) with the IP
address A is performing an exploit against a target (dstip) with the IP address B. If, following
that event, an Interflow traffic record is observed where the target host (srcip) with IP address B
initiates a network connection to the attacker (dstip) whose IP address is A, an alert is triggered.
When an alert is triggered a new correlation event is generated. The Interflow of the correlation
event includes the reference ID of the exploit event (exploit_id), the reference ID of the traffic
record (seen_traffic_id), the IP address of the attacker (correlation_info.srcip of the
exploit event or correlation_info.dstip of the traffic record), the IP address of the victim
(correlation_info.dstip of the exploit event or correlation_info.srcip of the traffic
record).
External Account Login Failure Anomaly
An anomalously large number of user login failures was observed for an account. Check with the
user.
This alert type has the following subtypes:
Office 365 / Entra ID
Windows Security Events
VPN Logon Events

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_cloud_account_login_failure.
Severity
45
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — cloud account user ID
or
srcip_username — cloud account user name
 The key field for this alert type can be either srcip_usersid or srcip_username,
depending on the data feed.
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
Use Case with Data Points
Login failures and successes are calculated periodically for every account (srcip_usersid). If
the number of failures is significantly larger than the number of successes, an alert is triggered. A
sample Interflow includes the login type (login_type), source host (srcip_host), and source
reputation (srcip_reputation).
Alert Subtype: Office 365 / Entra ID
The Office 365 / Entra ID alert subtype is the same as the External Account Login Failure
Anomaly alert type above, with the following differences:
The subtype is for data sources from Office 365 and Microsoft Entra ID (formerly Azure
AD).
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_cloud_account_login_failure_o365_azure.
Alert Subtype: Windows Security Events
The Windows Security Events alert subtype is the same as the External Account Login Failure
Anomaly alert type above, with the following differences:
The subtype is for data sources from all Windows security events.

The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_cloud_account_login_failure_windows.
Alert Subtype: VPN Logon Events
The VPN Logon Events alert subtype is the same as the External Account Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from all VPN logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_cloud_account_login_failure_vpn.
The supported VPNs are FortiGate, Check Point, and Palo Alto Networks Panorama.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Brute-Forced Successful User Login
A successful login was observed from an IP address that had previously seen a large number of
login failures, or a successful login to a user account was observed from another IP address or
IP addresses that had previously seen a large number of login failures to that account. Check
with the user.
This alert type has the following subtypes:
Source IP Based
User ID Based
 This alert type has a relatively long detection delay of up to 40 minutes because it waits for
login events from high latency data sources and is sensitive to the event order of user
logins.
XDR Kill Chain

Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_user_success_brute_forcer.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
srcip_usersid
Alert Subtype: Source IP Based
The source IP-based alert subtype has the same XDR Kill Chain as the user ID-based alert
subtype, but differs in the Key Fields and Relevant Data Points and Use Case with Data
Points.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_success_brute_forcer_srcip.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_usersid — Windows SID associated with the source IP address
srcip_host — source host name
srcip_reputation — source reputation
source_geo.countryName — source country
dstip_host — destination host name
login_type — type of login
username — user name
related_alert._id — link to the related External User Login Failure Anomaly
Use Case with Data Points
The login records are checked for every external source IP address (srcip). An alert is triggered
if that IP address:
1. Has so many failed login attempts that it triggered the External User Login Failure
Anomaly, and
2. Had a successful login

A sample Interflow includes the source IP address (srcip), login type (login_type), source host
(srcip_host), source reputation (srcip_reputation), source country
(srcip_geo.countryName), and user name (username).
Alert Subtype: User ID Based
The user ID-based alert subtype has the same XDR Kill Chain as the source IP-based alert
subtype, but differs in the Key Fields and Relevant Data Points and Use Case with Data
Points.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_success_brute_forcer_srcip_usersid.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — Windows SID associated with the source IP address
srcip — source IP address
srcip_host — source host name
srcip_reputation — source reputation
source_geo.countryName — source country
dstip_host — destination host name
login_type — type of login
username — user name
related_alert._id — link to the related External Account Login Failure Anomaly
Use Case with Data Points
The login records to a user account (srcip_usersid) are checked for every external source IP
address (srcip). An alert is triggered if that user account:
1. Has so many failed login attempts that it triggered the External Account Login Failure
Anomaly, and
2. Had a successful login
A sample Interflow includes the source IP address (srcip), login type (login_type), source host
(srcip_host), source reputation (srcip_reputation), source country
(srcip_geo.countryName), and user name (username).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.

Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Credential Stuffing
An anomalously large amount of username/password testing was observed on AWS, Okta, or
Windows. Check the activity after successful logins, and consider blocking the source IP
addresses.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_credential_stuffing.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
msg_class
service_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
msg_class — name of the service: cloudtrail for AWS, okta for Okta, Microsoft-
Windows-Security-Auditing for Windows
service_id — specific account ID of a service
login_failure_rate — rate of login failures per minute in the period
unknown_users_rate — rate of unknown user names per minute in the period
unknown_users_to_login_failures — ratio of unknown user names to login failures
in the period
suspicious_ips — suspicious source IP addresses (up to 100)
possible_breached_ips — list of malicious IP addresses that may have successful
breach activities

Use Case with Data Points
External credential stuffing is the constant testing of username/password combinations on the
AWS, Okta, or Windows authentication functions. Login activity is monitored and if the number of
failed logins is larger than normal for that service, an alert is triggered. The Interflow includes the
service (msg_class), tenant's account ID on that service (service_id), suspicious source IP
address (suspicious_ips), login failure rate (login_failure_rate), unknown user rate
(unknown_users_rate), the ratio of unknown users to login failures
(unknown_users_to_login_failures), and a list of source IP addresses that might have
suspicious activities and should be investigated (possible_breached_ips).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Exploited Vulnerability
A host with a vulnerability discovered by a security scanning tool was exploited by an attack on
that same vulnerability, indicating a high probability of success. Check the target to see if it was
compromised.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Exploited Vulnerability (XT2015)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_vuln_exploit_correlation.

Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
scan_record’s srcip, dstip, ids.cve
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
tenantid — tenant ID
vulnerability_id — ID of the original security scan result
ids_event_id — ID of the original IDS exploit event
srcip (of security scan result) — IP address of the target correlation_info.srcip
dstip (of IDS event) — IP address of the target (correlation_info.dstip)
srcip (of IDS event) — IP address of the attacker (correlation_info.srcip)
vulnerability.cve — CVE associated with the reported vulnerability
ids.cve — CVE the attacker used to exploit the host
Use Case with Data Points
An attacker (srcip) with IP address A is performing an exploit against a target (dstip) with
internal IP address B using a vulnerability (ids.cve) with CVE x. If any security scanning tool
found the target (srcip) with IP address B to have a vulnerability (vulnerability.cve) with
CVE x, an alert is triggered.
When an alert is triggered, a new correlation event is generated. The Interflow of the correlation
event includes the ID of the IDS exploit event (ids_event_id), the ID of the security scan record
(vulnerability_id), the IP address of the attacker (correlation_info.srcip of the IDS
event), the IP address of the victim (correlation_info.dstip of the IDS event or
correlation_info.srcip of the security scan record), and the CVE that was used in the
exploit (vulnerability.cve and ids.cve).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an

INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Firewall Denial Anomaly
A source host had actions blocked by a firewall too many times. Investigate the firewall rules that
were violated. If suspicious, block the source IP address.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Firewall Anomaly (XT2002)
Tags: [External; Firewall Anomalies; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_fw_action.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_host
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source host IP address
srcip_host — source host IP address
actual — actual number of firewall denials in the period
typical — typical number of firewall denials in the period
dstip_host — host name of corresponding destination IP address
dev_name — name of the firewall
engid_name — name of the sensor
Use Case with Data Points
The number of firewall denials for every source IP address (srcip) is calculated periodically. If a
source IP address’s number of firewall denials (actual) is much larger than the historical count
(typical) of all IP addresses, an alert is triggered. The Interflow includes the name of the
firewall (dev_name), the name of the sensor (engid_name), and the destination host
(dstip_host).
More on Internal versus External and Inbound vs Outbound...

Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Firewall Policy Anomaly
A firewall policy was triggered that has never been seen before (or has very rarely been seen).
Investigate the policy, the intent, and the associated traffic to determine whether this activity is
legitimate or malicious.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Firewall Anomaly (XT2002)
Tags: [External; Firewall Anomalies; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_fw_policy_id.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
fw_policy_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
fw_policy_id — ID of the violated firewall policy
days_silent — number of days since this firewall policy was last seen

srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
dev_name — device name
dev_type — device type
engid_name — sensor name
Use Case with Data Points
A firewall policy ID (fw_policy_id), which is raised by a device (dev_name and dev_type) and
captured by a sensor (engid_name), shows never seen or very rare (days_silent) traffic
between a host (srcip_host) and another host (dstip_host). This will trigger an alert.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Handshake Failure
There were too many handshake failures between two hosts, which might indicate port scanning.
Check the source host to see if this was expected and, if not, consider blocking the host.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_handshake_failure.
Severity

10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
appid_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host with the handshake failures
srcip_host — source host name
dstip — destination IP address of the host with the handshake failures
dstip_host — destination host name
timestamp — when the scan happened
Use Case with Data Points
If a host (srcip) scans across many ports on another host (dstip), an alert is triggered. The
Interflow includes the IP address of the potential attacker (srcip), the IP address of the victim
(dstip), a special message flag (msgtyp), and when the scan happened (timestamp).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External IDS Signature Spike
A source IP address transmitted an anomalous number of different IDS signatures. Typically, this
indicates host penetration or vulnerability scanning.

XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_ids_signature_spike.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ids_signatures_summarize — summarized IDS signatures of the
exploit
srcip_host — source host name
actual — actual number of unique IDS signatures in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IDS signatures from the source IP address, with
critical IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
Use Case with Data Points
The number of unique IDS signatures (ids.signature), weighted by their severity
(ids.severity), are calculated periodically. If many different exploits with unique IDS signatures
are observed, an alert is triggered. The Interflow includes a source (srcip), timestamp, an
accumulated severity of IDS signatures (actual), the usual accumulated severity of IDS
signatures (typical), and a sampling of the IDS signatures used in the attack
(ids_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).

Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External IP / Port Scan Anomaly
A host has either generated an anomalous number of connections compared to the typical
amount, or has triggered an anomalous number of connection failure responses, in the
measured interval. This can indicate that an attacker is scanning for computers or ports to
exploit. If the source IP address is internal targeting an external address, check with the user. If
the source IP address is external targeting any addresses, it could be a scanning campaign.
This alert type has the following subtypes:
Connection Failure Anomaly (Sensor Traffic)
Connection Spike Anomaly (Firewall / Windows Traffic)
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_port_scan.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Alert Subtype: Connection Failure Anomaly (Sensor Traffic)
The xdr_event.subtype.name for this alert subtype in the Interflow data is
connection_failure_anomaly.
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
num_failed — unique number of (destination IP and destination port) tuples that
respond with failed status
num_successful — unique number of (destination IP and destination port) tuples that
respond with success status
percent_failed — percent of unique (destination IP and destination port) tuples that
respond with failed status
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
dstip_host — host name of corresponding destination IP address
appid_name — application name
summary_port_scan_type — port scan type
Example of Event Summarization in the Alert Description
Within a 5.0-minute period the overall traffic from 10.1.1.1 consisted of the following scans:
64.94% to 10.2.1.26/31 on port(s) ranging from 2 to 49157, 35.06% to 10.2.1.28/30 on port(s)
ranging from 1 to 49157.
Use Case with Data Points
For every unique triplet (source IP address, destination IP address, and destination port)
browsed by each source IP address (srcip), the number of response failures and successes is
calculated periodically. If the number of failures is significantly larger than the number of
successes, an alert is triggered. The Interflow includes the source host (srcip_host),
destination host (dstip_host), and application name (appid_name).
Considering that a lateral scan (private to private) is more sensitive than a non-lateral scan, this
alert type is divided into two parts. One focuses on lateral scan analysis, the other focuses on
non-lateral scan analysis. The mechanism remains the same as before, with the trigger condition
for lateral scan alert being more sensitive than non-lateral one.
Validation / Remediation
If the source IP address is internal targeting an external address, check with the user if they are
aware of the activity or if they are authorized to perform the activity. Inform the user's supervisor
if the activity is unauthorized.
If the source IP address is external targeting any addresses, check the reputation of the source
IP address as in known malicious/scanner.
Potential False Positives
Some legitimate activities such as vulnerability scans or penetration testing may trigger this alert
type, if from an external IP address to an internal IP address.
Alert Subtype: Connection Spike Anomaly (Firewall / Windows Traffic)

The xdr_event.subtype.name for this alert subtype in the Interflow data is
connection_spike_anomaly.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_port_scan_tsa.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
actual — actual number of connections to the destination IP address in the time period
typical — typical number of connections to the destination IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
summary_port_scan_type — port scan type
Example of Event Summarization in the Alert Description
Within a 5.0-minute period the overall traffic from 10.1.1.1 consisted of the following scans:
64.94% to 10.2.1.26/31 on port(s) ranging from 2 to 49157, 35.06% to 10.2.1.28/30 on port(s)
ranging from 1 to 49157.
Use Case with Data Points
For every unique (destination IP address and destination port) browsed by each source IP
address (srcip), the number of response failures and successes and the number of total data
volume are calculated periodically. If the total data volume is significantly larger than the typical
number, an alert is triggered. The Interflow includes the source host (srcip_host), destination
host (dstip_host), and application name (appid_name).
Considering that a lateral scan (private to private) is more sensitive than a non-lateral scan, this
alert type is divided into two parts. One focuses on lateral scan analysis, the other focuses on

non-lateral scan analysis. The mechanism remains the same as before, with the trigger condition
for lateral scan alert being more sensitive than non-lateral one.
Validation / Remediation
If the source IP address is internal targeting an external address, check with the user if they are
aware of the activity or if they are authorized to perform the activity. Inform the user's supervisor
if the activity is unauthorized.
If the source IP address is external targeting any addresses, check the reputation of the source
IP address as in known malicious/scanner.
Potential False Positives
Some legitimate activities such as vulnerability scans or penetration testing may trigger this alert
type, if from an external IP address to an internal IP address.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Non-Standard Port Anomaly
An application had an anomalously large number of connections or a rarely seen connection on
non-standard ports. Check the application to be sure this is benign.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] Command and Control (TA0011 )
Technique: Non-Standard Port (T1571 )
Tags: [External; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is
external_non_std_port_anomaly.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
dstport
appid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — destination IP address
dstport — destination port
appid — application ID
days_silent — number of days since the application was last seen
appid_name — application name
dstip_host — host name of corresponding destination IP address
actual — actual number of connections in the period
typical — typical number of connections in the period
Use Case with Data Points
The number of connections for an application (dst_ip + dstport + appid) is calculated
periodically. If a non-standard combination has an actual number of connections (actual) that is
much larger than the typical number of connections (typical), or the combination has not
appeared for a long time, an alert is triggered. The Interflow includes the source host
(srcip_host), destination IP address (dstip), destination port (dstport), application ID
(appid), and application name (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead

list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Other Malware
Malware with uncategorized malicious activity was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] XDR Malware (XTA0006)
Technique: XDR Miscellaneous Malware (XT6001)
Tags: [External; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_malware_activity.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
ids.severity — severity of the IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the malware

event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates malware that cannot be categorized as ransomware, spyware,
trojan, PUA, or adware, an alert is triggered. A sample Interflow includes malicious activity for
sandbox (maltrace-cloud.data.malicious_activity), IDS signature for ML-IDS
(ids.signature), event source (event_source), source host (srcip_host), source country
(srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the malware (file_name) from
the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Password Spraying
.An anomalously large number of failed logins with unknown user names was observed on
external Windows authentication services. Check the activity after successful logins, and
consider blocking the source IP addresses.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Sub-technique: Password Spraying (T1110.003 )
Tags: [External; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_password_spray.

Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.Workstation
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address generating a failed login
or
event_data.Workstation — workstation generating a failed login
 The key field for this alert type can be either srcip or event_data.Workstation,
depending on the data feed.
srcip_host — source host name
event_id — Windows event ID corresponding to the login failures
login_type — type of login protocol; the available values vary by event_id
actual — actual number of failed logins with unknown user names in a 5-minute period
typical — typical number of failed logins with unknown user names in a 5-minute
period
event_summary.password_spray_user_summary — list of up to 100 unknown user
names associated with the failed logins (the first three are shown in the alert
description)
Use Case with Data Points
If a potential password spraying attack is observed, an alert is triggered. The Interflow includes a
source (srcip or event_data.Workstation), timestamp, the type of login (login_type), the
number of failed logins (actual), the usual number of failed logins (typical), and a sampling of
the user names used in the attack (password_spray_user_summary).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.

Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External PII Leaked
Personally identifiable information (social security numbers or credit cards) has been observed in
the clear. Check the source to see if it is compromised. If so, consider blocking it.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Exfiltration (TA0010 )
Technique: Automated Exfiltration (T1020 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_pii_leak.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the PII leak
dstip — destination IP address of the PII leak
ids.signature — IDS signature
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
If a personally identifiable information leak is detected by IDS, an alert is triggered. A sample
Interflow includes the IDS signature (ids.signature), source IP address (srcip), destination IP
address (dstip), source host (srcip_host), and destination host (dstip_host).

More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Plain Text Passwords Detected
A plain text password was detected in unencrypted traffic. Check with the user.
This alert type looks for the presence of metadata.request.password,
metadata.request.auth_password, and metadata.request.auth_simple in the Interflow
records from the sensors. When plain text passwords are present in the network traffic, the
sensors are able to decode and create the corresponding Interflow fields. To preserve privacy,
the actual passwords are replaced by a sequence of asterisks (*).
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Clear Password (XT2006)
Tags: [External; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_clear_password.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
actual — actual number of connections with a plain text password in the period
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
Use Case with Data Points
If there are plain text passwords in unencrypted traffic records with a public source IP address
(srcip) or destination IP address (dstip), an alert is triggered. A sample Interflow includes the
source IP address (srcip), destination IP address (dstip), source host (srcip_host),
destination host (dstip_host), and application (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Protocol Account Login Failure Anomaly
An anomalously large number of login failures over SMB or FTP was observed. Check with the
user.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; Network Traffic Analysis; Identity Detection]

Event Name
The xdr_event.name for this alert type in the Interflow data is
external_protocol_account_login_failure.
Severity
35
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.username
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.request.username — user name in the HTTP connection request
event_summary.total_failed — number of failed logins in the period
event_summary.total_successful — number of successful logins in the period
event_summary.total_fail_ratio — percent of failed logins in the period, which is:
event_summary.total_failed / (event_summary.total_failed +
event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
appid_name — application name
login_type — type of login
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
Use Case with Data Points
For every user name (metadata.request.username) in the HTTP connections names (that do
not begin with "Mozilla" or "Aella"), the number of failed and successful logins are calculated
periodically. If the number of failed logins is much greater than successful logins, an alert is
triggered. The Interflow includes the application name (appid_name), login type (login_type),
source host (srcip_host), and source reputation (srcip_reputation).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.

Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External PUA
Unwanted applications or malware that bombards the user with advertisements has been
observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] XDR Malware (XTA0006)
Technique: XDR PUA (XT6002)
Tags: [External; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_pua.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country

file_name — name of the file that carries the PUA
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates potentially unwanted applications (PUA), an alert is triggered. A
sample Interflow includes malicious activity for sandbox (maltrace-
cloud.data.malicious_activity) or IDS signature for ML-IDS (ids.signature), along with
event source (event_source), source host (srcip_host), source country
(srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the PUA (file_name) from the
sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Ransomware
Malware that prevents you from accessing your system or files and demands ransom payment in
order to regain access was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Impact (TA0040 )
Technique: Data Encrypted for Impact (T1486 )
Tags: [External; Malware; Ransomware]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_ransomware.
Severity

80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the ransomware
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates ransomware, an alert is triggered. A sample Interflow includes
malicious activity for sandbox (maltrace-cloud.data.malicious_activity), IDS signature for
ML-IDS (ids.signature), event source (event_source), source host (srcip_host), source
country (srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the ransomware (file_name)
from the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.

Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External RDP BlueKeep
Use of a scanner by zerosum0x0 that discovers targets vulnerable to BlueKeep (CVE-2019-
0708) has been observed. Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [External] Privilege Escalation (TA0004 )
Technique: Exploitation for Privilege Escalation (T1068 )
Tags: [External; RDP; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_rdp_bluekeep.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
ids.signature
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
srcip_host — source host name
dstip_host — destination host name
Use Case with Data Points
If the scanner by zerosum0x0 is used, an alert is triggered. A sample Interflow includes the IDS
signature (ids.signature), source host (srcip_host), and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow

as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External RDP Brute Force Attack
An anomalously large number of RDP connections to an RDP server was observed. Check the
source IP addresses to determine whether they are unknown or malicious, and monitor any
successful RDP logins.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; RDP; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_rdp_brute_force.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — IP address of the destination RDP server
dstip_host — destination host name
actual — actual number of RDP connections to the destination IP address in the
observed time bucket

typical — typical number of RDP connections to the destination IP address in most
time buckets
srcip — source IP address
srcip_host — source host name
Use Case with Data Points
RDP connection activity is monitored and the number of connections are calculated periodically.
If the number of connections to an RDP server (actual) is much greater than normal (typical),
an alert is triggered. A sample Interflow includes the destination IP address (dstip) and source
IP address (srcip).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External RDP Suspicious Outbound
Non-standard tools connecting to TCP port 3389 were observed. Check the IP address and block
if necessary.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR App Anomaly (XT2003)
Tags: [External; RDP; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_rdp_suspicious_outbound.
Severity

60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host that connects to TCP port 3389 with a non-
standard tool
srcip_host — source host name
process_name — process name
Use Case with Data Points
Connections to TCP port 3389 are monitored, and if non-standard tools connect, an alert is
triggered. A sample Interflow includes the source IP address (srcip) and the process name
(process_name). The following are the standard tools:
mstsc.exe
RTSApp.exe
RTS2App.exe
RDCMan.exe
ws_TunnelService.exe
RSSensor.exe
RemoteDesktopManagerFree.exe
RemoteDesktopManager.exe
RemoteDesktopManager64.exe
mRemoteNG.exe
mRemote.exe
Terminals.exe
spiceworks-finder.exe
FSDiscovery.exe
FSAssessment.exe
MobaRTE.exe
chrome.exe
thor.exe
thor64.exe
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).

Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Scanner Behavior Anomaly
An anomalously large amount of scanning behavior or a rarely seen scan behavior was found.
Cross-check with the IP / Port Scan Anomaly alert.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_scan_anomalies.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address

appid_name — application name
Use Case with Data Points
The number of occurrences of each scanner, based on IDS signature (ids.signature), is
calculated periodically. If one scanner occurs (actual) much more often than its history
(typical), an alert is triggered. The Interflow includes information such as the traffic application
type (appid_name), source (srcip_host), and destination (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SMB Read Anomaly
An IP address sent an anomalously large number of read requests to SMB protocol based
service(s). Investigate the files that the IP address tried to read. If suspicious, block the source IP
address.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; SMB; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_smb_read_anomaly.
Severity
15
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
actual — actual number of SMB reads from the source IP address in the period
typical — typical number of SMB reads from other source IP addresses in the period
dstip_host — destination host name
smb_username — SMB user name
event_summary.smb_path_list — folders experiencing a high volume of SMB read
requests (the first three are shown in the alert description)
Use Case with Data Points
The number of SMB read requests for every source IP address (srcip) is calculated periodically.
If a source IP address’s number of SMB reads (actual) is much larger than the typical number
(typical) and that of other IP addresses in any period, an alert is triggered. The Interflow
includes the SMB user (smb_username) and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SMB Username Enumeration
At least 5 different users SMB login attempts and 1 denied attempt or at least 10 different users
SMB login attempts, were observed from the same source. Check the source IP address. If
malicious, consider blocking it.

XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; SMB; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_smb_user_scan.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
actual — actual unique SMB user count
typical — SMB user count threshold
smb_username_set — all SMB login user names
Use Case with Data Points
If one source IP address (srcip) has several SMB login attempts with (1) at least 5 unique user
names and at least 1 denied attempt or (2) at least 10 unique user names, an alert is triggered. A
sample Interflow includes the source IP address (srcip), source host (srcip_host), destination
host (dstip_host), and all the user names (smb_username_set).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead

list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SMB Write Anomaly
An IP address sent an anomalously large number of SMB write requests. Investigate the files
that the IP address tried to write. If suspicious, block the source IP address.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Impact (TA0040 )
Technique: Data Manipulation (T1565 )
Tags: [External; SMB; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_smb_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host name
actual — actual number of SMB writes in the period
typical — typical number of SMB writes in the period
dstip_host — destination host name
smb_username — SMB user name
event_summary.smb_path_list — folders experiencing a high volume of SMB write
requests (the first three are shown in the alert description)
Use Case with Data Points
The number of SMB write requests for every source IP address (srcip_host) is calculated
periodically. If a source IP address’s number of SMB writes (actual) is much larger than the
typical number (typical) and that of other IP addresses in any period, an alert is triggered. The
Interflow includes the SMB user (smb_username) and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...

Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Spyware
Malware that collects and shares information about a device without consent was observed.
Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] XDR Malware (XTA0006)
Technique: XDR Spyware (XT6003)
Tags: [External; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_spyware_activity.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the spyware
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates spyware activity, an alert is triggered. A sample Interflow includes
malicious activity for sandbox (maltrace-cloud.data.malicious_activity), IDS signature for
ML-IDS (ids.signature), event source (event_source), source host (srcip_host), source
country (srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the spyware (file_name) from
the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SQL Anomaly
An IP address sent an anomalously large number of queries to one or more SQL servers.
Investigate the queries. If suspicious, block the source IP address.
XDR Kill Chain

Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Database; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_mysql_anomaly.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host name
srcip_geo.countryName — name of the source country
actual — actual number of SQL queries in the period
typical — typical number of SQL queries from the source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of SQL queries for every source IP address (srcip_host) is calculated periodically.
If a source IP’s SQL query count (actual) is much larger than the typical count (typical) and
that of other IP addresses in any period, an alert is triggered. The source IP’s country is
(srcip_geo.countryName). The Interflow includes the destination host (dstip_host) the source
IP visits.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an

INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SQL Dumpfile Execution
The SQL dumpfile command was observed. This command is commonly used to dump
database content or query output to a file on disk. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [External] Collection (TA0009 )
Technique: Data Staged (T1074 )
Tags: [External; Database; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_sql_db_dump.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
actual — number of SQL dumpfile queries
srcip_host — source host name
source_geo.countryName — source country
dstip_host — destination host name
Use Case with Data Points
If the SQL dumpfile command is seen on any source IP address (srcip), an alert is triggered. A
sample Interflow includes the source IP address (srcip), source host (srcip_host), source
country (srcip_geo.countryName), destination host (dstip_host), and number of SQL
dumpfile queries in the period (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow

as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SQL Shell Command
Shell commands were observed over a SQL connection, which is a common way hackers try to
gain shell access over vulnerable SQL applications. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_database_command.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
dstip — destination IP address
srcip_host — source host name

srcip_reputation — source reputation
dstip_host — destination host name
dstip_reputation — destination reputation
metadata.request.query — SQL query command
actual — number of query records from one source to one destination in one period
Use Case with Data Points
For SQL query records, if special commands (such as select mylab_sys_exec) are found, an
alert is triggered. A sample Interflow includes the source IP address (srcip), destination IP
address (dstip), source host (srcip_host), source reputation (srcip_reputation), destination
host (dstip_host), destination reputation (dstip_reputation), and SQL query records
(metadata.request.query).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Suspected Malicious User Agent
An external HTTP connection was made by a user agent that has been identified as potentially
malicious. Investigate the connection's destination.
This alert type has the following subtypes:
Predicted Malicious Agent
Known Malicious Agent Match
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR User Agent Anomaly (XT2012)

Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
external_suspected_malicious_user_agent.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.user_agent
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
user_agent.original — user agent in the HTTP connection request
metadata.request.user_agent — user agent in the HTTP connection request
stellar.confidence — model's confidence in the prediction
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
Use Case with Data Points
If a seen user agent is identified as suspicious, an alert is triggered. The alert includes the
suspicious user agent (metadata.request.user_agent), confidence (stellar.confidence),
tenant (tenant_name), source IP (srcip), and destination IP (dstip) in the key fields.
Additionally, the confidence level of the model is displayed in the alert description in a pop-up
box.
Alert Subtype: Predicted Malicious Agent
The Predicted Malicious Agent alert subtype is the same as the External Suspected Malicious
User Agent alert type above, with the following differences:
The stellar.anomaly_tag is predicted_external.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_suspected_malicious_user_agent.
It is triggered by a machine learning classifier.
Alert Subtype: Known Malicious Agent Match
The Known Malicious Agent Match alert subtype is the same as the External Suspected
Malicious User Agent alert type above, with the following differences:
The stellar.anomaly_tag is known_external.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_suspected_malicious_user_agent_known_malicious.
It is triggered by known threats.

More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Suspected SQL Injection
A source host is exhibiting external SQL injection behavior with multiple queries observed in the
last 60 minutes.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_http_sqli.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host name

dstip_host — destination host name
dstport — destination port
event_summary.sqli.top_sqli_uris — suspected queries from source host
observed in time window (top 5 shown when more than 5 are detected)
stellar.sqli_variation — unique queries from the source host observed in the time
window
stellar.sqli_duration — time window for suspicious queries observation from
source host
Use Case with Data Points
An external host is attacking your web services with SQL injection attacks using many unique
payloads observed in the last 60 minutes. Consider blocking this source and check if the attack
succeeds.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SYN Flood Attacker
An attacker sends a large amount of SYN requests to a target's system in an attempt to consume
enough server resources to make the system unresponsive to legitimate traffic.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Impact (TA0040 )
Technique: Endpoint Denial of Service (T1499 )
Tags: [External; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is external_syn_flood_attacker.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the SYN flood
srcip_host — source host name
dstip — target IP address of the SYN flood
dstip_host — destination host name
dstport — port on target host that received the SYN flood
syn_flood_events — number of SYN packets during the period
Use Case with Data Points
If an external host (srcip) sends too many SYN packets (syn_flood_events) to internal
target(s) (dstip) in a five-minute time window, an alert is triggered. The Interflow includes the IP
address of the source host (srcip), the IP address of the target host (dstip), the port of the
target host (dstport), and how many SYN packets were observed (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External SYN Flood Victim

A large amount of SYN requests were observed, which can indicate an attempt to consume
server resources and make the target unresponsive. Check to see if the host is malicious or
compromised. If so, consider blocking the source host.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Impact (TA0040 )
Technique: Endpoint Denial of Service (T1499 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_syn_flood.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the SYN flood
srcip_host — source host name
dstip — target IP address of the SYN flood
dstip_host — destination host name
dstport — port on target host that received the SYN flood
syn_flood_events — number of SYN packets during the period
Use Case with Data Points
If an external host (srcip) sends too many SYN packets (syn_flood_events) to internal
target(s) (dstip) in a five-minute time window, an alert is triggered. The Interflow includes the IP
address of the source host (srcip), the IP address of the target host (dstip), the port of the
target host (dstport), and how many SYN packets were observed (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.

When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External Trojan
Malware that disguises itself as legitimate software in order to gain access to a system or files
has been observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] XDR Malware (XTA0006)
Technique: XDR Trojan (XT6004)
Tags: [External; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_trojan_activity.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country

dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the trojan
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates trojan activity, an alert is triggered. A sample Interflow includes
malicious activity for sandbox (maltrace-cloud.data.malicious_activity), IDS signature for
ML-IDS (ids.signature), event source (event_source), source host (srcip_host), source
country (srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the trojan (file_name) from the
sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External URL Reconnaissance Anomaly
An anomalous number of HTTP 4xx errors were observed. This can indicate an attacker
scanning for pages to exploit. Check with the user.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_url_scan.

Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
event_summary.total_failed — number of unique URLs with HTTP error status
response in the period
event_summary.total_successful — number of unique URLs with HTTP success
status response in the period
event_summary.total_fail_ratio — percent of unique URLs with HTTP error status
response in the period, which is: event_summary.total_failed /
(event_summary.total_failed + event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
srcip_geo.countryName — source country name
Use Case with Data Points
For every unique URL browsed by each source IP address (srcip), the number of HTTP
response failures and successes is calculated periodically. If the number of failures is
significantly larger than the number of successes, an alert is triggered. The Interflow includes the
source host (srcip_host), destination host (dstip_host), and source country
(srcip_geo.countryName).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead

list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External User Application Usage Anomaly
A user who typically uses a small, consistent number of applications used a new application.
Investigate the application, to see if it is benign. Check with the user to see if this was expected.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR App Anomaly (XT2003)
Tags: [External; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_user_uncommon_app.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID
appid_name — application name
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_family — application family
srcip_username — source user name
stability — score measuring the time since the last new application was used
days_stable — time since the last new application was used
diversity — score measuring the number of applications that the user used
child_count — number of applications that the user used
Use Case with Data Points
An alert is triggered under the following conditions:
a user (srcip_usersid, srcip_username) with a small number of applications
(diversity, child_count) who has not used a new application for a long period of

time (stability, days_stable), and then
a new application (appid_name) belonging to an application family (appid_family)
appears on a host (scrip_host) with this user, and
that host connects to another host (scrip_host)
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External User Data Volume Anomaly
A user had an anomalously large volume of traffic compared to its typical volume or that of its
peers. Investigate the user to determine if this is expected.
 Firewall and non-firewall data do not contribute to the same alert, so this alert will have
either entirely firewall data or no firewall data.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Bytes Anomaly (XT3001)
Tags: [External; User Behavior Analytics; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_user_bytes_sum.
Severity
30
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID
actual — actual traffic volume in the period
typical — typical traffic volume from the user
srcip_host — host name of corresponding source IP address
srcip_username — source user name
dstip_host — host name of corresponding destination IP address
dstip_reputation — destination reputation
dstip_geo.countryName — destination country
appid_name — application name
Use Case with Data Points
The total traffic volume of each user identified by user ID (scrip_usersid) is calculated
periodically. If the volume in one period (actual) is much larger than its normal volume
(typical), an alert is triggered.
The Interflow includes the source IP address (scrip_host), destination IP address
(dstip_host), destination reputation (dstip_reputation), destination country
(dstip_geo.countryName), and application of the traffic (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
External User Login Failure Anomaly

An anomalous number of login failures was observed for one of the following applications: SSH,
SMTP, FTP, RDP, SMB, databases, Active Directory, Office 365, Okta, AWS CloudTrail, VPNs, or
Google Workspace. For Okta, an anomalous number of multi-factor authentication (MFA) failures
was observed. Check with the user.
This alert type has the following subtypes:
Office 365 / Entra ID
Source IP Based
Destination IP Based
Kerberos Events
Source IP Based Windows Logon Events
Destination IP Based Windows Logon Events
VPN Logon Events

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_user_login_fail.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
dstip — destination IP address
dstip_host — destination host name

event_summary.total_failed — number of failed logins in the period
event_summary.total_successful — number of successful logins in the period
event_summary.total_fail_ratio — percent of failed logins in the period, which is:
event_summary.total_failed / (event_summary.total_failed +
event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
login_type — type of login, such as ssh_traffic, okta_log, or aws_cloudtrail
srcip_host — source host name
srcip_reputation — source reputation
Use Case with Data Points
Login failures and successes are calculated periodically for every source (srcip) and destination
(dstip) IP address. If the number of failures is significantly larger than the number of successes,
an alert is triggered. The Interflow includes the login type (login_type), source host
(srcip_host), and source reputation (srcip_reputation).
Alert Subtype: Office 365 / Entra ID
The Office 365 / Entra ID alert subtype is the same as the External User Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from Office 365 and Microsoft Entra ID (formerly Azure
AD).
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_o365_azure.
Alert Subtype: Source IP Based
The Source IP-based alert subtype is the same as the External User Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from network traffic, system logs, Linux events, and
AWS events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_srcip.
Alert Subtype: Destination IP Based
The Destination IP-based alert subtype is the same as the External User Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from network traffic, system logs, Linux events, and
AWS events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_dstip.
Alert Subtype: Kerberos Events

The Kerberos Events alert subtype is the same as the External User Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from Kerberos events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_kerberos.
Alert Subtype: Source IP Based Windows Logon Events
The Source IP-based Windows Logon Events alert subtype is the same as the External User
Login Failure Anomaly alert type above, with the following differences:
The subtype is for data sources from Windows logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_src_win_logon.
Alert Subtype: Destination IP Based Windows Logon Events
The Destination IP-based Windows Logon Events alert subtype is the same as the External User
Login Failure Anomaly alert type above, with the following differences:
The subtype is for data sources from Windows logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_dst_win_logon.
Alert Subtype: VPN Logon Events
The VPN Logon Events alert subtype is the same as the External User Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from all VPN logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
external_user_login_fail_vpn.
The supported VPNs are FortiGate, Check Point, and Palo Alto Networks Panorama.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as

the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
File Action Anomaly
Actions, such as move, copy, delete, or change attribute, were taken on a file or files an
anomalous number of times. Investigate the actions and the user to see if this is expected.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Data Manipulation (T1565 )
Tags: [Internal; File Anomaly]
Event Name
The xdr_event.name for this alert type in the Interflow data is anomalous_file_action.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
secondary
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
secondary — user name
actual — actual number of file actions in the period
typical — typical number of file actions in the period
path — path to the file
Use Case with Data Points
The number of file actions for each user (secondary) is calculated periodically. If the volume
(actual) is anomalous compared to the typical volume (typical) of file actions in any period, an
alert is triggered. The Interflow includes the directory to the file (path).
File Creation Anomaly
A file or files were created an anomalously large number of times. Check with the user to see if
this is expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)

Technique: XDR File Anomaly (XT1003)
Tags: [File Anomaly; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is file_creation.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
secondary
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
secondary — user name
actual — actual number of file creations in the period
typical — typical number of file creations in the period
path — path to the file(s) created
Use Case with Data Points
The number of file creations for each user (command) is calculated periodically. If the volume
(actual) is much larger than the typical volume (typical) of file creations in any period, an alert
is triggered. The Interflow includes the directory to the file (path).
Google Workspace Account Manipulation
A Google Workspace user was manipulated. Check with the user to make sure this was
expected.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Account Anomaly (XT4007)
Tags: [External; GSuite; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is gsuite_account_manipulation.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_detail.affected_email_address

event_detail.name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_detail.affected_email_address — key ID for the account
event_detail.name — Google Workspace suspicious event name
event_detail.type — Google Workspace suspicious event type
Use Case with Data Points
For each Google Workspace account (event_detail.affected_email_address), account
manipulation is evaluated periodically. This alert is triggered if the Google Security center reports
a leaked password or a user account being suspended for specific reasons. The Interflow
includes the account ID (event_detail.affected_email_address), Google Workspace event
name (event_detail.name), and Google Workspace event type (event_detail.type).
Google Workspace Attack Warning
Attacks to a Google Workspace account were observed. Check with the account holder.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [External; GSuite; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is gsuite_attack_warning.
Severity
74
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_detail.name
gsuite.actor.email
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
actor.email — key ID for the account
srcip — source IP address of the account
srcip_host — source host name
event_detail.name — Google Workspace suspicious event name

event_detail.type — Google Workspace suspicious event type
Use Case with Data Points
For each Google Workspace account (actor.email), attacks are searched periodically. If an
attack is identified, an alert is triggered. The Interflow includes the account ID (actor.email),
source IP address (srcip), Google Workspace event name (event_detail.name), and Google
Workspace event type (event_detail.type).
Google Workspace Suspicious Activities
Suspicious activities were observed in a Google Workspace account. Check with the account
holder.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Login Anomaly (XT4006)
Tags: [External; GSuite; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
gsuite_suspicious_activities.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_detail.name
srcip
user.name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
user.name — key ID for the account
srcip — source IP address of the account
srcip_host — source host name
event_detail.name — Google Workspace suspicious event name
event_detail.type — Google Workspace suspicious event type
Use Case with Data Points
For each Google Workspace account (actor.email), suspicious activities are searched
periodically. If suspicious activities are detected, an alert is triggered. The Interflow includes the

account ID (actor.email), source IP address (srcip), Google Workspace event name
(event_detail.name), and Google Workspace event type (event_detail.type).
Google Workspace User Suspended
A Google Workspace user was suspended. Check with the user to make sure this was expected.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Account Anomaly (XT4007)
Tags: [External; GSuite; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is gsuite_user_suspended.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_detail.name
gsuite.actor.email
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
actor.email — key ID for the account
srcip — source IP address of the account
srcip_host — source host name
event_detail.name — Google Workspace suspicious event name
event_detail.type — Google Workspace suspicious event type
Use Case with Data Points
For each Google Workspace account (actor.email), suspension status is searched periodically.
If a user is suspended, an alert is triggered. The Interflow includes the account ID
(actor.email), source IP address (srcip), Google Workspace event name
(event_detail.name), and Google Workspace event type (event_detail.type).
Hydra Password Guessing Hack Tool
A user from a Windows host executed a command-line script that launched either the hydra.exe
command or a command using known Hydra parameters, which may be an inappropriate use of
the Hydra password guessing tool.
XDR Kill Chain

Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Hydra; Brute Force; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
hydra_password_guessing_hack_tool.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
event_data.Image
event_data.CommandLine
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — device internal IP address
computer_name — name of the Windows host
event_data.CommandLine — command used to run the tool
event_data.Image — process running hydra.exe for password cracking
Use Case with Data Points
This alert is triggered if a Windows host (hostip) executes a PowerShell script with a context
that includes one or more flags (event_data.Imageor event_data.CommandLine indicating
usage of the Hydra password guessing hack tool. The Interflow includes the IP address of the
Windows host (hostip), the host name (computer_name), and the script image
(event_data.Image) or script payload (event_data.CommandLine).
Validation / Remediation
Check the body of the Powershell script that is reported on the Windows host to identify whether
the contents of the script are actually malicious. If malicious, consider quarantining the host.
Potential False Positives
The running of any executable named hydra.exe or a command that has parameters of -u and
-p or ^user^ and ^pass^ triggers this alert.
ICMP Based Exfiltration or Tunneling
Possible ICMP based exfiltration activities have been observed.

XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Exfiltration (TA0010 )
Technique: Exfiltration Over Alternative Protocol (T1048 )
Tags: [ICMP; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is icmp_tunnel.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
dstip — destination IP address
inbytes_delta — total received bytes
inpkts_delta — total received packets
outbytes_delta — total sent bytes
outpkts_delta — total sent packets
actual — actual packet size transmitted through the tunnel in the time period
typical — typical packet size transmitted through the tunnel in the time period
Use Case with Data Points
An anomalously large tunneled ICMP packet (actual) bytes has been observed between
(srcip) and (dstip). The typical ICMP packet size transmitted through this tunnel is (typical)
bytes, measured in a 5-minute interval. This indicates potential ICMP based exfiltration or
tunneling.
Validation / Remediation
Check whether the abnormal ICMP packet is benign and whether the destination IP address is
malicious.
Potential False Positives
New benign DNS server or CDN servers may utilize ICMP to transmit data.
For example, a user or IT script sending ping -l 1400 8.8.8.8 (or ping -s 1400 on
Linux/MacOS) to test network MTU or connectivity may trigger this detection. These larger-than-
normal ICMP packets can appear anomalous compared to the typical 32–64 byte payloads,

especially if repeated within a short interval. However, this behavior is usually benign, particularly
when the destination is a well-known diagnostic IP like Google DNS (8.8.8.8).
 You can use an alert filter combined with a lookup list to filter false positives.
Impacket PsExec Execution
The Impacket PsExec Execution rules detect suspicious SMB traffic related to Impacket PsExec
execution. Any one or more of these will trigger the Impacket PsExec Execution alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Impossible Travel Anomaly
A user logged in from locations that are geographically impossible to travel between in the time
frame. Check with the user.


This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
 For the Impossible Travel Anomaly, there are two chances for ingestion delay, so the
slowest of the two records will define the delay. This alert type is also sensitive to the order
of user logins.
 The Impossible Travel Anomaly employs frequent location alert suppression to address
common false positive alert scenarios. If a user is known to frequently visit the travel
destination, the alert will be suppressed.
 You can customize the Impossible Travel Anomaly in the Detection Management System.
See Configuring Customizations for ML Detections.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Location Anomaly (XT2001)
Tags: [External; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is user_impossible_travel.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the source user
srcip_username — source user name
srcip — source IP address
srcip_host — source host name
engid_gateway — gateway IP address, used to determine the geo location when the
source IP address is private

srcip_geo — source IP address geo location, including latitude and longitude
has_mfa — whether a Multi-Factor Authentication (MFA) event is associated with the
current login
distance_deviation — deviation in distance between two login locations (miles)
time_deviation_human_readable— deviation in time between the two login events
time_deviation — deviation in time between the two login events (seconds)
travel_speed — calculated speed for the user to travel between two locations
(miles/hour)
appid_name — application name for the login event
last_login_time — timestamp of event 2, the 2nd login
_id2 — ID of event 2
_index2 — index of event 2
srcip2 — source IP address of event 2
srcip_geo2 — source IP address geo location of event 2, including latitude and
longitude
has_mfa2 — whether an MFA event is associated with the previous login (event 2)
 has_mfa and has_mfa2 are best-effort and are not guaranteed to be accurate, specifically
when there are ingestion delays.
About srcip and srcip2: For any given travel, there is a source and a destination, which are
defined by timestamp, so the source timestamp is less than the destination timestamp. Since the
destination record arrives later than the source record, the destination is used as the basis for
the alert. This means that srcip comes from the destination and srcip2 is added to that record
from the source login. (This can be counterintuitive because one might assume that srcip2
comes after srcip.)
Use Case with Data Points
Login events (event 1 and event 2) are examined for a user (srcip_usersid), to see if the login
locations (srcip_geo and srcip_geo2), that are at least 100 miles apart, changed faster
(travel_speed = distance_deviation/time_deviation) than possible with the typical
commercial flight speed of 600 miles/hour.
Event 1 is the basis for the Interflow. The srcip_usersid and srcip_username identify the
user, appid_name identifies the application, and last_login_time identifies the time when the 2
nd login event (event 2) happened. You can find detailed information about event 2 by checking
id2 in index2, source IP (srcip2), and geo location (srcip_geo2).
Remove Duplicate Login Events for Microsoft 365 and Entra ID
When both Microsoft 365 and Entra ID data sources report the same login ID, Stellar Cyber will
prioritize Entra ID for alert generation of login location anomalies, provided there is no significant
ingestion delay. If Stellar Cyber can correlate the two logins by their login ID, the Entra ID record
will be sent. The Entra ID records have metadata related to MFA logins as well as specific Azure

location enrichment, that the Microsoft 365 records do not have. The Entra ID record will still be
prioritized even if it is not for MFA authentication.
However, if the Entra ID record is delayed, such as due to an ingestion delay, in order to maintain
responsiveness, the Microsoft 365 record will be sent.
And if only Microsoft 365 is configured, those logs will continue to be used exclusively.
Using ASNs and User Agents to Improve Location Alert Triage
To improve triage of location-based alerts, Stellar Cyber will begin collecting user history for
Autonomous System Number (ASN), ASN org, and user agents (if available from Microsoft 365),
and then use this history to enrich alerts.
Enrichment fields are added to alerts detailing whether that user or tenant has seen that ASN,
ASN org, or user agent before.
For the user and tenant scopes, the enriched fields are: asn_seen_before,
asn_org_seen_before, user_agent_seen_before, and location_seen_before.
The user scope has an additional enriched field: user_start_time_ms, which is the time that
tracking ASN and user agents started, in UNIX milliseconds.
 The location_seen_before field only tracks locations seen before the
user_start_time_ms.
Using ASNs and user agents improves accuracy in anomaly detection and reduces false
positives. You can also use the enriched fields for Automated Threat Hunting (ATH) or alert
filtering.
Internal Account Login Failure Anomaly
An anomalously large number of login failures from an internal source IP address to an internal
destination IP address was observed for an account. Check with the user.
This alert type has the following subtypes:
Windows Logon Events
Kerberos Events
NTLM Events
Hibun Security Logs

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )

Technique: Brute Force (T1110 )
Tags: [Internal; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_cloud_account_login_failure.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — account user ID
or
srcip_username — account user name, enriched from event_data.targetusername
 The key field for this alert type can be either srcip_usersid or srcip_username,
depending on the data feed.
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
Use Case with Data Points
Login failures and successes between any internal IP addresses are calculated periodically for
every account (srcip_usersid). If the number of failures is significantly larger than the number
of successes, an alert is triggered. A sample Interflow includes the login type (login_type),
source host (srcip_host), and source reputation (srcip_reputation).
Alert Subtype: Windows Logon Events
The Windows Logon Events alert subtype is the same as the Internal Account Login Failure
Anomaly alert type above, with the following differences:

The subtype is for data sources from Windows logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_cloud_account_login_failure_win_logon.
Alert Subtype: Kerberos Events
The Kerberos Events alert subtype is the same as the Internal Account Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from Kerberos events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_cloud_account_login_failure_kerberos.
Alert Subtype: NTLM Events
The NTLM Events alert subtype is the same as the Internal Account Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from NTLM events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_cloud_account_login_failure_ntlm.
Alert Subtype: Hibun Security Logs
The Hibun Security Logs alert subtype is the same as the Internal Account Login Failure
Anomaly alert type above, with the following differences:
The subtype is for data sources from Hibun security logs.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_cloud_account_login_failure_hibun.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.

Internal Brute-Forced Successful User Login
A successful login was observed from an IP address that had previously seen a large number of
login failures, or a successful login to a user account was observed from another IP address or
IP addresses that had previously seen a large number of login failures to that account. Check
with the user.
This alert type has the following subtypes:
Source IP Based
User ID Based
 This alert type has a relatively long detection delay of up to 40 minutes because it waits for
login events from high latency data sources and is sensitive to the event order of user
logins.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; Brute Force; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_user_success_brute_forcer.
Severity
95
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
srcip_usersid
Alert Subtype: Source IP Based
The source IP-based alert subtype has the same XDR Kill Chain as the user ID-based alert
subtype, but differs in the Key Fields and Relevant Data Points and Use Case with Data
Points.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_success_brute_forcer_srcip_usersid.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_usersid — Windows SID associated with the source IP address

srcip_host — source host name
srcip_reputation — source reputation
source_geo.countryName — source country
dstip_host — destination host name
login_type — type of login
username — user name
related_alert._id — link to the related Internal User Login Failure Anomaly
Use Case with Data Points
The login records to an internal IP address (dstip) are checked for every internal source IP
address (srcip). An alert is triggered if that IP address:
1. Has so many failed login attempts that it triggered the Internal User Login Failure
Anomaly, and
2. Had a successful login
A sample Interflow includes the source IP address (srcip), login type (login_type), source host
name (srcip_host), source reputation (srcip_reputation), source country
(srcip_geo.countryName), and user name (username).
Alert Subtype: User ID Based
The user ID-based alert subtype has the same XDR Kill Chain as the source IP-based alert
subtype, but differs in the Key Fields and Relevant Data Points and Use Case with Data
Points.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_success_brute_forcer_srcip.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_usersid — Windows SID associated with the source IP address
srcip_host — source host name
srcip_reputation — source reputation
source_geo.countryName — source country
dstip_host — destination host name
login_type — type of login
username — user name
related_alert._id — link to the related Internal Account Login Failure Anomaly
Use Case with Data Points
The login records to a user account (srcip_usersid) are checked for every internal source IP
address (srcip). An alert is triggered if that user account:
1. Has so many failed login attempts that it triggered the Internal Account Login Failure
Anomaly, and
2. Had a successful login

A sample Interflow includes the source IP address (srcip), login type (login_type), source host
name (srcip_host), source reputation (srcip_reputation), source country
(srcip_geo.countryName), and user name (username).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Credential Stuffing
An anomalously large amount of username/password testing was observed on an internal
Windows authentication service. Check the activity after successful logins, and consider blocking
the internal source IP addresses.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_credential_stuffing.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
msg_class

service_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
msg_class — Microsoft-Windows-Security-Auditing for Windows
service_id — specific account ID of a service
login_failure_rate — rate of login failures per minute in the period
unknown_users_rate — rate of unknown user names per minute in the period
unknown_users_to_login_failures — ratio of unknown user names to login failures
in the period
suspicious_ips — suspicious source IP addresses (up to 100)
possible_breached_ips — list of malicious IP addresses that may have successful
breach activities
Use Case with Data Points
Internal credential stuffing is the constant testing of username/password combinations on the
AWS, Okta, or Windows authentication functions. Login activity is monitored and if the number of
failed logins is larger than normal for that service, an alert is triggered. The Interflow includes the
service (msg_class), tenant's account ID on that service (service_id), suspicious source IP
address (suspicious_ips), login failure rate (login_failure_rate), unknown user rate
(unknown_users_rate), the ratio of unknown users to login failures
(unknown_users_to_login_failures), and a list of source IP addresses that might have
suspicious activities and should be investigated (possible_breached_ips).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Exploited Vulnerability

A host with a vulnerability discovered by a security scanning tool was exploited by an attack on
that same vulnerability, indicating a high probability of success. Check the target to see if it was
compromised.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Exploited Vulnerability (XT2015)
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_vuln_exploit_correlation.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
scan_record’s srcip, dstip, ids.cve
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
tenantid — tenant ID
vulnerability_id — ID of the original security scan result
ids_event_id — ID of the original IDS exploit event
srcip (of security scan result) — IP address of the target correlation_info.srcip
dstip (of IDS event) — IP address of the target (correlation_info.dstip)
srcip (of IDS event) — IP address of the attacker (correlation_info.srcip)
vulnerability.cve — CVE associated with the reported vulnerability
ids.cve — CVE the attacker used to exploit the host
Use Case with Data Points
An attacker (srcip) with IP address A is performing an exploit against a target (dstip) with IP
address B using a vulnerability (ids.cve) with CVE x. If any security scanning tool found the
target (srcip) with IP address B to have a vulnerability (vulnerability.cve) with CVE x, an
alert is triggered.
When an alert is triggered, a new correlation event is generated. The Interflow of the correlation
event includes the ID of the IDS exploit event (ids_event_id), the ID of the security scan record
(vulnerability_id), the IP address of the attacker (correlation_info.srcip of the IDS
event), the IP address of the victim (correlation_info.dstip of the IDS event or
correlation_info.srcip of the security scan record), and the CVE that was used in the
exploit (vulnerability.cve and ids.cve).

More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Firewall Denial Anomaly
An internal source host had actions blocked by a firewall too many times. Investigate the firewall
rules that were violated. If suspicious, block the internal source IP address.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Firewall Anomaly (XT2002)
Tags: [Internal; Firewall Anomalies; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_fw_action.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_host
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address

srcip_host — source host name
actual — actual number of firewall denials in the period
typical — typical number of firewall denials in the period
dstip_host — host name of corresponding destination IP address
dev_name — name of the firewall
engid_name — name of the sensor
Use Case with Data Points
The number of firewall denials for every internal source IP address (srcip) is calculated
periodically. If an internal source IP address’s number of firewall denials (actual) is much larger
than the historical count (typical) of all internal IP addresses, an alert is triggered. The Interflow
includes the name of the firewall (dev_name), the name of the sensor (engid_name), and the
destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Firewall Policy Anomaly
In internal traffic, a firewall policy was triggered that has never been seen before (or has very
rarely been seen). Investigate the policy, the intent, and the associated traffic to determine
whether this activity is legitimate or malicious.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Firewall Anomaly (XT2002)
Tags: [Internal; Firewall Anomalies; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is internal_fw_policy_id.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
fw_policy_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
fw_policy_id — ID of the violated firewall policy
days_silent — number of days since this firewall policy was last seen
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
dev_name — device name
dev_type — device type
engid_name — sensor name
Use Case with Data Points
A firewall policy ID (fw_policy_id), which is raised by a device (dev_name and dev_type) and
captured by a sensor (engid_name), shows never seen or very rare (days_silent) traffic
between an internal host (srcip_host) and another internal host (dstip_host). This will trigger
an alert.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.

Internal Handshake Failure
There were too many handshake failures between two internal hosts, which might indicate port
scanning. Check the source host to see if this was expected, and if not, consider blocking the
host.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] Discovery (TA0007 )
Technique: Network Service Scanning (T1046 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_handshake_failure.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
appid_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host with the handshake failures
srcip_host — source host name
dstip — destination IP address of the host with the handshake failures
dstip_host — destination host name
timestamp — when the scan happened
Use Case with Data Points
If an internal host (srcip) scans across many ports on another internal host (dstip), an alert is
triggered. The Interflow includes the IP address of the potential attacker (srcip), the IP address
of the victim (dstip), a special message flag (msgtyp), and when the scan happened
(timestamp).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts

have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal IDS Signature Spike
A source IP address transmitted an anomalous number of different IDS signatures. Typically, this
indicates host penetration or vulnerability scanning.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_ids_signature_spike.
Severity
65
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ids_signatures_summarize — summarized IDS signatures
srcip_host — source host name
actual — actual number of unique IDS signatures in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IDS signatures from the source IP address, with
critical IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others

counted as 1
Use Case with Data Points
The number of unique IDS signatures (ids.signature) and severity (ids.severity), are
calculated periodically. If many different exploits with unique IDS signatures are observed, an
alert is triggered. The Interflow includes a source (srcip), timestamp, an accumulated severity of
IDS signatures (actual), the usual accumulated severity of IDS signatures (typical), and a
sampling of the IDS signatures used in the attack (ids_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal IP / Port Scan Anomaly
A host has either generated an anomalous number of connections compared to the typical
amount, or has triggered an anomalous number of connection failure responses, in the
measured interval. This can indicate that an attacker is scanning for computers or ports to
exploit. Check with the user.
This alert type has the following subtypes:
Connection Failure Anomaly (Sensor Traffic)
Connection Spike Anomaly (Firewall / Windows Traffic)
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] Discovery (TA0007 )
Technique: Network Service Scanning (T1046 )
Tags: [Internal; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is internal_port_scan.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Alert Subtype: Connection Failure Anomaly (Sensor Traffic)
The xdr_event.subtype.name for this alert subtype in the Interflow data is
connection_failure_anomaly.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
num_failed — unique number of (destination IP and destination port) tuples that
respond with failed status
num_successful — unique number of (destination IP and destination port) tuples that
respond with success status
percent_failed — percent of unique (destination IP and destination port) tuples that
respond with failed status
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
dstip_host — host name of corresponding destination IP address
appid_name — application name
summary_port_scan_type — port scan type
Example of Event Summarization in the Alert Description
Within a 5.0-minute period the overall traffic from 10.1.1.1 consisted of the following scans:
64.94% to 10.2.1.26/31 on port(s) ranging from 2 to 49157, 35.06% to 10.2.1.28/30 on port(s)
ranging from 1 to 49157.
Use Case with Data Points
For each internal source IP address (srcip), the number of unique internal destination IP:port
pairs that gave fail responses and the number of unique destination IP:port pairs that gave
success responses are calculated periodically. If the number of failures is significantly larger than
the number of successes, an alert is triggered. The Interflow includes the source host
(srcip_host), destination host (dstip_host), and application name (appid_name).
Validation / Remediation
Check with the user related to the internal source IP address. Inform the user's supervisor if the
activity is unauthorized.

Potential False Positives
Some legitimate activities such as vulnerability scans or penetration testing may trigger this alert
type.
Alert Subtype: Connection Spike Anomaly (Firewall / Windows Traffic)
Event Name
The xdr_event.subtype.name for this alert subtype in the Interflow data is
connection_spike_anomaly.
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
actual — actual number of connections to the destination IP address in the period
typical — typical number of connections to the destination IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
summary_port_scan_type — port scan type
Example of Event Summarization in the Alert Description
Within a 5.0-minute period the overall traffic from 10.1.1.1 consisted of the following scans:
64.94% to 10.2.1.26/31 on port(s) ranging from 2 to 49157, 35.06% to 10.2.1.28/30 on port(s)
ranging from 1 to 49157.
Use Case with Data Points
For every unique triplet (source IP address, destination IP address, and destination port)
browsed by each source IP address (srcip), the number of response failures and successes
and the number of total data volume are calculated periodically. If the number of failures is
significantly larger than the number of successes, or the total data volume is significantly larger
than the typical number, an alert is triggered. The Interflow includes the source host
(srcip_host), destination host (dstip_host), and application name (appid_name).
Considering that a lateral scan (private to private) is more sensitive than a non-lateral scan, this
alert type is divided into two parts. One focuses on lateral scan analysis, the other focuses on
non-lateral scan analysis. The mechanism remains the same as before, with the trigger condition
for lateral scan alert being more sensitive than non-lateral one.
Validation / Remediation
Check with the user related to the internal source IP address. Inform the user's supervisor if the
activity is unauthorized.
Potential False Positives
Some legitimate activities such as vulnerability scans or penetration testing may trigger this alert
type.
More on Internal versus External and Inbound vs Outbound...

Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Non-Standard Port Anomaly
An application had an anomalously large number of connections or a rarely seen connection to
an internal IP address on non-standard ports. Check the application to be sure this is benign.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Service on Non-Standard Port (XT2011)
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_non_std_port_anomaly.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
dstport
appid
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — destination IP address
dstport — destination port
appid — application ID
days_silent — number of days since the application was last seen
appid_name — application name
dstip_host — host name of corresponding destination IP address
actual — actual number of connections in the period
typical — typical number of connections in the period
Use Case with Data Points
The number of connections for an application (dst_ip + dstport + appid) to an internal
IP address is calculated periodically. If a non-standard combination has an actual number of
connections (actual) that is much larger than the typical number of connections (typical), or
the combination has not appeared for a long time, an alert is triggered. The Interflow includes the
source host (srcip_host), destination IP address (dstip), destination port (dstport),
application ID (appid), and application name (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Other Malware
Malware with uncategorized malicious activity in internal traffic was observed. Check with the
user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR Malware (XTA0006)

Technique: XDR Miscellaneous Malware (XT6001)
Tags: [Internal; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_malware_activity.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
ids.severity — severity of the IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the malware
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates malware in internal traffic that cannot be categorized as
ransomware, spyware, trojan, PUA, or adware, an alert is triggered. A sample Interflow includes
malicious activity for sandbox (maltrace-cloud.data.malicious_activity), IDS signature for
ML-IDS (ids.signature), event source (event_source), source host (srcip_host), source
country (srcip_geo.countryName), destination host (dstip_host), destination country
(dstip_geo.countryName), and the name of the file that carries the malware (file_name) from
the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow

as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Password Spraying
An anomalously large number of failed logins with unknown user names was observed on
internal Windows authentication services. Check the activity after successful logins, and consider
blocking the internal source IP addresses.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Sub-technique: Password Spraying (T1110.003 )
Tags: [Internal; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_password_spray.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.Workstation
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address generating a failed login

or
event_data.Workstation — workstation generating a failed login (if applicable)
 The key field for this alert type can be either srcip or event_data.Workstation,
depending on the data feed.
srcip_host — source host name
event_id — Windows event ID corresponding to the login failures
login_type — type of login protocol; the available values vary by event_id
actual — actual number of failed logins with unknown user names in a 5-minute period
typical — typical number of failed logins with unknown user names in a 5-minute
period
event_summary.password_spray_user_summary — list of up to 100 unknown user
names associated with the failed logins (the first three are shown in the alert
description)
Use Case with Data Points
If a potential password spraying attack is observed, an alert is triggered. The Interflow includes a
source (srcip or event_data.Workstation), timestamp, the type of login (login_type), the
number of failed logins (actual), the usual number of failed logins (typical), and a sampling of
the user names used in the attack (password_spray_user_summary).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal PII Leaked
Personally identifiable information (social security numbers or credit cards) has been observed in
internal traffic in the clear. Check the source to see if it is compromised. If so, consider blocking
it.

XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [Internal] Exfiltration (TA0010 )
Technique: Automated Exfiltration (T1020 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_pii_leak.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the PII leak
dstip — destination IP address of the PII leak
ids.signature — IDS signature of the exploit
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
If a personally identifiable information leak is detected by IDS, an alert is triggered. A sample
Interflow includes the IDS signature (ids.signature), source IP address (srcip), destination IP
address (dstip), source host (srcip_host), and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.

Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Plain Text Passwords Detected
A plain text password was observed in unencrypted traffic between internal systems. Check with
the user.
This alert type looks for the presence of metadata.request.password,
metadata.request.auth_password, and metadata.request.auth_simple in the Interflow
records from the sensors. When plain text passwords are present in the network traffic, the
sensors are able to decode and create the corresponding Interflow fields. To preserve privacy,
the actual passwords are replaced by a sequence of asterisks (*).
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Clear Password (XT2006)
Tags: [Internal; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_clear_password.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
actual — actual number of connections with a plain text password in the period
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
Use Case with Data Points

If there are plain text passwords in traffic records with a public source IP address (srcip) or
destination IP address (dstip), an alert is triggered. A sample Interflow includes the source IP
address (srcip), destination IP address (dstip), source host (srcip_host), destination host
(dstip_host), and application (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Protocol Account Login Failure Anomaly
An anomalously large number of login failures between internal IP addresses over SMB or FTP
was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_protocol_account_login_failure.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.username

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.request.username — user name in the HTTP connection request
event_summary.total_failed — number of failed logins in the period
event_summary.total_successful — number of successful logins in the period
event_summary.total_fail_ratio — percent of failed logins in the period, which is:
event_summary.total_failed / (event_summary.total_failed +
event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
appid_name — application name
login_type — type of login
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
Use Case with Data Points
For every user name (metadata.request.username) in the HTTP connections names (that do
not begin with "Mozilla" or "Aella"), the number of failed and successful logins are calculated
periodically. If the number of failed logins is much greater than successful logins, an alert is
triggered. The Interflow includes the application name (appid_name), login type (login_type),
source host (srcip_host), and source reputation (srcip_reputation).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Protocol Pattern Anomaly

An uncommon pattern of applications usage was observed. Investigate if the source host has
unexpected application connections. It could be a malware infected host.
This alert type focuses on lateral movement protocols (ssh, smb, rdp, ldap, ldaps, msrpc, dcerpc,
telnet, teamviewer, krb5, pcanywhere, anydesk, realvnc, and wmi).
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_appflow_outlier.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
appid_name
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
appid_name — name of the internal protocol
dstip_type — IP address type of the connection destination
num_clust — number of common protocol patterns observed
sum_clust_size — number of source IP addresses that have a similar protocol pattern
training_days — number of days of protocol pattern data
Use Case with Data Points
The usage pattern from (srcip) of (dstip_type) (appid_name) is unusual compared to other
(num_clust) different types of usage patterns observed from (sum_clust_size) source IP
addresses in (training_days) days.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).

Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal PUA
Unwanted applications or malware that bombards the user with advertisements in internal traffic
has been observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR Malware (XTA0006)
Technique: XDR PUA (XT6002)
Tags: [Internal; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_pua.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)

srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the PUA
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates potentially unwanted applications (PUA) in internal traffic, an alert
is triggered. A sample Interflow includes malicious activity for sandbox (maltrace-
cloud.data.malicious_activity), IDS signature for ML-IDS (ids.signature), event source
(event_source), source host (srcip_host), source country (srcip_geo.countryName),
destination host (dstip_host), destination country (dstip_geo.countryName), and the name of
the file that carries the PUA (file_name) from the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Ransomware
Malware that prevents you from accessing your system or files and demands ransom payment in
order to regain access in internal traffic was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [Internal] Impact (TA0040 )
Technique: Data Encrypted for Impact (T1486 )
Tags: [Internal; Malware; Ransomware]
Event Name

The xdr_event.name for this alert type in the Interflow data is internal_ransomware.
Severity
98
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the ransomware
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates ransomware in internal traffic, an alert is triggered. A sample
Interflow includes malicious activity for sandbox (maltrace-
cloud.data.malicious_activity), IDS signature for ML-IDS (ids.signature), event source
(event_source), source host (srcip_host), source country (srcip_geo.countryName),
destination host (dstip_host), destination country (dstip_geo.countryName), and the name of
the file that carries the ransomware (file_name) from the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.

When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal RDP BlueKeep
The use of a scanner by zerosum0x0 that discovers targets vulnerable to BlueKeep (CVE-2019-
0708) has been observed between internal hosts. Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Privilege Escalation (TA0004 )
Technique: Exploitation for Privilege Escalation (T1068 )
Tags: [Internal; RDP; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_rdp_bluekeep.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
ids.signature
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
srcip_host — source host name
dstip_host — destination host name
Use Case with Data Points
If the scanner by zerosum0x0 is used, an alert is triggered. A sample Interflow includes the IDS
signature (ids.signature), source host (srcip_host), and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...

Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal RDP Brute Force Attack
An anomalously large number of RDP connections from internal host(s) to an RDP server were
observed. Check the source IP addresses to see if they are unknown or malicious, and monitor
any successful RDP logins.
XDR Kill Chain
Kill Chain Stage:Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; RDP; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_rdp_brute_force.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — IP address of the destination RDP server
dstip_host — destination host name

actual — actual number of RDP connections to the destination IP address in the
period
typical — typical number of RDP connections to the destination IP address in most
time buckets
srcip — source IP address
srcip_host — source host name
Use Case with Data Points
RDP connection activity is monitored and the number of connections calculated periodically. If
the number of connections from internal host(s) to an RDP server (actual) is much greater than
normal (typical), an alert is triggered. A sample Interflow includes the destination IP address
(dstip) and source IP address (srcip).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal RDP Suspicious Outbound
Non-standard tools from an internal host connecting to TCP port 3389 in the other internal host
were observed. This could indicate lateral movement attempting to establish an RDP connection.
Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Tags: [Internal; RDP; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is
internal_rdp_suspicious_outbound.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host that connects to TCP port 3389 with a non-
standard tool
srcip_host — source host name
process_name — process name
Use Case with Data Points
Connections to TCP port 3389 are monitored, and if non-standard tools connect, an alert is
triggered. A sample Interflow includes the source IP address (srcip) and the process name
(process_name). The following are the standard tools:
mstsc.exe
RTSApp.exe
RTS2App.exe
RDCMan.exe
ws_TunnelService.exe
RSSensor.exe
RemoteDesktopManagerFree.exe
RemoteDesktopManager.exe
RemoteDesktopManager64.exe
mRemoteNG.exe
mRemote.exe
Terminals.exe
spiceworks-finder.exe
FSDiscovery.exe
FSAssessment.exe
MobaRTE.exe
chrome.exe
thor.exe
thor64.exe
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:

Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Scanner Behavior Anomaly
An anomalously large amount of scanning behavior or a rarely seen scan behavior between
internal hosts was observed. Cross-check with the IP / Port Scan Anomaly alert.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] Discovery (TA0007 )
Technique: Network Service Scanning (T1046 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_scan_anomalies.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as

1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
Use Case with Data Points
The number of occurrences of each scanner, based on IDS signature (ids.signature) between
internal hosts, is calculated periodically. If one scanner occurs (actual) much more often
compared to its history (typical), an alert is triggered. A sample Interflow is presented with
information such as the traffic application type (appid_name), source host (srcip_host), and
destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SMB Read Anomaly
An internal IP address sent an anomalously large number of read requests to an internal SMB
protocol based service(s). Investigate the files that this internal IP address tried to read. If
suspicious, block the specific internal source IP address.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; SMB; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_smb_read_anomaly.

Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
actual — actual number of SMB reads from the source IP address in the period
typical — typical number of SMB reads from other source IP addresses in the period
dstip_host — destination host name
smb_username — SMB user name
event_summary.smb_path_list — folders experiencing a high volume of SMB read
requests (the first three are shown in the alert description)
Use Case with Data Points
The number of SMB read requests for every internal source IP address (srcip) is calculated
periodically. If a source IP address’s number of SMB reads (actual) is much larger than the
typical number (typical) and that of other IP addresses in any period, an alert is triggered. The
Interflow includes the SMB user (smb_username) and destination host (dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.

Internal SMB Username Enumeration
At least 5 different users SMB login attempts and 1 denied attempt or at least 10 different users
SMB login attempts, were observed from an internal IP address to other internal IP address(es).
Check the source IP address. If malicious, consider blocking it.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; SMB; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_smb_user_scan.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
actual — actual unique SMB user count
typical — SMB user count threshold
smb_username_set — all SMB login user names
Use Case with Data Points
If an internal source IP address (srcip) has several SMB login attempts with (1) at least 5
unique user names and at least 1 denied attempt or (2) at least 10 unique user names, an alert is
triggered. A sample Interflow includes the source IP address (srcip), source host
(srcip_host), destination host (dstip_host), and all the user names (smb_username_set).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).

Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SMB Write Anomaly
An internal IP address sent an anomalously large number of SMB write requests to other internal
IP address(es). Investigate the files that the IP address tried to write. If suspicious, block the
source IP address.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Tags: [Internal; SMB; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_smb_anomaly.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host name
actual — actual number of SMB writes in the period
typical — typical number of SMB writes in the period
dstip_host — destination host name
smb_username — SMB user name
event_summary.smb_path_list — folders experiencing a high volume of SMB write
requests (the first three are shown in the alert description)

Use Case with Data Points
The number of SMB write requests to internal IP address(es) for every internal source IP address
(srcip_host) is calculated periodically. If a source IP address’s number of SMB writes (actual)
is much larger than the typical number (typical) and that of other IP addresses in any period,
an alert is triggered. The Interflow includes the SMB user (smb_username) and destination host
(dstip_host).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Spyware
Malware that collects and shares information about a device without consent in internal traffic
was observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR Malware (XTA0006)
Technique: XDR Spyware (XT6003)
Tags: [Internal; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_spyware_activity.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

dstip
fileid
ids.signature
maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the spyware
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates spyware activity in internal traffic, an alert is triggered. A sample
Interflow includes malicious activity for sandbox (maltrace-
cloud.data.malicious_activity), IDS signature for ML-IDS (ids.signature), event source
(event_source), source host (srcip_host), source country (srcip_geo.countryName),
destination host (dstip_host), destination country (dstip_geo.countryName), and the name of
the file that carries the spyware (file_name) from the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction

of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SQL Anomaly
An internal IP address sent an anomalously large number of queries to an internal SQL server.
Investigate the queries. If suspicious, block the source IP address.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_mysql_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
srcip_geo.countryName — source country
actual — actual number of SQL queries in the period
typical — typical number of SQL queries from the source IP address
dstip_host — destination host name
Use Case with Data Points
The number of SQL queries for every internal source IP address (srcip_host) is calculated
periodically. If an internal source IP’s SQL query count (actual) is much larger than the typical
count (typical) and that of other internal IP addresses in any period, an alert is triggered. The
internal source IP’s country is (srcip_geo.countryName). The Interflow includes the internal
destination host (dstip_host) the source IP visits.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:

Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SQL Dumpfile Execution
The SQL dumpfile command between two internal IP addresses was observed. This command
is commonly used to dump database content or query output to a file on disk. Check with the
user.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] Collection (TA0009 )
Technique: Data Staged (T1074 )
Tags: [Internal; Database; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_sql_db_dump.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
actual — number of SQL dumpfile queries
srcip_host — source host name
source_geo.countryName — source country

dstip_host — destination host name
Use Case with Data Points
If any SQL dumpfile commands are detected between an internal source IP address (srcip)
and an internal destination IP address (dstip), an alert is triggered. A sample Interflow includes
the source IP address (srcip), source host (srcip_host), source country
(srcip_geo.countryName), destination host (dstip_host), and the number of SQL dumpfile
queries in the period (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SQL Shell Command
Shell commands were observed over a SQL connection, which is a common way hackers try to
gain shell access over vulnerable SQL applications. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [Internal] Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Tags: [Internal; Database; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_database_command.
Severity
70
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
dstip — destination IP address
srcip_host — source host name
srcip_reputation — source reputation
dstip_host — destination host name
dstip_reputation — destination reputation
metadata.request.query — SQL query command
actual — number of query records from one source to one destination in one period
Use Case with Data Points
For SQL query records, if special commands (such as select mylab_sys_exec) are found, an
alert is triggered. A sample Interflow includes the source IP address (srcip), destination IP
address (dstip), source host (srcip_host), source reputation (srcip_reputation), destination
host (dstip_host), destination reputation (dstip_reputation), and SQL query records
(metadata.request.query).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Suspected Malicious User Agent

An internal HTTP connection was made by a user agent that has been identified as potentially
malicious. Investigate the connection's destination.
This alert type has the following subtypes:
Predicted Malicious Agent
Known Malicious Agent Match
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR User Agent Anomaly (XT2012)
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
internal_suspected_malicious_user_agent.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.user_agent
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.request.user_agent — user agent in the HTTP connection request
user_agent.original — user agent in the HTTP connection request
stellar.confidence — model's confidence in the prediction used to make the alert
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
Use Case with Data Points
If a seen user agent is identified as suspicious, an alert is triggered. The alert will contain the
suspicious user agent (metadata.request.user_agent), confidence (stellar.confidence),
tenant (tenant_name), source IP (srcip), and destination IP (dstip) in the key fields.
Additionally, the confidence level of the model is displayed in the alert description in a pop-up
box.
Alert Subtype: Predicted Malicious Agent
The Predicted Malicious Agent alert subtype is the same as the Internal Suspected Malicious
User Agent alert type above, with the following differences:
The stellar.anomaly_tag is predicted_internal.

The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_suspected_malicious_user_agent.
It is triggered by a machine learning classifier.
Alert Subtype: Known Malicious Agent Match
The Known Malicious Agent Match alert subtype is the same as the Internal Suspected Malicious
User Agent alert type above, with the following differences:
The stellar.anomaly_tag is known_internal.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_suspected_malicious_user_agent_known_malicious.
It is triggered by known threats.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Suspected SQL Injection
A source host is exhibiting internal SQL injection behavior with multiple queries observed in the
last 60 minutes.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_http_sqli.

Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host name
dstip_host — destination host name
dstport — destination port
event_summary.sqli.top_sqli_uris — suspected queries from source host
observed in time window (top 5 shown when more than 5 are detected)
stellar.sqli_variation — unique queries from the source host observed in the time
window
stellar.sqli_duration — time window for suspicious queries observation from
source host
Use Case with Data Points
An internal host is attacking your web services with SQL injection attacks using many unique
payloads observed in the last 60 minutes. Consider disconnecting this host and check for
malicious programs.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SYN Flood Attacker

An internal attacker sends a large amount of SYN requests to internal target system(s) in an
attempt to consume enough server resources to make the system unresponsive to legitimate
traffic.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [Internal] Impact (TA0040 )
Technique: Endpoint Denial of Service (T1499 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_syn_flood_attacker.
Severity
25
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the SYN flood
srcip_host — source host name
dstip — target IP address of the SYN flood
dstip_host — destination host name
dstport — port on the target host that received the SYN flood
syn_flood_events — number of SYN packets during the period
Use Case with Data Points
If an internal host (srcip) sends too many SYN packets (syn_flood_events) to internal
target(s) (dstip) in a five-minute time window, an alert is triggered. The Interflow includes the IP
address of the source host (srcip), the IP address of the target host (dstip), the port of the
target host (dstport), and how many SYN packets were observed (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.

When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal SYN Flood Victim
A large amount of SYN requests to an internal target were observed, which can indicate an
attempt to consume server resources and make the target unresponsive. Check to see if the host
is malicious or compromised. If so, consider blocking the source host.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [Internal] Impact (TA0040 )
Technique: Endpoint Denial of Service (T1499 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_syn_flood.
Severity
25
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address for the SYN flood
srcip_host — source host name
dstip — target IP address of the SYN flood
dstip_host — destination host name
dstport — port on the target host that received the SYN flood
syn_flood_events — number of SYN packets during the period
Use Case with Data Points
If an internal host (srcip) sends too many SYN packets (syn_flood_events) to internal
target(s) (dstip) in a five-minute time window, an alert is triggered. The Interflow includes the IP

address of the source host (srcip), the IP address of the target host (dstip), the port of the
target host (dstport), and how many SYN packets were observed (actual).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal Trojan
Malware that disguises itself as legitimate software in order to gain access to a system or files in
internal traffic has been observed. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR Malware (XTA0006)
Technique: XDR Trojan (XT6004)
Tags: [Internal; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_trojan_activity.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
fileid
ids.signature

maltrace-cloud.data.malicious_activity
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — IDS signature
maltrace-cloud.data.malicious_activity — malicious activity
actual — number of records for one IDS signature or malicious activity in the period
lateral — boolean, indicating whether this activity is lateral (from private to private)
srcip_host — source host name
srcip_geo.countryName — source country
dstip_host — destination host name
dstip_geo.countryName — destination country
file_name — name of the file that carries the trojan
event_source — source of the event, either ids or sandbox
Use Case with Data Points
If ML-IDS or sandbox indicates trojan activity in internal traffic, an alert is triggered. A sample
Interflow includes malicious activity for sandbox (maltrace-
cloud.data.malicious_activity), IDS signature for ML-IDS (ids.signature), event source
(event_source), source host (srcip_host), source country (srcip_geo.countryName),
destination host (dstip_host), destination country (dstip_geo.countryName), and the name of
the file that carries the trojan (file_name) from the sandbox.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal URL Reconnaissance Anomaly

An anomalous number of HTTP 4xx errors from an internal IP address to other internal IP
addresses were observed. This can indicate an attacker scanning for pages to exploit. Check
with the user.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] Discovery (TA0007 )
Technique: Network Service Scanning (T1046 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_url_scan.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
event_summary.total_failed — number of unique URLs with HTTP error status
response in the period
event_summary.total_successful — number of unique URLs with HTTP success
status response in the period
event_summary.total_fail_ratio — percent of unique URLs with HTTP error status
response in the period, which is: event_summary.total_failed /
(event_summary.total_failed + event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
srcip_geo.countryName — source country name
Use Case with Data Points
For each internal source IP address (srcip), the number of unique URLs that responded with
failure HTTP status and the number of unique URLs that responded with success HTTP status
are calculated periodically. If the fail metric is significantly larger than the success metric, an alert
is triggered. A sample Interflow includes the source host (srcip_host), destination host
(dstip_host), and source country (srcip_geo.countryName).
More on Internal versus External and Inbound vs Outbound...

Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal User Application Usage Anomaly
An internal user who usually runs a few applications with internal service IP addresses suddenly
runs a new application. Investigate the application to see if it is benign. Check with the user to
see if this was expected.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR UBA (XTA0004)
Technique: XDR App Anomaly (XT2003)
Tags: [Internal; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_user_uncommon_app.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID
appid_name — application name

srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_family — application family
srcip_username — source user name
stability — score measuring the time since the last new application was used
days_stable — time since the last new application was used
diversity — score measuring the number of applications that the user used
child_count — number of applications that the user used
Use Case with Data Points
An alert is triggered under the following conditions:
a user (srcip_usersid, srcip_username) with a small number of applications
(diversity, child_count) who has not used a new application for a long period of
time (stability, days_stable), and then
a new application (appid_name) belonging to an application family (appid_family)
appears on a host (scrip_host) with this user, and
that host connects to another host (scrip_host)
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal User Data Volume Anomaly
A user had an anomalously large volume of internal traffic compared to its typical volume or that
of its peers. Investigate the user to determine if this is expected.
 Firewall and non-firewall data do not contribute to the same alert, so this alert will have
either entirely firewall data or no firewall data.
XDR Kill Chain

Kill Chain Stage: Propagation
Tactic: [Internal] XDR UBA (XTA0004)
Technique: XDR Bytes Anomaly (XT3001)
Tags: [Internal; User Behavior Analytics; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_user_bytes_sum.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID
actual — actual traffic volume in the period
typical — typical traffic volume from the user
srcip_host — host name of corresponding source IP address
srcip_username — source user name
dstip_host — host name of corresponding destination IP address
dstip_reputation — destination reputation
dstip_geo.countryName — destination country
appid_name — application name
Use Case with Data Points
The total internal traffic volume of each user identified by user ID (scrip_usersid) is calculated
periodically. If the volume in one period (actual) is much larger than its normal volume
(typical), an alert is triggered.
The Interflow includes the source IP address (srcip_host), destination IP address
(dstip_host), destination reputation (dstip_reputation), destination country
(dstip_geo.countryName), and application of the traffic (appid_name).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.

When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Internal User Login Failure Anomaly
An anomalous number of login failures between internal IP addresses was observed for one of
the following applications: SSH, SMTP, FTP, RDP, SMB, databases, Active Directory, Office 365,
Okta, AWS CloudTrail, Google Workspace, Salesforce, or Microsoft Entra ID (formerly Azure
Active Directory). Check with the user.
This alert type has the following subtypes:
Source IP Based
Destination IP Based
NTLM Events
Kerberos Events
Windows Logon Events

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is internal_user_login_fail.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
service_id — source domain, workstation, organization, or service
dstip — destination IP address
dstip_host — destination host name
event_summary.total_failed — number of failed logins in the period
event_summary.total_successful — number of successful logins in the period
event_summary.total_fail_ratio — percent of failed logins in the period, which is:
event_summary.total_failed / (event_summary.total_failed +
event_summary.total_successful)
weighted_anomaly_score — net score based on weighted rating of successful versus
failed attempts (scanning, login, or other). Scores greater than the detection threshold
will generate an alert.
login_type — type of login, such as ssh_traffic, okta_log, or aws_cloudtrail
srcip_host — source host name
srcip_reputation — source reputation
Use Case with Data Points
Login failures and successes between internal IP addresses are calculated periodically for every
source (srcip) and destination (dstip) IP address. If the number of failures is significantly larger
than the number of successes, an alert is triggered. The Interflow includes the login type
(login_type), source host (srcip_host), and source reputation (srcip_reputation).
Alert Subtype: Source IP Based
The Source IP-based alert subtype is the same as the Internal User Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from network traffic, system logs, Linux events, and
AWS events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_login_fail_srcip.
Alert Subtype: Destination IP Based
The Destination IP-based alert subtype is the same as the Internal User Login Failure Anomaly
alert type above, with the following differences:
The subtype is for data sources from network traffic, system logs, Linux events, and
AWS events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_login_fail_dstip.
Alert Subtype: NTLM Events

The NTLM Events alert subtype is the same as the Internal User Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from NTLM events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_login_fail_ntlm.
Alert Subtype: Kerberos Events
The Kerberos Events alert subtype is the same as the Internal User Login Failure Anomaly alert
type above, with the following differences:
The subtype is for data sources from Kerberos events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_login_fail_kerberos.
Alert Subtype: Windows Logon Events
The Windows Logon Events alert subtype is the same as the Internal User Login Failure
Anomaly alert type above, with the following differences:
The subtype is for data sources from Windows Logon events.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
internal_user_login_fail_win_logon.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Login Attempt Location Count
A user has login attempts from an unusually high number of locations within a 24-hour period.
XDR Kill Chain

Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Location Anomaly (XT2001)
Tags: [External; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is login_location_count.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID where logins were attempted
actual — number of distinct login attempt locations. Near-duplicates, locations that are
similar, are merged using geohashing.
typical — Typical number of login attempt locations
event_summary.login_location_count.location_summary — enumerated
locations. This is an event summary for logins from this user over the last 24 hours.
Near-duplicates may be considered identical by the alert type but are separated here. If
the user has a very high number of logins, not all of them will be shown here.
 T he number of locations displayed in actual may be less than the number of locations
displayed in location_summary. These fields process the number of locations differently,
which may result in a lower number for actual than the fully enumerated locations in
location_summary.
In Stellar Cyber, geohashing is a method of converting latitude/longitude coordinates into a
short alphanumeric code that represents a geographic area. With a precision of 4, each
geohash corresponds to a grid cell roughly 25 miles in diameter. Locations within the same
cell share the same geohash, allowing the system to group near-duplicate points and
reduce noise caused by unstable or inconsistent location enrichment. If two locations fall
near a geohash boundary, they may be assigned different codes and treated as separate.
This grouping is applied only for display and summarization purposes; the full list of unique
enriched locations is still available in the alert.
Use Case with Data Points
A user (srcip_usersid) has experienced login attempts from an unusually high number of
locations (actual) over the last 24 hours. This covers certain types of brute-forced login
attempts and login location patterns that are not captured by other detections.

Validation / Remediation
Investigate the sources of logins for that user to identify if this behavior is expected.
Potential False Positives
N/A
Login Time Anomaly
A user logged in at an abnormal time. Check with the user.

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
This alert type reads the System Timezone in Global Settings and puts the timezone into the
alert descriptions. (In Global Settings, set your timezone relative to UTC.)
When a Login Time Anomaly occurs, the timezone is bound to the alert description with the
following priorities:
The timezone inferred from engid_gateway takes precedence over the DP timezone,
but only when it is present. If engid_gateway is present, the description will use the
timezone where the login actually happened.
If engid_gateway is not present, the DP timezone setting is used.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Time Anomaly (XT4005)
Tags: [External; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is user_login_time.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID of the source user
or
event_data.TargetUserName — name of the user (Windows event)
 The key field for this alert type can be either srcip_usersid or
event_data.TargetUserName, depending on the data feed.
srcip_username — source user name
srcip_host — host name of corresponding source IP address
srcip_geo.countryName — source country
actual_range — actual login time range
typical_range — typical login time range
Use Case with Data Points
Every user's (srcip_usersid) login time (actual) is compared to the typical login times
(typical_range). If it is outside the range, an alert is triggered. The Interflow includes
information such as the source user name (srcip_username), source host name (srcip_host),
and source country (srcip_geo.countryName), as well as the destination host (dstip_host).
Long App Session Anomaly
An application had an anomalously long session compared to its typical session length or that of
its peers. Investigate the application to see if this session was expected.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Session Anomaly (XT2005)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is long_session_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
appid_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

appid_name — application name
actual — actual maximum session length in the period
typical — typical session length from the application’s own history
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
Every application's (appid_name) maximum session duration is calculated periodically. If an
application’s maximum duration (actual) is much larger than its normal value (typical) or the
typical value of other applications, an alert is triggered. The Interflow includes the source host
(srcip_host) and destination host (dstip_host).
Malicious Site Access
A host accessed a URL with a reputation for potentially hosting malware. Check the URL and, if
malicious, consider blocking it. Check the host for compromise.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Bad Reputation (XT2010)
Tags: [External; Network Traffic Analysis; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is mal_access.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
url
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the host that initiated the site access
srcip_host — source host name
url — URL that was accessed
url_reputation — reputation of the accessed URL
Use Case with Data Points
When a host (srcip) accesses a URL with a reputation (srcip_reputation) as potential
malware hosting (MalAccess), an alert is triggered. The Interflow includes the source host IP
address (srcip), the URL accessed (url), and the reputation of the URL (url_reputation).

Malware on Disk
Malicious software or a potentially unwanted application was found on a device and reported as
not cleaned. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR Malware (XTA0006)
Technique: XDR Miscellaneous Malware (XT6001)
Tags: [Internal; Malware]
Event Name
The xdr_event.name for this alert type in the Interflow data is malware_on_disk.
Severity
90 (Windows Defender)
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
file_path
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host
file_path — file path
computer_name — computer name
malware_engine — malware engine, Windows Defender
group — type of malware
type — status of malware
Use Case with Data Points
If either of the following occurs, an alert is triggered:
Windows Defender indicates a failure or error when taking actions to protect the system
A sample Interflow includes the computer name (computer_name), malware engine
(malware_engine), host IP address (hostip), and path to the file (file_path).
Microsoft Entra Application Configuration Changes
The Microsoft Entra Application Configuration Changes rules are used to identify suspicious
Microsoft Entra application configuration changes. Any one or more of these will trigger the
Microsoft Entra Application Configuration Changes alert type.
XDR Kill Chain

Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Tactic: Impact (TA0040 )
Technique: Service Stop (T1489 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Microsoft Entra Apps Modified to Allow Multi-Tenant Access
Microsoft Entra ID (formerly Azure Active Directory) observed an application being modified to
allow multi-tenant access. Check with the organization to be sure this was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Microsoft Entra; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
azure_ad_add_app_multitenant.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_usersid — user account that modified the property change
activityDisplayName — description of the action
targetResources.modifiedProperties.displayName — properties that were
changed (Display Name, New Value, Old Value)
Use Case with Data Points
If Microsoft Entra ID detects any user (srcip_usersid) changing an application to allow multi-
tenant access, an alert is triggered. A sample Interflow includes the user ID (srcip_usersid),
activity name (activityDisplayName), and name of the changed property
(targetResources.modifiedProperties.displayName).
Microsoft Entra Bitlocker Key Retrieval
The Microsoft Entra Bitlocker Key Retrieval rules are used to identify suspicious Microsoft Entra
Bitlocker key retrieval activity. Any one or more of these will trigger the Microsoft Entra Bitlocker
Key Retrieval alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Credentials from Password Stores (T1555 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Modify Authentication Process (T1556 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Domain Policy Modification (T1484 )
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
Tactic: Persistence (TA0003 )
Technique: Valid Accounts (T1078 )

Sub-technique: Cloud Accounts (T1078.004 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Microsoft Entra Custom Domains Changed
Microsoft Entra ID (formerly Azure Active Directory) observed a custom domain being changed.
Check with the organization to be sure this was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Domain Policy Modification (T1484 )
Tags: [Microsoft Entra; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is azure_ad_change_domain.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — user account that made the domain change
activityDisplayName — activity display name
activity_name — action description
targetResources.modifiedProperties — properties that were changed (Display
Name, New Value, Old Value)
Use Case with Data Points
If Microsoft Entra ID detects any user (srcip_usersid) changing a custom domain, an alert is
triggered. A sample Interflow includes the user ID (srcip_usersid) and activity name
(activity_name).
Microsoft Entra Federation Modified
The Microsoft Entra Federation Modified rules are used to identify suspicious Microsoft Entra
federation modified activity. Any one or more of these will trigger the Microsoft Entra Federation
Modified alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Domain Policy Modification (T1484 )
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
Tactic: Persistence (TA0003 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Tactic: Discovery (TA0007 )
Technique: Account Discovery (T1087 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Modify Cloud Compute Infrastructure (T1578 )
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
Tactic: Discovery (TA0007 )
Technique: Account Discovery (T1087 )

Sub-technique: Cloud Account (T1087.004 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Modify Authentication Process (T1556 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Indicator Removal (T1070 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
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
Tactic: Initial Access (TA0001 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Mimikatz Credential Dump
A potential Mimikatz memory dump was observed. Check the process to determine whether the
host is compromised. Consider quarantining the host.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
Tags: [Internal; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is mimikatz_mem_scan.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
access_subject
computer_name
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
access_subject — process attempting access
access_mask — mask that the suspicious process used to obtain access privileges
(different access masks indicate different capabilities obtained by the suspicious
process)
Use Case with Data Points
If a process (access_subject) on a Windows host (srcip) tries to access lsass.exe with a
special access mask (access_mask), an alert is triggered. The Interflow includes the IP address
of the Windows host (srcip), the process performing mimikatz activity (access_subject), and
the access mask used to acquire access privilege (access_mask).
Rule Based Detection
The Mimikatz Credential Dump rules are used to identify suspicious activity relating to potential
Mimikatz memory dump. Any one or more of these will trigger the Mimikatz Credential Dump
alert type.
The rule-based detection is the same as the Mimikatz Credential Dump alert type above, with the
following difference:
The detection_flag is a Stellar Cyber enriched field:
2301: Mimikatz access to lsass.exe
Link to Rule-Based Alert Types
Rules Contributing to Mimikatz Credential Dump Alert Type
Mimikatz DCSync
An attempt to replicate Active Directory for the first time on a domain controller, or the first time
by that account, has occurred. Evaluate whether the replication is intended and, if not, consider
disabling the account involved in the replication and investigate for further signs of compromise.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
Tags: [Internal, Active Directory; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is mimikatz_dcsync.
Severity
90
Alert Suppression Fields

Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
event_data.SubjectUserSid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the targeted domain controller
hostip_host — host name of the targeted domain controller
event_data.SubjectDomainName — domain of the account that attempted the Active
Directory replication
event_data.SubjectUserName — name of the account that attempted the Active
Directory replication
Use Case with Data Points
This alert is triggered when replication of an Active Directory domain controller (hostip) occurs
for the first time or is attempted by a user account or computer account
(event_data.SubjectUserName) that has rarely occurred (days_silent) or never initiated
replication on that DC before. The Interflow includes the IP address of the targeted domain
controller (hostip), the account (event_data.SubjectUserName) attempting the replication and
its domain (event_data.SubjectDomainName), and the replication operation attempted
(event_data.Properties). (For guidance understanding the GUID in the event_data.Properties
field, refer to Microsoft Documentation .)
Validation / Remediation
To triage an alert of this type, consider first verifying whether the Active Directory replication
event was expected. If the replication is not intended, then the alert has indicated that a DCSync
attack is highly likely. This attack can be very severe, because all password hashes stored on the
targeted domain controller might have been dumped. Disable the account involved in the
replication as soon as possible and further investigate the account for any signs of compromise.
There is no simple remediation for a confirmed DCSync attack. Evaluate the overall risks of
credential leakage and apply appropriate corrective actions, including minimizing accounts with
permissions to perform Active Directory replication, and forcing a change of credentials for
accounts with weak passwords.
Potential False Positives
The following will trigger an alert:
Set up of a new DC
Replication of a DC for the first time
OCI Discovery Activity
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.

The OCI Discovery Activity rules are used to identify suspicious discovery activity in OCI. Any
one or more of these will trigger the OCI Discovery Activity alert type.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: Discovery (TA0007 )
Technique: Cloud Infrastructure Discovery (T1580 )
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
Tactic: Discovery (TA0007 )
Technique: Permission Groups Discovery (T1069 )
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
Tactic: Discovery (TA0007 )
Technique: Cloud Infrastructure Discovery (T1580 )
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
Tactic: Discovery (TA0007 )
Technique: Permission Groups Discovery (T1069 )
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
Tactic: Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
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
Office 365 Admin Audit Logging Disabled
Office 365 admin audit logging was disabled. Make sure this change was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable Cloud Logs (T1562 .008 )

Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_admin_audit_logging_disabled.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationName — organization with audit logging
Use Case with Data Points
Office 365 monitors each Office 365 account (srcip_usersid) for admin audit logging status. If
admin audit logging is disabled, an alert is triggered. A sample Interflow includes the account ID
(srcip_usersid) and organization name (OrganizationName).
Office 365 Content Filter Policy Changed
The Microsoft Exchange content policy was changed. An overly permissive content policy can
allow spammers to send your organization unwanted email. Make sure this change was
expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_content_filter_policy_changed.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id

srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationId — ID of the organization with the Microsoft content policy change
OrganizationName — organization with the Microsoft content policy change
Use Case with Data Points
Office 365 monitors all Office 365 accounts (srcip_usersid) in each organization
(OrganizationId) for a Microsoft Exchange content policy change. If a change is detected, an
alert is triggered. A sample Interflow includes the Office 365 account ID (srcip_usersid),
organization ID (OrganizationId), and organization name (OrganizationName).
Office 365 File Sharing with Outside Entities
An Office 365 account shared multiple files with entities outside of the organization. Check with
the user to make sure this was expected.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Exfiltration (TA0010 )
Technique: Transfer Data to Cloud Account (T1537 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_outside_entity_file_sharing.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
srcip — source IP address of the sharing action
srcip_host — source host name
srcip_geo.countryName — source country
Use Case with Data Points

Office 365 monitors sharing with outside entities for each Office 365 account (srcip_usersid). If
an account shares multiple files with outside entities, an alert is triggered. A sample Interflow
includes the user ID (srcip_usersid), source IP address (srcip), and source country
(srcip_geo.countryName).
Office 365 Malware Filter Policy Changed
The Microsoft Exchange malware filter policy changed. An overly permissive malware filter policy
can allow attackers to send malicious attachments to your organization. Make sure this change
was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Tags: [Office 365; Malware; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_malware_filter_policy_changed.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationId — ID of the organization with the Microsoft Exchange malware policy
change
OrganizationName — organization with the Microsoft Exchange malware policy
change
Use Case with Data Points
Office 365 monitors all Office 365 accounts (srcip_usersid) in every organization
(OrganizationId) for Microsoft Exchange malware policy changes. If a change is discovered,
an alert is triggered. A sample Interflow includes the account ID (srcip_usersid), organization
ID (OrganizationId), and organization name (OrganizationName).
Office 365 Multiple Files Restored
Office 365 observed that multiple files were restored in a short period. Check with the user.

XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: Collection (TA0009 )
Technique: Data Staged (T1074 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_multi_file_restore.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
EventSource — event source
srcip — source IP address that caused the restore
srcip_host — source host name
Use Case with Data Points
Office 365 periodically checks file restore records. If multiple file restore records are detected
within a short period, an alert is triggered. A sample Interflow includes the Office 365 account ID
(srcip_usersid), event source (EventSource), and source IP address (srcip).
Office 365 Multiple Users Deleted
Office 365 observed that multiple users were deleted in a short period. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Account Access Removal (T1531 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_multi_user_deleted.
Severity

50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
EventSource — event source
srcip — source IP address that did the deletion
srcip_host — source host name
Use Case with Data Points
Office 365 periodically checks user deletion records. If multiple users were deleted within a short
period, an alert is triggered. A sample Interflow includes the Office 365 account ID
(srcip_usersid), event source (EventSource), and source IP address (srcip).
Office 365 Network Security Configuration Changed
Office 365 identified a change to your organization's network security configuration, which is
uncommon. Make sure this was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_security_conf_changed.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip_usersid — key ID for the Office 365 account
OrganizationId — ID of the organization whose security configuration changed
OrganizationName — name of the organization whose security configuration changed
Use Case with Data Points
Office 365 monitors all Office 365 accounts (srcip_usersid) in every organization
(OrganizationId) for network security configuration changes. If a change is detected, an alert is
triggered. A sample Interflow includes the Office 365 account ID (srcip_usersid), organization
ID (OrganizationId), and organization name (OrganizationName).
Office 365 Password Policy Changed
Office 365 identified a change to the organization's password policy, which is uncommon. Make
sure this was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Modify Authentication Process (T1556 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_password_policy_changed.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationId — ID of the organization whose password policy changed
OrganizationName — name of the organization whose password policy changed
Use Case with Data Points
Office 365 monitors all Office 365 accounts (srcip_usersid) in every organization
(OrganizationId) for sharing policy changes. If a change is detected, an alert is triggered. A
sample Interflow includes the account ID (srcip_usersid), organization ID (OrganizationId),
and organization name (OrganizationName).

Office365 Rare Operations
The Office365 Rare Operations rules are used to identify rare and suspicious Microsoft 365
mailbox operations. Any one or more of these will trigger the Microsoft 365 Rare Operations alert
type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Office 365 Sharing Policy Changed
Office 365 identified a change to your organization's sharing policy, which is uncommon. Make
sure this was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_sharing_policy_changed.

Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
service_id
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationId — ID of the organization whose sharing policy changed
OrganizationName — name of the organization whose sharing policy changed
Use Case with Data Points
Office 365 monitors all Office 365 accounts (srcip_usersid) in every organization
(OrganizationId) for password policy changes. If a change is detected, an alert is triggered. A
sample Interflow includes the Office 365 account ID (srcip_usersid), organization ID
(OrganizationId), and organization name (OrganizationName).
Office 365 User Network Admin Changed
The Office 365 account’s network admin information was changed. Make sure this change was
expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Office 365; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
office365_user_network_admin_changed.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the Office 365 account
OrganizationName — name of the organization
Use Case with Data Points
Office 365 monitors the network admin information for each Office 365 account
(srcip_usersid). If changes to the network admin are discovered, an alert is triggered. A
sample Interflow includes the account ID (srcip_usersid) and organization name
(OrganizationName).
Outbound Destination Country Anomaly
A host that typically communicates with a small, consistent number of countries communicated
with a new country. Investigate the destination to see if it is benign.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Location Anomaly (XT2001)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is
country_communication_anomaly.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip_geo.countryName — name of the destination country
srcip — source IP address
dstip — destination IP address
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
appid_name — application name
stability — score measuring the time since the host communicated with the last new
country
days_stable — time since the host communicated with the last new country

diversity — score measuring the number of countries with which the host
communicated
child_count — number of countries with which the host communicated
Use Case with Data Points
Hosts (srcip_host) and destination countries (dstip_geo.countryName) are examined
periodically. If a host (srcip_host) with a small number of destination countries (diversity,
child_count) has not visited a new country for a long time (stability, days_stable) visits a
host (dstip_host) in a new country with an application (appid_name), an alert is triggered.
Outbytes Anomaly
A source IP address transmitted an anomalously high amount of outbound traffic. This could
indicate data exfiltration.
This alert type has the following subtype:
Outbytes Delta Anomaly
 Firewall and non-firewall data do not contribute to the same alert, so this alert will have
either entirely firewall data or no firewall data.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Exfiltration (TA0010 )
Technique: Automated Exfiltration (T1020 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is outbytes_anomaly.
Severity
35
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_host
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
actual — actual amount of outbound traffic in the period
typical — typical amount of outbound traffic from the source IP address
dstip_host — destination host name
Use Case with Data Points

Every source host's (srcip_host) transferred data volume is calculated periodically. If a host's
volume in outbytes_total (actual) is much higher than its normal volume (typical) in any
period, an alert is triggered. The Interflow includes the destination host (dstip_host).
Alert Subtype: Outbytes Delta Anomaly
The Outbytes Delta Anomaly alert subtype is the same as the Outbytes Anomaly alert type
above, with the following differences:
The alert subtype is only available for vendors that support the outbytes_delta field.
The description for this alert subtype is: A source IP address transmitted an
anomalously high amount of outbound traffic. This momentary spike could indicate data
exfiltration.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
outbytesdelta_spike.
The Use Case with Data Points is as follows:
Every source host's (srcip_host) transferred data volume is calculated periodically. If a
host's volume in outbytes_delta (actual) is much higher than its normal volume
(typical) in any period, an alert is triggered. The Interflow includes the destination host
(dstip_host).
Password Cracking with Hashcat
A user from a Windows host executed a command-line script that launched either the
hashcat.exe command or a command using known Hashcat parameters (-a -m 1000 -r). The
Hashcat command is known to use a SAM file from the Windows registry along with a password
list to crack passwords.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Hashcat; Brute Force; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
password_cracking_with_hashcat.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
event_data.Image
event_data.CommandLine

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — device internal IP address
computer_name — name of the Windows host
event_data.CommandLine — command used to run the tool
event_data.Image — process running the hashcat tool
Use Case with Data Points
This alert is triggered if a Windows host (hostip) executes a PowerShell script with a context
that includes one or more flags (event_data.Image or event_data.CommandLine) indicating
usage of the Hashcat password cracking tool. The Interflow includes the IP address of the
Windows host (hostip), the host name (computer_name), and the script image
(event_data.Image) or script payload (event_data.CommandLine).
Validation / Remediation
Check the body of the Powershell script that is reported on the Windows host to identify whether
the contents are actually malicious. If malicious, consider quarantining the host.
Potential False Positives
The running of any executable named hashcat.exe or any command that uses the hashcat
signature parameter list (-a -m 1000 -r).
Password Reset By User Account
The Password Reset By User Account rules are used to identify events when a password is reset
by a user account. Any one or more of these will trigger the Password Reset By User Account
alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Password Resets Anomaly
An account reset/changed one or more target accounts' passwords for an anomalously large
number of times. Check the subject account and major target accounts.
This alert type has the following subtype:
Windows Account Password Reset Anomaly
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
Tags: [Account Manipulation; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is password_resets_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.SubjectDomainName
event_data.SubjectUserName
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_data.SubjectDomainName — domain to which the SubjectUserName belongs

event_data.SubjectUserName — user name of the account that resets/changes the
password
actual — actual time of the password resets/changes made by the user
typical — expected maximum time of password resets/changes made by the user
Use Case with Data Points
The daily number of password reset/change actions of a user (SubjectDomainName +
SubjectUserName) are monitored by (actual), which is compared with a dynamic upper
threshold of (typical). An alert is triggered when the actual number exceeds the threshold.
Validation / Remediation
Validate the alert by checking the account activity on the date. If the number of resets/changes
are abnormal, check the target user names that are being reset to verify if the action is expected.
Potential False Positives
False positives can be triggered in the following situations:
Traffic pattern change, such as when an account is newly added or has some
systematic change from the typical number of resets/changes
Resets of usually silent accounts
Alert Subtype: Windows Account Password Reset Anomaly
The xdr_event.subtype.name for this alert subtype in the Interflow data is
windows_account_password_resets_anomaly.
Password Spraying Attempts Using Dsacls
A user from a Windows host executed a command-line script to launch a command that by name
and parameter list indicates an attempt to abuse dsacls.exe for password spraying.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Signed Binary Proxy Execution (T1218 )
Tags: [Password Spray; Dsacls]
Event Name
The xdr_event.name for this alert type in the Interflow data is
password_spraying_attempts_using_dsacls.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
event_data.CommandLine

event_data.OriginalFileName
process_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — device internal IP address
computer_name — name of the Windows host
event_data.CommandLine — command used to run the tool
event_data.Image — process running dsacls for password cracking
event_data.OriginalFileName — actual file name that was executed
Use Case with Data Points
This alert is triggered if a Windows host (hostip) executes a dsacls.exe with a context that
includes one or more flags (event_data.Image, event_data.CommandLine, or
event_data.OriginalFileName including /user and /passwd as parameters). This indicates
possible usage of Dcacls as a password spraying tool. The Interflow includes the IP address of
the Windows host (hostip), the host name (computer_name), and the script image
(event_data.Image) or the original file name (event_data.OriginalFileName), and script
commandline (event_data.CommandLine).
Validation / Remediation
Check whether the usage was actually malicious. If so, consider quarantining the Windows host.
Potential False Positives
This alert could be triggered even if the use is a legitimate use of dsacls to bind to an
LDAP session.
Persistence and Execution at Scale via GPO Scheduled Task
The Persistence and Execution at Scale via GPO Scheduled Task rules detect suspicious SMB
traffic related to GPO scheduled task creation/access. Any one or more of these will trigger the
Persistence and Execution at Scale via GPO Scheduled Task alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Scheduled Task/Job (T1053 )
Sub-technique: Scheduled Task (T1053.005 )
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
Tactic: Initial Access (TA0001 )
Technique: Phishing (T1566 )
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
Phishing URL
A connection to a site with a phishing reputation was observed. Check with the user to determine
whether their system is compromised.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Initial Access (TA0001 )
Technique: Phishing (T1566 )
Tags: [Phishing; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is phishing.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
url
dstip_host
metadata.response.subject_alt_name
username
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address of the connection to the phishing URL reputation site
dstip — destination IP address of the phishing URL reputation site
url — URL of the phishing site
dstip_host — destination host name

metadata.response.subject_alt_name — Subject Alternative Name of the phishing
site
username — name of the visitor
dstip_geo.countryName — destination country
srcip_host — source host name
Use Case with Data Points
If a connection from a source (scrip) to a site with a phishing reputation is detected, an alert is
triggered. The Interflow includes the source IP address (srcip), source host (srcip_host),
destination IP address (dstip), destination host (dstip_host), URL of the site (url), destination
country (dstip_geo.countryName), Subject Alternative Name of the site
(metadata.response.subject_alt_name), and user name (username).
Possible Encrypted Phishing Site Visit
A possible phishing site visit to a recently registered domain was observed in encrypted traffic.
Check with the user to determine whether their system is compromised.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Initial Access (TA0001 )
Technique: Phishing (T1566 )
Tags: [Phishing; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is encrypted_phishing_site.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.response.effective_tld — effective top-level domain of the possible
phishing site
srcip — IP address of the visitor to the possible phishing site
dstip — IP address of the possible phishing site
srcip_host — source host name
dstip_host — destination host name
dstip_geo.countryName — destination country

Use Case with Data Points
If an encrypted connection to a recently registered site (metadata.response.effective_tld)
is observed, an alert is triggered. The Interflow includes the source IP address (srcip), source
host (srcip_host), destination IP address (dstip), destination host (dstip_host), destination
country (dstip_geo.countryName), and effective top-level domain of the site
(metadata.response.effective_tld).
Possible Impacket SecretDump Remote Activity
The Possible Impacket SecretDump Remote Activity rules detect suspicious SMB traffic related
to credential dumping using Impacket. Any one or more of these will trigger the Possible
Impacket SecretDump Remote Activity alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Forced Authentication (T1187 )
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
Possible Phishing Site Visit from Email
A user visited a recently registered domain shortly after using email, indicating a possible
phishing site visit. Check to see if the site is malicious. If so, check with the user to see if they are
compromised.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Initial Access (TA0001 )
Technique: Phishing (T1566 )
Tags: [Phishing; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is
email_recent_domain_correlation.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip_domain_creation record’s srcip, dstip, appid_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
recent_domain_id — ID that points to the original record of the recently registered
domain visit
email_traffic_id — ID that points to the original record of email traffic
correlation_info.0.appid_name — application on the visited domain accessed by
the user
correlation_info.0.srcip — IP address of the user
correlation_info.0.dstip — IP address of the recently registered domain (useful if
the correlation_info.0.appid_name is not DNS)
correlation_info.0.dstip_host — recently registered domain that was visited
(useful if the correlation_info.0.appid_name is not DNS)
correlation_info.0.metadata.response.query — recently registered domain
name the victim queried in DNS traffic. This field is only useful if the
correlation_info.0.appid_name is DNS.
correlation_info.0.metadata.response.resolved_ips — IP addresses of the
recently registered domain name the victim queried in DNS traffic. This field is only
useful if correlation_info.0.appid_name is DNS.
Use Case with Data Points
If a user (srcip) uses email (appid_name) and then either queries a recently registered
(metadata.response.domain_creation) domain (metadata.response.query) or visits a
recently registered (dstip_domain_creation) domain (dstip_host), an alert is triggered.
When an alert is triggered, a new correlation event is created. The Interflow includes the
reference ID of the original record of the domain visit (recent_domain_id), the reference ID
pointing to the original record of email traffic (email_traffic_id), the IP address of the user
(correlation_info.0.srcip), the application involved in the recently registered site visit
(correlation_info.0.appid_name), and the visited domain
(correlation_info.0.dstip_host or correlation_info.0.metadata.response.query).
Logic Details of Possible Phishing Site Visit from Email
The timeframe of the alert type logic is as follows:
The rule operates in cycles, running every 2 hours.
During each run, it scans for email usage within the monitored traffic.

After an email action, if a DNS lookup action occurs within a 30-minute window from the
same source IP address, an alert is generated.
The domain query and DNS lookups are as follows:
The domain creation date is queried from DNS traffic.
The data points concerning domain creation dates are gathered from fields in the DNS
traffic, including dstip_domain_creation, metadata.response.domain_creation,
and metadata.request.domain_creation.
The alert type logic considers a domain as recent if it has been created within the past
14 days.
The alert generation conditions are as follows:
The alert is triggered if, within a 30-minute window, for the same source IP address,
there is first, an email action, then there is DNS traffic indicating a domain creation
event in the past 14 days from the same source IP address as the email’s. (The rule
runs every 2 hours, so this trigger could be delayed at most by 2 hours, but the two
correlation events (email action and DNS traffic) need to happen within 30 minutes.)
This logic ensures all specified conditions are met before an alert is generated.
Note that even though the rule runs every 2 hours, the 30-minute time window can be seen as a
sliding window without gaps. For example: the rule runs now as a new cycle, but an email action
happened during the last run, say 2 hours and 10 minutes ago. If the corresponding recent
domain creation event happens in this cycle, say 1 hour and 50 minutes ago, this will also trigger
the alert.
Possible Unencrypted Phishing Site Visit
A possible phishing site visit to a recently registered domain was observed in unencrypted traffic.
Check with the user to determine whether their system is compromised.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Initial Access (TA0001 )
Technique: Phishing (T1566 )
Tags: [Phishing; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is unencrypted_phishing_site.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.response.effective_tld — effective top-level domain of the possible
phishing site
srcip — IP address of the visitor to the phishing site
dstip — IP address of the possible phishing site
srcip_host — source host name
dstip_host — destination host name
dstip_geo.countryName — destination country
Use Case with Data Points
If an unencrypted connection to a recently registered site
(metadata.response.effective_tld) is detected, an alert is triggered. The Interflow includes
the source IP address (srcip), source host (srcip_host), destination IP address (dstip),
destination host (dstip_host), destination country (dstip_geo.countryName), and effective
top-level domain of the site (metadata.response.effective_tld).
Potentially Malicious AWS Activity
The Potentially Malicious AWS Activity rules are used to identify suspicious activity within AWS
logs. Any one or more of these will trigger the Potentially Malicious AWS Activity alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Indicator Blocking (T1562.006 )
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

PowerShell Remote Access
A Windows host executed a PowerShell script interacting with a remote host. Investigate the
script and the remote host to determine whether the script is malicious. If so, consider
quarantining the host.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Tags: [External; PowerShell]
Event Name
The xdr_event.name for this alert type in the Interflow data is powershell_cnc.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
remote_ip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the Windows host
hostip_host — host name
remote_ip — IP address of the remote host involved in the script
event_data.ScriptBlockText — contents of the PowerShell script
Use Case with Data Points
If a Windows host (srcip) executes a PowerShell script that includes potential communication
(event_data.ScriptBlockText) with a remote host (remote_ip), an alert is triggered. The
Interflow includes the IP address of the Windows host (srcip), the script body
(event_data.ScriptBlockText), and the remote host IP address (remote_ip).
Rule Based Detection
The PowerShell Remote Access rules are used to identify when a Windows host executed a
PowerShell script interacting with a remote host. Any one or more of these will trigger the
PowerShell Remote Access alert type.
The rule-based detection is the same as the PowerShell Remote Access alert type above, with
the following difference:
The detection_flag is a Stellar Cyber enriched field:
2200: PowerShell script embedded with remote IP

2201: PowerShell script block with IP embedded at warning level (High fidelity)
Link to Rule-Based Alert Types
Rules Contributing to PowerShell Remote Access Alert Type
Private to Private Exploit Anomaly
A private IP address initiated a large number of exploit attempts identified by a given signature or
a rarely seen exploit attempt to another private IP address. Investigate that signature.
This alert type has the following subtypes:
IDS Traffic Anomaly
IPS Traffic Anomaly
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is exploit_attempt_priv_priv.
Severity
75
Alert Subtype: IDS Traffic Anomaly
The IDS Traffic Anomaly alert subtype is the same as the Private to Private Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ids_traffic_anomaly.
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
ids.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1

typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IDS signatures (ids.signature), weighted by their severity
(ids.severity), are calculated periodically. If many different exploits with unique IDS signatures
are observed, an alert is triggered. . The Interflow includes a source IP address (srcip),
timestamp, an accumulated severity of IDS signatures (actual), the usual accumulated severity
of IDS signatures (typical), and a sampling of the IDS signatures used in the attack
(ids_signatures_summarize).
Alert Subtype: IPS Traffic Anomaly
The IPS Traffic Anomaly alert subtype is the same as the Private to Private Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ips_traffic_anomaly.
The Tags are: [Internal; Network Traffic Analysis; IPS Detection]
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ips.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ips.signature — signature of the exploit
ips.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects

the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Private to Private IPS Signature Spike
A source IP address transmitted an anomalous number of different IPS signatures. Typically, this
indicates host penetration or vulnerability scanning.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Lateral Movement (TA0008 )
Technique: Exploitation of Remote Services (T1210 )
Tags: [Internal; Network Traffic Analysis; IPS Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
ips_signature_spike_priv_priv.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ips_signatures_summarize — signatures of the exploit
srcip_host — host name of corresponding source IP address
actual — actual number of unique IPS signatures in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IPS signatures from the source IP address, with
critical IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
Private to Public Exploit Anomaly
A private IP address initiated a large number of exploit attempts identified by a given signature or
a rarely seen exploit attempt to a public IP address. Investigate that signature.
This alert type has the following subtypes:
IDS Traffic Anomaly
IPS Traffic Anomaly
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is exploit_attempt_priv_pub.
Severity
60
Alert Subtype: IDS Traffic Anomaly
The IDS Traffic Anomaly alert subtype is the same as the Private to Public Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ids_traffic_anomaly.

The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
ids.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IDS signatures (ids.signature), weighted by their severity
(ids.severity), are calculated periodically. If many different exploits with unique IDS signatures
are observed, an alert is triggered. . The Interflow includes a source IP address (srcip),
timestamp, an accumulated severity of IDS signatures (actual), the usual accumulated severity
of IDS signatures (typical), and a sampling of the IDS signatures used in the attack
(ids_signatures_summarize).
Alert Subtype: IPS Traffic Anomaly
The IPS Traffic Anomaly alert subtype is the same as the Private to Public Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ips_traffic_anomaly.
The Tags are: [External; Network Traffic Analysis; IPS Detection]
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ips.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

ips.signature — signature of the exploit
ips.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Private to Public IPS Signature Spike
A source IP address transmitted an anomalous number of different IPS signatures. Typically, this
indicates host penetration or vulnerability scanning.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )

Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis; IPS Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
ips_signature_spike_priv_pub.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ips_signatures_summarize — signatures of the exploit
srcip_host — host name of corresponding source IP address
actual — actual number of unique IPS signatures in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IPS signatures from the source IP address, with
critical IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
Process Anomaly
A process has been launched an anomalously large number of times. Investigate the process
and the user to see if this is expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)
Technique: XDR Process Anomaly (XT1001)
Tags: [Internal; Process Anomaly]
Event Name

The xdr_event.name for this alert type in the Interflow data is bad_process.
Severity
15
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
process_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
process_name — name of the process
actual — actual number of launches in the period
typical — typical number of launches in the period
Use Case with Data Points
The number of times a process (process_name) has been launched is calculated periodically. If
the volume (actual) is much larger than the typical volume (typical) of the command or other
commands in any period, an alert is triggered. The Interflow includes the (hostip) who launched
the process.
Protected Storage Service Access
The Protected Storage Service Access rules detect suspicious SMB traffic accessing protected
storage services. Any one or more of these will trigger the Protected Storage Service Access
alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Public to Private Exploit Anomaly
A public IP address initiated a large number of exploit attempts identified by a given signature or
a rarely seen exploit attempt to a private IP address. Investigate that signature.
This alert type has the following subtypes:
IDS Traffic Anomaly
IPS Traffic Anomaly
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is exploit_attempt_pub_priv.
Severity
60
Alert Subtype: IDS Traffic Anomaly
The IDS Traffic Anomaly alert subtype is the same as the Public to Private Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ids_traffic_anomaly.
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
ids.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IDS signatures (ids.signature), weighted by their severity
(ids.severity), are calculated periodically. If many different exploits with unique IDS signatures
are observed, an alert is triggered. . The Interflow includes a source IP address (srcip),
timestamp, an accumulated severity of IDS signatures (actual), the usual accumulated severity
of IDS signatures (typical), and a sampling of the IDS signatures used in the attack
(ids_signatures_summarize).
Alert Subtype: IPS Traffic Anomaly
The IPS Traffic Anomaly alert subtype is the same as the Public to Private Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ips_traffic_anomaly.
The Tags are: [External; Network Traffic Analysis; IPS Detection]
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ips.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ips.signature — signature of the exploit
ips.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1

typical — typical number of times this signature is seen in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Public to Private IPS Signature Spike
A source IP address transmitted an anomalous number of different IPS signatures. Typically, this
indicates host penetration or vulnerability scanning.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis; IPS Detection]
Event Name

The xdr_event.name for this alert type in the Interflow data is
ips_signature_spike_pub_priv.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ips_signatures_summarize — signatures of the exploit
srcip_host — host name of corresponding source IP address
actual — actual number of unique IPS signatures in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IPS signatures from the source IP address, with
critical IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
Public to Public Exploit Anomaly
A public IP address initiated a large number of exploit attempts identified by a given signature or
a rarely seen exploit attempt to another public IP address. Investigate that signature.
This alert type has the following subtypes:
IDS Traffic Anomaly
IPS Traffic Anomaly
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis]
Event Name

The xdr_event.name for this alert type in the Interflow data is exploit_attempt_pub_pub.
Severity
50
Alert Subtype: IDS Traffic Anomaly
The IDS Traffic Anomaly alert subtype is the same as the Public to Public Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ids_traffic_anomaly.
The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ids.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ids.signature — signature of the exploit
ids.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IDS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IDS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IDS signatures (ids.signature), weighted by their severity
(ids.severity), are calculated periodically. If many different exploits with unique IDS signatures
are observed, an alert is triggered. . The Interflow includes a source IP address (srcip),
timestamp, an accumulated severity of IDS signatures (actual), the usual accumulated severity
of IDS signatures (typical), and a sampling of the IDS signatures used in the attack
(ids_signatures_summarize).
Alert Subtype: IPS Traffic Anomaly
The IPS Traffic Anomaly alert subtype is the same as the Public to Public Exploit Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
ips_traffic_anomaly.
The Tags are: [External; Network Traffic Analysis; IPS Detection]

The Alert Suppression Fields, Key Fields and Relevant Data Points, and Use Case
with Data Points are as follows:
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
ips.signature
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
ips.signature — signature of the exploit
ips.severity — severity of the exploit
actual — actual number of times this signature was found in the period, with critical
IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
typical — typical number of times this signature is seen in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:
Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction

of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Public to Public IPS Signature Spike
A source IP address transmitted an anomalous number of different IPS signatures. Typically, this
indicates host penetration or vulnerability scanning.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
Tags: [External; Network Traffic Analysis; IPS Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is ips_signature_spike_pub_pub.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_summary.ips_signatures_summarize — signatures of the exploit
srcip_host — host name of corresponding source IP address
actual — actual number of unique IPS signatures in the period, with critical IPS
signatures counted as 2, high counted as 1, low counted as 0.5, and others counted as
1
typical — typical number of unique IPS signatures from the source IP address, with
critical IPS signatures counted as 2, high counted as 1, low counted as 0.5, and others
counted as 1
Use Case with Data Points
The number of unique IPS signatures (ips.signature), weighted by their severity
(ips.severity), are calculated periodically. If many different exploits with unique IPS signatures
are observed, an alert is triggered. Additionally, the action (ips.action) taken by the IPS affects
the alert fidelity. The Interflow includes a source IP address (srcip), timestamp, an accumulated
severity of IPS signatures (actual), the usual accumulated severity of IPS signatures (typical),
and a sampling of the IPS signatures used in the attack (ips_signatures_summarize).
RDP Outbytes Anomaly

An internal host transferred an anomalously high amount of data to external host(s) through
RDP. This could indicate data exfiltration. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Exfiltration (TA0010 )
Technique: Exfiltration Over Alternative Protocol (T1048 )
Tags: [RDP; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is rdp_outbytes_anomaly.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
dstip — destination IP address
dstip_host — destination host name
actual — actual amount of outbound traffic in the period
typical — typical amount of outbound traffic from the destination IP address
srcip_host — source IP address that initiates the RDP connection
Use Case with Data Points
Every destination host's (dstip) transferred data volume through RDP is calculated periodically.
If a host's volume (actual) is much greater than normal (typical) in any period, an alert is
triggered. A sample Interflow includes the destination host (dstip_host).
RDP Port Opening
Netsh commands to open TCP port 3389 were observed. This could indicate Sarwent malware
attempting to establish an RDP connection. Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Tags: [RDP]
Event Name

The xdr_event.name for this alert type in the Interflow data is rdp_port_opening.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — source IP address that executes the command
hostip_host — host name
process_name — process name
event_data.CommandLine — command line used
Use Case with Data Points
Commands that open TCP port 3389 are monitored, and if netsh commands are seen, an alert is
triggered. A sample Interflow includes the source IP address (hostip) and the command used
(event_data.CommandLine).
RDP Registry Modification
Modifications of the property values of fDenyTSConnections and UserAuthentication to
enable remote desktop connections were observed. Check the IP address and block if
necessary.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Modify Registry (T1112 )
Tags: [RDP]
Event Name
The xdr_event.name for this alert type in the Interflow data is rdp_registry_modification.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host that made the setting change
hostip_host — host name
event_data.TargetObject — name of the registry key
event_data.Details — value of the registry
Use Case with Data Points
The property values of fDenyTSConnections and UserAuthentication are monitored, and if a
possible malicious modification of the settings to enable remote desktop connections is
observed, an alert is triggered. A sample Interflow includes the source IP address (hostip) and
the registry name (event_data.TargetObject).
RDP Reverse Tunnel
An svchost hosting RDP termsvcs communicating with the loopback address on TCP port 3389
was observed. Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Command and Control (TA0011 )
Technique: Protocol Tunneling (T1572 )
Tags: [RDP]
Event Name
The xdr_event.name for this alert type in the Interflow data is rdp_reverse_tunnel.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
event_data.Image — process communicating with the loopback address
Use Case with Data Points
If an svchost hosting RDP termsvcs communicating with the loopback address is found on TCP
port 3389, an alert is triggered. A sample Interflow includes the host IP address (hostip) and
host name (hostip_host).

RDP Session Hijacking
A suspicious RDP session using tscon.exe or MSTSC shadowing was observed. This could
indicate a hijacked RDP session. Check the IP address and block if necessary.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Service Session Hijacking (T1563 )
Tags: [RDP; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is rdp_session_hijacking.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address that executes the command
hostip_host — host name
process_name — process name
event_data.CommandLine — command line used
Use Case with Data Points
If an RDP session redirect using tscon.exe or MSTSC is detected, an alert is triggered. A
sample Interflow includes the host IP address (hostip), name of the process used
(process_name), and command used (event_data.CommandLine).
RDP Settings Hijacking
Changes to RDP terminal services settings were observed. Check the IP address and block if
necessary.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Modify Registry (T1112 )
Tags: [RDP]
Event Name

The xdr_event.name for this alert type in the Interflow data is rdp_settings_hijack.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host that made the setting change
hostip_host — host name
event_data.TargetObject — name of the registry key
event_data.EventType — event type on the registry key (SetValue, DeleteValue)
event_data.Details — value of the registry
Use Case with Data Points
RDP terminal service settings are monitored, and if changes are found to these settings, an alert
is triggered. A sample Interflow includes the source IP address (hostip) and the registry name
(event_data.TargetObject).
RDP Suspicious Logon
An RDP logon with a local source IP address was observed. This could indicate a tunneled
logon. Check with the user.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Command and Control (TA0011 )
Technique: Protocol Tunneling (T1572 )
Tags: [RDP]
Event Name
The xdr_event.name for this alert type in the Interflow data is rdp_suspicious_logon.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address of the RDP server
event_data.TargetDomainName — domain of the login account
event_data.TargetUserName — user name of the login account
hostip_host — host name
Use Case with Data Points
Remote desktop logins are monitored, and if a local source IP address is seen, an alert is
triggered. A sample Interflow includes the source IP address (hostip) and host name
(hostip_host).
RDP Suspicious Logon Attempt
An authenticated user who is not allowed to log on remotely has attempted to connect through
RDP. Check with the user.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Internal; RDP; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is
rdp_suspicious_logon_attempt.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address of the RDP server
hostip_host — host name
event_data.AccountDomain — account domain of the user who attempts to connect
event_data.AccountName — account name of the user who attempts to connect
event_data.ClientAddress — IP address of the user who attempts to connect
Use Case with Data Points
Windows remote desktop logins are monitored, and if a user who is not allowed to remotely log
in tries to log in with RDP, an alert is triggered. A sample Interflow includes the source IP address

(hostip) and host name (hostip_host).
Recently Registered Domains
A DNS request was observed for a site that was registered less than 90 days ago. Check the
domain. If suspicious, notify users.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR New Domain (XT2008)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is new_registered_domain.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.effective_tld
dns.question.registered_domain
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
metadata.request.effective_tld — top-level domain name in the request
srcip_host — host name of corresponding source IP address
dstip_host — host name of corresponding destination IP address
metadata.response.domain_creation — domain creation time
metadata.response.effective_tld — top-level domain name in the response
metadata.response.resolved_ips — list of resolved IP addresses
actual — number of visits to the domain in the period
domain_creation — domain creation time
dns.question.registered_domain — highest registered domain
dns.question.name — domain name in request
Use Case with Data Points
If a domain has been registered within the last 90 days, an alert is triggered. A sample Interflow
includes the domain name (metadata.request.effective_tld), source host (srcip_host),
destination host (dstip_host), and domain creation time
(metadata.response.domain_creation).

Remote Access Pattern Anomaly
An uncommon pattern of applications usage was observed. Investigate if the source host has
unexpected application connections. It could be a malware infected host.
This alert type focuses on suspicious file-sharing/storage apps (onedrive, quic, github, wireguard,
and openvpn).
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: [External] Exfiltration (TA0010 )
Technique: Exfiltration Over Web Service (T1567 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is external_appflow_outlier.
Severity
40
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
appid_name
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
appid_name — name of the remote access application
dstip_type — IP address type of the remote access destination
num_clust — number of remote access patterns
sum_clust_size — number of source IP addresses that have a similar remote access
pattern
training_days — number of days of remote access data
Use Case with Data Points
The usage pattern from (srcip) of (dstip_type) (appid_name) is unusual compared to other
(num_clust) different types of usage patterns observed from (sum_clust_size) source IP
addresses in (training_days) days.
More on Internal versus External and Inbound vs Outbound...
Stellar Cyber reports both internal and external versions of some alerts, with different analysis
and recommended actions for each. Similarly, IDS signatures report the direction of data flow
as inbound or outbound. Use the following as a guide for these concepts:

Addresses with a srcip_type and dstip_type of private are identified as
internal. All other values are identified as external (when applicable; not all alerts
have unique analytics for internal/external).
Communications between hosts where srcip_type and dstip_type are both
private are considered internal communications.
When an anomaly is observed on an internal communication, the attack is
considered to be internal.
Stellar Cyber always sets the srcip in the Interflow record as the initiating IP address
of an event. Note that IDS signatures, which are reported with relevant alerts, instead
list addresses based on the direction of data flow, not the initiating address. So an
INBOUND data flow may show the dstip as the source address and the srcip as
the destination address, even though the srcip was the initiator of the request. Use
INBOUND and OUTBOUND information in the signature to understand the direction
of data flow, together with Stellar Cyber’s Interflow record of srcip and dstip to
understand which address initiated the threat event.
Remote Service Activity via SVCCTL Named Pipe
The Remote Service Activity via SVCCTL Named Pipe rules detect suspicious SMB traffic
accessing SVCCTL named pipes. Any one or more of these will trigger the Remote Service
Activity via SVCCTL Named Pipe alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Tactic: Persistence (TA0003 )
Technique: Scheduled Task/Job (T1053 )
Sub-technique: At (Windows) (T1053.002 )
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
Scanner Reputation Anomaly

An anomalously large amount of connections were observed from an IP address with a
reputation of being a scanner. Cross-check with the IP / Port Scan Anomaly alert, and check the
links and content for possible spam or phishing.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is scanner_rep.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_host
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
srcip_geo.countryName — source country
actual — actual number of connections from this source in the period
typical — typical number of connections from this source in the period
dstip_host — host name of corresponding destination IP address
Use Case with Data Points
The number of connections from a source IP address (srcip_host) with a reputation as a
scanner (srcip_reputation) is calculated every 5 minutes. If the number of connections
(actual) is much greater than normal (typical), an alert is triggered. The Interflow includes
information such as the source country (srcip_geo.countryName) and a destination
(dstip_host).
Sensitive Windows Active Directory Attribute Modification
The Sensitive Windows Active Directory Attribute Modification rules are used to identify
suspicious activity with sensitive Windows Active Directory attribute modification. Any one or
more of these will trigger the Sensitive Windows Active Directory Attribute Modification alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )

Technique: Domain Policy Modification (T1484 )
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
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Sensor Status Anomaly
The sensor has changed its status from "connected" to "disconnected".
For Windows Agent sensors, this alert type logs the status of each sensor every 5 minutes. The
status includes whether or not the sensor is connected and whether or not the sensor is sending
data.
This alert type has the following subtypes:
Sensor Status Flipped
Disconnected but still sending data
Disconnected and stopped sending data
Disconnected and inactive
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: XDR SBA (XTA0003)
Technique: XDR Status Anomaly (XT3002)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is ade_outbytes_anomaly_flip.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
engid
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
engid — sensor ID
engid_name — sensor name
metadata.status — sensor (engine) status
Use Case with Data Points
For each sensor, its connection status is checked periodically, if the status changes from
“connected“ to “disconnected“, the anomaly is triggered. A sample Interflow includes the sensor
ID (engid) and sensor name (engid_name).
Alert Subtype: Sensor Status Flipped
The Sensor Status Flipped alert subtype is the same as the Sensor Status Anomaly alert type
above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
sensor_status_anomaly_flip.
The subtype is for data sources from Windows Agent sensors.
It is triggered instantly when a disconnection is logged.
Alert Subtype: Disconnected but still sending data
The Disconnected but still sending data alert subtype is the same as the Sensor Status Anomaly
alert type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
sensor_status_anomaly_sending_data.
The subtype is for data sources from Windows Agent sensors.
It indicates a connection status of disconnected but still sending data.
A disconnection alert is sent if the sensor stays disconnected or sends no data for 15
minutes.
Alert Subtype: Disconnected and stopped sending data
The Disconnected and stopped sending data alert subtype is the same as the Sensor Status
Anomaly alert type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
sensor_status_anomaly_stopped_sending_data.
The subtype is for data sources from Windows Agent sensors.
It indicates a connection status of disconnected and stopped sending data.
A disconnection alert is sent if the sensor stays disconnected or sends no data for 15
minutes.
Alert Subtype: Disconnected and inactive

The Disconnected and inactive alert subtype is the same as the Sensor Status Anomaly alert
type above, with the following differences:
The xdr_event.subtype.name for this alert subtype in the Interflow data is
sensor_status_anomaly_no_data.
The subtype is for data sources from Windows Agent sensors.
It indicates a transition from a connection status of connected, not sending data to
disconnected, not sending data.
A disconnection alert is sent if the sensor stays disconnected or sends no data for 15
minutes.
SMB Impacket Lateralization
The execution of wmiexec, dcomexec, atexec, smbexec, or PSExec from the Impacket
framework was observed. Check the source host. If malicious, consider blocking the host.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Execution (TA0002 )
Technique: Windows Management Instrumentation (T1047 )
Tags: [SMB; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is smb_impacket_lateralization.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
event_data.CommandLine — command line of the command that was executed
event_data.ParentCommandLine — command line of the parent process
Use Case with Data Points
If a Windows host (srcip) executes a command (wmiexec, dcomexec, atexec, smbexec, or
PSExec) from the Impacket framework, an alert is triggered. A sample Interflow includes the
source IP address (srcip), source host (srcip_host), and the command executed
(event_data.CommandLine).

SMB Specific Service Installation
A specific service installation used by the Impacket tool or Metasploit was observed. Check the
source host. If malicious, consider blocking the host.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Execution (TA0002 )
Technique: System Services (T1569 )
Tags: [SMB]
Event Name
The xdr_event.name for this alert type in the Interflow data is smb_hack_smbexec.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
event_data.ServiceName
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
event_data.ServiceName — name of the service installed
Use Case with Data Points
If a Windows host (srcip) installs a specific service installation that is used by the smbexec.py
tool, an alert is triggered. A sample Interflow includes the source IP address (srcip), source host
(srcip_host), and the service installed (event_data.ServiceName).
SMB Suspicious Copy
A suspicious copy command from a remote C$ or ADMIN$ share was observed. Check the
source host. If malicious, consider blocking the host.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: Collection (TA0009 )
Technique: Data from Network Shared Drive (T1039 )
Tags: [SMB]
Event Name

The xdr_event.name for this alert type in the Interflow data is smb_suspicious_copy.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — host IP address
hostip_host — host name
event_data.CommandLine — command line of the copy command
Use Case with Data Points
If a Windows host (srcip) uses the copy command to copy files from a remote C$ or ADMIN$
share, an alert is triggered. A sample Interflow includes the source IP address (srcip), source
host (srcip_host), and the command executed (event_data.CommandLine).
Startup/Logon Script Added to Group Policy Object
The Startup/Logon Script Added to Group Policy Object rules detect suspicious SMB traffic
related to GPO script modifications. Any one or more of these will trigger the Startup/Logon
Script Added to Group Policy Object alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Boot or Logon Autostart Execution (T1547 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Steal or Forge Kerberos Tickets (T1558 )
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
Successful Login After Brute Force
A successful login occurred from a new IP address after the user's account experienced brute
force activity. Verify the login is legitimate and investigate the source of the failed attempts.
 You can customize the Successful Login After Brute Force alert type in the Detection
Management System. See Configuring Customizations for ML Detections.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Credential Access (TA0006 )
Technique: Brute Force (T1110 )
Tags: [Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is brute_force_success.
Severity
90
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — user account that experienced the brute force activity
srcip — source IP address of the successful login
login_type — type of login (for exmaple, interactive, network)
event_summary.unique_failure_ips_short — number of unique IP addresses with
login failures in the last 30 minutes
event_summary.unique_failure_ips_long — number of unique IP addresses with
login failures in the last 24 hours
event_summary.failure_ips — list of IP addresses that had failed login attempts (up
to 100)
srcip_asn — Autonomous System Number (ASN) of the source IP address of the
successful login that triggered the alert
srcip_asn_org — autonomous system organization of the source IP address of the
successful login that triggered the alert
srcip_geo — source IP address geo location of login success, including latitude and
longitude

srcip_host — hostname associated with the source IP address of the successful login
that triggered the alert
srcip_reputation — reputation of the source IP address of the successful login that
triggered the alert
event_summary.short_window_triggered — whether the 30-minute failure window
threshold was triggered
event_summary.long_window_triggered — whether the 24-hour failure window
threshold was triggered
Use Case with Data Points
This alert type is triggered if a user (srcip_usersid) has login failures from multiple different IP
addresses within a 30-minute or 24-hour window followed by a login success from an IP address
with no recent login successes. The number of login failures required for each window can be
customized in the Detection Management System.
The login success is the basis for the Interflow. It will be enriched with information about the login
failures. The event_summary.failure_ips field lists the IP addresses with failures. The
unique_failure_ips_short and unique_failure_ips_long fields list the number of unique
failure IP addresses within the 30-minute and 24-hour windows respectively.
Suspected AS-REP Roasting Attacks
Suspected Authentication Server Response (AS-REP) Roasting attacks have been observed.
These are suspicious Kerberos authentication events without pre-authentication. Investigate the
source IP address and target user name.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: Steal or Forge Kerberos Tickets (T1558 )
Sub-technique: AS-REP Roasting (T1558.004 )
Tags: [Internal; Kerberos; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is kerberos_roasting.
Severity
75
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

srcip — source IP address
login_result — login result
event_data.PreAuthType — pre-authentication type (0: disabled)
event_summary.kerberos_roasting.user_summary — user names without pre-
authentication
actual — actual number of users without pre-authentication in 5-minute interval
threshold — typical number of users without pre-authentication in 5-minute interval
Use Case with Data Points
Detect AS-REP roasting by checking for spikes in the number of Kerberos Ticket Granting Ticket
(TGT) requests without pre-authorization.
An unusually high number (actual) of user accounts without pre-authentication was observed
from the source IP address (srcip). The expected number of user accounts without pre-
authentication for (srcip) is (threshold), measured in a 5-minute interval. This indicates a
potential AS-REP roasting attack.
Suspected Network Beaconing Activities
Suspected network beaconing activity was observed. If malicious, block the IP address of the
Command and Control server and consider containing the source hosts.
Command and Control (C&C or C2) beaconing describes the behavior of bots actively,
persistently, and regularly connecting to a C2 server. (The regular interval is a characteristic
allowing detection.)
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: [External] XDR Intel (XTA0005)
Technique: Application Layer Protocol (T1071 )
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is c2beaconing.
Severity
70
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
dstport
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.

dstip — destination IP address
srcip — source IP address
period_cnt — number of beaconing connections observed
period_mean — frequency of beaconing connections
dstport — destination port
connection_prevalence — prevalence of beaconing connection destination
Use Case with Data Points
The beaconing behavior between source host (srcip) and destination (dstip):(dstport) has
frequency and persistency. The c2beaconing frequency (period_mean) should be between 100
to 400 seconds and the behavior should be persistent (period_cnt) for over a day. A low
prevalence connection means the destination IP address belongs to an ASN to which only a few
hosts connect. If a connection is low prevalence and the beaconing behavior has frequency and
persistency, an alert is triggered.
Suspicious Access Attempt to Windows Object
The Suspicious Access Attempt to Windows Object rules are used to identify suspicious activity
with access attempt to Windows objects. Any one or more of these will trigger the Suspicious
Access Attempt to Windows Object alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Persistence (TA0003 )
Technique: Create Account (T1136 )
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
Tactic: Discovery (TA0007 )
Technique: Cloud Infrastructure Discovery (T1580 )
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
Tactic: Collection (TA0009 )
Technique: Data Staged (T1074 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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

Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Persistence (TA0003 )
Technique: Create Account (T1136 )
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
Tactic: Persistence (TA0003 )
Technique: Valid Accounts (T1078 )
Sub-technique: Cloud Accounts (T1078.004 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Resource Development (TA0042 )
Technique: Obtain Capabilities (T1588 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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

Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Privilege Escalation (TA0004 )
Technique: Account Manipulation (T1098 )
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
Tactic: Impact (TA0040 )
Technique: Resource Hijacking (T1496 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable or Modify Cloud Firewall (T1562.007 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Credentials from Password Stores (T1555 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Unsecured Credentials (T1552 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Impact (TA0040 )
Technique: Data Destruction (T1485 )
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
Tactic: Persistence (TA0003 )
Technique: Scheduled Task/Job (T1053 )
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

Tactic: Privilege Escalation (TA0004 )
Technique: Valid Accounts (T1078 )
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
Tactic: Impact (TA0040 )
Technique: Network Denial of Service (T1498 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Sub-technique: PowerShell (T1059.001 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
Sub-technique: LSASS Memory (T1003.001 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: Steal or Forge Kerberos Tickets (T1558 )
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
Suspicious LDAP Search Request
A suspicious LDAP search request was observed for the first time. This behavior indicates that
an attacker might be attempting to collect information from the Active Directory (AD) service.
 To turn on structured LDAP query parsing, enable ldap-metadata in the sensor CLI.
This alert type has the following subtypes:
Domain Trust Enumeration
All Object Enumeration
Wildcard Query
XDR Kill Chain
Kill Chain Stage: Exploration

Tactic: Discovery (TA0007 )
Technique: Account Discovery (T1087 )
Tags: [LDAP; Network Traffic Analysis; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is suspicious_ldap.
Severity
74
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip
dstip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_host — source host that sent the suspicious LDAP search request
srcip_geo.countryName — country of the suspicious source host
dstip_host — destination host to which the suspicious LDAP search request was sent
metadata.request.base_object — baseObject parameter of the suspicious LDAP
search request
metadata.request.scope — scope parameter of the suspicious LDAP search request
metadata.request.filter — filter parameter of the suspicious LDAP search request
Use Case with Data Points
The parameters (metadata.request.filter) of LDAP requests captured from network traffic
are examined. If an LDAP request with suspicious parameters is seen for the first time, an alert is
triggered. Each alert subtype has its own criteria for detecting suspicious parameters. See the
descriptions below.
Validation / Remediation
Check the metadata field of the alert to see if the LDAP requests are legitimate. If the metadata
looks suspicious, further investigate the source IP address that is sending the requests.
Potential False Positives
LDAP is widely used in AD environments by legitimate services to exchange domain information.
If the user performs a domain backup or DCSync operation, the corresponding LDAP traffic may
be flagged as suspicious.
Alert Subtype: Domain Trust Enumeration
The Domain Trust Enumeration alert subtype is the same as the Suspicious LDAP Search
Request alert type above, with the following differences:

The alert subtype detects domain trust enumeration behaviors from LDAP request
parameters. The subtype is for LDAP search requests that have scope set to 2
(wholeSubtree) and filter set to (objectclass=trusteddomain).
The xdr_event.subtype.name for this alert subtype in the Interflow data is
suspicious_ldap_domaintrust_enumeration.
Technique: Domain Trust Discovery (T1482 ).
Alert Subtype: All Object Enumeration
The All Object Enumeration alert subtype is the same as the Suspicious LDAP Search Request
alert type above, with the following differences:
The alert subtype detects all object enumeration behaviors from LDAP request
parameters. The subtype is for LDAP search requests that have scope set to 2
(wholeSubtree) and filter set to (objectclass=*).
The xdr_event.subtype.name for this alert subtype in the Interflow data is
suspicious_ldap_all_object_enumeration.
Technique: Account Discovery (T1087 ).
Alert Subtype: Wildcard Query
The Wildcard Query alert subtype is the same as the Suspicious LDAP Search Request alert
type above, with the following differences:
The alert subtype detects wildcard queries in LDAP requests. The subtype is for LDAP
search requests that have an asterisk (*) in the filter part, excluding some false
positives.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
suspicious_ldap_wildcard_query.
Technique: Account Discovery (T1087 ).
Has an Alert Suppression Field, metadata.request.filter, in addition to srcip and dstip.
Suspicious LSASS Process Access
The Suspicious LSASS Process Access rules are used to identify suspicious process access to
or from the Local Security Authority Subsystem Service (LSASS). Any one or more of these will
trigger the Suspicious LSASS Process Access alert type.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
Sub-technique: LSASS Memory (T1003.001 )
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
Tactic: Impact (TA0040 )
Technique: Network Denial of Service (T1498 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Modify Cloud Compute Infrastructure (T1578 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )

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
Tactic: Discovery (TA0007 )
Technique: Cloud Infrastructure Discovery (T1580 )
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
Tactic: Discovery (TA0007 )
Technique: Cloud Infrastructure Discovery (T1580 )
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
Suspicious OCI Cross Tenancy Communication
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
An outbound request from an OCI tenant targeting another tenancy is observed, signaling
potential lateral movement.
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: Direct Cloud VM Connections (T1021.008 )
Tags: [OCI]
Event Name
The xdr_event.name for this alert type in the Interflow data is
suspicious_oci_cross_tenancy_communication.
Severity
25
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
oracle.oracle.tenantid
oracle.data.identity.tenantId
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
oracle.oracle.tenantid — tenancy owning the resource targeted by the event
oracle.data.identity.tenantId — tenancy emitting the event (the tenant from
which the request was made)
Use Case with Data Points

Stellar Cyber detects OCI cross-tenancy communication (that is, outbound requests from a
tenant targeting another tenancy) by checking whether the tenant from which the request was
made (data.identity.tenantId) is identical to the tenancy that owns the resource targeted by
the request (oracle.tenantId). Note that data.identity.tenantId does not always exist (for
example, if an action was performed by Oracle-managed control plan services and therefore did
not originate from an end-user or resource with a tenant association), but oracle.tenantId
should always exist.
Suspicious OCI Event Rule Deletion
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The Suspicious OCI Event Rule Deletion rules are used to identify suspicious deletion activity of
event rules in OCI. Any one or more of these will trigger the Suspicious OCI Event Rule Deletion
alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Defense Evasion (TA0005 )
Technique: Indicator Removal (T1070 )
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
Tactic: Impact (TA0040 )
Technique: Account Access Removal (T1531 )
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
Tactic: Persistence (TA0003 )
Technique: Account Manipulation (T1098 )
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
Tactic: Initial Access (TA0001 )
Technique: Exploit Public-Facing Application (T1190 )
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
Tactic: Impact (TA0040 )
Technique: Resource Hijacking (T1496 )
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
Tactic: Exfiltration (TA0010 )
Technique: Transfer Data to Cloud Account (T1537 )
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
Tactic: Impact (TA0040 )
Technique: Data Destruction (T1485 )

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
Tactic: Impact (TA0040 )
Technique: Data Destruction (T1485 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable or Modify Cloud Logs (T1562.008 )
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
Tactic: Reconnaissance (TA0043 )
Technique: Active Scanning (T1595 )
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

Tactic: Defense Evasion (TA0005 )
Technique: Impair Defenses (T1562 )
Sub-technique: Disable or Modify Tools (T1562.001 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Hide Artifacts (T1564 )
Sub-technique: Email Hiding Rules (T1564.008 )
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
Tactic: Collection (TA0009 )
Technique: Email Collection (T1114 )
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
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Sub-technique: PowerShell (T1059.001 )
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
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
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
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Tactic: [Internal] Credential Access (TA0006 )
Technique: OS Credential Dumping (T1003 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Valid Accounts (T1078 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Signed Binary Proxy Execution (T1218 )
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
Tactic: Defense Evasion (TA0005 )
Technique: Signed Binary Proxy Execution (T1218 )
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
Tactic: Impact (TA0040 )
Technique: Defacement (T1491 )
Sub-technique: Internal Defacement (T1491.001 )
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
Tactic: Persistence (TA0003 )
Technique: Office Application Startup (T1137 )
Sub-technique: Add-ins (T1137.006 )
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
Tactic: Execution (TA0002 )
Technique: Command and Scripting Interpreter (T1059 )
Sub-technique: PowerShell (T1059.001 )
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
Tactic: Lateral Movement (TA0008 )
Technique: Remote Services (T1021 )
Sub-technique: SMB/Windows Admin Shares (T1021.002 )
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
Unapproved Asset Activity
Activity of an asset that was marked as unapproved in one of the Asset Analytics tabs has been
observed.
Unapproved assets generate one alert per day until their approval status is changed with either
the Approve or Ignore button in the Asset Analytics tabs.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR Unapproved Asset Activity (XT2013)
Tags: [Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is asset_violation.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
asset_id
Key Fields and Relevant Data Points

Key fields are meaningful and human-readable data points representing observable(s) being
detected.
asset_id — ID of a specific asset
vendor — vendor of this asset
Use Case with Data Points
If an analyst marks an asset as unapproved in the Asset Activity tabs, a daily alert is triggered
until the asset is either manually approved or ignored.
Uncommon Application Anomaly
Private (internal assets) to public (Internet) traffic has revealed an application that has never
been seen before (or been seen very rarely). Investigate that application and ensure that it is
benign.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR App Anomaly (XT2003)
Tags: [External; Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is network_uncommon_app.
Severity
20
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
appid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
appid_name — application name
days_silent — number of days since this application was last seen
srcip_host — host name of corresponding source IP address
srcip_reputation — source reputation
srcip_geo.countryName — source country
dstip_host — host name of corresponding destination IP address
dstip_reputation — destination reputation
dstip_geo.countryName — destination country
Use Case with Data Points
If an application (appid) has never been observed by Stellar Cyber or been seen very rarely
(days_silent), an alert is triggered. The Interflow includes the internal assets (srcip_host),

source reputation (srcip_reputation), and source country (srcip_geo.countryName), and the
destination host (dstip_host), destination reputation (dstip_reputation), and destination
country (dstip_geo.countryName).
Uncommon Process Anomaly
An asset launched a process that has never been seen before (or has very rarely been seen).
This could indicate a malware attack.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)
Technique: XDR Process Anomaly (XT1001)
Tags: [Process Anomaly]
Event Name
The xdr_event.name for this alert type in the Interflow data is network_uncommon_process.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
process_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host running the process
hostip_host — host name
process_name — name of the process
wineventlog_user — user that created the process
days_silent — number of days since this process was last seen
Use Case with Data Points
If a process (process_name) has never been observed by Stellar Cyber or been seen very rarely
(days_silent), an alert is triggered. The Interflow includes the user (process_user) and host
(srcip) that executed the process.
Uncommon Top-Level Domain Anomaly
A host has sent a suspicious DNS query with a top-level domain (TLD) that has never been seen
before (or has very rarely been seen). This could indicate a malware attack. Check the DNS
domain and consider blocking the host.
New or unusual TLDs might signal a threat vector, for example:

Threat actors often register new domains with rare or newly delegated TLDs to avoid
blacklists (such as, .zip, .click, or .lol).
These TLDs are frequently used for malware delivery, phishing, or Command and
Control (C&C or C2) infrastructure, especially in the early days before domain
reputation systems catch up.
Detecting new TLDs can surface early-stage recon or delivery attempts before other
threat intelligence flags them.
 The data sources for this alert type are Stellar Cyber sensor and third-party data from
vendors such as HYAS.
This alert type has the following subtypes:
Sensor DNS Data Source
Vendor DNS Data Source
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: Command and Control (TA0011 )
Technique: Application Layer Protocol (T1071 )
Tags: [DNS Anomaly; Top-Level Domain]
Event Name
The xdr_event.name for this alert type in the Interflow data is dns_new_tld.
Severity
20
Alert Subtype: Sensor DNS Data Source
The xdr_event.subtype.name for this alert subtype in the Interflow data is dns_new_tld_sensor.
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.query
metadata.request.effective_tld
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
metadata.request.query — DNS query domain, such as www.stellarcyber.ai
metadata.request.effective_tld — effective top-level domain, such as
stellarcyber.ai
days_silent — number of days since last activity

Use Case with Data Points
If a DNS query is observed to have a new top-level domain, an alert is triggered. The Interflow
includes a DNS query domain (metadata.request.query), a top-level domain
(metadata.request.effective_tld), the number of days since the same TLD was seen last
time (days_silent), and the last seen timestamp for the TLD (last_seen_ts).
Validation / Remediation
Validate the alert by checking the suspiciousness of the DNS query and block the query domain
if the domain is suspicious.
Potential False Positives
Legitimate software updates may trigger unusual DNS queries as they contact
uncommon domains for downloading updates.
Internal applications using dynamic DNS services might generate rare DNS queries.
Third-party security tools or monitoring solutions may use unique DNS queries for their
operations
Cloud services often use diverse and uncommon domains for legitimate operations.
New or infrequently accessed legitimate websites may appear as unusual.
Alert Subtype: Vendor DNS Data Source
The xdr_event.subtype.name for this alert subtype in the Interflow data is dns_new_tld_vendor.
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
dns.question.name
dns.question.top_level_domain
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — source host name
dns.question.name — DNS query domain, such as www.stellarcyber.ai
dns.question.top_level_domain — normalized top-level domain, such as .ai
days_silent — number of days since last activity
Use Case with Data Points
If a DNS query is observed to have a new top-level domain, an alert is triggered. The Interflow
includes a DNS query domain (dns.question.name), a top-level domain
(dns.question.top_level_domain), the number of days since the same TLD was seen last
time (days_silent), and the last seen timestamp for the TLD (last_seen_ts).
Validation / Remediation

Validate the alert by checking if the DNS query is suspicious and block the query domain if the
domain is suspicious.
Potential False Positives
Legitimate software updates may trigger unusual DNS queries as they contact
uncommon domains for downloading updates.
Internal applications using dynamic DNS services might generate rare DNS queries.
Third-party security tools or monitoring solutions may use unique DNS queries for their
operations
Cloud services often use diverse and uncommon domains for legitimate operations.
New or infrequently accessed legitimate websites may appear as unusual.
User Asset Access Anomaly
A user who typically uses a small, consistent number of assets was observed in Windows
logons, Kerberos service tickets, or SMB traffic to access a new asset. Investigate the asset and
user to see if this was expected.
This alert type has the following subtypes:
SMB User Based
Kerberos TGS Requests
XDR Kill Chain
Kill Chain Stage: Propagation
Tactic: [Internal] XDR UBA (XTA0004)
Technique: XDR Asset Anomaly (XT4004)
Tags: [Internal; User Behavior Analytics; Identity Detection]
Event Name
The xdr_event.name for this alert type in the Interflow data is user_asset_access.
Severity
30
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.TargetUserName
metadata.request.username
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — source user ID

dstip_host — host name of corresponding destination IP address
srcip_host — host name of corresponding source IP address
srcip_username — source user name
stability — score measuring the time since the last new asset was accessed
days_stable — time since the last new asset was accessed
diversity — score measuring the number of assets that the user accessed
child_count — number of assets that the user accessed
Use Case with Data Points
Users (srcip_usersid and srcip_username) with a small number of assets (diversity,
child_count) who also have not used a new asset (srcip_host) for a long time (stability,
days_stable) are examined. If a new asset appears on a host (srcip_host) with this user, an
alert is triggered.
The user is identified with the scrip_userid and scrip_username fields. The asset is identified
with the scrip_host field. Active Directory, which is identified from the dstip_host field,
provides the relationship between the user and the asset. Stability is identified with the
stability field and diversity is identified with the diversity field.
Alert Subtype: SMB User Based
The SMB User Based alert subtype is the same as the User Asset Access Anomaly alert type
above, with the following differences:
The subtype is more specific to SMB users authenticating to a new asset. It uses
network traffic to monitor the network shares the users accessed.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
smb_user_asset_access.
It has the following Alert Suppression Fields and Key Fields and Relevant Data
Points.
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
metadata.request.username
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
dstip — destination IP address
event_summary.ueba_smb_username — SMB user that accessed the assets
stability — score measuring the time since the last new asset was accessed
days_stable — time since the last new asset was accessed
diversity — score measuring the number of assets that the user accessed
child_count — number of assets that the user accessed
Alert Subtype: Kerberos TGS Requests

The Kerberos TGS Requests alert subtype is the same as the User Asset Access Anomaly alert
type above, with the following differences:
The subtype enhances detection of anomalous user asset relations on Windows
environments by monitoring Kerberos Ticket Granting Service (TGS) requests.
The xdr_event.subtype.name for this alert subtype in the Interflow data is
kerberos_user_asset_access.
It has the following Alert Suppression Fields and Key Fields and Relevant Data
Points.
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
event_data.TargetUserName
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event_data.IPAddress — IP address
event_data.ServiceName — Service Principal Name (SPN) servicename
event_data.TargetUserName — SPN user name
stability — score measuring the time since the last new asset was accessed
days_stable — time since the last new asset was accessed
diversity — score measuring the number of assets that the user accessed
child_count — number of assets that the user accessed
User Login Location Anomaly
A login to a user account occurred from a source IP address that is anomalously distant from the
nearest location typically observed for logins to that user account.

This alert type has a detection delay for on-time records while maintaining detection
coverage for high latency data sources. High latency data will have a detection delay
corresponding to their amount of latency.
The expected detection delay is 5-10 minutes, although it could be longer when there is an
ingestion delay. Sources without ingestion delays will get their alerts between 5 and 10
minutes after ingestion.
 You can customize the User Login Location Anomaly in the Detection Management System.
See Configuring Customizations for ML Detections.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR UBA (XTA0004)
Technique: XDR Location Anomaly (XT2001)
Tags: [External; User Behavior Analytics; Identity Detection]

Event Name
The xdr_event.name for this alert type in the Interflow data is user_login_region.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — key ID for the source user
distance_deviation — deviation in distance between two login locations (miles)
srcip_host — source host name
srcip_reputation — reputation of the source IP address
srcip_geo.countryName — source IP country name
srcip_geo.region — source IP region name
srcip_geo.city — source IP city name
login_type — type of login
has_mfa — whether a Multi-Factor Authentication (MFA) event is associated with the
current login
appId — application ID
appDisplayName — application display name
Use Case with Data Points
Successful login events for certain login types (login_type) of a user (srcip_usersid) from a
source host (srcip_host) and country location (srcip_geo.countryName are examined. If the
detected login location is too far away (distance_deviation in miles) from that user's typical
locations, an alert is triggered. The source host's reputation (srcip_reputation) is also
checked. Map views of the Interflow include data points for the closest typical login locations
for the user.
Location History Retention
To optimize location history tracking and improve detection accuracy, this alert type manages
historical data. A location history retention mechanism provides the detection model with the last
visit times and location, ensuring that more relevant data is retained for analysis and that noise
from irrelevant historical locations is reduced. Users can receive alerts for locations they have
visited in the past, if enough time has passed.
The last visited times are tracked for each location. If a user has not visited the location in a long
time, another alert can be triggered, as follows:

A user with only one location can get an alert on that location if three months have
elapsed without another visit to that location.
A user who visits lots of locations (defined as 10 unique locations in total and six
locations in the last month (30 days)), can get an alert on that location after six months.
If 50 users, sharing a tenant ID, visit a location, no further alerts for users with that
tenant ID and location will be generated.
Remove Duplicate Login Events for Microsoft 365 and Entra ID
When both Microsoft 365 and Entra ID data sources report the same login ID, Stellar Cyber will
prioritize Entra ID for alert generation of login location anomalies, provided there is no significant
ingestion delay. If Stellar Cyber can correlate the two logins by their login ID, the Entra ID record
will be sent. The Entra ID records have metadata related to MFA logins as well as specific Azure
location enrichment, that the Microsoft 365 records do not have. The Entra ID record will still be
prioritized even if it is not for MFA authentication.
However, if the Entra ID record is delayed, such as due to an ingestion delay, in order to maintain
responsiveness, the Microsoft 365 record will be sent.
And if only Microsoft 365 is configured, those logs will continue to be used exclusively.
Using ASNs and User Agents to Improve Location Alert Triage
To improve triage of location-based alerts, Stellar Cyber will begin collecting user history for
Autonomous System Number (ASN), ASN org, and user agents (if available from Microsoft 365),
and then use this history to enrich alerts.
Enrichment fields are added to alerts detailing whether that user or tenant has seen that ASN,
ASN org, or user agent before.
For the user and tenant scopes, the enriched fields are: asn_seen_before,
asn_org_seen_before, and user_agent_seen_before.
The user scope has an additional enriched field: user_start_time_ms, which is the time that
tracking ASN and user agents started, in UNIX milliseconds.
Using ASNs and user agents improves accuracy in anomaly detection and reduces false
positives. You can also use the enriched fields for Automated Threat Hunting (ATH) or alert
filtering.
User Process Usage Anomaly
A user who typically executes a small, consistent number of processes suddenly executed a new
process. Investigate the process to see if it is benign. Check with the user to see if this process
was expected.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: XDR EBA (XTA0001)
Technique: XDR Process Anomaly (XT1001)
Tags: [Process Anomaly; User Behavior Analytics; Identity Detection]

Event Name
The xdr_event.name for this alert type in the Interflow data is user_uncommon_process.
Severity
10
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip_usersid
user.name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip_usersid — non-Windows source user ID
or
user.identifier — Windows source user ID
 The key field for this alert type can be either srcip_usersid or
user.identifier, depending on the data feed.
hostip — IP address of the host
hostip_host — host name
srcip_username — source user name
wineventlog_user.name — source user name (Windows)
user.name — source user name (Windows)
process_name — name of the process
stability — score measuring the time since the last new process was executed
days_stable — time since the last new process was executed
diversity — score measuring the number of processes that the user executed
child_count — number of processes that the user executed
Use Case with Data Points
Looks for a user (srcip_usersid or user.identifier and a srcip_username) with a small
number of processes (diversity, child_count) who also has not used a new process for a
long time (stability, days_stable). If a new process (process_name) appears on a host
(srcip_host) with this user and connects to another host (dstip_host), an alert is triggered.
The user is identified with the scrip_userid or user.identifier and scrip_username fields.
The process is identified with the process_name field. The host on which the user is running the
process is identified with the srcip_host field. The destination of the traffic generated by the
process is identified with the dstip_host field. Stability is identified with the stability field,
and diversity is identified with the diversity field.
Volume Shadow Copy Deletion via VssAdmin

The vssadmin.exe utility was used to delete the Shadow Copy on an endpoint. Ransomware
and other malware do this to prevent system recovery. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Inhibit System Recovery (T1490 )
Tags: [Malware; Ransomware]
Event Name
The xdr_event.name for this alert type in the Interflow data is
ransomware_volume_shadow_copy_deletion_via_vssadminedit.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
computer_name
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host where the Shadow Copy was deleted
hostip_host — host name
process_name — name of the executed process
event_data.CommandLine — command line that is executed to delete the Shadow
Copy
Use Case with Data Points
If vssadmin.exe is used to delete the Shadow Copy on an endpoint, an alert is triggered. The
Interflow ibncludes the host IP address (hostip), process name (process_name), and command
line (event_data.CommandLine).
Volume Shadow Copy Deletion via WMIC
The wmic.exe utility was used to delete the Shadow Copy on an endpoint. Ransomware and
other malware do this to prevent system recovery. Check with the user.
XDR Kill Chain
Kill Chain Stage: Exfiltration & Impact
Tactic: Impact (TA0040 )
Technique: Inhibit System Recovery (T1490 )
Tags: [Malware; Ransomware]

Event Name
The xdr_event.name for this alert type in the Interflow data is
ransomware_volume_shadow_copy_deletion_via_wmicredit.
Severity
80
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
hostip
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
hostip — IP address of the host where the Shadow Copy was deleted
hostip_host — host name
process_name — name of the executed process
event_data.CommandLine — command line that is executed to delete the Shadow
Copy
Use Case with Data Points
If wmic.exe is used to delete the Shadow Copy on an endpoint, an alert is triggered. The
Interflow includes the host IP address (hostip), process name (process_name), and command
line (event_data.CommandLine).
WAF Internal Attacker Anomaly
Internal web requests from a private IP address have been blocked/alerted by the Web
Application Firewall (WAF). Investigate the source requester and ensure they are not
compromised.
XDR Kill Chain
Kill Chain Stage: Exploration
Tactic: [Internal] XDR NBA (XTA0002)
Technique: XDR WAF Anomaly (XT2009)
Tags: [Internal; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is waf_internal_attacker.
Severity
60
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.
srcip

Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
srcip — source IP address
srcip_host — host name of corresponding source IP address
action — status of web requests
event.severity_str — severity level of web requests
event.uri — URI of the web request
event.reason — attack type (signature name)
The above fields are standardized to support a variety of WAFs. The original fields, listed below,
remain in the F5 WAF Interflow record for backward compatibility.
List of F5 legacy fields
|     | Original Stellar Cyber | Standardized Stellar Cyber |
| --- | ---------------------- | -------------------------- |
F5 Field Purpose
WAF Field Name WAF Field Name
| Signature ID        | f5.sig_ids          | event.sig_id          |
| ------------------- | ------------------- | --------------------- |
| Signature name      | f5.sig_names        | event.reason          |
| Staged signature ID | f5.staged_sig_ids   | event.staged_sig_id   |
| Staged signature ID | f5.staged_sig_names | event.staged_sig_name |
| Violation           | f5.violations       | event.violations      |
| Sub violation       | f5.sub_violations   | event.sub_violations  |
Threat campaign f5.threat_campaign_names event.threat_campaign_names
| Request status | f5.request_status | action             |
| -------------- | ----------------- | ------------------ |
| Severity       | f5.severity       | event.severity_str |
| Attack type    | f5.attack_type    | threat             |
| Client IP      | srcip             |                    |
srcip
service.origin.ip
| Client Port | srcport |     |
| ----------- | ------- | --- |
srcport
service.origin.port
| Service IP | dstip | dstip |
| ---------- | ----- | ----- |
service.target.ip
| Service Port | dstport | dstport |
| ------------ | ------- | ------- |
service.target.port
| Violation Details | f5.violation_details | event.description |
| ----------------- | -------------------- | ----------------- |
Telemetry Event f5.telemetryEventCategory event.telemetry_event_category
Category
| url | f5.uri | event.uri |
| --- | ------ | --------- |
Web application name f5.web_application_name event.web_application_name
Use Case with Data Points

If web requests (f5.uri) from an internal IP address (srcip) to a web application
(f5.web_application_name) have been blocked/alerted (f5.request_status) by the WAF, an alert is
triggered. The Interflow includes the level of severity (f5.severity), the attack type
(f5.attack_type), and the violation information (f5.violations), as well as signature name
(f5.sig_names), staged signature name (f5.staged_sig_names), sub violation information
(f5.sub_violations), and threat campaign name (f5.violation_details_xml.request-
violations.violation.threat_campaign_data.threat_campaign_name), if applicable.
If web requests (event.uri) from an internal IP address ( srcip) to a web application
(event.web_application_name) have been blocked/alerted (action) by the WAF, an alert is
triggered. The Interflow includes the level of severity (event.severity_str), the attack type
(threat), and the violation information (event.description), as well as signature name
(event.reason). If applicable for the WAF type, the Interflow also includes staged signature
name (event.staged_sig_id), sub violation information (event.sub_violations), and threat
campaign name (event.threat_campaign.names).
Ingestion Types Supported for this Alert
F5 Big-IP Firewall
F5 Silverline WAF
Barracuda WAF
AWS CloudWatch WAF
Imperva Incapsula
WAF Rule Violation Anomaly
Web requests have been blocked/alerted by the Web Application Firewall (WAF) due to a surge
in violations or violating a rule that is rarely invoked. Investigate the blocked/alerted web requests
and ensure they are benign.
 Refer to Log Parser Portsfor the most current list of WAF parsers.
XDR Kill Chain
Kill Chain Stage: Initial Attempts
Tactic: [External] XDR NBA (XTA0002)
Technique: XDR Rule Violation (XT2004)
Tags: [External; Network Traffic Analysis]
Event Name
The xdr_event.name for this alert type in the Interflow data is waf_rule_violation.
Severity
50
Alert Suppression Fields
Alert suppression fields are attribute values that trigger deduplication of alerts sharing them.

event.sig_id
Key Fields and Relevant Data Points
Key fields are meaningful and human-readable data points representing observable(s) being
detected.
event.sig_id — signature ID
srcip — source IP address
srcip_host — host name of corresponding source IP address
event.severity_str — severity level of web requests
event.web_application_name — web application name
event.uri — URI of the web request
event.reason — signature name
actual — actual number of specific WAF violations in the period
typical — typical number of specific WAF violations in the period
The above fields are standardized to support a variety of WAFs. The original fields, listed below,
remain in the F5 WAF Interflow record for backward compatibility.
List of F5 legacy fields
|     | Original Stellar Cyber | Standardized Stellar Cyber |
| --- | ---------------------- | -------------------------- |
F5 Field Purpose
WAF Field Name WAF Field Name
| Signature ID        | f5.sig_ids          | event.sig_id          |
| ------------------- | ------------------- | --------------------- |
| Signature name      | f5.sig_names        | event.reason          |
| Staged signature ID | f5.staged_sig_ids   | event.staged_sig_id   |
| Staged signature ID | f5.staged_sig_names | event.staged_sig_name |
| Violation           | f5.violations       | event.violations      |
| Sub violation       | f5.sub_violations   | event.sub_violations  |
Threat campaign f5.threat_campaign_names event.threat_campaign_names
| Request status | f5.request_status | action             |
| -------------- | ----------------- | ------------------ |
| Severity       | f5.severity       | event.severity_str |
| Attack type    | f5.attack_type    | threat             |
| Client IP      | srcip             |                    |
srcip
service.origin.ip
| Client Port | srcport |     |
| ----------- | ------- | --- |
srcport
service.origin.port
| Service IP | dstip | dstip |
| ---------- | ----- | ----- |
service.target.ip
| Service Port | dstport | dstport |
| ------------ | ------- | ------- |
service.target.port
| Violation Details | f5.violation_details | event.description |
| ----------------- | -------------------- | ----------------- |
Telemetry Event f5.telemetryEventCategory event.telemetry_event_category
Category

Original Stellar Cyber Standardized Stellar Cyber
F5 Field Purpose
WAF Field Name WAF Field Name
url f5.uri event.uri
Web application name f5.web_application_name event.web_application_name
Use Case with Data Points
If web requests (event.uri) to a web application ( event.web_application_name) have been
blocked/alerted (action) by the WAF due to violating certain rules, which include the level of
severity (event.severity_str), the attack type (threat), and the violation information
(event.violations). If the violations (actual) surge compared to the normal number of
violations in a period (typical), an alert is triggered.
Ingestion Types Supported for this Alert
F5 Big-IP Firewall
F5 Silverline WAF
Barracuda WAF
AWS CloudWatch WAF
Imperva Incapsula
Windows Network Access Suspicious desktop.ini Action
The Windows Network Access Suspicious desktop.ini Action rules detect suspicious SMB traffic
accessing desktop.ini files. Any one or more of these will trigger the Windows Network Access
Suspicious desktop.ini Action alert type.
XDR Kill Chain
Kill Chain Stage: Persistent Foothold
Tactic: Persistence (TA0003 )
Technique: Boot or Logon Autostart Execution (T1547 )
Sub-technique: Shortcut Modification (T1547.009 )
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
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  