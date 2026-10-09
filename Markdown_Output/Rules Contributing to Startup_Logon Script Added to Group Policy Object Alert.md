Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Startup/Logon Script
Added to Group Policy Object Alert

The following rules detect suspicious SMB traffic related to GPO script modifications. Any one or
more of these will trigger the Startup/Logon Script Added to Group Policy Object Alert. Details for
each rule can be viewed by clicking the More Details link in the description.

Title

Description

Startup/Logon Script added
to Group Policy Object

Detects the modification of Group Policy Objects (GPO) to add a startup/logon script to users or
computer objects.

More details

Rule ID

network_security_6

Query

{'selection_protocol': {'appid_name': 'smb'}, 'selection_share
': {'metadata|contains': 'Policies'}, 'selection_relative_targ
et_name': {'metadata|re': "'request'\\s*:\\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*scripts\\.ini[^']*'[^}]*'c
ommand'\\s*:\\s*9[^}]*\\}"}, 'condition': 'all of selection*'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network
traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0003 , T1547 , TA0005 , T1484 

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

2024/07/05

medium

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

