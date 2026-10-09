Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious PsExec
Execution Alert

The following rules detect suspicious SMB traffic related to PsExec Execution activities. Any one
or more of these will trigger the Suspicious PsExec Execution Alert. Details for each rule can be
viewed by clicking the More Details link in the description.

Title

Description

Suspicious
PsExec Execution

detects execution of psexec or paexec with renamed service name, this rule helps to filter out the noise if
psexec is used for legit purposes or if attacker uses a different psexec client other than sysinternal one

More details

Rule ID

network_security_11

Query

{'selection': {'appid_name': 'smb', 'metadata|contains': ['-
stdin', '-stdout', '-
stderr']}, 'filter': {'metadata|contains': 'PSEXESVC'}, 'condition':
 'selection and not filter'}

Log Source

Stellar Cyber Network Events configured for:

Requirements: Network/Security/Modular sensor must be able to capture network traffic

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References
N/A

Severity

75

Suppression Logic Based On

appid_name

Title

Description

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

