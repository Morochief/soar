Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Connection to
Another Process Alerts

The following rules are used to identify suspicious connection to another process. Any one or
more of these will trigger Suspicious Connection to Another Process Alert. Details for each rule
can be viewed by clicking the More Details link in the description.

Windows Events Required: 5156

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Remote PowerShell Sessions
Network Connections (WinRM)

Detects basic PowerShell Remoting (WinRM) by monitoring for network inbound connections
to ports 5985 OR 5986

More details

Rule ID

windows_security_166

Query

{'selection': {'EventID': 5156, 'DestPort': ['5985', '5986'
], 'LayerRTID': '44'}, 'filter': {'Application': ['System']
}, 'condition': 'selection and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,13acf386-b8c6-4fe0-9a6e-c4756b974698

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0002 , T1059.001 

References

https://threathunterplaybook.com/hunts/windows/190511-
RemotePwshExecution/notebook.html 

Title

Description

Severity

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturit
y

Creation
Date

Risk
Level

test

2019/09/12

high

False Positives

Legitimate use of remote PowerShell
execution

Suspicious Outbound Kerberos
Connection - Security

Detects suspicious outbound network activity via kerberos default port indicating possible
lateral movement or first stage PrivEsc via delegation.

More details

Rule ID

windows_security_167

Query

{'selection': {'EventID': 5156, 'DestPort': '88', 'Directio
n': '%%14593'}, 'filter_exact': {'Application': ['System',
'\\device\\harddiskvolume*\\windows\\system32\\lsass.exe',
'\\device\\harddiskvolume*\\*\\nmap.exe', '\\device\\harddi
skvolume*\\*\\chrome.exe', '\\device\\harddiskvolume*\\*\\f
irefox.exe', '\\device\\harddiskvolume*\\*\\msedge.exe', '\
\device\\harddiskvolume*\\*\\iexplore.exe']}, 'condition':
'selection and not 1 of filter_*'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,eca91c7c-9214-47b9-b4c5-cb1d7e4f2350

Author: Ilyas Ochkov, oscd.community

Tactics, Techniques, and Procedures

TA0006 , T1558.003 

References

https://github.com/GhostPack/Rubeus 

Severity

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2019/10/24

high

Web Browsers

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

