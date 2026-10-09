✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Potentially Malicious AWS
Activity Alert
The following rules are used to identify suspicious activity within AWS logs. Any one or more of
these will trigger a Potentially Malicious AWS Activity Alert. Details for each rule can be viewed
by clicking the More Details link in the description.
Title Description
SES Identity Has Been Deleted Detects an instance of an SES identity being deleted via the "DeleteIdentity" event. This
may be an indicator of an adversary removing the account that carried out suspicious or
malicious activities
More details
Rule ID
aws_3
Query
{'selection': {'eventSource': 'ses.amazonaws.com', 'event
Name': 'DeleteIdentity'}, 'condition': 'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,20f754db-d025-4a8f-9d74-e0037e999a9a
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/

Severity
50

Title Description
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/13 medium
Unknown
AWS GuardDuty Important Change Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts
against malicious IPs.
More details
Rule ID
aws_4
Query
{'selection_source': {'eventSource': 'guardduty.amazonaws
.com', 'eventName': 'CreateIPSet'}, 'condition': 'selecti
on_source'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,6e61ee20-ce00-4f8d-8aee-bedd8216f7e3
Author: faloker
Tactics, Techniques, and Procedures
TA0005 , T1562.001 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0
524c817f2c5b181/pacu/modules/guardduty__whitelist_ip/main.py#L9 
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2020/02/11 high
Valid change in the GuardDuty (e.g. to ignore
internal scanners)
AWS Glue Development Endpoint Detects possible suspicious glue development endpoint activity.
Activity
More details
Rule ID
aws_5

Title Description
Query
{'selection': {'eventSource': 'glue.amazonaws.com', 'even
tName': ['CreateDevEndpoint', 'DeleteDevEndpoint', 'Updat
eDevEndpoint']}, 'condition': 'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,4990c2e3-f4b8-45e3-bc3c-30b14ff0ed26
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1078 
References
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/

https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDevEndpoint.html

Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Matu Creat Risk False Positives
rity ion Lev
Date el
exper 2021/ low
Glue Development Endpoint Activity may be performed by
iment 10/03 a system administrator. Verify whether the user identity,
al user agent, and/or hostname should be making changes
in your environment.
If known behavior is causing false positives, it can be
exempted from the rule.
AWS ECS Backdoor Task Detects when an Elastic Container Service (ECS) Task Definition has been modified and
Definition run. This can indicate an adversary adding a backdoor to establish persistence or
escalate privileges. This rule is based on examining events created upon execution of
Rhino Security Lab's Pacu in a lab environment.
More details
Rule ID
aws_7
Query
{'selection': {'eventSource': 'ecs.amazonaws.com', 'event
Name': ['DescribeTaskDefinition', 'RegisterTaskDefinition
', 'RunTask'], 'requestParameters_containerDefinitions_co
mmand|contains|all': ['169.254', '$AWS_CONTAINER_CREDENTI
ALS']}, 'condition': 'selection'}
Log Source

Title Description
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,b94bf91e-c2bf-4047-9c43-c6810f43baad
Author: Darin Smith
Tactics, Techniques, and Procedures
TA0003 , T1525 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0
524c817f2c5b181/pacu/modules/ecs__backdoor_task_def/main.py 
https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Register
TaskDefinition.html 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturit Creatio Risk False Positives
y n Date Level
experi 2022/06 mediu
Task Definition being modified to request credentials
mental /07 m from the Task Metadata Service for valid reasons
AWS Attached Malicious Lambda Detects when an user attached a Lambda layer to an existing function to override a
Layer library that is in use by the function, where their malicious code could utilize the function's
IAM role for AWS API calls. This would give an adversary access to the privileges
associated with the Lambda service role that is attached to that function.
More details
Rule ID
aws_9
Query
{'selection': {'eventSource': 'lambda.amazonaws.com', 'ev
entName|startswith': 'UpdateFunctionConfiguration'}, 'con
dition': 'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,97fbabf8-8e1b-47a2-b7d5-a418d2b95e3d
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0004 , T1548 
References

Title Description
https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfigurat
ion.html 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urit ion Leve
y Date l
test 2021/ medi
Lambda Layer being attached may be performed by a
09/23 um system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment.
Lambda Layer being attached from unfamiliar users should
be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS EKS Cluster Created or Identifies when an EKS cluster is created or deleted.
Deleted
More details
Rule ID
aws_10
Query
{'selection': {'eventSource': 'eks.amazonaws.com', 'event
Name': ['CreateCluster', 'DeleteCluster']}, 'condition':
'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,33d50d03-20ec-4b74-a74e-1e65a38af1c0
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0040 , T1485 
References
https://any-api.com/amazonaws_com/eks/docs/API_Description 
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Title Description
Mat Creati Risk False Positives
urit on Leve
y Date l
test 2021/ low
EKS Cluster being created or deleted may be performed
08/16 by a system administrator.
Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.
EKS Cluster created or deleted from unfamiliar users
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS SecurityHub Findings Detects the modification of the findings on SecurityHub.
Evasion
More details
Rule ID
aws_15
Query
{'selection': {'eventSource': 'securityhub.amazonaws.com'
, 'eventName': ['BatchUpdateFindings', 'DeleteInsight', '
UpdateFindings', 'UpdateInsight']}, 'condition': 'selecti
on'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,a607e1fe-74bf-4440-a3ec-b059b9103157
Author: Sittikorn S
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
https://docs.aws.amazon.com/cli/latest/reference/securityhub/ 
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
stable 2021/06/ high
System or Network administrator behaviors
28
DEV, UAT, SAT environment. You should apply this
rule with PROD environment only.
AWS GuardDuty Detector Deletion Identifies the deletion of an Amazon GuardDuty detector. Upon deletion, GuardDuty stops
monitoring the environment and all existing findings are lost.
More details

Title Description
Rule ID
aws_16
Query
{'selection1': {'eventSource': 'guardduty.amazonaws.com'}
, 'selection2': {'eventName': 'DeleteDetector'}, 'conditi
on': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2020/ high
The GuardDuty detector may be deleted by a system or
uctio 05/28 network administrator. Verify whether the user identity,
n user agent, and/or hostname should be making changes in
your environment. Detector deletions by unfamiliar users
or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
AWS ElastiCache Security Group Identifies when an ElastiCache security group has been created.
Created
More details
Rule ID
aws_22
Query
{'selection1': {'eventSource': 'elasticache.amazonaws.com
'}, 'selection2': {'eventName': 'Create Cache Security Gr
oup'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 

Title Description
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2021/ low
A ElastiCache security group may be created by a system
uctio 07/19 or network administrator. Verify whether the user identity,
n user agent, and/or hostname should be making changes in
your environment. Security group creations by unfamiliar
users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
AWS IAM Password Recovery Identifies AWS IAM password recovery requests. An adversary may attempt to gain
Requested unauthorized AWS access by abusing password recovery mechanisms.
More details
Rule ID
aws_25
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, '
selection2': {'eventName': 'PasswordRecoveryRequested'},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Title Description
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2020/ low
Verify whether the user identity, user agent, and/or
uctio 07/02 hostname should be requesting changes in your
n environment. Password reset attempts from unfamiliar
users should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
AWS EventBridge Rule Disabled or Identifies when a user has disabled or deleted an EventBridge rule. This activity can
Deleted result in an unintended loss of visibility in applications or a break in the flow with other
AWS services.
More details
Rule ID
aws_27
Query
{'selection1': {'eventSource': 'eventbridge.amazonaws.com
'}, 'selection2': {'eventName': ['DeleteRule', 'DisableRu
le']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1489 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2021/ low
EventBridge Rules could be deleted or disabled by a
uctio 10/17 system administrator. Verify whether the user identity, user
n agent, and/or hostname should be making changes in your
environment. EventBridge Rules being deleted or disabled
by unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted
from the rule.
AWS CloudWatch Alarm Deletion Identifies the deletion of an AWS CloudWatch alarm. An adversary may delete alarms in
an attempt to evade defenses.
More details
Rule ID

Title Description
aws_28
Query
{'selection1': {'eventSource': 'monitoring.amazonaws.com'
}, 'selection2': {'eventName': 'DeleteAlarms'}, 'conditio
n': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2020/ medi
Verify whether the user identity, user agent, and/or
uctio 06/15 um hostname should be making changes in your environment.
n Alarm deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives,
it can be exempted from the rule.
AWS Configuration Recorder Identifies an AWS configuration change to stop recording a designated set of resources.
Stopped
More details
Rule ID
aws_39
Query
{'selection1': {'eventSource': 'config.amazonaws.com'}, '
selection2': {'eventName': 'StopConfigurationRecorder'},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References

Title Description
N/A
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2020/ high
Verify whether the user identity, user agent, and/or
uctio 06/16 hostname should be making changes in your environment.
n Recording changes from unfamiliar users or hosts should
be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS Config Resource Deletion Identifies attempts to delete an AWS Config Service resource. An adversary may tamper
with Config services in order to reduce visibility into the security posture of an account
and / or its workload instances.
More details
Rule ID
aws_41
Query
{'selection1': {'eventSource': 'config.amazonaws.com'}, '
selection2': {'eventName': ['DeleteConfigRule', 'DeleteOr
ganizationConfigRule', 'DeleteConfigurationAggregator', '
DeleteConfigurationRecorder', 'DeleteConformancePack', 'D
eleteOrganizationConformancePack', 'DeleteDeliveryChannel
', 'DeleteRemediationConfiguration', 'DeleteRetentionConf
iguration']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Title Description
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2020/ low
Privileged IAM users with security responsibilities may be
uctio 06/26 expected to make changes to the Config service in order to
n align with local security policies and requirements.
Automation, orchestration, and security tools may also
make changes to the Config service, where they are used
to automate setup or configuration of AWS accounts. Other
kinds of user or service contexts do not commonly make
changes to this service.
AWS STS GetSessionToken Abuse Identifies the suspicious use of GetSessionToken. Tokens could be created and used by
attackers to move laterally and escalate privileges.
More details
Rule ID
aws_43
Query
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'sel
ection2': {'eventName': 'GetSessionToken'}, 'selection3':
{'userIdentity_type': 'IAMUser'}, 'condition': 'selectio
n1 and selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1548 , TA0008 , T1550 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2021/ low
GetSessionToken may be done by a system or network
uctio 05/17 administrator. Verify whether the user identity, user agent,
n and/or hostname should be making changes in your
environment. GetSessionToken from unfamiliar users or
hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
AWS WAF Rule or Rule Group Identifies the deletion of a specified AWS Web Application Firewall (WAF) rule or rule
Deletion group.
More details

Title Description
Rule ID
aws_46
Query
{'selection1': {'eventSource': ['waf.amazonaws.com', 'waf
-
regional.amazonaws.com', 'wafv2.amazonaws.com']}, 'select
ion2': {'eventName': ['DeleteRule', 'DeleteRuleGroup']},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2020/ medi
WAF rules or rule groups may be deleted by a system or
uctio 06/09 um network administrator. Verify whether the user identity,
n user agent, and/or hostname should be making changes in
your environment. Rule deletions by unfamiliar users or
hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
AWS ElastiCache Security Group Identifies when an ElastiCache security group has been modified or deleted.
Modified or Deleted
More details
Rule ID
aws_47
Query
{'selection1': {'eventSource': 'elasticache.amazonaws.com
'}, 'selection2': {'eventName': ['Delete Cache Security G
roup', 'Authorize Cache Security Group Ingress', 'Revoke
Cache Security Group Ingress', 'AuthorizeCacheSecurityGro
upEgress', 'RevokeCacheSecurityGroupEgress']}, 'condition
': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source

Title Description
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2021/ low
A ElastiCache security group deletion may be done by a
uctio 07/19 system or network administrator. Verify whether the user
n identity, user agent, and/or hostname should be making
changes in your environment. Security Group deletions by
unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted
from the rule.
AWS WAF Access Control List Identifies the deletion of a specified AWS Web Application Firewall (WAF) access control
Deletion list.
More details
Rule ID
aws_49
Query
{'selection1': {'eventSource': 'waf.amazonaws.com'}, 'sel
ection2': {'eventName': 'DeleteWebACL'}, 'condition': 'se
lection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id

Title Description
Additional Information
| Mat Creat  | Risk False Positives |     |     |
| ---------- | -------------------- | --- | --- |
| urity ion  | Leve                 |     |     |
| Date       | l                    |     |     |
| prod 2020/ | medi                 |     |     |
Firewall ACL's may be deleted by a system or network
uctio 05/21 um administrator. Verify whether the user identity, user agent,
| n   |     | and/or hostname should be making changes in your |     |
| --- | --- | ------------------------------------------------ | --- |
environment. Web ACL deletions by unfamiliar users or
hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
AWS CloudWatch Log Stream Identifies the deletion of an AWS CloudWatch log stream, which permanently deletes all
Deletion associated archived log events with the stream.
More details
Rule ID
aws_52
Query
{'selection1': {'eventSource': 'logs.amazonaws.com'}, 'se
lection2': {'eventName': 'DeleteLogStream'}, 'condition':
 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
| TA0005 | , T1562 , TA0040 | , T1485 |    |
| ------ | ------------------ | -------- | --- |
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
| Mat Creat   | Risk False Positives |                                                        |     |
| ----------- | -------------------- | ------------------------------------------------------ | --- |
| urity ion   | Leve                 |                                                        |     |
| Date        | l                    |                                                        |     |
| prod 2020/  | medi                 | A log stream may be deleted by a system administrator. |     |
| uctio 05/20 | um                   | Verify whether the user identity, user agent, and/or   |     |
| n           |                      | hostname should be making changes in your environment. |     |
Log stream deletions by unfamiliar users or hosts should
be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS SAML Activity Identifies when SAML activity has occurred in AWS. An adversary could manipulate SAML
to maintain access to the target.
More details
Rule ID

Title Description
aws_53
Query
{'selection1': {'eventSource': 'iam.amazonaws.com', 'even
tName': 'AssumeRoleWithSAML'}, 'selection2': {'eventSourc
e': 'sts.amazonaws.com', 'eventName': 'UpdateSAMLProvider
'}, 'condition': 'selection1 or selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1078 , TA0005 , T1550 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2021/ low
SAML Provider could be updated by a system
uctio 09/22 administrator. Verify whether the user identity, user agent,
n and/or hostname should be making changes in your
environment. SAML Provider updates by unfamiliar users
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS CloudWatch Log Group Identifies the deletion of a specified AWS CloudWatch log group. When a log group is
Deletion deleted, all the archived log events associated with the log group are also permanently
deleted.
More details
Rule ID
aws_55
Query
{'selection1': {'eventSource': 'logs.amazonaws.com'}, 'se
lection2': {'eventName': 'DeleteLogGroup'}, 'condition':
'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

Title Description
TA0005 , T1562 , TA0040 , T1485 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2020/ medi
Verify whether the user identity, user agent, and/or
uctio 05/18 um hostname should be making changes in your environment.
n Log group deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives,
it can be exempted from the rule.
AWS KMS Customer Managed Identifies attempts to disable or schedule the deletion of an AWS KMS Customer
Key Disabled or Scheduled for Managed Key (CMK). Deleting an AWS KMS key is destructive and potentially
Deletion dangerous. It deletes the key material and all metadata associated with the KMS key and
is irreversible. After a KMS key is deleted, the data that was encrypted under that KMS
key can no longer be decrypted, which means that data becomes unrecoverable.
More details
Rule ID
aws_56
Query
{'selection1': {'eventSource': 'kms.amazonaws.com'}, 'sel
ection2': {'eventName': ['DisableKey', 'ScheduleKeyDeleti
on']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1485 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Title Description
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2022/ medi
A KMS customer managed key may be disabled or
uctio 09/21 um scheduled for deletion by a system administrator. Verify
n whether the user identity, user agent, and/or hostname
should be making changes in your environment. Key
deletions by unfamiliar users should be investigated. If
known behavior is causing false positives, it can be
exempted from the rule.
AWS Redshift Cluster Creation Identifies the creation of an Amazon Redshift cluster. Unexpected creation of this cluster
by a non-administrative user may indicate a permission or role issue with current users. If
unexpected, the resource may not properly be configured and could introduce security
vulnerabilities.
More details
Rule ID
aws_61
Query
{'selection1': {'eventSource': 'redshift.amazonaws.com'},
'selection2': {'eventName': 'CreateCluster'}, 'condition
': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Lev
Date el
prod 2022/ low
Valid clusters may be created by a system or network
uctio 04/12 administrator. Verify whether the user identity, user agent,
n and/or hostname should be making changes in your
environment. Cluster creations by unfamiliar users or hosts
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
AWS EFS File System or Mount Detects when an EFS File System or Mount is deleted. An adversary could break any file
Deleted system using the mount target that is being deleted, which might disrupt instances or
applications using those mounts. The mount must be deleted prior to deleting the File
System, or the adversary will be unable to delete the File System.

Title Description
More details
Rule ID
aws_67
Query
{'selection1': {'eventSource': 'elasticfilesystem.amazona
ws.com'}, 'selection2': {'eventName': ['DeleteMountTarget
', 'DeleteFileSystem']}, 'condition': 'selection1 and sel
ection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1485 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2021/ medi
File System or Mount being deleted may be performed by
uctio 08/27 um a system administrator. Verify whether the user identity,
n user agent, and/or hostname should be making changes in
your environment. File System Mount deletion by
unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the
rule.
AWS Security Token Service (STS) Identifies the use of AssumeRole. AssumeRole returns a set of temporary security
AssumeRole Usage credentials that can be used to access AWS resources. An adversary could use those
credentials to move laterally and escalate privileges.
More details
Rule ID
aws_70
Query
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'sel
ection2': {'eventName': 'AssumedRole'}, 'condition': 'sel
ection1 and selection2'}
Log Source
Stellar Cyber AWS configured.

Title Description
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1548 , TA0008 , T1550 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
product 2021/05/1 low
Automated processes that use Terraform may
ion 7 lead to false positives.
AWS Lambda This analytic is designed to detect IAM users attempting to update/modify AWS lambda
UpdateFunctionCode code via the AWS CLI to gain persistence, further access into AWS environment and to
facilitate planting backdoors. In this instance, an attacker may upload malicious
code/binary to a lambda function which will be executed automatically when the function
is triggered.
More details
Rule ID
aws_89
Query
{'selection2': {'eventSource': 'lambda.amazonaws.com'}, '
selection3': {'eventName': 'UpdateFunctionCode*'}, 'selec
tion4': {'errorCode': 'success'}, 'selection5': {'userIde
ntity_type': 'IAMUser'}, 'condition': 'selection2 and sel
ection3 and selection4 and selection5'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1204 
References
https://sysdig.com/blog/exploit-mitigate-aws-lambdas-mitre/ 
Severity
70
Suppression Logic Based On
service_id
aws.eventSource

Title Description
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2022- medi
While this search has no known false positives, it is
uctio 02-24 um possible that an AWS admin or an authorized IAM user
n has updated the lambda function code legitimately.
AWS ECR Container Scanning This search looks for AWS CloudTrail events from AWS Elastic Container Registry (ECR)
Findings Service.
More details
Rule ID
aws_90
Query
{'selection2': {'eventSource': 'ecr.amazonaws.com'}, 'sel
ection3': {'eventName': 'DescribeImageScanFindings'}, 'co
ndition': 'selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1204 
References
https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-
scanning.html 
Severity
10
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022-08-25 medium
unknown
AWS SAML Access by Provider This search provides specific SAML access from specific Service Provider, user and
User and Principal targeted principal at AWS. It also provides specific information to detect abnormal access
or potential credential hijack or forgery, specially in federated environments using SAML
protocol inside the perimeter or cloud provider.
More details
Rule ID
aws_111
Query

Title Description
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'sel
ection2': {'eventName': 'AssumeRoleWithSAML'}, 'condition
': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1078 
References
https://www.cisa.gov/uscert/ncas/alerts/aa21-008a 
https://www.splunk.com/en_us/blog/security/a-golden-saml-journey-
solarwinds-continued.html 
https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/wp-m-unc2452-
2021-000343-01.pdf 
https://www.cyberark.com/resources/threat-research-blog/golden-saml-newly-
discovered-attack-technique-forges-authentication-to-cloud-apps 
Severity
80
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Mat Creat Risk False Positives
urity ion Leve
Date l
prod 2021- medi
Attacks using a Golden SAML or SAML assertion hijacks
uctio 01-26 um or forgeries are very difficult to detect as accessing cloud
n providers with these assertions looks exactly like normal
access, however things such as source IP
sourceIPAddress user, and principal targeted at receiving
cloud provider along with endpoint credential access and
abuse detection searches can provide the necessary
context to detect these attacks.
KMS Keys Creation This search provides detection of KMS Keys Creation
More details
Rule ID
aws_118
Query
{'selection1': {'eventSource': 'kms.amazonaws.com'}, 'sel
ection2': {'eventName': 'CreateKey'}, 'selection3': {'eve
ntName': 'PutKeyPolicy'}, 'condition': 'selection1 and (s
election2 or selection3)'}
Log Source
Stellar Cyber AWS configured.
Rule Source

Title Description
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
| TA0040 , T1486 |    |     |     |
| --------------- | --- | --- | --- |
References
https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/ 
| https://github.com/d1vious/git-wild-hunt    |     |    |     |
| ------------------------------------------- | --- | --- | --- |
| https://www.youtube.com/watch?v=PgzNib37g0M |     |     |    |
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
| Maturity   | Creation Date | Risk Level | False Positives |
| ---------- | ------------- | ---------- | --------------- |
| production | 2021-01-11    | medium     | unknown         |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        