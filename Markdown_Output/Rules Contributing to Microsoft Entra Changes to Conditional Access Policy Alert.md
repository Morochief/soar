Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Changes
to Conditional Access Policy Alert

The following rules are used to identify suspicious Microsoft Entra changes to conditional access
policy. Any one or more of these will trigger the Microsoft Entra Changes to Conditional Access
Policy Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

New CA Policy by Non-
Approved Actor

Monitor and alert on conditional access changes.

More details

Rule ID

azure_28

Query

{'selection': {'properties_message': 'Add conditional access
 policy'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,0922467f-db53-4348-b7bf-dee8d0d348c6

Author: Corissa Koopmans, '@corissalea'

Tactics, Techniques, and Procedures

TA0005 , T1556 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId

Title

Description

stellar.rule_id

Additional Information

Maturit
y

Creatio
n Date

Risk
Level

experi
mental

2022/07
/18

mediu
m

False Positives

Misconfigured role permissions

Verify whether the user identity, user agent, and/or
hostname should be making changes in your
environment.

CA Policy Updated by Non-
Approved Actor

Monitor and alert on conditional access changes. Is Initiated by (actor) approved to make
changes? Review Modified Properties and compare "old" vs "new" value.

More details

Rule ID

azure_29

Query

{'keywords': {'properties_message': 'Update conditional acce
ss policy'}, 'condition': 'keywords'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,50a3c7aa-ec29-44a4-92c1-fce229eef6fc

Author: Corissa Koopmans, '@corissalea'

Tactics, Techniques, and Procedures

TA0005 , T1548 , T1556 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturit
y

Creatio
n Date

Risk
Level

experi
mental

2022/07
/19

mediu
m

False Positives

Misconfigured role permissions

Verify whether the user identity, user agent, and/or
hostname should be making changes in your
environment.

User Added to Group with CA
Policy Modification Access

Monitor and alert on group membership additions of groups that have CA policy modification
access

More details

Rule ID

azure_30

Title

Description

Query

{'selection': {'properties_message': 'Add member from group'
}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,91c95675-1f27-46d0-bead-d1ae96b97cd3

Author: Mark Morowczynski '@markmorow', Thomas Detzner '@tdetzner'

Tactics, Techniques, and Procedures

TA0005 , T1548 , T1556 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity

experimenta
l

Creation
Date

Risk
Level

2022/08/04

medium

False Positives

User removed from the group is
approved

CA Policy Removed by Non-
Approved Actor

Monitor and alert on conditional access changes where non approved actor removed CA
Policy.

More details

Rule ID

azure_31

Query

{'selection': {'properties_message': 'Delete conditional acc
ess policy'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,26e7c5e2-6545-481e-b7e6-050143459635

Author: Corissa Koopmans, '@corissalea'

Tactics, Techniques, and Procedures

TA0005 , T1548 , T1556 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 

Title

Description

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturit
y

Creatio
n Date

Risk
Level

experi
mental

2022/07
/19

mediu
m

False Positives

Misconfigured role permissions

Verify whether the user identity, user agent, and/or
hostname should be making changes in your
environment.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

