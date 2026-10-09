Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Remote Task Creation via
ATSVC Named Pipe Alert

The following rules detect suspicious SMB traffic accessing ATSVC named pipes. Any one or
more of these will trigger the Remote Task Creation via ATSVC Named Pipe Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Remote Task Creation via
ATSVC Named Pipe

Detects remote task creation via at.exe or API interacting with ATSVC namedpipe

More details

Rule ID

network_security_7

Query

{'selection': {'appid_name': 'smb', 'metadata|contains': ['IPC$
']}, 'selection_atsvc': {'metadata|re': "'request'\\s*:\\s*\\
{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*atsvc[^']*'[^}]*'command'\\
s*:\\s*9[^}]*\\}"}, 'condition': 'selection and selection_atsvc
'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1053.002 

References
N/A

Severity

50

Suppression Logic Based On

Title

Description

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

2024/07/09

medium

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

