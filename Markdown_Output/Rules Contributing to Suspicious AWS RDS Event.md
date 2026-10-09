Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS RDS
Event

The following rules are used to identify suspicious activity related to AWS RDS events. Any one
or more of these will trigger Suspicious AWS RDS Event Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

Restore Public AWS
RDS Instance

Detects the recovery of a new public database instance from a snapshot. It may be a part of data
exfiltration.

More details

Rule ID

aws_1

Query

{'selection_source': {'eventSource': 'rds.amazonaws.com', 'respo
nseElements_publiclyAccessible': True, 'eventName': 'RestoreDBIn
stanceFromDBSnapshot'}, 'condition': 'selection_source'}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,c3f265c7-ff03-4056-8ab2-d486227b4599

Author: faloker

Tactics, Techniques, and Procedures

TA0010 , T1020 

References

https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2
c5b181/pacu/modules/rds__explore_snapshots/main.py 

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

Creation Date

Risk Level

False Positives

test

2020/02/12

high

Unknown

AWS RDS Master
Password Change

Detects the change of database master password. It may be a part of data exfiltration.

More details

Rule ID

aws_14

Query

{'selection_source': {'eventSource': 'rds.amazonaws.com', 'respo
nseElements_pendingModifiedValues_masterUserPassword|contains':
'*', 'eventName': 'ModifyDBInstance'}, 'condition': 'selection_s
ource'}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,8a63cdd4-6207-414a-85bc-7e032bd3c1a2

Author: faloker

Tactics, Techniques, and Procedures

TA0010 , T1020 

References

https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2
c5b181/pacu/modules/rds__explore_snapshots/main.py 

Severity

50

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
stellar.rule_id

Additional Information

AWS RDS Snapshot
Export

Maturity

Creation Date

Risk Level

False Positives

experimental

2020/02/12

medium

Benign changes to a db instance

Identifies the export of an Amazon Relational Database Service (RDS) Aurora database snapshot.

More details

Rule ID

aws_21

Query

Title

Description

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': 'StartExportTask'}, 'condition': 'selection1 an
d selection2'}

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

Risk
Leve
l

low

Creati
on
Date

2021/0
6/06

Matu
rity

prod
uctio
n

False Positives

Exporting snapshots may be done by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.
Snapshot exports from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

AWS RDS Cluster
Creation

Identifies the creation of a new Amazon Relational Database Service (RDS) Aurora DB cluster or
global database spread across multiple regions.

More details

Rule ID

aws_36

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': ['CreateDBCluster', 'CreateGlobalCluster']}, 'c
ondition': 'selection1 and selection2'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1133 

References
N/A

Title

Description

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
5/20

prod
uctio
n

False Positives

Valid clusters may be created by a system or network administrator.
Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment. Cluster creations by
unfamiliar users or hosts should be investigated. If known behavior
is causing false positives, it can be exempted from the rule.

AWS RDS Snapshot
Restored

Identifies when an attempt was made to restore an RDS Snapshot. Snapshots are sometimes
shared by threat actors in order to exfiltrate bulk data or evade detection after performing malicious
activities. If the permissions were modified, verify if the snapshot was shared with an unauthorized or
unexpected AWS account.

More details

Rule ID

aws_59

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': 'RestoreDBInstanceFromDBSnapshot', 'responseEle
ments_publiclyAccessible': False}, 'condition': 'selection1 and
selection2'}

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

Matu
rity

Creati
on
Date

Risk
Level

prod
uctio

2021/0
6/29

medi
um

False Positives

Restoring snapshots may be done by a system or network
administrator. Verify whether the user identity, user agent, and/or

Title

Description

AWS RDS
Instance/Cluster
Stoppage

Matu
rity

Creati
on
Date

Risk
Level

n

False Positives

hostname should be making changes in your environment.
Snapshot restoration by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Identifies that an Amazon Relational Database Service (RDS) cluster or instance has been stopped.

More details

Rule ID

aws_60

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': ['StopDBCluster', 'StopDBInstance']}, 'conditio
n': 'selection1 and selection2'}

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

Matu
rity

Creati
on
Date

Risk
Level

2020/0
5/20

medi
um

prod
uctio
n

False Positives

Valid clusters or instances may be stopped by a system
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. Cluster
or instance stoppages from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

AWS Deletion of RDS
Instance or Cluster

Identifies the deletion of an Amazon Relational Database Service (RDS) Aurora database cluster,
global database cluster, or database instance.

More details

Rule ID

aws_64

Query

Title

Description

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': ['DeleteDBCluster', 'DeleteGlobalCluster', 'Del
eteDBInstance']}, 'condition': 'selection1 and selection2'}

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

Matu
rity

Creati
on
Date

Risk
Level

2020/0
5/21

medi
um

prod
uctio
n

False Positives

Clusters or instances may be deleted by a system administrator.
Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment. Cluster or instance
deletions by unfamiliar users or hosts should be investigated. If
known behavior is causing false positives, it can be exempted from
the rule.

AWS RDS Security
Group Deletion

Identifies the deletion of an Amazon Relational Database Service (RDS) Security group.

More details

Rule ID

aws_65

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': 'DeleteDBSecurityGroup'}, 'condition': 'selecti
on1 and selection2'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0040 , T1531 

References
N/A

Severity

Title

Description

25

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
stellar.rule_id

Additional Information

AWS RDS Instance
Creation

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
6/05

prod
uctio
n

False Positives

An RDS security group deletion may be done by a system or
network administrator. Verify whether the user identity, user agent,
and/or hostname should be making changes in your environment.
Security group deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Identifies the creation of an Amazon Relational Database Service (RDS) Aurora database instance.

More details

Rule ID

aws_68

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': 'CreateDBInstance'}, 'condition': 'selection1 a
nd selection2'}

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

Risk
Leve
l

low

Creati
on
Date

2021/0
6/06

Matu
rity

prod
uctio
n

False Positives

A database instance may be created by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment.
Instances creations by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Title

Description

AWS RDS Snapshot
Created

A copy of an AWS RDS database has been created.

More details

Rule ID

aws_97

Query

{'selection1': {'eventSource': 'rds.amazonaws.com'}, 'selection2
': {'eventName': 'CreateDBSnapshot'}, 'condition': 'selection1 a
nd selection2'}

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

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

AWS RDS Security
Group Modified

A RDS security group has been modified.

More details

Rule ID

aws_103

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2
': {'eventName': 'AuthorizeDBSecurityGroupIngress'}, 'selection3
': {'eventName': 'RevokeDBSecurityGroupIngress'}, 'selection4':
{'eventName': 'AuthorizeDBSecurityGroupEgress'}, 'selection5': {
'eventName': 'RevokeDBSecurityGroupEgress'}, 'selection6': {'use
rAgent': 'cloudformation.amazonaws.com'}, 'condition': 'selectio
n1 and (selection2 or selection3 or selection4 or selection5) an
d not selection6'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Title

Description

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

