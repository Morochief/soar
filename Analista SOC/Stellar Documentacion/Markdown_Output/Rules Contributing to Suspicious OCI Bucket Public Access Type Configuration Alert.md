Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Bucket
Public Access Type Configuration Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious public access type configuration of OCI
buckets. Any one or more of these will trigger the Suspicious OCI Bucket Public Access Type
Configuration Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

OCI Bucket Public
Access Type
Configuration

Identifies potential OCI bucket misconfiguration of public access type. A bucket is a container for
storing objects in a compartment within a namespace. If a bucket that contains sensitive
information is set to be public accessible, it can lead to subsequent data exfiltration.

More details

Rule ID

oci_audit_24

Query

{'selection': {'eventName': ['createbucket', 'updatebucket']},
'filter1': {'publicAccessType': 'NoPublicAccess'}, 'condition':
 'selection and not filter1'}

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

Maturit
y

Creatio
n Date

Risk
Level

experi
mental

2025/04
/16

low

False Positives

A bucket could be intentionally configured to be publicly
accessible and does not contain any sensitive information.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

