Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS VPC
Flow Logs Modification Alert

The following rules are used to identify suspicious modification of AWS VPC Flow logs. Any one
or more of these will trigger Suspicious AWS VPC Flow Logs Modification Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Description

AWS VPC Flow
Logs Deletion

Identifies the deletion of one or more flow logs in AWS Elastic Compute Cloud (EC2). An adversary may
delete flow logs in an attempt to evade defenses.

More details

Rule ID

aws_66

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {
'eventName': 'DeleteFlowLogs'}, 'condition': 'selection1 and selecti
on2'}

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

Title

Description

Additional Information

Risk
Level

high

Creati
on
Date

2020/0
6/15

Matu
rity

prod
uctio
n

False Positives

Verify whether the user identity, user agent, and/or hostname should be
making changes in your environment. Flow log deletions by unfamiliar
users or hosts should be investigated. If known behavior is causing false
positives, it can be exempted from the rule.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

