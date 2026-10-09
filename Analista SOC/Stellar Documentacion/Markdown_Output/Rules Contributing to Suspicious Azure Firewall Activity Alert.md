Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure Firewall
Activity Alert

The following rules are used to identify suspicious Azure firewall activity. Any one or more of
these will trigger the Suspicious Azure Firewall Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.

Title

Description

Azure Firewall Rule
Configuration Modified or
Deleted

Identifies when a Firewall Rule Configuration is Modified or Deleted.

More details

Rule ID

azure_50

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/FIREWALLP
OLICIES/RULECOLLECTIONGROUPS/WRITE', 'MICROSOFT.NETWORK/FIREW
ALLPOLICIES/RULECOLLECTIONGROUPS/DELETE', 'MICROSOFT.NETWORK/
FIREWALLPOLICIES/RULEGROUPS/WRITE', 'MICROSOFT.NETWORK/FIREWA
LLPOLICIES/RULEGROUPS/DELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,2a7d64cf-81fa-4daf-ab1b-ab80b789c067

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562.007 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

Severity

50

Suppression Logic Based On

Title

Description

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Azure Firewall Rule
Collection Modified or
Deleted

Mat
urit
y

Creati
on
Date

test 2021/
08/08

Risk
Leve
l

medi
um

False Positives

Firewall Rule Configuration being modified or deleted may be
performed by a system administrator. Verify whether the user
identity, user agent, and/or hostname should be making
changes in your environment.

Firewall Rule Configuration modified or deleted from unfamiliar
users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Identifies when Rule Collections (Application, NAT, and Network) is being modified or deleted.

More details

Rule ID

azure_63

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/AZUREFIRE
WALLS/APPLICATIONRULECOLLECTIONS/WRITE', 'MICROSOFT.NETWORK/A
ZUREFIREWALLS/APPLICATIONRULECOLLECTIONS/DELETE', 'MICROSOFT.
NETWORK/AZUREFIREWALLS/NATRULECOLLECTIONS/WRITE', 'MICROSOFT.
NETWORK/AZUREFIREWALLS/NATRULECOLLECTIONS/DELETE', 'MICROSOFT
.NETWORK/AZUREFIREWALLS/NETWORKRULECOLLECTIONS/WRITE', 'MICRO
SOFT.NETWORK/AZUREFIREWALLS/NETWORKRULECOLLECTIONS/DELETE']},
 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,025c9fe7-db72-49f9-af0d-31341dd7dd57

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562.007 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

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

Rule Collections (Application, NAT, and Network) being modified
or deleted may be performed by a system administrator. Verify

Title

Description

Mat
urit
y

Creati
on
Date

Risk
Leve
l

False Positives

whether the user identity, user agent, and/or hostname should
be making changes in your environment.

Rule Collections (Application, NAT, and Network) modified or
deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

Azure Firewall Modified or
Deleted

Identifies when a firewall is created, modified, or deleted.

More details

Rule ID

azure_67

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/AZUREFIRE
WALLS/WRITE', 'MICROSOFT.NETWORK/AZUREFIREWALLS/DELETE']}, 'c
ondition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,512cf937-ea9b-4332-939c-4c2c94baadcd

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562.007 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

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

Firewall being modified or deleted may be performed by a
system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment.

Firewall modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Azure Network Firewall
Policy Modified or Deleted

Identifies when a Firewall Policy is Modified or Deleted.

More details

Rule ID

Title

Description

azure_85

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/FIREWALLP
OLICIES/WRITE', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/JOIN/ACTI
ON', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/CERTIFICATES/ACTION'
, 'MICROSOFT.NETWORK/FIREWALLPOLICIES/DELETE']}, 'condition':
 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,83c17918-746e-4bd9-920b-8e098bf88c23

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562.007 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

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
09/02

medi
um

False Positives

Firewall Policy being modified or deleted may be performed by a
system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment.

Firewall Policy modified or deleted from unfamiliar users should
be investigated. If known behavior is causing false positives, it
can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

