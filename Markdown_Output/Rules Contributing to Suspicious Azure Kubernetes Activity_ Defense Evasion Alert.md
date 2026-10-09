Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Kubernetes Activity: Defense Evasion Alert

The following rules are used to identify suspicious Azure Kubernetes activity usually in the
defense evasion stage. Any one or more of these will trigger the Suspicious Azure Kubernetes
Activity: Defense Evasion Alert. Details for each rule can be viewed by clicking the More Details
link in the description.

Title

Description

Azure Kubernetes
Events Deleted

Detects when Events are deleted in Azure Kubernetes. An adversary may delete events in Azure
Kubernetes in an attempt to evade detection.

More details

Rule ID

azure_58

Query

{'selection': {'operationName': 'MICROSOFT.KUBERNETES/CONNECTEDCLUS
TERS/EVENTS.K8S.IO/EVENTS/DELETE'}, 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,225d8b09-e714-479c-a0e4-55e6f29adf35

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0005 , T1562.001 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

https://github.com/elastic/detection-
rules/blob/da3852b681cf1a33898b1535892eab1f3a76177a/rules/integrations/azure/defense_
evasion_kubernetes_events_deleted.toml 

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

7/24

Risk
Level

medi
um

False Positives

Event deletions may be done by a system or network administrator.
Verify whether the username, hostname, and/or resource name should
be making changes in your environment. Events deletions from
unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

