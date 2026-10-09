Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Azure
Kubernetes Activity: Persistence Alert

The following rules are used to identify suspicious Azure Kubernetes activity usually in the
persistence stage. Any one or more of these will trigger the Suspicious Azure Kubernetes
Activity: Persistence Alert. Details for each rule can be viewed by clicking the More Details link
in the description.

Title

Azure
Kubernetes
CronJob

Description

Identifies when a Azure Kubernetes CronJob runs in Azure Cloud. Kubernetes Job is a controller that
creates one or more pods and ensures that a specified number of them successfully terminate. Kubernetes
Job can be used to run containers that perform finite tasks for batch jobs. Kubernetes CronJob is used to
schedule Jobs. An Adversary may use Kubernetes CronJob for scheduling execution of malicious code that
would run as a container in the cluster.

More details

Rule ID

azure_62

Query

{'selection': {'operationName|startswith': ['MICROSOFT.KUBERNETES/CON
NECTEDCLUSTERS/BATCH', 'MICROSOFT.CONTAINERSERVICE/MANAGEDCLUSTERS/BA
TCH'], 'operationName|endswith': ['/CRONJOBS/WRITE', '/JOBS/WRITE']},
 'condition': 'selection'}

Log Source

Stellar Cyber Microsoft Entra Events configured.

Rule Source

SigmaHQ,1c71e254-6655-42c1-b2d6-5e4718d7fc0a

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0003 , T1053.007 

References

https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 

Title

Description

https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/ 

https://kubernetes.io/docs/concepts/workloads/controllers/job/ 

https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/ 

Severity

50

Suppression Logic Based On

azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2021/11/22 medium

False Positives

Azure Kubernetes CronJob/Job may be done by a system
administrator.

If known behavior is causing false positives, it can be exempted
from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

