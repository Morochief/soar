Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure Network
Activity Alert

The following rules are used to identify suspicious Azure network activity. Any one or more of
these will trigger the Suspicious Azure Network Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.

Title

Description

Azure VPN Connection
Modified or Deleted

Identifies when a VPN connection is modified or deleted.

More details

Rule ID

azure_49

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/VPNGATEWAYS/
VPNCONNECTIONS/WRITE', 'MICROSOFT.NETWORK/VPNGATEWAYS/VPNCONNECT
IONS/DELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,61171ffc-d79c-4ae5-8e10-9323dba19cd3

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

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

VPN Connection being modified or deleted may be performed by a
system administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your environment.

VPN Connection modified or deleted from unfamiliar users should
be investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Azure Point-to-site VPN
Modified or Deleted

Identifies when a Point-to-site VPN is Modified or Deleted.

More details

Rule ID

azure_77

Query

{'selection': {'operationName': ['MICROSOFT.NETWORK/P2SVPNGATEWA
YS/WRITE', 'MICROSOFT.NETWORK/P2SVPNGATEWAYS/DELETE', 'MICROSOFT
.NETWORK/P2SVPNGATEWAYS/RESET/ACTION', 'MICROSOFT.NETWORK/P2SVPN
GATEWAYS/GENERATEVPNPROFILE/ACTION', 'MICROSOFT.NETWORK/P2SVPNGA
TEWAYS/DISCONNECTP2SVPNCONNECTIONS/ACTION', 'MICROSOFT.NETWORK/P
2SVPNGATEWAYS/PROVIDERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WR
ITE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,d9557b75-267b-4b43-922f-a775e2d1f792

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

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

Title

Description

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

Point-to-site VPN being modified or deleted may be performed by a
system administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your environment.

Point-to-site VPN modified or deleted from unfamiliar users should
be investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Azure Virtual Network
Modified or Deleted

Identifies when a Virtual Network is modified or deleted in Azure.

More details

Rule ID

azure_86

Query

{'selection': {'operationName|startswith': ['MICROSOFT.NETWORK/V
IRTUALNETWORKGATEWAYS/', 'MICROSOFT.NETWORK/VIRTUALNETWORKS/'],
'operationName|endswith': ['/WRITE', '/DELETE']}, 'condition': '
selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,bcfcc962-0e4a-4fd9-84bb-a833e672df3f

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

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

test 2021/0

8/08

Risk
Level

medi
um

False Positives

Virtual Network being modified or deleted may be performed by a
system administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your environment.

Virtual Network modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

