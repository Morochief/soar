Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Windows
Logon Event Alerts

The following rules are used to identify suspicious Windows logon activities. Any one or more of
these will trigger Suspicious Windows Logon Alert. Details for each rule can be viewed by
clicking the More Details link in the description.

Windows Events Required: 4624

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Hacktool Ruler

This events that are generated when using the hacktool Ruler by Sensepost

More details

Rule ID

windows_security_113

Query

{'selection1': {'EventID': 4776, 'Workstation': 'RULER'}, 'selec
tion2': {'EventID': [4624, 4625], 'WorkstationName': 'RULER'}, '
condition': '(1 of selection*)'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,24549159-ac1b-479c-8175-d42aea947cae

Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures

TA0002 , T1059 , TA0005 , T1550.002 , TA0007 , T1087 , TA0009 , T1114 

References

https://github.com/sensepost/ruler 

https://github.com/sensepost/ruler/issues/47 

Title

Description

https://github.com/staaldraad/go-
ntlm/blob/cd032d41aa8ce5751c07cb7945400c0f5c81e2eb/ntlm/ntlmv1.go#L427 

https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4776 

https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-
4624 

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

2017/05/31

high

False Positives

Go utilities that use staaldraad awesome NTLM
library

Remote WMI
ActiveScriptEventConsu
mers

Detect potential adversaries leveraging WMI ActiveScriptEventConsumers remotely to move
laterally in a network

More details

Rule ID

windows_security_134

Query

{'selection': {'EventID': 4624, 'LogonType': '3', 'ProcessName|e
ndswith': 'scrcons.exe'}, 'filter': {'TargetLogonId': '0x3e7'},
'condition': 'selection and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,9599c180-e3a8-4743-8f92-7fb96d3be648

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)

Tactics, Techniques, and Procedures

TA0003 , T1546.003 

References

https://threathunterplaybook.com/hunts/windows/200902-
RemoteWMIActiveScriptEventConsumers/notebook.html 

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

2020/09/02

high

SCCM

Title

Description

RottenPotato Like Attack
Pattern

Detects logon events that have characteristics of events generated during an attack with
RottenPotato and the like

More details

Rule ID

windows_security_136

Query

{'selection': {'EventID': 4624, 'LogonType': '3', 'TargetUserNam
e|re': '(?:ANONYMOUS(_| )LOGON)$', 'WorkstationName': ['-
', ''], 'IpAddress': ['127.0.0.1', '::1']}, 'condition': 'select
ion'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,16f5d8ca-44bd-47c8-acbe-6fc95a16c12f

Author: @SBousseaden, Florian Roth

Tactics, Techniques, and Procedures

TA0004 , T1068 

References

https://twitter.com/SBousseaden/status/1195284233729777665 

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

2019/11/15

high

Unknown

Successful Overpass
the Hash Attempt

Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash
behavior of e.g Mimikatz's sekurlsa::pth module.

More details

Rule ID

windows_security_138

Query

{'selection': {'EventID': 4624, 'LogonType': '9', 'LogonProcessN
ame': 'seclogo', 'AuthenticationPackageName': 'Negotiate'}, 'con
dition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

Title

Description

SigmaHQ,192a0330-c20b-4356-90b6-7b7049ae0b87

Author: Roberto Rodriguez (source), Dominik Schaudel (rule)

Tactics, Techniques, and Procedures

TA0005 , T1550.002 

References
N/A

Severity

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturi
ty

Creation
Date

Risk
Level

test

2018/02/12 high

False Positives

Runas command-line tool using /netonly parameter

Legitimate use of Active Directory management tools (e.g.,
ADManager Plus)

Group Policy Client service (gpsvc) applying user-specific
settings

DiagTrackEoP Default
Login Username

Detects the default "UserName" used by the DiagTrackEoP POC

More details

Rule ID

windows_security_140

Query

{'selection': {'EventID': 4624, 'LogonType': '9', 'TargetOutboun
dUserName': 'thisisnotvaliduser'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,2111118f-7e46-4fc8-974a-59fd8ec95196

Author: Nasreddine Bencherchali (Nextron Systems)

Tactics, Techniques, and Procedures

TA0005 , T1078 

References

https://github.com/Wh04m1001/DiagTrackEoP/blob/3a2fc99c9700623eb7dc7d4b5f314fd
9ce5ef51f/main.cpp#L46 

Severity

90

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Title

Description

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/08/03

critical

Unlikely

Access Token Abuse

This rule tries to detect token impersonation and theft. (Example: DuplicateToken(Ex) and
ImpersonateLoggedOnUser with the LOGON32_LOGON_NEW_CREDENTIALS flag.)

More details

Rule ID

windows_security_142

Query

{'selection': {'EventID': 4624, 'LogonType': '9', 'LogonProcessN
ame': 'Advapi', 'AuthenticationPackageName': 'Negotiate', 'Imper
sonationLevel': '%%1833'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,02f7c9c1-1ae8-4c6a-8add-04693807f92f

Author: Michaela Adams, Zach Mathis

Tactics, Techniques, and Procedures

TA0005 , T1134.001 

References

https://www.elastic.co/fr/blog/how-attackers-abuse-access-token-manipulation 

https://www.manageengine.com/log-management/cyber-security/access-token-
manipulation.html 

Severity

50

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/11/06

medium

Anti-Virus

KrbRelayUp Attack
Pattern

Detects logon events that have characteristics of events generated during an attack with
KrbRelayUp and the like

More details

Rule ID

windows_security_143

Query

{'selection1': {'EventID': 4624, 'LogonType': '3', 'Authenticati
onPackageName': 'Kerberos', 'TargetUserSid|startswith': 'S-1-5-
21-
', 'TargetUserSid|endswith': '-500'}, 'selection2': {'IpAddress'

Title

Description

: ['::1', '127.0.0.1']}, 'condition': 'selection1 and selection2
'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,749c9f5e-b353-4b90-a9c1-05243357ca4b

Author: Elastic, @SBousseaden

Tactics, Techniques, and Procedures

TA0008 , T1550 

References

https://github.com/elastic/detection-
rules/blob/fb6ee2c69864ffdfe347bf3b050cb931f53067a6/rules/windows/privilege_escalat
ion_krbrelayup_suspicious_logon.toml 

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

experimental

2022/04/27

high

Unknown

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

