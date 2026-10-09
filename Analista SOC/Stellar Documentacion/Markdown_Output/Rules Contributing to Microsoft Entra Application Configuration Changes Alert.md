Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Application
Configuration Changes Alert

The following rules are used to identify suspicious Microsoft Entra application configuration
changes. Any one or more of these will trigger the Microsoft Entra Application Configuration
Changes Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

Application AppID Uri
Configuration Changes

Detects when a configuration change is made to an application's AppID URI.

More details

Rule ID

azure_16

Query

{'selection': {'properties_message': ['Update Application', 'Up
date Service principal']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,1b45b0d1-773f-4f23-aedc-814b759563b1

Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'

Tactics, Techniques, and Procedures

TA0003 , T1078.004 , TA0006 , T1552 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#appid-uri-added-modified-or-removed 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId

Title

Description

stellar.rule_id

Additional Information

Maturi
ty

Creatio
n Date

Risk
Level

experi
mental

2022/0
6/02

high

False Positives

When an administrator is making legitimate AppID URI
configuration changes to an application. This should be a
planned event.

Added Credentials to
Existing Application

Detects when a new credential is added to an existing application. Any additional credentials added
outside of expected processes could be a malicious actor using those credentials.

More details

Rule ID

azure_18

Query

{'selection': {'properties_message': 'Update Service principal/
Update Application'}, 'selection2': {'properties_message|contai
ns|all': ['Update Application', 'Certificates and secrets manag
ement']}, 'condition': 'selection or selection2'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,cbb67ecc-fb70-4467-9350-c910bdf7c628

Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'

Tactics, Techniques, and Procedures

TA0003 , T1098.001 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#application-credentials 

Severity

75

Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information

Maturity Creation

Date

experime
ntal

2022/05/2
6

Risk
Level

high

False Positives

When credentials are added/removed as part of the
normal working hours/workflows

Added Owner to
Application

Detects when a new owner is added to an application. This gives that account privileges to make
modifications and configuration changes to the application.

More details

Rule ID

azure_23

Query

Title

Description

{'selection': {'properties_message': 'Add owner to application'
}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,74298991-9fc4-460e-a92e-511aa60baec1

Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'

Tactics, Techniques, and Procedures

TA0003 , T1078.004 

References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#new-owner 

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

2022/06/02 medium

False Positives

When a new application owner is added by an
administrator

Azure Application
Credential Modified

Identifies when an application credential is modified.

More details

Rule ID

azure_51

Query

{'selection': {'properties_message': 'Update application -
 Certificates and secrets management'}, 'condition': 'selection
'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,cdeef967-f9a1-4375-90ee-6978c5f23974

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0003 , T1098 

References

https://www.cloud-architekt.net/auditing-of-msi-and-service-principals/ 

Severity

50

Title

Description

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

9/02

Risk
Level

medi
um

False Positives

Application credential addition may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Application credential added from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

