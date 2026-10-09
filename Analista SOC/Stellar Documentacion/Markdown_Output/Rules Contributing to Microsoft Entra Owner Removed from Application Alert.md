Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Owner
Removed from Application Alert

The following rules are used to identify events when a Microsoft Entra owner is removed from an
application. Any one or more of these will trigger the Microsoft Entra Owner Removed from
Application Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

Azure Owner Removed from
Application or Service Principal

Identifies when an owner was removed from an application or service principal in Azure.

More details

Rule ID

azure_57

Query

{'selection': {'properties_message': ['Remove owner from se
rvice principal', 'Remove owner from application']}, 'condi
tion': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,636e30d5-3736-42ea-96b1-e6e2f8429fd6

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1070 

References

https://docs.microsoft.com/en-us/azure/active-directory/reports-
monitoring/reference-audit-activities#application-proxy 

Severity

50

Suppression Logic Based On

azure ad.initiatedBy.user.id

Title

Description

_

y

azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Mat
urit
y

Creati
on
Date

test 2021/0

9/03

Risk
Level

medi
um

False Positives

Owner being removed may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Owner removed from unfamiliar users should be
investigated. If known behavior is causing false positives, it
can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

