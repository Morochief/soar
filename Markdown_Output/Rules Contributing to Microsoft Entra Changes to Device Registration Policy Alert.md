✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra Changes
to Device Registration Policy Alert
The following rules are used to identify suspicious Microsoft Entra changes to device registration
policy. Any one or more of these will trigger the Microsoft Entra Changes to Device Registration
Policy Alert. Details for each rule can be viewed by clicking the More Details link in the
description.
Title Description
Changes to Device Monitor and alert for changes to the device registration policy.
Registration Policy
More details
Rule ID
azure_27
Query
{'selection': {'Category': 'Policy', 'ActivityDisplayName': 'Set
device registration policies'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,9494bff8-959f-4440-bbce-fb87a208d517
Author: Michael Epping, '@mepples21'
Tactics, Techniques, and Procedures
TA0005 , T1484 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-operations-
devices#device-registrations-and-joins-outside-policy 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId

Title Description
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2022/06/28    | high       |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        