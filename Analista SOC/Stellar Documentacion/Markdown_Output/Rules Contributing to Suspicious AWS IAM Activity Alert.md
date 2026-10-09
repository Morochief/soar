Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS IAM
Activity Alert

The following rules are used to identify suspicious activity within AWS IAM logs. Any one or more
of these will trigger a Suspicious AWS IAM Activity Alert. Details for each rule can be viewed by
clicking the More Details link in the description.

Title

Description

AWS User Login Profile
Was Modified

An attacker with the iam:UpdateLoginProfile permission on other users can change the password
used to login to the AWS console on any user that already has a login profile setup. With this
alert, it is used to detect anyone is changing password on behalf of other users.

More details

Rule ID

aws_2

Query

{'selection_source': {'eventSource': 'iam.amazonaws.com', 'eve
ntName': 'UpdateLoginProfile'}, 'filter': {'userIdentity_arn|c
ontains': 'requestParameters.userName'}, 'condition': 'selecti
on_source and not filter'}

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

Title

Description

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id

Additional Information

Maturity Creation Date

Risk Level

False Positives

test

2021/08/09

high

Legit User Account Administration

AWS IAM Backdoor Users
Keys

Detects AWS API key creation for a user by another user. Backdoored users can be used to
obtain persistence in the AWS environment. Also with this alert, you can detect a flow of AWS
keys in your org.

More details

Rule ID

aws_13

Query

{'selection_source': {'eventSource': 'iam.amazonaws.com', 'eve
ntName': 'CreateAccessKey'}, 'filter': {'userIdentity_arn|cont
ains': 'responseElements.accessKey.userName'}, 'condition': 's
election_source and not filter'}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,0a5177f4-6ca9-44c2-aacf-d3f3d8b6e4d2

Author: faloker

Tactics, Techniques, and Procedures

TA0003 , T1098 

References

https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c81
7f2c5b181/pacu/modules/iam__backdoor_users_keys/main.py 

Severity

50

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id

Additional Information

Matu
rity

Creation
Date

Risk
Level

test

2020/02/
12

mediu
m

False Positives

Adding user keys to their own accounts (the filter cannot
cover all possible variants of user naming)

AWS API keys legitimate exchange workflows

Title

Description

AWS IAM User Addition to
Group

Identifies the addition of a user to a specified group in AWS Identity and Access Management
(IAM).

More details

Rule ID

aws_24

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'AddUserToGroup'}, 'condition': 'selection1
 and selection2'}

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

Matu
rity

Creati
on
Date

Risk
Leve
l

low

2020/0
6/04

prod
uctio
n

False Positives

Adding users to a specified group may be done by a system or
network administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment. User additions from unfamiliar users or hosts
should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

AWS IAM Group Creation

Identifies the creation of a group in AWS Identity and Access Management (IAM). Groups specify
permissions for multiple users. Any user in a group automatically has the permissions that are
assigned to the group.

More details

Rule ID

aws_26

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateGroup'}, 'condition': 'selection1 an
d selection2'}

Log Source

Title

Description

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

Matu
rity

Creati
on
Date

Risk
Leve
l

low

2020/0
6/05

prod
uctio
n

False Positives

A group may be created by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment. Group creations
by unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS IAM Assume Role
Policy Update

Identifies attempts to modify an AWS IAM Assume Role Policy. An adversary may attempt to
modify the AssumeRolePolicy of a misconfigured role in order to gain the privileges of that role.

More details

Rule ID

aws_42

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'UpdateAssumeRolePolicy'}, 'condition': 'se
lection1 and selection2'}

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

Title

Description

aws.eventSource
aws.eventName
aws.errorCode
stellar.rule_id

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

2020/0
7/06

prod
uctio
n

False Positives

Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment. Policy updates
from unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS IAM Deactivation of
MFA Device

Identifies the deactivation of a specified multi-factor authentication (MFA) device and removes it
from association with the user name for which it was originally enabled. In AWS Identity and
Access Management (IAM), a device must be deactivated before it can be deleted.

More details

Rule ID

aws_44

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': ['DeactivateMFADevice', 'DeleteVirtualMFADe
vice']}, 'condition': 'selection1 and selection2'}

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

Creati
on
Date

2020/
05/26

Risk
Leve
l

medi
um

Matu
rity

prod
uctio
n

False Positives

A MFA device may be deactivated by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. MFA
device deactivations from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can
be exempted from the rule.

Title

Description

AWS IAM Group Deletion

Identifies the deletion of a specified AWS Identity and Access Management (IAM) resource group.
Deleting a resource group does not delete resources that are members of the group; it only
deletes the group structure.

More details

Rule ID

aws_50

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'DeleteGroup'}, 'condition': 'selection1 an
d selection2'}

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

Matu
rity

Creati
on
Date

Risk
Leve
l

low

2020/0
5/21

prod
uctio
n

False Positives

A resource group may be deleted by a system administrator.
Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment. Resource group
deletions by unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted
from the rule.

AWS New MFA Method
Registered For User

The following analytic identifies the registration of a new Multi Factor authentication method for an
AWS account. Adversaries who have obtained unauthorized access to an AWS account may
register a new MFA method to maintain persistence.

More details

Rule ID

aws_75

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateVirtualMFADevice'}, 'condition': 'se
lection1 and selection2'}

Title

Description

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

Matur
ity

Creatio
n Date

Risk
Level

produ
ction

2023-
01-31

mediu
m

False Positives

Newly onboarded users who are registering an MFA method
for the first time will also trigger this detection.

AWS IAM User Created

A new account has been created in AWS IAM.

More details

Rule ID

aws_80

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateUser'}, 'condition': 'selection1 and
 selection2'}

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

Title

Description

Created AWS IAM
Credentials

aws.errorCode
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

New IAM credentials have been generated.

More details

Rule ID

aws_81

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateAccessKey'}, 'condition': 'selection
1 and selection2'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

IAM Policy Modification

The IAM policies associated with a user have been modified.

More details

Rule ID

aws_82

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'UpdateUserAccessPolicy'}, 'selection3': {'
eventName': 'DeleteUserAccessPolicy'}, 'selection4': {'eventNa
me': 'AddAccessPolicyToGroup'}, 'selection5': {'eventName': 'A
ddUserToGroup'}, 'selection6': {'eventName': 'RemoveUsersFromG
roup'}, 'condition': 'selection1 and (selection2 or selection3
 or selection4 or selection5 or selection6)'}

Title

Description

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

AWS IAM AccessDenied
Discovery Event

The following detection identifies AccessDenied event. It is possible that an access key to AWS
may have been stolen and is being misused to perform discovery events.

More details

Rule ID

aws_83

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'errorCode': 'AccessDenied'}, 'selection3': {'userIdenti
ty_type': 'IAMUser'}, 'selection4': {'userAgent': '*.amazonaws
.com'}, 'condition': 'selection1 and selection2 and selection3
 and not selection4'}

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

Title

Description

aws.errorCode
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

producti
on

2021-11-
12

medium

False Positives

It is possible to start this detection will need to be tuned
by source IP or user.

AWS IAM Delete Policy

The following detection identifies when a policy is deleted on AWS. This does not identify whether
successful or failed, but the error messages tell a story of suspicious attempts.

More details

Rule ID

aws_84

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'DeletePolicy'}, 'selection3': {'userAgent'
: '*.amazonaws.com'}, 'condition': 'selection1 and selection2
and not selection3'}

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

