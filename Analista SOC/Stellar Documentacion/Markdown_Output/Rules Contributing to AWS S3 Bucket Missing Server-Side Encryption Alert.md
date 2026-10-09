✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to AWS S3 Bucket Missing
Server-Side Encryption Alert
The following rules are used to detect S3 buckets without server-side encryption. Any one or
more of these will trigger the AWS S3 Bucket Missing Server-Side Encryption Alert. Details for
each rule can be viewed by clicking the More Details link in the description.
Title Description
AWS S3 Bucket Missing Detects S3 buckets that lack server-side encryption (SSE) configuration. Without SSE enabled,
Server-Side Encryption data stored in S3 buckets is vulnerable to unauthorized access if the bucket permissions are
misconfigured or if physical media is compromised.
More details
Rule ID
aws_config_6
Query
{'selection1': {'configResourceType': 'AWS::S3::Bucket'}, 'sel
ection2': {'serverSideEncryptionConfiguration': ''}, 'selectio
n3': {'serverSideEncryptionConfiguration_sseAlgorithm': ''}, '
condition': 'selection1 and (not selection2) and selection3'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1530 
References
N/A
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule id

_
Title Description
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/12/17    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        