Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Kubernetes Activity: Impact Alert

The following rules are used to identify suspicious Azure Kubernetes activity usually in the impact
stage. Any one or more of these will trigger the Suspicious Azure Kubernetes Activity: Impact
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Title

Description

Azure Kubernetes Pods
Deleted

Identifies the deletion of Azure Kubernetes Pods.

More details

Rule ID

azure_46

Query

{'selection': {'operationName': 'MICROSOFT.KUBERNETES/CONNECT
EDCLUSTERS/PODS/DELETE'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,b02f9591-12c3-4965-986a-88028629b2e1

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1485 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

https://github.com/elastic/detection-
rules/blob/065bf48a9987cd8bd826c098a30ce36e6868ee46/rules/integrations/azure/
impact_kubernetes_pod_deleted.toml 

Severity

50

Suppression Logic Based On

Title

Description

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

test 2021/
07/24

Risk
Leve
l

medi
um

False Positives

Pods may be deleted by a system administrator. Verify whether
the user identity, user agent, and/or hostname should be
making changes in your environment.

Pods deletions from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Azure Kubernetes Cluster
Created or Deleted

Detects when a Azure Kubernetes Cluster is created or deleted.

More details

Rule ID

azure_54

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNEC
TEDCLUSTERS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/D
ELETE']}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,9541f321-7cba-4b43-80fc-fbd1fb922808

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1485 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

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

Title

Description

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

Kubernetes cluster being created or deleted may be performed
by a system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment.

Kubernetes cluster created or deleted from unfamiliar users
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Azure Kubernetes Service
Account Modified or Deleted

Identifies when a service account is modified or deleted.

More details

Rule ID

azure_59

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNEC
TEDCLUSTERS/SERVICEACCOUNTS/WRITE', 'MICROSOFT.KUBERNETES/CON
NECTEDCLUSTERS/SERVICEACCOUNTS/DELETE', 'MICROSOFT.KUBERNETES
/CONNECTEDCLUSTERS/SERVICEACCOUNTS/IMPERSONATE/ACTION']}, 'co
ndition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,12d027c3-b48c-4d9d-8bb6-a732200034b2

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1531 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/ 

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

Risk
Leve
l

test 2021/
08/07

medi
um

False Positives

Service account being modified or deleted may be performed by
a system administrator. Verify whether the user identity, user

Title

Description

Mat
urit
y

Creati
on
Date

Risk
Leve
l

False Positives

agent, and/or hostname should be making changes in your
environment.

Service account modified or deleted from unfamiliar users
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Azure Kubernetes Network
Policy Change

Identifies when a Azure Kubernetes network policy is modified or deleted.

More details

Rule ID

azure_61

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNEC
TEDCLUSTERS/NETWORKING.K8S.IO/NETWORKPOLICIES/WRITE', 'MICROS
OFT.KUBERNETES/CONNECTEDCLUSTERS/NETWORKING.K8S.IO/NETWORKPOL
ICIES/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/EXTENS
IONS/NETWORKPOLICIES/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDC
LUSTERS/EXTENSIONS/NETWORKPOLICIES/DELETE']}, 'condition': 's
election'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,08d6ac24-c927-4469-b3b7-2e422d6e3c43

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0040 , T1498 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/ 

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

test 2021/
08/07

Risk
Leve
l

medi
um

False Positives

Network Policy being modified and deleted may be performed
by a system administrator. Verify whether the user identity, user

Title

Description

Mat
urit
y

Creati
on
Date

Risk
Leve
l

False Positives

agent, and/or hostname should be making changes in your
environment.

Network Policy being modified and deleted from unfamiliar
users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

