Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious AWS Bucket
Enumeration Alert

The following rules are used to identify suspicious activity related to AWS Bucket enumeration.
Any one or more of these will trigger AWS Bucket Enumeration Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

Potential Bucket
Enumeration on AWS

Looks for potential enumeration of AWS buckets via ListBuckets.

More details

Rule ID

aws_6

Query

{'selection': {'eventSource': 'ec2.amazonaws.com', 'eventName': '
ListBuckets'}, 'filter': {'type': 'AssumedRole'}, 'condition': 's
election and not filter'}

Log Source

Stellar Cyber AWS configured for:

AWS Cloudtrail

Rule Source

SigmaHQ,f305fd62-beca-47da-ad95-7690a0620084

Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io

Tactics, Techniques, and Procedures

TA0007 , T1580 

References

https://github.com/Lifka/hacking-
resources/blob/c2ae355d381bd0c9f0b32c4ead049f44e5b1573f/cloud-hacking-cheat-
sheets.md 

https://jamesonhacking.blogspot.com/2020/12/pivoting-to-private-aws-s3-buckets.html 

https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/ 

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

Maturit
y

Creation
Date

Risk
Level

experim
ental

2023/01/
06

low

False Positives

Administrators listing buckets, it may be necessary to filter out
users who commonly conduct this activity.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

