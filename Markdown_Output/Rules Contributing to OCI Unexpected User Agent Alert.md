✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to OCI Unexpected User
Agent Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify unexpected user agents in OCI. Any one or more of these
will trigger the OCI Unexpected User Agent Alert. Details for each rule can be viewed by clicking
the More Details link in the description.
Title Description
OCI Unexpected User Detects unexpected user agent strings.
Agent
More details
Rule ID
oci_audit_23
Query
{'selection': {'userAgent|re': '^.
{1,10}$'}, 'condition': 'selection'}
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
oracle.data.identity.userAgent

Title Description
srcip
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/03/04    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        