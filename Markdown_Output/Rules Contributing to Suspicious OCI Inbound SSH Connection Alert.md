✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious OCI Inbound
SSH Connection Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify suspicious inbound SSH connection activity in OCI. Any
one or more of these will trigger the Suspicious OCI Inbound SSH Connection Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Title Description
OCI Inbound SSH Detects inbound SSH connection.
Connection
More details
Rule ID
oci_vcn_1
Query
{'selection1': {'srcip_type': 'private'}, 'selection2': {'dstport':
22}, 'condition': 'not selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
srcip

Title Description
dstip
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/02/27    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        