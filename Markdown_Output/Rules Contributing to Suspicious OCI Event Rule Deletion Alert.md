✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious OCI Event
Rule Deletion Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify suspicious deletion activity of event rules in OCI. Any one
or more of these will trigger the Suspicious OCI Event Rule Deletion Alert. Details for each rule
can be viewed by clicking the More Details link in the description.
Title Description
OCI Event Rule Detects when event rule was deleted.
Deleted
More details
Rule ID
oci_audit_18
Query
{'selection': {'eventName': 'deleterule'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
N/A
Severity
75
Suppression Logic Based On
oracle.data.resourceId

Title Description
oracle.data.eventName
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/02/27    | high       | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        