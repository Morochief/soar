Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI IAM
Activity: Impact Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious OCI IAM activity usually in the impact stage.
Any one or more of these will trigger the Suspicious OCI IAM Activity: Impact Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

OCI IAM Successful
Group Deletion

Identifies the deletion of a specified Oracle Cloud Infrastructure (OCI) Identity and Access Management
(IAM) group, which is a collection of users who share a similar set of access privileges. The group must
be empty.

More details

Rule ID

oci_audit_1

Query

{'selection1': {'eventName': 'deletegroup'}, 'selection2': {'statu
s': ['200', '204']}, 'condition': 'selection1 and selection2'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1531 

References
N/A

Severity

25

Title

Description

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Risk
Leve
l

low

Creati
on
Date

2025/0
2/21

Matur
ity

experi
menta
l

False Positives

Routine administrative tasks may trigger alerts when IAM groups are
deleted as part of regular maintenance or restructuring. To manage
this, create exceptions for known maintenance periods or specific
administrative accounts.

Automated scripts or tools that manage IAM resources might delete
groups as part of their normal operation. Identify these scripts and
exclude their actions from triggering alerts by using specific user or
role identifiers.

Temporary groups created for short-term projects or testing purposes
might be deleted frequently. Document these groups and exclude
their deletion from monitoring by using naming conventions or tags.

Changes in organizational structure or policy might necessitate the
deletion of certain groups. Coordinate with relevant teams to
anticipate these changes and adjust monitoring rules accordingly.

OCI IAM Deactivation
of MFA Device

Identifies the deactivation of a specified multi-factor authentication (MFA) time-based one-time
password (TOTP) device and removes it from association with the user for which it was originally
enabled.

More details

Rule ID

oci_audit_15

Query

{'selection': {'eventName': 'deletemfatotpdevice'}, 'condition': '
selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1531 , TA0003 , T1556.006 

References
N/A

Severity

50

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Title

Description

Matur
ity

Creati
on
Date

Risk
Level

2025/0
2/26

medi
um

experi
menta
l

False Positives

A MFA device may be deactivated by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. MFA
device deactivations from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

While this activity can be done by administrators, all users must use
MFA. The security team should address any potential benign true
positive (B-TP), as this configuration can risk the user and domain.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

