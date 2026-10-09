✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to AWS IAM Policy with
Wildcard Privileges Alert
The following rules are used to detect IAM policies granting excessive permissions via wildcards.
Any one or more of these will trigger the AWS IAM Policy with Wildcard Privileges Alert. Details
for each rule can be viewed by clicking the More Details link in the description.
Title Description
AWS IAM Policy with Detects IAM policies that grant excessive privileges using wildcard (*) in either the Action or
Wildcard Privileges Resource fields. Policies with Action set to "*" or "*:*" grant full permissions to all AWS services and
operations. Policies with Resource set to "*" allow actions on all resources. This violates the
principle of least privilege and can lead to privilege escalation and unauthorized access to sensitive
resources.
More details
Rule ID
aws_config_3
Query
{'selection1': {'configResourceType': 'AWS::IAM::Policy'}, 'sele
ction2': {'policyVersionList|contains': ["'Resource': '*'", "'Ac
tion': '*'", "'Action': '*:*'"]}, 'condition': 'selection1 and s
election2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0004 , T1078.004 
References
N/A
Severity
70

Title Description
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/12/17    | high       | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        