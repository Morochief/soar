Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Bucket
Enumeration Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious bucket enumeration activity in OCI. Any one or
more of these will trigger the Suspicious OCI Bucket Enumeration Alert. Details for each rule can
be viewed by clicking the More Details link in the description.

Title

Description

OCI Potential
Bucket Enumeration

Looks for potential enumeration of OCI buckets via ListBuckets. A bucket is a container for storing
objects in a compartment within a namespace.

More details

Rule ID

oci_audit_14

Query

{'selection': {'eventName': 'listbuckets'}, 'filter1': {'principal
Id|contains': ['.instance.', ':cloudguard-
agent:']}, 'filter2': {'principalId|startswith': 'cloudguard/'}, '
condition': 'selection and not (filter1 or filter2)'}

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

Creation
Date

Risk
Level

experim
ental

2025/02/
25

low

False Positives

Administrators listing buckets, it may be necessary to filter out
users who commonly conduct this activity.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

