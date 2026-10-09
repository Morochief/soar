Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to DCERPC SMB Spoolss
Named Pipe Alert

The following rules detect suspicious SMB traffic accessing Spoolss named pipes. Any one or
more of these will trigger the DCERPC SMB Spoolss Named Pipe Alert. Details for each rule can
be viewed by clicking the More Details link in the description.

Title

Description

DCERPC SMB
Spoolss Named Pipe

Detects the use of the spoolss named pipe over SMB. This can be used to trigger the authentication
via NTLM of any machine that has the spoolservice enabled.

More details

Rule ID

network_security_8

Query

{'selection': {'appid_name': 'smb', 'metadata|contains|all': ['IP
C$']}, 'selection_spoolss': {'metadata|re': "'request'\\s*:\\s*\\
{[^}]*
(?:'filename'|'path')\\s*:\\s*'[^']*spoolss[^']*'[^}]*'command'\\
s*:\\s*9[^}]*\\}"}, 'condition': 'selection and selection_spoolss
'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References

https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-
trusts-71f2b33688e1 

https://dirkjanm.io/a-different-way-of-abusing-zerologon/ 

https://twitter.com/_dirkjan/status/1309214379003588608 

Title

Description

Severity

50

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

N/A

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

