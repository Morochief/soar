✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to OCI Discovery Activity
Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify suspicious discovery activity in OCI. Any one or more of
these will trigger the OCI Discovery Activity Alert. Details for each rule can be viewed by clicking
the More Details link in the description.
Title Description
OCI Discovery Detects possible discovery activity.
Activity
More details
Rule ID
oci_audit_20
Query
{'selection': {'eventName|startswith': ['get', 'list']}, 'condition':
'selection | count() by CreatedBy > 20', 'timeframe': '10m'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.definedTags.Oracle-Tags.CreatedBy

Title Description
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/03/03    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        