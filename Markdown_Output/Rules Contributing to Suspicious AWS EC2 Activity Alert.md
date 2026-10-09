Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS EC2
Activity Alert

The following rules are used to identify suspicious activity within AWS EC2 logs. Any one or more
of these will trigger Suspicious AWS EC2 Activity Alert. Details for each rule can be viewed by
clicking the More Details link in the description.

Title

Description

AWS EC2 Startup Shell
Script Change

Detects changes to the EC2 instance startup script. The shell script will be executed as
root/SYSTEM every time the specific instances are booted up.

More details

Rule ID

aws_8

Query

{'selection_source': {'eventSource': 'ec2.amazonaws.com', 'req
uestParameters_attribute': 'userData', 'eventName': 'ModifyIns
tanceAttribute'}, 'condition': 'selection_source'}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,1ab3c5ed-5baf-417b-bb6b-78ca33f6c3df

Author: faloker

Tactics, Techniques, and Procedures

TA0002 , T1059 

References

https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c81
7f2c5b181/pacu/modules/ec2__startup_shell_script/main.py#L9 

Severity

75

Title

Description

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
stellar.rule_id

Additional Information

Maturity

Creation Date Risk Level False Positives

experimental 2020/02/12

high

Valid changes to the startup script

AWS EC2 Network Access
Control List Creation

Identifies the creation of an AWS Elastic Compute Cloud (EC2) network access control list (ACL)
or an entry in a network ACL with a specified rule number.

More details

Rule ID

aws_30

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': ['CreateNetworkAcl', 'CreateNetworkAclEntry
']}, 'condition': 'selection1 and selection2'}

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

Network ACL's may be created by a network administrator. Verify
whether the user identity, user agent, and/or hostname should be
making changes in your environment. Network ACL creations by
unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS EC2 Network Access
Control List Deletion

Identifies the deletion of an Amazon Elastic Compute Cloud (EC2) network access control list
(ACL) or one of its ingress/egress entries.

More details

Rule ID

aws_45

Title

Description

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': ['DeleteNetworkAcl', 'DeleteNetworkAclEntry
']}, 'condition': 'selection1 and selection2'}

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

Network ACL's may be deleted by a network administrator. Verify
whether the user identity, user agent, and/or hostname should be
making changes in your environment. Network ACL deletions by
unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS EC2 Snapshot
Activity

An attempt was made to modify AWS EC2 snapshot attributes. Snapshots are sometimes shared
by threat actors in order to exfiltrate bulk data from an EC2 fleet. If the permissions were
modified, verify the snapshot was not shared with an unauthorized or unexpected AWS account.

More details

Rule ID

aws_51

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'ModifySnapshotAttribute'}, 'condition': 's
election1 and selection2'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0010 , T1537 

Title

Description

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

Creati
on
Date

2020/
06/24

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

IAM users may occasionally share EC2 snapshots with another
AWS account belonging to the same organization. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS EC2 VM Export
Failure

Identifies an attempt to export an AWS EC2 instance. A virtual machine (VM) export may indicate
an attempt to extract or exfiltrate information.

More details

Rule ID

aws_54

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateInstanceExportTask'}, 'condition': '
selection1 and selection2'}

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

Matu
rity

Creati
on
Date

Risk
Leve
l

low

2021/0
4/22

prod
uctio
n

False Positives

VM exports may be done by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname
should be making changes in your environment. VM exports from

Title

Description

Matu
rity

Creati
on
Date

Risk
Leve
l

False Positives

unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from the
rule.

AWS EC2 Full Network
Packet Capture Detected

Identifies potential Traffic Mirroring in an Amazon Elastic Compute Cloud (EC2) instance. Traffic
Mirroring is an Amazon VPC feature that you can use to copy network traffic from an Elastic
network interface. This feature can potentially be abused to exfiltrate sensitive data from
unencrypted internal traffic.

More details

Rule ID

aws_57

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': ['CreateTrafficMirrorFilter', 'CreateTraffi
cMirrorFilterRule', 'CreateTrafficMirrorSession', 'CreateTraff
icMirrorTarget']}, 'condition': 'selection1 and selection2'}

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

Creati
on
Date

2021/
05/05

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

Traffic Mirroring may be done by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. Traffic
Mirroring from unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted
from the rule.

AWS EC2 Encryption
Disabled

Identifies disabling of Amazon Elastic Block Store (EBS) encryption by default in the current
region. Disabling encryption by default does not change the encryption status of your existing
volumes.

More details

Rule ID

Title

Description

aws_58

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'DisableEbsEncryptionByDefault'}, 'conditio
n': 'selection1 and selection2'}

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

Creati
on
Date

2020/
06/05

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

Disabling encryption may be done by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.
Disabling encryption by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can
be exempted from the rule.

EC2 Snapshot Attribute
Modification

The following analytic utilizes AWS CloudTrail events to identify when an EC2 snapshot
permissions are modified.

More details

Rule ID

aws_76

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'ModifySnapshotAttribute'}, 'condition': 's
election1 and selection2'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0010 , T1537 

Title

Description

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

Maturi
ty

Creation
Date

Risk
Level

produc
tion

2023-03-
20

mediu
m

False Positives

It is possible that an AWS admin has legitimately modified
permissions of EC2 Snapshot.

AWS EC2 Security Group
Deleted

An EC2 security group has been deleted.

More details

Rule ID

aws_77

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'DeleteSecurityGroup'}, 'selection3': {'use
rAgent': 'cloudformation.amazonaws.com'}, 'condition': 'select
ion1 and selection2 and not selection3'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

Title

Description

AWS EC2 Security Group
Modified

An EC2 security group has been modified.

More details

Rule ID

aws_78

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'DeleteRouteTable'}, 'selection3': {'eventN
ame': 'DeleteSubnet'}, 'selection4': {'eventName': 'CreateDBSu
bnetGroup'}, 'selection5': {'eventName': 'DeleteDBSubnetGroup'
}, 'selection6': {'eventName': 'ModifyDBSubnetGroup'}, 'select
ion7': {'userAgent': 'cloudformation.amazonaws.com'}, 'conditi
on': 'selection1 and (selection2 or selection3 or selection4 o
r selection5 or selection6) and not selection7'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

AWS EC2 Security Group
Created

An EC2 security group has been created.

More details

Rule ID

aws_79

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateSecurityGroup'}, 'selection3': {'use
rAgent': 'cloudformation.amazonaws.com'}, 'condition': 'select
ion1 and selection2 and not selection3'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Title

Description

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

AWS Credential Access
GetPasswordData

This detection analytic identifies GetPasswordData API call made to your AWS account. Attackers
can retrieve the encrypted administrator password for a running Windows instance.

More details

Rule ID

aws_88

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'GetPasswordData'}, 'condition': 'selection
1 and selection2'}

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

Maturity Creation

Date

Risk
Level

producti
on

2022-08-10 medium

False Positives

Administrator tooling or automated scripts may
make these calls

Title

Description

AWS VPC Network ACL
Modified

The ACL for a VPC has been modified.

More details

Rule ID

aws_104

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selectio
n2': {'eventName': 'CreateACLEntry'}, 'selection3': {'eventNam
e': 'DeleteACL'}, 'selection4': {'eventName': 'DeleteACLEntry'
}, 'selection5': {'eventName': 'UpdateACLAssociation'}, 'selec
tion6': {'userAgent': 'cloudformation.amazonaws.com'}, 'condit
ion': 'selection1 and (selection2 or selection3 or selection4
or selection5) and not selection6'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

