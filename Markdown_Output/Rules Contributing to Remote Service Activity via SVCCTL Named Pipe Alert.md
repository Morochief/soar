Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Remote Service Activity
via SVCCTL Named Pipe Alert

The following rules detect suspicious SMB traffic accessing SVCCTL named pipes. Any one or
more of these will trigger the Remote Service Activity via SVCCTL Named Pipe Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Remote Service Activity via
SVCCTL Named Pipe

Detects remote service activity via remote access to the svcctl named pipe

More details

Rule ID

network_security_12

Query

{'selection': {'appid_name': 'smb', 'metadata|contains': ['IPC
$']}, 'selection_svcctl': {'metadata|re': "'request'\\s*:\\s*\
\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*svcctl[^']*'[^}]*'command'
\\s*:\\s*9[^}]*\\}"}, 'condition': 'selection and selection_sv
cctl'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network
traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References
N/A

Severity

50

Title

Description

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

2024/07/13

medium

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

