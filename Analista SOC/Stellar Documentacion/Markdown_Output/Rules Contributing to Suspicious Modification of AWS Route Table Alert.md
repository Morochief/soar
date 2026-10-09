Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Modification of
AWS Route Table Alert

The following rules are used to identify suspicious activity related to modification of AWS route
table. Any one or more of these will trigger Suspicious Modification of AWS Route Table Alert.
Details for each rule can be viewed by clicking the More Details link in the description.

Title

AWS Route Table
Created

Identifies when an AWS Route Table has been created.

Description

More details

Rule ID

aws_18

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'sele
ction2': {'eventName': ['CreateRoute', 'CreateRouteTable']}, 'con
dition': 'selection1 and selection2'}

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

Title

Description

Additional Information

Risk
Leve
l

low

Creati
on
Date

2021/0
6/05

Matu
rity

prod
uctio
n

False Positives

Route Tables may be created by a system or network administrators.
Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment. Route Table creation by
unfamiliar users or hosts should be investigated. If known behavior is
causing false positives, it can be exempted from the rule. Automated
processes that use Terraform may lead to false positives.

AWS Route Table
Modified or Deleted

Identifies when an AWS Route Table has been modified or deleted.

More details

Rule ID

aws_29

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'sele
ction2': {'eventName': ['ReplaceRoute', 'ReplaceRouteTableAssocia
tion', 'DeleteRouteTable', 'DeleteRoute', 'DisassociateRouteTable
']}, 'condition': 'selection1 and selection2'}

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

Risk
Leve
l

low

Creati
on
Date

2021/0
6/05

Matu
rity

prod
uctio
n

False Positives

Route Table could be modified or deleted by a system administrator.
Verify whether the user identity, user agent, and/or hostname should
be making changes in your environment. Route Table being modified
from unfamiliar users should be investigated. If known behavior is
causing false positives, it can be exempted from the rule. Also
automated processes that use Terraform may lead to false positives.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

