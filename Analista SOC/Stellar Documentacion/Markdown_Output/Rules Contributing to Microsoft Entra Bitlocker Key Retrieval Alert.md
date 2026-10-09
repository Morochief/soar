✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Microsoft Entra Bitlocker
Key Retrieval Alert
The following rules are used to identify suspicious Microsoft Entra Bitlocker key retrieval activity.
Any one or more of these will trigger the Microsoft Entra Bitlocker Key Retrieval Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Title Description
BitLocker Key Monitor and alert for BitLocker key retrieval.
Retrieval
More details
Rule ID
azure_25
Query
{'selection': {'Category': 'KeyManagement', 'OperationName': 'Read Bit
Locker key'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,a0413867-daf3-43dd-9245-734b3a787942
Author: Michael Epping, '@mepples21'
Tactics, Techniques, and Procedures
TA0006 , T1555 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-operations-
devices#bitlocker-key-retrieval 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Title Description
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2022/06/28    | medium     |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        