Creati
on
Date

2021-
04-01

Risk
Leve
l

medi
um

Matu
rity

prod
uctio
n

False Positives

This detection will require tuning to provide high fidelity detection
capabilities. Tune based on src addresses (corporate offices,
VPN terminations) or by groups of users. Not every user with
AWS access should have permission to delete policies (least
privilege). In addition, this may be saved separately and tuned for
failed or success attempts only.

AWS IAM Failure Group
Deletion

This detection identifies failure attempts to delete groups. We want to identify when a group is
attempting to be deleted, but either access is denied, there is a conflict or there is no group. This
is indicative of administrators performing an action, but also could be suspicious behavior
occurring.

Title

Description

More details

Rule ID

aws_85

Query

{'selection2': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n3': {'eventName': 'DeleteGroup'}, 'selection4': {'errorCode':
 ['NoSuchEntityException', 'DeleteConflictException']}, 'selec
tion5': {'errorCode': 'AccessDenied'}, 'selection6': {'userAge
nt': '*.amazonaws.com'}, 'condition': 'selection2 and selectio
n3 and (selection4 or selection5) and not selection6'}

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

Creati
on
Date

Risk
Leve
l

2021-
04-01

medi
um

Matu
rity

prod
uctio
n

False Positives

This detection will require tuning to provide high fidelity detection
capabilities. Tune based on src addresses (corporate offices,
VPN terminations) or by groups of users. Not every user with
AWS access should have permission to delete groups (least
privilege).

AWS
SetDefaultPolicyVersion

This search looks for AWS CloudTrail events where a user has set a default policy versions.
Attackers have been know to use this technique for Privilege Escalation in case the previous
versions of the policy had permissions to access more resources than the current version of the
policy

More details

Rule ID

aws_86

Query

{'selection2': {'eventName': 'SetDefaultPolicyVersion'}, 'sele
ction3': {'eventSource': 'iam.amazonaws.com'}, 'condition': 's

Title

Description

election2 and selection3'}

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

Creati
on
Date

2021-
03-02

Risk
Leve
l

medi
um

Matu
rity

prod
uctio
n

False Positives

While this search has no known false positives, it is possible that
an AWS admin has legitimately set a default policy to allow a
user to access all resources. That said, AWS strongly advises
against granting full control to all AWS resources

AWS Create Policy Version
to allow all resources

This search looks for AWS CloudTrail events where a user created a policy version that allows
them to access any resource in their account.

More details

Rule ID

aws_87

Query

{'selection2': {'eventName': 'CreatePolicyVersion'}, 'selectio
n3': {'eventSource': 'iam.amazonaws.com'}, 'selection4': {'err
orCode': 'success'}, 'condition': 'selection2 and selection3 a
nd selection4'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1078.004 

References

https://bishopfox.com/blog/privilege-escalation-in-aws 

Title

Description

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

Creati
on
Date

2022-
05-17

Risk
Leve
l

medi
um

Matu
rity

prod
uctio
n

False Positives

While this search has no known false positives, it is possible that
an AWS admin has legitimately created a policy to allow a user to
access all resources. That said, AWS strongly advises against
granting full control to all AWS resources and you must verify this
activity.

AWS CreateLoginProfile

This search looks for AWS CloudTrail events where a user A (victim A) creates a login profile.

More details

Rule ID

aws_119

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateLoginProfile'}, 'condition': 'select
ion1 and selection2'}

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

Title

Matur
ity

Creatio
n Date

Risk
Level

produ
ction

2021-
07-19

mediu
m

Description

False Positives

While this search has no known false positives, it is possible
that an AWS admin has legitimately created a login profile.

AWS CreateAccessKey

This search looks for AWS CloudTrail events where a user creates access keys.

More details

Rule ID

aws_120

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateAccessKey'}, 'selection3': {'userAge
nt': 'console.amazonaws.com'}, 'selection4': {'errorCode': 'su
ccess'}, 'condition': 'selection1 and (selection2 and (not sel
ection3) and selection4)'}

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

Maturity

Creation Date

Risk Level

False Positives

production

2022-03-03

medium

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

