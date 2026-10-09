Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Application
Deleted Alert

The following rules are used to identify events when a Microsoft Entra application is deleted. Any
one or more of these will trigger the Microsoft Entra Application Deleted Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Azure
Application
Deleted

Identifies when an application is deleted in Azure.

Description

More details

Rule ID

azure_80

Query

{'selection': {'properties_message': ['Delete application', 'Hard Del
ete application']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,410d2a41-1e6d-452f-85e5-abdd8257a823

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1489 

References

https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-audit-
activities#application-proxy 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Title

Description

Additional Information

Matu
rity

Creatio
n Date

Risk
Level

test

2021/09
/03

mediu
m

False Positives

Application being deleted may be performed by a system administrator.

Verify whether the user identity, user agent, and/or hostname should be
making changes in your environment.

Application deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

