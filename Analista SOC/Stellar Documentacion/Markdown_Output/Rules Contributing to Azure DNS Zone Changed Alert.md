Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Azure DNS Zone Changed
Alert

The following rules are used to identify events when an Azure DNS zone is changed. Any one or
more of these will trigger the Azure DNS Zone Changed Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Azure DNS Zone
Modified or Deleted

Identifies when DNS zone is modified or deleted.

Description

More details

Rule ID

azure_73

Query

{'selection': {'operationName|startswith': 'MICROSOFT.NETWORK/DNSZ
ONES', 'operationName|endswith': ['/WRITE', '/DELETE']}, 'conditio
n': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,af6925b0-8826-47f1-9324-337507a0babd

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0011 , T1071.004 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

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

test 2021/0

8/08

Risk
Level

medi
um

False Positives

DNS zone modified and deleted may be performed by a system
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.

DNS zone modification from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from
the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

