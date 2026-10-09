✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Suspicious AWS EBS
Activity Alert
The following rules are used to identify suspicious AWS EBS activity. Any one or more of these
will trigger Suspicious AWS EBS Activity Alert. Details for each rule can be viewed by clicking the
More Details link in the description.
Title Description
EBS Snapshot A copy of an EBS volume has been created.
Created
More details
Rule ID
aws_96
Query
{'selection1': {'eventSource': 'ec2.amazonaws.com'}, 'selection2': {'e
ventName': 'CreateSnapshots'}, 'selection3': {'eventName': 'BackupEBSV
olume'}, 'condition': 'selection1 and (selection2 or selection3)'}
Log Source
Stellar Cyber AWS configured.
Rule Source
Developed internally by Stellar Cyber
Tactics, Techniques, and Procedures
TA0009 , T1074 
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