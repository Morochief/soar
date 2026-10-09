Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious OCI Security
Service Impairment Alert

 This topic covers a feature that is not available for all customers yet. See Early Access

Program Features and Topics Under Development.

The following rules are used to identify suspicious impairment activity to security services in OCI.
Any one or more of these will trigger the Suspicious OCI Security Service Impairment Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

OCI Impair
Security Services

Description

Identifies attempts to delete critical OCI security service configurations, such as CloudGuard detector
recipes and recipes from Vulnerability Scanning Service (VSS). This activity is significant because it
indicates potential efforts to disable security monitoring and evade detection. If confirmed malicious, this
could allow attackers to operate undetected, escalate privileges, or exfiltrate data without triggering
security alerts, severely compromising the security posture of the OCI environment.

More details

Rule ID

oci_audit_12

Query

{'selection': {'eventName': ['deletecontainerscanrecipe', 'deletehos
tscanrecipe', 'deletecontainerscantarget', 'deletehostscantarget', '
deletedetectorrecipe', 'deletedetectorrecipedetectorrule', 'deletede
tectorrecipedetectorruledatasource']}, 'condition': 'selection'}

Log Source

Stellar Cyber OCI configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1562.001 

References
N/A

Title

Description

Severity

75

Suppression Logic Based On

oracle.data.resourceId
oracle.data.eventName
stellar.rule_id

Additional Information

Maturi
ty

Creati
on
Date

Risk
Level

experi
mental

2025/0
2/24

high

False Positives

Routine maintenance or administrative actions may lead to the deletion
of a detector or scan recipe. Verify if the deletion aligns with scheduled
maintenance or administrative tasks.

Automated scripts or tools used for environment cleanup might
inadvertently delete detector or scan recipes. Review and adjust
automation scripts to prevent unintended deletions.

Organizational policy changes or restructuring could result in recipe
deletions. Ensure that policy changes are communicated and
understood by all relevant teams to avoid unnecessary deletions.

Exclude known and authorized users or roles from triggering alerts by
creating exceptions for specific IAM roles or user accounts that are
responsible for legitimate recipe deletions.

Implement logging and alerting for recipe deletions to quickly identify
and verify the legitimacy of the action, allowing for rapid response to
potential false positives.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

