Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Deployment Activity Alert

The following rules are used to identify suspicious Azure deployment activity. Any one or more of
these will trigger the Suspicious Azure Deployment Activity Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

Number Of Resource
Creation Or Deployment
Activities

Number of VM creations or deployment activities occur in Azure via Azure Activity Log.

More details

Rule ID

azure_48

Query

{'selection': {'OperationNameValue': ['Microsoft.Compute/vir
tualMachines/write', 'Microsoft.Resources/deployments/write'
]}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,d2d901db-7a75-45a1-bc39-0cbf00812192

Author: sawwinnnaung

Tactics, Techniques, and Procedures

TA0040 , T1496 

References

https://github.com/Azure/Azure-
Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActi
vity/Creating_Anomalous_Number_Of_Resources_detection.yaml 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId

Title

Description

azure_activity_log.operationName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2020/05/07

medium

Valid change

Azure Container Registry
Modified or Deleted

Detects when a Container Registry is created, updated, or deleted.

More details

Rule ID

azure_65

Query

{'selection': {'operationName': ['MICROSOFT.CONTAINERREGISTR
Y/REGISTRIES/WRITE', 'MICROSOFT.CONTAINERREGISTRY/REGISTRIES
/DELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,93e0ef48-37c8-49ed-a02c-038aab23628e

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1485 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/ 

https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-
4c2359654bf1 

https://attack.mitre.org/matrices/enterprise/cloud/ 

Severity

25

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
08/07

low

False Positives

Container Registry being created, updated, or deleted may be
performed by a system administrator. Verify whether the user
identity, user agent, and/or hostname should be making
changes in your environment.

Container Registry created, updated, or deleted from unfamiliar
users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

