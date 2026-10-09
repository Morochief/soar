Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Hybrid
Health AD FS Service Deleted Alert

The following rules are used to identify events when a hybrid health AD FS server is deleted. Any
one or more of these will trigger the Microsoft Entra Hybrid Health AD FS Service Deleted Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

Description

Azure Active Directory Hybrid
Health AD FS Service Delete

This detection uses Azure Activity Log (Administrative category) to identify the deletion of a
Microsoft Entra Hybrid health AD FS service instance in a tenant. A threat actor can create a
new Health AD FS service and create a fake server to spoof AD FS signing logs. The health
AD FS service can then be deleted after it is not longer needed via HTTP requests to Azure.

More details

Rule ID

azure_72

Query

{'selection': {'CategoryValue': 'Administrative', 'ResourceI
d|contains': 'AdFederationService', 'OperationNameValue': 'M
icrosoft.ADHybridHealthService/services/delete'}, 'condition
': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,48739819-8230-4ee3-a8ea-e0289d1fb0ff

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC

Tactics, Techniques, and Procedures

TA0005 , T1578.003 

References

https://o365blog.com/post/hybridhealthagent/ 

Severity

50

Title

Description

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Maturi
ty

Creation
Date

Risk
Level

test

2021/08/2
6

medium

False Positives

Legitimate AAD Health AD FS service instances
being deleted in a tenant

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

