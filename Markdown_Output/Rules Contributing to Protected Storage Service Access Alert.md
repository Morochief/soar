Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Protected Storage Service
Access Alert

The following rules detect suspicious SMB traffic accessing protected storage services. Any one
or more of these will trigger the Protected Storage Service Access Alert. Details for each rule can
be viewed by clicking the More Details link in the description.

Title

Description

Protected Storage
Service Access

Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract
domain backup keys from Domain Controllers

More details

Rule ID

network_security_5

Query

{'selection': {'appid_name': 'smb', 'metadata|re': "'request'\\s*:\
\s*\\{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*protected_storage[^']*'[^}]*'co
mmand'\\s*:\\s*9[^}]*\\}"}, 'condition': 'selection'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References

https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 

Severity

75

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

2024/07/13

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

