Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Application
Permission Changes Alert

The following rules are used to identify suspicious Microsoft Entra application permission
changes. Any one or more of these will trigger the Microsoft Entra Application Permission
Changes Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

App Granted Privileged
Delegated or App
Permissions

Detects when administrator grants either application permissions (app roles) or highly privileged
delegated permissions

More details

Rule ID

azure_21

Query

{'selection': {'properties_message': 'Add app role assignment
 to service principal'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,5aecf3d5-f8a0-48e7-99be-3a759df7358f

Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#application-granted-highly-privileged-permissions 

Severity

75

Suppression Logic Based On

azure ad.initiatedBy.user.id

Title

Description

_

y

azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

experiment
al

Creation
Date

Risk
Level

2022/07/28 high

False Positives

When the permission is legitimately needed for
the app

App Role Added

Detects when an app is assigned Microsoft Entra roles, such as global administrator, or
Microsoft Entra RBAC roles, such as subscription owner.

More details

Rule ID

azure_24

Query

{'selection': {'properties_message': ['Add member to role', '
Add eligible member to role', 'Add scoped member to role']},
'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,b04934b2-0a68-4845-8a19-bdfed3a68a7a

Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#service-principal-assigned-to-a-role 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

Creation
Date

Risk
Level

experiment
al

2022/07/19 medium

False Positives

When the permission is legitimately needed for
the app

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

