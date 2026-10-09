Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Access
Attempt to Windows Object Alerts

The following rules are used to identify suspicious activity with access attempt to Windows
objects. Any one or more of these will trigger Suspicious Access Attempt to Windows Object
Alert. Details for each rule can be viewed by clicking the More Details link in the description.

Windows Events Required: 4657, 4663

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

SysKey Registry Keys Access

Detects handle requests and access operations to specific registry keys to calculate the
SysKey

More details

Rule ID

windows_security_2

Query

{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key'
, 'ObjectName|endswith': ['\\Lsa\\JD', '\\Lsa\\GBG', '\\Lsa
\\Skew1', '\\Lsa\\Data']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,9a4ff3b8-6187-4fd2-8e8b-e0eae1129495

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0007 , T1012 

References

https://threathunterplaybook.com/hunts/windows/190625-
RegKeyAccessSyskey/notebook.html 

Title

Description

Severity

75

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2019/08/12

high

Unknown

Sysmon Channel Reference
Deletion

Potential threat actor tampering with Sysmon manifest and eventually disabling it

More details

Rule ID

windows_security_19

Query

{'selection1': {'EventID': 4657, 'ObjectName|contains': ['W
INEVT\\Publishers\\{5770385f-c22a-43e0-bf4c-
06f5698ffbd9}', 'WINEVT\\Channels\\Microsoft-Windows-
Sysmon/Operational'], 'ObjectValueName': 'Enabled', 'NewVal
ue': '0'}, 'selection2': {'EventID': 4663, 'ObjectName|cont
ains': ['WINEVT\\Publishers\\{5770385f-c22a-43e0-bf4c-
06f5698ffbd9}', 'WINEVT\\Channels\\Microsoft-Windows-
Sysmon/Operational'], 'AccessMask': '0x10000'}, 'condition'
: '1 of selection*'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,18beca67-ab3e-4ee3-ba7a-a46ca8d7d0cc

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)

Tactics, Techniques, and Procedures

TA0005 , T1112 

References

https://twitter.com/Flangvik/status/1283054508084473861 

https://twitter.com/SecurityJosh/status/1283027365770276866 

https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html 

https://gist.github.com/Cyb3rWard0g/cf08c38c61f7e46e8404b38201ca01c8 

Severity

75

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2020/07/14

high

Unknown

Title

Description

Suspicious Teams Application
Related ObjectAcess Event

Detects an access to authentication tokens and accounts of Microsoft Teams desktop
application.

More details

Rule ID

windows_security_24

Query

{'selection': {'EventID': 4663, 'ObjectName|contains': ['\\
Microsoft\\Teams\\Cookies', '\\Microsoft\\Teams\\Local Stor
age\\leveldb']}, 'filter': {'ProcessName|contains': '\\Micr
osoft\\Teams\\current\\Teams.exe'}, 'condition': 'selection
 and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,25cde13e-8e20-4c29-b949-4e795b76f16f

Author: @SerkinValery

Tactics, Techniques, and Procedures

TA0006 , T1528 

References

https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-
tokens-as-cleartext-in-windows-linux-macs/ 

https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-
tokens 

Severity

75

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

experimental

2022/09/16

high

Unknown

Processes Accessing the
Microphone and Webcam

Potential adversaries accessing the microphone and webcam in an endpoint.

More details

Rule ID

windows_security_48

Query

{'selection': {'EventID': [4657, 4656, 4663], 'ObjectName|c
ontains': ['\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\
\CapabilityAccessManager\\ConsentStore\\microphone\\NonPack
aged', '\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Cap
abilityAccessManager\\ConsentStore\\webcam\\NonPackaged']},
 'condition': 'selection'}

Title

Description

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,8cd538a4-62d5-4e83-810b-12d41e428d6e

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)

Tactics, Techniques, and Procedures

TA0009 , T1123 

References

https://twitter.com/duzvik/status/1269671601852813320 

https://medium.com/@7a616368/can-you-track-processes-accessing-the-camera-
and-microphone-7e6885b37072 

Severity

50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Microsoft Entra Health Service
Agents Registry Keys Access

Maturity

Creation Date

Risk Level

False Positives

test

2020/06/07

medium

Unknown

This detection uses Windows security events to detect suspicious access attempts to the
registry key values and sub-keys of Microsoft Entra Health service agents (e.g AD FS).
Information from AD Health service agents can be used to potentially abuse some of the
features provided by those services in the cloud (e.g. Federation). This detection requires an
access control entry (ACE) on the system access control list (SACL) of the following
securable object: HKLM:\SOFTWARE\Microsoft\ADHealthAgent. Make sure you set the
SACL to propagate to its sub-keys.

More details

Rule ID

windows_security_54

Query

{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key'
, 'ObjectName': '\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\
ADHealthAgent'}, 'filter': {'ProcessName|contains': ['Micro
soft.Identity.Health.Adfs.DiagnosticsAgent.exe', 'Microsoft
.Identity.Health.Adfs.InsightsService.exe', 'Microsoft.Iden
tity.Health.Adfs.MonitoringAgent.Startup.exe', 'Microsoft.I
dentity.Health.Adfs.PshSurrogate.exe', 'Microsoft.Identity.
Health.Common.Clients.ResourceMonitor.exe']}, 'condition':
'selection and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,1d2ab8ac-1a01-423b-9c39-001510eae8e8

Title

Description

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC

Tactics, Techniques, and Procedures

TA0007 , T1012 

References

https://o365blog.com/post/hybridhealthagent/ 

https://github.com/OTRF/Set-
AuditRule/blob/c3dec5443414231714d850565d364ca73475ade5/rules/registry/a
ad_connect_health_service_agent.yml 

Severity

50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2021/08/26

medium

Unknown

Microsoft Entra Health
Monitoring Agent Registry Keys
Access

This detection uses Windows security events to detect suspicious access attempts to the
registry key of Microsoft Entra Health monitoring agent. This detection requires an access
control entry (ACE) on the system access control list (SACL) of the following securable
object HKLM\SOFTWARE\Microsoft\Microsoft Online\Reporting\MonitoringAgent.

More details

Rule ID

windows_security_70

Query

{'selection': {'EventID': [4656, 4663], 'ObjectType': 'Key'
, 'ObjectName': '\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\
Microsoft Online\\Reporting\\MonitoringAgent'}, 'filter': {
'ProcessName|contains': ['Microsoft.Identity.Health.Adfs.Di
agnosticsAgent.exe', 'Microsoft.Identity.Health.Adfs.Insigh
tsService.exe', 'Microsoft.Identity.Health.Adfs.MonitoringA
gent.Startup.exe', 'Microsoft.Identity.Health.Adfs.PshSurro
gate.exe', 'Microsoft.Identity.Health.Common.Clients.Resour
ceMonitor.exe']}, 'condition': 'selection and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,ff151c33-45fa-475d-af4f-c2f93571f4fe

Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC

Tactics, Techniques, and Procedures

TA0007 , T1012 

References

https://o365blog.com/post/hybridhealthagent/ 

https://github.com/OTRF/Set-
AuditRule/blob/c3dec5443414231714d850565d364ca73475ade5/rules/registry/a

Title

Description

ad_connect_health_monitoring_agent.yml 

Severity

50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2021/08/26

medium

Unknown

WCE wceaux.dll Access

Detects wceaux.dll access while WCE pass-the-hash remote command execution on source
host

More details

Rule ID

windows_security_93

Query

{'selection': {'EventID': [4656, 4658, 4660, 4663], 'Object
Name|endswith': '\\wceaux.dll'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,1de68c67-af5c-4097-9c85-fe5578e09e67

Author: Thomas Patzke

Tactics, Techniques, and Procedures

TA0006 , T1003 

References

https://www.jpcert.or.jp/english/pub/sr/ir_research.html 

https://jpcertcc.github.io/ToolAnalysisResultSheet 

Severity

90

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2017/06/14

critical

Unknown

Secure Deletion with SDelete

Detects renaming of file while deletion with SDelete tool.

More details

Rule ID

windows_security_101

Title

Description

Query

{'selection': {'EventID': [4656, 4663, 4658], 'ObjectName|e
ndswith': ['.AAA', '.ZZZ']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,39a80702-d7ca-4a83-b776-525b1f86a36d

Author: Thomas Patzke

Tactics, Techniques, and Procedures

TA0005 , T1070.004 , T1027.005 , T1553.002 , TA0040 , T1485 

References

https://jpcertcc.github.io/ToolAnalysisResultSheet/details/sdelete.htm 

https://www.jpcert.or.jp/english/pub/sr/ir_research.html 

https://docs.microsoft.com/en-gb/sysinternals/downloads/sdelete 

Severity

50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity Creation Date

Risk Level

False Positives

test

2017/06/14

medium

Legitimate usage of SDelete

Windows Defender Exclusion
Set

Detects scenarios where an windows defender exclusion was added in registry where an
entity would want to bypass antivirus scanning from windows defender

More details

Rule ID

windows_security_111

Query

{'selection': {'EventID': [4657, 4656, 4660, 4663], 'Object
Name|contains': '\\Microsoft\\Windows Defender\\Exclusions\
\'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Requirements: Audit Policy : Security Settings/Local Policies/Audit Policy,
Registry System Access Control (SACL): Auditing/User

Rule Source

SigmaHQ,e9c8808f-4cfb-4ba9-97d4-e5f3beaa244d

Author: @BarryShooshooga, Nasreddine Bencherchali (Nextron Systems)

Tactics, Techniques, and Procedures

Title

Description

TA0005 , T1562.001 

References

https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-
windows-defender-by-setting-path-exclusions/ 

Severity

75

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturity Creation Date Risk Level False Positives

test

2019/10/26

high

Intended inclusions by administrator

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

