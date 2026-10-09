Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Instance
Image Export Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious instance image export activity in OCI. Any one
or more of these will trigger the Suspicious OCI Instance Image Export Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Description

OCI Instance Image
Export Failure

Identifies a failed attempt to export an OCI instance. A virtual machine (VM) export may indicate an
attempt to extract or exfiltrate information.

More details

Rule ID

oci_audit_16

Query

{'selection1': {'eventName': 'exportimage'}, 'selection2': {'statu
s': ['400', '401', '404', '409', '412']}, 'condition': 'selection1
 and selection2'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0009 , T1005 , TA0010 , T1537 

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
2/26

Matur
ity

experi
menta
l

False Positives

VM exports may be done by a system or network administrator. Verify
whether the user identity, user agent, and/or hostname should be
making changes in your environment. VM exports from unfamiliar
users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.

Routine backup operations may trigger the rule if they involve failed
export attempts. To manage this, identify and whitelist specific IAM
roles or users that regularly perform legitimate backup tasks.

Development and testing environments often involve frequent export
attempts for non-production instances. Exclude these environments
by tagging instances appropriately and adjusting the detection rule to
ignore these tags.

Misconfigured export tasks due to incorrect permissions or settings
can lead to false positives. Regularly review and update IAM policies
and export configurations to ensure they align with intended
operations.

Automated scripts or tools that manage instances might occasionally
fail due to transient issues, causing false alerts. Monitor and log these
scripts' activities to distinguish between expected failures and
potential threats.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

