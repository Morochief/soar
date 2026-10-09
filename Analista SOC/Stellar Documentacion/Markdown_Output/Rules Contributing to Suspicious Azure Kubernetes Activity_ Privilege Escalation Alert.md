Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Kubernetes Activity: Privilege Escalation Alert

The following rules are used to identify suspicious Azure Kubernetes activity usually in the
privilege escalation stage. Any one or more of these will trigger the Suspicious Azure Kubernetes
Activity: Privilege Escalation Alert. Details for each rule can be viewed by clicking the More
Details link in the description.

Title

Description

Azure Kubernetes Sensitive Role
Access

Identifies when ClusterRoles/Roles are being modified or deleted.

More details

Rule ID

azure_76

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CO
NNECTEDCLUSTERS/RBAC.AUTHORIZATION.K8S.IO/ROLES/WRITE', '
MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATION
.K8S.IO/ROLES/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLU
STERS/RBAC.AUTHORIZATION.K8S.IO/ROLES/BIND/ACTION', 'MICR
OSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATION.K8S
.IO/ROLES/ESCALATE/ACTION', 'MICROSOFT.KUBERNETES/CONNECT
EDCLUSTERS/RBAC.AUTHORIZATION.K8S.IO/CLUSTERROLES/WRITE',
 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATI
ON.K8S.IO/CLUSTERROLES/DELETE', 'MICROSOFT.KUBERNETES/CON
NECTEDCLUSTERS/RBAC.AUTHORIZATION.K8S.IO/CLUSTERROLES/BIN
D/ACTION', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.A
UTHORIZATION.K8S.IO/CLUSTERROLES/ESCALATE/ACTION']}, 'con
dition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,818fee0c-e0ec-4e45-824e-83e4817b0887

Author: Austin Songer @austinsonger

Title

Description

Tactics, Techniques, and Procedures

TA0004 , T1078 

References

Azure Kubernetes
RoleBinding/ClusterRoleBinding
Modified and Deleted

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/


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

Creat
ion
Date

Risk
Leve
l

test 2021/
08/07

medi
um

False Positives

ClusterRoles/Roles being modified and deleted may be
performed by a system administrator. Verify whether the
user identity, user agent, and/or hostname should be
making changes in your environment.

ClusterRoles/Roles modification from unfamiliar users
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Detects the creation or patching of potential malicious RoleBinding/ClusterRoleBinding.

More details

Rule ID

azure_79

Query

{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CO
NNECTEDCLUSTERS/RBAC.AUTHORIZATION.K8S.IO/CLUSTERROLEBIND
INGS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC
.AUTHORIZATION.K8S.IO/CLUSTERROLEBINDINGS/DELETE', 'MICRO
SOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATION.K8S.
IO/ROLEBINDINGS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCL
USTERS/RBAC.AUTHORIZATION.K8S.IO/ROLEBINDINGS/DELETE']},
'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,25cb259b-bbdc-4b87-98b7-90d7c72f8743

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0004 , T1078 

Title

Description

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-
provider-operations#microsoftkubernetes 

https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-
environments-with-updated-threat-matrix-for-kubernetes/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/


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

Creat
ion
Date

Risk
Leve
l

test 2021/
08/07

medi
um

False Positives

RoleBinding/ClusterRoleBinding being modified and
deleted may be performed by a system administrator.
Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.

RoleBinding/ClusterRoleBinding modification from
unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the
rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

