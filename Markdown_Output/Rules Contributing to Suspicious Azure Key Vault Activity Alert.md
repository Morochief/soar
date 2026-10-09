Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure Key
Vault Activity Alert

The following rules are used to identify suspicious Azure Key Vault activity. Any one or more of
these will trigger the Suspicious Azure Key Vault Activity Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Azure Keyvault Key
Modified or Deleted

Identifies when a Keyvault Key is modified or deleted in Azure.

Description

More details

Rule ID

azure_60

Query

{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/KEYS
/UPDATE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/CREATE', 'MICRO
SOFT.KEYVAULT/VAULTS/KEYS/CREATE/ACTION', 'MICROSOFT.KEYVAULT/VA
ULTS/KEYS/IMPORT/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/RECOVE
R/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/RESTORE/ACTION', 'MIC
ROSOFT.KEYVAULT/VAULTS/KEYS/DELETE', 'MICROSOFT.KEYVAULT/VAULTS/
KEYS/BACKUP/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/PURGE/ACTIO
N']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,80eeab92-0979-4152-942d-96749e11df40

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0006 , T1555.006 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 

Severity

Title

Description

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Mat
urity

Creati
on
Date

test 2021/0

8/16

Risk
Level

medi
um

False Positives

Key being modified or deleted may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Key modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Azure Key Vault
Modified or Deleted

Identifies when a key vault is modified or deleted.

More details

Rule ID

azure_69

Query

{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/WRIT
E', 'MICROSOFT.KEYVAULT/VAULTS/DELETE', 'MICROSOFT.KEYVAULT/VAUL
TS/DEPLOY/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/ACCESSPOLICIES/WRI
TE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,459a2970-bb84-4e6a-a32e-ff0fbd99448d

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0006 , T1555.006 

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

8/16

Risk
Level

medi
um

False Positives

Key Vault being modified or deleted may be performed by a system
administrator.

Title

Description

Mat
urit
y

Creati
on
Date

Risk
Level

False Positives

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Key Vault modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Azure Keyvault Secrets
Modified or Deleted

Identifies when secrets are modified or deleted in Azure.

More details

Rule ID

azure_87

Query

{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/SECR
ETS/WRITE', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/DELETE', 'MICROSO
FT.KEYVAULT/VAULTS/SECRETS/BACKUP/ACTION', 'MICROSOFT.KEYVAULT/V
AULTS/SECRETS/PURGE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/
UPDATE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/RECOVER/ACTIO
N', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/RESTORE/ACTION', 'MICROSO
FT.KEYVAULT/VAULTS/SECRETS/SETSECRET/ACTION']}, 'condition': 'se
lection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,b831353c-1971-477b-abb6-2828edc3bca1

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0006 , T1555.006 

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
urity

Creati
on
Date

test 2021/0

8/16

Risk
Level

medi
um

False Positives

Secrets being modified or deleted may be performed by a system
administrator.

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment.

Secrets modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

