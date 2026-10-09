Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Microsoft Entra
Service Principal Activity Alert

The following rules are used to identify suspicious Microsoft Entra service principal activity. Any
one or more of these will trigger the Suspicious Microsoft Entra Service Principal Activity Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

Azure Service
Principal Created

Identifies when a service principal is created in Azure.

Description

More details

Rule ID

azure_74

Query

{'selection': {'properties_message': 'Add service principal'}, 'con
dition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,0ddcff6d-d262-40b0-804b-80eb592de8e3

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1578 

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

Mat
urity

Creatio
n Date

Risk
Level

test 2021/0

9/02

mediu
m

False Positives

Service principal being created may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment.

Service principal created from unfamiliar users should be investigated.
If known behavior is causing false positives, it can be exempted from
the rule.

Azure Service
Principal Removed

Identifies when a service principal was removed in Azure.

More details

Rule ID

azure_75

Query

{'selection': {'properties_message': 'Remove service principal'}, '
condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,448fd1ea-2116-4c62-9cde-a92d120e0f08

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1578.003 

References

https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-audit-
activities#application-proxy 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Mat
urity

Creati
on
Date

test 2021/0

9/03

Risk
Level

mediu
m

False Positives

Service principal being removed may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment.

Service principal removed from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

