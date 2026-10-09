Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Azure Security
Configuration Changed Alert

The following rules are used to identify events when an Azure security configuration is changed.
Any one or more of these will trigger the Azure Security Configuration Changed Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Azure Application Security
Group Modified or Deleted

Identifies when a application security group is modified or deleted.

More details

Rule ID

azure_64

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/APPLICAT
IONSECURITYGROUPS/WRITE', 'MICROSOFT.NETWORK/APPLICATIONSECU
RITYGROUPS/DELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,835747f1-9329-40b5-9cc3-97d465754ce6

Author: Austin Songer

Tactics, Techniques, and Procedures

TA0005 , T1562 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName

Title

Description

stellar.rule_id

Additional Information

Mat
urit
y

Creati
on
Date

Risk
Leve
l

test 2021/
08/16

medi
um

False Positives

Application security group being modified or deleted may be
performed by a system administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Application security group modified or deleted from unfamiliar
users should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.

Azure Suppression Rule
Created

Identifies when a suppression rule is created in Azure. Adversary's could attempt this to evade
detection.

More details

Rule ID

azure_66

Query

{'selection': {'operationName': 'MICROSOFT.SECURITY/ALERTSSU
PPRESSIONRULES/WRITE'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,92cc3e5d-eb57-419d-8c16-5c63f325a401

Author: Austin Songer

Tactics, Techniques, and Procedures

TA0005 , T1562 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Mat
urit
y

Creati
on
Date

test 2021/0

8/16

Risk
Leve
l

medi
um

False Positives

Suppression Rule being created may be performed by a
system administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Suppression Rule created from unfamiliar users should be
investigated. If known behavior is causing false positives, it
can be exempted from the rule.

Title

Description

Azure Network Security
Configuration Modified or
Deleted

Identifies when a network security configuration is modified or deleted.

More details

Rule ID

azure_84

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/NETWORKS
ECURITYGROUPS/WRITE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROU
PS/DELETE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURIT
YRULES/WRITE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECU
RITYRULES/DELETE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/
JOIN/ACTION', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/PROVI
DERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE']}, 'condit
ion': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,d22b4df4-5a67-4859-a578-8c9a0b5af9df

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Mat
urit
y

Creati
on
Date

Risk
Leve
l

test 2021/
08/08

medi
um

False Positives

Network Security Configuration being modified or deleted may
be performed by a system administrator. Verify whether the
user identity, user agent, and/or hostname should be making
changes in your environment.

Network Security Configuration modified or deleted from
unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

