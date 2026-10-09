Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to OCI Insecure NFS Export
Configuration Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify insecure NFS export configuration in OCI. Any one or
more of these will trigger the OCI Insecure NFS Export Configuration Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Description

OCI Insecure
NFS Export

Identifies potentially insecure OCI NFS server export configuration. If the NFS server is poorly configured
(e.g., no IP or read-only restrictions and no root squash), malicious hosts can mount the file systems and
lead to subsequent data exfiltration.

More details

Rule ID

oci_audit_25

Query

{'selection': {'eventName': ['createexport', 'updateexport']}, 'filte
r1': {'exportSource': '0.0.0.0/0'}, 'filter2': {'exportAccess': 'READ
_ONLY'}, 'filter3': {'exportIdentitySquash': 'NONE'}, 'condition': 's
election and (filter1 or not filter2 or filter3)'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0007 , T1580 

References
N/A

Severity

Title

Description

25

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturity Creation

Date

experim
ental

2025/04/
16

Risk
Level

low

False Positives

An NFS server could be intentionally configured without IP or read-
only restrictions, or without root squash.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

