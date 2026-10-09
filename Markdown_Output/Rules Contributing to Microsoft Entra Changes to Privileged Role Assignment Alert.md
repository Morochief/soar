Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Changes
to Privileged Role Assignment Alert

The following rules are used to identify suspicious Microsoft Entra changes to privileged role
assignment. Any one or more of these will trigger the Microsoft Entra Changes to Privileged Role
Assignment Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

Bulk Deletion Changes to
Privileged Account
Permissions

Detects when a user is removed from a privileged role. Bulk changes should be investigated.

More details

Rule ID

azure_39

Query

{'selection': {'properties_message': ['Remove eligible membe
r (permanent)', 'Remove eligible member (eligible)']}, 'cond
ition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,102e11e3-2db5-4c9e-bc26-357d42585d21

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 

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

Maturity Creation

Date

Risk
Level

experime
ntal

2022/08/05 high

False Positives

Legitimate administrator actions of removing
members from a role

PIM Approvals and Deny
Elevation

Detects when a PIM elevation is approved or denied. Outside of normal operations should be
investigated.

More details

Rule ID

azure_40

Query

{'selection': {'properties_message': 'Request Approved/Denie
d'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,039a7469-0296-4450-84c0-f6966b16dc6d

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/08/09

high

Actual admin using PIM.

User Added to Privilege Role

Detects when a user is added to a privileged role.

More details

Rule ID

azure_42

Query

{'selection': {'properties_message': ['Add eligible member (
permanent)', 'Add eligible member (eligible)']}, 'condition'
: 'selection'}

Title

Description

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,49a268a4-72f4-4e38-8a7b-885be690c5b5

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity Creation

Date

Risk
Level

experime
ntal

2022/08/06 high

False Positives

Legitimate administrator actions of adding
members from a role

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

