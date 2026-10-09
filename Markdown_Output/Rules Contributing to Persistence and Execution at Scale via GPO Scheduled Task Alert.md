Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Persistence and Execution
at Scale via GPO Scheduled Task Alert

The following rules detect suspicious SMB traffic related to GPO scheduled task creation/access.
Any one or more of these will trigger the Persistence and Execution at Scale via GPO Scheduled
Task Alert. Details for each rule can be viewed by clicking the More Details link in the
description.

Title

Description

Persistence and Execution at
Scale via GPO Scheduled Task

Detect lateral movement using GPO scheduled task, usually used to deploy ransomware at
scale

More details

Rule ID

network_security_9

Query

{'selection': {'appid_name': 'smb', 'metadata|re': "'reques
t'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*ScheduledTasks\\.xml[^'
]*'[^}]*'command'\\s*:\\s*9[^}]*\\}"}, 'condition': 'select
ion'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network
traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1053.005 

References

https://twitter.com/menasec1/status/1106899890377052160 

https://www.secureworks.com/blog/ransomware-as-a-distraction 

Severity

Title

Description

75

Suppression Logic Based On

appid_name
srcip
dstip
dstip_host
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2024/07/05

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

