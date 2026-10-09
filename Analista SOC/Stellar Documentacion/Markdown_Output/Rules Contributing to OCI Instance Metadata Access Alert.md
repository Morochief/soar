✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to OCI Instance Metadata
Access Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify suspicious metadata access of OCI instances. Any one or
more of these will trigger the OCI Instance Metadata Access Alert. Details for each rule can be
viewed by clicking the More Details link in the description.
Title Description
OCI Instance Metadata Detects instance metadata access.
Access
More details
Rule ID
oci_vcn_2
Query
{'selection': {'dstip': '169.254.169.254'}, 'condition': 'sele
ction'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1069 
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
| experimental | 2025/02/28    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        