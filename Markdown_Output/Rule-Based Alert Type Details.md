Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rule-Based Alert Type Details

Rule-based detection detects anomalies by observing events in the system and applying a set of
rules that lead to a decision.

Certain Stellar Cyber alert types are based on specific rules. This topic describes information
relating to rule-based alert types as well as some differences between rule-based and Machine
Learning (ML) alert types.

Rule-Based Alerts Kill Chain Mapping
Rule-based alerts have general kill chain mapping information such as Stage, Tactic, and
Technique, as follows:

Based on what the rule detects, each rule can have a different Stage, Tactic, and Technique, as
follows:

Getting Rule-Based Alerts Details
In the Actions column of the table, click i or More Info to display details on an individual rule-
based alert.

To get the Knowledge Base description for an individual rule-based alert, in the Key Fields tab,
click the Stellar Rule ID link, for example, process_creation_17.

For links to the Knowledge Base description for all rule-based alert types, see Rule-Based Alert
Types.

Rule Matching in Queries
Rule matching in queries includes both case-sensitive matching and case-insensitive matching.
Whether to use case-sensitive or case-insensitive matching depends on the rule as well as the
relevant fields specified in the rule.

For example, case-sensitive matching means using the exact query string. For example, if get is
expected, Stellar Cyber will not trigger an alert for Get or GET.

For case-insensitive matching, Stellar Cyber will trigger an alert for get, Get, and GET.

In general, rule matching is case-sensitive, but there are exceptions. For the following rules and
fields, case-insensitive matching is being used on:

Suspicious PowerShell Script: event_data.ScriptBlockText

Suspicious Process Creation Commandline (currently Windows only):
event_data.CommandLine and event_data.ParentCommandLine

Suspicious Windows Network Connection: event_data.Image

Suspicious LSASS Process Access: event_data.CallTrace and
event_data.TargetImage and event_data.SourceImage

Abnormal Parent / Child Process: parent_proc_name and process_name

Miscellaneous IDS rules: ids.signature

Windows Rule-Based Alerts

 Windows rule-based alerts require the updated Windows Detection Profile (Low Volume) in

the sensor profile settings.

Metadata for Rule-Based Alerts
For alert types from rule-based detection, the Rules tab displays the rule's metadata.

The Rules tab displays metadata about the rule itself, such as the name of the rule, description,
status, rule ID, and other fields. It also displays the rule configuration in YAML format, which you
can download.

Maturity Status

In the YAML format in the Rules tab, there is a maturity status, for example, maturity: test.
Stellar Cyber passes any status from Sigma or other open source rule sources. It also develops
rules internally.

The following are the maturity statuses for both Sigma and non-Sigma rules:

Production—for rules that are reliable in a production environment

Stable—for rules that have had one year of use

Test—for rules that have had months of use

Experimental—for new rules

The status of a rule may be updated in the future based on observations made.

Number of Rule-Based Alerts
The number of rule-based alerts of each type are as follows:

Rule-Based Alert Types

PowerShell Script

Process Creation Commandline

Process Creation Parent/Child

Active Directory (AD)

AWS

DNS

Microsoft Entra (formerly Azure AD)

Microsoft Office 365

Oracle Cloud Infrastructure (OCI)

Traffic (see Limitations of Rule-Based Traffic Alert

Types)

Windows, including:

Identity and Threat Detection Rules (ITDR)
(3)

Windows Security (113)

Process Creation Image (25)

Windows Network Connection (5)

# of Rules

133

239

66

2

102

5

71

6

28

13

159

Rule-Based Alert Types

# of Rules

Windows Process Access (6)

Windows Registry Set (2)

certutil.exe Certificate Extraction (1)

Mimikatz Credential Dump (1)

Encoded PowerShell (1)

PowerShell Remote Access (2)

Total

824

For links to the Knowledge Base description for all rule-based alert types, see Rule-Based Alert
Types.

Limitations of Rule-Based Traffic Alert Types

Stellar Cyber parses the ICMP/SMB traffic and gathers all necessary information related
to the attack activities into one record to perform Sigma rule matching on these records.
However, sometimes the SMB traffic is split by the network sensor into different records
and this will potentially cause false negatives.

SMB/SMB2 protocols are supported, as well as SMB 3.0 when SMB Multichannel is not
in use. Stellar Cyber only performs detection with these protocols AND when SMB
encryption is not enabled.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

