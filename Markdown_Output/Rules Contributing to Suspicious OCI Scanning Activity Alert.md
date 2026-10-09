✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious OCI Scanning
Activity Alert
 This topic covers a feature that is not available for all customers yet. See Early Access
Program Features and Topics Under Development.
The following rules are used to identify suspicious scanning activity in OCI. Any one or more of
these will trigger the Suspicious OCI Scanning Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.
Title Description
OCI SSH Detects possible SSH scanning activity.
Scanner
More details
Rule ID
oci_vcn_3
Query
{'selection1': {'action': 'REJECT', 'dstip_type': 'private', 'dstport':
22}, 'selection2': {'srcip_type': 'private'}, 'condition': 'selection1 a
nd not selection2 | count(dstip) by srcip > 5', 'timeframe': '5m'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0043 , T1595 
References
N/A
Severity
75
Suppression Logic Based On

Title Description
srcip
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/03/03    | high       | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        