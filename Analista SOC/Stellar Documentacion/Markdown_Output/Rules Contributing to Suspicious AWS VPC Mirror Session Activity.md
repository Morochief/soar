Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS VPC
Mirror Session Activity

The following rules are used to identify suspicious AWS VPC mirror session activity. Any one or
more of these will trigger Suspicious AWS VPC Mirror Session Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Update VPC
Mirror created

A VPC mirror session has been created.

Description

More details

Rule ID

aws_107

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'
eventName': 'CreateTrafficMirrorSession'}, 'selection3': {'userIdenti
ty_sessionContext_sessionIssuer_userName': ''}, 'condition': 'selecti
on1 and selection2 and not selection3'}

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

Title

Description

Additional Information

Maturity

Creation Date

test

2022/01/05

Risk Level

medium

False Positives

N/A

Update VPC
Mirror deleted

A VPC mirror session has been deleted.

More details

Rule ID

aws_108

Query

{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'
eventName': 'DeleteTrafficMirrorSession'}, 'selection3': {'eventName'
: 'DeleteTrafficMirrorTarget'}, 'selection4': {'eventName': 'DeleteTr
afficMirrorFilter'}, 'selection5': {'userIdentity_sessionContext_sess
ionIssuer_userName': ''}, 'condition': 'selection1 and (selection2 or
 selection3 or selection4) and not selection5'}

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

Maturity

Creation Date

test

2022/01/05

Risk Level

medium

False Positives

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

