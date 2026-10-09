Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Modification of
S3 Bucket Alert

The following rules are used to identify suspicious activity within S3 Bucket logs. Any one or
more of these will trigger the Suspicious Modification of S3 Bucket Alert. Details for each rule can
be viewed by clicking the More Details link in the description.

Title

Description

AWS S3 Data
Management Tampering

Detects when a user tampers with S3 data management in Amazon Web Services.

More details

Rule ID

aws_11

Query

{'selection': {'eventSource': 's3.amazonaws.com', 'eventName': [
'PutBucketLogging', 'PutBucketWebsite', 'PutEncryptionConfigurat
ion', 'PutLifecycleConfiguration', 'PutReplicationConfiguration'
, 'ReplicateObject', 'RestoreObject']}, 'condition': 'selection'
}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,78b3756a-7804-4ef7-8555-7b9024a02e2d

Author: Austin Songer @austinsonger

Tactics, Techniques, and Procedures

TA0010 , T1537 

References

https://github.com/elastic/detection-rules/pull/1145/files 

https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html 

https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html 

https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html 

Title

Description

https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html 

https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-
overview.html 

https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html 

Severity

25

Suppression Logic Based On

service_id
aws.eventSource
aws.eventName
stellar.rule_id

Additional Information

Mat
urit
y

Creati
on
Date

Risk
Leve
l

test 2021/0

low

7/24

False Positives

A S3 configuration change may be done by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. S3
configuration change from unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

AWS S3 Bucket
Configuration Deletion

Identifies the deletion of various Amazon Simple Storage Service (S3) bucket configuration
components.

More details

Rule ID

aws_37

Query

{'selection1': {'eventSource': 's3.amazonaws.com'}, 'selection2'
: {'eventName': ['DeleteBucketPolicy', 'DeleteBucketReplication'
, 'DeleteBucketCors', 'DeleteBucketEncryption', 'DeleteBucketLif
ecycle']}, 'condition': 'selection1 and selection2'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1070 

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

low

2020/0
5/27

prod
uctio
n

False Positives

Bucket components may be deleted by a system or network
administrator. Verify whether the user identity, user agent, and/or
hostname should be making changes in your environment. Bucket
component deletions by unfamiliar users or hosts should be
investigated. If known behavior is causing false positives, it can be
exempted from the rule.

Modification of AWS S3
Access Control List

This search detects modification of Access Control List of an S3 Bucket.

More details

Rule ID

aws_92

Query

{'selection2': {'eventSource': 's3.amazonaws.com'}, 'selection3'
: {'eventName': 'PutBucketAcl'}, 'condition': 'selection2 and se
lection3'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0009 , T1530 

References
N/A

Severity

60

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

production

2021-07-19

medium

Unknown

AWS Defense Evasion
PutBucketLifecycle

This analytic identifies `PutBucketLifecycle` events in CloudTrail logs where a user has created a
new lifecycle rule for an S3 bucket with a short expiration period.

More details

Rule ID

aws_113

Query

{'selection1': {'eventSource': 's3.amazonaws.com'}, 'selection2'
: {'eventName': 'PutBucketLifecycle'}, 'selection3': {'userIdent
ity_type': 'IAMUser'}, 'selection4': {'errorCode': 'success'}, '

Title

Description

condition': 'selection1 and selection2 and selection3 and select
ion4'}

Log Source

Stellar Cyber AWS configured.

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0005 , T1562.008 

References

https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-
lifecycle-rule/ 

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

2022-
07-25

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

While this search has no known false positives, it is possible that it
is a legitimate admin activity. Please consider filtering out these
noisy events using userAgent, user_arn field names.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

