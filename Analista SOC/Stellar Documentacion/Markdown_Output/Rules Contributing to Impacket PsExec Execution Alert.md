✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Rules Contributing to Impacket PsExec
Execution Alert
The following rules detect suspicious SMB traffic related to Impacket PsExec execution. Any one
or more of these will trigger the Impacket PsExec Execution Alert. Details for each rule can be
viewed by clicking the More Details link in the description.
Title Description
Impacket PsExec Detects execution of Impacket's psexec.py.
Execution
More details
Rule ID
network_security_10
Query
{'selection_protocol': {'appid_name': 'smb'}, 'selection_sharename':
{'metadata|contains': ['IPC$']}, 'selection_relative_target_name': {'
metadata|contains': ['RemCom_stdin', 'RemCom_stdout', 'RemCom_stderr'
]}, 'condition': 'all of selection_*'}
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
srcip
dstip

Title Description
dstip_host
stellar.rule_id
Additional Information
| Maturity     | Creation Date | Risk Level | False Positives |
| ------------ | ------------- | ---------- | --------------- |
| experimental | 2024/07/09    | high       |                 |
Unknown
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        