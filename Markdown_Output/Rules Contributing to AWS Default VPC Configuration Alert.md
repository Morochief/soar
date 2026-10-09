✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to AWS Default VPC
Configuration Alert
The following rules are used to detect the use of AWS default VPC settings. Any one or more of
these will trigger the AWS Default VPC Configuration Alert. Details for each rule can be viewed
by clicking the More Details link in the description.
Title Description
AWS Default Detects the use of AWS default VPCs. Default VPCs are automatically created by AWS in each region and
VPC Usage come with preconfigured network settings that may not align with security best practices. They often have
permissive default security groups, automatic public IP assignment, and Internet gateway configurations that
can lead to unintended exposure of resources.
More details
Rule ID
aws_config_5
Query
{'selection1': {'configResourceType': 'AWS::EC2::VPC'}, 'selection2':
{'configuration_isDefault': True}, 'condition': 'selection1 and sele
ction2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0001 , T1190 
References
N/A
Severity
25
Suppression Logic Based On
aws.configurationItem.ARN
stellar.rule id

_
Title Description
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/12/17    | low        | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        