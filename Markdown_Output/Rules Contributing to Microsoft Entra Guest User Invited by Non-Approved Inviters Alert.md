✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra Guest
User Invited by Non-Approved Inviters Alert
The following rules are used to identify suspicious Microsoft Entra guest user invited by non-
approved inviters. Any one or more of these will trigger the Microsoft Entra Guest User Invited by
Non-Approved Inviters Alert. Details for each rule can be viewed by clicking the More Details link
in the description.
Title Description
Guest User Invited by Detects when a user that doesn't have permissions to invite a guest user attempts to invite one.
Non-Approved Inviters
More details
Rule ID
azure_38
Query
{'selection': {'Result': 'failure', 'properties_message': 'Invi
te external user'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,0b4b72e3-4c53-4d5b-b198-2c58cfef39a9
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#things-to-monitor 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId

Title Description
stellar.rule_id
Additional Information
| Maturity   | Creation   | Risk False Positives |
| ---------- | ---------- | -------------------- |
|            | Date       | Level                |
| experiment | 2022/08/10 | medium               |
A non malicious user is unaware of the proper
al process
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        