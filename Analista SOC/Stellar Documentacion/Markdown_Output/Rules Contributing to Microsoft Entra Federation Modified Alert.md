✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra Federation
Modified Alert
The following rules are used to identify suspicious Microsoft Entra federation modified activity.
Any one or more of these will trigger the Microsoft Entra Federation Modified Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Title Description
Azure Domain Identifies when a user or application modified the federation settings on the domain.
Federation Settings
More details
Modified
Rule ID
azure_45
Query
{'selection': {'ActivityDisplayName': 'Set federation settings o
n domain'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,352a54e1-74ba-4929-9d47-8193d67aba1e
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0005 , T1484 
References
https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-monitor-
federation-changes 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Title Description
Additional Information
| Matur Creati | Risk False Positives |     |
| ------------ | -------------------- | --- |
| ity on       | Level                |     |
Date
| experi 2021/0 | medi |     |
| ------------- | ---- | --- |
Federation Settings being modified or deleted may be performed
| menta 9/06 | um  | by a system administrator. |
| ---------- | --- | -------------------------- |
l
Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.
Federation Settings modified from unfamiliar users should be
investigated. If known behavior is causing false positives, it can
be exempted from the rule.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        