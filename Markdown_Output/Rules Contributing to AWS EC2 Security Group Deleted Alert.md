✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to AWS EC2 Security Group
Deleted Alert
The following rules are used to detect the deletion of an AWS EC2 security group. Any one or
more of these will trigger the AWS EC2 Security Group Deleted Alert. Details for each rule can be
viewed by clicking the More Details link in the description.
Title Description
AWS Security Group Detects the deletion of AWS EC2 Security Groups. Unexpected deletion of Security Groups may
Deletion Detected indicate misconfiguration, operational errors, or malicious activity aimed at disrupting network
security controls or creating gaps in security posture.
More details
Rule ID
aws_config_4
Query
{'selection1': {'configResourceType': 'AWS::EC2::SecurityGroup'}
, 'selection2': {'configurationItemStatus': 'ResourceDeleted'},
'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
N/A
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id

Title Description
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/12/17    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        