Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Windows Network Access
Suspicious desktop.ini Action Alert

The following rules detect suspicious SMB traffic accessing desktop.ini files. Any one or more of
these will trigger the Windows Network Access Suspicious desktop.ini Action Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Windows Network Access
Suspicious desktop.ini Action

Detects unusual processes accessing desktop.ini remotely over network share, which can be
leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without
changing them on disk.

More details

Rule ID

network_security_3

Query

{'selection': {'appid_name': 'smb', 'metadata|re': "'request
'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*desktop\\.ini[^']*'[^}]*
'command'\\s*:\\s*9[^}]*\\}"}, 'condition': 'selection'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network
traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1547.009 

References

https://isc.sans.edu/forums/diary/Desktopini+as+a+postexploitation+tool/25912/ 

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

