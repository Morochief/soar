✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra ID MFA
Disabled Alert
The following rules are used to identify events when a Microsoft Entra ID multi-factor
authentication is disabled. Any one or more of these will trigger the Microsoft Entra ID MFA
Disabled Alert. Details for each rule can be viewed by clicking the More Details link in the
description.
Title Description
Disabled MFA to Bypass Detection for when multi-factor authentication has been disabled, which might indicate a
Authentication Mechanisms malicious activity to bypass authentication mechanisms.
More details
Rule ID
azure_52
Query
{'selection': {'properties_message': 'Disable Strong Authenti
cation', 'result': 'success'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,7ea78478-a4f9-42a6-9dcd-f861816122bf
Author: @ionsor
Tactics, Techniques, and Procedures
TA0005 , T1556.006 
References
https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-
userstates 
Severity
50
Suppression Logic Based On
azure ad.initiatedBy.user.id

_ y
Title Description
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
| Maturity Creation Date | Risk Level | False Positives |
| ---------------------- | ---------- | --------------- |
| test 2022/02/08        | medium     |                 |
Authorized modification by administrators
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        