✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to AWS High-Risk Ports
Exposed to Internet Alert
The following rules are used to detect AWS security group rules that expose high-risk ports to the
Internet. Any one or more of these will trigger the AWS High-Risk Ports Exposed to Internet Alert.
Details for each rule can be viewed by clicking the More Details link in the description.
Title Description
AWS High-Risk Ports Identifies when a specified inbound (ingress) rule is added or adjusted for a VPC security group in
Exposed to Internet AWS EC2 that allows traffic from any IP address to common remote access ports.
More details
Rule ID
aws_config_1
Query
{'selection1': {'configResourceType': 'AWS::EC2::SecurityGroup'}
, 'selection2': {'ipPermissions_fromPort': [22, 3389, 389, 445],
'ipPermissions_ipRanges': ['0.0.0.0/0', '::/0']}, 'condition':
'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0005 , T1562.007 
References
https://www.linkedin.com/pulse/my-backdoors-your-aws-infrastructure-part-3-network-
micha%C5%82-brygidyn/ 
Severity
50
Suppression Logic Based On
aws.configurationItem.ARN
aws.configurationItem.configuration.ipPermissions.fromPort

Title Description
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2025/12/17    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        