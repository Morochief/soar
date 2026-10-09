Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Kubernetes Activity: Credential Access Alert

The following rules are used to identify suspicious Azure Kubernetes activity usually in the
credential access stage. Any one or more of these will trigger the Suspicious Azure Kubernetes
Activity: Credential Access Alert. Details for each rule can be viewed by clicking the More Details
link in the description.

Title

Description

Azure Kubernetes Secret
or Config Object Access

Identifies when a Kubernetes account access a sensitive objects such as configmaps or secrets.

More details

Rule ID

azure_68

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECT
EDCLUSTERS/CONFIGMAPS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDC
LUSTERS/CONFIGMAPS/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLU
STERS/SECRETS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/
SECRETS/DELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,7ee0b4aa-d8d4-4088-b661-20efdf41a04c

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0006 , T1552.001 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/ 

Title

Description

https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-
4c2359654bf1 

https://attack.mitre.org/matrices/enterprise/cloud/ 

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

8/07

Risk
Leve
l

medi
um

False Positives

Sensitive objects may be accessed by a system administrator.
Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment. Sensitive objects
accessed from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

