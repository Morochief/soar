Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI
Kubernetes Activity Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious Kubernetes activity in OCI. Any one or more of
these will trigger the Suspicious OCI Kubernetes Activity Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

OCI Kubernetes Cluster
Created or Deleted

Detects when an OCI Kubernetes Cluster is created or deleted.

More details

Rule ID

oci_audit_17

Query

{'selection': {'eventName': ['createcluster', 'deletecluster']},
 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1485 

References
N/A

Severity

25

Suppression Logic Based On

oracle.data.resourceId

Title

Description

oracle.data.eventName
stellar.rule_id

Additional Information

Matur
ity

Creati
on
Date

Risk
Leve
l

low

2025/0
2/27

experi
menta
l

False Positives

Kubernetes cluster being created or deleted may be performed by
a system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment.

Kubernetes cluster created or deleted from unfamiliar users should
be investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

