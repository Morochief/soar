Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS Root
Account Activity Alert

The following rules are used to identify suspicious activity with AWS Root Account. Any one or
more of these will trigger the Suspicious AWS Root Account Activity Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Title

Description

AWS Root Credentials Detects AWS root account usage

More details

Rule ID

aws_12

Query

{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selectio
n_usertype': {'userIdentity_type': 'Root'}, 'selection_eventtype'
: {'eventType': 'AwsServiceEvent'}, 'condition': 'selection1 and
selection_usertype and not selection_eventtype'}

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

Title

Description

service_id
aws.eventSource
aws.eventName
stellar.rule_id

Additional Information

Mat
urity

Creatio
n Date

Risk
Level

test 2020/0

1/21

mediu
m

False Positives

AWS Tasks That Require AWS Account Root User Credentials
https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-
require-root.html

AWS Management
Console Root Login

Identifies a successful login to the AWS Management Console by the Root user.

More details

Rule ID

aws_31

Query

{'selection1': {'eventSource': 'signin.amazonaws.com'}, 'selectio
n2': {'eventName': 'ConsoleLogin'}, 'selection3': {'userIdentity_
type': 'Root'}, 'condition': 'selection1 and selection2 and selec
tion3'}

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

Matu
rity

Creati
on
Date

Risk
Level

2020/0
6/11

medi
um

prod
uctio
n

False Positives

It's strongly recommended that the root user is not used for everyday
tasks, including the administrative ones. Verify whether the IP
address, location, and/or hostname should be logging in as root in
your environment. Unfamiliar root logins should be investigated
immediately. If known behavior is causing false positives, it can be
exempted from the rule.

Root access key
created

An access key was created for the root account.

More details

Rule ID

Title

Description

aws_109

Query

{'selection1': {'eventSource': 'cloudtrail.amazonaws.com'}, 'sele
ction2': {'userIdentity_type': 'Root'}, 'selection3': {'eventName
': 'CreateAccessKey'}, 'condition': 'selection1 and selection2 an
d selection3'}

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

