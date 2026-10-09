Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS SSL
Certificate Activity Alert

The following rules are used to identify suspicious activity with AWS SSL certificate. Any one or
more of these will trigger a Suspicious AWS SSL Certificate Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Update SSL
Certificate Created

A new SSL certificate has been created in your environment.

Description

More details

Rule ID

aws_99

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2':
{'eventName': 'UploadServerCertificate'}, 'condition': 'selection1
and selection2'}

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

Title

Description

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2022/01/05

medium

N/A

Update SSL
Certificate Deleted

A certificate used for establishing SSL connection in your environment has been deleted.

More details

Rule ID

aws_100

Query

{'selection1': {'eventSource': 'iam.amazonaws.com'}, 'selection2':
{'eventName': 'DeleteServerCertificate'}, 'condition': 'selection1
and selection2'}

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

