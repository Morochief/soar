Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Microsoft Entra
Device Activity Alert

The following rules are used to identify suspicious Microsoft Entra device activity. Any one or
more of these will trigger the Suspicious Microsoft Entra Device Activity Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Description

Azure Device No Longer
Managed or Compliant

Identifies when a device in Azure is no longer managed or compliant

More details

Rule ID

azure_47

Query

{'selection': {'properties_message': ['Device no longer compli
ant', 'Device no longer managed']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,542b9912-c01f-4e3f-89a8-014c48cdca7d

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

References

https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#core-directory 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Title

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2021/09/03 medium

Description

False Positives

Administrator may have forgotten to review the
device.

Azure Device or
Configuration Deleted

Identifies when a device or device configuration in Azure is deleted.

More details

Rule ID

azure_70

Query

{'selection': {'properties_message': ['Delete device', 'Delete
 device configuration']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,46530378-f9db-4af9-a9e5-889c177d3881

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

References

https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#core-directory 

Severity

50

Suppression Logic Based On

azure_ad.initiatedBy.user.id
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
Leve
l

medi
um

False Positives

Device or device configuration being modified or deleted may be
performed by a system administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Device or device configuration modified or deleted from unfamiliar
users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

