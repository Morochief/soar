✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
All Rules
This article contains all Stellar Cyber rules, including SigmaHQ rules and rules developed
internally by Stellar Cyber. The rules are listed alphabetically by their rule ID.
 Due to silent or deleted rules, the rule IDs are not sequential.
Active Directory (AD) Rule IDs
Rule Details: Active Directory MachineAccountQuota Compromise
MachineAccountQuota is an attribute in Active Directory that specifies how many machine
accounts a user can create in the domain. Compromise of MachineAccountQuota occurs when
an attacker abuses this privilege to create unauthorised machine accounts. Machine accounts
are assigned credentials, just like user accounts. Attackers can extract the credentials (password
hashes) for further use. These accounts can then be used for other malicious purposes, often
bypassing standard account monitoring mechanisms.
Rule ID
ad_machineAccountQuota_compromise
Query
{'selection': {'EventID': [4741, 4720], 'TargetUserName|endswith': '$'}, 'condition':
'selection | count() by SubjectUserName > 3', 'timeframe': '15m'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136 

References
https://rootguard.gitbook.io/cyberops/detection-engineering/ad-attack-detections-and-
mitigations/machineaccountquota-compromise 
Severity
50
Suppression Logic Based On
event_data.SubjectUserName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/06/ mediu False positives are possible if multiple machine accounts are created by legitimate users. We
recommend excluding trusted service accounts or administrators. However, limiting the ability
ental 13 m of non-privileged users to register devices is highly recommended.
Amazon Web Services (AWS) Rule IDs
Rule Details: Restore Public AWS RDS Instance
Detects the recovery of a new public database instance from a snapshot. It may be a part of data
exfiltration.
Rule ID
aws_1
Query
{'selection_source': {'eventSource': 'rds.amazonaws.com', 'responseElements_publiclyA
ccessible': True, 'eventName': 'RestoreDBInstanceFromDBSnapshot'}, 'condition': 'sele
ction_source'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,c3f265c7-ff03-4056-8ab2-d486227b4599
Author: faloker
Tactics, Techniques, and Procedures
TA0010 , T1020 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/rds__explore_snapshots/main.py 

Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/02/12 high Unknown
Rule Details: AWS User Login Profile Was Modified
An attacker with the iam:UpdateLoginProfile permission on other users can change the password
used to login to the AWS console on any user that already has a login profile setup. With this
alert, it is used to detect anyone is changing password on behalf of other users.
Rule ID
aws_2
Query
{'selection_source': {'eventSource': 'iam.amazonaws.com', 'eventName': 'UpdateLoginPr
ofile'}, 'filter': {'userIdentity_arn|contains': 'requestParameters.userName'}, 'cond
ition': 'selection_source and not filter'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,055fb148-60f8-462d-ad16-26926ce050f1
Author: toffeebr33k
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://github.com/RhinoSecurityLabs/AWS-IAM-Privilege-Escalation 
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName

aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high Legit User Account Administration
Rule Details: SES Identity Has Been Deleted
Detects an instance of an SES identity being deleted via the "DeleteIdentity" event. This may be
an indicator of an adversary removing the account that carried out suspicious or malicious
activities.
Rule ID
aws_3
Query
{'selection': {'eventSource': 'ses.amazonaws.com', 'eventName': 'DeleteIdentity'}, 'c
ondition': 'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,20f754db-d025-4a8f-9d74-e0037e999a9a
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/ 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/13 medium Unknown
Rule Details: AWS GuardDuty Important Change

Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts against
malicious IPs.
Rule ID
aws_4
Query
{'selection_source': {'eventSource': 'guardduty.amazonaws.com', 'eventName': 'CreateI
PSet'}, 'condition': 'selection_source'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,6e61ee20-ce00-4f8d-8aee-bedd8216f7e3
Author: faloker
Tactics, Techniques, and Procedures
TA0005 , T1562.001 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/guardduty__whitelist_ip/main.py#L9 
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/02/11 high Valid change in the GuardDuty (e.g. to ignore internal scanners)
Rule Details: AWS Glue Development Endpoint Activity
Detects possible suspicious glue development endpoint activity.
Rule ID
aws_5
Query
{'selection': {'eventSource': 'glue.amazonaws.com', 'eventName': ['CreateDevEndpoint'
, 'DeleteDevEndpoint', 'UpdateDevEndpoint']}, 'condition': 'selection'}

Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,4990c2e3-f4b8-45e3-bc3c-30b14ff0ed26
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1078 
References
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/ 
https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDevEndpoint.html 
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
experim 2021/10/ low Glue Development Endpoint Activity may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
ental 03
environment.
If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Potential Bucket Enumeration on AWS
Looks for potential enumeration of AWS buckets via ListBuckets.
Rule ID
aws_6
Query
{'selection': {'eventSource': 'ec2.amazonaws.com', 'eventName': 'ListBuckets'}, 'filt
er': {'type': 'AssumedRole'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source

SigmaHQ,f305fd62-beca-47da-ad95-7690a0620084
Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
https://github.com/Lifka/hacking-
resources/blob/c2ae355d381bd0c9f0b32c4ead049f44e5b1573f/cloud-hacking-cheat-
sheets.md 
https://jamesonhacking.blogspot.com/2020/12/pivoting-to-private-aws-s3-
buckets.html 
https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/ 
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2023/01/06 low Administrators listing buckets, it may be necessary to filter out users who commonly
conduct this activity.
tal
Rule Details: AWS ECS Backdoor Task Definition
Detects when an Elastic Container Service (ECS) Task Definition has been modified and run.
This can indicate an adversary adding a backdoor to establish persistence or escalate privileges.
This rule is based on examining events created upon execution of Rhino Security Lab's Pacu in
a lab environment.
Rule ID
aws_7
Query
{'selection': {'eventSource': 'ecs.amazonaws.com', 'eventName': ['DescribeTaskDefinit
ion', 'RegisterTaskDefinition', 'RunTask'], 'requestParameters_containerDefinitions_c
ommand|contains|all': ['169.254', '$AWS_CONTAINER_CREDENTIALS']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber AWS configured for:

AWS Cloudtrail
Rule Source
SigmaHQ,b94bf91e-c2bf-4047-9c43-c6810f43baad
Author: Darin Smith
Tactics, Techniques, and Procedures
TA0003 , T1525 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/ecs__backdoor_task_def/main.py 
https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefin
ition.html 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/06/07 medium Task Definition being modified to request credentials from the Task Metadata Service
for valid reasons
tal
Rule Details: AWS EC2 Startup Shell Script Change
Detects changes to the EC2 instance startup script. The shell script will be executed as
root/SYSTEM every time the specific instances are booted up.
Rule ID
aws_8
Query
{'selection_source': {'eventSource': 'ec2.amazonaws.com', 'requestParameters_attribut
e': 'userData', 'eventName': 'ModifyInstanceAttribute'}, 'condition': 'selection_sour
ce'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source

SigmaHQ,1ab3c5ed-5baf-417b-bb6b-78ca33f6c3df
Author: faloker
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/ec2__startup_shell_script/main.py#L9 
Severity
75
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/02/12 high Valid changes to the startup script
Rule Details: AWS Attached Malicious Lambda Layer
Detects when an user attached a Lambda layer to an existing function to override a library that is
in use by the function, where their malicious code could utilize the function's IAM role for AWS
API calls. This would give an adversary access to the privileges associated with the Lambda
service role that is attached to that function.
Rule ID
aws_9
Query
{'selection': {'eventSource': 'lambda.amazonaws.com', 'eventName|startswith': 'Update
FunctionConfiguration'}, 'condition': 'selection'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,97fbabf8-8e1b-47a2-b7d5-a418d2b95e3d
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0004 , T1548 

References
https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfiguration.html

Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/09/ mediu Lambda Layer being attached may be performed by a system administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
23 m
Lambda Layer being attached from unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.
Rule Details: AWS EKS Cluster Created or Deleted
Identifies when an EKS cluster is created or deleted.
Rule ID
aws_10
Query
{'selection': {'eventSource': 'eks.amazonaws.com', 'eventName': ['CreateCluster', 'De
leteCluster']}, 'condition': 'selection'}
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ low EKS Cluster being created or deleted may be performed by a system administrator.
16 Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
EKS Cluster created or deleted from unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.
Rule Details: AWS S3 Data Management Tampering
Detects when a user tampers with S3 data management in Amazon Web Services.
Rule ID
aws_11
Query
{'selection': {'eventSource': 's3.amazonaws.com', 'eventName': ['PutBucketLogging', '
PutBucketWebsite', 'PutEncryptionConfiguration', 'PutLifecycleConfiguration', 'PutRep
licationConfiguration', 'ReplicateObject', 'RestoreObject']}, 'condition': 'selection
'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,78b3756a-7804-4ef7-8555-7b9024a02e2d
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0010 , T1537 
References
https://github.com/elastic/detection-rules/pull/1145/files 
https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html 
https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html 
https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html 
https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html 

https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-
overview.html 
https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html 
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/07/ low A S3 configuration change may be done by a system or network administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
24 S3 configuration change from unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Root Credentials
Detects AWS root account usage.
Rule ID
aws_12
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selection_usertype': {'userI
dentity_type': 'Root'}, 'selection_eventtype': {'eventType': 'AwsServiceEvent'}, 'con
dition': 'selection1 and selection_usertype and not selection_eventtype'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,8ad1600d-e9dc-4251-b0ee-a65268f29add
Author: vitaliy0x1
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html 
Severity
50

Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2020/01/2 mediu AWS Tasks That Require AWS Account Root User Credentials
https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html
1 m
Rule Details: AWS IAM Backdoor Users Keys
Detects AWS API key creation for a user by another user. Backdoored users can be used to
obtain persistence in the AWS environment. Also with this alert, you can detect a flow of AWS
keys in your org.
Rule ID
aws_13
Query
{'selection_source': {'eventSource': 'iam.amazonaws.com', 'eventName': 'CreateAccessK
ey'}, 'filter': {'userIdentity_arn|contains': 'responseElements.accessKey.userName'},
'condition': 'selection_source and not filter'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,0a5177f4-6ca9-44c2-aacf-d3f3d8b6e4d2
Author: faloker
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/iam__backdoor_users_keys/main.py 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName

aws.errorCode
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2020/02/12 medium Adding user keys to their own accounts (the filter cannot cover all possible variants of
user naming)
AWS API keys legitimate exchange workflows
Rule Details: AWS RDS Master Password Change
Detects the change of database master password. It may be a part of data exfiltration.
Rule ID
aws_14
Query
{'selection_source': {'eventSource': 'rds.amazonaws.com', 'responseElements_pendingMo
difiedValues_masterUserPassword|contains': '*', 'eventName': 'ModifyDBInstance'}, 'co
ndition': 'selection_source'}
Log Source
Stellar Cyber AWS configured for:
AWS Cloudtrail
Rule Source
SigmaHQ,8a63cdd4-6207-414a-85bc-7e032bd3c1a2
Author: faloker
Tactics, Techniques, and Procedures
TA0010 , T1020 
References
https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817
f2c5b181/pacu/modules/rds__explore_snapshots/main.py 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2020/02/12 medium Benign changes to a db instance
Rule Details: AWS SecurityHub Findings Evasion
Detects the modification of the findings on SecurityHub.
Rule ID
aws_15
Query
{'selection': {'eventSource': 'securityhub.amazonaws.com', 'eventName': ['BatchUpdate
Findings', 'DeleteInsight', 'UpdateFindings', 'UpdateInsight']}, 'condition': 'select
ion'}
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
Maturit Creation Risk False Positives
y Date Level
stable 2021/06/28 high System or Network administrator behaviors
DEV, UAT, SAT environment. You should apply this rule with PROD environment
only.
Rule Details: AWS GuardDuty Detector Deletion
Identifies the deletion of an Amazon GuardDuty detector. Upon deletion, GuardDuty stops
monitoring the environment and all existing findings are lost.

Rule ID
aws_16
Query
{'selection1': {'eventSource': 'guardduty.amazonaws.com'}, 'selection2': {'eventName'
: 'DeleteDetector'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ high The GuardDuty detector may be deleted by a system or network administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
tion 28 Detector deletions by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS Route Table Created
Identifies when an AWS Route Table has been created.
Rule ID
aws_18
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'eventName
': ['CreateRoute', 'CreateRouteTable']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ low Route Tables may be created by a system or network administrators. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Route
tion 05
Table creation by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule. Automated processes that use
Terraform may lead to false positives.
Rule Details: AWS RDS Snapshot Export
Identifies the export of an Amazon Relational Database Service (RDS) Aurora database
snapshot.
Rule ID
aws_21
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': 'Sta
rtExportTask'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0010 , T1567 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ low Exporting snapshots may be done by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 06
Snapshot exports from unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS ElastiCache Security Group Created
Identifies when an ElastiCache security group has been created.
Rule ID
aws_22
Query
{'selection1': {'eventSource': 'elasticache.amazonaws.com'}, 'selection2': {'eventNam
e': 'Create Cache Security Group'}, 'condition': 'selection1 and selection2'}
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

Maturi Creation Risk False Positives
ty Date Level
produc 2021/07/ low A ElastiCache security group may be created by a system or network administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
tion 19
environment. Security group creations by unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS IAM User Addition to Group
Identifies the addition of a user to a specified group in AWS Identity and Access Management
(IAM).
Rule ID
aws_24
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Add
UserToGroup'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ low Adding users to a specified group may be done by a system or network administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
tion 04
environment. User additions from unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS IAM Password Recovery Requested

Identifies AWS IAM password recovery requests. An adversary may attempt to gain unauthorized
AWS access by abusing password recovery mechanisms.
Rule ID
aws_25
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selection2': {'eventName': '
PasswordRecoveryRequested'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/07/ low Verify whether the user identity, user agent, and/or hostname should be requesting changes in
your environment. Password reset attempts from unfamiliar users should be investigated. If
tion 02 known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS IAM Group Creation
Identifies the creation of a group in AWS Identity and Access Management (IAM). Groups specify
permissions for multiple users. Any user in a group automatically has the permissions that are
assigned to the group.
Rule ID
aws_26
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateGroup'}, 'condition': 'selection1 and selection2'}

Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ low A group may be created by a system or network administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. Group creations
tion 05
by unfamiliar users or hosts should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
Rule Details: AWS EventBridge Rule Disabled or Deleted
Identifies when a user has disabled or deleted an EventBridge rule. This activity can result in an
unintended loss of visibility in applications or a break in the flow with other AWS services.
Rule ID
aws_27
Query
{'selection1': {'eventSource': 'eventbridge.amazonaws.com'}, 'selection2': {'eventNam
e': ['DeleteRule', 'DisableRule']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/10/ low EventBridge Rules could be deleted or disabled by a system administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 17
EventBridge Rules being deleted or disabled by unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS CloudWatch Alarm Deletion
Identifies the deletion of an AWS CloudWatch alarm. An adversary may delete alarms in an
attempt to evade defenses.
Rule ID
aws_28
Query
{'selection1': {'eventSource': 'monitoring.amazonaws.com'}, 'selection2': {'eventName
': 'DeleteAlarms'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ mediu Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Alarm deletions by unfamiliar users or hosts should be investigated. If
tion 15 m
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Route Table Modified or Deleted
Identifies when an AWS Route Table has been modified or deleted.
Rule ID
aws_29
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'eventName
': ['ReplaceRoute', 'ReplaceRouteTableAssociation', 'DeleteRouteTable', 'DeleteRoute'
, 'DisassociateRouteTable']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ low Route Table could be modified or deleted by a system administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Route
tion 05 Table being modified from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule. Also automated processes that use
Terraform may lead to false positives.
Rule Details: AWS EC2 Network Access Control List Creation

Identifies the creation of an AWS Elastic Compute Cloud (EC2) network access control list (ACL)
or an entry in a network ACL with a specified rule number.
Rule ID
aws_30
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': ['Cr
eateNetworkAcl', 'CreateNetworkAclEntry']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1133 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ low Network ACL's may be created by a network administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. Network ACL
tion 04 creations by unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS Management Console Root Login
Identifies a successful login to the AWS Management Console by the Root user.
Rule ID
aws_31
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selection2': {'eventName': '
ConsoleLogin'}, 'selection3': {'userIdentity_type': 'Root'}, 'condition': 'selection1
and selection2 and selection3'}

Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1078 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ mediu It's strongly recommended that the root user is not used for everyday tasks, including the
administrative ones. Verify whether the IP address, location, and/or hostname should be
tion 11 m logging in as root in your environment. Unfamiliar root logins should be investigated
immediately. If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Route53 private hosted zone associated with a VPC
Identifies when a Route53 private hosted zone has been associated with VPC.
Rule ID
aws_32
Query
{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'selection2': {'eventName':
'AssociateVPCWithHostedZone'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/07/ low A private hosted zone may be asssociated with a VPC by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
tion 19 your environment. If known behavior is causing false positives, it can be exempted from the
rule.
Rule Details: AWS CloudTrail Log Updated
Identifies an update to an AWS log trail setting that specifies the delivery of log files.
Rule ID
aws_34
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'eventName
': 'UpdateTrail'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 , TA0040 , T1565 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ low Trail updates may be made by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Trail
tion 10 updates from unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS Route 53 Domain Transfer Lock Disabled
Identifies when a transfer lock was removed from a Route 53 domain. It is recommended to
refrain from performing this action unless intending to transfer the domain to a different registrar.
Rule ID
aws_35
Query
{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'selection2': {'eventName':
'DisableDomainTransferLock'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/05/ low A domain transfer lock may be disabled by a system or network administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
tion 10
Activity from unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS RDS Cluster Creation

Identifies the creation of a new Amazon Relational Database Service (RDS) Aurora DB cluster or
global database spread across multiple regions.
Rule ID
aws_36
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': ['Cr
eateDBCluster', 'CreateGlobalCluster']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1133 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ low Valid clusters may be created by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Cluster
tion 20 creations by unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS S3 Bucket Configuration Deletion
Identifies the deletion of various Amazon Simple Storage Service (S3) bucket configuration
components.
Rule ID
aws_37
Query
{'selection1': {'eventSource': 's3.amazonaws.com'}, 'selection2': {'eventName': ['Del
eteBucketPolicy', 'DeleteBucketReplication', 'DeleteBucketCors', 'DeleteBucketEncrypt

ion', 'DeleteBucketLifecycle']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ low Bucket components may be deleted by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 27
Bucket component deletions by unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Configuration Recorder Stopped
Identifies an AWS configuration change to stop recording a designated set of resources.
Rule ID
aws_39
Query
{'selection1': {'eventSource': 'config.amazonaws.com'}, 'selection2': {'eventName': '
StopConfigurationRecorder'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ high Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Recording changes from unfamiliar users or hosts should be investigated. If
tion 16
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Config Resource Deletion
Identifies attempts to delete an AWS Config Service resource. An adversary may tamper with
Config services in order to reduce visibility into the security posture of an account and / or its
workload instances.
Rule ID
aws_41
Query
{'selection1': {'eventSource': 'config.amazonaws.com'}, 'selection2': {'eventName': [
'DeleteConfigRule', 'DeleteOrganizationConfigRule', 'DeleteConfigurationAggregator',
'DeleteConfigurationRecorder', 'DeleteConformancePack', 'DeleteOrganizationConformanc
ePack', 'DeleteDeliveryChannel', 'DeleteRemediationConfiguration', 'DeleteRetentionCo
nfiguration']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ low Privileged IAM users with security responsibilities may be expected to make changes to the
Config service in order to align with local security policies and requirements. Automation,
tion 26 orchestration, and security tools may also make changes to the Config service, where they are
used to automate setup or configuration of AWS accounts. Other kinds of user or service
contexts do not commonly make changes to this service.
Rule Details: AWS IAM Assume Role Policy Update
Identifies attempts to modify an AWS IAM Assume Role Policy. An adversary may attempt to
modify the AssumeRolePolicy of a misconfigured role in order to gain the privileges of that role.
Rule ID
aws_42
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Upd
ateAssumeRolePolicy'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1078 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information

Maturi Creation Risk False Positives
ty Date Level
produc 2020/07/ low Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Policy updates from unfamiliar users or hosts should be investigated. If
tion 06
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS STS GetSessionToken Abuse
Identifies the suspicious use of GetSessionToken. Tokens could be created and used by
attackers to move laterally and escalate privileges.
Rule ID
aws_43
Query
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'selection2': {'eventName': 'Get
SessionToken'}, 'selection3': {'userIdentity_type': 'IAMUser'}, 'condition': 'selecti
on1 and selection2 and selection3'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/05/ low GetSessionToken may be done by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment.
tion 17
GetSessionToken from unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS IAM Deactivation of MFA Device

Identifies the deactivation of a specified multi-factor authentication (MFA) device and removes it
from association with the user name for which it was originally enabled. In AWS Identity and
Access Management (IAM), a device must be deactivated before it can be deleted.
Rule ID
aws_44
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': ['De
activateMFADevice', 'DeleteVirtualMFADevice']}, 'condition': 'selection1 and selectio
n2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1531 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu A MFA device may be deactivated by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 26 m MFA device deactivations from unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS EC2 Network Access Control List Deletion
Identifies the deletion of an Amazon Elastic Compute Cloud (EC2) network access control list
(ACL) or one of its ingress/egress entries.
Rule ID
aws_45
Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': ['De
leteNetworkAcl', 'DeleteNetworkAclEntry']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu Network ACL's may be deleted by a network administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. Network ACL
tion 26 m deletions by unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS WAF Rule or Rule Group Deletion
Identifies the deletion of a specified AWS Web Application Firewall (WAF) rule or rule group.
Rule ID
aws_46
Query
{'selection1': {'eventSource': ['waf.amazonaws.com', 'waf-
regional.amazonaws.com', 'wafv2.amazonaws.com']}, 'selection2': {'eventName': ['Delet
eRule', 'DeleteRuleGroup']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ mediu WAF rules or rule groups may be deleted by a system or network administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
tion 09 m Rule deletions by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS ElastiCache Security Group Modified or Deleted
Identifies when an ElastiCache security group has been modified or deleted.
Rule ID
aws_47
Query
{'selection1': {'eventSource': 'elasticache.amazonaws.com'}, 'selection2': {'eventNam
e': ['Delete Cache Security Group', 'Authorize Cache Security Group Ingress', 'Revoke
Cache Security Group Ingress', 'AuthorizeCacheSecurityGroupEgress', 'RevokeCacheSecu
rityGroupEgress']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/07/ low A ElastiCache security group deletion may be done by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
tion 19
your environment. Security Group deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS WAF Access Control List Deletion
Identifies the deletion of a specified AWS Web Application Firewall (WAF) access control list.
Rule ID
aws_49
Query
{'selection1': {'eventSource': 'waf.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteWebACL'}, 'condition': 'selection1 and selection2'}
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

Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu Firewall ACL's may be deleted by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Web
tion 21 m
ACL deletions by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS IAM Group Deletion
Identifies the deletion of a specified AWS Identity and Access Management (IAM) resource
group. Deleting a resource group does not delete resources that are members of the group; it
only deletes the group structure.
Rule ID
aws_50
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteGroup'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1531 
References
N/A
Severity
25
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ low A resource group may be deleted by a system administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. Resource group
tion 21 deletions by unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS EC2 Snapshot Activity

An attempt was made to modify AWS EC2 snapshot attributes. Snapshots are sometimes shared
by threat actors in order to exfiltrate bulk data from an EC2 fleet. If the permissions were
modified, verify the snapshot was not shared with an unauthorized or unexpected AWS account.
Rule ID
aws_51
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Mod
ifySnapshotAttribute'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0010 , T1537 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ mediu IAM users may occasionally share EC2 snapshots with another AWS account belonging to the
same organization. If known behavior is causing false positives, it can be exempted from the
tion 24 m
rule.
Rule Details: AWS CloudWatch Log Stream Deletion
Identifies the deletion of an AWS CloudWatch log stream, which permanently deletes all
associated archived log events with the stream.
Rule ID
aws_52
Query
{'selection1': {'eventSource': 'logs.amazonaws.com'}, 'selection2': {'eventName': 'De
leteLogStream'}, 'condition': 'selection1 and selection2'}

Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu A log stream may be deleted by a system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your environment. Log stream deletions
tion 20 m by unfamiliar users or hosts should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
Rule Details: AWS SAML Activity
Identifies when SAML activity has occurred in AWS. An adversary could manipulate SAML to
maintain access to the target.
Rule ID
aws_53
Query
{'selection1': {'eventSource': 'iam.amazonaws.com', 'eventName': 'AssumeRoleWithSAML'
}, 'selection2': {'eventSource': 'sts.amazonaws.com', 'eventName': 'UpdateSAMLProvide
r'}, 'condition': 'selection1 or selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/09/ low SAML Provider could be updated by a system administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. SAML Provider
tion 22
updates by unfamiliar users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
Rule Details: AWS EC2 VM Export Failure
Identifies an attempt to export an AWS EC2 instance. A virtual machine (VM) export may indicate
an attempt to extract or exfiltrate information.
Rule ID
aws_54
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateInstanceExportTask'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1005 , TA0010 , T1537 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/04/ low VM exports may be done by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. VM
tion 22
exports from unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS CloudWatch Log Group Deletion
Identifies the deletion of a specified AWS CloudWatch log group. When a log group is deleted, all
the archived log events associated with the log group are also permanently deleted.
Rule ID
aws_55
Query
{'selection1': {'eventSource': 'logs.amazonaws.com'}, 'selection2': {'eventName': 'De
leteLogGroup'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Log group deletions by unfamiliar users or hosts should be investigated. If
tion 18 m known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS KMS Customer Managed Key Disabled or Scheduled for Deletion

Identifies attempts to disable or schedule the deletion of an AWS KMS Customer Managed Key
(CMK). Deleting an AWS KMS key is destructive and potentially dangerous. It deletes the key
material and all metadata associated with the KMS key and is irreversible. After a KMS key is
deleted, the data that was encrypted under that KMS key can no longer be decrypted, which
means that data becomes unrecoverable.
Rule ID
aws_56
Query
{'selection1': {'eventSource': 'kms.amazonaws.com'}, 'selection2': {'eventName': ['Di
sableKey', 'ScheduleKeyDeletion']}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2022/09/ mediu A KMS customer managed key may be disabled or scheduled for deletion by a system
administrator. Verify whether the user identity, user agent, and/or hostname should be making
tion 21 m changes in your environment. Key deletions by unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS EC2 Full Network Packet Capture Detected
Identifies potential Traffic Mirroring in an Amazon Elastic Compute Cloud (EC2) instance. Traffic
Mirroring is an Amazon VPC feature that you can use to copy network traffic from an Elastic
network interface. This feature can potentially be abused to exfiltrate sensitive data from
unencrypted internal traffic.
Rule ID

aws_57
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': ['Cr
eateTrafficMirrorFilter', 'CreateTrafficMirrorFilterRule', 'CreateTrafficMirrorSessio
n', 'CreateTrafficMirrorTarget']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1074 , TA0010 , T1020 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/05/ mediu Traffic Mirroring may be done by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Traffic
tion 05 m Mirroring from unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS EC2 Encryption Disabled
Identifies disabling of Amazon Elastic Block Store (EBS) encryption by default in the current
region. Disabling encryption by default does not change the encryption status of your existing
volumes.
Rule ID
aws_58
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Dis
ableEbsEncryptionByDefault'}, 'condition': 'selection1 and selection2'}
Log Source

Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1565 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ mediu Disabling encryption may be done by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 05 m
Disabling encryption by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS RDS Snapshot Restored
Identifies when an attempt was made to restore an RDS Snapshot. Snapshots are sometimes
shared by threat actors in order to exfiltrate bulk data or evade detection after performing
malicious activities. If the permissions were modified, verify if the snapshot was shared with an
unauthorized or unexpected AWS account.
Rule ID
aws_59
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': 'Res
toreDBInstanceFromDBSnapshot', 'responseElements_publiclyAccessible': False}, 'condit
ion': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0005 , T1578 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ mediu Restoring snapshots may be done by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 29 m Snapshot restoration by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS RDS Instance/Cluster Stoppage
Identifies that an Amazon Relational Database Service (RDS) cluster or instance has been
stopped.
Rule ID
aws_60
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': ['St
opDBCluster', 'StopDBInstance']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1489 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu Valid clusters or instances may be stopped by a system administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Cluster
tion 20 m or instance stoppages from unfamiliar users or hosts should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.
Rule Details: AWS Redshift Cluster Creation
Identifies the creation of an Amazon Redshift cluster. Unexpected creation of this cluster by a
non-administrative user may indicate a permission or role issue with current users. If
unexpected, the resource may not properly be configured and could introduce security
vulnerabilities.
Rule ID
aws_61
Query
{'selection1': {'eventSource': 'redshift.amazonaws.com'}, 'selection2': {'eventName':
'CreateCluster'}, 'condition': 'selection1 and selection2'}
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

Maturi Creation Risk False Positives
ty Date Level
produc 2022/04/ low Valid clusters may be created by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Cluster
tion 12
creations by unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: AWS Route 53 Domain Transferred to Another Account
Identifies when a request has been made to transfer a Route 53 domain to another AWS
account.
Rule ID
aws_63
Query
{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'selection2': {'eventName':
'TransferDomainToAnotherAwsAccount'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/05/ low A domain may be transferred to another AWS account by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
tion 10 your environment. Domain transfers from unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS Deletion of RDS Instance or Cluster
Identifies the deletion of an Amazon Relational Database Service (RDS) Aurora database cluster,
global database cluster, or database instance.

Rule ID
aws_64
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': ['De
leteDBCluster', 'DeleteGlobalCluster', 'DeleteDBInstance']}, 'condition': 'selection1
and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/05/ mediu Clusters or instances may be deleted by a system administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. Cluster
tion 21 m
or instance deletions by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS RDS Security Group Deletion
Identifies the deletion of an Amazon Relational Database Service (RDS) Security group.
Rule ID
aws_65
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteDBSecurityGroup'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1531 
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ low An RDS security group deletion may be done by a system or network administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
tion 05
environment. Security group deletions by unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS VPC Flow Logs Deletion
Identifies the deletion of one or more flow logs in AWS Elastic Compute Cloud (EC2). An
adversary may delete flow logs in an attempt to evade defenses.
Rule ID
aws_66
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteFlowLogs'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2020/06/ high Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Flow log deletions by unfamiliar users or hosts should be investigated. If
tion 15
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS EFS File System or Mount Deleted
Detects when an EFS File System or Mount is deleted. An adversary could break any file system
using the mount target that is being deleted, which might disrupt instances or applications using
those mounts. The mount must be deleted prior to deleting the File System, or the adversary will
be unable to delete the File System.
Rule ID
aws_67
Query
{'selection1': {'eventSource': 'elasticfilesystem.amazonaws.com'}, 'selection2': {'ev
entName': ['DeleteMountTarget', 'DeleteFileSystem']}, 'condition': 'selection1 and se
lection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/08/ mediu File System or Mount being deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
tion 27 m environment. File System Mount deletion by unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: AWS RDS Instance Creation
Identifies the creation of an Amazon Relational Database Service (RDS) Aurora database
instance.
Rule ID
aws_68
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateDBInstance'}, 'condition': 'selection1 and selection2'}
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
Maturi Creation Risk False Positives
ty Date Level
produc 2021/06/ low A database instance may be created by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
tion 06
Instances creations by unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: AWS Security Token Service (STS) AssumeRole Usage

Identifies the use of AssumeRole. AssumeRole returns a set of temporary security credentials
that can be used to access AWS resources. An adversary could use those credentials to move
laterally and escalate privileges.
Rule ID
aws_70
Query
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'selection2': {'eventName': 'Ass
umedRole'}, 'condition': 'selection1 and selection2'}
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
Maturity Creation Date Risk Level False Positives
production 2021/05/17 low Automated processes that use Terraform may lead to false positives.
Rule Details: AWS New MFA Method Registered For User
The following analytic identifies the registration of a new Multi Factor authentication method for
an AWS account. Adversaries who have obtained unauthorized access to an AWS account may
register a new MFA method to maintain persistence.
Rule ID
aws_75
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateVirtualMFADevice'}, 'condition': 'selection1 and selection2'}

Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1556 
References
https://aws.amazon.com/blogs/security/you-can-now-assign-multiple-mfa-devices-in-
iam/ 
https://twitter.com/jhencinski/status/1618660062352007174 
Severity
80
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
producti 2023-01-31 medium Newly onboarded users who are registering an MFA method for the first time will also
trigger this detection.
on
Rule Details: EC2 Snapshot Attribute Modification
The following analytic utilizes AWS CloudTrail events to identify when an EC2 snapshot
permissions are modified.
Rule ID
aws_76
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Mod
ifySnapshotAttribute'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures
TA0010 , T1537 
References
https://labs.nettitude.com/blog/how-to-exfiltrate-aws-ec2-data/ 
https://stratus-red-team.cloud/attack-techniques/AWS/aws.exfiltration.ec2-share-ebs-
snapshot/ 
https://hackingthe.cloud/aws/enumeration/loot_public_ebs_snapshots/ 
Severity
60
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2023-03-20 medium It is possible that an AWS admin has legitimately modified permissions of EC2
Snapshot.
n
Rule Details: AWS EC2 Security Group Deleted
An EC2 security group has been deleted.
Rule ID
aws_77
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteSecurityGroup'}, 'selection3': {'userAgent': 'cloudformation.amazonaws.com'}, 'con
dition': 'selection1 and selection2 and not selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS EC2 Security Group Modified
An EC2 security group has been modified.
Rule ID
aws_78
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteRouteTable'}, 'selection3': {'eventName': 'DeleteSubnet'}, 'selection4': {'eventNa
me': 'CreateDBSubnetGroup'}, 'selection5': {'eventName': 'DeleteDBSubnetGroup'}, 'sel
ection6': {'eventName': 'ModifyDBSubnetGroup'}, 'selection7': {'userAgent': 'cloudfor
mation.amazonaws.com'}, 'condition': 'selection1 and (selection2 or selection3 or sel
ection4 or selection5 or selection6) and not selection7'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS EC2 Security Group Created
An EC2 security group has been created.
Rule ID
aws_79
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateSecurityGroup'}, 'selection3': {'userAgent': 'cloudformation.amazonaws.com'}, 'con
dition': 'selection1 and selection2 and not selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS IAM User Created
A new account has been created in AWS IAM.
Rule ID
aws_80
Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateUser'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Created AWS IAM Credentials
New IAM credentials have been generated.
Rule ID
aws_81
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateAccessKey'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References

N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: IAM Policy Modification
The IAM policies associated with a user have been modified.
Rule ID
aws_82
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Upd
ateUserAccessPolicy'}, 'selection3': {'eventName': 'DeleteUserAccessPolicy'}, 'select
ion4': {'eventName': 'AddAccessPolicyToGroup'}, 'selection5': {'eventName': 'AddUserT
oGroup'}, 'selection6': {'eventName': 'RemoveUsersFromGroup'}, 'condition': 'selectio
n1 and (selection2 or selection3 or selection4 or selection5 or selection6)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName

aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS IAM AccessDenied Discovery Event
The following detection identifies AccessDenied event. It is possible that an access key to AWS
may have been stolen and is being misused to perform discovery events.
Rule ID
aws_83
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'errorCode': 'Acc
essDenied'}, 'selection3': {'userIdentity_type': 'IAMUser'}, 'selection4': {'userAgen
t': '*.amazonaws.com'}, 'condition': 'selection1 and selection2 and selection3 and no
t selection4'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-iam-
permission-errors/ 
Severity
20
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021-11-12 medium It is possible to start this detection will need to be tuned by source IP or user.
Rule Details: AWS IAM Delete Policy

The following detection identifies when a policy is deleted on AWS. This does not identify
whether successful or failed, but the error messages tell a story of suspicious attempts.
Rule ID
aws_84
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Del
etePolicy'}, 'selection3': {'userAgent': '*.amazonaws.com'}, 'condition': 'selection1
and selection2 and not selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicy.html 
https://docs.aws.amazon.com/cli/latest/reference/iam/delete-policy.html 
Severity
20
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021-04- mediu This detection will require tuning to provide high fidelity detection capabilities. Tune based on
src addresses (corporate offices, VPN terminations) or by groups of users. Not every user with
tion 01 m AWS access should have permission to delete policies (least privilege). In addition, this may
be saved separately and tuned for failed or success attempts only.
Rule Details: AWS IAM Failure Group Deletion
This detection identifies failure attempts to delete groups. We want to identify when a group is
attempting to be deleted, but either access is denied, there is a conflict or there is no group. This
is indicative of administrators performing an action, but also could be suspicious behavior
occurring.
Rule ID

aws_85
Query
{'selection2': {'eventSource': 'iam.amazonaws.com'}, 'selection3': {'eventName': 'Del
eteGroup'}, 'selection4': {'errorCode': ['NoSuchEntityException', 'DeleteConflictExce
ption']}, 'selection5': {'errorCode': 'AccessDenied'}, 'selection6': {'userAgent': '*
.amazonaws.com'}, 'condition': 'selection2 and selection3 and (selection4 or selectio
n5) and not selection6'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-
group.html 
https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroup.html 
Severity
10
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021-04- mediu This detection will require tuning to provide high fidelity detection capabilities. Tune based on
src addresses (corporate offices, VPN terminations) or by groups of users. Not every user with
tion 01 m AWS access should have permission to delete groups (least privilege).
Rule Details: AWS SetDefaultPolicyVersion
This search looks for AWS CloudTrail events where a user has set a default policy versions.
Attackers have been know to use this technique for Privilege Escalation in case the previous
versions of the policy had permissions to access more resources than the current version of the
policy.
Rule ID
aws_86

Query
{'selection2': {'eventName': 'SetDefaultPolicyVersion'}, 'selection3': {'eventSource'
: 'iam.amazonaws.com'}, 'condition': 'selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1078.004 
References
https://bishopfox.com/blog/privilege-escalation-in-aws 
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation-part-2/

Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021-03- mediu While this search has no known false positives, it is possible that an AWS admin has
legitimately set a default policy to allow a user to access all resources. That said, AWS strongly
tion 02 m
advises against granting full control to all AWS resources
Rule Details: AWS Create Policy Version to allow all resources
This search looks for AWS CloudTrail events where a user created a policy version that allows
them to access any resource in their account.
Rule ID
aws_87
Query
{'selection2': {'eventName': 'CreatePolicyVersion'}, 'selection3': {'eventSource': 'i
am.amazonaws.com'}, 'selection4': {'errorCode': 'success'}, 'condition': 'selection2
and selection3 and selection4'}
Log Source

Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1078.004 
References
https://bishopfox.com/blog/privilege-escalation-in-aws 
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation-part-2/

Severity
70
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2022-05- mediu While this search has no known false positives, it is possible that an AWS admin has
legitimately created a policy to allow a user to access all resources. That said, AWS strongly
tion 17 m advises against granting full control to all AWS resources and you must verify this activity.
Rule Details: AWS Credential Access GetPasswordData
This detection analytic identifies GetPasswordData API call made to your AWS account.
Attackers can retrieve the encrypted administrator password for a running Windows instance.
Rule ID
aws_88
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Get
PasswordData'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0006 , T1110.001 
References
https://stratus-red-team.cloud/attack-techniques/AWS/aws.credential-access.ec2-get-
password-data/ 
Severity
70
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022-08-10 medium Administrator tooling or automated scripts may make these calls
Rule Details: AWS Lambda UpdateFunctionCode
This analytic is designed to detect IAM users attempting to update/modify AWS lambda code via
the AWS CLI to gain persistence, further access into AWS environment and to facilitate planting
backdoors. In this instance, an attacker may upload malicious code/binary to a lambda function
which will be executed automatically when the function is triggered.
Rule ID
aws_89
Query
{'selection2': {'eventSource': 'lambda.amazonaws.com'}, 'selection3': {'eventName': '
UpdateFunctionCode*'}, 'selection4': {'errorCode': 'success'}, 'selection5': {'userId
entity_type': 'IAMUser'}, 'condition': 'selection2 and selection3 and selection4 and
selection5'}
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
aws.eventName
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2022-02- mediu While this search has no known false positives, it is possible that an AWS admin or an
authorized IAM user has updated the lambda function code legitimately.
tion 24 m
Rule Details: AWS ECR Container Scanning Findings
This search looks for AWS CloudTrail events from AWS Elastic Container Registry (ECR)
Service.
Rule ID
aws_90
Query
{'selection2': {'eventSource': 'ecr.amazonaws.com'}, 'selection3': {'eventName': 'Des
cribeImageScanFindings'}, 'condition': 'selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1204 
References
https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html 
Severity
10
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
production 2022-08-25 medium unknown
Rule Details: Modification of AWS S3 Access Control List
This search detects modification of Access Control List of an S3 Bucket.
Rule ID
aws_92
Query
{'selection2': {'eventSource': 's3.amazonaws.com'}, 'selection3': {'eventName': 'PutB
ucketAcl'}, 'condition': 'selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 
References
N/A
Severity
60
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021-07-19 medium Unknown
Rule Details: EBS Snapshot Created
A copy of an EBS volume has been created.
Rule ID
aws_96
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateSnapshots'}, 'selection3': {'eventName': 'BackupEBSVolume'}, 'condition': 'selecti

on1 and (selection2 or selection3)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1074 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS RDS Snapshot Created
A copy of an AWS RDS database has been created.
Rule ID
aws_97
Query
{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateDBSnapshot'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1074 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS ELB Security Group Modified
Identifies the modification of an ELB security group.
Rule ID
aws_98
Query
{'selection1': {'eventSource': 'elasticloadbalancing.amazonaws.com'}, 'selection2': {
'eventName': 'ApplySecurityGroupsToLoadBalancer'}, 'condition': 'selection1 and selec
tion2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A

Rule Details: Update SSL Certificate Created
A new SSL certificate has been created in your environment.
Rule ID
aws_99
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Upl
oadServerCertificate'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0042 , T1588 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Update SSL Certificate Deleted
A certificate used for establishing SSL connection in your environment has been deleted.
Rule ID
aws_100
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteServerCertificate'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0042 , T1588 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS RDS Security Group Modified
A RDS security group has been modified.
Rule ID
aws_103
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Aut
horizeDBSecurityGroupIngress'}, 'selection3': {'eventName': 'RevokeDBSecurityGroupIng
ress'}, 'selection4': {'eventName': 'AuthorizeDBSecurityGroupEgress'}, 'selection5':
{'eventName': 'RevokeDBSecurityGroupEgress'}, 'selection6': {'userAgent': 'cloudforma
tion.amazonaws.com'}, 'condition': 'selection1 and (selection2 or selection3 or selec
tion4 or selection5) and not selection6'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS VPC Network ACL Modified
The ACL for a VPC has been modified.
Rule ID
aws_104
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateACLEntry'}, 'selection3': {'eventName': 'DeleteACL'}, 'selection4': {'eventName':
'DeleteACLEntry'}, 'selection5': {'eventName': 'UpdateACLAssociation'}, 'selection6':
{'userAgent': 'cloudformation.amazonaws.com'}, 'condition': 'selection1 and (selecti
on2 or selection3 or selection4 or selection5) and not selection6'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
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

Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Update VPC Mirror created
A VPC mirror session has been created.
Rule ID
aws_107
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateTrafficMirrorSession'}, 'selection3': {'userIdentity_sessionContext_sessionIssuer_
userName': ''}, 'condition': 'selection1 and selection2 and not selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1119 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Update VPC Mirror deleted
A VPC mirror session has been deleted.
Rule ID
aws_108
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'eventName': 'Del
eteTrafficMirrorSession'}, 'selection3': {'eventName': 'DeleteTrafficMirrorTarget'},

'selection4': {'eventName': 'DeleteTrafficMirrorFilter'}, 'selection5': {'userIdentit
y_sessionContext_sessionIssuer_userName': ''}, 'condition': 'selection1 and (selectio
n2 or selection3 or selection4) and not selection5'}
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Root access key created
An access key was created for the root account.
Rule ID
aws_109
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'userIdent
ity_type': 'Root'}, 'selection3': {'eventName': 'CreateAccessKey'}, 'condition': 'sel
ection1 and selection2 and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1078 

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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: Federated user attempting to assume role
A federated user is attempting to assume a role. Federation users enable to manage access to
AWS accounts by adding and removing users from the corporate directory, such as Microsoft
Active Directory.
Rule ID
aws_110
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'errorMess
age': 'Roles may not be assumed by federated users'}, 'condition': 'selection1 and se
lection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1078 
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
Maturity Creation Date Risk Level False Positives
test 2022/01/05 medium N/A
Rule Details: AWS SAML Access by Provider User and Principal
This search provides specific SAML access from specific Service Provider, user and targeted
principal at AWS. It also provides specific information to detect abnormal access or potential
credential hijack or forgery, specially in federated environments using SAML protocol inside the
perimeter or cloud provider.
Rule ID
aws_111
Query
{'selection1': {'eventSource': 'sts.amazonaws.com'}, 'selection2': {'eventName': 'Ass
umeRoleWithSAML'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1078 
References
https://www.cisa.gov/uscert/ncas/alerts/aa21-008a 
https://www.splunk.com/en_us/blog/security/a-golden-saml-journey-solarwinds-
continued.html 
https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/wp-m-unc2452-2021-
000343-01.pdf 
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

Maturi Creation Risk False Positives
ty Date Level
produc 2021-01- mediu Attacks using a Golden SAML or SAML assertion hijacks or forgeries are very difficult to detect
as accessing cloud providers with these assertions looks exactly like normal access, however
tion 26 m
things such as source IP sourceIPAddress user, and principal targeted at receiving cloud
provider along with endpoint credential access and abuse detection searches can provide the
necessary context to detect these attacks.
Rule Details: AWS Defense Evasion PutBucketLifecycle
This analytic identifies `PutBucketLifecycle` events in CloudTrail logs where a user has created a
new lifecycle rule for an S3 bucket with a short expiration period.
Rule ID
aws_113
Query
{'selection1': {'eventSource': 's3.amazonaws.com'}, 'selection2': {'eventName': 'PutB
ucketLifecycle'}, 'selection3': {'userIdentity_type': 'IAMUser'}, 'selection4': {'err
orCode': 'success'}, 'condition': 'selection1 and selection2 and selection3 and selec
tion4'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.008 
References
https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-
lifecycle-rule/ 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2022-07- mediu While this search has no known false positives, it is possible that it is a legitimate admin
activity. Please consider filtering out these noisy events using userAgent, user_arn field
tion 25 m
names.

Rule Details: AWS Impair Security Services
This analytic looks for several delete specific API calls made to AWS Security Services like
CloudWatch, GuardDuty and Web Application Firewalls.
Rule ID
aws_116
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'selection2': {'eventName
': 'DeleteLogStream'}, 'selection3': {'eventName': 'DeleteDetector'}, 'selection4': {
'eventName': 'DeleteIPSet'}, 'selection5': {'eventName': 'DeleteWebACL'}, 'selection6
': {'eventName': 'DeleteRule'}, 'selection7': {'eventName': 'DeleteRuleGroup'}, 'sele
ction8': {'eventName': 'DeleteLoggingConfiguration'}, 'selection9': {'eventName': 'De
leteAlarms'}, 'condition': 'selection1 and (selection2 or selection3 or selection4 or
selection5 or selection6 or selection7 or selection8 or selection9)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.008 
References
https://docs.aws.amazon.com/cli/latest/reference/guardduty/index.html 
https://docs.aws.amazon.com/cli/latest/reference/waf/index.html 
https://www.elastic.co/guide/en/security/current/prebuilt-rules.html 
Severity
70
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2022-07-26 medium While this search has no known false positives, it is possible that it is a legitimate
admin activity.
n
Rule Details: AWS Console Login Failed During MFA Challenge

The following analytic identifies an authentication attempt event against an AWS Console that
fails during the Multi Factor Authentication challenge.
Rule ID
aws_117
Query
{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selection2': {'eventName': '
ConsoleLogin'}, 'selection3': {'errorMessage': 'Failed authentication'}, 'selection4'
: {'additionalEventData_MFAUsed': 'Yes'}, 'condition': 'selection1 and selection2 and
selection3 and selection4'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0042 , T1586 
References
https://aws.amazon.com/what-is/mfa/ 
Severity
80
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2022-10-03 medium Legitimate users may miss to reply the MFA challenge within the time window or deny
it by mistake.
n
Rule Details: KMS Keys Creation
This search provides detection of KMS Keys Creation.
Rule ID
aws_118
Query
{'selection1': {'eventSource': 'kms.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateKey'}, 'selection3': {'eventName': 'PutKeyPolicy'}, 'condition': 'selection1 and (

selection2 or selection3)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1486 
References
https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/ 
https://github.com/d1vious/git-wild-hunt 
https://www.youtube.com/watch?v=PgzNib37g0M 
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021-01-11 medium unknown
Rule Details: AWS CreateLoginProfile
This search looks for AWS CloudTrail events where a user A (victim A) creates a login profile.
Rule ID
aws_119
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateLoginProfile'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136.003 

References
https://bishopfox.com/blog/privilege-escalation-in-aws 
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation-part-2/

Severity
90
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
producti 2021-07- medium While this search has no known false positives, it is possible that an AWS admin has
legitimately created a login profile.
on 19
Rule Details: AWS CreateAccessKey
This search looks for AWS CloudTrail events where a user creates access keys.
Rule ID
aws_120
Query
{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2': {'eventName': 'Cre
ateAccessKey'}, 'selection3': {'userAgent': 'console.amazonaws.com'}, 'selection4': {
'errorCode': 'success'}, 'condition': 'selection1 and (selection2 and (not selection3
) and selection4)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136.003 
References
https://bishopfox.com/blog/privilege-escalation-in-aws 
https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation-part-2/


Severity
70
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022-03-03 medium Unknown
Rule Details: AWS Privilege Escalation via Group/Role/User Policy
Identifies the request for privilege escalation by modifying AWS Group/Role/User Policy
Rule ID
aws_200
Query
{'selection1': {'eventSource': 'cloudtrail.amazonaws.com', 'eventName': ['AttachGroup
Policy', 'PutGroupPolicy', 'AttachRolePolicy', 'PutRolePolicy', 'AttachUserPolicy', '
PutUserPolicy']}, 'selection2': {'requestParameters_policyArn': ['arn:aws:iam::aws:po
licy/AdministratorAccess', 'arn:aws:iam::aws:policy/AmazonSNSFullAccess', 'arn:aws:ia
m::aws:policy/AmazonEC2FullAccess', 'arn:aws:iam::aws:policy/AmazonS3FullAccess', 'ar
n:aws:iam::aws:policy/AmazonDynamoDBFullAccess', 'arn:aws:iam::aws:policy/AWSCodeComm
itPowerUser', 'arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser', 'arn:aws:ia
m::aws:policy/PowerUserAccess', 'arn:aws:iam::aws:policy/DatabaseAdministrator', 'arn
:aws:iam::aws:policy/NetworkAdministrator', 'arn:aws:iam::aws:policy/SystemAdministra
tor', 'arn:aws:iam::aws:policy/Billing']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1548 
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
Maturity Creation Date Risk Level False Positives
test 2023/06/22 high Valid changes to policy by authorized user/administrator
AWS Config Rule IDs
Rule Details: AWS High-Risk Ports Exposed to Internet
Identifies when a specified inbound (ingress) rule is added or adjusted for a VPC security group
in AWS EC2 that allows traffic from any IP address to common remote access ports.
Rule ID
aws_config_1
Query
{'selection1': {'configResourceType': 'AWS::EC2::SecurityGroup'}, 'selection2': {'ipP
ermissions_fromPort': [22, 3389, 389, 445], 'ipPermissions_ipRanges': ['0.0.0.0/0', '
::/0']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://www.linkedin.com/pulse/my-backdoors-your-aws-infrastructure-part-3-network-
micha%C5%82-brygidyn/ 
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
aws.configurationItem.configuration.ipPermissions.fromPort
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 medium N/A

Rule Details: Public Access in AWS S3 Bucket Policy
Detects S3 bucket policies that allow public access by granting permissions to all principals
(Principal: "*"). This configuration can result in unauthorized data exposure and potential data
breaches.
Rule ID
aws_config_2
Query
{'selection1': {'configResourceType': 'AWS::S3::Bucket'}, 'selection2': {'bucketPolic
y_statement_principle': '*', 'bucketPolicy_statement_effect': 'Allow', 'bucketPolicy_
statement_action': ['s3:GetObject']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 
References
N/A
Severity
70
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 high N/A
Rule Details: AWS IAM Policy with Wildcard Privileges
Detects IAM policies that grant excessive privileges using wildcard (*) in either the Action or
Resource fields. Policies with Action set to "*" or "*:*" grant full permissions to all AWS services
and operations. Policies with Resource set to "*" allow actions on all resources. This violates the
principle of least privilege and can lead to privilege escalation and unauthorized access to
sensitive resources.
Rule ID
aws_config_3
Query

{'selection1': {'configResourceType': 'AWS::IAM::Policy'}, 'selection2': {'policyVers
ionList|contains': ["'Resource': '*'", "'Action': '*'", "'Action': '*:*'"]}, 'conditi
on': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
N/A
Severity
70
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 high N/A
Rule Details: AWS Security Group Deletion Detected
Detects the deletion of AWS EC2 Security Groups. Unexpected deletion of Security Groups may
indicate misconfiguration, operational errors, or malicious activity aimed at disrupting network
security controls or creating gaps in security posture.
Rule ID
aws_config_4
Query
{'selection1': {'configResourceType': 'AWS::EC2::SecurityGroup'}, 'selection2': {'con
figurationItemStatus': 'ResourceDeleted'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References

N/A
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 medium N/A
Rule Details: AWS Default VPC Usage
Detects the use of AWS default VPCs. Default VPCs are automatically created by AWS in each
region and come with preconfigured network settings that may not align with security best
practices. They often have permissive default security groups, automatic public IP assignment,
and Internet gateway configurations that can lead to unintended exposure of resources.
Rule ID
aws_config_5
Query
{'selection1': {'configResourceType': 'AWS::EC2::VPC'}, 'selection2': {'configuration
_isDefault': True}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
25
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 low N/A

Rule Details: AWS S3 Bucket Missing Server-Side Encryption
Detects S3 buckets that lack server-side encryption (SSE) configuration. Without SSE enabled,
data stored in S3 buckets is vulnerable to unauthorized access if the bucket permissions are
misconfigured or if physical media is compromised.
Rule ID
aws_config_6
Query
{'selection1': {'configResourceType': 'AWS::S3::Bucket'}, 'selection2': {'serverSideE
ncryptionConfiguration': ''}, 'selection3': {'serverSideEncryptionConfiguration_sseAl
gorithm': ''}, 'condition': 'selection1 and (not selection2) and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 
References
N/A
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/12/17 medium N/A
Azure Rule IDs
Rule Details: Discovery Using AzureHound
Detects AzureHound (A BloodHound data collector for Microsoft Azure) activity via the default
User-Agent that is used during its operation after successful authentication.
Rule ID
azure_1
Query
{'selection': {'userAgent|contains': 'azurehound', 'login_result': 'success'}, 'condi
tion': 'selection'}

Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,35b781cc-1a08-4a5a-80af-42fd7c315c6b
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0007 , T1087.004 , T1526 
References
https://github.com/BloodHoundAD/AzureHound 
Severity
75
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/27 high Unknown
Rule Details: Sign-in Failure Due to Conditional Access Requirements Not Met
Define a baseline threshold for failed sign-ins due to Conditional Access failures
Rule ID
azure_3
Query
{'selection': {'ResultType': 53003}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,b4a6d707-9430-4f5f-af68-0337f52d5c42
Author: Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 
References
https://docs.microsoft.com/en-gb/azure/active-directory/fundamentals/security-
operations-privileged-accounts 

Severity
75
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/01 high Service Account misconfigured
Misconfigured Systems
Vulnerability Scanners
Rule Details: Multifactor Authentication Denied
User has indicated they haven't instigated the MFA prompt and could indicate an attacker has
the password for the account.
Rule ID
azure_4
Query
{'selection': {'status_additionalDetails|contains': 'MFA denied'}, 'condition': 'sele
ction'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,e40f4962-b02b-4192-9bfe-245f7ece1f99
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 
References
https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-
organizations-for-data-exfiltration-and-destruction/ 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/03/24 medium Users actually login but mis-click into the Deny button when MFA prompt.
Rule Details: Multifactor Authentication Interrupted
Identifies user login with multifactor authentication failures, which might be an indication an
attacker has the password for the account but can't pass the MFA challenge.
Rule ID
azure_5
Query
{'selection_50074': {'ResultType': 50074}, 'selection_500121': {'ResultType': 500121}
, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,5496ff55-42ec-4369-81cb-00f417029e25
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/10 medium Unknown
Rule Details: Account Lockout
Identifies user account which has been locked because the user tried to sign in too many times
with an incorrect user ID or password.
Rule ID
azure_6
Query

{'selection': {'ResultType': 50053}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,2b7d6fc0-71ac-4cf7-8ed1-b5788ee5257a
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0006 , T1110 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/10/10 medium Unknown
Rule Details: Use of Legacy Authentication Protocols
Alert on when legacy authentication has been used on an account.
Rule ID
azure_9
Query
{'selection': {'login_result': 'success', 'ClientApp': ['Other clients', 'IMAP', 'POP
3', 'MAPI', 'SMTP', 'Exchange ActiveSync', 'Exchange Web Services']}, 'filter': {'src
ip_username': ''}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,60f6535a-760f-42a9-be3f-c9a0a025906e
Author: Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0001 , T1078.004 , TA0006 , T1110 

References
https://docs.microsoft.com/en-gb/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
75
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/17 high User has been put in exception group so they can use legacy authentication
Rule Details: Suspicious Sign-ins From a Non-Registered Device
Detects risky authentication from a non AD registered device without MFA being required.
Rule ID
azure_10
Query
{'selection': {'ResultType': 0, 'RiskState': 'atRisk', 'DeviceDetail_trusttype': ''},
'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,572b12d4-9062-11ed-a1eb-0242ac120002
Author: Harjot Singh, '@cyb3rjy0t'
Tactics, Techniques, and Procedures
TA0001 , T1078 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#non-compliant-device-sign-in 
Severity
75
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2023/01/10 high Unknown
Rule Details: Device Registration or Join without MFA
Monitor and alert for device registration or join events where MFA was not performed.
Rule ID
azure_11
Query
{'selection': {'ResourceDisplayName': 'Device Registration Service', 'conditionalAcce
ssStatus': 'success'}, 'filter_mfa': {'status_additionalDetails|startswith': 'MFA'},
'condition': 'selection and not filter_mfa'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,5afa454e-030c-4ab4-9253-a90aa7fcc581
Author: Michael Epping, '@mepples21'
Tactics, Techniques, and Procedures
TA0001 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#device-registrations-and-joins-outside-policy 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 medium Unknown
Rule Details: Azure Unusual Authentication Interruption
Detects when there is an interruption in the authentication process.
Rule ID
azure_12
Query

{'selection_50097': {'ResultType': 50097}, 'selection_50155': {'ResultType': 50155},
'selection_50158': {'ResultType': 50158}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,8366030e-7216-476b-9927-271d79f13cf3
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0001 , T1078 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/26 medium Unknown
Rule Details: Login to Disabled Account
Detect failed attempts to sign in to disabled accounts.
Rule ID
azure_14
Query
{'selection': {'ResultType': 50057}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,908655e0-25cf-4ae1-b775-1c8ce9cf43d8
Author: AlertIQ
Tactics, Techniques, and Procedures
TA0001 , T1078.004 

References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
50
Suppression Logic Based On
srcip_username
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/10/10 medium Unknown
Rule Details: Application AppID Uri Configuration Changes
Detects when a configuration change is made to an application's AppID URI.
Rule ID
azure_16
Query
{'selection': {'properties_message': ['Update Application', 'Update Service principal
']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,1b45b0d1-773f-4f23-aedc-814b759563b1
Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 , TA0006 , T1552 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#appid-uri-added-modified-or-removed 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experime 2022/06/0 high When an administrator is making legitimate AppID URI configuration changes to an
application. This should be a planned event.
ntal 2
Rule Details: Added Credentials to Existing Application
Detects when a new credential is added to an existing application. Any additional credentials
added outside of expected processes could be a malicious actor using those credentials.
Rule ID
azure_18
Query
{'selection': {'properties_message': 'Update Service principal/Update Application'},
'selection2': {'properties_message|contains|all': ['Update Application', 'Certificate
s and secrets management']}, 'condition': 'selection or selection2'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,cbb67ecc-fb70-4467-9350-c910bdf7c628
Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
Tactics, Techniques, and Procedures
TA0003 , T1098.001 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#application-credentials 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimenta 2022/05/26 high When credentials are added/removed as part of the normal working
hours/workflows
l
Rule Details: App Granted Privileged Delegated or App Permissions

Detects when administrator grants either application permissions (app roles) or highly privileged
delegated permissions.
Rule ID
azure_21
Query
{'selection': {'properties_message': 'Add app role assignment to service principal'},
'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,5aecf3d5-f8a0-48e7-99be-3a759df7358f
Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#application-granted-highly-privileged-permissions 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/07/28 high When the permission is legitimately needed for the app
Rule Details: Added Owner to Application
Detects when a new owner is added to an application. This gives that account privileges to make
modifications and configuration changes to the application.
Rule ID
azure_23
Query
{'selection': {'properties_message': 'Add owner to application'}, 'condition': 'selec
tion'}
Log Source

Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,74298991-9fc4-460e-a92e-511aa60baec1
Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#new-owner 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/02 medium When a new application owner is added by an administrator
Rule Details: App Role Added
Detects when an app is assigned Microsoft Entra roles, such as global administrator, or Microsoft
Entra RBAC roles, such as subscription owner.
Rule ID
azure_24
Query
{'selection': {'properties_message': ['Add member to role', 'Add eligible member to r
ole', 'Add scoped member to role']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,b04934b2-0a68-4845-8a19-bdfed3a68a7a
Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References

https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-applications#service-principal-assigned-to-a-role 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/07/19 medium When the permission is legitimately needed for the app
Rule Details: BitLocker Key Retrieval
Monitor and alert for BitLocker key retrieval.
Rule ID
azure_25
Query
{'selection': {'Category': 'KeyManagement', 'OperationName': 'Read BitLocker key'}, '
condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,a0413867-daf3-43dd-9245-734b3a787942
Author: Michael Epping, '@mepples21'
Tactics, Techniques, and Procedures
TA0006 , T1555 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#bitlocker-key-retrieval 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 medium Unknown
Rule Details: Changes to Device Registration Policy
Monitor and alert for changes to the device registration policy.
Rule ID
azure_27
Query
{'selection': {'Category': 'Policy', 'ActivityDisplayName': 'Set device registration
policies'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,9494bff8-959f-4440-bbce-fb87a208d517
Author: Michael Epping, '@mepples21'
Tactics, Techniques, and Procedures
TA0005 , T1484 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-devices#device-registrations-and-joins-outside-policy 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 high Unknown
Rule Details: New CA Policy by Non-Approved Actor
Monitor and alert on conditional access changes.
Rule ID
azure_28
Query

{'selection': {'properties_message': 'Add conditional access policy'}, 'condition': '
selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,0922467f-db53-4348-b7bf-dee8d0d348c6
Author: Corissa Koopmans, '@corissalea'
Tactics, Techniques, and Procedures
TA0005 , T1556 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/07/18 medium Misconfigured role permissions
tal Verify whether the user identity, user agent, and/or hostname should be making
changes in your environment.
Rule Details: CA Policy Updated by Non-Approved Actor
Monitor and alert on conditional access changes. Is Initiated by (actor) approved to make
changes? Review Modified Properties and compare "old" vs "new" value.
Rule ID
azure_29
Query
{'keywords': {'properties_message': 'Update conditional access policy'}, 'condition':
'keywords'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,50a3c7aa-ec29-44a4-92c1-fce229eef6fc

Author: Corissa Koopmans, '@corissalea'
Tactics, Techniques, and Procedures
TA0005 , T1548 , T1556 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2022/07/19 medium Misconfigured role permissions
tal Verify whether the user identity, user agent, and/or hostname should be making
changes in your environment.
Rule Details: User Added to Group with CA Policy Modification Access
Monitor and alert on group membership additions of groups that have CA policy modification
access.
Rule ID
azure_30
Query
{'selection': {'properties_message': 'Add member from group'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,91c95675-1f27-46d0-bead-d1ae96b97cd3
Author: Mark Morowczynski '@markmorow', Thomas Detzner '@tdetzner'
Tactics, Techniques, and Procedures
TA0005 , T1548 , T1556 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 

Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/04 medium User removed from the group is approved
Rule Details: CA Policy Removed by Non-Approved Actor
Monitor and alert on conditional access changes where non approved actor removed CA Policy.
Rule ID
azure_31
Query
{'selection': {'properties_message': 'Delete conditional access policy'}, 'condition'
: 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,26e7c5e2-6545-481e-b7e6-050143459635
Author: Corissa Koopmans, '@corissalea'
Tactics, Techniques, and Procedures
TA0005 , T1548 , T1556 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-infrastructure#conditional-access 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experimen 2022/07/19 medium Misconfigured role permissions
tal Verify whether the user identity, user agent, and/or hostname should be making
changes in your environment.
Rule Details: Password Reset by User Account
Detect when a user has reset their password in Microsoft Entra ID
Rule ID
azure_34
Query
{'selection': {'Category': 'UserManagement', 'Result': 'Success', 'ActivityDisplayNam
e|contains': 'Password reset'}, 'self_service_activity': {'ActivityDisplayName|contai
ns': 'flow activity progress'}, 'self_service_reason': {'ResultReason': 'User success
fully reset password'}, 'filter': {'initiatedBy_user_userPrincipalName': ''}, 'condit
ion': 'selection and not filter and (not self_service_activity or self_service_reason
)'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,340ee172-4b67-4fb4-832f-f961bdc1f3aa
Author: YochanaHenderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts 
Severity
30
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/03 medium If this was approved by System Administrator or confirmed user action.
Rule Details: Azure Subscription Permission Elevation via AuditLogs

Detects when a user has been elevated to manage all Azure Subscriptions. This change should
be investigated immediately if it isn't planned. This setting could allow an attacker access to
Azure subscriptions in your environment.
Rule ID
azure_35
Query
{'selection': {'Category': 'Administrative', 'OperationName': 'Assigns the caller to
user access admin'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,ca9bf243-465e-494a-9e54-bf9fc239057d
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1078 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#assignment-and-elevation 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/26 high If this was approved by System Administrator.
Rule Details: Temporary Access Pass Added to an Account
Detects when a temporary access pass (TAP) is added to an account. TAPs added to privileged
accounts should be investigated.
Rule ID
azure_36
Query
{'selection': {'ResultReason': 'Admin registered temporary access pass method for use
r', 'properties_message': 'Admin registered security info'}, 'condition': 'selection'

}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,fa84aaf5-8142-43cd-9ec2-78cfebf878ce
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#changes-to-privileged-accounts 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/10 high Administrator adding a legitimate temporary access pass
Rule Details: Privileged Account Creation
Detects when a new admin is created.
Rule ID
azure_37
Query
{'selection': {'Result': 'Success', 'properties_message|contains|all': ['Add user', '
Add member to role']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,f7b5b004-dece-46e4-a4a5-f6fd0e1c6947
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H', Tim Shelton
Tactics, Techniques, and Procedures
TA0003 , T1078.004 

References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#changes-to-privileged-accounts 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/11 medium A legitimate new admin account being created
Rule Details: Guest User Invited by Non-Approved Inviters
Detects when a user that doesn't have permissions to invite a guest user attempts to invite one.
Rule ID
azure_38
Query
{'selection': {'Result': 'failure', 'properties_message': 'Invite external user'}, 'c
ondition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,0b4b72e3-4c53-4d5b-b198-2c58cfef39a9
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0003 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-accounts#things-to-monitor 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/10 medium A non malicious user is unaware of the proper process
Rule Details: Bulk Deletion Changes to Privileged Account Permissions
Detects when a user is removed from a privileged role. Bulk changes should be investigated.
Rule ID
azure_39
Query
{'selection': {'properties_message': ['Remove eligible member (permanent)', 'Remove e
ligible member (eligible)']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,102e11e3-2db5-4c9e-bc26-357d42585d21
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/05 high Legitimate administrator actions of removing members from a role
Rule Details: PIM Approvals and Deny Elevation
Detects when a PIM elevation is approved or denied. Outside of normal operations should be
investigated.
Rule ID
azure_40

Query
{'selection': {'properties_message': 'Request Approved/Denied'}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,039a7469-0296-4450-84c0-f6966b16dc6d
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/09 high Actual admin using PIM.
Rule Details: Changes to PIM Settings
Detects when changes are made to PIM roles.
Rule ID
azure_41
Query
{'selection': {'properties_message': 'Update role setting in PIM'}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,db6c06c4-bf3b-421c-aa88-15672b88c743
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'

Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/09 high Legit administrative PIM setting configuration changes
Rule Details: User Added to Privilege Role
Detects when a user is added to a privileged role.
Rule ID
azure_42
Query
{'selection': {'properties_message': ['Add eligible member (permanent)', 'Add eligibl
e member (eligible)']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,49a268a4-72f4-4e38-8a7b-885be690c5b5
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 
Severity
75
Suppression Logic Based On

azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/06 high Legitimate administrator actions of adding members from a role
Rule Details: PIM Alert Setting Changes to Disabled
Detects when PIM alerts are set to disabled.
Rule ID
azure_43
Query
{'selection': {'properties_message': 'Disable PIM Alert'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,aeaef14c-e5bf-4690-a9c8-835caad458bd
Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
Tactics, Techniques, and Procedures
TA0004 , T1078 
References
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/security-
operations-privileged-identity-management#azure-ad-roles-assignment 
Severity
75
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/09 high Administrator disabling PIM alerts as an active choice.
Rule Details: Azure Domain Federation Settings Modified
Identifies when a user or application modified the federation settings on the domain.
Rule ID

azure_45
Query
{'selection': {'ActivityDisplayName': 'Set federation settings on domain'}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,352a54e1-74ba-4929-9d47-8193d67aba1e
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0005 , T1484 
References
https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-monitor-
federation-changes 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2021/09/ mediu Federation Settings being modified or deleted may be performed by a system administrator.
ental 06 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Federation Settings modified from unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Pods Deleted
Identifies the deletion of Azure Kubernetes Pods.
Rule ID
azure_46
Query
{'selection': {'operationName': 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/PODS/DELETE'}
, 'condition': 'selection'}
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
rules/blob/065bf48a9987cd8bd826c098a30ce36e6868ee46/rules/integrations/azure/im
pact_kubernetes_pod_deleted.toml 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/07/ mediu Pods may be deleted by a system administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your environment.
24 m
Pods deletions from unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Device No Longer Managed or Compliant
Identifies when a device in Azure is no longer managed or compliant.
Rule ID
azure_47
Query
{'selection': {'properties_message': ['Device no longer compliant', 'Device no longer
managed']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,542b9912-c01f-4e3f-89a8-014c48cdca7d

Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1498 
References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#core-directory 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/03 medium Administrator may have forgotten to review the device.
Rule Details: Number Of Resource Creation Or Deployment Activities
Number of VM creations or deployment activities occur in Azure via Azure Activity Log.
Rule ID
azure_48
Query
{'selection': {'OperationNameValue': ['Microsoft.Compute/virtualMachines/write', 'Mic
rosoft.Resources/deployments/write']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,d2d901db-7a75-45a1-bc39-0cbf00812192
Author: sawwinnnaung
Tactics, Techniques, and Procedures
TA0040 , T1496 
References
https://github.com/Azure/Azure-
Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActivity/
Creating_Anomalous_Number_Of_Resources_detection.yaml 
Severity

50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/07 medium Valid change
Rule Details: Azure VPN Connection Modified or Deleted
Identifies when a VPN connection is modified or deleted.
Rule ID
azure_49
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/VPNGATEWAYS/VPNCONNECTIONS/WRITE'
, 'MICROSOFT.NETWORK/VPNGATEWAYS/VPNCONNECTIONS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,61171ffc-d79c-4ae5-8e10-9323dba19cd3
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1498 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu VPN Connection being modified or deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
08 m
environment.
VPN Connection modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Firewall Rule Configuration Modified or Deleted
Identifies when a Firewall Rule Configuration is Modified or Deleted.
Rule ID
azure_50
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/FIREWALLPOLICIES/RULECOLLECTIONGR
OUPS/WRITE', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/RULECOLLECTIONGROUPS/DELETE', 'MICRO
SOFT.NETWORK/FIREWALLPOLICIES/RULEGROUPS/WRITE', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/
RULEGROUPS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,2a7d64cf-81fa-4daf-ab1b-ab80b789c067
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Firewall Rule Configuration being modified or deleted may be performed by a system
administrator. Verify whether the user identity, user agent, and/or hostname should be making
08 m
changes in your environment.
Firewall Rule Configuration modified or deleted from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Application Credential Modified
Identifies when an application credential is modified.
Rule ID
azure_51
Query
{'selection': {'properties_message': 'Update application -
Certificates and secrets management'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,cdeef967-f9a1-4375-90ee-6978c5f23974
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://www.cloud-architekt.net/auditing-of-msi-and-service-principals/ 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/09/ mediu Application credential addition may be performed by a system administrator.
02 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Application credential added from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Disabled MFA to Bypass Authentication Mechanisms

Detection for when multi-factor authentication has been disabled, which might indicate a
malicious activity to bypass authentication mechanisms.
Rule ID
azure_52
Query
{'selection': {'properties_message': 'Disable Strong Authentication', 'result': 'succ
ess'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,7ea78478-a4f9-42a6-9dcd-f861816122bf
Author: @ionsor
Tactics, Techniques, and Procedures
TA0005 , T1556.006 
References
https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-
userstates 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/08 medium Authorized modification by administrators
Rule Details: Azure Kubernetes Cluster Created or Deleted
Detects when a Azure Kubernetes Cluster is created or deleted.
Rule ID
azure_54
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/WRITE', 'MIC
ROSOFT.KUBERNETES/CONNECTEDCLUSTERS/DELETE']}, 'condition': 'selection'}
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ low Kubernetes cluster being created or deleted may be performed by a system administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
07
your environment.
Kubernetes cluster created or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Active Directory Hybrid Health AD FS New Server
This detection uses Azure Activity Log (Administrative category) to identify the creation or update
of a server instance in a Microsoft Entra Hybrid health AD FS service. A threat actor can create a
new Health AD FS service and create a fake server instance to spoof AD FS signing logs. There
is no need to compromise an on-prem AD FS server. This can be done programmatically via
HTTP requests to Azure.
Rule ID
azure_55
Query

{'selection': {'CategoryValue': 'Administrative', 'ResourceId|contains': 'AdFederatio
nService', 'OperationNameValue': 'Microsoft.ADHybridHealthService/services/servicemem
bers/action'}, 'condition': 'selection'}
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
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/26 medium Legitimate AD FS servers added to an AAD Health AD FS service instance
Rule Details: Azure New CloudShell Created
Identifies when a new cloudshell is created inside of Azure portal.
Rule ID
azure_56
Query
{'selection': {'operationName': 'MICROSOFT.PORTAL/CONSOLES/WRITE'}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,72af37e2-ec32-47dc-992b-bc288a2708cb
Author: Austin Songer
Tactics, Techniques, and Procedures

TA0002 , T1059 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/21 medium A new cloudshell may be created by a system administrator.
Rule Details: Azure Owner Removed from Application or Service Principal
Identifies when an owner was removed from an application or service principal in Azure.
Rule ID
azure_57
Query
{'selection': {'properties_message': ['Remove owner from service principal', 'Remove
owner from application']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,636e30d5-3736-42ea-96b1-e6e2f8429fd6
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#application-proxy 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId

stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/09/0 medium Owner being removed may be performed by a system administrator.
3 Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Owner removed from unfamiliar users should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Events Deleted
Detects when Events are deleted in Azure Kubernetes. An adversary may delete events in Azure
Kubernetes in an attempt to evade detection.
Rule ID
azure_58
Query
{'selection': {'operationName': 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/EVENTS.K8S.IO
/EVENTS/DELETE'}, 'condition': 'selection'}
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
rules/blob/da3852b681cf1a33898b1535892eab1f3a76177a/rules/integrations/azure/def
ense_evasion_kubernetes_events_deleted.toml 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/07/ mediu Event deletions may be done by a system or network administrator. Verify whether the
username, hostname, and/or resource name should be making changes in your environment.
24 m
Events deletions from unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Service Account Modified or Deleted
Identifies when a service account is modified or deleted.
Rule ID
azure_59
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/SERVICEACCOU
NTS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/SERVICEACCOUNTS/DELETE', 'MICROSO
FT.KUBERNETES/CONNECTEDCLUSTERS/SERVICEACCOUNTS/IMPERSONATE/ACTION']}, 'condition': '
selection'}
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Service account being modified or deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
07 m environment.
Service account modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Keyvault Key Modified or Deleted
Identifies when a Keyvault Key is modified or deleted in Azure.
Rule ID
azure_60
Query
{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/KEYS/UPDATE/ACTION', 'MIC
ROSOFT.KEYVAULT/VAULTS/KEYS/CREATE', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/CREATE/ACTION',
'MICROSOFT.KEYVAULT/VAULTS/KEYS/IMPORT/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/RECOV
ER/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/RESTORE/ACTION', 'MICROSOFT.KEYVAULT/VAUL
TS/KEYS/DELETE', 'MICROSOFT.KEYVAULT/VAULTS/KEYS/BACKUP/ACTION', 'MICROSOFT.KEYVAULT/
VAULTS/KEYS/PURGE/ACTION']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,80eeab92-0979-4152-942d-96749e11df40
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0006 , T1555.006 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matur Creation Risk False Positives
ity Date Level
test 2021/08/ mediu Key being modified or deleted may be performed by a system administrator.
16 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Key modified or deleted from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Network Policy Change
Identifies when a Azure Kubernetes network policy is modified or deleted.
Rule ID
azure_61
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/NETWORKING.K
8S.IO/NETWORKPOLICIES/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/NETWORKING.K8S.
IO/NETWORKPOLICIES/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/EXTENSIONS/NETWOR
KPOLICIES/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/EXTENSIONS/NETWORKPOLICIES/
DELETE']}, 'condition': 'selection'}
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Network Policy being modified and deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
07 m
environment.
Network Policy being modified and deleted from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes CronJob
Identifies when a Azure Kubernetes CronJob runs in Azure Cloud. Kubernetes Job is a controller
that creates one or more pods and ensures that a specified number of them successfully
terminate. Kubernetes Job can be used to run containers that perform finite tasks for batch jobs.
Kubernetes CronJob is used to schedule Jobs. An Adversary may use Kubernetes CronJob for
scheduling execution of malicious code that would run as a container in the cluster.
Rule ID
azure_62
Query
{'selection': {'operationName|startswith': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/B
ATCH', 'MICROSOFT.CONTAINERSERVICE/MANAGEDCLUSTERS/BATCH'], 'operationName|endswith':
['/CRONJOBS/WRITE', '/JOBS/WRITE']}, 'condition': 'selection'}
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
Maturity Creation Date Risk Level False Positives
test 2021/11/22 medium Azure Kubernetes CronJob/Job may be done by a system administrator.
If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Firewall Rule Collection Modified or Deleted
Identifies when Rule Collections (Application, NAT, and Network) is being modified or deleted.
Rule ID
azure_63
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/AZUREFIREWALLS/APPLICATIONRULECOL
LECTIONS/WRITE', 'MICROSOFT.NETWORK/AZUREFIREWALLS/APPLICATIONRULECOLLECTIONS/DELETE'
, 'MICROSOFT.NETWORK/AZUREFIREWALLS/NATRULECOLLECTIONS/WRITE', 'MICROSOFT.NETWORK/AZU
REFIREWALLS/NATRULECOLLECTIONS/DELETE', 'MICROSOFT.NETWORK/AZUREFIREWALLS/NETWORKRULE
COLLECTIONS/WRITE', 'MICROSOFT.NETWORK/AZUREFIREWALLS/NETWORKRULECOLLECTIONS/DELETE']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,025c9fe7-db72-49f9-af0d-31341dd7dd57
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Rule Collections (Application, NAT, and Network) being modified or deleted may be performed
by a system administrator. Verify whether the user identity, user agent, and/or hostname should
08 m
be making changes in your environment.
Rule Collections (Application, NAT, and Network) modified or deleted from unfamiliar users
should be investigated. If known behavior is causing false positives, it can be exempted from
the rule.
Rule Details: Azure Application Security Group Modified or Deleted
Identifies when a application security group is modified or deleted.
Rule ID
azure_64
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/APPLICATIONSECURITYGROUPS/WRITE',
'MICROSOFT.NETWORK/APPLICATIONSECURITYGROUPS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,835747f1-9329-40b5-9cc3-97d465754ce6
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Application security group being modified or deleted may be performed by a system
administrator.
16 m
Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Application security group modified or deleted from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.

Rule Details: Azure Container Registry Modified or Deleted
Detects when a Container Registry is created, updated, or deleted.
Rule ID
azure_65
Query
{'selection': {'operationName': ['MICROSOFT.CONTAINERREGISTRY/REGISTRIES/WRITE', 'MIC
ROSOFT.CONTAINERREGISTRY/REGISTRIES/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,93e0ef48-37c8-49ed-a02c-038aab23628e
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ low Container Registry being created, updated, or deleted may be performed by a system
administrator. Verify whether the user identity, user agent, and/or hostname should be making
07
changes in your environment.
Container Registry created, updated, or deleted from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.

Rule Details: Azure Suppression Rule Created
Identifies when a suppression rule is created in Azure. Adversary's could attempt this to evade
detection.
Rule ID
azure_66
Query
{'selection': {'operationName': 'MICROSOFT.SECURITY/ALERTSSUPPRESSIONRULES/WRITE'}, '
condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,92cc3e5d-eb57-419d-8c16-5c63f325a401
Author: Austin Songer
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/08/ mediu Suppression Rule being created may be performed by a system administrator.
16 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Suppression Rule created from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Firewall Modified or Deleted
Identifies when a firewall is created, modified, or deleted.
Rule ID
azure_67

Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/AZUREFIREWALLS/WRITE', 'MICROSOFT
.NETWORK/AZUREFIREWALLS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,512cf937-ea9b-4332-939c-4c2c94baadcd
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Firewall being modified or deleted may be performed by a system administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
08 m
Firewall modified or deleted from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Secret or Config Object Access
Identifies when a Kubernetes account access a sensitive objects such as configmaps or secrets.
Rule ID
azure_68
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/CONFIGMAPS/W
RITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/CONFIGMAPS/DELETE', 'MICROSOFT.KUBERNE
TES/CONNECTEDCLUSTERS/SECRETS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/SECRETS
/DELETE']}, 'condition': 'selection'}
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Sensitive objects may be accessed by a system administrator. Verify whether the user identity,
user agent, and/or hostname should be making changes in your environment. Sensitive objects
07 m accessed from unfamiliar users should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.
Rule Details: Azure Key Vault Modified or Deleted
Identifies when a key vault is modified or deleted.
Rule ID
azure_69
Query
{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/WRITE', 'MICROSOFT.KEYVAU
LT/VAULTS/DELETE', 'MICROSOFT.KEYVAULT/VAULTS/DEPLOY/ACTION', 'MICROSOFT.KEYVAULT/VAU
LTS/ACCESSPOLICIES/WRITE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.

Rule Source
SigmaHQ,459a2970-bb84-4e6a-a32e-ff0fbd99448d
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0006 , T1555.006 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Key Vault being modified or deleted may be performed by a system administrator.
16 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Key Vault modified or deleted from unfamiliar users should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.
Rule Details: Azure Device or Configuration Deleted
Identifies when a device or device configuration in Azure is deleted.
Rule ID
azure_70
Query
{'selection': {'properties_message': ['Delete device', 'Delete device configuration']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,46530378-f9db-4af9-a9e5-889c177d3881
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1498 

References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#core-directory 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/09/ mediu Device or device configuration being modified or deleted may be performed by a system
administrator.
03 m
Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Device or device configuration modified or deleted from unfamiliar users should be investigated.
If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Subscription Permission Elevation Via ActivityLogs
Detects when a user has been elevated to manage all Azure Subscriptions. This change should
be investigated immediately if it isn't planned. This setting could allow an attacker access to
Azure subscriptions in your environment.
Rule ID
azure_71
Query
{'selection': {'operationName': 'MICROSOFT.AUTHORIZATION/ELEVATEACCESS/ACTION'}, 'con
dition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,09438caa-07b1-4870-8405-1dbafe3dad95
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1098.003 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftauthorization 
Severity

75
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/26 high If this was approved by System Administrator.
Rule Details: Azure Active Directory Hybrid Health AD FS Service Delete
This detection uses Azure Activity Log (Administrative category) to identify the deletion of a
Microsoft Entra Hybrid health AD FS service instance in a tenant. A threat actor can create a new
Health AD FS service and create a fake server to spoof AD FS signing logs. The health AD FS
service can then be deleted after it is not longer needed via HTTP requests to Azure.
Rule ID
azure_72
Query
{'selection': {'CategoryValue': 'Administrative', 'ResourceId|contains': 'AdFederatio
nService', 'OperationNameValue': 'Microsoft.ADHybridHealthService/services/delete'},
'condition': 'selection'}
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
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/08/26 medium Legitimate AAD Health AD FS service instances being deleted in a tenant
Rule Details: Azure DNS Zone Modified or Deleted
Identifies when DNS zone is modified or deleted.
Rule ID
azure_73
Query
{'selection': {'operationName|startswith': 'MICROSOFT.NETWORK/DNSZONES', 'operationNa
me|endswith': ['/WRITE', '/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,af6925b0-8826-47f1-9324-337507a0babd
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0011 , T1071.004 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations#microsoftkubernetes 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu DNS zone modified and deleted may be performed by a system administrator. Verify whether
the user identity, user agent, and/or hostname should be making changes in your environment.
08 m
DNS zone modification from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Service Principal Created
Identifies when a service principal is created in Azure.
Rule ID

azure_74
Query
{'selection': {'properties_message': 'Add service principal'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,0ddcff6d-d262-40b0-804b-80eb592de8e3
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1578 
References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#application-proxy 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/09/ mediu Service principal being created may be performed by a system administrator.
02 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Service principal created from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Service Principal Removed
Identifies when a service principal was removed in Azure.
Rule ID
azure_75
Query
{'selection': {'properties_message': 'Remove service principal'}, 'condition': 'selec
tion'}
Log Source

Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,448fd1ea-2116-4c62-9cde-a92d120e0f08
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1578.003 
References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#application-proxy 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/09/ mediu Service principal being removed may be performed by a system administrator.
03 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Service principal removed from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes Sensitive Role Access
Identifies when ClusterRoles/Roles are being modified or deleted.
Rule ID
azure_76
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORI
ZATION.K8S.IO/ROLES/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATIO
N.K8S.IO/ROLES/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATION.K8
S.IO/ROLES/BIND/ACTION', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZATION.K
8S.IO/ROLES/ESCALATE/ACTION', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZAT
ION.K8S.IO/CLUSTERROLES/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORIZ
ATION.K8S.IO/CLUSTERROLES/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHO
RIZATION.K8S.IO/CLUSTERROLES/BIND/ACTION', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RB
AC.AUTHORIZATION.K8S.IO/CLUSTERROLES/ESCALATE/ACTION']}, 'condition': 'selection'}
Log Source

Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,818fee0c-e0ec-4e45-824e-83e4817b0887
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1078 
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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu ClusterRoles/Roles being modified and deleted may be performed by a system administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
07 m
your environment.
ClusterRoles/Roles modification from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Point-to-site VPN Modified or Deleted
Identifies when a Point-to-site VPN is Modified or Deleted.
Rule ID
azure_77
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/P2SVPNGATEWAYS/WRITE', 'MICROSOFT
.NETWORK/P2SVPNGATEWAYS/DELETE', 'MICROSOFT.NETWORK/P2SVPNGATEWAYS/RESET/ACTION', 'MI
CROSOFT.NETWORK/P2SVPNGATEWAYS/GENERATEVPNPROFILE/ACTION', 'MICROSOFT.NETWORK/P2SVPNG

ATEWAYS/DISCONNECTP2SVPNCONNECTIONS/ACTION', 'MICROSOFT.NETWORK/P2SVPNGATEWAYS/PROVID
ERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,d9557b75-267b-4b43-922f-a775e2d1f792
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1498 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Point-to-site VPN being modified or deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
08 m
environment.
Point-to-site VPN modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Application Gateway Modified or Deleted
Identifies when a application gateway is modified or deleted.
Rule ID
azure_78
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/APPLICATIONGATEWAYS/WRITE', 'MICR
OSOFT.NETWORK/APPLICATIONGATEWAYS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,ad87d14e-7599-4633-ba81-aeb60cfe8cd6

Author: Austin Songer
Tactics, Techniques, and Procedures
TA0003 , T1133 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Application gateway being modified or deleted may be performed by a system administrator.
16 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Application gateway modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Kubernetes RoleBinding/ClusterRoleBinding Modified and Deleted
Detects the creation or patching of potential malicious RoleBinding/ClusterRoleBinding.
Rule ID
azure_79
Query
{'selection': {'operationName': ['MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBAC.AUTHORI
ZATION.K8S.IO/CLUSTERROLEBINDINGS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/RBA
C.AUTHORIZATION.K8S.IO/CLUSTERROLEBINDINGS/DELETE', 'MICROSOFT.KUBERNETES/CONNECTEDCL
USTERS/RBAC.AUTHORIZATION.K8S.IO/ROLEBINDINGS/WRITE', 'MICROSOFT.KUBERNETES/CONNECTED
CLUSTERS/RBAC.AUTHORIZATION.K8S.IO/ROLEBINDINGS/DELETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,25cb259b-bbdc-4b87-98b7-90d7c72f8743
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0004 , T1078 

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
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu RoleBinding/ClusterRoleBinding being modified and deleted may be performed by a system
administrator. Verify whether the user identity, user agent, and/or hostname should be making
07 m changes in your environment.
RoleBinding/ClusterRoleBinding modification from unfamiliar users should be investigated. If
known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Application Deleted
Identifies when an application is deleted in Azure.
Rule ID
azure_80
Query
{'selection': {'properties_message': ['Delete application', 'Hard Delete application'
]}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,410d2a41-1e6d-452f-85e5-abdd8257a823
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1489 

References
https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-
audit-activities#application-proxy 
Severity
50
Suppression Logic Based On
azure_ad.initiatedBy.user.id
azure_ad.initiatedBy.app.servicePrincipalId
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/09/0 mediu Application being deleted may be performed by a system administrator.
3 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Application deleted from unfamiliar users should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Rule Details: Granting Of Permissions To An Account
Identifies IPs from which users grant access to other users on azure resources and alerts when a
previously unseen source IP address is used.
Rule ID
azure_82
Query
{'selection': {'OperationNameValue': ['Microsoft.Authorization/roleAssignments/write'
]}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,a622fcd2-4b5a-436a-b8a2-a4171161833c
Author: sawwinnnaung
Tactics, Techniques, and Procedures
TA0004 , T1098.003 
References
https://github.com/Azure/Azure-
Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActivity/
Granting_Permissions_To_Account_detection.yaml 
Severity

50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/07 medium Valid change
Rule Details: Azure Network Security Configuration Modified or Deleted
Identifies when a network security configuration is modified or deleted.
Rule ID
azure_84
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/WRITE', 'MI
CROSOFT.NETWORK/NETWORKSECURITYGROUPS/DELETE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROU
PS/SECURITYRULES/WRITE', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/DELET
E', 'MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/JOIN/ACTION', 'MICROSOFT.NETWORK/NETWORK
SECURITYGROUPS/PROVIDERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE']}, 'condition':
'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,d22b4df4-5a67-4859-a578-8c9a0b5af9df
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Network Security Configuration being modified or deleted may be performed by a system
administrator. Verify whether the user identity, user agent, and/or hostname should be making
08 m
changes in your environment.
Network Security Configuration modified or deleted from unfamiliar users should be
investigated. If known behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Network Firewall Policy Modified or Deleted
Identifies when a Firewall Policy is Modified or Deleted.
Rule ID
azure_85
Query
{'selection': {'operationName': ['MICROSOFT.NETWORK/FIREWALLPOLICIES/WRITE', 'MICROSO
FT.NETWORK/FIREWALLPOLICIES/JOIN/ACTION', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/CERTIFI
CATES/ACTION', 'MICROSOFT.NETWORK/FIREWALLPOLICIES/DELETE']}, 'condition': 'selection
'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,83c17918-746e-4bd9-920b-8e098bf88c23
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information

Matu Creation Risk False Positives
rity Date Level
test 2021/09/ mediu Firewall Policy being modified or deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
02 m
environment.
Firewall Policy modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: Azure Virtual Network Modified or Deleted
Identifies when a Virtual Network is modified or deleted in Azure.
Rule ID
azure_86
Query
{'selection': {'operationName|startswith': ['MICROSOFT.NETWORK/VIRTUALNETWORKGATEWAYS
/', 'MICROSOFT.NETWORK/VIRTUALNETWORKS/'], 'operationName|endswith': ['/WRITE', '/DEL
ETE']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,bcfcc962-0e4a-4fd9-84bb-a833e672df3f
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0040 , T1498 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2021/08/ mediu Virtual Network being modified or deleted may be performed by a system administrator. Verify
whether the user identity, user agent, and/or hostname should be making changes in your
08 m
environment.
Virtual Network modified or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.

Rule Details: Azure Keyvault Secrets Modified or Deleted
Identifies when secrets are modified or deleted in Azure.
Rule ID
azure_87
Query
{'selection': {'operationName': ['MICROSOFT.KEYVAULT/VAULTS/SECRETS/WRITE', 'MICROSOF
T.KEYVAULT/VAULTS/SECRETS/DELETE', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/BACKUP/ACTION',
'MICROSOFT.KEYVAULT/VAULTS/SECRETS/PURGE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS
/UPDATE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/RECOVER/ACTION', 'MICROSOFT.KEYVA
ULT/VAULTS/SECRETS/RESTORE/ACTION', 'MICROSOFT.KEYVAULT/VAULTS/SECRETS/SETSECRET/ACTI
ON']}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft Entra Events configured.
Rule Source
SigmaHQ,b831353c-1971-477b-abb6-2828edc3bca1
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0006 , T1555.006 
References
https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-
operations 
Severity
50
Suppression Logic Based On
azure_activity_log.resourceId
azure_activity_log.operationName
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2021/08/ mediu Secrets being modified or deleted may be performed by a system administrator.
16 m Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment.
Secrets modified or deleted from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule.
certutil.exe Rule IDs
Rule Details: certutil.exe Certificate Extraction

The following analytic identifies the use of certutil.exe with arguments indicating the manipulation
or extraction of certificates. This activity is significant because extracting certificates can allow
attackers to sign new authentication tokens, particularly in federated environments like Windows
ADFS. If confirmed malicious, this could enable attackers to forge authentication tokens,
potentially leading to unauthorized access and privilege escalation within the network.
Rule ID
certutil_exe_certificate_extraction
Query
{'selection1': {'Image|endswith': '\\certutil.exe'}, 'selection2': {'CommandLine|cont
ains': '-exportPFX'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1649 
References
https://blog.sygnia.co/detection-and-hunting-of-golden-saml-attack 
https://strontic.github.io/xcyclopedia/library/certutil.exe-
09A8A29BAA3A451713FD3D07943B4A43.html 
Severity
90
Suppression Logic Based On
computer_name
process_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/08/ critical Unless there are specific use cases, manipulating or exporting certificates using certutil is
uncommon. Extraction of certificate has been observed during attacks such as Golden SAML
ental 18
and other campaigns targeting Federated services.
Domain Name Service (DNS) Rule IDs
Rule Details: DNS Query to TOR Proxy Domain

DNS query to onion domains and proxy domains for TOR network.
Rule ID
dns_1
Query
{'selection_domain': {'DnsQuestionName|endswith': ['.onion', '.tor2web.org', '.tor2we
b.com', '.torlink.co', '.onion.to', '.onion.ink', '.onion.cab', '.onion.nu', '.onion.
link', '.onion.it', '.onion.city', '.onion.direct', '.onion.top', '.onion.casa', '.on
ion.plus', '.onion.rip', '.onion.dog', '.tor2web.fi', '.tor2web.blutmagie.de', '.onio
n.sh', '.onion.lu', '.onion.pet', '.t2w.pw', '.tor2web.ae.org', '.tor2web.io', '.tor2
web.xyz', '.onion.lt', '.s1.tor-gateways.de', '.s2.tor-gateways.de', '.s3.tor-
gateways.de', '.s4.tor-gateways.de', '.s5.tor-
gateways.de', '.hiddenservice.net']}, 'condition': 'selection_domain'}
Log Source
Stellar Cyber Network Events configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0010 , T1048 , TA0011 , T1090.003 
References
https://github.com/Azure/Azure-
Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/ASimDNS/im
DNS_TorProxies.yaml 
Severity
30
Suppression Logic Based On
srcip
dns.question.name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experim 2024/05/1 medium Legitimate access to TOR network. TOR network is rarely used for normal daily use unless
your services have special anonymity needs.
ental 5
Rule Details: Phishing Domain With File Extension TLD
DNS query to TLDs that resemble file extensions. Attackers may use these TLDs for phishing.
Rule ID
dns_2

Query
{'selection_domain': {'DnsQuestionName|endswith': ['.zip', '.mov']}, 'condition': 'se
lection_domain'}
Log Source
Stellar Cyber Network Events configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1566 
References
https://arstechnica.com/information-technology/2023/05/critics-say-googles-new-zip-
and-mov-domains-will-be-a-boon-to-scammers/ 
https://www.trendmicro.com/en_us/research/23/e/future-exploitation-vector-file-
extensions-as-top-level-domains.html 
Severity
30
Suppression Logic Based On
srcip
dns.question.name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2024/05/15 low Legitimate domains with .zip or .mov TLDs. These new TLDs are rarely seen in
common websites.
al
Rule Details: DNS Query to External Service Interaction Domains
DNS query to external service interaction domains often used for out-of-band interactions after
successful RCE.
Rule ID
dns_3
Query
{'selection_domain': {'DnsQuestionName|endswith': ['.interact.sh', '.oast.pro', '.oas
t.live', '.oast.site', '.oast.online', '.oast.fun', '.oast.me', '.burpcollaborator.ne
t', '.oastify.com', '.canarytokens.com', '.requestbin.net', '.dnslog.cn']}, 'conditio
n': 'selection_domain'}
Log Source

Stellar Cyber Network Events configured.
Rule Source
SigmaHQ,aff715fa-4dd5-497a-8db3-910bea555566
Author: Florian Roth (Nextron Systems), Matt Kelly (list of domains)
Tactics, Techniques, and Procedures
TA0001 , T1190 , TA0043 , T1595.002 
References
https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410c9a
55/rules/network/dns/net_dns_external_service_interaction_domains.yml 
https://twitter.com/breakersall/status/1533493587828260866 
Severity
30
Suppression Logic Based On
srcip
dns.question.name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2022/06/0 medium Legitimate external service access. May be initiated by internal security engineers for out-
of-band application security testing.
7
Rule Details: DNS Query to Monero Crypto Coin Mining Pool Domains
DNS query to Monero crypto coin mining pool domains.
Rule ID
dns_4
Query
{'selection_domain': {'DnsQuestionName|endswith': ['pool.minexmr.com', 'fr.minexmr.co
m', 'de.minexmr.com', 'sg.minexmr.com', 'ca.minexmr.com', 'us-
west.minexmr.com', 'pool.supportxmr.com', 'mine.c3pool.com', 'xmr-
eu1.nanopool.org', 'xmr-eu2.nanopool.org', 'xmr-us-east1.nanopool.org', 'xmr-us-
west1.nanopool.org', 'xmr-asia1.nanopool.org', 'xmr-jp1.nanopool.org', 'xmr-
au1.nanopool.org', 'xmr.2miners.com', 'xmr.hashcity.org', 'xmr.f2pool.com', 'xmrpool.
eu', 'pool.hashvault.pro']}, 'condition': 'selection_domain'}
Log Source
Stellar Cyber Network Events configured.
Rule Source

SigmaHQ,b593fd50-7335-4682-a36c-4edcb68e4641
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0040 , T1496 , TA0010 , T1567 
References
https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410c9a
55/rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml 
https://www.nextron-systems.com/2021/10/24/monero-mining-pool-fqdns/ 
Severity
50
Suppression Logic Based On
srcip
dns.question.name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
stable 2021/10/24 high Legitimate access to Monero mining pools. Rarely happens unless legitimate programs
contain crypto mining functions.
Rule Details: DNS Query to Anonymous File Upload Domains
DNS query to anonymous file upload platform domains often used for malicious purposes.
Rule ID
dns_6
Query
{'selection_domain': {'DnsQuestionName|endswith': ['.anonfiles.com', '.api.put.io', '
.upload.put.io', '.ufile.io']}, 'condition': 'selection_domain'}
Log Source
Stellar Cyber Network Events configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0010 , T1567.002 
References
https://github.com/SigmaHQ/sigma/blob/29dce312bc49a9101d33e4d390a7c349c8d985
a2/rules/windows/builtin/dns_client/win_dns_client_anonymfiles_com.yml 

https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-
spotlight-blackbyte 
https://github.com/SigmaHQ/sigma/blob/29dce312bc49a9101d33e4d390a7c349c8d985
a2/rules/windows/builtin/dns_client/win_dns_client_put_io.yml 
https://darkatlas.io/blog/medusa-ransomware-group-opsec-failure 
https://github.com/SigmaHQ/sigma/blob/598d29f811c1859ba18e05b8c419cc94410c9a
55/rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml 
https://thedfirreport.com/2021/12/13/diavol-ransomware/ 
Severity
20
Suppression Logic Based On
srcip
dns.question.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2024/12/20 low Legitimate use of anonymous file sharing services.
Mimikatz Rule IDs
Rule Details: Mimikatz Credential Dump
The mask the suspicious process used to obtain access privilege. the different access_mask
means different capability obtained by the suspicious process.
Rule ID
mimikatz_mem_scan
Query
{'selection1': {'DetectionFlag': 2301}, 'selection2': {'SourceImage': ['C:\\Windows\\
System32\\MsiExec.exe', 'C:\\Program Files\\McAfee\\Endpoint Security\\Adaptive Threa
t Protection\\mfeatp.exe', 'C:\\Program Files\\Guardicore\\gc-
launcher.exe', 'c:\\Program Files\\Microsoft Security Client\\MsMpEng.exe']}, 'select
ion3': [{'SourceImage|re': 'C:\\\\Program Files\\\\SentinelOne\\\\Sentinel Agent ([0-
9]{2,3}\\.[0-9]\\.[0-9]\\.[0-9]
{1,4})\\\\SentinelAgent\\.exe'}], 'condition': 'selection1 and not selection2 and not
selection3'}
Detection Flag
Note: detection_flag is a Stellar enriched field.
2301: Mimikatz access to lsass.exe
Log Source

Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A
Severity
90
Suppression Logic Based On
computer_name
access_subject
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/12/13 critical N/A
Network Security Rule IDs
Rule Details: Possible Impacket SecretDump Remote Activity
Detect AD credential dumping using Impacket SecretDump HKTL.
Rule ID
network_security_2
Query
{'selection': {'appid_name': 'smb', 'metadata|contains|all': ['ADMIN$', 'SYSTEM32\\',
'.tmp']}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A

Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/01 high Unknown
Rule Details: Windows Network Access Suspicious desktop.ini Action
Detects unusual processes accessing desktop.ini remotely over network share, which can be
leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing
them on disk.
Rule ID
network_security_3
Query
{'selection': {'appid_name': 'smb', 'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*desktop\\.ini[^']*'[^}]*'command'\\s*:\\s*9[^}]*\
\}"}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1547.009 
References
https://isc.sans.edu/forums/diary/Desktopini+as+a+postexploitation+tool/25912/ 
Severity
50
Suppression Logic Based On
appid_name
srcip
dstip

dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 medium Unknown
Rule Details: Possible PetitPotam Coerce Authentication Attempt
Detect PetitPotam coerced authentication activity.
Rule ID
network_security_4
Query
{'selection': {'appid_name': 'smb', 'metadata|contains|all': ['IPC$', 'lsarpc', 'ANON
YMOUS LOGON']}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1187 
References
https://github.com/topotam/PetitPotam 
https://github.com/splunk/security_content/blob/0dd6de32de2118b2818550df9e65255f4
109a56d/detections/endpoint/petitpotam_network_share_access_request.yml 
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/05 high Unknown.
Rule Details: Protected Storage Service Access

Detects access to a protected_storage service over the network. Potential abuse of DPAPI to
extract domain backup keys from Domain Controllers.
Rule ID
network_security_5
Query
{'selection': {'appid_name': 'smb', 'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*protected_storage[^']*'[^}]*'command'\\s*:\\s*9[^
}]*\\}"}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 high Unknown
Rule Details: Startup/Logon Script added to Group Policy Object
Detects the modification of Group Policy Objects (GPO) to add a startup/logon script to users or
computer objects.
Rule ID
network_security_6
Query

{'selection_protocol': {'appid_name': 'smb'}, 'selection_share': {'metadata|contains'
: 'Policies'}, 'selection_relative_target_name': {'metadata|re': "'request'\\s*:\\s*\
\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*scripts\\.ini[^']*'[^}]*'command'\\s*:\\s*9[^}]*\
\}"}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1547 , TA0005 , T1484 
References
N/A
Severity
50
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/05 medium Unknown
Rule Details: Remote Task Creation via ATSVC Named Pipe
Detects remote task creation via at.exe or API interacting with ATSVC namedpipe.
Rule ID
network_security_7
Query
{'selection': {'appid_name': 'smb', 'metadata|contains': ['IPC$']}, 'selection_atsvc'
: {'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*atsvc[^']*'[^}]*'command'\\s*:\\s*9[^}]*\\}"}, 'c
ondition': 'selection and selection_atsvc'}
Log Source
Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1053.002 
References
N/A
Severity
50
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/09 medium Unknown
Rule Details: DCERPC SMB Spoolss Named Pipe
Detects the use of the spoolss named pipe over SMB. This can be used to trigger the
authentication via NTLM of any machine that has the spoolservice enabled.
Rule ID
network_security_8
Query
{'selection': {'appid_name': 'smb', 'metadata|contains|all': ['IPC$']}, 'selection_sp
oolss': {'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*spoolss[^']*'[^}]*'command'\\s*:\\s*9[^}]*\\}"},
'condition': 'selection and selection_spoolss'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1021.002 

References
https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-
trusts-71f2b33688e1 
https://dirkjanm.io/a-different-way-of-abusing-zerologon/ 
https://twitter.com/_dirkjan/status/1309214379003588608 
Severity
50
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 medium N/A
Rule Details: Persistence and Execution at Scale via GPO Scheduled Task
Detect lateral movement using GPO scheduled task, usually used to deploy ransomware at
scale.
Rule ID
network_security_9
Query
{'selection': {'appid_name': 'smb', 'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*ScheduledTasks\\.xml[^']*'[^}]*'command'\\s*:\\s*
9[^}]*\\}"}, 'condition': 'selection'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://twitter.com/menasec1/status/1106899890377052160 
https://www.secureworks.com/blog/ransomware-as-a-distraction 

Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/05 high Unknown
Rule Details: Impacket PsExec Execution
Detects execution of Impacket's psexec.py.
Rule ID
network_security_10
Query
{'selection_protocol': {'appid_name': 'smb'}, 'selection_sharename': {'metadata|conta
ins': ['IPC$']}, 'selection_relative_target_name': {'metadata|contains': ['RemCom_std
in', 'RemCom_stdout', 'RemCom_stderr']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
N/A
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/09 high Unknown
Rule Details: Suspicious PsExec Execution
Detects execution of psexec or paexec with renamed service name, this rule helps to filter out
the noise if psexec is used for legit purposes or if attacker uses a different psexec client other
than sysinternal one.
Rule ID
network_security_11
Query
{'selection': {'appid_name': 'smb', 'metadata|contains': ['-stdin', '-stdout', '-
stderr']}, 'filter': {'metadata|contains': 'PSEXESVC'}, 'condition': 'selection and n
ot filter'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
N/A
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 high Unknown
Rule Details: Remote Service Activity via SVCCTL Named Pipe
Detects remote service activity via remote access to the svcctl named pipe.

Rule ID
network_security_12
Query
{'selection': {'appid_name': 'smb', 'metadata|contains': ['IPC$']}, 'selection_svcctl
': {'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*svcctl[^']*'[^}]*'command'\\s*:\\s*9[^}]*\\}"}, '
condition': 'selection and selection_svcctl'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
N/A
Severity
50
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 medium Unknown
Rule Details: T1047 Wmiprvse Wbemcomn DLL Hijack
Detects a threat actor creating a file named `wbemcomn.dll` in the
`C:\Windows\System32\wbem\` directory over the network for a WMI DLL Hijack scenario.
Rule ID
network_security_13
Query
{'selection': {'appid_name': 'smb', 'metadata|contains': ['\\\\wbem\\\\wbemcomn.dll']
}, 'condition': 'selection'}
Log Source

Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1047 , TA0008 , T1021.002 
References
https://threathunterplaybook.com/hunts/windows/201009-
RemoteWMIWbemcomnDLLHijack/notebook.html 
Severity
75
Suppression Logic Based On
appid_name
srcip
dstip
dstip_host
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024/07/13 high Unknown
Rule Details: BloodHound Enumeration Activity
Detects unusual LDAP search requests, which can be potential domain enumeration activity from
BloodHound or other Active Directory data collection tools.
Rule ID
network_security_14
Query
{'selection_search': {'metadata|contains': ["'message_type': 3"]}, 'selection_generic
': {'metadata|contains': ['(grouptype:1.2.840.113556.1.4.803:=2147483648)', '(groupty
pe:1.2.840.113556.1.4.803:=2147483656)', '(grouptype:1.2.840.113556.1.4.803:=21474836
52)', '(grouptype:1.2.840.113556.1.4.803:=2147483650)', '(samaccounttype=805306369)',
'(samaccounttype=805306368)', '(samaccounttype=536870913)', '(samaccounttype=5368709
12)', '(samaccounttype=268435457)', '(samaccounttype=268435456)', '(objectcategory=gr
ouppolicycontainer)', '(objectcategory=organizationalunit)', '(objectcategory=compute
r)', '(objectcategory=ntdsdsa)', '(objectcategory=server)', '(objectcategory=domain)'
, '(objectcategory=person)', '(objectcategory=group)', '(objectcategory=user)', '(obj
ectclass=trusteddomain)', '(objectclass=computer)', '(objectclass=server)', '(objectc
lass=group)', '(objectclass=user)', '(primarygroupid=521)', '(primarygroupid=516)', '
(primarygroupid=515)', '(primarygroupid=512)', 'objectguid=', '(schemaidguid=']}, 'se

lection_dn_enum': {'metadata|contains': ['cn=domain admins', 'cn=enterprise admins',
'cn=group policy creator owners']}, 'selection_allobject': {'metadata|contains': ["'f
ilter': '(objectclass=*)'"]}, 'selection_suspicious': {'metadata|contains': ['(userac
countcontrol:1.2.840.113556.1.4.803:=4194304)', '(useraccountcontrol:1.2.840.113556.1
.4.803:=2097152)', '!
(useraccountcontrol:1.2.840.113556.1.4.803:=1048574)', '(useraccountcontrol:1.2.840.1
13556.1.4.803:=524288)', '(useraccountcontrol:1.2.840.113556.1.4.803:=65536)', '(user
accountcontrol:1.2.840.113556.1.4.803:=8192)', '(useraccountcontrol:1.2.840.113556.1.
4.803:=544)', '!(useraccountcontrol:1.2.840.113556.1.4.803:=2)', 'msds-
allowedtoactonbehalfofotheridentity', 'msds-allowedtodelegateto', 'msds-
groupmanagedserviceaccount', '(accountexpires=9223372036854775807)', '(accountexpires
=0)', '(admincount=1)', 'ms-mcs-
admpwd']}, 'filter_generic': {'metadata|contains': ['(domainsid=', '(objectsid=', '(c
n=']}, 'condition': 'selection_search and (((selection_generic or (selection_dn_enum
and selection_allobject)) and not filter_generic) or selection_suspicious)'}
Log Source
Stellar Cyber Network Events configured for:
Requirements: Network/Security/Modular sensor must be able to capture network traffic
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1482 , T1087.002 , T1069.002 
References
https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ldap/win_ldap_rec
on.yml 
https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/hunting-for-
reconnaissance-activities-using-ldap-search-filters/ba-p/824726 
https://github.com/PowerShellMafia/PowerSploit/blob/d943001a7defb5e0d1657085a77
a0e78609be58f/Recon/PowerView.ps1 
https://github.com/BloodHoundAD/SharpHound3/blob/7d96b991b1887ff50349ce59c809
80bc0d95c86a/SharpHound3/LdapBuilder.cs 
https://medium.com/falconforce/falconfriday-detecting-active-directory-data-collection-
0xff21-c22d1a57494c 
https://github.com/fox-
it/BloodHound.py/blob/d65eb614831cd30f26028ccb072f5e77ca287e0b/bloodhound/ad/
domain.py#L427 
https://ipurple.team/2024/07/15/sharphound-detection/ 
Severity
74

Suppression Logic Based On
srcip
dstip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2024/10/28 high LDAP search requests sent by legitimate tools or services
Oracle Cloud Infrastructure (OCI) Audit Rule IDs
Rule Details: OCI IAM Successful Group Deletion
Identifies the deletion of a specified Oracle Cloud Infrastructure (OCI) Identity and Access
Management (IAM) group, which is a collection of users who share a similar set of access
privileges. The group must be empty.
Rule ID
oci_audit_1
Query
{'selection1': {'eventName': 'deletegroup'}, 'selection2': {'status': ['200', '204']}
, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1531 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Routine administrative tasks may trigger alerts when IAM groups are deleted as part of
regular maintenance or restructuring. To manage this, create exceptions for known
ental 21
maintenance periods or specific administrative accounts.

Maturit Creation Risk False Positives
y Date Level
Automated scripts or tools that manage IAM resources might delete groups as part of their
normal operation. Identify these scripts and exclude their actions from triggering alerts by
using specific user or role identifiers.
Temporary groups created for short-term projects or testing purposes might be deleted
frequently. Document these groups and exclude their deletion from monitoring by using
naming conventions or tags.
Changes in organizational structure or policy might necessitate the deletion of certain groups.
Coordinate with relevant teams to anticipate these changes and adjust monitoring rules
accordingly.
Rule Details: OCI IAM Failure Group Deletion
Identifies failed attempts to delete OCI IAM groups, detecting events where the DeleteGroup
action fails due to errors like Forbidden, Not Found, or Conflict. This activity is significant as it
may indicate unauthorized attempts to modify IAM group configurations, which could be a
precursor to privilege escalation or other malicious actions. If confirmed malicious, this could
allow an attacker to disrupt IAM policies, potentially leading to unauthorized access or denial of
service within the OCI environment.
Rule ID
oci_audit_2
Query
{'selection1': {'eventName': 'deletegroup'}, 'selection2': {'status': ['400', '401',
'403', '404', '409', '412', '429']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
10
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information

Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ mediu This detection will require tuning to provide high fidelity detection capabilities. Tune based on
src addresses (corporate offices, VPN terminations) or by groups of users. Not every user
ental 21 m
with OCI access should have permission to delete groups (least privilege).
Rule Details: OCI IAM Delete Policy
The following detection identifies when a policy is deleted on OCI. This does not identify whether
successful or failed, but the error messages tell a story of suspicious attempts.
Rule ID
oci_audit_3
Query
{'selection': {'eventName': 'deletepolicy'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
20
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ mediu This detection will require tuning to provide high fidelity detection capabilities. Tune based on
src addresses (corporate offices, VPN terminations) or by groups of users. Not every user
ental 21 m
with OCI access should have permission to delete policies (least privilege). In addition, this
may be saved separately and tuned for failed or success attempts only.
Rule Details: OCI IAM Group Creation
Identifies the creation of a group in Oracle Cloud Infrastructure (OCI) Identity and Access
Management (IAM). Groups specify permissions for multiple users. Any user in a group
automatically has the permissions that are assigned to the group.
Rule ID

oci_audit_4
Query
{'selection': {'eventName': 'creategroup'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1136 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Routine administrative actions by authorized personnel can trigger alerts. Regularly review
and document legitimate group creation activities to differentiate them from unauthorized
ental 24 actions.
Automated scripts or tools used for infrastructure management may create groups as part of
their normal operation. Identify and whitelist these scripts to prevent unnecessary alerts.
Temporary groups created for short-term projects or testing purposes might be flagged.
Implement a naming convention for such groups and exclude them from alerts based on this
pattern.
Scheduled tasks or maintenance activities that involve group creation should be logged and
approved in advance. Use these logs to create exceptions in the detection rule.
Third-party integrations or services that require group creation for functionality can cause
false positives. Verify these integrations and adjust the rule to exclude their known actions.
Rule Details: OCI Route Table Created
Identifies when an OCI Route Table has been created for the specified VCN.
Rule ID
oci_audit_5
Query
{'selection1': {'eventName': 'createroutetable'}, 'selection2': {'status': '200'}, 'c
ondition': 'selection1 and selection2'}
Log Source

Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Routine infrastructure updates or deployments may trigger route table creation events. To
manage this, establish a baseline of expected behavior during scheduled maintenance
ental 24
windows and exclude these from alerts.
Automated cloud management tools often create route tables as part of their operations.
Identify these tools and create exceptions for their known activities to reduce noise.
Development and testing environments frequently undergo changes, including the creation of
route tables. Consider excluding these environments from alerts or applying a different set of
monitoring rules.
Legitimate changes by authorized personnel can be mistaken for suspicious activity.
Implement a process to verify and document authorized changes, allowing for quick exclusion
of these events from alerts.
Multi-account setups might have centralized networking teams that create route tables across
accounts. Coordinate with these teams to understand their activities and exclude them from
triggering alerts.
Rule Details: OCI Route Table Modified or Deleted
Identifies OCI events where a route table has been modified or deleted. Route table can be used
by attackers to disrupt network traffic, reroute communications, or maintain persistence in a
compromised environment.
Rule ID
oci_audit_6
Query
{'selection': {'eventName': ['deleteroutetable']}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Route table modifications are often part of routine administrative tasks, such as creating new
routes, updating associations, or removing unused resources.
ental 24
Automated workflows may trigger these events. Verify whether the source IP matches known
automation tools.
Confirm whether these actions align with maintenance activities or scaling events (e.g.,
adding or removing subnets).
Rule Details: OCI Network Security Group Configuration Change Detection
Identifies a change to an OCI network security group configuration. A network security group
(NSG) provides virtual firewall rules for a specific set of VNICs in a VCN. A security rule is one of
the items in a NetworkSecurityGroup; it can be for either inbound or outbound IP packets.
Modifying configurations may allow unauthorized access. Threat actors may abuse this to
establish persistence, exfiltrate data, or pivot in an OCI environment.
Rule ID
oci_audit_7
Query
{'selection': {'eventName': ['createnetworksecuritygroup', 'updatenetworksecuritygrou
p', 'deletenetworksecuritygroup', 'updatenetworksecuritygroupsecurityrules', 'removen
etworksecuritygroupsecurityrules']}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 

References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Network security group modifications may be part of regular infrastructure maintenance.
Verify if this action aligns with known, scheduled administrative activities.
ental 24
If you are using automated tools like `Terraform` or `CloudFormation`, confirm if the change
matches expected configuration drift corrections or deployments.
Rule Details: OCI IAM Policy Modification
OCI IAM policies associated with a user have been modified.
Rule ID
oci_audit_8
Query
{'selection': {'eventName': ['addusertogroup', 'removeuserfromgroup']}, 'condition':
'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2025/02/24 medium N/A
Rule Details: OCI Defense Evasion PutObjectLifecyclePolicy
This analytic identifies `PutObjectLifecyclePolicy` events in OCI audit logs where a user has
created or replaced an object lifecycle policy for a bucket. This detection leverages OCI logs to
identify suspicious lifecycle configurations. This activity is significant because attackers may use
it to delete logs quickly, thereby evading detection and impairing forensic investigations. If
confirmed malicious, this could allow attackers to cover their tracks, making it difficult to trace
their actions and respond to the breach effectively.
Rule ID
oci_audit_9
Query
{'selection1': {'eventName': 'putobjectlifecyclepolicy'}, 'selection2': {'status': '2
00'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.008 , TA0040 , T1485.001 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experim 2025/02/ mediu While this search has no known false positives, it is possible that it is a legitimate admin
activity. Please consider filtering out these noisy events.
ental 24 m
Rule Details: OCI Log Group Deletion
Identifies the deletion of a specified OCI LogGroup. When a log group is deleted, all the archived
log entries associated with the log group are also permanently deleted.

Rule ID
oci_audit_10
Query
{'selection': {'eventName': 'deleteloggroup'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.001 , TA0040 , T1485 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ mediu Verify whether the user identity, user agent, and/or hostname should be making changes in
your environment. Log group deletions by unfamiliar users or hosts should be investigated. If
ental 24 m
known behavior is causing false positives, it can be exempted from the rule.
If this rule is noisy in your environment due to expected activity, consider adding exceptions
— preferably with a combination of user and IP address conditions.
Rule Details: OCI Log Object Deletion
Identifies the deletion of an OCI log object, which permanently deletes all associated archived
log entries.
Rule ID
oci_audit_11
Query
{'selection': {'eventName': 'deletelog'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.001 , TA0040 , T1485 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ mediu A log object may be deleted by a system administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your environment. Log deletions by
ental 24 m
unfamiliar users or hosts should be investigated. If known behavior is causing false positives,
it can be exempted from the rule.
If this rule is noisy in your environment due to expected activity, consider adding exceptions
— preferably with a combination of user and IP address conditions.
Rule Details: OCI Impair Security Services
Identifies attempts to delete critical OCI security service configurations, such as CloudGuard
detector recipes and recipes from Vulnerability Scanning Service (VSS). This activity is
significant because it indicates potential efforts to disable security monitoring and evade
detection. If confirmed malicious, this could allow attackers to operate undetected, escalate
privileges, or exfiltrate data without triggering security alerts, severely compromising the security
posture of the OCI environment.
Rule ID
oci_audit_12
Query
{'selection': {'eventName': ['deletecontainerscanrecipe', 'deletehostscanrecipe', 'de
letecontainerscantarget', 'deletehostscantarget', 'deletedetectorrecipe', 'deletedete
ctorrecipedetectorrule', 'deletedetectorrecipedetectorruledatasource']}, 'condition':
'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0005 , T1562.001 
References
N/A
Severity
75
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ high Routine maintenance or administrative actions may lead to the deletion of a detector or scan
recipe. Verify if the deletion aligns with scheduled maintenance or administrative tasks.
ental 24
Automated scripts or tools used for environment cleanup might inadvertently delete detector
or scan recipes. Review and adjust automation scripts to prevent unintended deletions.
Organizational policy changes or restructuring could result in recipe deletions. Ensure that
policy changes are communicated and understood by all relevant teams to avoid
unnecessary deletions.
Exclude known and authorized users or roles from triggering alerts by creating exceptions for
specific IAM roles or user accounts that are responsible for legitimate recipe deletions.
Implement logging and alerting for recipe deletions to quickly identify and verify the legitimacy
of the action, allowing for rapid response to potential false positives.
Rule Details: OCI Log Object Updated
Identifies an update to an existing OCI log object with configuration that specifies the delivery of
log files.
Rule ID
oci_audit_13
Query
{'selection': {'eventName': 'updatelog'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 , TA0040 , T1565.001 
References
N/A
Severity

25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Log object updates may be made by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
ental 25 Log object updates from unfamiliar users or hosts should be investigated. If known behavior
is causing false positives, it can be exempted from the rule -- preferably with a combination of
user and IP address conditions.
Rule Details: OCI Potential Bucket Enumeration
Looks for potential enumeration of OCI buckets via ListBuckets. A bucket is a container for
storing objects in a compartment within a namespace.
Rule ID
oci_audit_14
Query
{'selection': {'eventName': 'listbuckets'}, 'filter1': {'principalId|contains': ['.in
stance.', ':cloudguard-
agent:']}, 'filter2': {'principalId|startswith': 'cloudguard/'}, 'condition': 'select
ion and not (filter1 or filter2)'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experimen 2025/02/25 low Administrators listing buckets, it may be necessary to filter out users who commonly
conduct this activity.
tal
Rule Details: OCI IAM Deactivation of MFA Device
Identifies the deactivation of a specified multi-factor authentication (MFA) time-based one-time
password (TOTP) device and removes it from association with the user for which it was originally
enabled.
Rule ID
oci_audit_15
Query
{'selection': {'eventName': 'deletemfatotpdevice'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1531 , TA0003 , T1556.006 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ mediu A MFA device may be deactivated by a system or network administrator. Verify whether the
user identity, user agent, and/or hostname should be making changes in your environment.
ental 26 m
MFA device deactivations from unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
While this activity can be done by administrators, all users must use MFA. The security team
should address any potential benign true positive (B-TP), as this configuration can risk the
user and domain.
Rule Details: OCI Instance Image Export Failure
Identifies a failed attempt to export an OCI instance. A virtual machine (VM) export may indicate
an attempt to extract or exfiltrate information.

Rule ID
oci_audit_16
Query
{'selection1': {'eventName': 'exportimage'}, 'selection2': {'status': ['400', '401',
'404', '409', '412']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1005 , TA0010 , T1537 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low VM exports may be done by a system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making changes in your environment. VM
ental 26
exports from unfamiliar users or hosts should be investigated. If known behavior is causing
false positives, it can be exempted from the rule.
Routine backup operations may trigger the rule if they involve failed export attempts. To
manage this, identify and whitelist specific IAM roles or users that regularly perform legitimate
backup tasks.
Development and testing environments often involve frequent export attempts for non-
production instances. Exclude these environments by tagging instances appropriately and
adjusting the detection rule to ignore these tags.
Misconfigured export tasks due to incorrect permissions or settings can lead to false
positives. Regularly review and update IAM policies and export configurations to ensure they
align with intended operations.
Automated scripts or tools that manage instances might occasionally fail due to transient
issues, causing false alerts. Monitor and log these scripts' activities to distinguish between
expected failures and potential threats.
Rule Details: OCI Kubernetes Cluster Created or Deleted
Detects when an OCI Kubernetes Cluster is created or deleted.
Rule ID
oci_audit_17

Query
{'selection': {'eventName': ['createcluster', 'deletecluster']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1485 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/02/ low Kubernetes cluster being created or deleted may be performed by a system administrator.
Verify whether the user identity, user agent, and/or hostname should be making changes in
ental 27 your environment.
Kubernetes cluster created or deleted from unfamiliar users should be investigated. If known
behavior is causing false positives, it can be exempted from the rule.
Rule Details: OCI Event Rule Deleted
Detects when event rule was deleted.
Rule ID
oci_audit_18
Query
{'selection': {'eventName': 'deleterule'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0005 , T1070 
References
N/A
Severity
75
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/02/27 high N/A
Rule Details: OCI Insecure Metadata Endpoint
Detects insecure metadata endpoint.
Rule ID
oci_audit_19
Query
{'selection': {'url|contains': ['/opc/v1', '/openstack'], 'status': '200'}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1069 
References
N/A
Severity
75
Suppression Logic Based On
oracle.data.resourceId
oracle.data.request.headers.oci-original-url
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2025/02/27 high N/A
Rule Details: OCI Discovery Activity
Detects possible discovery activity.
Rule ID
oci_audit_20
Query
{'selection': {'eventName|startswith': ['get', 'list']}, 'condition': 'selection |
count() by CreatedBy > 20', 'timeframe': '10m'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.definedTags.Oracle-Tags.CreatedBy
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/03/03 medium N/A
Rule Details: OCI Multiple Instances Terminated
Detects when multiple instances were terminated.
Rule ID
oci_audit_21
Query
{'selection': {'eventName': 'TerminateInstance'}, 'condition': 'selection |
count() by srcip >= 5', 'timeframe': '10m'}
Log Source
Stellar Cyber OCI configured.

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1529 
References
N/A
Severity
75
Suppression Logic Based On
srcip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/03/03 high N/A
Rule Details: OCI Multiple Instances Launched
Detects when multiple instances were launched.
Rule ID
oci_audit_22
Query
{'selection': {'eventName': 'LaunchInstance'}, 'condition': 'selection |
count() by srcip >= 5', 'timeframe': '10m'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1496 
References
N/A
Severity
50
Suppression Logic Based On
srcip
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/03/03 medium N/A
Rule Details: OCI Unexpected User Agent
Detects unexpected user agent strings.
Rule ID
oci_audit_23
Query
{'selection': {'userAgent|re': '^.{1,10}$'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
oracle.data.identity.userAgent
srcip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/03/04 medium N/A
Rule Details: OCI Bucket Public Access Type Configuration
Identifies potential OCI bucket misconfiguration of public access type. A bucket is a container for
storing objects in a compartment within a namespace. If a bucket that contains sensitive
information is set to be public accessible, it can lead to subsequent data exfiltration.
Rule ID
oci_audit_24
Query
{'selection': {'eventName': ['createbucket', 'updatebucket']}, 'filter1': {'publicAcc
essType': 'NoPublicAccess'}, 'condition': 'selection and not filter1'}

Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 
References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2025/04/16 low A bucket could be intentionally configured to be publicly accessible and does not
contain any sensitive information.
ntal
Rule Details: OCI Insecure NFS Export
Identifies potentially insecure OCI NFS server export configuration. If the NFS server is poorly
configured (e.g., no IP or read-only restrictions and no root squash), malicious hosts can mount
the file systems and lead to subsequent data exfiltration.
Rule ID
oci_audit_25
Query
{'selection': {'eventName': ['createexport', 'updateexport']}, 'filter1': {'exportSou
rce': '0.0.0.0/0'}, 'filter2': {'exportAccess': 'READ_ONLY'}, 'filter3': {'exportIden
titySquash': 'NONE'}, 'condition': 'selection and (filter1 or not filter2 or filter3)
'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1580 

References
N/A
Severity
25
Suppression Logic Based On
oracle.data.resourceId
oracle.data.eventName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2025/04/16 low An NFS server could be intentionally configured without IP or read-only restrictions, or
without root squash.
tal
OCI Virtual Cloud Network (VCN) Rule IDs
Rule Details: OCI Inbound SSH Connection
Detects inbound SSH connection.
Rule ID
oci_vcn_1
Query
{'selection1': {'srcip_type': 'private'}, 'selection2': {'dstport': 22}, 'condition':
'not selection1 and selection2'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
srcip
dstip
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/02/27 medium N/A
Rule Details: OCI Instance Metadata Access
Detects instance metadata access.
Rule ID
oci_vcn_2
Query
{'selection': {'dstip': '169.254.169.254'}, 'condition': 'selection'}
Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1069 
References
N/A
Severity
50
Suppression Logic Based On
srcip
dstip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/02/28 medium N/A
Rule Details: OCI SSH Scanner
Detects possible SSH scanning activity.
Rule ID
oci_vcn_3
Query
{'selection1': {'action': 'REJECT', 'dstip_type': 'private', 'dstport': 22}, 'selecti
on2': {'srcip_type': 'private'}, 'condition': 'selection1 and not selection2 |
count(dstip) by srcip > 5', 'timeframe': '5m'}

Log Source
Stellar Cyber OCI configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0043 , T1595 
References
N/A
Severity
75
Suppression Logic Based On
srcip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/03/03 high N/A
Office 365 Mail Rule IDs
Rule Details: Office365 Mail Redirect via ExO Transport Rule
Identifies when an Exchange Online transport rule is configured to forward emails. This could be
an adversary mailbox configured to collect mail from multiple user accounts.
Rule ID
office365_mail_1
Query
{'selection1': {'Operation': ['new-transportrule', 'set-
transportrule']}, 'selection2': {'BlindCopyTo': ''}, 'selection3': {'RedirectMessageT
o': ''}, 'condition': 'selection1 and (not selection2 or not selection3)'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1114 , TA0010 , T1020 
References
N/A

Severity
50
Suppression Logic Based On
office365.Operation
office365.ObjectId
office365.Name
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 medium N/A
Rule Details: Malicious Office365 Inbox Rule
Often times after the initial compromise, the attackers create inbox rules to delete emails that
contain certain keywords. This is done so as to limit ability to warn compromised users that they
have been compromised.
Rule ID
office365_mail_2
Query
{'selection1': {'Operation': 'new-
inboxrule', 'ResultStatus': ['true', 'succeeded'], 'Parameters|contains': ['deleted i
tems', 'junk email', 'deletemessage']}, 'selection2': {'SubjectContainsWords|contains
': ['helpdesk', ' alert', ' suspicious', 'fake', 'malicious', 'phishing', 'spam', 'do
not click', 'do not open', 'hijacked', 'fatal']}, 'selection3': {'BodyContainsWords|
contains': ['helpdesk', ' alert', ' suspicious', 'fake', 'malicious', 'phishing', 'sp
am', 'do not click', 'do not open', 'hijacked', 'fatal']}, 'selection4': {'SubjectOrB
odyContainsWords|contains': ['helpdesk', ' alert', ' suspicious', 'fake', 'malicious'
, 'phishing', 'spam', 'do not click', 'do not open', 'hijacked', 'fatal']}, 'conditio
n': 'selection1 and (selection2 or selection3 or selection4)'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1564.008 , TA0003 , T1098 
References
https://www.reddit.com/r/sysadmin/comments/7kyp0a/recent_phishing_attempts_my_ex
perience_and_what/ 
Severity

50
Suppression Logic Based On
office365.Operation
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 medium N/A
Rule Details: Suspicious Office365 Inbox MoveToFolder Rule
Identifies when the parameters of Microsoft 365 inbox MoveToFolder rules have suspicious
characteristics that move emails to the RSS folder, which attackers sometimes use to hide
incoming mail like security alerts or MFA notifications.
Rule ID
office365_mail_3
Query
{'selection': {'Operation': ['new-inboxrule', 'set-
inboxrule'], 'MoveToFolder|contains': 'rss'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1564.008 , TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
office365.Operation
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 medium N/A
Rule Details: Suspicious Office365 Inbox Rule Name

Identifies when the parameters of Microsoft 365 inbox rules have suspicious characteristics that
are often used in automated or attacker-created rules, specifically rule names that contain
strange strings or strings used in known attacks.
Rule ID
office365_mail_4
Query
{'selection1': {'Operation': ['new-inboxrule', 'set-
inboxrule']}, 'selection2': {'Name|contains': ['erder', 'ddd']}, 'selection3': [{'Nam
e|re': '/(^|\\s+)\\.+($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\w{0,3}\\.\\w{0,3}
($|\\s+)/'}, {'Name|re': '/(^|\\s+).($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\,+,
($|\\s+)/'}, {'Name|re': '/(^|\\s+)\\W{0,4}($|\\s+)/'}, {'Name|re': '/(^|\\s+)
(.)\\1{0,3}($|\\s+)/'}, {'Name|re': '/(^|\\s+)[a-z]{0,3}
($|\\s+)/'}], 'condition': 'selection1 and (selection2 or selection3)'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1564.008 , TA0003 , T1098 
References
N/A
Severity
25
Suppression Logic Based On
office365.Operation
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 low N/A
Rule Details: Rare and Potentially High-Risk Office365 Operations
Identifies Office365 operations that are typically rare and can provide capabilities useful to
attackers.
Rule ID
office365_mail_5
Query

{'selection1': {'Operation': ['add-mailboxfolderpermission', 'new-
managementroleassignment', 'new-inboxrule', 'set-inboxrule', 'set-
transportrule']}, 'selection2': {'Operation': ['add-mailboxpermission', 'set-
mailbox']}, 'selection3': {'UserId|contains': ['nt authority\\system (microsoft.excha
nge.servicehost)', 'nt authority\\system (microsoft.exchange.adminapi.netcore)', 'nt
authority\\system (w3wp)', 'devilfish-
applicationaccount']}, 'condition': 'selection1 or (selection2 and not selection3)'}
Log Source
Stellar Cyber Microsoft 365 configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 , TA0009 , T1114 
References
N/A
Severity
25
Suppression Logic Based On
office365.Operation
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 low N/A
Rule Details: Malicious Office365 Inbox Deletion Rule
Identifies when a Microsoft 365 inbox rule is set up such that it deletes all incoming messages,
without specifying any condition (e.g., from a specific sender, with a certain subject, etc.).
Attackers often use this to hide inbound warnings, MFA emails, or incident response
communication after compromising an account.
Rule ID
office365_mail_6
Query
{'selection': {'Operation': ['new-inboxrule', 'set-
inboxrule'], 'DeleteMessage': 'true'}, 'condition': 'selection'}
Log Source
Stellar Cyber Microsoft 365 configured.

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1564.008 , TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
office365.Operation
user.name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/06/09 medium N/A
PowerShell Command and Control (CNC) Rule IDs
Rule Details: PowerShell Remote Access
A Windows host executed a PowerShell script interacting with a remote host. Investigate the
script and the remote host to determine whether the script is malicious. If so, consider
quarantining the host.
Rule ID
powershell_cnc_2200
Query
{'selection1': {'DetectionFlag': 2200}, 'selection2': [{'RemoteIP|re': '^169\\.254\\.
169\\.254$'}, {'RemoteIP|re': '\\.0$'}], 'condition': 'selection1 and not selection2'
}
Detection Flag
Note: detection_flag is a Stellar enriched field.
2200: PowerShell script embedded with remote IP
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0002 , T1059 
References
N/A
Severity
80
Suppression Logic Based On
computer_name
remote_ip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/03/30 critical N/A
Rule Details: PowerShell Remote Access (High Fidelity)
A Windows host executed a PowerShell script interacting with a remote host. Investigate the
script and the remote host to determine whether the script is malicious. If so, consider
quarantining the host.
Rule ID
powershell_cnc_2201
Query
{'selection1': {'DetectionFlag': 2201}, 'selection2': [{'RemoteIP|re': '^169\\.254\\.
169\\.254$'}, {'RemoteIP|re': '\\.0$'}], 'condition': 'selection1 and not selection2'
}
Detection Flag
Note: detection_flag is a Stellar enriched field.
2201: PowerShell script block with IP embedded at warning level (High fidelity)
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
N/A
Severity
80

Suppression Logic Based On
computer_name
remote_ip
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/03/30 critical N/A
PowerShell Scriptblock Rule ID
Rule Details: PowerShell Mailbox Collection Script
Detects PowerShell scripts that can be used to collect data from mailboxes. Adversaries may
target user email to collect sensitive information.
Rule ID
powershell_scriptblock_1
Query
{'selection1': {'ScriptBlockText|contains': ['Microsoft.Office.Interop.Outlook', 'Int
erop.Outlook.olDefaultFolders', '::olFolderInBox', 'Microsoft.Exchange.WebServices.Da
ta.Folder', 'Microsoft.Exchange.WebServices.Data.FileAttachment']}, 'condition': 'sel
ection1'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1114 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/11 medium N/A

Rule Details: Live Memory Dump Using Powershell
Detects usage of a PowerShell command to dump the live memory of a Windows machine.
Rule ID
powershell_scriptblock_3
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-StorageDiagnosticInfo', '-
IncludeLiveDump']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,cd185561-4760-45d6-a63e-a51325112cae
Author: Max Altgelt (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
https://docs.microsoft.com/en-us/powershell/module/storage/get-
storagediagnosticinfo 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/21 high Diagnostics
Rule Details: Invoke-Obfuscation CLIP+ Launcher - PowerShell
Detects Obfuscated use of Clip.exe to execute PowerShell.
Rule ID
powershell_scriptblock_4
Query
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}(?:/c|/r).+clip(?:\\.exe)?.
{0,4}&&.+clipboard]::\\(\\s\\\\"\\{\\d\\}.+-f.+"'}, 'condition': 'selection_4104'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,73e67340-0d25-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high Unknown
Rule Details: Suspicious Service DACL Modification Via Set-Service Cmdlet - PS
Detects usage of the "Set-Service" powershell cmdlet to configure a new SecurityDescriptor that
allows a service to be hidden from other utilities such as "sc.exe", "Get-Service"...etc. (Works
only in powershell 7.)
Rule ID
powershell_scriptblock_5
Query
{'selection_sddl_flag': {'ScriptBlockText|contains': ['-SecurityDescriptorSddl ', '-
sd ']}, 'selection_set_service': {'ScriptBlockText|contains|all': ['Set-
Service ', 'D;;'], 'ScriptBlockText|contains': [';;;IU', ';;;SU', ';;;BA', ';;;SY', '
;;;WD']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source

SigmaHQ,22d80745-6f2c-46da-826b-77adaededd74
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 
References
https://twitter.com/Alh4zr3d/status/1580925761996828672 
https://learn.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/set-service?view=powershell-
7.2 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/24 high Rare intended use of hidden services
Rare FP could occure due to the non linearity of the ScriptBlockText log
Rule Details: Potential Invoke-Mimikatz PowerShell Script
Detects Invoke-Mimikatz PowerShell script and alike. Mimikatz is a credential dumper capable of
obtaining plaintext Windows account logins and passwords.
Rule ID
powershell_scriptblock_6
Query
{'selection_1': {'ScriptBlockText|contains|all': ['DumpCreds', 'DumpCerts']}, 'select
ion_2': {'ScriptBlockText|contains': 'sekurlsa::logonpasswords'}, 'selection_3': {'Sc
riptBlockText|contains|all': ['crypto::certificates', 'CERT_SYSTEM_STORE_LOCAL_MACHIN
E']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
SigmaHQ,189e3b02-82b2-4b90-9662-411eb64486d4
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0006 , T1003 
References
https://www.elastic.co/guide/en/security/current/potential-invoke-mimikatz-powershell-
script.html#potential-invoke-mimikatz-powershell-script 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/28 high Mimikatz can be useful for testing the security of networks
Rule Details: Disable-WindowsOptionalFeature Command PowerShell
Detect built in PowerShell cmdlet Disable-WindowsOptionalFeature, Deployment Image
Servicing and Management tool. Similar to DISM.exe, this cmdlet is used to enumerate, install,
uninstall, configure, and update features and packages in Windows images.
Rule ID
powershell_scriptblock_7
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['Disable-
WindowsOptionalFeature', '-Online', '-
FeatureName']}, 'selection_feature': {'ScriptBlockText|contains': ['Windows-Defender-
Gui', 'Windows-Defender-Features', 'Windows-Defender', 'Windows-Defender-
ApplicationGuard']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,99c4658d-2c5e-4d87-828d-7c066ca537c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References

https://github.com/redcanaryco/atomic-red-
team/blob/5b67c9b141fa3918017f8fa44f2f88f0b1ecb9e1/atomics/T1562.001/T1562.00
1.md 
https://docs.microsoft.com/en-us/powershell/module/dism/disable-
windowsoptionalfeature?view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/10 high Unknown
Rule Details: Powershell DNSExfiltration
DNSExfiltrator allows for transferring (exfiltrate) a file over a DNS request covert channel.
Rule ID
powershell_scriptblock_8
Query
{'selection_cmdlet': [{'ScriptBlockText|contains': 'Invoke-
DNSExfiltrator'}, {'ScriptBlockText|contains|all': [' -i ', ' -d ', ' -p ', ' -
doh ', ' -t ']}], 'condition': 'selection_cmdlet'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d59d7842-9a21-4bc6-ba98-64bfe0091355
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048/T1048.md#ato
mic-test-3---dnsexfiltration-doh 
https://github.com/Arno0x/DNSExfiltrator 

Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/07 high Legitimate script
Rule Details: Powershell Empire agent CnC activity
A Powershell Empire framework agent is running on the machine, and it's trying to access the
CnC server.
Rule ID
powershell_scriptblock_9
Query
{'selection1': {'ScriptBlockText|contains': 'IF($PSVERSIonTAblE.PSVERsIOn.MajOr -
ge 3)
{'}, 'selection2': {'ScriptBlockText|contains': '[Ref].ASsEmbLY.GeTTYpe('}, 'selectio
n3': {'ScriptBlockText|contains': 'System.Management.Automation.AmsiUtils'}, 'conditi
on': 'selection1 and selection2 and selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A

Rule Details: Powershell Directory Enumeration
Detects technique used by MAZE ransomware to enumerate directories using Powershell.
Rule ID
powershell_scriptblock_10
Query
{'selection': {'ScriptBlockText|contains|all': ['foreach', 'Get-ChildItem', '-
Path ', '-ErrorAction ', 'SilentlyContinue', 'Out-File ', '-
append']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,162e69a7-7981-4344-84a9-0f1c9a217a52
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1083 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1083/T1083.md 
https://www.mandiant.com/resources/tactics-techniques-procedures-associated-with-
maze-ransomware-incidents 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 medium Legitimate PowerShell scripts
Rule Details: Invoke-Obfuscation Via Use MSHTA - PowerShell
Detects Obfuscated Powershell via use MSHTA in Scripts.
Rule ID
powershell_scriptblock_11

Query
{'selection_4104': {'ScriptBlockText|contains|all': ['set', '&&', 'mshta', 'vbscript:
createobject', '.run', '(window.close)']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e55a5195-4724-480e-a77e-3ebe64bd3759
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/08 high Unknown
Rule Details: Root Certificate Installed - PowerShell
Adversaries may install a root certificate on a compromised system to avoid warnings when
connecting to adversary controlled web servers.
Rule ID
powershell_scriptblock_12
Query
{'selection1': {'ScriptBlockText|contains|all': ['Move-
Item', 'Cert:\\LocalMachine\\Root']}, 'selection2': {'ScriptBlockText|contains|all':
['Import-Certificate', 'Cert:\\LocalMachine\\Root']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,42821614-9264-4761-acfc-5772c3286f76
Author: oscd.community, @redcanary, Zach Stanford @svch0st
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004
.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2020/10/1 medium Help Desk or IT may need to manually add a corporate Root CA on occasion. Need to
test if GPO push doesn't trigger FP
ntal 0
Rule Details: Clearing Windows Console History
Identifies when a user attempts to clear console history. An adversary may clear the command
history of a compromised account to conceal the actions undertaken during an intrusion.
Rule ID
powershell_scriptblock_15
Query
{'selection1': {'ScriptBlockText|contains': 'Clear-
History'}, 'selection2a': {'ScriptBlockText|contains': ['Remove-
Item', 'rm']}, 'selection2b': {'ScriptBlockText|contains': ['ConsoleHost_history.txt'
, '(Get-
PSReadlineOption).HistorySavePath']}, 'condition': 'selection1 or selection2a and sel
ection2b'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled

Rule Source
SigmaHQ,bde47d4b-9987-405c-94c7-b080410e8ea7
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://stefanos.cloud/blog/kb/how-to-clear-the-powershell-command-history/ 
https://www.shellhacks.com/clear-history-powershell/ 
https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-
forensics 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/25 high Unknown
Rule Details: Windows Firewall Profile Disabled
Detects when a user disables the Windows Firewall via a Profile to help evade defense.
Rule ID
powershell_scriptblock_16
Query
{'selection_args': {'ScriptBlockText|contains|all': ['Set-NetFirewallProfile ', ' -
Enabled ', ' False']}, 'selection_opt': {'ScriptBlockText|contains': [' -
All ', 'Public', 'Domain', 'Private']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,488b44e7-3781-4a71-888d-c95abfacf44d
Author: Austin Songer @austinsonger
Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0005 , T1562.004 
References
https://docs.microsoft.com/en-us/powershell/module/netsecurity/set-netfirewallprofile?
view=windowsserver2019-ps 
https://www.tutorialspoint.com/how-to-get-windows-firewall-profile-settings-using-
powershell 
http://powershellhelp.space/commands/set-netfirewallrule-psv5.php 
http://woshub.com/manage-windows-firewall-powershell/ 
https://www.elastic.co/guide/en/security/current/windows-firewall-disabled-via-
powershell.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/12 medium Unknown
Rule Details: Suspicious Portable Executable Encoded in Powershell Script
Detects the presence of a portable executable (PE) in a PowerShell script by looking for its
encoded header. Attackers embed PEs into PowerShell scripts to inject them into memory,
avoiding defences by not writing to disk.
Rule ID
powershell_scriptblock_17
Query
{'selection1': {'ScriptBlockText|contains': 'TVqQAAMAAAAEAAAA'}, 'selection2': {'User
Id': 'S-1-5-18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References

N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/15 medium N/A
Rule Details: PowerShell Suspicious Script with Screenshot Capabilities
Detects PowerShell scripts that can take screenshots, which is a common feature in post-
exploitation kits and remote access tools (RATs).
Rule ID
powershell_scriptblock_19
Query
{'selection1': {'ScriptBlockText|contains': 'CopyFromScreen'}, 'selection2': {'Script
BlockText|contains': 'System.Drawing.Bitmap'}, 'selection3': {'ScriptBlockText|contai
ns': 'Drawing.Bitmap'}, 'selection4': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (selection2 or selection3) and (not selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1113 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
production 2021/10/19 medium N/A
Rule Details: Registry-Free Process Scope COR_PROFILER
Adversaries may leverage the COR_PROFILER environment variable to hijack the execution
flow of programs that load the .NET CLR. The COR_PROFILER is a .NET Framework feature
which allows developers to specify an unmanaged (or external of .NET) profiling DLL to be
loaded into each .NET process that loads the Common Language Runtime (CLR). These
profiliers are designed to monitor, troubleshoot, and debug managed code executed by the .NET
CLR. (Citation: Microsoft Profiling Mar 2017) (Citation: Microsoft COR_PROFILER Feb 2013)
Rule ID
powershell_scriptblock_20
Query
{'selection': {'ScriptBlockText|contains|all': ['$env:COR_ENABLE_PROFILING', '$env:CO
R_PROFILER', '$env:COR_PROFILER_PATH']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,23590215-4702-4a70-8805-8dc9e58314a2
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.012 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.012/T1574.012
.md#atomic-test-3---registry-free-process-scope-cor_profiler 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/30 medium Legitimate administrative script

Rule Details: Invoke-Obfuscation RUNDLL LAUNCHER - PowerShell
Detects Obfuscated Powershell via RUNDLL LAUNCHER.
Rule ID
powershell_scriptblock_21
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['rundll32.exe', 'shell32.dll', '
shellexec_rundll', 'powershell']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e6cb92b4-b470-4eb8-8a9d-d63e8583aae0
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium Unknown
Rule Details: Execution via CL_Invocation.ps1 - Powershell
Detects Execution via SyncInvoke in CL_Invocation.ps1 module.
Rule ID
powershell_scriptblock_23
Query
{'selection': {'ScriptBlockText|contains|all': ['CL_Invocation.ps1', 'SyncInvoke']},
'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4cd29327-685a-460e-9dac-c3ab96e549dc
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Cl_invocation/ 
https://twitter.com/bohops/status/948061991012327424 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/14 high Unknown
Rule Details: Suspicious TCP Tunnel Via PowerShell Script
Detects powershell scripts that creates sockets/listeners which could be indicative of tunneling
activity.
Rule ID
powershell_scriptblock_24
Query
{'selection': {'ScriptBlockText|contains|all': ['[System.Net.HttpWebRequest]', 'Syste
m.Net.Sockets.TcpListener', 'AcceptTcpClient']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bd33d2aa-497e-4651-9893-5c5364646595
Author: Nasreddine Bencherchali (Nextron Systems)

Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1090 
References
https://github.com/Arno0x/PowerShellScripts/blob/a6b7d5490fbf0b20f91195838f3a1115
6724b4f7/proxyTunnel.ps1 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/07/08 medium Unknown
Rule Details: Powershell Store File In Alternate Data Stream
Storing files in Alternate Data Stream (ADS) similar to Astaroth malware.
Rule ID
powershell_scriptblock_25
Query
{'selection_compspec': {'ScriptBlockText|contains|all': ['Start-Process', '-
FilePath "$env:comspec" ', '-
ArgumentList ', '>']}, 'condition': 'selection_compspec'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a699b30e-d010-46c8-bbd1-ee2e26765fe9
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004
.md 

Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/02 medium Unknown
Rule Details: Potential PowerShell Obfuscation Using Character Join
Detects specific techniques often seen used inside of PowerShell scripts to obfscuate Alias
creation.
Rule ID
powershell_scriptblock_26
Query
{'selection': {'ScriptBlockText|contains|all': ['-Alias', ' -Value (-
join(']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e8314f79-564d-4f79-bc13-fbc0bf2660d8
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
N/A
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/09 low Unknown

Rule Details: Windows UAC Bypass
A User Account Control Bypass activity was detected. This can be due to either regular operation
or because an attacker is trying to escalate privileges.
Rule ID
powershell_scriptblock_27
Query
{'selection1': {'ScriptBlockText|contains': 'Invoke-
UACBypass'}, 'selection2': {'ScriptBlockText|contains': 'Invoke-
EventVwrBypass'}, 'selection3': {'ScriptBlockText|contains': 'Invoke-
SDCLTBypass'}, 'condition': 'selection1 or selection2 or selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious IO.FileStream
Open a handle on the drive volume via the \\.\ DOS device path specifier and perform direct
access read of the first few bytes of the volume.
Rule ID
powershell_scriptblock_28
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object', 'IO.FileStream', '\\\\.\\']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,70ad982f-67c8-40e0-a955-b920c2fa05cb
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1006/T1006.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/09 medium Legitimate PowerShell scripts
Rule Details: Invoke-Obfuscation VAR+ Launcher - PowerShell
Detects Obfuscated use of Environment Variables to execute PowerShell.
Rule ID
powershell_scriptblock_29
Query
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}(?:/c|/r)(?:\\s|)"set\\s[a-zA-
Z]{3,6}.*(?:\\{\\d\\}){1,}\\\\"\\s+?-f(?:.*\\))
{1,}.*"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,0adfbc14-0ed1-11eb-adc1-0242ac120002

Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high Unknown
Rule Details: Powershell XML Execute Command
Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a
powerful interactive command-line interface and scripting environment included in the Windows
operating system. (Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a
number of actions, including discovery of information and execution of code.
Rule ID
powershell_scriptblock_30
Query
{'selection_xml': {'ScriptBlockText|contains|all': ['New-
Object', 'System.Xml.XmlDocument', '.Load']}, 'selection_exec': {'ScriptBlockText|con
tains': ['IEX ', 'Invoke-Expression ', 'Invoke-Command ', 'ICM -
']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,6c6c6282-7671-4fe9-a0ce-a2dcebdc342b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References

https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.001/T1059.001
.md#atomic-test-8---powershell-xml-requests 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/19 medium Legitimate administrative script
Rule Details: Dump Credentials from Windows Credential Manager With PowerShell
Adversaries may search for common password storage locations to obtain user credentials.
Passwords are stored in several places on a system, depending on the operating system or
application holding the credentials.
Rule ID
powershell_scriptblock_33
Query
{'selection_kiddie': {'ScriptBlockText|contains': ['Get-
PasswordVaultCredentials', 'Get-
CredManCreds']}, 'selection_rename_Password': {'ScriptBlockText|contains|all': ['New-
Object', 'Windows.Security.Credentials.PasswordVault']}, 'selection_rename_credman':
{'ScriptBlockText|contains|all': ['New-
Object', 'Microsoft.CSharp.CSharpCodeProvider', '[System.Runtime.InteropServices.Runt
imeEnvironment]::GetRuntimeDirectory())', 'Collections.ArrayList', 'System.CodeDom.Co
mpiler.CompilerParameters']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,99c49d9c-34ea-45f7-84a7-4751ae6b2cbc
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555 
References

https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555/T1555.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium Unknown
Rule Details: Potential Suspicious Windows Feature Enabled
Detects usage of the built-in PowerShell cmdlet "Enable-WindowsOptionalFeature" used as a
Deployment Image Servicing and Management tool. Similar to DISM.exe, this cmdlet is used to
enumerate, install, uninstall, configure, and update features and packages in Windows images.
Rule ID
powershell_scriptblock_35
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['Enable-
WindowsOptionalFeature', '-Online', '-
FeatureName']}, 'selection_feature': {'ScriptBlockText|contains': ['TelnetServer', 'I
nternet-Explorer-Optional-amd64', 'TFTP', 'SMB1Protocol', 'Client-
ProjFS', 'Microsoft-Windows-Subsystem-Linux']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,55c925c1-7195-426b-a136-a9396800e29b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://docs.microsoft.com/en-us/powershell/module/dism/enable-
windowsoptionalfeature?view=windowsserver2022-ps 
https://learn.microsoft.com/en-us/windows/win32/projfs/enabling-windows-projected-file-
system 

https://learn.microsoft.com/en-us/windows/wsl/install-on-server 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/10 medium Unknown
Rule Details: Suspicious PowerShell Mailbox SMTP Forward Rule
Detects usage of the powerShell Set-Mailbox Cmdlet to set-up an SMTP forwarding rule.
Rule ID
powershell_scriptblock_36
Query
{'selection': {'ScriptBlockText|contains|all': ['Set-Mailbox ', ' -
DeliverToMailboxAndForward ', ' -ForwardingSmtpAddress ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,15b7abbb-8b40-4d01-9ee2-b51994b1d474
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2022/10/26 medium Legitimate usage of the cmdlet to forward emails
Rule Details: Powershell Add Name Resolution Policy Table Rule
Detects powershell scripts that adds a Name Resolution Policy Table (NRPT) rule for the
specified namespace. This will bypass the default DNS server and uses a specified server for
answering the query.
Rule ID
powershell_scriptblock_37
Query
{'selection': {'ScriptBlockText|contains|all': ['Add-DnsClientNrptRule', '-
Namesp', '-NameSe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4368354e-1797-463c-bc39-a309effbe8d7
Author: Borna Talebi
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1565 
References
https://twitter.com/NathanMcNulty/status/1569497348841287681 
https://docs.microsoft.com/en-us/powershell/module/dnsclient/add-dnsclientnrptrule?
view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/14 high Unknown
Rule Details: Security Software Discovery by Powershell

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and
sensors that are installed on a system or in a cloud environment. This may include things such
as firewall rules and anti-virus.
Rule ID
powershell_scriptblock_38
Query
{'selection_1': {'ScriptBlockText|contains|all': ['get-process', '.Description', '-
like']}, 'selection_2': {'ScriptBlockText|contains': ['"*virus*"', '"*carbonblack*"',
'"*defender*"', '"*cylance*"']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,904e8e61-8edf-4350-b59c-b905fc8e810c
Author: frack113, Anish Bogati, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1518.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.001/T1518.001
.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/16 low Unknown
Rule Details: Suspicious New-PSDrive to Admin Share
Adversaries may use to interact with a remote network share using Server Message Block
(SMB). The adversary may then perform actions as the logged-on user.
Rule ID
powershell_scriptblock_39

Query
{'selection': {'ScriptBlockText|contains|all': ['New-PSDrive', '-
psprovider ', 'filesystem', '-root ', '\\\\', '$']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1c563233-030e-4a07-af8c-ee0490a66d3a
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0008 , T1021.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.002/T1021.002
.md#atomic-test-2---map-admin-share-powershell 
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/new-psdrive?
view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/13 medium Unknown
Rule Details: PowerShell Script with Token Impersonation Capabilities
Detects scripts that contain PowerShell functions, structures, or Windows API functions related to
token impersonation/theft. Attackers may duplicate then impersonate another user's token to
escalate privileges and bypass access controls.
Rule ID
powershell_scriptblock_40
Query

{'selection1': {'ScriptBlockText|contains': ['Invoke-
TokenManipulation', 'ImpersonateNamedPipeClient', 'NtImpersonateThread']}, 'selection
2': {'ScriptBlockText|contains': 'STARTUPINFOEX'}, 'selection3': {'ScriptBlockText|co
ntains': 'UpdateProcThreadAttribute'}, 'selection4': {'ScriptBlockText|contains': 'Ad
justTokenPrivileges'}, 'selection5': {'ScriptBlockText|contains': 'SeDebugPrivilege'}
, 'selection6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and selection3) or (selection4 and sel
ection5)) and (not selection6)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 , TA0005 , T1134 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/08/17 medium N/A
Rule Details: Disable of ETW Trace - Powershell
Detects usage of powershell cmdlets to disable or remove ETW trace sessions.
Rule ID
powershell_scriptblock_41
Query
{'selection_pwsh_remove': {'ScriptBlockText|contains': 'Remove-
EtwTraceProvider '}, 'selection_pwsh_set': {'ScriptBlockText|contains|all': ['Set-
EtwTraceProvider ', '0x11']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,115fdba9-f017-42e6-84cf-d5573bf2ddf8
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070 , T1562.006 
References
https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-
and-defense-4be7ac62ac63 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 high Unknown
Rule Details: Service Registry Permissions Weakness Check
Adversaries may execute their own malicious payloads by hijacking the Registry entries used by
services. Adversaries may use flaws in the permissions for registry to redirect from the originally
specified executable to one that they control, in order to launch their own code at Service start.
Windows stores local service configuration information in the Registry under
HKLM\SYSTEM\CurrentControlSet\Services.
Rule ID
powershell_scriptblock_42
Query
{'selection': {'ScriptBlockText|contains|all': ['get-
acl', 'REGISTRY::HKLM\\SYSTEM\\CurrentControlSet\\Services\\']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,95afc12e-3cbb-40c3-9340-84a032e596a3

Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.011/T1574.011.
md#atomic-test-1---service-registry-permissions-weakness 
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-
acl?view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/30 medium Legitimate administrative script
Rule Details: Potential COM Objects Download Cradles Usage - PS Script
Detects usage of COM objects that can be abused to download files in PowerShell by CLSID.
Rule ID
powershell_scriptblock_43
Query
{'selection_1': {'ScriptBlockText|contains': '[Type]::GetTypeFromCLSID('}, 'selection
_2': {'ScriptBlockText|contains': ['0002DF01-0000-0000-C000-000000000046', 'F6D90F16-
9C73-11D3-B32E-00C04F990BB4', 'F5078F35-C551-11D3-89B9-0000F81FE221', '88d96a0a-f192-
11d4-a65f-0040963251e5', 'AFBA6B42-5692-48EA-8141-DC517DCF0EF1', 'AFB40FFD-B609-40A3-
9828-F88BBE11E4E3', '88d96a0b-f192-11d4-a65f-0040963251e5', '2087c2f4-2cef-4953-a8ab-
66779b670495', '000209FF-0000-0000-C000-000000000046', '00024500-0000-0000-C000-
000000000046']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Script Block Logging must be enable
Rule Source
SigmaHQ,3c7d1587-3b13-439f-9941-7d14313dbdfe
Author: frack113

Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://learn.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?view=net-
7.0 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=57 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium Legitimate use of the library
Rule Details: Dnscat Execution
Dnscat exfiltration tool execution.
Rule ID
powershell_scriptblock_44
Query
{'selection': {'ScriptBlockText|contains': 'Start-
Dnscat2'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a6d67db4-6220-436d-8afc-f3842fe05d43
Author: Daniil Yugoslavskiy, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048 
References
N/A
Severity
95

Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 critical Legitimate usage of PowerShell Dnscat2 — DNS Exfiltration tool (unlikely)
Rule Details: Suspicious Unblock-File
Remove the Zone.Identifier alternate data stream which identifies the file as downloaded from
the internet.
Rule ID
powershell_scriptblock_45
Query
{'selection': {'ScriptBlockText|contains|all': ['Unblock-File ', '-
Path ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,5947497f-1aa4-41dd-9693-c9848d58727d
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005
.md#atomic-test-3---remove-the-zoneidentifier-alternate-data-stream 
https://docs.microsoft.com/en-
us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/02/01 medium Legitimate PowerShell scripts
Rule Details: AMSI Bypass Pattern Assembly GetType
Detects code fragments found in small and obfuscated AMSI bypass PowerShell scripts.
Rule ID
powershell_scriptblock_47
Query
{'selection': {'ScriptBlockText|contains|all': ['[Ref].Assembly.GetType', 'SetValue($
null,$true)', 'NonPublic,Static']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e0d6c087-2d1c-47fd-8799-3904103c5a98
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References
https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/ 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/09 high Unknown
Rule Details: Remove Account From Domain Admin Group
Adversaries may interrupt availability of system and network resources by inhibiting access to
accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex:
changed credentials) to remove access to accounts.
Rule ID
powershell_scriptblock_48

Query
{'selection': {'ScriptBlockText|contains|all': ['Remove-ADGroupMember', '-
Identity ', '-Members ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,48a45d45-8112-416b-8a67-46e03a4b2107
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1531 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1531/T1531.md#ato
mic-test-3---remove-account-from-domain-admin-group 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/26 medium Unknown
Rule Details: Suspicious Hyper-V Cmdlets
Adversaries may carry out malicious operations using a virtual instance to avoid detection.
Rule ID
powershell_scriptblock_49
Query
{'selection': {'ScriptBlockText|contains': ['New-VM', 'Set-VMFirmware', 'Start-
VM']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,42d36aa1-3240-4db0-8257-e0118dcdd9cd
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.006 
References
https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-
hyper-v 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.006/T1564.006
.md#atomic-test-3---create-and-start-hyper-v-virtual-machine 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/09 medium Legitimate PowerShell scripts
Rule Details: Zip A Folder With PowerShell For Staging In Temp - PowerShell Script
Use living off the land tools to zip a file and stage it in the Windows temporary folder for later
exfiltration.
Rule ID
powershell_scriptblock_50
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['Compress-Archive ', ' -
Path ', ' -DestinationPath ', '$env:TEMP\\']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,b7a3c9a3-09ea-4934-8864-6a32cacd98d9
Author: Nasreddine Bencherchali (Nextron Systems), frack113

Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1074.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1074.001/T1074.001
.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/20 medium Unknown
Rule Details: PowerShell ShellCode
Detects Base64 encoded Shellcode.
Rule ID
powershell_scriptblock_52
Query
{'selection': {'ScriptBlockText|contains': 'AAAAYInlM'}, 'selection2': {'ScriptBlockT
ext|contains': ['OiCAAAAYInlM', 'OiJAAAAYInlM']}, 'condition': 'selection and selecti
on2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,16b37b70-6fcf-4814-a092-c36bd3aafcbd
Author: David Ledbetter (shellcode), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1055 
References
https://twitter.com/cyb3rops/status/1063072865992523776 
Severity

74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/11/17 high Unknown
Rule Details: Suspicious Eventlog Clear
Detects usage of known powershell cmdlets such as "Clear-EventLog" to clear the windows
event logs.
Rule ID
powershell_scriptblock_53
Query
{'selection': {'ScriptBlockText|contains': ['Clear-EventLog ', 'Remove-
EventLog ', 'Limit-EventLog ', 'Clear-WinEvent ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,0f017df3-8f5a-414f-ad6b-24aff1128278
Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.001 
References
https://twitter.com/oroneequalsone/status/1568432028361830402 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.001/T1070.001
.md 
https://eqllib.readthedocs.io/en/latest/analytics/5b223758-07d6-4100-9e11-
238cfdd0fe97.html 
Severity
49
Suppression Logic Based On

computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/09/ mediu Rare need to clear logs before doing something. Sometimes used by installers or cleaner
scripts. The script should be investigated to determine if it's legitimate
ental 12 m
Rule Details: Powershell Local Email Collection
Adversaries may target user email on local systems to collect sensitive information. Files
containing email data can be acquired from a users local system, such as Outlook storage or
cache files.
Rule ID
powershell_scriptblock_54
Query
{'selection': {'ScriptBlockText|contains': ['Get-
Inbox.ps1', 'Microsoft.Office.Interop.Outlook', 'Microsoft.Office.Interop.Outlook.olD
efaultFolders', '-comobject outlook.application']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,2837e152-93c8-43d2-85ba-c3cd3c2ae614
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1114.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1114.001/T1114.001.
md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/07/21 medium Unknown
Rule Details: Suspicious FromBase64String Usage On Gzip Archive - Ps Script
Detects attempts of decoding a base64 Gzip archive in a PowerShell script. This technique is
often used as a method to load malicious content into memory afterward.
Rule ID
powershell_scriptblock_55
Query
{'selection': {'ScriptBlockText|contains|all': ['FromBase64String', 'MemoryStream', '
H4sI']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,df69cb1d-b891-4cd9-90c7-d617d90100ce
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=43 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium Legitimate administrative script
Rule Details: PowerShell ADRecon Execution
Detects execution of ADRecon.ps1 for AD reconnaissance which has been reported to be
actively used by FIN7.
Rule ID
powershell_scriptblock_56

Query
{'selection': {'ScriptBlockText|contains': ['Function Get-ADRExcelComOb', 'Get-
ADRGPO', 'Get-ADRDomainController', 'ADRecon-
Report.xlsx']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bf72941a-cba0-41ea-b18c-9aca3925690d
Author: Bhabesh Raj
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/sense-of-
security/ADRecon/blob/11881a24e9c8b207f31b56846809ce1fb189bcc9/ADRecon.ps1

https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-
disguises-its-malware-as-an-ethical-hackers-c23c9a75e319 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/16 high Unknown
Rule Details: Access to Browser Login Data
Adversaries may acquire credentials from web browsers by reading files specific to the target
browser. Web browsers commonly save credentials such as website usernames and passwords
so that they do not need to be entered manually in the future. Web browsers typically store the
credentials in an encrypted format within a credential store.
Rule ID
powershell_scriptblock_57
Query

{'selection_cmd': {'ScriptBlockText|contains|all': ['Copy-Item', '-
Destination']}, 'selection_path': {'ScriptBlockText|contains': ['\\Opera Software\\Op
era Stable\\Login Data', '\\Mozilla\\Firefox\\Profiles', '\\Microsoft\\Edge\\User Dat
a\\Default', '\\Google\\Chrome\\User Data\\Default\\Login Data', '\\Google\\Chrome\\U
ser Data\\Default\\Login Data For Account']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,fc028194-969d-4122-8abe-0470d5b8f12f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555.003/T1555.003
.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/30 medium Unknown
Rule Details: Abuse of Service Permissions to Hide Services Via Set-Service - PS
Detects usage of the "Set-Service" powershell cmdlet to configure a new SecurityDescriptor that
allows a service to be hidden from other utilities such as "sc.exe", "Get-Service"...etc. (Works
only in powershell 7.)
Rule ID
powershell_scriptblock_58
Query
{'selection': {'ScriptBlockText|contains|all': ['Set-
Service ', 'DCLCWPDTSD'], 'ScriptBlockText|contains': ['-SecurityDescriptorSddl ', '-
sd ']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,953945c5-22fe-4a92-9f8a-a9edc1e522da
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1574.011 
References
https://twitter.com/Alh4zr3d/status/1580925761996828672 
https://learn.microsoft.com/en-
us/powershell/module/microsoft.powershell.management/set-service?view=powershell-
7.2 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/17 high Rare intended use of hidden services
Rare FP could occure due to the non linearity of the ScriptBlockText log
Rule Details: Computer Discovery And Export Via Get-ADComputer Cmdlet - PowerShell
Detects usage of the Get-ADComputer cmdlet to collect computer information and output it to a
file.
Rule ID
powershell_scriptblock_59
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-ADComputer ', ' -
Filter *'], 'ScriptBlockText|contains': [' | Select ', 'Out-File', 'Set-
Content', 'Add-Content']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,db885529-903f-4c5d-9864-28fe199e6370
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html 
https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-beware-a-case-
for-post-ransomware-investigations/ 
https://www.cisa.gov/uscert/sites/default/files/publications/aa22-
320a_joint_csa_iranian_government-
sponsored_apt_actors_compromise_federal%20network_deploy_crypto%20miner_cred
ential_harvester.pdf 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/11/ mediu Legitimate admin scripts may use the same technique, it's better to exclude specific
computers or users who execute these commands or scripts often
ental 17 m
Rule Details: PowerShell PSAttack
Detects the use of PSAttack PowerShell hack tool
Rule ID
powershell_scriptblock_60
Query
{'selection': {'ScriptBlockText|contains': 'PS ATTACK!!!'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source

SigmaHQ,b7ec41a4-042c-4f31-a5db-d0fcde9fa5c5
Author: Sean Metcalf (source), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://adsecurity.org/?p=2921 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/05 high Unknown
Rule Details: PowerShell Invoke-NinjaCopy script
Detects PowerShell scripts that contain the default exported functions used on Invoke-
NinjaCopy. Attackers can use Invoke-NinjaCopy to read SYSTEM files that are normally locked,
such as the NTDS.dit file or registry hives.
Rule ID
powershell_scriptblock_61
Query
{'selection1': {'ScriptBlockText|contains': ['StealthReadFile', 'StealthReadFileAddr'
, 'StealthCloseFileDelegate', 'StealthOpenFile', 'StealthCloseFile', 'Invoke-
NinjaCopy']}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 
References
N/A
Severity

49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/23 medium N/A
Rule Details: Delete Volume Shadow Copies via WMI with PowerShell - PS Script
Deletes Windows Volume Shadow Copies with PowerShell code and Get-WMIObject. This
technique is used by numerous ransomware families such as Sodinokibi/REvil.
Rule ID
powershell_scriptblock_62
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-
WmiObject', 'Win32_Shadowcopy', '.Delete()']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e17121b4-ef2a-4418-8a59-12fb1631fa9e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#ato
mic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-powershell 
Severity
80
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/12/26 high Unknown
Rule Details: PowerShell ICMP Exfiltration
Detects Exfiltration Over Alternative Protocol - ICMP. Adversaries may steal data by exfiltrating it
over an un-encrypted network protocol other than that of the existing command and control
channel.
Rule ID
powershell_scriptblock_63
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object', 'System.Net.NetworkInformation.Ping', '.Send(']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4c4af3cd-2115-479c-8193-6b8bfce9001c
Author: Bartlomiej Czyz @bczyz1, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0010 , T1048.003 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048.003/T1048.003
.md#atomic-test-2---exfiltration-over-alternative-protocol---icmp 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/10 medium Legitimate usage of System.Net.NetworkInformation.Ping class
Rule Details: AD Groups Or Users Enumeration Using PowerShell - ScriptBlock
Adversaries may attempt to find domain-level groups and permission settings. The knowledge of
domain-level permission groups can help adversaries determine which groups exist and which

users belong to a particular group. Adversaries may use this information to determine which
users have elevated permissions, such as domain administrators.
Rule ID
powershell_scriptblock_64
Query
{'test_2': {'ScriptBlockText|contains': 'get-
ADPrincipalGroupMembership'}, 'test_7': {'ScriptBlockText|contains|all': ['get-
aduser', '-f ', '-pr ', 'DoesNotRequirePreAuth']}, 'condition': '1 of test_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,88f0884b-331d-403d-a3a1-b668cf035603
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1069.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002
.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/15 low Unknown
Rule Details: Tamper Windows Defender Remove-MpPreference - ScriptBlockLogging
Detects attempts to remove windows defender configuration using the 'MpPreference' cmdlet.
Rule ID
powershell_scriptblock_65
Query

{'selection_remove': {'ScriptBlockText|contains': 'Remove-
MpPreference'}, 'selection_tamper': {'ScriptBlockText|contains': ['-
ControlledFolderAccessProtectedFolders ', '-AttackSurfaceReductionRules_Ids ', '-
AttackSurfaceReductionRules_Actions ', '-
CheckForSignaturesBeforeRunningScan ']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,ae2bdd58-0681-48ac-be7f-58ab4e593458
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562.001 
References
https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/windows-10-
controlled-folder-access-event-search/ba-p/2326088 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/05 high Legitimate PowerShell scripts
Rule Details: Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell
Detects Obfuscated Powershell via COMPRESS OBFUSCATION.
Rule ID
powershell_scriptblock_66
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['new-
object', 'text.encoding]::ascii'], 'ScriptBlockText|contains': ['system.io.compressio
n.deflatestream', 'system.io.streamreader'], 'ScriptBlockText|endswith': 'readtoend'}
, 'condition': 'selection_4104'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,20e5497e-331c-4cd5-8d36-935f6e2a9a07
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium Unknown
Rule Details: Potential Data Exfiltration Via Audio File
Detects potential exfiltration attempt via audio file using PowerShell.
Rule ID
powershell_scriptblock_67
Query
{'selection_main': {'ScriptBlockText|contains|all': ['[System.Math]::', '[IO.FileMode
]::', 'BinaryWriter']}, 'selection_header_wav': {'ScriptBlockText|contains|all': ['0x
52', '0x49', '0x46', '0x57', '0x41', '0x56', '0x45', '0xAC']}, 'condition': 'selectio
n_main and 1 of selection_header_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e4f93c99-396f-47c8-bb0f-201b1fa69034
Author: Nasreddine Bencherchali (Nextron Systems)

Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/gtworek/PSBits/blob/e97cbbb173b31cbc4d37244d3412de0a114dacf
b/NoDLP/bin2wav.ps1 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/16 medium Unknown
Rule Details: Create Volume Shadow Copy with Powershell
Adversaries may attempt to access or create a copy of the Active Directory domain database in
order to steal credential information.
Rule ID
powershell_scriptblock_68
Query
{'selection': {'ScriptBlockText|contains|all': ['win32_shadowcopy', ').Create(', 'Cli
entAccessible']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,afd12fed-b0ec-45c9-a13d-aa86625dac81
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003.003 
References
https://attack.mitre.org/datasources/DS0005/ 
Severity
74

Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/12 high Legitimate PowerShell scripts
Rule Details: Invoke-Obfuscation Obfuscated IEX Invocation - PowerShell
Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-
Obfuscation framework from the following code block \u2014.
Rule ID
powershell_scriptblock_69
Query
{'selection_iex': [{'ScriptBlockText|re': '\\$PSHome\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$PSHome\\['}, {'ScriptBlockText|re': '\\$ShellId\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$ShellId\\
['}, {'ScriptBlockText|re': '\\$env:Public\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$env:Public\\
['}, {'ScriptBlockText|re': '\\$env:ComSpec\\[(\\s*\\d{1,3}\\s*,)
{2}'}, {'ScriptBlockText|re': '\\*mdr\\*\\W\\s*\\)\\.Name'}, {'ScriptBlockText|re': '
\\$VerbosePreference\\.ToString\\('}], 'condition': 'selection_iex'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1b9dc62e-6e9e-42a3-8990-94d7a10007f7
Author: Daniel Bohannon (@Mandiant/@FireEye), oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-
Obfuscation/blob/f20e7f843edd0a3a7716736e9eddfa423395dd26/Out-
ObfuscatedStringCommand.ps1#L873-L888 
Severity
74
Suppression Logic Based On

computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/11/08 high Unknown
Rule Details: Malicious ShellIntel PowerShell Commandlets
Detects Commandlet names from ShellIntel exploitation scripts.
Rule ID
powershell_scriptblock_70
Query
{'selection': {'ScriptBlockText|contains': ['Invoke-SMBAutoBrute', 'Invoke-
GPOLinks', 'Invoke-Potato']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,402e1e1d-ad59-47b6-bf80-1ee44985b3a7
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/Shellntel/scripts/ 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high Unknown
Rule Details: Change User Agents with WebRequest
Adversaries may communicate using application layer protocols associated with web traffic to
avoid detection/network filtering by blending in with existing traffic. Commands to the remote

system, and often the results of those commands, will be embedded within the protocol traffic
between the client and server.
Rule ID
powershell_scriptblock_71
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke-WebRequest', '-
UserAgent ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d4488827-73af-4f8d-9244-7b7662ef046e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1071.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1071.001/T1071.001
.md#t1071001---web-protocols 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/23 medium Unknown
Rule Details: Powershell Timestomp
Adversaries may modify file time attributes to hide new or changes to existing files.
Timestomping is a technique that modifies the timestamps of a file (the modify, access, create,
and change times), often to mimic files that are in the same folder.
Rule ID
powershell_scriptblock_72
Query

{'selection_ioc': {'ScriptBlockText|contains': ['.CreationTime =', '.LastWriteTime ='
, '.LastAccessTime =', '[IO.File]::SetCreationTime', '[IO.File]::SetLastAccessTime',
'[IO.File]::SetLastWriteTime']}, 'condition': 'selection_ioc'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c6438007-e081-42ce-9483-b067fbef33c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.006/T1070.006
.md 
https://www.offensive-security.com/metasploit-unleashed/timestomp/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/03 medium Legitimate admin script
Rule Details: Powershell MsXml COM Object
Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a
powerful interactive command-line interface and scripting environment included in the Windows
operating system. (Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a
number of actions, including discovery of information and execution of code.
Rule ID
powershell_scriptblock_73
Query
{'selection': {'ScriptBlockText|contains|all': ['New-Object', '-
ComObject', 'MsXml2.', 'XmlHttp']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,78aa1347-1517-4454-9982-b338d6df8343
Author: frack113, MatilJ
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.001/T1059.001
.md#atomic-test-7---powershell-msxml-com-object---with-prompt 
https://docs.microsoft.com/en-us/previous-
versions/windows/desktop/ms766431(v=vs.85) 
https://www.trendmicro.com/en_id/research/22/e/uncovering-a-kingminer-botnet-attack-
using-trend-micro-managed-x.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/19 medium Legitimate administrative script
Rule Details: User Discovery And Export Via Get-ADUser Cmdlet - PowerShell
Detects usage of the Get-ADUser cmdlet to collect user information and output it to a file.
Rule ID
powershell_scriptblock_74
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-ADUser ', ' -
Filter *'], 'ScriptBlockText|contains': [' > ', ' | Select ', 'Out-File', 'Set-
Content', 'Add-Content']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c2993223-6da8-4b1a-88ee-668b8bf315e9
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html 
https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-beware-a-case-
for-post-ransomware-investigations/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/11/ mediu Legitimate admin scripts may use the same technique, it's better to exclude specific
computers or users who execute these commands or scripts often
ental 17 m
Rule Details: Active Directory Group Enumeration With Get-AdGroup
Detects usage of the "Get-AdGroup" cmdlet to enumerate Groups within Active Directory.
Rule ID
powershell_scriptblock_75
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-AdGroup ', '-
Filter']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8c3a6607-b7dc-4f0d-a646-ef38c00b76ee

Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1069.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/03/17 low Unknown
Rule Details: WMIC Unquoted Services Path Lookup - PowerShell
Detects known WMI recon method to look for unquoted service paths, often used by pentest
inside of powershell scripts attackers enum scripts.
Rule ID
powershell_scriptblock_76
Query
{'selection': {'ScriptBlockText|contains': ['Get-
WmiObject ', 'gwmi '], 'ScriptBlockText|contains|all': [' Win32_Service ', 'Name', 'D
isplayName', 'PathName', 'StartMode']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,09658312-bc27-4a3b-91c5-e49ab9046d1b
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1047 , T1059.001 
References

https://github.com/nccgroup/redsnarf/blob/35949b30106ae543dc6f2bc3f1be10c6d9a8d
40e/redsnarf.py 
https://github.com/S3cur3Th1sSh1t/Creds/blob/eac23d67f7f90c7fc8e3130587d86158c2
2aa398/PowershellScripts/jaws-enum.ps1 
https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/20 medium Unknown
Rule Details: Get-ADUser Enumeration Using UserAccountControl Flags
Detects AS-REP roasting is an attack that is often-overlooked. It is not very common as you have
to explicitly set accounts that do not require pre-authentication.
Rule ID
powershell_scriptblock_77
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-ADUser', '-
Filter', 'useraccountcontrol', '-band', '4194304']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,96c982fe-3d08-4df4-bed2-eb14e02f21c8
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1033 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002
.md#atomic-test-11---get-aduser-enumeration-using-useraccountcontrol-flags-as-rep-
roasting 

https://shellgeek.com/useraccountcontrol-flags-to-manipulate-properties/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 medium Legitimate PowerShell scripts
Rule Details: Windows Defender Exclusions Added - PowerShell
Detects modifications to the Windows Defender configuration settings using PowerShell to add
exclusions.
Rule ID
powershell_scriptblock_79
Query
{'selection_args_exc': {'ScriptBlockText|contains': [' -ExclusionPath ', ' -
ExclusionExtension ', ' -ExclusionProcess ', ' -
ExclusionIpAddress ']}, 'selection_args_pref': {'ScriptBlockText|contains': ['Add-
MpPreference ', 'Set-MpPreference ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c1344fa2-323b-4d2e-9176-84b4d4821c88
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1562 
References
https://www.elastic.co/guide/en/security/current/windows-defender-exclusions-added-
via-powershell.html 
Severity
49
Suppression Logic Based On
computer_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/16 medium Unknown
Rule Details: Suspicious Get-ADReplAccount
The DSInternals PowerShell Module exposes several internal features of Active Directory and
Microsoft Entra ID. These include FIDO2 and NGC key auditing, offline ntds.dit file manipulation,
password auditing, DC recovery from IFM backups and password hash calculation.
Rule ID
powershell_scriptblock_80
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-ADReplAccount', '-All ', '-
Server ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,060c3ef1-fd0a-4091-bf46-e7d625f60b73
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003.006 
References
https://www.powershellgallery.com/packages/DSInternals 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.006/T1003.006
.md#atomic-test-2---run-dsinternals-get-adreplaccount 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/06 medium Legitimate PowerShell scripts

Rule Details: PowerShell Suspicious Script with Audio Capture Capabilities
Detects PowerShell scripts that can record audio, a common feature in popular post-exploitation
tooling.
Rule ID
powershell_scriptblock_81
Query
{'selection1': {'ScriptBlockText|contains': 'Get-
MicrophoneAudio'}, 'selection2': {'ScriptBlockText|contains': 'waveInGetNumDevs'}, 's
election3': {'ScriptBlockText|contains': 'mciSendStringA'}, 'selection4': {'UserId':
'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and selection3)) and (not selection4)'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1123 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/19 medium N/A
Rule Details: PowerShell Suspicious Script with Clipboard Retrieval Capabilities
Detects PowerShell scripts that can get the contents of the clipboard, which attackers can abuse
to retrieve sensitive information like credentials, messages, etc.
Rule ID
powershell_scriptblock_82
Query

{'selection1': {'ScriptBlockText|contains': 'Get-
Clipboard'}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1115 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/12 medium N/A
Rule Details: PowerShell Get-Process LSASS in ScriptBlock
Detects a Get-Process command on lsass process, which is in almost all cases a sign of
malicious activity.
Rule ID
powershell_scriptblock_83
Query
{'selection': {'ScriptBlockText|contains': 'Get-
Process lsass'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,84c174ab-d3ef-481f-9c86-a50d0b8e3edb
Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003.001 
References
https://twitter.com/PythonResponder/status/1385064506049630211 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2021/04/2 high Legitimate certificate exports invoked by administrators or users (depends on processes in
the environment - filter if unusable)
3
Rule Details: Password Policy Discovery With Get-AdDefaultDomainPasswordPolicy
Detetcts PowerShell activity in which Get-Addefaultdomainpasswordpolicy is used to get the
default password policy for an Active Directory domain.
Rule ID
powershell_scriptblock_84
Query
{'selection': {'ScriptBlockText|contains': 'Get-
AdDefaultDomainPasswordPolicy'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,bbb9495b-58fc-4016-b9df-9a3a1b67ca82
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1201 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1201/T1201.md#ato

mic-test-9---enumerate-active-directory-password-policy-with-get-
addefaultdomainpasswordpolicy 
https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-
addefaultdomainpasswordpolicy 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/17 low Legitimate PowerShell scripts
Rule Details: Suspicious PowerShell Invocations - Generic
Detects suspicious PowerShell invocation command parameters.
Rule ID
powershell_scriptblock_85
Query
{'selection_encoded': {'ScriptBlockText|contains': [' -enc ', ' -
EncodedCommand ', ' -ec ']}, 'selection_hidden': {'ScriptBlockText|contains': [' -
w hidden ', ' -window hidden ', ' -windowstyle hidden ', ' -
w 1 ']}, 'selection_noninteractive': {'ScriptBlockText|contains': [' -noni ', ' -
noninteractive ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,ed965133-513f-41d9-a441-e38076a0798f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
74

Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/12 high Very special / sneaky PowerShell scripts
Rule Details: NTFS Alternate Data Stream
Detects writing data into NTFS alternate data streams from powershell. Needs Script Block
Logging.
Rule ID
powershell_scriptblock_88
Query
{'selection_content': {'ScriptBlockText|contains': ['set-content', 'add-
content']}, 'selection_stream': {'ScriptBlockText|contains': '-
stream'}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8c521530-5169-495d-a199-0a3a881ad24e
Author: Sami Ruohonen
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004
.md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2018/07/24 high Unknown
Rule Details: Suspicious Invoke-Item From Mount-DiskImage
Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to deliver
malicious payloads that may not be tagged with MOTW.
Rule ID
powershell_scriptblock_89
Query
{'selection': {'ScriptBlockText|contains|all': ['Mount-DiskImage ', '-
ImagePath ', 'Get-Volume', '.DriveLetter', 'invoke-
item ', '):\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,902cedee-0398-4e3a-8183-6f3a89773a96
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005
.md#atomic-test-2---mount-an-iso-image-and-run-executable-from-the-iso 
https://docs.microsoft.com/en-us/powershell/module/storage/mount-diskimage?
view=windowsserver2022-ps 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/01 medium Legitimate PowerShell scripts
Rule Details: PowerShell WMI Win32_Product Install MSI

Detects the execution of an MSI file using PowerShell and the WMI Win32_Product class.
Rule ID
powershell_scriptblock_90
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke-CimMethod ', '-
ClassName ', 'Win32_Product ', '-MethodName ', '.msi']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,91109523-17f0-4248-a800-f81d9e7c081d
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1218.007 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007
.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/24 medium Unknown
Rule Details: Suspicious GetTypeFromCLSID ShellExecute
Detects suspicious Powershell code that execute COM Objects.
Rule ID
powershell_scriptblock_92
Query
{'selection': {'ScriptBlockText|contains|all': ['::GetTypeFromCLSID(', '.ShellExecute
(']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,8bc063d5-3a3a-4f01-a140-bc15e55e8437
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1546.015 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.015/T1546.015
.md#atomic-test-2---powershell-execute-com-object 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/02 medium Legitimate PowerShell scripts
Rule Details: Silence.EDA Detection
Detects Silence EmpireDNSAgent as described in the Group-IP report.
Rule ID
powershell_scriptblock_93
Query
{'empire': {'ScriptBlockText|contains|all': ['System.Diagnostics.Process', 'Stop-
Computer', 'Restart-Computer', 'Exception in execution', '$cmdargs', 'Close-
Dnscat2Tunnel']}, 'dnscat': {'ScriptBlockText|contains|all': ['set type=$LookupType`n
server', '$Command | nslookup 2>&1 | Out-String', 'New-
RandomDNSField', '[Convert]::ToString($SYNOptions, 16)', '$Session.Dead = $True', '$S
ession["Driver"] -eq']}, 'condition': 'empire and dnscat'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,3ceb2083-a27f-449a-be33-14ec1b7cc973
Author: Alina Stepchenkova, Group-IB, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1071.004 , T1572 , TA0040 , T1529 
References
https://www.group-ib.com/resources/threat-research/silence_2.0.going_global.pdf 
Severity
95
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/11/01 critical Unknown
Rule Details: Potential Active Directory Enumeration Using AD Module - PsScript
Detects usage of the "Import-Module" cmdlet to load the
"Microsoft.ActiveDirectory.Management.dl" DLL. Which is often used by attackers to perform AD
enumeration.
Rule ID
powershell_scriptblock_94
Query
{'selection_generic': {'ScriptBlockText|contains|all': ['Import-
Module ', 'Microsoft.ActiveDirectory.Management.dll']}, 'selection_specific': {'Scrip
tBlockText|contains': 'ipmo Microsoft.ActiveDirectory.Management.dll'}, 'condition':
'1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enable
Rule Source
SigmaHQ,9e620995-f2d8-4630-8430-4afd89f77604
Author: frack113, Nasreddine Bencherchali

Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/samratashok/ADModule 
https://twitter.com/cyb3rops/status/1617108657166061568?s=20 
https://www.ired.team/offensive-security-experiments/active-directory-kerberos-
abuse/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/22 medium Legitimate use of the library for administrative activity
Rule Details: Automated Collection Bookmarks Using Get-ChildItem PowerShell
Adversaries may enumerate browser bookmarks to learn more about compromised hosts.
Browser bookmarks may reveal personal information about users (ex: banking sites, interests,
social media, etc.) as well as details about internal network resources such as servers,
tools/dashboards, or other related infrastructure.
Rule ID
powershell_scriptblock_95
Query
{'selection': {'ScriptBlockText|contains|all': ['Get-ChildItem', ' -Recurse ', ' -
Path ', ' -Filter Bookmarks', ' -ErrorAction SilentlyContinue', ' -
Force']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e0565f5d-d420-4e02-8a68-ac00d864f9cf
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1217 

References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1217.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/13 low Unknown
Rule Details: SyncAppvPublishingServer Execution to Bypass Powershell Restriction
Detects SyncAppvPublishingServer process execution which usually utilized by adversaries to
bypass PowerShell execution restrictions.
Rule ID
powershell_scriptblock_96
Query
{'selection': {'ScriptBlockText|contains': 'SyncAppvPublishingServer.exe'}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,dddfebae-c46f-439c-af7a-fdb6bde90218
Author: Ensar Şamil, @sblmsrsn, OSCD Community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1218 
References
https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/ 
Severity
49
Suppression Logic Based On
computer_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/05 medium App-V clients
Rule Details: Disable Powershell Command History
Detects scripts or commands that disabled the Powershell command history by removing
psreadline module.
Rule ID
powershell_scriptblock_97
Query
{'selection': {'ScriptBlockText|contains|all': ['Remove-
Module', 'psreadline']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,602f5669-6927-4688-84db-0d4b7afb2150
Author: Ali Alwashali
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://twitter.com/DissectMalware/status/1062879286749773824 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/21 high Legitimate script that disables the command history
Rule Details: Manipulation of User Computer or Group Security Principals Across AD
Adversaries may create a domain account to maintain access to victim systems. Domain
accounts are those managed by Active Directory Domain Services where access and

permissions are configured across systems and services that are part of that domain.
Rule ID
powershell_scriptblock_98
Query
{'selection': {'ScriptBlockText|contains': 'System.DirectoryServices.AccountManagemen
t'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,b29a93fb-087c-4b5b-a84d-ee3309e69d08
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1136.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.002/T1136.002.
md#atomic-test-3---create-a-new-domain-account-using-powershell 
https://docs.microsoft.com/en-
us/dotnet/api/system.directoryservices.accountmanagement?view=dotnet-plat-ext-
6.0 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/28 medium Legitimate administrative script
Rule Details: PowerShell Suspicious Payload Encoded and Compressed
Identifies the use of .NET functionality for decompression and base64 decoding combined in
PowerShell scripts, which malware and security tools heavily use to deobfuscate payloads and
load them directly in memory to bypass defenses.
Rule ID

powershell_scriptblock_99
Query
{'selection1': {'ScriptBlockText|contains': 'System.IO.Compression.DeflateStream'}, '
selection2': {'ScriptBlockText|contains': 'System.IO.Compression.GzipStream'}, 'selec
tion3': {'ScriptBlockText|contains': 'IO.Compression.DeflateStream'}, 'selection4': {
'ScriptBlockText|contains': 'IO.Compression.GzipStream'}, 'selection5': {'ScriptBlock
Text|contains': 'FromBase64String'}, 'selection6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or selection2 or selection3 or selection4) and select
ion5 and (not selection6)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 , T1140 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/19 medium Legitimate PowerShell Scripts which makes use of compression and encoding.
Rule Details: Powershell Trigger Profiles by Add_Content
Adversaries may gain persistence and elevate privileges by executing malicious content
triggered by PowerShell profiles.
Rule ID
powershell_scriptblock_100
Query
{'selection': {'ScriptBlockText|contains|all': ['Add-Content', '$profile', '-
Value'], 'ScriptBlockText|contains': ['Start-
Process', '""']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,05b3e303-faf0-4f4a-9b30-46cc13e69152
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1546.013 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.013/T1546.013
.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/18 medium Unknown
Rule Details: Windows Screen Capture with CopyFromScreen
Adversaries may attempt to take screen captures of the desktop to gather information over the
course of an operation. Screen capturing functionality may be included as a feature of a remote
access tool used in post-compromise operations.
Rule ID
powershell_scriptblock_101
Query
{'selection': {'ScriptBlockText|contains': '.CopyFromScreen'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,d4a11f63-2390-411c-9adf-d791fd152830

Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1113 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T1113.md#ato
mic-test-6---windows-screen-capture-copyfromscreen 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/28 medium Unknown
Rule Details: Clear PowerShell History - PowerShell
Detects keywords that could indicate clearing PowerShell history.
Rule ID
powershell_scriptblock_102
Query
{'selection1a': {'ScriptBlockText|contains': ['del', 'Remove-
Item', 'rm']}, 'selection1b': {'ScriptBlockText|contains': '(Get-
PSReadlineOption).HistorySavePath'}, 'selection_2': {'ScriptBlockText|contains|all':
['Set-PSReadlineOption', '–
HistorySaveStyle', 'SaveNothing']}, 'selection_3': {'ScriptBlockText|contains|all': [
'Set-PSReadlineOption', '-
HistorySaveStyle', 'SaveNothing']}, 'condition': '1 of selection_* or all of selectio
n1*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,26b692dc-1722-49b2-b496-a8258aa6371d
Author: Ilyas Ochkov, Jonhnathan Ribeiro, Daniil Yugoslavskiy, oscd.community
Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0005 , T1070.003 
References
https://gist.github.com/hook-s3c/7363a856c3cdbadeb71085147f042c1a 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/25 medium Legitimate PowerShell scripts
Rule Details: PowerShell Share Enumeration Script
Detects scripts that contain PowerShell functions, structures, or Windows API functions related to
windows share enumeration activities. Attackers, mainly ransomware groups, commonly identify
and inspect network shares, looking for critical information for encryption and/or exfiltration.
Rule ID
powershell_scriptblock_103
Query
{'selection1': {'ScriptBlockText|contains': ['Invoke-ShareFinder', 'Invoke-
ShareFinderThreaded']}, 'selection2': {'ScriptBlockText|contains': 'shi1_netname'}, '
selection3': {'ScriptBlockText|contains': 'shi1_remark'}, 'selection4': {'ScriptBlock
Text|contains': 'NetShareEnum'}, 'selection5': {'ScriptBlockText|contains': 'NetApiBu
fferFree'}, 'selection6': {'UserId': 'S-1-5-
18'}, 'condition': '(selection1 or (selection2 and selection3) or (selection4 and sel
ection5)) and (not selection6)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 , TA0007 , T1135 
References
N/A
Severity

49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/08/17 medium N/A
Rule Details: DirectorySearcher Powershell Exploitation
Enumerates Active Directory to determine computers that are joined to the domain.
Rule ID
powershell_scriptblock_104
Query
{'selection': {'ScriptBlockText|contains|all': ['New-
Object ', 'System.DirectoryServices.DirectorySearcher', '.PropertiesToLoad.Add', '.fi
ndall()', 'Properties.name']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1f6399cf-2c80-4924-ace1-6fcff3393480
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1018 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md#ato
mic-test-15---enumerate-domain-computers-within-active-directory-using-
directorysearcher 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/02/12 medium Unknown
Rule Details: Invoke-Obfuscation STDIN+ Launcher - Powershell
Detects Obfuscated use of stdin to execute PowerShell.
Rule ID
powershell_scriptblock_105
Query
{'selection_4104': {'ScriptBlockText|re': '.*cmd.{0,5}(?:/c|/r).+powershell.+(?:\\$?
\\{?input\\}?|noexit).+"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,779c8c12-0eb1-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high Unknown
Rule Details: Powershell Install a DLL in System Directory
Uses PowerShell to install/copy a file into a system directory such as "System32" or
"SysWOW64".
Rule ID
powershell_scriptblock_106

Query
{'selection_copy': {'ScriptBlockText|contains|all': ['Copy-Item ', '-
Destination ']}, 'selection_paths': {'ScriptBlockText|contains': ['\\Windows\\System3
2', '\\Windows\\SysWOW64']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,63bf8794-9917-45bc-88dd-e1b5abc0ecfd
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1556.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1556.002/T1556.002
.md#atomic-test-1---install-and-register-password-filter-dll 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/27 high Unknown
Rule Details: Deletion of Volume Shadow Copies via WMI with PowerShell - PS Script
Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-WMIObject.
This technique is used by numerous ransomware families such as Sodinokibi/REvil.
Rule ID
powershell_scriptblock_107
Query
{'selection_get': {'ScriptBlockText|contains': ['Get-WmiObject', 'gwmi', 'Get-
CimInstance', 'gcim']}, 'selection_shadowcopy': {'ScriptBlockText|contains': 'Win32_S
hadowcopy'}, 'selection_delete': {'ScriptBlockText|contains': ['.Delete()', 'Remove-
WmiObject', 'rwmi', 'Remove-CimInstance', 'rcim']}, 'condition': 'all of selection*'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
SigmaHQ,c1337eb8-921a-4b59-855b-4ba188ddcc42
Author: Tim Rauch, frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#ato
mic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-powershell 
https://www.elastic.co/guide/en/security/current/volume-shadow-copy-deletion-via-
powershell.html 
Severity
80
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/20 high Unknown
Rule Details: Code Executed Via Office Add-in XLL File
Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised
system. Office add-ins can be used to add functionality to Office programs.
Rule ID
powershell_scriptblock_108
Query
{'selection': {'ScriptBlockText|contains|all': ['new-object ', '-
ComObject ', '.application', '.RegisterXLL']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source

SigmaHQ,36fbec91-fa1b-4d5d-8df1-8d8edcb632ad
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1137.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137.006/T1137.006.
md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/28 high Unknown
Rule Details: PSAsyncShell - Asynchronous TCP Reverse Shell
Detects the use of PSAsyncShell an Asynchronous TCP Reverse Shell written in powershell.
Rule ID
powershell_scriptblock_109
Query
{'selection': {'ScriptBlockText|contains': 'PSAsyncShell'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,afd3df04-948d-46f6-ae44-25966c44b97f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/JoelGMSec/PSAsyncShell 

Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/04 high Unlikely
Rule Details: Recon Information for Export with PowerShell
Once established within a system or network, an adversary may use automated techniques for
collecting internal data.
Rule ID
powershell_scriptblock_110
Query
{'selection_action': {'ScriptBlockText|contains': ['Get-Service ', 'Get-
ChildItem ', 'Get-
Process ']}, 'selection_redirect': {'ScriptBlockText|contains': '> $env:TEMP\\'}, 'co
ndition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a9723fcc-881c-424c-8709-fd61442ab3c3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1119 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T1119.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/30 medium Unknown
Rule Details: Enable Windows Remote Management
Adversaries may use Valid Accounts to interact with remote systems using Windows Remote
Management (WinRM). The adversary may then perform actions as the logged-on user.
Rule ID
powershell_scriptblock_111
Query
{'selection_cmdlet': {'ScriptBlockText|contains': 'Enable-
PSRemoting '}, 'condition': 'selection_cmdlet'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,991a9744-f2f0-44f2-bd33-9092eba17dc3
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0008 , T1021.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.006/T1021.006
.md#atomic-test-1---enable-windows-remote-management 
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-
psremoting?view=powershell-7.2 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/07 medium Legitimate script
Rule Details: Enumerate Credentials from Windows Credential Manager With PowerShell

Adversaries may search for common password storage locations to obtain user credentials.
Passwords are stored in several places on a system, depending on the operating system or
application holding the credentials.
Rule ID
powershell_scriptblock_112
Query
{'selection_cmd': {'ScriptBlockText|contains|all': ['vaultcmd', '/listcreds:']}, 'sel
ection_option': {'ScriptBlockText|contains': ['Windows Credentials', 'Web Credentials
']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,603c6630-5225-49c1-8047-26c964553e0e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1555 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555/T1555.md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium Unknown
Rule Details: Potential Persistence Via Security Descriptors - ScriptBlock
Detects usage of certain functions and keywords that are used to manipulate security descriptors
in order to potentially set a backdoor. As seen used in the DAMP project.
Rule ID
powershell_scriptblock_114
Query

{'selection': {'ScriptBlockText|contains|all': ['win32_Trustee', 'win32_Ace', '.Acces
sMask', '.AceType', '.SetSecurityDescriptor'], 'ScriptBlockText|contains': ['\\Lsa\\J
D', '\\Lsa\\Skew1', '\\Lsa\\Data', '\\Lsa\\GBG']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,2f77047c-e6e9-4c11-b088-a3de399524cd
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/HarmJ0y/DAMP 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/05 high Unknown
Rule Details: PowerShell Script with Encryption/Decryption Capabilities
Identifies the use of Cmdlets and methods related to encryption/decryption of files in PowerShell
scripts, which malware and offensive security tools can abuse to encrypt data or decrypt
payloads to bypass security solutions.
Rule ID
powershell_scriptblock_115
Query
{'selection1': {'ScriptBlockText|contains': 'Cryptography.AESManaged'}, 'selection2':
{'ScriptBlockText|contains': 'Cryptography.RijndaelManaged'}, 'selection3': {'Script
BlockText|contains': 'Cryptography.SHA1Managed'}, 'selection4': {'ScriptBlockText|con
tains': 'Cryptography.SHA256Managed'}, 'selection5': {'ScriptBlockText|contains': 'Cr
yptography.SHA384Managed'}, 'selection6': {'ScriptBlockText|contains': 'Cryptography.
SHA512Managed'}, 'selection7': {'ScriptBlockText|contains': 'Cryptography.SymmetricAl
gorithm'}, 'selection8': {'ScriptBlockText|contains': 'PasswordDeriveBytes'}, 'select

ion9': {'ScriptBlockText|contains': 'Rfc2898DeriveBytes'}, 'selection10': {'ScriptBlo
ckText|contains': 'CipherMode'}, 'selection11': {'ScriptBlockText|contains': 'Padding
Mode'}, 'selection12': {'ScriptBlockText|contains': '.CreateEncryptor'}, 'selection13
': {'ScriptBlockText|contains': '.CreateDecryptor'}, 'selection14': {'UserId': 'S-1-
5-
18'}, 'condition': '(selection1 or selection2 or selection3 or selection4 or selectio
n5 or selection6 or selection7 or selection8 or selection9) and selection10 and selec
tion11 and (selection12 or selection13) and (not selection14)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1140 , T1027 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/01/23 medium Legitimate PowerShell Scripts which makes use of encryption.
Rule Details: Suspicious SSL Connection
Adversaries may employ a known encryption algorithm to conceal command and control traffic
rather than relying on any inherent protections provided by a communication protocol.
Rule ID
powershell_scriptblock_116
Query
{'selection': {'ScriptBlockText|contains|all': ['System.Net.Security.SslStream', 'Net
.Security.RemoteCertificateValidationCallback', '.AuthenticateAsClient']}, 'condition
': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,195626f3-5f1b-4403-93b7-e6cfd4d6a078
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1573 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1573/T1573.md#ato
mic-test-1---openssl-c2 
https://medium.com/walmartglobaltech/openssl-server-reverse-shell-from-windows-
client-aee2dbfa0926 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/23 low Legitimate administrative script
Rule Details: Potential Keylogger Activity
Detects PowerShell scripts that contains reference to keystroke capturing functions.
Rule ID
powershell_scriptblock_117
Query
{'selection': {'ScriptBlockText|contains': '[Windows.Input.Keyboard]::IsKeyDown([Syst
em.Windows.Input.Key]::'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,965e2db9-eddb-4cf6-a986-7a967df651e4

Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1056.001 
References
https://twitter.com/ScumBots/status/1610626724257046529 
https://www.virustotal.com/gui/file/d4486b63512755316625230e0c9c81655093be93876
e0d80732e7eeaf7d83476/content 
https://www.virustotal.com/gui/file/720a7ee9f2178c70501d7e3f4bcc28a4f456e200486d
bd401b25af6da3b4da62/content 
https://learn.microsoft.com/en-
us/dotnet/api/system.windows.input.keyboard.iskeydown?view=windowsdesktop-7.0 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/04 medium Unknown
Rule Details: Invoke-Obfuscation Via Use Clip - Powershell
Detects Obfuscated Powershell via use Clip.exe in Scripts.
Rule ID
powershell_scriptblock_118
Query
{'selection_4104': {'ScriptBlockText|re': '(?i).*?echo.*clip.*&&.*(Clipboard|i`?n`?
v`?o`?k`?e`?).*'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,db92dd33-a3ad-49cf-8c2c-608c3e30ace0
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high Unknown
Rule Details: Execution via CL_Mutexverifiers.ps1
Detects Execution via runAfterCancelProcess in CL_Mutexverifiers.ps1 module.
Rule ID
powershell_scriptblock_119
Query
{'selection': {'ScriptBlockText|contains|all': ['CL_Mutexverifiers.ps1', 'runAfterCan
celProcess']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,39776c99-1c7b-4ba0-b5aa-641525eee1a4
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/CL_mutexverifiers/ 
https://twitter.com/pabraeken/status/995111125447577600 
Severity
74
Suppression Logic Based On

computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/14 high Unknown
Rule Details: Bloodhound Hack Tool Usage via PowerShell
Detects the usage of PowerShell to execute Bloodhound hacktool on endpoint.
Rule ID
powershell_scriptblock_120
Query
{'selection': {'ScriptBlockText|contains': ['Invoke-BloodHound', 'Invoke-
AzureHound', 'Get-BloodHoundData']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1482 
References
https://github.com/BloodHoundAD/BloodHound 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2023/03/30 high Unknown
Rule Details: Suspicious X509Enrollment - Ps Script
Detect use of X509Enrollment.
Rule ID
powershell_scriptblock_121

Query
{'selection': {'ScriptBlockText|contains': ['X509Enrollment.CBinaryConverter', '884e2
002-217d-11da-b2a4-000e7bbb2b09']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,504d63cb-0dba-4d02-8531-e72981aace2c
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=42 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=41 
https://learn.microsoft.com/en-
us/dotnet/api/microsoft.hpc.scheduler.store.cx509enrollmentwebclassfactoryclass?
view=hpc-sdk-5.1.6115 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium Legitimate administrative script
Rule Details: Add New Windows Capability - ScriptBlock
Detects usage of the "Add-WindowsCapability" cmdlet to add new windows capabilities. Notable
capabilities could be "OpenSSH" and others.
Rule ID
powershell_scriptblock_122
Query
{'selection_cmdlet': {'ScriptBlockText|contains': 'Add-
WindowsCapability '}, 'selection_capa': {'ScriptBlockText|contains': 'OpenSSH.'}, 'co
ndition': 'all of selection_*'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,155c7fd5-47b4-49b2-bbeb-eb4fab335429
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://learn.microsoft.com/en-us/windows-
server/administration/openssh/openssh_install_firstuse?tabs=powershell 
https://www.virustotal.com/gui/file/af1c82237b6e5a3a7cdbad82cc498d298c67845d9297
1bada450023d1335e267/content 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimenta 2023/01/22 medium Legitimate usage of the capabilities by administartors or users. Filter
accordingly
l
Rule Details: Invoke-Obfuscation Via Use Rundll32 - PowerShell
Detects Obfuscated Powershell via use Rundll32 in Scripts.
Rule ID
powershell_scriptblock_123
Query
{'selection_4104': {'ScriptBlockText|contains|all': ['&&', 'rundll32', 'shell32.dll',
'shellexec_rundll'], 'ScriptBlockText|contains': ['value', 'invoke', 'comspec', 'iex
']}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts

Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,a5a30a6e-75ca-4233-8b8c-42e0f2037d3b
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/10/08 high Unknown
Rule Details: Anti-VM check with WMI Query
WMI Queries allow to inspect Windows properties like the BIOS features. This technique is used
by malware to identify virtual and sandboxed host machines, in order to evade security analysis.
Rule ID
powershell_scriptblock_124
Query
{'selection1': {'ScriptBlockText|contains': '-
query'}, 'selection2': {'ScriptBlockText|re': '.*(Get-WMIObject|gwmi) .*?-
query .*? win32_(BIOS|SystemBIOS).*?
(bochs|qemu|VBOX|VirtualBox|VM).*'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References

N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious Connection to Remote Account
Adversaries with no prior knowledge of legitimate credentials within the system or environment
may guess passwords to attempt access to accounts. Without knowledge of the password for an
account, an adversary may opt to systematically guess the password using a repetitive or
iterative mechanism.
Rule ID
powershell_scriptblock_125
Query
{'selection': {'ScriptBlockText|contains': ['System.DirectoryServices.Protocols.LdapD
irectoryIdentifier', 'System.Net.NetworkCredential', 'System.DirectoryServices.Protoc
ols.LdapConnection']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,1883444f-084b-419b-ac62-e0d0c5b3693f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1110.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1110.001/T1110.001.
md#atomic-test-2---brute-force-credentials-of-single-active-directory-domain-user-via-
ldap-against-domain-controller-ntlm-or-kerberos 
Severity
24

Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/27 low Unknown
Rule Details: Suspicious Export-PfxCertificate
Detects Commandlet that is used to export certificates from the local certificate store and
sometimes used by threat actors to steal private keys from compromised machines.
Rule ID
powershell_scriptblock_126
Query
{'selection': {'ScriptBlockText|contains': ['Export-PfxCertificate', 'export-
certificate']}, 'filter_moduleexport': {'ScriptBlockText|contains': 'CmdletsToExport
= @('}, 'condition': 'selection and not 1 of filter*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,aa7a3fce-bef5-4311-9cc1-5f04bb8c308c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1552.004 
References
https://us-cert.cisa.gov/ncas/analysis-reports/ar21-112a 
https://docs.microsoft.com/en-us/powershell/module/pki/export-pfxcertificate 
https://dev.to/iamthecarisma/managing-windows-pfx-certificates-through-powershell-
3pj 
https://learn.microsoft.com/en-us/powershell/module/pki/export-certificate?
view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name

stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experime 2021/04/2 high Legitimate certificate exports invoked by administrators or users (depends on processes
in the environment - filter if unusable)
ntal 3
Rule Details: Powershell Sensitive File Discovery
Detect adversaries enumerate sensitive files.
Rule ID
powershell_scriptblock_127
Query
{'selection_action': {'ScriptBlockText|contains': ['ls', 'get-
childitem', 'gci']}, 'selection_recurse': {'ScriptBlockText|contains': '-
recurse'}, 'selection_file': {'ScriptBlockText|contains': ['.pass', '.kdbx', '.kdb']}
, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,7d416556-6502-45b2-9bad-9d2f05f38997
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1083 
References
https://twitter.com/malmoeb/status/1570814999370801158 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/16 medium Unknown
Rule Details: Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - PowerShell

Detects Obfuscated Powershell via VAR++ LAUNCHER.
Rule ID
powershell_scriptblock_128
Query
{'selection_4104': {'ScriptBlockText|re': '(?i).*&&set.*(\\{\\d\\}){2,}\\\\"\\s+?-
f.*&&.*cmd.*/c'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,e54f5149-6ba3-49cf-b153-070d24679126
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high Unknown
Rule Details: Testing Usage of Uncommonly Used Port
Adversaries may communicate using a protocol and port paring that are typically not associated.
For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation:
Fortinet Agent Tesla April 2018) as opposed to the traditional port 443.
Rule ID
powershell_scriptblock_129
Query
{'selection': {'ScriptBlockText|contains|all': ['Test-NetConnection', '-
ComputerName ', '-

port ']}, 'filter': {'ScriptBlockText|contains': [' 443 ', ' 80 ']}, 'condition': 'se
lection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,adf876b3-f1f8-4aa9-a4e4-a64106feec06
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0011 , T1571 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1571/T1571.md#ato
mic-test-1---testing-usage-of-uncommonly-used-port-with-powershell 
https://docs.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?
view=windowsserver2022-ps 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/23 medium Legitimate administrative script
Rule Details: Troubleshooting Pack Cmdlet Execution
Detects execution of "TroubleshootingPack" cmdlets to leverage CVE-2022-30190 or action
similar to "msdt" lolbin (as described in LOLBAS).
Rule ID
powershell_scriptblock_130
Query
{'selection': {'ScriptBlockText|contains|all': ['Invoke-
TroubleshootingPack', 'C:\\Windows\\Diagnostics\\System\\PCW', '-AnswerFile', '-
Unattended']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,03409c93-a7c7-49ba-9a4c-a00badf2a153
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1202 
References
https://twitter.com/nas_bench/status/1537919885031772161 
https://lolbas-project.github.io/lolbas/Binaries/Msdt/ 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation DateRisk LevelFalse Positives
experimental2022/06/21 medium Legitimate usage of "TroubleshootingPack" cmdlet for troubleshooting
purposes
Rule Details: Invoke-Obfuscation Via Stdin - Powershell
Detects Obfuscated Powershell via Stdin in Scripts.
Rule ID
powershell_scriptblock_131
Query
{'selection_4104': {'ScriptBlockText|re': '(?i).*(set).*&&\\s?set.*
(environment|invoke|\\$\\{?input).*&&.*"'}, 'condition': 'selection_4104'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,86b896ba-ffa1-4fea-83e3-ee28a4c915c7
Author: Nikita Nazarov, oscd.community

Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/12 high Unknown
Rule Details: Suspicious Mount-DiskImage
Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to deliver
malicious payloads that may not be tagged with MOTW.
Rule ID
powershell_scriptblock_132
Query
{'selection': {'ScriptBlockText|contains|all': ['Mount-DiskImage ', '-
ImagePath ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,29e1c216-6408-489d-8a06-ee9d151ef819
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1553 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005
.md#atomic-test-1---mount-iso-image 

https://docs.microsoft.com/en-us/powershell/module/storage/mount-diskimage?
view=windowsserver2022-ps 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/01 low Legitimate PowerShell scripts
Rule Details: Suspicious PowerShell Mailbox Export to Share - PS
Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a mailbox to a
remote or local share, as used in ProxyShell exploitations.
Rule ID
powershell_scriptblock_133
Query
{'selection': {'ScriptBlockText|contains|all': ['New-MailboxExportRequest', ' -
Mailbox ', ' -FilePath \\\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,4a241dea-235b-4a7e-8d76-50d817b146c4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://youtu.be/5mqid-7zp8k?t=2481 
https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-
1.html 
https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-
49743a4ea9a1 
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/ 

Severity
95
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/26 critical Unknown
Rule Details: Data Compressed - PowerShell
An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration
in order to make it portable and minimize the amount of data sent over the network.
Rule ID
powershell_scriptblock_134
Query
{'selection': {'ScriptBlockText|contains|all': ['-Recurse', '|', 'Compress-
Archive']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,6dc5d284-69ea-42cf-9311-fb1c3932a69a
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0009 , T1560 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560/T1560.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2019/10/21 low Highly likely if archive operations are done via PowerShell.
Rule Details: PowerShell Create Local User
Detects creation of a local user via PowerShell.
Rule ID
powershell_scriptblock_135
Query
{'selection': {'ScriptBlockText|contains': 'New-
LocalUser'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,243de76f-4725-4f2e-8225-a8a69b15ad61
Author: @ROxPinTeddy
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1136.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.001/T1136.001.
md 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/11 medium Legitimate user creation
Rule Details: WMI lateral movement using MSI package
Windows Management Instrumentation (WMI) is able to install MSI packages in remote
computers. An attacker can use it to performa lateral movement and execute malicious code.
Rule ID

powershell_scriptblock_136
Query
{'selection1': {'ScriptBlockText|contains': 'win32_product'}, 'selection2': {'ScriptB
lockText|contains': 'install'}, 'selection3': {'ScriptBlockText|contains': '-
ComputerName'}, 'selection4': {'ScriptBlockText|contains': '-
Credential'}, 'condition': 'selection1 and selection2 and selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Replace Desktop Wallpaper by Powershell
An adversary may deface systems internal to an organization in an attempt to intimidate or
mislead users. This may take the form of modifications to internal websites, or directly to user
systems with the replacement of the desktop wallpaper.
Rule ID
powershell_scriptblock_137
Query
{'selection_1': {'ScriptBlockText|contains|all': ['Get-
ItemProperty', 'Registry::', 'HKEY_CURRENT_USER\\Control Panel\\Desktop\\', 'WallPape
r']}, 'selection_2': {'ScriptBlockText|contains': 'SystemParametersInfo(20,0,*,3)'},
'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,c5ac6a1e-9407-45f5-a0ce-ca9a0806a287
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0040 , T1491.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1491.001/T1491.001
.md 
Severity
24
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/26 low Unknown
Rule Details: PowerShell MiniDump Script
This rule detects PowerShell scripts capable of dumping process memory using
WindowsErrorReporting or Dbghelp.dll MiniDumpWriteDump. Attackers can use this tooling to
dump LSASS and get access to credentials.
Rule ID
powershell_scriptblock_138
Query
{'selection1': {'ScriptBlockText|contains': ['MiniDumpWriteDump', 'MiniDumpWithFullMe
mory', 'pmuDetirWpmuDiniM']}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0002 , T1059.001 , TA0006 , T1003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/05 high PowerShell scripts that use this capability for troubleshooting.
Rule Details: PowerShell PSReflect Script
Detects the use of PSReflect in PowerShell scripts. Attackers leverage PSReflect as a library
that enables PowerShell to access win32 API functions.
Rule ID
powershell_scriptblock_139
Query
{'selection1': {'ScriptBlockText|contains': ['New-InMemoryModule', 'Add-
Win32Type', 'psenum', 'DefineDynamicAssembly', 'DefineDynamicModule', 'Reflection.Typ
eAttributes', 'Reflection.Emit.OpCodes', 'Reflection.Emit.CustomAttributeBuilder', 'R
untime.InteropServices.DllImportAttribute']}, 'selection2': {'UserId': 'S-1-5-
18'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , T1106 
References
N/A
Severity
49
Suppression Logic Based On
computer_name

stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2021/10/15 medium Legitimate PowerShell scripts that make use of PSReflect to access the win32
API
n
Rule Details: Winlogon Helper DLL
Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the
secure attention sequence (SAS) triggered by Ctrl-Alt-Delete. Registry entries in
HKLM\Software[Wow6432Node]Microsoft\Windows NT\CurrentVersion\Winlogon\ and
HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ are used to manage additional
helper programs and functionalities that support Winlogon. Malicious modifications to these
Registry keys may cause Winlogon to load and execute malicious DLLs and/or executables.
Rule ID
powershell_scriptblock_140
Query
{'selection': {'ScriptBlockText|contains': 'CurrentVersion\\Winlogon'}, 'selection2':
{'ScriptBlockText|contains': ['Set-ItemProperty', 'New-
Item']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,851c506b-6b7c-4ce2-8802-c703009d03c0
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1547.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.004/T1547.004
.md 
Severity
49
Suppression Logic Based On
computer_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/10/21 medium Unknown
Rule Details: Code Executed Via Office Add-in
Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised
system. Office add-ins can be used to add functionality to Office programs.
Rule ID
powershell_scriptblock_147
Query
{'selection_xll': {'ScriptBlockText|contains|all': ['Copy', '\\Microsoft\\AddIns\\',
'.xll']}, 'selection_wll': {'ScriptBlockText|contains|all': ['Copy', '\\Microsoft\\Wo
rd\\Startup\\', '.wll']}, 'selection_xlam': {'ScriptBlockText|contains|all': ['Copy',
'\\Microsoft\\Excel\\XLSTART\\', '.xlam']}, 'selection_ppam': {'ScriptBlockText|cont
ains|all': ['Copy', '\\Microsoft\\Addins\\', '.ppam']}, 'condition': '1 of selection_
*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1137.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137.006/T1137.006.
md 
Severity
74
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2024/01/26 high Unknown
Rule Details: Potential Unconstrained Delegation Discovery Via Get-ADComputer -
ScriptBlock
Detects the use of the "Get-ADComputer" cmdlet in order to identify systems which are
configured for unconstrained delegation.
Rule ID
powershell_scriptblock_148
Query
{'selection1': {'ScriptBlockText|contains': 'Get-
ADComputer'}, 'selection2': {'ScriptBlockText|contains': ['-
Properties*TrustedForDelegation', '-Properties*TrustedToAuthForDelegation', '-
Properties*msDS-AllowedToDelegateTo', '-
Properties*PrincipalsAllowedToDelegateToAccount', '-LDAPFilter*
(userAccountControl:1.2.840.113556.1.4.803:=524288)']}, 'condition': 'selection1 and
selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enable
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0043 , T1589.002 , TA0007 , T1018 , TA0006 , T1558 
References
https://pentestlab.blog/2022/03/21/unconstrained-delegation/ 
https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer?
view=windowsserver2022-ps 
Severity
50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025-03-05 medium Legitimate use of the library for administrative activity

Rule Details: PowerShell Kerberos Ticket Dump
Detects PowerShell scripts that have the capability of dumping Kerberos tickets from LSA, which
potentially indicates an attacker's attempt to acquire credentials for lateral movement.
Rule ID
powershell_scriptblock_149
Query
{'selection1': {'ScriptBlockText|contains': 'LsaCallAuthenticationPackage'}, 'selecti
on2': {'ScriptBlockText|contains': ['KerbRetrieveEncodedTicketMessage', 'KerbQueryTic
ketCacheMessage', 'KerbQueryTicketCacheExMessage', 'KerbQueryTicketCacheEx2Message',
'KerbRetrieveTicketMessage', 'KerbDecryptDataMessage']}, 'condition': 'selection1 and
selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 , T1558 
References
N/A
Severity
75
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2023/07/26 high N/A
Rule Details: DSInternals Suspicious PowerShell Cmdlets - ScriptBlock
Detects execution and usage of the DSInternals PowerShell module. Which can be used to
perform what might be considered as suspicious activity such as dumping DPAPI backup keys or
manipulating NTDS.DIT files. The DSInternals PowerShell Module exposes several internal
features of Active Directory and Azure Active Directory. These include FIDO2 and NGC key
auditing, offline ntds.dit file manipulation, password auditing, DC recovery from IFM backups and
password hash calculation.
Rule ID

powershell_scriptblock_150
Query
{'selection': {'ScriptBlockText|contains': ['Add-ADDBSidHistory', 'Add-
ADNgcKey', 'Add-ADReplNgcKey', 'ConvertFrom-ADManagedPasswordBlob', 'ConvertFrom-
GPPrefPassword', 'ConvertFrom-ManagedPasswordBlob', 'ConvertFrom-
UnattendXmlPassword', 'ConvertFrom-UnicodePassword', 'ConvertTo-AADHash', 'ConvertTo-
GPPrefPassword', 'ConvertTo-KerberosKey', 'ConvertTo-LMHash', 'ConvertTo-
MsoPasswordHash', 'ConvertTo-NTHash', 'ConvertTo-OrgIdHash', 'ConvertTo-
UnicodePassword', 'Disable-ADDBAccount', 'Enable-ADDBAccount', 'Get-
ADDBAccount', 'Get-ADDBBackupKey', 'Get-ADDBDomainController', 'Get-
ADDBGroupManagedServiceAccount', 'Get-ADDBKdsRootKey', 'Get-
ADDBSchemaAttribute', 'Get-ADDBServiceAccount', 'Get-ADDefaultPasswordPolicy', 'Get-
ADKeyCredential', 'Get-ADPasswordPolicy', 'Get-ADReplAccount', 'Get-
ADReplBackupKey', 'Get-ADReplicationAccount', 'Get-ADSIAccount', 'Get-
AzureADUserEx', 'Get-BootKey', 'Get-KeyCredential', 'Get-LsaBackupKey', 'Get-
LsaPolicy', 'Get-SamPasswordPolicy', 'Get-SysKey', 'Get-SystemKey', 'New-
ADDBRestoreFromMediaScript', 'New-ADKeyCredential', 'New-ADNgcKey', 'New-
NTHashSet', 'Remove-ADDBObject', 'Save-DPAPIBlob', 'Set-ADAccountPasswordHash', 'Set-
ADDBAccountPassword', 'Set-ADDBBootKey', 'Set-ADDBDomainController', 'Set-
ADDBPrimaryGroup', 'Set-ADDBSysKey', 'Set-AzureADUserEx', 'Set-LsaPolicy', 'Set-
SamAccountPasswordHash', 'Set-WinUserPasswordHash', 'Test-
ADDBPasswordQuality', 'Test-ADPasswordQuality', 'Test-ADReplPasswordQuality', 'Test-
PasswordQuality', 'Unlock-ADDBAccount', 'Write-ADNgcKey', 'Write-
ADReplNgcKey']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Requirements: Script Block Logging must be enabled
Rule Source
SigmaHQ,846c7a87-8e14-4569-9d49-ecfd4276a01c
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
https://github.com/MichaelGrafnetter/DSInternals/blob/39ee8a69bbdc1cfd12c9afdd7513
b4788c4895d4/Src/DSInternals.PowerShell/DSInternals.psd1 
Severity
75
Suppression Logic Based On

computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2024-06-26 high Legitimate usage of DSInternals for administration or audit purpose.
Rule Details: Windows PowerSploit GPP Discovery
The following analytic detects the execution of the Get-GPPPassword PowerShell cmdlet, which
is used to search for unsecured credentials in Group Policy Preferences (GPP). This detection
leverages PowerShell Script Block Logging to identify specific script block text associated with
this cmdlet. Monitoring this activity is crucial as it can indicate an attempt to retrieve and decrypt
stored credentials from SYSVOL, potentially leading to unauthorized access. If confirmed
malicious, this activity could allow an attacker to escalate privileges or move laterally within the
network by exploiting exposed credentials.
Rule ID
powershell_scriptblock_151
Query
{'selection': {'ScriptBlockText|contains': ['Get-GPPPassword', 'Get-
CachedGPPPassword']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1552.006 
References
https://pentestlab.blog/2017/03/20/group-policy-preferences/ 
https://adsecurity.org/?p=2288 
https://www.hackingarticles.in/credential-dumping-group-policy-preferences-gpp/ 
https://adsecurity.org/?p=2288 
https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-
preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-
8cd617073c30 
Severity
50

Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2025-02-10 medium Unknown
Rule Details: Windows PowerView Unconstrained Delegation Discovery
The following analytic detects the use of PowerView commandlets to discover Windows
endpoints with Kerberos Unconstrained Delegation. It leverages PowerShell Script Block
Logging (EventCode=4104) to identify specific commands like `Get-DomainComputer` or `Get-
NetComputer` with the `-Unconstrained` parameter. This activity is significant as it indicates
potential reconnaissance efforts by adversaries or Red Teams to map out privileged delegation
settings in Active Directory. If confirmed malicious, this could allow attackers to identify high-
value targets for further exploitation, potentially leading to privilege escalation or lateral
movement within the network.
Rule ID
powershell_scriptblock_152
Query
{'selection1': {'ScriptBlockText|contains': ['Get-DomainComputer', 'Get-
NetComputer']}, 'selection2': {'ScriptBlockText|contains': '-
Unconstrained'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1018 
References
https://adsecurity.org/?p=1667 
https://docs.microsoft.com/en-us/defender-for-identity/cas-isp-unconstrained-
kerberos 
https://www.ired.team/offensive-security-experiments/active-directory-kerberos-
abuse/domain-compromise-via-unrestricted-kerberos-delegation 
https://www.cyberark.com/resources/threat-research-blog/weakness-within-kerberos-
delegation 
Severity

50
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2024-11-13 medium Administrators or power users may leverage PowerView for system management or
troubleshooting.
n
Rule Details: Get-ForestTrust with PowerShell Script Block
The following analytic detects the execution of the Get-ForestTrust command from PowerSploit
using PowerShell Script Block Logging (EventCode=4104). This method captures the full
command sent to PowerShell, providing detailed visibility into potentially suspicious activities.
Monitoring this behavior is crucial as it can indicate an attempt to gather domain trust
information, which is often a precursor to lateral movement or privilege escalation. If confirmed
malicious, this activity could allow an attacker to map trust relationships within the domain,
facilitating further exploitation and access to sensitive resources.
Rule ID
powershell_scriptblock_153
Query
{'selection': {'ScriptBlockText|contains': ['get-
foresttrust']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1482 
References
https://powersploit.readthedocs.io/en/latest/Recon/Get-ForestTrust/ 
https://www.splunk.com/en_us/blog/security/hunting-for-malicious-powershell-using-
script-block-logging.html 
Severity
50
Suppression Logic Based On

computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2024-11-13 medium False positives may be present. Tune as needed.
Rule Details: PowerShell Kerberos Ticket Request
Detects PowerShell scripts that have the capability of requesting kerberos tickets, which is a
common step in Kerberoasting toolkits to crack service accounts.
Rule ID
powershell_scriptblock_154
Query
{'selection1': {'ScriptBlockText|contains': 'KerberosRequestorSecurityToken'}, 'selec
tion2': {'UserId': ['S-1-5-18', 'S-1-5-
20']}, 'selection3': {'ScriptBlockText|contains': 'sentinelbreakpoints'}, 'selection4
': {'ScriptBlockText|contains': ['Set-PSBreakpoint', 'Set-
HookFunctionTabs']}, 'selection5': {'ScriptBlockText|contains|all': ['function global
', '\\windows\\sentinel\\4']}, 'condition': 'selection1 and (not selection2) and (not
((selection3 and selection4) or selection5))'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring PowerShell scripts
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0006 , T1003 , T1558 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/24 medium N/A

Process Creation Commandline Rule IDs
Rule Details: SystemNightmare Exploitation Script Execution
Detects the exploitation of PrinterNightmare to get a shell as LOCAL_SYSTEM.
Rule ID
process_creation_commandline_1
Query
{'selection': {'CommandLine|contains': ['printnightmare.gentilkiwi.com', ' /user:gent
ilguest ', 'Kiwi Legit Printer']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c01f7bd6-0c1d-47aa-9c61-187b91273a16
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0004 , T1068 
References
https://github.com/GossiTheDog/SystemNightmare 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/11 critical Unknown
Rule Details: Suspicious Reg Add Open Command
Threat actors performed dumping of SAM, SECURITY and SYSTEM registry hives using
DelegateExecute key.
Rule ID
process_creation_commandline_2
Query

{'selection_1': {'CommandLine|contains|all': ['reg', 'add', 'hkcu\\software\\classes\
\ms-
settings\\shell\\open\\command', '/ve ', '/d']}, 'selection_2': {'CommandLine|contain
s|all': ['reg', 'add', 'hkcu\\software\\classes\\ms-
settings\\shell\\open\\command', '/v', 'DelegateExecute']}, 'selection_3': {'CommandL
ine|contains|all': ['reg', 'delete', 'hkcu\\software\\classes\\ms-
settings']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,dd3ee8cc-f751-41c9-ba53-5a32ed47e563
Author: frack113, Swachchhanda Shrawan Poudel (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://thedfirreport.com/2021/12/13/diavol-ransomware/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/20 medium Unknown
Rule Details: CL_LoadAssembly.ps1 Proxy Execution
Detects the use of a Microsoft signed script to execute commands and bypassing AppLocker.
Rule ID
process_creation_commandline_3
Query
{'selection': {'CommandLine|contains': ['\\CL_LoadAssembly.ps1', 'LoadAssemblyFromPat
h ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,c57872c7-614f-4d7f-a40d-b78c8df2d30d
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-
powershell-diagnostic-scripts/ 
https://lolbas-project.github.io/lolbas/Scripts/CL_LoadAssembly/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/21 medium Unknown
Rule Details: Suspicious Characters in CommandLine
Detects suspicious Unicode characters in the command line, which could be a sign of
obfuscation or defense evasion.
Rule ID
process_creation_commandline_4
Query
{'selection_spacing_modifiers': {'CommandLine|contains': ['ˣ', '˪', 'ˢ']}, 'selection_
unicode_slashes': {'CommandLine|contains': ['⁄', '⁄']}, 'selection_unicode_hyphens':
{'CommandLine|contains': ['―', '—']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2c0d2d7b-30d6-4d14-9751-7b9113042ab9
Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/27 high Unknown
Rule Details: Firewall Disabled via Netsh.EXE
Detects netsh commands that turns off the Windows firewall.
Rule ID
process_creation_commandline_5
Query
{'selection_img': [{'Image|endswith': '\\netsh.exe'}, {'OriginalFileName': 'netsh.exe
'}], 'selection_cli_1': {'CommandLine|contains|all': ['firewall', 'set', 'opmode', 'd
isable']}, 'selection_cli_2': {'CommandLine|contains|all': ['advfirewall', 'set', 'st
ate', 'off']}, 'condition': 'selection_img and 1 of selection_cli_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,57c4bf16-227f-4394-8ec7-1b745ee061c3
Author: Fatih Sirin
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.004 
References
https://www.winhelponline.com/blog/enable-and-disable-windows-firewall-quickly-using-
command-line/ 
https://app.any.run/tasks/210244b9-0b6b-4a2c-83a3-04bd3175d017/ 

https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004
.md#atomic-test-1---disable-microsoft-defender-firewall 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/11/01 medium Legitimate administration activity
Rule Details: Ke3chang Registry Key Modifications
Detects Registry modifications performed by Ke3chang malware in campaigns running in 2019
and 2020.
Rule ID
process_creation_commandline_6
Query
{'selection1': {'CommandLine|contains': ['-Property DWORD -
name DisableFirstRunCustomize -value 2 -Force', '-Property String -
name Check_Associations -value', '-Property DWORD -name IEHarden -value 0 -
Force']}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b544661-69fc-419f-9a59-82ccc328f205
Author: Markus Neis, Swisscom
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://www.verfassungsschutz.de/embed/broschuere-2020-06-bfv-cyber-brief-2020-
01.pdf 
https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-new-tidepool-
malware/ 
Severity

95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/06/18 critical Will need to be looked for combinations of those processes
Rule Details: Potential PowerShell Obfuscation Via WCHAR
Detects suspicious encoded character syntax often used for defense evasion.
Rule ID
process_creation_commandline_7
Query
{'selection': {'CommandLine|contains': '(WCHAR)0x'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e312efd0-35a1-407f-8439-b8d434b438a6
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://twitter.com/0gtweet/status/1281103918693482496 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/09 high Unknown
Rule Details: Conti Volume Shadow Listing

Detects a command used by conti to find volume shadow backups.
Rule ID
process_creation_commandline_8
Query
{'selection': {'CommandLine|contains|all': ['vssadmin list shadows', 'log.txt']}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b30e0a7-c675-4b24-8a46-82fa67e2433d
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0042 , T1587.001 , TA0002 , T1059.003 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9d
aecaf06331a95410aa5f8/detection 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high Unknown
Rule Details: InfDefaultInstall.exe .inf Execution
Executes SCT script using scrobj.dll from a command in entered into a specially prepared INF
file.
Rule ID
process_creation_commandline_9
Query

{'selection': {'CommandLine|contains|all': ['InfDefaultInstall.exe ', '.inf']}, 'cond
ition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ce7cf472-6fcc-490a-9481-3786840b5d9b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md#ato
mic-test-4---infdefaultinstallexe-inf-execution 
https://lolbas-project.github.io/lolbas/Binaries/Infdefaultinstall/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/13 medium Unknown
Rule Details: Root Certificate Installed From Susp Locations
Adversaries may install a root certificate on a compromised system to avoid warnings when
connecting to adversary controlled web servers.
Rule ID
process_creation_commandline_10
Query
{'selection': {'CommandLine|contains|all': ['Import-Certificate', ' -
FilePath ', 'Cert:\\LocalMachine\\Root'], 'CommandLine|contains': ['\\AppData\\Local\
\Temp\\', ':\\Windows\\TEMP\\', '\\Desktop\\', '\\Downloads\\', '\\Perflogs\\', ':\\U
sers\\Public\\']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5f6a601c-2ecb-498b-9c33-660362323afa
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1553.004 
References
https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-phosphorus-
ransomware-operations/ 
https://docs.microsoft.com/en-us/powershell/module/pki/import-certificate?
view=windowsserver2022-ps 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/09 high Unlikely
Rule Details: Suspicious PrinterPorts Creation (CVE-2020-1048)
Detects new commands that add new printer port which point to suspicious file.
Rule ID
process_creation_commandline_11
Query
{'selection1': {'CommandLine|contains': 'Add-PrinterPort -
Name'}, 'selection2': {'CommandLine|contains': ['.exe', '.dll', '.bat']}, 'selection3
': {'CommandLine|contains': 'Generic / Text Only'}, 'condition': '(selection1 and sel
ection2) or selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cc08d590-8b90-413a-aff6-31d1a99678d7

Author: EagleEye Team, Florian Roth
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://windows-internals.com/printdemon-cve-2020-1048/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/13 high New printer port install on host
Rule Details: PowerShell Script Run in AppData
Detects a suspicious command line execution that invokes PowerShell with reference to an
AppData folder.
Rule ID
process_creation_commandline_12
Query
{'selection1': {'CommandLine|contains': ['powershell.exe', '\\powershell', '\\pwsh',
'pwsh.exe']}, 'selection2': {'CommandLine|contains|all': ['/c ', '\\AppData\\'], 'Com
mandLine|contains': ['Local\\', 'Roaming\\']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ac175779-025a-4f12-98b0-acdaeb77ea85
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://twitter.com/JohnLaTwC/status/1082851155481288706 
https://app.any.run/tasks/f87f1c4e-47e2-4c46-9cf4-31454c06ce03 

Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/01/09 medium Administrative scripts
Rule Details: Potential Remote Desktop Tunneling
Detects potential use of an SSH utility to establish RDP over a reverse SSH Tunnel. This can be
used by attackers to enable routing of network packets that would otherwise not reach their
intended destination.
Rule ID
process_creation_commandline_13
Query
{'selection': {'CommandLine|contains': ':3389'}, 'selection_opt': {'CommandLine|conta
ins': [' -L ', ' -P ', ' -R ', ' -pw ', ' -ssh ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8a3038e8-9c9d-46f8-b184-66234a160f6f
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1021 
References
https://www.elastic.co/guide/en/security/current/potential-remote-desktop-tunneling-
detected.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/27 medium Unknown
Rule Details: MSTSC Shadowing
Detects RDP session hijacking by using MSTSC shadowing.
Rule ID
process_creation_commandline_14
Query
{'selection': {'CommandLine|contains|all': ['noconsentprompt', 'shadow:']}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6ba5a05f-b095-4f0a-8654-b825f4f16334
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1563.002 
References
https://twitter.com/kmkz_security/status/1220694202301976576 
https://github.com/kmkz/Pentesting/blob/47592e5e160d3b86c2024f09ef04ceb87d2049
95/Post-Exploitation-Cheat-Sheet 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/24 high Unknown
Rule Details: Suspicious Scan Loop Network
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other
logical identifier on a network that may be used for Lateral Movement from the current system.

Rule ID
process_creation_commandline_15
Query
{'selection_loop': {'CommandLine|contains': ['for ', 'foreach ']}, 'selection_tools':
[{'CommandLine|re': '\\bnslookup\\b'}, {'CommandLine|re': '\\bping\\b'}], 'condition
': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f8ad2e2c-40b6-4117-84d7-20b89896ab23
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1018 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md 
https://ss64.com/nt/for.html 
https://ss64.com/ps/foreach-object.html 
Severity
49
Suppression Logic Based On
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/12 medium Legitimate script
Rule Details: Obfuscated IP Download
Detects use of an encoded/obfuscated version of an IP address (hex, octal...) in an URL
combined with a download command.
Rule ID
process_creation_commandline_16
Query
{'selection_img': {'CommandLine|contains': ['Invoke-
WebRequest', 'iwr ', 'wget ', 'curl ', 'DownloadFile', 'DownloadString']}, 'selection

_ip': [{'CommandLine|contains': ['//0x', '.0x', '.00x']}, {'CommandLine|contains|all'
: ['http://%', '%2e']}], 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cb5a2333-56cf-4562-8fcb-22ba1bca728d
Author: Florian Roth (Nextron Systems), X__Junior (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://h.43z.one/ipconverter/ 
https://twitter.com/Yasser_Elsnbary/status/1553804135354564608 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/03 medium Unknown
Rule Details: MSExchange Transport Agent Installation
Detects the Installation of a Exchange Transport Agent.
Rule ID
process_creation_commandline_17
Query
{'selection': {'CommandLine|contains': 'Install-
TransportAgent'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,83809e84-4475-4b69-bc3e-4aad8568612f

Author: Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1505.002 
References
https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-
server-or-outlook?slide=7 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/06/08 medium Legitimate installations of exchange TransportAgents. AssemblyPath is a good
indicator for this.
Rule Details: Pubprn.vbs Proxy Execution
Detects the use of the 'Pubprn.vbs' Microsoft signed script to execute commands.
Rule ID
process_creation_commandline_18
Query
{'selection': {'CommandLine|contains|all': ['\\pubprn.vbs', 'script:']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1fb76ab8-fa60-4b01-bddd-71e89bf555da
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216.001 
References
https://lolbas-project.github.io/lolbas/Scripts/Pubprn/ 
Severity

49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/28 medium Unknown
Rule Details: Tamper Windows Defender Remove-MpPreference
Detects attempts to remove windows defender configuration using the 'MpPreference' cmdlet.
Rule ID
process_creation_commandline_19
Query
{'selection_remove': {'CommandLine|contains': 'Remove-
MpPreference'}, 'selection_tamper': {'CommandLine|contains': ['-
ControlledFolderAccessProtectedFolders ', '-AttackSurfaceReductionRules_Ids ', '-
AttackSurfaceReductionRules_Actions ', '-
CheckForSignaturesBeforeRunningScan ']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,07e3cb2c-0608-410d-be4b-1511cb1a0448
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/windows-10-
controlled-folder-access-event-search/ba-p/2326088 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/05 high Legitimate PowerShell scripts
Rule Details: AnyDesk Silent Installation
Detects AnyDesk Remote Desktop silent installation. Which can be used by attackers to gain
remote access.
Rule ID
process_creation_commandline_20
Query
{'selection': {'CommandLine|contains|all': ['--install', '--start-with-win', '--
silent']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,114e7f1c-f137-48c8-8f54-3088c24ce4b9
Author: Ján Trenčanský
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1219 
References
https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/06 high Legitimate deployment of AnyDesk
Rule Details: Execution via CL_Invocation.ps1
Detects Execution via SyncInvoke in CL_Invocation.ps1 module.
Rule ID
process_creation_commandline_21

Query
{'selection': {'CommandLine|contains|all': ['CL_Invocation.ps1', 'SyncInvoke']}, 'con
dition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a0459f02-ac51-4c09-b511-b8c9203fc429
Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Cl_invocation/ 
https://twitter.com/bohops/status/948061991012327424 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/14 high Unknown
Rule Details: Writing Of Malicious Files To The Fonts Folder
Monitors for the hiding possible malicious files in the C:\Windows\Fonts\ location. This folder
doesn't require admin privillege to be written and executed from.
Rule ID
process_creation_commandline_24
Query
{'selection_1': {'CommandLine|contains': ['echo', 'copy', 'type', 'file createnew', '
cacls']}, 'selection_2': {'CommandLine|contains': 'C:\\Windows\\Fonts\\'}, 'selection
_3': {'CommandLine|contains': ['.sh', '.exe', '.dll', '.bin', '.bat', '.cmd', '.js',
'.msh', '.reg', '.scr', '.ps', '.vb', '.jar', '.pl', '.inf', '.cpl', '.hta', '.msi',
'.vbs']}, 'condition': 'all of selection_*'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ae9b0bd7-8888-4606-b444-0ed7410cb728
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1211 
References
https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/21 medium Unknown
Rule Details: Suspicious FromBase64String Usage On Gzip Archive - Process Creation
Detects attempts of decoding a base64 Gzip archive via PowerShell. This technique is often
used as a method to load malicious content into memory afterward.
Rule ID
process_creation_commandline_25
Query
{'selection': {'CommandLine|contains|all': ['FromBase64String', 'MemoryStream', 'H4sI
']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d75d6b6b-adb9-48f7-824b-ac2e786efe1f
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 

References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=43 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium Legitimate administrative script
Rule Details: Suspicious Usage Of ShellExec_RunDLL
Detects suspicious usage of the ShellExec_RunDLL function to launch other commands as seen
in the the raspberry-robin attack.
Rule ID
process_creation_commandline_26
Query
{'selection_openasrundll': {'CommandLine|contains': 'ShellExec_RunDLL'}, 'selection_s
uspcli': {'CommandLine|contains': ['regsvr32', 'msiexec', '\\Users\\Public\\', 'odbcc
onf', '\\Desktop\\', '\\Temp\\', 'Invoke-
', 'iex', 'comspec']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d87bd452-6da1-456e-8155-7dc988157b7d
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://redcanary.com/blog/raspberry-robin/ 
https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-
of-larger-ecosystem-facilitating-pre-ransomware-activity/ 
https://github.com/SigmaHQ/sigma/issues/1009 
Severity

74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/01 high Unknown
Rule Details: Turla Group Lateral Movement
Detects automated lateral movement by Turla group.
Rule ID
process_creation_commandline_27
Query
{'selection': {'CommandLine': ['net use \\\\%DomainController%\\C$ "P@ssw0rd" *', 'di
r c:\\*.doc* /s', 'dir %TEMP%\\*.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c601f20d-570a-4cde-a7d6-e17f99cb8e7f
Author: Markus Neis
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1083 , T1135 , TA0008 , T1021.002 
References
https://securelist.com/the-epic-turla-operation/65545/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/07 critical Unknown

Rule Details: Netsh RDP Port Opening
Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent Malware.
Rule ID
process_creation_commandline_28
Query
{'selection1': {'CommandLine|contains|all': ['netsh', 'firewall add portopening', 'tc
p 3389']}, 'selection2': {'CommandLine|contains|all': ['netsh', 'advfirewall firewall
add rule', 'action=allow', 'protocol=TCP', 'localport=3389']}, 'condition': '1 of se
lection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,01aeb693-138d-49d2-9403-c4f52d7d3d62
Author: Sander Wiebing
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.004 
References
https://labs.sentinelone.com/sarwent-malware-updates-command-detonation/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/23 high Legitimate administration
Rule Details: PowerShell DownloadFile
Detects the execution of powershell, a WebClient object creation and the invocation of
DownloadFile in a single command line.
Rule ID
process_creation_commandline_29
Query

{'selection': {'CommandLine|contains|all': ['powershell', '.DownloadFile', 'System.Ne
t.WebClient']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8f70ac5f-1f6f-4f8e-b454-db19561216c5
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0011 , T1104 , T1105 
References
https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-
campaign-using-multiple-exploits.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/08/28 high Unknown
Rule Details: Powershell Defender Exclusion
Detects requests to exclude files, folders or processes from Antivirus scanning using PowerShell
cmdlets.
Rule ID
process_creation_commandline_30
Query
{'selection1': {'CommandLine|contains': ['Add-MpPreference ', 'Set-
MpPreference ']}, 'selection2': {'CommandLine|contains': [' -ExclusionPath ', ' -
ExclusionExtension ', ' -ExclusionProcess ', ' -
ExclusionIpAddress ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,17769c90-230e-488b-a463-e05c08e9d48f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-
process-opened-file-exclusions-microsoft-defender-antivirus 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001
.md 
https://twitter.com/AdamTheAnalyst/status/1483497517119590403 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/04/29 medium Possible Admin Activity
Other Cmdlets that may use the same parameters
Rule Details: Lazarus Loaders
Detects different loaders as described in various threat reports on Lazarus group activity.
Rule ID
process_creation_commandline_31
Query
{'selection_cmd1': {'CommandLine|contains|all': ['cmd.exe /c ', ' -
p 0x']}, 'selection_cmd2': {'CommandLine|contains': ['C:\\ProgramData\\', 'C:\\RECYCL
ER\\']}, 'selection_rundll1': {'CommandLine|contains|all': ['rundll32.exe ', 'C:\\Pro
gramData\\']}, 'selection_rundll2': {'CommandLine|contains': ['.bin,', '.tmp,', '.dat
,', '.io,', '.ini,', '.db,']}, 'condition': '( selection_cmd1 and selection_cmd2 ) or
( selection_rundll1 and selection_rundll2 )'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,7b49c990-4a9a-4e65-ba95-47c9cc448f6e
Author: Florian Roth (Nextron Systems), wagga
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.hvs-consulting.de/lazarus-report/ 
https://securelist.com/lazarus-covets-covid-19-related-intelligence/99906/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/12/23 critical Unknown
Rule Details: Suspicious GrpConv Execution
Detects the suspicious execution of a utility to convert Windows 3.x .grp files or for persistence
purposes by malicious software or actors.
Rule ID
process_creation_commandline_32
Query
{'selection': {'CommandLine|contains': ['grpconv.exe -o', 'grpconv -
o']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f14e169e-9978-4c69-acb3-1cff8200bc36
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547 
References

https://twitter.com/0gtweet/status/1526833181831200770 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/19 high Unknown
Rule Details: Disabled RestrictedAdminMode For RDS - ProcCreation
Detect activation of DisableRestrictedAdmin to desable RestrictedAdmin mode. RestrictedAdmin
mode prevents the transmission of reusable credentials to the remote system to which you
connect using Remote Desktop. This prevents your credentials from being harvested during the
initial connection process if the remote server has been compromise.
Rule ID
process_creation_commandline_33
Query
{'selection': {'CommandLine|contains|all': ['\\System\\CurrentControlSet\\Control\\Ls
a\\', 'DisableRestrictedAdmin', ' 1']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,28ac00d6-22d9-4a3c-927f-bbd770104573
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1112 
References
https://github.com/redcanaryco/atomic-red-
team/blob/a8e3cf63e97b973a25903d3df9fd55da6252e564/atomics/T1112/T1112.md 
https://social.technet.microsoft.com/wiki/contents/articles/32905.remote-desktop-
services-enable-restricted-admin-mode.aspx 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/13 high Unknown
Rule Details: Malicious Base64 Encoded Powershell Invoke Cmdlets
Detects base64 encoded powershell cmdlet invocation of known suspicious cmdlets.
Rule ID
process_creation_commandline_34
Query
{'selection': {'CommandLine|contains': ['SQBuAHYAbwBrAGUALQBCAGwAbwBvAGQASABvAHUAbgBk
A', 'kAbgB2AG8AawBlAC0AQgBsAG8AbwBkAEgAbwB1AG4AZA', 'JAG4AdgBvAGsAZQAtAEIAbABvAG8AZAB
IAG8AdQBuAGQA', 'SQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AHoA', 'kAbgB2AG8AawBlAC0ATQBpAG
0AaQBrAGEAdAB6A', 'JAG4AdgBvAGsAZQAtAE0AaQBtAGkAawBhAHQAeg', 'SQBuAHYAbwBrAGUALQBXAE0
ASQBFAHgAZQBjA', 'kAbgB2AG8AawBlAC0AVwBNAEkARQB4AGUAYw', 'JAG4AdgBvAGsAZQAtAFcATQBJAE
UAeABlAGMA']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fd6e2919-3936-40c9-99db-0aa922c356f7
Author: pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/05/31 high Unlikely
Rule Details: Uninstall Crowdstrike Falcon
Adversaries may disable security tools to avoid possible detection of their tools and activities by
uninstalling Crowdstrike Falcon.
Rule ID
process_creation_commandline_35
Query
{'selection': {'CommandLine|contains|all': ['\\WindowsSensor.exe', ' /uninstall', ' /
quiet']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f0f7be61-9cf5-43be-9836-99d6ef448a18
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001
.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/12 medium Uninstall by admin
Rule Details: Suspicious Powershell No File or Command
Detects suspicious powershell execution that ends with a common flag instead of a command or
a filename to execute (could be a sign of implicit execution that uses files in WindowsApps
directory).

Rule ID
process_creation_commandline_36
Query
{'selection': {'CommandLine|endswith': [' -windowstyle hidden"', ' -
windowstyle hidden', " -windowstyle hidden'", ' -w hidden"', ' -w hidden', " -
w hidden'", ' -ep bypass"', ' -ep bypass', " -ep bypass'", ' -noni"', ' -noni', " -
noni'"]}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b66474aa-bd92-4333-a16c-298155b120df
Author: pH-T (Nextron Systems), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0003 , T1053.005 
References
https://blog.malwarebytes.com/threat-intelligence/2022/04/colibri-loader-combines-task-
scheduler-and-powershell-in-clever-persistence-technique/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/08 high Unknown
Rule Details: New Network Provider - CommandLine
Detects when an attacker tries to add a new network provider in order to dump clear text
credentials, similar to how the NPPSpy tool does it.
Rule ID
process_creation_commandline_37
Query
{'selection': {'CommandLine|contains|all': ['\\System\\CurrentControlSet\\Services\\'
, '\\NetworkProvider']}, 'filter': {'CommandLine|contains': ['\\System\\CurrentContro

lSet\\Services\\WebClient\\NetworkProvider', '\\System\\CurrentControlSet\\Services\\
LanmanWorkstation\\NetworkProvider', '\\System\\CurrentControlSet\\Services\\RDPNP\\N
etworkProvider']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,baef1ec6-2ca9-47a3-97cc-4cf2bda10b77
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/network-
provider-settings-removed-in-place-upgrade 
https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/23 high Other legitimate network providers used and not filtred in this rule
Rule Details: Turla Group Commands May 2020
Detects commands used by Turla group as reported by ESET in May 2020.
Rule ID
process_creation_commandline_38
Query
{'selection1': {'CommandLine|contains': ['tracert -
h 10 yahoo.com', '.WSqmCons))|iex;', 'Fr`omBa`se6`4Str`ing']}, 'selection2': {'Comman
dLine|contains|all': ['net use https://docs.live.net', '@aol.co.uk']}, 'condition': '
1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,9e2e51c5-c699-4794-ba5a-29f5da40ac0c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0003 , T1053.005 , TA0005 , T1027 
References
https://www.welivesecurity.com/wp-
content/uploads/2020/05/ESET_Turla_ComRAT.pdf 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/26 critical Unknown
Rule Details: Potential Data Stealing Via Chromium Headless Debugging
Detects chromium based browsers starting in headless and debugging mode and pointing to a
user profile. This could be a sign of data stealing or remote control.
Rule ID
process_creation_commandline_39
Query
{'selection': {'CommandLine|contains|all': ['--remote-debugging-', '--user-data-
dir', '--headless']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3e8207c5-fcd2-4ea6-9418-15d45b4890e4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1185 

References
https://github.com/defaultnamehere/cookie_crimes/ 
https://mango.pdf.zone/stealing-chrome-cookies-without-a-password 
https://embracethered.com/blog/posts/2020/cookie-crimes-on-mirosoft-edge/ 
https://embracethered.com/blog/posts/2020/chrome-spy-remote-control/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 high Unknown
Rule Details: Invoke-Obfuscation Via Use MSHTA
Detects Obfuscated Powershell via use MSHTA in Scripts.
Rule ID
process_creation_commandline_40
Query
{'selection': {'CommandLine|contains|all': ['set', '&&', 'mshta', 'vbscript:createobj
ect', '.run', '(window.close)']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ac20ae82-8758-4f38-958e-b44a3140ca88
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On

computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/08 high Unknown
Rule Details: Suspicious Rundll32 Script in CommandLine
Detects suspicious process related to rundll32 based on arguments.
Rule ID
process_creation_commandline_41
Query
{'selection': {'CommandLine|contains|all': ['rundll32', 'mshtml,RunHTMLApplication'],
'CommandLine|contains': ['javascript:', 'vbscript:']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,73fcad2e-ff14-4c38-b11d-4172c8ac86c7
Author: frack113, Zaw Min Htun (ZETA)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://gist.github.com/ryhanson/227229866af52e2d963cf941af135a52 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.011/T1218.011.
md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experiment 2021/12/04 medium False positives depend on scripts and administrative tools used in the monitored
environment
al
Rule Details: Suspicious Base64 Encoded Powershell Invoke
Detects base64 encoded powershell 'Invoke-' call.
Rule ID
process_creation_commandline_42
Query
{'selection': {'CommandLine|contains': ['SQBuAHYAbwBrAGUALQ', 'kAbgB2AG8AawBlAC0A', '
JAG4AdgBvAGsAZQAtA']}, 'filter_other_rule': {'CommandLine|contains': ['SQBuAHYAbwBrAG
UALQBCAGwAbwBvAGQASABvAHUAbgBkA', 'kAbgB2AG8AawBlAC0AQgBsAG8AbwBkAEgAbwB1AG4AZA', 'JA
G4AdgBvAGsAZQAtAEIAbABvAG8AZABIAG8AdQBuAGQA', 'SQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AH
oA', 'kAbgB2AG8AawBlAC0ATQBpAG0AaQBrAGEAdAB6A', 'JAG4AdgBvAGsAZQAtAE0AaQBtAGkAawBhAHQ
Aeg', 'SQBuAHYAbwBrAGUALQBXAE0ASQBFAHgAZQBjA', 'kAbgB2AG8AawBlAC0AVwBNAEkARQB4AGUAYw'
, 'JAG4AdgBvAGsAZQAtAFcATQBJAEUAeABlAGMA']}, 'condition': 'selection and not 1 of fil
ter*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6385697e-9f1b-40bd-8817-f4a91f40508e
Author: pH-T (Nextron Systems), Harjot Singh, @cyb3rjy0t
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/20 high Unlikely

Rule Details: HackTool - Bloodhound/Sharphound Execution
Detects command line parameters used by Bloodhound and Sharphound hack tools.
Rule ID
process_creation_commandline_44
Query
{'selection_cli_1': {'CommandLine|contains': [' -CollectionMethod All ', ' --
CollectionMethods Session ', ' --Loop --Loopduration ', ' --
PortScanTimeout ', '.exe -c All -d ', 'Invoke-Bloodhound', 'Get-
BloodHoundData']}, 'selection_cli_2': {'CommandLine|contains|all': [' -
JsonFolder ', ' -
ZipFileName ']}, 'selection_cli_3': {'CommandLine|contains|all': [' DCOnly ', ' --
NoSaveCache ']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f376c8a7-a2d0-4ddc-aa0c-16c17236d962
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0007 , T1087 , T1482 , T1069 
References
https://github.com/BloodHoundAD/BloodHound 
https://github.com/BloodHoundAD/SharpHound 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/12/20 high Other programs that use these command line option and accepts an 'All' parameter
Rule Details: Explorer Process Tree Break
Detects a command line process that uses explorer.exe to launch arbitrary commands or
binaries, which is similar to cmd.exe /c, only it breaks the process tree and makes its parent a
new instance of explorer spawning from "svchost".

Rule ID
process_creation_commandline_45
Query
{'selection': [{'CommandLine|contains': '/factory,{75dff2b7-6936-4c06-a8bb-
676a7b00b24b}'}, {'CommandLine|contains|all': ['explorer.exe', ' /root,']}], 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,949f1ffb-6e85-4f00-ae1e-c3c5b190d605
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems),
@gott_cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 
References
https://twitter.com/CyberRaiju/status/1273597319322058752 
https://twitter.com/bohops/status/1276357235954909188?s=12 
https://twitter.com/nas_bench/status/1535322450858233858 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/06/29 medium Unknown how many legitimate software products use that method
Rule Details: Suspicious Del in CommandLine
Detects suspicious command line to remove and 'exe' or 'dll'.
Rule ID
process_creation_commandline_46
Query
{'susp_del_exe': {'CommandLine|contains|all': ['del ', '*.exe', '/f ', '/q ']}, 'susp
_del_dll': {'CommandLine|contains|all': ['del ', '*.dll', 'C:\\ProgramData\\']}, 'con

dition': 'susp_del_exe or susp_del_dll'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,204b17ae-4007-471b-917b-b917b315c5db
Author: frack113 , X__Junior (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1070.004 
References
https://www.joesandbox.com/analysis/509330/0/html#1044F3BDBE3BB6F734E357235
F4D5898582D 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/02 medium Unknown
Rule Details: Invoke-Obfuscation COMPRESS OBFUSCATION
Detects Obfuscated Powershell via COMPRESS OBFUSCATION.
Rule ID
process_creation_commandline_47
Query
{'selection': {'CommandLine|contains|all': ['new-
object', 'text.encoding]::ascii'], 'CommandLine|contains': ['system.io.compression.de
flatestream', 'system.io.streamreader', 'readtoend(']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7eedcc9d-9fdb-4d94-9c54-474e8affc0c7

Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/18 medium Unknown
Rule Details: Operation Wocao Activity
Detects activity mentioned in Operation Wocao report.
Rule ID
process_creation_commandline_48
Query
{'selection': {'CommandLine|contains': ['checkadmin.exe 127.0.0.1 -
all', 'netsh advfirewall firewall add rule name=powershell dir=in', 'cmd /c powershel
l.exe -ep bypass -
file c:\\s.ps1', '/tn win32times /f', 'create win32times binPath=', '\\c$\\windows\\s
ystem32\\devmgr.dll', ' -exec bypass -
enc JgAg', 'type *keepass\\KeePass.config.xml', 'iie.exe iie.txt', 'reg query HKEY_CU
RRENT_USER\\Software\\*\\PuTTY\\Sessions\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,1cfac73c-be78-4f9a-9b08-5bde0c3953ab
Author: Florian Roth (Nextron Systems), frack113
Tactics, Techniques, and Procedures

TA0002 , T1059 , TA0003 , T1053.005 , TA0005 , T1036.004 , T1027 ,
TA0007 , T1012 
References
https://twitter.com/SBousseaden/status/1207671369963646976 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/12/20 high Administrators that use checkadmin.exe tool to enumerate local administrators
Rule Details: Fireball Archer Install
Detects Archer malware invocation via rundll32.
Rule ID
process_creation_commandline_49
Query
{'selection': {'CommandLine|contains|all': ['rundll32.exe', 'InstallArcherSvc']}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3d4aebe0-6d29-45b2-a8a4-3dfde586a26d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.virustotal.com/en/file/9b4971349ae85aa09c0a69852ed3e626c954954a392
7b3d1b6646f139b930022/analysis/ 
https://www.hybrid-
analysis.com/sample/9b4971349ae85aa09c0a69852ed3e626c954954a3927b3d1b6646
f139b930022?environmentId=100 
Severity

74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/06/03 high Unknown
Rule Details: Zip A Folder With PowerShell For Staging In Temp
Use living off the land tools to zip a file and stage it in the Windows temporary folder for later
exfiltration.
Rule ID
process_creation_commandline_50
Query
{'selection': {'CommandLine|contains|all': ['Compress-Archive ', ' -Path ', ' -
DestinationPath ', '$env:TEMP\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,85a8e5ba-bd03-4bfb-bbfa-a4409a8f8b98
Author: Nasreddine Bencherchali (Nextron Systems), frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1074.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1074.001/T1074.001
.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/07/20 medium Unknown
Rule Details: Registry Dump of SAM Creds and Secrets
Adversaries may attempt to extract credential material from the Security Account Manager (SAM)
database either through Windows Registry where the SAM database is stored.
Rule ID
process_creation_commandline_51
Query
{'selection_reg': {'CommandLine|contains': ' save '}, 'selection_key': {'CommandLine|
contains': ['HKLM\\sam', 'HKLM\\system', 'HKLM\\security']}, 'condition': 'all of sel
ection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,038cd51c-3ad8-41c5-ba8f-5d1c92f3cc1e
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.002 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002
.md#atomic-test-1---registry-dump-of-sam-creds-and-secrets 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/05 high Unknown
Rule Details: Procdump Evasion
Detects uses of the SysInternals Procdump utility in which procdump or its output get renamed or
a dump file is moved ot copied to a different name.

Rule ID
process_creation_commandline_52
Query
{'selection1': {'CommandLine|contains': ['copy procdump', 'move procdump']}, 'selecti
on2': {'CommandLine|contains|all': ['copy ', '.dmp '], 'CommandLine|contains': ['2.dm
p', 'lsass', 'out.dmp']}, 'selection3': {'CommandLine|contains': ['copy lsass.exe_',
'move lsass.exe_']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,79b06761-465f-4f88-9ef2-150e24d3d737
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 , TA0006 , T1003.001 
References
https://twitter.com/mrd0x/status/1480785527901204481 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2022/01/11 high Cases in which procdump just gets copied to a different directory without any
renaming
Rule Details: Powershell Token Obfuscation - Process Creation
Detects TOKEN OBFUSCATION technique from Invoke-Obfuscation.
Rule ID
process_creation_commandline_53
Query
{'selection': [{'CommandLine|re': '\\w+`(\\w+|-
|.)`[\\w+|\\s]'}, {'CommandLine|re': '"(\\{\\d\\})+"\\s*-
f'}, {'CommandLine|re': '\\$\\{((e|n|v)*`(e|n|v)*)+:path\\}|\\$\\

{((e|n|v)*`(e|n|v)*)+:((p|a|t|h)*`(p|a|t|h)*)+\\}|\\$\\{env:
((p|a|t|h)*`(p|a|t|h)*)+\\}'}], 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,deb9b646-a508-44ee-b7c9-d8965921c6b6
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-Obfuscation 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/27 high Unknown
Rule Details: Suspicious Minimized MSEdge Start
Detects the suspicious minimized start of MsEdge browser, which can be used to download files
from the Internet.
Rule ID
process_creation_commandline_54
Query
{'selection': {'CommandLine|contains': 'start /min msedge'}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,94771a71-ba41-4b6e-a757-b531372eaab6

Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://twitter.com/mrd0x/status/1478234484881436672?s=12 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
test 2022/01/11 high Software that uses MsEdge to download components in the background (see
ParentImage, ParentCommandLine)
Rule Details: Suspicious PowerShell Download and Execute Pattern
Detects suspicious PowerShell download patterns that are often used in malicious scripts,
stagers or downloaders (make sure that your backend applies the strings case-insensitive).
Rule ID
process_creation_commandline_55
Query
{'selection': {'CommandLine|contains': ['IEX ((New-
Object Net.WebClient).DownloadString', 'IEX (New-
Object Net.WebClient).DownloadString', 'IEX((New-
Object Net.WebClient).DownloadString', 'IEX(New-
Object Net.WebClient).DownloadString', ' -command (New-
Object System.Net.WebClient).DownloadFile(', ' -c (New-
Object System.Net.WebClient).DownloadFile(']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e6c54d94-498c-4562-a37c-b469d8e9a275
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059 
References
https://gist.github.com/jivoi/c354eaaf3019352ce32522f916c03d70 
https://www.trendmicro.com/en_us/research/22/j/lv-ransomware-exploits-proxyshell-in-
attack.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/02/28 high Software installers that pull packages from remote systems and execute them
Rule Details: Add User to Local Administrators
Detects suspicious command line that adds an account to the local
administrators/administrateurs group.
Rule ID
process_creation_commandline_56
Query
{'selection_net': {'Image|endswith': ['\\net.exe', '\\net1.exe'], 'CommandLine|contai
ns|all': ['localgroup ', ' /add']}, 'selection_powershell': {'Image|endswith': ['\\po
wershell.exe', '\\pwsh.exe'], 'CommandLine|contains|all': ['Add-
LocalGroupMember ', ' -
Group ']}, 'selection_group': {'CommandLine|contains': [' administrators ', ' adminis
trateur']}, 'filter_domain_admins_compliance': {'UserId': 'S-1-5-
18', 'CommandLine|contains': 'domain admin'}, 'condition': '(selection_net or selecti
on_powershell) and selection_group and not filter_domain_admins_compliance'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1098 
References

https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/12 medium Administrative activity
Rule Details: Taskkill Symantec Endpoint Protection
Detects one of the possible scenarios for disabling symantec endpoint protection. Symantec
Endpoint Protection antivirus software services incorrectly implement the protected service
mechanism. As a result, the NT AUTHORITY/SYSTEM user can execute the taskkill /im
command several times ccSvcHst.exe /f, thereby killing the process belonging to the service, and
thus shutting down the service.
Rule ID
process_creation_commandline_57
Query
{'selection': {'CommandLine|contains|all': ['taskkill', ' /F ', ' /IM ', 'ccSvcHst.ex
e']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,4a6713f6-3331-11ed-a261-0242ac120002
Author: Ilya Krestinichev, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://www.exploit-db.com/exploits/37525 
https://community.spiceworks.com/topic/2195015-batch-script-to-uninstall-symantec-
endpoint-protection 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/13 high Unknown
Rule Details: MsiExec Web Install
Detects suspicious msiexec process starts with web addresses as parameter.
Rule ID
process_creation_commandline_58
Query
{'selection': {'CommandLine|contains|all': [' msiexec', '://']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f7b5f842-a6af-4da5-9e95-e32478f3cd2f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.007 , TA0011 , T1105 
References
https://blog.trendmicro.com/trendlabs-security-intelligence/attack-using-windows-
installer-msiexec-exe-leads-lokibot/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2018/02/09 medium False positives depend on scripts and administrative tools used in the monitored
environment

Rule Details: PsExec Service Start
Detects a PsExec service start.
Rule ID
process_creation_commandline_59
Query
{'selection': {'CommandLine': 'C:\\Windows\\PSEXESVC.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3ede524d-21cc-472d-a3ce-d21b568d8db7
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 
References
N/A
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/13 low Administrative activity
Rule Details: Scheduled Task WScript VBScript
Detects specific process parameters as used by ACTINIUM scheduled task persistence creation.
Rule ID
process_creation_commandline_60
Query
{'selection': {'CommandLine|contains|all': ['schtasks', 'create', 'wscript', 'e:vbscr
ipt']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,e1118a8f-82f5-44b3-bb6b-8a284e5df602
Author: Andreas Hunkeler (@Karneades)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1053.005 
References
https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-
organizations 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/07 high Unlikely
Rule Details: Dropping Of Password Filter DLL
Detects dropping of dll files in system32 that may be used to retrieve user credentials from
LSASS.
Rule ID
process_creation_commandline_61
Query
{'selection_cmdline': {'CommandLine|contains|all': ['HKLM\\SYSTEM\\CurrentControlSet\
\Control\\Lsa', 'scecli\\0*', 'reg add']}, 'condition': 'selection_cmdline'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b7966f4a-b333-455b-8370-8ca53c229762
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1556.002 

References
https://pentestlab.blog/2020/02/10/credential-access-password-filter-dll/ 
https://github.com/3gstudent/PasswordFilter/tree/master/PasswordFilter 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/29 medium Unknown
Rule Details: Suspicious UltraVNC Execution
Detects suspicious UltraVNC command line flag combination that indicate a auto reconnect upon
execution, e.g. startup (as seen being used by Gamaredon threat group).
Rule ID
process_creation_commandline_62
Query
{'selection': {'CommandLine|contains|all': ['-autoreconnect ', '-connect ', '-
id:']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,871b9555-69ca-4993-99d3-35a59f9f3599
Author: Bhabesh Raj
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1021.005 
References
https://www.ria.ee/sites/default/files/content-
editors/kuberturve/tale_of_gamaredon_infection.pdf 
https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/04 high Unknown
Rule Details: Potential AMSI Bypass Using NULL Bits - ProcessCreation
Detects usage of special strings/null bits in order to potentially bypass AMSI functionalities.
Rule ID
process_creation_commandline_63
Query
{'selection': {'CommandLine|contains': ["if(0){{{0}}}' -f $(0 -as [char]) +", '#
<NULL>']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,92a974db-ab84-457f-9ec0-55db83d7a825
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/r00t-3xp10it/hacking-material-
books/blob/43cb1e1932c16ff1f58b755bc9ab6b096046853f/obfuscation/simple_obfusca
tion.md#amsi-bypass-using-null-bits-satoshi 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/04 medium Unknown

Rule Details: Invoke-Obfuscation CLIP+ Launcher
Detects Obfuscated use of Clip.exe to execute PowerShell.
Rule ID
process_creation_commandline_65
Query
{'selection': {'CommandLine|contains|all': ['cmd', '&&', 'clipboard]::', '-
f'], 'CommandLine|contains': ['/c', '/r']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b222df08-0e07-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 high Unknown
Rule Details: SyncAppvPublishingServer VBS Execute Arbitrary PowerShell Code
Executes arbitrary PowerShell code using SyncAppvPublishingServer.vbs.
Rule ID
process_creation_commandline_67
Query
{'selection': {'CommandLine|contains|all': ['\\SyncAppvPublishingServer.vbs', ';']},
'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,36475a7d-0f6d-4dce-9b01-6aeb473bbaf1
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , T1216 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1216/T1216.md 
https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/16 medium Unknown
Rule Details: Suspicious Add User to Remote Desktop Users Group
Detects suspicious command line in which a user gets added to the local Remote Desktop Users
group.
Rule ID
process_creation_commandline_68
Query
{'selection_main': [{'CommandLine|contains|all': ['localgroup ', ' /add']}, {'Command
Line|contains|all': ['Add-LocalGroupMember ', ' -
Group ']}], 'selection_group': {'CommandLine|contains': ['Remote Desktop Users', 'Uti
lisateurs du Bureau à distance', 'Usuarios de escritorio remoto']}, 'condition': 'all
of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,ffa28e60-bdb1-46e0-9f82-05f7a61cc06e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1133 , T1136.001 , TA0008 , T1021.001 
References
https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-
actor-activity-mstic-presentation-at-cyberwarcon-2021/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/06 high Administrative activity
Rule Details: GatherNetworkInfo.vbs Script Usage
Adversaries can abuse of C:\Windows\System32\gatherNetworkInfo.vbs script along with
cscript.exe to gather information about the target.
Rule ID
process_creation_commandline_69
Query
{'selection': {'CommandLine|contains|all': ['cscript.exe', 'gatherNetworkInfo.vbs']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,575dce0c-8139-4e30-9295-1ee75969f7fe
Author: blueteamer8699
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://posts.slayerlabs.com/living-off-the-land/#gathernetworkinfovbs 

Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/03 medium Administrative activity
Rule Details: APT29
This method detects a suspicious PowerShell command line combination as used by APT29 in a
campaign against U.S. think tanks.
Rule ID
process_creation_commandline_70
Query
{'selection': {'CommandLine|contains|all': ['-noni', '-
ep', 'bypass', '$']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,033fe7d6-66d1-4240-ac6b-28908009c71f
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://www.microsoft.com/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-
think-tanks-non-profits-public-sector-by-unidentified-attackers/ 
https://www.fireeye.com/blog/threat-research/2018/11/not-so-cozy-an-uncomfortable-
examination-of-a-suspected-apt29-phishing-campaign.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/12/04 high Unknown
Rule Details: Suspicious WMIC ActiveScriptEventConsumer Creation
Detects WMIC executions in which a event consumer gets created in order to establish
persistence.
Rule ID
process_creation_commandline_71
Query
{'selection': {'CommandLine|contains|all': ['ActiveScriptEventConsumer', ' CREATE ']}
, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ebef4391-1a81-4761-a40a-1db446c0e625
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.003 
References
https://twitter.com/johnlatwc/status/1408062131321270282?s=12 
https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-
windows-management-instrumentation.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/06/25 high Legitimate software creating script event consumers
Rule Details: TAIDOOR RAT DLL Load

Detects specific process characteristics of Chinese TAIDOOR RAT malware load.
Rule ID
process_creation_commandline_72
Query
{'selection1': {'CommandLine|contains': ['dll,MyStart', 'dll MyStart']}, 'selection2a
': {'CommandLine|endswith': ' MyStart'}, 'selection2b': {'CommandLine|contains': 'run
dll32.exe'}, 'condition': 'selection1 or ( selection2a and selection2b )'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d1aa3382-abab-446f-96ea-4de52908210b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1055.001 
References
https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/30 high Unknown
Rule Details: Empire PowerShell UAC Bypass
Detects some Empire PowerShell UAC bypass methods.
Rule ID
process_creation_commandline_73
Query
{'selection': {'CommandLine|contains': [' -NoP -NonI -w Hidden -
c $x=$((gp HKCU:Software\\Microsoft\\Windows Update).Update)', ' -NoP -NonI -
c $x=$((gp HKCU:Software\\Microsoft\\Windows Update).Update);']}, 'condition': 'selec
tion'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3268b746-88d8-4cd3-bffc-30077d02c787
Author: Ecco
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1548.002 
References
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13
055/data/module_source/privesc/Invoke-EventVwrBypass.ps1#L64 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13
055/data/module_source/privesc/Invoke-FodHelperBypass.ps1#L64 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/08/30 critical Unknown
Rule Details: Emotet Process Creation
Detects all Emotet like process executions that are not covered by the more generic rules.
Rule ID
process_creation_commandline_74
Query
{'selection': {'CommandLine|contains': [' -
e* PAA', 'JABlAG4AdgA6AHUAcwBlAHIAcAByAG8AZgBpAGwAZQ', 'QAZQBuAHYAOgB1AHMAZQByAHAAcgB
vAGYAaQBsAGUA', 'kAGUAbgB2ADoAdQBzAGUAcgBwAHIAbwBmAGkAbABlA', 'IgAoACcAKgAnACkAOwAkA'
, 'IAKAAnACoAJwApADsAJA', 'iACgAJwAqACcAKQA7ACQA', 'JABGAGwAeAByAGgAYwBmAGQ', 'PQAkAG
UAbgB2ADoAdABlAG0AcAArACgA', '0AJABlAG4AdgA6AHQAZQBtAHAAKwAoA', '9ACQAZQBuAHYAOgB0AGU
AbQBwACsAKA']}, 'filter': {'CommandLine|contains': ['fAAgAEMAbwBuAHYAZQByAHQAVABvAC0A
SgBzAG8AbgAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQAaQBuA
HUAZQ', 'wAIABDAG8AbgB2AGUAcgB0AFQAbwAtAEoAcwBvAG4AIAAtAEUAcgByAG8AcgBBAGMAdABpAG8Abg
AgAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUA', '8ACAAQwBvAG4AdgBlAHIAdABUAG8ALQBKAH

MAbwBuACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQB
lA']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d02e8cf5-6099-48cf-9bfc-1eec2d0c7b18
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://app.any.run/tasks/e13ab713-64cf-4b23-ad93-6dceaa5429ac/ 
https://app.any.run/tasks/81f3c28c-c686-425d-8a2b-a98198d244e1/ 
https://app.any.run/tasks/97f875e8-0e08-4328-815f-055e971ba754/ 
https://app.any.run/tasks/84fc9b4a-ea2b-47b1-8aa6-9014402dfb56/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/09/30 high Unlikely
Rule Details: Esentutl Gather Credentials
Conti recommendation to its affiliates to use esentutl to access NTDS dumped file. Trickbot also
uses this utilities to get MSEdge info via its module pwgrab.
Rule ID
process_creation_commandline_75
Query
{'selection': {'CommandLine|contains|all': ['esentutl', ' /p']}, 'condition': 'select
ion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,7df1713a-1a5b-4a4b-a071-dc83b144a101
Author: sam0x90
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.003 
References
https://twitter.com/vxunderground/status/1423336151860002816 
https://attack.mitre.org/software/S0404/ 
https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-
cobalt-strike/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/06 medium To be determined
Rule Details: EvilNum Golden Chickens Deployment via OCX Files
Detects Golden Chickens deployment method as used by Evilnum in report published in July
2020.
Rule ID
process_creation_commandline_76
Query
{'selection': {'CommandLine|contains|all': ['regsvr32', '/s', '/i', '\\AppData\\Roami
ng\\', '.ocx']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8acf3cfa-1e8c-4099-83de-a0c4038e18f0
Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/ 
https://app.any.run/tasks/33d37fdf-158d-4930-aa68-813e1d5eb8ba/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/10 critical Unknown
Rule Details: Suspicious Dosfuscation Character in Commandline
Detects possible payload obfuscation via the commandline.
Rule ID
process_creation_commandline_77
Query
{'selection': {'CommandLine|contains': ['^^', ',;,', '%COMSPEC:~', ' s^et ', ' s^e^t
', ' se^t ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a77c1610-fc73-4019-8e29-0f51efc04a51
Author: frack113, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/dosfuscation-report.pdf 
Severity
49

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/02/15 medium Legitimate use
Rule Details: WhoAmI as Parameter
Detects a suspicious process command line that uses whoami as first parameter (as e.g. used
by EfsPotato).
Rule ID
process_creation_commandline_78
Query
{'selection': {'CommandLine|contains': '.exe whoami'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e9142d84-fbe0-401d-ac50-3e519fb00c89
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1033 
References
https://twitter.com/blackarrowsec/status/1463805700602224645?s=12 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/29 high Unknown
Rule Details: Powershell Inline Execution From A File

Detects inline execution of PowerShell code from a file.
Rule ID
process_creation_commandline_79
Query
{'selection_exec': {'CommandLine|contains': ['iex ', 'Invoke-Expression ', 'Invoke-
Command ', 'icm ']}, 'selection_read': {'CommandLine|contains': ['cat ', 'get-
content ', 'type ']}, 'selection_raw': {'CommandLine|contains': ' -
raw'}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ee218c12-627a-4d27-9e30-d6fb2fe22ed2
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=50 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium Unknown
Rule Details: Base64 Encoded PowerShell Command Detected
Detects usage of the "FromBase64String" function in the commandline which is used to decode
a base64 encoded string.
Rule ID
process_creation_commandline_80
Query
{'selection': {'CommandLine|contains': '::FromBase64String('}, 'condition': 'selectio
n'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e32d4572-9826-4738-b651-95fa63747e8a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 , T1140 
References
https://gist.github.com/Neo23x0/6af876ee72b51676c82a2db8d2cd3639 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/29 high Administrative script libraries
Rule Details: CL_Mutexverifiers.ps1 Proxy Execution
Detects the use of a Microsoft signed script to execute commands.
Rule ID
process_creation_commandline_81
Query
{'selection': {'CommandLine|contains|all': ['\\CL_Mutexverifiers.ps1', 'runAfterCance
lProcess ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1e0e1a81-e79b-44bc-935b-ddb9c8006b3d
Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia Shornikova,
frack113
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/CL_mutexverifiers/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/21 medium Unknown
Rule Details: Suspicious X509Enrollment - Process Creation
Detect use of X509Enrollment.
Rule ID
process_creation_commandline_82
Query
{'selection': {'CommandLine|contains': ['X509Enrollment.CBinaryConverter', '884e2002-
217d-11da-b2a4-000e7bbb2b09']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,114de787-4eb2-48cc-abdb-c0b449f93ea4
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=42 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=41 
https://learn.microsoft.com/en-
us/dotnet/api/microsoft.hpc.scheduler.store.cx509enrollmentwebclassfactoryclass?
view=hpc-sdk-5.1.6115 
Severity

49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/23 medium Legitimate administrative script
Rule Details: Suspicious Regsvr32 HTTP IP Pattern
Detects a certain command line flag combination used by regsvr32 when used to download and
register a DLL from a remote address which uses HTTP (not HTTPS) and a IP address and not
FQDN.
Rule ID
process_creation_commandline_83
Query
{'selection_flags': {'CommandLine|contains|all': [' /s', ' /u']}, 'selection_ip': {'C
ommandLine|contains': [' /i:http://1', ' /i:http://2', ' /i:http://3', ' /i:http://4'
, ' /i:http://5', ' /i:http://6', ' /i:http://7', ' /i:http://8', ' /i:http://9', ' /
i:https://1', ' /i:https://2', ' /i:https://3', ' /i:https://4', ' /i:https://5', ' /
i:https://6', ' /i:https://7', ' /i:https://8', ' /i:https://9']}, 'condition': 'all
of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2dd2c217-bf68-437a-b57c-fe9fd01d5de8
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.010 
References
https://twitter.com/mrd0x/status/1461041276514623491c19-ps 
https://twitter.com/tccontre18/status/1480950986650832903 
Severity
74
Suppression Logic Based On
computer_name

event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/11 high FQDNs that start with a number
Rule Details: Rundll32 Without Parameters
Detects rundll32 execution without parameters as observed when running Metasploit
windows/smb/psexec exploit module.
Rule ID
process_creation_commandline_84
Query
{'selection': {'CommandLine': 'rundll32.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5bb68627-3198-40ca-b458-49f973db8752
Author: Bartlomiej Czyz, Relativity
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 , TA0008 , T1021.002 , T1570 
References
https://bczyz1.github.io/2021/01/30/psexec.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/31 high Unknown
Rule Details: Suspicious Ntdll Pipe Redirection
Detects command that type the content of ntdll.dll to a different file or a pipe in order to evade AV
/ EDR detection.

Rule ID
process_creation_commandline_85
Query
{'selection': {'CommandLine|contains': ['type %windir%\\system32\\ntdll.dll', 'type %
systemroot%\\system32\\ntdll.dll', 'type c:\\windows\\system32\\ntdll.dll', '\\ntdll.
dll > \\\\.\\pipe\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bbc865e4-7fcd-45a6-8ff1-95ced28ec5b2
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/05 high Unknown
Rule Details: Raccine Uninstall
Detects commands that indicate a Raccine removal from an end system. Raccine is a free
ransomware protection tool.
Rule ID
process_creation_commandline_86
Query
{'selection1': {'CommandLine|contains|all': ['taskkill ', 'RaccineSettings.exe']}, 's
election2': {'CommandLine|contains|all': ['reg.exe', 'delete', 'Raccine Tray']}, 'sel
ection3': {'CommandLine|contains|all': ['schtasks', '/DELETE', 'Raccine Rules Updater
']}, 'condition': '1 of selection*'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a31eeaed-3fd5-478e-a8ba-e62c6b3f9ecc
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/Neo23x0/Raccine 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/21 high Legitimate deinstallation by administrative staff
Rule Details: REGISTER_APP.VBS Proxy Execution
Detects the use of a Microsoft signed script 'REGISTER_APP.VBS' to register a VSS/VDS
Provider as a COM+ application.
Rule ID
process_creation_commandline_88
Query
{'selection': {'CommandLine|contains|all': ['\\register_app.vbs', '-
register']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1c8774a0-44d4-4db0-91f8-e792359c70bd
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0005 , T1218 
References
https://twitter.com/sblmsrsn/status/1456613494783160325?s=20 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2022/08/19 medium Legitimate usage of the script. Always investigate what's being registered to confirm
if it's benign
al
Rule Details: PowerShell Get-Process LSASS
Detects a "Get-Process" cmdlet and it's aliases on lsass process, which is in almost all cases a
sign of malicious activity.
Rule ID
process_creation_commandline_89
Query
{'selection': {'CommandLine|contains': ['Get-
Process lsas', 'ps lsas', 'gps lsas']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b2815d0d-7481-4bf0-9b6c-a4c48a94b349
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1552.004 
References
https://twitter.com/PythonResponder/status/1385064506049630211 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/04/23 high Unknown
Rule Details: Raspberry Robin Dot Ending File
Detects commandline containing reference to files ending with a "." This scheme has been seen
used by raspberry-robin.
Rule ID
process_creation_commandline_90
Query
{'selection': {'CommandLine|re': '\\\\([a-zA-Z0-9]{1,32})\\.([a-zA-Z0-9]{1,6})\\.
(\\s*(["\'])|(\\s+[^a-zA-Z0-9\\s.]))'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a35c97c8-d9c4-4c89-a3e7-533dc0bcb73a
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-
of-larger-ecosystem-facilitating-pre-ransomware-activity/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/28 high Unknown

Rule Details: LockerGoga Ransomware
Detects LockerGoga Ransomware command line.
Rule ID
process_creation_commandline_91
Query
{'selection': {'CommandLine|contains': '-i SM-tgytutrc -
s'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,74db3488-fd28-480a-95aa-b7af626de068
Author: Vasiliy Burov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://medium.com/@malwaredancer/lockergoga-input-arguments-ipc-communication-
and-others-bd4e5a7ba80a 
https://blog.f-secure.com/analysis-of-lockergoga-ransomware/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/10/18 critical Unlikely
Rule Details: Write Protect For Storage Disabled
Looks for changes to registry to disable any write-protect property for storage devices. This could
be a precursor to a ransomware attack and has been an observed technique used by
cypherpunk group.
Rule ID
process_creation_commandline_92

Query
{'selection': {'CommandLine|contains|all': ['reg add', '\\system\\currentcontrolset\\
control', 'write protection', '0'], 'CommandLine|contains': ['storage', 'storagedevic
epolicies']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,75f7a0e2-7154-4c4d-9eae-5cdb4e0a5c13
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/06/11 medium Unknown
Rule Details: Audio Capture via PowerShell
Detects audio capture via PowerShell Cmdlet.
Rule ID
process_creation_commandline_93
Query
{'selection': {'CommandLine|contains': 'WindowsAudioDevice-Powershell-
Cmdlet'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,932fb0d8-692b-4b0f-a26e-5643a50fe7d6
Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community,
Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1123 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1123/T1123.md 
https://eqllib.readthedocs.io/en/latest/analytics/ab7a6ef4-0983-4275-a4f1-
5c6bd3c31c23.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 medium Legitimate audio capture by legitimate user.
Rule Details: Potential Suspicious Windows Feature Enabled - ProcCreation
Detects usage of the built-in PowerShell cmdlet "Enable-WindowsOptionalFeature" used as a
Deployment Image Servicing and Management tool. Similar to DISM.exe, this cmdlet is used to
enumerate, install, uninstall, configure, and update features and packages in Windows images.
Rule ID
process_creation_commandline_94
Query
{'selection_cmd': {'CommandLine|contains|all': ['Enable-WindowsOptionalFeature', '-
Online', '-
FeatureName']}, 'selection_feature': {'CommandLine|contains': ['TelnetServer', 'Inter
net-Explorer-Optional-amd64', 'TFTP', 'SMB1Protocol', 'Client-ProjFS', 'Microsoft-
Windows-Subsystem-Linux']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c740d4cf-a1e9-41de-bb16-8a46a4f57918

Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://docs.microsoft.com/en-us/powershell/module/dism/enable-
windowsoptionalfeature?view=windowsserver2022-ps 
https://learn.microsoft.com/en-us/windows/win32/projfs/enabling-windows-projected-file-
system 
https://learn.microsoft.com/en-us/windows/wsl/install-on-server 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/29 medium Unknown
Rule Details: Reg Disable Security Service
Detects a suspicious reg.exe invocation that looks as if it would disable an important security
service.
Rule ID
process_creation_commandline_96
Query
{'selection_reg_add': {'CommandLine|contains|all': ['reg', 'add']}, 'selection_cli_re
g_start': {'CommandLine|contains|all': [' /d 4', ' /v Start'], 'CommandLine|contains'
: ['\\Sense', '\\WinDefend', '\\MsMpSvc', '\\NisSrv', '\\WdBoot', '\\WdNisDrv', '\\Wd
NisSvc', '\\wscsvc', '\\SecurityHealthService', '\\wuauserv', '\\UsoSvc', '\\WdFilter
', '\\AppIDSvc']}, 'selection_cli_reg_disable_defender': {'CommandLine|contains|all':
[' /d 1', 'Windows Defender'], 'CommandLine|contains': ['DisableIOAVProtection', 'Di
sableOnAccessProtection', 'DisableRoutinelyTakingAction', 'DisableScanOnRealtimeEnabl
e', 'DisableBlockAtFirstSeen', 'DisableBehaviorMonitoring', 'DisableEnhancedNotificat
ions', 'DisableAntiSpyware', 'DisableAntiSpywareRealtimeProtection', 'DisableConfig',
'DisablePrivacyMode', 'SignatureDisableUpdateOnStartupWithoutEngine', 'DisableArchiv
eScanning', 'DisableIntrusionPreventionSystem', 'DisableScriptScanning']}, 'condition
': 'selection_reg_add and 1 of selection_cli_*'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5e95028c-5229-4214-afae-d653d573d0ec
Author: Florian Roth (Nextron Systems), John Lambert (idea), elhoim
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://twitter.com/JohnLaTwC/status/1415295021041979392 
https://github.com/gordonbay/Windows-On-
Reins/blob/e587ac7a0407847865926d575e3c46f68cf7c68d/wor.ps1 
https://vms.drweb.fr/virus/?i=24144899 
https://bidouillesecurity.com/disable-windows-defender-in-powershell/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/14 high Unknown
Other security solution installers
Rule Details: Serv-U Exploitation CVE-2021-35211 by DEV-0322
Detects patterns as noticed in exploitation of Serv-U CVE-2021-35211 vulnerability by threat
group DEV-0322.
Rule ID
process_creation_commandline_97
Query
{'selection_whoami': {'CommandLine|contains': 'whoami'}, 'selection_cmd_1': {'Command
Line|contains': ['./Client/Common/', '.\\Client\\Common\\']}, 'selection_cmd_2': {'Co
mmandLine|contains': 'C:\\Windows\\Temp\\Serv-
U.bat'}, 'condition': 'selection_whoami and 1 of selection_cmd*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,75578840-9526-4b2a-9462-af469a45e767
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1136.001 
References
https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-
targeting-solarwinds-serv-u-software-with-0-day-exploit/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/14 critical Unlikely
Rule Details: Suspicious Debugger Registration Cmdline
Detects the registration of a debugger for a program that is available in the logon screen (sticky
key backdoor).
Rule ID
process_creation_commandline_98
Query
{'selection1': {'CommandLine|contains': '\\CurrentVersion\\Image File Execution Optio
ns\\'}, 'selection2': {'CommandLine|contains': ['sethc.exe', 'utilman.exe', 'osk.exe'
, 'magnify.exe', 'narrator.exe', 'displayswitch.exe', 'atbroker.exe', 'HelpPane.exe']
}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ae215552-081e-44c7-805f-be16f975c8a2
Author: Florian Roth (Nextron Systems), oscd.community, Jonhnathan Ribeiro
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0003 , T1546.008 
References
https://blogs.technet.microsoft.com/jonathantrull/2016/10/03/detecting-sticky-key-
backdoors/ 
https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1ab5ac77e4
00dd475748236a6cc81/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/09/06 high Unknown
Rule Details: CrackMapExec Command Execution
Detect various execution methods of the CrackMapExec pentesting framework.
Rule ID
process_creation_commandline_99
Query
{'selection': {'CommandLine|endswith': ['cmd.exe /Q /c * 1> \\\\*\\*\\* 2>&1', 'cmd.e
xe /C * > \\\\*\\*\\* 2>&1', 'cmd.exe /C * > *\\Temp\\* 2>&1'], 'CommandLine|contains
': ['powershell.exe -exec bypass -noni -nop -w 1 -C "', 'powershell.exe -noni -nop -
w 1 -enc ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,058f4380-962d-40a5-afce-50207d36d7e2
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0002 , T1047 , T1059 , TA0003 , T1053 
References
https://github.com/byt3bl33d3r/CrackMapExec 
Severity

74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/05/22 high Unknown
Rule Details: DevInit Lolbin Download
Detects a certain command line flag combination used by devinit.exe lolbin to download arbitrary
MSI packages on a Windows system.
Rule ID
process_creation_commandline_100
Query
{'selection': {'CommandLine|contains|all': [' -t msi-install ', ' -
i http']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90d50722-0483-4065-8e35-57efaadd354d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://twitter.com/mrd0x/status/1460815932402679809 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/11 high Unknown

Rule Details: Sticky-Key Backdoor Copy Cmd.exe
By replacing the sticky keys executable with the local admins CMD executable, an attacker is
able to access a privileged windows console session without authenticating to the system. When
the sticky keys are "activated" the privilleged shell is launched.
Rule ID
process_creation_commandline_101
Query
{'selection': {'CommandLine': 'copy /y C:\\windows\\system32\\cmd.exe C:\\windows\\sy
stem32\\sethc.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1070db9a-3e5d-412e-8e7b-7183b616e1b3
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.008 
References
https://www.fireeye.com/blog/threat-research/2017/03/apt29_domain_frontin.html 
https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-
Campaign-v1.pdf 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/02/18 medium Unknown
Rule Details: Suspicious Use of Procdump on LSASS
Detects suspicious uses of the SysInternals Procdump utility by using a special command line
parameter in combination with the lsass.exe process. This way we're also able to catch cases in
which the attacker has renamed the procdump executable.
Rule ID

process_creation_commandline_102
Query
{'selection1': {'CommandLine|contains': [' -
ma ', ' /ma ']}, 'selection2': {'CommandLine|contains': ' ls'}, 'condition': 'all of
selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5afee48e-67dd-4e03-a783-f74259dcf998
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036 , TA0006 , T1003.001 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/10/30 high Unlikely, because no one should dump an lsass process memory
Another tool that uses the command line switches of Procdump
Rule Details: Suspicious Rundll32 Activity Invoking Sys File
Detects suspicious process related to rundll32 based on command line that includes a *.sys file
as seen being used by UNC2452.
Rule ID
process_creation_commandline_103
Query
{'selection1': {'CommandLine|contains': 'rundll32.exe'}, 'selection2': {'CommandLine|
contains': ['.sys,', '.sys ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,731231b9-0b5d-4219-94dd-abb6959aa7ea
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-
nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high Unknown
Rule Details: ETW Logging Tamper In .NET Processes
Detects changes to environment variables related to ETW logging. This could indicate potential
adversaries stopping ETW providers recording loaded .NET assemblies.
Rule ID
process_creation_commandline_104
Query
{'selection': {'CommandLine|contains': ['COMPlus_ETWEnabled', 'COMPlus_ETWFlags']}, '
condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,41421f44-58f9-455d-838a-c398859841d4
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562 

References
https://twitter.com/_xpn_/status/1268712093928378368 
https://github.com/dotnet/runtime/blob/ee2355c801d892f2894b0f7b14a20e6cc50e0e54/
docs/design/coreclr/jit/viewing-jit-dumps.md#setting-configuration-variables 
https://github.com/dotnet/runtime/blob/f62e93416a1799aecc6b0947adad55a0d9870732
/src/coreclr/src/inc/clrconfigvalues.h#L35-L38 
https://github.com/dotnet/runtime/blob/7abe42dc1123722ed385218268bb9fe04556e3d3
/src/coreclr/src/inc/clrconfig.h#L33-L39 
http://managed670.rssing.com/chan-5590147/all_p1.html 
https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227d30e723/d
ocs/coding-guidelines/clr-jit-coding-conventions.md#1412-disabling-code 
https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-No-Vici-
Attacks-On-ETW-Blind-EDRs.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/02 high Unlikely
Rule Details: Suspicious WMIC Execution - ProcessCallCreate
Detects WMIC executing "process call create" with suspicious calls to processes such as
"rundll32", "regsrv32"...etc.
Rule ID
process_creation_commandline_105
Query
{'selection': {'CommandLine|contains|all': ['process ', 'call ', 'create '], 'Command
Line|contains': ['rundll32', 'bitsadmin', 'regsvr32', 'cmd.exe /c ', 'cmd.exe /k ', '
cmd.exe /r ', 'cmd /c ', 'cmd /k ', 'cmd /r ', 'powershell', 'pwsh', 'certutil', 'csc
ript', 'wscript', 'mshta', '\\Users\\Public\\', '\\Windows\\Temp\\', '\\AppData\\Loca
l\\', '%temp%', '%tmp%', '%ProgramData%', '%appdata%', '%comspec%', '%localappdata%']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,3c89a1e8-0fba-449e-8f1b-8409d6267ec8
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1047 , T1059.003 
References
https://thedfirreport.com/2020/10/08/ryuks-return/ 
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ransomware-
hive-conti-avoslocker 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high Unknown
Rule Details: Potential APT-C-12 BlueMushroom DLL Load Activity Via Regsvr32
Detects potential BlueMushroom DLL loading activity via regsvr32 from AppData Local.
Rule ID
process_creation_commandline_106
Query
{'selection': {'CommandLine|contains|all': ['regsvr32', '\\AppData\\Local\\', '.dll',
',DllEntry']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bd70d3f8-e60e-4d25-89f0-0b5a9cff20e0
Author: Florian Roth (Nextron Systems), Tim Shelton, Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.010 

References
https://pbs.twimg.com/media/EF3yLGoWkAEGeLa?format=jpg 
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/02 medium Unknown
Rule Details: Mshtml DLL RunHTMLApplication Abuse
Detects suspicious command line using the "mshtml.dll" RunHTMLApplication export to run
arbitrary code via different protocol handlers (vbscript, javascript, file, htpp...).
Rule ID
process_creation_commandline_107
Query
{'selection': {'CommandLine|contains|all': ['\\..\\', 'mshtml', 'RunHTMLApplication']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,4782eb5a-a513-4523-a0ac-f3082b26ac5c
Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems), Josh
Nickels, frack113, Zaw Min Htun (ZETA)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/n1nj4sec/status/1421190238081277959 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/14 high Unlikely
Rule Details: Persistence Via TypedPaths - CommandLine
Detects modification addition to the 'TypedPaths' key in the user or admin registry via the
commandline. Which might indicate persistence attempt.
Rule ID
process_creation_commandline_109
Query
{'selection': {'CommandLine|contains': '\\Software\\Microsoft\\Windows\\CurrentVersio
n\\Explorer\\TypedPaths'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ec88289a-7e1a-4cc3-8d18-bd1f60e4b9ba
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/dez_/status/1560101453150257154 
https://forensafe.com/blogs/typedpaths.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/22 medium Unknown
Rule Details: UtilityFunctions.ps1 Proxy Dll
Detects the use of a Microsoft signed script executing a managed DLL with PowerShell.

Rule ID
process_creation_commandline_110
Query
{'selection': {'CommandLine|contains': ['UtilityFunctions.ps1', 'RegSnapin ']}, 'cond
ition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0403d67d-6227-4ea8-8145-4e72db7da120
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/UtilityFunctions/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/28 medium Unknown
Rule Details: Unidentified Attacker November 2018
A sigma rule detecting an unidetefied attacker who used phishing emails to target high profile
orgs on November 2018. The Actor shares some TTPs with YYTRIUM/APT29 campaign in 2016.
Rule ID
process_creation_commandline_111
Query
{'selection': {'CommandLine|contains': 'cyzfc.dat,', 'CommandLine|endswith': 'PointFu
nctionCall'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,7453575c-a747-40b9-839b-125a0aae324b
Author: Florian Roth (Nextron Systems), @41thexplorer
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://twitter.com/DrunkBinary/status/1063075530180886529 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/11/20 high N/A
Rule Details: Powershell AMSI Bypass via .NET Reflection
Detects Request to "amsiInitFailed" that can be used to disable AMSI Scanning.
Rule ID
process_creation_commandline_112
Query
{'selection': {'CommandLine|contains': ['System.Management.Automation.AmsiUtils', 'am
siInitFailed']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,30edb182-aa75-42c0-b0a9-e998bb29067c
Author: Markus Neis, @Kostastsale
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/ 

Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/08/17 high Unlikely
Rule Details: PowerShell SAM Copy
Detects suspicious PowerShell scripts accessing SAM hives.
Rule ID
process_creation_commandline_113
Query
{'selection_1': {'CommandLine|contains|all': ['\\HarddiskVolumeShadowCopy', 'System32
\\config\\sam']}, 'selection_2': {'CommandLine|contains': ['Copy-
Item', 'cp $_.', 'cpi $_.', 'copy $_.', '.File]::Copy(']}, 'condition': 'all of selec
tion*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1af57a4b-460a-4738-9034-db68b880c665
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003.002 
References
https://twitter.com/splinter_code/status/1420546784250769408 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/07/29 high Some rare backup scenarios
PowerShell scripts fixing HiveNightmare / SeriousSAM ACLs
Rule Details: UAC Bypass Using Event Viewer RecentViews
Detects the pattern of UAC Bypass using Event Viewer RecentViews.
Rule ID
process_creation_commandline_114
Query
{'selection_path': {'CommandLine|contains': ['\\Event Viewer\\RecentViews', '\\EventV
~1\\RecentViews']}, 'selection_redirect': {'CommandLine|contains': '>'}, 'condition':
'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,30fc8de7-d833-40c4-96b6-28319fbc4f6c
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/orange_8361/status/1518970259868626944 
https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/#execute 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/11/22 high Unknown
Rule Details: Suspicious Office Token Search Via CLI
Detects possible search for office tokens via CLI by looking for the string "eyJ0eX". This string is
used as an anchor to look for the start of the JWT token used by office and similar apps.

Rule ID
process_creation_commandline_115
Query
{'selection': {'CommandLine|contains': ['eyJ0eXAiOi', ' eyJ0eX', ' "eyJ0eX"', " 'eyJ0
eX'"]}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6d3a3952-6530-44a3-8554-cf17c116c615
Author: Nasreddine Bencherchali (Nextron Systems), kagebunsher
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1528 
References
https://mrd0x.com/stealing-tokens-from-office-applications/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/25 medium Legitimate command-lines containing the string mentioned in the command-line
Rule Details: Change Default File Association To Executable
Detects when a program changes the default file association of any extension to an executable.
Rule ID
process_creation_commandline_116
Query
{'selection': {'CommandLine|contains|all': ['cmd', 'assoc ', 'exefile'], 'CommandLine
|contains': [' /c ', ' /r ', ' /k ']}, 'filter': {'CommandLine|contains': '.exe=exefi
le'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,ae6f14e6-14de-45b0-9f44-c0986f50dc89
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.001 
References
https://docs.microsoft.com/en-us/windows-server/administration/windows-
commands/assoc 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/06/28 high Unknown
Rule Details: Conti Backup Database
Detects a command used by conti to dump database.
Rule ID
process_creation_commandline_118
Query
{'selection_tools': {'CommandLine|contains': ['sqlcmd ', 'sqlcmd.exe']}, 'selection_s
vr': {'CommandLine|contains': ' -
S localhost '}, 'selection_query': {'CommandLine|contains': ['sys.sysprocesses', 'mas
ter.dbo.sysdatabases', 'BACKUP DATABASE']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2f47f1fd-0901-466e-a770-3b7092834a1b
Author: frack113
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0009 , T1005 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9d
aecaf06331a95410aa5f8/detection 
https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/16 high Unknown
Rule Details: Winnti Pipemon Characteristics
Detects specific process characteristics of Winnti Pipemon malware reported by ESET.
Rule ID
process_creation_commandline_119
Query
{'selection1': {'CommandLine|contains': 'setup0.exe -
p'}, 'selection2a': {'CommandLine|contains': 'setup.exe'}, 'selection2b': {'CommandLi
ne|endswith': ['-x:0', '-x:1', '-
x:2']}, 'condition': 'selection1 or all of selection2*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,73d70463-75c9-4258-92c6-17500fe972f2
Author: Florian Roth (Nextron Systems), oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1574.002 
References
https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/ 

Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2020/07/30 critical Legitimate setups that use similar flags
Rule Details: Suspicious ZipExec Execution
ZipExec is a Proof-of-Concept (POC) tool to wrap binary-based tools into a password-protected
zip file.
Rule ID
process_creation_commandline_120
Query
{'run': {'CommandLine|contains|all': ['/generic:Microsoft_Windows_Shell_ZipFolder:fil
ename=', '.zip', '/pass:', '/user:']}, 'delete': {'CommandLine|contains|all': ['/dele
te', 'Microsoft_Windows_Shell_ZipFolder:filename=', '.zip']}, 'condition': 'run or de
lete'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90dcf730-1b71-4ae7-9ffc-6fcf62bd0132
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , T1202 
References
https://twitter.com/SBousseaden/status/1451237393017839616 
https://github.com/Tylous/ZipExec 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
| Maturity | Creation Date |     | Risk Level |     | False Positives |
| -------- | ------------- | --- | ---------- | --- | --------------- |
| test     | 2021/11/07    |     | medium     |     |                 |
Unknown
Rule Details: NirCmd Tool Execution As LOCAL SYSTEM
Detects the use of NirCmd tool for command execution as SYSTEM user.
Rule ID
process_creation_commandline_121
Query
{'selection': {'CommandLine|contains': ' runassystem '}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d9047477-0359-48c9-b8c7-792cedcdc9c4
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
| TA0002 | , T1569.002 | , T1059.003 |    |     |     |
| ------ | ------------ | ------------ | --- | --- | --- |
References
|     | https://www.nirsoft.net/utils/nircmd.html |     |     |    |     |
| --- | ----------------------------------------- | --- | --- | --- | --- |
https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-
windows/ 
|     | https://www.nirsoft.net/utils/nircmd2.html#using |     |     |    |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- |
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |                                  |     |
| -------- | ------------- | ---------- | --------------- | -------------------------------- | --- |
| test     | 2022/01/24    | high       |                 | Legitimate use by administrators |     |
Rule Details: Invoke-Obfuscation Via Use Clip
Detects Obfuscated Powershell via use Clip.exe in Scripts.

Rule ID
process_creation_commandline_122
Query
{'selection': {'CommandLine|contains|all': ['echo', 'clip', '&&'], 'CommandLine|conta
ins': ['clipboard', 'invoke', 'i`', 'n`', 'v`', 'o`', 'k`', 'e`']}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e1561947-b4e3-4a74-9bdd-83baed21bdb5
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/09 high Unknown
Rule Details: PowerShell Base64 Encoded Shellcode
Detects Base64 encoded Shellcode.
Rule ID
process_creation_commandline_123
Query
{'selection': {'CommandLine|contains': ['OiCAAAAYInlM', 'OiJAAAAYInlM']}, 'condition'
: 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,2d117e49-e626-4c7c-bd1f-c3c0147774c8
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://twitter.com/cyb3rops/status/1063072865992523776 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/11/17 critical Unknown
Rule Details: Ryuk Ransomware
Detects Ryuk ransomware activity.
Rule ID
process_creation_commandline_124
Query
{'selection': {'CommandLine|contains|all': ['Microsoft\\Windows\\CurrentVersion\\Run'
, 'C:\\users\\Public\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c37510b8-2107-4b78-aa32-72f251e7a844
Author: Florian Roth (Nextron Systems), Vasiliy Burov, Nasreddine Bencherchali (Nextron
Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References

https://app.any.run/tasks/d860402c-3ff4-4c1f-b367-0237da714ed1/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/12/16 high Unlikely
Rule Details: Arbitrary Shell Command Execution Via Settingcontent-Ms
The .SettingContent-ms file type was introduced in Windows 10 and allows a user to create
"shortcuts" to various Windows 10 setting pages. These files are simply XML and contain paths
to various Windows 10 settings binaries.
Rule ID
process_creation_commandline_125
Query
{'selection': {'CommandLine|contains': '.SettingContent-
ms'}, 'filter': {'CommandLine|contains': 'immersivecontrolpanel'}, 'condition': 'sele
ction and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,24de4f3b-804c-4165-b442-5a06a2302c7e
Author: Sreeman
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , TA0002 , T1204 , T1059.003 
References
https://posts.specterops.io/the-tale-of-settingcontent-ms-files-f1ea253e4d39 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/03/13 medium Unknown
Rule Details: Base64 Encoded Reflective Assembly Load
Detects base64 encoded .NET reflective loading of Assembly.
Rule ID
process_creation_commandline_127
Query
{'selection': {'CommandLine|contains': ['WwBSAGUAZgBsAGUAYwB0AGkAbwBuAC4AQQBzAHMAZQBt
AGIAbAB5AF0AOgA6AEwAbwBhAGQAKA', 'sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAe
QBdADoAOgBMAG8AYQBkACgA', 'bAFIAZQBmAGwAZQBjAHQAaQBvAG4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6A
DoATABvAGEAZAAoA', 'AFsAcgBlAGYAbABlAGMAdABpAG8AbgAuAGEAcwBzAGUAbQBiAGwAeQBdADoAOgAoA
CIATABvAGEAZAAiAC', 'BbAHIAZQBmAGwAZQBjAHQAaQBvAG4ALgBhAHMAcwBlAG0AYgBsAHkAXQA6ADoAKA
AiAEwAbwBhAGQAIgAp', 'AWwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAbAB5AF0AOgA6AC
gAIgBMAG8AYQBkACIAK', 'WwBSAGUAZgBsAGUAYwB0AGkAbwBuAC4AQQBzAHMAZQBtAGIAbAB5AF0AOgA6AC
gAIgBMAG8AYQBkACIAKQ', 'sAUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAeQBdADoAOgA
oACIATABvAGEAZAAiACkA', 'bAFIAZQBmAGwAZQBjAHQAaQBvAG4ALgBBAHMAcwBlAG0AYgBsAHkAXQA6ADo
AKAAiAEwAbwBhAGQAIgApA', 'WwByAGUAZgBsAGUAYwB0AGkAbwBuAC4AYQBzAHMAZQBtAGIAbAB5AF0AOgA
6AEwAbwBhAGQAKA', 'sAcgBlAGYAbABlAGMAdABpAG8AbgAuAGEAcwBzAGUAbQBiAGwAeQBdADoAOgBMAG8A
YQBkACgA', 'bAHIAZQBmAGwAZQBjAHQAaQBvAG4ALgBhAHMAcwBlAG0AYgBsAHkAXQA6ADoATABvAGEAZAAo
A']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,62b7ccc9-23b4-471e-aa15-6da3663c4d59
Author: Christian Burkard (Nextron Systems), pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08d
cb6/yara/mal_revil.yar 
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high Unlikely
Rule Details: Suspicious NT Resource Kit Auditpol Usage
Threat actors can use an older version of the auditpol binary available inside the NT resource kit
to change audit policy configuration to impair detection capability. This can be carried out by
selectively disabling/removing certain audit policies as well as restoring a custom policy owned
by the threat actor.
Rule ID
process_creation_commandline_128
Query
{'selection': {'CommandLine|contains': ['/logon:none', '/system:none', '/sam:none', '
/privilege:none', '/object:none', '/process:none', '/policy:none']}, 'condition': 'se
lection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c6c56ada-612b-42d1-9a29-adad3c5c2c1e
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.002 
References
https://github.com/3CORESec/MAL-
CL/tree/master/Descriptors/Windows%202000%20Resource%20Kit%20Tools/AuditPol

Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/18 high Unknown
Rule Details: Weak or Abused Passwords In CLI
Detects weak passwords or often abused passwords (seen used by threat actors) via the CLI. An
example would be a threat actor creating a new user via the net command and providing the
password inline.
Rule ID
process_creation_commandline_129
Query
{'selection': {'CommandLine|contains': ['Asd123.aaaa', 'password123', '123456789', 'P
@ssw0rd!']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,91edcfb1-2529-4ac2-9ecc-7617f895c7e4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-
governments 
https://thedfirreport.com/2022/09/26/bumblebee-round-two/ 
https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-
opportunistic-ransomware-campaigns-impacting-us-education-sector/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experiment 2022/09/14 medium Legitimate usage of the passwords by users via commandline (should be
discouraged)
al
Other currently unknown false positives
Rule Details: Suspicious Encoded Obfuscated LOAD String
Detects suspicious base64 encoded and obbfuscated LOAD string often used for
reflection.assembly load.
Rule ID
process_creation_commandline_130
Query
{'selection': {'CommandLine|contains': ['OgA6ACgAIgBMACIAKwAiAG8AYQBkACIAKQ', 'oAOgAo
ACIATAAiACsAIgBvAGEAZAAiACkA', '6ADoAKAAiAEwAIgArACIAbwBhAGQAIgApA', 'OgA6ACgAIgBMAG8
AIgArACIAYQBkACIAKQ', 'oAOgAoACIATABvACIAKwAiAGEAZAAiACkA', '6ADoAKAAiAEwAbwAiACsAIgB
hAGQAIgApA', 'OgA6ACgAIgBMAG8AYQAiACsAIgBkACIAKQ', 'oAOgAoACIATABvAGEAIgArACIAZAAiACk
A', '6ADoAKAAiAEwAbwBhACIAKwAiAGQAIgApA', 'OgA6ACgAJwBMACcAKwAnAG8AYQBkACcAKQ', 'oAOg
AoACcATAAnACsAJwBvAGEAZAAnACkA', '6ADoAKAAnAEwAJwArACcAbwBhAGQAJwApA', 'OgA6ACgAJwBMA
G8AJwArACcAYQBkACcAKQ', 'oAOgAoACcATABvACcAKwAnAGEAZAAnACkA', '6ADoAKAAnAEwAbwAnACsAJ
wBhAGQAJwApA', 'OgA6ACgAJwBMAG8AYQAnACsAJwBkACcAKQ', 'oAOgAoACcATABvAGEAJwArACcAZAAnA
CkA', '6ADoAKAAnAEwAbwBhACcAKwAnAGQAJwApA']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9c0295ce-d60d-40bd-bd74-84673b7592b1
Author: pH-T (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08d
cb6/yara/mal_revil.yar 
https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high Unlikely
Rule Details: RunXCmd Tool Execution As System
Detects the use of RunXCmd tool for command execution.
Rule ID
process_creation_commandline_131
Query
{'selection': {'CommandLine|contains|all': [' /account=system ', '/exec=']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,93199800-b52a-4dec-b762-75212c196542
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , T1059.003 
References
https://www.d7xtech.com/free-software/runx/ 
https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-
windows/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/24 high Legitimate use by administrators
Rule Details: Base64 Encoded Listing of Shadowcopy
Detects base64 encoded listing Win32_Shadowcopy.

Rule ID
process_creation_commandline_132
Query
{'selection': {'CommandLine|contains': ['VwBpAG4AMwAyAF8AUwBoAGEAZABvAHcAYwBvAHAAeQAg
AHwAIABGAG8AcgBFAGEAYwBoAC0ATwBiAGoAZQBjAHQA', 'cAaQBuADMAMgBfAFMAaABhAGQAbwB3AGMAbwB
wAHkAIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0A', 'XAGkAbgAzADIAXwBTAGgAYQBkAG8Adw
BjAG8AcAB5ACAAfAAgAEYAbwByAEUAYQBjAGgALQBPAGIAagBlAGMAdA']}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,47688f1b-9f51-4656-b013-3cc49a166a36
Author: Christian Burkard (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08d
cb6/yara/mal_revil.yar 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/03/01 high Unlikely
Rule Details: MERCURY Command Line Patterns
Detects suspicious command line patterns as seen being used by MERCURY threat actor.
Rule ID
process_creation_commandline_133
Query
{'selection_base': {'CommandLine|contains|all': ['-exec bypass -w 1 -
enc', 'UwB0AGEAcgB0AC0ASgBvAGIAIAAtAFMAYwByAGkAcAB0AEIAbABvAGMAaw']}, 'condition': 'a

ll of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a62298a3-1fe0-422f-9a68-ffbcbc5a123d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://www.microsoft.com/security/blog/2022/08/25/mercury-leveraging-log4j-2-
vulnerabilities-in-unpatched-systems-to-target-israeli-organizations/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/26 high Unknown
Rule Details: DTRACK Process Creation
Detects specific process parameters as seen in DTRACK infections.
Rule ID
process_creation_commandline_134
Query
{'selection': {'CommandLine|contains': ' echo EEEE > '}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f1531fa4-5b84-4342-8f68-9cf3fdbd83d4
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0040 , T1490 
References
https://securelist.com/my-name-is-dtrack/93338/ 
https://app.any.run/tasks/4bc9860d-ab51-4077-9e09-59ad346b92fd/ 
https://app.any.run/tasks/ce4deab5-3263-494f-93e3-afb2b9d79f14/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/10/30 critical Unlikely
Rule Details: Suspicious Netsh Discovery Command
Adversaries may look for details about the network configuration and settings of systems they
access or through information discovery of remote systems.
Rule ID
process_creation_commandline_135
Query
{'selection': {'CommandLine|contains|all': ['netsh ', 'show ', 'firewall '], 'Command
Line|contains': ['config ', 'state ', 'rule ', 'name=all']}, 'condition': 'selection'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0e4164da-94bc-450d-a7be-a4b176179f1f
Author: frack113, Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1016 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T1016.md#ato
mic-test-2---list-windows-firewall-rules 

Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/07 low Administrative activity
Rule Details: F-Secure C3 Load by Rundll32
F-Secure C3 produces DLLs with a default exported StartNodeRelay function.
Rule ID
process_creation_commandline_136
Query
{'selection': {'CommandLine|contains|all': ['rundll32.exe', '.dll', 'StartNodeRelay']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b18c9d4c-fac9-4708-bd06-dd5bfacf200f
Author: Alfie Champion (ajpc500)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://github.com/FSecureLABS/C3/blob/11a081fd3be2aaf2a879f6b6e9a96ecdd24966
ef/Src/NodeRelayDll/NodeRelayDll.cpp#L12 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2021/06/02 critical Unknown
Rule Details: Suspicious RunAs-Like Flag Combination
Detects suspicious command line flags that let the user set a target user and command as e.g.
seen in PsExec-like tools.
Rule ID
process_creation_commandline_137
Query
{'selection_user': {'CommandLine|contains': [' -u system ', ' --user system ', ' -
u NT', ' -u "NT', " -u 'NT", ' --system ', ' -
u administrator ']}, 'selection_command': {'CommandLine|contains': [' -c cmd', ' -
c "cmd', ' -c powershell', ' -c "powershell', ' --command cmd', ' --
command powershell', ' -c whoami', ' -c wscript', ' -
c cscript']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,50d66fb0-03f8-4da0-8add-84e77d12a020
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://www.trendmicro.com/en_us/research/22/k/hack-the-real-box-apt41-new-
subgroup-earth-longzhi.html 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/11 medium Unknown
Rule Details: Stop Or Remove Antivirus Service

Detects usage of 'Stop-Service' or 'Remove-Service' powershell cmdlet to disable AV services.
Adversaries may disable security tools to avoid possible detection of their tools and activities by
stopping antivirus service.
Rule ID
process_creation_commandline_138
Query
{'selection_action': {'CommandLine|contains': ['Stop-Service ', 'Remove-
Service ']}, 'selection_product': {'CommandLine|contains': [' McAfeeDLPAgentService',
' Trend Micro Deep Security Manager', ' TMBMServer', 'Sophos', 'Symantec']}, 'condit
ion': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6783aa9e-0dc3-49d4-a94a-8b39c5fd700b
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001
.md 
https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-
ransomware-attack/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/07/07 high Unknown
Rule Details: Adwind RAT / JRAT
Detects javaw.exe in AppData folder as used by Adwind / JRAT.
Rule ID

process_creation_commandline_139
Query
{'selection': [{'CommandLine|contains|all': ['\\AppData\\Roaming\\Oracle', '\\java',
'.exe ']}, {'CommandLine|contains|all': ['cscript.exe', 'Retrive', '.vbs ']}], 'condi
tion': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1fac1481-2dbc-48b2-9096-753c49b4ec71
Author: Florian Roth (Nextron Systems), Tom Ueltschi, Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://www.hybrid-
analysis.com/sample/ba86fa0d4b6af2db0656a88b1dd29f36fe362473ae8ad04255c4e5
2f214a541c?environmentId=100 
https://www.first.org/resources/papers/conf2017/Advanced-Incident-Detection-and-
Threat-Hunting-using-Sysmon-and-Splunk.pdf 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/10 high N/A
Rule Details: Suspicious AdvancedRun Runas Priv User
Detects the execution of AdvancedRun utility in the context of the TrustedInstaller, SYSTEM,
Local Service or Network Service accounts.
Rule ID
process_creation_commandline_140
Query
{'selection': {'CommandLine|contains': ['/EXEFilename', '/CommandLine']}, 'selection_
runas': [{'CommandLine|contains': [' /RunAs 8 ', ' /RunAs 4 ', ' /RunAs 10 ', ' /RunA

s 11 ']}, {'CommandLine|endswith': ['/RunAs 8', '/RunAs 4', '/RunAs 10', '/RunAs 11']
}], 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fa00b701-44c6-4679-994d-5a18afa8a707
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://twitter.com/splinter_code/status/1483815103279603714 
https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-
ukraine-9d5d158f19f3 
https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-
windows/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/01/20 high Unknown
Rule Details: ShimCache Flush
Detects actions that clear the local ShimCache and remove forensic evidence.
Rule ID
process_creation_commandline_141
Query
{'selection1a': {'CommandLine|contains|all': ['rundll32', 'apphelp.dll']}, 'selection
1b': {'CommandLine|contains': ['ShimFlushCache', '#250']}, 'selection2a': {'CommandLi
ne|contains|all': ['rundll32', 'kernel32.dll']}, 'selection2b': {'CommandLine|contain
s': ['BaseFlushAppcompatCache', '#46']}, 'condition': '( selection1a and selection1b
) or ( selection2a and selection2b )'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b0524451-19af-4efa-a46f-562a977f792e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1112 
References
https://medium.com/@blueteamops/shimcache-flush-89daff28d15e 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2021/02/01 high Unknown
Rule Details: Sliver C2 Implant Activity Pattern
Detects process activity patterns as seen being used by Sliver C2 framework implants.
Rule ID
process_creation_commandline_142
Query
{'selection_cmdline': {'CommandLine|contains': '-NoExit -
Command [Console]::OutputEncoding=
[Text.UTF8Encoding]::UTF8'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,42333b2c-b425-441c-b70e-99404a17170f
Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059.003 
References
https://github.com/BishopFox/sliver/blob/79f2d48fcdfc2bee4713b78d431ea4b27f733f30
/implant/sliver/shell/shell_windows.go#L36 
https://www.microsoft.com/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-
for-emerging-command-and-control-frameworks/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/25 critical Unlikely
Rule Details: Disabled IE Security Features
Detects command lines that indicate unwanted modifications to registry keys that disable
important Internet Explorer security features.
Rule ID
process_creation_commandline_143
Query
{'selection1': {'CommandLine|contains|all': [' -name IEHarden ', ' -
value 0 ']}, 'selection2': {'CommandLine|contains|all': [' -name DEPOff ', ' -
value 1 ']}, 'selection3': {'CommandLine|contains|all': [' -
name DisableFirstRunCustomize ', ' -value 2 ']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fb50eb7a-5ab1-43ae-bcc9-091818cb8424
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References

https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-new-tidepool-
malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2020/06/19 high Unknown, maybe some security software installer disables these features
temporarily
Rule Details: Invoke-Obfuscation RUNDLL LAUNCHER
Detects Obfuscated Powershell via RUNDLL LAUNCHER.
Rule ID
process_creation_commandline_144
Query
{'selection': {'CommandLine|contains|all': ['rundll32.exe', 'shell32.dll', 'shellexec
_rundll', 'powershell']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,056a7ee1-4853-4e67-86a0-3fd9ceed7555
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/18 medium Unknown
Rule Details: Tasks Folder Evasion
The Tasks folder in system32 and syswow64 are globally writable paths. Adversaries can take
advantage of this and load or influence any script hosts or ANY .NET Application in Tasks to load
and execute a custom assembly into cscript, wscript, regsvr32, mshta, eventvwr.
Rule ID
process_creation_commandline_145
Query
{'selection1': {'CommandLine|contains': ['echo ', 'copy ', 'type ', 'file createnew']
}, 'selection2': {'CommandLine|contains': [' C:\\Windows\\System32\\Tasks\\', ' C:\\W
indows\\SysWow64\\Tasks\\']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cc4e02ba-9c06-48e2-b09e-2500cace9ae0
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1574.002 
References
https://twitter.com/subTee/status/1216465628946563073 
https://gist.github.com/am0nsec/8378da08f848424e4ab0cc5b317fdd26 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/13 high Unknown
Rule Details: Sofacy Trojan Loader Activity
Detects Trojan loader activity as used by APT28.

Rule ID
process_creation_commandline_146
Query
{'selection1': {'CommandLine|contains|all': ['rundll32.exe', '%APPDATA%\\']}, 'select
ion2': [{'CommandLine|contains': '.dat",'}, {'CommandLine|endswith': ['.dll",#1', '.d
ll #1', '.dll" #1']}], 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ba778144-5e3d-40cf-8af9-e28fb1df1e20
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218.011 
References
https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-
government-entities/ 
https://twitter.com/ClearskySec/status/960924755355369472 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/01 high Unknown
Rule Details: Suspicious Commandline Escape
Detects suspicious process that use escape characters.
Rule ID
process_creation_commandline_147
Query
{'selection': {'CommandLine|contains': ['h^t^t^p', 'h"t"t"p']}, 'condition': 'selecti
on'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f0cdd048-82dc-4f7a-8a7a-b87a52b6d0fd
Author: juju4
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1140 
References
https://twitter.com/vysecurity/status/885545634958385153 
https://twitter.com/Hexacorn/status/885553465417756673 
https://twitter.com/Hexacorn/status/885570278637678592 
https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html 
http://www.windowsinspired.com/understanding-the-command-line-string-and-
arguments-received-by-a-windows-program/ 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2018/12/11 low False positives depend on scripts and administrative tools used in the monitored
environment
Rule Details: Suspicious Rundll32 Invoking Inline VBScript
Detects suspicious process related to rundll32 based on command line that invokes inline
VBScript as seen being used by UNC2452.
Rule ID
process_creation_commandline_148
Query
{'selection': {'CommandLine|contains|all': ['rundll32.exe', 'Execute', 'RegRead', 'wi
ndow.close']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1cc50f3f-1fc8-4acf-b2e9-6f172e1fdebd
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1055 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-
nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high Unknown
Rule Details: Disabled Volume Snapshots
Detects commands that temporarily turn off Volume Snapshots.
Rule ID
process_creation_commandline_149
Query
{'selection': {'CommandLine|contains|all': ['reg', ' add ', '\\Services\\VSS\\Diag',
'/d Disabled']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,dee4af55-1f22-4e1d-a9d2-4bdc7ecb472a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 

References
https://twitter.com/0gtweet/status/1354766164166115331 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/28 high Legitimate administration
Rule Details: PowerShell Get-Clipboard Cmdlet Via CLI
Detects usage of the 'Get-Clipboard' cmdlet via CLI.
Rule ID
process_creation_commandline_150
Query
{'selection': {'CommandLine|contains': 'Get-Clipboard'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b9aeac14-2ffd-4ad3-b967-1354a4e628c3
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1115 
References
https://github.com/OTRF/detection-hackathon-apt29/issues/16 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2020/05/02 medium Unknown
Rule Details: Suspicious Reg Add BitLocker
Detects suspicious addition to BitLocker related registry keys via the reg.exe utility.
Rule ID
process_creation_commandline_151
Query
{'selection': {'CommandLine|contains|all': ['REG', 'ADD', '\\SOFTWARE\\Policies\\Micr
osoft\\FVE', '/v', '/f'], 'CommandLine|contains': ['EnableBDEWithNoTPM', 'UseAdvanced
Startup', 'UseTPM', 'UseTPMKey', 'UseTPMKeyPIN', 'RecoveryKeyMessageSource', 'UseTPMP
IN', 'RecoveryKeyMessage']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0e0255bf-2548-47b8-9582-c0955c9283f5
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-
ransomware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/15 high Unlikely
Rule Details: Suspicious Reconnaissance Activity Using Get-LocalGroupMember Cmdlet
Detects suspicious reconnaissance command line activity on Windows systems using the
PowerShell Get-LocalGroupMember Cmdlet.

Rule ID
process_creation_commandline_152
Query
{'selection_cmdlet': {'CommandLine|contains': 'Get-
LocalGroupMember '}, 'selection_group': {'CommandLine|contains': ['domain admins', '
administrator', ' administrateur', 'enterprise admins', 'Exchange Trusted Subsystem',
'Remote Desktop Users', 'Utilisateurs du Bureau à distance', 'Usuarios de escritorio
remoto']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c8a180d6-47a3-4345-a609-53f9c3d834fc
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1087.001 
References
https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/10 medium Administrative activity
Rule Details: Conti Ransomware Execution
Conti ransomware command line ioc.
Rule ID
process_creation_commandline_153
Query
{'selection': {'CommandLine|contains|all': ['-m ', '-net ', '-size ', '-nomutex ', '-
p \\\\', '$']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,689308fc-cfba-4f72-9897-796c1dc61487
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1486 
References
https://news.sophos.com/en-us/2021/09/03/conti-affiliates-use-proxyshell-exchange-
exploit-in-ransomware-attacks/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/10/12 critical Unlikely
Rule Details: Snatch Ransomware
Detects specific process characteristics of Snatch ransomware word document droppers.
Rule ID
process_creation_commandline_154
Query
{'selection': {'CommandLine|contains': ['shutdown /r /f /t 00', 'net stop SuperBackup
Man']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5325945e-f1f0-406e-97b8-65104d393fff
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1204 , T1059.003 

References
https://news.sophos.com/en-us/2019/12/09/snatch-ransomware-reboots-pcs-into-safe-
mode-to-bypass-protection/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
stable 2020/08/26 high Scripts that shutdown the system immediately and reboot them in safe mode are
unlikely
Rule Details: Copy from Volume Shadow Copy
Detects a copy execution that targets a shadow copy (sometimes used to copy registry hives that
are in use).
Rule ID
process_creation_commandline_155
Query
{'selection': {'CommandLine|contains': 'copy \\\\?
\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c73124a7-3e89-44a3-bdc1-25fe4df754b1
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9d
aecaf06331a95410aa5f8/detection 
https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/ 

Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/09 medium Some rare backup scenarios
Rule Details: Suspicious VBScript UN2452 Pattern
Detects suspicious inline VBScript keywords as used by UNC2452.
Rule ID
process_creation_commandline_156
Query
{'selection': {'CommandLine|contains|all': ['Execute', 'CreateObject', 'RegRead', 'wi
ndow.close', '\\Microsoft\\Windows\\CurrentVersion']}, 'filter': {'CommandLine|contai
ns': '\\Software\\Microsoft\\Windows\\CurrentVersion\\Run'}, 'condition': 'selection
and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,20c3f09d-c53d-4e85-8b74-6aa50e2f1b61
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References
https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-
nobelium-malware/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/03/05 high Unknown
Rule Details: Sensitive Registry Access via Volume Shadow Copy
Detects a command that accesses password storing registry hives via volume shadow backups.
Rule ID
process_creation_commandline_157
Query
{'selection_1': {'CommandLine|contains': '\\\\?
\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy'}, 'selection_2': {'CommandLine|contai
ns': ['\\NTDS.dit', '\\SYSTEM', '\\SECURITY', 'C:\\tmp\\log']}, 'condition': 'all of
selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f57f8d16-1f39-4dcb-a604-6c73d9b54b3d
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9d
aecaf06331a95410aa5f8/detection 
https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/09 high Some rare backup scenarios
Rule Details: Abusable Invoke-ATHRemoteFXvGPUDisablementCommand

RemoteFXvGPUDisablement.exe is an abusable, signed PowerShell host executable that was
introduced in Windows 10 and Server 2019 (OS Build 17763.1339).
Rule ID
process_creation_commandline_158
Query
{'selection_cmd': {'CommandLine|contains': 'Invoke-
ATHRemoteFXvGPUDisablementCommand '}, 'selection_opt': {'CommandLine|contains': ['-
ModuleName ', '-ModulePath ', '-ScriptBlock ', '-
RemoteFXvGPUDisablementFilePath']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a6fc3c46-23b8-4996-9ea2-573f4c4d88c5
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md 
https://github.com/redcanaryco/AtomicTestHarnesses/blob/7e1e4da116801e3d6fcc6be
db207064577e40572/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemo
teFXvGPUDisablementCommand.ps1 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/13 medium Unknown
Rule Details: Execute From Alternate Data Streams
Detects execution from an Alternate Data Stream (ADS). Adversaries may use NTFS file
attributes to hide their malicious data in order to evade detection.
Rule ID

process_creation_commandline_159
Query
{'selection_stream': {'CommandLine|contains': 'txt:'}, 'selection_tools_type': {'Comm
andLine|contains|all': ['type ', ' > ']}, 'selection_tools_makecab': {'CommandLine|co
ntains|all': ['makecab ', '.cab']}, 'selection_tools_reg': {'CommandLine|contains|all
': ['reg ', ' export ']}, 'selection_tools_regedit': {'CommandLine|contains|all': ['r
egedit ', ' /E ']}, 'selection_tools_esentutl': {'CommandLine|contains|all': ['esentu
tl ', ' /y ', ' /d ', ' /o ']}, 'condition': 'selection_stream and (1 of selection_to
ols_*)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7f43c430-5001-4f8b-aaa9-c3b88f18fa5c
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1564.004 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004
.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/09/01 medium Unknown
Rule Details: Potential Tampering With Security Products Via WMIC
Detects uninstallation or termination of security products using the WMIC utility.
Rule ID
process_creation_commandline_160
Query

{'selection_cli_1': {'CommandLine|contains|all': ['wmic', 'product where ', 'call uni
nstall', '/nointeractive']}, 'selection_cli_2': {'CommandLine|contains|all': ['wmic',
'caption like '], 'CommandLine|contains': ['call delete', 'call terminate']}, 'selec
tion_cli_3': {'CommandLine|contains|all': ['process ', 'where ', 'delete']}, 'selecti
on_product': {'CommandLine|contains': ['%carbon%', '%cylance%', '%endpoint%', '%eset%
', '%malware%', '%Sophos%', '%symantec%', 'Antivirus', 'AVG ', 'Carbon Black', 'Carbo
nBlack', 'Cb Defense Sensor 64-
bit', 'Crowdstrike Sensor', 'Cylance ', 'Dell Threat Defense', 'DLP Endpoint', 'Endpo
int Detection', 'Endpoint Protection', 'Endpoint Security', 'Endpoint Sensor', 'ESET
File Security', 'LogRhythm System Monitor Service', 'Malwarebytes', 'McAfee Agent', '
Microsoft Security Client', 'Sophos Anti-
Virus', 'Sophos AutoUpdate', 'Sophos Credential Store', 'Sophos Management Console',
'Sophos Management Database', 'Sophos Management Server', 'Sophos Remote Management S
ystem', 'Sophos Update Manager', 'Threat Protection', 'VirusScan', 'Webroot SecureAny
where', 'Windows Defender']}, 'condition': '1 of selection_cli_* and selection_produc
t'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,847d5ff3-8a31-4737-a970-aeae8fe21765
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 
References
https://twitter.com/cglyer/status/1355171195654709249 
https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/ 
https://www.mandiant.com/resources/unc2165-shifts-to-evade-sanctions 
https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-
ransomware-attack/ 
https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-group-
targets-manufacturing-companies.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/30 high Legitimate administration
Rule Details: Potential Download/Upload Activity Using Type Command
Detects usage of the "type" command to download/upload data from WebDAV server.
Rule ID
process_creation_commandline_161
Query
{'selection_upload': {'CommandLine|contains|all': ['type ', ' > \\\\']}, 'selection_d
ownload': {'CommandLine|contains|all': ['type \\\\', ' > ']}, 'condition': '1 of sele
ction_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://mr0range.com/a-new-lolbin-using-the-windows-type-command-to-upload-
download-files-81d7b6179e22 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/14 medium Unknown
Rule Details: Invoke-Obfuscation Via Stdin
Detects Obfuscated Powershell via Stdin in Scripts.
Rule ID

process_creation_commandline_162
Query
{'selection': {'CommandLine|contains|all': ['set', '&&'], 'CommandLine|contains': ['e
nvironment', 'invoke', 'input']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9c14c9fa-1a63-4a64-8e57-d19280559490
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high Unknown
Rule Details: Wscript Shell Run In CommandLine
Detects the presence of the keywords "Wscript", "Shell" and "Run" in the command, which could
indicate a suspicious activity.
Rule ID
process_creation_commandline_163
Query
{'selection': {'CommandLine|contains|all': ['Wscript.', '.Shell', '.Run']}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,2c28c248-7f50-417a-9186-a85b223010ee
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
http://blog.talosintelligence.com/2022/08/modernloader-delivers-multiple-
stealers.html 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/31 high Rare legitimate inline scripting by some administrators
Rule Details: Reg Add RUN Key
Detects suspicious command line reg.exe tool adding key to RUN key in Registry.
Rule ID
process_creation_commandline_164
Query
{'selection': {'CommandLine|contains|all': ['reg', ' ADD ', 'Software\\Microsoft\\Win
dows\\CurrentVersion\\Run']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,de587dce-915e-4218-aac4-835ca6af6f70
Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1547.001 
References
https://app.any.run/tasks/9c0f37bc-867a-4314-b685-e101566766d7/ 

https://docs.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-
keys 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2021/06/28 medium Legitimate software automatically (mostly, during installation) sets up autorun keys for
legitimate reasons.
Legitimate administrator sets up autorun keys for legitimate reasons.
Discord
Rule Details: Disable or Delete Windows Eventlog
Detects command that is used to disable or delete Windows eventlog via logman Windows utility.
Rule ID
process_creation_commandline_165
Query
{'selection_tools': {'CommandLine|contains': 'logman '}, 'selection_action': {'Comman
dLine|contains': ['stop ', 'delete ']}, 'selection_service': {'CommandLine|contains':
'EventLog-System'}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cd1f961e-0b96-436b-b7c6-38da4583ec00
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1562.001 , T1070.001 
References
https://twitter.com/0gtweet/status/1359039665232306183?s=21 
https://ss64.com/nt/logman.html 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/02/11 high Legitimate deactivation by administrative staff
Installer tools that disable services, e.g. before log collection agent installation
Rule Details: Java Running with Remote Debugging
Detects a JAVA process running with remote debugging allowing more than just localhost to
connect.
Rule ID
process_creation_commandline_166
Query
{'selection_jdwp_transport': {'CommandLine|contains': 'transport=dt_socket,address='}
, 'selection_old_jvm_version': {'CommandLine|contains': ['jre1.', 'jdk1.']}, 'exclusi
on': [{'CommandLine|contains': 'address=127.0.0.1'}, {'CommandLine|contains': 'addres
s=localhost'}], 'condition': 'all of selection* and not exclusion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8f88e3f6-2a49-48f5-a5c4-2f7eedf78710
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1203 , T1059.003 
References
https://dzone.com/articles/remote-debugging-java-applications-with-jdwp 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2019/01/16 medium Unknown
Rule Details: Monitoring For Persistence Via BITS
BITS will allow you to schedule a command to execute after a successful download to notify you
that the job is finished. When the job runs on the system the command specified in the BITS job
will be executed. This can be abused by actors to create a backdoor within the system and for
persistence. It will be chained in a BITS job to schedule the download of malware/additional
binaries and execute the program after being downloaded.
Rule ID
process_creation_commandline_167
Query
{'selection_1': {'CommandLine|contains|all': ['bitsadmin', '/SetNotifyCmdLine'], 'Com
mandLine|contains': ['%COMSPEC%', 'cmd.exe', 'regsvr32.exe']}, 'selection_2': {'Comma
ndLine|contains|all': ['bitsadmin', '/Addfile'], 'CommandLine|contains': ['http:', 'h
ttps:', 'ftp:', 'ftps:']}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b9cbbc17-d00d-4e3d-a827-b06d03d2380d
Author: Sreeman
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1197 
References
https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-
ransomware-chaser.html 
http://0xthem.blogspot.com/2014/03/t-emporal-persistence-with-and-schtasks.html 
https://isc.sans.edu/diary/Wipe+the+drive+Stealthy+Malware+Persistence+Mechanism+
-+Part+1/15394 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2020/10/29 medium Unknown
Rule Details: Obfuscated Command Line Using Special Unicode Characters
Adversaries may attempt to make an executable or file difficult to discover or analyze by
encrypting, encoding, or otherwise obfuscating its contents on the system or in transit.
Rule ID
process_creation_commandline_168
Query
{'selection': {'CommandLine|contains': ['â', '€', '£', '¯', '®', 'µ', '¶']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e0552b19-5a83-4222-b141-b36184bb8d79
Author: frack113, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1027 
References
https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027/T1027.md#ato
mic-test-6---dlp-evasion-via-sensitive-data-in-vba-macro-over-http 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/15 high Unknown
Rule Details: Compress Data and Lock With Password for Exfiltration With 7-ZIP
An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party
utilities.

Rule ID
process_creation_commandline_169
Query
{'selection_7z': {'CommandLine|contains': ['7z.exe', '7za.exe']}, 'selection_password
': {'CommandLine|contains': ' -
p'}, 'selection_action': {'CommandLine|contains': [' a ', ' u ']}, 'condition': 'all
of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9fbf5927-5261-4284-a71d-f681029ea574
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001
.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/27 medium Command line parameter combinations that contain all included strings
Rule Details: Suspicious DIR Execution
Detects usage of the "dir" command that's part of windows batch/cmd to collect information about
directories.
Rule ID
process_creation_commandline_170
Query

{'selection': {'CommandLine|contains|all': ['dir ', ' /s', ' /b']}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7c9340a9-e2ee-4e43-94c5-c54ebbea1006
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1217 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1217.md 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/13 low Unknown
Rule Details: Suspicious Diantz Download and Compress Into a CAB File
Download and compress a remote file and store it in a cab file on local machine.
Rule ID
process_creation_commandline_172
Query
{'selection': {'CommandLine|contains|all': ['diantz.exe', ' \\\\', '.cab']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,185d7418-f250-42d0-b72e-0c8b70661e93

Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://lolbas-project.github.io/lolbas/Binaries/Diantz/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/26 medium Unknown
Rule Details: Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION
Detects Obfuscated Powershell via VAR++ LAUNCHER.
Rule ID
process_creation_commandline_173
Query
{'selection': {'CommandLine|contains|all': ['&&set', 'cmd', '/c', '-
f'], 'CommandLine|contains': ['{0}', '{1}', '{2}', '{3}', '{4}', '{5}']}, 'condition'
: 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e9f55347-2928-4c06-88e5-1a7f8169942e
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 high Unknown
Rule Details: Ps.exe Renamed SysInternals Tool
Detects renamed SysInternals tool execution with a binary named ps.exe as used by Dragonfly
APT group and documented in TA17-293A report.
Rule ID
process_creation_commandline_174
Query
{'selection': {'CommandLine': 'ps.exe -accepteula'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,18da1007-3f26-470f-875d-f77faf1cab31
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1036.003 
References
https://www.us-cert.gov/ncas/alerts/TA17-293A 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/10/22 high Renamed SysInternals tool
Rule Details: TropicTrooper Campaign November 2018

Detects TropicTrooper activity, an actor who targeted high-profile organizations in the energy and
food and beverage sectors in Asia.
Rule ID
process_creation_commandline_175
Query
{'selection': {'CommandLine|contains': 'abCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCc'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8c7090c3-e0a0-4944-bd08-08c3a0cecf79
Author: @41thexplorer, Microsoft Defender ATP
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://cloudblogs.microsoft.com/microsoftsecure/2018/11/28/windows-defender-atp-
device-risk-score-exposes-new-cyberattack-drives-conditional-access-to-protect-
networks/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/11/12 high N/A
Rule Details: Shadow Copies Access via Symlink
Shadow Copies storage symbolic link creation using operating systems utilities.
Rule ID
process_creation_commandline_176
Query
{'selection': {'CommandLine|contains|all': ['mklink', 'HarddiskVolumeShadowCopy']}, '
condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,40b19fa6-d835-400c-b301-41f3a2baacaf
Author: Teymur Kheirkhabarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-
environment 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/22 medium Legitimate administrator working with shadow copies, access for backup purposes
Rule Details: Suspicious Desktopimgdownldr Command
Detects a suspicious Microsoft desktopimgdownldr execution with parameters used to download
files from the Internet.
Rule ID
process_creation_commandline_177
Query
{'selection1': {'CommandLine|contains': ' /lockscreenurl:'}, 'selection1_filter': {'C
ommandLine|contains': ['.jpg', '.jpeg', '.png']}, 'selection_reg': {'CommandLine|cont
ains|all': ['reg delete', '\\PersonalizationCSP']}, 'condition': '( selection1 and no
t selection1_filter ) or selection_reg'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bb58aa4a-b80b-415a-a2c0-2f65a4c81009

Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1105 
References
https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/ 
https://twitter.com/SBousseaden/status/1278977301745741825 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2020/07/03 high False positives depend on scripts and administrative tools used in the monitored
environment
Rule Details: Rundll32 JS RunHTMLApplication Pattern
Detects suspicious command line patterns used when rundll32 is used to run JavaScript code.
Rule ID
process_creation_commandline_178
Query
{'selection1': {'CommandLine|contains|all': ['rundll32', 'javascript', '..\\..\\mshtm
l,RunHTMLApplication']}, 'selection2': {'CommandLine|contains': ';document.write();Ge
tObject("script'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9f06447a-a33a-4cbe-a94f-a3f43184a7a3
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References

http://hyp3rlinx.altervista.org/advisories/MICROSOFT_WINDOWS_DEFENDER_DETE
CTION_BYPASS.txt 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/01/14 high Unlikely
Rule Details: ADCSPwn Hack Tool
Detects command line parameters used by ADCSPwn, a tool to escalate privileges in an active
directory network by coercing authenticate from machine accounts and relaying to the certificate
service.
Rule ID
process_creation_commandline_179
Query
{'selection': {'CommandLine|contains|all': [' --adcs ', ' --
port ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cd8c163e-a19b-402e-bdd5-419ff5859f12
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1557.001 
References
https://github.com/bats3c/ADCSPwn 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/31 high Unlikely
Rule Details: Potential PowerShell Execution Policy Tampering - ProcCreation
Detects changes to the PowerShell execution policy registry key in order to bypass signing
requirements for script execution from the CommandLine.
Rule ID
process_creation_commandline_180
Query
{'selection_path': {'CommandLine|contains': ['\\ShellIds\\Microsoft.PowerShell\\Execu
tionPolicy', '\\Policies\\Microsoft\\Windows\\PowerShell\\ExecutionPolicy']}, 'select
ion_values': {'CommandLine|contains': ['Bypass', 'RemoteSigned', 'Unrestricted']}, 'c
ondition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cf2e938e-9a3e-4fe8-a347-411642b28a9f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://learn.microsoft.com/de-de/powershell/module/microsoft.powershell.security/set-
executionpolicy?view=powershell-7.3 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/11 high Unknown
Rule Details: CrackMapExec PowerShell Obfuscation

The CrachMapExec pentesting framework implements a PowerShell obfuscation with some
static strings detected by this rule.
Rule ID
process_creation_commandline_181
Query
{'powershell_execution': {'CommandLine|contains': ['powershell.exe', 'pwsh.exe']}, 's
nippets': {'CommandLine|contains': ['join*split', "
( $ShellId[1]+$ShellId[13]+'x')", '( $PSHome[*]+$PSHOME[*]+', "
( $env:Public[13]+$env:Public[5]+'x')", "( $env:ComSpec[4,*,25]-Join'')", "[1,3]+'x'-
Join'')"]}, 'condition': 'powershell_execution and snippets'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6f8b3439-a203-45dc-a88b-abf57ea15ccf
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027.005 
References
https://github.com/byt3bl33d3r/CrackMapExec 
https://github.com/byt3bl33d3r/CrackMapExec/blob/0a49f75347b625e81ee6aa8c33d39
70b5515ea9e/cme/helpers/powershell.py#L242 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/22 high Unknown
Rule Details: Copy DMP Files From Share
Detects usage of the copy command to copy files with the .dmp extensions from a remote share.
Rule ID
process_creation_commandline_182

Query
{'selection': {'CommandLine|contains|all': ['.dmp', 'copy ', ' \\\\'], 'CommandLine|c
ontains': [' /c ', ' /r ', ' /k ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,044ba588-dff4-4918-9808-3f95e8160606
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://thedfirreport.com/2022/09/26/bumblebee-round-two/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/27 high Unknown
Rule Details: Deletion of Volume Shadow Copies via WMI with PowerShell
Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-WMIObject.
This technique is used by numerous ransomware families such as Sodinokibi/REvil.
Rule ID
process_creation_commandline_183
Query
{'selection_get': {'CommandLine|contains': ['Get-WmiObject', 'gwmi', 'Get-
CimInstance', 'gcim']}, 'selection_shadowcopy': {'CommandLine|contains': 'Win32_Shado
wcopy'}, 'selection_delete': {'CommandLine|contains': ['.Delete()', 'Remove-
WmiObject', 'rwmi', 'Remove-CimInstance', 'rcim']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,21ff4ca9-f13a-41ad-b828-0077b2af2e40
Author: Tim Rauch, Elastic (idea)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0040 , T1490 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#ato
mic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-powershell 
https://www.elastic.co/guide/en/security/current/volume-shadow-copy-deletion-via-
powershell.html 
Severity
80
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/20 high Unknown
Rule Details: ScreenConnect Remote Access
Detects ScreenConnect program starts that establish a remote access to that system (not
meeting, not remote support).
Rule ID
process_creation_commandline_184
Query
{'selection': {'CommandLine|contains|all': ['e=Access&', 'y=Guest&', '&p=', '&c=', '&
k=']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,75bfe6e6-cd8e-429e-91d3-03921e1d7962
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059.003 , TA0003 , T1133 
References
https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-
cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/02/11 high Legitimate use by administrative staff
Rule Details: Curl Start Combination
Adversaries can use curl to download payloads remotely and execute them. Curl is included by
default in Windows 10 build 17063 and later.
Rule ID
process_creation_commandline_185
Query
{'selection': {'CommandLine|contains|all': [' /c ', 'curl ', 'http', '-
o', '&']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,21dd6d38-2b18-4453-9404-a0fe4a0cc288
Author: Sreeman, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1218 , TA0011 , T1105 
References
https://medium.com/@reegun/curl-exe-is-the-new-rundll32-exe-lolbin-3f79c5f35983 
Severity
74
Suppression Logic Based On

computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/13 high Administrative scripts (installers)
Rule Details: Suspicious Usage of the Manage-bde.wsf Script
Detects usage of the manage-bde.wsf script that may indicate an attempt of proxy execution
from script.
Rule ID
process_creation_commandline_186
Query
{'selection': {'CommandLine|contains|all': ['cscript', 'manage-
bde.wsf']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c363385c-f75d-4753-a108-c1a8e28bdbda
Author: oscd.community, Natalia Shornikova, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216 
References
https://lolbas-project.github.io/lolbas/Scripts/Manage-bde/ 
https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712 
https://twitter.com/bohops/status/980659399495741441 
https://twitter.com/JohnLaTwC/status/1223292479270600706 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1216/T1216.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 medium Unknown
Rule Details: Potential COM Objects Download Cradles Usage - Process Creation
Detects usage of COM objects that can be abused to download files in PowerShell by CLSID.
Rule ID
process_creation_commandline_187
Query
{'selection_1': {'CommandLine|contains': '[Type]::GetTypeFromCLSID('}, 'selection_2':
{'CommandLine|contains': ['0002DF01-0000-0000-C000-000000000046', 'F6D90F16-9C73-
11D3-B32E-00C04F990BB4', 'F5078F35-C551-11D3-89B9-0000F81FE221', '88d96a0a-f192-11d4-
a65f-0040963251e5', 'AFBA6B42-5692-48EA-8141-DC517DCF0EF1', 'AFB40FFD-B609-40A3-9828-
F88BBE11E4E3', '88d96a0b-f192-11d4-a65f-0040963251e5', '2087c2f4-2cef-4953-a8ab-
66779b670495', '000209FF-0000-0000-C000-000000000046', '00024500-0000-0000-C000-
000000000046']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,02b64f1b-3f33-4e67-aede-ef3b0a5a8fcf
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://learn.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?view=net-
7.0 
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=57 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/25 medium Legitimate use of the library

Rule Details: Base64 MZ Header In CommandLine
Detects encoded base64 MZ header in the commandline.
Rule ID
process_creation_commandline_188
Query
{'selection': {'CommandLine|contains': ['TVqQAAMAAAAEAAAA', 'TVpQAAIAAAAEAA8A', 'TVqA
AAEAAAAEABAA', 'TVoAAAAAAAAAAAAA', 'TVpTAQEAAAAEAAAA']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,22e58743-4ac8-4a9f-bf19-00a0428d8c5f
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/07/12 high Unlikely
Rule Details: Capture a Network Trace with netsh.exe
Detects capture a network trace via netsh.exe trace functionality.
Rule ID
process_creation_commandline_189
Query
{'selection': {'CommandLine|contains|all': ['netsh', 'trace', 'start']}, 'condition':
'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d3c3861d-c504-4c77-ba55-224ba82d0118
Author: Kutepov Anton, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1040 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2019/10/24 medium Legitimate administrator or user uses netsh.exe trace functionality for legitimate
reason
Rule Details: Baby Shark Activity
Detects activity that could be related to Baby Shark malware.
Rule ID
process_creation_commandline_190
Query
{'selection': {'CommandLine|contains': ['reg query "HKEY_CURRENT_USER\\Software\\Micr
osoft\\Terminal Server Client\\Default"', 'powershell.exe mshta.exe http', 'cmd.exe /
c taskkill /im cmd.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,2b30fa36-3a18-402f-a22d-bf4ce2189f35
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures

TA0002 , T1059 , TA0005 , T1218.005 , TA0007 , T1012 
References
https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-
security-think-tanks/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/02/24 high Unknown
Rule Details: Suspicious Ping/Del Command Combination
Detects a method often used by ransomware. Which combines the "ping" to wait a couple of
seconds and then "del" to delete the file in question. Its used to hide the file responsible for the
initial infection for example.
Rule ID
process_creation_commandline_191
Query
{'selection_count': {'CommandLine|contains': [' -
n ', ' /n ']}, 'selection_nul': {'CommandLine|contains': 'Nul'}, 'selection_del_param
': {'CommandLine|contains': [' /f ', ' -f ', ' /q ', ' -
q ']}, 'selection_all': {'CommandLine|contains|all': ['ping', 'del ']}, 'condition':
'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,54786ddc-5b8a-11ed-9b6a-0242ac120002
Author: Ilya Krestinichev
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1070.004 
References
https://blog.sygnia.co/kaseya-ransomware-supply-chain-attack 

https://media.kasperskycontenthub.com/wp-
content/uploads/sites/43/2022/06/23093553/Common-TTPs-of-the-modern-
ransomware_low-res.pdf 
https://www.acronis.com/en-us/blog/posts/lockbit-ransomware/ 
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/blackbyte-
exbyte-ransomware 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/03 high False positive could occur in admin scripts that execute inline
Rule Details: Change Default File Association
When a file is opened, the default program used to open the file (also called the file association
or handler) is checked. File association selections are stored in the Windows Registry and can
be edited by users, administrators, or programs that have Registry access or by administrators
using the built-in assoc utility. Applications can modify the file association for a given file
extension to call an arbitrary program when a file with the given extension is opened.
Rule ID
process_creation_commandline_192
Query
{'selection': {'CommandLine|contains|all': ['cmd', 'assoc'], 'CommandLine|contains':
[' /c ', ' /k ', ' /r ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3d3aa6cd-6272-44d6-8afc-7e88dfef7061
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0003 , T1546.001 
References

https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.001/T1546.001
.md 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/21 low Admin activity
Rule Details: PowerShell Web Download and Execution
Detects suspicious ways to download files or content and execute them using PowerShell
Invoke-Expression.
Rule ID
process_creation_commandline_193
Query
{'selection_download': {'CommandLine|contains': ['.DownloadString(', '.DownloadFile('
, 'Invoke-
WebRequest ', 'iwr ']}, 'selection_iex': {'CommandLine|contains': ['IEX(', 'IEX (', '
I`EX', 'IE`X', 'I`E`X', '| IEX', '|IEX ', 'Invoke-
Expression', ';iex $']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,85b0b087-eddf-4a2b-b033-d771fa2b9775
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 
References
https://github.com/VirtualAlllocEx/Payload-Download-
Cradles/blob/88e8eca34464a547c90d9140d70e9866dcbc6a12/Download-
Cradles.cmd 
Severity

74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/03/24 high Scripts or tools that download files and execute them
Rule Details: Empire PowerShell Launch Parameters
Detects suspicious powershell command line parameters used in Empire.
Rule ID
process_creation_commandline_194
Query
{'selection': {'CommandLine|contains': [' -NoP -sta -NonI -W Hidden -Enc ', ' -noP -
sta -w 1 -enc ', ' -NoP -NonI -W Hidden -enc ', ' -noP -sta -w 1 -enc', ' -
enc SQB', ' -nop -exec bypass -EncodedCommand ']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,79f4ede3-402e-41c8-bc3e-ebbf5f162581
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
https://github.com/EmpireProject/Empire/blob/c2ba61ca8d2031dad0cfc1d5770ba723e8
b710db/lib/common/helpers.py#L165 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13
055/lib/modules/powershell/persistence/powerbreach/deaduser.py#L191 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13
055/lib/modules/powershell/persistence/powerbreach/resolver.py#L178 
https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13
055/data/module_source/privesc/Invoke-EventVwrBypass.ps1#L64 
Severity
74

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/04/20 high Other tools that incidentally use the same command line parameters
Rule Details: Invoke-Obfuscation STDIN+ Launcher
Detects Obfuscated use of stdin to execute PowerShell.
Rule ID
process_creation_commandline_195
Query
{'selection_main': {'CommandLine|contains|all': ['cmd', 'powershell'], 'CommandLine|c
ontains': ['/c', '/r']}, 'selection_other': [{'CommandLine|contains': 'noexit'}, {'Co
mmandLine|contains|all': ['input', '$']}], 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6c96fc76-0eb1-11eb-adc1-0242ac120002
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/15 high Unknown
Rule Details: Conti NTDS Exfiltration Command

Detects a command used by conti to exfiltrate NTDS.
Rule ID
process_creation_commandline_196
Query
{'selection': {'CommandLine|contains|all': ['7za.exe', '\\C$\\temp\\log.zip']}, 'cond
ition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa92fd02-09f2-48b0-8a93-864813fb8f41
Author: Max Altgelt (Nextron Systems), Tobias Michalski (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560 
References
https://twitter.com/vxunderground/status/1423336151860002816?s=20 
https://www.virustotal.com/gui/file/03e9b8c2e86d6db450e5eceec057d7e369ee2389b9d
aecaf06331a95410aa5f8/detection 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/09 high Unknown
Rule Details: Covenant Launcher Indicators
Detects suspicious command lines used in Covenant luanchers.
Rule ID
process_creation_commandline_198
Query
{'selection': {'CommandLine|contains|all': ['-Sta', '-Nop', '-
Window', 'Hidden'], 'CommandLine|contains': ['-Command', '-

EncodedCommand']}, 'selection2': {'CommandLine|contains': ['sv o (New-
Object IO.MemorySteam);sv d ', 'mshta file.hta', 'GruntHTTP', '-
EncodedCommand cwB2ACAAbwAgA']}, 'condition': 'selection or selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c260b6db-48ba-4b4a-a76f-2f67644e99d2
Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1564.003 
References
https://posts.specterops.io/covenant-v0-5-eee0507b85ba 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/06/04 high N/A
Rule Details: UNC2452 PowerShell Pattern
Detects a specific PowerShell command line pattern used by the UNC2452 actors as mentioned
in Microsoft and Symantec reports.
Rule ID
process_creation_commandline_199
Query
{'selection1': {'CommandLine|contains|all': ['Invoke-WMIMethod win32_process -
name create -
argumentlist', 'rundll32 c:\\windows']}, 'selection2': {'CommandLine|contains|all': [
'wmic /node:', 'process call create "rundll32 c:\\windows']}, 'condition': '1 of sele
ction*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,b7155193-8a81-4d8f-805d-88de864ca50c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , T1047 
References
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-
raindrop-malware 
https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-
compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-
defender-helps-protect/ 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1047/T1047.md#ato
mic-test-7---create-a-process-using-wmi-query-and-an-encoded-command 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/01/20 critical Unlikely
Rule Details: Launch-VsDevShell.PS1 Proxy Execution
Detects the use of the 'Launch-VsDevShell.ps1' Microsoft signed script to execute commands.
Rule ID
process_creation_commandline_200
Query
{'selection_script': {'CommandLine|contains': 'Launch-
VsDevShell.ps1'}, 'selection_flags': {'CommandLine|contains': ['VsWherePath ', 'VsIns
tallationPath ']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,45d3a03d-f441-458c-8883-df101a3bb146
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1216.001 
References
https://twitter.com/nas_bench/status/1535981653239255040 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/19 medium Legitimate usage of the script by a developer
Rule Details: Detect Virtualbox Driver Installation OR Starting Of VMs
Adversaries can carry out malicious operations using a virtual instance to avoid detection. This
rule is built to detect the registration of the Virtualbox driver or start of a Virtualbox VM.
Rule ID
process_creation_commandline_201
Query
{'selection_1': {'CommandLine|contains': ['VBoxRT.dll,RTR3Init', 'VBoxC.dll', 'VBoxDr
v.sys']}, 'selection_2': {'CommandLine|contains': ['startvm', 'controlvm']}, 'conditi
on': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bab049ca-7471-4828-9024-38279a4c04da
Author: Janantha Marasinghe
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0005 , T1564.006 
References

https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-
machine-to-dodge-security/ 
https://threatpost.com/maze-ransomware-ragnar-locker-virtual-machine/159350/ 
Severity
24
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2020/09/26 low This may have false positives on hosts where Virtualbox is legitimately being used
for operations
al
Rule Details: Suspicious RDP Redirect Using TSCON
Detects a suspicious RDP session redirect using tscon.exe.
Rule ID
process_creation_commandline_202
Query
{'selection': {'CommandLine|contains': ' /dest:rdp-tcp:'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0008 , T1563.002 , T1021.001 
References
http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html 
https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-
sessions-transparently-to-move-through-an-da2a1e73a5f6 
Severity
74
Suppression Logic Based On

computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/17 high Unknown
Rule Details: Rar Usage with Password and Compression Level
Detects the use of rar.exe, on the command line, to create an archive with password protection
or with a specific compression level. This is pretty indicative of malicious actions.
Rule ID
process_creation_commandline_203
Query
{'selection_password': {'CommandLine|contains': ' -
hp'}, 'selection_other': {'CommandLine|contains': [' -
m', ' a ']}, 'condition': 'selection_password and selection_other'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,faa48cae-6b25-4f00-a094-08947fef582f
Author: @ROxPinTeddy
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References
https://labs.sentinelone.com/the-anatomy-of-an-apt-attack-and-cobaltstrike-beacons-
encoded-configuration/ 
https://ss64.com/bash/rar.html 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001
.md 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/12 high Legitimate use of Winrar command line version
Other command line tools, that use these flags
Rule Details: Invoke-Obfuscation VAR+ Launcher
Detects Obfuscated use of Environment Variables to execute PowerShell.
Rule ID
process_creation_commandline_204
Query
{'selection': {'CommandLine|contains|all': ['cmd', '"set', '-
f'], 'CommandLine|contains': ['/c', '/r']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,27aec9c9-dbb0-4939-8422-1742242471d0
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/15 high Unknown
Rule Details: Suspicious SYSVOL Domain Group Policy Access
Detects Access to Domain Group Policies stored in SYSVOL.
Rule ID
process_creation_commandline_205

Query
{'selection': {'CommandLine|contains|all': ['\\SYSVOL\\', '\\policies\\']}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,05f3c945-dcc8-4393-9f3d-af65077a8f86
Author: Markus Neis, Jonhnathan Ribeiro, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0006 , T1552.006 
References
https://adsecurity.org/?p=2288 
https://www.hybrid-
analysis.com/sample/f2943f5e45befa52fb12748ca7171d30096e1d4fc3c365561497c61
8341299d5?environmentId=100 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/04/09 medium Administrative activity
Rule Details: AnyDesk Piped Password Via CLI
Detects piping the password to an anydesk instance via CMD and the '--set-password' flag.
Rule ID
process_creation_commandline_206
Query
{'selection': {'CommandLine|contains|all': ['/c ', 'echo ', '.exe --set-
password']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
SigmaHQ,b1377339-fda6-477a-b455-ac0923f9ec2c
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0011 , T1219 
References
https://redcanary.com/blog/misbehaving-rats/ 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2022/09/28 medium Legitimate piping of the password to anydesk
al Some FP could occure with similar tools that uses the same command line '--set-
password'
Rule Details: Suspicious PowerShell Mailbox Export to Share
Detects usage of the powerShell New-MailboxExportRequest Cmdlet to exports a mailbox to a
remote or local share, as used in ProxyShell exploitations.
Rule ID
process_creation_commandline_207
Query
{'selection': {'CommandLine|contains|all': ['New-MailboxExportRequest', ' -
Mailbox ', ' -FilePath \\\\']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,889719ef-dd62-43df-86c3-768fb08dc7c0
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 

References
https://youtu.be/5mqid-7zp8k?t=2481 
https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-
1.html 
https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-
49743a4ea9a1 
https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/ 
Severity
95
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/07 critical Unknown
Rule Details: Compress Data and Lock With Password for Exfiltration With WINZIP
An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party
utilities.
Rule ID
process_creation_commandline_208
Query
{'selection_winzip': {'CommandLine|contains': ['winzip.exe', 'winzip64.exe']}, 'selec
tion_password': {'CommandLine|contains': '-
s"'}, 'selection_other': {'CommandLine|contains': [' -min ', ' -
a ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e2e80da2-8c66-4e00-ae3c-2eebd29f6b6d
Author: frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0009 , T1560.001 
References

https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001
.md 
Severity
49
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/07/27 medium Unknown
Rule Details: Network Reconnaissance Activity
Detects a set of suspicious network related commands often used in recon stages.
Rule ID
process_creation_commandline_209
Query
{'selection_nslookup': {'CommandLine|contains|all': ['nslookup', '_ldap._tcp.dc._msdc
s.']}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,e6313acd-208c-44fc-a0ff-db85d572e90e
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059.003 , TA0007 , T1087 , T1082 
References
https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/ 
Severity
74
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2022/02/07 high False positives depend on scripts and administrative tools used in the monitored
environment
Rule Details: File overwritten by cipher tool
The Windows tool cipher can be used to remove data from available unused disk space on the
entire volume. Ransomware could use this technique to prevent the victim from using file
recovery tools to recover their files.
Rule ID
process_creation_commandline_301
Query
{'selection3': {'Image|contains': '\\cipher.exe'}, 'selection5': {'CommandLine|re': '
\\/w\\:[A-Z]{1}'}, 'condition': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: PowerShell reverse shell one-liner
A PowerShell process with arguments that may indicate a reverse shell execution has been
detected.
Rule ID

process_creation_commandline_302
Query
{'selection3': {'Image|contains': 'powershell.exe'}, 'selection5': {'CommandLine|cont
ains': 'Sockets.TCPClient'}, 'selection6': {'CommandLine|contains': 'GetStream()'}, '
selection7': {'CommandLine|contains': 'IEX'}, 'selection8': {'CommandLine|contains':
'DownloadString'}, 'selection9': {'CommandLine|contains': 'mini-
reverse.ps1'}, 'condition': 'selection3 and ((selection5 and selection6) or (selectio
n7 and selection8 and selection9))'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Shellcode execution via InstallUtil.exe
Suspicious file/code has been executed via InstallUtil.exe. This is a common technique used by
malware to install additional malicious components and/or execute Shellcode.
Rule ID
process_creation_commandline_303
Query
{'selection3': {'Image|contains': 'InstallUtil.exe'}, 'selection4': {'CommandLine|con
tains': '/LogToConsole=false'}, 'selection5': {'CommandLine|contains': '/logfile= '},
'condition': 'selection3 and selection4 and selection5'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: ALPC Task Scheduler Exploit LPE
Microsoft Windows task scheduler contains a local privilege escalation vulnerability in the
Advanced Local Procedure Call (ALPC) interface, which can allow an attacker to perform a local
privilege escalation.
Rule ID
process_creation_commandline_304
Query
{'selection3': {'Image|contains': '\\schtasks.exe'}, 'selection5': {'CommandLine|cont
ains': '/change /TN'}, 'selection6': {'CommandLine|contains': '/RU'}, 'selection7': {
'CommandLine|contains': '/RP'}, 'condition': 'selection3 and selection5 and selection
6 and selection7'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1053.005 

References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Behavior DNS cache cleared
The DNS cache has been cleared in the system.
Rule ID
process_creation_commandline_305
Query
{'selection': {'Image|endswith': '\\ipconfig.exe', 'CommandLine|contains': '/flushdns
', 'ParentImage|endswith': ['\\cmd.exe', '\\powershell.exe', '\\pwsh.exe', '\\wscript
.exe', '\\cscript.exe', '\\mshta.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: WMIC sending output to clipboard
WMIC command is using /output:clipboard as a way to hide the normal output of process
creation that is printed when creating a process with WMIC.
Rule ID
process_creation_commandline_307
Query
{'selection3': {'Image|contains': '\\wmic.exe'}, 'selection5': {'CommandLine|contains
': '/output:clipboard'}, 'selection6': {'CommandLine|contains': 'process call create'
}, 'condition': 'selection3 and selection5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1036 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: CnC Channel through Nslookup
A Windows process was detected using Nslookup with abnormal flag(s) usually used by malware
to communicate with the Command and Control.
Rule ID
process_creation_commandline_308
Query

{'selection3': {'Image|contains': '\\slookup.exe'}, 'selection4': {'CommandLine|conta
ins': ' aaaa'}, 'selection5': {'CommandLine|contains': '=aaaa'}, 'selection6': {'Comm
andLine|re': '[a-z0-9]{15,45}\\. [a-z0-9]{1,15}\\.[a-z0-9]
{1,4}'}, 'condition': 'selection3 and (selection4 or selection5) and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: WMIC Retrieving Security Configuration
The wmic.exe command was executed to get information from the security configurations. This
could be an indication of malicious activity.
Rule ID
process_creation_commandline_309
Query
{'selection3': {'Image|contains': '\\wmic.exe'}, 'selection4': {'CommandLine|contains
': 'SecurityCenter2'}, 'selection5': {'CommandLine|contains': ['AntiVirusProduct', 'F
irewallProduct']}, 'condition': 'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1005 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Taskkill killing Antivirus process
An attempt to kill an Antivirus process has been detected. This can be the result of a manual
command used by an attacker or an automated process as part of malware being deployed in
the system.
Rule ID
process_creation_commandline_310
Query
{'selection3': {'Image|contains': 'Taskkill'}, 'selection4': {'CommandLine|re': '(?:f
sav32|MsMpEng|FPAVServer|TMBMSRV|Mcshield|avgnsx|AvastSvc|dwengine|secenter|avguard|c
cSvcHst|avp|360sd|360tray|AvastUi)\\.exe'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: WSH Injection via PubPrn
An attempt to inject malicious code into a Microsoft signed WSH script has been detected. This
can be an attempt to bypass whitelisting restrictions.
Rule ID
process_creation_commandline_312
Query
{'selection3': {'Image|contains': 'wscript.exe'}, 'selection4': {'CommandLine|contain
s': 'pubprn.vbs'}, 'selection5': {'CommandLine|contains': 'script:'}, 'condition': 's
election3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1055 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: AppLocker Bypass

A successful attempt to bypass AppLocker has been detected. This can indicate an attacker is
trying to bypass whitelisting technologhies and escalate privileges or/and move laterally in your
network.
Rule ID
process_creation_commandline_314
Query
{'selection3': {'Image|contains': '\\regsvr32.exe'}, 'selection4': {'CommandLine|cont
ains': '/s'}, 'selection5': {'CommandLine|contains': '/i:http'}, 'selection6': {'Comm
andLine|contains': 'scrobj.dll'}, 'condition': 'selection3 and selection4 and selecti
on5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.010 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: File Deletion Backup files deleted recursively
An attempt to delete files and folders that migth contain backup data has been detected. This
could be an indication of a ransomware infection or an attacker trying to cause damage.
Rule ID
process_creation_commandline_315
Query
{'selection3': {'Image|contains': '\\cmd.exe'}, 'selection4': {'CommandLine|contains'
: ' del '}, 'selection5': {'CommandLine|re': '(?:backup|bkup|\\.bak|\\.bac|\\.dsk|\\.

win|\\.bkf|\\.wbcat)'}, 'condition': 'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Attempt to stop or delete Windows Defender service
Windows Defender Real-time Protection scanning for malware and other potentially unwanted
software has been stopped.
Rule ID
process_creation_commandline_316
Query
{'selection3': {'Image|contains': '\\et.exe'}, 'selection5': {'Image|contains': '\\sc
.exe'}, 'selection7': {'CommandLine|contains': 'stop'}, 'selection8': {'CommandLine|c
ontains': 'delete'}, 'selection9': {'CommandLine|contains': 'WinDefend'}, 'condition'
: '(selection3 or selection5) and (selection7 or selection8) and selection9'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0005 , T1562.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows Process Argument contains Base64 Encoded PE Header
A process has been launched with a Base64 encoded argument. Once decoded, the argument
corresponds to the PE Header. This can indicate an attacker is trying to bypass any present
execution policy.
Rule ID
process_creation_commandline_317
Query
{'selection3': {'CommandLine|contains': 'TVqQAAMAAAAEAAA'}, 'condition': 'selection3'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1140 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Cobalt Gang Windows script execution
A known Cobalt Gang script has been executed in the system. This could mean that your
computer has been compromised and malicious code is running in your endpoint.
Rule ID
process_creation_commandline_319
Query
{'selection3': {'Image|contains': '\\wscript.exe'}, 'selection5': {'CommandLine|conta
ins': 'error_log.vbe'}, 'condition': '(selection3) and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows execution using odbcconf tool
The odbcconf tool allows users to configure Open Database Connectivity (ODBC) drivers. The
utility can be misused to execute malicious code and evade detection techniques.
Rule ID
process_creation_commandline_320
Query

{'selection3': {'Image|contains': '\\odbcconf.exe'}, 'selection5': {'CommandLine|cont
ains': 'REGSVR'}, 'condition': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows INF file launch
The Advanced INF Package Installer (advpack.dll) can use the LaunchINFSection function to
invoke a section from .inf files. This could be used by attackers to remotely launch staged SCT
files with malicious code.
Rule ID
process_creation_commandline_321
Query
{'selection3': {'Image|contains': '\\rundll32.exe'}, 'selection5': {'CommandLine|re':
'advpack\\.dll, (?:LaunchINFSection|#46)\\s+'}, 'condition': 'selection3 and selecti
on5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows MavInject DLL Injection
MavInject is a Windows utility that can be used to execute code. Mavinject can be used to inject
a DLL into a running process.
Rule ID
process_creation_commandline_322
Query
{'selection3': {'Image|re': '\\\\Mavinject(?:32|64)?.exe'}, 'selection5': {'CommandLi
ne|contains': '/INJECTRUNNING'}, 'condition': 'selection3 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious ACL Change
A suspicious change was detected to an access control list (ACL). In this case, 'Full Access' was
granted to 'Everyone' on a file or folder.
Rule ID
process_creation_commandline_324
Query
{'selection3': {'Image|contains': '\\icacls.exe'}, 'selection4': {'CommandLine|re': '
\\/grant(?::r)?\\s+Everyone:F'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Credential Access Tool Detected - LaZagne
LaZagne is a multiplatform tool capable to retrieve user credentials from several system services
and applications, such as web browsers.
Rule ID
process_creation_commandline_325

Query
{'selection3': {'Image|contains': '\\lazagne'}, 'selection4': {'CommandLine|contains'
: '-quiet'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Indirect command execution using pcalua.exe
An user tried to use a Windows pcalua.exe utility to execute commands in an alternative way
(without using cmd.exe or powershell.exe). Attackers may use this technique to avoid invoking
the cmd but still execute commands.
Rule ID
process_creation_commandline_327
Query
{'selection3': {'Image|contains': '\\pcalua.exe'}, 'selection5': {'CommandLine|contai
ns': ' - a '}, 'selection6': {'CommandLine|re': '\\.
(?:hta|vbs|vbe|js|jse|wsf|wsh)'}, 'condition': 'selection3 and selection5 and selecti
on6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1202 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows UAC Bypass
A User Account Control Bypass activity was detected. This can be due to either regular operation
or because an attacker is trying to escalate privileges.
Rule ID
process_creation_commandline_328
Query
{'selection3': {'CommandLine|contains': 'TpmInitUACBypass.exe'}, 'condition': 'select
ion3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: SAM, SECURITY or SYSTEM Registry Hive Export
These hives can be used with a password cracker or creddump to dump the LANMAN/NTLM
hashes, view cached credentials, and decrypt LSA secrets. This could be an indication of a
ransomware infection or an attacker trying to cause damage.
Rule ID
process_creation_commandline_329
Query
{'selection3': {'Image|contains': '\\reg.exe'}, 'selection4': {'CommandLine|re': 'sav
e.+ (?:hklm|hkey_local_machine)\\\\
(?:system|security|sam)'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious PowerShell Argument

PowerShell was executed with suspicious command line argument. The script is likely attempting
to download files from a remote server. This could be an indication of malicious activity.
Rule ID
process_creation_commandline_330
Query
{'selection3': {'Image|contains': '\\powershell.exe'}, 'selection4': {'CommandLine|co
ntains': 'Net.WebClient'}, 'selection5': {'CommandLine|contains': 'Download'}, 'condi
tion': 'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows UAC bypass - UACME tool
User Account Control Bypass activity was detected. This can be due to either a regular operation
or because an attacker is trying to escalate privileges.
Rule ID
process_creation_commandline_331
Query
{'selection9': {'CommandLine|re': '\\.exe\\".*cleanmgr\\.exe \\/autoclean'}, 'conditi
on': 'selection9'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Ransomware Decryption Instructions File Detected
After a ransomware malware infects a host machine, a file with instructions to recover the
encrypted files is created. A file with these characteristics was opened in the system, what is an
indicator of ransomware infection.
Rule ID
process_creation_commandline_332
Query
{'selection3': {'CommandLine|re': '_Locky_recover_instructions.txt|Coin.Locker.txt DE
CRYPT_ReadMe.TXT|Contact_Here_To_Recover_Your_Files.txt|DECRYPT_INSTRUCTION.TXT|DECRY
PT_INSTRUCTIONS.TXT|DecryptAllFiles.txt|encryptor_raas_readme_liesmich.txt|FILESAREGO
NE.TXT|help_decrypt_your_files.html|HELP_RECOVER_FILES.txt|HELP_TO_DECRYPT_YOUR_FILES
.txt|HELPDECRYPT.TXT|HELPDECYPRT_YOUR_FILES.HTML|How_To_Recover_Files.txt|Howto_Resto
re_FILES.TXT|HOW TO DECRYPT YOUR DATA.txt|IHAVEYOURSECRET.KEY|INSTRUCCIONES_DESCIFRAD
O.TXT|ReadDecryptFilesHere.txt|Readme to restore your files.txt|!SBLOCK_INFO!.rtf|
КАК ВОССТАНОВИТЬ ЗАШИФРОВАННЫЕ ФАЙЛЫ.TXT|README_LOCKED.txt'}, 'condition': 'selection
3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0040 , T1486 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows Autorun Registry Entry Added via reg.exe
An executable was added to the Windows Autorun registry. While this may have occurred due to
normal software installation, this is a common technique used by malware to ensure it is started
after reboots.
Rule ID
process_creation_commandline_333
Query
{'selection3': {'Image|contains': 'reg.exe'}, 'selection4': {'CommandLine|contains':
'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'}, 'selection5': {'CommandLine|con
tains': ' add '}, 'condition': 'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1547.001 
References
N/A
Severity
50

Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: File Deletion Backup Catalog Deletion
If the backup catalog is deleted for a computer, you will not be able to access the backups
created of that computer using the Windows Server Backup snap-in. This could be an indication
of a ransomware infection or an attacker trying to cause damage.
Rule ID
process_creation_commandline_334
Query
{'selection3': {'Image|contains': '\\wbadmin.exe'}, 'selection4': {'CommandLine|conta
ins': 'delete catalog'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Wireless Network Password Retrieval

The password of a wireless network was accessed. This could be an indication of malicious
activity.
Rule ID
process_creation_commandline_335
Query
{'selection3': {'ParentImage|contains': '\\etsh.exe'}, 'selection5': {'CommandLine|co
ntains': 'wlan'}, 'selection6': {'CommandLine|contains': 'key=clear'}, 'condition': '
selection3 and selection5 and selection6'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1555 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Metasploit MSSQL Command Execution
An attacked gained access to the MSSQL Server database and is executing the Metasploit
module mssql_exec.
Rule ID
process_creation_commandline_337
Query
{'selection3': {'ParentImage|contains': 'sqlservr.exe'}, 'selection4': {'CommandLine|
contains': 'echo OWNED'}, 'condition': 'selection3 and selection4'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Internet Explorer executing suspicious wmic command
An attacker can execute code after a successful exploit attack. Internet Explorer is a commonly
targeted software in Exploit Kit campaigns.
Rule ID
process_creation_commandline_338
Query
{'selection3': {'ParentImage|contains': '\\iexplore.exe'}, 'selection4': {'Image|cont
ains': '\\WMIC.exe'}, 'selection6': {'CommandLine|contains': 'process call create'},
'selection7': {'CommandLine|contains': '\\Temp\\'}, 'condition': 'selection3 and (sel
ection4 and selection6 and selection7)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1203 
References

N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: File Deletion Windows Shadow Copies Deletion via Powershell
An attempt to delete all shadow copies using the Windows Volume Shadow Copy Service (VSS)
via Powershell has been detected. This could be an indication of a ransomware infection or an
attacker trying to cause damage.
Rule ID
process_creation_commandline_339
Query
{'selection7': {'Image|contains': '\\powershell.exe'}, 'selection8': {'CommandLine|co
ntains': 'RwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAFcAaQBuADMAMgBfAFMAaABhAGQAbwB3AGMAbwB
wAHkAIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0ACAAewAkAF8ALgBEAGUAbABlAHQAZQAoACkA
OwB9AA=='}, 'condition': '(selection7 and selection8)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1070.004 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: HackTool - Certipy Execution
Detects Certipy execution, a tool for Active Directory Certificate Services enumeration and abuse
based on PE metadata characteristics and common command line arguments.
Rule ID
process_creation_commandline_340
Query
{'selection_img': [{'Image|endswith': '\\Certipy.exe'}], 'selection_cli_commands': {'
CommandLine|contains': [' account ', ' auth ', ' cert ', ' find ', ' forge ', ' ptt '
, ' relay ', ' req ', ' shadow ', ' template ']}, 'selection_cli_flags': {'CommandLin
e|contains': [' -bloodhound', ' -ca-pfx ', ' -dc-ip ', ' -kirbi', ' -old-
bloodhound', ' -pfx ', ' -target', ' -template', ' -username ', ' -
vulnerable', 'auth -
pfx', 'shadow auto', 'shadow list']}, 'condition': 'selection_img or all of selection
_cli_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,6938366d-8954-4ddc-baff-c830b3ba8fcd
Author: pH-T (Nextron Systems), Sittikorn Sangrattanapitak
Tactics, Techniques, and Procedures
TA0006 , T1649 
References
https://github.com/ly4k/Certipy 
https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-
request-methods-and-more-7237d88061f7 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2023-04-17 high Unlikely
Rule Details: Findstr GPP Passwords
Look for the encrypted cpassword value within Group Policy Preference files on the Domain
Controller. This value can be decrypted with gpp-decrypt.
Rule ID
process_creation_commandline_341
Query
{'selection_img': [{'Image|endswith': ['\\find.exe', '\\findstr.exe']}], 'selection_c
li': {'CommandLine|contains|all': ['cpassword', '\\sysvol\\', '.xml']}, 'condition':
'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,91a2c315-9ee6-4052-a853-6f6a8238f90d
Author: frack113
Tactics, Techniques, and Procedures
TA0006 , T1552.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.006/T1552.006
.md#atomic-test-1---gpp-passwords-findstr 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021-12-27 high Unknown
Rule Details: Domain Trust Discovery Via Dsquery
Detects execution of "dsquery.exe" for domain trust discovery.

Rule ID
process_creation_commandline_342
Query
{'selection_img': [{'Image|endswith': '\\dsquery.exe'}], 'selection_cli': {'CommandLi
ne|contains': 'trustedDomain'}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3bad990e-4848-4a78-9530-b427d854aac0
Author: E.M. Anhaus, Tony Lambert, oscd.community, omkar72
Tactics, Techniques, and Procedures
TA0007 , T1482 
References
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1482/T1482.md 
https://posts.specterops.io/an-introduction-to-manual-active-directory-querying-with-
dsquery-and-ldapsearch-84943c13d7eb?gi=41b97a644843 
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019-10-24 medium Legitimate use of the utilities by legitimate user for legitimate reason
Rule Details: PUA - DIT Snapshot Viewer
Detects the use of Ditsnap tool, an inspection tool for Active Directory database, ntds.dit.
Rule ID
process_creation_commandline_343
Query
{'selection': [{'Image|endswith': '\\ditsnap.exe'}, {'CommandLine|contains': 'ditsnap
.exe'}], 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d3b70aad-097e-409c-9df2-450f80dc476b
Author: Furkan Caliskan (@caliskanfurkan_)
Tactics, Techniques, and Procedures
TA0006 , T1003.003 
References
https://thedfirreport.com/2020/06/21/snatch-ransomware/ 
https://web.archive.org/web/20201124182207/https://github.com/yosqueoy/ditsnap 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020-07-04 high Legitimate admin usage
Rule Details: Suspicious Process Patterns NTDS.DIT Exfil
Detects suspicious process patterns used in NTDS.DIT exfiltration.
Rule ID
process_creation_commandline_344
Query
{'selection_tool': [{'Image|endswith': ['\\NTDSDump.exe', '\\NTDSDumpEx.exe']}, {'Com
mandLine|contains|all': ['ntds.dit', 'system.hiv']}, {'CommandLine|contains': 'NTDSgr
ab.ps1'}], 'selection_oneliner_1': {'CommandLine|contains|all': ['ac i ntds', 'create
full']}, 'selection_onliner_2': {'CommandLine|contains|all': ['/c copy ', '\\windows
\\ntds\\ntds.dit']}, 'selection_onliner_3': {'CommandLine|contains|all': ['activate i
nstance ntds', 'create full']}, 'selection_powershell': {'CommandLine|contains|all':
['powershell', 'ntds.dit']}, 'set1_selection_ntds_dit': {'CommandLine|contains': 'ntd
s.dit'}, 'set1_selection_image_folder': [{'ParentImage|contains': ['\\apache', '\\tom
cat', '\\AppData\\', '\\Temp\\', '\\Public\\', '\\PerfLogs\\']}, {'Image|contains': [
'\\apache', '\\tomcat', '\\AppData\\', '\\Temp\\', '\\Public\\', '\\PerfLogs\\']}], '
condition': '1 of selection* or all of set1*'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8bc64091-6875-4881-aaf9-7bd25b5dda08
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1003.003 
References
https://www.ired.team/offensive-security/credential-access-and-credential-
dumping/ntds.dit-enumeration 
https://www.n00py.io/2022/03/manipulating-user-passwords-without-mimikatz/ 
https://pentestlab.blog/tag/ntds-dit/ 
https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee196d91ae4
47283e/Gather/Copy-VSS.ps1 
https://github.com/zcgonvh/NTDSDumpEx 
https://github.com/rapid7/metasploit-
framework/blob/d297adcebb5c1df6fe30b12ca79b161deb71571c/data/post/powershell/
NTDSgrab.ps1 
https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022-03-11 high Unknown
Rule Details: Get-ForestTrust with PowerShell
The following analytic detects the execution of the Get-ForestTrust command via PowerShell,
commonly used by adversaries to gather domain trust information. This detection leverages data
from Endpoint Detection and Response (EDR) agents, focusing on process names and
command-line executions. Identifying this activity is crucial as it indicates potential
reconnaissance efforts to map out domain trusts, which can inform further attacks. If confirmed

malicious, this activity could allow attackers to understand domain relationships, aiding in lateral
movement and privilege escalation within the network.
Rule ID
process_creation_commandline_345
Query
{'selection1': {'Image|endswith': ['powershell.exe', 'cmd.exe']}, 'selection2': {'Com
mandLine|contains': 'get-foresttrust'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1482 
References
https://powersploit.readthedocs.io/en/latest/Recon/Get-ForestTrust/ 
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
producti 2024-11-13 medium Limited false positives as this requires an active Administrator or adversary to bring in,
import, and execute.
on
Rule Details: Renamed AdFind Execution
Detects the use of a renamed Adfind.exe. AdFind continues to be seen across majority of
breaches. It is used to domain trust discovery to plan out subsequent steps in the attack chain.
Rule ID
process_creation_commandline_346
Query
{'selection_1': {'CommandLine|contains': ['domainlist', 'trustdmp', 'dcmodes', 'adinf
o', ' dclist ', 'computer_pwdnotreqd', 'objectcategory=', '-subnets -

f', 'name="Domain Admins"', '-
sc u:', 'domainncs', 'dompol', ' oudmp ', 'subnetdmp', 'gpodmp', 'fspdmp', 'users_noe
xpire', 'computers_active', 'computers_pwdnotreqd']}, 'selection_2': {'Hashes|contain
s': ['IMPHASH=BCA5675746D13A1F246E2DA3C2217492', 'IMPHASH=53E117A96057EAF19C41380D0E8
7F1C2']}, 'selection_3': {'OriginalFileName': 'AdFind.exe'}, 'filter': {'Image|endswi
th': '\\AdFind.exe'}, 'condition': '1 of selection* and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,df55196f-f105-44d3-a675-e9dfb6cc2f2b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0007 , T1018 , T1087.002 , T1482 , T1069.002 
References
https://www.joeware.net/freetools/tools/adfind/ 
https://thedfirreport.com/2020/05/08/adfind-recon/ 
https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/ 
https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-
second-stage-activation-from-sunburst-to-teardrop-and-raindrop/ 
https://social.technet.microsoft.com/wiki/contents/articles/7535.adfind-command-
examples.aspx 
https://github.com/center-for-threat-informed-
defense/adversary_emulation_library/blob/bf62ece1c679b07b5fb49c4bae947fe24c8181
1f/fin6/Emulation_Plan/Phase1.md 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022-08-21 high Unknown
Rule Details: Enumerating Domain Trusts via NLTEST.EXE

Identifies the use of nltest.exe for domain trust discovery purposes. Adversaries may use this
command-line utility to enumerate domain trusts and gain insight into trust relationships, as well
as the state of Domain Controller (DC) replication in a Microsoft Windows NT Domain.
Rule ID
process_creation_commandline_347
Query
{'selection1': {'Image|endswith': '\\nltest.exe'}, 'selection2': {'CommandLine|contai
ns': ['/dclist:', '/dcname:', '/parentdomain', '/domain_trusts', '/bdc_query:']}, 'fi
lter_parent': {'ParentImage|endswith': 'PDQInventoryScanner.exe'}, 'filter_system_use
rs': {'UserId': ['S-1-5-18', 'S-1-5-19', 'S-1-5-
20']}, 'condition': 'selection1 and selection2 and (not filter_parent) and (not filte
r_system_users)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1018 , T1482 
References
N/A
Severity
25
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Matu Creation Risk False Positives
rity Date Level
test 2022/05/ low Domain administrators may use this command-line utility for legitimate information gathering
purposes, but it is not common for environments with Windows Server 2012 and newer.
31
Rule Details: Potential SPN Enumeration Via Setspn.EXE
Detects service principal name (SPN) enumeration used for Kerberoasting.
Rule ID
process_creation_commandline_348
Query

{'selection_pe': [{'Image|endswith': '\\setspn.exe'}], 'selection_cli': {'CommandLine
|contains': [' -q ', ' /q ']}, 'selection_cli2': {'CommandLine|contains|all': [' -
t ', ' -f ']}, 'condition': 'selection_pe and (selection_cli or selection_cli2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1558.003 
References
https://web.archive.org/web/20200329173843/https://p16.praetorian.com/blog/how-to-
use-kerberoasting-t1208-for-privilege-escalation 
https://www.praetorian.com/blog/how-to-use-kerberoasting-t1208-for-privilege-
escalation/?edition=2019 
Severity
50
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018-11-14 medium Administration activity
Rule Details: HackTool - Mimikatz Execution
Detects well-known mimikatz command line arguments.
Rule ID
process_creation_commandline_349
Query
{'selection_tools_name': {'CommandLine|contains': ['DumpCreds', 'mimikatz']}, 'select
ion_function_names': {'CommandLine|contains': ['::aadcookie', '::detours', '::memssp'
, '::mflt', '::ncroutemon', '::ngcsign', '::printnightmare', '::skeleton', '::preshut
down', '::mstsc', '::multirdp']}, 'selection_module_names': {'CommandLine|contains':
['rpc::', 'token::', 'crypto::', 'dpapi::', 'sekurlsa::', 'kerberos::', 'lsadump::',
'privilege::', 'process::', 'vault::']}, 'condition': '1 of selection_*'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,a642964e-bead-4bed-8910-1bb4d63e3b4d
Author: Teymur Kheirkhabarov, oscd.community, David ANDRE (additional keywords), Tim
Shelton
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-
environment 
https://tools.thehacker.recipes/mimikatz/modules 
Severity
75
Suppression Logic Based On
computer_name
event_data.CommandLine
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2025/08/13 high Unlikely
Process Creation Image Rule IDs
Rule Details: Powershell Process Created by Internet Explorer
A Powershell process has been created by Internet Explorer. This can indicate a malicious
website has successfully launched an exploit.
Rule ID
process_creation_image_1
Query
{'selection3': {'ParentImage|contains': 'iexplore.exe'}, 'selection4': {'Image|contai
ns': 'powershell.exe'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Powershell Process Created by Office PowerPoint
A Powershell process has been created by Microsoft Office PowerPoint. This can indicate a
malicious document containing a macro or an exploit has been opened by the user.
Rule ID
process_creation_image_2
Query
{'selection3': {'ParentImage|contains': 'POWERPNT.EXE'}, 'selection4': {'Image|contai
ns': 'powershell.exe'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name

process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Executable with Suspicious Extension
An executable was launched with a well-known extension preceding the executable extension.
This could be an indication that a user was tricked into executing a malicious program.
Rule ID
process_creation_image_5
Query
{'selection3': {'Image|re': '\\.(jpeg|jpg|png|gif|tiff|ico|zip|rar|pdf)\\.
(exe|msi|scr|hta|bat|hta)$'}, 'selection4': {'CurrentDirectory|re': '(?:\\\\Program F
iles(?:\\(x86\\))?|\\\\PROGRA~
(?:1|2))'}, 'condition': 'selection3 and not selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1036 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Process created by dbgsrv debugger
A known signed debugger software has been detected creating a remote process. This could be
used by an attacker trying to bypass whitelisted applications.

Rule ID
process_creation_image_6
Query
{'selection3': {'ParentImage|contains': '\\dbgsrv.exe'}, 'selection4': {'ParentComman
dLine|contains': 'clicon='}, 'selection5': {'ParentCommandLine|contains': 'port='}, '
condition': 'selection3 and selection4 and selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Powershell Process Created by Office Word
A Powershell process has been created by Microsoft Office Word. This can indicate a malicious
document containing a macro or an exploit has been opened by the user.
Rule ID
process_creation_image_8
Query
{'selection3': {'ParentImage|contains': 'WINWORD.EXE'}, 'selection4': {'Image|contain
s': 'powershell.exe'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation

Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Java Process Spawning Scripting Process
A suspicious process has been created by Java Software. This could be an indication of
malicious activity.
Rule ID
process_creation_image_10
Query
{'selection3': {'ParentImage|re': '\\\\java[w]?
\\.exe'}, 'selection4': {'Image|re': '(?:powershell|wscript|cscript|mshta)\\.exe'}, '
condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1216 
References
N/A
Severity
50

Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Powershell Process Created by webserver process
A webserver process has created a Powershell session. This could be the result of a successful
exploitation of the webserver or the installation of a webshell.
Rule ID
process_creation_image_11
Query
{'selection3': {'Image|contains': 'powershell.exe'}, 'selection4': {'ParentImage|cont
ains': 'w3wp.exe'}, 'selection5': {'ParentImage|contains': 'httpd.exe'}, 'selection6'
: {'ParentImage|contains': 'tomcat6.exe'}, 'selection7': {'ParentImage|contains': 'ng
inx.exe'}, 'selection8': {'ParentImage|contains': 'php-
cgi.exe'}, 'selection9': {'ParentImage|contains': 'tomcat.exe'}, 'condition': 'select
ion3 and (selection4 or selection5 or selection6 or selection7 or selection8 or selec
tion9)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Process Execution Using pcwutl.dll
A process has been launched using the pcwutl.dll library. This can indicate an attacker is trying to
bypass whitelisting technologies.
Rule ID
process_creation_image_12
Query
{'selection3': {'ParentImage|contains': '\\rundll32.exe'}, 'selection4': {'ParentComm
andLine|contains': 'pcwutl.dll'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.011 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows Hacking Tool Detected
A common hacking tool was detected being used on this machine. While hacking tools can be
used for System diagnostics during routine maintenance it is also a common indicator of
malware performing additional reconnaissance or privilege escalation.
Rule ID
process_creation_image_13
Query

{'selection3': {'Image|re': '\\\\(?:(?:
(?:win32dd|win64dd|wce|mailpv|rdpv|logreader|netpass|iepv|routerpass|pstpass|vncpass|
mspass)\\.exe)|WebBrowserPassView|VNCPassView|Cachedump|Fgdump|gsecdump|Lslsass|mimik
atz|pwdump|getlsasrvaddr|timestomp|BulletsPassView|WebBrowserPassView|WirelessKeyView
|Chromepass|dialupass|lookpass|Fluxay5Beta1|pstpassword|OperaPassView|routerpassview|
PasswordFox)'}, 'condition': 'selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Executable launched using Windows PresentationHost tool
Windows Presentation Foundation Host (PresentationHost.exe) enables applications to be
hosted in compatible browsers. This tool can bypass code integrity enforcement in Windows
Defender Application Control.
Rule ID
process_creation_image_14
Query
{'selection3': {'ParentImage|contains': '\\PresentationHost.exe'}, 'selection4': {'Im
age|re': '\\\\
(?:iexplore|chrome|firefox)\\.exe'}, 'condition': 'selection3 and not selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Executable Launched from System Volume Information
Running executables from the System Volume Information folder is a common technique used by
malware in order to hide itself. This could be an indication of malicious activity.
Rule ID
process_creation_image_15
Query
{'selection3': {'Image|contains': ':\\System Volume Information\\'}, 'condition': 'se
lection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1036 
References
N/A
Severity

50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Powershell Process Created by Office Excel
A Powershell process has been created by Microsoft Office Excel. This can indicate a malicious
document containing a macro or an exploit has been opened by the user.
Rule ID
process_creation_image_16
Query
{'selection3': {'ParentImage|contains': 'EXCEL.EXE'}, 'selection4': {'Image|contains'
: 'powershell.exe'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Detected scripting process spawned by WinRAR

A scripting process executed with wscript.exe, cscript.exe or mshta.exe was directly executed
from WinRAR. This behavior is commonly executed by packed malware.
Rule ID
process_creation_image_17
Query
{'selection3': {'ParentImage|contains': '\\WinRAR.exe'}, 'selection4': {'Image|re': '
\\\\(wscript|cscript|mshta)\\.exe$'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: RDP process spawning a suspicious process
An unauthenticated attacker could connect to the target system using RDP and send specially
crafted requests. This vulnerability could execute arbitrary code on the target system.
Rule ID
process_creation_image_18
Query
{'selection3': {'ParentImage|contains': '\\svchost.exe'}, 'selection4': {'ParentComma
ndLine|contains': 'svchost.exe -
k termsvcs'}, 'selection5': {'Image|contains': '\\rdpclip.exe'}, 'condition': 'select
ion3 and selection4 and not selection5'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0008 , T1210 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows UAC bypass - UACME tool
User Account Control Bypass activity was detected. This can be due to either a regular operation
or because an attacker is trying to escalate privileges.
Rule ID
process_creation_image_19
Query
{'selection3': {'ParentImage|contains': '\\dism.exe'}, 'selection4': {'ParentCommandL
ine|contains': '.xml'}, 'selection5': {'Image|re': '\\\\appdata\\\\.*\\\\dismhost\\.e
xe'}, 'selection6': {'Image|contains': '\\wusa.exe'}, 'selection7': {'CommandLine|con
tains': '/quiet'}, 'selection8': {'ParentImage|contains': '\\explorer.exe'}, 'selecti
on10': {'ParentImage|contains': 'dccw.exe'}, 'selection11': {'ParentImage|contains':
'\\slui.exe'}, 'condition': '((selection3 and selection4 and not selection5) or (sele
ction6 and selection7 and not selection8) or selection10 or selection11)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: MS Exchange transport agent backdoor
Transport agents let you install custom software on an Exchange server. This could be used by
malware to gain persistence and install backdoors.
Rule ID
process_creation_image_20
Query
{'selection3': {'ParentImage|contains': '\\EdgeTransport.exe'}, 'condition': 'selecti
on3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1129 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Executable launched using Synaptics Touchpad Enhancements tool
Synaptics Touchpad Enhancements utility allows you to run binaries in the system. This tool can
bypass code integrity enforcement in Windows Defender Application Control.
Rule ID
process_creation_image_21
Query
{'selection3': {'ParentImage|contains': '\\SynTPEnh.exe'}, 'selection4': {'ParentComm
andLine|contains': '/SHELLEXEC'}, 'selection5': {'Image|contains': '\\SynTPHelper.exe
'}, 'selection6': {'Image|contains': '\\WerFault.exe'}, 'condition': 'selection3 and
selection4 and not (selection5 or selection6)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: SharPyShell Process Execution Detected
SharPyShell is a known hacking tool that is able to deploy a shell into the ASP.NET server. This
shell can be controlled remotely from a malicious server. A process with these characteristics has
been detected, what is an indicator of compromise by SharPyShell.

Rule ID
process_creation_image_22
Query
{'selection3': {'SubjectDomainName': 'IIS APPPOOL'}, 'selection4': {'SubjectUserName'
: 'sharpy'}, 'condition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1505.003 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious Process Created by mshta.exe
A suspicious process process has been created by mshta.exe. This can indicate an attacker is
using built-in Windows functionality to perform malicious activity.
Rule ID
process_creation_image_24
Query
{'selection3': {'ParentImage|contains': '\\mshta.exe'}, 'selection4': {'Image|re': '\
\\\(?:powershell|
(?:w|c)script|cmd)\\.exe'}, 'selection5': {'CurrentDirectory|re': '(?:\\\\Program Fil
es(?:\\(x86\\))?|\\\\PROGRA~
(?:1|2))'}, 'condition': 'selection3 and selection4 and not selection5'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.005 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Java Process Spawning WMIC
The wmic.exe process was executed by Java Software. This could be an indication of malicious
activity.
Rule ID
process_creation_image_25
Query
{'selection3': {'ParentImage|re': '\\\\java[w]?
\\.exe'}, 'selection4': {'Image|contains': '\\wmic.exe'}, 'condition': 'selection3 an
d selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1047 
References
N/A

Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Process Spawning Fodhelper
A process has spawned Fodhelper.exe. There is a known UAC bypass that can be used to
escalate privileges.
Rule ID
process_creation_image_26
Query
{'selection3': {'ParentImage|re': '\\\\(?:powershell|
(?:w|c)script|cmd)\\.exe'}, 'selection4': {'Image|contains': '\\fodhelper.exe'}, 'con
dition': 'selection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1548.002 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A

Rule Details: Executable Launched from Recycle Bin
Running executables from the Recycle Bin folder is a common technique used by malware in
order to hide itself. This could be an indication of malicious activity.
Rule ID
process_creation_image_28
Query
{'selection3': {'Image|contains': ':\\$Recycle.Bin\\'}, 'selection4': {'Image|contain
s': ':\\Recycler\\'}, 'condition': '(selection3 or selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1036 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious Process Created by Notepad or Calculator
A potentially suspicious process was started by either Notepad or Calculator. This could be the
result of malicious file being opened by the user or a proof-of-concept being tested.
Rule ID
process_creation_image_31
Query
{'selection3': {'ParentImage|contains': '\\NOTEPAD.EXE'}, 'selection4': {'Image|re':
'\\\\
(?:notepad|ctfmon|Microsoft\\.Uev\\.SyncController)\\.exe'}, 'selection5': {'CommandL

ine|contains': '\\DRIVERS\\'}, 'selection6': {'ParentImage|contains': '\\CALC.EXE'},
'selection7': {'Image|contains': 'CALC.EXE'}, 'selection8': {'Image|contains': ':\\Pr
ogram Files'}, 'selection9': {'Image|contains': '":\\Windows\\splwow64.exe"'}, 'condi
tion': '((selection3 and not (selection4 or selection5)) or (selection6 and not selec
tion7)) and not (selection8 or selection9)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1203 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Suspicious Process Created by Microsoft Office Application
A potentially suspicious process was started by a Microsoft Office application. This can indicate a
malicious document containing a macro or an exploit has been opened by the user.
Rule ID
process_creation_image_32
Query
{'selection3': {'ParentImage|re': '(?:winword|excel|powerpnt|msaccess|infopath)\\.exe
'}, 'selection6': {'Image|re': '(?:cmd|svchost|wscript|notepad|rundll32|schtasks|ntvd
m|bitsadmin|msiexec|regsvr32|certutil|mshta|[A-
Z]:\\\\Users\\\\.*)\\.exe$'}, 'selection4': {'Image|contains': '\\AppData\\'}, 'selec
tion5': {'CommandLine|contains': '\\DRIVERS\\'}, 'condition': 'selection3 and selecti
on6 and not (selection4 or selection5)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1203 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Windows mofcomp with suspicious file extension
The Managed Object Format (MOF) compiler parses a file containing MOF statements and adds
the classes and class instances defined in the file to the WMI repository. Attackers could use this
tool to compile malicious WMI classes.
Rule ID
process_creation_image_33
Query
{'selection3': {'Image': '\\mofcomp.exe'}, 'selection5': {'CommandLine|re': '\\.mof'}
, 'condition': 'selection3 and not selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1047 
References
N/A
Severity

50
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Process Creation Parent Child Rule IDs
Rule Details: MSHTA Spawning Windows Shell
It is suspicious for the mshta process to launch a Windows command line executable.
Rule ID
parent_child_1
Query
{'selection': {'ParentImage|endswith': '\\mshta.exe'}, 'selection2': [{'Image|endswit
h': ['\\cmd.exe', '\\powershell.exe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '
\\bash.exe', '\\reg.exe', '\\regsvr32.exe']}, {'Image|contains': ['\\BITSADMIN']}], '
condition': 'selection and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,03cc0c25-389f-4bf8-b48d-11878079f1ca
Author: Michael Haag
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218.005 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/01/16 high Printer software / driver installations
HP software
Rule Details: New Lolbin Process by Office Applications
A Microsoft Office application that launches a new LOLBin process is very suspicious.
Rule ID
parent_child_2
Query
{'selection1': {'Image|endswith': ['\\regsvr32.exe', '\\rundll32.exe', '\\msiexec.exe
', '\\mshta.exe', '\\verclsid.exe']}, 'selection2': {'ParentImage|endswith': ['\\winw
ord.exe', '\\excel.exe', '\\powerpnt.exe']}, 'condition': 'selection1 and selection2'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,23daeb52-e6eb-493c-8607-c4f0246cb7d8
Author: Vadim Khrykov (ThreatIntel), Cyb3rEng (Rule), Michael Haag, Christopher Peacock
@securepeacock (Update), SCYTHE @scythe_io (Update)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 , T1047 , TA0005 , T1218.010 
References
https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/ 
https://github.com/vadim-hunter/Detection-Ideas-
Rules/blob/main/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi
_(aka_REvil)_Ransomware.yaml 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2021/08/23 high Unknown
Rule Details: Droppers Exploiting CVE-2017-11882
This is indicative an attempt to exploit vulnerabilities described in CVE-2017-11882, in which
exploits often start EQNEDT32.EXE and other sub-processes such as mshta.exe.
Rule ID
parent_child_3
Query
{'selection': {'ParentImage|endswith': '\\EQNEDT32.EXE'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,678eb5f4-8597-4be6-8be7-905e4234b53a
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 , T1204.002 
References
https://www.hybrid-
analysis.com/sample/2a4ae284c76f868fc51d3bb65da8caa6efacb707f265b25c30f3425
0b76b7507?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/11/23 critical unknown
Rule Details: Exploit for CVE-2017-8759
As described in CVE-2017-8759, launch of csc.exe from Winword may be an exploit attempt.
Rule ID

parent_child_4
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'Image|endswith': '\\csc.exe'
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,fdd84c68-a1f6-47c9-9477-920584f94905
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 , T1204.002 
References
https://www.hybrid-
analysis.com/sample/0b4ef455e385b750d9f90749f1467eaf00e46e8d6c2885c260e1b78
211a51684?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/09/15 critical Unknown
Rule Details: Suspicious Shells Spawn by WinRM
A WinRM host process that launches a shell is suspicious.
Rule ID
parent_child_5
Query
{'selection': {'ParentImage': '*\\wsmprovhost.exe', 'Image': ['*\\cmd.exe', '*\\sh.ex
e', '*\\bash.exe', '*\\powershell.exe', '*\\schtasks.exe', '*\\certutil.exe', '*\\who
ami.exe', '*\\bitsadmin.exe']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,5cc2cda8-f261-4d88-a2de-e9e193c86716
Author: Andreas Hunkeler (@Karneades), Markus Neis
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/05/20 high Legitimate WinRM usage
Rule Details: Suspicious Shells Spawned by Java
A Java host process that launches certain child processes, particularly a shell process, is
suspicious and may indicate exploitation such as log4j.
Rule ID
parent_child_6
Query
{'selection': {'ParentImage|endswith': '\\java.exe', 'Image|endswith': ['\\sh.exe', '
\\bash.exe', '\\powershell.exe', '\\schtasks.exe', '\\certutil.exe', '\\whoami.exe',
'\\bitsadmin.exe', '\\wscript.exe', '\\cscript.exe', '\\scrcons.exe', '\\regsvr32.exe
', '\\hh.exe', '\\wmic.exe', '\\mshta.exe', '\\rundll32.exe', '\\forfiles.exe', '\\sc
riptrunner.exe', '\\mftrace.exe', '\\AppVLP.exe', '\\curl.exe']}, 'condition': 'selec
tion'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0d34ed8b-1c12-4ff2-828c-16fc860b766d

Author: Andreas Hunkeler (@Karneades), Florian Roth
Tactics, Techniques, and Procedures
XTA0001 , XT1002 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/17 high Legitimate calls to system binaries
Company specific internal usage
Rule Details: WMI Backdoor Exchange Transport Agent
This indicates that a WMI event filter has been used to create a backdoor in an Exchange
Transport Agent.
Rule ID
parent_child_7
Query
{'selection': {'ParentImage|endswith': '\\EdgeTransport.exe'}, 'condition': 'selectio
n'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,797011dc-44f4-4e6f-9f10-a8ceefbe566b
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1546.003 
References
https://twitter.com/cglyer/status/1182389676876980224 
https://twitter.com/cglyer/status/1182391019633029120 

Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/11 critical Unknown
Rule Details: Exploit for CVE-2017-0261
Launch of FLTLDR.exe from Winword is uncommon and indicative of exploits described in CVE-
2017-0261 and CVE-2017-0262.
Rule ID
parent_child_8
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'Image|contains': '\\FLTLDR.e
xe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,864403a1-36c9-40a2-a982-4c9a45f7d833
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 , T1204.002 
References
https://www.fireeye.com/blog/threat-research/2017/05/eps-processing-zero-
days.html 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2018/02/22 medium Several false positives identified, check for suspicious file names or locations (e.g.
Temp folders)
Rule Details: Exploited CVE-2020-10189 Zoho ManageEngine
This is indicative of CVE-2020-10189 which describes exploitation of Zoho ManageEngine
Desktop Central - Java Deserialization.
Rule ID
parent_child_9
Query
{'selection': {'ParentImage|endswith': 'DesktopCentral_Server\\jre\\bin\\java.exe', '
Image|endswith': ['\\cmd.exe', '\\powershell.exe', '\\bitsadmin.exe']}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,846b866e-2a57-46ee-8e16-85fa92759be7
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0002 , T1059 
References
https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-
campaign-using-multiple-exploits.html 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/03/25 critical Unknown
Rule Details: Microsoft Office Product Spawning Windows Shell

It is suspicious for a Microsoft Office application to launch a Windows command and scripting
interpreter executable.
Rule ID
parent_child_10
Query
{'selection': {'ParentImage|endswith': ['\\WINWORD.EXE', '\\EXCEL.EXE', '\\POWERPNT.e
xe', '\\MSPUB.exe', '\\VISIO.exe', '\\MSACCESS.EXE', '\\EQNEDT32.EXE'], 'Image|endswi
th': ['\\cmd.exe', '\\powershell.exe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe',
'\\bash.exe', '\\scrcons.exe', '\\schtasks.exe', '\\regsvr32.exe', '\\hh.exe', '\\wmi
c.exe', '\\mshta.exe', '\\rundll32.exe', '\\msiexec.exe', '\\forfiles.exe', '\\script
runner.exe', '\\mftrace.exe', '\\AppVLP.exe', '\\svchost.exe', '\\msbuild.exe']}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,438025f9-5856-4663-83f7-52f878a70a50
Author: Florian Roth (Nextron Systems), Markus Neis, FPT.EagleEye Team, Vadim Khrykov,
Cyb3rEng, Michael Haag, Christopher Peacock @securepeacock, @scythe_io
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 
References
https://www.hybrid-
analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8bad54e2
95f28bbc21?environmentId=100 
https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/04/06 high unknown
Rule Details: Suspicious Parent of Csc.exe

It is considered suspicious when certain parent processes (such as wscript or mshta) have
launched cwc.exe.
Rule ID
parent_child_11
Query
{'selection': {'Image|endswith': '\\csc.exe', 'ParentImage|endswith': ['\\wscript.exe
', '\\cscript.exe', '\\mshta.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b730a276-6b63-41b8-bcf8-55930c8fc6ee
Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems), X__Junior
(Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , TA0005 , T1218.005 , T1027.004 
References
https://twitter.com/SBousseaden/status/1094924091256176641 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/02/11 high Unknown
Rule Details: MSHTA Spawned by SVCHOST
This is indicative of LethalHTA (a lateral movement technique).
Rule ID
parent_child_12
Query
{'selection': {'ParentImage|endswith': '\\svchost.exe', 'Image|endswith': '\\mshta.ex
e'}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ed5d72a6-f8f4-479d-ba79-02f6a80d7471
Author: Markus Neis
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218.005 
References
https://codewhitesec.blogspot.com/2018/07/lethalhta.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/06/07 high Unknown
Rule Details: Suspicious HWP Sub Processes
Certain sub-processes of the Hangul Word Processor (Hanword) application may indicate an
exploitation attempt.
Rule ID
parent_child_13
Query
{'selection': {'ParentImage|endswith': '\\Hwp.exe', 'Image|endswith': '\\gbb.exe'}, '
condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,023394c4-29d5-46ab-92b8-6a534c6f447b
Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures
TA0001 , T1566.001 , XTA0001 , XT1002 , TA0002 , T1203 , T1059.003 
References
https://www.securitynewspaper.com/2016/11/23/technical-teardown-exploit-malware-
hwp-files/ 
https://twitter.com/cyberwar_15/status/1187287262054076416 
https://blog.alyac.co.kr/1901 
https://en.wikipedia.org/wiki/Hangul_(word_processor) 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Unknown
Rule Details: Time Travel Debugging Utility Usage
Use of the Time Travel Debugging Utility (tttracer.exe) is suspicious since adversaries can use it
to run malicious processes and dump processes, such as lsass.exe.
Rule ID
parent_child_14
Query
{'selection': {'ParentImage|endswith': '\\tttracer.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,0b4ae027-2a2d-4b93-8c7e-962caaba5b2a
Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 , TA0006 , T1003.001 
References

https://lolbas-project.github.io/lolbas/Binaries/Tttracer/ 
https://twitter.com/mattifestation/status/1196390321783025666 
https://twitter.com/oulusoyum/status/1191329746069655553 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/06 high Legitimate usage by software developers/testers
Rule Details: CMSTP Execution Process Creation
This is an indicator of an attempt to use Microsoft Connection Manager Profile to bypass UAC.
Rule ID
parent_child_15
Query
{'selection': {'ParentImage|endswith': '\\cmstp.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7d4cdc5a-0076-40ca-aac8-f7e714570e47
Author: Nik Seetharaman
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218.003 
References
https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-
cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/ 
Severity
74
Suppression Logic Based On
computer_name

parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/07/16 high Legitimate CMSTP use (unlikely in modern enterprise environments)
Rule Details: Winnti Malware HK University Campaign
This is a characteristic of Winnti malware as reported in a Dec/Jan 2020 campaign against Hong
Kong universities.
Rule ID
parent_child_16
Query
{'selection2': {'ParentImage|startswith': 'C:\\ProgramData\\DRM', 'Image|endswith': '
\\wmplayer.exe'}, 'selection3': {'ParentImage|endswith': '\\Test.exe', 'Image|endswit
h': '\\wmplayer.exe'}, 'selection4': {'Image': 'C:\\ProgramData\\DRM\\CLR\\CLR.exe'},
'selection5': {'ParentImage|startswith': 'C:\\ProgramData\\DRM\\Windows', 'Image|end
swith': '\\SearchFilterHost.exe'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,3121461b-5aa0-4a41-b910-66d25524edbb
Author: Florian Roth (Nextron Systems), Markus Neis
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1574.002 
References
https://www.welivesecurity.com/2020/01/31/winnti-group-targeting-universities-hong-
kong/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2020/02/01 critical Unlikely
Rule Details: Shells Spawned by Web Servers
A web server process that runs a shell process indicates a possible placement of a web shell for
malicious use.
Rule ID
parent_child_17
Query
{'selection': {'ParentImage|endswith': ['\\w3wp.exe', '\\httpd.exe', '\\nginx.exe', '
\\php-
cgi.exe', '\\tomcat.exe', '\\UMWorkerProcess.exe', '\\ws_TomcatService.exe'], 'Image|
endswith': ['\\cmd.exe', '\\sh.exe', '\\bash.exe', '\\powershell.exe', '\\bitsadmin.e
xe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8202070f-edeb-4d31-a010-a26c72ac5600
Author: Thomas Patzke, Florian Roth (Nextron Systems), Zach Stanford @svch0st, Tim Shelton,
Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0003 , T1505.003 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/01/16 high Particular web applications may spawn a shell process legitimately
Rule Details: Sdclt Child Processes

The sdclt process creating a child process indicates a possible attempt to bypass UAC.
Rule ID
parent_child_18
Query
{'selection': {'ParentImage|endswith': '\\sdclt.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,da2738f2-fadb-4394-afa7-0a0674885afa
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://github.com/OTRF/detection-hackathon-apt29/issues/6 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/05/02 medium unknown
Rule Details: LOLBins Process Creation with WmiPrvse
A LOLBin process created by wmiprvse is suspicious.
Rule ID
parent_child_19
Query
{'selection1': {'Image|endswith': ['\\regsvr32.exe', '\\rundll32.exe', '\\msiexec.exe
', '\\mshta.exe', '\\verclsid.exe']}, 'selection2': {'ParentImage|endswith': '\\wbem\
\WmiPrvSE.exe'}, 'condition': 'selection1 and selection2'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,8a582fe2-0882-4b89-a82a-da6b2dc32937
Author: Vadim Khrykov (ThreatIntel), Cyb3rEng, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 , T1047 , TA0005 , T1218.010 
References
https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/ 
https://github.com/vadim-hunter/Detection-Ideas-
Rules/blob/main/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi
_(aka_REvil)_Ransomware.yaml 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/08/23 high Unknown
Rule Details: MMC Spawning Windows Shell
It is suspicious for MMC to launch a Windows command-line executable.
Rule ID
parent_child_20
Query
{'selection': {'ParentImage|endswith': '\\mmc.exe'}, 'selection2': [{'Image|endswith'
: ['\\cmd.exe', '\\powershell.exe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '\\
bash.exe', '\\reg.exe', '\\regsvr32.exe']}, {'Image|contains': ['\\BITSADMIN']}], 'co
ndition': 'selection and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,05a2ab7e-ce11-4b63-86db-ab32e763e11d
Author: Karneades, Swisscom CSIRT
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0008 , T1021.003 
References
https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-
object/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/05 high N/A
Rule Details: Suspicious Shells Spawn by Java Utility Keytool
It is suspicious for the Java utility keytool process to launch a shell and indicates potential
exploitations, such as adselfservice.
Rule ID
parent_child_21
Query
{'selection': {'ParentImage|endswith': '\\keytool.exe', 'Image|endswith': ['\\cmd.exe
', '\\sh.exe', '\\bash.exe', '\\powershell.exe', '\\schtasks.exe', '\\certutil.exe',
'\\whoami.exe', '\\bitsadmin.exe', '\\wscript.exe', '\\cscript.exe', '\\scrcons.exe',
'\\regsvr32.exe', '\\hh.exe', '\\wmic.exe', '\\mshta.exe', '\\rundll32.exe', '\\forf
iles.exe', '\\scriptrunner.exe', '\\mftrace.exe', '\\AppVLP.exe']}, 'condition': 'sel
ection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,90fb5e62-ca1f-4e22-b42e-cc521874c938
Author: Andreas Hunkeler (@Karneades)
Tactics, Techniques, and Procedures

XTA0001 , XT1002 
References
https://redcanary.com/blog/intelligence-insights-december-2021 
https://www.synacktiv.com/en/publications/how-to-exploit-cve-2021-40539-on-
manageengine-adselfservice-plus.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/12/22 high unknown
Rule Details: UAC Bypass via Windows Event Viewer
A UAC bypass attempt to run code with elevated permissions may be indicated when
eventvwr.exe launches mmc.exe or WerFault.exe.
Rule ID
parent_child_22
Query
{'methprocess': {'ParentImage|endswith': '\\eventvwr.exe'}, 'filterprocess': {'Image'
: ['?:\\Windows\\SysWOW64\\mmc.exe', '?:\\Windows\\System32\\mmc.exe', '?:\\Windows\\
SysWOW64\\WerFault.exe', '?:\\Windows\\System32\\WerFault.exe']}, 'condition': 'methp
rocess and not filterprocess'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,be344333-921d-4c4d-8bb8-e584cf584780
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References

https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-
hijacking/ 
https://www.hybrid-
analysis.com/sample/e122bc8bf291f15cab182a5d2d27b8db1e7019e4e96bb5cdbd1dfe
7446f3f51f?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/03/19 critical unknown
Rule Details: Malicious PE Execution by Microsoft Visual Studio Debugger
The MS VS Just-In-Time Debugger (vsjitdebugger.exe), which is a signed/verified binary, can be
exploited to launch malicious code.
Rule ID
parent_child_23
Query
{'selection': {'ParentImage|endswith': '\\vsjitdebugger.exe'}, 'reduction1': {'Image|
endswith': '\\vsimmersiveactivatehelper*.exe'}, 'reduction2': {'Image|endswith': '\\d
evenv.exe'}, 'condition': 'selection and not (reduction1 or reduction2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,15c7904e-6ad1-4a45-9b46-5fb25df37fd2
Author: Agro (@agro_sev), Ensar Şamil (@sblmsrsn), oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
https://twitter.com/pabraeken/status/990758590020452353 
https://github.com/LOLBAS-
Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vsjitdebugger.yml 

https://docs.microsoft.com/en-us/visualstudio/debugger/debug-using-the-just-in-time-
debugger?view=vs-2019 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/14 medium the process spawned by vsjitdebugger.exe is uncommon.
Rule Details: CVE-2021-26857 Exchange Exploitation
The CVE-2021-26857 vulnerability is indicated when abnormal subprocesses are launched from
Microsoft Exchange Server’s Unified Messaging service.
Rule ID
parent_child_24
Query
{'selection': {'ParentImage|endswith': '\\UMWorkerProcess.exe'}, 'filter': {'Image|en
dswith': ['\\wermgr.exe', '\\WerFault.exe']}, 'condition': 'selection and not filter'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,cd479ccc-d8f0-4c66-ba7d-e06286f3f887
Author: Bhabesh Raj
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1203 
References
https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-
servers/ 
Severity
95
Suppression Logic Based On

computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2021/03/03 critical Unknown
Rule Details: MS Office Product Spawning Exe in User Dir
It is suspicious for a Microsoft Office application to launch an executable in the Users directory.
Rule ID
parent_child_25
Query
{'selection': {'ParentImage|endswith': ['\\WINWORD.EXE', '\\EXCEL.EXE', '\\POWERPNT.e
xe', '\\MSPUB.exe', '\\VISIO.exe'], 'Image|startswith': 'C:\\users\\', 'Image|endswit
h': '.exe'}, 'filter': {'Image|endswith': '\\Teams.exe'}, 'condition': 'selection and
not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,aa3a6f94-890e-4e22-b634-ffdfd54792cc
Author: Jason Lynch
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 
References
https://blog.morphisec.com/fin7-not-finished-morphisec-spots-new-campaign 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2019/04/02 high unknown
Rule Details: Execution via stordiag.exe
The stordiag.exe process launch processes such as systeminfo.exe from a non-standard path is
suspicious.
Rule ID
parent_child_26
Query
{'selection': {'ParentImage|endswith': '\\stordiag.exe', 'Image|endswith': ['\\schtas
ks.exe', '\\systeminfo.exe', '\\fltmc.exe']}, 'filter': {'ParentImage|startswith': ['
c:\\windows\\system32\\', 'c:\\windows\\syswow64\\']}, 'condition': 'selection and no
t filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,961e0abb-1b1e-4c84-a453-aafe56ad0d34
Author: Austin Songer (@austinsonger)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
https://strontic.github.io/xcyclopedia/library/stordiag.exe-
1F08FC87C373673944F6A7E8B18CD845.html 
https://twitter.com/eral4m/status/1451112385041911809 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/21 high Legitimate usage of stordiag.exe.
Rule Details: Always Install Elevated MSI Spawned Cmd And Powershell

Detects Windows Installer service (msiexec.exe) spawning "cmd" or "powershell".
Rule ID
parent_child_27
Query
{'selection_img': {'Image|endswith': ['\\cmd.exe', '\\powershell.exe', '\\pwsh.exe']}
, 'selection_parent': {'ParentImage|contains|all': ['\\Windows\\Installer\\', 'msi'],
'ParentImage|endswith': ['tmp']}, 'filter': {'CommandLine|contains': '\\program file
s\\aella\\bins'}, 'condition': 'all of selection_* and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,1e53dd56-8d83-4eb4-a43e-b790a05510aa
Author: Teymur Kheirkhabarov (idea), Mangatas Tondang (rule), oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-181117201458/95/hunting-
for-privilege-escalation-in-windows-environment-50-638.jpg 
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 medium Penetration test
Rule Details: Wsreset UAC Bypass
The Wsreset.exe tool can be used to reset the Windows Store to bypass UAC.
Rule ID
parent_child_28
Query
{'selection': {'ParentImage|endswith': ['\\WSreset.exe']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,bdc8918e-a1d5-49d1-9db7-ea0fd91aa2ae
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://lolbas-project.github.io/lolbas/Binaries/Wsreset/ 
https://www.activecyber.us/activelabs/windows-uac-bypass 
https://twitter.com/ReaQta/status/1222548288731217921 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/01/30 high Unknown sub processes of Wsreset.exe
Rule Details: DNS RCE CVE-2020-1350
This indicates possible exploitation of a DNS RCE bug, as described in CVE-2020-1350.
Rule ID
parent_child_29
Query
{'selection': {'ParentImage|endswith': '\\System32\\dns.exe'}, 'filter': {'Image|ends
with': ['\\System32\\werfault.exe', '\\System32\\conhost.exe', '\\System32\\dnscmd.ex
e', '\\System32\\dns.exe']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,b5281f31-f9cc-4d0d-95d0-45b91c45b487

Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0002 , T1569.002 
References
https://research.checkpoint.com/2020/resolving-your-way-into-domain-admin-exploiting-
a-17-year-old-bug-in-windows-dns-servers/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/15 critical Unknown but benign sub processes of the Windows DNS service dns.exe
Rule Details: ScreenConnect Backstage Mode Anomaly
This indicates the use of Backstage mode of the ScreenConnect client, which is suspicious.
Rule ID
parent_child_30
Query
{'selection': {'ParentImage|endswith': '\\ScreenConnect.ClientService.exe', 'Image|en
dswith': ['\\cmd.exe', '\\powershell.exe', '\\pwsh.exe']}, 'selection_cli': {'Command
Line|contains': '\\TEMP\\ScreenConnect\\'}, 'condition': 'selection and selection_cli
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0011 , T1219 
References
https://www.mandiant.com/resources/telegram-malware-iranian-espionage 

https://docs.connectwise.com/ConnectWise_Control_Documentation/Get_started/Host_
client/View_menu/Backstage_mode 
Severity
50
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimenta 2022/02/25 medium Case in which administrators are allowed to use ScreenConnect's Backstage
mode
l
Rule Details: Suspicious LSASS Process Clone
This is a suspicious LSASS process clone, which could be a sign of process dumping activity.
Rule ID
parent_child_31
Query
{'selection': {'Image|endswith': '\\Windows\\System32\\lsass.exe', 'ParentImage|endsw
ith': '\\Windows\\System32\\lsass.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,c8da0dfd-4ed0-4b68-962d-13c9c884384e
Author: Florian Roth (Nextron Systems), Samir Bousseaden
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0006 , T1003.001 
References
https://www.matteomalvica.com/blog/2019/12/02/win-defender-atp-cred-bypass/ 
https://twitter.com/Hexacorn/status/1420053502554951689 
https://twitter.com/SBousseaden/status/1464566846594691073?s=20 
Severity
80

Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/11/27 critical Unknown
Rule Details: Visual Basic Command Line Compiler Usage
Use of vbc.exe with child process cvtres.exe (Windows Resource to Object Converter) should
not be seen in an enterprise environment.
Rule ID
parent_child_32
Query
{'selection': {'ParentImage|endswith': '\\vbc.exe', 'Image|endswith': '\\cvtres.exe'}
, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7b10f171-7f04-47c7-9fa2-5be43c76e535
Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1027.004 
References
https://lolbas-project.github.io/lolbas/Binaries/Vbc/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2020/10/07 high Utilization of this tool should not be seen in enterprise environment
Rule Details: Suspicious Service Run-time Directory
The services or svchost process running in a non-standard directory is suspicious.
Rule ID
parent_child_33
Query
{'selection': {'Image|contains': ['\\Users\\Public\\', '\\$Recycle.bin', '\\Users\\Al
l Users\\', '\\Users\\Default\\', '\\Users\\Contacts\\', '\\Users\\Searches\\', 'C:\\
Perflogs\\', '\\config\\systemprofile\\', '\\Windows\\Fonts\\', '\\Windows\\IME\\', '
\\Windows\\addins\\'], 'ParentImage|endswith': ['\\services.exe', '\\svchost.exe']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,883faa95-175a-4e22-8181-e5761aeb373c
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1202 
References
https://blog.truesec.com/2021/03/07/exchange-zero-day-proxylogon-and-hafnium/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/03/09 high Unknown
Rule Details: Mshta Spawning Windows Shell
The mshta.exe process launching a command shell process is suspicious.

Rule ID
parent_child_34
Query
{'selection': {'ParentImage|endswith': '\\mshta.exe', 'Image|endswith': ['\\powershel
l.exe', '\\cmd.exe', '\\WScript.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,772bb24c-8df2-4be0-9157-ae4dfa794037
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , TA0005 , T1218 
References
https://app.any.run/tasks/f0fac90f-84ac-4faa-b5b2-f4353c388969/# 
https://app.any.run/tasks/9c0f37bc-867a-4314-b685-e101566766d7/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/06/28 high Unknown
Rule Details: Bypass UAC via Fodhelper.exe
This could indicate the use of Fodhelper.exe to bypass User Account Control. Adversaries may
use this technique to run privileged processes.
Rule ID
parent_child_35
Query
{'selection': {'ParentImage|endswith': '\\fodhelper.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process creation
Rule Source
SigmaHQ,7f741dcf-fc22-4759-87b4-9ae8376676a2
Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert), oscd.community
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://eqllib.readthedocs.io/en/latest/analytics/e491ce22-792f-11e9-8f5c-
d46d6d62a49e.html 
https://github.com/redcanaryco/atomic-red-
team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T1548.002
.md 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Legitimate use of fodhelper.exe utility by legitimate user
Rule Details: Suspicious Serv-U Process Pattern
Certain child processes launched by Serve-U.exe indicate possible exploitation.
Rule ID
parent_child_36
Query
{'selection': {'ParentImage|endswith': '\\Serv-
U.exe', 'Image|endswith': ['\\cmd.exe', '\\powershell.exe', '\\wscript.exe', '\\cscri
pt.exe', '\\sh.exe', '\\bash.exe', '\\schtasks.exe', '\\regsvr32.exe', '\\wmic.exe',
'\\mshta.exe', '\\rundll32.exe', '\\msiexec.exe', '\\forfiles.exe', '\\scriptrunner.e
xe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,58f4ea09-0fc2-4520-ba18-b85c540b0eaf
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0006 , T1555 
References
https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-
targeting-solarwinds-serv-u-software-with-0-day-exploit/ 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experimen 2021/07/14 critical Legitimate uses in which users or programs use the SSH service of Serv-U for remote
command execution
tal
Rule Details: HTML Help Shell Spawn
It is a suspicious a child process of the Microsoft HTML Help system.
Rule ID
parent_child_37
Query
{'selection': {'ParentImage': 'C:\\Windows\\hh.exe', 'Image|endswith': ['\\cmd.exe',
'\\powershell.exe', '\\wscript.exe', '\\cscript.exe', '\\regsvr32.exe', '\\wmic.exe',
'\\rundll32.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,52cad028-0ff0-4854-8f67-d25dfcbc78b4
Author: Maxim Pavlunin, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 , T1047 , TA0005 , T1218 

References
https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/chm-badness-
delivers-a-banking-trojan/ 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/04/01 high unknown
Rule Details: Regedit as Trusted Installer
Running the regedit process as a TrustedInstaller is suspicious.
Rule ID
parent_child_38
Query
{'selection': {'Image|endswith': '\\regedit.exe', 'ParentImage|endswith': ['\\Trusted
Installer.exe', '\\ProcessHacker.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,883835a7-df45-43e4-bf1d-4268768afda4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548 
References
https://twitter.com/1kwpeter/status/1397816101455765504 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name

process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/05/27 high Unlikely
Rule Details: Script Event Consumer Spawning Process
The scrcons.exe process launching PowerShell or other uncommon processes is suspicious.
Rule ID
parent_child_39
Query
{'selection': {'ParentImage|endswith': ['\\scrcons.exe'], 'Image|endswith': ['\\svcho
st.exe', '\\dllhost.exe', '\\powershell.exe', '\\pwsh.exe', '\\wscript.exe', '\\cscri
pt.exe', '\\schtasks.exe', '\\regsvr32.exe', '\\mshta.exe', '\\rundll32.exe', '\\msie
xec.exe', '\\msbuild.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,f6d1dd2f-b8ce-40ca-bc23-062efb686b34
Author: Sittikorn S
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1047 
References
https://redcanary.com/blog/child-processes/ 
https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-
reference/cortex-xdr-analytics-alert-reference/scrcons-exe-rare-child-process.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information

| Maturity | Creation Date |     |     | Risk Level | False Positives |
| -------- | ------------- | --- | --- | ---------- | --------------- |
| test     | 2021/06/21    |     |     | high       | Unknown         |
Rule Details: WMI Persistence - Script Event Consumer
A persistent scrcons.exe child process indicates a WMI backdoor may have been created.
Rule ID
parent_child_40
Query
{'selection': {'Image': 'C:\\WINDOWS\\system32\\wbem\\scrcons.exe', 'ParentImage': 'C
:\\Windows\\System32\\svchost.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,ec1d5e28-8f3b-4188-a6f8-6e8df81dc28e
Author: Thomas Patzke
Tactics, Techniques, and Procedures
| XTA0001 | , XT1002 | , TA0003 | , T1546.003 |    |     |
| ------- | --------- | --------- | ------------ | --- | --- |
References
|     | https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/ |     |     |     |    |
| --- | ----------------------------------------------------- | --- | --- | --- | --- |
Severity
50
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
| Matu Creation | Risk  | False Positives            |     |     |     |
| ------------- | ----- | -------------------------- | --- | --- | --- |
| rity Date     | Level |                            |     |     |     |
| test 2018/03/ | mediu | Legitimate event consumers |     |     |     |
07 m Dell computers on some versions register an event consumer that is known to cause false
positives when brightness is changed by the corresponding keyboard button
Rule Details: Suspicious Svchost Process
Launch of svchost.exe from certain parent processes is suspicious.
Rule ID

parent_child_41
Query
{'selection': {'Image|endswith': '\\svchost.exe'}, 'filter': {'ParentImage|endswith':
['\\services.exe', '\\MsMpEng.exe', '\\Mrt.exe', '\\rpcnet.exe', '\\svchost.exe', '\
\ngen.exe', '\\TiWorker.exe']}, 'filter_null1': {'ParentImage': None}, 'filter_null2'
: {'ParentImage': ''}, 'filter_emptysysmon': {'ParentImage': '-
'}, 'condition': 'selection and not 1 of filter*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,01d2e2a1-5f09-44f7-9fc1-24faa7479b6d
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036.005 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/08/15 high Unknown
Rule Details: Exploit for CVE-2015-1641
Launch of MicroScMgmt.exe from Winword is uncommon and indicative of exploits described in
CVE-2015-1641.
Rule ID
parent_child_42
Query
{'selection': {'ParentImage|endswith': '\\WINWORD.EXE', 'Image|endswith': '\\MicroScM
gmt.exe'}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,7993792c-5ce2-4475-a3db-a3a5539827ef
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036.005 
References
https://www.virustotal.com/en/file/5567408950b744c4e846ba8ae726883cb15268a539f3
bb21758a466e47021ae8/analysis/ 
https://www.hybrid-
analysis.com/sample/5567408950b744c4e846ba8ae726883cb15268a539f3bb21758a4
66e47021ae8?environmentId=100 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2018/02/22 critical Unknown
Rule Details: TA505 Dropper Load Pattern
Loading of the mshta process by the wmiprvse process is indicative of TA505 malicious
documents.
Rule ID
parent_child_43
Query
{'selection': {'Image|endswith': '\\mshta.exe', 'ParentImage|endswith': '\\wmiprvse.e
xe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

SigmaHQ,18cf6cf0-39b0-4c22-9593-e244bdc9a2d4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1106 
References
https://twitter.com/ForensicITGuy/status/1334734244120309760 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/12/08 critical unknown
Rule Details: Execution via WorkFolders.exe
It is suspicious for WorkFolders.exe to run an arbitrary control.exe.
Rule ID
parent_child_44
Query
{'selection': {'Image|endswith': '\\control.exe', 'ParentImage|endswith': '\\WorkFold
ers.exe'}, 'filter': {'Image': 'C:\\Windows\\System32\\control.exe'}, 'condition': 's
election and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Requirements: Sysmon ProcessCreation logging must be activated
Rule Source
SigmaHQ,0bbc6369-43e3-453d-9944-cae58821c173
Author: Maxime Thiebaut (@0xThiebaut)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References

https://twitter.com/elliotkillick/status/1449812843772227588 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/10/21 high Legitimate usage of the uncommon Windows Work Folders feature.
Rule Details: Microsoft Outlook Product Spawning Windows Shell
It is suspicious for Microsoft Outlook to start a Windows command and scripting interpreter
executable.
Rule ID
parent_child_45
Query
{'selection': {'ParentImage|endswith': '\\OUTLOOK.EXE', 'Image|endswith': ['\\cmd.exe
', '\\powershell.exe', '\\wscript.exe', '\\cscript.exe', '\\sh.exe', '\\bash.exe', '\
\scrcons.exe', '\\schtasks.exe', '\\regsvr32.exe', '\\hh.exe', '\\wmic.exe', '\\mshta
.exe', '\\msiexec.exe', '\\forfiles.exe', '\\scriptrunner.exe', '\\mftrace.exe', '\\A
ppVLP.exe', '\\svchost.exe', '\\msbuild.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,208748f7-881d-47ac-a29c-07ea84bf691d
Author: Michael Haag, Florian Roth (Nextron Systems), Markus Neis, Elastic, FPT.EagleEye
Team
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204.002 
References
https://www.hybrid-
analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8bad54e2
95f28bbc21?environmentId=100 
https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html 

Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/28 high unknown
Rule Details: Bypass UAC via WSReset.exe
This could indicate the use of WSReset.exe to bypass User Account Control. Adversaries may
use this technique to run privileged processes.
Rule ID
parent_child_46
Query
{'selection': {'ParentImage|endswith': '\\wsreset.exe'}, 'filter': {'Image|endswith':
'\\conhost.exe'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,d797268e-28a9-49a7-b9a8-2f5039011c5c
Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert), oscd.community,
Florian Roth
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1548.002 
References
https://eqllib.readthedocs.io/en/latest/analytics/532b5ed4-7930-11e9-8f5c-
d46d6d62a49e.html 
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Unknown
Rule Details: Emissary Panda Malware SLLauncher
This indicates running of DLL side-loading malware which is used by the threat group Emissary
Panda, also known as APT27.
Rule ID
parent_child_48
Query
{'selection': {'ParentImage|endswith': '\\sllauncher.exe', 'Image|endswith': '\\svcho
st.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
SigmaHQ,9aa01d62-7667-4d3b-acb8-8cb5103e2014
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1574.002 
References
https://app.any.run/tasks/579e7587-f09d-4aae-8b07-472833262965 
https://twitter.com/cyb3rops/status/1168863899531132929 
Severity
95
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/09/03 critical Unknown
Rule Details: Suspicious JAVA Child Process

This may indicate an attempt to run a malicious JAR file or an attempt to exploit a JAVA-specific
vulnerability.
Rule ID
parent_child_49
Query
{'selection1': {'ParentImage|endswith': '/java'}, 'selection2': {'Image|endswith': ['
/sh', '/bash', '/dash', '/ksh', '/tcsh', '/zsh', '/curl', '/wget']}, 'condition': 'se
lection1 and selection2'}
Log Source
Stellar Cyber linux configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
hostip
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/01/19 medium N/A
Rule Details: Suspicious SolarWinds Child Process
A SolarWinds process that launches a child process may indicate an attempt to run malicious
programs.
Rule ID
parent_child_50
Query
{'selection1': {'ParentImage|endswith': ['\\SolarWinds.BusinessLayerHost.exe', '\\Sol
arWinds.BusinessLayerHostx64.exe']}, 'selection2': {'Image|endswith': ['\\APMServiceC
ontrol.exe', '\\ExportToPDFCmd.Exe', '\\SolarWinds.Credentials.Orion.WebApi.exe', '\\

SolarWinds.Orion.Topology.Calculator.exe', '\\Database-
Maint.exe', '\\SolarWinds.Orion.ApiPoller.Service.exe', '\\WerFault.exe', '\\WerMgr.e
xe']}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1195 , XTA0001 , XT1002 , TA0002 , T1106 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
producti 2020/12/14 medium Trusted SolarWinds child processes, verify process details such as network
connections and file writes.
on
Rule Details: Execution via MSSQL xp_cmdshell Stored Procedure
Use of MSSQL to run a stored procedure with xp_cmdshell, disabled by default, indicates a user
may be attempting to elevate their privileges.
Rule ID
parent_child_51
Query
{'selection1': {'Image|endswith': '\\cmd.exe'}, 'selection2': {'ParentImage|endswith'
: '\\sqlservr.exe'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/14 high N/A
Rule Details: Process Activity via Compiled HTML File
Compiled HTML files (.chm), commonly distributed as help systems, have the capability of
concealing malicious code and delivering to a victim system. It is suspicious when the runtime
program for .chm files (hh.exe) launches other certain processes (such as a command shell).
Rule ID
parent_child_52
Query
{'selection1': {'ParentImage|endswith': '\\hh.exe'}, 'selection2': {'Image|endswith':
['\\mshta.exe', '\\cmd.exe', '\\powershell.exe', '\\pwsh.exe', '\\powershell_ise.exe
', '\\cscript.exe', '\\wscript.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1204 , TA0005 , T1218 
References
N/A
Severity

49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/02/ mediu The HTML Help executable program (hh.exe) runs whenever a user clicks a compiled help
(.chm) file or menu item that opens the help file inside the Help Viewer. This is not always
tion 18 m
malicious, but adversaries may abuse this technology to conceal malicious code.
Rule Details: Signed Proxy Execution via MS WorkFolders
Use of Windows Work Folders to run a control.exe file in the current working directory is
indicative of potential malicious activity.
Rule ID
parent_child_53
Query
{'selection1': {'Image|endswith': '\\control.exe'}, 'selection2': {'ParentImage|endsw
ith': '\\WorkFolders.exe'}, 'selection3': {'Image': ['?:\\Windows\\System32\\control.
exe', '?:\\Windows\\SysWOW64\\control.exe']}, 'condition': 'selection1 and selection2
and (not selection3)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1218 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/03/02 medium N/A
Rule Details: Microsoft Exchange Server UM Spawning Suspicious Processes
The CVE-2021-26857 vulnerability may be indicated when Exchange Server UM processes
launch unexpected child processes.
Rule ID
parent_child_54
Query
{'selection1': {'ParentImage|endswith': ['\\UMService.exe', '\\UMWorkerProcess.exe']}
, 'selection2': {'Image|endswith': ['\\werfault.exe', '\\wermgr.exe']}, 'condition':
'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2021/03/ mediu Legitimate processes may be spawned from the Microsoft Exchange Server Unified
Messaging (UM) service. If known processes are causing false positives, they can be
tion 04 m
exempted from the rule.
Rule Details: Unusual Parent-Child Relationship
A Windows program run from an unexpected parent process could indicate masquerading or
other strange activity on a system.

Rule ID
parent_child_55
Query
{'selection1': {'Image|endswith': '\\autochk.exe'}, 'selection2': {'ParentImage|endsw
ith': '\\smss.exe'}, 'selection3': {'Image|endswith': ['\\fontdrvhost.exe', '\\dwm.ex
e']}, 'selection4': {'ParentImage|endswith': ['\\wininit.exe', '\\winlogon.exe']}, 's
election5': {'Image|endswith': ['\\consent.exe', '\\RuntimeBroker.exe', '\\TiWorker.e
xe']}, 'selection6': {'ParentImage|endswith': '\\svchost.exe'}, 'selection7': {'Image
|endswith': '\\SearchIndexer.exe'}, 'selection8': {'ParentImage|endswith': '\\service
s.exe'}, 'selection9': {'Image|endswith': '\\SearchProtocolHost.exe'}, 'selection10':
{'ParentImage|endswith': ['\\SearchIndexer.exe', '\\dllhost.exe']}, 'selection11': {
'Image|endswith': '\\dllhost.exe'}, 'selection12': {'ParentImage|endswith': ['\\servi
ces.exe', '\\svchost.exe']}, 'selection13': {'Image|endswith': '\\smss.exe'}, 'select
ion14': {'ParentImage|endswith': ['System', '\\smss.exe']}, 'selection15': {'Image|en
dswith': '\\csrss.exe'}, 'selection16': {'ParentImage|endswith': ['\\smss.exe', '\\sv
chost.exe']}, 'selection17': {'Image|endswith': '\\wininit.exe'}, 'selection18': {'Im
age|endswith': '\\winlogon.exe'}, 'selection19': {'Image|endswith': ['\\lsass.exe', '
\\LsaIso.exe']}, 'selection20': {'ParentImage|endswith': '\\wininit.exe'}, 'selection
21': {'Image|endswith': '\\LogonUI.exe'}, 'selection22': {'Image|endswith': '\\servic
es.exe'}, 'selection23': {'Image|endswith': '\\svchost.exe'}, 'selection24': {'Parent
Image|endswith': ['\\MsMpEng.exe', '\\services.exe']}, 'selection25': {'Image|endswit
h': '\\spoolsv.exe'}, 'selection26': {'Image|endswith': '\\taskhost.exe'}, 'selection
27': {'Image|endswith': '\\taskhostw.exe'}, 'selection28': {'Image|endswith': '\\user
init.exe'}, 'selection29': {'ParentImage|endswith': ['\\dwm.exe', '\\winlogon.exe']},
'selection30': {'Image|endswith': ['\\wmiprvse.exe', '\\wsmprovhost.exe', '\\winrsho
st.exe']}, 'selection31': {'ParentImage|endswith': ['\\SearchProtocolHost.exe', '\\cs
rss.exe']}, 'selection32': {'Image|endswith': ['\\werfault.exe', '\\wermgr.exe', '\\W
erFaultSecure.exe']}, 'selection33': {'ParentImage|endswith': '\\autochk.exe'}, 'sele
ction34': {'Image|endswith': ['\\chkdsk.exe', '\\doskey.exe', '\\WerFault.exe']}, 'se
lection35': {'Image|endswith': ['\\autochk.exe', '\\smss.exe', '\\csrss.exe', '\\wini
nit.exe', '\\winlogon.exe', '\\setupcl.exe', '\\WerFault.exe']}, 'selection36': {'Par
entImage|endswith': '\\wermgr.exe'}, 'selection37': {'Image|endswith': ['\\WerFaultSe
cure.exe', '\\wermgr.exe', '\\WerFault.exe']}, 'selection38': {'ParentImage|endswith'
: '\\conhost.exe'}, 'selection39': {'Image|endswith': ['\\mscorsvw.exe', '\\wermgr.ex
e', '\\WerFault.exe', '\\WerFaultSecure.exe']}, 'condition': '((selection1 and (not s
election2)) or (selection3 and (not selection4)) or (selection5 and (not selection6))
or (selection7 and (not selection8)) or (selection9 and (not selection10)) or (selec
tion11 and (not selection12)) or (selection13 and (not selection14)) or (selection15
and (not selection16)) or (selection17 and (not selection2)) or (selection18 and (not
selection2)) or (selection19 and (not selection20)) or (selection21 and (not selecti
on4)) or (selection22 and (not selection20)) or (selection23 and (not selection24)) o
r (selection25 and (not selection8)) or (selection26 and (not selection12)) or (selec
tion27 and (not selection12)) or (selection28 and (not selection29)) or (selection30
and (not selection6)) or (selection31 and (not selection32)) or (selection33 and (not

selection34)) or (selection2 and (not selection35)) or (selection36 and (not selecti
on37)) or (selection38 and (not selection39)))'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1055 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/02/18 medium N/A
Rule Details: Suspicious Process from Conhost
A suspicious Conhost child process may indicate code injection activity.
Rule ID
parent_child_56
Query
{'selection1': {'ParentImage|endswith': '\\conhost.exe'}, 'selection2': {'Image': ['?
:\\Windows\\splwow64.exe', '?:\\Windows\\System32\\WerFault.exe', '?:\\Windows\\Syste
m32\\conhost.exe']}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

XTA0001 , XT1002 , TA0005 , T1055 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/31 high N/A
Rule Details: Suspicious Zoom Child Process
Launch of Zoom from a command shell may indicate an attempt to run Zoom undetected.
Rule ID
parent_child_57
Query
{'selection1': {'ParentImage|endswith': '\\Zoom.exe'}, 'selection2': {'Image|endswith
': ['\\cmd.exe', '\\powershell.exe', '\\pwsh.exe', '\\powershell_ise.exe']}, 'conditi
on': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036 , T1055 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name

stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/09/03 medium N/A
Rule Details: Unusual Parent Process for cmd.exe
Launching of cmd.exe from an unusual parent process is suspicious.
Rule ID
parent_child_58
Query
{'selection1': {'Image|endswith': '\\cmd.exe'}, 'selection2': {'ParentImage|endswith'
: ['\\lsass.exe', '\\csrss.exe', '\\epad.exe', '\\regsvr32.exe', '\\dllhost.exe', '\\
LogonUI.exe', '\\wermgr.exe', '\\spoolsv.exe', '\\jucheck.exe', '\\jusched.exe', '\\c
tfmon.exe', '\\taskhostw.exe', '\\GoogleUpdate.exe', '\\sppsvc.exe', '\\sihost.exe',
'\\slui.exe', '\\SIHClient.exe', '\\SearchIndexer.exe', '\\SearchProtocolHost.exe', '
\\FlashPlayerUpdateService.exe', '\\WerFault.exe', '\\WUDFHost.exe', '\\unsecapp.exe'
, '\\wlanext.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/21 medium N/A
Rule Details: Suspicious MS Office Child Process

Certain child processes being launched from MS Office applications or documents with macros
are indicative of malicious activity.
Rule ID
parent_child_59
Query
{'selection1': {'ParentImage|endswith': ['\\eqnedt32.exe', '\\excel.exe', '\\fltldr.e
xe', '\\msaccess.exe', '\\mspub.exe', '\\powerpnt.exe', '\\winword.exe']}, 'selection
2': {'Image|endswith': ['\\Microsoft.Workflow.Compiler.exe', '\\arp.exe', '\\atbroker
.exe', '\\bginfo.exe', '\\bitsadmin.exe', '\\cdb.exe', '\\certutil.exe', '\\cmd.exe',
'\\cmstp.exe', '\\control.exe', '\\cscript.exe', '\\csi.exe', '\\dnx.exe', '\\dsget.
exe', '\\dsquery.exe', '\\forfiles.exe', '\\fsi.exe', '\\ftp.exe', '\\gpresult.exe',
'\\hostname.exe', '\\ieexec.exe', '\\iexpress.exe', '\\installutil.exe', '\\ipconfig.
exe', '\\mshta.exe', '\\msxsl.exe', '\\nbtstat.exe', '\\net.exe', '\\net1.exe', '\\ne
tsh.exe', '\\netstat.exe', '\\nltest.exe', '\\odbcconf.exe', '\\ping.exe', '\\powersh
ell.exe', '\\pwsh.exe', '\\qprocess.exe', '\\quser.exe', '\\qwinsta.exe', '\\rcsi.exe
', '\\reg.exe', '\\regasm.exe', '\\regsvcs.exe', '\\regsvr32.exe', '\\sc.exe', '\\sch
tasks.exe', '\\systeminfo.exe', '\\tasklist.exe', '\\tracert.exe', '\\whoami.exe', '\
\wmic.exe', '\\wscript.exe', '\\xwizard.exe', '\\explorer.exe', '\\rundll32.exe', '\\
hh.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1566 , XTA0001 , XT1002 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/02/18 medium N/A

Rule Details: Microsoft Build Engine Started by a System Process
It is unusual for Explorer or the WMI (Windows Management Instrumentation) subystem to
launch MSBuild, the Microsoft Build Engine.
Rule ID
parent_child_60
Query
{'selection1': {'Image|endswith': '\\MSBuild.exe'}, 'selection2': {'ParentImage|endsw
ith': ['\\explorer.exe', '\\wmiprvse.exe']}, 'condition': 'selection1 and selection2'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1127 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
productio 2020/03/25 medium The Build Engine is commonly used by Windows developers but use by non-
engineers is unusual.
n
Rule Details: Microsoft Build Engine Started by an Office Application
Launch of the Microsoft Build Engine from an Office application is unusual and may indicate the
associated document has run a malicious script payload.
Rule ID
parent_child_61
Query

{'selection1': {'Image|endswith': '\\MSBuild.exe'}, 'selection2': {'ParentImage|endsw
ith': ['\\eqnedt32.exe', '\\excel.exe', '\\fltldr.exe', '\\msaccess.exe', '\\mspub.ex
e', '\\outlook.exe', '\\powerpnt.exe', '\\winword.exe']}, 'condition': 'selection1 an
d selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1127 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/03/ high The Build Engine is commonly used by Windows developers but use by non-engineers is
unusual. It is quite unusual for this program to be started by an Office application like Word or
tion 25 Excel.
Rule Details: Command Execution via SolarWinds Process
A SolarWinds process that launches a command-line call or PowerShell command is considered
suspicious.
Rule ID
parent_child_62
Query
{'selection1': {'Image|endswith': ['\\cmd.exe', '\\powershell.exe']}, 'selection2': {
'ParentImage|endswith': ['\\ConfigurationWizard.exe', '\\NetflowDatabaseMaintenance.e
xe', '\\NetFlowService.exe', '\\SolarWinds.Administration.exe', '\\SolarWinds.Collect
or.Service.exe', '\\SolarwindsDiagnostics.exe']}, 'condition': 'selection1 and select
ion2'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1195 , XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
producti 2020/12/14 medium Trusted SolarWinds child processes. Verify process details such as network
connections and file writes.
on
Rule Details: Suspicious .NET Code Compilation
This may indicate suspicious .NET or Visual Basic compilation of downloaded code.
Rule ID
parent_child_63
Query
{'selection1': {'Image|endswith': ['\\csc.exe', '\\vbc.exe']}, 'selection2': {'Parent
Image|endswith': ['\\wscript.exe', '\\mshta.exe', '\\cscript.exe', '\\wmic.exe', '\\s
vchost.exe', '\\rundll32.exe', '\\cmstp.exe', '\\regsvr32.exe']}, 'condition': 'selec
tion1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

XTA0001 , XT1002 , TA0005 , T1027 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/21 medium N/A
Rule Details: Conhost Spawned By Suspicious Parent Process
The Console Window Host (conhost.exe) process being launched by a suspicious parent
process is indicative of code injection.
Rule ID
parent_child_64
Query
{'selection1': {'Image|endswith': '\\conhost.exe'}, 'selection2': {'ParentImage|endsw
ith': ['\\svchost.exe', '\\lsass.exe', '\\services.exe', '\\smss.exe', '\\winlogon.ex
e', '\\explorer.exe', '\\dllhost.exe', '\\rundll32.exe', '\\regsvr32.exe', '\\userini
t.exe', '\\wininit.exe', '\\spoolsv.exe', '\\wermgr.exe', '\\csrss.exe', '\\ctfmon.ex
e']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0002 , T1059 
References
N/A
Severity
74
Suppression Logic Based On

computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/17 high N/A
Rule Details: Unusual Child Process of dns.exe
Such an unexpected process being launched from dns.exe may indicate activity related to
running of remote code or other forms of exploitation.
Rule ID
parent_child_65
Query
{'selection1': {'ParentImage|endswith': '\\dns.exe'}, 'selection2': {'Image|endswith'
: '\\conhost.exe'}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0003 , T1133 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2020/07/ high Werfault.exe will legitimately spawn when dns.exe crashes, but the DNS service is very stable
and so this is a low occurring event. Denial of Service (DoS) attempts by intentionally crashing
tion 16
the service will also cause werfault.exe to spawn.

Rule Details: Script Process Child of Common Web Processes
A parent web process, such as httpd.exe, that runs a script process, such as powershell.exe, is
suspicious and indicative of possible attempts for remote shell access.
Rule ID
parent_child_66
Query
{'selection1': {'ParentImage|endswith': ['\\w3wp.exe', '\\httpd.exe', '\\nginx.exe',
'\\php.exe', '\\php-
cgi.exe', '\\tomcat.exe']}, 'selection2': {'Image|endswith': ['\\cmd.exe', '\\cscript
.exe', '\\powershell.exe', '\\pwsh.exe', '\\powershell_ise.exe', '\\wmic.exe', '\\wsc
ript.exe']}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 , XTA0001 , XT1002 , TA0003 , T1505 
References
N/A
Severity
74
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
producti 2021/08/24 high Security audits, maintenance, and network administrative scripts may trigger this alert
when run under web processes.
on
Rule Details: Suspicious Endpoint Security Parent Process
A suspicious Endpoint Security parent process was detected, which may indicate process
hollowing or other form of code injection.
Rule ID

parent_child_67
Query
{'selection1': {'Image|endswith': ['\\esensor.exe', '\\elastic-
endpoint.exe']}, 'selection2': {'ParentImage': ['C:\\Program Files\\Elastic\\*', 'C:\
\Windows\\System32\\services.exe', 'C:\\Windows\\System32\\WerFault*.exe', 'C:\\Windo
ws\\System32\\wermgr.exe']}, 'condition': 'selection1 and (not selection2)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process creation
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
XTA0001 , XT1002 , TA0005 , T1036 
References
N/A
Severity
49
Suppression Logic Based On
computer_name
parent_proc_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2020/08/24 medium N/A
Suspicious AD Kerberos Rule IDs
Rule Details: Suspicious Active Directory Kerberos Certificate Authentication
A Golden Certificate is a persistence technique that expands upon an AD CS compromise. If
malicious actors obtain administrative access to a CA, they can extract a CA certificate and
private key. Once obtained, these can be used to forge valid certificates for client authentication
to impersonate any other user object in the domain. This rule detects unusual certificate usage
by monitoring certificate-based authentication.
Rule ID
suspicious_kerberos_certificate_authentication
Query

{'selection': {'EventID': 4768}, 'condition': 'selection |
count() by TargetUserName > 5', 'timeframe': '15m'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1558 
References
https://rootguard.gitbook.io/cyberops/detection-engineering/ad-attack-detections-and-
mitigations/golden-certificate 
Severity
50
Suppression Logic Based On
event_data.CertIssuerName
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2025/06/ mediu False positives are possible if multiple legitimate users requested Kerberos authentication
tickets from legitimate Active Directory Certificate Services (AD CS). We recommend
ental 16 m excluding known trusted accounts or administrators.
Encoded PowerShell Rule IDs
Rule Details: Encoded PowerShell
A Windows host executed an encoded PowerShell script. Investigate the script contents to see if
it is malicious. If so, consider quarantining the host.
Rule ID
threat_encoded_powershell
Query
{'selection1': {'detection_flag': [2100, 2101]}, 'condition': 'selection1'}
Detection Flag
Note: detection_flag is a Stellar enriched field.
2100: Encoded PowerShell
2101: Encoded PowerShell with hidden flag

Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0002 , T1059 
References
N/A
Severity
80
Suppression Logic Based On
srcip
detection_flag
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2018/12/01 critical N/A
Windows Identity Threat Detection and Response (ITDR)
Rule IDs
Rule Details: Security-Enabled Universal Group was Created
A Security-Enabled Universal Group has been created. This could be an indication of malicious
activity.
Rule ID
windows_itdr_4
Query
{'selection1': {'EventID': 4754}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 

References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName
event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Security-Enabled Global Group was Created
A Security-Enabled Global Group has been created. This could be an indication of malicious
activity.
Rule ID
windows_itdr_5
Query
{'selection1': {'EventID': 4727}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName

event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Security-Enabled Local Group was Created
A Security-Enabled Local Group has been created. This could be an indication of malicious
activity.
Rule ID
windows_itdr_8
Query
{'selection1': {'EventID': 4731}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.SubjectDomainName
event_data.SubjectUserSid
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows Network Connection Rule IDs
Rule Details: Network Activity From MSBuild

MSBuild is a powerful tool used to compile and package code. If the MSBuild utility is accessing
network resources, it might be using code from a third party or even downloading malicious code
or executables. Malicious executables can even run inside of MSBuild with little indication it is
doing so.
Rule ID
windows_network_connection_1
Query
{'selection': {'EventImage|endswith': '\\MSBuild.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring Windows network connection events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1127 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.Image
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Network Activity From mshta
Mshta is the Microsoft HTML Application Host and allows the execution of .hta files. If the mshta
utility is accessing network resources, it might be using code from a third party or even
downloading malicious code or executables.
Rule ID
windows_network_connection_2
Query
{'selection': {'EventImage|endswith': '\\mshta.exe'}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Monitoring Windows network connection events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218.005 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.Image
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Network Activity From msxsl
Msxsl allows you to perform command line Extensible Stylesheet Language (XSL)
transformations. If the msxsl utility is accessing network resources, it might be using code from a
third party or even downloading malicious code or executables.
Rule ID
windows_network_connection_3
Query
{'selection': {'EventImage|endswith': '\\msxsl.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring Windows network connection events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A

Severity
50
Suppression Logic Based On
computer_name
event_data.Image
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Network Activity From verclsid
Verclsid allows you to validate shell extensions before they are instantiated by the Windows shell
or Windows Explorer. If the verclsid utility is accessing network resources, it might be using code
from a third party or even downloading malicious code or executables.
Rule ID
windows_network_connection_4
Query
{'selection': {'EventImage|endswith': '\\verclsid.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring Windows network connection events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.Image
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A

Rule Details: Unexpected Network Activity from Microsoft Tool
A Microsoft tool was executed with suspicious network connection activity. This could be an
indication of malicious activity.
Rule ID
windows_network_connection_5
Query
{'selection': {'EventImage|endswith': ['\\bginfo.exe', '\\rcsi.exe', '\\control.exe',
'\\odbcconf.exe']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring Windows network connection events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1218 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.Image
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Windows Process Access Rule IDs
Rule Details: LSASS Memory Access by Tool With Dump Keyword In Name
Detects LSASS process access requests from a source process with the "dump" keyword in its
image name.
Rule ID
windows_process_access_1
Query

{'selection': {'TargetImage|endswith': '\\lsass.exe', 'SourceImage|contains': 'dump'}
, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process access
Rule Source
SigmaHQ,9bd012ee-0dff-44d7-84a0-aa698cfd87a3
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
https://twitter.com/_xpn_/status/1491557187168178176 
https://www.ired.team/offensive-security/credential-access-and-credential-
dumping/dump-credentials-from-lsass-process-without-mimikatz 
Severity
75
Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/02/10 high Rare programs that contain the word dump in their name and access lsass
Rule Details: Credential Dumping Activity By Python Based Tool
Detects LSASS process access for potential credential dumping by a Python-like tool such as
LaZagne or Pypykatz.
Rule ID
windows_process_access_2
Query
{'selection': {'TargetImage|endswith': '\\lsass.exe', 'CallTrace|contains': '_ctypes.
pyd'}, 'filter_av': {'SourceImage': ['?:\\Windows\\TEMP\\rapid7\\ir_agent.exe']}, 'co
ndition': 'selection and not filter_av'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Monitoring process access
Rule Source
SigmaHQ,f8be3e82-46a3-4e4e-ada5-8e538ae8b9c9
Author: Bhabesh Raj, Jonhnathan Ribeiro
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
https://twitter.com/bh4b3sh/status/1303674603819081728 
https://github.com/skelsec/pypykatz 
Severity
75
Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2023/11/27 high Unknown
Rule Details: LSASS Memory Access by Process in Temp Folder
Identifies suspicious access to LSASS from a source process in Temp folder.
Rule ID
windows_process_access_3
Query
{'selection': {'TargetImage|endswith': '\\lsass.exe', 'SourceImage': ['*\\Local\\Temp
\\*', '*\\LocalLow\\Temp\\*', '*\\Roaming\\Temp\\*']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process access
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References

N/A
Severity
75
Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2024/01/26 high Unknown
Rule Details: Suspicious LSASS Access via MalSecLogon
Identifies suspicious access to LSASS handle from a call trace pointing to seclogon.dll and with a
suspicious access rights value. This may indicate an attempt to leak an LSASS handle via
abusing the Secondary Logon service in preparation for credential access.
Rule ID
windows_process_access_4
Query
{'selection1': {'TargetImage|endswith': '\\lsass.exe'}, 'selection2': {'CallTrace|con
tains': 'seclogon.dll'}, 'selection3': {'SourceImage|endswith': 'svchost.exe'}, 'sele
ction4': {'GrantedAccess': '0x14c0'}, 'condition': 'selection1 and selection2 and sel
ection3 and selection4'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process access
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
N/A
Severity
75
Suppression Logic Based On
computer_name
event_data.SourceImage

event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/06/29 high N/A
Rule Details: Potential Credential Access via DuplicateHandle in LSASS
Identifies suspicious access to an LSASS handle via DuplicateHandle from an unknown call
trace module. This may indicate an attempt to bypass the NtOpenProcess API to evade
detection and dump LSASS memory for credential access.
Rule ID
windows_process_access_5
Query
{'selection1': {'SourceImage|endswith': '\\lsass.exe'}, 'selection2': {'GrantedAccess
': '0x40'}, 'selection3': {'CallTrace|contains': 'UNKNOWN'}, 'condition': 'selection1
and selection2 and selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process access
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/09/27 medium N/A
Rule Details: Potential Credential Access via LSASS Memory Dump

Identifies suspicious access to LSASS handle from a call trace pointing to DBGHelp.dll or
DBGCore.dll, which both export the MiniDumpWriteDump method that can be used to dump
LSASS memory content in preparation for credential access.
Rule ID
windows_process_access_6
Query
{'selection1': {'TargetImage|endswith': '\\lsass.exe'}, 'selection2': {'CallTrace|con
tains': ['dbghelp.dll', 'dbgcore.dll']}, 'selection3': {'SourceImage': ['?:\\Windows\
\System32\\WerFault.exe', '?:\\Windows\\System32\\WerFaultSecure.exe', '?:\\Windows\\
System32\\tasklist.exe']}, 'condition': 'selection1 and selection2 and (not selection
3)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring process access
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
N/A
Severity
75
Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/10/07 high N/A
Windows Registry Set Rule IDs
Rule Details: Potential Ransomware Activity Using LegalNotice Message
Detect changes to the "LegalNoticeCaption" or "LegalNoticeText" registry values where the
message set contains keywords often used in ransomware ransom messages
Rule ID

windows_registry_set_1
Query
{'selection': {'TargetObject|contains': ['\\SOFTWARE\\Microsoft\\Windows\\CurrentVers
ion\\Policies\\System\\LegalNoticeCaption', '\\SOFTWARE\\Microsoft\\Windows\\CurrentV
ersion\\Policies\\System\\LegalNoticeText']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring registry events
Rule Source
SigmaHQ,8b9606c9-28be-4a38-b146-0e313cc232c1
Author: frack113
Tactics, Techniques, and Procedures
TA0040 , T1491.001 
References
https://github.com/redcanaryco/atomic-red-
team/blob/5c1e6f1b4fafd01c8d1ece85f510160fc1275fbf/atomics/T1491.001/T1491.001.
md 
Severity
75
Suppression Logic Based On
computer_name
event_data.TargetObject
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/11 high Unknown
Rule Details: Potential Persistence Via Microsoft office Add-in
Detect potential persistence via the creation of a Microsoft office add-in file to make it run
automatically.
Rule ID
windows_registry_set_2
Query
{'selection1': {'TargetObject|contains': ['\\Software\\Microsoft\\Office\\']}, 'selec
tion2': {'TargetObject|contains': ['\\Excel\\Options\\OPEN'], 'Details|startswith': '
/R ', 'Details|endswith': '.xll'}, 'selection3': {'TargetObject|contains|all': ['\\Po

werPoint\\AddIns', '\\Path'], 'Details|endswith': '.ppam'}, 'condition': 'selection1
and (selection2 or selection3)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Monitoring registry events
Rule Source
SigmaHQ,961e33d1-4f86-4fcf-80ab-930a708b2f82
Author: frack113
Tactics, Techniques, and Procedures
TA0003 , T1137.006 
References
https://github.com/redcanaryco/atomic-red-
team/blob/4ae9580a1a8772db87a1b6cdb0d03e5af231e966/atomics/T1137.006/T1137.
006.md 
https://labs.withsecure.com/publications/add-in-opportunities-for-office-persistence 
Severity
75
Suppression Logic Based On
computer_name
event_data.TargetObject
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2023/01/15 high Unknown
Windows Security Rule IDs
Rule Details: Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - Security
Detects Obfuscated Powershell via VAR++ LAUNCHER.
Rule ID
windows_security_1
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['&&set', 'cmd', '/c'
, '-
f'], 'ServiceFileName|contains': ['{0}', '{1}', '{2}', '{3}', '{4}', '{5}']}, 'condit
ion': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,4c54ba8f-73d2-4d40-8890-d9cf1dca3d30
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/13 high Unknown
Rule Details: SysKey Registry Keys Access
Detects handle requests and access operations to specific registry keys to calculate the SysKey.
Rule ID
windows_security_2
Query
{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key', 'ObjectName|endswith': [
'\\Lsa\\JD', '\\Lsa\\GBG', '\\Lsa\\Skew1', '\\Lsa\\Data']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,9a4ff3b8-6187-4fd2-8e8b-e0eae1129495
Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures
TA0007 , T1012 
References
https://threathunterplaybook.com/hunts/windows/190625-
RegKeyAccessSyskey/notebook.html 
Severity
75
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/12 high Unknown
Rule Details: ETW Logging Disabled In .NET Processes - Registry
Potential adversaries stopping ETW providers recording loaded .NET assemblies.
Rule ID
windows_security_3
Query
{'selection_etw_enabled': {'EventID': 4657, 'ObjectName|endswith': '\\SOFTWARE\\Micro
soft\\.NETFramework', 'ObjectValueName': 'ETWEnabled', 'NewValue': '0'}, 'selection_c
omplus': {'EventID': 4657, 'ObjectName|contains': '\\Environment', 'ObjectValueName':
['COMPlus_ETWEnabled', 'COMPlus_ETWFlags'], 'NewValue': '0'}, 'condition': '1 of sel
ection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,a4c90ea1-2634-4ca0-adbb-35eae169b6fc
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0005 , T1112 , T1562 
References
https://twitter.com/_xpn_/status/1268712093928378368 

https://github.com/dotnet/runtime/blob/ee2355c801d892f2894b0f7b14a20e6cc50e0e54/
docs/design/coreclr/jit/viewing-jit-dumps.md#setting-configuration-variables 
https://github.com/dotnet/runtime/blob/f62e93416a1799aecc6b0947adad55a0d9870732
/src/coreclr/src/inc/clrconfigvalues.h#L35-L38 
https://github.com/dotnet/runtime/blob/7abe42dc1123722ed385218268bb9fe04556e3d3
/src/coreclr/src/inc/clrconfig.h#L33-L39 
http://managed670.rssing.com/chan-5590147/all_p1.html 
https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227d30e723/d
ocs/coding-guidelines/clr-jit-coding-conventions.md#1412-disabling-code 
https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-No-Vici-
Attacks-On-ETW-Blind-EDRs.pdf 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/06/05 high Unknown
Rule Details: NetNTLM Downgrade Attack
Detects NetNTLM downgrade attack.
Rule ID
windows_security_4
Query
{'selection': {'EventID': 4657, 'ObjectName|contains|all': ['\\REGISTRY\\MACHINE\\SYS
TEM', 'ControlSet', '\\Control\\Lsa'], 'ObjectValueName': ['LmCompatibilityLevel', 'N
tlmMinClientSec', 'RestrictSendingNTLMTraffic']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: Audit Policy : Object Access > Audit Registry (Success)
Rule Source
SigmaHQ,d3abac66-f11c-4ed0-8acb-50cc29c97eed
Author: Florian Roth (Nextron Systems), wagga

Tactics, Techniques, and Procedures
TA0005 , T1562.001 , T1112 
References
https://www.optiv.com/blog/post-exploitation-using-netntlm-downgrade-attacks 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/20 high Unknown
Rule Details: Windows Defender Discarded Signature
Dynamic Signature Service signature of Windows Defender has been discarded. This may be
due to an attacker or a user disabling a security feature that can led the computer exposed to
malware and other threats.
Rule ID
windows_security_5
Query
{'selection2': {'EventID': 2013}, 'condition': 'selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.006 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: PetitPotam Suspicious Kerberos TGT Request
Detect suspicious Kerberos TGT requests. Once an attacer obtains a computer certificate by
abusing Active Directory Certificate Services in combination with PetitPotam, the next step would
be to leverage the certificate for malicious purposes. One way of doing this is to request a
Kerberos Ticket Granting Ticket using a tool like Rubeus. This request will generate a 4768 event
with some unusual fields depending on the environment. This analytic will require tuning, we
recommend filtering Account_Name to the Domain Controller computer accounts.
Rule ID
windows_security_7
Query
{'selection': {'EventID': 4768, 'TargetUserName|endswith': '$', 'CertThumbprint|conta
ins': '*'}, 'filter_local': {'IpAddress': '::1'}, 'filter_thumbprint': {'CertThumbpri
nt': ''}, 'condition': 'selection and not 1 of filter_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Account Logon > Kerberos Authentication Service"
must be configured for Success/Failure
Rule Source
SigmaHQ,6a53d871-682d-40b6-83e0-b7c1a6c4e3a5
Author: Mauricio Velazco, Michael Haag
Tactics, Techniques, and Procedures
TA0006 , T1187 
References
https://github.com/topotam/PetitPotam 
https://isc.sans.edu/forums/diary/Active+Directory+Certificate+Services+ADCS+PKI+do
main+admin+vulnerability/27668/ 
https://github.com/splunk/security_content/blob/develop/detections/endpoint/petitpotam
_suspicious_kerberos_tgt_request.yml 
Severity
75
Suppression Logic Based On
event_id

computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2021/09/ high False positives are possible if the environment is using certificates for authentication. We
recommend filtering Account_Name to the Domain Controller computer accounts.
ental 02
Rule Details: Malicious Service Installations
Detects known malicious service installs that only appear in cases of lateral movement,
credential dumping, and other suspicious activities.
Rule ID
windows_security_8
Query
{'selection': {'EventID': 4697}, 'malsvc_apt29': {'ServiceName': 'javamtsup'}, 'condi
tion': 'selection and 1 of malsvc_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,cb062102-587e-4414-8efa-dbe3c7bf19c6
Author: Florian Roth (Nextron Systems), Daniil Yugoslavskiy, oscd.community (update)
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , TA0003 , T1543.003 , TA0006 , T1003 
References
https://awakesecurity.com/blog/threat-hunting-for-paexec/ 
https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html 
https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/27 critical Unknown
Rule Details: Invoke-Obfuscation Via Use MSHTA - Security
Detects Obfuscated Powershell via use MSHTA in Scripts.
Rule ID
windows_security_10
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['mshta', 'vbscript:c
reateobject', '.run', 'window.close']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,9b8d9203-4e0f-4cd9-bb06-4cc4ea6d0e9a
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high Unknown
Rule Details: Potential LSASS Clone Creation via PssCaptureSnapShot
Identifies the creation of an LSASS process clone via PssCaptureSnapShot where the parent
process is the initial LSASS process instance. This may indicate an attempt to evade detection
and dump LSASS memory for credential access.

Rule ID
windows_security_11
Query
{'selection1': {'Image': '?:\\Windows\\System32\\lsass.exe'}, 'selection2': {'ParentI
mage': '?:\\Windows\\System32\\lsass.exe'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A
Severity
75
Suppression Logic Based On
computer_name
process_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/11/27 high N/A
Rule Details: Suspicious LDAP-Attributes Used
Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange
via LDAP by the tool LDAPFragger and are additionally not commonly used in companies.
Rule ID
windows_security_12
Query
{'selection': {'EventID': 5136, 'AttributeValue|contains': '*', 'AttributeLDAPDisplay
Name': ['primaryInternationalISDNNumber', 'otherFacsimileTelephoneNumber', 'primaryTe
lexNumber']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events

The "Audit Directory Service Changes" logging policy must be configured in order to
receive events. Audit events are generated only for objects with configured system
access control lists (SACLs). Audit events are generated only for objects with
configured system access control lists (SACLs) and only when accessed in a manner
that matches their SACL settings. This policy covers the following events ids - 5136,
5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For
that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
Rule Source
SigmaHQ,d00a9a72-2c09-4459-ad03-5e0a23351e36
Author: xknow @xknow_infosec
Tactics, Techniques, and Procedures
TA0011 , T1001.003 
References
https://medium.com/@ivecodoe/detecting-ldapfragger-a-newly-released-cobalt-strike-
beacon-using-ldap-for-c2-communication-c274a7f00961 
https://blog.fox-it.com/2020/03/19/ldapfragger-command-and-control-over-ldap-
attributes/ 
https://github.com/fox-it/LDAPFragger 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/03/24 high Companies, who may use these default LDAP-Attributes for personal information
Rule Details: Service Installed By Unusual Client - Security
Detects a service installed by a client which has PID 0 or whose parent has PID 0.
Rule ID
windows_security_13
Query
{'selection': {'EventID': 4697}, 'selection_pid': [{'ClientProcessId': 0}, {'ParentPr
ocessId': 0}], 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,c4e92a97-a9ff-4392-9d2d-7a4c642768ca
Author: Tim Rauch (Nextron Systems), Elastic (idea)
Tactics, Techniques, and Procedures
TA0003 , T1543 
References
https://www.elastic.co/guide/en/security/current/windows-service-installed-via-an-
unusual-client.html 
https://twitter.com/SBousseaden/status/1490608838701166596 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/15 high Unknown
Rule Details: User account exposed to Kerberoasting
Detects when a user account has the servicePrincipalName attribute modified. Attackers can
abuse write privileges over a user to configure Service Principle Names (SPNs) so that they can
perform Kerberoasting. Administrators can also configure this for legitimate purposes, exposing
the account to Kerberoasting.
Rule ID
windows_security_15
Query
{'selection1': {'EventID': 5136}, 'selection2': {'ObjectClass': 'user'}, 'selection3'
: {'AttributeLDAPDisplayName': 'servicePrincipalName'}, 'condition': 'selection1 and
selection2 and selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1558 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/02/22 high N/A
Rule Details: Register new Logon Process by Rubeus
Detects potential use of Rubeus via registered new trusted logon process.
Rule ID
windows_security_16
Query
{'selection': {'EventID': 4611, 'LogonProcessName': 'User32LogonProcesss'}, 'conditio
n': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,12e6d621-194f-4f59-90cc-1959e21e69f7
Author: Roberto Rodriguez (source), Ilyas Ochkov (rule), oscd.community
Tactics, Techniques, and Procedures
TA0006 , T1558.003 
References
https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-
trusts-71f2b33688e1 
Severity
75

Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Unknown
Rule Details: DPAPI Domain Master Key Backup Attempt
Detects anyone attempting a backup for the DPAPI Master Key. This events gets generated at
the source and not the Domain Controller.
Rule ID
windows_security_18
Query
{'selection': {'EventID': 4692}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,39a94fd1-8c9a-4ff6-bf22-c058762f8014
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0006 , T1003.004 
References
https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019/08/1 medium If a computer is a member of a domain, DPAPI has a backup mechanism to allow
unprotection of the data. Which will trigger this event.
0

Rule Details: Sysmon Channel Reference Deletion
Potential threat actor tampering with Sysmon manifest and eventually disabling it
Rule ID
windows_security_19
Query
{'selection1': {'EventID': 4657, 'ObjectName|contains': ['WINEVT\\Publishers\\
{5770385f-c22a-43e0-bf4c-06f5698ffbd9}', 'WINEVT\\Channels\\Microsoft-Windows-
Sysmon/Operational'], 'ObjectValueName': 'Enabled', 'NewValue': '0'}, 'selection2': {
'EventID': 4663, 'ObjectName|contains': ['WINEVT\\Publishers\\{5770385f-c22a-43e0-
bf4c-06f5698ffbd9}', 'WINEVT\\Channels\\Microsoft-Windows-
Sysmon/Operational'], 'AccessMask': '0x10000'}, 'condition': '1 of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,18beca67-ab3e-4ee3-ba7a-a46ca8d7d0cc
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0005 , T1112 
References
https://twitter.com/Flangvik/status/1283054508084473861 
https://twitter.com/SecurityJosh/status/1283027365770276866 
https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html 
https://gist.github.com/Cyb3rWard0g/cf08c38c61f7e46e8404b38201ca01c8 
Severity
75
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/07/14 high Unknown
Rule Details: Scanner PoC for CVE-2019-0708 RDP RCE Vuln

Detects the use of a scanner by zerosum0x0 that discovers targets vulnerable to CVE-2019-
0708 RDP RCE aka BlueKeep.
Rule ID
windows_security_21
Query
{'selection': {'EventID': 4625, 'TargetUserName': 'AAAAAAA'}, 'condition': 'selection
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,8400629e-79a9-4737-b387-5db940ab2367
Author: Florian Roth (Nextron Systems), Adam Bradbury (idea)
Tactics, Techniques, and Procedures
TA0008 , T1210 
References
https://twitter.com/AdamTheAnalyst/status/1134394070045003776 
https://github.com/zerosum0x0/CVE-2019-0708 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/06/02 high Unlikely
Rule Details: Suspicious Scheduled Task Update
Detects update to a scheduled task event that contain suspicious keywords.
Rule ID
windows_security_23
Query
{'selection_eid': {'EventID': 4702}, 'selection_paths': {'TaskContentNew|contains': [
'\\AppData\\Local\\Temp\\', '\\AppData\\Roaming\\', '\\Users\\Public\\', '\\WINDOWS\\

Temp\\', 'C:\\Temp\\', '\\Desktop\\', '\\Downloads\\', '\\Temporary Internet', 'C:\\P
rogramData\\', 'C:\\Perflogs\\']}, 'selection_commands': {'TaskContentNew|contains':
['regsvr32', 'rundll32', 'cmd.exe</Command>', 'cmd</Command>', '<Arguments>/c ', '<Ar
guments>/k ', '<Arguments>/r ', 'powershell', 'pwsh', 'mshta', 'wscript', 'cscript',
'certutil', 'bitsadmin', 'bash.exe', 'bash ', 'scrcons', 'wmic ', 'wmic.exe', 'forfil
es', 'scriptrunner', 'hh.exe']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access Events
has to be configured to allow this detection. We also recommend extracting the
Command field from the embedded XML in the event data.
Rule Source
SigmaHQ,614cf376-6651-47c4-9dcc-6b9527f749f4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4698 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high Unknown
Rule Details: Suspicious Teams Application Related ObjectAcess Event
Detects an access to authentication tokens and accounts of Microsoft Teams desktop
application.
Rule ID
windows_security_24
Query

{'selection': {'EventID': 4663, 'ObjectName|contains': ['\\Microsoft\\Teams\\Cookies'
, '\\Microsoft\\Teams\\Local Storage\\leveldb']}, 'filter': {'ProcessName|contains':
'\\Microsoft\\Teams\\current\\Teams.exe'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,25cde13e-8e20-4c29-b949-4e795b76f16f
Author: @SerkinValery
Tactics, Techniques, and Procedures
TA0006 , T1528 
References
https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-
as-cleartext-in-windows-linux-macs/ 
https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-
tokens 
Severity
75
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/09/16 high Unknown
Rule Details: Meterpreter or Cobalt Strike Getsystem Service Installation - Security
Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting a specific service
installation.
Rule ID
windows_security_26
Query
{'selection_id': {'EventID': 4697}, 'selection': [{'ServiceFileName|contains|all': ['
cmd', '/c', 'echo', '\\pipe\\']}, {'ServiceFileName|contains|all': ['%COMSPEC%', '/c'
, 'echo', '\\pipe\\']}, {'ServiceFileName|contains|all': ['cmd.exe', '/c', 'echo', '\
\pipe\\']}, {'ServiceFileName|contains|all': ['rundll32', '.dll,a', '/p:']}], 'condit
ion': 'selection_id and selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,ecbc5e16-58e0-4521-9c60-eb9a7ea4ad34
Author: Teymur Kheirkhabarov, Ecco, Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1134 
References
https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-
environment 
https://blog.cobaltstrike.com/2014/04/02/what-happens-when-i-type-getsystem/ 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/26 critical Highly unlikely
Rule Details: Powerview Add-DomainObjectAcl DCSync AD Extend Right
Backdooring domain object to grant the rights associated with DCSync to a regular user or
machine account using Powerview\Add-DomainObjectAcl DCSync Extended Right cmdlet, will
allow to re-obtain the pwd hashes of any user/computer.
Rule ID
windows_security_27
Query
{'selection': {'EventID': 5136, 'AttributeLDAPDisplayName': 'ntSecurityDescriptor', '
AttributeValue|contains': ['1131f6ad-9c07-11d1-f79f-00c04fc2dcd2', '1131f6aa-9c07-
11d1-f79f-00c04fc2dcd2', '89e95b76-444d-4c62-991a-
0facbeda640c']}, 'filter1': {'ObjectClass': ['dnsNode', 'dnsZoneScope', 'dnsZone']},
'condition': 'selection and not 1 of filter*'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The "Audit Directory Service Changes" logging policy must be configured in order to
receive events. Audit events are generated only for objects with configured system
access control lists (SACLs). Audit events are generated only for objects with
configured system access control lists (SACLs) and only when accessed in a manner
that matches their SACL settings. This policy covers the following events ids - 5136,
5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For
that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
Rule Source
SigmaHQ,2c99737c-585d-4431-b61a-c911d86ff32f
Author: Samir Bousseaden, Roberto Rodriguez @Cyb3rWard0g, oscd.community, Tim Shelton,
Maxence Fossat
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://twitter.com/menasec1/status/1111556090137903104 
https://www.specterops.io/assets/resources/an_ace_up_the_sleeve.pdf 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2019/04/ high New Domain Controller computer account, check user SIDs within the value attribute of
event 5136 and verify if it's a regular user or DC computer account.
ental 03
Rule Details: Windows Defender Disabled
Windows Defender Real-time Protection scanning for malware and other potentially unwanted
software was disabled.
Rule ID
windows_security_28
Query
{'selection2': {'EventID': 5001}, 'condition': 'selection2'}

Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: ADCS Certificate Template Configuration Vulnerability
Detects certificate creation with template allowing risk permission subject.
Rule ID
windows_security_29
Query
{'selection1': {'EventID': 4898, 'TemplateContent|contains': 'CT_FLAG_ENROLLEE_SUPPLI
ES_SUBJECT'}, 'selection2': {'EventID': 4899, 'NewTemplateContent|contains': 'CT_FLAG
_ENROLLEE_SUPPLIES_SUBJECT'}, 'condition': 'selection1 or selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Certificate services loaded a template would trigger event ID 4898 and certificate
Services template was updated would trigger event ID 4899. A risk permission seems to
be coming if template contain specific flag.
Rule Source
SigmaHQ,5ee3a654-372f-11ec-8d3d-0242ac130003
Author: Orlinum , BlueDefenZer
Tactics, Techniques, and Procedures

TA0004 , T1068 
References
https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf 
Severity
25
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/17 low Administrator activity
Proxy SSL certificate with subject modification
Smart card enrollement
Rule Details: Security-Enabled Local Group was Deleted
A Security-Enabled Local Group has been deleted. This could be an indication of malicious
activity.
Rule ID
windows_security_31
Query
{'selection1': {'EventID': 4734}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id

computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Invoke-Obfuscation RUNDLL LAUNCHER - Security
Detects Obfuscated Powershell via RUNDLL LAUNCHER.
Rule ID
windows_security_32
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['rundll32.exe', 'she
ll32.dll', 'shellexec_rundll', 'powershell']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,f241cf1b-3a6b-4e1a-b4f9-133c00dd95ca
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium Unknown
Rule Details: Invoke-Obfuscation Via Use Rundll32 - Security

Detects Obfuscated Powershell via use Rundll32 in Scripts.
Rule ID
windows_security_33
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['&&', 'rundll32', 's
hell32.dll', 'shellexec_rundll'], 'ServiceFileName|contains': ['value', 'invoke', 'co
mspec', 'iex']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,cd0f7229-d16f-42de-8fe3-fba365fbcb3a
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high Unknown
Rule Details: DPAPI Domain Backup Key Extraction
Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers.
Rule ID
windows_security_37
Query

{'selection': {'EventID': 4662, 'ObjectType': 'SecretObject', 'AccessMask': '0x2', 'O
bjectName|contains': 'BCKUPKEY'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,4ac1f50b-3bd0-4968-902d-868b4647937e
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0006 , T1003.004 
References
https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/06/20 high Unknown
Rule Details: Addition of Domain Trusts
Addition of domains is seldom and should be verified for legitimacy.
Rule ID
windows_security_38
Query
{'selection': {'EventID': 4706}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,0255a820-e564-4e40-af2b-6ac61160335c
Author: Thomas Patzke

Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2019/12/03 medium Legitimate extension of domain structure
Rule Details: User Added to Local Administrators
This rule triggers on user accounts that are added to the local Administrators group, which could
be legitimate activity or a sign of privilege escalation activity.
Rule ID
windows_security_40
Query
{'selection': {'EventID': 4732}, 'selection_group1': {'TargetUserName|startswith': 'A
dministr'}, 'selection_group2': {'TargetSid': 'S-1-5-32-
544'}, 'filter': {'SubjectUserName|endswith': '$'}, 'condition': 'selection and (1 of
selection_group*) and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,c265cf08-3f99-46c1-8d59-328247057d57
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1078 , T1098 
References
N/A
Severity
50

Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2017/03/14 medium Legitimate administrative activity
Rule Details: Sensitive Privilege SeEnableDelegationPrivilege assigned to a User
Identifies the assignment of the SeEnableDelegationPrivilege sensitive "user right" to a user. The
SeEnableDelegationPrivilege "user right" enables computer and user accounts to be trusted for
delegation. Attackers can abuse this right to compromise Active Directory accounts and elevate
their privileges.
Rule ID
windows_security_41
Query
{'selection1': {'EventID': 4704}, 'selection2': {'PrivilegeList': 'SeEnableDelegation
Privilege'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/01/27 high N/A
Rule Details: Suspicious Computer Account Name Change CVE-2021-42287

Detects the renaming of an existing computer account to a account name that doesn't contain a
$ symbol as seen in attacks against CVE-2021-42287.
Rule ID
windows_security_44
Query
{'selection': {'EventID': 4781, 'OldTargetUserName|contains': '$'}, 'filter': {'NewTa
rgetUserName|contains': '$'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,45eb2ae2-9aa2-4c3a-99a5-6e5077655466
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1078 
References
https://medium.com/@mvelazco/hunting-for-samaccountname-spoofing-cve-2021-
42287-and-domain-controller-impersonation-f704513c8a45 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/12/22 high Unknown
Rule Details: Suspicious Remote Logon with Explicit Credentials
Detects suspicious processes logging on with explicit credentials.
Rule ID
windows_security_45
Query
{'selection': {'EventID': 4648, 'ProcessName|endswith': ['\\cmd.exe', '\\powershell.e
xe', '\\pwsh.exe', '\\winrs.exe', '\\wmic.exe', '\\net.exe', '\\net1.exe', '\\reg.exe
']}, 'filter1': {'TargetServerName': 'localhost'}, 'filter2': {'SubjectUserName|endsw

ith': '$', 'TargetUserName|endswith': '$'}, 'condition': 'selection and not 1 of filt
er*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,941e5c45-cda7-4864-8cea-bbb7458d194a
Author: oscd.community, Teymur Kheirkhabarov @HeirhabarovT, Zach Stanford @svch0st, Tim
Shelton
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/05 medium Administrators that use the RunAS command or scheduled tasks
Rule Details: The Password Hash of an Account was Accessed
The Password Hash of an Account was Accessed. This could be an indication of malicious
activity.
Rule ID
windows_security_46
Query
{'selection1': {'EventID': 4782}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0006 , T1003 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Processes Accessing the Microphone and Webcam
Potential adversaries accessing the microphone and webcam in an endpoint.
Rule ID
windows_security_48
Query
{'selection': {'EventID': [4657, 4656, 4663], 'ObjectName|contains': ['\\SOFTWARE\\Mi
crosoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\microphone\\
NonPackaged', '\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManage
r\\ConsentStore\\webcam\\NonPackaged']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,8cd538a4-62d5-4e83-810b-12d41e428d6e
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0009 , T1123 
References
https://twitter.com/duzvik/status/1269671601852813320 
https://medium.com/@7a616368/can-you-track-processes-accessing-the-camera-and-
microphone-7e6885b37072 
Severity
50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/06/07 medium Unknown
Rule Details: Defrag Deactivation - Security
Detects the deactivation and disabling of the Scheduled defragmentation task as seen by
Slingshot APT group.
Rule ID
windows_security_49
Query
{'selection': {'EventID': 4701, 'TaskName': '\\Microsoft\\Windows\\Defrag\\ScheduledD
efrag'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: Audit Policy : Audit Other Object Access Events > Success
Rule Source
SigmaHQ,c5a178bf-9cfb-4340-b584-e4df39b6a3e7
Author: Florian Roth (Nextron Systems), Bartlomiej Czyz (@bczyz1)
Tactics, Techniques, and Procedures
TA0003 , T1053 
References
https://securelist.com/apt-slingshot/84312/ 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/03/04 medium Unknown

Rule Details: Invoke-Obfuscation STDIN+ Launcher - Security
Detects Obfuscated use of stdin to execute PowerShell.
Rule ID
windows_security_50
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['cmd', 'powershell']
}, 'selection2': {'ServiceFileName|contains': ['${input}', 'noexit']}, 'selection3':
{'ServiceFileName|contains': [' /c ', ' /r ']}, 'condition': 'all of selection*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,0c718a5e-4284-4fb9-b4d9-b9a50b3a1974
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high Unknown
Rule Details: Invoke-Obfuscation Via Stdin - Security
Detects Obfuscated Powershell via Stdin in Scripts.
Rule ID
windows_security_53
Query

{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['set', '&&'], 'Servi
ceFileName|contains': ['environment', 'invoke', '${input)']}, 'condition': 'selection
'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,80b708f3-d034-40e4-a6c8-d23b7a7db3d1
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/12 high Unknown
Rule Details: Microsoft Entra Health Service Agents Registry Keys Access
This detection uses Windows security events to detect suspicious access attempts to the registry
key values and sub-keys of Microsoft Entra Health service agents (e.g AD FS). Information from
AD Health service agents can be used to potentially abuse some of the features provided by
those services in the cloud (e.g. Federation). This detection requires an access control entry
(ACE) on the system access control list (SACL) of the following securable object:
HKLM:\SOFTWARE\Microsoft\ADHealthAgent. Make sure you set the SACL to propagate to its
sub-keys.
Rule ID
windows_security_54
Query

{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key', 'ObjectName': '\\REGISTR
Y\\MACHINE\\SOFTWARE\\Microsoft\\ADHealthAgent'}, 'filter': {'ProcessName|contains':
['Microsoft.Identity.Health.Adfs.DiagnosticsAgent.exe', 'Microsoft.Identity.Health.Ad
fs.InsightsService.exe', 'Microsoft.Identity.Health.Adfs.MonitoringAgent.Startup.exe'
, 'Microsoft.Identity.Health.Adfs.PshSurrogate.exe', 'Microsoft.Identity.Health.Commo
n.Clients.ResourceMonitor.exe']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,1d2ab8ac-1a01-423b-9c39-001510eae8e8
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
Tactics, Techniques, and Procedures
TA0007 , T1012 
References
https://o365blog.com/post/hybridhealthagent/ 
https://github.com/OTRF/Set-
AuditRule/blob/c3dec5443414231714d850565d364ca73475ade5/rules/registry/aad_co
nnect_health_service_agent.yml 
Severity
50
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/26 medium Unknown
Rule Details: Invoke-Obfuscation CLIP+ Launcher - Security
Detects Obfuscated use of Clip.exe to execute PowerShell.
Rule ID
windows_security_55
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['cmd', '&&', 'clipbo
ard]::']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,4edf51e1-cb83-4e1a-bc39-800e396068e3
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/13 high Unknown
Rule Details: Password Protected ZIP File Opened (Email Attachment)
Detects the extraction of password protected ZIP archives. See the filename variable for more
details on which file has been opened.
Rule ID
windows_security_59
Query
{'selection': {'EventID': 5379, 'TargetName|contains|all': ['Microsoft_Windows_Shell_
ZipFolder:filename', '\\Temporary Internet Files\\Content.Outlook']}, 'condition': 's
election'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,571498c8-908e-40b4-910b-d2369159a3da
Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures
TA0006 , T1212 
References
https://twitter.com/sbousseaden/status/1523383197513379841 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/09 high Legitimate used of encrypted ZIP files
Rule Details: WMI Persistence - Security
Detects suspicious WMI event filter and command line event consumer based on WMI and
Security Logs.
Rule ID
windows_security_60
Query
{'selection': {'EventID': 4662, 'ObjectType': 'WMI Namespace', 'ObjectName|contains':
'subscription'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,f033f3f3-fd24-4995-97d8-a3bb17550a88
Author: Florian Roth (Nextron Systems), Gleb Sukhodolskiy, Timur Zinniatullin oscd.community
Tactics, Techniques, and Procedures
TA0003 , T1546.003 
References
https://twitter.com/mattifestation/status/899646620148539397 
https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/ 
Severity
50

Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/08/22 medium Unknown (data set is too small; further testing needed)
Rule Details: Metasploit Or Impacket Service Installation Via SMB PsExec
Detects usage of Metasploit SMB PsExec (exploit/windows/smb/psexec) and Impacket
psexec.py by triggering on specific service installation.
Rule ID
windows_security_61
Query
{'selection': {'EventID': 4697, 'ServiceFileName|re': '^%systemroot%\\\\[a-zA-Z]
{8}\\.exe$', 'ServiceName|re': '(^[a-zA-Z]{4}$)|(^[a-zA-Z]{8}$)|(^[a-zA-Z]
{16}$)', 'ServiceStartType': '3', 'ServiceType': '0x10'}, 'filter': {'ServiceName': '
PSEXESVC'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,6fb63b40-e02a-403e-9ffd-3bcc1d749442
Author: Bartlomiej Czyz, Relativity
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , TA0008 , T1021.002 , T1570 
References
https://bczyz1.github.io/2021/01/30/psexec.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Maturity Creation Risk False Positives
Date Level
experiment 2021/01/21 high Possible, different agents with a 8 character binary and a 4, 8 or 16 character
service name
al
Rule Details: AD Privileged Users or Groups Reconnaissance
Detect priv users or groups recon based on 4661 eventid and known privileged users or groups
SIDs.
Rule ID
windows_security_62
Query
{'selection': {'EventID': 4661, 'ObjectType': ['SAM_USER', 'SAM_GROUP']}, 'selection_
object': [{'ObjectName|endswith': ['-512', '-502', '-500', '-505', '-519', '-520', '-
544', '-551', '-555']}, {'ObjectName|contains': 'admin'}], 'filter': {'SubjectUserNam
e|endswith': '$'}, 'condition': 'selection and selection_object and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: enable Object Access SAM on your Domain Controllers
Rule Source
SigmaHQ,35ba1d85-724d-42a3-889f-2e2362bcaf23
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0007 , T1087.002 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/04/03 high If source account name is not an admin then its super suspicious
Rule Details: Password Protected ZIP File Opened (Suspicious Filenames)

Detects the extraction of password protected ZIP archives with suspicious file names. See the
filename variable for more details on which file has been opened.
Rule ID
windows_security_63
Query
{'selection': {'EventID': 5379, 'TargetName|contains': 'Microsoft_Windows_Shell_ZipFo
lder:filename'}, 'selection_filename': {'TargetName|contains': ['invoice', 'new order
', 'rechnung', 'factura', 'delivery', 'purchase', 'order', 'payment']}, 'condition':
'selection and selection_filename'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,54f0434b-726f-48a1-b2aa-067df14516e4
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
https://twitter.com/sbousseaden/status/1523383197513379841 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/05/09 high Legitimate used of encrypted ZIP files
Rule Details: Microsoft Entra Health Monitoring Agent Registry Keys Access
This detection uses Windows security events to detect suspicious access attempts to the registry
key of Microsoft Entra Health monitoring agent. This detection requires an access control entry
(ACE) on the system access control list (SACL) of the following securable object
HKLM\SOFTWARE\Microsoft\Microsoft Online\Reporting\MonitoringAgent.
Rule ID
windows_security_70

Query
{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key', 'ObjectName': '\\REGISTR
Y\\MACHINE\\SOFTWARE\\Microsoft\\Microsoft Online\\Reporting\\MonitoringAgent'}, 'fil
ter': {'ProcessName|contains': ['Microsoft.Identity.Health.Adfs.DiagnosticsAgent.exe'
, 'Microsoft.Identity.Health.Adfs.InsightsService.exe', 'Microsoft.Identity.Health.Ad
fs.MonitoringAgent.Startup.exe', 'Microsoft.Identity.Health.Adfs.PshSurrogate.exe', '
Microsoft.Identity.Health.Common.Clients.ResourceMonitor.exe']}, 'condition': 'select
ion and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,ff151c33-45fa-475d-af4f-c2f93571f4fe
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
Tactics, Techniques, and Procedures
TA0007 , T1012 
References
https://o365blog.com/post/hybridhealthagent/ 
https://github.com/OTRF/Set-
AuditRule/blob/c3dec5443414231714d850565d364ca73475ade5/rules/registry/aad_co
nnect_health_monitoring_agent.yml 
Severity
50
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/08/26 medium Unknown
Rule Details: Invoke-Obfuscation Obfuscated IEX Invocation - Security
Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-
Obfuscation framework from the code block linked in the references.
Rule ID
windows_security_71
Query

{'selection_eid': {'EventID': 4697}, 'selection_servicefilename': [{'ServiceFileName|
re': '\\$PSHome\\[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$PSHome\\
['}, {'ServiceFileName|re': '\\$ShellId\\[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$ShellId\\
['}, {'ServiceFileName|re': '\\$env:Public\\
[\\s*\\d{1,3}\\s*\\]\\s*\\+\\s*\\$env:Public\\
['}, {'ServiceFileName|re': '\\$env:ComSpec\\[(\\s*\\d{1,3}\\s*,)
{2}'}, {'ServiceFileName|re': '\\\\*mdr*\\W\\s*\\)\\.Name'}, {'ServiceFileName|re': '
\\$VerbosePreference\\.ToString\\
('}, {'ServiceFileName|re': '\\String\\]\\s*\\$VerbosePreference'}], 'condition': 'al
l of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,fd0f5778-d3cb-4c9a-9695-66759d04702a
Author: Daniel Bohannon (@Mandiant/@FireEye), oscd.community
Tactics, Techniques, and Procedures
TA0005 , T1027 
References
https://github.com/danielbohannon/Invoke-
Obfuscation/blob/f20e7f843edd0a3a7716736e9eddfa423395dd26/Out-
ObfuscatedStringCommand.ps1#L873-L888 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/11/08 high Unknown
Rule Details: Possible Shadow Credentials Added
Detects possible addition of shadow credentials to an active directory object.
Rule ID
windows_security_72

Query
{'selection': {'EventID': 5136, 'AttributeLDAPDisplayName': 'msDS-
KeyCredentialLink'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The "Audit Directory Service Changes" logging policy must be configured in order to
receive events. Audit events are generated only for objects with configured system
access control lists (SACLs). Audit events are generated only for objects with
configured system access control lists (SACLs) and only when accessed in a manner
that matches their SACL settings. This policy covers the following events ids - 5136,
5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For
that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
Rule Source
SigmaHQ,f598ea0c-c25a-4f72-a219-50c44411c791
Author: Nasreddine Bencherchali (Nextron Systems), Elastic (idea)
Tactics, Techniques, and Procedures
TA0005 , T1556 
References
https://www.elastic.co/guide/en/security/8.4/potential-shadow-credentials-added-to-ad-
object.html 
https://cyberstoph.org/posts/2022/03/detecting-shadow-credentials/ 
https://twitter.com/SBousseaden/status/1581300963650187264? 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
experim 2022/10/ high Modifications in the msDS-KeyCredentialLink attribute can be done legitimately by the
Microsoft Entra Connect synchronization account or the ADFS service account. These
ental 17
accounts can be added as Exceptions. (From elastic FP section)
Rule Details: Potential Shadow Credentials added to AD Object
Identify the modification of the msDS-KeyCredentialLink attribute in an Active Directory
Computer or User Object. Attackers can abuse control over the object and create a key pair,

append to raw public key in the attribute, and obtain persistent and stealthy access to the target
user or computer object.
Rule ID
windows_security_73
Query
{'selection1': {'EventID': 5136}, 'selection2': {'AttributeLDAPDisplayName': 'msDS-
KeyCredentialLink'}, 'selection3': {'AttributeValue': 'B:828*'}, 'condition': 'select
ion1 and selection2 and selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1556 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturi Creation Risk False Positives
ty Date Level
produc 2022/01/ high Modifications in the msDS-KeyCredentialLink attribute can be done legitimately by the
Microsoft Entra Connect synchronization account or the ADFS service account. These
tion 26 accounts can be added as Exceptions.
Rule Details: Invoke-Obfuscation Via Use Clip - Security
Detects Obfuscated Powershell via use Clip.exe in Scripts.
Rule ID
windows_security_76
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains': '(Clipboard|i'}, 'conditi
on': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,1a0a2ff1-611b-4dac-8216-8a7b47c618a6
Author: Nikita Nazarov, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/09 high Unknown
Rule Details: AD Object WriteDAC Access
Detects WRITE_DAC access to a domain object.
Rule ID
windows_security_77
Query
{'selection': {'EventID': 4662, 'ObjectServer': 'DS', 'AccessMask': '0x40000', 'Objec
tType': ['19195a5b-6da0-11d0-afd3-
00c04fd930c9', 'domainDNS']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,028c7842-4243-41cd-be6f-12f3cf1a26c7
Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures
TA0005 , T1222.001 
References
https://threathunterplaybook.com/hunts/windows/180815-
ADObjectAccessReplication/notebook.html 
https://threathunterplaybook.com/library/windows/active_directory_replication.html 
https://threathunterplaybook.com/hunts/windows/190101-
ADModDirectoryReplication/notebook.html 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/09/12 critical Unknown
Rule Details: Access to a Sensitive LDAP Attribute
Identify access to sensitive Active Directory object attributes that contains credentials and
decryption keys such as unixUserPassword, ms-PKI-AccountCredentials and msPKI-
CredentialRoamingTokens.
Rule ID
windows_security_81
Query
{'selection1': {'EventID': 4662}, 'selection2': {'SubjectUserSid': 'S-1-5-
18'}, 'selection3': {'Properties': ['*612cb747-c0e8-4f92-9221-
fdd5f15b550d*', '*b8dfa744-31dc-4ef1-ac7c-84baf7ef9da7*', '*b3f93023-9239-4f7c-b99c-
6745d87adbc2*', '*b7ff5a38-0818-42b0-8110-
d3d154c97f24*']}, 'selection4': {'AccessMask': ['0x0', '0x100']}, 'condition': 'selec
tion1 and (not selection2) and selection3 and (not selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 

References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/11/09 medium N/A
Rule Details: Security Eventlog Cleared
One of the Windows Eventlogs has been cleared. e.g. caused by "wevtutil cl" command
execution.
Rule ID
windows_security_82
Query
{'selection_517': {'EventID': 517, 'ProviderName': 'Security'}, 'selection_1102': {'E
ventID': 1102, 'ProviderName': 'Microsoft-Windows-
Eventlog'}, 'condition': '1 of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,d99b79d2-0a6f-4f46-ad8b-260b6e17f982
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1070.001 
References
https://twitter.com/deviouspolack/status/832535435960209408 
https://www.hybrid-
analysis.com/sample/027cc450ef5f8c5f653329641ec1fed91f694e0d229928963b30f6b0
d7d3a745?environmentId=100 
Severity
75

Suppression Logic Based On
computer_name
event_id
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2017/01/10 high Rollout of log collection agents (the setup routine often includes a reset of the local
Eventlog)
System provisioning (system reset before the golden image creation)
Rule Details: Operation Wocao Activity - Security
Detects activity mentioned in Operation Wocao report.
Rule ID
windows_security_83
Query
{'selection': {'EventID': 4799, 'TargetUserName|startswith': 'Administr', 'CallerProc
essName|endswith': '\\checkadmin.exe'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,74ad4314-482e-4c3e-b237-3f7ed3b9ca8d
Author: Florian Roth (Nextron Systems), frack113
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0003 , T1053.005 , TA0005 , T1036.004 , T1027 ,
TA0007 , T1012 
References
https://twitter.com/SBousseaden/status/1207671369963646976 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
test 2019/12/20 high Administrators that use checkadmin.exe tool to enumerate local administrators
Rule Details: Kerberos Manipulation
This method triggers on rare Kerberos Failure Codes caused by manipulations of Kerberos
messages.
Rule ID
windows_security_84
Query
{'selection': {'EventID': [675, 4768, 4769, 4771], 'FailureCode': ['0x9', '0xA', '0xB
', '0xF', '0x10', '0x11', '0x13', '0x14', '0x1A', '0x1F', '0x21', '0x22', '0x23', '0x
24', '0x26', '0x27', '0x28', '0x29', '0x2C', '0x2D', '0x2E', '0x2F', '0x31', '0x32',
'0x3E', '0x3F', '0x40', '0x41', '0x43', '0x44']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,f7644214-0eb0-4ace-9455-331ec4c09253
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0006 , T1212 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/02/10 high Faulty legacy applications
Rule Details: Windows Login Default Point Of Sale Credentials
Windows has reported a login from a user with the default username used by a Point of Sale
system. These are well known and are often used as the targets of brute force attacks leading to
unauthorized access of the payment infrastructure.

Rule ID
windows_security_85
Query
{'selection2': {'EventID': 4625}, 'selection3': {'TargetUserName': 'aloha'}, 'selecti
on4': {'TargetUserName': 'micros'}, 'selection5': {'TargetUserName': 'posi'}, 'select
ion7': {'TargetUserName': 'ddpos'}, 'selection8': {'TargetUserName': 'term1'}, 'selec
tion9': {'TargetUserName': 'pos'}, 'selection10': {'TargetUserName': 'pos2'}, 'condit
ion': 'selection2 and (selection3 or selection4 or selection5 or selection7 or select
ion8 or selection9 or selection10)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1110 
References
N/A
Severity
50
Suppression Logic Based On
computer_name
event_id
event_data.TargetUserName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: SCM Database Privileged Operation
Detects non-system users performing privileged operation os the SCM database.
Rule ID
windows_security_86
Query
{'selection': {'EventID': 4674, 'ObjectType': 'SC_MANAGER OBJECT', 'ObjectName': 'ser
vicesactive', 'PrivilegeList': 'SeTakeOwnershipPrivilege'}, 'filter': {'SubjectLogonI
d': '0x3e4', 'ProcessName|endswith': ':\\Windows\\System32\\services.exe'}, 'conditio
n': 'selection and not filter'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,dae8171c-5ec6-4396-b210-8466585b53e9
Author: Roberto Rodriguez @Cyb3rWard0g, Tim Shelton
Tactics, Techniques, and Procedures
TA0005 , T1548 
References
https://threathunterplaybook.com/hunts/windows/190826-
RemoteSCMHandle/notebook.html 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/15 medium Unknown
Rule Details: Security-Enabled Universal Group was Deleted
A Security-Enabled Universal Group has been deleted. This could be an indication of malicious
activity.
Rule ID
windows_security_87
Query
{'selection1': {'EventID': 4758}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures

TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Reconnaissance Activity
Detects activity as "net user administrator /domain" and "net group domain admins /domain".
Rule ID
windows_security_88
Query
{'selection': {'EventID': 4661, 'AccessMask': '0x2d', 'ObjectType': ['SAM_USER', 'SAM
_GROUP'], 'ObjectName|startswith': 'S-1-5-21-
', 'ObjectName|endswith': ['-500', '-512']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The volume of Event ID 4661 is high on Domain Controllers and therefore "Audit SAM"
and "Audit Kernel Object" advanced audit policy settings are not configured in the
recommendations for server systems
Rule Source
SigmaHQ,968eef52-9cff-4454-8992-1e74b9cbad6c
Author: Florian Roth (Nextron Systems), Jack Croock (method), Jonhnathan Ribeiro
(improvements), oscd.community
Tactics, Techniques, and Procedures
TA0007 , T1087.002 , T1069.002 
References
https://findingbad.blogspot.de/2017/01/hunting-what-does-it-look-like.html 
Severity

75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/07 high Administrator activity
Rule Details: Kerberos Policy was Changed
The Kerberos policy was changed. This could be an indication of malicious activity.
Rule ID
windows_security_89
Query
{'selection1': {'EventID': 4713}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Invoke-Obfuscation VAR+ Launcher - Security
Detects Obfuscated use of Environment Variables to execute PowerShell.
Rule ID

windows_security_90
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['cmd', '"set', '-
f'], 'ServiceFileName|contains': ['/c', '/r']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,dcf2db1f-f091-425b-a821-c05875b8925a
Author: Jonathan Cheong, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/15 high Unknown
Rule Details: Hacking Tool detected by Antivirus
The Windows Defender AntiVirus has detected a hacking tool in the system. This is an indication
that an attacker has access to your system and is trying to install tools to gain persistence,
compromise other systems, etc.
Rule ID
windows_security_92
Query
{'selection2': {'EventID': 1116}, 'selection3': {'MalwareFamily|re': '(?:hacktool|met
erpreter|metasploit|powersploit|cobalt|mimikatz|wpdump|htool|wce)'}, 'selection4': {'

FileName': ''}, 'selection5': {'MalwareFamily': ''}, 'condition': 'selection2 and sel
ection3 and not selection4 and not selection5'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0007 , T1518 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: WCE wceaux.dll Access
Detects wceaux.dll access while WCE pass-the-hash remote command execution on source
host.
Rule ID
windows_security_93
Query
{'selection': {'EventID': [4656, 4658, 4660, 4663], 'ObjectName|endswith': '\\wceaux.
dll'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,1de68c67-af5c-4097-9c85-fe5578e09e67
Author: Thomas Patzke
Tactics, Techniques, and Procedures

TA0006 , T1003 
References
https://www.jpcert.or.jp/english/pub/sr/ir_research.html 
https://jpcertcc.github.io/ToolAnalysisResultSheet 
Severity
90
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/06/14 critical Unknown
Rule Details: Important Scheduled Task Deleted/Disabled
Detects when adversaries stop services or processes by deleting or disabling their respective
scheduled tasks in order to conduct data destructive activities.
Rule ID
windows_security_95
Query
{'selection': {'EventID': [4699, 4701], 'TaskName|contains': ['\\Windows\\SystemResto
re\\SR', '\\Windows\\Windows Defender\\', '\\Windows\\BitLocker', '\\Windows\\Windows
Backup\\', '\\Windows\\WindowsUpdate\\', '\\Windows\\UpdateOrchestrator\\Schedule', '
\\Windows\\ExploitGuard']}, 'filter_sys_username': {'EventID': 4699, 'SubjectUserName
|endswith': '$', 'TaskName|contains': '\\Windows\\Windows Defender\\'}, 'condition':
'selection and not 1 of filter_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access Events
has to be configured to allow this detection. We also recommend extracting the
Command field from the embedded XML in the event data.
Rule Source
SigmaHQ,7595ba94-cf3b-4471-aa03-4f6baa9e5fad
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 

References
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4699 
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4701 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high Unknown
Rule Details: Account Tampering - Suspicious Failed Logon Reasons
This method uses uncommon error codes on failed logons to determine suspicious activity and
tampering with accounts that have been disabled or somehow restricted.
Rule ID
windows_security_97
Query
{'selection': {'EventID': [4625, 4776], 'Status': ['0xC0000072', '0xC000006F', '0xC00
00070', '0xC0000413', '0xC000018C', '0xC000015B']}, 'filter': {'SubjectUserSid': 'S-
1-0-0'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,9eb99343-d336-4020-a3cd-67f3819e68ee
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1078 
References
https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4625 
https://twitter.com/SBousseaden/status/1101431884540710913 

Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2017/02/19 medium User using a disabled account
Rule Details: Encrypted Data Recovery Policy was Changed
The Encrypted Data policy was changed. This could be an indication of malicious activity.
Rule ID
windows_security_99
Query
{'selection1': {'EventID': 4714}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Secure Deletion with SDelete
Detects renaming of file while deletion with SDelete tool.

Rule ID
windows_security_101
Query
{'selection': {'EventID': [4656, 4663, 4658], 'ObjectName|endswith': ['.AAA', '.ZZZ']
}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,39a80702-d7ca-4a83-b776-525b1f86a36d
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0005 , T1070.004 , T1027.005 , T1553.002 , TA0040 , T1485 
References
https://jpcertcc.github.io/ToolAnalysisResultSheet/details/sdelete.htm 
https://www.jpcert.or.jp/english/pub/sr/ir_research.html 
https://docs.microsoft.com/en-gb/sysinternals/downloads/sdelete 
Severity
50
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/06/14 medium Legitimate usage of SDelete
Rule Details: Invoke-Obfuscation COMPRESS OBFUSCATION - Security
Detects Obfuscated Powershell via COMPRESS OBFUSCATION.
Rule ID
windows_security_102
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains|all': ['new-
object', 'text.encoding]::ascii', 'readtoend'], 'ServiceFileName|contains': ['system.
io.compression.deflatestream', 'system.io.streamreader']}, 'condition': 'selection'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,7a922f1b-2635-4d6c-91ef-af228b198ad3
Author: Timur Zinniatullin, oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1059.001 , TA0005 , T1027 
References
https://github.com/SigmaHQ/sigma/issues/1009 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2020/10/18 medium Unknown
Rule Details: ADCS Certificate Template Configuration Vulnerability with Risky EKU
Detects certificate creation with template allowing risk permission subject and risky EKU.
Rule ID
windows_security_104
Query
{'selection10': {'EventID': 4898, 'TemplateContent|contains': ['1.3.6.1.5.5.7.3.2', '
1.3.6.1.5.2.3.4', '1.3.6.1.4.1.311.20.2.2', '2.5.29.37.0']}, 'selection11': {'Templat
eContent|contains': 'CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT'}, 'selection20': {'EventID':
4899, 'NewTemplateContent|contains': ['1.3.6.1.5.5.7.3.2', '1.3.6.1.5.2.3.4', '1.3.6.
1.4.1.311.20.2.2', '2.5.29.37.0']}, 'selection21': {'NewTemplateContent|contains': 'C
T_FLAG_ENROLLEE_SUPPLIES_SUBJECT'}, 'condition': '(selection10 and selection11) or (s
election20 and selection21)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events
Certificate services loaded a template would trigger event ID 4898 and certificate
Services template was updated would trigger event ID 4899. A risk permission seems to
be coming if template contain specific flag with risky EKU.
Rule Source
SigmaHQ,bfbd3291-de87-4b7c-88a2-d6a5deb28668
Author: Orlinum , BlueDefenZer
Tactics, Techniques, and Procedures
TA0004 , T1068 
References
https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/11/17 high Administrator activity
Proxy SSL certificate with subject modification
Smart card enrollement
Rule Details: PowerShell Scripts Installed as Services - Security
Detects powershell script installed as a Service.
Rule ID
windows_security_106
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains': ['powershell', 'pwsh']},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source

SigmaHQ,2a926e6a-4b81-4011-8a96-e36cc8c04302
Author: oscd.community, Natalia Shornikova
Tactics, Techniques, and Procedures
TA0002 , T1569.002 
References
https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/06 high Unknown
Rule Details: AdminSDHolder Backdoor
Detects modifications in the AdminSDHolder object. Attackers can abuse the SDProp process to
implement a persistent backdoor in Active Directory. SDProp compares the permissions on
protected objects with those defined on the AdminSDHolder object. If the permissions on any of
the protected accounts and groups do not match, the permissions on the protected accounts and
groups are reset to match those of the domain's AdminSDHolder object, regaining their
Administrative Privileges.
Rule ID
windows_security_108
Query
{'selection1': {'EventID': 5136}, 'selection2': {'ObjectDN': 'CN=AdminSDHolder,CN=Sys
tem*'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A

Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/01/31 high N/A
Rule Details: KRBTGT Delegation Backdoor
Identifies the modification of the msDS-AllowedToDelegateTo attribute to KRBTGT. Attackers can
use this technique to maintain persistence to the domain by having the ability to request tickets
for the KRBTGT service.
Rule ID
windows_security_109
Query
{'selection1': {'EventID': 4738}, 'selection2': {'AllowedToDelegateTo': '*krbtgt*'},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 , TA0006 , T1558 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2022/01/27 high N/A
Rule Details: HybridConnectionManager Service Installation

Rule to detect the Hybrid Connection Manager service installation.
Rule ID
windows_security_110
Query
{'selection': {'EventID': 4697, 'ServiceName': 'HybridConnectionManager', 'ServiceFil
eName|contains': 'HybridConnectionManager'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,0ee4d8a5-4e67-4faf-acfa-62a78457d1f2
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0003 , T1554 
References
https://twitter.com/Cyb3rWard0g/status/1381642789369286662 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2021/04/12 high Legitimate use of Hybrid Connection Manager via Azure function apps.
Rule Details: Windows Defender Exclusion Set
Detects scenarios where an windows defender exclusion was added in registry where an entity
would want to bypass antivirus scanning from windows defender.
Rule ID
windows_security_111
Query

{'selection': {'EventID': [4657, 4656, 4660, 4663], 'ObjectName|contains': '\\Microso
ft\\Windows Defender\\Exclusions\\'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Requirements: Audit Policy : Security Settings/Local Policies/Audit Policy, Registry
System Access Control (SACL): Auditing/User
Rule Source
SigmaHQ,e9c8808f-4cfb-4ba9-97d4-e5f3beaa244d
Author: @BarryShooshooga, Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1562.001 
References
https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-
defender-by-setting-path-exclusions/ 
Severity
75
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/26 high Intended inclusions by administrator
Rule Details: Password Change on Directory Service Restore Mode (DSRM) Account
The Directory Service Restore Mode (DSRM) account is a local administrator account on
Domain Controllers. Attackers may change the password to gain persistence.
Rule ID
windows_security_112
Query
{'selection': {'EventID': 4794}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events

Rule Source
SigmaHQ,53ad8e36-f573-46bf-97e4-15ba5bf4bb51
Author: Thomas Patzke
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
https://adsecurity.org/?p=1714 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
stable 2017/02/19 high Initial installation of a domain controller
Rule Details: Hacktool Ruler
This events that are generated when using the hacktool Ruler by Sensepost.
Rule ID
windows_security_113
Query
{'selection1': {'EventID': 4776, 'Workstation': 'RULER'}, 'selection2': {'EventID': [
4624, 4625], 'WorkstationName': 'RULER'}, 'condition': '(1 of selection*)'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,24549159-ac1b-479c-8175-d42aea947cae
Author: Florian Roth (Nextron Systems)
Tactics, Techniques, and Procedures
TA0002 , T1059 , TA0005 , T1550.002 , TA0007 , T1087 , TA0009 , T1114 
References
https://github.com/sensepost/ruler 
https://github.com/sensepost/ruler/issues/47 

https://github.com/staaldraad/go-
ntlm/blob/cd032d41aa8ce5751c07cb7945400c0f5c81e2eb/ntlm/ntlmv1.go#L427 
https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4776 
https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4624 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/05/31 high Go utilities that use staaldraad awesome NTLM library
Rule Details: Tap Driver Installation - Security
Well-known TAP software installation. Possible preparation for data exfiltration using tunnelling
techniques.
Rule ID
windows_security_114
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains': 'tap0901'}, 'condition':
'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,9c8afa4d-0022-48f0-9456-3712466f9701
Author: Daniil Yugoslavskiy, Ian Davis, oscd.community
Tactics, Techniques, and Procedures
TA0010 , T1048 
References
N/A

Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 medium Legitimate OpenVPN TAP insntallation
Rule Details: Suspicious Scheduled Task Creation
Detects suspicious scheduled task creation events. Based on attributes such as paths,
commands line flags, etc.
Rule ID
windows_security_115
Query
{'selection_eid': {'EventID': 4698}, 'selection_paths': {'TaskContent|contains': ['\\
AppData\\Local\\Temp\\', '\\AppData\\Roaming\\', '\\Users\\Public\\', '\\WINDOWS\\Tem
p\\', 'C:\\Temp\\', '\\Desktop\\', '\\Downloads\\', '\\Temporary Internet', 'C:\\Prog
ramData\\', 'C:\\Perflogs\\']}, 'selection_commands': {'TaskContent|contains': ['regs
vr32', 'rundll32', 'cmd.exe</Command>', 'cmd</Command>', '<Arguments>/c ', '<Argument
s>/k ', '<Arguments>/r ', 'powershell', 'pwsh', 'mshta', 'wscript', 'cscript', 'certu
til', 'bitsadmin', 'bash.exe', 'bash ', 'scrcons', 'wmic ', 'wmic.exe', 'forfiles', '
scriptrunner', 'hh.exe']}, 'condition': 'all of selection_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The Advanced Audit Policy setting Object Access > Audit Other Object Access Events
has to be configured to allow this detection. We also recommend extracting the
Command field from the embedded XML in the event data.
Rule Source
SigmaHQ,3a734d25-df5c-4b99-8034-af1ddb5883a4
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4698 

Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/12/05 high Unknown
Rule Details: User Couldn't Call a Privileged Service 'LsaRegisterLogonProcess
The 'LsaRegisterLogonProcess' function verifies that the application making the function call is a
logon process by checking that it has the SeTcbPrivilege privilege set. Possible Rubeus tries to
get a handle to LSA.
Rule ID
windows_security_116
Query
{'selection': {'EventID': 4673, 'Service': 'LsaRegisterLogonProcess()', 'Keywords': '
0x8010000000000000'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,6daac7fc-77d1-449a-a71a-e6b4d59a0e54
Author: Roberto Rodriguez (source), Ilyas Ochkov (rule), oscd.community
Tactics, Techniques, and Procedures
TA0006 , T1558.003 
References
https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-
trusts-71f2b33688e1 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id

Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Unknown
Rule Details: User Account Deleted
A user account has been deleted. This could be an indication of malicious activity.
Rule ID
windows_security_118
Query
{'selection1': {'EventID': 4726}, 'condition': 'selection1'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Possible DC Shadow Attack
Detects DCShadow via create new SPN.
Rule ID
windows_security_121
Query
{'selection1': {'EventID': 4742, 'ServicePrincipalNames|contains': 'GC/'}, 'selection
2': {'EventID': 5136, 'AttributeLDAPDisplayName': 'servicePrincipalName', 'AttributeV
alue|startswith': 'GC/'}, 'condition': '1 of selection*'}

Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The "Audit Directory Service Changes" logging policy must be configured in order to
receive events. Audit events are generated only for objects with configured system
access control lists (SACLs). Audit events are generated only for objects with
configured system access control lists (SACLs) and only when accessed in a manner
that matches their SACL settings. This policy covers the following events ids - 5136,
5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For
that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
Rule Source
SigmaHQ,32e19d25-4aed-4860-a55a-be99cb0bf7ed
Author: Ilyas Ochkov, oscd.community, Chakib Gzenayi (@Chak092), Hosni Mribah
Tactics, Techniques, and Procedures
TA0005 , T1207 
References
https://twitter.com/gentilkiwi/status/1003236624925413376 
https://gist.github.com/gentilkiwi/dcc132457408cf11ad2061340dcb53c2 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/10/25 medium Valid on domain controllers; exclude known DCs
Rule Details: Replay Attack Detected
Detects possible Kerberos Replay Attack on the domain controllers when
"KRB_AP_ERR_REPEAT" Kerberos response is sent to the client.
Rule ID
windows_security_124
Query
{'selection': {'EventID': 4649}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,5a44727c-3b85-4713-8c44-4401d5499629
Author: frack113
Tactics, Techniques, and Procedures
TA0008 , T1550 
References
https://github.com/Yamato-
Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6aa4ef19d
ef/ConfiguringSecurityLogAuditPolicies.md 
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4649 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/14 high Unknown
Rule Details: Security-Enabled Global Group was Deleted
A Security-Enabled Global Group has been deleted. This could be an indication of malicious
activity.
Rule ID
windows_security_127
Query
{'selection1': {'EventID': 4730}, 'selection2': {'SubjectUserName': ''}, 'selection3'
: {'SubjectDomainName': ''}, 'condition': 'selection1 and not selection2 and not sele
ction3'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: Credential Dumping Tools Service Execution - Security
Detects well-known credential dumping tools execution via service execution events.
Rule ID
windows_security_128
Query
{'selection': {'EventID': 4697, 'ServiceFileName|contains': ['fgexec', 'dumpsvc', 'ca
chedump', 'mimidrv', 'gsecdump', 'servpw', 'pwdump']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The 'System Security Extension' audit subcategory need to be enabled to log the EID
4697
Rule Source
SigmaHQ,f0d1feba-4344-4ca9-8121-a6c97bd6df52
Author: Florian Roth (Nextron Systems), Teymur Kheirkhabarov, Daniil Yugoslavskiy,
oscd.community
Tactics, Techniques, and Procedures
TA0002 , T1569.002 , TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-
environment 
Severity

75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/03/05 high Legitimate Administrator using credential dumping tool for password recovery
Rule Details: Modification of the msPKIAccountCredentials
Identify the modification of the msPKIAccountCredentials attribute in an Active Directory User
Object. Attackers can abuse the credentials roaming feature to overwrite an arbitrary file for
privilege escalation. ms-PKI-AccountCredentials contains binary large objects (BLOBs) of
encrypted credential objects from the credential manager store, private keys, certificates, and
certificate requests.
Rule ID
windows_security_129
Query
{'selection1': {'EventID': 5136}, 'selection2': {'AttributeLDAPDisplayName': 'msPKIAc
countCredentials'}, 'selection3': {'OperationType': '%%14674'}, 'selection4': {'Subje
ctUserSid': 'S-1-5-
18'}, 'condition': 'selection1 and selection2 and selection3 and (not selection4)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1068 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
production 2022/11/09 medium N/A
Rule Details: Device Installation Blocked
Detects an installation of a device that is forbidden by the system policy.
Rule ID
windows_security_130
Query
{'selection': {'EventID': 6423}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,c9eb55c3-b468-40ab-9089-db2862e42137
Author: frack113
Tactics, Techniques, and Procedures
TA0001 , T1200 
References
https://github.com/Yamato-
Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6aa4ef19d
ef/ConfiguringSecurityLogAuditPolicies.md 
https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
6423 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/10/14 medium Unknown
Rule Details: Webshell detected by Antivirus
The Windows Defender AntiVirus has detected a webshell in the system. This is an indication
that an attacker gained access to your server and he is trying to deploy a webshell in the
webserver.

Rule ID
windows_security_131
Query
{'selection1': {'EventID': 1116}, 'selection2': {'MalwareFamily|contains': 'webshell'
}, 'selection3': {'MalwareFamily|contains': 'chopper'}, 'selection4': {'MalwareFamily
|re': '(?:PHP|JSP|ASP) [\\/]Backdoor'}, 'selection5': {'MalwareFamily|re': 'Backdoor[
.:]
(?:PHP|JSP|ASP)'}, 'condition': 'selection1 and (selection2 or selection3 or selectio
n4 or selection5)'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1505.003 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2022/05/01 medium N/A
Rule Details: OilRig APT Schedule Task Persistence - Security
Detects OilRig schedule task persistence as reported by Nyotron in their March 2018 report.
Rule ID
windows_security_132
Query
{'selection_service': {'EventID': 4698, 'TaskName': ['SC Scheduled Scan', 'UpdatMachi
ne']}, 'condition': 'selection_service'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events
Rule Source
SigmaHQ,c0580559-a6bd-4ef6-b9b7-83703d98b561
Author: Florian Roth (Nextron Systems), Markus Neis, Jonhnathan Ribeiro, Daniil Yugoslavskiy,
oscd.community
Tactics, Techniques, and Procedures
TA0003 , T1053.005 , T1543.003 , TA0005 , T1112 , TA0011 , T1071.004 
References
https://web.archive.org/web/20180402134442/https://nyotron.com/wp-
content/uploads/2018/03/Nyotron-OilRig-Malware-Report-March-2018C.pdf 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/03/23 critical Unlikely
Rule Details: Remote WMI ActiveScriptEventConsumers
Detect potential adversaries leveraging WMI ActiveScriptEventConsumers remotely to move
laterally in a network.
Rule ID
windows_security_134
Query
{'selection': {'EventID': 4624, 'LogonType': '3', 'ProcessName|endswith': 'scrcons.ex
e'}, 'filter': {'TargetLogonId': '0x3e7'}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,9599c180-e3a8-4743-8f92-7fb96d3be648
Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
Tactics, Techniques, and Procedures

TA0003 , T1546.003 
References
https://threathunterplaybook.com/hunts/windows/200902-
RemoteWMIActiveScriptEventConsumers/notebook.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/09/02 high SCCM
Rule Details: RottenPotato Like Attack Pattern
Detects logon events that have characteristics of events generated during an attack with
RottenPotato and the like.
Rule ID
windows_security_136
Query
{'selection': {'EventID': 4624, 'LogonType': '3', 'TargetUserName|re': '(?:ANONYMOUS(
_| )LOGON)$', 'WorkstationName': ['-
', ''], 'IpAddress': ['127.0.0.1', '::1']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,16f5d8ca-44bd-47c8-acbe-6fc95a16c12f
Author: @SBousseaden, Florian Roth
Tactics, Techniques, and Procedures
TA0004 , T1068 
References
https://twitter.com/SBousseaden/status/1195284233729777665 
Severity
75

Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/11/15 high Unknown
Rule Details: Successful Overpass the Hash Attempt
Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the
Hash behavior of e.g Mimikatz's sekurlsa::pth module.
Rule ID
windows_security_138
Query
{'selection': {'EventID': 4624, 'LogonType': '9', 'LogonProcessName': 'seclogo', 'Aut
henticationPackageName': 'Negotiate'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,192a0330-c20b-4356-90b6-7b7049ae0b87
Author: Roberto Rodriguez (source), Dominik Schaudel (rule)
Tactics, Techniques, and Procedures
TA0005 , T1550.002 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/02/12 high Runas command-line tool using /netonly parameter
Legitimate use of Active Directory management tools (e.g., ADManager Plus)
Group Policy Client service (gpsvc) applying user-specific settings

Rule Details: DiagTrackEoP Default Login Username
Detects the default "UserName" used by the DiagTrackEoP POC.
Rule ID
windows_security_140
Query
{'selection': {'EventID': 4624, 'LogonType': '9', 'TargetOutboundUserName': 'thisisno
tvaliduser'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,2111118f-7e46-4fc8-974a-59fd8ec95196
Author: Nasreddine Bencherchali (Nextron Systems)
Tactics, Techniques, and Procedures
TA0005 , T1078 
References
https://github.com/Wh04m1001/DiagTrackEoP/blob/3a2fc99c9700623eb7dc7d4b5f314f
d9ce5ef51f/main.cpp#L46 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/08/03 critical Unlikely
Rule Details: Access Token Abuse
This rule tries to detect token impersonation and theft. (Example: DuplicateToken(Ex) and
ImpersonateLoggedOnUser with the LOGON32_LOGON_NEW_CREDENTIALS flag.)
Rule ID
windows_security_142
Query

{'selection': {'EventID': 4624, 'LogonType': '9', 'LogonProcessName': 'Advapi', 'Auth
enticationPackageName': 'Negotiate', 'ImpersonationLevel': '%%1833'}, 'condition': 's
election'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,02f7c9c1-1ae8-4c6a-8add-04693807f92f
Author: Michaela Adams, Zach Mathis
Tactics, Techniques, and Procedures
TA0005 , T1134.001 
References
https://www.elastic.co/fr/blog/how-attackers-abuse-access-token-manipulation 
https://www.manageengine.com/log-management/cyber-security/access-token-
manipulation.html 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/11/06 medium Anti-Virus
Rule Details: KrbRelayUp Attack Pattern
Detects logon events that have characteristics of events generated during an attack with
KrbRelayUp and the like.
Rule ID
windows_security_143
Query
{'selection1': {'EventID': 4624, 'LogonType': '3', 'AuthenticationPackageName': 'Kerb
eros', 'TargetUserSid|startswith': 'S-1-5-21-
', 'TargetUserSid|endswith': '-500'}, 'selection2': {'IpAddress': ['::1', '127.0.0.1'
]}, 'condition': 'selection1 and selection2'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,749c9f5e-b353-4b90-a9c1-05243357ca4b
Author: Elastic, @SBousseaden
Tactics, Techniques, and Procedures
TA0008 , T1550 
References
https://github.com/elastic/detection-
rules/blob/fb6ee2c69864ffdfe347bf3b050cb931f53067a6/rules/windows/privilege_escal
ation_krbrelayup_suspicious_logon.toml 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2022/04/27 high Unknown
Rule Details: Password Dumper Activity on LSASS
Detects process handle on LSASS process with certain access mask and object type
SAM_DOMAIN.
Rule ID
windows_security_146
Query
{'selection': {'EventID': 4656, 'ProcessName|endswith': '\\lsass.exe', 'AccessMask':
'0x705', 'ObjectType': 'SAM_DOMAIN'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,aa1697b7-d611-4f9a-9cb2-5125b4ccfd5c
Author: sigma

Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
https://twitter.com/jackcr/status/807385668833968128 
Severity
75
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2017/02/12 high Unknown
Rule Details: SAM Registry Hive Handle Request
Detects handles requested to SAM registry hive.
Rule ID
windows_security_147
Query
{'selection': {'EventID': 4656, 'ObjectType': 'Key', 'ObjectName|endswith': '\\SAM'},
'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,f8748f2c-89dc-4d95-afb0-5a2dfdbad332
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0007 , T1012 , TA0006 , T1552.002 
References
https://threathunterplaybook.com/hunts/windows/190725-
SAMRegistryHiveHandleRequest/notebook.html 
Severity
75
Suppression Logic Based On

computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/12 high Unknown
Rule Details: Impacket PsExec Execution
Detects execution of Impacket's psexec.py.
Rule ID
windows_security_150
Query
{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$', 'RelativeTargetName|cont
ains': ['RemCom_stdin', 'RemCom_stdout', 'RemCom_stderr']}, 'condition': 'selection1'
}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,32d56ea1-417f-44ff-822b-882873f5f43b
Author: Bhabesh Raj
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/12/14 high Unknown

Rule Details: Remote Task Creation via ATSVC Named Pipe
Detects remote task creation via at.exe or API interacting with ATSVC namedpipe.
Rule ID
windows_security_151
Query
{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$', 'RelativeTargetName': 'at
svc', 'Accesses|contains': ['WriteData', '%%4417']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,f6de6525-4509-495a-8a82-1f8b0ed73a00
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0003 , T1053.002 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/04/03 medium Unknown
Rule Details: Protected Storage Service Access
Detects access to a protected_storage service over the network. Potential abuse of DPAPI to
extract domain backup keys from Domain Controllers.
Rule ID
windows_security_152
Query

{'selection': {'EventID': 5145, 'ShareName|contains': 'IPC', 'RelativeTargetName': 'p
rotected_storage'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,45545954-4016-43c6-855e-eae8f1c369dc
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/08/10 high Unknown
Rule Details: Persistence and Execution at Scale via GPO Scheduled Task
Detect lateral movement using GPO scheduled task, usually used to deploy ransomware at
scale.
Rule ID
windows_security_153
Query
{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\SYSVOL', 'RelativeTargetName|end
swith': 'ScheduledTasks.xml', 'Accesses|contains': ['WriteData', '%%4417']}, 'conditi
on': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,a8f29a7b-b137-4446-80a0-b804272f3da2
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0003 , T1053.005 
References
https://twitter.com/menasec1/status/1106899890377052160 
https://www.secureworks.com/blog/ransomware-as-a-distraction 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Matur Creation Risk False Positives
ity Date Level
test 2019/04/0 high If the source IP is not localhost then it's super suspicious, better to monitor both local and
remote changes to GPO scheduledtasks
3
Rule Details: First Time Seen Remote Named Pipe
This detection excludes known named pipes accessible remotely and notify on newly observed
ones, may help to detect lateral movement and remote exec using named pipes.
Rule ID
windows_security_154
Query
{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$'}, 'false_positives': {'Re
lativeTargetName': ['atsvc', 'samr', 'lsarpc', 'lsass', 'winreg', 'netlogon', 'srvsvc
', 'protected_storage', 'wkssvc', 'browser', 'netdfs', 'svcctl', 'spoolss', 'ntsvcs',
'LSM_API_service', 'HydraLsPipe', 'TermSrv_API_service', 'MsFteWds', 'sql\\query', '
eventlog']}, 'condition': 'selection1 and not false_positives'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,52d8b0c6-53d6-439a-9e41-52ad442ad9ad
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
https://twitter.com/menasec1/status/1104489274387451904 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/04/03 high Update the excluded named pipe to filter out any newly observed legit named pipe
Rule Details: DCERPC SMB Spoolss Named Pipe
Detects the use of the spoolss named pipe over SMB. This can be used to trigger the
authentication via NTLM of any machine that has the spoolservice enabled.
Rule ID
windows_security_155
Query
{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$', 'RelativeTargetName': 'sp
oolss'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,214e8f95-100a-4e04-bb31-ef6cba8ce07e
Author: OTR (Open Threat Research)
Tactics, Techniques, and Procedures
TA0008 , T1021.002 

References
https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-
trusts-71f2b33688e1 
https://dirkjanm.io/a-different-way-of-abusing-zerologon/ 
https://twitter.com/_dirkjan/status/1309214379003588608 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2018/11/28 medium Domain Controllers acting as printer servers too? :)
Rule Details: T1047 Wmiprvse Wbemcomn DLL Hijack
Detects a threat actor creating a file named `wbemcomn.dll` in the
`C:\Windows\System32\wbem\` directory over the network for a WMI DLL Hijack scenario.
Rule ID
windows_security_157
Query
{'selection': {'EventID': 5145, 'RelativeTargetName|endswith': '\\wbem\\wbemcomn.dll'
}, 'filter': {'SubjectUserName|endswith': '$'}, 'condition': 'selection and not filte
r'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,f6c68d5f-e101-4b86-8c84-7d96851fd65c
Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
Tactics, Techniques, and Procedures
TA0002 , T1047 , TA0008 , T1021.002 
References
https://threathunterplaybook.com/hunts/windows/201009-
RemoteWMIWbemcomnDLLHijack/notebook.html 
Severity

75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high Unknown
Rule Details: CVE-2021-1675 Print Spooler Exploitation IPC Access
Detects remote printer driver load from Detailed File Share in Security logs that are a sign of
successful exploitation attempts against print spooler vulnerability CVE-2021-1675 and CVE-
2021-34527.
Rule ID
windows_security_159
Query
{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$', 'RelativeTargetName': 'sp
oolss', 'AccessMask': '0x3', 'ObjectType': 'File'}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,8fe1c584-ee61-444b-be21-e9054b229694
Author: INIT_6
Tactics, Techniques, and Procedures
TA0002 , T1569 
References
https://twitter.com/INIT_3/status/1410662463641731075 
Severity
90
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

Maturity Creation Date Risk Level False Positives
experimental 2021/07/02 critical Unknown
Rule Details: Possible PetitPotam Coerce Authentication Attempt
Detect PetitPotam coerced authentication activity.
Rule ID
windows_security_161
Query
{'selection': {'EventID': 5145, 'ShareName|startswith': '\\\\', 'ShareName|endswith':
'\\IPC$', 'RelativeTargetName': 'lsarpc', 'SubjectUserName': 'ANONYMOUS LOGON'}, 'co
ndition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Object Access > Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,1ce8c8a3-2723-48ed-8246-906ac91061a6
Author: Mauricio Velazco, Michael Haag
Tactics, Techniques, and Procedures
TA0006 , T1187 
References
https://github.com/topotam/PetitPotam 
https://github.com/splunk/security_content/blob/0dd6de32de2118b2818550df9e65255f4
109a56d/detections/endpoint/petitpotam_network_share_access_request.yml 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2021/09/02 high Unknown. Feedback welcomed.
Rule Details: Possible Impacket SecretDump Remote Activity

Detect AD credential dumping using impacket secretdump HKTL.
Rule ID
windows_security_162
Query
{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\ADMIN$', 'RelativeTargetName|con
tains|all': ['SYSTEM32\\', '.tmp']}, 'condition': 'selection'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,252902e3-5830-4cf6-bf21-c22083dfd5cf
Author: Samir Bousseaden, wagga
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
experimental 2019/04/03 high Unknown
Rule Details: Suspicious PsExec Execution
Detects execution of psexec or paexec with renamed service name, this rule helps to filter out
the noise if psexec is used for legit purposes or if attacker uses a different psexec client other
than sysinternal one.
Rule ID
windows_security_164
Query

{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$', 'RelativeTargetName|ends
with': ['-stdin', '-stdout', '-
stderr']}, 'filter': {'RelativeTargetName|startswith': 'PSEXESVC'}, 'condition': 'sel
ection1 and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
The advanced audit policy setting "Object Access > Audit Detailed File Share" must be
configured for Success/Failure
Rule Source
SigmaHQ,c462f537-a1e3-41a6-b5fc-b2c2cef9bf82
Author: Samir Bousseaden
Tactics, Techniques, and Procedures
TA0008 , T1021.002 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/04/03 high Unknown
Rule Details: DCOM InternetExplorer.Application Iertutil DLL Hijack - Security
Detects a threat actor creating a file named `iertutil.dll` in the `C:\Program Files\Internet
Explorer\` directory over the network for a DCOM InternetExplorer DLL Hijack scenario.
Rule ID
windows_security_165
Query
{'selection': {'EventID': 5145, 'RelativeTargetName|endswith': '\\Internet Explorer\\
iertutil.dll'}, 'filter': {'SubjectUserName|endswith': '$'}, 'condition': 'selection
and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events
Rule Source
SigmaHQ,c39f0c81-7348-4965-ab27-2fde35a1b641
Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
Tactics, Techniques, and Procedures
TA0008 , T1021 
References
https://threathunterplaybook.com/hunts/windows/201009-
RemoteDCOMIErtUtilDLLHijack/notebook.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2020/10/12 high Unknown
Rule Details: Remote PowerShell Sessions Network Connections (WinRM)
Detects basic PowerShell Remoting (WinRM) by monitoring for network inbound connections to
ports 5985 OR 5986.
Rule ID
windows_security_166
Query
{'selection': {'EventID': 5156, 'DestPort': ['5985', '5986'], 'LayerRTID': '44'}, 'fi
lter': {'Application': ['System']}, 'condition': 'selection and not filter'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,13acf386-b8c6-4fe0-9a6e-c4756b974698
Author: Roberto Rodriguez @Cyb3rWard0g
Tactics, Techniques, and Procedures
TA0002 , T1059.001 

References
https://threathunterplaybook.com/hunts/windows/190511-
RemotePwshExecution/notebook.html 
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/09/12 high Legitimate use of remote PowerShell execution
Rule Details: Suspicious Outbound Kerberos Connection - Security
Detects suspicious outbound network activity via kerberos default port indicating possible lateral
movement or first stage PrivEsc via delegation.
Rule ID
windows_security_167
Query
{'selection': {'EventID': 5156, 'DestPort': '88', 'Direction': '%%14593'}, 'filter_ex
act': {'Application': ['System', '\\device\\harddiskvolume*\\windows\\system32\\lsass
.exe', '\\device\\harddiskvolume*\\*\\nmap.exe', '\\device\\harddiskvolume*\\*\\chrom
e.exe', '\\device\\harddiskvolume*\\*\\firefox.exe', '\\device\\harddiskvolume*\\*\\m
sedge.exe', '\\device\\harddiskvolume*\\*\\iexplore.exe']}, 'condition': 'selection a
nd not 1 of filter_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,eca91c7c-9214-47b9-b4c5-cb1d7e4f2350
Author: Ilyas Ochkov, oscd.community
Tactics, Techniques, and Procedures
TA0006 , T1558.003 
References
https://github.com/GhostPack/Rubeus 
Severity

75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2019/10/24 high Web Browsers
Rule Details: Potentially Suspicious AccessMask Requested From LSASS
Detects process handle on LSASS process with certain access mask.
Rule ID
windows_security_169
Query
{'selection_1': {'EventID': 4656, 'ObjectName|endswith': '\\lsass.exe', 'AccessMask|c
ontains': ['0x40', '0x1400', '0x100000', '0x1410', '0x1010', '0x1438', '0x143a', '0x1
418', '0x1f0fff', '0x1f1fff', '0x1f2fff', '0x1f3fff']}, 'selection_2': {'EventID': 46
63, 'ObjectName|endswith': '\\lsass.exe', 'AccessList|contains': ['4484', '4416']}, '
filter_main_specific': {'ProcessName|endswith': ['\\csrss.exe', '\\GamingServices.exe
', '\\lsm.exe', '\\MicrosoftEdgeUpdate.exe', '\\minionhost.exe', '\\MRT.exe', '\\MsMp
Eng.exe', '\\perfmon.exe', '\\procexp.exe', '\\procexp64.exe', '\\svchost.exe', '\\ta
skmgr.exe', '\\thor.exe', '\\thor64.exe', '\\vmtoolsd.exe', '\\VsTskMgr.exe', '\\wini
nit.exe', '\\wmiprvse.exe', '\\WmiPrvSE.exe', 'RtkAudUService64'], 'ProcessName|conta
ins': [':\\Program Files (x86)\\', ':\\Program Files\\', ':\\ProgramData\\Microsoft\\
Windows Defender\\Platform\\', ':\\Windows\\SysNative\\', ':\\Windows\\System32\\', '
:\\Windows\\SysWow64\\', ':\\Windows\\Temp\\asgard2-
agent\\']}, 'filter_main_generic': {'ProcessName|contains': ':\\Program Files'}, 'fil
ter_main_exact': {'ProcessName|endswith': [':\\Windows\\System32\\taskhostw.exe', ':\
\Windows\\System32\\msiexec.exe', ':\\Windows\\CCM\\CcmExec.exe', '\\Windows\\explore
r.exe', '\\jre\\bin\\java.exe', ':\\Windows\\LTSvc\\LTSVC.exe']}, 'filter_main_sysmon
': {'ProcessName|endswith': ':\\Windows\\Sysmon64.exe', 'AccessList|contains': '%%448
4'}, 'filter_main_aurora': {'ProcessName|contains': ':\\Windows\\Temp\\asgard2-agent-
sc\\aurora\\', 'ProcessName|endswith': '\\aurora-agent-
64.exe', 'AccessList|contains': '%%4484'}, 'filter_main_scenarioengine': {'ProcessNam
e|endswith': '\\x64\\SCENARIOENGINE.EXE', 'AccessList|contains': '%%4484'}, 'filter_m
ain_avira1': {'ProcessName|contains|all': [':\\Users\\', '\\AppData\\Local\\Temp\\is-
'], 'ProcessName|endswith': '\\avira_system_speedup.tmp', 'AccessList|contains': '%%4
484'}, 'filter_main_avira2': {'ProcessName|contains': ':\\Windows\\Temp\\', 'ProcessN
ame|endswith': '\\avira_speedup_setup_update.tmp', 'AccessList|contains': '%%4484'},
'filter_main_snmp': {'ProcessName|endswith': ':\\Windows\\System32\\snmp.exe', 'Acces
sList|contains': '%%4484'}, 'filter_main_googleupdate': {'ProcessName|contains': ':\\
Windows\\SystemTemp\\', 'ProcessName|endswith': '\\GoogleUpdate.exe', 'AccessList|con
tains': '%%4484'}, 'filter_optional_procmon': {'ProcessName|endswith': ['\\procmon64.

exe', '\\procmon.exe'], 'AccessList|contains': '%%4484'}, 'condition': '1 of selectio
n_* and not 1 of filter_main_* and not 1 of filter_optional_*'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
SigmaHQ,4a1b6da0-d94f-4fc3-98fc-2d9cb9e5ee76
Author: Roberto Rodriguez, Teymur Kheirkhabarov, Dimitrios Slamaris, Mark Russinovich,
Aleksey Potapov, oscd.community (update)
Tactics, Techniques, and Procedures
TA0006 , T1003.001 
References
https://web.archive.org/web/20230208123920/https://cyberwardog.blogspot.com/2017/0
3/chronicles-of-threat-hunter-hunting-for_22.html 
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-
environment 
Severity
50
Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id
Additional Information
Maturity Creation Risk False Positives
Date Level
experiment 2019/11/01 medium Legitimate software accessing LSASS process for legitimate reason; update the
whitelist with it
al
Rule Details: Transferring Files with Credential Data via Network Shares
Transferring files with well-known filenames (sensitive files with credential data) using network
shares.
Rule ID
windows_security_170
Query
{'selection': {'EventID': 5145, 'RelativeTargetName|contains': ['\\mimidrv.sys', '\\w
indows\\minidump\\', '\\hiberfil.sys', '\\ntds.dit']}, 'condition': 'selection'}
Log Source

Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0006 , T1003 
References
https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-
environment 
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturit Creation Risk False Positives
y Date Level
test 2019-10-22 medium Transferring sensitive files for legitimate administration work by legitimate
administrator
Rule Details: Startup/Logon Script added to Group Policy Object
Detects the modification of Group Policy Objects (GPO) to add a startup/logon script to users or
computer objects.
Rule ID
windows_security_171
Query
{'selection1': {'EventID': 5136}, 'selection2': {'AttributeLDAPDisplayName': ['gPCMac
hineExtensionNames', 'gPCUserExtensionNames']}, 'selection3': {'AttributeValue|contai
ns': '42B5FAAE-6536-11D2-AE5A-
0000F87571E3'}, 'selection4': {'AttributeValue|contains': ['40B66650-4972-11D1-A7CA-
0000F87571E3', '40B6664F-4972-11D1-A7CA-
0000F87571E3']}, 'condition': 'selection1 and selection2 and selection3 and selection
4'}
Log Source
Stellar Cyber Windows Server Sensor configured.
Rule Source

Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1484.001 , T1547 
References
N/A
Severity
50
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
production 2021/11/08 medium Legitimate Administrative Activity
Rule Details: Windows Privilege Escalation through Security Group Modification
This rule detects request for privilege escalation by modifying windows security group.
Rule ID
windows_security_201
Query
{'selection1': {'EventID': [632, 4728, 636, 4732, 660, 4756]}, 'selection2': {'Target
UserName': ['Group Policy Creator Owners', 'Administrators', 'DHCP Administrators', '
DNS Admins', 'Domain Admins', 'Enterprise Admins', 'Enterprise Key Admins', 'Hyper-
V Administrators', 'Key Admins', 'Schema Admins', 'Storage Replica Administrators']},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1078 , T1098 
References
N/A
Severity
50

Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information
Maturity Creation Date Risk Level False Positives
test 2023/06/22 high Legitimate administrative activity
Rule Details: Windows AD SID History Attribute Modified
Detects modifications to the SID History attribute in Active Directory. This detection identifies
changes to the sIDHistory attribute which can be exploited by adversaries to inherit permissions
from other accounts, potentially granting unauthorized access. If confirmed malicious, this activity
could allow attackers to maintain persistent access and escalate privileges within the domain,
posing a significant security risk.
Rule ID
windows_security_300
Query
{'selection1': {'EventID': 5136}, 'selection2': {'AttributeLDAPDisplayName': 'sIDHist
ory'}, 'selection3': {'OperationType': '%%14674'}, 'condition': 'selection1 and selec
tion2 and selection3'}
Log Source
Stellar Cyber Windows Server Sensor configured for:
Collecting Windows security events
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1134.005 
References
N/A
Severity
75
Suppression Logic Based On
event_id
computer_name
stellar.rule_id
Additional Information

| Maturity     | Creation Date | Risk Level | False Positives               |
| ------------ | ------------- | ---------- | ----------------------------- |
| experimental | 2025/08/14    | high       | Domain mergers and migrations |
Legitimate administrative operations involving SID history
ADMT (Active Directory Migration Tool) operations
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        