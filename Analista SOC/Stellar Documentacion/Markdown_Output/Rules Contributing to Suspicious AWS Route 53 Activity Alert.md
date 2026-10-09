Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS Route 53
Activity Alert

The following rules are used to identify suspicious activity within AWS Route 53 logs. Any one or
more of these will trigger Suspicious AWS Route 53 Activity Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

AWS Route53 private hosted
zone associated with a VPC

Identifies when a Route53 private hosted zone has been associated with VPC.

More details

Rule ID

aws_32

Query

{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'se
lection2': {'eventName': 'AssociateVPCWithHostedZone'}, 'con
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

Creati
on
Date

Risk
Leve
l

low

2021/
07/19

Mat
urity

prod
uctio
n

False Positives

A private hosted zone may be asssociated with a VPC by a
system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making
changes in your environment. If known behavior is causing
false positives, it can be exempted from the rule.

AWS Route 53 Domain
Transfer Lock Disabled

Identifies when a transfer lock was removed from a Route 53 domain. It is recommended to
refrain from performing this action unless intending to transfer the domain to a different
registrar.

More details

Rule ID

aws_35

Query

{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'se
lection2': {'eventName': 'DisableDomainTransferLock'}, 'cond
ition': 'selection1 and selection2'}

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

Creati
on
Date

Risk
Leve
l

low

2021/
05/10

Mat
urity

prod
uctio
n

False Positives

A domain transfer lock may be disabled by a system or
network administrator. Verify whether the user identity, user
agent, and/or hostname should be making changes in your
environment. Activity from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it
can be exempted from the rule.

Identifies when a request has been made to transfer a Route 53 domain to another AWS
account.

More details

Rule ID

AWS Route 53 Domain
Transferred to Another
Account

Title

Description

aws_63

Query

{'selection1': {'eventSource': 'route53.amazonaws.com'}, 'se
lection2': {'eventName': 'TransferDomainToAnotherAwsAccount'
}, 'condition': 'selection1 and selection2'}

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

Creati
on
Date

Risk
Leve
l

low

2021/
05/10

Mat
urity

prod
uctio
n

False Positives

A domain may be transferred to another AWS account by a
system or network administrator. Verify whether the user
identity, user agent, and/or hostname should be making
changes in your environment. Domain transfers from
unfamiliar users or hosts should be investigated. If known
behavior is causing false positives, it can be exempted from
the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

