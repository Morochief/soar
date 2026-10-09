Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Logging
Activity Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious logging activity in OCI. Any one or more of
these will trigger the Suspicious OCI Logging Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.

Title

Description

OCI Log Group
Deletion

Identifies the deletion of a specified OCI LogGroup. When a log group is deleted, all the archived log entries
associated with the log group are also permanently deleted.

More details

Rule ID

oci_audit_10

Query

{'selection': {'eventName': 'deleteloggroup'}, 'condition': 'selection
'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1562.001 , TA0040 , T1485 

References
N/A

Severity

50

Suppression Logic Based On

Title

Description

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturi
ty

Creati
on
Date

Risk
Level

experi
mental

2025/0
2/24

medi
um

False Positives

Verify whether the user identity, user agent, and/or hostname should be
making changes in your environment. Log group deletions by unfamiliar
users or hosts should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

If this rule is noisy in your environment due to expected activity, consider
adding exceptions — preferably with a combination of user and IP
address conditions.

OCI Log Object
Deletion

Identifies the deletion of an OCI log object, which permanently deletes all associated archived log entries.

More details

Rule ID

oci_audit_11

Query

{'selection': {'eventName': 'deletelog'}, 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1562.001 , TA0040 , T1485 

References
N/A

Severity

50

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturi
ty

Creati
on
Date

Risk
Level

experi
mental

2025/0
2/24

medi
um

False Positives

A log object may be deleted by a system administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in
your environment. Log deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

If this rule is noisy in your environment due to expected activity, consider
adding exceptions — preferably with a combination of user and IP
address conditions.

OCI Log Object
Updated

Identifies an update to an existing OCI log object with configuration that specifies the delivery of log files.

More details

Title

Description

Rule ID

oci_audit_13

Query

{'selection': {'eventName': 'updatelog'}, 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0009 , T1530 , TA0040 , T1565.001 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturi
ty

Creati
on
Date

Risk
Level

experi
mental

2025/0
2/25

low

False Positives

Log object updates may be made by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname should be
making changes in your environment. Log object updates from unfamiliar
users or hosts should be investigated. If known behavior is causing false
positives, it can be exempted from the rule -- preferably with a
combination of user and IP address conditions.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

