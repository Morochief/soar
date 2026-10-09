✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to OCI Insecure Metadata
Endpoint Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify potentially insecure metadata endpoints in OCI. Any one
or more of these will trigger the OCI Insecure Metadata Endpoint Alert. Details for each rule can
be viewed by clicking the More Details link in the description.
Title Description
OCI Insecure Detects insecure metadata endpoint.
Metadata Endpoint
More details
Rule ID
oci_audit_19
Query
{'selection': {'url|contains': ['/opc/v1', '/openstack'], 'status'
: '200'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1069 
References
N/A
Severity
75
Suppression Logic Based On
oracle.data.resourceId

Title Description
oracle.data.request.headers.oci-original-url
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/02/27    | high       | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        