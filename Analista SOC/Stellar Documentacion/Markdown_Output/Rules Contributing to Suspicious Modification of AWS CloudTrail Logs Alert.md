Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Modification of
AWS CloudTrail Logs Alert

The following rules are used to identify suspicious activity within AWS Cloudtrail logs. Any one or
more of these will trigger Suspicious Modification of AWS CloudTrail Logs Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

AWS CloudTrail Log
Updated

Description

Identifies an update to an AWS log trail setting that specifies the delivery of log files.

More details

Rule ID

aws_34

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, '
selection2': {'eventName': 'UpdateTrail'}, 'condition': 'sele
ction1 and selection2'}

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

Title

Description

Additional Information

Matu
rity

Creati
on
Date

Risk
Leve
l

low

2020/
06/10

prod
uctio
n

False Positives

Trail updates may be made by a system or network
administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your
environment. Trail updates from unfamiliar users or hosts should
be investigated. If known behavior is causing false positives, it
can be exempted from the rule.

Federated user attempting to
assume role

A federated user is attempting to assume a role. Federation users enable to manage access to
AWS accounts by adding and removing users from the corporate directory, such as Microsoft
Active Directory.

More details

Rule ID

aws_110

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, '
selection2': {'errorMessage': 'Roles may not be assumed by fe
derated users'}, 'condition': 'selection1 and selection2'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

AWS Impair Security
Services

This analytic looks for several delete specific API calls made to AWS Security Services like
CloudWatch, GuardDuty and Web Application Firewalls.

More details

Rule ID

aws_116

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, '
selection2': {'eventName': 'DeleteLogStream'}, 'selection3':

Title

Description

{'eventName': 'DeleteDetector'}, 'selection4': {'eventName':
'DeleteIPSet'}, 'selection5': {'eventName': 'DeleteWebACL'},
'selection6': {'eventName': 'DeleteRule'}, 'selection7': {'ev
entName': 'DeleteRuleGroup'}, 'selection8': {'eventName': 'De
leteLoggingConfiguration'}, 'selection9': {'eventName': 'Dele
teAlarms'}, 'condition': 'selection1 and (selection2 or selec
tion3 or selection4 or selection5 or selection6 or selection7
 or selection8 or selection9)'}

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

Maturi
ty

Creation
Date

Risk
Level

produc
tion

2022-07-
26

mediu
m

False Positives

While this search has no known false positives, it is
possible that it is a legitimate admin activity.

AWS Privilege Escalation via
Group/Role/User Policy

Identifies the request for privilege escalation by modifying AWS Group/Role/User Policy

More details

Rule ID

aws_200

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com', 'e
ventName': ['AttachGroupPolicy', 'PutGroupPolicy', 'AttachRol
ePolicy', 'PutRolePolicy', 'AttachUserPolicy', 'PutUserPolicy
']}, 'selection2': {'requestParameters_policyArn': ['arn:aws:
iam::aws:policy/AdministratorAccess', 'arn:aws:iam::aws:polic
y/AmazonSNSFullAccess', 'arn:aws:iam::aws:policy/AmazonEC2Ful
lAccess', 'arn:aws:iam::aws:policy/AmazonS3FullAccess', 'arn:
aws:iam::aws:policy/AmazonDynamoDBFullAccess', 'arn:aws:iam::
aws:policy/AWSCodeCommitPowerUser', 'arn:aws:iam::aws:policy/
AWSKeyManagementServicePowerUser', 'arn:aws:iam::aws:policy/P
owerUserAccess', 'arn:aws:iam::aws:policy/DatabaseAdministrat
or', 'arn:aws:iam::aws:policy/NetworkAdministrator', 'arn:aws

Title

Description

:iam::aws:policy/SystemAdministrator', 'arn:aws:iam::aws:poli
cy/Billing']}, 'condition': 'selection1 and selection2'}

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

Maturit
y

Creation
Date

Risk
Level

test

2023/06/22

high

False Positives

Valid changes to policy by authorized
user/administrator

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

