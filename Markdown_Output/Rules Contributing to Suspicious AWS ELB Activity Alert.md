✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious AWS ELB
Activity Alert
The following rules are used to identify suspicious activity with AWS ELB. Any one or more of
these will trigger the Suspicious AWS ELB Activity Alert. Details for each rule can be viewed by
clicking the More Details link in the description.
Title Description
AWS ELB Security Identifies the modification of an ELB security group.
Group Modified
More details
Rule ID
aws_98
Query
{'selection1': {'eventSource': 'elasticloadbalancing.amazonaws.com
'}, 'selection2': {'eventName': 'ApplySecurityGroupsToLoadBalancer
'}, 'condition': 'selection1 and selection2'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0003 , T1098 
References
N/A
Severity
50
Suppression Logic Based On
service_id
aws.eventSource
aws.eventName
stellar.rule_id

Title Description
Additional Information
| Maturity | Creation Date | Risk Level | False Positives |
| -------- | ------------- | ---------- | --------------- |
| test     | 2022/01/05    | medium     | N/A             |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        