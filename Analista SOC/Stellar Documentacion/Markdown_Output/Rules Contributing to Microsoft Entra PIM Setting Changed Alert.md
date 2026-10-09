Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra PIM
Setting Changed Alert

The following rules are used to identify suspicious Microsoft Entra PIM setting changed. Any one
or more of these will trigger the Microsoft Entra PIM Setting Changed Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Changes to PIM
Settings

Detects when changes are made to PIM roles

Description

More details

Rule ID

azure_41

Query

{'selection': {'properties_message': 'Update role setting in PIM'
}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,db6c06c4-bf3b-421c-aa88-15672b88c743

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0004 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-operations-
privileged-identity-management#azure-ad-roles-assignment 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Title

Additional Information

Maturity

experiment
al

Creation
Date

Risk
Level

2022/08/09

high

Description

False Positives

Legit administrative PIM setting configuration
changes

PIM Alert Setting
Changes to Disabled

Detects when PIM alerts are set to disabled.

More details

Rule ID

azure_43

Query

{'selection': {'properties_message': 'Disable PIM Alert'}, 'condi
tion': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,aeaef14c-e5bf-4690-a9c8-835caad458bd

Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures

TA0004 , T1078 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-operations-
privileged-identity-management#azure-ad-roles-assignment 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
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

2022/08/09

high

False Positives

Administrator disabling PIM alerts as an active
choice.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

