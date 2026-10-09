Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious LSASS
Process Access Alert

The following rules are used to identify suspicious process access to or from the Local Security
Authority Subsystem Service (LSASS). Any one or more of these will trigger the Suspicious
LSASS Process Access Alert. Details for each rule can be viewed by clicking the More Details
link in the description.

Windows Events Required: 10, 4656, 4663

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

LSASS Memory Access by Tool
With Dump Keyword In Name

Detects LSASS process access requests from a source process with the "dump" keyword in
its image name.

More details

Rule ID

windows_process_access_1

Query

{'selection': {'TargetImage|endswith': '\\lsass.exe', 'Sour
ceImage|contains': 'dump'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

SigmaHQ,9bd012ee-0dff-44d7-84a0-aa698cfd87a3

Author: Florian Roth (Nextron Systems)

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References

https://twitter.com/_xpn_/status/1491557187168178176 

Title

Description

https://www.ired.team/offensive-security/credential-access-and-credential-
dumping/dump-credentials-from-lsass-process-without-mimikatz 

Severity

75

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Matur
ity

Creation
Date

Risk
Level

test

2022/02/1
0

high

False Positives

Rare programs that contain the word dump in their
name and access lsass

Credential Dumping Activity By
Python Based Tool

Detects LSASS process access for potential credential dumping by a Python-like tool such
as LaZagne or Pypykatz.

More details

Rule ID

windows_process_access_2

Query

{'selection': {'TargetImage|endswith': '\\lsass.exe', 'Call
Trace|contains': '_ctypes.pyd'}, 'filter_av': {'SourceImage
': ['?:\\Windows\\TEMP\\rapid7\\ir_agent.exe']}, 'condition
': 'selection and not filter_av'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

SigmaHQ,f8be3e82-46a3-4e4e-ada5-8e538ae8b9c9

Author: Bhabesh Raj, Jonhnathan Ribeiro

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References

https://twitter.com/bh4b3sh/status/1303674603819081728 

https://github.com/skelsec/pypykatz 

Severity

75

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

stable

2023/11/27

high

Unknown

Title

Description

LSASS Memory Access by
Process in Temp Folder

Identifies suspicious access to LSASS from a source process in Temp folder.

More details

Rule ID

windows_process_access_3

Query

{'selection': {'TargetImage|endswith': '\\lsass.exe', 'Sour
ceImage': ['*\\Local\\Temp\\*', '*\\LocalLow\\Temp\\*', '*\
\Roaming\\Temp\\*']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References
N/A

Severity

75

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

test

2024/01/26

high

Unknown

Suspicious LSASS Access via
MalSecLogon

Identifies suspicious access to LSASS handle from a call trace pointing to seclogon.dll and
with a suspicious access rights value. This may indicate an attempt to leak an LSASS handle
via abusing the Secondary Logon service in preparation for credential access.

More details

Rule ID

windows_process_access_4

Query

{'selection1': {'TargetImage|endswith': '\\lsass.exe'}, 'se
lection2': {'CallTrace|contains': 'seclogon.dll'}, 'selecti
on3': {'SourceImage|endswith': 'svchost.exe'}, 'selection4'
: {'GrantedAccess': '0x14c0'}, 'condition': 'selection1 and
 selection2 and selection3 and selection4'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

Title

Description

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References
N/A

Severity

75

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

production

2022/06/29

high

N/A

Potential Credential Access via
DuplicateHandle in LSASS

Identifies suspicious access to an LSASS handle via DuplicateHandle from an unknown call
trace module. This may indicate an attempt to bypass the NtOpenProcess API to evade
detection and dump LSASS memory for credential access.

More details

Rule ID

windows_process_access_5

Query

{'selection1': {'SourceImage|endswith': '\\lsass.exe'}, 'se
lection2': {'GrantedAccess': '0x40'}, 'selection3': {'CallT
race|contains': 'UNKNOWN'}, 'condition': 'selection1 and se
lection2 and selection3'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References
N/A

Severity

50

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

production

2021/09/27

medium

N/A

Title

Description

Potential Credential Access via
LSASS Memory Dump

Identifies suspicious access to LSASS handle from a call trace pointing to DBGHelp.dll or
DBGCore.dll, which both export the MiniDumpWriteDump method that can be used to dump
LSASS memory content in preparation for credential access.

More details

Rule ID

windows_process_access_6

Query

{'selection1': {'TargetImage|endswith': '\\lsass.exe'}, 'se
lection2': {'CallTrace|contains': ['dbghelp.dll', 'dbgcore.
dll']}, 'selection3': {'SourceImage': ['?:\\Windows\\System
32\\WerFault.exe', '?:\\Windows\\System32\\WerFaultSecure.e
xe', '?:\\Windows\\System32\\tasklist.exe']}, 'condition':
'selection1 and selection2 and (not selection3)'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Monitoring process access

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References
N/A

Severity

75

Suppression Logic Based On
computer_name
event_data.SourceImage
event_data.TargetImage
stellar.rule_id

Additional Information

Maturity

Creation Date

Risk Level

False Positives

production

2021/10/07

high

N/A

Password Dumper Activity on
LSASS

Detects process handle on LSASS process with certain access mask and object type
SAM_DOMAIN

More details

Rule ID

windows_security_146

Query

{'selection': {'EventID': 4656, 'ProcessName|endswith': '\\
lsass.exe', 'AccessMask': '0x705', 'ObjectType': 'SAM_DOMAI
N'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Title

Description

Potentially Suspicious
AccessMask Requested From
LSASS

Rule Source

SigmaHQ,aa1697b7-d611-4f9a-9cb2-5125b4ccfd5c

Author: sigma

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References

https://twitter.com/jackcr/status/807385668833968128 

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

2017/02/12

high

Unknown

Detects process handle on LSASS process with certain access mask

More details

Rule ID

windows_security_169

Query

{'selection_1': {'EventID': 4656, 'ObjectName|endswith': '\
\lsass.exe', 'AccessMask|contains': ['0x40', '0x1400', '0x1
00000', '0x1410', '0x1010', '0x1438', '0x143a', '0x1418', '
0x1f0fff', '0x1f1fff', '0x1f2fff', '0x1f3fff']}, 'selection
_2': {'EventID': 4663, 'ObjectName|endswith': '\\lsass.exe'
, 'AccessList|contains': ['4484', '4416']}, 'filter_main_sp
ecific': {'ProcessName|endswith': ['\\csrss.exe', '\\Gaming
Services.exe', '\\lsm.exe', '\\MicrosoftEdgeUpdate.exe', '\
\minionhost.exe', '\\MRT.exe', '\\MsMpEng.exe', '\\perfmon.
exe', '\\procexp.exe', '\\procexp64.exe', '\\svchost.exe',
'\\taskmgr.exe', '\\thor.exe', '\\thor64.exe', '\\vmtoolsd.
exe', '\\VsTskMgr.exe', '\\wininit.exe', '\\wmiprvse.exe',
'\\WmiPrvSE.exe', 'RtkAudUService64'], 'ProcessName|contain
s': [':\\Program Files (x86)\\', ':\\Program Files\\', ':\\
ProgramData\\Microsoft\\Windows Defender\\Platform\\', ':\\
Windows\\SysNative\\', ':\\Windows\\System32\\', ':\\Window
s\\SysWow64\\', ':\\Windows\\Temp\\asgard2-
agent\\']}, 'filter_main_generic': {'ProcessName|contains':
 ':\\Program Files'}, 'filter_main_exact': {'ProcessName|en
dswith': [':\\Windows\\System32\\taskhostw.exe', ':\\Window
s\\System32\\msiexec.exe', ':\\Windows\\CCM\\CcmExec.exe',
'\\Windows\\explorer.exe', '\\jre\\bin\\java.exe', ':\\Wind
ows\\LTSvc\\LTSVC.exe']}, 'filter_main_sysmon': {'ProcessNa
me|endswith': ':\\Windows\\Sysmon64.exe', 'AccessList|conta
ins': '%%4484'}, 'filter_main_aurora': {'ProcessName|contai
ns': ':\\Windows\\Temp\\asgard2-agent-
sc\\aurora\\', 'ProcessName|endswith': '\\aurora-agent-
64.exe', 'AccessList|contains': '%%4484'}, 'filter_main_sce
narioengine': {'ProcessName|endswith': '\\x64\\SCENARIOENGI

Title

Description

NE.EXE', 'AccessList|contains': '%%4484'}, 'filter_main_avi
ra1': {'ProcessName|contains|all': [':\\Users\\', '\\AppDat
a\\Local\\Temp\\is-
'], 'ProcessName|endswith': '\\avira_system_speedup.tmp', '
AccessList|contains': '%%4484'}, 'filter_main_avira2': {'Pr
ocessName|contains': ':\\Windows\\Temp\\', 'ProcessName|end
swith': '\\avira_speedup_setup_update.tmp', 'AccessList|con
tains': '%%4484'}, 'filter_main_snmp': {'ProcessName|endswi
th': ':\\Windows\\System32\\snmp.exe', 'AccessList|contains
': '%%4484'}, 'filter_main_googleupdate': {'ProcessName|con
tains': ':\\Windows\\SystemTemp\\', 'ProcessName|endswith':
 '\\GoogleUpdate.exe', 'AccessList|contains': '%%4484'}, 'f
ilter_optional_procmon': {'ProcessName|endswith': ['\\procm
on64.exe', '\\procmon.exe'], 'AccessList|contains': '%%4484
'}, 'condition': '1 of selection_* and not 1 of filter_main
_* and not 1 of filter_optional_*'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,4a1b6da0-d94f-4fc3-98fc-2d9cb9e5ee76

Author: Roberto Rodriguez, Teymur Kheirkhabarov, Dimitrios Slamaris, Mark
Russinovich, Aleksey Potapov, oscd.community (update)

Tactics, Techniques, and Procedures

TA0006 , T1003.001 

References

https://web.archive.org/web/20230208123920/https://cyberwardog.blogspot.com/
2017/03/chronicles-of-threat-hunter-hunting-for_22.html 

https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-
windows-environment 

Severity

50

Suppression Logic Based On
computer_name
event_data.ObjectName
stellar.rule_id

Additional Information

Maturit
y

Creatio
n Date

Risk
Level

experim
ental

2019/11/
01

mediu
m

False Positives

Legitimate software accessing LSASS process for
legitimate reason; update the whitelist with it

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

