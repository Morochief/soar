Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI IAM
Activity: Persistence Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious OCI IAM activity usually in the persistence
stage. Any one or more of these will trigger the Suspicious OCI IAM Activity: Persistence Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

OCI IAM Failure
Group Deletion

Description

Identifies failed attempts to delete OCI IAM groups, detecting events where the DeleteGroup action fails
due to errors like Forbidden, Not Found, or Conflict. This activity is significant as it may indicate
unauthorized attempts to modify IAM group configurations, which could be a precursor to privilege
escalation or other malicious actions. If confirmed malicious, this could allow an attacker to disrupt IAM
policies, potentially leading to unauthorized access or denial of service within the OCI environment.

More details

Rule ID

oci_audit_2

Query

{'selection1': {'eventName': 'deletegroup'}, 'selection2': {'status
': ['400', '401', '403', '404', '409', '412', '429']}, 'condition':
 'selection1 and selection2'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 

References
N/A

Title

Description

Severity

10

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Matur
ity

Creati
on
Date

Risk
Level

2025/0
2/21

medi
um

experi
menta
l

False Positives

This detection will require tuning to provide high fidelity detection
capabilities. Tune based on src addresses (corporate offices, VPN
terminations) or by groups of users. Not every user with OCI access
should have permission to delete groups (least privilege).

OCI IAM Delete
Policy

The following detection identifies when a policy is deleted on OCI. This does not identify whether
successful or failed, but the error messages tell a story of suspicious attempts.

More details

Rule ID

oci_audit_3

Query

{'selection': {'eventName': 'deletepolicy'}, 'condition': 'selectio
n'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 

References
N/A

Severity

20

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Risk
Level

Creati
on
Date

2025/0
2/21

medi
um

Matur
ity

experi
menta
l

False Positives

This detection will require tuning to provide high fidelity detection
capabilities. Tune based on src addresses (corporate offices, VPN
terminations) or by groups of users. Not every user with OCI access
should have permission to delete policies (least privilege). In addition,
this may be saved separately and tuned for failed or success attempts
only.

Title

Description

OCI IAM Group
Creation

Identifies the creation of a group in Oracle Cloud Infrastructure (OCI) Identity and Access Management
(IAM). Groups specify permissions for multiple users. Any user in a group automatically has the
permissions that are assigned to the group.

More details

Rule ID

oci_audit_4

Query

{'selection': {'eventName': 'creategroup'}, 'condition': 'selection
'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1136 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Risk
Level

low

Creati
on
Date

2025/0
2/24

Matur
ity

experi
menta
l

False Positives

Routine administrative actions by authorized personnel can trigger
alerts. Regularly review and document legitimate group creation
activities to differentiate them from unauthorized actions.

Automated scripts or tools used for infrastructure management may
create groups as part of their normal operation. Identify and whitelist
these scripts to prevent unnecessary alerts.

Temporary groups created for short-term projects or testing purposes
might be flagged. Implement a naming convention for such groups and
exclude them from alerts based on this pattern.

Scheduled tasks or maintenance activities that involve group creation
should be logged and approved in advance. Use these logs to create
exceptions in the detection rule.

Third-party integrations or services that require group creation for
functionality can cause false positives. Verify these integrations and
adjust the rule to exclude their known actions.

OCI IAM Policy
Modification

OCI IAM policies associated with a user have been modified.

More details

Rule ID

oci_audit_8

Query

Title

Description

{'selection': {'eventName': ['addusertogroup', 'removeuserfromgroup
']}, 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1098 

References
N/A

Severity

50

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2025/02/24

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

