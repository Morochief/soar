Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Object
Storage Activity Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious object storage activity in OCI. Any one or more
of these will trigger the Suspicious OCI Object Storage Activity Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

OCI Defense Evasion
PutObjectLifecyclePolicy

This analytic identifies `PutObjectLifecyclePolicy` events in OCI audit logs where a user has
created or replaced an object lifecycle policy for a bucket. This detection leverages OCI logs to
identify suspicious lifecycle configurations. This activity is significant because attackers may use it
to delete logs quickly, thereby evading detection and impairing forensic investigations. If confirmed
malicious, this could allow attackers to cover their tracks, making it difficult to trace their actions
and respond to the breach effectively.

More details

Rule ID

oci_audit_9

Query

{'selection1': {'eventName': 'putobjectlifecyclepolicy'}, 'sele
ction2': {'status': '200'}, 'condition': 'selection1 and select
ion2'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1562.008 , TA0040 , T1485.001 

References
N/A

Title

Description

Severity

50

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
2/24

medi
um

experi
menta
l

False Positives

While this search has no known false positives, it is possible
that it is a legitimate admin activity. Please consider filtering out
these noisy events.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

