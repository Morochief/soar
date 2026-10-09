Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Sensitive Windows
Network Share File or Folder Accessed Alerts

The following rules are used to identify suspicious activity with Windows network share file or
folder access. Any one or more of these will trigger Sensitive Windows Network Share File or
Folder Accessed Alert. Details for each rule can be viewed by clicking the More Details link in
the description.

Windows Events Required: 5145

The Windows Detect Profile (Low Volume)  covers these required Windows events.

Title

Description

Impacket PsExec Execution

Detects execution of Impacket's psexec.py.

More details

Rule ID

windows_security_150

Query

{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$'
, 'RelativeTargetName|contains': ['RemCom_stdin', 'RemCom_s
tdout', 'RemCom_stderr']}, 'condition': 'selection1'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

SigmaHQ,32d56ea1-417f-44ff-822b-882873f5f43b

Author: Bhabesh Raj

Tactics, Techniques, and Procedures

Title

Description

TA0008 , T1021.002 

References
N/A

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

2020/12/14

high

Unknown

Remote Task Creation via
ATSVC Named Pipe

Detects remote task creation via at.exe or API interacting with ATSVC namedpipe

More details

Rule ID

windows_security_151

Query

{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$',
 'RelativeTargetName': 'atsvc', 'Accesses|contains': ['Writ
eData', '%%4417']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

SigmaHQ,f6de6525-4509-495a-8a82-1f8b0ed73a00

Author: Samir Bousseaden

Tactics, Techniques, and Procedures

TA0003 , T1053.002 

References
N/A

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

test

2019/04/03

medium

Unknown

Protected Storage Service
Access

Detects access to a protected_storage service over the network. Potential abuse of DPAPI
to extract domain backup keys from Domain Controllers

Title

Description

More details

Rule ID

windows_security_152

Query

{'selection': {'EventID': 5145, 'ShareName|contains': 'IPC'
, 'RelativeTargetName': 'protected_storage'}, 'condition':
'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,45545954-4016-43c6-855e-eae8f1c369dc

Author: Roberto Rodriguez @Cyb3rWard0g

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References

https://threathunterplaybook.com/hunts/windows/190620-
DomainDPAPIBackupKeyExtraction/notebook.html 

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

2019/08/10

high

Unknown

Persistence and Execution at
Scale via GPO Scheduled Task

Detect lateral movement using GPO scheduled task, usually used to deploy ransomware at
scale

More details

Rule ID

windows_security_153

Query

{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\SYSVOL
', 'RelativeTargetName|endswith': 'ScheduledTasks.xml', 'Ac
cesses|contains': ['WriteData', '%%4417']}, 'condition': 's
election'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

Title

Description

SigmaHQ,a8f29a7b-b137-4446-80a0-b804272f3da2

Author: Samir Bousseaden

Tactics, Techniques, and Procedures

TA0003 , T1053.005 

References

https://twitter.com/menasec1/status/1106899890377052160 

https://www.secureworks.com/blog/ransomware-as-a-distraction 

Severity

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Mat
urity

Creati
on
Date

Risk
Level

test 2019/0

high

4/03

False Positives

If the source IP is not localhost then it's super suspicious,
better to monitor both local and remote changes to GPO
scheduledtasks

First Time Seen Remote Named
Pipe

This detection excludes known named pipes accessible remotely and notify on newly
observed ones, may help to detect lateral movement and remote exec using named pipes

More details

Rule ID

windows_security_154

Query

{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$'
}, 'false_positives': {'RelativeTargetName': ['atsvc', 'sam
r', 'lsarpc', 'lsass', 'winreg', 'netlogon', 'srvsvc', 'pro
tected_storage', 'wkssvc', 'browser', 'netdfs', 'svcctl', '
spoolss', 'ntsvcs', 'LSM_API_service', 'HydraLsPipe', 'Term
Srv_API_service', 'MsFteWds', 'sql\\query', 'eventlog']}, '
condition': 'selection1 and not false_positives'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

SigmaHQ,52d8b0c6-53d6-439a-9e41-52ad442ad9ad

Author: Samir Bousseaden

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References

https://twitter.com/menasec1/status/1104489274387451904 

Title

Description

Severity

75

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Matur
ity

Creation
Date

Risk
Level

test

2019/04/0
3

high

False Positives

Update the excluded named pipe to filter out any
newly observed legit named pipe

DCERPC SMB Spoolss Named
Pipe

Detects the use of the spoolss named pipe over SMB. This can be used to trigger the
authentication via NTLM of any machine that has the spoolservice enabled.

More details

Rule ID

windows_security_155

Query

{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$',
 'RelativeTargetName': 'spoolss'}, 'condition': 'selection'
}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,214e8f95-100a-4e04-bb31-ef6cba8ce07e

Author: OTR (Open Threat Research)

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References

https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-
forests-trusts-71f2b33688e1 

https://dirkjanm.io/a-different-way-of-abusing-zerologon/ 

https://twitter.com/_dirkjan/status/1309214379003588608 

Severity

50

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

2018/11/28 medium

False Positives

Domain Controllers acting as printer servers
too? :)

Title

Description

T1047 Wmiprvse Wbemcomn
DLL Hijack

Detects a threat actor creating a file named `wbemcomn.dll` in the
`C:\Windows\System32\wbem\` directory over the network for a WMI DLL Hijack scenario.

More details

Rule ID

windows_security_157

Query

{'selection': {'EventID': 5145, 'RelativeTargetName|endswit
h': '\\wbem\\wbemcomn.dll'}, 'filter': {'SubjectUserName|en
dswith': '$'}, 'condition': 'selection and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,f6c68d5f-e101-4b86-8c84-7d96851fd65c

Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)

Tactics, Techniques, and Procedures

TA0002 , T1047 , TA0008 , T1021.002 

References

https://threathunterplaybook.com/hunts/windows/201009-
RemoteWMIWbemcomnDLLHijack/notebook.html 

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

2020/10/12

high

Unknown

CVE-2021-1675 Print Spooler
Exploitation IPC Access

Detects remote printer driver load from Detailed File Share in Security logs that are a sign of
successful exploitation attempts against print spooler vulnerability CVE-2021-1675 and
CVE-2021-34527

More details

Rule ID

windows_security_159

Query

{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$',
 'RelativeTargetName': 'spoolss', 'AccessMask': '0x3', 'Obj
ectType': 'File'}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Title

Description

Rule Source

SigmaHQ,8fe1c584-ee61-444b-be21-e9054b229694

Author: INIT_6

Tactics, Techniques, and Procedures

TA0002 , T1569 

References

https://twitter.com/INIT_3/status/1410662463641731075 

Severity

90

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

2021/07/02

critical

Unknown

Possible PetitPotam Coerce
Authentication Attempt

Detect PetitPotam coerced authentication activity.

More details

Rule ID

windows_security_161

Query

{'selection': {'EventID': 5145, 'ShareName|startswith': '\\
\\', 'ShareName|endswith': '\\IPC$', 'RelativeTargetName':
'lsarpc', 'SubjectUserName': 'ANONYMOUS LOGON'}, 'condition
': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Detailed File Share" must be
configured for Success/Failure

Rule Source

SigmaHQ,1ce8c8a3-2723-48ed-8246-906ac91061a6

Author: Mauricio Velazco, Michael Haag

Tactics, Techniques, and Procedures

TA0006 , T1187 

References

https://github.com/topotam/PetitPotam 

https://github.com/splunk/security_content/blob/0dd6de32de2118b2818550df9e6
5255f4109a56d/detections/endpoint/petitpotam_network_share_access_request.
yml 

Severity

75

Suppression Logic Based On

Title

Description

event_id
computer_name
stellar.rule_id

Additional Information

Maturity

Creation Date Risk Level False Positives

experimental 2021/09/02

high

Unknown. Feedback welcomed.

Possible Impacket SecretDump
Remote Activity

Detect AD credential dumping using impacket secretdump HKTL

More details

Rule ID

windows_security_162

Query

{'selection': {'EventID': 5145, 'ShareName': '\\\\*\\ADMIN$
', 'RelativeTargetName|contains|all': ['SYSTEM32\\', '.tmp'
]}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

SigmaHQ,252902e3-5830-4cf6-bf21-c22083dfd5cf

Author: Samir Bousseaden, wagga

Tactics, Techniques, and Procedures

TA0006 , T1003 

References
N/A

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

2019/04/03

high

Unknown

Suspicious PsExec Execution

detects execution of psexec or paexec with renamed service name, this rule helps to filter
out the noise if psexec is used for legit purposes or if attacker uses a different psexec client
other than sysinternal one

More details

Rule ID

windows_security_164

Query

Title

Description

{'selection1': {'EventID': 5145, 'ShareName': '\\\\*\\IPC$'
, 'RelativeTargetName|endswith': ['-stdin', '-stdout', '-
stderr']}, 'filter': {'RelativeTargetName|startswith': 'PSE
XESVC'}, 'condition': 'selection1 and not filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

The advanced audit policy setting "Object Access > Audit Detailed File Share"
must be configured for Success/Failure

Rule Source

SigmaHQ,c462f537-a1e3-41a6-b5fc-b2c2cef9bf82

Author: Samir Bousseaden

Tactics, Techniques, and Procedures

TA0008 , T1021.002 

References
N/A

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

2019/04/03

high

Unknown

DCOM
InternetExplorer.Application
Iertutil DLL Hijack - Security

Detects a threat actor creating a file named `iertutil.dll` in the `C:\Program Files\Internet
Explorer\` directory over the network for a DCOM InternetExplorer DLL Hijack scenario.

More details

Rule ID

windows_security_165

Query

{'selection': {'EventID': 5145, 'RelativeTargetName|endswit
h': '\\Internet Explorer\\iertutil.dll'}, 'filter': {'Subje
ctUserName|endswith': '$'}, 'condition': 'selection and not
 filter'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

SigmaHQ,c39f0c81-7348-4965-ab27-2fde35a1b641

Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)

Tactics, Techniques, and Procedures

TA0008 , T1021 

Title

Description

References

https://threathunterplaybook.com/hunts/windows/201009-
RemoteDCOMIErtUtilDLLHijack/notebook.html 

Transferring Files with
Credential Data via Network
Shares

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

2020/10/12

high

Unknown

Transferring files with well-known filenames (sensitive files with credential data) using
network shares

More details

Rule ID

windows_security_170

Query

{'selection': {'EventID': 5145, 'RelativeTargetName|contain
s': ['\\mimidrv.sys', '\\windows\\minidump\\', '\\hiberfil.
sys', '\\ntds.dit']}, 'condition': 'selection'}

Log Source

Stellar Cyber Windows Server Sensor configured for:

Collecting Windows security events

Rule Source

Developed internally by Stellar Cyber

Tactics, Techniques, and Procedures

TA0006 , T1003 

References

https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-
windows-environment 

Severity

50

Suppression Logic Based On

event_id
computer_name
stellar.rule_id

Additional Information

Matur
ity

Creation
Date

Risk
Level

test

2019-10-
22

mediu
m

False Positives

Transferring sensitive files for legitimate administration
work by legitimate administrator

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

