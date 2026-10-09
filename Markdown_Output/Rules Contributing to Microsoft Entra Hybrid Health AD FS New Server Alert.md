Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Microsoft Entra Hybrid
Health AD FS New Server Alert

The following rules are used to identify a new hybrid health AD FS server. Any one or more of
these will trigger the Microsoft Entra Hybrid Health AD FS New Server Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Description

Azure Active Directory Hybrid
Health AD FS New Server

This detection uses Azure Activity Log (Administrative category) to identify the creation or
update of a server instance in a Microsoft Entra Hybrid health AD FS service. A threat actor can
create a new Health AD FS service and create a fake server instance to spoof AD FS signing
logs. There is no need to compromise an on-prem AD FS server. This can be done
programmatically via HTTP requests to Azure.

More details

Rule ID

azure_55

Query

{'selection': {'CategoryValue': 'Administrative', 'ResourceI
d|contains': 'AdFederationService', 'OperationNameValue': 'M
icrosoft.ADHybridHealthService/services/servicemembers/actio
n'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,288a39fc-4914-4831-9ada-270e9dc12cb4

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC

Tactics, Techniques, and Procedures

TA0007 , T1087 

References

https://o365blog.com/post/hybridhealthagent/ 

Severity

Title

Description

50

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

Legitimate AD FS servers added to an AAD Health AD
FS service instance

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

